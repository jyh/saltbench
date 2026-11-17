#!/usr/bin/env python3
"""Derive block WC's WC_SOURCES (24 rows) from the 24 P1 baselines (saltbench evidence/blockWC-2026-11-15/p1-baselines.tsv), by NC
§C2 rules 3-4 as WC §WC2 carries them: eligible landings fill n=1.. in ascending cell-id order; each open n is a fresh phase 1 under
WFO/WFS, id clb<y|z><prob><arm><nn>, root cells-clb-wf{o,s}-<prob>-<arm>. Prints the table; --check <clb_stage.sh> compares it to
the stager's WC_SOURCES byte for byte (rc 0 equal, rc 1 differ)."""
import csv, sys, re
rows = list(csv.DictReader(open(sys.argv[1]), delimiter='\t'))
assert len(rows) == 24, len(rows)
PL = {"NTT": "t", "WHT": "w"}; AL = {"plain": "p", "salt-diet": "s"}
root = lambda m, p, a: "cells-clb-%s-%s-%s" % ("wo" if m == "Opus" else "ws", p.lower(), a.replace("salt-diet", "saltdiet"))
out = []
for m in ("Opus", "Sonnet"):
    for p in ("NTT", "WHT"):
        for a in ("plain", "salt-diet"):
            el = sorted(r["cell"] for r in rows if (r["model"], r["problem"], r["arm"]) == (m, p, a) and r["eligible"] == "YES")
            for n in range(1, 4):
                if n <= len(el):
                    src = root(m, p, a) + "/" + el[n - 1]
                else:
                    src = "cells-clb-%s-%s-%s/clb%s%s%s%02d" % ("wfo" if m == "Opus" else "wfs", p.lower(), a.replace("salt-diet", "saltdiet"),
                                                              "y" if m == "Opus" else "z", PL[p], AL[a], n)
                out.append("%s %s %s %d %s" % (m, p, a, n, src))
text = "\n".join(out)
if len(sys.argv) > 3 and sys.argv[2] == "--check":
    s = open(sys.argv[3]).read()
    mm = re.search(r"^WC_SOURCES='(.*?)'$", s, re.S | re.M)
    if not mm: print("NO WC_SOURCES in", sys.argv[3]); sys.exit(2)
    ok = mm.group(1) == text
    print("WC_SOURCES %s the derivation (%d rows; fresh %d)" % ("EQUALS" if ok else "DIFFERS FROM", len(out), sum("/clby" in r or "/clbz" in r for r in out)))
    sys.exit(0 if ok else 1)
print(text)
