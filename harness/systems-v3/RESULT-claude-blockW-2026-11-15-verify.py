#!/usr/bin/env python3
"""RESULT-claude-blockW-2026-11-15-verify.py --block WO|WS [--print | --check <RESULT.md>] | --selftest

Block W's figure lines, DERIVED from the two tables (never typed):
  evidence/blockW-2026-11-14/cells.tsv      one row per cell (w-derive.sh: withheld suite, meter, served model)
  evidence/blockW-2026-11-14/cellfacts.tsv  one row per cell (pool, export, concurrency at fire, fire log)
--print writes the figure lines for one model column; --check asserts every one of them occurs, byte for byte, in the result file
(exit 1 on the first missing line). The form is block NO's verifier (RESULT-claude-blockNO-2026-09-28-verify.py), re-written for W's
two problems and table shape.
Rules applied (AMENDMENT-O37-wht-ntt-greenfield-claude-2026-11-11 §W6 = block N §N6, lane B §Q6):
  - a CAP-COST cell's cost ENTERS AT THE CAP; its metered figure is printed on its own line and used in no median, ratio or total;
    (ERRATUM 2026-11-17: true of COST only; the total T below sums every cell's metered T, capped ones included)
  - a premium is UNRESOLVED-CENSORED when either arm's median IS a capped cell's figure (it sits at the cap), else UNRESOLVED-UNDERPOWERED;
  - a ratio whose numerator median is a capped figure prints >= ; whose denominator median is capped prints <= ;
  - correctness is the withheld suite's FULL PASS; a capped cell's pass is a floor.
"""
import argparse, csv, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.normpath(os.path.join(HERE, '..', '..', 'evidence', 'blockW-2026-11-14'))
PROBLEMS = ['WHT', 'NTT']
ARMS = ['plain', 'salt-diet']
MODEL = {'WO': 'claude-opus-5', 'WS': 'claude-sonnet-5'}


def rows(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def money(x):
    return '$%.2f' % x


def lines(block, cells, facts):
    C = [r for r in cells if r['model_block'] == block]
    if len(C) != 12:
        raise SystemExit('REFUSE: %d cells for %s, 12 expected' % (len(C), block))
    F = {r['cell']: r for r in facts}
    cap = float(C[0]['cap'])
    out = []
    kinds = {}
    for r in C:
        kinds[r['end1_kind']] = kinds.get(r['end1_kind'], 0) + 1
    out.append('cells 12 · conditions 4 · model %s · cap COST %.2f' % (MODEL[block], cap))
    out.append('run_state ' + ' · '.join('ENDED: %s %d' % (k, kinds[k]) for k in sorted(kinds)))
    ex = {}
    for r in C:
        ex[r['export12']] = ex.get(r['export12'], 0) + 1
    out.append('export ' + ' · '.join('%s %d' % (k, ex[k]) for k in sorted(ex)))
    ef = {}
    for r in C:
        ef[r['end_from']] = ef.get(r['end_from'], 0) + 1
    out.append('end_from ' + ' · '.join('%s %d' % (k, ef[k]) for k in sorted(ef)))
    sv = sum(1 for r in C if r['served_verdict'] == 'clean')
    heads = sorted({r['served_head'].split('=')[0] for r in C})
    out.append('served: %d of 12 cells clean · head %s only' % (sv, ','.join(heads)))
    # §2 correctness
    fp = {a: 0 for a in ARMS}
    for p in PROBLEMS:
        parts = []
        for a in ARMS:
            rs = sorted([r for r in C if r['problem'] == p and r['arm'] == a], key=lambda r: r['cell'])
            n = sum(1 for r in rs if r['suite'] == 'PASS')
            fp[a] += n
            parts.append('%s %d/3 [%s]' % (a, n, ' '.join(r['tests'] for r in rs)))
        out.append('%-4s %s' % (p, ' · '.join(parts)))
    for a in ARMS:
        out.append('FULL PASS %s %d of 6' % (a, fp[a]))
    # §3 cost
    tot = {a: 0.0 for a in ARMS}
    totT = {a: 0 for a in ARMS}
    capped_metered = []
    over = []
    for p in PROBLEMS:
        med = {}
        capn = {}
        mark = {}
        for a in ARMS:
            rs = [r for r in C if r['problem'] == p and r['arm'] == a]
            vals = []
            for r in rs:
                c = float(r['final_COST'])
                if r['capped'] == 'yes':
                    capped_metered.append(c)
                    c = cap
                elif c > cap:
                    over.append(r['cell'])
                vals.append((c, r['capped'] == 'yes'))
                tot[a] += c
                totT[a] += int(r['final_T'])
            if len(vals) != 3:
                raise SystemExit('REFUSE: %s %s %s has %d cells; the median here is vals[1], defined only at n = 3' % (block, p, a, len(vals)))
            # sort by (cost, uncapped): on an exact tie at the cap the CAPPED figure sorts first, so the CENSORED reading never depends on row order
            vals.sort(key=lambda v: (v[0], not v[1]))
            med[a] = vals[1][0]
            mark[a] = vals[1][1]
            capn[a] = sum(1 for v in vals if v[1])
        ratio = med['salt-diet'] / med['plain']
        m = '≥ ' if mark['salt-diet'] and not mark['plain'] else ('≤ ' if mark['plain'] and not mark['salt-diet'] else '')
        verdict = 'UNRESOLVED-CENSORED' if (mark['salt-diet'] or mark['plain']) else 'UNRESOLVED-UNDERPOWERED'
        out.append('%-4s median COST plain %s · salt-diet %s · ratio %s%.1fx · CAP-COST plain %d salt-diet %d · %s' % (
            p, money(med['plain']), money(med['salt-diet']), m, ratio, capn['plain'], capn['salt-diet'], verdict))
    for a in ARMS:
        out.append('total COST (capped at the cap) %s %s · total T %s' % (a, money(tot[a]), format(totT[a], ',')))
    if capped_metered:
        out.append('capped cells METERED (not used above): %d, %s .. %s against cap %s' % (
            len(capped_metered), money(min(capped_metered)), money(max(capped_metered)), money(cap)))
    out.append('uncapped cells ending above the cap: %d%s' % (len(over), (' (' + ', '.join(sorted(over)) + ')') if over else ''))
    # §4 predictions
    held = 0
    strict = 0
    for p in PROBLEMS:
        cp = sum(1 for r in C if r['problem'] == p and r['arm'] == 'plain' and r['capped'] == 'yes')
        cs = sum(1 for r in C if r['problem'] == p and r['arm'] == 'salt-diet' and r['capped'] == 'yes')
        held += cs >= cp
        strict += cs > cp
    out.append('(i) salt-diet CAP-COST >= plain in %d of 2 problems (%d strictly, %d ties)' % (held, strict, held - strict))
    out.append('(ii) CAP-WALL cells %d' % sum(1 for r in C if r['end1_kind'] == 'CAP-WALL'))
    # §5 declared columns
    def live(field, r):
        v = F[r['cell']][field]
        return v.split('=')[1].split()[0] if '=' in v else 'UNREAD'
    pools = sorted({F[r['cell']]['pool'] for r in C})
    out.append('pool %s for all 12' % ' + '.join(pools))
    cl = [live('claude_live_at_fire', r) for r in C]
    ag = [live('agy_live_at_fire', r) for r in C]
    out.append('claude_live_at_fire >0 in %d of 12 cells · unread %d' % (sum(1 for v in cl if v not in ('0', 'UNREAD')), cl.count('UNREAD')))
    out.append('agy_live_at_fire >0 in %d of 12 cells · unread %d' % (sum(1 for v in ag if v not in ('0', 'UNREAD')), ag.count('UNREAD')))
    return out


def selftest():
    cells = rows(os.path.join(EV, 'cells.tsv'))
    facts = rows(os.path.join(EV, 'cellfacts.tsv'))
    ok = 0
    base = lines('WS', cells, facts)
    # mutant 1: a capped cell's cost is NOT entered at the cap (its metered figure used): the total line must move
    m = [dict(r) for r in cells]
    for r in m:
        if r['capped'] == 'yes':
            r['capped'] = 'no'
    if lines('WS', m, facts) != base:
        ok += 1
    else:
        print('FAIL mutant 1 (cap rule) produced identical lines')
    # mutant 2: a FAIL read as PASS: the FULL PASS line must move
    m = [dict(r) for r in cells]
    for r in m:
        if r['suite'] == 'FAIL':
            r['suite'] = 'PASS'
    if [l for l in lines('WS', m, facts) if l.startswith('FULL PASS')] != [l for l in base if l.startswith('FULL PASS')]:
        ok += 1
    else:
        print('FAIL mutant 2 (correctness) produced identical lines')
    # refusal arm: a block with a missing cell refuses
    try:
        lines('WS', [r for r in cells if r['cell'] != 'clbits03'], facts)
        print('FAIL refusal arm: 11 cells did not refuse')
    except SystemExit:
        ok += 1
    # mutant 3: the CENSORED rule keyed on the COUNT of capped cells (the first draft's rule): Opus WHT, whose salt-diet median is its
    # one capped cell, must still print CENSORED under the real rule
    wo = lines('WO', cells, facts)
    if any(l.startswith('WHT  median') and l.endswith('UNRESOLVED-CENSORED') for l in wo):
        ok += 1
    else:
        print('FAIL mutant 3: Opus WHT does not read CENSORED')
    # arm 5 (gemini's tie, driven): clbdws01 set to exactly the cap, uncapped, beside the capped clbdws02; both row orders must read the same
    t = [dict(r) for r in cells]
    for r in t:
        if r['cell'] == 'clbdws01':
            r['final_COST'] = r['cap']
    a1 = [l for l in lines('WO', t, facts) if l.startswith('WHT  median')]
    a2 = [l for l in lines('WO', list(reversed(t)), facts) if l.startswith('WHT  median')]
    if a1 == a2 and a1[0].endswith('UNRESOLVED-CENSORED'):
        ok += 1
    else:
        print('FAIL arm 5: a tie at the cap reads by row order: %s vs %s' % (a1, a2))
    print('selftest %d/5' % ok)
    return 0 if ok == 5 else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--block', choices=['WO', 'WS'])
    ap.add_argument('--print', action='store_true')
    ap.add_argument('--check')
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    L = lines(a.block, rows(os.path.join(EV, 'cells.tsv')), rows(os.path.join(EV, 'cellfacts.tsv')))
    if a.print or not a.check:
        print('\n'.join(L))
        return 0
    doc = open(a.check, encoding='utf-8').read()
    miss = [l for l in L if l not in doc]
    for l in miss:
        print('MISSING: ' + l)
    print('verify %s: %d of %d figure lines present' % (a.block, len(L) - len(miss), len(L)))
    return 1 if miss else 0


if __name__ == '__main__':
    sys.exit(main())
