#!/usr/bin/env python3
"""item7_join.py <cellmap.tsv> <exposure_census.out> — item 7 (bench, relight 149). Zero spend, reads two files.
For every DONE row of the correctness cell map that names a cell, find that cell's census window, resolving a cell id that lives in more
than one root BY RULE (the state file's (a)): (1) the map's own root= field; else (2) drop roots suffixed .HALTED .VOID .ABORTED
.DISCARDED (never the record); else (3) l8cpss01/03 -> the -cp root (census ADDENDUM 22). A row still ambiguous is printed AMBIGUOUS, never
picked. COUNT and CONDITION rows have no per-cell id and are printed UNMEASURABLE-BY-CELL with their count.
Status per record cell: EXPOSED (some other root was born inside its window) · CLEAN (none) · NO-WINDOW (unmeasured, never clean) ·
MISSING (no ctl dir on the box) · AMBIGUOUS.
"""
import csv, re, sys
from collections import Counter, defaultdict

DEAD = re.compile(r"\.(HALTED|VOID|ABORTED|DISCARDED|UNFIRED)")
# (4) an id still ambiguous after rules 1-3, resolved by MEASUREMENT at the box, each with its evidence (relight 149)
OVERRIDE = {"l5cp01": ("cells-l5-crc32-plain", "its ctl logs read T 3993025 = RESULT-gemini-flash-level5-2026-09-15.md:30; the -a1 copy reads T 4526170")}


def main(mapf, censf):
    census = defaultdict(list)
    for l in open(censf):
        if not l.startswith("CELL\t"):
            continue
        _, cell, root, s, e, src, inside = (l.rstrip("\n").split("\t") + [""] * 7)[:7]
        census[cell].append((root, s, e, src, inside))
    rows = list(csv.DictReader((l for l in open(mapf) if not l.startswith("#")), delimiter="\t"))
    out, tally, unm = [], Counter(), Counter()
    for r in rows:
        if r["status"] != "DONE":
            continue
        c = r["cell"]
        if c in ("COUNT", "CONDITION"):
            unm[c] += 1
            continue
        cands = census.get(c, [])
        why = "single" if len(cands) == 1 else ("none" if not cands else "UNRESOLVED")
        if len(cands) > 1:
            m = re.search(r"root=([A-Za-z0-9_.-]+)", r["sources"] + " " + r["note"])
            if m and any(x[0] == m.group(1) for x in cands):
                cands, why = [x for x in cands if x[0] == m.group(1)], "map root="
            else:
                live = [x for x in cands if not DEAD.search(x[0])]
                if len(live) == 1:
                    cands, why = live, "dead-suffix rule"
                elif re.fullmatch(r"l8cpss0[13]", c):
                    cp = [x for x in live if x[0].endswith("-cp")]
                    cands, why = (cp, "ADDENDUM 22 rule") if len(cp) == 1 else (cands, why)
                elif c in OVERRIDE and any(x[0] == OVERRIDE[c][0] for x in cands):
                    cands, why = [x for x in cands if x[0] == OVERRIDE[c][0]], "measured: " + OVERRIDE[c][1]
        if not cands:
            st, root, inside = "MISSING", "-", ""
        elif len(cands) > 1:
            st, root, inside = "AMBIGUOUS", "|".join(x[0] for x in cands), ""
        else:
            root, s, e, src, inside = cands[0]
            st = "NO-WINDOW" if src == "NO-WINDOW" else ("EXPOSED" if inside else "CLEAN")
        tally[(r["model"], st)] += 1
        out.append((r["model"], r["problem"], r["field"], r["arm"], r["extras"], c, root, st, why, inside))
    print("#model\tproblem\tfield\tarm\textras\tcell\troot\tstatus\tresolved_by\tborn_inside")
    for o in out:
        print("\t".join(o))
    print("# record rows by cell: %d (%d distinct ids)" % (len(out), len({o[5] for o in out})))
    for k in sorted(tally):
        print("# %s %s %d" % (k[0], k[1], tally[k]))
    for k, n in unm.items():
        print("# UNMEASURABLE-BY-CELL %s rows: %d (no per-cell id in the map)" % (k, n))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
