#!/usr/bin/env python3
"""zf_result.py — the desk ZF set's RESULT of record, derived (AMENDMENT-ZF-gemini4-argon-2026-10-13.md).

bench (lead), 2026-10-24. Read-only. Every figure it prints is computed from its inputs; nothing is typed.

INPUTS
  --cells     evidence/zf-result/zf-cells.tsv     one row per harvested ZF cell (zf_flatten.py, recorded beside it)
  --hist      harness/systems-v3/RESULT-correctness-tables-v3-2026-10-01.md   the 3.x cells of record (§G3's HISTORICAL column)
              It also DEFINES the population: §G1's 46 conditions are the ones it does not print as `—`.
  --pt        the A7.2 print-timeout census (one line per root: `<root> files=N hits=H`)
  --pt-p1     its phase-1 complement (`<root> p1files=N p1hits=H`): A7.4 (2) declares that the A7.2 command reads phase 2 only

RULES IT APPLIES (each cited where it prints)
  §G1  46 conditions x 2 models x n = 3 = 276 cells. A condition below 3 is printed SHORT with its count, never dropped (§G2 stop rule).
  §G3  no prediction about direction; the PRIMARY reading is the same-day pair; 3.x is a HISTORICAL column, labelled.
  A6.2 every rate two ways: (a) COUNTED, a wedge is a FAIL in its arm's denominator — the headline where they differ; (b) EXCLUDED,
       the scored cells only. Beside both, per arm: fired · scored · wedge · other.
  A7   the print-timeout hits by model and arm, beside the rates.

MODES
  --print          the RESULT body on stdout
  --check FILE     every derived line of --print must occur in FILE verbatim (a hand edit to a figure turns it red)
  --selftest       fixture arms, each validated by its ability to fail
"""
import argparse, collections, os, re, sys

MODELS = ('argon', 'flash')
MODEL_NAME = {'argon': 'gemini-4-argon-high', 'flash': 'gemini-3.8-flash-high'}
PROBLEMS = ('Crc32', 'LRU', 'FreeList', 'LZW', 'Paxos')
N = 3
WEDGE_DR = ('WEDGED', 'TURN-TIMEOUT')


def read_cells(path):
    rows, hdr = [], None
    for l in open(path):
        if l.startswith('#'):
            continue
        f = l.rstrip('\n').split('\t')
        if hdr is None:
            hdr = f
            continue
        assert len(f) == len(hdr), ('ragged row', f[:2])
        rows.append(dict(zip(hdr, f)))
    return rows


def read_hist(path):
    """{(model3x, problem, field, card, arm): 'k / n …'}; field gf|bf, card none|statement|spec-change, arm plain|salt."""
    h, sec = {}, None
    for l in open(path).read().splitlines():
        if l.startswith('## P1'): sec = ('gf', ('none', 'none', 'statement', 'statement'))
        elif l.startswith('## P2'): sec = ('bf', ('none', 'none', 'statement', 'statement'))
        elif l.startswith('## P3'): sec = ('gf', ('spec-change', 'spec-change'))
        elif l.startswith('## '): sec = None
        if sec and l.startswith('| gemini'):
            c = [x.strip() for x in l.strip('|').split('|')]
            arms = ('plain', 'salt', 'plain', 'salt')
            for card, arm, v in zip(sec[1], arms, c[2:]):
                h[(c[0], c[1], sec[0], card, arm)] = v
    return h


def population(hist):
    """§G1: the conditions the 3.x cells of record carry (not `—`), the same for both 3.x models."""
    by = collections.defaultdict(set)
    for (m, p, fld, card, arm), v in hist.items():
        if v != '—':
            by[m].add((p, fld, card, arm))
    sets = list(by.values())
    assert len(sets) == 2 and sets[0] == sets[1], 'the two 3.x models do not carry the same conditions (§G1 says they do)'
    order = {p: i for i, p in enumerate(PROBLEMS)}
    key = lambda c: ({'gf': 0, 'bf': 1}[c[1]], {'none': 0, 'statement': 1, 'spec-change': 2}[c[2]], order[c[0]], c[3])
    return sorted(sets[0], key=key)


def klass(r):
    """A6.2: a wedge is a NOT-SCORED cell whose turn loop (either phase, extract_legs.py) ended WEDGED or TURN-TIMEOUT."""
    v = r['verdict']
    if v == 'PASS': return 'pass'
    if v == 'FAIL': return 'fail'
    if v == 'NOT-SCORED' and any(w in r['done_reason'] for w in WEDGE_DR): return 'wedge'
    return 'other'


def tally(rs):
    c = collections.Counter(klass(r) for r in rs)
    return dict(fired=len(rs), scored=c['pass'] + c['fail'], p=c['pass'], f=c['fail'], w=c['wedge'], o=c['other'])


def rates(t):
    counted = f"{t['p']} / {t['p'] + t['f'] + t['w']}"
    excluded = f"{t['p']} / {t['p'] + t['f']}"
    return counted, excluded


def fmt_cell(t):
    if not t['fired']:
        return 'not fired'
    c, e = rates(t)
    s = c if c == e else f"{c} (excl. {e})"
    return s + f" · {t['fired']}/{t['scored']}/{t['w']}/{t['o']}"


def pt_tally(pt_lines, p1_lines):
    """A7: hits per (model, arm), phase-2/single-phase (the registered A7.2 command) and the phase-1 complement.
    DISCARDED roots are excluded (A7.4 (1)); a root with files=0 has no client stderr yet and is counted apart."""
    agg = collections.defaultdict(lambda: collections.Counter())
    def parse(root):
        m = re.match(r'cells-(?:l8)?zf-(\w+)-(argon|flash)-(plain|salt)-', root)
        if not m: raise SystemExit('UNPARSED root ' + root)
        return m.group(2), m.group(3)
    for l in pt_lines:
        root, files, hits = l.split()
        if 'DISCARDED' in root: continue
        k = parse(root); n, h = int(files.split('=')[1]), int(hits.split('=')[1])
        if n == 0: agg[k]['nofile'] += 1; continue
        agg[k]['roots'] += 1; agg[k]['roots_hit'] += h > 0; agg[k]['hits'] += h
    for l in p1_lines:
        root, files, hits = l.split()
        if 'DISCARDED' in root: continue
        k = parse(root); n, h = int(files.split('=')[1]), int(hits.split('=')[1])
        if n == 0: agg[k]['p1_nofile'] += 1; continue
        agg[k]['p1_roots'] += 1; agg[k]['p1_roots_hit'] += h > 0; agg[k]['p1_hits'] += h
    return agg


# Conditions CUT by ruling, whole (both arms, both models, n = 0): council 2026-10-20 ④, the conditional cut (AMENDMENT-ZF
# ADDENDUM 4 rule 2), fired by bench's ADA line at Z264's harvest (2026-10-24 23:53). A cut pair is still printed SHORT with its
# count; it does not hold the set PARTIAL. A cut condition with ANY harvested cell refuses: the ruling cut it whole.
# ADDENDUM 4 (the helm, 23:51): wherever a belted verdict is printed, including the result, EACH ROW carries this, so a reader of one
# row meets it. ROW, TOTAL and FAIL lines print belted Z verdicts; the 3.x column on a ROW is historical and was not belted.
VC = 'Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)'
CUT = {('Paxos', 'gf', 'spec-change'): 'CUT by ruling, council 2026-10-20 ④ (ADA at Z264)'}


def derive(cells, hist, pt_lines, p1_lines, cut=CUT):
    pop = population(hist)
    popset = set(pop)
    out = []
    by = collections.defaultdict(list)
    for r in cells:
        k = (r['problem'], r['field'], r['card'], r['arm'])
        assert k in popset, ('a harvested cell outside §G1', r['z'], k)
        assert r['model'] in MODELS, r['model']
        by[(k, r['model'])].append(r)
    for (k, m), rs in by.items():
        reps = collections.Counter(r['rep'] for r in rs)
        assert all(v == 1 for v in reps.values()), ('a replicate harvested twice', k, m, reps)
    fired = len(cells)
    short = [(k, m, len(by[(k, m)])) for k in pop for m in MODELS if len(by[(k, m)]) < N]
    for k, m, n in short:
        assert not (k[:3] in cut and n), ('a CUT condition has harvested cells', k, m, n)
    complete = all(k[:3] in cut for k, m, n in short)
    out.append(f"POPULATION §G1: {len(pop)} conditions x {len(MODELS)} models x n = {N} = {len(pop) * len(MODELS) * N} cells; "
               f"harvested {fired}; SHORT {len(short)} condition-model pairs")
    out.append(f"STATE: COMPLETE — every SHORT pair is a condition CUT by ruling ({len(short)} pairs)" if complete and short else
               'STATE: COMPLETE' if complete else
               'STATE: PARTIAL — the set has not ended; every figure below is a reading of the cells harvested so far, not the RESULT')
    for k, m, n in short:
        out.append(f"SHORT {m:5} {k[0]} {k[1]} {k[2]} {'salt-diet' if k[3] == 'salt' else 'plain'}: {n} of {N}"
                   + (f" ({cut[k[:3]]})" if k[:3] in cut else ''))
    out.append('TABLE problem | field | card | arm | ' + ' | '.join(f"{MODEL_NAME[m]} counted (excl.) · fired/scored/wedge/other" for m in MODELS)
               + ' | 3.x of record (HISTORICAL) gemini-3.1-pro-high · gemini-3.8-flash-high')
    for k in pop:
        cols = [fmt_cell(tally(by[(k, m)])) for m in MODELS]
        h = [hist.get((x,) + k, '?') for x in ('gemini-3.1-pro-high', 'gemini-3.8-flash-high')]
        out.append(f"ROW {k[0]} | {k[1]} | {k[2]} | {'salt-diet' if k[3] == 'salt' else 'plain'} | "
                   + ' | '.join(cols) + f" | {h[0]} · {h[1]} | {VC}")
    for m in MODELS:
        for arm in ('plain', 'salt'):
            t = tally([r for r in cells if r['model'] == m and r['arm'] == arm])
            c, e = rates(t)
            out.append(f"TOTAL {MODEL_NAME[m]} {'salt-diet' if arm == 'salt' else 'plain'}: COUNTED {c} · EXCLUDED {e} · "
                       f"fired {t['fired']} · scored {t['scored']} · wedge {t['w']} · other {t['o']} | {VC}")
    for m in MODELS:
        t = tally([r for r in cells if r['model'] == m])
        c, e = rates(t)
        out.append(f"TOTAL {MODEL_NAME[m]} both arms: COUNTED {c} · EXCLUDED {e} · fired {t['fired']} · wedge {t['w']} · other {t['o']} | {VC}")
    for r in sorted((r for r in cells if klass(r) in ('wedge', 'other')), key=lambda r: int(r['z'][1:])):
        out.append(f"NOT-SCORED {r['z']} {r['cid']} {r['model']} {r['problem']} {r['field']} {r['card']} "
                   f"{'salt-diet' if r['arm'] == 'salt' else 'plain'} r{r['rep']}: {klass(r).upper()} ({r['done_reason']}; end {r['end']})")
    for r in sorted((r for r in cells if r['verdict'] == 'FAIL'), key=lambda r: int(r['z'][1:])):
        out.append(f"FAIL {r['z']} {r['cid']} {r['model']} {r['problem']} {r['field']} {r['card']} "
                   f"{'salt-diet' if r['arm'] == 'salt' else 'plain'} r{r['rep']}: {r['tests']} | {VC}")
    agg = pt_tally(pt_lines, p1_lines)
    legs = collections.Counter((r['model'], r['arm']) for r in cells)
    for m in MODELS:
        for arm in ('plain', 'salt'):
            a = agg[(m, arm)]
            out.append(f"A7 {MODEL_NAME[m]} {'salt-diet' if arm == 'salt' else 'plain'}: final-phase roots {a['roots']} · with a hit "
                       f"{a['roots_hit']} · hits {a['hits']} | spec-change phase 1 roots {a['p1_roots']} · with a hit {a['p1_roots_hit']} · "
                       f"hits {a['p1_hits']} | roots with no stderr yet {a['nofile'] + a['p1_nofile']} | harvested legs {legs[(m, arm)]}")
    tr = collections.Counter((r['model'], r['arm']) for r in cells if r['trunc'] == 'TRUNC')
    out.append('TRUNCATED-ROW cells (a TRUNCATED score row beside the verdict): '
               + ' · '.join(f"{MODEL_NAME[m]} {'salt-diet' if a == 'salt' else 'plain'} {tr[(m, a)]}" for m in MODELS for a in ('plain', 'salt')))
    em = collections.Counter((r['model'], r['arm']) for r in cells
                             if r['empty_final'] not in ('0',) or r['empty_p1'] not in ('0', '-'))
    out.append('EMPTY-TURN cells (>= 1 turn with no output, either phase): '
               + ' · '.join(f"{MODEL_NAME[m]} {'salt-diet' if a == 'salt' else 'plain'} {em[(m, a)]}" for m in MODELS for a in ('plain', 'salt')))
    unread = [r['z'] for r in cells if 'UNREAD' in (r['empty_final'] + r['empty_p1'] + r['done_reason'])]
    out.append(f"UNREAD fields: {len(unread)}" + (f" ({' '.join(unread)})" if unread else ''))
    return out, complete


PROSE = """
# §0 · WHAT THIS FILE IS
The desk ZF set (AMENDMENT-ZF-gemini4-argon-2026-10-13.md): gemini-4-argon-high beside its same-day control gemini-3.8-flash-high on the
pilot's 46 conditions at n = 3 (§G1). Every line in the code block is printed by `harness/systems-v3/zf_result.py --print` from the
inputs it names; `--check` proves this file still carries every one of them verbatim.

# §1 · HOW TO READ THE TABLE
- Each cell is `COUNTED (excl. EXCLUDED) · fired/scored/wedge/other` (A6.2). COUNTED makes a wedge a FAIL in its arm's denominator and is the
  headline wherever the two differ, because it is the reading that goes against the arm that wedges. `other` is a NOT-SCORED cell that did not
  wedge; each one is listed by name.
- The PRIMARY comparison is a row's two model columns, fired adjacent in time on one export (§G1, §G3). The last column is HISTORICAL: the 3.x
  cells of record, a patchwork of levels and harness versions (§G4 1–2), and its Pro figures have no same-day counterpart (§G4 4).
- No p-value, no direction, and no claim that the method helps or hurts (§G3).

# §2 · LIMITS THAT RIDE WITH EVERY RATE
1. **A7, the per-turn print timeout binds salt-diet.** The `A7` lines give hits by model and arm. The final-phase figures are the A7.2 command;
   the phase-1 figures are its complement, since A7.4 (2) declares that the A7.2 command reads phase 2 only. A hit says the clock fired.
   Whether a hit changed a verdict is NOT MEASURED (A7.4 (3)). A7 counts ROOTS on the run box; the table counts HARVESTED LEGS, printed
   last on each A7 line. A root whose leg has not yet harvested (a cell in flight at the census) is in A7 and not in the table.
2. **§G4.** The historical column confounds model with harness, client and fence (§G4 1–3). The control is a Flash model, never Pro (§G4 4).
3. **§G5.** Nothing about Gemini 4 against 3.x in general, the other two effort variants, or the O29 qualification.
4. **TRUNCATED-ROW and EMPTY-TURN counts** are printed by arm because both are arm-correlated readings in this campaign (A6, A7). No ZF
   row carries a cause for an empty turn (A6.1).
5. **No token figure is reported here.** The chain's per-leg §G2 reads carry them; on the bus, 4 of the 251 §G2 posts parsed read the
   meter control FAIL with sub-agent tokens UNMEASURED (Z028 · Z172 · Z240 · Z263). Any token figure quoted from this set carries that
   beside it. No rate in this file reads a token.
"""


def selftest(cells, hist, pt, p1):
    ok, n = 0, 0
    def arm(name, cond):
        nonlocal ok, n
        n += 1; ok += bool(cond)
        print(('PASS ' if cond else 'FAIL ') + name)
    base, _ = derive(cells, hist, pt, p1)
    def run(cs):
        try: return derive(cs, hist, pt, p1)[0]
        except (AssertionError, SystemExit) as e: return ['RAISED ' + str(e)]
    def ln(o, pre): return [l for l in o if l.startswith(pre)]
    # 1 a wedge moves COUNTED and not EXCLUDED
    c2 = [dict(r) for r in cells]; i = next(j for j, r in enumerate(c2) if r['verdict'] == 'PASS' and r['model'] == 'argon' and r['arm'] == 'plain')
    c2[i].update(verdict='NOT-SCORED', done_reason='WEDGED')
    t0 = ln(base, 'TOTAL gemini-4-argon-high plain')[0]; t1 = ln(run(c2), 'TOTAL gemini-4-argon-high plain')[0]
    m0 = re.search(r'COUNTED (\d+) / (\d+) · EXCLUDED (\d+) / (\d+)', t0).groups(); m1 = re.search(r'COUNTED (\d+) / (\d+) · EXCLUDED (\d+) / (\d+)', t1).groups()
    arm('A6.2 a wedge is a FAIL in COUNTED, absent from EXCLUDED',
        int(m1[0]) == int(m0[0]) - 1 and m1[1] == m0[1] and int(m1[3]) == int(m0[3]) - 1)
    # 2 a NOT-SCORED that did not wedge is OTHER, never a wedge
    c3 = [dict(r) for r in cells]; c3[i].update(verdict='NOT-SCORED', done_reason='LANDED')
    arm('a NOT-SCORED non-wedge is OTHER', any('OTHER (LANDED' in l for l in run(c3)))
    # 3 a dropped cell makes its condition SHORT, by name
    c4 = [r for j, r in enumerate(cells) if j != i]
    arm('a missing cell prints SHORT, never vanishes', any(l.startswith('SHORT argon') for l in run(c4)) and
        any(l.startswith('STATE: PARTIAL') for l in run(c4)))
    # 4 a duplicate replicate refuses
    arm('a replicate harvested twice refuses', run(cells + [dict(cells[0])])[0].startswith('RAISED'))
    # 5 a cell outside §G1 refuses
    c5 = [dict(r) for r in cells]; c5[0].update(problem='Paxos', field='gf', card='statement')
    arm('a cell outside the 46 refuses', run(c5)[0].startswith('RAISED'))
    # 6 the population is 46 and matches §G1
    arm('§G1 population is 46', ln(base, 'POPULATION')[0].startswith('POPULATION §G1: 46 conditions'))
    # 7 the phase-1 complement moves the A7 phase-1 column only
    p1b = [l.replace('p1hits=0', 'p1hits=7', 1) if 'argon-plain' in l and 'p1files=1' in l and 'p1hits=0' in l else l for l in p1]
    a0 = ln(base, 'A7 gemini-4-argon-high plain')[0]; a1 = ln(derive(cells, hist, pt, p1b)[0], 'A7 gemini-4-argon-high plain')[0]
    arm('A7 phase-1 hits counted apart from the registered command', a0.split('|')[0] == a1.split('|')[0] and a0 != a1)
    # 8 --check reddens on a one-character edit of a figure
    body = render(base)
    t = ln(base, 'TOTAL')[0]; bad = body.replace(t, t.replace('COUNTED ', 'COUNTED 1', 1))
    arm('--check reddens on an edited figure', check_text(base, bad) != [] and check_text(base, body) == [])
    # 9 the registered cut makes a set whose only SHORT pairs are cut read COMPLETE; with no cut the same set is PARTIAL
    st_cut = ln(base, 'STATE')[0]; st_nocut = ln(derive(cells, hist, pt, p1, cut={})[0], 'STATE')[0]
    only_cut = all('CUT by ruling' in l for l in ln(base, 'SHORT '))
    arm('a set SHORT only on cut conditions is COMPLETE; without the cut it is PARTIAL',
        (st_cut.startswith('STATE: COMPLETE') and st_nocut.startswith('STATE: PARTIAL')) if only_cut else st_cut.startswith('STATE: PARTIAL'))
    # 10 a cut condition that holds a harvested cell refuses
    c6 = [dict(r) for r in cells]; c6[0].update(problem='Paxos', field='gf', card='spec-change', rep='1')
    arm('a cell in a CUT condition refuses', run(c6)[0].startswith('RAISED'))
    # 11 every line that prints a belted Z verdict carries the verdict-channel limit (ADDENDUM 4)
    vlines = [l for l in base if l.startswith(('ROW ', 'TOTAL ', 'FAIL '))]
    arm('every ROW, TOTAL and FAIL line carries the verdict-channel limit', vlines and all(l.endswith(VC) for l in vlines))
    print(f"SELFTEST {ok}/{n}")
    return ok == n


def render(lines):
    return '```\n' + '\n'.join(lines) + '\n```\n'


def check_text(lines, text):
    return [l for l in lines if l not in text.splitlines()]


def main():
    here = os.path.dirname(os.path.abspath(__file__)); repo = os.path.dirname(os.path.dirname(here))
    ap = argparse.ArgumentParser()
    ap.add_argument('--cells', default=os.path.join(repo, 'evidence/zf-result/zf-cells.tsv'))
    ap.add_argument('--hist', default=os.path.join(here, 'RESULT-correctness-tables-v3-2026-10-01.md'))
    ap.add_argument('--pt', default=os.path.join(repo, 'evidence/zf-result/pt-census.txt'))
    ap.add_argument('--pt-p1', default=os.path.join(repo, 'evidence/zf-result/pt-census-p1.txt'))
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--print', action='store_true'); g.add_argument('--check'); g.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    cells, hist = read_cells(a.cells), read_hist(a.hist)
    pt, p1 = open(a.pt).read().splitlines(), open(a.pt_p1).read().splitlines()
    if a.selftest:
        return 0 if selftest(cells, hist, pt, p1) else 1
    lines, complete = derive(cells, hist, pt, p1)
    if a.print:
        sys.stdout.write(render(lines) + PROSE)
        return 0
    miss = check_text(lines, open(a.check).read())
    for l in miss: print('MISSING ' + l)
    print(('CHECK GREEN' if not miss else 'CHECK RED') + f": {len(lines)} derived lines, {len(miss)} missing")
    return 0 if not miss else 1


if __name__ == '__main__':
    sys.exit(main())
