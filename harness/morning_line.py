#!/usr/bin/env python3
"""morning_line.py — the stage-0 report, computed the one pre-declared way (SCOUT-STAGE0 §7.6).
usage: morning_line.py <STATE dir> <scoring report json for a0> <for a1>"""
import glob, json, math, os, sys
st = sys.argv[1]; reps = {"a0": sys.argv[2], "a1": sys.argv[3]}
def resolved(path):
    r = json.load(open(path)); return set(r.get("resolved_ids", []))
man = [json.load(open(p)) for p in glob.glob(os.path.join(st, "*", "manifest.json"))]
def base(t): return t.split("+")[0]
scor = {}
for m in man:
    t = m["termination"]
    if base(t) in ("DONE", "ROUNDS_EXHAUSTED", "WALLCLOCK", "TOKEN_CEILING") and not t.startswith(("VOID", "HARNESS")):
        scor[(m["instance_id"], m["arm"])] = m
tasks = sorted({i for (i, _) in scor})
pairs = [i for i in tasks if (i, "a0") in scor and (i, "a1") in scor]
res = {a: resolved(reps[a]) for a in reps}
b = sum(1 for i in pairs if i in res["a0"] and i not in res["a1"]); c = sum(1 for i in pairs if i in res["a1"] and i not in res["a0"])
nd = b + c
def sign_null(nd, k):  # P(|b-c| >= k | identical arms) exact two-sided
    if nd == 0: return 1.0 if k == 0 else 0.0
    p = 0.0
    for x in range(nd + 1):
        if abs(2 * x - nd) >= k: p += math.comb(nd, x) / 2 ** nd
    return p
def pct(v, q):
    v = sorted(v); return v[min(len(v) - 1, int(math.ceil(q * len(v)) - 1))] if v else None
print("STAGE-0 MORNING LINE  pairs=%d (tasks with both arms scorable)" % len(pairs))
for a in ("a0", "a1"):
    ok = [m for (i, x), m in scor.items() if x == a and i in pairs]
    ms = [m["metered_sum_governing"] or m["metered_sum"] for m in ok if m.get("metered_sum")]
    print("  %s solved %d/%d  metered p50=%s p90=%s max=%s  terminations=%s" % (
        a, sum(1 for i in pairs if i in res[a]), len(pairs), pct(ms, .5), pct(ms, .9), max(ms) if ms else None,
        {t: sum(1 for m in ok if base(m["termination"]) == t) for t in set(base(m["termination"]) for m in ok)}))
print("  b(a0 only)=%d c(a1 only)=%d n_d=%d  |b-c|=%d  P(|b-c|>=%d | identical arms)=%.3f  %s" % (
    b, c, nd, abs(b - c), abs(b - c), sign_null(nd, abs(b - c)), "INDISTINGUISHABLE AT k=15 (|b-c|<5) — not narrated" if abs(b - c) < 5 else "reported with the null probability beside it"))
a0 = [m for (i, x), m in scor.items() if x == "a0" and base(m["termination"]) in ("DONE", "ROUNDS_EXHAUSTED")]
ms0 = [m["metered_sum_governing"] or m["metered_sum"] for m in a0 if m.get("metered_sum")]
cens = sum(1 for (i, x), m in scor.items() if x == "a0" and base(m["termination"]) in ("WALLCLOCK", "TOKEN_CEILING"))
print("  p90 the cap rule consumes (a0, DONE|ROUNDS_EXHAUSTED): %s over %d episodes; censored a0 rows excluded: %d" % (pct(ms0, .9), len(ms0), cens))
caps = {a: sum(1 for (i, x), m in scor.items() if x == a and base(m["termination"]) in ("ROUNDS_EXHAUSTED", "WALLCLOCK", "TOKEN_CEILING")) for a in ("a0", "a1")}
print("  cap-bound episodes a0=%d a1=%d  %s" % (caps["a0"], caps["a1"], "CAP-CONFOUNDED (differ by >=2)" if abs(caps["a0"] - caps["a1"]) >= 2 else ""))
removed = [m for m in man if (m["instance_id"], m["arm"]) not in scor and m["termination"] not in ("DRY", "SMOKE")]
print("  removed rows (VOID/QUOTA/ERROR/HARNESS_ERROR): %d  %s" % (len(removed), [(m["instance_id"], m["arm"], m["termination"]) for m in removed]))
print("  url mentions / blocked escapes per arm: %s" % {a: (sum((json.load(open(os.path.join(st, m["episode"], "meter.json"))).get("url_mentions", 0)) for (i, x), m in scor.items() if x == a and os.path.exists(os.path.join(st, m["episode"], "meter.json")))) for a in ("a0", "a1")})
print("  no p-value, by design; no task-arm repeated, so sampling variance and arm effect are not separated at stage 0.")
