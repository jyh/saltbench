#!/usr/bin/env python3
"""o90_ids.py — the O90 stage-1 population [F4], DERIVED, never typed: U15 (the first fifteen UNFLAGGED ids of the seeded
draw, registered by amendment 3 and run by amendment 8) plus the NEXT fifteen unflagged ids of the same order.
Uses draw.py's order and flagged.json's flag list unchanged; the only literal here is U15 as REGISTERED, and the tool
refuses if the derivation disagrees with it (the self-check is the point: a changed flag list or seed cannot pass).
  usage: o90_ids.py [--depth]      prints the 30 ids space-separated (draw order); --depth also prints each id's draw depth
  exit 0 ok · 1 the derivation disagrees with the registered U15"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S2 = os.path.dirname(HERE)
sys.path.insert(0, S2); import draw
U15_REGISTERED = [73, 0, 146, 16, 4, 38, 142, 96, 112, 141, 31, 54, 127, 18, 74]   # SCOUT-S2LEAN-STAGE0.md amendment 8, verbatim
F = set(json.load(open(os.path.join(S2, "flagged.json")))["flagged_spec_ids"])
full = [draw.pid(t) for t in draw.draw(len(draw.IDS) - len(draw.EXCLUDED))]
unf = [(d + 1, i) for d, i in enumerate(full) if i not in F]
u15, nxt = unf[:15], unf[15:30]
if [i for _, i in u15] != U15_REGISTERED:
    sys.exit("REFUSE: the derived U15 %s != the registered %s" % ([i for _, i in u15], U15_REGISTERED))
if u15[-1][0] != 27 or nxt[0] != (29, 82):
    sys.exit("REFUSE: U15 must end at depth 27 and the next id must be 82 at depth 29 (design §4); got %s, %s" % (u15[-1], nxt[0]))
if "--depth" in sys.argv:
    for d, i in u15 + nxt: print("%3d %3d %s" % (d, i, "U15" if (d, i) in u15 else "next"))
else:
    print(" ".join(str(i) for _, i in u15 + nxt))
