#!/usr/bin/env python3
"""ta_price.py — block TA's price, in cell wall (the agy lane's binding resource), from tracked files only.

Inputs (each a tracked file of this repo):
  NA   harness/systems-v3/RESULT-gemini-blockNA-2026-09-28-cells.tsv   block NA's agy cells on the six (extras none)
  WAF  evidence/blockWA-2026-11-14/cells.tsv                           WA Flash's 12 cells (WHT, NTT)
  WAP  evidence/blockWA-pro-2026-11-15/cells.tsv                       WA Pro's cells (gemini-4-argon-high)

Method (registered in the TA amendment §TA3):
  Flash, per problem x arm: 3 x NA's Flash median wall for that problem and arm (cells in the registered n only).
  Argon, per problem x arm: the Flash figure x WA's argon/Flash median-wall ratio for that ARM (WHT and NTT pooled), because no argon
  cell has run on the six; NA's Pro cells were gemini-3.1-pro-high, a different model (WA ADDENDUM 2's seam), and are not used.
Every figure printed is computed here; nothing is typed.
"""
import csv, os, statistics, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
NA = os.path.join(ROOT, "harness/systems-v3/RESULT-gemini-blockNA-2026-09-28-cells.tsv")
WAF = os.path.join(ROOT, "evidence/blockWA-2026-11-14/cells.tsv")
WAP = os.path.join(ROOT, "evidence/blockWA-pro-2026-11-15/cells.tsv")
SIX = ["Luby", "AES", "Liveness", "MaxFlow", "BinomialHeap", "LinearScan"]
ARMS = ["plain", "salt-diet"]
FLASH, ARGON = "gemini-3.8-flash-high", "gemini-4-argon-high"


def rows(p):
    with open(p, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    na = [r for r in rows(NA) if r["served"] == FLASH and r.get("in_registered_n", "yes") == "yes"]
    waf = [r for r in rows(WAF) if r["requested_model"] == FLASH]
    wap = [r for r in rows(WAP) if r["requested_model"] == ARGON]
    if not na or not waf or not wap:
        sys.exit(f"REFUSE: an input is empty (NA flash {len(na)}, WA flash {len(waf)}, WA argon {len(wap)})")
    ratio = {}
    for a in ARMS:
        f = [float(r["wall_seconds"]) for r in waf if r["arm"] == a]
        p = [float(r["wall_seconds"]) for r in wap if r["arm"] == a]
        if not f or not p:
            sys.exit(f"REFUSE: no WA wall for arm {a} (flash {len(f)}, argon {len(p)})")
        ratio[a] = statistics.median(p) / statistics.median(f)
        print(f"WA {a}: argon n {len(p)} median wall {statistics.median(p):.1f} s · flash n {len(f)} median {statistics.median(f):.1f} s · ratio {ratio[a]:.3f}")
    tf = ta = 0.0
    per = {}
    for P in SIX:
        for a in ARMS:
            w = [float(r["wall_s"]) for r in na if r["problem"] == P and r["arm"] == a]
            if not w:
                print(f"NA {P} {a}: NO FLASH CELL in the registered n — this condition is UNPRICED")
                continue
            m = statistics.median(w)
            f3, p3 = 3 * m, 3 * m * ratio[a]
            tf += f3; ta += p3; per[(P, a)] = f3 + p3
            print(f"NA {P} {a}: flash n {len(w)} median wall {m:.1f} s · Flash price 3 x {m:.1f} = {f3:.0f} s · argon price 3 x {m:.1f} x {ratio[a]:.3f} = {p3:.0f} s")
    print(f"Flash price, 36 cells: {tf:.0f} s = {tf/3600:.1f} h")
    print(f"argon price, 36 cells: {ta:.0f} s = {ta/3600:.1f} h")
    print(f"TA price, 72 cells: {tf+ta:.0f} s = {(tf+ta)/3600:.1f} h of cell wall; agy pool points per cell UNMEASURED")
    big = max(per, key=per.get)
    print(f"largest condition pair: {big[0]} {big[1]} {per[big]:.0f} s = {100*per[big]/(tf+ta):.0f} % of the price")


if __name__ == "__main__":
    main()
