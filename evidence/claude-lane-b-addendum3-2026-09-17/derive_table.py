#!/usr/bin/env python3
"""derive_table.py <hc1-lru-plain-token-table.txt> — every figure ADDENDUM 3 §A3.5 quotes, derived from the
capture's own bytes (idiom law clause 1: a hand-typed expected value is correct-not-verified). Prints the
per-cell RECEIPT rows it parsed, the T band, and the exec output-per-record signal. rc 1 if the parse finds
fewer than 3 cells or a cell with no head RECEIPT row — an absence is never silently a smaller n."""
import re, sys
txt = open(sys.argv[1]).read()
cells, cur = [], None
for line in txt.splitlines():
    m = re.match(r"===== CELL (\S+)", line)
    if m:
        cur = {"id": m.group(1), "rows": [], "lower_bound": False}; cells.append(cur); continue
    if cur is None: continue
    if "VOID(UNDERSTATED)" in line: cur["lower_bound"] = True
    m = re.match(r"^T_head (\d+)\s+T_exec (.*?)\s+T_wf (\d+)\s+T (\d+)$", line)
    if m: cur["T_head"], cur["T"] = int(m.group(1)), int(m.group(4))
    m = re.match(r"^RECEIPT (head|exec) (\S+) records (\d+) input (\d+) cache_creation (\d+) \((\d+)/(\d+)\) cache_read (\d+) output (\d+) T (\d+)", line)
    if m:
        cur["rows"].append({"bucket": m.group(1), "model": m.group(2), "records": int(m.group(3)),
                            "input": int(m.group(4)), "cc": int(m.group(5)), "cr": int(m.group(8)),
                            "output": int(m.group(9)), "T": int(m.group(10))})
bad = [c["id"] for c in cells if not any(r["bucket"] == "head" for r in c["rows"])]
print("cells parsed: %d  %s" % (len(cells), " ".join(c["id"] for c in cells)))
print()
print("PER CELL (ARM B, the cfg the cell records) — T by bucket, and the head's direction split")
for c in cells:
    h = [r for r in c["rows"] if r["bucket"] == "head"][0]
    print("  %s  T %s%s  T_head %s (%.0f%% of T)  head: cache_read %.2f%% · output %.2f%% · input %.4f%% · cache_creation %.2f%%" % (
        c["id"], f"{c['T']:,}", "  ⛔ LOWER BOUND (interrupted turn)" if c["lower_bound"] else "",
        f"{h['T']:,}", 100.0*h["T"]/c["T"], 100.0*h["cr"]/h["T"], 100.0*h["output"]/h["T"],
        100.0*h["input"]/h["T"], 100.0*h["cc"]/h["T"]))
print()
Ts = sorted((c["T"], c["id"], c["lower_bound"]) for c in cells)
lo, mid, hi = Ts
if mid[2] or lo[2]:
    print("MEDIAN T: a BAND, not a number — %s carries an interrupted turn, so its T is a LOWER BOUND and its rank is undetermined." % lo[1])
    print("  the median lies in [%s , %s]  (it is %s if the bounded cell stays below it, and at most %s)" % (
        f"{mid[0]:,}", f"{hi[0]:,}", f"{mid[0]:,}", f"{hi[0]:,}"))
else:
    print("MEDIAN T: %s (%s) — all three clean" % (f"{mid[0]:,}", mid[1]))
print()
print("THE EXEC SIGNAL — output tokens PER RECORD, same cell, same bucket, two models (UNCONTROLLED: different work)")
for c in cells:
    e = {r["model"]: r for r in c["rows"] if r["bucket"] == "exec"}
    if "claude-opus-5" in e and "claude-sonnet-5" in e:
        o, s = e["claude-opus-5"], e["claude-sonnet-5"]
        print("  %s  opus %6.0f/rec (%d rec)   sonnet %6.0f/rec (%d rec)   ratio %.2fx" % (
            c["id"], o["output"]/o["records"], o["records"], s["output"]/s["records"], s["records"],
            (s["output"]/s["records"])/(o["output"]/o["records"])))
if bad or len(cells) < 3:
    print("REFUSE: %d cell(s) with no head RECEIPT row: %s" % (len(bad), bad)); sys.exit(1)
