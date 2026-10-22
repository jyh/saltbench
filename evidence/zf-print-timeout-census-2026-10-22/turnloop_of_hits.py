"""For every census.txt root with >= 1 hit, print the turn loop record of each cell, in every phase.

Run on the run box from the home directory, census.txt on stdin's neighbour:
  python3 turnloop_of_hits.py census.txt > turnloop-of-hit-roots.tsv
The population is census.txt's (DISCARDED excluded), never a fresh glob: a root born after the census is not in it.
A phase's ctl/ is <root>/<cell>/ctl/ or, once a spec-change harvest has set phase 1 aside, <root>/_aside/<cell>/phase<N>/ctl/.
Hits are counted from the stderr beside each turn loop file, at the read (a census taken mid-leg can read fewer).
The agy-turnloop-env-* files are skipped. A root with a hit and no turn loop file prints NO-RECORD.
"""
import glob, json, os, re, sys

H = os.path.expanduser('~')
print('\t'.join(['root', 'phase', 'where', 'hits', 'done_reason', 'turns_sent', 'turns_no_output', 'landed', 'wall_s']))
for line in open(sys.argv[1]):
    root, files, hits = line.split()
    if 'DISCARDED' in root or hits == 'hits=0':
        continue
    found = 0
    for ctl in sorted(glob.glob(f'{H}/{root}/*/ctl') + glob.glob(f'{H}/{root}/_aside/*/phase*/ctl')):
        where = 'aside' if '/_aside/' in ctl else 'root'
        for t in sorted(glob.glob(ctl + '/agy-turnloop-*.json')):
            m = re.search(r'agy-turnloop-(\d+)\.json$', t)
            if not m:
                continue
            ph = m.group(1)
            n = sum(open(f, errors='replace').read().count('print timeout') for f in glob.glob(f'{ctl}/agy-stderr-{ph}.txt'))
            j = json.load(open(t))
            found += 1
            print('\t'.join(map(str, [root, ph, where, n, j.get('done_reason'), j.get('turns_sent'), j.get('turns_no_output'),
                                      j.get('landed'), round(j.get('wall_seconds') or 0)])))
    if not found:
        print('\t'.join([root, '-', '-', '-', 'NO-RECORD', '-', '-', '-', '-']))
