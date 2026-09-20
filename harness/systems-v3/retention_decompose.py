#!/usr/bin/env python3
"""retention_decompose.py --harness <dir> --tasks <tasks-root> (--declared <file> | <cell> ...)
                          [--out <tsv>] | --selftest

Emit `surv` and `growth` beside `retained` for brownfield cells, as level 8 ADDENDUM 6 registers.

    retained  difflib's line-level similarity ratio of the END file against the SEED  (§B5, UNCHANGED)
    surv      seed lines MATCHED by that same differ / seed lines
    growth    end lines / seed lines

⛔ WHY THIS EXISTS. `retained` is SYMMETRIC IN ADDITIONS AND DELETIONS, and §B5's words are about
   REWRITING — "present and rewritten wholesale" vs "present and EDITED" — which is a claim about what
   SURVIVED. Measured on two lanes on 2026-09-19, the separation `retained` reports is GROWTH: block SB's
   two arms have the SAME survival range (0.420–0.990 vs 0.419–0.995) and disjoint growth (0.96x–1.18x vs
   3.92x–14.70x), and level 7's published 7-of-8 direction is 3-of-8 on survival, flipping on half the pairs.
   ⇒ These two columns let a reader see which one a separation is made of. They are REPORTED, not registered
   as separators: NO threshold, NO class, NO band, NO direction claim (ADDENDUM 6 §A6.1).

⛔ IT DOES NOT REIMPLEMENT THE CLASSIFIER, IT IMPORTS IT, and asserts its own `retained` EQUALS
   `classify()`'s on EVERY row — refusing the whole run otherwise. A reimplementation would diverge on
   `autojunk`, on the end-file choice (working tree if dirty, else HEAD) and on the seed path, and each of
   those produced a wrong table during this tool's own construction.

⛔⛔ THE TASKS ROOT IS THE EXPORT THE CELLS WERE **BUILT FROM**, AND THAT IS NOT ALWAYS THE TREE THAT
   CARRIES THE SUITES. On 2026-09-19 those were two different exports with COMPLEMENTARY content, and
   pointing this at the suite tree made 18 of 30 cells read `class REFUSED` — which reading rule §241
   item 6 would have entered in the census as `VOID(GIVEN)`, a finding against the harness. ⇒ **Pass the
   BUILD export. If a cell REFUSES with `W2 ctl/seed-sha … != W1 task seed …`, suspect the tree before the cell.**
⛔ AND A TASKS ROOT IS NOT RELOCATABLE: each rung's `_common.sh` sources `../../../../harness/...`, four
   levels up and OUT of the tasks tree. A composed tasks tree runs nothing; a composed EXPORT does.

LIMITS (they ride with the verdict, printed at every run):
   · `surv` counts lines the differ MATCHED, so it is a LOWER BOUND on survival — a moved line may not match.
   · it reads cells READ-ONLY and re-runs nothing; it cannot tell you the cells are what they claim to be.
   · it makes no claim about what any of the three numbers MEANS.
"""
import argparse, csv, difflib, os, sys

def decompose(classifier, cell, tasks_root):
    """-> dict. Raises AssertionError if our `retained` and classify()'s disagree."""
    r = classifier.classify(cell, tasks_root)
    cid = os.path.basename(os.path.realpath(cell))
    if r["err"]:
        return {"cell": cid, "task": "-", "class": "REFUSED", "retained": "-", "surv": "-", "growth": "-",
                "seed_lines": "-", "end_lines": "-", "kept": "-", "end_from": "-", "err": r["err"]}
    sb, _ss, _bad, _w1 = classifier.seed_witnesses(cell, tasks_root)
    eb, where = classifier.end_text(os.path.join(cell, "repo"))
    s = sb.decode("utf-8", "replace").splitlines()
    e = eb.decode("utf-8", "replace").splitlines()
    sm = difflib.SequenceMatcher(None, s, e, autojunk=False)
    kept = sum(b.size for b in sm.get_matching_blocks())
    assert abs(sm.ratio() - r["retained"]) < 1e-9, (
        "%s: our ratio %.12f != classify()'s %.12f — the differ configuration has diverged from the "
        "classifier's and no row of this run may be trusted" % (cid, sm.ratio(), r["retained"]))
    return {"cell": cid, "task": classifier.task_name(cell), "class": r["cls"],
            "retained": "%.3f" % r["retained"], "surv": "%.3f" % (kept / len(s)),
            "growth": "%.2f" % (len(e) / len(s)), "seed_lines": str(len(s)), "end_lines": str(len(e)),
            "kept": str(kept), "end_from": where, "err": ""}

COLS = ["cell", "task", "class", "retained", "surv", "growth", "seed_lines", "end_lines", "kept", "end_from", "err"]

def run(harness, tasks, cells, out):
    sys.path.insert(0, harness)
    import brownfield_rewrite_class as B
    w = csv.writer(out, delimiter="\t", lineterminator="\n")
    out.write("# retention_decompose.py — surv and growth beside retained (level 8 ADDENDUM 6)\n")
    out.write("# harness %s\n# tasks   %s   <- MUST be the export the cells were BUILT from\n" % (harness, tasks))
    out.write("# every `retained` below is ASSERTED EQUAL to brownfield_rewrite_class.classify()'s own value\n")
    out.write("# surv is a LOWER BOUND on survival: it counts lines the differ MATCHED\n")
    w.writerow(COLS)
    n = ref = 0
    for c in cells:
        row = decompose(B, c, tasks)
        ref += row["class"] == "REFUSED"; n += 1
        w.writerow([row[k] for k in COLS])
    return n, ref

def selftest():
    """Red-first. ⛔ IT DOES NOT TEST THE CLASSIFIER — that has its own selftest and this imports it.
    What it tests is THIS file's arithmetic, its assertion, and its refusal path, against a STUB."""
    import types
    N = [0, 0]
    def arm(label, ok, shown=""):
        N[0] += 1; N[1] += 0 if ok else 1
        print("  %s  %s%s" % ("ok  " if ok else "RED ", label, ("   [%s]" % shown) if shown else ""))

    def stub(seed, end, ratio=None, err=""):
        m = types.SimpleNamespace()
        sm = difflib.SequenceMatcher(None, seed, end, autojunk=False)
        m.classify = lambda c, t: {"err": err, "cls": "REPAIRED", "retained": sm.ratio() if ratio is None else ratio}
        m.seed_witnesses = lambda c, t: ("\n".join(seed).encode(), "x", [], ("p", "COVERED"))
        m.end_text = lambda repo: ("\n".join(end).encode(), "HEAD")
        m.task_name = lambda c: "T"
        return m

    seed = ["a%d" % i for i in range(100)]
    same = list(seed)
    grown = list(seed) + ["proof%d" % i for i in range(500)]        # EVERY seed line kept, 6x the file
    cut = seed[:20]                                                  # 80 lines deleted, nothing added

    r = decompose(stub(seed, same), "/c", "/t")
    arm("an UNTOUCHED file: surv 1.000, growth 1.00", (r["surv"], r["growth"]) == ("1.000", "1.00"))
    r = decompose(stub(seed, grown), "/c", "/t")
    arm("⭐ THE CASE THE WHOLE TOOL EXISTS FOR — every seed line kept, file 6x: surv 1.000",
        r["surv"] == "1.000", "surv %s growth %s retained %s" % (r["surv"], r["growth"], r["retained"]))
    arm("   and `retained` is DRAGGED DOWN by the growth alone", float(r["retained"]) < 0.5,
        "retained %s on a file that deleted NOTHING" % r["retained"])
    arm("   so the two columns disagree, which is the signal", float(r["surv"]) > float(r["retained"]) * 2)
    r = decompose(stub(seed, cut), "/c", "/t")
    arm("a file with 80 of 100 lines DELETED and nothing added: surv 0.200", r["surv"] == "0.200",
        "surv %s growth %s" % (r["surv"], r["growth"]))
    arm("   growth is below 1 when the file shrank", float(r["growth"]) < 1.0)
    r = decompose(stub(seed, grown, err="W2 ctl/seed-sha aa != W1 task seed bb"), "/c", "/t")
    arm("⭐ A REFUSAL IS PASSED THROUGH WITH ITS REASON, never silently scored",
        r["class"] == "REFUSED" and "W2" in r["err"] and r["surv"] == "-")
    bad = False
    try:
        decompose(stub(seed, grown, ratio=0.5), "/c", "/t")
    except AssertionError as e:
        bad = "diverged" in str(e)
    arm("⭐ RED: a classifier whose `retained` DISAGREES with ours raises and stops the run", bad)
    arm("   ...and the CONTROL: the same stub with the true ratio does NOT raise",
        decompose(stub(seed, grown), "/c", "/t")["class"] == "REPAIRED")
    arm("the column order is fixed and the header names every one", len(COLS) == len(set(COLS)) == 11)
    print("\n%d arms, %d RED" % (N[0], N[1]))
    print("LIMITS: this selftest exercises THIS file only — the classifier is imported and has its own.")
    print("        `surv` is a LOWER BOUND: it counts MATCHED lines, and a moved line may not match.")
    return 1 if N[1] else 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--harness"); ap.add_argument("--tasks")
    ap.add_argument("--declared", help="a file naming one cell directory per line; never a glob")
    ap.add_argument("--out"); ap.add_argument("--selftest", action="store_true")
    ap.add_argument("cells", nargs="*")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if not (a.harness and a.tasks):
        ap.error("--harness and --tasks are required")
    cells = list(a.cells)
    if a.declared:
        cells += [l.strip() for l in open(a.declared) if l.strip()]
    if not cells:
        ap.error("no cells: pass them as arguments or with --declared")
    out = open(a.out, "w") if a.out else sys.stdout
    n, ref = run(a.harness, a.tasks, cells, out)
    if a.out: out.close()
    sys.stderr.write("retention_decompose: %d cell(s), %d REFUSED\n" % (n, ref))
    sys.stderr.write("LIMITS: `surv` is a LOWER BOUND (matched lines only) · cells read READ-ONLY, nothing "
                     "re-run · no claim is made about what these numbers MEAN (ADDENDUM 6 §A6.1)\n")
    if ref:
        sys.stderr.write("⛔ %d REFUSED: suspect the --tasks tree before the cells. It must be the export the "
                         "cells were BUILT from, which is not always the tree carrying the suites.\n" % ref)
    sys.exit(0)

if __name__ == "__main__":
    main()
