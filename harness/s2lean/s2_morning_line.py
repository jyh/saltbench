#!/usr/bin/env python3
"""s2_morning_line.py — the S2-Lean stage-0 report, computed the one pre-declared way (SCOUT-S2LEAN-STAGE0 §7).
usage: s2_morning_line.py <STATE dir> <k>   (reads every manifest with substrate S2-Lean/CLEVER)"""
import collections, glob, json, math, os, sys
st, k = sys.argv[1], int(sys.argv[2])
man = sorted([json.load(open(p)) for p in glob.glob(os.path.join(st, "*", "manifest.json"))], key=lambda m: m.get("end_utc") or 0)
man = [m for m in man if m.get("substrate") == "S2-Lean/CLEVER" and m["arm"] in ("a0", "a1") and not m["termination"].startswith(("SMOKE", "DRY"))]
def base(t): return t.split("+")[0]
scor = {}
for m in man:
    if base(m["termination"]) in ("DONE", "ROUNDS_EXHAUSTED", "WALLCLOCK", "TOKEN_CEILING"):
        scor[(m["instance_id"], m["stage"], m["arm"])] = m   # latest by end_utc wins
tasks = sorted({i for (i, _, _) in scor})
def pct(v, q):
    v = sorted(v); return v[min(len(v) - 1, int(math.ceil(q * len(v)) - 1))] if v else None
def sign_null(nd, d):
    if nd == 0: return 1.0 if d == 0 else 0.0
    return sum(math.comb(nd, x) for x in range(nd + 1) if abs(2 * x - nd) >= d) / 2 ** nd
print("S2-LEAN STAGE-0 MORNING LINE  k=%d  tasks with any landing=%d  constants=%s" % (k, len(tasks), sorted({(m["max_turns"], m["wall_ceiling_s"], m["token_ceiling"], m["model_requested"], m["effort"]) for m in man})))
for stage, label in (("A", "spec compiles"), ("B", "ISOMORPHISM PROVEN (the F3 quantity)"), ("C", "impl + correctness proven")):
    pairs = [i for i in tasks if (i, stage, "a0") in scor and (i, stage, "a1") in scor]
    for a in ("a0", "a1"):
        rows = [scor[(i, stage, a)] for i in tasks if (i, stage, a) in scor]
        ok = [m for m in rows if m.get("passed")]
        ms = [m["metered_sum_governing"] or m["metered_sum"] for m in rows if m.get("metered_sum")]
        print("  stage %s %s: %s passed %d/%d (of k=%d: %.0f%%)  metered p50=%s p90=%s max=%s  terms=%s" % (stage, label, a, len(ok), len(rows), k, 100.0 * len(ok) / k if k else 0, pct(ms, .5), pct(ms, .9), max(ms) if ms else None, dict(collections.Counter(base(m["termination"]) for m in rows))))
    if pairs:
        b = sum(1 for i in pairs if scor[(i, stage, "a0")].get("passed") and not scor[(i, stage, "a1")].get("passed")); c = sum(1 for i in pairs if scor[(i, stage, "a1")].get("passed") and not scor[(i, stage, "a0")].get("passed"))
        print("     pairs=%d  b(a0 only)=%d c(a1 only)=%d n_d=%d |b-c|=%d P(|b-c|>=%d | identical)=%.3f %s" % (len(pairs), b, c, b + c, abs(b - c), abs(b - c), sign_null(b + c, abs(b - c)), "INDISTINGUISHABLE (|b-c| < 5)" if abs(b - c) < 5 else "reported with the null probability beside it"))
# the F3 reading on the PLAIN arm, stage B, over the k drawn problems (an unrun problem counts as not proven)
b_ok = sum(1 for i in tasks if (i, "B", "a0") in scor and scor[(i, "B", "a0")].get("passed")); rate = b_ok / k if k else 0
print("  F3 (plain arm, isomorphism proven over k=%d): %d/%d = %.1f%% ⇒ %s" % (k, b_ok, k, 100 * rate, "HOLD (≥80%: too easy at this tier)" if rate >= 0.8 else ("HOLD (<20%: a floor, not a reason to add arms)" if rate < 0.2 else "RUN THE SALT ARM (20–80%)")))
a0B = [m for (i, s, a), m in scor.items() if s == "B" and a == "a0" and base(m["termination"]) in ("DONE", "ROUNDS_EXHAUSTED")]
ms0 = [m["metered_sum_governing"] or m["metered_sum"] for m in a0B if m.get("metered_sum")]
print("  p90 the cap rule consumes (a0, stage B, DONE|ROUNDS_EXHAUSTED): %s over %d episodes" % (pct(ms0, .9), len(ms0)))
removed = [m for m in man if m["episode"] not in {x["episode"] for x in scor.values()}]
print("  removed rows: %d %s" % (len(removed), [(m["instance_id"], m["stage"], m["arm"], m["termination"]) for m in removed]))
print("  axiom failures (compiled, no sorry, but axioms outside the allowlist): %s" % [(m["instance_id"], m["stage"], m["arm"], (m.get("check") or {}).get("axioms")) for m in scor.values() if (m.get("check") or {}).get("compiled") and not (m.get("check") or {}).get("sorry_lines") and (m.get("check") or {}).get("axioms_ok") is False])
print("  no p-value, by design.")
