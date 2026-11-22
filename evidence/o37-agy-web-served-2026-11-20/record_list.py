#!/usr/bin/env python3
"""record_list.py — the agy CELLS OF RECORD, derived from the tracked record files at a git ref (never typed).

Sources (each: block label, path, cell-id column, root column or None, model column, arm column, filter):
  MATRIX  harness/systems-v3/CELLMAP-descriptive-tables-v2-2026-09-27.tsv  rows whose model starts 'gemini'
  NA      harness/systems-v3/RESULT-gemini-blockNA-2026-09-28-cells.tsv
  ZF      evidence/zf-result/zf-cells.tsv
  WA      evidence/blockWA-2026-11-14/cells.tsv
  WA-pro  evidence/blockWA-pro-2026-11-15/cells.tsv
  TA      evidence/blockTA-result-2026-11-20/cells.tsv
Output TSV: block  cell  root  model  arm  source   ('-' where the file names no root)
A line that does not have the header's column count is skipped and COUNTED (#SKIPPED), never silently dropped.
usage: record_list.py <repo> <ref>
"""
import subprocess, sys

repo, ref = sys.argv[1], sys.argv[2]
SRC = [
    ("MATRIX", "harness/systems-v3/CELLMAP-descriptive-tables-v2-2026-09-27.tsv", "cell", None, "model", "arm",
     lambda r: r["model"].startswith("gemini") and r["status"] == "DONE"),
    ("NA", "harness/systems-v3/RESULT-gemini-blockNA-2026-09-28-cells.tsv", "id", "root", "served", "arm", None),
    ("ZF", "evidence/zf-result/zf-cells.tsv", "cid", None, "model", "arm", None),
    ("WA", "evidence/blockWA-2026-11-14/cells.tsv", "id", "root", "init_model", "arm", None),
    ("WA-pro", "evidence/blockWA-pro-2026-11-15/cells.tsv", "id", "root", "init_model", "arm", None),
    ("TA", "evidence/blockTA-result-2026-11-20/cells.tsv", "id", "root", "init_model", "arm", None),
]
skipped = 0
for block, path, cc, rc, mc, ac, flt in SRC:
    txt = subprocess.run(["git", "-C", repo, "show", f"{ref}:{path}"], capture_output=True, text=True, check=True).stdout
    lines = [l for l in txt.split("\n") if l and not l.startswith("#")]
    hdr_i = next(i for i, l in enumerate(lines) if "\t" in l and cc in l.split("\t"))
    hdr = lines[hdr_i].split("\t")
    n = 0
    for l in lines[hdr_i + 1:]:
        f = l.split("\t")
        if len(f) != len(hdr):
            skipped += 1
            print(f"#SKIPPED\t{block}\t{l[:80]}")
            continue
        r = dict(zip(hdr, f))
        if flt and not flt(r):
            continue
        n += 1
        print("\t".join([block, r[cc], r[rc] if rc else "-", r.get(mc, "-"), r.get(ac, "-"), path]))
    print(f"#BLOCK\t{block}\t{n}\t{path}")
print(f"#SKIPPED_TOTAL\t{skipped}")
