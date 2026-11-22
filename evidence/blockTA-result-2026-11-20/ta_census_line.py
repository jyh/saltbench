#!/usr/bin/env python3
"""Print census ADDENDUM 50's block TA lines from cells.tsv beside this file, so no figure in the census is typed.

A condition is (problem, arm, requested_model). For each model the line counts conditions, the n of record per condition
(the cells of record, i.e. every row of cells.tsv; the discarded 503 attempt is not a row), the cells LANDED, the cells
the scorer passed, and the cells flagged MODEL-SEAM (a non-empty swarm_added_models). It refuses unless every condition
has the same n.

usage: ta_census_line.py            print the lines
       ta_census_line.py --check F  exit 1 unless every printed line occurs verbatim in file F
"""
import collections
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def lines():
    with open(os.path.join(HERE, 'cells.tsv'), newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    ids = [r['id'] for r in rows]
    if len(ids) != len(set(ids)):
        sys.exit('refuse: duplicate cell ids in cells.tsv')
    out = []
    conds_all = 0
    for model in sorted({r['requested_model'] for r in rows}):
        rs = [r for r in rows if r['requested_model'] == model]
        per = collections.Counter((r['problem'], r['arm']) for r in rs)
        ns = sorted(set(per.values()))
        if len(ns) != 1:
            sys.exit('refuse: %s conditions do not share one n: %s' % (model, dict(per)))
        landed = sum(1 for r in rs if r['done_reason'] == 'LANDED')
        passed = sum(1 for r in rs if r['verdict'] == 'PASS')
        seam = sum(1 for r in rs if r['swarm_added_models'].strip() not in ('', '-', 'none'))
        conds_all += len(per)
        out.append('block TA %s: %d conditions, %d at n = %d, cells of record %d · LANDED %d · PASS %d · MODEL-SEAM flagged %d'
                   % (model, len(per), len(per), ns[0], len(rs), landed, passed, seam))
    out.append('block TA: the six block-N problems x statement, agy lane: %d conditions, cells of record %d' % (conds_all, len(rows)))
    return out


def main(argv):
    ls = lines()
    if len(argv) == 2 and argv[0] == '--check':
        text = open(argv[1]).read()
        miss = [l for l in ls if l not in text]
        print('%d of %d census lines occur verbatim in %s' % (len(ls) - len(miss), len(ls), argv[1]))
        for l in miss:
            print('  MISSING: ' + l)
        return 1 if miss else 0
    if argv:
        sys.exit(__doc__)
    print('\n'.join(ls))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
