#!/usr/bin/env python3
"""tables.py: prints the README's tables from census.tsv and hits.tsv, so no figure is typed.
usage: python3 -I tables.py            print the tables
       python3 -I tables.py --check    exit 1 unless README.md carries them verbatim
"""
import collections, os, sys

D = os.path.dirname(os.path.abspath(__file__))
FLAGS = ('CTL-NAMED', 'OTHER-RECORD', 'HOME-ENV', 'TILDE', 'NONE-NAMED', 'UNMEASURED')


def tables():
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(D, 'census.tsv')) if not l.startswith('#')]
    out = []
    by = collections.defaultdict(collections.Counter)
    for r in rows:
        block, arm, state = r[0], r[3], r[5]
        for key in ((block, arm), (block, '*'), ('all', '*')):
            by[key]['cells'] += 1
            for f in state.split('+'):
                by[key][f] += 1
    out.append('  %-7s %-10s %6s %10s %13s %9s %6s %11s %11s' % (('block', 'arm', 'cells') + FLAGS))
    order = []
    for r in rows:
        for key in ((r[0], r[3]), (r[0], '*')):
            if key not in order:
                order.append(key)
    for key in sorted(order, key=lambda k: (order.index((k[0], '*')), k[1] == '*', k[1])) + [('all', '*')]:
        c = by[key]
        out.append('  %-7s %-10s %6d %10d %13d %9d %6d %11d %11d' % ((key[0], 'both' if key[1] == '*' else key[1], c['cells'])
                                                             + tuple(c[f] for f in FLAGS)))
    out.append('  (a cell can carry CTL-NAMED and OTHER-RECORD both; HOME-ENV only where OTHER-RECORD is absent; TILDE only where neither is)')
    hits = [l.rstrip('\n').split('\t') for l in open(os.path.join(D, 'hits.tsv')) if not l.startswith('#')]
    k = collections.Counter()
    for h in hits:
        for f in h[2].split('+'):
            k[f] += 1
    out.append('  tool calls listed in hits.tsv: %d (CTL %d · OTHER-RECORD %d · HOME-ENV %d · TILDE %d · PARENT %d)'
               % (len(hits), k['CTL'], k['OTHER-RECORD'], k['HOME-ENV'], k['TILDE'], k['PARENT']))
    return '\n'.join(out)


if __name__ == '__main__':
    t = tables()
    if sys.argv[1:] == ['--check']:
        ok = t in open(os.path.join(D, 'README.md')).read()
        print('README tables %s' % ('MATCH' if ok else 'DIFFER'))
        sys.exit(0 if ok else 1)
    print(t)
