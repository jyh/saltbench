"""NCA argon price re-cut (§NCA5 limit (e)) from the Luby argon sextet. Inputs: argon_walls-<date>.tsv beside this file (argon_walls.py,
run on the run box: root, id, p1 wall, p1 landed, p2 wall, p2 landed) and the registered nca_price.out at saltbench --ref.
usage: python3 recut.py <walls.tsv> <saltbench clone> [ref, default origin/main]"""
import re, statistics as st, subprocess, sys
W = [l.rstrip('\n').split('\t') for l in open(sys.argv[1])]
out = subprocess.run(['git', '-C', sys.argv[2], 'show', '%s:evidence/blockNCA-2026-11-23/nca_price.out' % (sys.argv[3] if len(sys.argv) > 3 else 'origin/main')],
                     capture_output=True, text=True, check=True).stdout
reg = {(m.group(1), m.group(2)): float(m.group(3)) for m in (re.match(r'(\w+)\s+(plain|salt-diet)\s.*argon\s+(\d+) s$', l.strip()) for l in out.splitlines()) if m}
if len(reg) != 12:
    sys.exit('REFUSE: %d registered conditions, 12 expected' % len(reg))
ratio = {}
for arm, tag in (('plain', 'plain'), ('salt-diet', 'salt')):
    cw = [float(r[2]) + float(r[4]) for r in W if r[0].startswith('cells-nca-luby-argon-%s-' % tag) and r[3] == r[5] == 'True']
    if len(cw) != 3:
        sys.exit('REFUSE: Luby argon %s has %d cells landed in both phases, 3 expected' % (arm, len(cw)))
    per = reg[('Luby', arm)] / 3
    ratio[arm] = st.median(cw) / per
    print('Luby argon %-9s n %d cell walls (p1+p2) %s median %.1f s · registered per cell %.1f s · measured/registered %.3f' % (
        arm, len(cw), ' '.join('%.1f' % x for x in cw), st.median(cw), per, ratio[arm]))
rest = {k: v for k, v in reg.items() if k[0] != 'Luby'}
old = sum(rest.values()); new = sum(v * ratio[k[1]] for k, v in rest.items())
print('argon rest (5 problems x 2 arms x 3 cells = 30 cells): registered %.0f s = %.1f h · re-cut %.0f s = %.1f h' % (old, old / 3600, new, new / 3600))
for arm in ('plain', 'salt-diet'):
    o = sum(v for k, v in rest.items() if k[1] == arm)
    print('  %-9s registered %.1f h -> re-cut %.1f h' % (arm, o / 3600, o * ratio[arm] / 3600))
