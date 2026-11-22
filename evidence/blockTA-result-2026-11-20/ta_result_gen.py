#!/usr/bin/env python3
"""Block TA (O37, the agy lane x block N's six x statement) per-cell table of record, and every figure the result quotes. Nothing is typed.
Reads TRACKED FILES ONLY, all in this directory unless named:
  flash-tally.tsv, argon-tally.tsv   the hand's tallies (byte copies, ta_collect.py): one row per cell; `statement` holds the CATEGORY
  cell_facts.json                    wa_facts.py per cell (ta_collect.py): model, client, export, wall_seconds, done_reason, turns
  receipts.tsv                       score_wave_v3.sh per cell (ta_collect.py): verdict, TESTS, the scorer's TRUNCATED figure, interface
  meters.tsv                         agy_meter_v3.py per cell (ta_collect.py): served models, meter verdict
  swarm.tsv                          ta_swarm_census.py on the run box: per cell dir, the agy `swarm` tool's workers the subject ADDED
                                     (their models), read from the main conversation's stream; a worker's own conversation is UNREAD
  events.tsv                         ta_events.sh on the run box: per cell dir, ^AGY_ERROR lines (timeout EVENTS) and `print timeout`
                                     lines (what the scorer and wa_facts.py count: 3 per event) in ctl/agy-stderr-1.txt
  ../blockTA-2026-11-17/ta_price.out        the REGISTERED price (§TA3)
  ../blockTA-2026-11-17/ta_recut_argon.out  ADDENDUM 8's argon re-cut of AES..LinearScan
A value that cannot be read is UNREAD, never blank and never zero. A cell present in one input and absent from another REFUSES.
  python3 ta_result_gen.py            -> the per-cell table (TSV, stdout); cells.tsv beside this file is its committed output
  python3 ta_result_gen.py --summary  -> the figure lines RESULT-gemini-blockTA-2026-11-20.md quotes, from the table's own rows
  python3 ta_result_gen.py --check <result.md>  -> rc 0 iff every --summary line occurs verbatim in that file (rc 1 names the missing)

CATEGORY is the label the lead ruled per cell (bench's six, bus 2026-11-19; EXEC USE per THE LINE, 2026-11-20), read from the head of the
tally's `statement` cell: the text after 'CATEGORY: ' up to the first ' ·', ' [' or a parenthesis that is not a qualifier. The qualifiers
kept are '(partial)', '(unverified)' and USED's '(partial: k of n …)', which reads as 'USED (partial)'."""
import csv, json, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, '..', 'blockTA-2026-11-17')
PROBLEMS = ('Luby', 'AES', 'Liveness', 'MaxFlow', 'BinomialHeap', 'LinearScan')
ARMS = ('plain', 'salt-diet')
WAVES = (('flash', 'gemini-3.8-flash-high'), ('argon', 'gemini-4-argon-high'))
CATS = ('USED', 'USED (partial)', 'USED (unverified)', 'SPEC TRANSCRIBED, CONTRACT ABSENT', 'EXEC USE', 'EXEC USE (partial)',
        'TEST ORACLE', 'TEST ORACLE (partial)', 'WEAK TRACE', 'NO TRACE')
COLS = ['id', 'wave', 'problem', 'arm', 'rep', 'requested_model', 'init_model', 'served_models', 'client_sha256', 'export_sha', 'root',
        'done_reason', 'verdict', 'TESTS', 'events', 'print_timeout_lines', 'scorer_truncated_lines', 'truncated', 'turns_sent',
        'wall_seconds', 'T', 'interface', 'category', 'swarm_added_models', 'receipt_sha256_16']


def category(stmt):
    m = re.match(r'CATEGORY: (.*)$', stmt)
    if not m:
        return 'UNREAD'
    s = m.group(1)
    if re.match(r'USED \(partial[:)]', s):   # before the loop: 'USED (partial: 1 of 2 …)' must not read as bare USED
        return 'USED (partial)'
    for c in sorted(CATS, key=len, reverse=True):
        if s.startswith(c):
            return c
    if s.startswith('USED'):
        return 'USED'
    return 'UNREAD'


def load():
    tally = {}
    for w, _ in WAVES:
        for r in csv.DictReader(open(os.path.join(HERE, '%s-tally.tsv' % w)), delimiter='\t'):
            if r['cell'] in tally:
                sys.exit('REFUSE: %s in two tallies' % r['cell'])
            tally[r['cell']] = dict(r, wave=w)
    facts = {f['id']: f for f in json.load(open(os.path.join(HERE, 'cell_facts.json')))}
    rec = {r['id']: r for r in csv.DictReader(open(os.path.join(HERE, 'receipts.tsv')), delimiter='\t')}
    met = {r['id']: r for r in csv.DictReader(open(os.path.join(HERE, 'meters.tsv')), delimiter='\t')}
    ev = {}
    for r in csv.DictReader(open(os.path.join(HERE, 'events.tsv')), delimiter='\t'):
        ev.setdefault(r['id'], []).append(r)
    sw = {}
    for r in csv.DictReader(open(os.path.join(HERE, 'swarm.tsv')), delimiter='\t'):
        sw[(r['id'], r['root'])] = r
    for name, d in (('cell_facts.json', facts), ('receipts.tsv', rec), ('meters.tsv', met)):
        if set(d) != set(tally):
            sys.exit('REFUSE: %s cells differ from the tallies: %s' % (name, sorted(set(d) ^ set(tally))))
    return tally, facts, rec, met, ev, sw


def table():
    tally, facts, rec, met, ev, sw = load()
    rows = []
    for i in sorted(tally, key=lambda i: (WAVES.index(next(x for x in WAVES if x[0] == tally[i]['wave'])),
                                          PROBLEMS.index(facts[i]['problem']), i[5], i[3:5])):
        f, t, r, m = facts[i], tally[i], rec[i], met[i]
        er = [e for e in ev.get(i, []) if e['root'] == f['root']]   # the cell of record's own root; a discarded attempt's root is another row
        stmt = t['statement']
        rows.append(dict(
            id=i, wave=t['wave'], problem=f['problem'], arm=f['arm'], rep=i[5], requested_model=f['requested_model'],
            init_model=f['init_model'], served_models=m['served_models'], client_sha256=f['client_sha256'],
            export_sha=f['export_sha'][:12], root=f['root'], done_reason=f['done_reason'], verdict=r['verdict'], TESTS=r['TESTS'],
            events=er[0]['events_AGY_ERROR'] if len(er) == 1 else 'UNREAD',
            print_timeout_lines=er[0]['scorer_lines_print_timeout'] if len(er) == 1 else 'UNREAD',
            scorer_truncated_lines=r['scorer_truncated_lines'],
            truncated=('UNREAD' if len(er) != 1 else ('yes' if int(er[0]['events_AGY_ERROR']) else 'no')),
            turns_sent=str(f['turns_sent']), wall_seconds='%.1f' % f['wall_seconds'], T=str(f['T']), interface=r['interface'],
            category=category(stmt), receipt_sha256_16=r['receipt_sha256_16'],
            swarm_added_models=sw[(i, f['root'])]['added_models'] if (i, f['root']) in sw else 'UNREAD'))
    return rows, ev


def count(vals):
    d = {}
    for v in vals:
        d[v] = d.get(v, 0) + 1
    return ' '.join('%s=%d' % kv for kv in sorted(d.items()))


def price():
    txt = open(os.path.join(REG, 'ta_price.out')).read()
    p = {}
    for P, a, fl, ar in re.findall(r'^NA (\w+) (plain|salt-diet): .*Flash price 3 x [0-9.]+ = ([0-9]+) s · argon price 3 x [0-9.]+ x [0-9.]+ = ([0-9]+) s$', txt, re.M):
        p[('flash', P, a)] = int(fl)
        p[('argon', P, a)] = int(ar)
    if len(p) != 24:
        sys.exit('REFUSE: %d price rows in ta_price.out, 24 expected' % len(p))
    rc = open(os.path.join(REG, 'ta_recut_argon.out')).read()
    m = re.search(r'^argon AES\.\.LinearScan: registered ([0-9]+) s = [0-9.]+ h · re-cut ([0-9]+) s', rc, re.M)
    if not m:
        sys.exit('REFUSE: no re-cut line in ta_recut_argon.out')
    return p, int(m.group(1)), int(m.group(2))


def summary(rows, ev):
    L = []
    p, a8_reg, a8_cut = price()
    for w, model in WAVES:
        rs = [r for r in rows if r['wave'] == w]
        L.append('%s: cells %d · scored %d · PASS %d · FULL PASS %d · receipts %d' % (
            w, len(rs), sum(r['verdict'] in ('PASS', 'FAIL') for r in rs), sum(r['verdict'] == 'PASS' for r in rs),
            sum(r['verdict'] == 'PASS' and r['TESTS'].split('/')[0] == r['TESTS'].split('/')[-1] for r in rs),
            sum(r['receipt_sha256_16'] != 'UNREAD' for r in rs)))
        for k in ('requested_model', 'init_model', 'served_models', 'export_sha', 'done_reason'):
            L.append('%s %s %s' % (w, k, count(r[k] for r in rs)))
        for c in sorted({r['client_sha256'] for r in rs}):
            ids = [r['id'] for r in rs if r['client_sha256'] == c]
            L.append('%s client %s: %d cells%s' % (w, c, len(ids), '' if len(ids) > 6 else ' (' + ' '.join(ids) + ')'))
        for P in PROBLEMS:
            for a in ARMS:
                c = [r for r in rs if r['problem'] == P and r['arm'] == a]
                L.append('%s %s %s: PASS %d of %d [%s] · truncated %d (events %d; print-timeout lines %d) · interface %s · clients %s' % (
                    w, P, a, sum(r['verdict'] == 'PASS' for r in c), len(c), ' '.join(r['TESTS'] for r in c),
                    sum(r['truncated'] == 'yes' for r in c), sum(int(r['events']) for r in c),
                    sum(int(r['print_timeout_lines']) for r in c), ','.join(sorted({r['interface'] for r in c})),
                    ','.join(sorted({r['client_sha256'][:8] for r in c}))))
        tr = [r for r in rs if r['truncated'] == 'yes']
        L.append('%s truncated %d cells, %d events, %d print-timeout lines (scorer figure %d): %s' % (
            w, len(tr), sum(int(r['events']) for r in tr), sum(int(r['print_timeout_lines']) for r in tr),
            sum(int(r['scorer_truncated_lines']) for r in tr),
            ' '.join('%s=%s/%s' % (r['id'], r['events'], r['print_timeout_lines']) for r in tr) or '-'))
        for a in ARMS:
            L.append('%s %s categories: %s' % (w, a, ' · '.join('%s %d' % (c, n) for c in CATS
                                                               for n in [sum(r['category'] == c for r in rs if r['arm'] == a)] if n)))
        sx = [r for r in rs if r['swarm_added_models'] != '-']
        out_ = lambda r: r['truncated'] == 'yes' or r['swarm_added_models'] != '-'   # the lead's ruling 2026-11-20: both leave every comparison
        L.append('%s comparison n per condition, truncated and swarm cells OUT: %s' % (w, ' · '.join(
            '%s %s %d' % (P, a, sum(not out_(r) for r in rs if r['problem'] == P and r['arm'] == a)) for P in PROBLEMS for a in ARMS)))
        L.append('%s salt-diet categories, swarm cells OUT: %s' % (w, ' · '.join('%s %d' % (c, n) for c in CATS
                 for n in [sum(r['category'] == c for r in rs if r['arm'] == 'salt-diet' and r['swarm_added_models'] == '-')] if n)))
        L.append('%s salt-diet PASS, swarm cells OUT: %d of %d' % (w, sum(r['verdict'] == 'PASS' for r in rs if r['arm'] == 'salt-diet' and r['swarm_added_models'] == '-'),
                                                                  sum(r['arm'] == 'salt-diet' and r['swarm_added_models'] == '-' for r in rs)))
        L.append('%s swarm workers added in %d of %d cells (swarm.tsv read %d): %s' % (
            w, len(sx), len(rs), sum(r['swarm_added_models'] != 'UNREAD' for r in rs),
            ' '.join('%s=%s' % (r['id'], r['swarm_added_models']) for r in sx) or '-'))
        spent = sum(float(r['wall_seconds']) for r in rs)
        reg = sum(v for (ww, P, a), v in p.items() if ww == w)
        L.append('%s cell wall SPENT %.1f s against the registered %d s (x%.3f) · a LOWER BOUND: %d truncated cells, %d with unmetered swarm workers' % (
            w, spent, reg, spent / reg, len(tr), len(sx)))
        for P in PROBLEMS:
            ps = sum(float(r['wall_seconds']) for r in rs if r['problem'] == P)
            L.append('%s %s sextet: SPENT %.1f s against the registered %d s' % (w, P, ps, p[(w, P, 'plain')] + p[(w, P, 'salt-diet')]))
        if w == 'argon':
            rest = sum(float(r['wall_seconds']) for r in rs if r['problem'] != 'Luby')
            L.append('argon AES..LinearScan SPENT %.1f s against ADDENDUM 8 re-cut %d s (x%.3f; registered %d s)' % (rest, a8_cut, rest / a8_cut, a8_reg))
        # §TA3 (i): within a condition, salt-diet's TURNS-CUT incidence >= plain's (cells with >= 1 timeout event)
        holds = [P for P in PROBLEMS if sum(r['truncated'] == 'yes' for r in rs if r['problem'] == P and r['arm'] == 'salt-diet')
                 >= sum(r['truncated'] == 'yes' for r in rs if r['problem'] == P and r['arm'] == 'plain')]
        L.append('%s prediction (i) holds in %d of 6 problems · truncated cells plain %d, salt-diet %d' % (
            w, len(holds), sum(r['truncated'] == 'yes' for r in rs if r['arm'] == 'plain'),
            sum(r['truncated'] == 'yes' for r in rs if r['arm'] == 'salt-diet')))
    of_record = {r['root'] for r in rows}
    other = sorted('%s %s' % (e['id'], e['root']) for v in ev.values() for e in v if e['root'] not in of_record)
    L.append('cell dirs on the run box not of record: %d: %s' % (len(other), ' · '.join(other) or '-'))
    return L


def main():
    rows, ev = table()
    if len(sys.argv) > 1 and sys.argv[1] == '--summary':
        print('\n'.join(summary(rows, ev)))
    elif len(sys.argv) > 2 and sys.argv[1] == '--check':
        text = open(sys.argv[2]).read()
        miss = [l for l in summary(rows, ev) if l not in text]
        n = len(summary(rows, ev))
        print('%d of %d summary lines occur verbatim in %s' % (n - len(miss), n, sys.argv[2]))
        for l in miss:
            print('MISSING: ' + l)
        sys.exit(1 if miss else 0)
    else:
        print('\t'.join(COLS))
        for r in rows:
            print('\t'.join(str(r[c]) for c in COLS))


if __name__ == '__main__':
    main()
