#!/usr/bin/env python3
"""change-1.md == customer preamble + blank + the card's '## Change request (phase 2)' section, with each bullet's indented continuation
lines joined to it by one space (the clause render's only transform), surrounding blank lines dropped. Written apart from customer.sh /
render_requirements.py. rc 0 equal, rc 1 differ (prints the first differing line)."""
import sys
card, ch = open(sys.argv[1]).read().split("\n"), open(sys.argv[2]).read().split("\n")
sec, f = [], 0
for l in card:
    if l.startswith("## Change request (phase 2)"): f = 1; continue
    if l.startswith("## "): f = 0
    if f: sec.append(l)
out = []
for l in sec:
    if l.startswith("  ") and l.strip() and out and out[-1].startswith("- "): out[-1] += " " + l.strip()
    else: out.append(l)
while out and not out[0].strip(): out.pop(0)
while out and not out[-1].strip(): out.pop()
body = ch[2:]
while body and not body[-1].strip(): body.pop()
pre_ok = ch[0].startswith("The interface has been changed only as the request below says") and ch[1] == ""
if out == body and pre_ok: print("EQUAL: preamble + card section (%d lines, bullets unwrapped)" % len(out)); sys.exit(0)
for i, (a, b) in enumerate(zip(out, body)):
    if a != b: print("DIFFER at line %d:\n card: %s\n file: %s" % (i, a[:120], b[:120])); break
else: print("DIFFER: lengths %d vs %d, preamble ok %s" % (len(out), len(body), pre_ok))
sys.exit(1)
