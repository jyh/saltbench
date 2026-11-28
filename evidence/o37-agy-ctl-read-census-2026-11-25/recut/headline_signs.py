#!/usr/bin/env python3
"""headline_signs.py OUTDIR: print OUTDIR/headline-signs.md's content from OUTDIR's NEW tables, cut verbatim: the
correctness P4 counts table (correctness-v3-new.md) and the descriptive T4 sign-count table (descriptive-v2-new.md), each the
first markdown table whose header row is the one named below. Read-only. Added 2026-11-25 (the 08:1x files were cut by hand;
--check OUTDIR exits 1 unless the tracked OUTDIR/headline-signs.md equals what this prints, the control for each arm)."""
import os, sys


def cut(path, header):
    lines = open(path, encoding='utf-8').read().split('\n')
    i = lines.index(header)
    j = i
    while j < len(lines) and lines[j].startswith('|'):
        j += 1
    return lines[i:j]


def render(d):
    p4 = cut(os.path.join(d, 'correctness-v3-new.md'), '| model | treatment | + | = | − | ? | no sign (—) |')
    t4 = cut(os.path.join(d, 'descriptive-v2-new.md'),
             '| model | treatment | k of m ratios > 1 | indeterminate | median of the ratios | bounded among them |')
    return '\n'.join(['## correctness P4 counts (tables_correctness_v3.py NEW)'] + p4 + ['', '## descriptive T4 sign counts (tables_v2.py NEW)'] + t4) + '\n'


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == '--check':
        got = render(a[1]); want = open(os.path.join(a[1], 'headline-signs.md'), encoding='utf-8').read()
        print('headline-signs %s: %s' % (a[1], 'SAME' if got == want else 'DIFFERS')); sys.exit(0 if got == want else 1)
    sys.stdout.write(render(a[0]))
