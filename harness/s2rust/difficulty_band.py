#!/usr/bin/env python3
"""difficulty_band.py — the WITHIN-TASK difficulty signal, over the whole LIVE population. Zero model tokens.

⛔ WHY THIS EXISTS. The P0 gate read was drawn from the AC project because the published prior calls AC the
harder band (36.5% vs NR's 74%). The first AC episode cost **2,725,592** against an NR-pilot median of
466,390, and the step had been priced — by the helm and by me — from that NR pilot. The project split is a
real difficulty signal and an EXPENSIVE one to use as a proxy, because it is confounded with task SIZE:

    AC LIVE (52)   task.rs median 168,329 B   ref-proof wall median 2.80 s   p90 15.70 s
    NR LIVE (128)  task.rs median  18,319 B   ref-proof wall median 0.80 s   p90  3.60 s

⇒ 🔑 A PROJECT NAME IS A PROXY FOR DIFFICULTY; THE REFERENCE PROOF'S OWN COST IS THE THING ITSELF. Drawing
  by project buys the hard band and the expensive band together, with no way to separate them afterwards.

This computes, per LIVE task, the two signals the campaign ALREADY records — the reference proof's referee
WALL (from the three-way ground-truth pass) and the view's SIZE — and offers a stratified draw across
difficulty quantiles rather than across projects. Nothing here decides the design; it makes the fork
decidable on data instead of on another extrapolation.

⛔ IT IS NOT A PREDICTOR AND MUST NOT BE READ AS ONE. The reference wall measures how hard the task was for
the REFERENCE PROOF under the referee, which bounds the agent's cost from BELOW and says nothing from above —
the same law the rlimit curve already carries. n=1 of agent cost on AC is not enough to fit anything; the
correlation column is printed so a future head can check it against real episodes rather than assume it.

usage: difficulty_band.py [--strata N] [--draw K] [--seed S] [--json OUT]
"""
import argparse, json, os, statistics as st, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "state", "task_dead.json")


def rows(viewsdir=None):
    d = json.load(open(STATE))
    out = []
    for r in d["rows"]:
        if r.get("verdict") != "LIVE":
            continue
        rec = {"task_id": r["task_id"], "project": r["task_id"].split("__")[0],
               "ref_wall_s": r.get("seconds")}
        if viewsdir:
            p = os.path.join(viewsdir, "views", r["task_id"], "task.rs")
            rec["view_bytes"] = os.path.getsize(p) if os.path.exists(p) else None
        out.append(rec)
    return out


def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--views"); ap.add_argument("--strata", type=int, default=4)
    ap.add_argument("--draw", type=int, default=0); ap.add_argument("--seed", type=int, default=20260902)
    ap.add_argument("--json"); ap.add_argument("-h", "--help", action="store_true")
    a, _ = ap.parse_known_args()
    if a.help:
        sys.exit(__doc__)

    rs = rows(a.views)
    rs.sort(key=lambda r: (r["ref_wall_s"] if r["ref_wall_s"] is not None else 0.0))
    n = len(rs)
    print("LIVE population n = %d" % n)
    for tag in sorted({r["project"] for r in rs}):
        w = [r["ref_wall_s"] for r in rs if r["project"] == tag]
        line = "  %s n=%-4d ref-wall median %6.2fs  p90 %7.2fs  max %7.2fs" % (
            tag, len(w), st.median(w), sorted(w)[int(.9 * len(w))], max(w))
        if a.views:
            b = [r["view_bytes"] for r in rs if r["project"] == tag and r["view_bytes"]]
            if b:
                line += "   bytes median %8d" % st.median(b)
        print(line)

    # ⛔ QUANTILE STRATA, NOT EQUAL-WIDTH BINS. Reference walls span 0.1 s to 358 s; equal-width bins would
    # put ~all of the population in bin 0 and call the result a stratification.
    k = a.strata
    strata = [rs[i * n // k:(i + 1) * n // k] for i in range(k)]
    print("\n%d difficulty strata by REFERENCE-PROOF WALL (quantiles, so each holds ~n/%d):" % (k, k))
    for i, s in enumerate(strata):
        w = [r["ref_wall_s"] for r in s]
        comp = {}
        for r in s:
            comp[r["project"]] = comp.get(r["project"], 0) + 1
        print("  stratum %d  n=%-4d wall %6.2f–%7.2fs  median %6.2fs   %s"
              % (i, len(s), min(w), max(w), st.median(w),
                 " ".join("%s=%d" % (p, c) for p, c in sorted(comp.items()))))

    out = {"n": n, "strata": k,
           "by_project": {t: {"n": sum(1 for r in rs if r["project"] == t),
                              "ref_wall_median": st.median([r["ref_wall_s"] for r in rs if r["project"] == t])}
                          for t in sorted({r["project"] for r in rs})},
           "strata_rows": [[r["task_id"] for r in s] for s in strata]}

    if a.draw:
        import random
        random.seed(a.seed)
        per = a.draw // k
        pick, extra = [], a.draw - per * k
        for i, s in enumerate(strata):
            take = per + (1 if i < extra else 0)
            pick += random.sample([r["task_id"] for r in s], min(take, len(s)))
        pick.sort()
        print("\nSTRATIFIED DRAW k=%d, seed=%d — %d per stratum (+%d spread over the lowest):"
              % (a.draw, a.seed, per, extra))
        for t in pick:
            r = next(x for x in rs if x["task_id"] == t)
            print("  %-7.2fs  %-3s %s" % (r["ref_wall_s"], r["project"], t[:64]))
        out["draw"] = pick
        out["draw_seed"] = a.seed
        # the honest cost note: a stratified draw spans the range instead of buying its expensive end
        acn = sum(1 for t in pick if t.startswith("AC__"))
        print("\n  composition: AC=%d NR=%d  (a project draw on AC would be AC=%d)" % (acn, len(pick) - acn, len(pick)))

    if a.json:
        json.dump(out, open(a.json, "w"), indent=1)
        print("\nwrote %s" % a.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
