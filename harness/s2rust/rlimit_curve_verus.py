#!/usr/bin/env python3
"""rlimit_curve_verus.py — THE RLIMIT CURVE AND THE DETERMINISM CONTROL (protocol §8.5).

TWO measurements, deliberately in one tool because they answer one question about the same pin:

1. THE CURVE. Run every LIVE task's REFERENCE body through our scaffold at R in {10, 50, 250} and report the
   PASS count per R. ⛔ THE PIN IS INDICTED IF THE CURVE IS STILL CLIMBING AT 250 — a budget that still buys
   passes at its ceiling is a budget chosen too low, and every failure attributed to an arm under it would
   be partly the budget's. If it climbs, raise and re-register with veval.py's 250 as the deviation baseline.
   ⛔ This replaces a x3 flip test AS THE PIN TEST: at a pinned deterministic rlimit and seed a x3 repeat
   proves determinism, which is a different claim and near-vacuous as evidence about the BUDGET.

2. THE DETERMINISM CONTROL. x3 at R = 250, expected flips 0. A nonzero count indicts the PIN (the rlimit or
   the seed), not the solver, and BLOCKS (§11.3).

usage: rlimit_curve_verus.py <viewsdir> <verus> [--dead F] [--rs 10,50,250] [--repeats 3] [--limit N] [--out F]
"""
import json, os, re, shutil, subprocess, sys, tempfile, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_views_verus as B

RESULTS = re.compile(r"verification results:: (\d+) verified, (\d+) errors")


def referee(verus, src, work, rlimit, seed, timeout=900):
    open(os.path.join(work, "task.rs"), "w", encoding="utf-8").write(src)
    p = subprocess.run(["perl", "-e", "alarm %d; exec @ARGV" % timeout, verus, "--crate-type=lib",
                        "--rlimit", str(rlimit), "--smt-option", "smt.random_seed=%d" % seed, "task.rs"],
                       cwd=work, capture_output=True, text=True)
    line = next((l for l in p.stdout.splitlines() if l.startswith("verification results::")), None)
    m = RESULTS.search(line) if line else None
    if p.returncode == 0 and m and int(m.group(2)) == 0 and int(m.group(1)) >= 1:
        return "PASS"
    if "Resource limit (rlimit) exceeded" in p.stderr:
        return "RLIMIT"
    return "COMPILE" if line is None else "VERIFY_FAIL"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    viewsdir, verus = args
    def opt(n, d, cast=str):
        for a in sys.argv[1:]:
            if a.startswith("--%s=" % n):
                return cast(a.split("=", 1)[1])
        return d
    rs = [int(x) for x in opt("rs", "10,50,250").split(",")]
    repeats = int(opt("repeats", "3"))
    limit = int(opt("limit", "0"))
    dead = opt("dead", os.path.join(viewsdir, "task_dead.json"))
    out = opt("out", os.path.join(viewsdir, "rlimit_curve.json"))

    live = [r["task_id"] for r in json.load(open(dead))["rows"] if r["verdict"] == "LIVE"]
    if limit:
        live = live[:limit]
    print("LIVE tasks: %d   curve R=%s   determinism x%d at R=%d" % (len(live), rs, repeats, max(rs)),
          flush=True)
    work = tempfile.mkdtemp(prefix="rcurve.")
    canon = {}
    for tid in live:
        fz = json.load(open(os.path.join(viewsdir, "views", tid, "frozen.json")))
        gt = json.load(open(os.path.join(viewsdir, "gt", tid + ".json")))
        canon[tid] = B.assemble(fz, gt)

    curve, detail = {}, {}
    t0 = time.time()
    for R in rs:
        tally = {}
        for i, tid in enumerate(live, 1):
            c = referee(verus, canon[tid], work, R, 0)
            tally[c] = tally.get(c, 0) + 1
            detail.setdefault(tid, {})["R%d" % R] = c
            if i % 25 == 0 or i == len(live):
                print("   R=%-4d %3d/%d  %s" % (R, i, len(live), json.dumps(tally)), flush=True)
        curve[R] = tally
        print("R=%-4d => PASS %d/%d   %s" % (R, tally.get("PASS", 0), len(live), json.dumps(tally)), flush=True)

    Rmax = max(rs)
    flips, per = 0, {}
    for rep in range(2, repeats + 1):
        for i, tid in enumerate(live, 1):
            c = referee(verus, canon[tid], work, Rmax, 0)
            first = detail[tid]["R%d" % Rmax]
            if c != first:
                flips += 1
                per.setdefault(tid, []).append([first, c])
            if i % 50 == 0 or i == len(live):
                print("   determinism rep %d  %3d/%d  flips=%d" % (rep, i, len(live), flips), flush=True)
    shutil.rmtree(work, ignore_errors=True)

    rep = dict(rs=rs, repeats=repeats, n=len(live), curve={str(k): v for k, v in curve.items()},
               flips=flips, flip_detail=per, wall_s=round(time.time() - t0, 1), per_task=detail)
    json.dump(rep, open(out, "w"), indent=1)
    print("\n=== CURVE ===")
    prev = None
    for R in rs:
        p = curve[R].get("PASS", 0)
        print("  R=%-5d PASS %3d/%d%s" % (R, p, len(live), "" if prev is None else "   (+%d)" % (p - prev)))
        prev = p
    climb = curve[rs[-1]].get("PASS", 0) - curve[rs[-2]].get("PASS", 0) if len(rs) > 1 else 0
    print("\nPIN VERDICT: %s" % ("⛔ INDICTED — the curve is STILL CLIMBING at R=%d (+%d). Raise and re-register."
                                 % (rs[-1], climb) if climb > 0 else
                                 "✅ NOT INDICTED — the curve is FLAT into R=%d (+%d)." % (rs[-1], climb)))
    print("DETERMINISM: flips=%d over %d repeats %s" % (flips, repeats,
          "✅ (expected 0)" if flips == 0 else "⛔ NONZERO — indicts the PIN, not the solver. BLOCKING."))
    print("wall %.1f min -> %s" % (rep["wall_s"] / 60, out))


if __name__ == "__main__":
    main()
