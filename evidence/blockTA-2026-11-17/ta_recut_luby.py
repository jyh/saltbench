#!/usr/bin/env python3
"""ta_recut_luby.py — §TA3's re-cut of the Flash price after the Luby sextet, from two tracked files only:
  ta_price.out              the registered price (NA's Flash median wall per problem and arm, x3)
  flash-luby-tally.tsv      the hand's tally of TA's six Flash Luby cells (wall_seconds by wa_facts.py), copied from its score dir
Per arm: ratio = (TA Luby Flash median wall) / (NA Luby Flash median wall); the remaining Flash conditions' registered price x that ratio.
Every printed figure is computed here."""
import csv, os, re, statistics, sys
H = os.path.dirname(os.path.abspath(__file__))
price = open(os.path.join(H, "ta_price.out")).read()
na = {(p, a): float(m) for p, a, m in re.findall(r"^NA (\w+) (plain|salt-diet): flash n \d+ median wall ([0-9.]+) s", price, re.M)}
if len(na) != 12: sys.exit(f"REFUSE: {len(na)} NA price rows, 12 expected")
rows = list(csv.DictReader(open(os.path.join(H, "flash-luby-tally.tsv")), delimiter="\t"))
wall = {"plain": [], "salt-diet": []}
for r in rows:
    a = "salt-diet" if "salt-diet" in r["condition"] else "plain"
    wall[a].append(float(r["wall_seconds(wa_facts.py)"]))
if any(len(v) != 3 for v in wall.values()): sys.exit(f"REFUSE: Luby cells per arm {[len(v) for v in wall.values()]}, 3 each expected")
ratio = {a: statistics.median(wall[a]) / na[("Luby", a)] for a in wall}
for a in ("plain", "salt-diet"):
    print(f"Luby Flash {a}: TA median {statistics.median(wall[a]):.1f} s · NA median {na[('Luby', a)]:.1f} s · ratio {ratio[a]:.3f}")
reg = cut = 0.0
for P in ("AES", "Liveness", "MaxFlow", "BinomialHeap", "LinearScan"):
    for a in ("plain", "salt-diet"):
        r_ = 3 * na[(P, a)]; c_ = r_ * ratio[a]; reg += r_; cut += c_
        print(f"{P} {a}: registered {r_:.0f} s · re-cut {c_:.0f} s")
done = sum(sum(v) for v in wall.values())
print(f"Flash Luby spent {done:.1f} s of cell wall (registered {3*na[('Luby','plain')]+3*na[('Luby','salt-diet')]:.0f} s)")
print(f"Flash AES..LinearScan: registered {reg:.0f} s = {reg/3600:.1f} h · re-cut {cut:.0f} s = {cut/3600:.1f} h")
