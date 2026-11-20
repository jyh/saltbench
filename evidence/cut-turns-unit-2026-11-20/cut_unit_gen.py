#!/usr/bin/env python3
"""The cut-turns UNIT correction (bench row 11): every figure the corrections quote, derived from tracked files. Nothing is typed.

Inputs (this directory; the run-box scripts that wrote them are beside them, read-only, run 2026-11-20):
  pt_shapes.tsv   pt_shapes.sh over every ~/cells-*/*/ctl/agy-*stderr-*.txt on the run box that carries 'print timeout':
                  mtime-day, path, LINES 'print timeout', LINES '^[agy] print timeout', LINES '^error: print timeout',
                  LINES '^AGY_ERROR' carrying 'print_timeout', client stamp
  ../blockWA-pro-2026-11-15/cell_facts.json, ../blockWA-2026-11-14/cell_facts.json, ../blockNA-2026-09-28/cell_facts.json
                  the cell facts each RESULT was generated from (cut_turns / cut_turns_all count LINES, by their own code)

THE UNIT. One client print-timeout EVENT writes ONE line `[agy] print timeout ...` in every era on the box. The November client (agy 1.5.x,
blocks WA and TA) also writes `error: print timeout ...` and an `AGY_ERROR {... "reason":"print_timeout"}` line, so a count of lines that
CONTAIN 'print timeout' is 3 per event there and 1 per event before. EVENTS here = the `^[agy] print timeout` lines; in a 3-line file the
AGY_ERROR count must equal it, or the file is reported MIXED and this tool exits 1.

  python3 cut_unit_gen.py --eras       the shape census by month (1-line / 3-line / MIXED)
  python3 cut_unit_gen.py --control    LINES in pt_shapes.tsv per cell == the cell facts' line counts (NA cut_turns, WA cut_turns_all), every cell
  python3 cut_unit_gen.py --summary    the corrected WA lines (cut turns in EVENTS) and the per-cell list
  python3 cut_unit_gen.py --check F    rc 0 iff every --summary line occurs verbatim in F
"""
import collections, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.dirname(HERE)


def shapes():
    rows = []
    for l in open(os.path.join(HERE, 'pt_shapes.tsv')):
        day, path, lines, agy, err, aj, client = l.rstrip('\n').split('\t')
        lines, agy, err, aj = int(lines), int(agy), int(err), int(aj)
        if err == 0 and aj == 0 and agy == lines:
            shape = '1-line'
        elif agy == err == aj and lines == 3 * agy:
            shape = '3-line'
        else:
            shape = 'MIXED'
        cell = path.split('/')[1]
        rows.append(dict(day=day, path=path, root=path.split('/')[0], cell=cell, file=path.split('/')[-1], lines=lines, events=agy, shape=shape))
    return rows


def facts(rel):
    return json.load(open(os.path.join(EV, rel)))


def per_cell(rows, files):
    agg = collections.defaultdict(lambda: [0, 0])
    for r in rows:
        if r['file'] in files:
            a = agg[(r['root'], r['cell'])]
            a[0] += r['lines']; a[1] += r['events']
    return agg


def eras(rows):
    c = collections.Counter((r['day'][:7], r['shape']) for r in rows)
    return ['%s %s %d files' % (m, s, n) for (m, s), n in sorted(c.items())]


def control():
    rows = shapes(); out = []; bad = 0
    for rel, field, files in (('blockNA-2026-09-28/cell_facts.json', 'cut_turns', ('agy-stderr-1.txt',)),
                              ('blockWA-2026-11-14/cell_facts.json', 'cut_turns_all', ('agy-stderr-1.txt', 'agy-turnloop-stderr-1.txt')),
                              ('blockWA-pro-2026-11-15/cell_facts.json', 'cut_turns_all', ('agy-stderr-1.txt', 'agy-turnloop-stderr-1.txt'))):
        agg = per_cell(rows, files); n = 0
        for f in facts(rel):
            mine = agg.get((f['root'], f['id']), [0, 0])[0]
            if mine != f[field]:
                bad += 1; out.append('MISMATCH %s %s facts=%s box=%s' % (rel, f['id'], f[field], mine))
            n += 1
        out.append('control %s: %d cells, %s == box LINES in %d' % (rel.split('/')[0], n, field, n - sum(1 for o in out if o.startswith('MISMATCH ' + rel))))
    return out, bad


def summary():
    rows = shapes()
    agg = per_cell(rows, ('agy-stderr-1.txt', 'agy-turnloop-stderr-1.txt'))
    L = []
    for rel, model in (('blockWA-2026-11-14/cell_facts.json', 'Flash'), ('blockWA-pro-2026-11-15/cell_facts.json', 'argon')):
        fs = facts(rel); groups = collections.OrderedDict()
        for f in fs:
            groups.setdefault((f['problem'], f['arm']), []).append(f)
        for (p, a), rs in groups.items():
            lines = sum(f['cut_turns_all'] for f in rs)
            ev = sum(agg.get((f['root'], f['id']), [0, 0])[1] for f in rs)
            sent = sum(f['turns_sent'] for f in rs)
            L.append('WA %s %s %s: cut turns %d of %d sent (EVENTS); the RESULT printed %d (print-timeout LINES)' % (model, p, a, ev, sent, lines))
        cut = ['%s=%d/%d' % (f['id'], agg.get((f['root'], f['id']), [0, 0])[1], f['cut_turns_all']) for f in fs if f['cut_turns_all']]
        L.append('WA %s cells cut (events/lines): %s' % (model, ' '.join(cut) if cut else 'none'))
    return L


if __name__ == '__main__':
    a = sys.argv[1:] or ['--summary']
    if a[0] == '--eras':
        print('\n'.join(eras(shapes())))
        sys.exit(1 if any(r['shape'] == 'MIXED' for r in shapes()) else 0)
    if a[0] == '--control':
        o, bad = control(); print('\n'.join(o)); sys.exit(1 if bad else 0)
    if a[0] == '--summary':
        print('\n'.join(summary())); sys.exit(0)
    if a[0] == '--check' and len(a) > 1:
        flat = ' '.join(open(a[1]).read().split())
        miss = [l for l in summary() if ' '.join(l.split()) not in flat]
        for m in miss:
            print('MISSING ' + m)
        print('check: %d of %d summary lines present' % (len(summary()) - len(miss), len(summary())))
        sys.exit(1 if miss else 0)
    sys.exit(__doc__)
