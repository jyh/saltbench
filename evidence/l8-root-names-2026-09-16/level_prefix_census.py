#!/usr/bin/env python3
"""level_prefix_census.py <home> -- read-only: the level prefixes of the cell roots directly under <home>, i.e. every
directory named cells-l<digits><letters>-..., counted by the prefix up to and including its first '-' after the level.
Only prefixes and counts are printed, never whole root names. REFUSES when <home> holds no cells-* root at all, so a
run on a box the cells never ran on cannot print an empty census that reads as "no such prefix"."""
import collections, os, re, sys
home = sys.argv[1]
roots = [d for d in os.listdir(home) if d.startswith("cells-") and os.path.isdir(os.path.join(home, d))]
if not roots: sys.exit("REFUSE: no cells-* root under %s -- this is not the box the cells ran on" % home)
c = collections.Counter(m.group(1) for d in roots for m in [re.match(r"(cells-l[0-9]+[a-z]*-)", d)] if m)
print("cells-* roots: %d" % len(roots))
print("roots with a level prefix: %d" % sum(c.values()))
for k in sorted(c): print("%s\t%d" % (k, c[k]))
