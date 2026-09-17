#!/usr/bin/env python3
"""hc1_subject_model_census.py <cells-home> -- for every HC1 cell (<cells-home>/cells-hc1-*/<id>/ctl), every
Agent/Task spawn its HEAD made, and the `model` parameter the SUBJECT passed on it (absent = the agent definition decides).
Read-only. The arm is read from the cell's own ctl/arm and the task from ctl/task, never from the root's name.
The transcript directory is <the cell's cfg, from ctl/run-cfg.tsv>/projects/<key>, key = the cell's repo path with every non-alphanumeric byte as '-'.
Output: one row per cell, then per-arm tallies. A cell with no transcript directory is printed as NO-TRANSCRIPT and
counted separately, never as a cell that passed no model."""
import collections, glob, json, os, re, sys
home = sys.argv[1]
def cell_cfg(c):
    # the cell's own CLAUDE_CONFIG_DIR, as its launcher recorded it in ctl/run-cfg.tsv (row `cfg`); never an argument
    for line in open(os.path.join(c, "ctl", "run-cfg.tsv")):
        k, _, v = line.rstrip("\n").partition("\t")
        if k == "cfg": return v
    return None
print("cell\tarm\ttask\ttranscript\tspawns\tspawns_with_model\tmodels_asked")
aside = []; cells = collections.Counter(); with_any = collections.Counter(); with_opus = collections.Counter(); notx = collections.Counter()
for c in sorted(glob.glob(os.path.join(home, "cells-hc1-*", "*"))):
    if not os.path.isdir(os.path.join(c, "ctl")): continue
    if "." in os.path.basename(c):
        # a directory renamed aside (e.g. <id>.FAILED-BUILD-...) is not a cell of the population; printed and counted, never skipped silently
        # only the id and the suffix's CLASS (its leading upper-case words) are printed: the rest of a suffix is free text
        stem, _, suffix = os.path.relpath(c, home).partition(".")
        m = re.match(r"[A-Z]+(?:-[A-Z]+)*", suffix); name = "%s.%s" % (stem, m.group(0) if m else "?")
        aside.append(name); print("\t".join([name, "-", "-", "ASIDE", "-", "-", "-"])); continue
    arm = open(os.path.join(c, "ctl", "arm")).read().strip()
    task = open(os.path.join(c, "ctl", "task")).read().split("\t")[0].strip()   # ctl/task is <task>\t<phase>\t...; the first field names the task
    key = re.sub(r"[^A-Za-z0-9]", "-", os.path.join(c, "repo"))
    cfg = cell_cfg(c)
    tdir = os.path.join(cfg, "projects", key) if cfg else ""
    cells[arm] += 1
    if not os.path.isdir(tdir):
        notx[arm] += 1
        print("\t".join([os.path.relpath(c, home), arm, task, "NO-TRANSCRIPT", "-", "-", "-"])); continue
    spawns = {}
    # the HEAD's own transcripts only: <tdir>/*.jsonl (sidechains live under <session>/subagents/ and are not searched)
    for f in sorted(glob.glob(os.path.join(tdir, "*.jsonl"))):
        for line in open(f, errors="replace"):
            try: m = json.loads(line)
            except ValueError: continue
            if m.get("type") != "assistant": continue
            for part in (m.get("message") or {}).get("content") or []:
                if isinstance(part, dict) and part.get("type") == "tool_use" and part.get("name") in ("Agent", "Task"):
                    spawns[part.get("id")] = (part.get("input") or {}).get("model")
    asked = [v for v in spawns.values() if v is not None]
    if asked: with_any[arm] += 1
    if "opus" in asked: with_opus[arm] += 1
    print("\t".join([os.path.relpath(c, home), arm, task, "read", str(len(spawns)), str(len(asked)),
                     ",".join("%s=%d" % kv for kv in sorted(collections.Counter(asked).items())) or "-"]))
if not cells:
    # a census of a HOME names no host: on the wrong box it would print an empty, clean-looking table. Refuse instead.
    sys.exit("REFUSE: no HC1 cell under %s -- this is not the box the cells ran on" % home)
for arm in sorted(cells):
    print("# ARM %s cells=%d no_transcript=%d with_explicit_model=%d asked_opus=%d" % (arm, cells[arm], notx[arm], with_any[arm], with_opus[arm]))
print("# ASIDE %d %s" % (len(aside), " ".join(aside) or "-"))
print("# TOTAL cells=%d no_transcript=%d with_explicit_model=%d asked_opus=%d" % (sum(cells.values()), sum(notx.values()), sum(with_any.values()), sum(with_opus.values())))
