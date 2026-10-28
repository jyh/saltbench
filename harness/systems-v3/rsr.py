#!/usr/bin/env python3
"""rsr.py -- the review-surface ratio (O94, STATUS-bench item 18).

For one cell's final Rust/Verus source, count lines by class and report

    ratio = SPEC / (IMPL + PROOF)

DECLARED AS A PROXY for review attention, never a measure of it: it counts lines, and a line of
specification is not a unit of a reviewer's time.

Classes, one per physical line:
  SPEC     a spec fn (any visibility or open/closed/uninterp form) with its attributes; an exec fn's
           requires / ensures / recommends / returns clause lines; a ghost or tracked struct field
  PROOF    a proof fn (or broadcast proof fn / broadcast group) in whole, its own requires/ensures
           included -- a lemma's statement is proof scaffolding, not the component's spec; a proof { }
           block; a Verus assert / assume / reveal (never Rust's assert! macro, which is IMPL) / hide / broadcast use statement through its end (a
           `by { }` body included); a let ghost / let tracked statement; a loop's invariant / ensures /
           decreases clauses; an exec fn's decreases / opens_invariants / no_unwind clauses
  IMPL     every other line holding code, including structure (verus! { }, impl, struct, the braces
           that open an exec body or a loop body)
  TEST     a code line in tests/**.rs, or inside a #[cfg(test)] mod in a source file
  COMMENT  a line holding only comment text
  BLANK    a line holding only whitespace

LIMITS (they ride with every number this tool prints):
  - A line is classed by how it STARTS: a clause written on its fn's header line is IMPL, an assert
    written after other code on a line is IMPL.
  - A plain (non-Verus) arm has SPEC 0 by construction: its tests are counted as TEST and are not
    folded into SPEC, so the plain arms' ratio is 0 and says nothing about how they are reviewed.
  - The classifier is lexical, not a parser. It is validated by --selftest against two hand-labelled
    fixtures (one real cell, one synthetic for the constructs that cell lacks), and nothing else.
  - SUBJECT-written lines are the final lines not matched to the seed (root commit) by difflib; a line
    the subject rewrote to the seed's exact text counts as seed.

Usage:
  rsr.py --selftest
  rsr.py --classify FILE            per-line labels
  rsr.py --cell REPO_DIR [--id ID]  one TSV row (header with --header)
"""
import difflib
import os
import re
import subprocess
import sys

CLASSES = ['SPEC', 'PROOF', 'IMPL', 'TEST', 'COMMENT', 'BLANK']
CODE_CLASSES = ['SPEC', 'PROOF', 'IMPL', 'TEST']

_VIS = r'(?:pub(?:\([^)]*\))?\s+)?'
RE_SPEC_FN = re.compile(r'^\s*' + _VIS + r'(?:(?:open|closed|uninterp)\s+)*spec\s+fn\b')
RE_PROOF_FN = re.compile(r'^\s*' + _VIS + r'(?:broadcast\s+)?(?:proof\s+fn\b|group\b)')
RE_EXEC_FN = re.compile(r'^\s*' + _VIS + r'(?:(?:const|unsafe|async|exec|extern\s+"[^"]*")\s+)*fn\b')
RE_MOD = re.compile(r'^\s*' + _VIS + r'mod\b')
RE_ATTR = re.compile(r'^\s*#!?\[.*\]\s*$')
RE_CFG_TEST = re.compile(r'^\s*#\[cfg\(test\)\]\s*$')
RE_GHOST_FIELD = re.compile(r'^\s*' + _VIS + r'(?:ghost|tracked)\s+\w+\s*:')
RE_PROOF_STMT = re.compile(r'^\s*(?:assert\b(?!\s*!)|assert_by|assume\b(?!\s*!)|reveal\b|reveal_with_fuel\b|hide\b|'
                           r'broadcast\s+use\b|let\s+(?:ghost|tracked)\b)')
RE_PROOF_BLOCK = re.compile(r'^\s*proof\s*\{')
RE_SIG_SPEC_CLAUSE = re.compile(r'^\s*(?:requires|ensures|recommends|returns)\b')
RE_SIG_PROOF_CLAUSE = re.compile(r'^\s*(?:decreases|opens_invariants|no_unwind)\b')
RE_LOOP_CLAUSE = re.compile(r'^\s*(?:invariant_except_break|invariant|ensures|decreases|requires)\b')


def strip_code(lines):
    """Per line: (code text with comments removed and string/char contents blanked, had_comment)."""
    out = []
    in_block = 0          # nesting depth of /* */
    in_str = False        # inside a "..." string
    raw_hashes = None     # inside r#"..."#: the number of hashes
    for line in lines:
        code = []
        had_comment = False
        i, n = 0, len(line)
        while i < n:
            c = line[i]
            if in_block:
                had_comment = True
                if line.startswith('*/', i):
                    in_block -= 1
                    i += 2
                elif line.startswith('/*', i):
                    in_block += 1
                    i += 2
                else:
                    i += 1
                continue
            if raw_hashes is not None:
                end = '"' + '#' * raw_hashes
                if line.startswith(end, i):
                    code.append(end)
                    i += len(end)
                    raw_hashes = None
                else:
                    code.append(' ')
                    i += 1
                continue
            if in_str:
                if c == '\\':
                    code.append('  ')
                    i += 2
                elif c == '"':
                    code.append('"')
                    in_str = False
                    i += 1
                else:
                    code.append(' ')
                    i += 1
                continue
            if line.startswith('//', i):
                had_comment = True
                break
            if line.startswith('/*', i):
                in_block = 1
                had_comment = True
                i += 2
                continue
            m = re.match(r'r(#*)"', line[i:])
            if m and (i == 0 or not (line[i - 1].isalnum() or line[i - 1] == '_')):
                raw_hashes = len(m.group(1))
                code.append(m.group(0))
                i += len(m.group(0))
                continue
            if c == '"':
                in_str = True
                code.append('"')
                i += 1
                continue
            if c == "'":
                m = re.match(r"'(?:\\.[^']*|[^\\'])'", line[i:])
                if m:
                    code.append("'" + ' ' * (len(m.group(0)) - 2) + "'")
                    i += len(m.group(0))
                    continue
            code.append(c)
            i += 1
        out.append((''.join(code), had_comment))
    return out


def classify(text, all_test=False):
    """One label per physical line of text."""
    lines = text.split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]
    stripped = strip_code(lines)
    labels = [None] * len(lines)

    stack = []            # frame classes: 'SPEC' 'PROOF' 'TEST' for whole regions, 'IMPL' otherwise
    paren = 0             # ( and [ depth
    pending = None        # class of an item whose header is seen and whose body brace is not yet open
    sig = None            # exec fn signature mode: None, or the current clause class ('IMPL' before a clause)
    loopc = False         # in a loop's clause list
    stmt = None           # proof statement: the brace depth it started at
    pending_test = False  # #[cfg(test)] seen
    deferred = []         # attribute lines waiting for the next code line's class

    def region():
        for f in reversed(stack):
            if f != 'IMPL':
                return f
        return 'IMPL'

    for idx, (code, had_comment) in enumerate(stripped):
        s = code.strip()
        if not s:
            labels[idx] = 'COMMENT' if had_comment else 'BLANK'
            continue
        if all_test:
            labels[idx] = 'TEST'
            continue

        ctx = region()
        opener_class = None   # class of the frame the body brace on this line opens
        if ctx != 'IMPL':
            cls = ctx
        elif pending is not None:
            cls = pending
        elif stmt is not None:
            cls = 'PROOF'
        elif sig is not None and (RE_SIG_SPEC_CLAUSE.match(code) or RE_SIG_PROOF_CLAUSE.match(code)):
            sig = 'SPEC' if RE_SIG_SPEC_CLAUSE.match(code) else 'PROOF'
            cls = sig
        elif sig is not None:
            cls = sig if (sig != 'IMPL' and s != '{') else 'IMPL'
        elif loopc:
            cls = 'IMPL' if s == '{' else 'PROOF'
        elif RE_CFG_TEST.match(code):
            pending_test = True
            deferred.append(idx)
            continue
        elif RE_ATTR.match(code):
            deferred.append(idx)
            continue
        elif RE_SPEC_FN.match(code):
            cls = pending = 'SPEC'
        elif RE_PROOF_FN.match(code):
            cls = pending = 'PROOF'
        elif pending_test and RE_MOD.match(code):
            cls = pending = 'TEST'
        elif RE_EXEC_FN.match(code):
            cls = 'IMPL'
            sig = 'IMPL'
        elif RE_GHOST_FIELD.match(code):
            cls = 'SPEC'
        elif RE_PROOF_BLOCK.match(code):
            cls = 'PROOF'
            opener_class = 'PROOF'
        elif RE_PROOF_STMT.match(code):
            cls = 'PROOF'
            stmt = len(stack)
        elif RE_LOOP_CLAUSE.match(code):
            cls = 'PROOF'
            loopc = True
        else:
            cls = 'IMPL'
        pending_test = pending_test and cls != 'TEST' and pending is None and RE_ATTR.match(code) is not None
        for d in deferred:
            labels[d] = cls
        deferred = []
        labels[idx] = cls

        # braces and parens
        for ch in code:
            if ch in '([':
                paren += 1
            elif ch in ')]':
                paren = max(0, paren - 1)
            elif ch == '{':
                if opener_class is not None:
                    stack.append(opener_class)
                    opener_class = None
                elif pending is not None and paren == 0:
                    stack.append(pending)
                    pending = None
                elif (sig is not None or loopc) and paren == 0:
                    stack.append('IMPL')
                    sig = None
                    loopc = False
                elif stmt is not None:
                    stack.append('PROOF')
                else:
                    stack.append(region())
            elif ch == '}':
                if stack:
                    stack.pop()
        if pending is not None and paren == 0 and s.endswith(';'):
            pending = None          # a bodiless item
        if stmt is not None and len(stack) <= stmt and paren == 0 and (s.endswith(';') or s.endswith('}')):
            stmt = None
        if sig is not None and paren == 0 and s.endswith(';'):
            sig = None              # a trait method declaration
    for d in deferred:
        labels[d] = 'IMPL'
    return labels


def tally(labels):
    t = dict((c, 0) for c in CLASSES)
    for lab in labels:
        t[lab] += 1
    return t


def read_labels(path, n):
    want = [None] * n
    for line in open(path, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        rng, cls = line.split()
        a, _, b = rng.partition('-')
        a = int(a)
        b = int(b) if b else a
        for k in range(a, b + 1):
            want[k - 1] = cls
    return want


def selftest():
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rsr-fixtures')
    bad = 0
    names = sorted(f[:-3] for f in os.listdir(here) if f.endswith('.rs'))
    if not names:
        print('SELFTEST VOID: no fixtures in', here)
        return 2
    for name in names:
        text = open(os.path.join(here, name + '.rs'), encoding='utf-8').read()
        got = classify(text)
        want = read_labels(os.path.join(here, name + '.labels'), len(got))
        if None in want:
            print('SELFTEST %s: labels do not cover line %d' % (name, want.index(None) + 1))
            bad += 1
            continue
        miss = [(k + 1, want[k], got[k]) for k in range(len(got)) if want[k] != got[k]]
        tg, tw = tally(got), tally(want)
        print('SELFTEST %-16s lines %3d  hand %s' % (name, len(got), ' '.join('%s %d' % (c, tw[c]) for c in CLASSES)))
        print('SELFTEST %-16s            tool %s  -> %s' % ('', ' '.join('%s %d' % (c, tg[c]) for c in CLASSES),
                                                         'PASS' if not miss else 'FAIL %d line(s)' % len(miss)))
        for k, w, g in miss:
            print('    line %d: hand %s, tool %s' % (k, w, g))
        bad += bool(miss)
    return 1 if bad else 0


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True)
    return r.returncode, r.stdout


def source_files(repo):
    """The cell's Rust files on disk: (path, is_test). bin/ docs/ .seat/ target/ and interface.rs are the harness's."""
    out = []
    for root, dirs, files in os.walk(repo):
        rel = os.path.relpath(root, repo)
        parts = [] if rel == '.' else rel.split(os.sep)
        if parts and parts[0] in ('.git', 'target', '.seat', 'bin', 'docs', '.lake', 'tmp', 'inbox', 'memory'):
            dirs[:] = []
            continue
        for f in files:
            if not f.endswith('.rs'):
                continue
            p = os.path.normpath(os.path.join(rel, f))
            if p == 'interface.rs':
                continue
            out.append((p, bool(parts) and parts[0] == 'tests'))
    return sorted(out)


def measure_cell(repo):
    rc, root = git(repo, 'rev-list', '--max-parents=0', 'HEAD')
    seed_sha = root.split()[-1] if rc == 0 and root.split() else None
    all_t = dict((c, 0) for c in CLASSES)
    sub_t = dict((c, 0) for c in CLASSES)
    files = source_files(repo)
    dirty = 0
    for p, is_test in files:
        text = open(os.path.join(repo, p), encoding='utf-8', errors='replace').read()
        labels = classify(text, all_test=is_test)
        final = text.split('\n')
        if final and final[-1] == '':
            final = final[:-1]
        seed = []
        if seed_sha:
            rc, s = git(repo, 'show', '%s:%s' % (seed_sha, p))
            if rc == 0:
                seed = s.split('\n')
                if seed and seed[-1] == '':
                    seed = seed[:-1]
            rc, h = git(repo, 'show', 'HEAD:%s' % p)
            if rc != 0 or h != text:
                dirty += 1
        in_seed = [False] * len(final)
        for blk in difflib.SequenceMatcher(None, seed, final, autojunk=False).get_matching_blocks():
            for k in range(blk.b, blk.b + blk.size):
                in_seed[k] = True
        for k, lab in enumerate(labels):
            all_t[lab] += 1
            if not in_seed[k]:
                sub_t[lab] += 1
    return files, dirty, all_t, sub_t, seed_sha


def ratio(t):
    d = t['IMPL'] + t['PROOF']
    return ('%.4f' % (t['SPEC'] / d)) if d else 'UNDEFINED'


HEADER = ('cell\tfiles\tdirty_vs_head\t' + '\t'.join('all_' + c for c in CLASSES) + '\t' +
          '\t'.join('sub_' + c for c in CLASSES) + '\tratio_all\tratio_sub')


def quartiles(xs):
    xs = sorted(xs)
    if not xs:
        return None

    def q(p):
        k = (len(xs) - 1) * p
        lo, hi = int(k), min(int(k) + 1, len(xs) - 1)
        return xs[lo] + (xs[hi] - xs[lo]) * (k - lo)
    return xs[0], q(0.25), q(0.5), q(0.75), xs[-1]


def report(path):
    """The distribution per arm and problem from a --cell table (with its six condition columns)."""
    import csv
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    bad = [r for r in rows if r.get('files') in ('NO-REPO', 'NO-SOURCE')]
    print('# rsr.py --report %s: %d rows (cell x condition), %d distinct cells, %d without source'
          % (path, len(rows), len({r['cell'] for r in rows}), len(bad)))
    print('# ratio = SPEC / (IMPL + PROOF), a PROXY for review attention, not a measure of it. A plain arm reads 0 by')
    print('# construction (no Verus): its review surface is its tests, so TEST/IMPL is printed beside it.')
    print('# all = the final source on disk; sub = lines not matched to the seed (root commit). Five-number summaries.')
    print('arm\tproblem\tn\tratio_all min/q1/med/q3/max\tratio_sub min/q1/med/q3/max\tSPEC med\tPROOF med\tIMPL med\tTEST/IMPL med\tPROOF=0')
    groups = {}
    for r in rows:
        if r in bad:
            continue
        groups.setdefault((r['arm'], r['problem']), []).append(r)

    def fmt(t):
        return 'UNDEFINED' if t is None else '/'.join('%.3f' % v for v in t)
    for (arm, prob) in sorted(groups):
        g = groups[(arm, prob)]
        ra = [float(r['ratio_all']) for r in g if r['ratio_all'] != 'UNDEFINED']
        rs = [float(r['ratio_sub']) for r in g if r['ratio_sub'] != 'UNDEFINED']
        med = lambda k: quartiles([int(r[k]) for r in g])[2]
        ti = [int(r['all_TEST']) / int(r['all_IMPL']) for r in g if int(r['all_IMPL'])]
        print('%s\t%s\t%d\t%s\t%s\t%g\t%g\t%g\t%s\t%d' % (
            arm, prob, len(g), fmt(quartiles(ra)), fmt(quartiles(rs)), med('all_SPEC'), med('all_PROOF'),
            med('all_IMPL'), '%.3f' % quartiles(ti)[2] if ti else 'UNDEFINED',
            sum(1 for r in g if int(r['all_PROOF']) == 0)))
    return 0


def main(argv):
    if '--selftest' in argv:
        return selftest()
    if '--report' in argv:
        return report(argv[argv.index('--report') + 1])
    if '--classify' in argv:
        p = argv[argv.index('--classify') + 1]
        for k, lab in enumerate(classify(open(p, encoding='utf-8').read(), all_test='--test' in argv)):
            print('%d\t%s' % (k + 1, lab))
        return 0
    if '--cell' in argv:
        repo = argv[argv.index('--cell') + 1]
        cid = argv[argv.index('--id') + 1] if '--id' in argv else os.path.basename(os.path.dirname(os.path.abspath(repo)))
        if '--header' in argv:
            print(HEADER)
        if not os.path.isdir(repo):
            print('%s\tNO-REPO' % cid)
            return 3
        files, dirty, a, s, seed = measure_cell(repo)
        if not files:
            print('%s\tNO-SOURCE' % cid)
            return 3
        print('%s\t%s\t%d\t%s\t%s\t%s\t%s' % (cid, ','.join(p for p, _ in files), dirty,
                                            '\t'.join(str(a[c]) for c in CLASSES),
                                            '\t'.join(str(s[c]) for c in CLASSES), ratio(a), ratio(s)))
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
