#!/usr/bin/env python3
"""l7_tripwire_gate.py <cell-dir> [--json] | --selftest

THE §L7 TRIPWIRE GATE of AMENDMENT-gemini-brownfield-level4-2026-09-13.

⛔ WHY THIS EXISTS. §L7 is the ONE thing in the level-4 freeze that is NOT
self-executing: a lead reads five fields off the first cell and writes the gate
result back into the freeze before cells 2..24 fire. Everything else in that
amendment runs without a person. A step that needs a person is a step that gets
done from memory, under time pressure, by whoever is awake -- so the branches
are encoded here, from the frozen text, BEFORE the cell lands.

⇒ 🔑 A GATE WRITTEN AFTER SEEING THE DATA IS NOT A GATE. This file is committed
  while `b4lzs01` is still running and its verdict cannot be tuned afterwards
  without that showing up in the history of this file.

THE FIVE FIELDS, AND WHERE THEY ACTUALLY LIVE (located at a landed cell, not
recalled -- the two files are written together at every terminal outcome):

    T                 ctl/agy-meter-1.json     .T
    commands_run      ctl/agy-meter-1.json     .commands_run
    done_reason       ctl/agy-turnloop-1.json  .done_reason
    wall_seconds      ctl/agy-turnloop-1.json  .wall_seconds
    turns_no_output   ctl/agy-turnloop-1.json  .turns_no_output

⛔ THE LANDING SIGNAL IS `agy-turnloop-1.json`, NEVER `ctl/end-1`. The end
marker carries the PERSISTENCE PROBE's verdict, not the cell's -- this desk has
a banked card on exactly that confusion. Censused over every agy cell on the
run box, the turnloop file is present at all five terminal outcomes
(79 LANDED / 14 TURN-TIMEOUT / 2 NO-FIRST-RESULT / 1 TURN-CAP /
1 SUBJECT-DECLARED-DONE, n=97), so keying on it cannot go quiet on a timeout --
which is the branch §L7 says to fire ON rather than hold on.

⛔⛔ THE AMBIGUITY THIS FILE HAD TO RESOLVE, FOUND BY ENCODING THE TABLE.
§L7's four rows read as though exactly one can fire. They are NOT mutually
exclusive:
  · CAP-TOKENS necessarily implies T at the 250M cap, hence T >= 50M -- those
    two rows ALWAYS co-occur, in every possible run.
  · TURN-TIMEOUT can co-occur with T >= 50M, and the two rows then give
    OPPOSITE instructions: "DO NOT HOLD" against "HOLD".
⇒ PRECEDENCE, DECLARED HERE BEFORE ANY DATA EXISTS:

    1  CAP-TOKENS      -> REGISTER-RESULT   (a brownfield cell does not fit in
                                             250M; register before any cap moves)
    2  T >= 50M        -> HOLD-AND-REDERIVE (in the file; never silently raise
                                             a cap and re-fire)
    3  TURN-TIMEOUT    -> FIRE-AND-REPORT   (fire the remaining 23, report the
                                             incidence; it was already 19%)
    4  otherwise       -> FIRE-UNCHANGED

AND THE REASONING, so it can be attacked rather than just obeyed: §L7's
TURN-TIMEOUT row says do not hold ON THE TIMEOUT, because holding there would
void a wave on a PREDICTION. It does not license ignoring a separate,
quantitative token finding. So a cell that is BOTH holds on the token reading
AND reports the timeout -- the two actions compose, they do not conflict.
`report_timeout` is therefore an INDEPENDENT FLAG, not a branch, and it is set
whenever done_reason is TURN-TIMEOUT no matter which verdict won.

⛔ A cell that is not terminal REFUSES (rc 3). "Not landed yet" and "landed with
no findings" must never share an exit code.
"""
import json, os, sys

TRIPWIRE_T = 50_000_000          # §L7. A TRIPWIRE, NOT A CAP. Nothing is capped here.
REGISTERED_CAP_T = 250_000_000   # pricing's T1_TOK, for context in the printout only.

VERDICTS = {
    "REGISTER-RESULT":   "a brownfield cell does not fit in the registered 250M. Register the reading and the reason BEFORE any cap moves.",
    "HOLD-AND-REDERIVE": "T is at or above the 50M tripwire. HOLD cells 2..24 and re-derive the number IN THE FREEZE. Never silently raise a cap and re-fire.",
    "FIRE-AND-REPORT":   "fire the remaining 23 and REPORT the TURN-TIMEOUT incidence. Do NOT hold: it was already 19% in greenfield's treatment arm and holding would void a wave on a prediction.",
    "FIRE-UNCHANGED":    "the expected case. Fire the remaining 23 unchanged; this needs no further word from the lead.",
}


def read_cell(cell):
    """Return (meter, turnloop) or raise RuntimeError naming what is missing."""
    meter_p = os.path.join(cell, "ctl", "agy-meter-1.json")
    turn_p = os.path.join(cell, "ctl", "agy-turnloop-1.json")
    missing = [p for p in (meter_p, turn_p) if not os.path.exists(p)]
    if missing:
        raise RuntimeError(
            "cell is NOT TERMINAL (or is not an agy cell): missing "
            + ", ".join(os.path.relpath(m, cell) for m in missing)
            + ". The turnloop file is written at EVERY terminal outcome, so its "
              "absence means the cell has not finished -- it is not a reading.")
    with open(meter_p) as f:
        meter = json.load(f)
    with open(turn_p) as f:
        turn = json.load(f)
    return meter, turn


def gate(meter, turn):
    """The §L7 branches, in the precedence declared in this file's docstring."""
    T = meter.get("T")
    done = turn.get("done_reason")
    commands_run = meter.get("commands_run")
    if T is None or done is None:
        raise RuntimeError("a required field is absent: T=%r done_reason=%r. "
                           "An absent field is never read as a passing value." % (T, done))
    report_timeout = (done == "TURN-TIMEOUT")
    # ⛔⛔ THE DEGENERATE CELL, FOUND BY DRIVING THIS GATE AGAINST REAL CELLS AND NOT
    # AGAINST ITS OWN FIXTURES. A real terminal cell on this box reads
    # T=0, commands_run=0, wall_seconds=0.2, done_reason=TURN-TIMEOUT -- it died
    # before doing anything. Every §L7 branch below would have happily read
    # T=0 < 50M and returned FIRE-AND-REPORT, firing 23 cells on a tripwire that
    # MEASURED NOTHING.
    # ⇒ 🔑 THIS IS §G7's DEFECT WEARING A DIFFERENT HAT: a probe that comes back
    #   actionable while testing nothing. §G7 put the tripwire on the arm that never
    #   trips the cap; this would accept a cell that never ran. Both read GREEN.
    # ⇒ A tripwire that spent no tokens and ran no commands is NOT a reading about a
    #   token cap. It REFUSES, and the wave re-fires the tripwire rather than the 23.
    if T == 0 and (commands_run or 0) == 0:
        raise RuntimeError(
            "DEGENERATE cell: T=0 and commands_run=0 (done_reason=%s, wall_seconds=%s). "
            "The cell terminated without spending tokens or running commands, so it says "
            "NOTHING about the token cap the tripwire exists to check. This is not a §L7 "
            "reading -- re-fire the TRIPWIRE, do not fire cells 2..24 on it." % (done, turn.get("wall_seconds")))
    if done == "CAP-TOKENS":
        v = "REGISTER-RESULT"
    elif T >= TRIPWIRE_T:
        v = "HOLD-AND-REDERIVE"
    elif report_timeout:
        v = "FIRE-AND-REPORT"
    else:
        v = "FIRE-UNCHANGED"
    return {
        "verdict": v,
        "action": VERDICTS[v],
        "report_timeout": report_timeout,
        "T": T,
        "done_reason": done,
        "wall_seconds": turn.get("wall_seconds"),
        "turns_no_output": turn.get("turns_no_output"),
        "commands_run": meter.get("commands_run"),
        "tripwire_T": TRIPWIRE_T,
        "registered_cap_T": REGISTERED_CAP_T,
        "T_margin_vs_cap": (REGISTERED_CAP_T / T) if T else None,
    }


def selftest():
    def m(T, cr=1):
        return {"T": T, "commands_run": cr}

    def t(done, wall=1.0, tno=0):
        return {"done_reason": done, "wall_seconds": wall, "turns_no_output": tno}

    arms, bad = [], []

    def ck(label, got, want):
        arms.append(label)
        ok = got == want
        if not ok:
            bad.append(label)
        print("  %-4s %s%s" % ("ok" if ok else "FAIL", label,
                               "" if ok else "   got %r want %r" % (got, want)))

    # the four §L7 rows, each alone
    ck("LANDED under the tripwire -> FIRE-UNCHANGED",
       gate(m(8_572_636), t("LANDED"))["verdict"], "FIRE-UNCHANGED")
    ck("T at or above 50M -> HOLD-AND-REDERIVE",
       gate(m(TRIPWIRE_T), t("LANDED"))["verdict"], "HOLD-AND-REDERIVE")
    ck("  and one token BELOW the tripwire still fires (the boundary is >=)",
       gate(m(TRIPWIRE_T - 1), t("LANDED"))["verdict"], "FIRE-UNCHANGED")
    ck("TURN-TIMEOUT under the tripwire -> FIRE-AND-REPORT, never a hold",
       gate(m(1_000_000), t("TURN-TIMEOUT"))["verdict"], "FIRE-AND-REPORT")
    ck("CAP-TOKENS -> REGISTER-RESULT",
       gate(m(REGISTERED_CAP_T), t("CAP-TOKENS"))["verdict"], "REGISTER-RESULT")

    # ⭐ THE OVERLAPS -- the rows §L7 does not say are exclusive, and they are not
    ck("OVERLAP CAP-TOKENS also has T>=50M by construction; CAP-TOKENS wins",
       gate(m(REGISTERED_CAP_T), t("CAP-TOKENS"))["verdict"], "REGISTER-RESULT")
    ck("OVERLAP TURN-TIMEOUT *and* T>=50M -> the HOLD wins",
       gate(m(60_000_000), t("TURN-TIMEOUT"))["verdict"], "HOLD-AND-REDERIVE")
    ck("  ⭐ and the timeout is STILL REPORTED -- the flag is independent of the verdict",
       gate(m(60_000_000), t("TURN-TIMEOUT"))["report_timeout"], True)
    ck("  and a non-timeout hold does NOT raise the report flag",
       gate(m(60_000_000), t("LANDED"))["report_timeout"], False)

    # the other terminal outcomes seen in the census are not special-cased, and say so
    for dr in ("NO-FIRST-RESULT", "TURN-CAP", "SUBJECT-DECLARED-DONE"):
        ck("%s under the tripwire -> FIRE-UNCHANGED (not a §L7 branch)" % dr,
           gate(m(1_000), t(dr))["verdict"], "FIRE-UNCHANGED")

    # ⭐ RED arms for the DEGENERATE cell -- the shape a REAL cell on the box has,
    # and the one the fixtures never produced
    for label, mm, tt, want_refuse in (
        ("RED DEGENERATE T=0 commands_run=0 REFUSES (would have been FIRE-AND-REPORT)",
         m(0, cr=0), t("TURN-TIMEOUT", wall=0.2, tno=1), True),
        ("  and T=0 with commands_run>0 is NOT degenerate -- it still reads",
         m(0, cr=5), t("TURN-TIMEOUT", wall=0.2, tno=1), False),
        ("  and a healthy cell is untouched by the guard (positive control)",
         m(8_572_636, cr=71), t("LANDED"), False),
    ):
        arms.append(label)
        try:
            gate(mm, tt)
            if want_refuse:
                bad.append(label)
                print("  FAIL %s   it returned a verdict instead of refusing" % label)
            else:
                print("  ok   %s" % label)
        except RuntimeError:
            if want_refuse:
                print("  ok   %s" % label)
            else:
                bad.append(label)
                print("  FAIL %s   it refused a cell it should have read" % label)

    # RED arms: absence must refuse, never pass
    for label, mm, tt in (
        ("RED absent T REFUSES", {"commands_run": 1}, t("LANDED")),
        ("RED absent done_reason REFUSES", m(1), {"wall_seconds": 1.0}),
    ):
        arms.append(label)
        try:
            gate(mm, tt)
            bad.append(label)
            print("  FAIL %s   it returned a verdict instead of refusing" % label)
        except RuntimeError:
            print("  ok   %s" % label)

    # RED arm: a non-terminal cell refuses at the READ, not at the gate
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "ctl"))
        label = "RED a cell with no turnloop file REFUSES (not landed != landed clean)"
        arms.append(label)
        try:
            read_cell(d)
            bad.append(label)
            print("  FAIL %s" % label)
        except RuntimeError:
            print("  ok   %s" % label)
        # POSITIVE CONTROL: the same directory, once both files exist, reads fine
        with open(os.path.join(d, "ctl", "agy-meter-1.json"), "w") as f:
            json.dump(m(123), f)
        with open(os.path.join(d, "ctl", "agy-turnloop-1.json"), "w") as f:
            json.dump(t("LANDED"), f)
        label = "  POSITIVE CONTROL: the same dir with both files present READS"
        arms.append(label)
        try:
            mm, tt = read_cell(d)
            ok = gate(mm, tt)["verdict"] == "FIRE-UNCHANGED"
            if not ok:
                bad.append(label)
            print("  %-4s %s" % ("ok" if ok else "FAIL", label))
        except RuntimeError as e:
            bad.append(label)
            print("  FAIL %s   %s" % (label, e))

    print("l7_tripwire_gate --selftest: %d of %d passed" % (len(arms) - len(bad), len(arms)))
    return 1 if bad else 0


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if not argv:
        print(__doc__.strip().splitlines()[0], file=sys.stderr)
        return 64
    as_json = "--json" in argv
    cell = [a for a in argv if not a.startswith("--")][0]
    try:
        meter, turn = read_cell(cell)
        out = gate(meter, turn)
    except RuntimeError as e:
        print("l7_tripwire_gate: REFUSE -- %s" % e, file=sys.stderr)
        return 3
    out["cell"] = os.path.abspath(cell)
    if as_json:
        print(json.dumps(out, indent=1, sort_keys=True))
        return 0
    print("§L7 TRIPWIRE READ -- %s" % out["cell"])
    for k in ("T", "done_reason", "wall_seconds", "turns_no_output", "commands_run"):
        print("  %-16s %s" % (k, out[k]))
    # ⛔ NEVER FORMAT A MARGIN THAT MAY NOT EXIST. The first real-cell drive of this
    # file crashed HERE with a TypeError on a T=0 cell -- AFTER printing the five
    # fields and BEFORE printing the verdict, so the operator saw data and no verdict,
    # at an rc that was neither the 0 of a reading nor the 3 of a refusal.
    mg = out["T_margin_vs_cap"]
    print("  %-16s %s" % ("margin vs cap",
                          ("%.2fx (registered cap %d / T)" % (mg, REGISTERED_CAP_T))
                          if mg is not None else "n/a (T is 0)"))
    print("VERDICT  %s" % out["verdict"])
    print("ACTION   %s" % out["action"])
    if out["report_timeout"] and out["verdict"] != "FIRE-AND-REPORT":
        print("ALSO     ⛔ TURN-TIMEOUT occurred and is REPORTED independently of the verdict above.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
