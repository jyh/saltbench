#!/usr/bin/env python3
"""cellroots_v3.py --map CELLMAP.tsv --inventory INVENTORY.tsv [--out OUT.tsv] [--selftest]

Step a of the v3 cost tables (desk YP; the price plan's ADDENDUM 1): resolve every cell of record in v2's cell map to ONE cells root
on the run box, so steps c and d read the right cell's own records. It is a join, and it REFUSES rather than guesses.

INVENTORY.tsv, one row per (cell, root) found on the run box (a directory `<root>/<cell>/ctl`):
    cell  root  shape            shape = CLAUDE (a METER watch.log + post-end) · AGY (an agy turn loop) · NONE
THE RULE, in order; the first that yields exactly one root decides, and the row names which rule decided:
    SOURCE-ROOT            the root the cell map's `sources` names (`root=<r>`), if that root holds the cell
    UNIQUE                 the only root holding the cell
    DEAD-SUFFIX-EXCLUDED   the only root left after excluding roots whose NAME declares them dead:
                           .UNFIRED · .ABORTED · .VOID · .HALTED · .superseded   (a name the lanes gave the root when it died)
    AMBIGUOUS              more than one root survives: REFUSED, every candidate printed, never picked
    RECORD                 an AMBIGUOUS cell settled by --resolved: a row  cell <TAB> root <TAB> citation  naming the RECORD that
                           decides it (a result file's line, a meter figure that matches the record's). A resolution is REFUSED if
                           its root does not hold the cell, or if the rule had NOT refused the cell (a citation never overrides a rule)
    ABSENT                 no root holds the cell: REFUSED
A cell appears once per id even when the map lists it twice (a spec-change cell has one row per phase).
rc 0 every id resolved · 1 at least one AMBIGUOUS or ABSENT (named on stderr; the table still prints them) · 2 usage.
The count line is the verdict's limit: it states how many ids each rule decided, so a reader sees how much rests on names."""
import argparse, collections, csv, io, os, re, sys

DEAD = re.compile(r"\.(UNFIRED|ABORTED|VOID|HALTED|superseded)", re.I)


def read_map(text):
    ids, src = [], {}
    for r in csv.DictReader(io.StringIO(text), delimiter="\t"):
        c = r.get("cell", "")
        if c in ("", "-"): continue
        if c not in src:
            ids.append(c)
            m = re.search(r"root=([^,|]+)", r.get("sources", ""))
            src[c] = m.group(1) if m else None
    return ids, src


def read_inventory(text):
    inv = collections.defaultdict(dict)
    for line in text.splitlines():
        if not line.strip() or line.startswith("#"): continue
        f = line.split("\t")
        if len(f) < 3: raise SystemExit("inventory row with fewer than 3 fields: %r" % line)
        inv[f[0]][f[1]] = f[2]
    return inv


def read_resolved(text):
    res = {}
    for line in text.splitlines():
        if not line.strip() or line.startswith("#"): continue
        f = line.split("\t")
        if len(f) < 3 or not f[2].strip(): raise SystemExit("a resolution needs cell, root AND a citation: %r" % line)
        res[f[0]] = (f[1], f[2])
    return res


def resolve(ids, src, inv, res=None):
    res = res or {}
    rows, counts = [], collections.Counter()
    for c in ids:
        roots = inv.get(c, {})
        rule, pick, cands = None, None, sorted(roots)
        if not roots:
            rule = "ABSENT"
        elif src.get(c) and src[c] in roots:
            rule, pick = "SOURCE-ROOT", src[c]
        elif len(roots) == 1:
            rule, pick = "UNIQUE", cands[0]
        else:
            live = [r for r in cands if not DEAD.search(r)]
            if len(live) == 1: rule, pick = "DEAD-SUFFIX-EXCLUDED", live[0]
            else: rule = "AMBIGUOUS"
        cite = "-"
        if c in res:
            rroot, cite = res[c]
            if rule not in ("AMBIGUOUS",): rule, pick, cite = "RESOLUTION-REFUSED(rule decided %s)" % rule, None, cite
            elif rroot not in roots: rule, pick = "RESOLUTION-REFUSED(root does not hold the cell)", None
            else: rule, pick = "RECORD", rroot
        counts[rule.split("(")[0]] += 1
        rows.append({"cell": c, "rule": rule, "root": pick or "-", "shape": roots.get(pick, "-") if pick else "-",
                     "candidates": ",".join(cands) if len(cands) > 1 else "-", "citation": cite})
    return rows, counts


def emit(rows, counts, out):
    out.write("# cellroots_v3: %s\n" % " · ".join("%s %d" % (k, counts[k]) for k in
              ("SOURCE-ROOT", "UNIQUE", "DEAD-SUFFIX-EXCLUDED", "RECORD", "AMBIGUOUS", "ABSENT", "RESOLUTION-REFUSED")))
    out.write("cell\trule\troot\tshape\tcandidates\tcitation\n")
    for r in rows: out.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (r["cell"], r["rule"], r["root"], r["shape"], r["candidates"], r["citation"]))


def selftest():
    ok = True
    def arm(name, cond):
        nonlocal ok; ok &= bool(cond); print(("  ok " if cond else "  FAIL ") + name)
    cmap = ("model\tproblem\tfield\tarm\textras\tstatus\tcell\tlower_bound\tlb_reason\tsources\tnote\n"
            "m\tP\tgreenfield\tplain\tnone\tDONE\tc_src\t0\t-\ttsv|x.tsv|root=r_named,cell=c_src|T|-\t-\n"
            "m\tP\tgreenfield\tplain\tnone\tDONE\tc_one\t0\t-\ttsv|x.tsv|cell=c_one|T|-\t-\n"
            "m\tP\tgreenfield\tplain\tnone\tDONE\tc_dead\t0\t-\ttsv|x.tsv|cell=c_dead|T|-\t-\n"
            "m\tP\tgreenfield\tplain\tnone\tDONE\tc_tie\t0\t-\ttsv|x.tsv|cell=c_tie|T|-\t-\n"
            "m\tP\tgreenfield\tplain\tnone\tDONE\tc_gone\t0\t-\ttsv|x.tsv|cell=c_gone|T|-\t-\n"
            "m\tP\tgreenfield\tsalt-diet\tnone\tDONE\tc_one\t0\t-\ttsv|x.tsv|cell=c_one|T|-\t-\n"
            "m\tP\tgreenfield\tplain\tnone\tINEXPR\t-\t0\t-\tNONE\t-\n")
    inv = ("c_src\tr_named\tCLAUDE\nc_src\tr_other\tCLAUDE\n"
           "c_one\tr1\tAGY\n"
           "c_dead\tr_live\tAGY\nc_dead\tr_x.VOID-wrong-model\tAGY\nc_dead\tr_y.HALTED-stall\tNONE\n"
           "c_tie\tr_a\tAGY\nc_tie\tr_a-cp\tAGY\n")
    ids, src = read_map(cmap)
    rows, counts = resolve(ids, src, read_inventory(inv))
    by = {r["cell"]: r for r in rows}
    arm("a cell listed twice in the map (one row per phase) resolves ONCE", ids.count("c_one") == 1 and len(ids) == 5)
    arm("the INEXPR row with cell '-' is not a cell", "-" not in by)
    arm("SOURCE-ROOT: the map's named root wins over a second live root", by["c_src"]["rule"] == "SOURCE-ROOT" and by["c_src"]["root"] == "r_named")
    arm("UNIQUE: one root, taken, with its artifact shape", by["c_one"]["rule"] == "UNIQUE" and by["c_one"]["shape"] == "AGY")
    arm("DEAD-SUFFIX-EXCLUDED: .VOID and .HALTED roots dropped, the live one taken", by["c_dead"]["rule"] == "DEAD-SUFFIX-EXCLUDED" and by["c_dead"]["root"] == "r_live")
    arm("⭐ AMBIGUOUS: a live two-way tie (a copy root) is REFUSED, never picked", by["c_tie"]["rule"] == "AMBIGUOUS" and by["c_tie"]["root"] == "-"
        and by["c_tie"]["candidates"] == "r_a,r_a-cp")
    arm("ABSENT: a cell on no root is REFUSED", by["c_gone"]["rule"] == "ABSENT")
    arm("the count line totals every id", sum(counts.values()) == len(ids))
    # the negative control: a map naming a root that does NOT hold the cell must not be believed
    ids2, src2 = read_map(cmap.replace("root=r_named", "root=r_nowhere"))
    rows2, _ = resolve(ids2, src2, read_inventory(inv))
    arm("⭐ a source-named root that does not hold the cell is NOT believed (it falls through, here to AMBIGUOUS)",
        {r["cell"]: r for r in rows2}["c_src"]["rule"] == "AMBIGUOUS")
    res = read_resolved("c_tie\tr_a-cp\ta result's line 7\nc_one\tr1\tan attempt to override a rule\n")
    by3 = {r["cell"]: r for r in resolve(ids, src, read_inventory(inv), res)[0]}
    arm("RECORD: a cited resolution settles a REFUSED tie to the root it names", by3["c_tie"]["rule"] == "RECORD" and by3["c_tie"]["root"] == "r_a-cp"
        and by3["c_tie"]["citation"] == "a result's line 7")
    arm("⭐ a resolution on a cell the RULE decided is REFUSED (a citation never overrides a rule)", by3["c_one"]["rule"].startswith("RESOLUTION-REFUSED"))
    by4 = {r["cell"]: r for r in resolve(ids, src, read_inventory(inv), read_resolved("c_tie\tr_nowhere\tx\n"))[0]}
    arm("⭐ a resolution naming a root that does not hold the cell is REFUSED", by4["c_tie"]["rule"].startswith("RESOLUTION-REFUSED"))
    try: read_resolved("c_tie\tr_a\t\n"); arm("a resolution without a citation is REFUSED", False)
    except SystemExit: arm("a resolution without a citation is REFUSED", True)
    print("cellroots_v3 selftest: %s" % ("OK" if ok else "FAILED")); return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--map"); ap.add_argument("--inventory"); ap.add_argument("--out"); ap.add_argument("--resolved")
    ap.add_argument("--selftest", action="store_true"); a = ap.parse_args()
    if a.selftest: return selftest()
    if not (a.map and a.inventory): ap.print_usage(sys.stderr); return 2
    ids, src = read_map(open(a.map, encoding="utf-8").read())
    res = read_resolved(open(a.resolved, encoding="utf-8").read()) if a.resolved else {}
    rows, counts = resolve(ids, src, read_inventory(open(a.inventory, encoding="utf-8").read()), res)
    out = open(a.out, "w", encoding="utf-8") if a.out else sys.stdout
    emit(rows, counts, out)
    if a.out: out.close()
    bad = [r for r in rows if r["rule"] in ("AMBIGUOUS", "ABSENT") or r["rule"].startswith("RESOLUTION-REFUSED")]
    for r in bad: print("REFUSED %s %s candidates=%s" % (r["cell"], r["rule"], r["candidates"]), file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
