#!/usr/bin/env python3
"""ta_recut_argon.py — §TA3's re-cut of the ARGON price after argon's own Luby sextet (ADDENDUM 2/5 form), from two tracked files:
  ta_price.out            the registered price: argon per cell = NA's Flash median wall x the WA argon/flash factor per arm
  argon-luby-tally.tsv    the hand's tally of TA's six argon Luby cells (wall_seconds by wa_facts.py), copied from its argon score dir
Per arm: ratio = (TA argon Luby median wall) / (registered argon per-cell Luby price); the remaining argon conditions' registered
price x that ratio. Every printed figure is computed here."""
import csv, os, re, statistics, sys
H = os.path.dirname(os.path.abspath(__file__))
price = open(os.path.join(H, "ta_price.out")).read()
ar = {(p, a): float(t) for p, a, t in re.findall(
    r"^NA (\w+) (plain|salt-diet): .*· argon price 3 x [0-9.]+ x [0-9.]+ = ([0-9]+) s$", price, re.M)}
if len(ar) != 12: sys.exit(f"REFUSE: {len(ar)} argon price rows, 12 expected")
rows = list(csv.DictReader(open(os.path.join(H, "argon-luby-tally.tsv")), delimiter="\t"))
wall = {"plain": [], "salt-diet": []}
for r in rows:
    if "argon" not in r["condition"] or not r["condition"].startswith("Luby"): sys.exit(f"REFUSE: row {r['cell']} is not an argon Luby cell")
    a = "salt-diet" if "salt-diet" in r["condition"] else "plain"
    wall[a].append(float(r["wall_seconds(wa_facts.py)"]))
if any(len(v) != 3 for v in wall.values()): sys.exit(f"REFUSE: Luby cells per arm {[len(v) for v in wall.values()]}, 3 each expected")
ratio = {a: statistics.median(wall[a]) / (ar[("Luby", a)] / 3) for a in wall}
for a in ("plain", "salt-diet"):
    print(f"Luby argon {a}: TA median {statistics.median(wall[a]):.1f} s · registered per cell {ar[('Luby', a)]/3:.1f} s · ratio {ratio[a]:.3f}")
reg = cut = 0.0
for P in ("AES", "Liveness", "MaxFlow", "BinomialHeap", "LinearScan"):
    for a in ("plain", "salt-diet"):
        r_ = ar[(P, a)]; c_ = r_ * ratio[a]; reg += r_; cut += c_
        print(f"{P} {a}: registered {r_:.0f} s · re-cut {c_:.0f} s")
done = sum(sum(v) for v in wall.values())
print(f"argon Luby spent {done:.1f} s of cell wall (registered {ar[('Luby','plain')]+ar[('Luby','salt-diet')]:.0f} s)")
print(f"argon AES..LinearScan: registered {reg:.0f} s = {reg/3600:.1f} h · re-cut {cut:.0f} s = {cut/3600:.1f} h")
