#!/usr/bin/env python3
"""extract.py — pull the agent-writable BODIES out of the agent's edited file by the section markers, and nothing else.
Stage A: generated_spec_body. Stage B: spec_isomorphism_proof + iso_helper_lemmas. Stage C: implementation +
correctness_proof + correctness_helper_lemmas. Every statement comes from frozen.json at assembly, so a change the
agent makes OUTSIDE its bodies is structurally discarded (statement immutability by construction).
usage: extract.py <stage A|B|C> <agent file> -> JSON on stdout"""
import json, re, sys
SEC = re.compile(r"--\s*start_def\s+(\w+)\s*[\r\n]+(.*?)--\s*end_def\s+\1", re.DOTALL | re.IGNORECASE)
WANT = {"A": ["generated_spec_body"], "B": ["spec_isomorphism_proof", "iso_helper_lemmas"], "C": ["implementation", "correctness_proof", "correctness_helper_lemmas"]}
stage, path = sys.argv[1], sys.argv[2]
s = {}
for m in SEC.finditer(open(path, encoding="utf-8", errors="replace").read()):
    s.setdefault(m.group(1).strip(), []).append(m.group(2).strip())
out = {k: (s.get(k) or [""])[0] for k in WANT[stage]}
out["_present"] = {k: (k in s) for k in WANT[stage]}
print(json.dumps(out))
