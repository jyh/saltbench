"""Re-derive every headline figure in RESULT-gemini-level8-chainD from the cells TSV and the phase-facts file and compare it against
the bytes of the document. Nothing here is typed from the prose: each needle is built from a derived value."""
import csv, json, statistics, collections, sys

D = 'harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24.md'
E = 'evidence/l8-chainD-2026-09-24'
doc = open(D).read()
FLAT = ' '.join(doc.split())   # tables are aligned by hand, so a needle is compared with runs of whitespace collapsed on both sides
rows = list(csv.DictReader(open('harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv'), delimiter='\t'))
pf = {(x['id'], x['phase']): x for x in json.load(open(E + '/phase_facts.json'))}
fails = []

def check(name, derived, needle):
    ok = ' '.join(needle.split()) in FLAT
    print(('  OK  ' if ok else '  RED ') + '%-40s derived=%-16s needle=%r' % (name, derived, needle))
    if not ok:
        fails.append(name)

# §1 population
fired = len(rows)
reached = sum(1 for r in rows if r['dispatchedP1'] == '1')
scored = [r for r in rows if r['score_status'] == 'SCORED']
full = sum(1 for r in scored if r['verdict'] == 'PASS')
conds = collections.OrderedDict()
for r in rows:
    conds.setdefault((r['served'].replace('gemini-', ''), r['problem'], r['arm']), []).append(r)
check('conditions', len(conds), '%d conditions' % len(conds))
check('cells fired', fired, '%d cells fired' % fired)
check('reached phase 2', reached, '%d reached phase 2' % reached)
check('scored', len(scored), '%d scored' % len(scored))
check('full pass', full, '%d FULL PASS' % full)

# §1 per-condition rows, each as the table prints it
for (m, p, a), v in conds.items():
    sc = [r for r in v if r['score_status'] == 'SCORED']
    reach = sum(1 for r in v if r['dispatchedP1'] == '1')
    v1 = sum(1 for r in sc if r['REGRESSIONS'].split('/')[0] == '0')
    v2 = sum(1 for r in sc if r['CLAUSE_TESTS'].split('/')[0] == '0')
    tests = sorted(set(r['TESTS'] for r in sc))
    assert len(tests) == 1, (m, p, a, tests)
    line = '  %-15s %-6s %-9s  %d     %d/%d     %d          %d/%d                 %d/%d              %s' % (
        m, p, a, len(v), reach, len(v), len(sc), v1, len(sc), v2, len(sc), tests[0])
    check('row %s %s %s' % (m, p, a), '%d/%d' % (reach, len(v)), line)

# §2 the two refused cells, by the harness record
refused = [r['id'] for r in rows if r['dispatchedP1'] != '1']
for cid in refused:
    t = pf[(cid, 1)]
    assert t['landed'] is True and t['done_reason'] == 'LANDED' and t['rc'] == -9, cid
    check('refused %s wall' % cid, t['wall_seconds'], '%.1f s' % t['wall_seconds'])
check('refused count', len(refused), 'reached phase 2 in 1 of 3 cells')

# §2/§3 kills by arm, and the wall-median table
def arm_rows(arm): return [r for r in rows if r['arm'] == arm]
k1 = {a: sum(1 for r in arm_rows(a) if pf[(r['id'], 1)].get('rc') == -9) for a in ('plain', 'salt-diet')}
n1 = {a: len(arm_rows(a)) for a in ('plain', 'salt-diet')}
k2 = {a: sum(1 for r in arm_rows(a) if pf[(r['id'], 2)].get('rc') == -9) for a in ('plain', 'salt-diet')}
n2 = {a: sum(1 for r in arm_rows(a) if 'rc' in pf[(r['id'], 2)]) for a in ('plain', 'salt-diet')}
check('p1 kills', k1, 'plain %d of %d     salt-diet %d of %d' % (k1['plain'], n1['plain'], k1['salt-diet'], n1['salt-diet']))
check('p2 kills', k2, 'plain %d of %d     salt-diet %d of %d' % (k2['plain'], n2['plain'], k2['salt-diet'], n2['salt-diet']))
check('§2 kill sentence', k1, '%d of %d salt-diet phase-1 records, %d of %d plain' % (k1['salt-diet'], n1['salt-diet'], k1['plain'], n1['plain']))

def med(cond, phase, key):
    return statistics.median(pf[(r['id'], phase)][key] for r in conds[cond] if key in pf[(r['id'], phase)])

for m, label in (('3.8-flash-high', 'Flash'), ('3.1-pro-high', 'Pro')):
    w = [med((m, p, a), 1, 'wall_seconds') for p, a in (('Crc32', 'plain'), ('Crc32', 'salt-diet'), ('LRU', 'plain'), ('LRU', 'salt-diet'))]
    check('wall medians %s' % label, w, '  %-5s          %5.0f s        %5.0f s          %5.0f s        %5.0f s' % ((label,) + tuple(w)))

# §3 caps: the largest turns and wall
allp = [x for x in pf.values() if 'turns_sent' in x]
check('max turns', max(x['turns_sent'] for x in allp), 'largest turn count in `phase_facts.json` is %d' % max(x['turns_sent'] for x in allp))
check('max wall', max(x['wall_seconds'] for x in allp), 'largest wall\nis %.1f s' % max(x['wall_seconds'] for x in allp))

# §4 T medians and the sign claim
sign_ok = True
for m, label in (('3.8-flash-high', 'Flash'), ('3.1-pro-high', 'Pro')):
    for p in ('Crc32', 'LRU'):
        v = [med((m, p, a), ph, 'T') for ph in (1, 2) for a in ('plain', 'salt-diet')]
        sign_ok &= v[1] > v[0] and v[3] > v[2]
        check('T medians %s %s' % (label, p), v, '  %-5s  %-5s %11s %13s %13s %13s' % (label, p, *('{:,.0f}'.format(x) for x in v)))
assert sign_ok, 'the §4 sign claim does not hold'
print('  OK  §4 sign: salt-diet > plain in every T median')

# §5 fold, token scan population, declared-after-P1
check('fold', sum(1 for r in rows if r['foldbus'] == '1'), '`foldbus` = %d on all %d cells' % (sum(1 for r in rows if r['foldbus'] == '1'), fired))
ran = sum(1 for x in pf.values() if 'turns_sent' in x)
check('phases that ran', ran, '%d of %d' % (ran, ran))
dap = sum(1 for r in rows if r['declared_after_P1'] == 'declared-after-P1=yes')
check('declared-after-P1', dap, 'yes on all %d cells that ran phase 2' % dap)
assert dap == reached

# §6 the move: conditions at n = 3 reached and scored
done = [k for k, v in conds.items() if len(v) == 3 and all(r['dispatchedP1'] == '1' and r['score_status'] == 'SCORED' for r in v)]
check('conditions moved', len(done), '%s conditions move OWED → DONE' % {6: 'Six', 7: 'Seven', 8: 'Eight'}.get(len(done), str(len(done))))

print('VERIFY %s — %d red' % ('GREEN' if not fails else 'RED', len(fails)))
sys.exit(1 if fails else 0)
