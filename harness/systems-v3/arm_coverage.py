#!/usr/bin/env python3
"""arm_coverage.py <referee-tasks-dir> [--tasks T,T,...] [--json OUT] | --selftest

THE TEST x MUTANT MATRIX FOR THE **WITHHELD** SUITE -- the referee's own arms, not the seat's.

`test_strength.py` scores the SEAT's tests against the withheld mutants and answers *is this
submission's suite any good*.  This tool points the same mutants at the WITHHELD suite and answers the
question nobody has asked campaign-wide: *is every arm of the referee's own hidden suite doing work?*

An arm that fails on NO mutant is DEAD.  It passes the reference, it passes every mutant, it appears in
every `TESTS p/t` denominator, and it discriminates nothing.  ⛔ IT IS INVISIBLE TO THE KILL RATE: a
suite can score 1.000 against every mutant while half its arms are dead, because the rate is computed
over MUTANTS and a dead arm hides in the DENOMINATOR OF THE TESTS LINE, not in the numerator of the
score.  On the one task where anyone looked, an arm was dead while every receipt read green.

⇒ THE TWO READINGS THIS PRINTS, AND THE SECOND IS THE ONE THE RATE DISCARDS:
   ROW reading (per arm)     how many mutants this arm kills.  0 = DEAD.
   COLUMN reading (per mutant) how many arms kill it.  1 = the kill rests on a single arm; delete that
                              arm and the mutant SURVIVES.  0 = the mutant SURVIVES already.

⛔ A DEAD ARM IS NOT AUTOMATICALLY A DEFECT and this tool does not call it one.  An arm may be dead
because no mutant in the set attacks what it checks -- that is a statement about the MUTANT SET, not
about the arm.  The tool reports the matrix; the reading is the reader's.  What it does assert is that
an unmeasured arm cannot be defended either way.

Exit 0 when the matrix was built for every requested task, 1 when any task could not be measured, 4 on
a refusal (missing path or the six-name toolchain contract).  Prints a table and, with --json, the raw
matrix.  Costs ZERO model tokens.
"""
import json, os, re, shutil, subprocess, sys, tempfile

TASKS = ["Crc32", "LRU", "LZW", "FreeList", "Paxos"]
TOOLCHAIN = ("VERUS_ROOT", "VERUS_GUARD", "RUSTUP_ROOT", "CARGO_ROOT", "RUST_TOOLCHAIN_PIN", "VERUS_SHA256")
LINE = re.compile(r"^(PASS|FAIL) (\S+)")
TESTS = re.compile(r"^TESTS (\d+)/(\d+)\s*$")


def refuse(why):
    print("arm_coverage: REFUSE -- %s" % why)
    sys.exit(4)


def parse_driver_output(text):
    """(arms, tests) from the withheld driver's stdout.

    ⛔⛔ THE ARM NAME IS THE FIRST TOKEN AFTER THE VERB, AND NOTHING ELSE.  A real FAIL line carries
    trailing detail that a PASS line does not:

        PASS check_value
        FAIL check_value  [FAIL: the check value "123456789": expected 0xcbf43926, got 0x2ac0a892]

    This regex read `(.+?)` to end-of-line and captured the WHOLE remainder, so the arm parsed off a FAIL line
    never equalled the same arm parsed off the reference's PASS line.  Every kill on such a task looked
    up as `None`, not `False`.  ⇒ THE SWEEP REPORTED 27 DEAD ARMS AND 9 SURVIVORS THAT DO NOT EXIST --
    **this tool manufactured, from a parsing bug, exactly the finding it was built to detect**, and the
    two affected tasks were the two whose drivers append detail.
    ⇒ 🔑 AN INSTRUMENT THAT REPORTS ABSENCE FAILS TOWARD ABSENCE.  A name that does not match reads as
    "this arm did nothing", which is indistinguishable from the finding.  The positive control (a
    wrecked reference must FAIL) is what separated them, and nothing else would have.

    ⛔⛔ AND THE ROOT IS THAT THE FIVE WITHHELD DRIVERS DO NOT SHARE AN OUTPUT CONTRACT.  Measured over
    `withheld/tests/*.rs` in all five pricing tasks:

        PASS   `println!("PASS {}")`          UNIFORM in 5 of 5
        FAIL   `println!("FAIL {}")`          LRU · LZW · FreeList
               `println!("FAIL {}{}")`        Crc32
               `println!("FAIL {} — ...")`    Paxos, in SEVEN distinct shapes

    ⇒ 🔑 THE VALIDITY CHECK EVERY TASK PASSES -- the reference run -- EXERCISES ONLY THE `PASS` PATH,
    WHICH IS THE ONE SHAPE THAT IS UNIFORM.  All the variation lives in the path that appears only when
    something fails, so a parser validated against the reference is validated against the half that
    could not have told it anything.  This is why the tool ran clean on 5 of 5 references and was wrong
    on 2 of 5 mutant sets.  Taking the arm name as the FIRST TOKEN after the verb is contract-free and
    survives all three shapes.

    ONE guard does the anchoring: `LINE` is anchored at `^` and requires a SPACE after the verb.

      "  FAIL: the implementation panicked"   the driver's panic line -- refused twice over
      "FAIL: the implementation panicked"     unindented        -- refused: "FAIL:" is not "FAIL "
      "  FAIL beta"                           indented, well-formed -- refused: `^` does not match
                                              at a leading space

    ⛔⛔ THIS FUNCTION CARRIED AN EXPLICIT `if line[:1] in (" ", "\t"): continue` SKIP, AND IT WAS DEAD
    CODE.  It was written to stop the panic line; a negative control showed the space-after-verb rule
    already did that; the comment was then "corrected" to say the skip stopped indented well-formed
    lines; **deleting the skip and re-running the suite changed nothing** -- `^` had that case too.
    ⇒ 🔑 TWO WRONG EXPLANATIONS IN A ROW FOR A GUARD THAT DOES NOTHING, AND BOTH READ AS CAREFUL.  The
    arm asserting the skip's job passed with the skip present AND absent: **it was a dead arm, in the
    tool built to find dead arms.**  Only the DELETION DRIVE separated them.
    ⇒ 🔑 A CASE BEING HANDLED IS NOT EVIDENCE THAT THE CODE YOU WROTE FOR IT HANDLES IT -- the same
    ATTRIBUTION defect this tool exists to measure, one level up.  The skip is deleted; the arms that
    characterise the real guard are kept.

    ⇒ WHY IT MATTERS THAT AN ARM IS NEVER INVENTED: a phantom arm appears in exactly one column, so it
    manufactures a KILL on that mutant AND reads as DEAD on every other -- one line of noise producing
    both of this tool's findings at once.
    """
    arms, tests = {}, None
    for line in text.split("\n"):
        m = LINE.match(line)
        if m:
            arms[m.group(2)] = (m.group(1) == "PASS")
        t = TESTS.match(line)
        if t:
            tests = (int(t.group(1)), int(t.group(2)))
    return arms, tests


def selftest():
    """Drive the parser on the shapes that actually occur, RED arms included."""
    fails = []

    def check(label, got, want):
        if got != want:
            fails.append("%s: got %r want %r" % (label, got, want))

    # A1 the ordinary shape
    a, t = parse_driver_output("PASS alpha\nFAIL beta\nTESTS 1/2\n")
    check("A1 arms", a, {"alpha": True, "beta": False})
    check("A1 tests", t, (1, 2))
    # A2 the real driver shape: the panic line must NOT become an arm
    a, _ = parse_driver_output("PASS alpha\n  FAIL: the implementation panicked\nFAIL beta\nTESTS 1/2\n")
    check("A2 no invented arm", a, {"alpha": True, "beta": False})
    # A3 ⛔ NEGATIVE CONTROL THAT REFUTED THIS TOOL'S OWN COMMENT.  Unindented, the panic line is STILL
    #    refused -- by the space after the verb, not by the indent skip.  So A2 passes with the indent
    #    guard removed and is NOT a test of it.  Asserted here so the claim cannot drift back.
    a, _ = parse_driver_output("FAIL: the implementation panicked\n")
    check("A3 space-guard refuses the panic line", a, {})
    # A3b ⛔ THE ARM THAT EXPOSED THE DEAD GUARD.  It was written to prove the indent skip was
    #     load-bearing; it passed with the skip DELETED, because `^` already refuses a leading space.
    #     Kept as a characterisation of the anchor -- and as the record that a deletion drive, not a
    #     passing arm, is what establishes that a guard does anything.
    a, _ = parse_driver_output("  FAIL beta\n")
    check("A3b the ^ anchor refuses a well-formed indented line", a, {})
    # A4 a driver that reports nothing (did not build): no arms, no tests -- NOT a kill
    a, t = parse_driver_output("error: could not compile\n")
    check("A4 empty", (a, t), ({}, None))
    # A5 TESTS is anchored: CLAUSE_TESTS must not be read as the totals line
    a, t = parse_driver_output("CLAUSE_TESTS 9/9\nTESTS 3/4\n")
    check("A5 anchored totals", t, (3, 4))
    # A6 ⛔ THE ARM THAT CAUSED THE BUG.  It asserted "names containing spaces survive intact" -- a
    #    shape NO driver in this campaign emits -- and that invented requirement is what licensed the
    #    capture-to-end-of-line that swallowed FAIL detail into the name.
    #    ⇒ A SELFTEST BUILT ON AN IMAGINED OUTPUT SHAPE CONSTRAINS THE PARSER AGAINST THE REAL ONE.
    #    Replaced with the real shape, pasted from a live Crc32 run.
    a, _ = parse_driver_output(
        'PASS check_value\n'
        'FAIL check_value  [FAIL: the check value "123456789" (9 bytes): expected 0xcbf43926, got 0x2ac0a892]\n')
    check("A6 trailing detail is not part of the name", a, {"check_value": False})
    # A7 and the PASS form of the same arm must key identically, which is the equality the sweep needs
    p1, _ = parse_driver_output("PASS check_value\n")
    f1, _ = parse_driver_output("FAIL check_value  [FAIL: detail]\n")
    check("A7 PASS and FAIL key the same arm", (sorted(p1), sorted(f1)), (["check_value"], ["check_value"]))

    for f in fails:
        print("  RED  " + f)
    print("selftest: %d arm(s), %d failed" % (8, len(fails)))
    return 1 if fails else 0


def run_one(runner, source):
    """Run the withheld driver over `source` staged as solution.rs. Returns (rc, {arm: bool}, tests)."""
    tmp = tempfile.mkdtemp(prefix="armcov.")
    try:
        shutil.copyfile(source, os.path.join(tmp, "solution.rs"))
        p = subprocess.run([runner, tmp], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        arms, tests = parse_driver_output(p.stdout)
        return p.returncode, arms, tests
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def sweep_task(root, task):
    g = os.path.join(root, task, "G")
    runner = os.path.join(g, "run_tests.sh")
    ref = os.path.join(g, "withheld", "reference", "solution.rs")
    mdir = os.path.join(g, "withheld", "mutants")
    for p in (runner, ref, mdir):
        if not os.path.exists(p):
            return {"task": task, "reading": "NOT MEASURED", "why": "missing %s" % os.path.basename(p)}

    rc, ref_arms, ref_tests = run_one(runner, ref)
    if rc != 0 or not ref_arms:
        # ⛔ THE SUITE IS INVALID ON ITS OWN REFERENCE.  Every column below would be unreadable:
        # an arm that fails everywhere is not discriminating, it is broken.  Refuse the task.
        return {"task": task, "reading": "INVALID",
                "why": "the withheld suite does not pass its own reference (rc=%d, %s)" % (rc, ref_tests)}

    mutants = sorted(f for f in os.listdir(mdir) if f.endswith(".rs"))
    matrix, unmeasured = {}, []
    for m in mutants:
        rc, arms, _ = run_one(runner, os.path.join(mdir, m))
        name = m[:-3]
        if not arms:
            # no per-arm lines at all: the mutant did not build or the driver died before reporting.
            # ⛔ THIS IS NOT A KILL.  Counting a non-building mutant as killed is how a suite scores
            # 1.000 without running.
            unmeasured.append(name)
            continue
        matrix[name] = arms

    all_arms = sorted(ref_arms)
    rows = {a: sorted(m for m in matrix if matrix[m].get(a) is False) for a in all_arms}
    cols = {m: sorted(a for a in all_arms if matrix[m].get(a) is False) for m in matrix}
    return {
        "task": task, "reading": "MEASURED",
        "arms": all_arms, "reference_tests": ref_tests,
        "mutants_measured": sorted(matrix), "mutants_unmeasured": unmeasured,
        "kills_by_arm": rows, "killers_by_mutant": cols,
        "dead_arms": [a for a in all_arms if not rows[a]],
        "survivors": [m for m in cols if not cols[m]],
        "margin_1": [m for m in cols if len(cols[m]) == 1],
    }


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(64)
    if a[0] == "--selftest":
        sys.exit(selftest())
    root = a[0]
    tasks = TASKS
    out = None
    if "--tasks" in a:
        tasks = a[a.index("--tasks") + 1].split(",")
    if "--json" in a:
        out = a[a.index("--json") + 1]
    if not os.path.isdir(root):
        refuse("no referee task tree at the given path")
    missing = [n for n in TOOLCHAIN if not os.environ.get(n)]
    if missing:
        refuse("%s not set (the six-name toolchain contract)" % ", ".join(missing))

    results = [sweep_task(root, t) for t in tasks]
    bad = False
    for r in results:
        print("=" * 78)
        if r["reading"] != "MEASURED":
            print("%-9s %s -- %s" % (r["task"], r["reading"], r["why"]))
            bad = True
            continue
        p, t = r["reference_tests"]
        print("%-9s MEASURED   arms %d   reference TESTS %d/%d   mutants %d measured, %d unmeasured"
              % (r["task"], len(r["arms"]), p, t, len(r["mutants_measured"]), len(r["mutants_unmeasured"])))
        if r["mutants_unmeasured"]:
            print("  ⛔ UNMEASURED (did not build or died before reporting; NOT counted as kills): %s"
                  % ", ".join(r["mutants_unmeasured"]))
        print("  ROW READING -- mutants killed by each arm (0 = DEAD ARM):")
        for arm in r["arms"]:
            k = r["kills_by_arm"][arm]
            print("    %-34s %d  %s" % (arm, len(k), "⛔ DEAD" if not k else ", ".join(k)))
        print("  COLUMN READING -- arms killing each mutant (1 = the kill rests on ONE arm):")
        for m in r["mutants_measured"]:
            k = r["killers_by_mutant"][m]
            flag = "⛔ SURVIVES" if not k else ("⚠️ MARGIN 1" if len(k) == 1 else "")
            print("    %-34s %d  %s %s" % (m, len(k), ", ".join(k), flag))
        if r["survivors"]:
            bad = True
    print("=" * 78)
    ok = [r for r in results if r["reading"] == "MEASURED"]
    print("SWEEP: %d of %d task(s) measured · %d DEAD ARM(S) · %d MARGIN-1 MUTANT(S) · %d SURVIVOR(S)"
          % (len(ok), len(results),
             sum(len(r["dead_arms"]) for r in ok),
             sum(len(r["margin_1"]) for r in ok),
             sum(len(r["survivors"]) for r in ok)))
    print("⛔ A KILL RATE OVER MUTANTS CANNOT SEE A DEAD ARM: the arm sits in the TESTS denominator,")
    print("   never in the score's numerator.  That is why this is a MATRIX and not a rate.")
    if out:
        json.dump(results, open(out, "w"), indent=1)
        print("raw matrix -> %s" % out)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
