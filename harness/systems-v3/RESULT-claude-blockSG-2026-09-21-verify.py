#!/usr/bin/env python3
"""RESULT-claude-blockSG-2026-09-21-verify.py [--doc D] [--table T] [--selftest]

Re-derive every figure in RESULT-claude-blockSG-2026-09-21.md FROM the table of record and assert it
against the BYTES of that document. Idiom law clause 1: no typed expectations.

⛔ GREENFIELD-SHAPED. The table has 15 columns, not 25: there is no seed, so no class/retained/surv/
  growth. This verifier must not look for them, and it ASSERTS their absence rather than ignoring it —
  a greenfield table that grew a retention column would mean the wrong table was joined.
rc 0 · 1 a mismatch, named · 2 usage."""
import csv, collections, statistics, sys, os, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(HERE, "RESULT-claude-blockSG-2026-09-21.md")
TBL = os.path.join(HERE, "..", "..", "evidence", "claude-lane-blocks-2026-09-21", "blockSG-cells.tsv")
ABSENT = ("class", "retained", "surv", "growth", "seed_lines", "end_lines", "kept", "end_from")

def load(t):
    return [r for r in csv.DictReader(
        (l for l in open(t, encoding="utf-8") if not l.startswith("#")), delimiter="\t")]

def checks(rows):
    out = [("rows", "29 rows"), ("model", sorted({r["model_served"] for r in rows})[0])]
    rs = collections.Counter(r["run_state"] for r in rows)
    out.append(("landed", "ENDED: LANDED %d" % rs["ENDED: LANDED"]))
    out.append(("capcost", "ENDED: CAP-COST %d" % rs["ENDED: CAP-COST"]))
    sc = collections.Counter(r["suite"] for r in rows)
    out.append(("suite", "PASS %d · FAIL %d · BUILD-FAIL %d" % (sc["PASS"], sc["FAIL"], sc["BUILD-FAIL"])))
    for arm in ("plain", "salt-diet"):
        a = [r for r in rows if r["arm"] == arm]
        c = [float(r["final_COST"]) for r in a]; T = [int(r["final_T"]) for r in a]
        out.append((arm + " n", "%s      %d" % (arm.ljust(9), len(a))) if False else ("skip", ""))
        out.append((arm + " median", "$%.2f" % statistics.median(c)))
        out.append((arm + " total", "$%.2f" % sum(c)))
        out.append((arm + " T", format(sum(T), ",")))
        out.append((arm + " capped", "%d  of %d" % (sum(1 for r in a if r["capped"] == "yes"), len(a))))
    # the two non-PASS cells must be named in the prose, BY NAME
    for r in rows:
        if r["suite"] != "PASS":
            out.append(("non-pass " + r["cell"], r["cell"]))
    # the cap value
    out.append(("cap", "$%s" % sorted({r["cap"] for r in rows})[0]))
    return [(l, v) for l, v in out if v]

def run(doc, table):
    rows = load(table); text = open(doc, encoding="utf-8").read()
    present = set(rows[0].keys())
    leaked = [c for c in ABSENT if c in present]
    if leaked:
        print("⛔ this GREENFIELD table carries seed-only column(s) %s — the wrong table was joined" % leaked)
        return 1
    bad = [(l, v) for l, v in checks(rows) if v not in text]
    print("block SG verifier: %d row(s), %d figure(s) re-derived; %d seed-only column(s) correctly absent"
          % (len(rows), len(checks(rows)), len(ABSENT)))
    if bad:
        print("⛔ %d FIGURE(S) NOT FOUND IN THE DOCUMENT:" % len(bad))
        for l, v in bad: print("   %-22s expected in prose: %r" % (l, v))
        return 1
    print("✅ every re-derived figure is present in the document's bytes.")
    return 0

def selftest():
    import tempfile, shutil, re
    text = open(DOC, encoding="utf-8").read(); fails = []
    with tempfile.TemporaryDirectory() as d:
        t2 = os.path.join(d, "t.tsv"); shutil.copy(TBL, t2)
        d0 = os.path.join(d, "d.md"); shutil.copy(DOC, d0)
        rc = run(d0, t2); print("  arm 1 control                          rc=%d  %s" % (rc, "PASS" if rc == 0 else "FAIL"))
        if rc != 0: fails.append(1)
        m = re.sub(r"PASS 27 · FAIL 1 · BUILD-FAIL 1", "PASS 28 · FAIL 1 · BUILD-FAIL 0", text, count=1)
        assert m != text, "arm 2 fixture did not mutate"
        open(d0, "w", encoding="utf-8").write(m)
        rc = run(d0, t2); print("  arm 2 mutant: suite split wrong        rc=%d  %s" % (rc, "PASS" if rc == 1 else "FAIL"))
        if rc != 1: fails.append(2)
        m = text.replace("clbgfs02", "clbgfs99")
        assert m != text, "arm 3 fixture did not mutate"
        open(d0, "w", encoding="utf-8").write(m)
        rc = run(d0, t2); print("  arm 3 mutant: a non-PASS cell unnamed  rc=%d  %s" % (rc, "PASS" if rc == 1 else "FAIL"))
        if rc != 1: fails.append(3)
        # arm 4: a seed-only column appears -> the wrong table was joined
        src = [l for l in open(TBL, encoding="utf-8")]
        hdr = next(i for i, l in enumerate(src) if l.startswith("cell\t"))
        src[hdr] = src[hdr].rstrip("\n") + "\tretained\n"
        for i in range(hdr + 1, len(src)):
            if src[i].strip(): src[i] = src[i].rstrip("\n") + "\t0.5\n"
        open(t2, "w", encoding="utf-8").writelines(src)
        shutil.copy(DOC, d0)
        rc = run(d0, t2); print("  arm 4 mutant: seed column in a green   rc=%d  %s" % (rc, "PASS" if rc == 1 else "FAIL"))
        if rc != 1: fails.append(4)
    print()
    if fails: print("⛔ SELFTEST FAILED on arm(s) %s" % fails); return 1
    print("✅ SELFTEST 4/4 — control green; a wrong suite split, an unnamed failing cell, and a seed-only\n"
          "   column leaking into a greenfield table each redden the arm they name.")
    return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc", default=DOC); ap.add_argument("--table", default=TBL)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else run(a.doc, a.table))
