#!/usr/bin/env python3
"""RESULT-claude-blockWC-2026-11-17-verify.py --block WCO|WCS [--print | --check <RESULT.md>] | --selftest

Block WC's figure lines, DERIVED from two tables (never typed):
  evidence/blockWC-2026-11-15/result/cells.tsv   one row per condition-cell (wc-derive.sh: B suite, meter, served model, export)
  evidence/blockWC-2026-11-15/p1-baselines.tsv   the 24 phase-1 baselines (prediction (i)'s eligible counts)
--print writes one model column's figure lines; --check asserts every one occurs, byte for byte, in the result file (exit 1 on the
first missing line). The form is block W's verifier, re-written for phase 2.
Rules (AMENDMENT-O37-wht-ntt-specchange-claude-2026-11-13 §WC5/§WC7 = block NC §C5/§C8, lane B §Q6):
  - correctness is the withheld B suite's FULL PASS (rc 0, TESTS passed = total, 0 regressions failed, 0 clause tests failed);
    a capped cell's pass is a floor;
  - a CAP-COST cell's cost ENTERS AT THE CAP; its metered COST is printed on its own line and used in no COST median, ratio or total; T is metered for every cell, capped ones included;
  - a ratio whose numerator median is a capped figure prints >= ; whose denominator median is capped prints <= ;
  - every premium is registered UNRESOLVED-UNDERPOWERED (NC §C8);
  - a REACH-LOSS row is a condition-cell with no phase 2: it is counted, never scored, never priced.
"""
import argparse, csv, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.normpath(os.path.join(HERE, '..', '..', 'evidence', 'blockWC-2026-11-15'))
PROBLEMS = ['NTT', 'WHT']
ARMS = ['plain', 'salt-diet']
MODEL = {'WCO': ('claude-opus-5', 'Opus'), 'WCS': ('claude-sonnet-5', 'Sonnet')}


def rows(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def money(x):
    return '$%.2f' % x


def frac_ok(s, failed_form):
    a, b = s.split('/')
    return (a == '0') if failed_form else (a == b and b != '0')


def full_pass(r):
    return (r['brc'] == '0' and frac_ok(r['tests'], False)
            and frac_ok(r['regressions_failed'], True) and frac_ok(r['clause_failed'], True))


def lines(block, cells, base):
    model, mname = MODEL[block]
    C = [r for r in cells if r['model_block'] == block]
    if len(C) != 12:
        raise SystemExit('REFUSE: %d rows for %s, 12 expected' % (len(C), block))
    S = [r for r in C if r['end2_kind'] != 'REACH-LOSS']
    L = [r for r in C if r['end2_kind'] == 'REACH-LOSS']
    cap = float(S[0]['cap'])
    out = []
    kinds = {}
    for r in C:
        kinds[r['end2_kind']] = kinds.get(r['end2_kind'], 0) + 1
    out.append('rows 12 · conditions 4 · phase-2 cells %d · REACH-LOSS %d · cap COST %s' % (len(S), len(L), S[0]['cap']))
    out.append('end_2 ' + ' · '.join('%s %d' % (k, kinds[k]) for k in sorted(kinds)))
    exps = {}
    for r in S:
        exps[r['export12']] = exps.get(r['export12'], 0) + 1
    out.append('export ' + ' · '.join('%s %d' % (k, exps[k]) for k in sorted(exps)))
    sc = {}
    for r in S:
        sc[r['scored']] = sc.get(r['scored'], 0) + 1
    out.append('scored ' + ' · '.join('%s %d' % (k, sc[k]) for k in sorted(sc)))
    clean = sum(1 for r in S if r['served_verdict'] == 'clean' and r['served_head'].startswith(model + '='))
    out.append('served: %d of %d phase-2 cells clean · head %s only' % (clean, len(S), model))
    for r in L:
        out.append('REACH-LOSS %s %s n=%s source %s end-1 %s, metered %s of %s' % (r['problem'], r['arm'], r['n'], r['cell'],
                   r['source_end1'], money(float(r['final_COST'])), money(float(r['cap']))))
    # §2 correctness
    tot = {a: [0, 0] for a in ARMS}
    for P in PROBLEMS:
        parts = []
        for A in ARMS:
            X = sorted([r for r in S if r['problem'] == P and r['arm'] == A], key=lambda r: r['n'])
            k = sum(1 for r in X if full_pass(r))
            tot[A][0] += k; tot[A][1] += len(X)
            parts.append('%s %d/%d [%s]' % (A, k, len(X), ' '.join(r['tests'] for r in X)))
        out.append('%s  %s' % (P, ' · '.join(parts)))
    for A in ARMS:
        out.append('FULL PASS %s %d of %d' % (A, tot[A][0], tot[A][1]))
    # §3 cost
    tc = {a: 0.0 for a in ARMS}; tT = {a: 0 for a in ARMS}
    for P in PROBLEMS:
        med = {}; capd = {}; ncap = {}
        for A in ARMS:
            X = [r for r in S if r['problem'] == P and r['arm'] == A]
            vals = [(cap if r['capped'] == 'yes' else float(r['final_COST'])) for r in X]
            ncap[A] = sum(1 for r in X if r['capped'] == 'yes')
            tc[A] += sum(vals); tT[A] += sum(int(r['final_T']) for r in X)
            med[A] = statistics.median(vals) if vals else None
            capd[A] = med[A] is not None and med[A] == cap and ncap[A] > 0
        if med['plain'] and med['salt-diet']:
            q = med['salt-diet'] / med['plain']
            op = '>= ' if capd['salt-diet'] else ('<= ' if capd['plain'] else '')
            ratio = 'ratio %s%.1fx' % (op, q)
        else:
            ratio = 'ratio -'
        nn = ' '.join('n %s %d' % (A, len([r for r in S if r['problem'] == P and r['arm'] == A])) for A in ARMS)
        out.append('%s  median COST plain %s · salt-diet %s · %s · CAP-COST plain %d salt-diet %d · %s · UNRESOLVED-UNDERPOWERED' % (
            P, money(med['plain']), money(med['salt-diet']), ratio, ncap['plain'], ncap['salt-diet'], nn))
    for A in ARMS:
        out.append('total COST (capped at the cap) %s %s · total T (metered, every cell) %s' % (A, money(tc[A]), format(tT[A], ',')))
    capped = [r for r in S if r['capped'] == 'yes']
    if capped:
        m = sorted(float(r['final_COST']) for r in capped)
        out.append('capped cells METERED COST (in no COST line above): %d, %s .. %s against cap %s' % (len(m), money(m[0]), money(m[-1]), money(cap)))
    else:
        out.append('capped cells METERED COST (in no COST line above): 0')
    over = [r['cell'] for r in S if r['capped'] != 'yes' and float(r['final_COST']) > cap]
    out.append('uncapped cells ending above the cap: %d%s' % (len(over), (' (' + ', '.join(over) + ')') if over else ''))
    # §4 predictions
    B = [r for r in base if r['model'] == mname]
    el = {A: sum(1 for r in B if r['arm'] == A and r['eligible'] == 'YES') for A in ARMS}
    nb = {A: sum(1 for r in B if r['arm'] == A) for A in ARMS}
    out.append('(i) eligible plain %d/%d · salt-diet %d/%d · %s' % (el['plain'], nb['plain'], el['salt-diet'], nb['salt-diet'],
               'HOLDS' if el['salt-diet'] < el['plain'] else 'MISS'))
    gt = tie = rev = 0; detail = []
    for P in PROBLEMS:
        inc = {}
        for A in ARMS:
            X = [r for r in S if r['problem'] == P and r['arm'] == A]
            inc[A] = (sum(1 for r in X if r['capped'] == 'yes'), len(X))
        a = inc['salt-diet'][0] * inc['plain'][1]; b = inc['plain'][0] * inc['salt-diet'][1]
        gt += a > b; tie += a == b; rev += a < b
        detail.append('%s salt-diet %d/%d plain %d/%d' % (P, inc['salt-diet'][0], inc['salt-diet'][1], inc['plain'][0], inc['plain'][1]))
    out.append('(ii) salt-diet CAP-COST incidence >= plain in %d of 2 problems (%d strictly, %d ties, %d reversed) · %s · %s' % (
        gt + tie, gt, tie, rev, ' · '.join(detail), 'HOLDS' if rev == 0 else 'MISS'))
    out.append('(iii) CAP-WALL cells %d' % kinds.get('CAP-WALL', 0))
    return out


def selftest():
    good = {'brc': '0', 'tests': '16/16', 'regressions_failed': '0/11', 'clause_failed': '0/5'}
    cases = [(good, True), (dict(good, tests='15/16'), False), (dict(good, regressions_failed='1/11'), False),
             (dict(good, clause_failed='2/5'), False), (dict(good, brc='1'), False), (dict(good, tests='0/0'), False)]
    bad = [i for i, (r, want) in enumerate(cases) if full_pass(r) != want]
    print('selftest full_pass: %d/%d arms' % (len(cases) - len(bad), len(cases)))
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--block', choices=sorted(MODEL))
    ap.add_argument('--print', action='store_true')
    ap.add_argument('--check')
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if not a.block:
        ap.error('--block is required')
    L = lines(a.block, rows(os.path.join(EV, 'result', 'cells.tsv')), rows(os.path.join(EV, 'p1-baselines.tsv')))
    if a.print:
        print('\n'.join(L))
    if a.check:
        doc = open(a.check).read()
        for l in L:
            if l not in doc:
                print('MISSING: ' + l); sys.exit(1)
        print('CHECK OK: %d figure lines of %s found in %s' % (len(L), a.block, os.path.basename(a.check)))


if __name__ == '__main__':
    main()
