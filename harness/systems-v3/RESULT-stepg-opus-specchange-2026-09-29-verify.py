#!/usr/bin/env python3
"""RESULT-stepg-opus-specchange-2026-09-29-verify.py [--render] [--selftest]

Re-derive every figure in RESULT-stepg-opus-specchange-2026-09-29.md FROM its tracked tables and assert each rendered block is present
VERBATIM in the document's bytes. Idiom law clause 1: no typed expectations. --render prints the blocks (the document is written from them).
  cells   evidence/stepg-2026-09-29/cells.tsv   (stepg-derive.sh: one row per block-G cell, read from the cells themselves)
  reach   evidence/stepg-2026-09-29/reach.tsv   (the same script: phase-1 reach per condition, the helm's MANDATORY column)
rc 0 · 1 a block missing from the document, named · 2 usage."""
import csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(HERE, "RESULT-stepg-opus-specchange-2026-09-29.md")
EV = os.path.join(HERE, "..", "..", "evidence", "stepg-2026-09-29")
PT = (0.02794, 0.03172)   # pt per USD, the lead's block-N re-cut (cited in the freeze §G4); a RATE, not a result


def load(name):
    with open(os.path.join(EV, name), encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def render(cells, reach):
    out = []
    b = ["  cell      task      arm        end-2     suite     tests  regr   clause  phase-2 $   served head        source"]
    for r in cells:
        b.append("  %-9s %-9s %-10s %-9s %-9s %-6s %-6s %-7s %-10s %-18s %s" % (
            r["cell"], r["task"], r["arm"], r["end2_kind"], r["suite"], r["tests"], r["regressions_failed"], r["clause_failed"],
            "%.2f" % float(r["final_COST"]), r["served_head"], r["source"]))
    out.append("\n".join(b))
    tot = sum(float(r["final_COST"]) for r in cells)
    out.append("SPEND: 7 cells, phase 2 only, $%.2f in all  =  %.2f – %.2f pt" % (tot, tot * PT[0], tot * PT[1]))
    kinds = {}
    for r in cells:
        kinds[r["suite"]] = kinds.get(r["suite"], 0) + 1
    out.append("SUITES: " + " · ".join("%s %d" % (k, kinds[k]) for k in sorted(kinds)))
    heads = sorted({r["served_head"].split("=")[0] for r in cells})
    vers = sorted({r["client_versions"] for r in cells})
    verd = sorted({r["served_verdict"] for r in cells})
    out.append("SERVED: head %s in %d of %d · verdict %s · client %s" % (",".join(heads), len(cells), len(cells), ",".join(verd), ",".join(vers)))
    rb = ["  task      arm        phase-1 landed / with end-1   not landed"]
    for r in reach:
        rb.append("  %-9s %-10s %d / %-26d %s" % (r["task"], r["arm"], int(r["landed"]), int(r["with_end1"]), r["not_landed_kinds"].strip() or "-"))
    out.append("\n".join(rb))
    return out


def main(argv):
    if "--selftest" in argv:
        c = [{"cell": "x", "task": "T", "arm": "plain", "end2_kind": "LANDED", "suite": "PASS", "tests": "1/1", "regressions_failed": "0/1",
              "clause_failed": "0/0", "final_COST": "1.004", "served_head": "claude-opus-5=3", "served_verdict": "clean", "client_versions": "v",
              "source": "r/s"}]
        rr = [{"task": "T", "arm": "plain", "landed": "1", "with_end1": "2", "not_landed_kinds": "CAP-COST=1 "}]
        bl = render(c, rr)
        ok = ("$1.00 in all" in bl[1]) and ("PASS 1" in bl[2]) and ("1 / 2" in bl[4]) and ("CAP-COST=1" in bl[4])
        doc = "\n".join(bl)
        mut = doc.replace("1 / 2", "2 / 2")
        miss = [x for x in bl if x not in mut]
        ok = ok and len(miss) == 1   # a mutated document must be caught on exactly the mutated block
        print("selftest:", "ok" if ok else "FAIL"); return 0 if ok else 1
    cells, reach = load("cells.tsv"), load("reach.tsv")
    blocks = render(cells, reach)
    if "--render" in argv:
        print("\n\n".join(blocks)); return 0
    doc = open(DOC, encoding="utf-8").read()
    missing = [b.splitlines()[0] for b in blocks if b not in doc]
    print("stepg verifier: %d cell rows · %d reach rows · %d blocks re-derived" % (len(cells), len(reach), len(blocks)))
    if missing:
        for m in missing: print("  MISSING from the document:", m)
        return 1
    print("✅ every re-derived block is present in the document's bytes."); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
