#!/usr/bin/env python3
"""RESULT-claude-blockO-2026-09-21-verify.py [--doc D] [--table T] [--selftest]

Re-derive every figure in RESULT-claude-blockO-2026-09-21.md FROM the table of record, and assert it
against the BYTES of that document. Idiom law clause 1: no typed expectations — each expected value is
COMPUTED from the TSV, then required to be PRESENT in the prose.

⛔ IT CANNOT SEE A FIELD THE TABLE DOES NOT CARRY. Block SB's verifier was green and accurate about
  everything it could reach while the model attribution was wrong, because the table had no model
  column. This table has one (column 25) and the model IS asserted below.
rc 0 all figures re-derived and found · 1 a mismatch, named · 2 usage."""
import csv, collections, statistics, sys, os, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(HERE, "RESULT-claude-blockO-2026-09-21.md")
TBL = os.path.join(HERE, "..", "..", "evidence", "claude-lane-blocks-2026-09-21", "blockO-cells.tsv")

def load(table):
    return [r for r in csv.DictReader(
        (l for l in open(table, encoding="utf-8") if not l.startswith("#")), delimiter="\t")]

def checks(rows):
    """-> list of (label, string-that-must-appear-in-the-doc). Every value COMPUTED."""
    out = []
    A = lambda arm: [r for r in rows if r["arm"] == arm]
    out.append(("n", "n=%d" % len(rows)))
    out.append(("model", sorted({r["model_served"] for r in rows})[0]))
    rs = collections.Counter(r["run_state"] for r in rows)
    out.append(("landed", "ENDED: LANDED %d" % rs["ENDED: LANDED"]))
    out.append(("capcost", "ENDED: CAP-COST %d" % rs["ENDED: CAP-COST"]))
    out.append(("suite", "PASS %d of %d" % (sum(1 for r in rows if r["suite"] == "PASS"), len(rows))))
    out.append(("fenced", "COVERED %d of %d" % (sum(1 for r in rows if r["w1_fenced"] == "COVERED"), len(rows))))
    for arm in ("plain", "salt-diet"):
        a = A(arm)
        ret = [float(r["retained"]) for r in a]; sv = [float(r["surv"]) for r in a]
        gr = [float(r["growth"]) for r in a]; c = [float(r["final_COST"]) for r in a]
        T = [int(r["final_T"]) for r in a]; el = [int(r["end_lines"]) for r in a]
        out.append((arm + " retained", "%.3f .. %.3f" % (min(ret), max(ret))))
        out.append((arm + " surv", "%.3f .. %.3f" % (min(sv), max(sv))))
        out.append((arm + " growth", "%.2fx .. %5.2fx" % (min(gr), max(gr))))
        out.append((arm + " medianCOST", "$%.2f" % statistics.median(c)))
        out.append((arm + " totalCOST", "$%.2f" % sum(c)))
        out.append((arm + " totalT", format(sum(T), ",")))
        out.append((arm + " end_lines", "%s" % format(max(el), ",") if max(el) >= 1000 else str(max(el))))
        cl = collections.Counter(r["class"] for r in a)
        out.append((arm + " REPAIRED", "REPAIRED %d" % cl["REPAIRED"]) if cl["REPAIRED"] else ("skip", ""))
    cap = [r for r in rows if r["capped"] == "yes"]
    if cap:
        out.append(("capped cell", cap[0]["cell"]))
        out.append(("capped cost", "$%.2f" % float(cap[0]["final_COST"])))
        out.append(("cap value", "$%.2f" % float(cap[0]["cap"])))
    return [(l, v) for l, v in out if v]

def run(doc, table):
    rows = load(table)
    text = open(doc, encoding="utf-8").read()
    bad = []
    for label, val in checks(rows):
        probe = val.replace("  ", " ")
        if val not in text and probe not in text:
            bad.append((label, val))
    print("block O verifier: %d cell(s), %d figure(s) re-derived from the table" % (len(rows), len(checks(rows))))
    if bad:
        print("⛔ %d FIGURE(S) NOT FOUND IN THE DOCUMENT:" % len(bad))
        for l, v in bad: print("   %-22s expected in prose: %r" % (l, v))
        return 1
    print("✅ every re-derived figure is present in the document's bytes.")
    return 0

def selftest():
    """RED-BACKWARDS: the fix is already in, so mutate the DOC and require the arm to redden."""
    import tempfile, shutil, re
    rows = load(TBL)
    text = open(DOC, encoding="utf-8").read()
    fails = []
    with tempfile.TemporaryDirectory() as d:
        t2 = os.path.join(d, "t.tsv"); shutil.copy(TBL, t2)
        d0 = os.path.join(d, "d.md"); shutil.copy(DOC, d0)
        rc = run(d0, t2)
        print("  arm 1 control (unmutated)                 rc=%d  %s" % (rc, "PASS" if rc == 0 else "FAIL"))
        if rc != 0: fails.append(1)
        # mutate the SUITE claim in the prose
        m = re.sub(r"PASS 30 of 30", "PASS 29 of 30", text, count=1)
        assert m != text, "arm 2 fixture did not mutate"
        open(d0, "w", encoding="utf-8").write(m)
        rc = run(d0, t2)
        print("  arm 2 mutant: suite claim wrong in prose  rc=%d  %s" % (rc, "PASS" if rc == 1 else "FAIL"))
        if rc != 1: fails.append(2)
        # mutate the MODEL claim — the field block SB's verifier could not see
        m = text.replace("claude-opus-5", "claude-sonnet-5")
        assert m != text, "arm 3 fixture did not mutate"
        open(d0, "w", encoding="utf-8").write(m)
        rc = run(d0, t2)
        print("  arm 3 mutant: MODEL wrong in prose        rc=%d  %s" % (rc, "PASS" if rc == 1 else "FAIL"))
        if rc != 1: fails.append(3)
    print()
    if fails:
        print("⛔ SELFTEST FAILED on arm(s) %s" % fails); return 1
    print("✅ SELFTEST 3/3 — control green, and a wrong SUITE figure and a wrong MODEL each redden it.")
    return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc", default=DOC); ap.add_argument("--table", default=TBL)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else run(a.doc, a.table))
