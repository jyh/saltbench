#!/usr/bin/env python3
"""c_dead_merge.py — the C-DEAD UNION, in ONE place (amendment 11, 2026-09-01, desk row AS).

`c_dead` (D7) was minted as an ELABORATION list: views_selftest.sh compiles every stage-C view and calls a
view dead when it does not elaborate. That measures whether the task can be STATED, never whether it can be
DONE. `problem_18` elaborates perfectly and is unpassable by any arm at any budget — a THEOREM, not a
judgement (AMENDMENT-11 §2, TRIAGE-B-failures-2026-09-01.md §4). So `c_dead` now means "the stage-C task
cannot be completed" and has TWO components:

    c_dead = c_dead_elaboration  ∪  c_dead_unsat
             (measured by the      (registered in c_dead_unsat.json, each id carrying its own
              161×3 sweep)          machine-checked refutation; added by dated amendment only)

⛔ WHY THIS IS A TOOL AND NOT AN EDIT. `view_status.json` is GENERATED. An id added to it by hand is dropped
the next time anyone runs the sweep — silently, because the sweep is *right* about elaboration and has no
idea the meaning was extended. The union therefore has to live in code that the generator itself calls, and
this file is the only implementation of it: views_selftest.sh calls this after writing its component, and a
by-hand refresh of an existing view_status.json calls exactly the same code path.

usage: c_dead_merge.py <view_status.json> [--unsat <c_dead_unsat.json>] [--in-place] [--quiet]
       c_dead_merge.py --selftest
exit 0 ok · 2 bad args · 6 REFUSE (the registry and the status file disagree about what they describe)
"""
import json, os, sys, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def load_unsat(path):
    d = json.load(open(path))
    return sorted(int(k) for k in d["unsat"])


def merge(status, unsat, where="<status>"):
    """Return (status, report). Pure: the caller decides whether to write."""
    problems = {k for k in status if k.startswith("problem_")}
    missing = [i for i in unsat if "problem_%d" % i not in problems]
    if missing:
        raise SystemExit("REFUSE: %s: c_dead_unsat.json names ids this status file has never seen: %s"
                         % (where, missing))
    if "c_dead_elaboration" in status:
        elab = sorted(status["c_dead_elaboration"])
    else:
        # Legacy file, written before the meaning was extended: its c_dead IS the elaboration component.
        legacy = sorted(status.get("c_dead", []))
        clash = sorted(set(legacy) & set(unsat))
        if clash:
            # Both components would claim these ids and the file cannot say which measured them. Refusing is
            # the only honest move: the split is not recoverable from what is written down.
            raise SystemExit("REFUSE: %s: legacy c_dead already contains registered-unsat ids %s and carries no "
                             "c_dead_elaboration key, so the split cannot be recovered — regenerate with "
                             "views_selftest.sh, which writes both components." % (where, clash))
        elab = legacy
    status["c_dead_elaboration"] = elab
    status["c_dead_unsat"] = sorted(unsat)
    status["c_dead"] = sorted(set(elab) | set(unsat))
    return status, {"elaboration": elab, "unsat": sorted(unsat), "c_dead": status["c_dead"]}


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if not argv or argv[0].startswith("-"):
        print(__doc__); return 2
    path = argv[0]
    unsat_path = os.path.join(HERE, "c_dead_unsat.json")
    inplace = quiet = False
    rest = argv[1:]
    while rest:
        a = rest.pop(0)
        if a == "--unsat": unsat_path = rest.pop(0)
        elif a == "--in-place": inplace = True
        elif a == "--quiet": quiet = True
        else: print("REFUSE: unknown arg %r" % a); return 2
    status = json.load(open(path))
    unsat = load_unsat(unsat_path) if os.path.exists(unsat_path) else []
    status, rep = merge(status, unsat, where=path)
    out = json.dumps(status, indent=1) + "\n"
    if inplace: open(path, "w").write(out)
    else: sys.stdout.write(out)
    if not quiet:
        sys.stderr.write("c_dead = %d elaboration-dead + %d unsat-dead (registered) = %d\n"
                         % (len(rep["elaboration"]), len(rep["unsat"]), len(rep["c_dead"])))
        for i in rep["unsat"]:
            sys.stderr.write("  UNSAT %d: its C view elaborates (%s) and the task is provably unsatisfiable "
                             "— c_dead_unsat.json\n" % (i, status["problem_%d" % i].get("C")))
    return 0


# ─────────────────────────── selftest: every arm a subprocess on the real argv ───────────────────────────
def selftest():
    ME = os.path.abspath(__file__)
    fails = []; arms = 0

    def run(args, stdin_files=None):
        return subprocess.run([sys.executable, ME] + args, capture_output=True, text=True)

    def arm(name, cond, detail=""):
        nonlocal arms
        arms += 1
        if not cond: fails.append("%s: %s" % (name, detail))

    with tempfile.TemporaryDirectory() as d:
        def write(name, obj):
            p = os.path.join(d, name); json.dump(obj, open(p, "w"), indent=1); return p

        base = {"problem_1": {"A": "ok", "B": "ok", "C": "error"},
                "problem_2": {"A": "ok", "B": "ok", "C": "ok"},
                "problem_3": {"A": "ok", "B": "ok", "C": "ok"}}
        reg2 = write("unsat2.json", {"unsat": {"2": {"reason": "test"}}})
        reg9 = write("unsat9.json", {"unsat": {"9": {"reason": "test"}}})
        regnone = write("unsatnone.json", {"unsat": {}})

        # 1. RED FIRST — with no registry the union is the elaboration component, i.e. 2 is NOT dead. If this
        #    arm ever goes green the tool has stopped being able to tell the components apart.
        st = write("legacy.json", dict(base, c_dead=[1]))
        r = run([st, "--unsat", regnone])
        d0 = json.loads(r.stdout)
        arm("red/no-registry", d0["c_dead"] == [1] and d0["c_dead_unsat"] == [], d0.get("c_dead"))

        # 2. GREEN — the registered id joins c_dead though its own C row says "ok".
        st = write("legacy2.json", dict(base, c_dead=[1]))
        r = run([st, "--unsat", reg2])
        d1 = json.loads(r.stdout)
        arm("green/union", d1["c_dead"] == [1, 2], d1.get("c_dead"))
        arm("green/components", d1["c_dead_elaboration"] == [1] and d1["c_dead_unsat"] == [2], str(d1))
        arm("green/elaborating-cell", d1["problem_2"]["C"] == "ok",
            "the point of the whole file: a dead cell whose view elaborates")

        # 3. IDEMPOTENT — running twice must not fold the unsat id into the elaboration component.
        st = write("idem.json", dict(base, c_dead=[1]))
        run([st, "--unsat", reg2, "--in-place"]); run([st, "--unsat", reg2, "--in-place"])
        d2 = json.load(open(st))
        arm("idempotent", d2["c_dead"] == [1, 2] and d2["c_dead_elaboration"] == [1], str(d2))

        # 4. REFUSE — a registry naming an id the sweep never saw.
        st = write("miss.json", dict(base, c_dead=[1]))
        r = run([st, "--unsat", reg9])
        arm("refuse/unknown-id", r.returncode != 0 and "REFUSE" in (r.stderr + r.stdout), r.stderr[-200:])

        # 5. REFUSE — a legacy file whose c_dead already claims a registered-unsat id and which carries no
        #    component split: the split is unrecoverable and guessing it would silently mislabel a measurement.
        st = write("clash.json", dict(base, c_dead=[1, 2]))
        r = run([st, "--unsat", reg2])
        arm("refuse/unrecoverable-split", r.returncode != 0 and "cannot be recovered" in (r.stderr + r.stdout),
            r.stderr[-200:])

        # 6. …but the same file WITH the split present is accepted and stays correct.
        st = write("split.json", dict(base, c_dead=[1, 2], c_dead_elaboration=[1, 2]))
        r = run([st, "--unsat", reg2])
        d3 = json.loads(r.stdout)
        arm("split-present/ok", r.returncode == 0 and d3["c_dead"] == [1, 2] and d3["c_dead_elaboration"] == [1, 2],
            r.stderr[-200:])

        # 7. --in-place writes, stdout mode does not.
        st = write("nowrite.json", dict(base, c_dead=[1]))
        before = open(st).read(); run([st, "--unsat", reg2]); arm("stdout/no-write", open(st).read() == before)

        # 8. REFUSE — unknown argument.
        r = run([st, "--nope"]); arm("refuse/bad-arg", r.returncode == 2, str(r.returncode))

        # 9. The real registered file parses and names exactly the ids the amendment registered.
        real = os.path.join(HERE, "c_dead_unsat.json")
        arm("real-registry", os.path.exists(real) and load_unsat(real) == [18],
            load_unsat(real) if os.path.exists(real) else "absent")

    print("c_dead_merge selftest: %d arms, %d failed" % (arms, len(fails)))
    for f in fails: print("  FAIL " + f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
