#!/usr/bin/env python3
"""selftest_morning_line.py — the driven gate for s2_morning_line.py's arm set (amendment 7, 2026-08-31).

⛔ THE LAW THIS FILE EXISTS TO OBEY, paid for on 2026-08-30 by `meter.py`: A SELF-TEST THAT NEVER MAKES THE CALL ITS
CALLER MAKES IS A SELF-TEST OF A DIFFERENT PROGRAM. meter.py's own cases all passed `ep=EP`; its caller, the
watchdog, passes no `--ep` at all, so the crash lived under a green self-test for the whole campaign. So every arm
below runs the REAL script as a SUBPROCESS on its REAL argv (`s2_morning_line.py <STATE> <k>`) with only the
environment the operator sets — never an in-process import of a function.

Both arms must differ: three GREEN arms assert the numbers, four RED arms assert a REFUSAL with a nonzero exit, and
two LABEL arms assert the mislabel is gone AND that the correct label is present (an absence assertion alone passes
against an empty output).

usage: s2_morning_line.py --selftest        (or: python3 selftest_morning_line.py)
"""
import json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "s2_morning_line.py")
sys.path.insert(0, HERE)
import draw as drawmod  # noqa: E402

K = 15
# proven(stage B) per arm over the first three drawn tasks — chosen so EVERY pair has a DIFFERENT (b, c), which is
# what makes a mis-paired contrast visible instead of coincidentally right.
#   a0 proves {t0}      a1 proves {t1}      a2 proves {t0, t1}
#   a0/a1: b=1 c=1   ·   a0/a2: b=0 c=1   ·   a1/a2: b=0 c=1   (and a1/a2's c is t0, a0/a2's is t1)
PROVEN_B = {"a0": {0}, "a1": {1}, "a2": {0, 1}}


def build_state(root):
    """a synthetic <STATE> of manifest.json files, in the shape the driver writes."""
    tasks = drawmod.draw(K)[:3]
    n = 0
    for ai, arm in enumerate(("a0", "a1", "a2")):
        for ti, task in enumerate(tasks):
            aep = "ep-A%s%d" % (arm, ti)
            bep = "ep-B%s%d" % (arm, ti)
            for stage, ep in (("A", aep), ("B", bep)):
                ok = True if stage == "A" else (ti in PROVEN_B[arm])
                m = {
                    "substrate": "S2-Lean/CLEVER", "arm": arm, "stage": stage, "instance_id": task,
                    "episode": ep, "termination": "DONE", "end_utc": 1700000000 + n,
                    "passed": ok, "metered_sum": 1000 + n, "calls": 5,
                    "max_turns": 100, "wall_ceiling_s": 5400, "token_ceiling": 20000000,
                    "model_requested": "claude-sonnet-5", "effort": "high",
                    "check": {"class": "PASS" if ok else "AXIOMS_FAIL", "passed": ok,
                              "compiled": True, "axioms_ok": ok, "statement_diffs": []},
                }
                if stage == "B":
                    m["a_episode"] = aep          # matches the scored A row ⇒ not an orphan
                    m["a_bodies_sha256"] = None
                d = os.path.join(root, ep)
                os.makedirs(d, exist_ok=True)
                json.dump(m, open(os.path.join(d, "manifest.json"), "w"))
                n += 1
    return tasks


def run(state, env_extra):
    env = dict(os.environ)
    env.pop("ML_ARMS", None)
    env["S2_LANDINGS"] = os.path.join(state, "_no_landings_log")   # deliberately absent
    env.update(env_extra)
    p = subprocess.run([sys.executable, SCRIPT, state, str(K)], capture_output=True, text=True, env=env)
    return p.returncode, p.stdout, p.stderr


def stageB(out):
    """the stage-B block only — stage A is all-pass by construction and would mask a stage-B error."""
    lines = out.splitlines()
    i = [n for n, l in enumerate(lines) if "ISOMORPHISM PROVEN" in l]
    j = [n for n, l in enumerate(lines) if "impl + correctness" in l]
    return "\n".join(lines[i[0]:(j[0] if j else len(lines))])


def main():
    fails, arms_run = [], 0
    root = tempfile.mkdtemp(prefix="ml-selftest-")
    try:
        build_state(root)

        def check(name, cond, detail=""):
            # ⛔ `detail` is str()-ed, and that is not tidiness: the first RED control run CRASHED here with
            # `can only concatenate str (not "list")`, because every green run had skipped this branch. A gate
            # whose FAILURE path has never executed is an untested gate — found by driving the control, which is
            # the only reason it was found at all.
            nonlocal fails
            print("  %-6s %s%s" % ("PASS" if cond else "FAIL", name, "" if cond else "   << " + str(detail)[:400]))
            if not cond: fails.append(name)

        # ---------- GREEN 1: default env == the frozen a0/a1 behaviour, a2 dropped as other-arm
        arms_run += 1
        rc, out, err = run(root, {})
        b = stageB(out)
        check("green1 rc==0", rc == 0, err[-300:])
        check("green1 a0 scored 1/15", re.search(r"a0 proven 1/15", b) is not None, b)
        check("green1 a1 scored 1/15", re.search(r"a1 proven 1/15", b) is not None, b)
        check("green1 a2 NOT scored", "a2 proven" not in out, b)
        check("green1 a2 rows dropped as other-arm", re.search(r"manifests: 12 considered \(6 dropped", out) is not None,
              [l for l in out.splitlines() if "manifests:" in l])
        check("green1 contrast a0/a1 = b1 c1", "b(a0 only)=1 c(a1 only)=1 n_d=2 |b-c|=0" in b, b)
        check("green1 exactly one contrast line", b.count("pairs over") == 1, b)
        check("green1 arms declared in header", "arms=a0(plain/control) a1(placebo)" in out,
              [l for l in out.splitlines() if "arms=" in l])

        # ---------- GREEN 2: a0,a2 — the pair the frozen tool could not compute at all
        arms_run += 1
        rc, out, err = run(root, {"ML_ARMS": "a0,a2"})
        b = stageB(out)
        check("green2 rc==0", rc == 0, err[-300:])
        check("green2 a2 scored 2/15", re.search(r"a2 proven 2/15", b) is not None, b)
        check("green2 a1 NOT scored", "a1 proven" not in out, b)
        check("green2 contrast a0/a2 = b0 c1", "b(a0 only)=0 c(a2 only)=1 n_d=1 |b-c|=1" in b, b)

        # ---------- GREEN 3: all three arms, all three pairwise contrasts, each with its own numbers
        arms_run += 1
        rc, out, err = run(root, {"ML_ARMS": "a0,a1,a2"})
        b = stageB(out)
        check("green3 rc==0", rc == 0, err[-300:])
        check("green3 three arm lines", all(re.search(r"%s proven" % a, b) for a in ("a0", "a1", "a2")), b)
        check("green3 three contrast lines", b.count("pairs over") == 3, b)
        check("green3 a0/a1", "b(a0 only)=1 c(a1 only)=1" in b, b)
        check("green3 a0/a2", "b(a0 only)=0 c(a2 only)=1" in b, b)
        check("green3 a1/a2", "b(a1 only)=0 c(a2 only)=1" in b, b)

        # ---------- LABEL 1 (negative): the frozen tool's mislabel is GONE
        arms_run += 1
        check("label1 no 'salt arm a1'", "salt arm a1" not in out, [l for l in out.splitlines() if "salt" in l])
        # ---------- LABEL 2 (positive): and the right labels are PRESENT — an absence assertion alone
        #            would pass against an empty report, so both halves are asserted.
        arms_run += 1
        check("label2 a1 named placebo", "a1(placebo)" in out, [l for l in out.splitlines() if "arms=" in l])
        check("label2 a2 named salt", "a2(salt)" in out, [l for l in out.splitlines() if "arms=" in l])

        # ---------- RED arms: every one must REFUSE with a nonzero exit
        for name, spec, needle in (
            ("red1 a0 absent", "a1,a2", "must contain a0"),
            ("red2 bad token", "a0,plain", "not an arm name"),
            ("red3 duplicate", "a0,a0", "repeated arm"),
            ("red4 empty", ",,", "must contain a0"),
        ):
            arms_run += 1
            rc, out, err = run(root, {"ML_ARMS": spec})
            check(name + " refuses", rc != 0 and needle in (err + out), "rc=%s err=%s" % (rc, err[-200:]))
    finally:
        shutil.rmtree(root, ignore_errors=True)

    print("SELF-TEST %s — %d arms driven (3 green, 2 label, 4 red), every arm a SUBPROCESS on the real argv"
          % ("PASS" if not fails else "FAIL: " + ", ".join(fails), arms_run))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
