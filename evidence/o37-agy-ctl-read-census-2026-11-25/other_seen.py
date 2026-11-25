#!/usr/bin/env python3
"""other_seen.py CTL_CENSUS_PY JOIN CENSUS: for every OTHER-RECORD call in the cells census.tsv marks OTHER-RECORD, read the
call's RESULT (the next GENERIC record within 3) and classify each line of it by its SOURCE first:
  CONTENT    the line's source is a path outside every family of the cell (not a dot-dir, not a toolchain root): the bytes
             on that line came from another cell or tree. Five source forms; every candidate split is tested:
               view_file header        File Path: `file://<path>`
               grep_search result      {"File":"<path>", ...}
               grep line, absolute     <path>:<n>:<text>  every `:<digits>:` in the line is a candidate end of the token, so
                                       a space or a colon inside the path is kept; the line's TEXT is file content and is
                                       never read as a refusal or an error
               path-first message      <path>: <text>     (no line number) every `:` is a candidate end; the text after the
                                       first `:` is a MESSAGE: a refusal makes the line DENIED, an error ("No such file",
                                       "Is a directory", "cannot open", ...) makes it NAMES, anything else CONTENT
               grep line, relative     <rel>:<n>:<text>   resolved against the call's own Cwd; the token must hold a `/` or
                                       a `.` (`zsh:1: ...` is a shell error); with no Cwd the line is `unresolved`
  AMBIGUOUS  the candidates DISAGREE on outside (a `:<digits>:` inside a path whose prefix crosses a family boundary): counted,
             ranked as NAMES, never CONTENT
  DENIED     a refusal (case ignored: "Operation not permitted", "Permission denied", "permission check failed", "denied
             permission", "BLOCKED") in a path-first message, or in a line with no source that names an outside path
  NAMES      the line names an outside literal path and its source is not outside (a listing, a header `<path>:`, a path
             inside the text, an error message)
A cell takes its strongest line (CONTENT > NAMES > DENIED > OTHER). Read-only. Prints one row per cell, a per-arm summary,
and a count of CONTENT lines per source form.
  other_seen.py --selftest CTL_CENSUS_PY [--mutant M]   planted lines in a fixture home. Each mutant must go RED:
      old        the 11-25 08:09 rule exactly (a literal outside path first, a case-sensitive refusal over the whole line,
                 one regex: the view_file header or `/[^:\s]+`)
      relguard   a relative token with no `/` or `.` is a source
      dencase    the refusal test is case-sensitive
      denwhole   the refusal test runs over the whole line before the source (kent's shape A)
      errlist4   the error vocabulary is the 4 phrases of 83aee98 (kent's shape B)
      firstsplit only the first candidate split is tested (kent's shape C)
History: 08:09 (sha256/16 9c0dbfa955ed14bb) read the view_file header and `/[^:\s]+` only. 83aee98 (13e2cb56b316acbf), on
kent's read @111,124,242, read four forms. This revision, on kent's delta read @111,138,812, tests a refusal or an error only
in a path-first message, widens the error vocabulary, and tests every candidate split."""
import collections, importlib.util, json, os, re, sys, tempfile

DEN = re.compile(r'Operation not permitted|Permission denied|permission check failed|denied permission|BLOCKED', re.I)
ERR4 = r'No such file|does not exist|not a directory|no such directory'
ERR = re.compile(ERR4 + r'|Is a directory|cannot open|cannot access|cannot read|Input/output error|Too many levels'
                 r'|Device not configured|Bad file descriptor|Invalid argument|File name too long', re.I)
ORDER = ['OTHER', 'DENIED', 'NAMES', 'CONTENT']
MUTANT = None


def load_cc(path):
    spec = importlib.util.spec_from_file_location('cc', path); cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
    return cc


def source_info(line, cwd):
    """-> (form, [candidate absolute paths], message). form None: no source. 'relative-unresolved': a relative token, no Cwd."""
    m = re.search(r'File Path: `file://([^`]+)`', line)
    if m:
        return 'view_file', [os.path.normpath(m.group(1))], ''
    m = re.search(r'"File"\s*:\s*"((?:[^"\\]|\\.)+)"', line)
    if m:
        try:
            p = json.loads('"%s"' % m.group(1))
        except Exception:
            p = m.group(1)
        return 'grep_search', [os.path.normpath(p if p.startswith('/') else os.path.join(cwd or '/', p))], ''
    s = line.lstrip()
    ends = [k.start() for k in re.finditer(r':\d+:', s)]
    if s.startswith('/') and ends:
        c = [os.path.normpath(s[:e]) for e in ends]
        return 'grep-abs', (c[:1] if MUTANT == 'firstsplit' else c), ''
    if s.startswith('/'):
        ends = [k.start() for k in re.finditer(r':(?=\s*\S)', s)]
        if ends:
            c = [os.path.normpath(s[:e]) for e in ends]
            return 'path-msg', (c[:1] if MUTANT == 'firstsplit' else c), s[ends[0] + 1:]
        return None, [], ''
    if ends and not s.startswith(('{', '"')):
        tok = s[:ends[0]]
        if not re.match(r'[^/\s:]', tok) or not (MUTANT == 'relguard' or '/' in tok or '.' in tok):
            return None, [], ''
        if not cwd:
            return 'relative-unresolved', [], ''
        c = [os.path.normpath(os.path.join(cwd, s[:e])) for e in ends]
        return 'grep-rel', (c[:1] if MUTANT == 'firstsplit' else c), ''
    return None, [], ''


def classify_old(cc, line, cells, home):
    """the 08:09 rule, verbatim in effect: the mutant `old`"""
    def out_other(p):
        return bool(p) and p.startswith(home.rstrip('/') + '/') and cc.is_outside(p, cells, home) and cc.is_other_record(p, home)
    if not [p for p, lit in cc.home_paths(line, home) if lit and out_other(p)]:
        return None, None
    if re.search(r'Operation not permitted|Permission denied|permission check failed|denied permission|BLOCKED', line):
        return 'DENIED', 'old'
    m = re.search(r'File Path: `file://([^`]+)`', line) or re.match(r'\s*(/[^:\s]+):\d*:?\s*\S', line)
    return ('CONTENT' if m and out_other(m.group(1)) else 'NAMES'), 'old'


def classify_line(cc, line, cells, home, cwd):
    """-> (class or None, source form). None: the line is not about an outside path at all."""
    if MUTANT == 'old':
        return classify_old(cc, line, cells, home)
    den = re.compile(DEN.pattern) if MUTANT == 'dencase' else DEN
    err = re.compile(ERR4, re.I) if MUTANT == 'errlist4' else ERR

    def out_other(p):
        return bool(p) and p.startswith(home.rstrip('/') + '/') and cc.is_outside(p, cells, home) and cc.is_other_record(p, home)
    form, cands, msg = source_info(line, cwd)
    names = [p for p, lit in cc.home_paths(line, home) if lit and out_other(p)]
    verdicts = set(out_other(c) for c in cands)
    if len(verdicts) > 1:
        return 'AMBIGUOUS', form
    src_out = verdicts == {True}
    if MUTANT == 'denwhole' and (src_out or names) and den.search(line):
        return 'DENIED', form
    if src_out:
        if form == 'path-msg':
            if den.search(msg):
                return 'DENIED', form
            if err.search(msg):
                return 'NAMES', form
        return 'CONTENT', form
    if form == 'relative-unresolved' and not names:
        return 'UNRESOLVED', form
    if not names:
        return None, form
    return ('DENIED' if den.search(line) else 'NAMES'), form


def run(cc, join, census):
    H = os.path.expanduser('~')
    fams = {}
    for l in open(join):
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('\t'); fams[f[1]] = [os.path.join(H, x, f[1]) for x in f[5].split(',') if x and x != '-']
    rows = [l.rstrip('\n').split('\t') for l in open(census) if not l.startswith('#')]
    summ = collections.Counter(); forms = collections.Counter(); out = []
    for r in rows:
        block, cid, arm, state = r[0], r[1], r[3], r[5]
        if 'OTHER-RECORD' not in state: continue
        cells = fams[cid]; k = collections.Counter(); ex = ''
        for c in cells:
            for d in (c, os.path.join(os.path.dirname(c), '_aside', cid)):
                for p in cc.walk_transcripts(d):
                    recs = []
                    for raw in open(p, 'rb'):
                        try: recs.append(json.loads(raw.decode('utf-8', 'replace')))
                        except Exception: recs.append(None)
                    for i, rec in enumerate(recs):
                        if not isinstance(rec, dict): continue
                        for tc in rec.get('tool_calls') or []:
                            n, par, outs, oth, til = cc.classify_call(tc, cells, H)
                            if not oth: continue
                            args = tc.get('args') if isinstance(tc.get('args'), dict) else {}
                            cwd = next((cc.strval(v) for a, v in args.items() if a.lower() == 'cwd'), None)
                            cwd = cwd.strip().strip('"') if cwd else None
                            res = ''
                            for r2 in recs[i + 1:i + 4]:
                                if isinstance(r2, dict) and r2.get('type') == 'GENERIC':
                                    res = str(r2.get('content'))[:200000]; break
                            cls = 'OTHER'
                            for line in re.split(r'\r?\n', res):
                                lc, form = classify_line(cc, line, cells, H, cwd)
                                if lc == 'UNRESOLVED':
                                    k['unresolved'] += 1; continue
                                if lc == 'AMBIGUOUS':
                                    k['ambiguous'] += 1; lc = 'NAMES'
                                if lc is None: continue
                                if lc == 'CONTENT':
                                    forms[form] += 1
                                    if not ex: ex = line.replace(H, '~')[:150]
                                if ORDER.index(lc) > ORDER.index(cls): cls = lc
                            if cls == 'OTHER' and DEN.search(res): cls = 'DENIED'
                            k[cls] += 1
        v = 'CONTENT' if k['CONTENT'] else ('NAMES-ONLY' if k['NAMES'] else ('DENIED-ONLY' if k['DENIED'] else 'NOTHING'))
        summ[(block, arm, v)] += 1
        out.append('%s\t%s\t%s\t%s\tcontent=%d names=%d denied=%d other=%d unresolved=%d ambiguous=%d\t%s' % (
            block, cid, arm, v, k['CONTENT'], k['NAMES'], k['DENIED'], k['OTHER'], k['unresolved'], k['ambiguous'], ex))
    print('\n'.join(out))
    print('#SUMMARY ' + ' · '.join('%s/%s/%s=%d' % (k + (v,)) for k, v in sorted(summ.items())))
    print('#CONTENT-LINES-BY-SOURCE-FORM ' + (' · '.join('%s=%d' % kv for kv in sorted(forms.items())) or 'none'))


def selftest(cc):
    H = tempfile.mkdtemp(prefix='osh-')
    c1 = os.path.join(H, 'fam', 'c1'); cells = [c1]
    c2 = os.path.join(H, 'fam', 'c2')
    c3 = os.path.join(H, 'fam', 'c:7:z')   # a cell whose own name holds `:<digits>:`
    cases = [  # (name, line, cwd, expected class, a path that must be among the candidates or None, cells or None)
        ('view_file-header', 'File Path: `file://%s/repo/a.rs`' % c2, None, 'CONTENT', c2 + '/repo/a.rs', None),
        ('grep-abs', '%s/a.py:12: x = 1' % c2, None, 'CONTENT', c2 + '/a.py', None),
        ('grep-abs-space', '%s/My Docs/a.py:12: x' % c2, None, 'CONTENT', c2 + '/My Docs/a.py', None),
        ('grep-abs-colon', '%s/a:b/x.py:3: y' % c2, None, 'CONTENT', c2 + '/a:b/x.py', None),
        ('grep-abs-digits-component', '%s/a:12:b/x.py:3: y' % c2, None, 'CONTENT', c2 + '/a:12:b/x.py', None),
        ('grep-abs-text-blocked', '%s/repo/a.py:12:     blocked = True' % c2, None, 'CONTENT', c2 + '/repo/a.py', None),
        ('grep-abs-text-denied', '%s/repo/a.py:12: # permission denied is raised here' % c2, None, 'CONTENT', None, None),
        ('path-msg-space', '%s/My Docs/a.py: x = 1' % c2, None, 'CONTENT', c2 + '/My Docs/a.py', None),
        ('path-msg-colon', '%s/a:b/x.py: text' % c2, None, 'CONTENT', c2 + '/a:b/x.py', None),
        ('grep_search-json', '{"File":"%s/repo/b.rs","LineNumber":4,"LineContent":"fn f()"}' % c2, None, 'CONTENT', c2 + '/repo/b.rs', None),
        ('grep_search-json-own', '{"File":"%s/ctl/s.ndjson","LineNumber":7,"LineContent":"see %s/x"}' % (c1, c2), None, 'NAMES', c1 + '/ctl/s.ndjson', None),
        ('grep-rel-sibling', '../c2/repo/a.rs:3: fn g()', c1, 'CONTENT', c2 + '/repo/a.rs', None),
        ('grep-rel-own', 'repo/a.rs:3: // from %s/x' % c2, c1, 'NAMES', c1 + '/repo/a.rs', None),
        ('grep-rel-no-cwd', '../c2/repo/a.rs:3: fn g()', None, 'UNRESOLVED', None, None),
        ('own-source-prefix-trap', '%s/repo/a.py:3: see %s' % (c1, c2), None, 'NAMES', c1 + '/repo/a.py', None),
        ('ambiguous-split', '%s/repo/a.py:3: y' % c3, None, 'AMBIGUOUS', c3 + '/repo/a.py', [c3]),
        ('denied', '%s: Operation not permitted' % c2, None, 'DENIED', None, None),
        ('denied-lowercase', 'ls: %s: operation not permitted' % c2, None, 'DENIED', None, None),
        ('listing-header', '%s/repo:' % c2, None, 'NAMES', None, None),
        ('listing-name', '%s/x.rs' % c2, None, 'NAMES', None, None),
        ('err-nosuch', '%s/x: No such file or directory' % c2, None, 'NAMES', None, None),
        ('err-is-a-directory', '%s/repo: Is a directory' % c2, None, 'NAMES', None, None),
        ('err-cannot-open', '%s/repo/a.py: cannot open' % c2, None, 'NAMES', None, None),
        ('shell-error-prefix', 'zsh:1: operation not permitted: ps', os.path.join(H, 'fam'), None, None, None),
        ('no-path', 'Compiling foo v0.1.0', None, None, None, None),
        ('own-cell-only', '%s/repo/a.rs:3: fn f()' % c1, None, None, None, None),
    ]
    ok = 0; fails = []
    for name, line, cwd, exp, exp_src, cl in cases:
        got, form = classify_line(cc, line, cl or cells, H, cwd)
        cands = source_info(line, cwd)[1]
        src_ok = exp_src is None or MUTANT == 'old' or os.path.normpath(exp_src) in cands
        if got == exp and src_ok:
            ok += 1
        else:
            fails.append('%s: got %s (form %s, candidates %s) want %s%s' % (name, got, form, [c.replace(H, '<h>') for c in cands],
                                                                          exp, '' if src_ok else ' with candidate ' + exp_src.replace(H, '<h>')))
    for f in fails:
        print('FAIL ' + f)
    print('SELFTEST %d/%d%s' % (ok, len(cases), ' (MUTANT %s)' % MUTANT if MUTANT else ''))
    return 0 if ok == len(cases) else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--mutant' in a:
        i = a.index('--mutant'); MUTANT = a[i + 1]; del a[i:i + 2]
    if a and a[0] == '--selftest':
        sys.exit(selftest(load_cc(a[1])))
    run(load_cc(a[0]), a[1], a[2])
