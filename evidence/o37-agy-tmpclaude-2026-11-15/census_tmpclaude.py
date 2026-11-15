#!/usr/bin/env python3
# provenance: written by the gemini seat of this project on 2026-11-15 and copied here unchanged except this line and line 3 (a host name). Paths are the run box's.
# run box: per stream, does a '/tmp/claude/' mention sit within 200 chars of 'not permitted' (either side)? tally by arm
import re, os, collections
pop = collections.Counter(); hit = collections.Counter(); rust = collections.Counter(); rows = []
for s in open(os.path.expanduser("~/bench-dry/gemini-streams.lst")).read().split():
    fam = s.split("/")[-4]; cell = s.split("/")[-3]; ph = s.rsplit("stream-", 1)[1][0]
    arm = "plain" if "plain" in fam else ("salt" if "salt" in fam else "other")
    era = "WA" if fam.startswith("cells-wa-") else "pre-WA"
    pop[(era, arm)] += 1
    b = open(s, "rb").read().decode("utf-8", "replace")
    h = any("not permitted" in b[max(0, m.start()-200):m.end()+200].lower() for m in re.finditer(r"/tmp/claude/", b))
    if h:
        hit[(era, arm)] += 1
        r = "rustc" in b and re.search(r"Operation not permitted \(os error \d+\) at path \\\\?\"/tmp/claude/rustc", b) is not None
        rust[(era, arm)] += r
        rows.append("%s\t%s\tphase=%s\t%s\t%s\trustc_tmp=%d" % (fam, cell, ph, era, arm, r))
open(os.path.expanduser("~/bench-dry/gemini-tmpclaude-perm-census-2026-11-15.tsv"), "w").write("\n".join(rows) + "\n")
print("era\tarm\tstreams\tperm-hit\trustc-tmp-abort")
for k in sorted(pop): print("%s\t%s\t%d\t%d\t%d" % (k[0], k[1], pop[k], hit[k], rust[k]))
print("total hit", sum(hit.values()), "of", sum(pop.values()))
