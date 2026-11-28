#!/usr/bin/env python3
"""lines_delta.py OTHER_SEEN_PY CTL_CENSUS_PY JOIN CENSUS: LINE-level census for kent's delta read of #474 (shapes A, B, C).
Over every result line of every OTHER-RECORD call in the 52 cells, class the line under the rule (no mutant) and under
each mutant, and count the lines whose class differs, by (mutant, rule class, mutant class). A mutant's count is the number
of lines in the population that its shape decides. Read-only."""
import collections, importlib.util, json, os, re, sys
spec = importlib.util.spec_from_file_location('os_', sys.argv[1]); osn = importlib.util.module_from_spec(spec); spec.loader.exec_module(osn)
cc = osn.load_cc(sys.argv[2]); H = os.path.expanduser('~')
fams = {}
for l in open(sys.argv[3]):
    if l.startswith('#') or not l.strip(): continue
    f = l.rstrip('\n').split('\t'); fams[f[1]] = [os.path.join(H, x, f[1]) for x in f[5].split(',') if x and x != '-']
rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[4]) if not l.startswith('#')]
MUTS = ['old', 'denwhole', 'errlist4', 'firstsplit', 'relguard', 'dencase']
delta = collections.Counter(); nlines = 0; rule = collections.Counter(); cells = set()
for r in rows:
    if 'OTHER-RECORD' not in r[5]: continue
    cl = fams[r[1]]
    for c in cl:
        for d in (c, os.path.join(os.path.dirname(c), '_aside', r[1])):
            for p in cc.walk_transcripts(d):
                recs = []
                for raw in open(p, 'rb'):
                    try: recs.append(json.loads(raw.decode('utf-8', 'replace')))
                    except Exception: recs.append(None)
                for i, rec in enumerate(recs):
                    if not isinstance(rec, dict): continue
                    for tc in rec.get('tool_calls') or []:
                        if not cc.classify_call(tc, cl, H)[3]: continue
                        args = tc.get('args') if isinstance(tc.get('args'), dict) else {}
                        cwd = next((cc.strval(v) for a, v in args.items() if a.lower() == 'cwd'), None)
                        cwd = cwd.strip().strip('"') if cwd else None
                        res = ''
                        for r2 in recs[i + 1:i + 4]:
                            if isinstance(r2, dict) and r2.get('type') == 'GENERIC':
                                res = str(r2.get('content'))[:200000]; break
                        for line in re.split(r'\r?\n', res):
                            osn.MUTANT = None
                            base = osn.classify_line(cc, line, cl, H, cwd)[0]
                            nlines += 1; rule[base] += 1
                            for m in MUTS:
                                osn.MUTANT = m
                                got = osn.classify_line(cc, line, cl, H, cwd)[0]
                                if got != base:
                                    delta[(m, base, got)] += 1; cells.add((m, r[1]))
osn.MUTANT = None
print('lines read %d; rule classes: %s' % (nlines, ' · '.join('%s=%d' % (k, v) for k, v in sorted(rule.items(), key=lambda kv: str(kv[0])))))
for m in MUTS:
    ks = [(k, v) for k, v in sorted(delta.items(), key=str) if k[0] == m]
    print('%-10s lines that differ %d%s; cells %s' % (m, sum(v for k, v in ks), ''.join(' · %s→%s %d' % (k[1], k[2], v) for k, v in ks),
                                                   ' '.join(sorted(c for mm, c in cells if mm == m)) or 'none'))
