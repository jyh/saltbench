#!/usr/bin/env python3
"""project_data.py — the ONLY dataset bytes present on the Studio during episodes: a projection of the
pilot rows to {instance_id, problem_statement, base_commit, repo, version}. No patch, no test_patch, no
hints_text, no F2P/P2P.   usage: project_data.py <verified.json> <TASKLIST.json> <out problem_statements.json>"""
import json, sys, hashlib
rows = json.load(open(sys.argv[1])); pilot = set(json.load(open(sys.argv[2]))["pilot"])
KEEP = ("instance_id", "problem_statement", "base_commit", "repo", "version")
out = [{k: r[k] for k in KEEP} for r in rows if r["instance_id"] in pilot]
assert len(out) == len(pilot), (len(out), len(pilot))
for r in out: assert set(r) == set(KEEP)
txt = json.dumps(out, sort_keys=True, separators=(",", ":"))
open(sys.argv[3], "w").write(txt)
print("rows", len(out), "sha256", hashlib.sha256(txt.encode()).hexdigest())
