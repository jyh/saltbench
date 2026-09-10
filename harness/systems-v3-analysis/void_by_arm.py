import csv, sys
rows = [r for r in csv.DictReader(open(sys.argv[1]), delimiter="\t") if r["root"] == "cells-matrix1"]
print("WHY CELLS ARE NOT PRICED, BY ARM  (an exclusion that is not arm-neutral biases the table)")
print("  %-10s %5s %5s %9s %9s %9s" % ("arm", "total", "OK", "VOID", "NO-TRANS", "OK-rate"))
for arm in ("plain", "salt-diet"):
    a = [r for r in rows if r["arm"] == arm]
    ok = [r for r in a if r["status"] == "OK"]
    vd = [r for r in a if r["status"].startswith("VOID")]
    nt = [r for r in a if r["status"] == "NO-TRANSCRIPT"]
    print("  %-10s %5d %5d %9d %9d %8.0f%%" % (arm, len(a), len(ok), len(vd), len(nt),
                                               100.0 * len(ok) / len(a)))
print()
print("THE VOID REASON, VERBATIM, counted:")
c = {}
for r in rows:
    if r["status"].startswith("VOID"):
        c[r["status"]] = c.get(r["status"], 0) + 1
for k, v in sorted(c.items(), key=lambda x: -x[1]):
    print("  %2d  %s" % (v, k))
