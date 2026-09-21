#!/usr/bin/env python3
"""slug_split_census.py [--home H] [--require CELL] [--json] [--selftest]

Census every cell's SESSION SLUG DIRECTORY across config dirs, and name any cell whose sessions are
SPLIT across more than one. Desk VV / VW, 2026-09-21.

⛔⛔ WHY THIS EXISTS, AND WHY NOTHING ELSE SEES IT. `cell-watch.sh:448` builds the meter's population as
  `$CLAUDE_CONFIG_DIR/projects/<cell repo path>`, so the meter is scoped to the POOL, not to the CELL.
  A cell whose phases (or whose probe and task) ran on DIFFERENT POOLS has its records under two config
  dirs, and every per-cell instrument that reads that slug — cell_meter, seal_kept, seal_aim, canary —
  sees one side only. ⇒ THE FIELD IS NOT "CUMULATIVE OVER THE CELL", IT IS "CUMULATIVE OVER THE POOL",
  AND THOSE COINCIDE ONLY WHEN THE CELL DID NOT MOVE.
  ⇒ MEASURED 2026-09-21 over 170 cells: 4 split. Two were a spec-change pair losing a WHOLE PHASE from
  the cumulative column; two were in blocks that ALREADY HAD RESULTS OF RECORD.
⛔ IT IS A CENSUS, NOT A VERDICT. A split is not by itself an error — a probe on another pool is a
  legitimate split. What is NEVER legitimate is a split nobody knows about, because the instruments that
  read the slug report the half they can see as if it were the whole.

⛔⛔ THE POSITIVE CONTROL IS NOT OPTIONAL AND THE REASON IS THIS TOOL'S OWN BIRTH. The first census of
  this exact condition used the needle `clb[a-z]{4}\\d{2}` where a cell id is `clb` + THREE letters + two
  digits, and it read 0 CELLS IN 170 — while the config-dir listing printed beside it as a "control"
  fired perfectly. ⇒ THAT CONTROL PROVED THE HAYSTACK WAS READABLE AND SAID NOTHING ABOUT THE PATTERN.
  `--require CELL` asserts a cell you KNOW exists is found, which is the only control that tests the
  NEEDLE against a member of the population. Without it, a zero here is UNVERIFIED, and this tool says so.

rc 0 no split (or census only) · 1 at least one cell is SPLIT · 2 the control failed — the census is a
REFUSAL, not an answer · 3 usage.
"""
import os, re, glob, json, argparse, sys, collections

# `clb` + three letters (block, problem, arm) + two digits. Derived from the id builder, not typed twice.
CELL_RE = re.compile(r'(clb[a-z]{3}\d{2})')

def census(home):
    """-> (cells{cell: {cfg: n_jsonl}}, cfgs_scanned, cfgs_without_projects)"""
    cells = collections.defaultdict(dict)
    scanned, noproj = [], []
    for c in sorted(glob.glob(os.path.join(home, ".claude-account-*")) +
                    glob.glob(os.path.join(home, ".claude-acct-*"))):
        name = os.path.basename(c)
        pd = os.path.join(c, "projects")
        if not os.path.isdir(pd):
            noproj.append(name); continue
        scanned.append(name)
        for d in os.listdir(pd):
            m = CELL_RE.search(d)
            if not m: continue
            n = len(glob.glob(os.path.join(pd, d, "*.jsonl")))
            cells[m.group(1)][name] = cells[m.group(1)].get(name, 0) + n
    return cells, scanned, noproj

def run(home, require, as_json):
    cells, scanned, noproj = census(home)
    split = {k: v for k, v in cells.items() if len(v) > 1}
    # ⛔ THE COVERAGE LINE IS ONLY AS WIDE AS THE PATTERN THAT BUILT ITS POPULATION, so both halves are
    #   declared: what was scanned AND what was found without a projects/ dir (never silently omitted).
    out = {"config_dirs_scanned": scanned, "config_dirs_without_projects": noproj,
           "cells": len(cells), "split": {k: v for k, v in sorted(split.items())},
           "by_block": dict(sorted(collections.Counter(k[3] for k in cells).items())),
           "control": require, "control_found": (require in cells) if require else None}
    if as_json:
        print(json.dumps(out, indent=2))
    else:
        print("config dirs scanned:            %s" % (", ".join(scanned) or "NONE"))
        if noproj: print("config dirs with no projects/:  %s  (declared, not skipped)" % ", ".join(noproj))
        print("cells with a slug dir:          %d   by block: %s" % (len(cells), out["by_block"]))
        if require:
            print("POSITIVE CONTROL %-14s %s" % (require, "FOUND" if out["control_found"] else "⛔ NOT FOUND"))
        print("cells SPLIT across >1 config dir: %d" % len(split))
        for k in sorted(split):
            print("   %-10s %s" % (k, "  ".join("%s=%d jsonl" % (c, n) for c, n in sorted(split[k].items()))))
    if require and not out["control_found"]:
        print("⛔ THE CONTROL WAS NOT FOUND, so this census is a REFUSAL and not a zero. The needle, the "
              "home or the population is wrong — do not read the split count above as an answer.",
              file=sys.stderr)
        return 2
    if require is None and not split:
        print("⚠️  no --require CELL was given, so a zero here is UNVERIFIED: nothing tested the needle "
              "against a member of the population.", file=sys.stderr)
    return 1 if split else 0

def selftest():
    """RED FIRST on a fixture: a split cell must be FOUND, an unsplit one must not be reported, and the
    control must be able to FAIL — the arm that the tool's own birth defect would have passed."""
    import tempfile
    fails = []
    with tempfile.TemporaryDirectory() as h:
        def mk(cfg, cell, n):
            d = os.path.join(h, ".claude-account-" + cfg, "projects", "-Users-jyh-" + cell)
            os.makedirs(d, exist_ok=True)
            for i in range(n): open(os.path.join(d, "s%d.jsonl" % i), "w").close()
        mk("poolA", "clbclp03", 2); mk("poolB", "clbclp03", 2)      # SPLIT
        mk("poolA", "clbclp01", 4)                                   # unsplit
        os.makedirs(os.path.join(h, ".claude-account-nocreds"), exist_ok=True)  # no projects/
        cells, scanned, noproj = census(h)
        a = len(cells) == 2 and set(cells["clbclp03"]) == {".claude-account-poolA", ".claude-account-poolB"}
        print("  arm 1 split cell found, unsplit not split   %s" % ("PASS" if a else "FAIL"))
        if not a: fails.append(1)
        b = noproj == [".claude-account-nocreds"]
        print("  arm 2 a dir with no projects/ is DECLARED   %s" % ("PASS" if b else "FAIL"))
        if not b: fails.append(2)
        rc = run(h, "clbclp03", False)
        print("  arm 3 rc=1 when a split exists, control OK   %s" % ("PASS" if rc == 1 else "FAIL"))
        if rc != 1: fails.append(3)
        # ⭐ THE ARM FOR THIS TOOL'S OWN BIRTH DEFECT: a control naming an ABSENT cell must REFUSE (rc 2),
        #   not quietly report a count. Without this arm, a wrong needle reads as a clean census.
        rc = run(h, "clbzzz99", False)
        print("  arm 4 absent control REFUSES rc=2           %s" % ("PASS" if rc == 2 else "FAIL"))
        if rc != 2: fails.append(4)
        # arm 5: the needle itself — the {4} that read 0 in 170 must NOT match a real id
        bad = re.compile(r'(clb[a-z]{4}\d{2})')
        c5 = bad.search("-Users-jyh-clbclp03") is None and CELL_RE.search("-Users-jyh-clbclp03") is not None
        print("  arm 5 the born-wrong needle {4} matches NOT  %s" % ("PASS" if c5 else "FAIL"))
        if not c5: fails.append(5)
    print()
    if fails:
        print("⛔ SELFTEST FAILED on arm(s) %s" % fails); return 1
    print("✅ SELFTEST 5/5 — a split is found, an unsplit is not, a credential-less dir is DECLARED,\n"
          "   an absent control REFUSES rather than reporting a count, and the needle that read 0 in 170\n"
          "   is pinned as a RED so it cannot come back.")
    return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--home", default=os.path.expanduser("~"))
    ap.add_argument("--require", help="a cell id you KNOW exists; a census that cannot find it is a REFUSAL")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else run(a.home, a.require, a.json))
