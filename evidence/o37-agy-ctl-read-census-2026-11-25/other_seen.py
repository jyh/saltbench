#!/usr/bin/env python3
"""other_seen.py CTL_CENSUS_PY JOIN CENSUS: for every OTHER-RECORD call in the cells census.tsv marks OTHER-RECORD, read the
call's RESULT (the next GENERIC record within 3) and classify each line of it:
  CONTENT  the line's SOURCE is a path outside every family of the cell (not a dot-dir, not a toolchain root): the bytes on
           that line came from another cell or tree. Four source forms, each tested as the WHOLE token, never a prefix:
             view_file header      File Path: `file://<path>`
             grep_search result    {"File":"<path>", ...}
             grep line, absolute   <path>:<n>:<text>   (the token runs to the FIRST `:<digits>:`, so a space or a colon
                                   inside the path is kept; with no line number, to the first `:` followed by text)
             grep line, relative   <rel>:<n>:<text>    resolved against the call's own Cwd argument; with no Cwd the line
                                   is counted `unresolved` and is never CONTENT; the token must hold a `/` or
                                   a `.` (so a shell error `zsh:1: ...` is not a source)
  DENIED   the line carries a refusal, case ignored ("Operation not permitted", zsh's "operation not permitted", "Permission denied", "permission check failed",
           "denied permission", "BLOCKED") and names an outside path or has an outside source
  NAMES    the line names an outside literal path (a listing, a header `<path>:`, a path inside the text, a
           "No such file" line) and its source is not outside
A cell takes its strongest line (CONTENT > NAMES > DENIED > OTHER). Read-only. Prints one row per cell, a per-arm summary,
and a count of CONTENT lines per source form.
  other_seen.py --selftest CTL_CENSUS_PY [--mutant old|relguard|dencase]   planted lines with a fixture home; each
      mutant must go RED: old = the 11-25 08:09 rule (one regex, no JSON, no relative); relguard = a relative token with
      no `/` or `.` is a source; dencase = the refusal test is case-sensitive
History: the 11-25 08:09 revision (sha256/16 9c0dbfa955ed14bb) tested only the view_file header and an absolute grep token
`/[^:\\s]+`, and filtered lines on a literal outside path BEFORE testing the source. kent's read of #474 (bus @111,124,242)
named the space and colon shapes; the probe names_lines.py found the JSON and relative forms."""
import collections, importlib.util, json, os, re, sys, tempfile

DEN = re.compile(r'Operation not permitted|Permission denied|permission check failed|denied permission|BLOCKED', re.I)
NOSUCH = re.compile(r'No such file|does not exist|not a directory|no such directory', re.I)
ORDER = ['OTHER', 'DENIED', 'NAMES', 'CONTENT']
MUTANT = None


def load_cc(path):
    spec = importlib.util.spec_from_file_location('cc', path); cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
    return cc


def source_path(line, cwd):
    """-> (form, path or None). path is absolute and normalised; None with form 'relative-unresolved' when no Cwd."""
    if MUTANT == 'old':
        m = re.search(r'File Path: `file://([^`]+)`', line) or re.match(r'\s*(/[^:\s]+):\d*:?\s*\S', line)
        return ('old', m.group(1)) if m else (None, None)
    m = re.search(r'File Path: `file://([^`]+)`', line)
    if m:
        return 'view_file', os.path.normpath(m.group(1))
    m = re.search(r'"File"\s*:\s*"((?:[^"\\]|\\.)+)"', line)
    if m:
        try:
            p = json.loads('"%s"' % m.group(1))
        except Exception:
            p = m.group(1)
        return 'grep_search', os.path.normpath(p) if p.startswith('/') else os.path.normpath(os.path.join(cwd or '/', p))
    s = line.lstrip()
    m = re.match(r'(/.+?):\d+:', s) or re.match(r'(/[^:]+?):\s*\S', s)
    if m:
        return 'grep-abs', os.path.normpath(m.group(1))
    m = re.match(r'([^/\s:{"][^:]*?):\d+:', s)
    if m and (MUTANT == 'relguard' or '/' in m.group(1) or '.' in m.group(1)):   # a path token; `zsh:1:` / `bash: line 1:` are shell errors
        if not cwd:
            return 'relative-unresolved', None
        return 'grep-rel', os.path.normpath(os.path.join(cwd, m.group(1)))
    return None, None


def classify_line(cc, line, cells, home, cwd):
    """-> (class or None, source form). None: the line is not about an outside path at all."""
    def out_other(p):
        return bool(p) and p.startswith(home.rstrip('/') + '/') and cc.is_outside(p, cells, home) and cc.is_other_record(p, home)
    form, src = source_path(line, cwd)
    src_out = out_other(src)
    names = [p for p, lit in cc.home_paths(line, home) if lit and out_other(p)]
    if MUTANT == 'old' and not names:
        return None, form
    if not src_out and not names:
        return (None, form) if form != 'relative-unresolved' else ('UNRESOLVED', form)
    if (re.compile(DEN.pattern).search(line) if MUTANT == 'dencase' else DEN.search(line)):
        return 'DENIED', form
    if src_out and not NOSUCH.search(line):
        return 'CONTENT', form
    return 'NAMES', form


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
                                if lc is None: continue
                                if lc == 'CONTENT':
                                    forms[form] += 1
                                    if not ex: ex = line.replace(H, '~')[:150]
                                if ORDER.index(lc) > ORDER.index(cls): cls = lc
                            if cls == 'OTHER' and DEN.search(res): cls = 'DENIED'
                            k[cls] += 1
        v = 'CONTENT' if k['CONTENT'] else ('NAMES-ONLY' if k['NAMES'] else ('DENIED-ONLY' if k['DENIED'] else 'NOTHING'))
        summ[(block, arm, v)] += 1
        out.append('%s\t%s\t%s\t%s\tcontent=%d names=%d denied=%d other=%d unresolved=%d\t%s' % (
            block, cid, arm, v, k['CONTENT'], k['NAMES'], k['DENIED'], k['OTHER'], k['unresolved'], ex))
    print('\n'.join(out))
    print('#SUMMARY ' + ' · '.join('%s/%s/%s=%d' % (k + (v,)) for k, v in sorted(summ.items())))
    print('#CONTENT-LINES-BY-SOURCE-FORM ' + (' · '.join('%s=%d' % kv for kv in sorted(forms.items())) or 'none'))


def selftest(cc):
    H = tempfile.mkdtemp(prefix='osh-')
    c1 = os.path.join(H, 'fam', 'c1'); cells = [c1]
    c2 = os.path.join(H, 'fam', 'c2')
    cases = [  # (name, line, cwd, expected class, expected source path or None to skip the check)
        ('view_file-header', 'File Path: `file://%s/repo/a.rs`' % c2, None, 'CONTENT', c2 + '/repo/a.rs'),
        ('grep-abs', '%s/a.py:12: x = 1' % c2, None, 'CONTENT', c2 + '/a.py'),
        ('grep-abs-space', '%s/My Docs/a.py:12: x' % c2, None, 'CONTENT', c2 + '/My Docs/a.py'),
        ('grep-abs-colon', '%s/a:b/x.py:3: y' % c2, None, 'CONTENT', c2 + '/a:b/x.py'),
        ('grep-abs-nonum-space', '%s/My Docs/a.py: x = 1' % c2, None, 'CONTENT', c2 + '/My Docs/a.py'),
        ('grep_search-json', '{"File":"%s/repo/b.rs","LineNumber":4,"LineContent":"fn f()"}' % c2, None, 'CONTENT', c2 + '/repo/b.rs'),
        ('grep_search-json-own', '{"File":"%s/ctl/s.ndjson","LineNumber":7,"LineContent":"see %s/x"}' % (c1, c2), None, 'NAMES', c1 + '/ctl/s.ndjson'),
        ('grep-rel-sibling', '../c2/repo/a.rs:3: fn g()', c1, 'CONTENT', c2 + '/repo/a.rs'),
        ('grep-rel-own', 'repo/a.rs:3: // from %s/x' % c2, c1, 'NAMES', c1 + '/repo/a.rs'),
        ('grep-rel-no-cwd', '../c2/repo/a.rs:3: fn g()', None, 'UNRESOLVED', None),
        ('own-source-prefix-trap', '%s/repo/a.py:3: see %s' % (c1, c2), None, 'NAMES', c1 + '/repo/a.py'),
        ('denied', '%s: Operation not permitted' % c2, None, 'DENIED', None),
        ('listing-header', '%s/repo:' % c2, None, 'NAMES', None),
        ('listing-name', '%s/x.rs' % c2, None, 'NAMES', None),
        ('nosuch', '%s/x: No such file or directory' % c2, None, 'NAMES', None),
        ('no-path', 'Compiling foo v0.1.0', None, None, None),
        ('shell-error-prefix', 'zsh:1: operation not permitted: ps', os.path.join(H, 'fam'), None, None),
        ('denied-lowercase', 'ls: %s: operation not permitted' % c2, None, 'DENIED', None),
        ('own-cell-only', '%s/repo/a.rs:3: fn f()' % c1, None, None, None),
    ]
    ok = 0; fails = []
    for name, line, cwd, exp, exp_src in cases:
        got, form = classify_line(cc, line, cells, H, cwd)
        src_ok = True
        if exp_src is not None:
            src_ok = source_path(line, cwd)[1] == os.path.normpath(exp_src)
        if got == exp and src_ok:
            ok += 1
        else:
            fails.append('%s: got %s (form %s, src %s) want %s%s' % (name, got, form, source_path(line, cwd)[1], exp,
                                                                     '' if src_ok else ' src ' + exp_src))
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
