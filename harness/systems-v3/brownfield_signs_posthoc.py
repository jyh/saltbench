#!/usr/bin/env python3
"""POST HOC: tables_v3.py's "$4 sign counts" rule, applied to the BROWNFIELD bare and statement ratios.

The registered summary ($4) covers greenfield only; this is not registered. It imports tables_v3 and
tables_v2 unchanged and reuses their build, summarise, ratio, sign and median rules; the summary block
below is tables_v3.render's "$4 sign counts" block with the grid swapped. CONTROL: the same function over
the GREENFIELD grid must reproduce the published $4 rows, or the script exits 1 and prints nothing else.
"""
import statistics, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tables_v3 as t3
v2 = t3.v2

ARMS = {"bare": ("none",), "statement": ("statement",), "spec-change": ("spec-change",)}

def ratios(conds, cur, field, treatment):
    out = {}
    for m in v2.MODELS:
        for p in v2.PROBLEMS:
            s = lambda arm: t3.summarise(conds.get((m, p, field, arm, treatment if treatment != "bare" else "none")), cur)
            out.setdefault(m, []).append((p,) + v2.ratio(s("salt-diet"), s("plain")))
    return out

def sign_rows(rs, name):
    rows = []
    for m in v2.MODELS:
        have = [(p, v, mk) for p, v, mk in rs[m] if v is not None]
        sg = [(p, v2.sign((v, mk))) for p, v, mk in have]
        k = sum(1 for _, s in sg if s is True)
        mm = sum(1 for _, s in sg if s is not None)
        ind = [p for p, s in sg if s is None]
        med = ("%.2f" % statistics.median([v for _, v, _ in have])) if have else "—"
        rows.append("| %s | %s | %d of %d | %s | %s | %d |" % (m, name, k, mm, ", ".join(ind) or "none", med,
                                                            sum(1 for _, _, mk in have if mk)))
    return rows

def main(map_path, ev, published):
    conds, prov, fails = t3.build(map_path, ev)
    pub = set(l.strip() for l in open(published, encoding="utf-8"))
    ctrl = [r for n in ("bare", "statement", "spec-change") for r in sign_rows(ratios(conds, "usd", "greenfield", n), n)]
    miss = [r for r in ctrl if r not in pub]
    print("CONTROL greenfield $4 rows reproduced: %d of %d" % (len(ctrl) - len(miss), len(ctrl)), file=sys.stderr)
    if miss or len(ctrl) != 12:
        for r in miss:
            print("CONTROL MISS " + r, file=sys.stderr)
        return 1
    print("| model | treatment | k of m ratios > 1 | indeterminate | median of the ratios | bounded among them |")
    print("|---|---|---|---|---|---|")
    rows = {n: sign_rows(ratios(conds, "usd", "brownfield", n), n) for n in ("bare", "statement")}
    for i in range(len(v2.MODELS)):
        print(rows["bare"][i]); print(rows["statement"][i])
    return 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:4]))
