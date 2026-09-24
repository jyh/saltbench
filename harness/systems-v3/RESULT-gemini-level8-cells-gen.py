"""Build the level-8 per-cell table of record (AMENDMENT-gemini-level8 §M10) from the chain's
harvest receipts. Nothing is typed: every column is read from a file the chain wrote, and a
value that could not be read is UNREAD, never blank and never zero.

Population: the legs of the chain run directories named on the command line. Legs 1-6 of
2026-09-22 are invalid-as-fired (census, the fence section) and are NOT a default input."""
import csv, glob, os, re, sys

RUNS = os.path.expanduser('~/.fleet/executors/gemini.runs')
COLS = ['id', 'leg', 'model', 'problem', 'arm', 'm3record', 'dispatchedP1', 'foldbus', 'payloadsha',
        'p1_end', 'p2_end', 'p1_turns', 'p2_turns', 'p2_wall_s', 'p2_false_done', 'p2_caps',
        'score_status', 'verdict', 'TESTS', 'REGRESSIONS', 'CLAUSE_TESTS', 'declared_after_P1',
        'score_receipt', 'adds_src']

def rows(path):
    return [l.rstrip('\n').split('\t') for l in open(path) if l.strip() and not l.startswith('#')]

def leg_meta(rundir, leg):
    man = os.path.join(rundir, 'l8u-%s.tsv' % leg)
    model = next((re.search(r'— (\S+)', l).group(1) for l in open(man) if l.startswith('# LEG')), 'UNREAD')
    arms = {r[4]: (r[1], r[2]) for r in rows(man)}          # prefix -> (problem, arm)
    return model, arms

def score_rows(leg, date):
    out = {}
    for f in glob.glob(os.path.join(RUNS, 'l8u-%s-%s-score' % (leg, date), '*.score.txt')):
        for l in open(f):
            m = re.match(r'(l8\w+)\s+(\S+)\s+\S+\s+(\S+)\s+(\S+)\s+TESTS (\S+) REGRESSIONS (\S+) CLAUSE_TESTS (\S+)', l)
            if m:
                out[m.group(1)] = dict(score_status=m.group(2), verdict=m.group(4), TESTS=m.group(5),
                                       REGRESSIONS=m.group(6), CLAUSE_TESTS=m.group(7),
                                       score_receipt=os.path.relpath(f, RUNS))
    return out

def main(rundirs):
    w = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
    w.writerow(COLS)
    for rundir in rundirs:
        date = os.path.basename(rundir.rstrip('/')).split('l8u-')[1]
        for h in sorted(glob.glob(os.path.join(rundir, 'harvest-*'))):
            leg = os.path.basename(h)[len('harvest-'):]
            if not os.path.exists(os.path.join(h, 'HARVESTED')):
                continue
            model, arms = leg_meta(rundir, leg)
            # A by-hand re-read supersedes the chain's adds when the chain named cells that never ran
            # (LRU-pro-rr: the chain wrote l8rpsr01..03, the cells are l8rpsra201..03). Its source is a column.
            byhand = sorted(glob.glob(os.path.join(h, 'byhand-adds-*', 'l8-cells.tsv')))
            adds = byhand[-1] if byhand else os.path.join(h, 'l8-cells.tsv')
            src = os.path.relpath(adds, RUNS)
            for m in glob.glob(os.path.join(os.path.dirname(adds), 'man-*.tsv')) if byhand else []:
                arms.update({r[4]: (r[1], r[2]) for r in rows(m)})
            facts = {r[0]: r for r in rows(os.path.join(h, 'cells.tsv'))}
            sc = score_rows(leg, date)
            for r in rows(adds):
                cid = r[0]
                prob, arm = next((v for p, v in sorted(arms.items(), key=lambda kv: -len(kv[0]))
                                  if cid.startswith(p)), ('UNREAD', 'UNREAD'))
                f = ' '.join(facts.get(cid, []))
                g = lambda k: (re.search(r'\b%s=(\S+)' % k, f) or [None, 'UNREAD'])[1]
                s = sc.get(cid, {})
                w.writerow([cid, leg, model, prob, arm] + r[1:9] + [g('wall_s'), g('false_done'), g('caps')] +
                           [s.get(k, 'UNREAD') for k in ('score_status', 'verdict', 'TESTS', 'REGRESSIONS', 'CLAUSE_TESTS')] +
                           [r[11], s.get('score_receipt', 'UNREAD'), src])

if __name__ == '__main__':
    main(sys.argv[1:] or [os.path.join(RUNS, 'l8u-2026-09-23')])
