#!/usr/bin/env python3
"""nca_result_gen.py — writes blocks NCA and WCA's four RESULT files, one per block x model (NCA §NCA8 and WCA §WCA8: "a result of record
per model"), into <repo>/harness/systems-v3/, and this directory's cells.tsv (the per-cell table of record, 96 rows).
  python3 nca_result_gen.py --write <repo>   -> writes the four files and cells.tsv
  python3 nca_result_gen.py --check <repo>   -> rc 0 iff each file carries EVERY --summary line of its block verbatim and cells.tsv equals
                                                the table nca_cells_gen.py prints now (rc 1 names what is missing or moved)
Every figure block is nca_cells_gen.py --summary's own lines for that block, selected by prefix; nothing in a code block is typed. The prose
is the lead's: it cites (registration sections, addenda, bus offsets, files) and carries no figure that is not in a block above it, except
where it names a cell or quotes a record by its offset."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nca_cells_gen as g

DATE = '2026-11-28'
REG = {'NCA': 'AMENDMENT-O37-blockNCA-specchange-agy-2026-11-23.md', 'WCA': 'AMENDMENT-O37-blockWCA-wht-ntt-specchange-agy-2026-11-23.md'}
MODEL = {'flash': 'gemini-3.8-flash-high', 'argon': 'gemini-4-argon-high'}
EVID = 'evidence/blockNCA-WCA-result-2026-11-24'


def fname(b):
    blk, m = b.split('-')
    return 'RESULT-gemini-block%s-%s-%s.md' % (blk, m, DATE)


def mine(b, S):
    return [l for l in S if l.startswith(b + ' ') or l.startswith(b + ':')]


def pick(b, S, pred):
    return '```\n' + '\n'.join(l for l in mine(b, S) if pred(l[len(b):])) + '\n```'


def is_cond(t):   # a condition line is '<block> <Problem> <arm>: ...'; 'phase 2:', 'phase 1:' and 'prediction verdicts:' also have two words
    return re.match(r' [A-Za-z0-9]+ (plain|salt-diet): ', t) is not None


NOTES = {
'NCA-flash': dict(
what='''- **Sources: block NA's Flash cells of record, copied** under §NCA2's Flash rule (a copy owes no fresh G baseline; its source was made
  eligible by the census, ADDENDUM 1). **Two cells are FRESH**, where NA had no eligible source (§NCA2): BinomialHeap · salt-diet #3
  (`cells-nca-binomialheap-flash-salt-r3`; NA's `nabhfs03` never landed) and LinearScan · salt-diet #2 (`cells-nca-linearscan-flash-salt-r2`;
  NA's `nalsfs202` failed its own G suite). Both fresh cells LANDED phase 1, and both G baselines on landed-1 read short of a full pass, so each
  is a **REACH LOSS under NC rule 4**: its phase 2 is listed in §2 and never counted (one attempt each, never re-run).
- **Two clients per copy** (§NCA9, §H-CLIENT: declared, and not a treatment): every phase 2 ran on the pinned client
  `62f2102784bb74b7`; each copy's phase 1 is NA's, on the client NA ran (the `clients` line). The two fresh cells ran both phases on the pin.
- **The hook.** The 34 copies carry the replaced web-deny hook whose hash is ADDENDUM 1's census value (`a6e064e307a8651d`); the two fresh cells
  were built by the release export with its own hook (`FRESH` in the table).
- **Web.** Four copies continue WEB-SERVED sources (census ADDENDUM 47): LinearScan · plain #1–#3 (`nalsfp201`–`nalsfp203`) and LinearScan ·
  salt-diet #3 (`nalsfs203`). Each keeps its verdict and leaves every comparison exactly as its source did (§NCA6 item 5). No phase 2 was
  served a search: the 11-20 census instrument (`web_brain_census.py`, unchanged) read every brain transcript of every standing cell
  (`web_census.tsv`, `web_transcripts.tsv`); its one `search_web` call in this block, `naaefp02`'s, was DENIED. Its positive control on the
  same box read NA's `nalsfp201`–`nalsfp203` at 7, 16 and 22 served, the 11-20 figures.
- **CTL-READ: `naaefs01`** (AES · salt-diet #1) read the harness's `ctl/` in its phase 2 (`ctl_census.tsv`, 8 calls). The lead's ruling (bus
  offset 110,731,568): the verdict stands, the cell leaves every comparison, and its briefing and P-PERSIST read UNMEASURED.''',
correct='''- **Liveness: five of six cells fail exactly one clause test each, with 0 regressions** (the bracket). NCA ADDENDUM 4: §NCA6 item 4 (the
  Liveness card amended before any later Liveness run) was not met by the release, so the six Flash Liveness cells stand as they fell (the
  helm's CONCUR, bus offset 110,631,802). These figures carry census ADDENDUM 46 NOTE 1 and are never read as a premium. Which clause test
  fails is not read here (the receipt counts failures; it does not name them).
- **LinearScan has no comparison:** its plain arm's three cells all continue WEB-SERVED sources, so 0 of 3 are in comparisons. The salt-diet
  cell `nalsfs203` (truncated, 13 of 14) also continues a WEB-SERVED source.''',
cost='''T is the agy meter's token total for phase 2; wall is phase 2's turn-loop wall. A rep prints only where its cell is COUNTED; a value
marked `*` leaves comparisons (§1), and a pair counts only when both its cells are in comparisons (kent's read of #479). A sign, never a
premium (§NCA5: no premium is registered), and no magnitude is claimed.''',
pred='''- **(i)** binds the ELIGIBLE count for Flash (§NCA5): salt-diet's is lower, by the two fresh cells' G baselines. **Holds.**
- **(ii)** compares the arms within a condition, so it reads cells IN COMPARISONS only; LinearScan gives no comparison (above). **Holds,
  trivially, at 0 ≥ 0** in all five conditions that give one: no cell in comparisons was cut in either arm. The one counted cell with cut
  turns, `nalsfs203` (LinearScan · salt-diet #3), leaves comparisons with its WEB-SERVED source. So (ii) was not tested in the direction it
  was registered to watch.
- **(iii)** CELL-KILLED binds no cell. **Holds.**'''),
'NCA-argon': dict(
what='''- **36 FRESH cells, both phases in one cell** (§NCA7 fork 1's default: argon has no source), level 8's one-cell form, every phase on the
  pinned client `62f2102784bb74b7`.
- **Two 503 discards** (the `attempts` line in this directory's README): LinearScan plain #2 and salt-diet #2 stand at attempt 2. A discarded
  attempt is a whole attempt, never pooled and never a row (L8 ADDENDUM 2 §A2.2).
- **`cells-nca-liveness-argon-salt-r1` was not reached.** Its subject deleted its own `landed-1` tag and re-landed inside phase 1, so the
  §A9.2 landed gate refused phase 2 (`tag=ABSENT`; the receipt reads INCOMPLETE because no phase 2 ran). The lead's ruling (a), bus offset
  111,293,855: a REACH LOSS. Liveness · salt-diet is n = 2.
- **`cells-nca-maxflow-argon-plain-r1` is NOT SCORED (harness).** Phase 1 LANDED; phase 2 was refused at launch by the launcher's brain
  check; ADDENDUM 5's re-fire route refused on a real copy, driven at zero spend. NCA ADDENDUM 6: phase 2 NOT-SCORED (harness), and
  MaxFlow · plain is n = 2 of 3.
- **Re-landings inside phase 1** (ADDENDUM 5 §A5.3): the hand's 21 extra G readings at P1^ each read ELIGIBLE and agree with the registered
  landed-1 reading (bus offset 112,527,193); no count moves.
- **Web.** A fresh cell's two phases share one brain, so its own reading covers both (`OWN:` in the table). Every cell read CLEAN.''',
correct='''- **Liveness · salt-diet: both counted cells fail one clause test each, with 0 regressions**; Liveness · plain passes 3 of 3. The
  clause figures carry census ADDENDUM 46 NOTE 1 (NCA ADDENDUM 4) and are never read as a premium.
- **Every counted cell that was truncated or cut is in salt-diet** (AES, LinearScan, Liveness): the AES and LinearScan ones PASS, and the
  Liveness ones fail one clause test each.''',
cost='''T is the agy meter's token total for phase 2; wall is phase 2's turn-loop wall. A rep prints only where its cell is COUNTED, and a pair
counts only when both its cells are in comparisons. A sign, never a premium (§NCA5), and no magnitude is claimed.''',
pred='''- **(i)** binds REACH for argon (§NCA5): salt-diet's is lower, by `cells-nca-liveness-argon-salt-r1`. **Holds.** (`cells-nca-maxflow-argon-plain-r1`
  was reached: its §A9.2 gate fired, and the harness refused after it.)
- **(ii)** **Holds in every condition.** Salt-diet was cut more often than plain in AES, LinearScan and Liveness, and tied at 0 in the rest.
- **(iii)** CELL-KILLED binds no cell. **Holds.**'''),
'WCA-flash': dict(
what='''- **Sources: block WA's 12 Flash cells of record, copied** (§WCA2: NCA §NCA2's Flash rule; all 24 WCA sources were eligible, ADDENDUM 3).
- **Two exports and two clients per pair** (§WCA6 item 3): each source ran phase 1 on WA's export `6413289d` and its client, before WA
  ADDENDUM 3's per-cell environment fix and ADDENDUM 5's `agentMode ""`; each phase 2 ran on the release export and the pinned client. So the
  client's own sandbox setting differs between a pair's phases. Nothing here compares a Flash figure with an argon one.
- **The order** was §WCA4's: the tripwire `T-WCA-F` (NTT · salt-diet #1) first, read by the lead at the object (bus offset 112,541,157), then the
  Flash rest by one chain (the hand's completion post, bus offset 112,670,115).
- **Web.** Every source read CLEAN in the 11-20 census, and no phase 2 was served a search.''',
correct='''- **Every cell passes the withheld B/ suite in full, both problems and both arms.** Both conditions of each problem are at CEILING, so this
  block says nothing about a difference between the arms in pass rate (UNRESOLVED-BY-CEILING).''',
cost='''T is the agy meter's token total for phase 2; wall is phase 2's turn-loop wall. A rep prints only where its cell is COUNTED, and a pair
counts only when both its cells are in comparisons. A sign, never a premium (§WCA5 carries NCA §NCA5), and no magnitude is claimed.''',
pred='''- **(i)** "lower for salt-diet": **MISS**, at a tie. Every source was eligible by the census, so neither arm lost a cell before phase 2.
- **(ii)** "salt-diet's cut-turn incidence ≥ plain's": no counted cell was cut in either arm. **Holds, trivially, at 0 ≥ 0**, so (ii) was not
  tested in the direction it was registered to watch.
- **(iii)** CELL-KILLED binds no cell. **Holds.**'''),
'WCA-argon': dict(
what='''- **Sources: block WA's 12 Pro-slot cells of record (gemini-4-argon-high), copied** (§WCA2; all 24 WCA sources were eligible, ADDENDUM 3).
  Each source ran phase 1 on WA Pro's export `3fd5edf1`; each phase 2 ran on the release export and the pinned client (§WCA6 item 3).
- **The order** was §WCA4's: the tripwire `T-WCA-A` (NTT · salt-diet #1) first, read by the lead at the object (bus offset 112,695,555), then
  the argon rest by one chain. After each cell, the chain's stop check judged the lead's five standing conditions. Argon is removed from the
  client on 2026-11-30, so a cell not fired by 2026-11-30 00:00Z is unreached, never re-cut.
- **One stop, lifted.** The stop check stopped the chain after WHT · plain #2 (`wawap201`) on one AGY_ERROR (bus offset 112,911,273). The lead
  read the cell at the object (bus offset 112,917,943): none of the five conditions held. The error was written after the cell's end, by its
  orphaned client, and the persistence probe had been answered (the harness-side paragraph below). The ruling was CONTINUE, and the chain went
  on (bus offset 112,922,934).
- **Web.** Every source read CLEAN in the 11-20 census, and no phase 2 was served a search.''',
correct='''- **Every counted cell passes the withheld B/ suite in full, both problems and both arms.** Both conditions of each problem are at CEILING, so this
  block says nothing about a difference between the arms in pass rate (UNRESOLVED-BY-CEILING).
- **The counted cells whose launcher `run_verdict` reads `ERROR(NO-COMMAND-PROVEN-OK)`** (the `harness-side` line gives their number) are
  scored like any other cell, and each passes in full (`cells.tsv`, columns `p2_run_verdict` and `verdict`).''',
cost='''T is the agy meter's token total for phase 2; wall is phase 2's turn-loop wall. A rep prints only where its cell is COUNTED, and a pair
counts only when both its cells are in comparisons. A sign, never a premium (§WCA5 carries NCA §NCA5), and no magnitude is claimed.''',
pred='''- **(i)** "lower for salt-diet": **MISS**, at a tie. Every source was eligible by the census (ADDENDUM 3), so neither arm lost a cell before
  phase 2.
- **(ii)** "salt-diet's cut-turn incidence ≥ plain's": no counted cell was cut in either arm. **Holds, trivially, at 0 ≥ 0**, so (ii) was not
  tested in the direction it was registered to watch.
- **(iii)** CELL-KILLED binds no cell. **Holds.**'''),
}

HARNESS = '''- **Harness-side events** (the `harness-side` line; `cells.tsv` columns `p2_results` … `p2_harness`). `run_verdict` is the launcher's
  own word on its phase-2 SERVED line; `ERROR(NO-COMMAND-PROVEN-OK)` marks a cell whose code is still scored, so §2's verdicts are the
  receipts' either way. `P-PERSIST` is the registered reader's (`agy_probes_v3.py`). Beside it, **as a hand read and not the registered
  instrument**, `nca_facts.py` reads whether the subject gave its ack token (validated against `launch.log`'s hash) AFTER the probe, in its own
  transcript or stream. **`PROBE-CUT-AT-EXIT-TIMEOUT`** names a cell that the reader read `indeterminate` although its subject DID answer the
  probe. The turn loop (`agy_turnloop_v3.py` at export `88b63df9`, lines 228-233 and 301-326) writes the probe after the FIRST opening
  result, so the second opening turn's result satisfied the probe's wait, and `--exit-timeout` (line 869) killed a subject still working
  after it had answered. L8 §A9.5's persistence cap did not bind. In each such cell the code landing predates the probe (read by hand: bus
  @112,925,340 for `cells-nca-linearscan-argon-plain-r1` and `cells-wa-wht-argon-plain-r2-wcacp2`, bus @112,991,853 for
  `cells-wa-wht-argon-salt-r3-wcacp3`), so no verdict or count moves. Their cost figures do: the kill ended a subject still working, so
  each such cell's phase-2 T and wall are FLOORS, and §3 does not mark them. Where a cut cell is the smaller side of a printed
  `salt-diet > plain` pair (the first two named above), that pair's sign is not established by its figures; where it is the larger
  (`cells-wa-wht-argon-salt-r3-wcacp3`), the sign stands (kent's read of #479, LOW R3). The turn-loop fix belongs to the next export;
  every cell of record ran this one (bus @112,917,943).'''

CANNOT = {
'NCA': '''§NCA8, carried: no magnitude or effect size; nothing Flash-versus-argon or Claude-versus-agy; nothing about a spec-change reached from a
phase 1 that did not land; nothing about a gemini-3.1-pro-high condition; nothing outside §NCA1. NC's reading rules (L8 §M7, NC §C8) are
carried, so every premium is UNRESOLVED-UNDERPOWERED. §NCA6 item 4 (one author for the six B/ suites, who is the lead) is carried. Nothing
here says whether the salt method helps or hurts. Any public sentence, and any claim about the method, is the Captain's.''',
'WCA': '''§WCA8 (NCA §NCA8, §NCA9 and §NCA10 carried, for NTT and WHT): no magnitude; nothing about gemini-3.1-pro-high; nothing Flash-versus-argon
or Claude-versus-agy. §WCA6 item 6: one author built both tasks and both B/ suites and leads this block, and NTT's reference proves less than
WHT's. Nothing here says whether the salt method helps or hurts. Any public sentence is the Captain's.''',
}


def doc(b, S):
    blk, m = b.split('-')
    n = NOTES[b]
    other = fname('%s-%s' % (blk, 'argon' if m == 'flash' else 'flash'))
    sec = '§NCA8' if blk == 'NCA' else '§WCA8'
    probs = 'the six block-N problems' if blk == 'NCA' else 'WHT and NTT'
    return '\n'.join([
        '# RESULT — O37 block %s, %s COLUMN · the agy lane × %s × greenfield → spec-change × extras=none · n = 3 · %s' % (blk, m.upper(), probs, MODEL[m]),
        '### bench (lead), %s, on the hand\'s files (gemini). **%s: "a result of record per model": this is %s\'s; the other is `%s`.**' % (DATE, sec, m.capitalize(), other),
        '## 📌 The registration is `%s`%s.' % (REG[blk], ' (§NCA0–§NCA10; ADDENDA 1–6)' if blk == 'NCA' else ' (§WCA0–§WCA8; ADDENDA 1–3), which carries block NCA by citation'),
        '## 📌 The per-cell table of record is `%s/cells.tsv` (96 rows: both blocks, both models), printed by `nca_cells_gen.py` beside it from the hand\'s score receipts, `cell_facts.json` (read on the run box by `nca_facts.py`), `ctl_census.tsv` and `web_census.tsv`. Its README says how each is made.' % EVID,
        '## ⛔ Every figure line in a code block below is printed by `nca_cells_gen.py --summary`, and `nca_result_gen.py --check` asserts that this file carries every line of its block verbatim. Bus offsets in the prose are citations to where a reader can look, not measurements.',
        '', '---', '# §1 · WHAT RAN, AND ON WHAT',
        pick(b, S, lambda t: t.startswith(':') or t.startswith(' phase 2:') or t.startswith(' clients:') or t.startswith(' web:') or t.startswith(' phase 1:')
             or t.startswith(' harness-side')),
        n['what'], HARNESS, '', '---',
        '# §2 · CORRECTNESS, VERIFIED FIRST (the withheld B/ suite; PASS is the receipt\'s word: TESTS all passed, 0 REGRESSIONS failed, 0 CLAUSE_TESTS failed)',
        'The bracket lists each counted cell\'s TESTS (passed/total), REGRESSIONS and CLAUSE_TESTS (failed/total), in cell order. A cell IN COMPARISONS is counted and does not leave comparisons (§1).',
        pick(b, S, lambda t: is_cond(t) or t.startswith(' FULL PASS')),
        n['correct'], '', '---',
        '# §3 · COST, AS A SIGN ONLY',
        pick(b, S, lambda t: 'phase-2 T by rep' in t or 'phase-2 wall_s by rep' in t),
        n['cost'], '', '---',
        '# §4 · THE REGISTERED PREDICTIONS (NCA §NCA5 (i)–(iii)%s); A MISS IS A RESULT' % (', carried by §WCA5' if blk == 'WCA' else ''),
        pick(b, S, lambda t: t.startswith(' predictions:') or t.startswith(' prediction verdicts:')),
        n['pred'], '', '---',
        '# §5 · WHAT THIS RESULT CANNOT ESTABLISH', CANNOT[blk], ''])


README = """# Blocks NCA and WCA — result evidence (bench, 2026-11-28)
The four RESULT files (`harness/systems-v3/RESULT-gemini-block{NCA,WCA}-{flash,argon}-2026-11-28.md`) quote figure lines printed from this
directory. Each input, how it is made, and what it does not see:

- **`manifests/`** — byte copies of the hand's four chain manifests (`cmp` EQUAL to the hand's at each re-fetch). They ARE the population
  (96 rows): a cell not yet scored reads UNSCORED, never absent.
- **`cell_facts.json`** — `nca_facts.py`, run on the run box by `nca_cells_gen.py --fetch HOST`, read-only, over the 96 rows: each row's
  standing attempt (a 503 re-queue is `<root>-a<k>`), its cell's own `ctl/` (meters, turn loops, end markers, launch lines, copy record),
  the phase-1 record the wave set aside (`<root>/_aside/<id>/phase1/ctl/`, or the cell's own `ctl/` when no phase 2 ran), the §A9.2 gate
  lines, a fresh cell's G baseline, and the P-PERSIST probe: the registered reader's word (`ctl/agy-probes-2.tsv`) beside whether the
  subject's validated ack token follows the probe in its own brain transcript or stream (a hand read, 2026-11-28). A value it cannot read is UNREAD, never blank or zero.
- **Score receipts** — the hand's (`score_wave_v3.sh`, one per cell), in its run directory on the lead's box, NOT in this repository (they
  name paths in a local-only tree). Each row's `score_receipt` column names the receipt it was read from; two receipts for one root are
  admitted only when they agree on every scored field (both are cited), and two that disagree refuse. WCA's sit in `wca-*-harvest*` dirs.
- **G receipts** — the hand's harvest ROW lines (`gbase.sh`'s own line with its rc), cross-checked against the box's G log per fresh cell;
  a disagreement refuses.
- **ctl census** — `ctl_census_join_input.tsv` (`--join-input`: a copy read in its standing root AND its source's family, a fresh cell in
  its standing root) → main's `evidence/o37-agy-ctl-read-census-2026-11-25/ctl_census.py` on the run box (`--fetch-ctl`: its `--selftest`
  first, then `--join`) → `ctl_census_join.tsv` + `ctl_census_hits.tsv` → `ctl_census.tsv` (`--derive-ctl`: manifest roots, reads =
  `ctl_named`, the paths its CTL hits name; an ambiguous id refuses). Its LIMIT: NONE-NAMED is a lower bound on contact with `ctl/`.
- **web census** — `web_census.tsv` + `web_transcripts.tsv` (`--fetch-web`): main's `evidence/o37-agy-web-served-2026-11-20/web_brain_census.py`,
  unchanged, run on the run box over a farm of symlinks to the standing roots. A cell with no brain transcript is UNMEASURED, never CLEAN.
  A copy's SOURCE state is the 11-20 census's `join.tsv`, keyed by (root, id).
- **`cells.tsv`** — the per-cell table of record, `nca_result_gen.py --write`; `--check` asserts it equals the table printed now, and that
  each RESULT file and this README carry every figure line of their own.
- **`nca_gen_selftest.sh`** — every refusal and every reading rule above driven on fixtures (the real receipt root is read, never written);
  each arm added since 2026-11-28 was shown to fail on a mutant of the rule it guards.

The population-wide lines (`nca_cells_gen.py --summary`, the lines no block owns):
"""


def readme_lines(S):
    blocks = ('NCA-flash', 'NCA-argon', 'WCA-flash', 'WCA-argon')
    return [l for l in S if not any(l.startswith(b + ' ') or l.startswith(b + ':') for b in blocks)]


CENSUS = os.path.join('harness', 'systems-v3', 'CENSUS-full-matrix-2026-09-14.md')


def census_lines(rows):
    """The census ADDENDUM's figure lines: per block x model, each condition's n = its COUNTED cells (a REACH-LOSS(G), INCOMPLETE or
    NOT-SCORED phase 2 is never counted). DONE needs n >= 1; a condition at n = 0 is named, never counted DONE (census ADDENDUM 46 §AQ1)."""
    L = []
    for b in ('NCA-flash', 'NCA-argon', 'WCA-flash', 'WCA-argon'):
        bb = [r for r in rows if r['block'] == b]
        cn = {}
        for r in bb:
            cn.setdefault((r['problem'], r['arm']), 0)
            cn[(r['problem'], r['arm'])] += r['counted'] == 'yes'
        by = {}
        for c, n in sorted(cn.items()):
            by.setdefault(n, []).append('%s %s' % c)
        blk, m = b.split('-')
        L.append('block %s, %s: %d conditions · %s · cells counted %d of %d' % (
            blk, MODEL[m], len(cn),
            ' · '.join('n=%d %d%s' % (n, len(v), (' [%s]' % ', '.join(v)) if n < 3 else '') for n, v in sorted(by.items(), reverse=True)),
            sum(r['counted'] == 'yes' for r in bb), len(bb)))
    return L


def main(a):
    if len(a) != 2 or a[0] not in ('--write', '--check'):
        sys.exit(__doc__)
    repo = a[1]
    rows = g.table()
    S = g.summary(rows)
    tab = '\t'.join(g.COLS) + '\n' + ''.join('\t'.join(str(r[c]) for c in g.COLS) + '\n' for r in rows)
    bad = 0
    for b in ('NCA-flash', 'NCA-argon', 'WCA-flash', 'WCA-argon'):
        p = os.path.join(repo, 'harness', 'systems-v3', fname(b))
        if a[0] == '--write':
            open(p, 'w').write(doc(b, S))
            print('wrote %s (%d figure lines)' % (os.path.relpath(p, repo), len(mine(b, S))))
        else:
            body = open(p).read() if os.path.exists(p) else ''
            miss = [l for l in mine(b, S) if l not in body]
            for l in miss:
                print('MISSING %s: %s' % (fname(b), l))
            print('check %s: %d of %d figure lines present' % (fname(b), len(mine(b, S)) - len(miss), len(mine(b, S))))
            bad += bool(miss)
    rp = os.path.join(HERE, 'README.md')
    if a[0] == '--write':
        open(rp, 'w').write(README + '```\n' + '\n'.join(readme_lines(S)) + '\n```\n')
        print('wrote %s/README.md (%d population lines)' % (EVID, len(readme_lines(S))))
    else:
        body = open(rp).read() if os.path.exists(rp) else ''
        miss = [l for l in readme_lines(S) if l not in body]
        for l in miss:
            print('MISSING README.md: %s' % l)
        print('check README.md: %d of %d population lines present' % (len(readme_lines(S)) - len(miss), len(readme_lines(S))))
        bad += bool(miss)
    C = census_lines(rows)
    if a[0] == '--write':
        print('census lines (ADDENDUM 53 quotes them; --check asserts them in the census):')
        print('\n'.join(C))
    else:
        body = open(os.path.join(repo, CENSUS)).read()
        miss = [l for l in C if l not in body]
        for l in miss:
            print('MISSING census: %s' % l)
        print('check census: %d of %d lines present' % (len(C) - len(miss), len(C)))
        bad += bool(miss)
    cp = os.path.join(HERE, 'cells.tsv')
    if a[0] == '--write':
        open(cp, 'w').write(tab)
        print('wrote %s/cells.tsv (%d rows)' % (EVID, len(rows)))
    else:
        same = os.path.exists(cp) and open(cp).read() == tab
        print('check cells.tsv: %s' % ('EQUAL to the table printed now' if same else 'DIFFERS from the table printed now'))
        bad += not same
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
