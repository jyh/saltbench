#!/usr/bin/env python3
"""Tally agy per-turn print-timeout hits in ZF cell roots, by model, arm and condition.

Input: census.txt, one line per cell root on the run box:
  <root> files=<n agy-stderr-*.txt> hits=<grep -c -F "print timeout" over their concatenation: one total per root>
Produced on the run box 2026-10-22 by:
  for d in ~/cells-*; do cat $d/ctl/agy-stderr-*.txt | grep -c -F "print timeout"; done
DISCARDED roots are excluded (their re-fire is counted instead).
"""
import collections, re, sys

def tally(lines):
    agg = collections.defaultdict(lambda: [0, 0, 0])
    for line in lines:
        root, files, hits = line.split()
        if 'DISCARDED' in root:
            continue
        m = re.match(r'cells-(?:l8)?zf-(\w+)-(argon|flash)-(plain|salt)-(.*)', root)
        if not m:
            raise SystemExit('UNPARSED ' + root)
        _, model, arm, rest = m.groups()
        cond = 'sc' if re.search(r'(^|-)sc($|-)', rest) else re.sub(r'-r\d.*', '', rest)
        h = int(hits.split('=')[1])
        a = agg[(model, arm, cond)]
        a[0] += 1; a[1] += h > 0; a[2] += h
    return agg

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'census.txt'
    agg = tally(open(path))
    print('model  arm    cond     roots  roots-hit  hits')
    tot = collections.defaultdict(lambda: [0, 0, 0])
    for k in sorted(agg):
        print('%-6s %-6s %-8s %5d %10d %5d' % (*k, *agg[k]))
        t = tot[k[1]]
        for i in range(3): t[i] += agg[k][i]
    for arm in sorted(tot):
        print('TOTAL  %-6s %-8s %5d %10d %5d' % (arm, '', *tot[arm]))
