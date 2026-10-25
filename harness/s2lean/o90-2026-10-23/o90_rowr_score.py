#!/usr/bin/env python3
"""o90_rowr_score.py — the lead's INDEPENDENT re-score of O90 stage 1's row R (AMENDMENT-O90-stage1 ADDENDUM 2, A2.3–A2.10).
gemini's harness carries its own `--score`; this is a second mechanism over the same raw rows, written apart from it, so the
figures posted to evidence are two scorers agreeing rather than one scorer's word (STATUS-bench item 13).
Inputs (all read, none written): the reader's `reads.tsv` and `u2-options.tsv`, its `draw.tsv`, and the frozen keys
`frozen/u1/drawn.tsv` · `frozen/u2/items.tsv` · `frozen-specrec.tsv`. `frozen/SHA256SUMS` and the specrec file must hash to the
registered sha256/16 (A2.1, A2.10 M1), and every key file must match its SHA256SUMS line, or it refuses.
Joins, each a refusal: every reads row equals its draw.tsv row on (seq, kind, item, episode, arm, problem); every u2-options row
names its read's item and episode, and its option is the one items.tsv freezes at that position; an OK U2 read carries 8 option
rows. A read set is COMPLETE when every draw.tsv seq has a reads row; otherwise it prints PARTIAL with the n reached and the
reader's HALT file (if any) beside it, and nothing is quoted from a PARTIAL set as row R's score.
Scoring (A2.3, A2.4, A2.10 Q3): U1 — yes/no against the kernel's key, `cannot tell` scored wrong and counted, no answer UNSCORED;
on ALL problems drawn (draw.tsv; registered 12) and on the NEITHER-YES subset (registered 6) (problems where no artifact is spec_recoverable=yes), per arm, with accuracy
over answered and the per-arm spec_recoverable counts beside it. U2 — accuracy PER ARTIFACT = correct options / scored options
(A2.4's own definition), printed per artifact, and per arm both POOLED over options and the MEAN of artifacts.
The U1 route (A2.10 (b)/(c)) is printed as a reading of its registered rule and nothing else: +10 points a5 over a0 on ALL and
on NEITHER-YES; fewer than 4 NEITHER-YES problems is UNRESOLVABLE. It decides no VOID by itself (§4 has other conditions).
Every figure is "by one reader mechanism (Gemini)" (A2.8 rider 2); the reader is not blind to the arm (A2.7).
usage: o90_rowr_score.py <rowR dir> [--sums16 1629c1c3912b0e69] [--specrec16 00f1d80781af8607] · o90_rowr_score.py --selftest
"""
import collections, hashlib, json, os, shutil, sys, tempfile

SUMS16, SPECREC16 = '1629c1c3912b0e69', '00f1d80781af8607'
PHRASE = 'by one reader mechanism (Gemini)'


def refuse(msg): raise SystemExit('REFUSE: ' + msg)
def sha16(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]
def tsv(p):
    rows = [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]
    return [dict(zip(rows[0], r)) for r in rows[1:]]


def load(d, sums16=SUMS16, specrec16=SPECREC16):
    fz = os.path.join(d, 'frozen')
    if sha16(os.path.join(fz, 'SHA256SUMS')) != sums16: refuse('frozen/SHA256SUMS sha256/16 %s, not the registered %s' % (sha16(os.path.join(fz, 'SHA256SUMS')), sums16))
    if sha16(os.path.join(d, 'frozen-specrec.tsv')) != specrec16: refuse('frozen-specrec.tsv sha256/16 %s, not the registered %s' % (sha16(os.path.join(d, 'frozen-specrec.tsv')), specrec16))
    sums = {l.split()[1].lstrip('./'): l.split()[0] for l in open(os.path.join(fz, 'SHA256SUMS')) if l.strip()}
    for rel in ('u1/drawn.tsv', 'u2/items.tsv'):
        got = hashlib.sha256(open(os.path.join(fz, rel), 'rb').read()).hexdigest()
        if sums.get(rel) != got: refuse('frozen/%s does not match its SHA256SUMS line' % rel)
    drawn = tsv(os.path.join(fz, 'u1', 'drawn.tsv'))
    u1key = {r['item']: r['key'] for r in drawn}; u1prob = {r['item']: r['problem'] for r in drawn}
    u2 = collections.defaultdict(dict)
    for r in tsv(os.path.join(fz, 'u2', 'items.tsv')):
        u2[r['item']][int(r['position'])] = (r['option'], r['key'], r['episode']); u2meta[r['item']] = (r['problem'], r['arm'], r['kind'])
    spec = tsv(os.path.join(d, 'frozen-specrec.tsv'))
    draw = {r['seq']: r for r in tsv(os.path.join(d, 'draw.tsv'))}
    reads = tsv(os.path.join(d, 'reads.tsv'))
    opts = tsv(os.path.join(d, 'u2-options.tsv'))
    return u1key, u2, spec, draw, reads, opts, u1prob


u2meta = {}


def check(u1key, u2, draw, reads, opts, spec, u1prob):
    # F1 (systems on #408): draw.tsv is the READER's file, so its arm/episode are joined to the FROZEN identities, and its
    # population must be exactly the frozen one: each U2 item once; each drawn U1 item once per in_u1 artifact of its problem
    u1art = collections.defaultdict(list)
    for x in spec:
        if x['in_u1'] == 'yes': u1art[x['problem']].append((x['episode'], x['arm']))
    want = collections.Counter(('U2', it) for it in u2)
    want.update(('U1', it, ep) for it, p in u1prob.items() for ep, _ in u1art.get(p, []))
    for r in list(draw.values()) + reads:   # G1 (systems on d350575): kind is the reader's label, so it must be one of two, and it must be the FROZEN one
        if r['kind'] not in ('U1', 'U2'): refuse('seq %s kind %r is neither U1 nor U2' % (r['seq'], r['kind']))
        if (r['kind'] == 'U1') != (r['item'] in u1prob) or (r['kind'] == 'U2') != (r['item'] in u2): refuse('seq %s says %s for %s, which the frozen keys file under the other kind' % (r['seq'], r['kind'], r['item']))
    got = collections.Counter(('U2', r['item']) if r['kind'] == 'U2' else ('U1', r['item'], r['episode']) for r in draw.values())
    if got != want: refuse('draw.tsv is not the frozen population: %d missing, %d extra (e.g. %s)' % (sum((want - got).values()), sum((got - want).values()),
                           sorted((want - got) | (got - want))[:2]))
    for r in draw.values():
        if r['kind'] == 'U2':
            idt = {(ep, u2meta[r['item']][0], u2meta[r['item']][1]) for (_, _, ep) in u2[r['item']].values()}
            if idt != {(r['episode'], r['problem'], r['arm'])}: refuse('draw seq %s U2 %s says %s %s %s, items.tsv freezes %s' % (r['seq'], r['item'], r['episode'], r['problem'], r['arm'], sorted(idt)))
        elif (r['episode'], r['arm']) not in u1art.get(r['problem'], []) or u1prob.get(r['item']) != r['problem']:
            refuse('draw seq %s U1 %s says %s %s %s, which is not an in_u1 artifact of its problem in the frozen specrec' % (r['seq'], r['item'], r['episode'], r['problem'], r['arm']))
    seen = set()
    for r in reads:
        dr = draw.get(r['seq'])
        if dr is None: refuse('reads seq %s is not in draw.tsv' % r['seq'])
        for c in ('kind', 'item', 'episode', 'arm', 'problem'):
            if r[c] != dr[c]: refuse('reads seq %s %s=%s, draw.tsv says %s' % (r['seq'], c, r[c], dr[c]))
        if r['seq'] in seen: refuse('reads seq %s appears twice' % r['seq'])
        seen.add(r['seq'])
        if r['kind'] == 'U1' and r['item'] not in u1key: refuse('U1 item %s has no frozen key' % r['item'])
        if r['kind'] == 'U2' and r['item'] not in u2: refuse('U2 item %s has no frozen key' % r['item'])
    byseq = collections.defaultdict(list)
    for o in opts: byseq[o['seq']].append(o)
    rd = {r['seq']: r for r in reads}
    for s, os_ in byseq.items():
        r = rd.get(s)
        if r is None or r['kind'] != 'U2': refuse('u2-options seq %s has no U2 read' % s)
        for o in os_:
            if (o['item'], o['episode']) != (r['item'], r['episode']): refuse('u2-options seq %s names %s %s, its read %s %s' % (s, o['item'], o['episode'], r['item'], r['episode']))
            fr = u2[r['item']].get(int(o['position']))
            if fr is None or fr[0] != o['option'] or fr[2] != r['episode']: refuse('u2-options seq %s position %s is %s, items.tsv freezes %s' % (s, o['position'], o['option'], fr and fr[0]))
        pos = [int(o['position']) for o in os_]   # F2 (systems): each frozen position exactly once
        if sorted(pos) != sorted(u2[r['item']]): refuse('u2-options seq %s positions %s, items.tsv freezes %s' % (s, sorted(pos), sorted(u2[r['item']])))
    for r in reads:
        if r['kind'] == 'U2' and len(byseq.get(r['seq'], [])) != len(u2[r['item']]):
            refuse('U2 read seq %s carries %d option rows, items.tsv freezes %d' % (r['seq'], len(byseq.get(r['seq'], [])), len(u2[r['item']])))
    return byseq


def theorem_verdict(lo, hi):
    """A6.8: lo/hi are the signs of a5 − a0 under the two bounds (1 · 0 · −1, None if an arm has nothing to bound)."""
    if lo is None or hi is None: return 'NOT COMPUTABLE (an arm has no U2-theorem option to bound)'
    if lo == hi and lo != 0: return 'the bounds agree'
    return 'UNDECIDED (the two bounds do not share one strict direction), beside the observed figure'


def plus10(acc):
    """A2.10 (b): a5's accuracy is AT LEAST 10 points above a0's, exactly: 10·(k5·n0 − k0·n5) ≥ n5·n0."""
    (k0, n0), (k5, n5) = acc['a0'], acc['a5']
    return 10 * (k5 * n0 - k0 * n5) >= n5 * n0


def pct(n, d): return '%.1f%%' % (100.0 * n / d) if d else 'n/a'


def score(d, sums16=SUMS16, specrec16=SPECREC16, registered=(12, 6)):
    u2meta.clear(); u1key, u2, spec, draw, reads, opts, u1prob = load(d, sums16, specrec16)
    byseq = check(u1key, u2, draw, reads, opts, spec, u1prob)
    complete = len(reads) == len(draw)
    halt = os.path.join(d, 'HALT') if os.path.exists(os.path.join(d, 'HALT')) else None
    over = ''.join(' ⚠️ %s OVERRIDDEN to %s (registered %s)' % (nm, v, reg) for nm, v, reg in (('SHA256SUMS', sums16, SUMS16), ('specrec', specrec16, SPECREC16)) if v != reg)   # L3
    out = ['# O90 stage 1 row R, RE-SCORED by bench (o90_rowr_score.py), %s; the reader is not blind to the arm (A2.7)%s' % (PHRASE, over),
           '# inputs: reads.tsv %s · u2-options.tsv %s · draw.tsv %s · frozen/SHA256SUMS %s · frozen-specrec.tsv %s'
           % (sha16(os.path.join(d, 'reads.tsv')), sha16(os.path.join(d, 'u2-options.tsv')), sha16(os.path.join(d, 'draw.tsv')), sums16, specrec16),
           ('COMPLETE: %d of %d reads' % (len(reads), len(draw))) if complete else
           ('PARTIAL: %d of %d reads — NOT row R\'s score%s' % (len(reads), len(draw), '; HALT: ' + open(halt).read().strip() if halt else '; no HALT file'))]
    u1 = [r for r in reads if r['kind'] == 'U1']
    probs = sorted({r['problem'] for r in draw.values() if r['kind'] == 'U1'}, key=int)   # the drawn population, not the reads so far
    yes_probs = {s['problem'] for s in spec if s['spec_recoverable'] == 'yes' and s['in_u1'] == 'yes'}   # M1 counts "on the 24 U1 artifacts"
    sub = [p for p in probs if p not in yes_probs]
    if (len(probs), len(sub)) != registered:
        out.append('⚠️ U1 problems ALL %d · NEITHER-YES %d, NOT the registered %d · %d (A2.10 C2, M1)' % ((len(probs), len(sub)) + registered))
    diffs = {}
    for name, ps in (('ALL', probs), ('NEITHER-YES', sub)):
        out.append('U1 %s: %d problems %s' % (name, len(ps), ' '.join(ps)))
        acc = {}
        for arm in ('a0', 'a5'):
            u = [r for r in u1 if r['arm'] == arm and r['problem'] in ps]
            sc = [r for r in u if r['status'] == 'OK' and r['answer'] in ('yes', 'no', 'cannot tell')]   # L3 (systems): never on the answer alone
            right = [r for r in sc if r['answer'] == u1key[r['item']]]
            ct = [r for r in sc if r['answer'] == 'cannot tell']
            ans = [r for r in sc if r['answer'] != 'cannot tell']
            srs = collections.Counter(s['spec_recoverable'] for s in spec if s['arm'] == arm and s['problem'] in ps and s['in_u1'] == 'yes')
            acc[arm] = (len(right), len(sc))
            out.append('  %s: reads %d · scored %d · correct %d · accuracy %s · cannot-tell %d (scored wrong) · accuracy over answered %s (%d) · '
                       'UNSCORED %d · spec_recoverable yes %d partial %d no %d' % (arm, len(u), len(sc), len(right), pct(len(right), len(sc)), len(ct),
                       pct(sum(r['answer'] == u1key[r['item']] for r in ans), len(ans)), len(ans), len(u) - len(sc), srs['yes'], srs['partial'], srs['no']))
        pair = collections.defaultdict(dict)
        for r in u1:
            if r['problem'] in ps and r['status'] == 'OK' and r['answer'] in ('yes', 'no', 'cannot tell'): pair[r['item']][r['arm']] = r['answer'] == u1key[r['item']]
        pr = [v for v in pair.values() if len(v) == 2]
        out.append('  paired items %d: both right %d · a5 only %d · a0 only %d · neither %d' % (len(pr), sum(v['a0'] and v['a5'] for v in pr),
                   sum(v['a5'] and not v['a0'] for v in pr), sum(v['a0'] and not v['a5'] for v in pr), sum(not v['a0'] and not v['a5'] for v in pr)))
        if acc['a0'][1] and acc['a5'][1]:
            diffs[name] = acc   # L1 (systems): the +10 test is exact integer cross-multiplication, never a float difference
            out.append('  a5 − a0 accuracy %+.1f points (%s)' % (100.0 * (acc['a5'][0] / acc['a5'][1] - acc['a0'][0] / acc['a0'][1]), PHRASE))
    if len(sub) < 4: route = 'UNRESOLVABLE at this n: NEITHER-YES holds %d problems, fewer than 4 (A2.10 (c))' % len(sub)
    elif 'ALL' not in diffs or 'NEITHER-YES' not in diffs: route = 'NOT COMPUTABLE: an arm has no scored U1 read'
    elif plus10(diffs['ALL']) and plus10(diffs['NEITHER-YES']): route = '+10 holds on ALL and on NEITHER-YES (A2.10 (b)): the U1 route condition is MET'
    elif plus10(diffs['ALL']): route = '+10 on ALL only: "U1 difference explained by recovered spec text; VOID not lifted by U1" (A2.10 (b))'
    else: route = '+10 not reached on ALL: the U1 route condition is NOT MET'
    out.append('U1 ROUTE (a reading of A2.10 (b)/(c), deciding no VOID by itself): ' + route + ('' if complete else ' — PARTIAL set, not quotable'))
    keyed = {}
    for s, os_ in byseq.items():
        r = next(x for x in reads if x['seq'] == s)
        for o in os_:
            keyed.setdefault((r['arm'], r['episode']), [])   # L2 (systems): an artifact read only UNSCORED is still listed
            if o['status'] != 'OK': continue
            fr = u2[r['item']][int(o['position'])]
            keyed.setdefault((r['arm'], r['episode']), []).append((o['verdict'] == 'USED') == (fr[1] == 'used'))
    unsc = collections.Counter()
    for s, os_ in byseq.items():
        r = next(x for x in reads if x['seq'] == s); unsc[r['arm']] += sum(o['status'] != 'OK' for o in os_)
    for arm in ('a0', 'a5'):
        arts = sorted(e for (a, e) in keyed if a == arm)
        per = [(e, sum(keyed[(arm, e)]), len(keyed[(arm, e)])) for e in arts]
        n_ok, n_sc = sum(p[1] for p in per), sum(p[2] for p in per)
        sc_ = [p for p in per if p[2]]; mean = sum(p[1] / p[2] for p in sc_) / len(sc_) if sc_ else None
        out.append('U2 %s: artifacts read %d (%d with a scored option) · options scored %d · UNSCORED options %d · POOLED accuracy %s · MEAN of per-artifact accuracy %s over %d (%s)'
                   % (arm, len(per), len(sc_), n_sc, unsc[arm], pct(n_ok, n_sc), '%.1f%%' % (100 * mean) if mean is not None else 'n/a', len(sc_), PHRASE))
        for e, k, n in per: out.append('  U2 %s %s: %d/%d = %s' % (arm, e, k, n, pct(k, n)) if n else '  U2 %s %s: 0 scored (every option UNSCORED)' % (arm, e))
    # ADDENDUM 6 A6.3: every UNSCORED read by CAUSE x KIND x ARM. A6.8 (evidence): a print timeout is missingness that can depend on
    # the arm, so the U2-theorem a0-vs-a5 comparison carries two bounds (every timed-out read's options WRONG, and RIGHT)
    def kind(r): return 'U1' if r['kind'] == 'U1' else 'U2-' + u2meta[r['item']][2]
    def cause(r):
        if r['status'] == 'OK': return None
        if 'timeout' in r['status']: return 'print timeout'
        fails = [f for f in os.listdir(os.path.join(d, 'out')) if f.startswith('read-%s.FAIL-' % r['seq'])] if os.path.isdir(os.path.join(d, 'out')) else []
        tails = [str(json.load(open(os.path.join(d, 'out', f))).get('stderr_tail', '')) for f in fails]
        return 'print timeout' if tails and all('print timeout' in x for x in tails) else 'parse'   # a row written before A6.3 names no cause
    cnt = collections.Counter((cause(r), kind(r), r['arm']) for r in reads if r['status'] != 'OK')
    def timed_out_once(r):   # G2 (systems): any attempt of this read, in any process, ended in the print timeout
        od = os.path.join(d, 'out')
        if not os.path.isdir(od): return False
        return any('print timeout' in str(json.load(open(os.path.join(od, f))).get('stderr_tail', '')) for f in os.listdir(od) if f.startswith('read-%s.FAIL-' % r['seq']))
    resc = collections.Counter((kind(r), r['arm']) for r in reads if r['status'] == 'OK' and timed_out_once(r))
    tot = collections.Counter((kind(r), r['arm']) for r in reads if timed_out_once(r) or (r['status'] != 'OK' and cause(r) == 'print timeout'))
    out.append('Reads with a print-timeout attempt, rescued (answered later) / all, by kind × arm (A6.5 condition): '
               + (' · '.join('%s %s %d/%d' % (k, a, resc[(k, a)], n) for (k, a), n in sorted(tot.items())) or 'none'))
    out.append('UNSCORED reads by cause × kind × arm (A6.3): ' + (' · '.join('%s %s %s %d' % (c, k, a, n) for (c, k, a), n in sorted(cnt.items())) or 'none'))
    to = {r['seq'] for r in reads if r['kind'] == 'U2' and u2meta[r['item']][2] == 'theorem' and cause(r) == 'print timeout'}
    b = {}
    for arm in ('a0', 'a5'):
        okn = scn = ton = 0
        for s_, os_ in byseq.items():
            r = next(x for x in reads if x['seq'] == s_)
            if r['arm'] != arm or u2meta[r['item']][2] != 'theorem': continue
            for o in os_:
                if s_ in to: ton += 1
                elif o['status'] == 'OK':
                    scn += 1; okn += (o['verdict'] == 'USED') == (u2[r['item']][int(o['position'])][1] == 'used')
        b[arm] = (okn, scn, ton)
        out.append('U2-theorem %s: options scored %d · correct %d · observed %s · timed-out options %d · bound WRONG %s · bound RIGHT %s (A6.8)'
                   % (arm, scn, okn, pct(okn, scn), ton, pct(okn, scn + ton), pct(okn + ton, scn + ton)))
    def sgn(k5, n5, k0, n0): return (k5 * n0 > k0 * n5) - (k5 * n0 < k0 * n5) if n5 and n0 else None
    (k0, n0, t0), (k5, n5, t5) = b['a0'], b['a5']
    obs, lo, hi = sgn(k5, n5, k0, n0), sgn(k5, n5 + t5, k0 + t0, n0 + t0), sgn(k5 + t5, n5 + t5, k0, n0 + t0)   # lo: a5 worst, a0 best
    word = {1: 'a5 > a0', -1: 'a5 < a0', 0: 'a5 = a0', None: 'n/a'}
    out.append('U2-theorem a5 vs a0: observed %s · a5-worst/a0-best %s · a5-best/a0-worst %s ⇒ %s (A6.8)' % (word[obs], word[lo], word[hi],
               theorem_verdict(lo, hi) if b['a0'][2] + b['a5'][2] else 'no timed-out option to bound: the observed figure stands alone'))
    return '\n'.join(out), complete


def selftest():
    ok = n = 0
    def arm(name, cond):
        nonlocal ok, n
        n += 1; ok += bool(cond); print(('PASS ' if cond else 'FAIL ') + name)
    def w(p, rows): os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(''.join('\t'.join(r) + '\n' for r in rows))
    def build(t):
        d = os.path.join(t, 'rowR'); fz = os.path.join(d, 'frozen')
        w(os.path.join(fz, 'u1', 'drawn.tsv'), [['problem', 'item', 'key'], ['1', 'p1-a', 'yes'], ['1', 'p1-b', 'no'], ['2', 'p2-a', 'yes'], ['3', 'p3-a', 'no'],
                                                ['4', 'p4-a', 'yes'], ['5', 'p5-a', 'no']])
        u2rows = [['item', 'episode', 'problem', 'arm', 'kind', 'position', 'option', 'key']]
        for it, ep, p, a, kd in (('p1-a0-d-0', 'e10', '1', 'a0', 'theorem'), ('p1-a5-d-0', 'e15', '1', 'a5', 'theorem'), ('p1-a5-d-1', 'e15', '1', 'a5', 'def')):
            u2rows += [[it, ep, p, a, kd, str(i), 'C%d' % i, 'used' if i < 4 else 'not-used'] for i in range(8)]
        w(os.path.join(fz, 'u2', 'items.tsv'), u2rows)
        open(os.path.join(fz, 'SHA256SUMS'), 'w').write(''.join('%s  ./%s\n' % (hashlib.sha256(open(os.path.join(fz, r), 'rb').read()).hexdigest(), r)
                                                                for r in ('u1/drawn.tsv', 'u2/items.tsv')))
        sp = [['episode', 'problem', 'arm', 'in_u1', 'has_explain', 'info_lines', 'recovered_lines', 'spec_recoverable']]
        for p in '12345':
            sp += [['e%s0' % p, p, 'a0', 'yes', 'no', '1', '0', 'no'], ['e%s5' % p, p, 'a5', 'yes', 'yes', '1', '1' if p == '1' else '0', 'yes' if p == '1' else 'no']]
        w(os.path.join(d, 'frozen-specrec.tsv'), sp)
        dr = [['seq', 'kind', 'item', 'episode', 'arm', 'problem']]; rd = [['seq', 'kind', 'item', 'episode', 'arm', 'problem', 'answer', 'status']]
        ans = {('p1-a', 'a0'): 'no', ('p1-a', 'a5'): 'yes', ('p1-b', 'a0'): 'no', ('p1-b', 'a5'): 'no', ('p2-a', 'a0'): 'cannot tell', ('p2-a', 'a5'): 'yes',
               ('p3-a', 'a0'): 'no', ('p3-a', 'a5'): 'no', ('p4-a', 'a0'): 'yes', ('p4-a', 'a5'): 'yes', ('p5-a', 'a0'): 'yes', ('p5-a', 'a5'): ''}
        s = 0
        for (it, a), v in ans.items():
            s += 1; p = it[1]; dr.append([str(s), 'U1', it, 'e%s%s' % (p, a[1]), a, p]); rd.append([str(s), 'U1', it, 'e%s%s' % (p, a[1]), a, p, v, 'OK' if v else 'UNSCORED'])
        op = [['seq', 'item', 'episode', 'position', 'option', 'verdict', 'status']]
        for it, ep, a, wrong in (('p1-a0-d-0', 'e10', 'a0', 2), ('p1-a5-d-0', 'e15', 'a5', 0), ('p1-a5-d-1', 'e15', 'a5', 4)):
            s += 1; dr.append([str(s), 'U2', it, ep, a, '1']); rd.append([str(s), 'U2', it, ep, a, '1', '', 'OK'])
            for i in range(8):
                v = 'USED' if i < 4 else 'NOT-USED'
                if i < wrong: v = 'NOT-USED' if v == 'USED' else 'USED'
                op.append([str(s), it, ep, str(i), 'C%d' % i, v, 'OK'])
        w(os.path.join(d, 'draw.tsv'), dr); w(os.path.join(d, 'reads.tsv'), rd); w(os.path.join(d, 'u2-options.tsv'), op)
        return d
    with tempfile.TemporaryDirectory() as t:
        d = build(t); s16, r16 = sha16(os.path.join(d, 'frozen', 'SHA256SUMS')), sha16(os.path.join(d, 'frozen-specrec.tsv'))
        txt, comp = score(d, s16, r16, (5, 4)); print(txt)
        arm('the drawn problem counts match the registration given, so no count warning prints', 'NOT the registered' not in txt)
        arm('a hash given on the command line is flagged OVERRIDDEN beside the registered one (L3)', 'SHA256SUMS OVERRIDDEN to %s (registered %s)' % (s16, SUMS16) in txt)
        arm('a complete set reads COMPLETE', comp and 'COMPLETE: 15 of 15' in txt)
        # a0 U1 on ALL: p1-a no(wrong) p1-b no(right) p2-a cannot tell(wrong) p3 no(right) p4 yes(right) p5 yes(wrong) = 3/6;
        # a5: p1-a p1-b p2-a p3-a p4-a all right, p5-a empty = 5/5 scored, 1 UNSCORED
        arm('U1 a0 ALL: cannot tell is scored wrong and counted; accuracy over answered excludes it',
            'a0: reads 6 · scored 6 · correct 3 · accuracy 50.0% · cannot-tell 1 (scored wrong) · accuracy over answered 60.0% (5)' in txt)
        arm('U1 a5 ALL: an empty answer is UNSCORED, never guessed', 'a5: reads 6 · scored 5 · correct 5 · accuracy 100.0%' in txt and 'UNSCORED 1' in txt)
        arm('NEITHER-YES drops the problem whose a5 artifact is spec_recoverable=yes', 'U1 NEITHER-YES: 4 problems 2 3 4 5' in txt)
        arm('the a5 − a0 difference on ALL is printed with the one-mechanism phrase', 'a5 − a0 accuracy +50.0 points (%s)' % PHRASE in txt)
        arm('U2 is per artifact (A2.4), pooled and mean beside it',
            'U2 a5: artifacts read 1 (1 with a scored option) · options scored 16 · UNSCORED options 0 · POOLED accuracy 75.0% · MEAN of per-artifact accuracy 75.0% over 1' in txt
            and 'U2 a0 e10: 6/8 = 75.0%' in txt)
        arm('the U1 route reads the registered rule on both sets', 'U1 ROUTE' in txt and 'MET' in txt)
        # mutations of the INPUT, each must refuse or degrade by name
        def mut(fn, expect):
            dd = os.path.join(t, 'm'); shutil.rmtree(dd, ignore_errors=True); shutil.copytree(d, dd); fn(dd)
            try: score(dd, s16, r16, (5, 4)); return False
            except SystemExit as e: return expect in str(e)
        def edit(p, a, b): s = open(p).read(); assert a in s; open(p, 'w').write(s.replace(a, b, 1))
        arm('a read whose arm disagrees with draw.tsv refuses', mut(lambda dd: edit(os.path.join(dd, 'reads.tsv'), '1\tU1\tp1-a\te10\ta0', '1\tU1\tp1-a\te10\ta5'), 'draw.tsv says'))
        arm('an option at the wrong position refuses', mut(lambda dd: edit(os.path.join(dd, 'u2-options.tsv'), '\t2\tC2\t', '\t2\tC3\t'), 'items.tsv freezes'))
        arm('a U2 read missing an option row refuses', mut(lambda dd: edit(os.path.join(dd, 'u2-options.tsv'), [l for l in open(os.path.join(dd, 'u2-options.tsv'))][-1], ''), 'positions [0, 1, 2, 3, 4, 5, 6]'))
        arm('an edited key file refuses against SHA256SUMS', mut(lambda dd: edit(os.path.join(dd, 'frozen', 'u1', 'drawn.tsv'), 'p1-a\tyes', 'p1-a\tno'), 'SHA256SUMS line'))
        arm('a SHA256SUMS that is not the registered one refuses', mut(lambda dd: open(os.path.join(dd, 'frozen', 'SHA256SUMS'), 'a').write('x  ./y\n'), 'not the registered'))
        def drop(p, needle): keep = [l for l in open(p) if needle not in l]; open(p, 'w').write(''.join(keep))   # read, THEN truncate
        def both(dd, a, b): edit(os.path.join(dd, 'draw.tsv'), a, b); edit(os.path.join(dd, 'reads.tsv'), a, b)
        arm('F1: a U2 read relabelled to the other arm in draw AND reads refuses against items.tsv',
            mut(lambda dd: both(dd, '\tU2\tp1-a0-d-0\te10\ta0', '\tU2\tp1-a0-d-0\te10\ta5'), 'items.tsv freezes'))
        arm('F1: a U1 read relabelled to the other arm in draw AND reads refuses against the frozen specrec',
            mut(lambda dd: both(dd, '\tU1\tp3-a\te30\ta0', '\tU1\tp3-a\te30\ta5'), 'not an in_u1 artifact'))
        arm('F1: a draw that drops a frozen read refuses as not the frozen population',
            mut(lambda dd: [drop(os.path.join(dd, f), '\tp5-a\te55\t') for f in ('draw.tsv', 'reads.tsv')],
                'not the frozen population: 1 missing'))
        arm('F2: a duplicated option position refuses even with the right row count',
            mut(lambda dd: edit(os.path.join(dd, 'u2-options.tsv'), [l for l in open(os.path.join(dd, 'u2-options.tsv')) if l.startswith('13\t') and '\t7\tC7\t' in l][0],
                                [l for l in open(os.path.join(dd, 'u2-options.tsv')) if l.startswith('13\t') and '\t6\tC6\t' in l][0]), 'positions'))
        arm('L1: exactly +10 points is MET, by integer arithmetic (3/5 vs 1/2; 30/60 vs 20/50)',
            plus10({'a0': (1, 2), 'a5': (3, 5)}) and plus10({'a0': (20, 50), 'a5': (30, 60)}) and not plus10({'a0': (1, 2), 'a5': (59, 100)}))
        dd = os.path.join(t, 'l2'); shutil.copytree(d, dd)
        o2 = open(os.path.join(dd, 'u2-options.tsv')).read().splitlines(True)
        open(os.path.join(dd, 'u2-options.tsv'), 'w').write(''.join(l.replace('\tOK\n', '\tUNSCORED(missing)\n') if l.startswith('13\t') else l for l in o2))
        txtl2, _ = score(dd, s16, r16, (5, 4))
        arm('L2: an artifact read only UNSCORED is listed as 0 scored and leaves the MEAN\'s n, stated',
            'U2 a0 e10: 0 scored (every option UNSCORED)' in txtl2 and 'U2 a0: artifacts read 1 (0 with a scored option)' in txtl2)
        arm('A6.8: with no timed-out option the line says so and the observed figure stands alone (systems\' L2)',
            'U2-theorem a5 vs a0: observed a5 > a0 · a5-worst/a0-best a5 > a0 · a5-best/a0-worst a5 > a0 ⇒ no timed-out option to bound' in txt)
        arm('G1: a kind outside U1/U2 refuses', mut(lambda dd: both(dd, '2\tU1\tp1-a\te15', '2\tu1\tp1-a\te15'), 'neither U1 nor U2'))
        arm('G1: a U1 item filed as U2 by the reader refuses against the frozen keys', mut(lambda dd: both(dd, '2\tU1\tp1-a\te15', '2\tU2\tp1-a\te15'), 'under the other kind'))
        arm('L1: a U2 read with ZERO option rows refuses (the count check on its own)',
            mut(lambda dd: drop(os.path.join(dd, 'u2-options.tsv'), '\tp1-a5-d-1\t'), 'carries 0 option rows'))
        dd = os.path.join(t, 'l3'); shutil.copytree(d, dd); edit(os.path.join(dd, 'reads.tsv'), 'p4-a\te40\ta0\t4\tyes\tOK', 'p4-a\te40\ta0\t4\tyes\tUNSCORED(x)')
        arm('L3: a U1 row whose status is not OK is never scored on its answer', 'a0: reads 6 · scored 5 · correct 2' in score(dd, s16, r16, (5, 4))[0])
        dd = os.path.join(t, 'g2'); shutil.copytree(d, dd); os.makedirs(os.path.join(dd, 'out'))
        json.dump({'stderr_tail': '[agy] print timeout after 30m0s with turn in progress'}, open(os.path.join(dd, 'out', 'read-14.FAIL-1.json'), 'w'))
        arm('G2: a read that timed out once and then answered is counted rescued, from its FAIL record', 'U2-theorem a5 1/1' in score(dd, s16, r16, (5, 4))[0])
        dd = os.path.join(t, 'to'); shutil.copytree(d, dd)   # seq 13 = the a0 theorem read, timed out on both attempts, written BEFORE A6.3
        edit(os.path.join(dd, 'reads.tsv'), '13\tU2\tp1-a0-d-0\te10\ta0\t1\t\tOK', '13\tU2\tp1-a0-d-0\te10\ta0\t1\t\tUNSCORED(no parseable answer after one retry)')
        o3 = open(os.path.join(dd, 'u2-options.tsv')).read().splitlines(True)
        open(os.path.join(dd, 'u2-options.tsv'), 'w').write(''.join(l.replace('\tOK\n', '\tUNSCORED(missing)\n') if l.startswith('13\t') else l for l in o3))
        os.makedirs(os.path.join(dd, 'out'))
        for k_ in (1, 2): json.dump({'stderr_tail': '[agy] print timeout after 30m0s with turn in progress'}, open(os.path.join(dd, 'out', 'read-13.FAIL-%d.json' % k_), 'w'))
        txto, _ = score(dd, s16, r16, (5, 4))
        arm('A6.3: a pre-A6.3 UNSCORED row is classed print timeout from its FAIL records, by cause × kind × arm', 'print timeout U2-theorem a0 1' in txto)
        arm('A6.8: a timed-out theorem read makes the bounds disagree, and the comparison reads UNDECIDED',
            'U2-theorem a0: options scored 0 · correct 0 · observed n/a · timed-out options 8 · bound WRONG 0.0% · bound RIGHT 100.0%' in txto
            and 'a5-worst/a0-best a5 = a0 · a5-best/a0-worst a5 > a0 ⇒ UNDECIDED' in txto)
        arm('A6.8: an arm with no theorem option reads NOT COMPUTABLE; a tie in either bound or opposite signs read UNDECIDED; one strict sign agrees',
            theorem_verdict(None, None).startswith('NOT COMPUTABLE') and theorem_verdict(1, None).startswith('NOT COMPUTABLE')
            and theorem_verdict(0, 0).startswith('UNDECIDED') and theorem_verdict(-1, 1).startswith('UNDECIDED') and theorem_verdict(-1, 0).startswith('UNDECIDED')
            and theorem_verdict(1, 1) == theorem_verdict(-1, -1) == 'the bounds agree')
        json.dump({'stderr_tail': ''}, open(os.path.join(dd, 'out', 'read-13.FAIL-2.json'), 'w'))
        arm('A6.3: a read whose attempts were not ALL timeouts is classed parse, and leaves the theorem bounds', 'parse U2-theorem a0 1' in score(dd, s16, r16, (5, 4))[0])
        dd = os.path.join(t, 'p'); shutil.copytree(d, dd); l = open(os.path.join(dd, 'reads.tsv')).read().splitlines(True); open(os.path.join(dd, 'reads.tsv'), 'w').write(''.join(l[:-1]))
        o = open(os.path.join(dd, 'u2-options.tsv')).read().splitlines(True); open(os.path.join(dd, 'u2-options.tsv'), 'w').write(''.join(o[:-8]))
        txt2, comp2 = score(dd, s16, r16, (5, 4))
        arm('a partial set prints PARTIAL with its n and marks the route not quotable', not comp2 and 'PARTIAL: 14 of 15' in txt2 and 'not quotable' in txt2)
        dd = os.path.join(t, 'u'); shutil.copytree(d, dd)
        edit(os.path.join(dd, 'frozen-specrec.tsv'), 'e25\t2\ta5\tyes\tyes\t1\t0\tno', 'e25\t2\ta5\tyes\tyes\t1\t1\tyes')
        edit(os.path.join(dd, 'frozen-specrec.tsv'), 'e35\t3\ta5\tyes\tyes\t1\t0\tno', 'e35\t3\ta5\tyes\tyes\t1\t1\tyes')
        txt3, _ = score(dd, s16, sha16(os.path.join(dd, 'frozen-specrec.tsv')), (5, 4))
        arm('a NEITHER-YES count off the registration is flagged beside the figures', '⚠️ U1 problems ALL 5 · NEITHER-YES 2, NOT the registered 5 · 4' in txt3)
        arm('fewer than 4 NEITHER-YES problems reads UNRESOLVABLE (A2.10 (c))', 'UNRESOLVABLE at this n: NEITHER-YES holds 2' in txt3)
    print('SELFTEST %d/%d' % (ok, n))
    return ok == n


if __name__ == '__main__':
    if sys.argv[1:] == ['--selftest']: sys.exit(0 if selftest() else 1)
    if not sys.argv[1:]: print(__doc__); sys.exit(2)
    a = sys.argv[1:]; kw = {}
    if '--sums16' in a: kw['sums16'] = a[a.index('--sums16') + 1]
    if '--specrec16' in a: kw['specrec16'] = a[a.index('--specrec16') + 1]
    txt, comp = score(a[0], **kw); print(txt); sys.exit(0 if comp else 3)
