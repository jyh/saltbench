#!/usr/bin/env python3
"""join_cells_table.py --stage <clb-score dir> --retention <tsv> --block <letter> [--out <tsv>]

Build a Claude-lane block's 24-column TABLE OF RECORD by a mechanical join of the three receipts
block SB's result names: the per-cell scoring pass, the retention decomposition, and each cell's own
frozen meter. Written for the four blocks that are harvested, scored, and have no result of record.

⛔⛔ IT ASSERTS RATHER THAN PREFERS. `class` and `retained` are produced INDEPENDENTLY by the scorer
  and by the retention decomposition. This tool REFUSES (rc 1) if they disagree for any cell — it does
  not pick one. Block SB's table was built under the same rule and it is the rule that makes the join
  evidence rather than a merge.
⛔ IT REFUSES A CELL MISSING ANY OF THE THREE SOURCES (rc 1). A row assembled from two of three is not
  a shorter row, it is a different claim.
⛔ THE MODEL IS NOT IN THIS TABLE BY ACCIDENT — see model_served_v3.py. ADDENDUM 12 had to correct a
  block's model after the fact because the 24-column table carried none, so the verifier could not see
  the one field that was wrong. `model_served` is column 25 here, derived from each cell's own receipt.

COLUMNS 1-24 are block SB's, in its order, so the two tables are directly comparable; 25 is new.
"""
import argparse, os, sys, csv

COLS = ["cell","problem","arm","field","extras","run_state","suite","tests","V1_bugs_fixed",
        "bugs_introduced","class","retained","surv","growth","seed_lines","end_lines","kept",
        "w1_fenced","end_from","final_T","final_COST","cap_unit","cap","capped","model_served"]

# ⛔⛔ A GREENFIELD BLOCK HAS NO SEED, SO IT HAS NO RETENTION AND NO REWRITE CLASS. Its table is a
#   DIFFERENT SHAPE, not a shorter one: `class`, `retained`, `surv`, `growth`, `seed_lines`,
#   `end_lines`, `kept` and `end_from` are all claims ABOUT A SEED and none of them exists here.
#   ⇒ They are OMITTED rather than emitted blank. A blank cell in a 25-column table reads as a
#     measurement that came back empty; an absent COLUMN cannot be misread that way, and the two
#     shapes must never be concatenated into one denominator.
GREENFIELD_COLS = ["cell","problem","arm","field","extras","run_state","suite","tests",
                   "w1_fenced","final_T","final_COST","cap_unit","cap","capped","model_served"]

def read_score(path, cell):
    for line in open(path, encoding="utf-8", errors="replace"):
        if line.startswith(cell + "\t"):
            f = line.rstrip("\n").split("\t")
            return {"problem": f[1], "arm": f[2], "field": f[3], "extras": f[4], "run_state": f[5],
                    "suite": f[7], "tests": f[8], "V1_bugs_fixed": f[10], "bugs_introduced": f[11],
                    "class": f[12], "retained": f[13], "w1_fenced": f[14]}
    return None

def read_served(path):
    # ⛔ A MISSING RECEIPT IS A REFUSAL, NEVER AN EXCEPTION AND NEVER A BLANK. `clbglp01` was fired and
    #   harvested BY HAND and has no served-*.out in the chain's run dir; the first cut of this tool
    #   raised FileNotFoundError and took the whole block down with a stack trace, which reads as a
    #   broken tool rather than as the one declared fact it is.
    import re, os
    if not os.path.exists(path): return None
    txt = open(path, encoding="utf-8", errors="replace").read()
    head = re.findall(r'^\s*served head\s+(.*)$', txt, re.M)
    if not head: return None
    models = sorted(set(re.findall(r'([A-Za-z0-9._-]+)=\d+', head[0])))
    return models[0] if len(models) == 1 else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True, help="the directory holding one dir per staged cell")
    ap.add_argument("--retention", help="REQUIRED for a brownfield block; omit for greenfield")
    ap.add_argument("--block", required=True, help="the cell-id block letter, e.g. o")
    ap.add_argument("--served-dir", help="dir holding served-<cell>.out (adds model_served)")
    ap.add_argument("--exclude", action="append", default=[], metavar="CELL:REASON",
                    help="exclude a cell BY NAME with a REASON, both of which are written into the "
                         "table's header. ⛔ A cell dropped without a reason is indistinguishable from "
                         "a cell that never existed, which is how an n silently shrinks.")
    ap.add_argument("--out")
    a = ap.parse_args()

    ret = {}
    if a.retention:
        for r in csv.DictReader((l for l in open(a.retention, encoding="utf-8") if not l.startswith("#")),
                                delimiter="\t"):
            ret[r["cell"]] = r
    excl = {}
    for e in a.exclude:
        if ":" not in e:
            print("REFUSE: --exclude %s has no REASON (use CELL:REASON)" % e, file=sys.stderr); return 2
        c, r = e.split(":", 1)
        if not r.strip():
            print("REFUSE: --exclude %s has an EMPTY reason" % e, file=sys.stderr); return 2
        excl[c] = r.strip()
    cells = sorted(d for d in os.listdir(a.stage)
                   if d.startswith("clb" + a.block) and d not in excl)
    if not cells:
        print("REFUSE: no staged cell whose id starts with clb%s" % a.block, file=sys.stderr); return 2

    rows, bad = [], []
    for cell in cells:
        sp = os.path.join(a.stage, cell, "score.out")
        cp = os.path.join(a.stage, cell, "cells", cell, "ctl", "post-end-1.tsv")
        if not os.path.exists(sp): bad.append((cell, "no score.out")); continue
        if a.retention and cell not in ret: bad.append((cell, "no retention row")); continue
        if not os.path.exists(cp):bad.append((cell, "no ctl/post-end-1.tsv (the frozen meter)")); continue
        s = read_score(sp, cell)
        if s is None: bad.append((cell, "score.out has no row for this cell")); continue
        r = ret.get(cell)
        # ⛔ THE ASSERTION — two independent producers must agree, or this is not a join.
        if r is not None and s["class"] != r["class"]:
            bad.append((cell, "class DISAGREES: scorer %s vs retention %s" % (s["class"], r["class"]))); continue
        if r is not None and s["retained"] != r["retained"]:
            bad.append((cell, "retained DISAGREES: scorer %s vs retention %s" % (s["retained"], r["retained"]))); continue
        m = list(csv.DictReader(open(cp, encoding="utf-8"), delimiter="\t"))[0]
        row = dict(s); row["cell"] = cell
        if r is not None:
            for k in ("surv","growth","seed_lines","end_lines","kept","end_from"): row[k] = r[k]
        for k in ("final_T","final_COST","cap_unit","cap"): row[k] = m[k]
        row["capped"] = "yes" if m["kind"].startswith("CAP") else "no"
        if a.served_dir:
            ms = read_served(os.path.join(a.served_dir, "served-%s.out" % cell))
            if ms is None:
                bad.append((cell, "no readable served-%s.out — the model cannot be derived, and a BLANK "
                                  "model column is the very defect ADDENDUM 12 had to correct" % cell)); continue
            row["model_served"] = ms
        else:
            row["model_served"] = ""
        rows.append(row)

    if bad:
        print("⛔ %d cell(s) REFUSED — a row assembled from fewer than three sources is a different claim:" % len(bad),
              file=sys.stderr)
        for c, w in bad: print("   %s  %s" % (c, w), file=sys.stderr)
        return 1
    cols = COLS if a.retention else GREENFIELD_COLS
    fields = {r["field"] for r in rows}
    if a.retention and fields != {"brownfield"}:
        print("REFUSE: --retention given but the block's field(s) are %s — retention is a claim about a SEED"
              % sorted(fields), file=sys.stderr); return 1
    if not a.retention and fields != {"greenfield"}:
        print("REFUSE: no --retention but the block's field(s) are %s — a brownfield block owes its "
              "retention decomposition" % sorted(fields), file=sys.stderr); return 1
    out = open(a.out, "w", encoding="utf-8") if a.out else sys.stdout
    for c in sorted(excl):
        out.write("# EXCLUDED\t%s\t%s\n" % (c, excl[c]))
    out.write("\t".join(cols) + "\n")
    for r in rows: out.write("\t".join(str(r.get(c, "")) for c in cols) + "\n")
    if a.out: out.close()
    if a.retention:
        print("joined %d cell(s) for block %s; class and retained AGREED across both producers for every one."
              % (len(rows), a.block), file=sys.stderr)
    else:
        # ⛔ NOT "agreed" — there is no second producer on a greenfield block. Claiming an agreement
        #   that was never tested is the vacuous-assertion defect this campaign keeps paying for.
        print("joined %d cell(s) for block %s; GREENFIELD — no seed, so no retention, no rewrite class, "
              "and NO cross-producer agreement was tested (there is only one producer)."
              % (len(rows), a.block), file=sys.stderr)
    return 0

if __name__ == "__main__":
    sys.exit(main())
