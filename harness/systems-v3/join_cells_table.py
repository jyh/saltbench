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
import argparse, os, re, sys, csv

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

# ⛔⛔ THE THIRD SHAPE. A SPEC-CHANGE (block SC) CONDITION IS A PAIR OF PHASES, NOT A LONGER ROW.
#   The scorer emits a DIFFERENT TABLE for phase 2 (score_claude_v3 :208) from the one it emits for
#   phase 1 (:114) — different columns, different meanings, same first field. So this table names the
#   PHASE in every column that could be either, and it NEVER reuses `V1_bugs_fixed` for phase 2's `V1`:
#   phase 1's counts baseline-failing tests that now pass; phase 2's is "the old behaviour survived".
#   ⇒ DIFFERENT QUANTITIES, COLLIDING NAME — the one mistake that would read as a working table.
#   The seed columns are absent for the same reason GREENFIELD_COLS omits them: block SC is greenfield
#   only (brownfield x spec-change is not in the matrix, and score_claude_v3 REFUSES the pair).
SPECCHANGE_COLS = ["cell","problem","arm","field","extras","model_served",
                   "p1_run_state","p1_suite","p1_tests","p1_w1_fenced",
                   "p1_T","p1_COST","p1_cap_unit","p1_cap","p1_capped",
                   "p2_run_state","p2_suite","p2_tests","p2_regressions","p2_clause_tests",
                   "p2_V1","p2_V2","p2_T","p2_COST","p2_cap_unit","p2_cap","p2_capped",
                   "cell_T_at_end2","cell_COST_at_end2"]

# ⛔⛔ THE PER-PHASE COST DOES **NOT** COME FROM THE FROZEN METER, AND THIS IS THE ONE THING IN THIS FILE
#   MOST LIKELY TO BE "SIMPLIFIED" BY A LATER READER. MEASURED 2026-09-21 on the first SC cell ever run:
#     post-end-1.tsv final_T 23,152,052  final_COST 7.4891
#     post-end-2.tsv final_T 31,692,783  final_COST 10.5232      <- 23.1M + 8.5M
#   ⇒ ***ctl/post-end-<phase>.tsv IS CUMULATIVE OVER THE CELL, NOT PER PHASE.*** For a one-phase cell the
#   two are the same number, which is why nothing noticed until a cell had two phases. Sourcing `p2_COST`
#   from post-end-2 would have put the CELL'S RUNNING TOTAL in a column named for phase 2 — a wrong number
#   in a table of record, arithmetically consistent and completely believable.
#   ✅ THE PER-PHASE FIGURES COME FROM THE HARVEST, which is the instrument that actually splits the phases
#   (`clb_harvest --phase`, and its own "PHASE SPLIT: N head(s) … are metered; M … are NOT"). That split is
#   the whole point of export eb18e5d; reading cost from the frozen meter would throw it away.
#   The frozen meters are still the source for cap_unit/cap/capped, which the harvest does not report, and
#   post-end-2's cumulative total is kept under a name that says what it is.
_METER_RE = re.compile(r"^--- METER: T (\d+) . COST \$([0-9.]+)", re.M)

def read_harvest_meter(path):
    """T and COST for ONE phase, from that phase's harvest — the only producer that meters the phases apart."""
    if not os.path.exists(path): return None
    m = _METER_RE.search(open(path, encoding="utf-8", errors="replace").read())
    return {"T": m.group(1), "COST": m.group(2)} if m else None

def read_score2(path, cell):
    """The PHASE-2 row: cell problem arm phase run_state end suite tests regressions clause_tests V1 V2 note."""
    for line in open(path, encoding="utf-8", errors="replace"):
        if line.startswith(cell + "\t"):
            f = line.rstrip("\n").split("\t")
            if len(f) < 13: return None
            # ⛔ THE PHASE IS ASSERTED, NOT ASSUMED: a phase-1 row in a -p2 score.out would otherwise be
            #   read positionally into these names and produce a confident, wrong row.
            if f[3] != "2": return None
            return {"problem": f[1], "arm": f[2], "p2_run_state": f[4], "p2_suite": f[6],
                    "p2_tests": f[7], "p2_regressions": f[8], "p2_clause_tests": f[9],
                    "p2_V1": f[10], "p2_V2": f[11]}
    return None

def read_meter(path):
    import csv as _csv
    rows = list(_csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"))
    return rows[0] if rows else None

# ⛔ THE HIGHEST INDEX read_score READS IS f[14], SO A ROW WITH FEWER THAN 15 FIELDS CANNOT BE READ
#   POSITIONALLY. read_score2 has carried `if len(f) < 13: return None` since it was written; this
#   reader was its sibling and never got the guard, so a short row raised IndexError and took the whole
#   block down with a stack trace — the SAME failure read_served's comment below records being fixed
#   once already. ⇒ A FIX DOES NOT TRAVEL TO ITS SIBLINGS; it has to be carried.
#   (Found by a non-author read of PR #227 — the author had the guard in mind in one function of two.)
_SCORE_MIN_FIELDS = 15

class ShortScoreRow(Exception):
    """A score.out row for this cell EXISTS but is too short to read positionally.

    ⛔ THIS IS A DIFFERENT FACT FROM `None` ("no row for this cell") AND MUST NOT SHARE ITS MESSAGE.
      Both call sites turn a None into "has no row for this cell"; reporting a malformed row that way
      would be a confident, accurate-sounding sentence about the wrong defect, and would send whoever
      reads it looking for a missing cell that is present.
    """
    def __init__(self, cell, n):
        super().__init__("score.out has a row for %s with only %d field(s) — this reader indexes f[14] "
                         "and needs %d. The row is MALFORMED, which is NOT the same as absent."
                         % (cell, n, _SCORE_MIN_FIELDS))

def read_score(path, cell):
    for line in open(path, encoding="utf-8", errors="replace"):
        if line.startswith(cell + "\t"):
            f = line.rstrip("\n").split("\t")
            if len(f) < _SCORE_MIN_FIELDS: raise ShortScoreRow(cell, len(f))
            return {"problem": f[1], "arm": f[2], "field": f[3], "extras": f[4], "run_state": f[5],
                    "suite": f[7], "tests": f[8], "V1_bugs_fixed": f[10], "bugs_introduced": f[11],
                    "class": f[12], "retained": f[13], "w1_fenced": f[14]}
    return None

def score_or_bad(path, cell, label, bad):
    """read_score, with BOTH refusals routed to `bad` under their own distinct messages.

    Returns the row, or None having already appended the reason. Used at every call site so the two
    failures can never be conflated by a caller that only remembers to test for None.
    """
    try:
        s = read_score(path, cell)
    except ShortScoreRow as e:
        bad.append((cell, str(e))); return None
    if s is None:
        bad.append((cell, "%s has no row for this cell" % label)); return None
    return s

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
    ap.add_argument("--harvest-dir",
                    help="dir holding harvest-<cell>.out and harvest-<cell>-p2.out; REQUIRED with "
                         "--spec-change, because per-phase cost comes from the harvest and NOT from the "
                         "frozen meter, which is cumulative over the cell")
    ap.add_argument("--spec-change", action="store_true",
                    help="block SC: each cell is a PAIR of phases. REQUIRED for a spec-change block, REFUSED for any other")
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
    allobs = sorted(d for d in os.listdir(a.stage)
                    if d.startswith("clb" + a.block) and d not in excl)
    p2s = {d[:-3] for d in allobs if d.endswith("-p2")}

    # ⛔⛔ THE TWO-WAY REFUSAL, THE SAME SHAPE AS --retention's. A spec-change block WITHOUT the flag
    #   would otherwise build a clean, plausible, PHASE-1-ONLY table and pass every check here — the
    #   cheap fix that silently discards the half the block exists to measure. It must be impossible.
    if p2s and not a.spec_change:
        print("REFUSE: %d '-p2' score dir(s) are present for block %s, so this is a SPEC-CHANGE block and "
              "each cell is a PAIR of phases. Pass --spec-change. ⛔ Without it this tool would either "
              "refuse confusingly or, worse, report phase 1 alone as the block's table."
              % (len(p2s), a.block), file=sys.stderr); return 2
    if a.spec_change and not p2s:
        print("REFUSE: --spec-change given but NO '-p2' score dir exists for block %s — a spec-change "
              "condition is a pair, and there is no second phase here." % a.block, file=sys.stderr); return 2

    if a.spec_change:
        if a.retention:
            print("REFUSE: --retention with --spec-change. Block SC is GREENFIELD ONLY (brownfield x "
                  "spec-change is not in the matrix; score_claude_v3 refuses the pair), so there is no "
                  "seed and no retention.", file=sys.stderr); return 2
        hdir = a.harvest_dir or a.served_dir
        if not hdir:
            print("REFUSE: --spec-change needs --harvest-dir (or --served-dir pointing at the same run "
                  "dir). Per-phase T and COST come from each phase's HARVEST; the frozen meter "
                  "post-end-<n>.tsv is CUMULATIVE over the cell and would report phase 1 + phase 2 in a "
                  "column named for phase 2.", file=sys.stderr); return 2
        p1s = [d for d in allobs if not d.endswith("-p2")]
        rows, bad = [], []
        # ⛔ A HALF-PRESENT PAIR IS REFUSED IN BOTH DIRECTIONS — it is the shape that otherwise becomes a
        #   silent n of 1 in a table whose unit is the pair.
        for orphan in sorted(p2s - set(p1s)):
            bad.append((orphan + "-p2", "a phase-2 score dir with NO phase-1 sibling"))
        for cell in p1s:
            if cell not in p2s:
                bad.append((cell, "no '%s-p2' score dir — phase 2 is missing, and a spec-change condition "
                                  "is the PAIR" % cell)); continue
            sp1 = os.path.join(a.stage, cell, "score.out")
            sp2 = os.path.join(a.stage, cell + "-p2", "score.out")
            # ⛔ BOTH FROZEN METERS LIVE UNDER THE -p2 DIR, KEYED BY THE REAL CELL ID — never by the score
            #   dir's name. Assuming `score-dir name == cell id` is the single defect desk VI records, and
            #   it surfaced as a missing post-end-1.tsv rather than where its author predicted.
            m1p = os.path.join(a.stage, cell + "-p2", "cells", cell, "ctl", "post-end-1.tsv")
            m2p = os.path.join(a.stage, cell + "-p2", "cells", cell, "ctl", "post-end-2.tsv")
            for label, path in (("phase-1 score.out", sp1), ("phase-2 score.out", sp2),
                                ("phase-1 frozen meter (post-end-1.tsv)", m1p),
                                ("phase-2 frozen meter (post-end-2.tsv)", m2p)):
                if not os.path.exists(path): bad.append((cell, "no %s" % label)); break
            else:
                s1 = score_or_bad(sp1, cell, "phase-1 score.out", bad)
                if s1 is None: continue
                s2 = read_score2(sp2, cell)
                if s2 is None:
                    bad.append((cell, "phase-2 score.out has no row for this cell WITH phase==2 — the "
                                      "phase is asserted, never assumed")); continue
                if (s1["problem"], s1["arm"]) != (s2["problem"], s2["arm"]):
                    bad.append((cell, "the two phases DISAGREE on problem/arm: %s/%s vs %s/%s"
                                % (s1["problem"], s1["arm"], s2["problem"], s2["arm"]))); continue
                m1, m2 = read_meter(m1p), read_meter(m2p)
                if m1 is None or m2 is None:
                    bad.append((cell, "a frozen meter has no data row")); continue
                row = {"cell": cell, "problem": s1["problem"], "arm": s1["arm"],
                       "field": s1["field"], "extras": s1["extras"],
                       "p1_run_state": s1["run_state"], "p1_suite": s1["suite"], "p1_tests": s1["tests"],
                       "p1_w1_fenced": s1["w1_fenced"]}
                row.update(s2)
                # cap fields from the frozen meters (the harvest does not report them)
                for pre, m in (("p1_", m1), ("p2_", m2)):
                    row[pre + "cap_unit"] = m["cap_unit"]; row[pre + "cap"] = m["cap"]
                    row[pre + "capped"] = "yes" if m["kind"].startswith("CAP") else "no"
                # the CUMULATIVE total, kept under a name that says so
                row["cell_T_at_end2"] = m2["final_T"]; row["cell_COST_at_end2"] = m2["final_COST"]
                # ⛔ PER-PHASE cost from the HARVEST, never from the frozen meter — see the note above.
                hm1 = read_harvest_meter(os.path.join(hdir, "harvest-%s.out" % cell))
                hm2 = read_harvest_meter(os.path.join(hdir, "harvest-%s-p2.out" % cell))
                if hm1 is None or hm2 is None:
                    bad.append((cell, "no METER line in harvest-%s.out and/or harvest-%s-p2.out — per-phase "
                                      "cost has no honest source and the frozen meter is cumulative"
                                % (cell, cell))); continue
                row["p1_T"], row["p1_COST"] = hm1["T"], hm1["COST"]
                row["p2_T"], row["p2_COST"] = hm2["T"], hm2["COST"]
                if a.served_dir:
                    ms = read_served(os.path.join(a.served_dir, "served-%s.out" % cell))
                    if ms is None:
                        bad.append((cell, "no readable served-%s.out — the model cannot be derived, and a "
                                          "BLANK model column is the very defect ADDENDUM 12 had to correct"
                                    % cell)); continue
                    row["model_served"] = ms
                else:
                    row["model_served"] = ""
                rows.append(row)
        if bad:
            print("⛔ %d cell(s) REFUSED — a spec-change row is a PAIR and a partial pair is a different "
                  "claim:" % len(bad), file=sys.stderr)
            for c, w in bad: print("   %s  %s" % (c, w), file=sys.stderr)
            return 1
        fields = {r["field"] for r in rows}
        if fields != {"greenfield"}:
            print("REFUSE: block SC is greenfield only, but the field(s) are %s" % sorted(fields),
                  file=sys.stderr); return 1
        out = open(a.out, "w", encoding="utf-8") if a.out else sys.stdout
        for c in sorted(excl): out.write("# EXCLUDED\t%s\t%s\n" % (c, excl[c]))
        out.write("\t".join(SPECCHANGE_COLS) + "\n")
        for r in rows: out.write("\t".join(str(r.get(c, "")) for c in SPECCHANGE_COLS) + "\n")
        if a.out: out.close()
        print("joined %d spec-change PAIR(s) for block %s; each row is one cell's TWO phases, metered and "
              "scored APART. ⛔ NO cross-producer agreement was tested (there is no retention on a "
              "greenfield block), and V1/V2 are PHASE 2's verdicts — not phase 1's V1_bugs_fixed."
              % (len(rows), a.block), file=sys.stderr)
        return 0

    cells = [d for d in allobs if not d.endswith("-p2")]
    if not cells:
        print("REFUSE: no staged cell whose id starts with clb%s" % a.block, file=sys.stderr); return 2

    rows, bad = [], []
    for cell in cells:
        sp = os.path.join(a.stage, cell, "score.out")
        cp = os.path.join(a.stage, cell, "cells", cell, "ctl", "post-end-1.tsv")
        if not os.path.exists(sp): bad.append((cell, "no score.out")); continue
        if a.retention and cell not in ret: bad.append((cell, "no retention row")); continue
        if not os.path.exists(cp):bad.append((cell, "no ctl/post-end-1.tsv (the frozen meter)")); continue
        s = score_or_bad(sp, cell, "score.out", bad)
        if s is None: continue
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
