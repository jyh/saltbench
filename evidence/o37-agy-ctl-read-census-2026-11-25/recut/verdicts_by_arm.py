#!/usr/bin/env python3
"""verdicts_by_arm.py CORRECTNESS_MD SETFILE: the gemini MATRIX cells' verdict class (the correctness tables' per-cell rows),
by arm and level, for the cells in SETFILE beside the cells that stay. Read-only; prints a table."""
import collections, re, sys
lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
i = [k for k, l in enumerate(lines) if l.startswith('## Per-cell verdicts')][0]
hdr, rows = None, []
for l in lines[i + 1:]:
    if l.startswith('##'):
        break
    if not l.startswith('|'):
        continue
    f = [x.strip() for x in l.strip('|').split('|')]
    if hdr is None:
        hdr = f
        continue
    if set(f[0]) <= set('-: '):
        continue
    rows.append(dict(zip(hdr, f)))
S = set(x.split()[0] for x in open(sys.argv[2]) if x.strip() and not x.startswith('#'))
t = collections.Counter()
for r in rows:
    if not r['model'].startswith('gemini'):
        continue
    lvl = re.match(r'(s3|b4|l5|l6v|l7|l8)', r['cell'])
    lvl = lvl.group(1) if lvl else '?'
    g = 'IN-SET' if r['cell'] in S else 'stays'
    for L in (lvl, 'all'):
        t[(g, r['arm'], L, r['class'])] += 1
classes = ['PASS', 'FAIL', 'by condition', 'CENSORED', 'UNSCORABLE', 'unmeasured']
print('| group | arm | level | ' + ' | '.join(classes) + ' | PASS of PASS+FAIL |')
print('|---|---|---|' + '---|' * (len(classes) + 1))
for g in ('IN-SET', 'stays'):
    for arm in ('plain', 'salt-diet'):
        for L in ('s3', 'b4', 'l5', 'l6v', 'l7', 'l8', 'all'):
            c = [t[(g, arm, L, k)] for k in classes]
            if not sum(c):
                continue
            pf = c[0] + c[1]
            print('| %s | %s | %s | %s | %s |' % (g, arm, L, ' | '.join(map(str, c)), '%d/%d' % (c[0], pf) if pf else '-'))
