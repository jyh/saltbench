#!/usr/bin/env python3
"""Desk KS (bench, 2026-10-01): the token figure beside every dollar figure RESULT-O37 publishes (§R1, §R2), derived from the same
files the dollars came from. Nothing typed.  Run from the repo root:  python3 evidence/o37-aeneas-pilot-2026-09-30/o37-tokens.py
"""
import csv, statistics

def rows(path, key):
    lines = [l for l in open(path) if not l.startswith('#') and l.strip()]
    head = next(i for i, l in enumerate(lines) if l.split('\t')[0] == key)
    return list(csv.DictReader(lines[head:], delimiter='\t'))

o37 = rows('evidence/o37-aeneas-pilot-2026-09-30/cells.tsv', 'cell')
ss = {r['cell']: r for r in rows('evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv', 'cell')}
raw = {r['cell']: r for r in rows('evidence/v3-cost-tables-2026-09-28/claude-cost-raw.tsv', 'cell')}
print('# source\tcell\tcondition\tUSD\tT\tnote')
groups = {}
def emit(src, cell, cond, usd, t, note='-'):
    print('%s\t%s\t%s\t%s\t%s\t%s' % (src, cell, cond, usd, t, note))
    groups.setdefault(cond, []).append((float(usd), int(t)))
for r in o37:
    emit('cells.tsv', r['cell'], 'lean-aeneas ' + r['condition'], r['final_COST'], r['final_T'])
for c in ('clbscs01', 'clbscs02', 'clbscs03'):
    r = ss[c]; emit('blockSS-cells.tsv', c, 'verus-statement sonnet', r['final_COST'], r['final_T'], 'final_T includes the sandbox probe (file header)')
for c in ('st04crc3', 'st05crc3', 'st06crc3'):
    r = raw[c]; emit('claude-cost-raw.tsv', c, 'verus-statement opus', r['COST'], r['T'], 'void=' + (r.get('void') or '-'))
for cond, xs in groups.items():
    print('# %s: n=%d  median USD %.4f  median T %d  sum USD %.4f  sum T %d' % (cond, len(xs), statistics.median(x[0] for x in xs),
          statistics.median(x[1] for x in xs), sum(x[0] for x in xs), sum(x[1] for x in xs)))
for m in ('opus', 'sonnet'):
    a, b = groups['lean-aeneas ' + m], groups['verus-statement ' + m]
    print('# ratio %s lean/verus at the median: USD %.2fx  T %.2fx' % (m, statistics.median(x[0] for x in a) / statistics.median(x[0] for x in b),
          statistics.median(x[1] for x in a) / statistics.median(x[1] for x in b)))
