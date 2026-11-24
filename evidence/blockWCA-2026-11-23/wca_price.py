#!/usr/bin/env python3
"""wca_price.py --saltbench <clone> --ref <sha> : block WCA's price in cell wall, written before any WCA call (DRAFT, gemini 2026-11-22).

Same unit and reason as nca_price.py (block WA ADDENDUM 2: the agy pool's unit did not move, so cell wall is the price). Inputs, tracked
files of saltbench at --ref, read by `git show`:
  SOURCES        evidence/blockWA-2026-11-14/cells.tsv (Flash, 12) and evidence/blockWA-pro-2026-11-15/cells.tsv (argon, 12): wall_seconds of
                 WA's cells of record, median per problem x arm x model. Every source is a copy candidate (both models have a source).
  PHASE-2 RATIO  evidence/l8-chain{D,F}-2026-09-24/phase_facts.json, as nca_price.py: f for Flash; p (gemini-3.1-pro-high) as the PROXY
                 for argon, declared (no argon phase 2 has run on this lane).
  price per condition = 3 phase-2 launches x source median x ratio. Shortfalls are decided by the G baselines after the signature, so
  a shortfall adds a fresh cell (phase 1 + phase 2) the price does not hold: it is a FLOOR.
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


print('wca_price: saltbench %s' % sha[:12])
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
    print('L8 phase2/phase1 wall, model letter %s: n %d median %.3f' % (m, len(rs), ratio[m]))
tot = {}
for model, f, letter in (('gemini-3.8-flash-high', 'evidence/blockWA-2026-11-14/cells.tsv', 'f'),
                         ('gemini-4-argon-high', 'evidence/blockWA-pro-2026-11-15/cells.tsv', 'p')):
    W = list(csv.DictReader(io.StringIO(show(f)), delimiter='\t'))
    if len(W) != 12 or any(r['requested_model'] != model for r in W):
        sys.exit('REFUSE: %s did not read as 12 cells of %s' % (f, model))
    nl = [r['id'] for r in W if r['landed'] != 'True']
    tot[model] = 0.0
    for p in ('NTT', 'WHT'):
        for arm in ('plain', 'salt-diet'):
            b = st.median([float(r['wall_seconds']) for r in W if r['problem'] == p and r['arm'] == arm])
            c = 3 * b * ratio[letter]
            tot[model] += c
            print('%-22s %-3s %-9s source median %7.1f s · phase 2 %6.0f s' % (model, p, arm, b, c))
    print('%s: sources not landed %d %s · 12 phase-2 launches floor · %.0f s = %.1f h' % (model, len(nl), ' '.join(nl), tot[model], tot[model] / 3600))
s = sum(tot.values())
print('WCA total: 24 launches floor · %.0f s = %.1f h of cell wall; agy pool points per cell UNMEASURED' % (s, s / 3600))
