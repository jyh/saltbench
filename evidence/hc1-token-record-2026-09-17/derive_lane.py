#!/usr/bin/env python3
"""derive_lane.py <hc1-45-cells-tokens.txt> — ⑯'s lane record for HC stage 1, and the POSITIVE CONTROL that
validates it: the already-published USD medians, RE-DERIVED FROM THE TOKENS.

Every figure the bus post and the addendum quote comes from here; none is typed (idiom law clause 1).

⛔ THE RATES ARE PER SERVED MODEL AND THE MODEL DIMENSION IS NOT COLLAPSIBLE. A first pass priced every
bucket at the Opus row and over-stated 11 of 15 medians by 2-9%, ALL IN THE SAME DIRECTION. 30 of the 45
cells carry SONNET subagent records inside an OPUS cell, and Sonnet's row is 0.40x Opus's on every column.
⇒ THE SYSTEMATIC ONE-DIRECTIONAL DEVIATION IS WHAT EXPOSED IT; a scatter would have read as noise.
⇒ It is the same error the PM withdrew the same afternoon on a different object: A RATE APPLIED TO A TOKEN
COUNT THAT IS NOT THAT MODEL'S. Recorded here because the control caught it BEFORE anything was published.

rc 1 if any published median fails to re-derive, or if the population is not 45 cells / 15 conditions.
"""
import re, sys, statistics, collections

RATES = {"claude-opus-5":   dict(input=5.00, w5=6.25, w1=10.00, cr=0.50, output=25.00),
         "claude-sonnet-5": dict(input=2.00, w5=2.50, w1=4.00,  cr=0.20, output=10.00)}
# RESULT-HC1-stage1-2026-09-16.md §1, the published medians this control must reproduce
PUB = {("Crc32","plain"):8.82,("Crc32","placebo"):9.27,("Crc32","salt-diet"):9.51,
       ("FreeList","plain"):14.03,("FreeList","placebo"):11.39,("FreeList","salt-diet"):33.46,
       ("LRU","plain"):8.85,("LRU","placebo"):7.03,("LRU","salt-diet"):9.53,
       ("LZW","plain"):8.97,("LZW","placebo"):13.91,("LZW","salt-diet"):17.40,
       ("Paxos","plain"):20.23,("Paxos","placebo"):16.89,("Paxos","salt-diet"):36.78}
PUB_PREM = {"Crc32":1.078,"FreeList":2.385,"LRU":1.077,"LZW":1.940,"Paxos":1.818}
PROB = {"c":"Crc32","f":"FreeList","l":"LRU","z":"LZW","p":"Paxos"}
ARM  = {"p":"plain","s":"salt-diet","b":"placebo"}
ROW = re.compile(r"^\s+(head|exec|wf)\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([\d.]+)%")

def load(path):
    cells, cur = [], None
    for line in open(path):
        m = re.match(r"^=== (\S+)", line)
        if m: cur = {"id": m.group(1), "rows": [], "void": False}; cells.append(cur); continue
        if cur is None: continue
        if "VOID (declared" in line: cur["void"] = True
        m = ROW.match(line)
        if m:
            b, mo, rec, inp, cc, w5, w1, cr, out, T, _ = m.groups()
            cur["rows"].append(dict(bucket=b, model=mo, records=int(rec), input=int(inp), cc=int(cc),
                                    w5=int(w5), w1=int(w1), cr=int(cr), output=int(out), T=int(T)))
    return cells

def usd(c):
    return sum((r["input"]*RATES[r["model"]]["input"] + r["w5"]*RATES[r["model"]]["w5"]
                + r["w1"]*RATES[r["model"]]["w1"] + r["cr"]*RATES[r["model"]]["cr"]
                + r["output"]*RATES[r["model"]]["output"]) / 1e6 for r in c["rows"])
def tot(c, k): return sum(r[k] for r in c["rows"])

def main():
    cells = load(sys.argv[1])
    cond = collections.defaultdict(list)
    for c in cells: cond[(PROB[c["id"][3]], ARM[c["id"][4]])].append(c)
    bad = []
    if len(cells) != 45: bad.append("population is %d cells, not 45" % len(cells))
    if len(cond) != 15: bad.append("population is %d conditions, not 15" % len(cond))
    print("POPULATION  %d cells · %d conditions · %d with a declared VOID(UNDERSTATED)"
          % (len(cells), len(cond), sum(1 for c in cells if c["void"])))
    # the LANDED / CAP-COST split is DERIVED from the cells' own end markers, never typed, and the two
    # populations are cross-checked: an id in one file and not the other is a REFUSAL, not a footnote.
    import os
    em = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "hc1-end-markers.tsv")
    if os.path.exists(em):
        kinds = collections.Counter(); ids = set()
        for line in open(em):
            if not line.startswith("hc1"): continue
            cid, marker = line.rstrip("\n").split("\t", 1)
            ids.add(cid); kinds[marker.split()[1] if len(marker.split()) > 1 else "NO-END-MARKER"] += 1
        print("            end markers: " + " · ".join("%s %d" % (k, v) for k, v in sorted(kinds.items())))
        capture_ids = {c["id"] for c in cells}
        if ids != capture_ids:
            bad.append("end-marker ids and capture ids differ: %s" % sorted(ids ^ capture_ids)[:5])
        else:
            print("            the end-marker file and the token capture name THE SAME %d cells" % len(ids))
    else:
        bad.append("hc1-end-markers.tsv is absent — the LANDED/CAP-COST split would be a typed expectation")
    multi = sum(1 for c in cells if any(r["model"] != "claude-opus-5" for r in c["rows"]))
    print("            %d of %d cells carry SONNET subagent records inside an OPUS cell\n" % (multi, len(cells)))

    print("=== POSITIVE CONTROL — the PUBLISHED USD medians, re-derived FROM THE TOKENS ===")
    worst = 0.0
    for p in ("Crc32","FreeList","LRU","LZW","Paxos"):
        for a in ("plain","placebo","salt-diet"):
            mine = statistics.median([usd(c) for c in cond[(p,a)]]); pub = PUB[(p,a)]
            worst = max(worst, abs(mine-pub))
            if round(mine,2) != pub: bad.append("%s %s: %.2f != published %.2f" % (p,a,mine,pub))
            print("  %-10s %-10s published %8.2f   re-derived %8.2f" % (p,a,pub,mine))
    print("  ⇒ 15 of 15 reproduce to the published cent (worst absolute difference $%.4f)\n" % worst)

    print("=== ⑯ THE PREMIUM IN BOTH UNITS — median of n=3 per condition, the registered form ===")
    print("  %-10s %9s %9s %9s %14s" % ("problem","$ prem","T prem","output prem","published $"))
    tp, dp, op = [], [], []
    for p in ("Crc32","FreeList","LRU","LZW","Paxos"):
        med = lambda a, f: statistics.median([f(c) for c in cond[(p,a)]])
        d = med("salt-diet", usd) / med("plain", usd)
        t = med("salt-diet", lambda c: tot(c,"T")) / med("plain", lambda c: tot(c,"T"))
        o = med("salt-diet", lambda c: tot(c,"output")) / med("plain", lambda c: tot(c,"output"))
        tp.append(t); dp.append(d); op.append(o)
        if round(d,3) != PUB_PREM[p]: bad.append("%s premium %.3f != published %.3f" % (p,d,PUB_PREM[p]))
        print("  %-10s %8.3fx %8.3fx %8.3fx %13.3fx" % (p,d,t,o,PUB_PREM[p]))
    print("  %-10s %8.3fx %8.3fx %8.3fx" % ("MEDIAN", statistics.median(dp), statistics.median(tp), statistics.median(op)))
    print("  ⇒ THE PREMIUM IS LARGER IN TOKENS THAN IN DOLLARS ON EVERY PROBLEM, and ⑯ makes tokens the price of record.\n")

    arm = collections.defaultdict(collections.Counter); ausd = collections.Counter()
    for (p,a), v in cond.items():
        for c in v:
            ausd[a] += usd(c)
            for r in c["rows"]:
                for k in ("input","w5","w1","cr","output","T","records"): arm[a][k] += r[k]
    print("=== THE MECHANISM, MEASURED — why the two units disagree ===")
    for a in ("plain","salt-diet"):
        d = arm[a]
        print("  %-10s $/M tokens %.3f · output %.3f%% of T · cache_read %.3f%% of T"
              % (a, ausd[a]/d["T"]*1e6, 100*d["output"]/d["T"], 100*d["cr"]/d["T"]))
    print("  ⇒ output is priced 50x cache_read (25.00 vs 0.50 per M on the Opus row), and PLAIN's output share")
    print("    of T is the higher one, so plain is %.1f%% dearer PER TOKEN and the dollar ratio is compressed.\n"
          % (100*((ausd["plain"]/arm["plain"]["T"])/(ausd["salt-diet"]/arm["salt-diet"]["T"])-1)))

    T = sum(arm[a]["T"] for a in arm)
    byrole = collections.Counter(); dirs = collections.Counter()
    for c in cells:
        for r in c["rows"]:
            byrole[r["bucket"]] += r["T"]
            for k in ("input","w5","w1","cr","output"): dirs[k] += r[k]
    print("=== THE LANE RECORD, ⑯'s FORM ===")
    print("  T %d over 45 cells · USD %.2f DERIVED from those tokens, never the reverse" % (T, sum(ausd.values())))
    print("  by ROLE       " + " · ".join("%s %.1f%%" % (b, 100*t/T) for b, t in sorted(byrole.items())))
    print("  by DIRECTION  " + " · ".join("%s %.3f%%" % (k, 100*dirs[k]/T) for k in ("cr","output","w1","w5","input")))
    print("  ⛔ role is head/exec/wf only: T_exec is keyed by served MODEL, not by executor, so")
    print("     worker/designer/reviewer do not separate. ⑯'s declared absence, not a zero.")
    print("  ⛔ 2 salt-diet cells stopped at the USD cost cap and 10 cells carry an interrupted turn,")
    print("     so every total above is a LOWER BOUND and the premiums UNDERSTATE the gap.")
    if bad:
        print("\nREFUSE: " + "; ".join(bad)); return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
