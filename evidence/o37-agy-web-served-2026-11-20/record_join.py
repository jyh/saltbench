#!/usr/bin/env python3
"""record_join.py — join the agy CELLS OF RECORD (records.tsv, from record_list.py) to the brain-transcript
web census (census.tsv, from web_brain_census.py), on the run box.

Per cell of record, the cell directory is located as $HOME/<root>/<cell> when the record names a root, else by
id over $HOME/cells-*/<cell> (a by-id match in more than one family is AMBIGUOUS, and every family is read).
STATES (one per cell of record):
  WEB-SERVED  a transcript of the cell carries >= 1 served search_web / read_url_content result
  CLEAN       >= 1 brain transcript read, 0 served (denied calls are counted beside it)
  UNMEASURED  the cell directory has no brain transcript, or no directory was found: never read as clean
Output TSV: block cell model arm match families transcripts web_calls served denied state queries
Trailer: '#STATE <block> <state> <n>' lines and '#TOTAL' — the table that the README prints.
usage: python3 -I record_join.py records.tsv census.tsv
"""
import collections, glob, os, sys

H = os.path.expanduser("~")
census = collections.defaultdict(lambda: [0, 0, 0, []])  # cell dir -> calls, served, denied, queries
for l in open(sys.argv[2]):
    if l.startswith("#"):
        continue
    f = l.rstrip("\n").split("\t")
    cell, conv, tool, calls, served, denied, other, nores, q = f
    c = census[cell]
    c[0] += int(calls); c[1] += int(served); c[2] += int(denied)
    if int(served) and q:
        c[3].append(q)

BRAIN = ".agyhome/.gemini/antigravity-cli/brain/*/.system_generated/logs/transcript_full.jsonl"
tally = collections.Counter()
for l in open(sys.argv[1]):
    if l.startswith("#") or not l.strip():
        continue
    block, cell, root, model, arm, src = l.rstrip("\n").split("\t")
    if root != "-":
        dirs = [os.path.join(H, root, cell)]
        match = "root"
    else:
        dirs = sorted(glob.glob(os.path.join(H, "cells-*", cell)))
        match = "id" if len(dirs) == 1 else ("ambiguous-id" if dirs else "none")
    dirs = [d for d in dirs if os.path.isdir(d)]
    trs = []
    for d in dirs:
        trs += glob.glob(os.path.join(d, BRAIN))
    calls = served = denied = 0
    qs = []
    for d in dirs:
        c = census.get(d)
        if c:
            calls += c[0]; served += c[1]; denied += c[2]; qs += c[3]
    if not trs:
        state = "UNMEASURED"
    elif served:
        state = "WEB-SERVED"
    else:
        state = "CLEAN"
    tally[(block, state)] += 1
    tally[("ALL", state)] += 1
    fams = ",".join(os.path.basename(os.path.dirname(d)) for d in dirs) or "-"
    print("\t".join([block, cell, model, arm, match, fams, str(len(trs)), str(calls), str(served), str(denied), state,
                     " | ".join(qs)[:300] or "-"]))
for (b, s), n in sorted(tally.items()):
    print(f"#STATE\t{b}\t{s}\t{n}")
