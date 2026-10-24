#!/usr/bin/env python3
"""spread.py -- the per-problem a2/a0 token-ratio spread of AMENDMENT 8 (U15, claude-opus-5), for O90 [F11c].

WHAT IT MEASURES
  For each U15 problem where BOTH arms (a0, a2) passed at stage B (manifest field `passed`, stage "B"), the ratio
      r_B   = T(a2, B) / T(a0, B)
      r_AB  = (T(a2, A) + T(a2, B)) / (T(a0, A) + T(a0, B))
  where T is the manifest field `metered_sum_governing` (the CLI's own modelUsage sum, which the episode's meter
  cross-checks against the transcript; it includes the CLI's small side-model calls). `metered_sum` (transcript-only,
  main model) is reported beside it. The population is DERIVED from the manifests; no problem id is typed here.

SPREAD (printed, several definitions; see README for the recommendation)
  med|r-1|            median of |r - 1|                    (the design's literal "per-problem spread", in %)
  IQR(r)              Q3 - Q1 of r (linear interpolation, numpy's default definition, implemented here)
  min/max(r)          the range
  MAD_log             median |ln r - median ln r|, reported as the factor exp(MAD_log): the DISPERSION of the ratio
                      around its own centre on a symmetric (log) scale; the arm SHIFT is removed by the centring.
  med|ln r|           median |ln r|, as a factor

SELF-CHECK (--selfcheck): three invariants, each from a source other than the computing path, and three mutants that
must each turn one of them red:
  I1  the 60-episode sum of the chosen field == the figure the amendment text states ("whole amendment cost
      N metered"), parsed from SCOUT-S2LEAN-STAGE0.md, never typed here
  I2  the both-passed population == the one derived independently from each episode's check.json `passed`
  I3  every per-problem r_B == the ratio recomputed from the landings log (ep task stage arm term metered), a record
      written by the driver with its own arm/stage labels
  mutants: --mutant swap (a0<->a2) · --mutant allprob (drop the both-passed filter) · --mutant field (metered_sum)

usage: spread.py --state <dir holding ep-*/> --landings <s2-landings.log> [--scout SCOUT-S2LEAN-STAGE0.md]
                 [--json out.json] [--mutant swap|allprob|field] [--selfcheck]
exit: 0 ok · 1 an invariant failed · 2 usage/input error
"""
import argparse, glob, json, math, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SCOUT = os.path.normpath(os.path.join(HERE, "..", "..", "..", "SCOUT-S2LEAN-STAGE0.md"))
FIELD = "metered_sum_governing"


def load(state):
    eps = []
    for d in sorted(glob.glob(os.path.join(state, "ep-*"))):
        mf = os.path.join(d, "manifest.json")
        if not os.path.isfile(mf):
            continue
        m = json.load(open(mf))
        ck = None
        cf = os.path.join(d, "check.json")
        if os.path.isfile(cf) and os.path.getsize(cf):
            ck = json.load(open(cf))
        eps.append({"ep": os.path.basename(d), "m": m, "check": ck})
    return eps


def quantile(xs, q):
    s = sorted(xs)
    if not s:
        return float("nan")
    pos = (len(s) - 1) * q
    lo, hi = math.floor(pos), math.ceil(pos)
    return s[lo] + (s[hi] - s[lo]) * (pos - lo)


def median(xs):
    return quantile(xs, 0.5)


def table(eps, field, mutant=None):
    """returns (rows, popset). rows: problem -> dict of per-arm per-stage tokens and passed flags."""
    arms = ("a0", "a2")
    if mutant == "swap":
        arms = ("a2", "a0")
    P = {}
    for e in eps:
        m = e["m"]
        pid = m["instance_id"]
        P.setdefault(pid, {})[(m["arm"], m["stage"])] = {"T": m[field], "passed": bool(m["passed"]), "ep": e["ep"]}
    rows = {}
    for pid, cells in P.items():
        need = [(a, s) for a in arms for s in ("A", "B")]
        if any(k not in cells for k in need):
            raise SystemExit("INPUT: problem %s lacks a cell among %s" % (pid, need))
        both = cells[(arms[0], "B")]["passed"] and cells[(arms[1], "B")]["passed"]
        if mutant != "allprob" and not both:
            continue
        x, y = arms  # ratio = y / x  (a2 / a0 unless swapped)
        rows[pid] = {
            "a0_B": cells[(x, "B")]["T"], "a2_B": cells[(y, "B")]["T"],
            "a0_A": cells[(x, "A")]["T"], "a2_A": cells[(y, "A")]["T"],
            "a0_B_ep": cells[(x, "B")]["ep"], "a2_B_ep": cells[(y, "B")]["ep"],
            "both_passed_B": both,
        }
        r = rows[pid]
        r["r_B"] = r["a2_B"] / r["a0_B"]
        r["r_AB"] = (r["a2_A"] + r["a2_B"]) / (r["a0_A"] + r["a0_B"])
    return rows


def spread(rs):
    lr = [math.log(r) for r in rs]
    ml = median(lr)
    return {
        "n": len(rs),
        "median_r": median(rs),
        "geomean_r": math.exp(sum(lr) / len(lr)) if lr else float("nan"),
        "med_abs_r_minus_1": median([abs(r - 1) for r in rs]),
        "q1_r": quantile(rs, 0.25), "q3_r": quantile(rs, 0.75),
        "iqr_r": quantile(rs, 0.75) - quantile(rs, 0.25),
        "min_r": min(rs), "max_r": max(rs), "max_over_min": max(rs) / min(rs),
        "mad_log_factor": math.exp(median([abs(x - ml) for x in lr])),
        "med_abs_log_factor": math.exp(median([abs(x) for x in lr])),
        "n_above_1": sum(r > 1 for r in rs),
        "n_above_1_5": sum(r > 1.5 for r in rs),
        "n_below_0_8": sum(r < 0.8 for r in rs),
    }


def amendment_total(scout):
    txt = " ".join(open(scout, encoding="utf-8").read().split())  # flatten: the phrase is hard-wrapped
    m = re.search(r"whole amendment cost ([0-9,]+) metered", txt)
    if not m:
        raise SystemExit("INPUT: the amendment-8 total phrase was not found in %s" % scout)
    return int(m.group(1).replace(",", ""))


def landings(path):
    L = {}
    for line in open(path):
        f = line.split()
        if len(f) < 6:
            continue
        ep, task, stage, arm, term, met = f[:6]
        L[(task, arm, stage)] = (ep, int(met))
    return L


def run(a):
    eps = load(a.state)
    if len(eps) == 0:
        print("FAIL: zero episodes under %s (a scan over nothing is not a reading)" % a.state)
        return 1
    field = "metered_sum" if a.mutant == "field" else FIELD
    rows = table(eps, field, a.mutant)
    out = {"state": "<state>", "episodes": len(eps), "field": field, "mutant": a.mutant, "rows": rows}
    fails = []

    # totals by field (both fields printed, the chosen one checked)
    tot = {f: {s: sum(e["m"][f] for e in eps if e["m"]["stage"] == s) for s in "AB"} for f in ("metered_sum", FIELD)}
    want = amendment_total(a.scout)
    got = tot[field]["A"] + tot[field]["B"]
    out["totals"] = tot
    out["amendment_total_from_text"] = want
    print("episodes: %d   (stage A %d, stage B %d)" % (len(eps), sum(e["m"]["stage"] == "A" for e in eps),
                                                     sum(e["m"]["stage"] == "B" for e in eps)))
    for f in ("metered_sum", FIELD):
        s = tot[f]["A"] + tot[f]["B"]
        print("  sum %-24s A %11s  B %11s  A+B %11s  %s amendment text %s" % (
            f, format(tot[f]["A"], ","), format(tot[f]["B"], ","), format(s, ","),
            "==" if s == want else "!=", format(want, ",")))
    if got != want:
        fails.append("I1 sum of %s = %d != amendment text %d" % (field, got, want))

    # I2: population from check.json
    byp = {}
    for e in eps:
        m = e["m"]
        if m["stage"] == "B":
            byp.setdefault(m["instance_id"], {})[m["arm"]] = bool((e["check"] or {}).get("passed"))
    pop_ck = sorted(p for p, d in byp.items() if d.get("a0") and d.get("a2"))
    if sorted(rows) != pop_ck:
        fails.append("I2 population %s != check.json both-passed %s" % (sorted(rows), pop_ck))

    # I3: ratios from the landings log
    L = landings(a.landings)
    for pid, r in rows.items():
        try:
            rb = L[(pid, "a2", "B")][1] / L[(pid, "a0", "B")][1]
        except KeyError:
            fails.append("I3 %s missing in landings" % pid)
            continue
        if abs(rb - r["r_B"]) > 1e-12:
            fails.append("I3 %s r_B %.6f != landings %.6f" % (pid, r["r_B"], rb))

    def num(p):
        return int(p.split("_")[-1])

    print("\nper problem, both arms passed at stage B (n = %d), field %s:" % (len(rows), field))
    print("  %-12s %11s %11s %7s   %11s %11s %7s" % ("problem", "a0 B", "a2 B", "r_B", "a0 A+B", "a2 A+B", "r_AB"))
    for pid in sorted(rows, key=num):
        r = rows[pid]
        print("  %-12s %11s %11s %7.3f   %11s %11s %7.3f" % (
            pid, format(r["a0_B"], ","), format(r["a2_B"], ","), r["r_B"],
            format(r["a0_A"] + r["a0_B"], ","), format(r["a2_A"] + r["a2_B"], ","), r["r_AB"]))
    S = {}
    for key in ("r_B", "r_AB"):
        rs = [rows[p][key] for p in rows]
        if not rs:
            fails.append("population empty")
            break
        S[key] = spread(rs)
        s = S[key]
        if key == "r_B":
            s0, s2 = sum(rows[p]["a0_B"] for p in rows), sum(rows[p]["a2_B"] for p in rows)
        else:
            s0 = sum(rows[p]["a0_A"] + rows[p]["a0_B"] for p in rows)
            s2 = sum(rows[p]["a2_A"] + rows[p]["a2_B"] for p in rows)
        s["aggregate_ratio"] = s2 / s0
        print("\nspread of %s (n = %d):" % (key, s["n"]))
        print("  aggregate (sum a2 / sum a0 over these problems) %.4f" % s["aggregate_ratio"])
        print("  median r %.3f · geometric mean %.3f · r > 1 in %d of %d · r > 1.5 in %d · r < 0.8 in %d" % (
            s["median_r"], s["geomean_r"], s["n_above_1"], s["n"], s["n_above_1_5"], s["n_below_0_8"]))
        print("  median |r-1| %.1f %%  ·  IQR(r) %.3f (Q1 %.3f, Q3 %.3f)  ·  min %.3f  max %.3f  max/min %.2f" % (
            100 * s["med_abs_r_minus_1"], s["iqr_r"], s["q1_r"], s["q3_r"], s["min_r"], s["max_r"], s["max_over_min"]))
        print("  dispersion about its own centre, log scale: exp(MAD ln r) = %.3f (i.e. +/-%.1f %%)  ·  exp(median |ln r|) = %.3f" % (
            s["mad_log_factor"], 100 * (s["mad_log_factor"] - 1), s["med_abs_log_factor"]))
    out["spread"] = S
    out["invariants_failed"] = fails
    if a.json:
        json.dump(out, open(a.json, "w"), indent=1, sort_keys=True)
    print("\nINVARIANTS: %s" % ("I1 I2 I3 hold" if not fails else "FAILED: " + " | ".join(fails)))
    return 1 if fails else 0


def selfcheck(a):
    me = os.path.abspath(__file__)
    base = [sys.executable, "-I", me, "--state", a.state, "--landings", a.landings, "--scout", a.scout]
    ok = True
    r = subprocess.run(base, capture_output=True, text=True)
    print("selfcheck  pristine          rc=%d  (want 0)  %s" % (r.returncode, r.stdout.strip().splitlines()[-1]))
    ok &= r.returncode == 0
    for mu in ("swap", "allprob", "field"):
        r = subprocess.run(base + ["--mutant", mu], capture_output=True, text=True)
        last = (r.stdout.strip().splitlines() or ["<no output>"])[-1]
        print("selfcheck  mutant %-10s rc=%d  (want 1)  %s" % (mu, r.returncode, last[:200]))
        ok &= r.returncode == 1
    print("SELFCHECK %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", required=True)
    ap.add_argument("--landings", required=True)
    ap.add_argument("--scout", default=DEFAULT_SCOUT)
    ap.add_argument("--json")
    ap.add_argument("--mutant", choices=("swap", "allprob", "field"))
    ap.add_argument("--selfcheck", action="store_true")
    a = ap.parse_args()
    sys.exit(selfcheck(a) if a.selfcheck else run(a))


if __name__ == "__main__":
    main()
