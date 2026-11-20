#!/usr/bin/env python3
"""web_brain_census.py — read-only census of the agy client's NETWORK tools (search_web, read_url_content)
and their RESULTS, read from the client's own conversation record (the "brain" transcript):
  <cell>/.agyhome/.gemini/antigravity-cli/brain/<conversation>/.system_generated/logs/transcript_full.jsonl

WHY THE BRAIN AND NOT THE STREAM. The main stream (ctl/stream-*.ndjson) records a client-executed tool as
step_update ACTIVE -> DONE with no result body, so a stream cannot tell a served call from a denied one.
The brain records the call (a PLANNER_RESPONSE step's tool_calls) and its result (the next GENERIC step).

CLASSES of a call's result step:
  SERVED  — "returned the following summary" (search_web) or a page body ("Content of" / no error) for read_url_content
  DENIED  — the result step says "permission check failed" or "denied" (the permission layer or a hook)
  OTHER   — a result step that is neither (printed so it is read, never counted as either)
  NO-RESULT — no GENERIC step within the next 3 records

Output (stdout, TSV): cell  conversation  tool  calls  served  denied  other  no_result  first_query
Trailer: '#POPULATION ...' with per-tool totals. Read-only; writes nothing.
usage: python3 -I web_brain_census.py [ROOT ...]   (default ROOT = $HOME; cells are ROOT/cells-*/<cell>/)
"""
import glob, json, os, sys

TOOLS = ("search_web", "read_url_content")


def classify(content):
    c = content
    if "permission check failed" in c or "denied permission" in c or "BLOCKED" in c:
        return "denied"
    if "returned the following summary" in c:
        return "served"
    if "Encountered error" in c:
        return "other"
    return "other"


roots = sys.argv[1:] or [os.path.expanduser("~")]
paths = []
for r in roots:
    paths += glob.glob(os.path.join(r, "cells-*", "*", ".agyhome", ".gemini", "antigravity-cli", "brain", "*",
                                    ".system_generated", "logs", "transcript_full.jsonl"))
paths = sorted(set(paths))
tot = {t: {"calls": 0, "served": 0, "denied": 0, "other": 0, "no_result": 0, "transcripts": 0} for t in TOOLS}
unread = 0
for p in paths:
    rows = []
    try:
        with open(p, "rb") as fh:
            for line in fh:
                try:
                    rows.append(json.loads(line.decode("utf-8", "replace")))
                except Exception:
                    rows.append(None)
    except Exception as e:
        unread += 1
        print(f"#UNREAD\t{p}\t{e}")
        continue
    per = {t: {"calls": 0, "served": 0, "denied": 0, "other": 0, "no_result": 0, "q": ""} for t in TOOLS}
    for i, r in enumerate(rows):
        if not isinstance(r, dict):
            continue
        for tc in r.get("tool_calls") or []:
            n = tc.get("name") if isinstance(tc, dict) else None
            if n not in TOOLS:
                continue
            per[n]["calls"] += 1
            if not per[n]["q"]:
                a = tc.get("args") or {}
                per[n]["q"] = str(a.get("query") or a.get("Url") or "")[:120]
            cls = "no_result"
            for r2 in rows[i + 1:i + 4]:
                if isinstance(r2, dict) and r2.get("type") == "GENERIC":
                    cls = classify(str(r2.get("content", "")))
                    break
            per[n][cls] += 1
    cell = p.split("/.agyhome/")[0]
    conv = p.split("/brain/")[1].split("/")[0]
    for t in TOOLS:
        d = per[t]
        if d["calls"]:
            tot[t]["transcripts"] += 1
            for k in ("calls", "served", "denied", "other", "no_result"):
                tot[t][k] += d[k]
            print("\t".join([cell, conv, t, str(d["calls"]), str(d["served"]), str(d["denied"]), str(d["other"]),
                             str(d["no_result"]), " ".join(d["q"].split())]))
summ = " ".join(f"{t}:transcripts={v['transcripts']},calls={v['calls']},served={v['served']},denied={v['denied']},"
                f"other={v['other']},no_result={v['no_result']}" for t, v in tot.items())
print(f"#POPULATION transcripts={len(paths)} unread={unread} {summ}")
