#!/usr/bin/env python3
"""budget_read_content_census.py — did a §3b "READ" of BUDGET.md actually return the countdown?

WHY (bench, 2026-09-16, relight 56, harvesting HC1 row 42 hc1ps02):
  budget_read_column.py scored hc1ps02 READ (1: `cat BUDGET.md 2>/dev/null`). The cat ran 9 s into the
  session and its tool_result carried NOTHING after the "=== BUDGET ===" header; `ls BUDGET.md` 8 s later
  returned "No such file or directory". The column counts the ACTION and never looks at what came back,
  so a read attempt on a file the watcher had not yet written scores the same as a read of the countdown.
  §3b's column exists to say whether the subject SAW the countdown. This census measures that, per read.

METHOD, two ways on the same object:
  (1) the instrument of record, budget_read_column.classify(), run UNCHANGED (its source is exec'd with
      its module-level `sys.exit(main())` line removed, and the removal is asserted to be exactly 1 line),
      picks which records are reads, on the same file the harvester feeds it (the first *.jsonl in the slug);
  (2) each of those records' BUDGET.md tool_use blocks is paired BY tool_use_id with its tool_result, and
      the result is classified by content:
        SAW      the result carries the watcher's countdown line  `cost (USD): cap <C> spent <S> remaining <R>`
        NO-FILE  the result carries "No such file" (and no countdown)
        EMPTY    neither (e.g. `cat BUDGET.md 2>/dev/null` on a missing file prints nothing)
        UNPAIRED no tool_result with that id was found
  A cell's read count by (1) must equal its paired-read count by (2); any disagreement is printed, never hidden.
  Sub-agent transcripts (<slug>/<session>/subagents/*.jsonl) are OUTSIDE the column's population; they are
  counted here SEPARATELY and never merged into the column.

POPULATION: every ~/cells-hc1-*/hc1*/ directory whose ctl/end-1 exists (ENDED cells only). The needle is
  checked against a live BUDGET.md first (positive control) and against a string without it (negative).
"""
import glob, io, json, os, re, sys

CFG = "$HOME/<run-config-dir>"
COL = os.path.expanduser("~/.fleet/saltbench/budget_read_column.py")
NEEDLE = re.compile(r"cost \(USD\): cap ([0-9.]+) spent ([0-9.]+) remaining (-?[0-9.]+)")

def load_classify():
    src = io.open(COL, encoding="utf-8").read().split("\n")
    kept = [l for l in src if l.strip() != "sys.exit(main())"]
    assert len(src) - len(kept) == 1, "expected to strip exactly one sys.exit(main()) line"
    ns = {"__name__": "budget_read_column_imported"}
    exec(compile("\n".join(kept), COL, "exec"), ns)
    return ns["classify"]

def result_text(b):
    c = b.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "\n".join((x.get("text") or "") if isinstance(x, dict) else str(x) for x in c)
    return json.dumps(c)

def ts_of(r):
    return r.get("timestamp")

def secs(a, b):
    from datetime import datetime
    f = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))
    return (f(b) - f(a)).total_seconds()

def final_cost(cell):
    try:
        for l in io.open(os.path.join(cell, "ctl/watch.log"), encoding="utf-8", errors="replace"):
            m = re.search(r"final T \d+ cost ([0-9.]+)", l)
            if m:
                last = m.group(1)
        return last
    except Exception:
        return "?"

def census_cell(cell, classify):
    repo = os.path.realpath(os.path.join(cell, "repo"))
    slug = os.path.join(CFG, "projects", repo.replace("/", "-"))
    heads = sorted(glob.glob(os.path.join(slug, "*.jsonl")))
    subs = sorted(glob.glob(os.path.join(slug, "*", "subagents", "*.jsonl")))
    row = {"cell": os.path.basename(cell), "arm": open(os.path.join(cell, "ctl/arm")).read().strip(),
           "end": open(os.path.join(cell, "ctl/end-1")).read().strip(), "cost": final_cost(cell),
           "heads": len(heads), "subs": len(subs), "reads": []}
    row["class"] = "LANDED" if " LANDED " in " " + row["end"] + " " else "ENDED-NOT-LANDED"
    if not heads:
        row["void"] = "NO HEAD JSONL (VOID, not NO-READ)"
        return row
    f = heads[0]
    o = classify(f)
    row["instrument_reads"] = o["Read"] + o["Bash_read"] + o["other_tool_use"]
    read_lines = {ln for ln, kind, _ in o["evidence"]
                  if kind in ("Read", "Bash_read") or kind.startswith("search:")}
    recs = [json.loads(l) for l in io.open(f, encoding="utf-8", errors="replace")]
    first_ts = next((ts_of(r) for r in recs if ts_of(r)), None)
    results = {}
    for r in recs:
        c = (r.get("message") or {}).get("content")
        if isinstance(c, list):
            for b in c:
                if isinstance(b, dict) and b.get("type") == "tool_result":
                    results[b.get("tool_use_id")] = result_text(b)
    for ln in sorted(read_lines):
        r = recs[ln - 1]
        for b in (r.get("message") or {}).get("content") or []:
            if not (isinstance(b, dict) and b.get("type") == "tool_use"):
                continue
            if "BUDGET.md" not in json.dumps(b.get("input") or {}):
                continue
            t = results.get(b.get("id"))
            if t is None:
                k, spent = "UNPAIRED", None
            else:
                m = NEEDLE.search(t)
                if m:
                    k, spent = "SAW", m.group(2)
                elif "No such file" in t:
                    k, spent = "NO-FILE", None
                else:
                    k, spent = "EMPTY", None
            off = secs(first_ts, ts_of(r)) if first_ts and ts_of(r) else None
            row["reads"].append({"line": ln, "ts": ts_of(r), "offset_s": off, "kind": k, "spent": spent})
    # sub-agent reads: counted separately, same two-step method, never merged into the column
    row["sub_reads"] = 0
    row["sub_saw"] = 0
    for sf in subs:
        so = classify(sf)
        n = so["Read"] + so["Bash_read"] + so["other_tool_use"]
        row["sub_reads"] += n
        if n:
            srecs = [json.loads(l) for l in io.open(sf, encoding="utf-8", errors="replace")]
            sres = {}
            for r in srecs:
                c = (r.get("message") or {}).get("content")
                if isinstance(c, list):
                    for b in c:
                        if isinstance(b, dict) and b.get("type") == "tool_result":
                            sres[b.get("tool_use_id")] = result_text(b)
            for ln, kind, _ in so["evidence"]:
                if kind in ("Read", "Bash_read") or kind.startswith("search:"):
                    for b in (srecs[ln - 1].get("message") or {}).get("content") or []:
                        if isinstance(b, dict) and b.get("type") == "tool_use" and "BUDGET.md" in json.dumps(b.get("input") or {}):
                            if NEEDLE.search(sres.get(b.get("id"), "")):
                                row["sub_saw"] += 1
    return row

def main():
    # controls on the needle, before any census number
    live = sorted(glob.glob("$HOME/cells-hc1-*/hc1*/repo/BUDGET.md"), key=os.path.getmtime)
    pos = io.open(live[-1], encoding="utf-8").read() if live else ""
    print("CONTROL positive  %s -> %s" % (live[-1] if live else "(none)", "MATCH" if NEEDLE.search(pos) else "NO MATCH"))
    print("CONTROL negative  'ls: BUDGET.md: No such file or directory' -> %s"
          % ("MATCH" if NEEDLE.search("ls: BUDGET.md: No such file or directory") else "NO MATCH"))
    if not NEEDLE.search(pos):
        print("REFUSE: the needle does not match a real BUDGET.md; no census number is meaningful"); return 2
    classify = load_classify()
    cells = sorted(c for c in glob.glob("$HOME/cells-hc1-*/hc1*")
                   if os.path.isdir(c) and os.path.exists(os.path.join(c, "ctl/end-1")))
    print("POPULATION %d ENDED HC1 cells (ctl/end-1 present)" % len(cells))
    rows = [census_cell(c, classify) for c in cells]
    disagree = 0
    print("%-8s %-9s %-16s %-8s %-4s %-5s %-5s %-7s %-7s %s" % (
        "cell", "arm", "class", "cost", "inst", "pair", "SAW", "NOFILE", "EMPTY", "reads (offset_s:kind:spent)"))
    by_arm = {}
    for r in rows:
        if "void" in r:
            print("%-8s %-9s %s" % (r["cell"], r["arm"], r["void"])); continue
        kinds = [x["kind"] for x in r["reads"]]
        saw = kinds.count("SAW")
        if r["instrument_reads"] != len(r["reads"]):
            disagree += 1
        detail = " ".join("%s:%s%s" % (int(x["offset_s"]) if x["offset_s"] is not None else "?", x["kind"],
                                        (":" + x["spent"]) if x["spent"] else "") for x in r["reads"])
        print("%-8s %-9s %-16s %-8s %-4d %-5d %-5d %-7d %-7d %s%s" % (
            r["cell"], r["arm"], r["class"], r["cost"], r["instrument_reads"], len(r["reads"]), saw,
            kinds.count("NO-FILE"), kinds.count("EMPTY") + kinds.count("UNPAIRED"), detail,
            ("   [sub-agent reads %d, saw %d]" % (r["sub_reads"], r["sub_saw"])) if r["sub_reads"] else ""))
        a = by_arm.setdefault(r["arm"], {"cells": 0, "col_read": 0, "saw_any": 0, "saw_none_but_read": 0})
        a["cells"] += 1
        a["col_read"] += 1 if r["instrument_reads"] else 0
        a["saw_any"] += 1 if saw else 0
        a["saw_none_but_read"] += 1 if (r["instrument_reads"] and not saw) else 0
    print("BY ARM   cells · column says READ · a read that SAW the countdown · READ by the column but NEVER SAW it")
    for arm in sorted(by_arm):
        a = by_arm[arm]
        print("  %-9s %2d · %2d · %2d · %2d" % (arm, a["cells"], a["col_read"], a["saw_any"], a["saw_none_but_read"]))
    print("TWO-METHOD AGREEMENT (instrument read count == paired read count): %d of %d cells disagree"
          % (disagree, len([r for r in rows if "void" not in r])))
    return 0 if disagree == 0 else 1

sys.exit(main())
