#!/usr/bin/env python3
"""od_d9_result.py [--print | --check <doc> | --selftest] [--cells <tsv>] — desk OD's block RESULT (§D9) lines, derived from the 27-row
cells table and nothing else (AMENDMENT-OD-effort-matrix-2026-10-16.md §D4, §D5, §D9; ADDENDA 5 and 7 for the labels).

  table     evidence/od-effort-matrix/od-d9-cells.tsv (default): 27 registered rows keyed on ROOT + CELL, each HARVESTED or OWED
  --print   the derived lines. ⛔ UNTIL ALL 27 ARE HARVESTED it prints the per-cell readings and ONE withholding line, and NO condition
            row, ceiling reading or prediction: the registration reads the block at n = 3 per condition, and a partial median is not one.
  --check   rc 0 iff every derived line occurs in <doc>; rc 1 names each missing line.
  --selftest  red-first arms on the real table and on in-memory fixtures (below). A verifier that cannot fail is decoration.

No expected value is typed here. The literals are the registration's: the configuration and problem ORDER (§D0 row 1, §D1), each
configuration's registered head (§D0 row 1, R1.3), n = 3 (§D0 row 2), P3's 1.2 (§D5), and §P4's interval rule with ADDENDUM 1's strict
separation (REGISTRATION-correctness-tables-v3-2026-10-01.md), which P2 and P4 name.
"""
import csv, os, statistics, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CELLS = os.path.join(ROOT, "evidence/od-effort-matrix/od-d9-cells.tsv")
CONFIGS = ["FX", "FH", "OX"]                                           # §D0 row 1
PROBLEMS = ["Crc32", "LZW", "FreeList"]                                # §D1
HEAD = {"FX": "claude-fable-5-1", "FH": "claude-fable-5-1", "OX": "claude-opus-5-5"}   # §D0 row 1 · R1.3 (F3')
N = 3                                                                  # §D0 row 2
P3_RATIO = 1.2                                                         # §D5 P3


def read_tsv(path):
    return list(csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t"))


def klass(c):   # §D4 / §P2 classes; the landing claim never decides one
    if c["suite"].startswith("PASS"):
        return "PASS"
    if "CAP" in c["run_state"]:
        return "CENSORED"
    if c["suite"].startswith("FAIL"):
        return "FAIL"
    return "UNSCORABLE"


def interval(cells):   # §P4: [pass / n, (pass + censored + unscorable) / n]
    k = [klass(c) for c in cells]
    p, open_ = k.count("PASS"), k.count("CENSORED") + k.count("UNSCORABLE")
    return Fraction(p, len(k)), Fraction(p + open_, len(k))


def sign(a, b):   # §P4 with ADDENDUM 1: STRICT separation; a shared endpoint is "?"
    if a[0] > b[1]:
        return "+"
    if a[1] < b[0]:
        return "-"
    if a[0] == a[1] == b[0] == b[1]:
        return "="
    return "?"


def validate(cells):
    keys = [(c["root"], c["cell"]) for c in cells]
    if len(cells) != 27 or len(set(keys)) != 27:
        raise SystemExit("REFUSE: the table is not 27 distinct (root, cell) rows (got %d rows, %d distinct)" % (len(cells), len(set(keys))))
    for k in CONFIGS:
        for p in PROBLEMS:
            if sum(1 for c in cells if c["config"] == k and c["problem"] == p) != N:
                raise SystemExit("REFUSE: condition %s × %s does not hold %d registered rows" % (k, p, N))
    for c in cells:
        if not c["root"].startswith("cells-clb-%s-" % c["config"].lower()):
            raise SystemExit("REFUSE: row %s/%s is not in its configuration's root" % (c["root"], c["cell"]))


def derive(cells):
    validate(cells)
    L = []
    h = [c for c in cells if c["status"] == "HARVESTED"]
    L.append("registered 27 · harvested %d · owed %d" % (len(h), 27 - len(h)))
    for p in PROBLEMS:
        for k in CONFIGS:
            for c in sorted((c for c in h if c["problem"] == p and c["config"] == k), key=lambda c: int(c["n"])):
                hid = c["served_head"].partition("=")[0]
                clean = "clean" if (c["served_verdict"].startswith("clean:") and hid == HEAD[k] and c["argv_model"] == HEAD[k]) else "NOT-CLEAN"
                L.append("%-8s %s#%s %s/%s  %s  --effort %s  head %s %s  T %s  output %s  list-USD $%s  wall %ss  escape %s" % (
                    p, k, c["n"], c["root"], c["cell"], klass(c), c["argv_effort"], c["served_head"], clean,
                    format(int(c["T"]), ","), format(int(c["output"]), ","), c["list_usd"], c["wall_s"], c["escape_hits"]))
    if len(h) < 27:
        L.append("COMPARISON WITHHELD: %d of 27 harvested; no condition row, ceiling reading or prediction until all 27 are in (§D9)" % len(h))
        return L
    by = {(p, k): [c for c in cells if c["problem"] == p and c["config"] == k] for p in PROBLEMS for k in CONFIGS}
    med = lambda cs, f: statistics.median(float(c[f]) for c in cs)
    for p in PROBLEMS:
        for k in CONFIGS:
            cs = by[(p, k)]; lo, hi = interval(cs)
            L.append("%-8s %s  PASS %d/%d  interval [%s, %s]  median T %s  median output %s  median list-USD $%.2f  median wall %ss  CAP-COST %d" % (
                p, k, sum(klass(c) == "PASS" for c in cs), N, lo, hi, format(int(med(cs, "T")), ","), format(int(med(cs, "output")), ","),
                med(cs, "list_usd"), int(med(cs, "wall_s")), sum("CAP-COST" in c["run_state"] for c in cs)))
    ceiling = {}
    for p in PROBLEMS:
        full = [k for k in CONFIGS if all(klass(c) == "PASS" for c in by[(p, k)])]
        ceiling[p] = len(full) == len(CONFIGS)
        for a, b in (("FX", "FH"), ("OX", "FX")):
            r = "NO INFORMATION (ceiling, R1)" if (a in full and b in full) else "sign %s" % sign(interval(by[(p, a)]), interval(by[(p, b)]))
            L.append("ability %-8s %s vs %s: %s" % (p, a, b, r))
    mo = {(p, k): med(by[(p, k)], "output") for p in PROBLEMS for k in CONFIGS}
    p1 = sum(mo[(p, "FX")] > mo[(p, "FH")] for p in PROBLEMS)
    L.append("P1 FX median output > FH's on %d of 3 problems: %s" % (p1, "MET" if p1 >= 2 else "NOT MET"))
    scor = [p for p in PROBLEMS if not ceiling[p]]
    if not scor:
        L.append("P2 NOT SCORED (every problem at 3/3, R1)")
        L.append("P4 NOT SCORED (every problem at 3/3, R1)")
    else:
        s2 = {p: sign(interval(by[(p, "FX")]), interval(by[(p, "FH")])) for p in scor}
        L.append("P2 on %s: %s" % (",".join(scor), "NOT MET" if "-" in s2.values() else "MET") + " (FX vs FH signs %s)" % " ".join("%s %s" % kv for kv in s2.items()))
        s4 = {p: sign(interval(by[(p, "OX")]), interval(by[(p, "FX")])) for p in scor}
        L.append("P4 on %s: %s" % (",".join(scor), "MET" if all(v == "=" for v in s4.values()) else "NOT MET") + " (OX vs FX signs %s)" % " ".join("%s %s" % kv for kv in s4.items()))
    rat = {p: mo[(p, "FX")] / mo[(p, "FH")] for p in PROBLEMS}
    L.append("P3 FX/FH median output ratio %s: %s" % (" · ".join("%s %.2f" % (p, rat[p]) for p in PROBLEMS),
                                                      "MET" if all(r > P3_RATIO for r in rat.values()) else "NOT MET"))
    capped = sum("CAP-COST" in c["run_state"] for c in cells)
    L.append("P5 CAP-COST bound %d cell(s): %s" % (capped, "MET" if capped == 0 else "NOT MET"))
    return L


def fixture_complete(cells):
    """the 9 real harvested rows cloned into the 18 OWED slots, IN MEMORY ONLY, so the full path can be driven before it has data."""
    h = {c["config"]: c for c in cells if c["status"] == "HARVESTED"}
    out = []
    for c in cells:
        if c["status"] == "OWED":
            d = dict(h[c["config"]]); d.update(root=c["root"], cell=c["cell"], problem=c["problem"], n=c["n"]); out.append(d)
        else:
            out.append(dict(c))
    return out


def selftest(cells):
    bad = 0
    def arm(name, ok):
        nonlocal bad
        print("  %s %s" % ("ok  " if ok else "FAIL", name)); bad += not ok
    try:
        real = derive(cells)
    except Exception as e:   # a partial table that reaches the median code CRASHES; that is the defect this arm names
        real = ["CRASH: %r" % e]
    arm("the real table (%d harvested) WITHHOLDS: one withholding line, no condition row, no ceiling, no prediction" % sum(c["status"] == "HARVESTED" for c in cells),
        any(l.startswith("COMPARISON WITHHELD") for l in real) and not any(l.startswith(("P1", "P2", "P3", "P4", "P5", "ability")) or "median T" in l for l in real))
    full = derive(fixture_complete(cells))
    arm("a complete fixture prints 9 condition rows, 6 ability rows and P1–P5",
        sum("median T" in l for l in full) == 9 and sum(l.startswith("ability") for l in full) == 6 and all(any(l.startswith(p) for l in full) for p in ("P1", "P2", "P3", "P4", "P5")))
    m = fixture_complete(cells); [c.update(suite="FAIL 5/6") for c in m if c["cell"] == "clbhzp01"]
    mf = derive(m)
    arm("mutant: one LZW FH cell FAILs -> LZW FH reads 2/3 and LZW's FX-vs-FH ability is a SIGN, not NO INFORMATION",
        any(l.startswith("LZW      FH  PASS 2/3") for l in mf) and any(l.startswith("ability LZW      FX vs FH: sign") for l in mf))
    arm("mutant (same): P2 and P4 are SCORED on LZW, the one problem below the ceiling, and on no other",
        any(l.startswith("P2 on LZW:") for l in mf) and any(l.startswith("P4 on LZW:") for l in mf))
    for name, mut in (("a duplicate (root, cell)", lambda t: t[:26] + [dict(t[0])]),
                      ("a lane-B row named clbwcp01 in another root", lambda t: t[:26] + [dict(t[26], root="cells-clb-x86w-crc32-plain", cell="clbwcp01")]),
                      ("a row dropped", lambda t: t[:26])):
        try:
            derive(mut([dict(c) for c in cells])); arm("REFUSES %s" % name, False)
        except SystemExit:
            arm("REFUSES %s" % name, True)
    m2 = fixture_complete(cells); [c.update(run_state="ENDED: CAP-COST", suite="FAIL 0/6") for c in m2 if c["cell"] == "clbxfp03"]
    arm("mutant: a capped FX FreeList cell -> P5 NOT MET and that cell is CENSORED (interval upper bound includes it)",
        any(l.startswith("P5 CAP-COST bound 1") and l.endswith("NOT MET") for l in derive(m2)) and any(l.startswith("FreeList FX  PASS 2/3  interval [2/3, 1]") for l in derive(m2)))
    # §P4 ADDENDUM 1's own example: plain 2/3 uncensored [2/3, 2/3] against k = 2, n = 2, c = 1 [2/3, 1] SHARES an endpoint -> "?", never a sign
    arm("sign(): touching intervals read ? (ADDENDUM 1, strict); separated read +/-; equal points read =",
        sign((Fraction(2, 3), Fraction(1)), (Fraction(2, 3), Fraction(2, 3))) == "?" and sign((Fraction(1), Fraction(1)), (Fraction(1, 3), Fraction(2, 3))) == "+"
        and sign((Fraction(0), Fraction(1, 3)), (Fraction(2, 3), Fraction(1))) == "-" and sign((Fraction(1), Fraction(1)), (Fraction(1), Fraction(1))) == "=")
    return 1 if bad else 0


def main():
    a = sys.argv[1:]
    path = a[a.index("--cells") + 1] if "--cells" in a else CELLS
    cells = read_tsv(path)
    if "--selftest" in a:
        return selftest(cells)
    lines = derive(cells)
    if "--check" in a:
        doc = open(a[a.index("--check") + 1], encoding="utf-8").read()
        miss = [l for l in lines if l not in doc]
        for l in miss:
            print("MISSING: " + l)
        print("CHECK %s: %d derived lines, %d missing" % ("GREEN" if not miss else "RED", len(lines), len(miss)))
        return 1 if miss else 0
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
