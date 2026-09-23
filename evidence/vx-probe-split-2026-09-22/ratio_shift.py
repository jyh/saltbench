#!/usr/bin/env python3
"""ratio_shift.py [probe-split.tsv] [--selftest]

For each Claude-lane block, the median COST ratio (salt-diet : plain) read two ways from ONE table:
PROBE-IN (cell + the harness's own sandbox probe, which is what `final_COST` in the published block
tables is) and PROBE-APART (the cell alone). The census states this ratio as
median(salt-diet final_COST) / median(plain final_COST) over a block's cells; this does the same.

Why it exists (desk VX): the probe's cost is near-constant while a cell's is not, so it is a larger
share of the cheaper arm. A constant offset is neutral in a difference and biasing in a ratio, and
here it pulls every Sonnet-block ratio DOWN, i.e. toward the treatment arm.

LIMITS, printed beside the verdict as well: the table covers the 180 cells metered on 2026-09-22 and
may differ from the population a given census line was computed on (the script prints the n it used).
It says nothing about correctness, only cost.

rc 0 printed · 1 a row did not parse · 2 usage."""
import sys, os, statistics as S, collections as C

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path):
    g = C.defaultdict(lambda: C.defaultdict(list))
    for n, line in enumerate(open(path), 1):
        p = line.rstrip('\n').split('\t')
        if p[0] == 'kind':
            continue
        if p[0] != 'ROW' or len(p) != 7:
            sys.exit(f"REFUSE line {n}: not a 7-field ROW: {line[:80]!r}")
        root = p[2]
        if root.endswith('-plain'):
            arm = 'plain'
        elif root.endswith('-saltdiet'):
            arm = 'saltdiet'
        else:
            sys.exit(f"REFUSE line {n}: root names no arm: {root}")
        block = root.split('-')[2]
        cell, probe = float(p[4]), float(p[6])
        g[block][arm].append((cell + probe, cell))
    return g


def ratios(g):
    out = []
    for b in sorted(g):
        a = g[b]
        if not a['plain'] or not a['saltdiet']:
            continue
        rin = S.median(x[0] for x in a['saltdiet']) / S.median(x[0] for x in a['plain'])
        rap = S.median(x[1] for x in a['saltdiet']) / S.median(x[1] for x in a['plain'])
        out.append((b, len(a['plain']), len(a['saltdiet']), rin, rap))
    return out


def selftest():
    import tempfile
    rows = ["kind\tslug\tcells_root\tcell_T\tcell_COST\tprobe_T\tprobe_COST",
            "ROW\tx1\tcells-clb-zz-lru-plain\t1\t1.0\t1\t0.1",
            "ROW\tx2\tcells-clb-zz-lru-saltdiet\t1\t10.0\t1\t0.1"]
    with tempfile.NamedTemporaryFile('w', suffix='.tsv', delete=False) as f:
        f.write('\n'.join(rows) + '\n')
    (b, _, _, rin, rap), = ratios(load(f.name))
    ok = abs(rin - 10.1 / 1.1) < 1e-9 and abs(rap - 10.0) < 1e-9
    # mutant: a constant probe must NOT move the apart ratio, and MUST move the in ratio
    print("selftest", "PASS" if ok and rin < rap else "FAIL", f"in={rin:.4f} apart={rap:.4f}")
    os.unlink(f.name)
    return 0 if ok and rin < rap else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'probe-split.tsv')
    print("block  n_plain n_saltdiet  PROBE-IN  PROBE-APART  shift")
    for b, np_, ns, rin, rap in ratios(load(path)):
        print(f"{b:5}  {np_:7} {ns:10}  {rin:7.2f}x  {rap:10.2f}x  {100*(rap/rin-1):+5.1f}%")
    print("LIMIT: population = this table's cells; a census line computed on another n may differ.")
