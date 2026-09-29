"""Every block-NA wave's CAPS line (level 6 ADDENDUM 7, A7.2: "The hand files that line with each wave's receipts, and a wave
whose line differs from A7.2 is reported as such"). One row per fire log under ~/.fleet/executors/gemini.runs/na-*/, which is
where the canary wave copies agy_wave_v3.sh's banner. Nothing is typed except A7.2's four registered values, quoted from
harness/systems-v3/AMENDMENT-gemini-level6-2026-09-16.md A7.2.   usage: python3 caps_lines.py > caps_lines.tsv"""
import glob, os, re, sys
RUNS = os.path.expanduser('~/.fleet/executors/gemini.runs')
HERE = os.path.dirname(os.path.abspath(__file__))
CELLS = os.path.join(HERE, '..', '..', 'harness', 'systems-v3', 'RESULT-gemini-blockNA-2026-09-28-cells.tsv')
A72 = {'per_turn': '1800s', 'controller_patience': '2100s', 'wall': '21600s', 'turns': '40'}   # A7.2, :741-744
CAPS = re.compile(r'CAPS per-turn (\S+) · controller patience (\S+) · probe patience (\S+) · wall (\S+) · turns (\S+)')
rows = [l.rstrip('\n').split('\t') for l in open(CELLS)]
h = {k: i for i, k in enumerate(rows[0])}
roots = {r[h['root']] for r in rows[1:]}
print('\t'.join(['wave_dir', 'root', 'in_table', 'stamp', 'export', 'per_turn', 'controller_patience', 'probe_patience', 'wall',
                 'turns', 'vs_A7.2', 'fire_log']))
bad = 0
for f in sorted(glob.glob(os.path.join(RUNS, 'na-*', 'cells-*.fire.log'))):
    txt = open(f, encoding='utf-8', errors='replace').read()
    caps = [l for l in txt.splitlines() if ' CAPS ' in l]
    exp = re.search(r'START arm=.* export ([0-9a-f]{12})', txt)
    root = os.path.basename(f)[:-len('.fire.log')]
    if len(caps) != 1 or not CAPS.search(caps[0]):
        bad += 1
        print('\t'.join([os.path.basename(os.path.dirname(f)), root, str(root in roots), '-', '-', *['UNREAD'] * 5,
                         'CAPS LINES=%d' % len(caps), os.path.relpath(f, RUNS)]))
        continue
    m = CAPS.search(caps[0])
    got = dict(zip(['per_turn', 'controller_patience', 'probe_patience', 'wall', 'turns'], m.groups()))
    diff = [k for k in A72 if got[k] != A72[k]]
    verdict = 'SAME (4 of 4) + probe_patience not in A7.2' if not diff else 'DIFFERS: ' + ','.join(diff)
    bad += bool(diff)
    print('\t'.join([os.path.basename(os.path.dirname(f)), root, str(root in roots), caps[0].split()[0],
                     exp.group(1) if exp else 'UNREAD', *[got[k] for k in ['per_turn', 'controller_patience', 'probe_patience',
                     'wall', 'turns']], verdict, os.path.relpath(f, RUNS)]))
missing = roots - {os.path.basename(f)[:-len('.fire.log')] for f in glob.glob(os.path.join(RUNS, 'na-*', 'cells-*.fire.log'))}
for r in sorted(missing):
    bad += 1
    print('\t'.join(['-', r, 'True', '-', '-', *['NO-FIRE-LOG'] * 5, 'NO CAPS LINE FILED', '-']))
sys.stderr.write('caps_lines: %d problem row(s)\n' % bad)
sys.exit(1 if bad else 0)
