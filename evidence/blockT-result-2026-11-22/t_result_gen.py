#!/usr/bin/env python3
"""t_result_gen.py — block T's figure lines, printed from the per-cell table and nothing typed.

  python3 t_result_gen.py --block TO|TS --print            print every figure line of that model's RESULT
  python3 t_result_gen.py --block TO|TS --check <RESULT.md> assert each printed line occurs as a whole line in the RESULT's bytes
  python3 t_result_gen.py --census                         the O37 re-cut's block-T line (24 conditions, n per condition)

Inputs, beside this file: cells.tsv (t-derive.sh, from the objects on the run box) and categories.tsv (the statement category per
cell: a READING of the subject's code, each row naming the post or addendum it was read in; it is not a score and not derived here).
Rules (block N §N6 and NC's RESULT form): a CAP-COST cell's COST ENTERS AT THE CAP in every median, ratio and total; its metered
COST is printed on its own line. T is metered for every cell. A ratio whose median sits at the cap is censored and prints its bound.
"""
import csv, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROBS = ['Luby', 'AES', 'Liveness', 'MaxFlow', 'BinomialHeap', 'LinearScan']
ARMS = ['plain', 'salt-diet']


def load():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'cells.tsv')), delimiter='\t'))
    cats = {r['cell']: r for r in csv.DictReader(open(os.path.join(HERE, 'categories.tsv')), delimiter='\t')}
    ids = [r['cell'] for r in rows]
    assert len(rows) == 72 and len(set(ids)) == 72, f'population: {len(rows)} rows, {len(set(ids))} unique, not 72'
    assert set(ids) == set(cats), f'categories.tsv and cells.tsv name different cells: {sorted(set(ids) ^ set(cats))}'
    for r in rows:
        r['category'] = cats[r['cell']]['category']
    return rows


def cost(r):
    cap = float(r['cap'])
    return cap if r['capped'] == 'yes' else float(r['final_COST'])


def money(x):
    return f'${x:,.2f}'


def block_lines(rows, b):
    R = [r for r in rows if r['model_block'] == b]
    assert len(R) == 36, f'{b}: {len(R)} rows'
    out = []
    cap = {r['cap'] for r in R}
    assert len(cap) == 1, f'{b}: caps {cap}'
    cap = float(cap.pop())
    ends = {}
    for r in R:
        ends[r['end1_kind']] = ends.get(r['end1_kind'], 0) + 1
    exp = sorted({r['export12'] for r in R})
    sc = {}
    for r in R:
        sc[r['scored']] = sc.get(r['scored'], 0) + 1
    heads = sorted({r['served_head'].split('=')[0] for r in R})
    clean = sum(1 for r in R if r['served_verdict'] == 'clean')
    out.append(f'rows {len(R)} · conditions {len({(r["problem"], r["arm"]) for r in R})} · cap COST {cap:.2f}')
    out.append('end_1 ' + ' · '.join(f'{k} {v}' for k, v in sorted(ends.items())))
    out.append('export ' + ' '.join(f'{e} {sum(1 for r in R if r["export12"] == e)}' for e in exp))
    out.append('scored ' + ' · '.join(f'{k} {v}' for k, v in sorted(sc.items())))
    out.append(f'served: {clean} of {len(R)} cells clean · head {" ".join(heads)} only')
    nb = [r for r in R if int(r['born_n'] or 0) > 0]
    out.append(f'born-during: {len(nb)} of {len(R)} cells saw a $HOME entry born during the run · transcript hits on those entries {sum(int(r["born_hits"] or 0) for r in R)} · control own-id hits > 0 in {sum(1 for r in R if int(r["control_own_id_hits"] or 0) > 0)} of {len(R)}')
    sc_ = {l.split('\t')[0]: l.split('\t')[3].strip() for l in open(os.path.join(HERE, 't_section_cmp.out')) if l.startswith('clb')}
    eq = sum(1 for r in R if sc_.get(r['cell']) == 'EQUAL')
    out.append(f'section as built (REQUIREMENTS.md at the root commit) equal to the export card: {eq} of {len(R)} · VOID by §T7 {len(R) - eq}')
    for r in sorted(R, key=lambda r: r['cell']):
        if r['scored'] != 'HEAD':
            out.append(f'scored at {r["scored"]}: {r["cell"]} ({r["problem"]} {r["arm"]} #{r["n"]}, {r["end1_kind"]})')
    for r in sorted(R, key=lambda r: r['cell']):
        if r['end1_kind'] not in ('LANDED', 'CAP-COST'):
            out.append(f'end {r["end1_kind"]}: {r["cell"]} ({r["problem"]} {r["arm"]} #{r["n"]}) at {r["end1_at"]}')
    # §2 correctness
    tot = {a: [0, 0] for a in ARMS}
    for p in PROBS:
        parts = []
        for a in ARMS:
            C = sorted([r for r in R if r['problem'] == p and r['arm'] == a], key=lambda r: r['n'])
            k = sum(1 for r in C if r['suite'] == 'PASS')
            tot[a][0] += k; tot[a][1] += len(C)
            parts.append(f'{a} {k}/{len(C)} [{" ".join(r["tests"] for r in C)}]')
        out.append(f'{p:<12} ' + ' · '.join(parts))
    for a in ARMS:
        out.append(f'FULL PASS {a} {tot[a][0]} of {tot[a][1]}')
    # §3 cost
    tc = {a: [0.0, 0] for a in ARMS}
    for p in PROBS:
        med, capn, atcap = {}, {}, {}
        for a in ARMS:
            C = [r for r in R if r['problem'] == p and r['arm'] == a]
            med[a] = statistics.median(cost(r) for r in C)
            capn[a] = sum(1 for r in C if r['capped'] == 'yes')
            atcap[a] = abs(med[a] - cap) < 1e-9
        ratio = med['salt-diet'] / med['plain']
        if atcap['salt-diet'] and atcap['plain']:
            rs = 'both medians at the cap'
        elif atcap['salt-diet']:
            rs = f'>= {ratio:.1f}x'
        elif atcap['plain']:
            rs = f'<= {ratio:.1f}x'
        else:
            rs = f'{ratio:.1f}x'
        out.append(f'{p:<12} median COST plain {money(med["plain"])} · salt-diet {money(med["salt-diet"])} · ratio {rs} · CAP-COST plain {capn["plain"]} salt-diet {capn["salt-diet"]} · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED')
    for a in ARMS:
        C = [r for r in R if r['arm'] == a]
        out.append(f'total COST (capped at the cap) {a} {money(sum(cost(r) for r in C))} · total T (metered, every cell) {sum(int(r["final_T"]) for r in C):,}')
    capped = [r for r in R if r['capped'] == 'yes']
    if capped:
        lo = min(float(r['final_COST']) for r in capped); hi = max(float(r['final_COST']) for r in capped)
        out.append(f'capped cells METERED COST (in no COST line above): {len(capped)}, {money(lo)} .. {money(hi)} against cap {money(cap)}')
    else:
        out.append('capped cells: 0')
    over = [r['cell'] for r in R if r['capped'] != 'yes' and float(r['final_COST']) > cap]
    out.append(f'uncapped cells ending above the cap: {len(over)}' + (f' ({", ".join(sorted(over))})' if over else ''))
    out.append(f'block total COST (capped at the cap) {money(sum(cost(r) for r in R))} · metered {money(sum(float(r["final_COST"]) for r in R))}')
    # §4 predictions
    held = 0; strict = 0; ties = 0; rev = 0
    for p in PROBS:
        s = sum(1 for r in R if r['problem'] == p and r['arm'] == 'salt-diet' and r['capped'] == 'yes')
        q = sum(1 for r in R if r['problem'] == p and r['arm'] == 'plain' and r['capped'] == 'yes')
        held += s >= q; strict += s > q; ties += s == q; rev += s < q
    out.append(f'(i) salt-diet CAP-COST incidence >= plain in {held} of {len(PROBS)} problems ({strict} strictly, {ties} ties, {rev} reversed) · {"HOLDS" if rev == 0 else "MISS"}')
    for p in PROBS:
        s = sum(1 for r in R if r['problem'] == p and r['arm'] == 'salt-diet' and r['capped'] == 'yes')
        q = sum(1 for r in R if r['problem'] == p and r['arm'] == 'plain' and r['capped'] == 'yes')
        out.append(f'(i) {p} salt-diet {s}/3 plain {q}/3')
    out.append(f'(ii) CAP-WALL cells {sum(1 for r in R if r["end1_kind"] == "CAP-WALL")}')
    # §5 the statement line (§T3's extra line), categories as READ
    for a in ARMS:
        C = [r for r in R if r['arm'] == a]
        cc = {}
        for r in C:
            cc[r['category']] = cc.get(r['category'], 0) + 1
        out.append(f'statement {a}: ' + ' · '.join(f'{k} {v}' for k, v in sorted(cc.items())))
    for p in PROBS:
        parts = []
        for a in ARMS:
            C = sorted([r for r in R if r['problem'] == p and r['arm'] == a], key=lambda r: r['n'])
            parts.append(f'{a} ' + ' | '.join(r['category'] for r in C))
        out.append(f'statement {p:<12} ' + ' · '.join(parts))
    S = [r for r in R if r['arm'] == 'salt-diet']
    diff = [r for r in S if ' diff=' in r['specdefs'] and not r['specdefs'].split(' diff=')[1].startswith('0')]
    out.append(f'salt-diet cells whose solution REDEFINES a provided spec fn (specdefs DIFFERENT > 0): {len(diff)} of {len(S)}')
    for r in sorted(diff, key=lambda r: (PROBS.index(r['problem']), r['n'])):
        out.append(f'  {r["cell"]} {r["problem"]} #{r["n"]} {r["specdefs"]}')
    return out


def census(rows):
    out = []
    conds = {}
    for r in rows:
        conds.setdefault((r['model_block'], r['problem'], r['arm']), []).append(r)
    n3 = sum(1 for v in conds.values() if len(v) == 3)
    out.append(f'block T: the six block-N problems x statement, Claude lane: {len(conds)} conditions, {n3} at n = 3, cells of record {sum(len(v) for v in conds.values())}')
    out.append(f'block T spend: COST (capped at the cap) {money(sum(cost(r) for r in rows))} · metered {money(sum(float(r["final_COST"]) for r in rows))} · Luby {money(sum(float(r["final_COST"]) for r in rows if r["problem"] == "Luby"))} metered')
    return out


def main(a):
    rows = load()
    if '--census' in a:
        print('\n'.join(census(rows))); return 0
    b = a[a.index('--block') + 1]
    L = block_lines(rows, b)
    if '--print' in a:
        print('\n'.join(L)); return 0
    if '--check' in a:
        doc = open(a[a.index('--check') + 1], encoding='utf-8').read().split('\n')
        S = set(doc); miss = [l for l in L if l not in S]
        for l in miss:
            print('MISSING:', l)
        print(f'check {b}: {len(L) - len(miss)} of {len(L)} figure lines present')
        return 1 if miss else 0
    print(__doc__); return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
