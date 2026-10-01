#!/usr/bin/env python3
"""Desk KS part 2 (bench, 2026-10-01): the token figure beside every dollar figure in RESULT-claude-block{OS,SBS,SS}-2026-09-21 and
RESULT-stepg-opus-specchange-2026-09-29, from the SAME tracked rows their dollars came from (each *-cells.tsv carries final_T).
It never re-reads a run: the rows are the ones the results were printed from. Run from the repo root."""
import csv, statistics

def rows(p):
    return list(csv.DictReader([l for l in open(p) if not l.startswith('#') and l.strip()], delimiter='\t'))

for b in ('OS', 'SBS', 'SS'):
    rs = rows('evidence/claude-lane-blocks-2026-09-21/block%s-cells.tsv' % b)
    print('## block %s (%d cells)' % (b, len(rs)))
    print('cell\tproblem\tarm\tfinal_COST\tfinal_T\tcapped')
    for r in rs:
        print('%s\t%s\t%s\t%s\t%s\t%s' % (r['cell'], r['problem'], r['arm'], r['final_COST'], r['final_T'], r['capped']))
    for arm in ('plain', 'salt-diet'):
        a = [r for r in rs if r['arm'] == arm]
        c = [float(r['final_COST']) for r in a]; t = [int(r['final_T']) for r in a]
        print('# %s %s: n=%d  median COST %.2f  median T %d  total COST %.2f  total T %d' % (b, arm, len(a), statistics.median(c),
              statistics.median(t), sum(c), sum(t)))
rs = rows('evidence/stepg-2026-09-29/cells.tsv')
print('## step g (%d cells, phase 2 only)' % len(rs))
print('cell\ttask\tarm\tfinal_COST\tfinal_T')
for r in rs:
    print('%s\t%s\t%s\t%s\t%s' % (r['cell'], r['task'], r['arm'], r['final_COST'], r['final_T']))
print('# stepg: total COST %.2f  total T %d' % (sum(float(r['final_COST']) for r in rs), sum(int(r['final_T']) for r in rs)))
