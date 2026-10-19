#!/usr/bin/env python3
"""ratio-correction-2026-10-19-verify.py [--selftest]

Re-derive every figure in the 2026-10-19 correction addenda (blocks SBS, SS, SG; census ADDENDUM 38) and the paper's corrected
ratio sentence FROM the block tables, and assert each against the BYTES of the addendum it belongs to. No typed expectations:
each expected string is COMPUTED. The addendum is the text after its `## §C ·` / `# ⚖️ ADDENDUM 38` heading, so a figure that
appears only in the unedited body above cannot satisfy a check.
rc 0 all found · 1 a mismatch, named."""
import csv, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
BL = os.path.join(ROOT, "evidence", "claude-lane-blocks-2026-09-21")
TEX = os.path.join(ROOT, "paper", "saltbench-v1.tex")

def rows(name):
    return [r for r in csv.DictReader((l for l in open(os.path.join(BL, name), encoding="utf-8") if not l.startswith("#")),
                                      delimiter="\t")]

def ratios(block):
    R = rows("block%s-cells.tsv" % block)
    c = {a: [float(r["final_COST"]) for r in R if r["arm"] == a] for a in ("plain", "salt-diet")}
    T = {a: sum(int(r["final_T"]) for r in R if r["arm"] == a) for a in ("plain", "salt-diet")}
    mp, ms = statistics.median(c["plain"]), statistics.median(c["salt-diet"])
    tp, ts = sum(c["plain"]), sum(c["salt-diet"])
    f = lambda x: "%.2fx" % x
    return dict(n=len(R), med=f(ms / mp), med_p=f(round(ms, 2) / round(mp, 2)), tot=f(ts / tp), tot_p=f(round(ts, 2) / round(tp, 2)),
                T=f(T["salt-diet"] / T["plain"]))

def tail(path, marker):
    t = open(path, encoding="utf-8").read()
    assert t.count(marker) == 1, (path, marker)
    return t[t.index(marker):]

def checks():
    """-> list of (where, label, expected string). Every expected value COMPUTED."""
    out = []
    H = lambda b: os.path.join(HERE, "RESULT-claude-block%s-2026-09-21.md" % b)
    sbs, ss, sg = ratios("SBS"), ratios("SS"), ratios("SG")
    o, os_ = ratios("O"), ratios("OS")
    # SBS §C: F1 figures, F4 ratios
    R = rows("blockSBS-cells.tsv")
    arm = lambda a: [r for r in R if r["arm"] == a]
    sv = {a: [float(r["surv"]) for r in arm(a)] for a in ("plain", "salt-diet")}
    kept = {a: sum(int(r["kept"]) for r in arm(a)) for a in ("plain", "salt-diet")}
    seed = sum(int(r["seed_lines"]) for r in arm("plain"))
    w = ("SBS", H("SBS"), "## §C ·")
    out += [(w, "median surv", "median `surv` %.3f against plain's %.3f" % (statistics.median(sv["salt-diet"]), statistics.median(sv["plain"]))),
            (w, "kept", "total `kept` %d against %d of %d seed lines each" % (kept["salt-diet"], kept["plain"], seed)),
            (w, "floors", "worst `surv` (%.3f) is\n   above plain's worst (%.3f)" % (min(sv["salt-diet"]), min(sv["plain"]))),
            (w, "median ratio", "ratio **%s** (printed %s)" % (sbs["med"], sbs["med_p"])),
            (w, "total ratio", "total COST ratio **%s** (printed %s)" % (sbs["tot"], sbs["tot_p"])),
            (w, "T ratio", "total T %s is right" % sbs["T"])]
    assert sbs["med"] != sbs["med_p"] and sbs["tot"] != sbs["tot_p"]
    # SS §C
    w = ("SS", H("SS"), "## §C ·")
    assert ss["med"] != ss["med_p"] and ss["tot"] == ss["tot_p"]
    out += [(w, "median ratio", "it is **%s** (printed %s)" % (ss["med"], ss["med_p"])),
            (w, "total+T", "total COST ratio %s and the T ratio %s are right" % (ss["tot"], ss["T"]))]
    out.append((w, "SG quoted", "quoted block-SG figure (%s) is likewise **%s** unrounded" % (sg["med_p"].replace("x", "×"), sg["med"].replace("x", "×"))))
    # OS §C: the three Sonnet ratios it quotes
    w = ("OS", H("OS"), "## §C ·")
    out.append((w, "quoted", "**%s (SG), %s (SS) and %s (SBS)**" % tuple(r["med"].replace("x", "×") for r in (sg, ss, sbs))))
    # SG §C
    w = ("SG", H("SG"), "## §C ·")
    assert sg["med"] != sg["med_p"] and sg["tot"] == sg["tot_p"]
    out += [(w, "cells", "`blockSG-cells.tsv`, %d cells" % sg["n"]),
            (w, "median ratio", "the unrounded ratio is **%s** (printed %s)" % (sg["med"], sg["med_p"])),
            (w, "total+T", "ratio %s and the T ratio %s are right" % (sg["tot"], sg["T"]))]
    # census ADDENDUM 38 table
    w = ("census", os.path.join(HERE, "CENSUS-full-matrix-2026-09-14.md"), "# ⚖️ ADDENDUM 38")
    out += [(w, "SG row", "SG       %s      %s     blockSG-cells.tsv (%d cells)" % (sg["med_p"], sg["med"], sg["n"])),
            (w, "SS row", "SS       %s      %s     blockSS-cells.tsv" % (ss["med_p"], ss["med"])),
            (w, "SBS row", "SBS      %s      %s     blockSBS-cells.tsv     (and its total COST ratio: %s printed, %s unrounded)"
                % (sbs["med_p"], sbs["med"], sbs["tot_p"], sbs["tot"])),
            (w, "O row", "O        %s      %s     right" % (o["med_p"], o["med"])),
            (w, "OS row", "OS       %s      %s     right" % (os_["med_p"], os_["med"]))]
    assert o["med"] == o["med_p"] and os_["med"] == os_["med_p"]
    # the paper: the corrected sentence, and the OS ratio it compares against
    t = lambda x: "$%s\\times$" % x[:-1]
    w = ("tex", TEX, None)
    out += [(w, "sonnet ratios", "all lower bounds, are %s, %s and %s." % (t(sg["med"]), t(ss["med"]), t(sbs["med"]))),
            (w, "OS ratio", "is %s at twelve cells an arm" % t(os_["med"])),
            (w, "split equal", "probe-in readings of %s and %s, equal to the record's" % (t(ss["med"]), t(sbs["med"]))),
            (w, "SG record", "where the record reads %s" % t(sg["med"])),
            (w, "v4 note", "printed as %s, %s and %s: each was a ratio of two rounded medians, and from the unrounded tables they are %s, %s and %s"
                % (t(sg["med_p"]), t(ss["med_p"]), t(sbs["med_p"]), t(sg["med"]), t(ss["med"]), t(sbs["med"])))]
    gone = ["all lower bounds, are " + t(sg["med_p"]) + ", " + t(ss["med_p"]) + " and " + t(sbs["med_p"]), "a hundredth below the record",
            "where the record reads %s" % t(sg["med_p"])]
    return out, gone

def run(over=None):
    over = over or {}
    C, gone = checks()
    miss = []
    for (where, path, marker), label, s in C:
        text = over.get(path) or open(path, encoding="utf-8").read()
        if marker:
            assert text.count(marker) == 1, (path, marker)
            text = text[text.index(marker):]
        if s not in text: miss.append((where, label, s))
    tex = over.get(TEX) or open(TEX, encoding="utf-8").read()
    for s in gone:
        if s in tex: miss.append(("tex", "OLD figures still present", s))
    for w, l, s in miss: print("MISSING  %-7s %-14s expected %r" % (w, l, s))
    n = len(C) + len(gone)
    print("%s: %d figures re-derived, %d found" % ("OK" if not miss else "FAIL", n, n - len(miss)))
    return 0 if not miss else 1

def selftest():
    bad = 0
    sbs = os.path.join(HERE, "RESULT-claude-blockSBS-2026-09-21.md")
    for path, old, new in ((TEX, "and $4.70\\times$. It cannot", "and $4.71\\times$. It cannot"), (sbs, "ratio **4.70x**", "ratio **4.71x**"),
                           (os.path.join(HERE, "CENSUS-full-matrix-2026-09-14.md"), "8.29x     blockSG", "8.27x     blockSG")):
        t = open(path, encoding="utf-8").read(); assert t.count(old) == 1, old
        rc = run({path: t.replace(old, new)}); print("  mutant %r -> rc %d" % (old, rc)); bad += rc != 1
    rc = run(); print("  original -> rc %d" % rc)
    return 0 if bad == 0 and rc == 0 else 1

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else run())
