#!/usr/bin/env python3
"""extract_verus.py — pull the agent-writable BODIES out of the agent's edited file by the section markers,
and nothing else. One rung, "P" (proof): the target's proof body and the top-level helper lemmas.

Every statement comes from frozen.json at assembly, so a change the agent makes OUTSIDE its two regions is
structurally discarded: statement immutability BY CONSTRUCTION, which is layer 0 of the grader.

⚠️ AMENDMENT 14's LAW BINDS THIS FILE AND THE `_present` IT WRITES: a finding about an AGENT must be measured
on a file the AGENT wrote. `_present` is read off the agent's `task.rs` and NEVER off the assembled canonical
(the canonical carries no markers at all, by design — reading it would report SCAFFOLD_DAMAGED on every
episode). `_present` is what `check_verus.py` gates SCAFFOLD_DAMAGED on; it is a marker-pair fact and never a
content fact.

usage: extract_verus.py <agent file>   ->  JSON on stdout
"""
import json, re, sys

SEC = re.compile(r"//\s*start_def\s+(\w+)\s*[\r\n]+(.*?)//\s*end_def\s+\1", re.DOTALL | re.IGNORECASE)
WANT = {"P": ["proof", "helpers"]}

if len(sys.argv) != 2:
    sys.exit(__doc__)
found = {}
for m in SEC.finditer(open(sys.argv[1], encoding="utf-8", errors="replace").read()):
    found.setdefault(m.group(1).strip(), []).append(m.group(2).strip())
out = {k: (found.get(k) or [""])[0] for k in WANT["P"]}
out["_present"] = {k: (k in found) for k in WANT["P"]}
print(json.dumps(out))
