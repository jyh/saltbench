#!/usr/bin/env python3
"""nca_price.py --saltbench <clone> --ref <sha> : block NCA's price in cell wall, written before any NCA call (DRAFT, gemini 2026-11-22).

The agy pool's own unit did not move over WA's 24 cells (block WA ADDENDUM 2: the pool read 100 % weekly at every fire), so, as WA's
Pro slot was, this block is priced in CELL WALL, the lane's binding resource (one cell at a time on one run box). Every input is a
tracked file of saltbench at --ref, read by `git show` (so the price names the sha it was cut from):

  FLASH PHASE 1    harness/systems-v3/RESULT-gemini-blockNA-2026-09-28-cells.tsv: wall_s of NA's Flash cells of record
                   (in_registered_n = yes), median per problem x arm. These are the SOURCES a Flash phase 2 continues.
  PHASE-2 RATIO    evidence/l8-chain{D,F}-2026-09-24/phase_facts.json: level 8, the agy lane's spec-change of record (phase 1 and
                   phase 2 in one cell). Per cell with BOTH phases LANDED, wall(phase 2) / wall(phase 1); median per model letter
                   (id char 4, e.g. l8cfps01: f = gemini-3.8-flash-high, p = gemini-3.1-pro-high).
  ARGON / FLASH    evidence/zf-result/zf-cells.tsv, exactly block WA ADDENDUM 2's ratio (pro_price.py): median argon wall over median
                   flash wall, greenfield x none, LANDED and SCORED legs, per arm.

  FLASH  per condition: 3 phase-2 launches x flash_p1_median x ratio_f. Fresh phase 1s are added only for KNOWN shortfalls (an NA
         Flash source with landed != True); the G baselines decide the rest after the signature, so this is a FLOOR on launches.
  ARGON  no argon source exists on the six (NA's Pro slot ran gemini-3.1-pro-high), so every argon cell is a fresh phase 1 + phase 2
         (level 8's form): 3 x [flash_p1_median x argon/flash(arm)] x (1 + ratio_p). ratio_p is 3.1-pro-high's level-8 ratio, a PROXY
         for argon (declared): no argon phase 2 has run on this lane.
"""
import argparse, csv, io, json, statistics as st, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument('--saltbench', required=True)
ap.add_argument('--ref', required=True)
a = ap.parse_args()
sha = subprocess.run(['git', '-C', a.saltbench, 'rev-parse', a.ref], capture_output=True, text=True, check=True).stdout.strip()


def show(path):
    r = subprocess.run(['git', '-C', a.saltbench, 'show', '%s:%s' % (sha, path)], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit('REFUSE: %s not at %s' % (path, sha[:12]))
    return r.stdout


print('nca_price: saltbench %s' % sha[:12])
NA = [r for r in csv.DictReader(io.StringIO(show('harness/systems-v3/RESULT-gemini-blockNA-2026-09-28-cells.tsv')), delimiter='\t')
      if r['in_registered_n'] == 'yes' and r['served'] == 'gemini-3.8-flash-high']
if len(NA) != 36:
    sys.exit('REFUSE: NA Flash cells of record read as %d, the population is 36' % len(NA))

L8 = []
for c in ('D', 'F'):
    L8 += json.loads(show('evidence/l8-chain%s-2026-09-24/phase_facts.json' % c))
by = {}
for r in L8:
    by.setdefault(r['id'], {})[r['phase']] = r
ratio = {}
for m in ('f', 'p'):
    rs = [v[2]['wall_seconds'] / v[1]['wall_seconds'] for k, v in by.items()
          if k[3] == m and 1 in v and 2 in v and v[1].get('landed') and v[2].get('landed') and v[1]['wall_seconds'] > 0]
    ratio[m] = st.median(rs)
    print('L8 phase2/phase1 wall, model letter %s: n %d median %.3f (min %.3f max %.3f)' % (m, len(rs), ratio[m], min(rs), max(rs)))

Z = [r for r in csv.DictReader((l for l in io.StringIO(show('evidence/zf-result/zf-cells.tsv')) if not l.startswith('#')), delimiter='\t')]
ZARM = {'plain': 'plain', 'salt-diet': 'salt'}
af = {}
for arm in ('plain', 'salt-diet'):
    w = {m: [float(r['wall_s']) for r in Z if r['field'] == 'gf' and r['card'] == 'none' and r['arm'] == ZARM[arm] and r['model'] == m
             and r['done_reason'] == 'LANDED' and r['scored'] == 'SCORED'] for m in ('argon', 'flash')}
    af[arm] = st.median(w['argon']) / st.median(w['flash'])
    print('Z argon/flash wall, %s: argon n %d · flash n %d · ratio %.3f' % (arm, len(w['argon']), len(w['flash']), af[arm]))

ft = at = 0.0
fl_launch = ar_launch = 0
short = []
for p in sorted({r['problem'] for r in NA}):
    for arm in ('plain', 'salt-diet'):
        cs = [r for r in NA if r['problem'] == p and r['arm'] == arm]
        b = st.median([float(r['wall_s']) for r in cs])
        ks = [r['id'] for r in cs if r['landed'] != 'True']
        short += ks
        f = 3 * b * ratio['f'] + len(ks) * b * (1 + ratio['f'])
        g = 3 * b * af[arm] * (1 + ratio['p'])
        ft += f; at += g; fl_launch += 3 + len(ks); ar_launch += 6
        print('%-12s %-9s flash p1 median %7.1f s · Flash %6.0f s (known shortfall %d%s) · argon %6.0f s' % (
            p, arm, b, f, len(ks), (' ' + ','.join(ks)) if ks else '', g))
print('KNOWN Flash shortfalls (landed != True): %d %s' % (len(short), ' '.join(short)))
print('Flash: %d launches floor · %.0f s = %.1f h of cell wall' % (fl_launch, ft, ft / 3600))
print('argon: %d launches · %.0f s = %.1f h of cell wall' % (ar_launch, at, at / 3600))
print('NCA total: %d launches floor · %.1f h of cell wall; agy pool points per cell UNMEASURED' % (fl_launch + ar_launch, (ft + at) / 3600))
