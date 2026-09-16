#!/usr/bin/env python3
"""lk_wait_census.py -- per-arm census of HC1 cells for build-lock waits. Zero spend, read-only.

A cell's bin/rt serialises builds on the cell's own .seat/rt.lock, and its detached runner keeps building after a
cut caller, so the NEXT rt call waits and prints the exact line below to the subject. That line is the in-cell
analogue of desk LK's wedge (a build that outlives its caller holding the lock the next build needs).
Second column: any mention of the fleet build wrapper (LK's own mechanism), expected 0 in cells that never call it.
Population: every ~/cells-hc1-*/hc1*/ cell dir. A cell without ctl/end-1 is LIVE and is listed, never counted.
Transcripts: every *.jsonl under the cell's client project slug (head and sub-agent files alike).
"""
import glob, os, re, sys, collections
HOME = os.path.expanduser("~")
CFG = os.path.join(HOME, "<run-config-dir>", "projects")
WAIT = "rt: a build is already running here; waiting for it"
FLEET = "saltbuild"
rows = []
for cell in sorted(glob.glob(os.path.join(HOME, "cells-hc1-*", "hc1*", ""))):
    cid = os.path.basename(cell.rstrip("/"))
    rd = lambda f: (open(os.path.join(cell, "ctl", f)).read().strip() if os.path.exists(os.path.join(cell, "ctl", f)) else "?")
    arm, task = rd("arm"), rd("task").split()[0] if rd("task") != "?" else "?"
    ended = os.path.exists(os.path.join(cell, "ctl", "end-1"))
    slug = os.path.join(CFG, re.sub(r"[^A-Za-z0-9]", "-", os.path.join(cell.rstrip("/"), "repo")))
    js = glob.glob(os.path.join(slug, "**", "*.jsonl"), recursive=True)
    nwait = nfleet = 0; cells_with = 0
    for j in js:
        t = open(j, errors="replace").read()
        nwait += t.count(WAIT); nfleet += t.count(FLEET)
    rt = os.path.join(cell, "repo", "bin", "rt")
    ctrl = WAIT in open(rt).read() if os.path.exists(rt) else None
    rows.append(dict(cid=cid, task=task, arm=arm, ended=ended, njs=len(js), wait=nwait, fleet=nfleet, ctrl=ctrl))
print("population: %d HC1 cell dirs; needle %r; control = the needle occurs in the cell's own bin/rt" % (len(rows), WAIT))
for r in rows:
    print("%-9s %-9s %-9s %-5s jsonl=%-2d wait_lines=%-3d fleet_wrapper_mentions=%-3d rt_control=%s"
          % (r["cid"], r["task"], r["arm"], "END" if r["ended"] else "LIVE", r["njs"], r["wait"], r["fleet"], r["ctrl"]))
agg = collections.defaultdict(lambda: [0, 0, 0, 0])
for r in rows:
    if not r["ended"]: continue
    a = agg[r["arm"]]; a[0] += 1; a[1] += (r["wait"] > 0); a[2] += r["wait"]; a[3] += (r["fleet"] > 0)
print("\nper arm, ENDED cells only:  arm  cells  cells_with_a_wait  wait_lines  cells_mentioning_fleet_wrapper")
for arm in sorted(agg):
    print("  %-9s %3d %3d %4d %3d" % (arm, *agg[arm]))
bad = [r["cid"] for r in rows if r["ctrl"] is not True]
print("rt control failed or absent for: %s" % (bad or "none"))
nojs = [r["cid"] for r in rows if r["ended"] and r["njs"] == 0]
print("ENDED cells with NO transcript found (UNMEASURED, not zero): %s" % (nojs or "none"))
