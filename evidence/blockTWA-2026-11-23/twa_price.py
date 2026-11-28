#!/usr/bin/env python3
"""twa_price.py — block TWA's price, in cell wall (the agy lane's binding resource), from tracked files only.

Inputs (each a tracked file of this repo):
  WAF  evidence/blockWA-2026-11-14/cells.tsv                           WA Flash's 12 cells (WHT, NTT; extras none)
  WAP  evidence/blockWA-pro-2026-11-15/cells.tsv                       WA Pro's 12 cells (gemini-4-argon-high; extras none)
  NA   harness/systems-v3/RESULT-gemini-blockNA-2026-09-28-cells.tsv   block NA's agy cells on the six (extras none)
  TA   evidence/blockTA-result-2026-11-20/cells.tsv                    block TA's 72 cells on the six (extras statement)

Method (registered in the TWA amendment §TWA3):
  Base, per model x problem x arm: 3 x WA's own median wall for WHT/NTT at that model and arm (extras none).
  Statement ratio, per arm: TA Flash's summed wall on the six / NA Flash's summed wall on the six (cells in NA's registered n),
  the same model on the same six problems, extras statement over extras none. No argon cell has run on the six with extras none
  (NA's Pro cells were gemini-3.1-pro-high), so the Flash ratio is applied to argon too: a DECLARED substitution.
  Price = base x ratio. Every figure printed is computed here; nothing is typed.
"""
import csv, os, statistics, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WAF = os.path.join(ROOT, "evidence/blockWA-2026-11-14/cells.tsv")
WAP = os.path.join(ROOT, "evidence/blockWA-pro-2026-11-15/cells.tsv")
NA = os.path.join(ROOT, "harness/systems-v3/RESULT-gemini-blockNA-2026-09-28-cells.tsv")
TA = os.path.join(ROOT, "evidence/blockTA-result-2026-11-20/cells.tsv")
SIX = ["Luby", "AES", "Liveness", "MaxFlow", "BinomialHeap", "LinearScan"]
TWO = ["WHT", "NTT"]
ARMS = ["plain", "salt-diet"]
FLASH, ARGON = "gemini-3.8-flash-high", "gemini-4-argon-high"


def rows(p):
    with open(p, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    wa = {FLASH: [r for r in rows(WAF) if r["requested_model"] == FLASH],
          ARGON: [r for r in rows(WAP) if r["requested_model"] == ARGON]}
    na = [r for r in rows(NA) if r["served"] == FLASH and r.get("in_registered_n", "yes") == "yes"]
    ta = [r for r in rows(TA) if r["requested_model"] == FLASH]
    for name, v in (("WA flash", wa[FLASH]), ("WA argon", wa[ARGON]), ("NA flash", na), ("TA flash", ta)):
        if not v:
            sys.exit(f"REFUSE: input {name} is empty")
    ratio = {}
    for a in ARMS:
        n = [float(r["wall_s"]) for r in na if r["arm"] == a and r["problem"] in SIX]
        t = [float(r["wall_seconds"]) for r in ta if r["arm"] == a and r["problem"] in SIX]
        if len(n) != 18 or len(t) != 18:
            sys.exit(f"REFUSE: arm {a}: NA flash cells {len(n)}, TA flash cells {len(t)}; 18 each expected")
        ratio[a] = sum(t) / sum(n)
        print(f"ratio {a}: TA flash six 18 cells {sum(t):.0f} s / NA flash six 18 cells {sum(n):.0f} s = {ratio[a]:.3f}")
    total = {FLASH: 0.0, ARGON: 0.0}
    unscaled = 0.0
    for m in (FLASH, ARGON):
        for P in TWO:
            for a in ARMS:
                w = [float(r["wall_seconds"]) for r in wa[m] if r["problem"] == P and r["arm"] == a]
                if len(w) != 3:
                    sys.exit(f"REFUSE: WA {m} {P} {a}: {len(w)} cells, 3 expected")
                med = statistics.median(w)
                price = 3 * med * ratio[a]
                total[m] += price
                unscaled += 3 * med
                print(f"{m} {P} {a}: WA n 3 median wall {med:.1f} s -> 3 x {med:.1f} x {ratio[a]:.3f} = {price:.0f} s")
    for m in (FLASH, ARGON):
        print(f"{m} price, 12 cells: {total[m]:.0f} s = {total[m]/3600:.1f} h")
    s = total[FLASH] + total[ARGON]
    print(f"TWA price, 24 cells: {s:.0f} s = {s/3600:.1f} h of cell wall; agy pool points per cell UNMEASURED")
    print(f"sensitivity, ratio 1 (WA's extras-none walls unscaled): {unscaled:.0f} s = {unscaled/3600:.1f} h")


if __name__ == "__main__":
    main()
