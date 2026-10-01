#!/usr/bin/env python3
"""Desk ZI (bench, 2026-10-01): the level-8 cells the census's 2026-09-23 fence ruling made INVALID AS FIRED, each with its
verdict AS SCORED, or UNREAD. Nothing is typed: the population is hidden_root_census.out's HIDDEN wave cells, and each verdict
is the cell's own row in a score file the run wrote.
Run:  python3 invalid_cells_verdicts.py <hidden_root_census.out> <runs dir> > invalid_cells_verdicts.tsv
Score-file choice, per cell: every `*-2026-09-2[12]-score*` / `*-rescore-e8c0d05` file under <runs dir> that holds the cell's
row; the declared scorer of record (e8c0d0512ab2, AMENDMENT-gemini-level8 §A8.10.3) is preferred when present. The scorer sha
is printed beside every verdict, read from the file's line 1. Paths are printed relative to <runs dir>.
A SELF-NOT row (the scorer's note that the subject's own LANDING.md declares requirements NOT met) is never read as the verdict.
"""
import glob, os, re, sys

census, runs = sys.argv[1], sys.argv[2]
cells = []
for line in open(census):
    f = line.rstrip('\n').split('\t')
    if len(f) == 3 and f[2] == 'HIDDEN' and not f[0].startswith('cells-l8u-dryrender'):
        cells.append((f[0], f[1]))
files = sorted(glob.glob(os.path.join(runs, 'l8u-*-2026-09-2[12]-score', '*.score.txt'))
               + glob.glob(os.path.join(runs, 'l8u-*-2026-09-2[12]-rescore-e8c0d05', '*.score.txt')))
rows = {}
for p in files:
    lines = open(p, errors='replace').read().splitlines()
    m = re.search(r'\(([0-9a-f]{12})\)', lines[0] if lines else '')
    sha = m.group(1) if m else 'UNREAD'
    for l in lines:
        t = l.split()
        if t and re.fullmatch(r'l8[a-z0-9]+', t[0]):
            rows.setdefault(t[0], []).append((sha, os.path.relpath(p, runs), l))
print('# population: %d HIDDEN wave cells (dry renders excluded) · score files read: %d' % (len(cells), len(files)))
print('root\tcell\tverdict\tend\ttests\tscorer\tscore_file\tnote')
unread = 0
for root, cell in cells:
    allrows = rows.get(cell, [])
    selfnote = [x for x in allrows if len(x[2].split()) > 4 and x[2].split()[4] == 'SELF-NOT']
    c = [x for x in allrows if x not in selfnote]          # a SELF-NOT row is the scorer's self-grade note, never the verdict
    pick = [x for x in c if x[0] == 'e8c0d0512ab2'] or c
    if not pick:
        unread += 1
        print('%s\t%s\tUNREAD\t-\t-\t-\t-\tno score file under the runs dir holds this cell\'s row' % (root, cell))
        continue
    sha, rel, l = pick[-1]
    t = l.split()
    verdict, end = (t[4], t[3]) if len(t) > 4 else ('UNREAD', '-')
    tests = ' '.join(t[5:]) if len(t) > 5 else '-'
    notes = []
    if len(c) > 1:
        notes.append('%d verdict rows in %d file(s); the scorer of record e8c0d0512ab2 is used' % (len(c), len({x[1] for x in c})))
    if selfnote:
        notes.append('the file also carries a SELF-NOT row (the subject\'s own LANDING.md says NOT); printed apart, never as the verdict')
    note = ' · '.join(notes) or '-'
    print('\t'.join([root, cell, verdict, end, tests, sha, rel, note]))
print('# UNREAD: %d of %d' % (unread, len(cells)))
