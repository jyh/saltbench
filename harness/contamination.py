#!/usr/bin/env python3
"""contamination.py — PRE-REG §5's contamination proxy, run ON THE SEAT (gold never nears the agent host).
The instrument, the cut and the reading rule are STATED in SCOUT-STAGE0.md addendum 6 and committed BEFORE
this script is run on the stage-0 archive. This file is the normative form of that statement.

  usage: contamination.py <verified.json> <archive state dir> <stage0-a0 report> <stage0-a1 report> [--cut 0.80]

PRIMARY instrument (per task, per arm; a0 is the control of record, a1 is reported beside it):
  C(P) := for a patch P, the sequence of changed lines ('+'/'-' lines, excluding the '+++'/'---' file
          headers), sign kept, trailing whitespace stripped, runs of blanks collapsed, joined by '\n' —
          RESTRICTED to the files the GOLD patch touches (an agent's scratch files are not the fix).
  sim   := 1 - Levenshtein(C(A), C(G)) / max(|C(A)|, |C(G)|)  (character level); sim = 0 if the agent
          touched none of gold's files.
  exact := the multiset of changed lines of A (gold-file-restricted) equals gold's.
  CUT   := HIGH iff sim >= 0.80 (stated before computing).
SECONDARY (reported, not read): the same sim over the UNRESTRICTED agent patch; the number of gold lines.
NAMED CONFOUND: a forced minimal fix is similar to gold whether or not the model has seen it; tasks whose
  gold changes <= 4 lines are flagged small-fix and the reading is also given without them.
READING RULE (stated before computing), over RESOLVED a0 tasks: f_high = fraction in the HIGH stratum.
  f_high >= 2/3  => CONTAMINATION-CONSISTENT (memorisation and forced fixes are not separable by this
                    instrument; the honest next substrate is S2-Lean, where the kernel decides)
  f_high <= 1/3  => CAPABILITY-CONSISTENT
  otherwise      => INDETERMINATE, reported as such.
"""
import json, os, re, sys, glob

def files_of(p):
    return set(re.findall(r"^diff --git a/(\S+) b/", p, flags=re.M))

def changed_lines(p, only_files=None):
    out, cur = [], None
    for line in p.splitlines():
        m = re.match(r"^diff --git a/(\S+) b/", line)
        if m:
            cur = m.group(1); continue
        if only_files is not None and cur not in only_files:
            continue
        if (line.startswith("+") or line.startswith("-")) and not line.startswith(("+++", "---")):
            out.append(re.sub(r"[ \t]+", " ", line.rstrip()))
    return out

def lev(a, b):
    if a == b: return 0
    if not a: return len(b)
    if not b: return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

def sim(a_lines, g_lines):
    A, G = "\n".join(a_lines), "\n".join(g_lines)
    if not A and not G: return 1.0
    if not A or not G: return 0.0
    return 1.0 - lev(A, G) / max(len(A), len(G))

def main():
    verified, st, ra0, ra1 = sys.argv[1:5]
    cut = float(sys.argv[sys.argv.index("--cut") + 1]) if "--cut" in sys.argv else 0.80
    rows = {r["instance_id"]: r for r in json.load(open(verified))}
    res = {"a0": set(json.load(open(ra0))["resolved_ids"]), "a1": set(json.load(open(ra1))["resolved_ids"])}
    mans = [json.load(open(p)) for p in glob.glob(os.path.join(st, "*", "manifest.json"))]
    latest = {}
    for m in sorted(mans, key=lambda m: m.get("end_utc") or 0):
        if m["arm"] in ("a0", "a1") and not m["termination"].startswith(("SMOKE", "DRY")):
            latest[(m["instance_id"], m["arm"])] = m
    table = []
    for (iid, arm), m in sorted(latest.items()):
        G = rows[iid]["patch"]; gf = files_of(G); gl = changed_lines(G, gf)
        try: A = open(os.path.join(st, m["episode"], "model_patch.diff"), "rb").read().decode("utf-8", errors="replace")
        except Exception: A = ""
        al = changed_lines(A, gf); alu = changed_lines(A)
        s = sim(al, gl); su = sim(alu, gl)
        table.append({"instance_id": iid, "arm": arm, "sim": round(s, 3), "sim_unrestricted": round(su, 3),
                      "exact": sorted(al) == sorted(gl), "stratum": "HIGH" if s >= cut else "LOW",
                      "gold_lines": len(gl), "agent_lines_in_gold_files": len(al), "agent_lines_total": len(alu),
                      "agent_files": len(files_of(A)), "gold_files": len(gf), "small_fix": len(gl) <= 4,
                      "resolved": iid in res[arm], "termination": m["termination"]})
    print("CONTAMINATION PROXY — cut HIGH >= %.2f (stated before computing); primary = a0" % cut)
    print("%-36s %-3s %5s %6s %5s %-4s %4s %4s %4s %-6s %s" % ("task", "arm", "sim", "unrest", "exact", "str", "gold", "agnt", "tot", "small", "resolved/term"))
    for t in table:
        print("%-36s %-3s %5.3f %6.3f %5s %-4s %4d %4d %4d %-6s %s/%s" % (t["instance_id"], t["arm"], t["sim"], t["sim_unrestricted"], t["exact"], t["stratum"], t["gold_lines"], t["agent_lines_in_gold_files"], t["agent_lines_total"], t["small_fix"], "✅" if t["resolved"] else "❌", t["termination"]))
    for arm in ("a0", "a1"):
        rs = [t for t in table if t["arm"] == arm and t["resolved"]]
        hi = [t for t in rs if t["stratum"] == "HIGH"]; ex = [t for t in rs if t["exact"]]
        big = [t for t in rs if not t["small_fix"]]; hib = [t for t in big if t["stratum"] == "HIGH"]
        f = len(hi) / len(rs) if rs else float("nan")
        read = "CONTAMINATION-CONSISTENT" if f >= 2/3 else ("CAPABILITY-CONSISTENT" if f <= 1/3 else "INDETERMINATE")
        sims = sorted(t["sim"] for t in table if t["arm"] == arm)
        print("%s: resolved %d; HIGH among resolved %d (f_high=%.2f) => %s%s; exact-match %d; excluding small-fix tasks: %d/%d HIGH; sim distribution (all 15): min %.3f p50 %.3f max %.3f" % (
            arm, len(rs), len(hi), f, read, " [PRIMARY]" if arm == "a0" else "", len(ex), len(hib), len(big), sims[0], sims[len(sims)//2], sims[-1]))
    json.dump(table, open(os.path.join(st, "..", "contamination.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
