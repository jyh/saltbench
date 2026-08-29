#!/usr/bin/env python3
"""draw.py — the frozen draw order over CLEVER's 161 problems: sort by sha256(problem_id + SEED), print the first k.
usage: draw.py <k>   (k=161 prints the whole order)"""
import hashlib, sys
SEED = "saltbench-s2lean-stage0-2026-08-29"
ids = ["problem_%d" % i for i in range(161)]
ids.sort(key=lambda i: hashlib.sha256((i + SEED).encode()).hexdigest())
print(" ".join(ids[:int(sys.argv[1])]))
