"""agg.py — token figures beside the dollar figure, per ROOT and never pooled across roots.

⛔ THE EXCLUSION-NEUTRALITY CHECK RUNS FIRST, BEFORE ANY AGGREGATE.
⛔⛔ AND THE ROOT FILTER IS EXPLICIT. An earlier cut hard-coded `root == "cells-matrix1"`, so running
it over a seven-root file produced an aggregate byte-identical to the one-root run — a summary that
silently described a different population than its input. A filter that narrows without saying so is
the same defect as a census over the tree in front of you.
⛔ ROOTS ARE NOT POOLED. They are different populations (different waves, arms, dates, task sets), and
pooling them is the confound this campaign already cards. Pass --root to pick one; the default reports
each separately.
"""
import csv, sys, statistics as st

args = [a for a in sys.argv[1:]]
path = args[0]
want = None
if "--root" in args:
    want = args[args.index("--root") + 1]
rows = list(csv.DictReader(open(path), delimiter="\t"))
ARMS = ("plain", "salt-diet")
roots = [want] if want else sorted({r["root"] for r in rows})

for root in roots:
    rr = [r for r in rows if r["root"] == root]
    arms_present = [a for a in ARMS if any(r["arm"] == a for r in rr)]
    print("=== %s (%d cells) ===" % (root, len(rr)))
    if not arms_present:
        print("  no plain/salt-diet cells\n"); continue
    for label, keep in (("STRICT", {"OK"}), ("FLOOR-INCLUSIVE", {"OK", "FLOOR"})):
        rates = {}
        for arm in arms_present:
            a = [r for r in rr if r["arm"] == arm]
            k = [r for r in a if r["status"] in keep]
            rates[arm] = 100.0 * len(k) / len(a) if a else 0
        gap = abs(rates[arms_present[0]] - rates[arms_present[-1]]) if len(arms_present) > 1 else 0
        print("  %-16s %s   arm gap %.0f pts %s" % (
            label,
            " ".join("%s=%d/%d" % (arm, len([r for r in rr if r["arm"] == arm and r["status"] in keep]),
                                   len([r for r in rr if r["arm"] == arm])) for arm in arms_present),
            gap, "NOT arm-neutral" if gap > 10 else "arm-neutral"))
    keep = {"OK", "FLOOR"}
    for arm in arms_present:
        a = [r for r in rr if r["arm"] == arm and r["status"] in keep]
        if not a: continue
        tT = sum(int(r["T"]) for r in a); tO = sum(int(r["output"]) for r in a)
        tc = sum(float(r["cost"]) for r in a)
        print("    %-10s n=%-3d $/M-T %6.3f   $/M-OUTPUT %7.2f   median $ %6.2f" %
              (arm, len(a), 1e6*tc/tT, 1e6*tc/tO, st.median(float(r["cost"]) for r in a)))
    print()
print("⛔ Roots are reported separately and never pooled: different waves, arms, dates and task sets.")
print("⛔ A FLOOR licenses a NUMBER, not a VERDICT.")
