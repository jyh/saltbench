#!/usr/bin/env python3
"""RESULT-gemini-blockNA-2026-09-28-prose-verify.py [--print | --selftest] — re-derive every figure line of the block NA
result PROSE (`RESULT-gemini-blockNA-2026-09-28.md`) from the hand's per-cell table of record
(`RESULT-gemini-blockNA-2026-09-28-cells.tsv`), and assert each line against the document's bytes.

This is the LEAD's verifier of the lead's prose. The hand's `RESULT-gemini-blockNA-2026-09-28-verify.py` verifies the TABLE
against its receipts; this one verifies that the prose says what the table says. They are two instruments on two claims.

--print     print the derived lines (the document quotes them verbatim)
default     rc 0 iff every derived line occurs in the document, rc 1 otherwise, naming each missing line
--selftest  two mutants must go RED: one in-n PASS turned FAIL, and the outside-n cell admitted into n. The unmutated check GREEN.

No expected value is typed here. The only literals are the registered problem ORDER (§NA2 = block N §N3) and the column names.
"""
import csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CELLS = os.path.join(HERE, "RESULT-gemini-blockNA-2026-09-28-cells.tsv")
DOC = os.path.join(HERE, "RESULT-gemini-blockNA-2026-09-28.md")
ORDER = ["Luby", "AES", "Liveness", "MaxFlow", "BinomialHeap", "LinearScan"]
ARMS = ["plain", "salt-diet"]


def read():
    return list(csv.DictReader((l for l in open(CELLS, encoding="utf-8") if not l.startswith("#")), delimiter="\t"))


def derive(rows):
    L = []
    inn = [r for r in rows if r["in_registered_n"] == "yes"]
    out = sorted(r["id"] for r in rows if r["in_registered_n"] != "yes")
    L.append("cells in n %d · outside n %d (%s) · conditions %d" % (
        len(inn), len(out), " ".join(out), len({(r["served"], r["cond"]) for r in inn})))
    L.append("exports %s · task trees vs e54f35a %s · x86-concurrent cells %d" % (
        " ".join(sorted({r["export_sha"][:7] for r in inn})),
        " ".join("%s %d" % (k, sum(r["tree_vs_e54f35a"] == k for r in inn)) for k in sorted({r["tree_vs_e54f35a"] for r in inn})),
        sum(r["x86_concurrent"] not in ("none", "0", "", "-") for r in inn)))
    dr = {}
    for r in inn: dr[r["done_reason"]] = dr.get(r["done_reason"], 0) + 1
    L.append("done_reason " + " · ".join("%s %d" % (k, dr[k]) for k in sorted(dr)))
    for model in sorted({r["served"] for r in inn}):
        m = [r for r in inn if r["served"] == model]
        L.append("== %s: %d cells" % (model, len(m)))
        for p in ORDER:
            parts = []
            for a in ARMS:
                c = sorted((r for r in m if r["problem"] == p and r["arm"] == a), key=lambda r: r["id"])
                scored = [r for r in c if r["verdict"] in ("PASS", "FAIL")]
                full = sum(r["verdict"] == "PASS" for r in scored)
                tr = sum(r["truncated"] == "yes" for r in c)
                nl = sum(r["non_landing"] != "-" for r in c)
                parts.append("%s %d/%d scored of %d fired [%s] trunc %d%s" % (
                    a, full, len(scored), len(c), " ".join(r["TESTS"] if r["TESTS"] != "-" else r["verdict"] for r in c), tr,
                    (" non-landing %d" % nl) if nl else ""))
            L.append("  %-12s %s" % (p, " · ".join(parts)))
        for a in ARMS:
            c = [r for r in m if r["arm"] == a]
            scored = [r for r in c if r["verdict"] in ("PASS", "FAIL")]
            L.append("  %s %s FULL PASS %d of %d scored · cut turns %d of %d sent · truncated cells %d of %d · cells with any cut %d" % (
                model, a, sum(r["verdict"] == "PASS" for r in scored), len(scored),
                sum(int(r["cut_turns"]) for r in c), sum(int(r["turns_sent"]) for r in c),
                sum(r["truncated"] == "yes" for r in c), len(c), sum(int(r["cut_turns"]) > 0 for r in c)))
        inc = {p: {a: sum(int(r["cut_turns"]) > 0 for r in m if r["problem"] == p and r["arm"] == a) for a in ARMS} for p in ORDER}
        held = sum(inc[p]["salt-diet"] >= inc[p]["plain"] for p in ORDER)
        L.append("  (i) %s: salt-diet cells-with-a-cut >= plain in %d of %d problems (%d strictly)" % (
            model, held, len(ORDER), sum(inc[p]["salt-diet"] > inc[p]["plain"] for p in ORDER)))
        for a in ARMS:
            seq = [inc[p][a] for p in ORDER]
            L.append("  (ii) %s %s cells-with-a-cut in reference-size order %s · non-decreasing %s" % (
                model, a, " ".join(map(str, seq)), "yes" if all(x <= y for x, y in zip(seq, seq[1:])) else "NO"))
    wall = sorted((r for r in inn if r["done_reason"] != "LANDED"), key=lambda r: r["id"])
    L.append("not LANDED by done_reason: " + " · ".join("%s %s %.0f s %s" % (r["id"], r["done_reason"], float(r["wall_s"]), r["verdict"]) for r in wall))
    return L


def check(lines, doc):
    return [l for l in lines if l not in doc]


def main():
    rows = read()
    if "--print" in sys.argv:
        print("\n".join(derive(rows))); return 0
    doc = open(DOC, encoding="utf-8").read()
    if "--selftest" in sys.argv:
        m1 = [dict(r) for r in rows]
        i = next(i for i, r in enumerate(m1) if r["verdict"] == "PASS" and r["in_registered_n"] == "yes")
        m1[i]["verdict"] = "FAIL"
        m2 = [dict(r) for r in rows]
        for r in m2:
            if r["in_registered_n"] != "yes": r["in_registered_n"] = "yes"
        r1, r2, g = check(derive(m1), doc), check(derive(m2), doc), check(derive(rows), doc)
        print("selftest: PASS->FAIL (%s) %s · outside-n admitted %s · unmutated %s" % (
            m1[i]["id"], "RED" if r1 else "GREEN (DEFECT)", "RED" if r2 else "GREEN (DEFECT)", "GREEN" if not g else "RED"))
        return 0 if (r1 and r2 and not g) else 1
    miss = check(derive(rows), doc)
    for l in miss: print("MISSING from the document: " + l)
    print("prose-verify: %d derived line(s), %d missing" % (len(derive(rows)), len(miss)))
    return 1 if miss else 0


if __name__ == "__main__":
    sys.exit(main())
