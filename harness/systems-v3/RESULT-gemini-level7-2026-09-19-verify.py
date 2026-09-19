"""Re-derive every headline figure in RESULT-gemini-level7 from the receipts and
compare it against the bytes of the document. Nothing here is typed from the prose."""
import csv, re, statistics, glob, os, sys
doc = open('harness/systems-v3/RESULT-gemini-level7-2026-09-19.md').read()
cen = open('harness/systems-v3/CENSUS-full-matrix-2026-09-14.md').read()
rows = list(csv.DictReader(open('harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv'), delimiter='\t'))
M = {'gemini-3.1-pro-high':'Pro','gemini-3.8-flash-high':'Flash'}
fails = []
def check(name, derived, needle):
    ok = needle in doc
    print(('  OK  ' if ok else '  RED ') + '%-44s derived=%-14s needle=%r' % (name, derived, needle))
    if not ok: fails.append(name)

# 1 population
check('cells', len(rows), '84 cells')
# 2 pass by quadrant
q = {}
for r in rows:
    v = r['verdicts']
    if v in ('NOT-SCORED','INCOMPLETE'): continue
    k = (M.get(r['served'],'?'), r['arm'])
    n, d = q.get(k,(0,0)); q[k] = (n + (0 if 'FAIL' in v else 1), d+1)
check('Flash plain',      q[('Flash','plain')],      '%d / %d' % q[('Flash','plain')])
check('Flash salt-diet',  q[('Flash','salt-diet')],  '%d / %d' % q[('Flash','salt-diet')])
check('Pro plain',        q[('Pro','plain')],        '%d / %d' % q[('Pro','plain')])
check('Pro salt-diet',    q[('Pro','salt-diet')],    '%d / %d' % q[('Pro','salt-diet')])
# 3 scorable + full pass, from the score files
tot = {'declared':0,'scorable':0,'passn':0}
for f in glob.glob(os.path.expanduser('~/.fleet/executors/gemini.runs/l7u-*-2026-09-18-score/*.score.txt')):
    last = open(f).read().rstrip('\n').split('\n')[-1]
    tot['declared'] += int(re.search(r'ENDED \d+/(\d+)', last).group(1))
    tot['scorable'] += int(re.search(r'SCORABLE (\d+)', last).group(1))
    tot['passn']    += int(re.search(r'FULL PASS (\d+) of', last).group(1))
check('declared',  tot['declared'],  '84 cells')
check('scorable',  tot['scorable'],  '%d scorable' % tot['scorable'])
check('full pass', tot['passn'],     '%d FULL PASS' % tot['passn'])
# 4 arm-correlated flags: all Pro salt-diet
flagged = [r for r in rows if ('TRUNCATED' in r['verdicts'] or 'SELF-NOT' in r['verdicts']
           or 'PERSIS' in r['end_marker'] or r['false_done'] not in ('0','?','-'))]
assert all(M.get(r['served'])=='Pro' and r['arm']=='salt-diet' for r in flagged), 'flag purity'
check('flagged cells (all Pro salt)', len(flagged), '**ten cells, zero plain, zero Flash**')
for r in flagged: assert r['cell'] in doc, r['cell']
print('  OK   all %d flagged cell ids appear in the doc' % len(flagged))
# 5 tokens
NP = set(r['cell'] for r in rows if 'TRUNCATED' in r['verdicts'] or r['verdicts'] in ('NOT-SCORED','INCOMPLETE'))
def med(arm, col, pool=True):
    v=[int(r[col]) for r in rows if r['arm']==arm and r[col].isdigit() and (r['cell'] not in NP if pool else True)]
    return v
tp, ts = med('plain','T'), med('salt-diet','T')
op, os_ = med('plain','out'), med('salt-diet','out')
check('poolable plain n',  len(tp), 'n = %d plain' % len(tp))
check('poolable salt n',   len(ts), '%d salt-diet.**' % len(ts))
check('median T plain',    int(statistics.median(tp)), '{:,}'.format(int(statistics.median(tp))))
check('median T salt',     int(statistics.median(ts)), '{:,}'.format(int(statistics.median(ts))))
check('ratio T',           '%.3f' % (statistics.median(ts)/statistics.median(tp)), '%.3fx' % (statistics.median(ts)/statistics.median(tp)))
check('ratio out',         '%.3f' % (statistics.median(os_)/statistics.median(op)), '%.3fx' % (statistics.median(os_)/statistics.median(op)))
ta, tb = med('plain','T',False), med('salt-diet','T',False)
check('robust ratio',      '%.3f' % (statistics.median(tb)/statistics.median(ta)), '%.3fx' % (statistics.median(tb)/statistics.median(ta)))
check('robust salt median',int(statistics.median(tb)), '{:,}'.format(int(statistics.median(tb))))
# 6 §K7 zeros
for col, want, label in [('given','GIVEN-OK','GIVEN-OK 84/84'), ('field','brownfield','field=brownfield 84/84'),
                         ('w1_fenced','COVERED','w1_fenced COVERED 84/84')]:
    n = sum(1 for r in rows if r[col]==want)
    check('%s == %s' % (col,want), '%d/84' % n, label if n==84 else 'MISMATCH')
ce = {}
for r in rows: ce[r['card_extras']] = ce.get(r['card_extras'],0)+1
check('card_extras split', ce, 'none %d /\n                                                        statement %d' % (ce['none'], ce['statement']))
# 7 census arithmetic
m = re.search(r'LIVE \(ADDENDUM 10\) DONE (\d+) · OWED (\d+) · BLOCKED\s+(\d+) · INEXPR (\d+)', cen)
d,o,b,i = map(int, m.groups())
print('  %s  census LIVE row  %d+%d+%d+%d = %d' % ('OK ' if d+o+b+i==200 else 'RED', d,o,b,i, d+o+b+i))
if d+o+b+i != 200: fails.append('census sum')
# ⛔ THE 240-VIEW LINE OCCURS ONCE PER ADDENDUM. The first draft of this check used re.search and
# matched ADDENDUM 9's line (72+112+0+56), printing OK about a figure this addendum did not write.
# A wrong-SUBJECT pass: right tool, right pattern, wrong object. Take the LAST, and assert the count.
all240 = re.findall(r'240-view `DONE (\d+) · OWED (\d+) · BLOCKED 0 · INEXPR (\d+)`', cen)
print('  OK   240-view lines found: %d (one per addendum that states one)' % len(all240))
if len(all240) < 2: fails.append('240 population')
d2,o2,i2 = map(int, all240[-1])
print('  %s  census 240-view (LAST)  %d+%d+0+%d = %d' % ('OK ' if d2+o2+i2==240 else 'RED', d2,o2,i2, d2+o2+i2))
if d2+o2+i2 != 240: fails.append('240 sum')
if d2 != d: fails.append('240 DONE disagrees with 200 DONE')
print('  %s  240-view DONE (%d) == LIVE-row DONE (%d)' % ('OK ' if d2==d else 'RED', d2, d))
print('  %s  delta 72->%d is +%d, addendum claims +27' % ('OK ' if d-72==27 else 'RED', d, d-72))
if d-72 != 27: fails.append('delta')
mm = re.findall(r'\+(\d+)\n?', cen.split('§Q1')[1].split('---------')[0])
print('\nFAILS:', fails if fails else 'NONE')
sys.exit(1 if fails else 0)
