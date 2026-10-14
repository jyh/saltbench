#!/usr/bin/env python3
"""O60 §R4 SETTING-EDITED census over the 40 archived cells' ctl/ (read-only).
usage: r4_quarantine_census.py <root holding cells-clb-x86p-o60-{plain,saltdiet}>
Per cell: SETTING-EDITED lines in ctl/watch.log, quarantine dirs, files under them,
non-empty files, and quarantine dirs holding no file at all."""
import os, re, sys
root = sys.argv[1]
print("cell\tevents\tquarantines\tfiles\tnonempty_files\tempty_quarantine_dirs")
T = [0]*5
for arm in ("plain", "saltdiet"):
    base = os.path.join(root, f"cells-clb-x86p-o60-{arm}")
    for cell in sorted(os.listdir(base)):
        ctl = os.path.join(base, cell, "ctl")
        ev = sum(1 for l in open(os.path.join(ctl, "watch.log"), errors="replace") if " SETTING-EDITED " in l)
        q = os.path.join(ctl, "quarantine")
        qs = sorted(os.listdir(q)) if os.path.isdir(q) else []
        files = nonempty = emptyq = 0
        for d in qs:
            n = 0
            for dp, dn, fn in os.walk(os.path.join(q, d)):
                for f in fn:
                    n += 1
                    if os.path.getsize(os.path.join(dp, f)) > 0: nonempty += 1
            files += n
            if n == 0: emptyq += 1
        row = [ev, len(qs), files, nonempty, emptyq]
        T = [a+b for a, b in zip(T, row)]
        print(cell + "\t" + "\t".join(map(str, row)))
print("TOTAL\t" + "\t".join(map(str, T)))
