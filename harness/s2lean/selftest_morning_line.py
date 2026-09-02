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


def build_state_C(root, k, proven_C):
    """A second, SEPARATE state root carrying stage-C rows (amendment 12).

    Separate on purpose: adding C rows to the shared root would move `manifests: N considered (M dropped)` and
    the three frozen contrast counts, so the nine amendment-7 arms would have to be re-baselined to test
    something they do not test. An additive change gets an additive fixture.
    """
    tasks = drawmod.draw(k)
    n = 0
    for arm in ("a0", "a2"):
        for task in tasks:
            ok = pid_of(task) in proven_C[arm]
            ep = "ep-C%s%d" % (arm, n)
            m = {"substrate": "S2-Lean/CLEVER", "arm": arm, "stage": "C", "instance_id": task, "episode": ep,
                 "termination": "DONE", "end_utc": 1700000000 + n, "passed": ok, "metered_sum": 1000 + n,
                 "calls": 5, "max_turns": 100, "wall_ceiling_s": 5400, "token_ceiling": 20000000,
                 "model_requested": "claude-opus-5", "effort": "high",
                 "check": {"class": "PASS" if ok else "AXIOMS_FAIL", "passed": ok, "compiled": True,
                           "axioms_ok": ok, "statement_diffs": []}}
            d = os.path.join(root, ep); os.makedirs(d, exist_ok=True)
            json.dump(m, open(os.path.join(d, "manifest.json"), "w"))
            n += 1
    return tasks



def _stop_is_4x(out):
    """The stop line must be 4x the cap line, PER STAGE, read off the tool's own output — never recomputed
    here from the fixture. A self-test that recomputes the quantity tests its own arithmetic, not the tool's."""
    import re as _re
    cap = next((l for l in out.splitlines() if "p90 the cap rule consumes" in l), None)
    stop = next((l for l in out.splitlines() if "per-episode TOKEN STOP" in l), None)
    if not cap or not stop: return False
    caps = dict(_re.findall(r"([ABC])=(\d+|None) ?\(?", cap.split(":", 1)[1]))
    stops = dict(_re.findall(r"([ABC])=(\d+|None)", stop.split(":", 1)[1]))
    if set(caps) != set(stops) or not caps: return False
    for k in caps:
        if caps[k] == "None": 
            if stops[k] != "None": return False
        elif int(stops[k]) != 4 * int(caps[k]): return False
    return True

def pid_of(t): return int(t.split("_")[1])


def run(state, env_extra):
    env = dict(os.environ)
    env.pop("ML_ARMS", None)
    env["S2_LANDINGS"] = os.path.join(state, "_no_landings_log")   # deliberately absent
    kk = env_extra.pop("_K", K)          # popped BEFORE the update: an int in the environ is a TypeError
    env.update(env_extra)
    p = subprocess.run([sys.executable, SCRIPT, state, str(kk)], capture_output=True, text=True, env=env)
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

        # ---------- AMENDMENT 12 (2026-09-01): the stage-C REGISTERED-POPULATION line.
        # The defect: stage C's block is over CE (the C-eligible DRAWN subset) while amendment 11's gate is a
        # COUNT over UC = U ∖ c_dead. At k=27 that is 22 against 12, and at a plausible outcome the printed
        # rate and the registered gate point OPPOSITE ways. Driven at k=27 because that is the live
        # configuration, and the fixture is built so CE and UC could not be confused by coincidence.
        rootC = tempfile.mkdtemp(prefix="ml-selftest-C-")
        try:
            # a0 proves 9 of the registered 12 AND 4 flagged-or-C-dead problems that are in CE but NOT in UC.
            # ⇒ CE count 13/22 = 59.1 % (inside the 20–80 % "RUN" band) while the registered count is 9/12,
            #   which is amendment 11's CEILING HOLD. If the instrument prints only the first, the run reads
            #   as its own opposite — this arm is that sentence, driven.
            REG12 = {73, 0, 146, 16, 4, 38, 142, 96, 141, 31, 127, 74}
            a0C = {73, 0, 146, 16, 4, 38, 142, 96, 141} | {109, 34, 90, 159}
            a2C = set(a0C)
            tasksC = build_state_C(rootC, 27, {"a0": a0C, "a2": a2C})
            arms_run += 1
            rc, out, err = run(rootC, {"ML_ARMS": "a0,a2", "_K": 27})
            check("amdt12 rc==0", rc == 0, err[-300:])
            check("amdt12 CE line still 13/22 (the frozen line is UNCHANGED)",
                  "a0 proven 13/22" in out, [l for l in out.splitlines() if "impl + correctness" in l])
            check("amdt12 registered line present and n=12",
                  re.search(r"REGISTERED POPULATION UC = U ∖ c_dead .* n=12 ", out) is not None,
                  [l for l in out.splitlines() if "REGISTERED" in l])
            check("amdt12 registered COUNT is 9/12, not 13/22",
                  "a0 proven 9/12" in out, [l for l in out.splitlines() if "REGISTERED" in l])
            # ⛔ The regex may not match at all — that is exactly what happens when this arm is driven against
            # the PRE-CHANGE tool, which is the red control. Reading `.group(1)` off None there turned a FAIL
            # into a TRACEBACK and took the remaining arms with it. Second instance in this same file of the
            # law it already carries: A GATE WHOSE FAILURE PATH HAS NEVER EXECUTED IS AN UNTESTED GATE — and
            # the failure path is reached by running the control, not by reading the code.
            mreg = re.search(r"n=12 ids \[([0-9, ]+)\]", out)
            regids = sorted(int(x) for x in mreg.group(1).split(",")) if mreg else None
            check("amdt12 the registered ids ARE amendment 11's twelve",
                  regids == sorted(REG12), regids if regids is not None else "no REGISTERED line at all")
            check("amdt12 18 is NOT in the registered ids (c_dead_unsat, amendment 11 §2)",
                  regids is not None and 18 not in regids,
                  regids if regids is not None else "no REGISTERED line at all")
            check("amdt12 a registered pairs line exists beside the CE one",
                  "pairs over the REGISTERED 12" in out, [l for l in out.splitlines() if "pairs over" in l])
            check("amdt12 stage A and B print NO registered line (stage C only)",
                  out.count("REGISTERED POPULATION") == len(("a0", "a2")),
                  out.count("REGISTERED POPULATION"))

            # ---------- amendment 14: "NO DATA" IS NOT 0, driven on the same C-only root and the same argv.
            # ⛔ Against the PRE-CHANGE tool these four FLIP: it printed
            #      "F3 (... k=27 drawn): 0/27 = 0.0% ⇒ HOLD (<20%: a floor, not a reason to add arms)"
            #      "READING: PROVISIONAL (F3 NOT YET READABLE) — HOLD (<20%: a floor, ...)"
            #    i.e. a REGISTERED DECISION about the plain arm, read off a stage that never ran, printed
            #    directly above the stage-C block that did. The PROVISIONAL prefix was already there and did
            #    not save it — it qualified the reading while the reading still named a band.
            fblock = "\n".join(l for l in out.splitlines()
                                if "F3 (" in l or "unflagged drawn subset" in l or "nl_leaked" in l
                                or "bands all-drawn" in l or "READING:" in l)
            arms_run += 1
            check("amdt14 F3 headline says NOT RUN at a stage-C-only root",
                  "NOT RUN AT THIS ROOT" in fblock, fblock)
            check("amdt14 NO band is printed anywhere in the F3 block",
                  "HOLD (<20%" not in fblock and "RUN THE SALT ARM" not in fblock
                  and "HOLD (≥80%" not in fblock, fblock)
            check("amdt14 the two subset lines are NOT RUN, not 0/n rates",
                  "(n=15, ids [73, 0, 146, 16, 4, 38, 142, 96, 112, 141, 31, 54, 127, 18, 74]): NOT RUN" in fblock
                  and "without nl_leaked [90] (n=26): NOT RUN" in fblock, fblock)
            check("amdt14 the two bands are NOT COMPARED (an absent band cannot 'agree')",
                  "bands all-drawn vs unflagged: NOT COMPARED" in fblock, fblock)
            check("amdt14 the SCAFFOLD_DAMAGED integrity line EXISTS (a class with no line is a class nobody sees)",
                  "SCAFFOLD_DAMAGED (marker pairs missing" in out,
                  [l for l in out.splitlines() if "SCAFFOLD" in l] or "no SCAFFOLD_DAMAGED line at all")
            check("amdt14 READING is NOT RUN and carries no PROVISIONAL prefix",
                  "READING: NOT RUN (stage B, arm a0, at this root)" in fblock
                  and "PROVISIONAL (F3 NOT YET READABLE) —" not in fblock, fblock)
        finally:
            shutil.rmtree(rootC, ignore_errors=True)

        # ---------- amendment 14 CONTROL, and it is the arm that matters most: a root where stage B DID
        # run must be BYTE-UNCHANGED. Four assertions that a NOT-RUN branch has not eaten a real reading —
        # a repair which suppresses a false HOLD by suppressing ALL holds passes the four arms above and
        # destroys the instrument. Driven on the SHARED root (stage A+B, a0 proves 1 of 15).
        arms_run += 1
        rc, out, err = run(root, {})
        fb = "\n".join(l for l in out.splitlines()
                        if "F3 (" in l or "bands all-drawn" in l or "READING:" in l)
        check("amdt14 control rc==0", rc == 0, err[-300:])
        check("amdt14 control F3 still prints its RATE and its BAND",
              "F3 (plain arm a0, stage B, proven over the k=15 drawn): 1/15 = 6.7% ⇒ HOLD (<20%" in fb, fb)
        check("amdt14 control NOT RUN does NOT appear on a root that ran",
              "NOT RUN" not in fb, fb)
        check("amdt14 the per-episode TOKEN STOP line is DERIVED and is 4x the printed p90",
              any(l.strip().startswith("per-episode TOKEN STOP") for l in out.splitlines())
              and _stop_is_4x(out),
              [l for l in out.splitlines() if "TOKEN STOP" in l or "p90 the cap rule" in l])
        check("amdt14 control bands are still COMPARED",
              "bands all-drawn vs unflagged: " in fb and "NOT COMPARED" not in fb, fb)

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

    print("SELF-TEST %s — %d arms driven (3 green, 2 label, 1 stage-C/amendment-12, 1 amendment-14 NOT-RUN, 1 amendment-14 control, 4 red), every arm a SUBPROCESS on the real argv"
          % ("PASS" if not fails else "FAIL: " + ", ".join(fails), arms_run))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
