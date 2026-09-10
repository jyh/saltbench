"""agg.py — the token figures beside the dollar figure, strict and floor-inclusive.

⛔ THE EXCLUSION-NEUTRALITY CHECK RUNS FIRST, BEFORE ANY AGGREGATE. An exclusion that is not
arm-neutral makes every by-arm number below a comparison of two differently-selected subsets, and
that has to be visible before the numbers are, not in a footnote after them.
"""
import csv, sys, statistics as st

rows = [r for r in csv.DictReader(open(sys.argv[1]), delimiter="\t")
        if r["root"] == "cells-matrix1"]
ARMS = ("plain", "salt-diet")

def show_balance(label, keep):
    print(label)
    print("  %-10s %6s %8s %9s" % ("arm", "total", "included", "rate"))
    rates = {}
    for arm in ARMS:
        a = [r for r in rows if r["arm"] == arm]
        k = [r for r in a if r["status"] in keep]
        rates[arm] = 100.0 * len(k) / len(a) if a else 0
        print("  %-10s %6d %8d %8.0f%%" % (arm, len(a), len(k), rates[arm]))
    gap = abs(rates[ARMS[0]] - rates[ARMS[1]])
    print("  ⇒ arm gap %.0f points — %s\n" % (
        gap, "NOT arm-neutral; the by-arm rows below are NOT an arm comparison"
             if gap > 10 else "arm-neutral within 10 points"))
    return gap

def table(label, keep):
    print(label)
    print("  %-10s %3s %10s %13s %12s %13s %9s" %
          ("arm", "n", "output", "cache_read", "cache_write", "T", "$"))
    for arm in ARMS:
        a = [r for r in rows if r["arm"] == arm and r["status"] in keep]
        if not a: continue
        med = lambda k: st.median(int(r[k]) for r in a)
        cw = st.median(int(r["cache_write_5m"]) + int(r["cache_write_1h"]) for r in a)
        print("  %-10s %3d %10d %13d %12d %13d %9.2f" %
              (arm, len(a), med("output"), med("cache_read"), cw, med("T"),
               st.median(float(r["cost"]) for r in a)))
    print()
    for arm in ARMS:
        a = [r for r in rows if r["arm"] == arm and r["status"] in keep]
        if not a: continue
        tT = sum(int(r["T"]) for r in a); tO = sum(int(r["output"]) for r in a)
        tc = sum(float(r["cost"]) for r in a)
        print("  %-10s $/million-T %6.3f    $/million-OUTPUT %7.2f" % (arm, 1e6*tc/tT, 1e6*tc/tO))
    print()

g1 = show_balance("① STRICT — priced cells only (a VOID cell is dropped)", {"OK"})
table("   medians per cell", {"OK"})
g2 = show_balance("② FLOOR-INCLUSIVE — a VOID(UNDERSTATED) cell is RETAINED as a LOWER BOUND",
                  {"OK", "FLOOR"})
table("   medians per cell (every figure a FLOOR where the cell is)", {"OK", "FLOOR"})
print("⇒ retaining the floors moves the arm gap from %.0f points to %.0f." % (g1, g2))
print("⛔ A FLOOR LICENSES A NUMBER, NOT A VERDICT: the understatement is unbounded on the one")
print("   interrupted record per cell, and it falls more often on the control arm.")
