#!/usr/bin/env python3
"""RESULT-claude-OD-identity-2026-10-17-verify.py [--print | --selftest] — re-derive every figure line of the desk OD identity
result FROM ITS CELLS TABLE, and assert each derived line against the BYTES of the result document.

  table     evidence/od-identity-triple-2026-10-17/od-identity-cells.tsv   (5 rows: the re-run triple and the two 2.1.259 readings)
  document  harness/systems-v3/RESULT-claude-OD-identity-2026-10-17.md

--print     print the derived lines (the document quotes them verbatim) and exit 0.
default     rc 0 iff every derived line occurs in the document; rc 1 names each one that does not.
--selftest  two mutants, each must go RED: one cell's suite turned FAIL in memory, and an identity-only cell counted among the matrix
            cells; then the unmutated check must be GREEN. A verifier that cannot fail is decoration.

No expected value is typed here. The only literals are the registered configuration ORDER (AMENDMENT OD §D0 row 1) and the
registered head per configuration (§D0 row 1, ADDENDUM 1 R1.3), which the check compares the SERVED head against.
"""
import csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CELLS = os.path.join(ROOT, "evidence/od-identity-triple-2026-10-17/od-identity-cells.tsv")
DOC = os.path.join(HERE, "RESULT-claude-OD-identity-2026-10-17.md")

ORDER = ["FX", "FH", "OX"]                                                      # §D0 row 1
HEAD = {"FX": "claude-fable-5-1", "FH": "claude-fable-5-1", "OX": "claude-opus-5-5"}   # §D0 row 1 · R1.3 (F3')


def read_tsv(path):
    return list(csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t"))


def mmss(s):
    s = int(s)
    return "%dm%02ds" % (s // 60, s % 60)


def derive(cells):
    L = []
    mat = [c for c in cells if c["role"] == "matrix"]
    idn = [c for c in cells if c["role"] == "identity-only"]
    L.append("cells %d · matrix %d (client %s) · identity-only %d (client %s)" % (
        len(cells), len(mat), ",".join(sorted({c["client"] for c in mat})), len(idn), ",".join(sorted({c["client"] for c in idn}))))
    for role, rows in (("matrix", mat), ("identity-only", idn)):
        for k in ORDER:
            for c in [c for c in rows if c["config"] == k]:
                hid, _, hn = c["served_head"].partition("=")
                ok = "clean" if (c["served_verdict"].startswith("clean:") and hid == HEAD[k] and c["argv_model"] == HEAD[k]) else "NOT-CLEAN"
                L.append("%-13s %s#%s %s  argv --model %s --effort %s  served head %s ×%s %s  sidechain %s" % (
                    role, k, c["n"], c["cell"], c["argv_model"], c["argv_effort"], hid, hn, ok, c["served_sidechain"]))
    for role, rows in (("matrix", mat), ("identity-only", idn)):
        for k in ORDER:
            for c in [c for c in rows if c["config"] == k]:
                L.append("%-13s %s#%s  %s  %s  T %s  output %s  list-USD $%s  wall %s  escape %s" % (
                    role, k, c["n"], c["run_state"], c["suite"], format(int(c["T"]), ","), format(int(c["output"]), ","),
                    c["list_usd"], mmss(c["wall_s"]), c["escape_hits"]))
    L.append("matrix total T %s · output %s · list-USD $%.2f · suites %s" % (
        format(sum(int(c["T"]) for c in mat), ","), format(sum(int(c["output"]) for c in mat), ","),
        sum(float(c["list_usd"]) for c in mat), " ".join(sorted({c["suite"] for c in mat}))))
    return L


def check(lines, doc):
    return [l for l in lines if l not in doc]


def main():
    cells = read_tsv(CELLS)
    if "--print" in sys.argv:
        print("\n".join(derive(cells)))
        return 0
    doc = open(DOC, encoding="utf-8").read()
    if "--selftest" in sys.argv:
        bad = 0
        m1 = [dict(c) for c in cells]; m1[2]["suite"] = "FAIL 5/6"
        m2 = [dict(c) for c in cells]; m2[0]["role"] = "matrix"
        for name, m in (("a suite turned FAIL", m1), ("an identity-only cell counted as matrix", m2)):
            red = bool(check(derive(m), doc))
            print("  %s mutant: %s" % ("ok  " if red else "FAIL", name + (" -> RED" if red else " -> still GREEN")))
            bad += not red
        g = check(derive(cells), doc)
        print("  %s unmutated -> %s" % ("ok  " if not g else "FAIL", "GREEN" if not g else "RED"))
        return 1 if (bad or g) else 0
    miss = check(derive(cells), doc)
    for l in miss:
        print("MISSING: " + l)
    print("VERIFY %s: %d derived lines, %d missing" % ("GREEN" if not miss else "RED", len(derive(cells)), len(miss)))
    return 1 if miss else 0


if __name__ == "__main__":
    sys.exit(main())
