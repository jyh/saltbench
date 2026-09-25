"""Re-derive every headline figure in RESULT-gemini-level8-chainF from the cells TSV, the phase-facts file, the attempts file and the leg
exports file, and compare it against the bytes of the document. Nothing here is typed from the prose: each needle is built from a derived value.
Tables are aligned by hand, so a needle is compared with runs of whitespace collapsed on both sides."""
import csv, json, statistics, collections, sys

D = 'harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md'
E = 'evidence/l8-chainF-2026-09-24'
doc = open(D).read()
FLAT = ' '.join(doc.split())
rows = list(csv.DictReader(open('harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv'), delimiter='\t'))
pf = {(x['id'], x['phase']): x for x in json.load(open(E + '/phase_facts.json'))}
att = list(csv.DictReader(open(E + '/attempts.tsv'), delimiter='\t'))
exp = list(csv.DictReader(open(E + '/leg_exports.tsv'), delimiter='\t'))
fails = []

def check(name, derived, needle):
    ok = ' '.join(needle.split()) in FLAT
    print(('  OK  ' if ok else '  RED ') + '%-44s derived=%-18s needle=%r' % (name, derived, needle[:90]))
    if not ok:
        fails.append(name)

# §1 population
assert all(r['leg'] != 'Crc32-pro-cp' for r in rows), 'the copy leg belongs to the chain-D result'
scored = [r for r in rows if r['score_status'] == 'SCORED']
conds = collections.OrderedDict()
for r in rows:
    conds.setdefault((r['served'].replace('gemini-', ''), r['problem'], r['arm']), []).append(r)
reached = sum(1 for r in rows if r['dispatchedP1'] == '1')
full = sum(1 for r in scored if r['verdict'] == 'PASS')
check('headline', (len(conds), len(rows)), '%d conditions · %d cells · %d reached phase 2 · %d scored · %d FULL PASS'
      % (len(conds), len(rows), reached, len(scored), full))

tp = lambda t: int(t.split('/')[0])
for (m, p, a), v in conds.items():
    sc = [r for r in v if r['score_status'] == 'SCORED']
    reach = sum(1 for r in v if r['dispatchedP1'] == '1')
    fp = sum(1 for r in sc if r['verdict'] == 'PASS')
    v1 = sum(1 for r in sc if r['REGRESSIONS'].split('/')[0] == '0')
    v2 = sum(1 for r in sc if r['CLAUSE_TESTS'].split('/')[0] == '0')
    tests = ' '.join(r['TESTS'] for r in sorted(sc, key=lambda r: (tp(r['TESTS']), r['TESTS'])))
    line = '  %-15s %-8s %-9s %d %d/%d %d %d/%d %d/%d %d/%d %s' % (m, p, a, len(v), reach, len(v), len(sc), fp, len(sc), v1, len(sc), v2, len(sc), tests)
    check('row %s %s %s' % (m, p, a), '%d/%d pass' % (fp, len(sc)), line)

# §2 attempts, per condition, in fire order
byc = collections.OrderedDict()
for a in att:
    byc.setdefault((a['model'].replace('gemini-', ''), a['problem'], a['arm']), []).append(a)
assert set(byc) == set(conds), 'attempts and cells name different conditions'
for k, v in byc.items():
    assert sum(1 for a in v if a['outcome'] == 'CONDITION-CLEAN') == 1, k
    assert v[-1]['outcome'] == 'CONDITION-CLEAN', ('the kept attempt is the last one', k)
    if len(v) > 1:
        check('attempts %s' % '/'.join(k), len(v), '  %-15s %-8s %-9s %d %s' % (k + (len(v), ' · '.join(a['outcome'] for a in v))))
single = sum(1 for v in byc.values() if len(v) == 1)
check('multi-attempt conditions', len(byc) - single, '%s conditions needed more than one attempt'
      % {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}.get(len(byc) - single, str(len(byc) - single)))

# §2 exports: run sha == score sha on every leg, and the two exports' legs
assert all(e['verdict'] == 'OK' and e['ran_on'] == e['scored_on'] for e in exp)
legs_in_rows = {r['leg'] for r in rows}
for sha in sorted({e['ran_on'] for e in exp if e['leg'] in legs_in_rows}):
    legs = [e['leg'] for e in exp if e['ran_on'] == sha and e['leg'] in legs_in_rows]
    for leg in legs:
        check('export %s %s' % (sha, leg), sha, leg)
    check('export %s named' % sha, len(legs), 'export %s' % sha)

# §3 the truncated cell
t = [r for r in rows if r['id'] == 'l8xpsr01'][0]
check('l8xpsr01 verdict', t['verdict'], 'is a %s at TESTS %s' % (t['verdict'], t['TESTS']))
x = pf[('l8xpsr01', 2)]
check('l8xpsr01 kill', (x['rc'], x['wall_seconds']), 'phase 2 `rc` %d after %.1f s' % (x['rc'], x['wall_seconds']))

# §4 kills by arm, caps
for ph in (1, 2):
    k = {a: sum(1 for r in rows if r['arm'] == a and pf[(r['id'], ph)].get('rc') == -9) for a in ('plain', 'salt-diet')}
    n = {a: sum(1 for r in rows if r['arm'] == a) for a in ('plain', 'salt-diet')}
    check('p%d kills' % ph, k, 'phase %d: plain %d of %d salt-diet %d of %d' % (ph, k['plain'], n['plain'], k['salt-diet'], n['salt-diet']))
killed = sorted('%s phase %d' % (i, ph) for (i, ph), v in pf.items() if v.get('rc') == -9)
assert all(v.get('rc') in (0, -9) for v in pf.values()) and all(v.get('done_reason') == 'LANDED' for v in pf.values())
for kname in killed:
    check('killed %s' % kname, kname, '`%s` %s' % tuple(kname.split(' ', 1)))
allp = [v for v in pf.values() if 'turns_sent' in v]
check('max turns', max(v['turns_sent'] for v in allp), 'largest turn count in `phase_facts.json` is %d' % max(v['turns_sent'] for v in allp))
check('max wall', max(v['wall_seconds'] for v in allp), 'largest wall is %.1f s' % max(v['wall_seconds'] for v in allp))

# §5 T medians and the sign claim
med = lambda k, ph: statistics.median(pf[(r['id'], ph)]['T'] for r in conds[k])
sign = True
for m, label in (('3.1-pro-high', 'Pro'), ('3.8-flash-high', 'Flash')):
    for p in ('Paxos', 'FreeList', 'LZW'):
        v = [med((m, p, a), ph) for ph in (1, 2) for a in ('plain', 'salt-diet')]
        sign &= v[1] > v[0] and v[3] > v[2]
        check('T %s %s' % (label, p), v, '  %-5s  %-8s %s' % (label, p, ' '.join('{:,.0f}'.format(z) for z in v)))
assert sign, 'the §5 sign claim does not hold'
print('  OK  §5 sign: salt-diet > plain in every condition and both phases')

# §7 the move
done = [k for k, v in conds.items() if len(v) == 3 and all(r['dispatchedP1'] == '1' and r['score_status'] == 'SCORED' for r in v)]
check('conditions moved', len(done), '%s conditions move OWED → DONE' % {12: 'Twelve'}.get(len(done), str(len(done))))
check('phase records', len(pf), '(%d records)' % len(pf))
check('per-cell rows', len(rows), '(%d rows;' % len(rows))

print('VERIFY %s — %d red' % ('GREEN' if not fails else 'RED', len(fails)))
sys.exit(1 if fails else 0)
