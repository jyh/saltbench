#!/usr/bin/env python3
"""arm_coverage_report.py <arm-coverage.json> [--title TEXT]

Render `arm_coverage.py --json` into the RESULT markdown.  ⛔ IT EXISTS SO THAT NO NUMBER IN THAT
DOCUMENT IS TYPED.  This campaign's standing defect is a derived table beside a hand-written sentence
that disagrees with it; the sentences here are built from the same dict as the table, so a figure and
its prose cannot drift apart.  Prints to stdout; costs zero model tokens.
"""
import json, sys


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(64)
    rows = json.load(open(a[0]))
    ok = [r for r in rows if r["reading"] == "MEASURED"]
    dead = {r["task"]: r["dead_arms"] for r in ok}
    surv = {r["task"]: r["survivors"] for r in ok}
    m1 = {r["task"]: r["margin_1"] for r in ok}
    n_arms = sum(len(r["arms"]) for r in ok)
    n_mut = sum(len(r["mutants_measured"]) for r in ok)

    print("## §1 · THE MATRIX — every withheld arm × every withheld mutant, on the five pricing tasks")
    print("```")
    print("  %-9s %5s %8s %10s %9s %10s" % ("task", "arms", "mutants", "dead arms", "margin-1", "survivors"))
    for r in ok:
        print("  %-9s %5d %8d %10d %9d %10d"
              % (r["task"], len(r["arms"]), len(r["mutants_measured"]),
                 len(r["dead_arms"]), len(r["margin_1"]), len(r["survivors"])))
    print("  %-9s %5d %8d %10d %9d %10d"
          % ("TOTAL", n_arms, n_mut,
             sum(len(v) for v in dead.values()),
             sum(len(v) for v in m1.values()),
             sum(len(v) for v in surv.values())))
    print("```")

    print("\n## §2 · DEAD ARMS — an arm that fails on NO mutant")
    any_dead = [(t, v) for t, v in dead.items() if v]
    if not any_dead:
        print("**NONE.** Every arm in every measured suite fails on at least one mutant.")
        print("⛔ **That is a statement about THIS MUTANT SET, not a clean bill of health for the arms.**")
        print("An arm is dead here only if no mutant attacks what it checks; a suite with a thin mutant")
        print("set can show zero dead arms and still be untested in the direction that matters.")
    else:
        for t, v in any_dead:
            print("* **%s** — %d dead: `%s`" % (t, len(v), "`, `".join(v)))

    print("\n## §3 · MARGIN — how many arms each mutant's death rests on")
    print("A mutant killed by exactly ONE arm is one deletion away from surviving. The kill RATE cannot")
    print("see this: it counts mutants, and a margin-1 mutant is a full point in the numerator.")
    any_m1 = [(t, v) for t, v in m1.items() if v]
    if not any_m1:
        print("\n**No mutant in any measured suite rests on a single arm.**")
    else:
        for t, v in any_m1:
            r = [x for x in ok if x["task"] == t][0]
            for mut in v:
                print("* **%s / `%s`** — killed only by `%s`" % (t, mut, r["killers_by_mutant"][mut][0]))

    print("\n## §4 · SURVIVORS — a mutant no arm kills")
    any_s = [(t, v) for t, v in surv.items() if v]
    if not any_s:
        print("**NONE.** Every measured mutant is killed by at least one arm in its suite.")
    else:
        for t, v in any_s:
            print("* ⛔ **%s** — %d survive: `%s`" % (t, len(v), "`, `".join(v)))

    print("\n## §5 · WHAT THIS DOES AND DOES NOT ESTABLISH")
    print("✅ It replaces the protocol's *first failing line* — which reads like attribution and is not —")
    print("with the full set of arms that fail on each mutant. **Attribution is now measured.**")
    print("⛔ It does NOT show any suite is strong. Every arm here is scored against a mutant set the")
    print("same author wrote; a mutant set and a suite that share an author share their blind spots.")
    print("⛔ And a task's `TESTS p/t` denominator is unchanged by any of this: a dead arm would still")
    print("count toward `p` and toward `t` on every submission, in every receipt.")
    unm = [(r["task"], r["mutants_unmeasured"]) for r in ok if r["mutants_unmeasured"]]
    if unm:
        print("\n⛔ **UNMEASURED mutants (did not build or died before reporting; NOT counted as kills):**")
        for t, v in unm:
            print("* %s — `%s`" % (t, "`, `".join(v)))
    bad = [r for r in rows if r["reading"] != "MEASURED"]
    if bad:
        print("\n⛔ **TASKS NOT MEASURED:**")
        for r in bad:
            print("* %s — %s: %s" % (r["task"], r["reading"], r["why"]))


if __name__ == "__main__":
    main()
