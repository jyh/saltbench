#!/usr/bin/env python3
# tw_price.py — block TW's registered price, printed from three TRACKED tables and nothing typed:
#   block N (extras none, the six) `evidence/claude-lane-blockN-2026-09-28/block{NO,NS}-cells.tsv`,
#   block T (extras statement, the same six) `evidence/blockT-result-2026-11-22/cells.tsv`,
#   block W (extras none, WHT and NTT) `evidence/blockW-2026-11-14/cells.tsv`.
# Per model x arm: ratio = T's metered final_COST sum over N's on the six (like for like: both metered, both include the harness's
# sandbox probe); estimate = W's metered sum on WHT/NTT x that ratio. The ratio rests on six OTHER problems: an assumption, stated.
import csv, os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SIX = {'Luby', 'AES', 'Liveness', 'MaxFlow', 'BinomialHeap', 'LinearScan'}
def rows(p):
    with open(os.path.join(R, p)) as f:
        L = [l for l in f if not l.startswith('#')]
    return list(csv.DictReader(L, delimiter='\t'))
N = [(m, r) for m, p in (('opus', 'claude-lane-blockN-2026-09-28/blockNO-cells.tsv'), ('sonnet', 'claude-lane-blockN-2026-09-28/blockNS-cells.tsv')) for r in rows(p)]
T = rows('blockT-result-2026-11-22/cells.tsv'); W = rows('blockW-2026-11-14/cells.tsv')
mT = {'TO': 'opus', 'TS': 'sonnet'}; mW = {'WO': 'opus', 'WS': 'sonnet'}
tot = 0.0
for m in ('opus', 'sonnet'):
    for a in ('plain', 'salt-diet'):
        n = [float(r['final_COST']) for mm, r in N if mm == m and r['arm'] == a and r['problem'] in SIX]
        t = [float(r['final_COST']) for r in T if mT[r['model_block']] == m and r['arm'] == a]
        w = [float(r['final_COST']) for r in W if mW[r['model_block']] == m and r['arm'] == a]
        ratio = sum(t) / sum(n); est = sum(w) * ratio; tot += est
        print(f'{m:<6} {a:<9} N six {len(n)} cells ${sum(n):,.2f} · T six {len(t)} cells ${sum(t):,.2f} · ratio {ratio:.3f} · W WHT/NTT {len(w)} cells ${sum(w):,.2f} -> ${est:,.2f}')
print(f'block TW estimate ${tot:,.2f} for {len(W)} cells · ceiling {len(W)} x $37.21 = ${len(W) * 37.21:,.2f}, plus each cell overrun past the cap')
