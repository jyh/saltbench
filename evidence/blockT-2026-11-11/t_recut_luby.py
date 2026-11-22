#!/usr/bin/env python3
"""t_recut_luby.py <luby-tally.tsv> — block T §T4: the price re-cut from the Luby cells, before AES fires.
Per model x arm: ratio = (T's Luby mean final_COST per cell) / (block N's Luby mean final_COST per cell, extras none); means, so a
condition with a cell not yet ended is not under-counted, from tracked files only.
The re-cut price of the other five problems = sum over model x arm of block N's spend there x that ratio.
Every figure printed is computed here from the two files; nothing is typed."""
import csv, sys, os
H = os.path.dirname(os.path.abspath(__file__))
N = os.path.join(H, '..', 'claude-lane-blockN-2026-09-28')
def rows(p):
    with open(p) as f:
        return [r for r in csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t')]
tally = [r for r in rows(sys.argv[1]) if r['final_T'] != 'NOT-ENDED' and r.get('final_COST')]
model = {'TO': 'opus', 'TS': 'sonnet'}
nfile = {'opus': 'blockNO-cells.tsv', 'sonnet': 'blockNS-cells.tsv'}
tot_rest = tot_rest_n = 0.0
print('model\tarm\tT_luby_n\tT_luby_sum\tN_luby_n\tN_luby_sum\tratio\tN_rest_sum\trest_recut')
for m in ('opus', 'sonnet'):
    nr = [r for r in rows(os.path.join(N, nfile[m])) if r.get('extras') == 'none']
    for arm in ('plain', 'salt-diet'):
        t = [float(r['final_COST']) for r in tally if model[r['block']] == m and r['arm'] == arm]
        nl = [float(r['final_COST']) for r in nr if r['problem'] == 'Luby' and r['arm'] == arm]
        rest = sum(float(r['final_COST']) for r in nr if r['problem'] != 'Luby' and r['arm'] == arm)
        ratio = (sum(t) / len(t)) / (sum(nl) / len(nl))
        tot_rest += rest * ratio; tot_rest_n += rest
        print(f'{m}\t{arm}\t{len(t)}\t{sum(t):.2f}\t{len(nl)}\t{sum(nl):.2f}\t{ratio:.3f}\t{rest:.2f}\t{rest*ratio:.2f}')
tl = sum(float(r['final_COST']) for r in tally)
capped = sum(1 for r in tally if r['capped'] == 'yes')
print(f'T Luby spent ${tl:.2f} over {len(tally)} cells (capped {capped}).')
print(f'AES..LinearScan (60 cells): block N spend ${tot_rest_n:.2f}; RE-CUT ${tot_rest:.2f}.')
print(f'Block T re-cut total = Luby spent + rest re-cut = ${tl + tot_rest:.2f} (registered price $1,253.64 for 72 cells).')
