#!/usr/bin/env python3
"""morning_line.py — the stage-0 report, computed the one pre-declared way (SCOUT-STAGE0 §7.6).
usage: morning_line.py <STATE dir> <scoring report json for a0> <for a1>"""
import collections, glob, json, math, os, sys
st = sys.argv[1]; reps = {"a0": sys.argv[2], "a1": sys.argv[3]}
def resolved(path):
    r = json.load(open(path)); return set(r.get("resolved_ids", []))
man = sorted([json.load(open(p)) for p in glob.glob(os.path.join(st, "*", "manifest.json"))], key=lambda m: (m.get("end_utc") or 0))
man = [m for m in man if m["arm"] in ("a0", "a1") and not m["termination"].startswith(("SMOKE", "DRY"))]
excl_ids = set()
if os.path.exists(os.path.join(st, "controls.json")):
    excl_ids = {r["instance_id"] for r in json.load(open(os.path.join(st, "controls.json"))) if r.get("excluded")}
man = [m for m in man if m["instance_id"] not in excl_ids]
consts = {(m["max_turns"], m["wall_ceiling_s"], m["token_ceiling"], m["model_requested"], m["effort"]) for m in man}
def base(t): return t.split("+")[0]
scor = {}
for m in man:
    t = m["termination"]
    if base(t) in ("DONE", "ROUNDS_EXHAUSTED", "WALLCLOCK", "TOKEN_CEILING"):
        scor[(m["instance_id"], m["arm"])] = m   # latest terminal wins (sorted glob = episode-id order; duplicates reported below)
dups = collections.Counter((m["instance_id"], m["arm"]) for m in man if base(m["termination"]) in ("DONE", "ROUNDS_EXHAUSTED", "WALLCLOCK", "TOKEN_CEILING"))
dups = {k: v for k, v in dups.items() if v > 1}
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
print("STAGE-0 MORNING LINE  pairs=%d (tasks with both arms scorable)  excluded_by_controls=%d  constants=%s%s" % (len(pairs), len(excl_ids), sorted(consts), "" if len(consts) == 1 else "  ⛔ MIXED CONSTANTS ACROSS EPISODES"))
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
caps = {a: sum(1 for (i, x), m in scor.items() if x == a and i in pairs and base(m["termination"]) in ("ROUNDS_EXHAUSTED", "WALLCLOCK", "TOKEN_CEILING")) for a in ("a0", "a1")}
print("  cap-bound episodes a0=%d a1=%d  %s" % (caps["a0"], caps["a1"], "CAP-CONFOUNDED (differ by >=2)" if abs(caps["a0"] - caps["a1"]) >= 2 else ""))
kept_eps = {m["episode"] for m in scor.values()}
removed = [m for m in man if m["episode"] not in kept_eps]   # by identity, so a held/retried cell's earlier landings stay visible (refuter F7)
print("  removed rows (VOID/QUOTA/ERROR/HARNESS_ERROR): %d  %s" % (len(removed), [(m["instance_id"], m["arm"], m["termination"]) for m in removed]))
def mj(m):
    try: return json.load(open(os.path.join(st, m["episode"], "meter.json")))
    except Exception: return {}
for a in ("a0", "a1"):
    ms = [mj(m) for (i, x), m in scor.items() if x == a]
    print("  %s url_mentions=%d blocked_escapes=%d tool_timeouts=%d compactions=%d" % (a, sum(x.get("url_mentions", 0) for x in ms), sum(len(x.get("escape_attempts_blocked", [])) for x in ms), sum(x.get("tool_timeouts", 0) or 0 for x in ms), sum(x.get("compactions", 0) or 0 for x in ms)))
deltas = []
for i in pairs:
    # warmth-invariant: input + cache_creation + cache_read of call 1 (a cache-read prefix is still a sent prefix) — refuter F4
    fc = lambda m: (m.get("first_call_usage") or {})
    tot = lambda u: sum(int(u.get(k) or 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
    if fc(scor[(i, "a0")]) and fc(scor[(i, "a1")]): deltas.append(tot(fc(scor[(i, "a1")])) - tot(fc(scor[(i, "a0")])))
print("  length term (a1-a0 first-call input+cache_creation+cache_read tokens): median=%s over %d pairs" % (pct(deltas, .5), len(deltas)))
print("  pairs whose arms landed different models/tiers: %s" % [i for i in pairs if (set(scor[(i, "a0")].get("models") or {}), set(scor[(i, "a0")].get("service_tiers") or {})) != (set(scor[(i, "a1")].get("models") or {}), set(scor[(i, "a1")].get("service_tiers") or {}))])
for a in ("a0", "a1"):
    print("  %s rt_unfinished total=%d" % (a, sum(int(m.get("rt_unfinished") or 0) for (i, x), m in scor.items() if x == a)))
print("  pair order / wall_s: " + " ".join("%s:%s(%ss)/%s(%ss)" % (i[:24], *( ("a0", scor[(i, "a0")]["wall_s"], "a1", scor[(i, "a1")]["wall_s"]) if scor[(i, "a0")]["start_utc"] <= scor[(i, "a1")]["start_utc"] else ("a1", scor[(i, "a1")]["wall_s"], "a0", scor[(i, "a0")]["wall_s"]) )) for i in pairs))
print("  canonical prompt equal within every pair: %s" % all(scor[(i, "a0")].get("prompt_sha256_canonical") == scor[(i, "a1")].get("prompt_sha256_canonical") for i in pairs))
print("  models seen per arm: %s" % {a: sorted({k for (i, x), m in scor.items() if x == a for k in (m.get("models") or {})}) for a in ("a0", "a1")})
if dups: print("  DUPLICATE terminal manifests (latest kept): %s" % dups)
print("  no p-value, by design; no task-arm repeated, so sampling variance and arm effect are not separated at stage 0.")
