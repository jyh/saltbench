import csv, sys, statistics as st
rows = list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
m1 = [r for r in rows if r["root"] == "cells-matrix1"]
ok = [r for r in m1 if r["status"] == "OK"]
print("POPULATION (cells-matrix1, the phase-1 greenfield landings)")
print("  cells total        %d" % len(m1))
by_status = {}
for r in m1:
    k = r["status"].split(":")[0]
    by_status[k] = by_status.get(k, 0) + 1
for k, v in sorted(by_status.items()):
    print("  %-18s %d" % (k, v))
print()
print("⛔ IS THE EXCLUSION ARM-NEUTRAL?  (a non-neutral exclusion biases the comparison)")
for arm in ("plain", "salt-diet"):
    a = [r for r in m1 if r["arm"] == arm]
    o = [r for r in a if r["status"] == "OK"]
    print("  %-10s %d of %d measurable (%.0f%%)" % (arm, len(o), len(a), 100.0*len(o)/len(a)))
print()
hdr = ("arm", "n", "output", "cache_read", "input", "cache_write", "T", "$")
print("MEDIAN PER CELL — the token figures beside the dollar figure")
print("  %-10s %3s %10s %13s %8s %12s %13s %8s" % hdr)
for arm in ("plain", "salt-diet"):
    a = [r for r in ok if r["arm"] == arm]
    if not a: continue
    def med(k): return st.median(int(r[k]) for r in a)
    cw = st.median(int(r["cache_write_5m"]) + int(r["cache_write_1h"]) for r in a)
    print("  %-10s %3d %10d %13d %8d %12d %13d %8.2f" % (
        arm, len(a), med("output"), med("cache_read"), med("input"), cw,
        med("T"), st.median(float(r["cost"]) for r in a)))
print()
print("SUM OVER THE MEASURABLE POPULATION")
tot = {k: sum(int(r[k]) for r in ok) for k in ("input","cache_write_5m","cache_write_1h","cache_read","output","T")}
cost = sum(float(r["cost"]) for r in ok)
for k in ("input","cache_write_5m","cache_write_1h","cache_read","output","T"):
    print("  %-16s %14d   %5.2f%% of T" % (k, tot[k], 100.0*tot[k]/tot["T"]))
print("  %-16s %14.2f" % ("cost_usd", cost))
print()
print("⇒ cache_read is %.1f%% of T; output is %.2f%% of T." % (
    100.0*tot["cache_read"]/tot["T"], 100.0*tot["output"]/tot["T"]))
print("⇒ cost per million T: $%.3f  |  cost per million OUTPUT tokens: $%.2f" % (
    1e6*cost/tot["T"], 1e6*cost/tot["output"]))
for arm in ("plain", "salt-diet"):
    a = [r for r in ok if r["arm"] == arm]
    tT = sum(int(r["T"]) for r in a); tO = sum(int(r["output"]) for r in a)
    tc = sum(float(r["cost"]) for r in a)
    print("   %-10s $/MT %.3f   $/M-output %.2f   (cost per T is ARM-DEPENDENT)" % (
        arm, 1e6*tc/tT, 1e6*tc/tO))
