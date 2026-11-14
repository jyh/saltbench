"""Block WA, the Pro slot re-registered on gemini-4-argon-high (council 2026-11-14 ruling 3): the price, written before the first Pro call.
§WA3 prices the agy lane in its own pool's unit, and that unit did not move: the hand read the agy pool at 100 % weekly at every Flash fire
(its delivery, bus offset 102,297,116), so 12 Flash cells give no points-per-cell figure to scale. The lane's binding resource is WALL
(one cell at a time on one run box), so the price is stated in cell-wall:
  ratio   per arm, median argon wall_s / median flash wall_s over the Z wave's greenfield x none legs (evidence/zf-result/zf-cells.tsv,
          tracked; LANDED and scored legs only, so a wedge's wall does not enter a median; its arm column spells salt-diet `salt`)
  base    WA Flash's own wall_seconds per cell (cells.tsv beside this file), per problem x arm median
  price   3 cells x base x ratio, per problem x arm; summed
  python3 pro_price.py   -> every figure the addendum quotes"""
import csv, os, statistics as st
H = os.path.dirname(os.path.abspath(__file__))
Z = [r for r in csv.DictReader((l for l in open(os.path.join(H, '..', 'zf-result', 'zf-cells.tsv')) if not l.startswith('#')), delimiter='\t')]
W = list(csv.DictReader(open(os.path.join(H, 'cells.tsv')), delimiter='\t'))
ratio = {}
ZARM = {'plain': 'plain', 'salt-diet': 'salt'}   # zf-cells.tsv spells the treatment arm `salt`
for arm in ('plain', 'salt-diet'):
    w = {m: [float(r['wall_s']) for r in Z if r['field'] == 'gf' and r['card'] == 'none' and r['arm'] == ZARM[arm] and r['model'] == m
             and r['done_reason'] == 'LANDED' and r['scored'] == 'SCORED'] for m in ('argon', 'flash')}
    ratio[arm] = st.median(w['argon']) / st.median(w['flash'])
    print('Z gf-none %s: argon n %d median wall %.1f s · flash n %d median %.1f s · ratio %.3f' % (
        arm, len(w['argon']), st.median(w['argon']), len(w['flash']), st.median(w['flash']), ratio[arm]))
allr = {}
for arm in ('plain', 'salt-diet'):
    w = {m: [float(r['wall_s']) for r in Z if r['field'] == 'gf' and r['card'] == 'none' and r['arm'] == ZARM[arm] and r['model'] == m]
         for m in ('argon', 'flash')}
    allr[arm] = st.median(w['argon']) / st.median(w['flash'])
    print('Z gf-none %s, every harvested leg (wedges included): argon n %d median %.1f s · flash n %d median %.1f s · ratio %.3f' % (
        arm, len(w['argon']), st.median(w['argon']), len(w['flash']), st.median(w['flash']), allr[arm]))
tot = 0.0; tot_all = 0.0
for p in ('WHT', 'NTT'):
    for arm in ('plain', 'salt-diet'):
        b = st.median([float(r['wall_seconds']) for r in W if r['problem'] == p and r['arm'] == arm])
        c = 3 * b * ratio[arm]; tot += c; tot_all += 3 * b * allr[arm]
        print('WA %s %s: Flash median wall %.1f s · Pro price 3 x %.1f x %.3f = %.0f s' % (p, arm, b, b, ratio[arm], c))
print('Pro price, every leg: %.0f s = %.1f h' % (tot_all, tot_all / 3600))
print('Pro price, 12 cells: %.0f s of cell wall = %.1f h; agy pool points per cell UNMEASURED (pool read 100 %% weekly through all 12 Flash cells)' % (tot, tot / 3600))
