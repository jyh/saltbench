#!/usr/bin/env python3
"""order.py — REGISTRATION-O60 §Z4: the fire order of the 20 tasks.

  "the 20 tasks in an order ranked by sha256("O60-ZD-order|<export full sha>|<row>"), each task's plain cell then its
   salt-diet cell"

The export is the one §Z1's draw names (population.tsv's header line: export=<x86lean full sha>); <row> is the census row id
in population.tsv's first column. Rank ascending by the full hex digest. The §Z1 index is the row's position in population.tsv.
Run:  python3 order.py population.tsv
"""
import hashlib, re, sys

def main():
    path = sys.argv[1]
    lines = open(path, encoding="utf-8").read().splitlines()
    m = [re.search(r"export=([0-9a-f]{40})\b", l) for l in lines if l.startswith("#")]
    exports = [x.group(1) for x in m if x]
    if len(exports) != 1:
        raise SystemExit(f"REFUSED: population.tsv must name exactly one export=<40-hex> in its header, found {len(exports)}")
    export = exports[0]
    body = [l for l in lines if l.strip() and not l.startswith("#")]
    if body[0].split("\t")[0] != "row":
        raise SystemExit("REFUSED: population.tsv's first non-comment line is not its 'row' header")
    rows = [l.split("\t")[0] for l in body[1:]]
    if len(rows) != 20 or len(set(rows)) != 20:
        raise SystemExit(f"REFUSED: {len(rows)} rows ({len(set(rows))} distinct); §Z1 registers 20")
    ranked = sorted((hashlib.sha256(f"O60-ZD-order|{export}|{r}".encode()).hexdigest(), i + 1, r) for i, r in enumerate(rows))
    print(f"# §Z4 order · export={export} · input {path}")
    print("rank\ttask\trow\tsha256/16")
    for k, (h, i, r) in enumerate(ranked, 1):
        print(f"{k}\t{i}\t{r}\t{h[:16]}")

if __name__ == "__main__":
    main()
