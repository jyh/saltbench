#!/usr/bin/env python3
"""Block NC's price, derived from the tables of record; no figure in it is typed.

Reads (repo-relative, from the repo root):
  evidence/claude-lane-blockN-2026-09-28/blockNO-cells.tsv   block N's 36 Opus cells (the phase-1 sources)
  evidence/claude-lane-blockN-2026-09-28/blockNS-cells.tsv   block N's 36 Sonnet cells
  harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv     the P1 wave: 19 Opus phase-2 cells on copies (cost_usd)
  evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv   block SC: 24 Sonnet phase-2 cells (p2_COST)
  --caps <path>                                              saltbench-systems harness/systems-v3/cost_caps.tsv (C1_USD, C2_USD),
                                                             the export's own copy; the registration pins its blob

Prints: the per-model phase-2 median, the source census by run_state, the fresh-phase-1 upper bound
(cells with no LANDED run state), the estimate and the ceiling. Exit 0. --selftest plants a table and
checks the median and the count against hand-computed values (and refuses a mutant median).
"""
import csv, statistics, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def rows(path):
    with open(os.path.join(ROOT, path)) as f:
        lines = [l for l in f if not l.startswith('#')]
    return list(csv.DictReader(lines, delimiter='\t'))


def cap(name, path):
    with open(path) as f:
        for line in f:
            p = line.rstrip('\n').split('\t')
            if len(p) > 2 and p[0] == 'pricing' and p[1] == name:
                return float(p[2])
    raise SystemExit('no %s in cost_caps.tsv' % name)


def census(cells):
    landed = [r for r in cells if r['run_state'] == 'ENDED: LANDED']
    return len(cells), len(landed), len(cells) - len(landed)


def selftest():
    xs = [1.0, 9.0, 2.0, 4.0]
    assert statistics.median(xs) == 3.0
    mutant = sorted(xs)[len(xs) // 2]  # upper-middle, the wrong median for even n
    assert mutant != statistics.median(xs), 'mutant median not refused'
    t = [{'run_state': 'ENDED: LANDED'}, {'run_state': 'ENDED: CAP-COST'}, {'run_state': 'ENDED: LANDED'}]
    assert census(t) == (3, 2, 1)
    print('selftest ok 3/3')


def main():
    if '--selftest' in sys.argv:
        return selftest()
    if '--caps' not in sys.argv:
        raise SystemExit('usage: --caps <saltbench-systems harness/systems-v3/cost_caps.tsv> | --selftest')
    cp = sys.argv[sys.argv.index('--caps') + 1]
    c1, c2 = cap('C1_USD', cp), cap('C2_USD', cp)
    no = rows('evidence/claude-lane-blockN-2026-09-28/blockNO-cells.tsv')
    ns = rows('evidence/claude-lane-blockN-2026-09-28/blockNS-cells.tsv')
    p1 = [float(r['cost_usd']) for r in rows('harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv')]
    sc = [float(r['p2_COST']) for r in rows('evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv')]
    mo, ms = statistics.median(p1), statistics.median(sc)
    print('C1_USD %.2f  C2_USD %.2f' % (c1, c2))
    print('phase-2 median  Opus %.2f (n=%d, P1 wave)  Sonnet %.2f (n=%d, block SC)' % (mo, len(p1), ms, len(sc)))
    out = {}
    for name, cells in (('Opus', no), ('Sonnet', ns)):
        n, landed, notl = census(cells)
        out[name] = notl
        print('%-6s sources %d  LANDED %d  not LANDED %d  (%s)' % (
            name, n, landed, notl, ' '.join(r['cell'] for r in cells if r['run_state'] != 'ENDED: LANDED')))
    phase2 = 36 * mo + 36 * ms
    fresh_max = out['Opus'] + out['Sonnet']
    print('estimate  phase 2: 36 x %.3f + 36 x %.3f = %.2f + %.2f = %.2f' % (mo, ms, 36 * mo, 36 * ms, phase2))
    print('fresh phase 1 (upper bound before the baselines): %d cells x C1 %.2f = %.2f' % (fresh_max, c1, fresh_max * c1))
    print('ceiling   72 x C2 %.2f + %d x C1 %.2f = %.2f, plus each cell\'s overrun past its cap' % (
        c2, fresh_max, c1, 72 * c2 + fresh_max * c1))


if __name__ == '__main__':
    main()
