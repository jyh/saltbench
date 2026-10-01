#!/usr/bin/env python3
"""O60 / desk ZD: derive the registered population from paris's census, by rule.

Inputs (both named by hash in the output, never typed into it):
  1. x86lean docs/PRIMITIVE-CENSUS.md at the export (read with `git show <sha>:docs/PRIMITIVE-CENSUS.md`)
  2. s2n-bignum include/s2n-bignum.h at the census's own s2n-bignum commit (the source of the strata)

The rule (registered in REGISTRATION-O60-scalar-population-2026-10-01.md §Z1, before this script was run):
  R1  the eligible rows are the census rows whose verdict cell begins **ALL COVERED**
  R2  exclude the two rows whose function is CRC-32 (crc32-poc, zlib-crc32): CRC-32 is O4 #1's proof of
      concept, whose cards, statement and results are already on record
  R3  every remaining row that is NOT s2n-bignum is in the population
  R4  the s2n rows fill the population to 20, split over three strata by the header's prototype:
        RETURN       no writable pointer parameter (the result is the return value)
        WRITE-FIXED  a writable `z[S2N_BIGNUM_STATIC n]` parameter (a fixed-size output)
        WRITE-VAR    any other writable pointer (a caller-sized output)
      each stratum's quota by largest-remainder allocation, proportional to its size
  R5  within a stratum, rows are ranked by sha256(SEED + "|" + row_id) and the first `quota` are taken,
      SEED = "O60-ZD|x86lean|" + the export's full sha
Run:  python3 draw.py <census.md> <s2n-bignum.h> <export-full-sha>
"""
import hashlib
import re
import sys

TOTAL = 20
CRC32_ROWS = {"crc32-poc", "zlib-crc32"}


def sha16(b):
    return hashlib.sha256(b).hexdigest()[:16]


def covered_rows(census):
    rows = []
    for line in census.splitlines():
        if not line.startswith("| `"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rid = cells[0].strip("`")
        if cells[-1].startswith("**ALL COVERED**"):
            rows.append((rid, cells[1], cells[2], cells[3]))
    return rows


def stratum(header, fn):
    m = re.search(r"^extern [a-z0-9_ ]+ " + re.escape(fn) + r" ?\((.*)\);$", header, re.M)
    if not m:
        raise SystemExit(f"REFUSED: no prototype for {fn} in the header")
    params = [p.strip() for p in m.group(1).split(",")]
    writable = [p for p in params if not p.startswith("const") and ("*" in p or "[" in p)]
    if not writable:
        return "RETURN"
    if any("S2N_BIGNUM_STATIC" in p for p in writable):
        return "WRITE-FIXED"
    return "WRITE-VAR"


def main():
    census_path, header_path, export = sys.argv[1:4]
    if not re.fullmatch(r"[0-9a-f]{40}", export):
        raise SystemExit("REFUSED: the export must be a full 40-hex sha")
    cb = open(census_path, "rb").read()
    hb = open(header_path, "rb").read()
    census, header = cb.decode(), hb.decode()
    m = re.search(r"## The verdict: (\d+) of (\d+) candidates are ALL COVERED", census)
    rows = covered_rows(census)
    print(f"# census sha256/16={sha16(cb)} bytes={len(cb)} · header sha256/16={sha16(hb)} bytes={len(hb)} · export={export}")
    print(f"# census heading: {m.group(1)} of {m.group(2)} · rows parsed ALL COVERED: {len(rows)}")
    if int(m.group(1)) != len(rows):
        raise SystemExit("REFUSED: the parsed ALL COVERED count disagrees with the census heading")
    eligible = [r for r in rows if r[0] not in CRC32_ROWS]
    non_s2n = [r for r in eligible if r[2] != "s2n"]
    s2n = [r for r in eligible if r[2] == "s2n"]
    print(f"# excluded (R2): {sorted(r[0] for r in rows if r[0] in CRC32_ROWS)} · non-s2n (R3): {len(non_s2n)} · s2n eligible: {len(s2n)}")
    need = TOTAL - len(non_s2n)
    strata = {}
    for r in s2n:
        fn = r[0][len("s2n-"):]
        strata.setdefault(stratum(header, fn), []).append(r)
    names = sorted(strata)
    exact = {k: need * len(strata[k]) / len(s2n) for k in names}
    quota = {k: int(exact[k]) for k in names}
    for k in sorted(names, key=lambda k: (-(exact[k] - quota[k]), k))[: need - sum(quota.values())]:
        quota[k] += 1
    for k in names:
        print(f"# stratum {k}: size {len(strata[k])} · exact {exact[k]:.3f} · quota {quota[k]}")
    seed = "O60-ZD|x86lean|" + export
    print(f"# seed: {seed}")
    picked = []
    for k in names:
        ranked = sorted(strata[k], key=lambda r: hashlib.sha256((seed + "|" + r[0]).encode()).hexdigest())
        print(f"# rank {k}: " + " ".join(r[0] for r in ranked))
        picked += [(r, k) for r in ranked[: quota[k]]]
    print("row\tfamily\treference\tinstrs\tstratum")
    for r in non_s2n:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t-")
    for r, k in picked:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{k}")
    n = len(non_s2n) + len(picked)
    print(f"# population: {n}")
    if n != TOTAL:
        raise SystemExit("REFUSED: population is not 20")


if __name__ == "__main__":
    main()
