"""Block W §W4: the WHT triple re-cuts the price before NTT fires. Reads wht-costs.tsv beside this file, one row per WHT cell:
cell id, end kind and final_COST, each copied by `tail -1 <cell>/ctl/post-end-1.tsv | cut -f1,5` on the run box (the meter the
cells' watcher writes; final_COST includes the harness's own sandbox probe, as block N's tables do). The cell id's 4th letter is the
model (d Opus, i Sonnet) and its 6th the arm (p plain, s salt-diet), per clb_stage.sh's block table.
  python3 reprice.py   -> the per model x arm medians, the WHT total and the NTT estimate the addendum quotes"""
import os, statistics as st
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wht-costs.tsv'))][1:]
M, A = {'d': 'Opus', 'i': 'Sonnet'}, {'p': 'plain', 's': 'salt-diet'}
est = 0.0
for m in 'di':
    for a in 'ps':
        v = [float(r[2]) for r in rows if r[0][3] == m and r[0][5] == a]
        caps = sum(r[1] == 'CAP-COST' for r in rows if r[0][3] == m and r[0][5] == a)
        est += 3 * st.median(v)
        print('%s %s: n %d · final_COST %s · median $%.2f · CAP-COST %d' % (M[m], A[a], len(v), ' '.join('%.2f' % x for x in v), st.median(v), caps))
print('WHT spent $%.2f over %d cells' % (sum(float(r[2]) for r in rows), len(rows)))
print('NTT estimate: 3 cells x each model x arm median = $%.2f · NTT ceiling 12 x $37.21 = $%.2f' % (est, 12 * 37.21))
