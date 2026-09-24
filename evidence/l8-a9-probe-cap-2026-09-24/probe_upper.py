"""Upper bound on the P-PERSIST probe turn, per cell and phase, for level 8 ADDENDUM 9 §A9.5.
  probe_upper_s = FIRING time of the phase (wave fire log) + the turn loop's wall_seconds - the landed-N commit time
Inputs, all in this directory:
  phase_fire_times.txt       `grep -o '<ts> widen-<task> FIRING <id> phase <n>'` over chain D's wave fire logs (last firing wins)
  landing_commit_times.txt   `<id> <phase> <committer ISO time of tag landed-<phase>>` read from each cell's repo on the run box
  phase_facts.json           wall_seconds and rc per cell and phase (ctl/agy-turnloop-N.json, or _aside/<id>/phase1/ctl/)
It is an UPPER bound: it includes the seconds between bin/declare's commit and the probe being sent."""
import json, datetime as dt, statistics as st, os
here = os.path.dirname(os.path.abspath(__file__))
ts = lambda s: dt.datetime.fromisoformat(s.replace('Z', '+00:00'))
pf = {(x['id'], x['phase']): x for x in json.load(open(os.path.join(here, 'phase_facts.json')))}
land = {(c, int(p)): ts(t) for c, p, t in (l.split() for l in open(os.path.join(here, 'landing_commit_times.txt'))) if t != 'NONE'}
fire = {}
for l in open(os.path.join(here, 'phase_fire_times.txt')):
    w = l.split(); fire[(w[3], int(w[5]))] = ts(w[0])
rows = []
for (c, p), x in sorted(pf.items()):
    if 'wall_seconds' in x and (c, p) in land and (c, p) in fire:
        rows.append({'id': c, 'phase': p, 'rc': x['rc'], 'wall_seconds': x['wall_seconds'],
                     'probe_upper_s': round((fire[(c, p)] + dt.timedelta(seconds=x['wall_seconds']) - land[(c, p)]).total_seconds(), 1)})
ok = sorted(r['probe_upper_s'] for r in rows if r['rc'] == 0)
print(json.dumps(rows, indent=1))
print('# rc0 n=%d median=%.0f p90=%.0f  within 251 s: %d  over 600 s (all rc): %d' % (
    len(ok), st.median(ok), ok[int(0.9 * len(ok)) - 1], sum(1 for v in ok if v <= 251), sum(1 for r in rows if r['probe_upper_s'] > 600)))
