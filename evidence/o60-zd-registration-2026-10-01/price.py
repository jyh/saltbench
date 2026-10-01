#!/usr/bin/env python3
"""O60 / desk ZD: price the first run from the only measured x86 Claude-row cells (O4 #1, CRC-32).

Reads the verbatim tables of the two Claude-row CRC-32 RESULTs (column `final_COST`, per arm) and prints the
first run's band (REGISTRATION §Z7). Nothing here is typed from a message: every figure comes from these files.
Run:  python3 price.py <RESULT-...-claude-none.md> <RESULT-...-claude-statement.md> <cells-per-arm> <cap-usd>
"""
import hashlib
import statistics
import sys


def table(path):
    b = open(path, "rb").read()
    lines = b.decode().splitlines()
    head = next(i for i, l in enumerate(lines) if l.startswith("id\tarm\tn\t"))
    cols = lines[head].split("\t")
    rows = []
    for l in lines[head + 1:]:
        if not l.strip() or "\t" not in l:
            break
        rows.append(dict(zip(cols, l.split("\t"))))
    return hashlib.sha256(b).hexdigest()[:16], rows


def main():
    paths, per_arm, cap = sys.argv[1:3], int(sys.argv[3]), float(sys.argv[4])
    cost = {"plain": [], "salt-diet": []}
    for p in paths:
        h, rows = table(p)
        print(f"# {p.rsplit('/', 1)[-1]} sha256/16={h} rows={len(rows)}")
        for r in rows:
            cost[r["arm"]].append(float(r["final_COST"]))
    for arm, xs in cost.items():
        print(f"# {arm}: n={len(xs)} min={min(xs):.4f} median={statistics.median(xs):.4f} max={max(xs):.4f}")
    lo = per_arm * (min(cost["plain"]) + min(cost["salt-diet"]))
    mid = per_arm * (statistics.median(cost["plain"]) + statistics.median(cost["salt-diet"]))
    over = max(0.0, max(x - cap for xs in cost.values() for x in xs))
    hi = 2 * per_arm * (cap + over)
    print(f"cells\t{2 * per_arm}")
    print(f"low_usd\t{lo:.2f}\t= {per_arm} x (min plain + min salt-diet)")
    print(f"central_usd\t{mid:.2f}\t= {per_arm} x (median plain + median salt-diet)")
    print(f"ceiling_usd\t{hi:.2f}\t= {2 * per_arm} cells x (cap {cap} + largest observed overrun {over:.4f})")


if __name__ == "__main__":
    main()
