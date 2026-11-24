#!/usr/bin/env python3
"""tw_recut_wht.py <tw-wht-tally.tsv> — block TW §TW4: the price re-cut from the WHT cells of each model, before NTT fires.
Per model x arm: ratio = TW's metered final COST on WHT over block W's metered final_COST on WHT (both extras statement vs none,
the same task tree); NTT re-cut = block W's NTT sum x that ratio. Every figure is computed here from the two files; nothing typed.
The ratio is measured on WHT and applied to NTT, a different problem: an assumption, stated (§TW4)."""
import csv, os, sys
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
W = list(csv.DictReader(open(os.path.join(R, 'blockW-2026-11-14', 'cells.tsv')), delimiter='\t'))
T = list(csv.DictReader(open(sys.argv[1]), delimiter='\t'))
MB = {'WO': 'opus', 'WS': 'sonnet'}
def wsum(model, arm, prob):
    xs = [float(r['final_COST']) for r in W if MB.get(r['model_block']) == model and r['arm'] == arm and r['problem'] == prob]
    return len(xs), sum(xs)
print('model\tarm\tTW_wht_n\tTW_wht_sum\tW_wht_n\tW_wht_sum\tratio\tW_ntt_n\tW_ntt_sum\tntt_recut')
spent = recut = 0.0; n = 0
for model in ('opus', 'sonnet'):
    for arm in ('plain', 'salt-diet'):
        t = [float(r['cost_final']) for r in T if r['model'] == model and r['arm'] == arm and r['problem'] == 'WHT']
        wn, ws = wsum(model, arm, 'WHT'); nn, ns = wsum(model, arm, 'NTT')
        ratio = sum(t) / ws if ws else float('nan'); rc = ns * ratio
        spent += sum(t); recut += rc; n += len(t)
        print('%s\t%s\t%d\t%.2f\t%d\t%.2f\t%.3f\t%d\t%.2f\t%.2f' % (model, arm, len(t), sum(t), wn, ws, ratio, nn, ns, rc))
print('TW WHT spent $%.2f over %d cells.' % (spent, n))
print('NTT (12 cells): RE-CUT $%.2f.' % recut)
print('Block TW re-cut total = WHT spent + NTT re-cut = $%.2f (registered estimate $370.54 for 24 cells).' % (spent + recut))
