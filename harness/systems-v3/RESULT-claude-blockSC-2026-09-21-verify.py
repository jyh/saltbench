#!/usr/bin/env python3
"""RESULT-claude-blockSC-2026-09-21-verify.py [--doc D] [--table T] [--selftest]

Re-derive every figure in block SC's result FROM the table of record and assert it against the BYTES of
that document. Idiom law clause 1: NO TYPED EXPECTATIONS — every expected value is COMPUTED from the TSV
and then required to be PRESENT in the prose.

⛔ BLOCK SC IS THE LANE'S FIRST SPEC-CHANGE BLOCK AND ITS TABLE IS A DIFFERENT SHAPE, so this verifier is
  NOT blockOS's with the name changed. A spec-change row is a PAIR of phases: 29 columns, `p1_`/`p2_`
  prefixes, per-phase T and COST that come from each phase's OWN harvest, and `cell_T_at_end2` which is
  CUMULATIVE over the cell. ⇒ THE ONE MISTAKE THIS FILE EXISTS TO MAKE IMPOSSIBLE is quoting the
  cumulative figure as if it were phase 2's: they differ by phase 1's whole cost, and both are plausible.

⛔ IT CANNOT SEE A FIELD THE TABLE DOES NOT CARRY. Block SB's verifier was green and accurate about
  everything it could reach while the model attribution was wrong, because the table had no model column.
  This table has one and the model IS asserted below — and if the table was built without --served-dir the
  column is EMPTY and DECLARED so in the table's own header, which this verifier REFUSES rather than
  silently passing over (a blank model is the ADDENDUM 12 defect).

rc 0 every figure re-derived and found · 1 a mismatch, named · 2 usage."""
import csv, collections, statistics, sys, os, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(HERE, "RESULT-claude-blockSC-2026-09-21.md")
TBL = os.path.join(HERE, "..", "..", "evidence", "claude-lane-blocks-2026-09-21", "blockSC-cells.tsv")

def load(table):
    return [r for r in csv.DictReader(
        (l for l in open(table, encoding="utf-8") if not l.startswith("#")), delimiter="\t")]

def declared_blank_model(table):
    """The table declares its own unpopulated model column; a verifier must not pass over it."""
    with open(table, encoding="utf-8") as f:
        return any(l.startswith("# model_served UNPOPULATED") for l in f)

def end2_is_cumulative(r):
    """Is this row's end-2 meter the WHOLE cell, or phase 2 alone? (desk VV)

    ⛔⛔ MY FIRST CUT OF THIS TEST WAS `cell_T_at_end2 < p1_T` — "a cumulative cannot be smaller than the
      phase 1 it contains." That is SOUND and it is NOT SUFFICIENT: driven on the real block it caught
      clbcls02 and MISSED clbclp03, whose phase-2-only meter happens to be LARGER than its phase 1
      (1,791,691 vs 1,397,336). ⇒ 🔑 A TEST THAT CATCHES THE SUBSET IT CAN *PROVE* READS AS CATCHING THE
      CLASS, and it fails in the flattering direction: 1 of 2 named, with no sign that the other exists.

    ✅ THE TEST USED INSTEAD IS A COMPARISON, NOT A THRESHOLD, so nothing is fitted to the run it judges
      (card `saltbench-a-gate-fitted-to-its-own-data-is-not-a-gate`): a cumulative meter should sit near
      p1+p2 and a phase-2-only meter near p2, so ASK WHICH IT IS CLOSER TO. Driven on the 5 complete SC
      pairs it classifies 5 of 5 correctly, including the one the sound-but-partial test missed.
    """
    p1, p2, e2 = int(r["p1_T"]), int(r["p2_T"]), int(r["cell_T_at_end2"])
    return abs(e2 - (p1 + p2)) <= abs(e2 - p2)

def checks(rows):
    """-> list of (label, string-that-must-appear-in-the-doc). Every value COMPUTED, none typed."""
    out = []
    A = lambda arm: [r for r in rows if r["arm"] == arm]
    out.append(("n", "n=%d" % len(rows)))
    out.append(("model", sorted({r["model_served"] for r in rows})[0]))
    for ph in ("p1", "p2"):
        rs = collections.Counter(r[ph + "_run_state"] for r in rows)
        for state, k in rs.items():
            out.append(("%s %s" % (ph, state), "%s %d" % (state, k)))
        sc = collections.Counter(r[ph + "_suite"] for r in rows)
        out.append((ph + " suite", "%s PASS %d of %d" % (ph, sc["PASS"], len(rows))))
    for arm in ("plain", "salt-diet"):
        a = A(arm)
        if not a:
            continue
        out.append((arm + " n", "%s n=%d" % (arm, len(a))))
        for ph in ("p1", "p2"):
            T = [int(r[ph + "_T"]) for r in a]
            C = [float(r[ph + "_COST"]) for r in a]
            out.append(("%s %s totalT" % (arm, ph), format(sum(T), ",")))
            out.append(("%s %s totalCOST" % (arm, ph), "$%.2f" % sum(C)))
            out.append(("%s %s medianCOST" % (arm, ph), "$%.2f" % statistics.median(C)))
        # ⛔⛔ THE CUMULATIVE COLUMN IS NOT ASSERTED, AND THAT IS DESK `VV`, MEASURED ON THIS BLOCK.
        #   `cell_*_at_end2` is CUMULATIVE for a cell whose two phases ran on ONE pool and PHASE-2-ONLY
        #   for a cell that crossed pools (5 of 5 over the first complete SC pairs; clbcls02's end-2 COST
        #   is 2.46 against its own end-1 of 4.58, which a cumulative cannot be). ⇒ SUMMING IT ACROSS A
        #   BLOCK UNDERSTATES THE BLOCK, and every value in it is a believable number.
        #   ⚠️ THIS VERIFIER ALMOST CERTIFIED THAT DEFECT: it asserted the summed column and was 6/6 green.
        #   A verifier that faithfully re-derives a WRONG column and finds it faithfully reproduced in the
        #   prose is GREEN AND WRONG. ⇒ 🔑 AN INSTRUMENT INHERITS ITS SOURCE'S DEFECTS AND CALLS THEM FACTS.
        pass
    capped = [r for r in rows if r["p1_capped"] == "yes" or r["p2_capped"] == "yes"]
    out.append(("capped", "capped %d" % len(capped)))
    return [(l, v) for l, v in out if v]

def run(doc, table):
    rows = load(table)
    if not rows:
        print("⛔ the table carries no data rows — an empty table is not a green verification"); return 1
    if declared_blank_model(table):
        print("⛔ the table DECLARES `model_served UNPOPULATED` — it was joined without --served-dir. "
              "The model cannot be verified, and a blank model column is the ADDENDUM 12 defect. "
              "Re-join with --served-dir before verifying."); return 1
    # ⛔ DESK `VV`, AND THE CHECK NEEDS NO MECHANISM: a genuine cumulative CANNOT be smaller than the
    #   phase-1 total it contains. Any row failing this has a phase-2-only end-2 meter, so no cumulative
    #   figure over this block may be quoted at all — and the verifier says which rows, not merely that.
    noncum = [r["cell"] for r in rows if not end2_is_cumulative(r)]
    if noncum:
        # ⛔ THE MESSAGE NAMES THE TEST THAT ACTUALLY RAN. It said `cell_T_at_end2 < p1_T` after that
        #   test had been replaced, which is the label-is-not-the-instrument defect in one line of prose.
        print("⚠️  %d of %d row(s) have a NON-CUMULATIVE end-2 meter (it sits nearer p2_T than p1_T+p2_T): %s"
              % (len(noncum), len(rows), ", ".join(noncum)))
        print("   Desk VV: the column is cumulative only when a cell's two phases ran on ONE pool. The "
              "per-phase harvest figures (p1_*, p2_*) are the sound ones and are asserted below; NO "
              "cumulative figure is re-derived, and the document must not quote one.")
    text = open(doc, encoding="utf-8").read()
    ck = checks(rows)
    bad = [(l, v) for l, v in ck if v not in text and v.replace("  ", " ") not in text]
    print("block SC verifier: %d PAIR(s), %d figure(s) re-derived from the table" % (len(rows), len(ck)))
    if bad:
        print("⛔ %d FIGURE(S) NOT FOUND IN THE DOCUMENT:" % len(bad))
        for l, v in bad: print("   %-26s expected in prose: %r" % (l, v))
        return 1
    print("✅ every re-derived figure is present in the document's bytes.")
    return 0

def selftest():
    """⭐ RED BACKWARDS (jas's law): there is no defect left to fail against, so MUTATE and require a redden.
    The doc is SYNTHESISED from the table, so the control cannot pass by accident of wording."""
    import tempfile
    fails = []
    with tempfile.TemporaryDirectory() as d:
        t = os.path.join(d, "t.tsv"); dc = os.path.join(d, "d.md")
        cols = ["cell","problem","arm","field","extras","model_served",
                "p1_run_state","p1_suite","p1_tests","p1_w1_fenced","p1_T","p1_COST","p1_cap_unit","p1_cap","p1_capped",
                "p2_run_state","p2_suite","p2_tests","p2_regressions","p2_clause_tests","p2_V1","p2_V2",
                "p2_T","p2_COST","p2_cap_unit","p2_cap","p2_capped","cell_T_at_end2","cell_COST_at_end2"]
        def row(cell, arm, t1, c1, t2, c2):
            v = dict.fromkeys(cols, "-")
            v.update(cell=cell, problem="LRU", arm=arm, field="greenfield", extras="none",
                     model_served="claude-sonnet-5", p1_run_state="ENDED: LANDED", p1_suite="PASS",
                     p1_T=str(t1), p1_COST="%.2f" % c1, p1_capped="no",
                     p2_run_state="ENDED", p2_suite="PASS", p2_T=str(t2), p2_COST="%.2f" % c2,
                     p2_capped="no", cell_T_at_end2=str(t1 + t2),
                     cell_COST_at_end2="%.2f" % (c1 + c2))
            return v
        rows = [row("clbclp01","plain",2271920,1.23,2120082,1.07),
                row("clbclp02","plain",1525617,0.71,1785445,0.79),
                row("clbcls01","salt-diet",23086119,7.33,8475379,2.96)]
        with open(t,"w",encoding="utf-8") as f:
            f.write("\t".join(cols)+"\n")
            for r in rows: f.write("\t".join(r[c] for c in cols)+"\n")
        base = "block SC\n" + "\n".join("%s :: %s" % (l, v) for l, v in checks(load(t))) + "\n"
        open(dc,"w",encoding="utf-8").write(base)
        rc = run(dc, t); print("  arm 1 control (doc carries every figure)      rc=%d  %s" % (rc,"PASS" if rc==0 else "FAIL"))
        if rc != 0: fails.append(1)

        # ⭐ THE ARM THIS FILE EXISTS FOR: the CUMULATIVE cost quoted where phase 2's belongs.
        p2 = "$%.2f" % sum(float(r["p2_COST"]) for r in rows if r["arm"]=="plain")
        cum = "$%.2f" % sum(float(r["cell_COST_at_end2"]) for r in rows if r["arm"]=="plain")
        assert p2 != cum, "fixture is vacuous: the two figures are equal"
        open(dc,"w",encoding="utf-8").write(base.replace(p2, cum, 1))
        rc = run(dc, t); print("  arm 2 mutant: cumulative quoted as phase 2   rc=%d  %s" % (rc,"PASS" if rc==1 else "FAIL"))
        if rc != 1: fails.append(2)

        open(dc,"w",encoding="utf-8").write(base.replace("claude-sonnet-5","claude-opus-5"))
        rc = run(dc, t); print("  arm 3 mutant: MODEL wrong in prose          rc=%d  %s" % (rc,"PASS" if rc==1 else "FAIL"))
        if rc != 1: fails.append(3)

        open(dc,"w",encoding="utf-8").write(base.replace("n=3","n=2",1))
        rc = run(dc, t); print("  arm 4 mutant: n wrong in prose              rc=%d  %s" % (rc,"PASS" if rc==1 else "FAIL"))
        if rc != 1: fails.append(4)

        # arm 5: a table joined WITHOUT --served-dir must be REFUSED, not passed over
        t5 = os.path.join(d,"t5.tsv")
        with open(t5,"w",encoding="utf-8") as f:
            f.write("# model_served UNPOPULATED\tno --served-dir was given\tdeclared\n")
            f.write("\t".join(cols)+"\n")
            for r in rows: f.write("\t".join(r[c] for c in cols)+"\n")
        open(dc,"w",encoding="utf-8").write(base)
        rc = run(dc, t5); print("  arm 5 table with UNPOPULATED model declared rc=%d  %s" % (rc,"PASS" if rc==1 else "FAIL"))
        if rc != 1: fails.append(5)

        # ⭐ arm 7 (desk VV): a row whose end-2 meter is PHASE-2-ONLY must be NAMED. Placed because a
        #   guard nobody drives is the defect this shift kept finding in other people's work; it would be
        #   absurd to ship one here untested. It is a WARNING, not a refusal — the per-phase figures are
        #   still sound and still verifiable — so the arm asserts the NAME appears and rc stays 0.
        import io, contextlib
        t7 = os.path.join(d, "t7.tsv")
        r7 = [dict(x) for x in rows]
        r7[0]["cell_T_at_end2"] = str(int(r7[0]["p2_T"]))     # the cross-pool shape: end-2 == phase 2 alone
        # ⛔ NOTE THE FIXTURE ROW: clbclp01 has p2_T > p1_T, so end-2 == p2 is LARGER than p1 and the
        #   old `e2 < p1_T` test would NOT have fired here. This arm therefore pins the real clbclp03
        #   shape, not the easy clbcls02 one.
        with open(t7, "w", encoding="utf-8") as f:
            f.write("\t".join(cols) + "\n")
            for r in r7: f.write("\t".join(r[c] for c in cols) + "\n")
        open(dc, "w", encoding="utf-8").write(base)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf): rc = run(dc, t7)
        got = buf.getvalue()
        named = r7[0]["cell"] in got and "NON-CUMULATIVE" in got
        print("  arm 7 phase-2-only end-2 meter is NAMED       rc=%d  %s" % (rc, "PASS" if (rc == 0 and named) else "FAIL"))
        if not (rc == 0 and named): fails.append(7)
        # ⭐ arm 8, the CONTROL for arm 7: an all-cumulative table must NOT raise it (else arm 7 is vacuous)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf): rc = run(dc, t)
        quiet = "NON-CUMULATIVE" not in buf.getvalue()
        print("  arm 8 CONTROL all-cumulative stays quiet     rc=%d  %s" % (rc, "PASS" if (rc == 0 and quiet) else "FAIL"))
        if not (rc == 0 and quiet): fails.append(8)

        # arm 6: an EMPTY table is not a green verification
        t6 = os.path.join(d,"t6.tsv"); open(t6,"w",encoding="utf-8").write("\t".join(cols)+"\n")
        rc = run(dc, t6); print("  arm 6 empty table is not a pass             rc=%d  %s" % (rc,"PASS" if rc==1 else "FAIL"))
        if rc != 1: fails.append(6)
    print()
    if fails: print("⛔ SELFTEST FAILED on arm(s) %s" % fails); return 1
    print("✅ SELFTEST 8/8 — control green; a cumulative-for-phase-2 swap, a wrong model, a wrong n, an\n"
          "   undeclarable model column and an empty table each redden it; a phase-2-only end-2 meter is\n"
          "   NAMED (desk VV) and an all-cumulative table stays quiet, so that arm is not vacuous.")
    return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc", default=DOC); ap.add_argument("--table", default=TBL)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else run(a.doc, a.table))
