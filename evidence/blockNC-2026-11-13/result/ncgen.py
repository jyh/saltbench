#!/usr/bin/env python3
# ncgen.py <repo> — writes block NC's two RESULT files; every figure block is the verifier's own --print output, never typed.
import subprocess, sys, os
repo = sys.argv[1]
V = os.path.join(repo, 'harness/systems-v3/RESULT-claude-blockNC-2026-11-17-verify.py')
REG = 'AMENDMENT-O37-blockNC-specchange-claude-2026-11-13.md'

def pr(b):
    return subprocess.run([sys.executable, V, '--block', b, '--print'], capture_output=True, text=True, check=True).stdout.rstrip('\n').split('\n')

def sect(L, pred):
    return '\n'.join(l for l in L if pred(l))

for b, model, name in [('NCO', 'claude-opus-5', 'OPUS'), ('NCS', 'claude-sonnet-5', 'SONNET')]:
    L = pr(b)
    s1 = sect(L, lambda l: l.startswith(('rows ', 'end_2 ', 'export ', 'scored ', 'served:', 'REACH-LOSS')))
    s2 = sect(L, lambda l: (' plain ' in l and '[' in l) or l.startswith('FULL PASS'))
    s3 = sect(L, lambda l: ' median COST ' in l or l.startswith(('total COST', 'capped cells', 'uncapped cells')))
    s4 = sect(L, lambda l: l.startswith(('(i)', '(ii)', '(iii)')))
    LIVE = ('⚠️ **EVERY LIVENESS FAILURE IS ONE CLAUSE TEST, `answer_is_the_count_honest_pair`, IN BOTH ARMS AND BOTH MODELS** (each failing '
            'cell: 0 regressions failed, 1 of 5 clause tests failed; the failing test named in each cell\'s B-suite output beside cells.tsv on '
            'the run box). The B suite\'s author (the lead) declared two readings of that card\'s count when building it (2026-11-09). Under '
            'NC §C6 item 4 a defect in a suite is a HARNESS finding, never an arm effect, so these failures are reported as they fell and the '
            'clause is put to a non-builder read; no arm reading rests on them.')
    if b == 'NCO':
        n1 = ('**Four condition-cells have no phase 2, all Opus LinearScan:** plain #3 and salt-diet #1–#3. Each source was a fresh phase 1 '
              '(block N\'s cells for those conditions were not eligible, `read_baselines.out`), and each ended CAP-COST at the fresh cap without landing. By §C2 they '
              'are REACH LOSSES: never re-run, never scored, never priced. So **Opus LinearScan salt-diet stands at n = 0** and plain at n = 2. '
              '**Two cells are scored at their WORKING TREE** (`clbfas02`, `clbfvs02`, both CAP-COST): their `solution.rs` was dirty at the cap, '
              'and score_claude_v3\'s rule reads the working tree. Their passes are floors.')
        n3 = ('⚠️ **Opus caps often in BOTH arms** (the CAP-COST counts above); a median at the cap is censored, and its ratio prints `>=`. '
              'The sign is the reading; the magnitudes are not, and the figures include the harness\'s own sandbox probe.')
        n4 = ('- **(ii) is a MISS for Opus:** in BinomialHeap and MaxFlow plain capped more often than salt-diet. LinearScan has no salt-diet '
              'phase-2 cell, so it gives no comparison. A miss is a result, reported as it fell.')
    else:
        n1 = ('**Five condition-cells have no phase 2.** Sonnet LinearScan salt-diet #1–#3: #1\'s fresh source LANDED but its G baseline read '
              '6 of 9 (REACH-LOSS-G: the code changed what the program computes), #2 and #3 ended CAP-COST. Sonnet MaxFlow salt-diet #2 and #3: '
              'both fresh sources ended CAP-COST. So **Sonnet LinearScan salt-diet stands at n = 0 and Sonnet MaxFlow salt-diet at n = 1**. '
              '**One cell ended EXIT-FORCED:** `clblvp03` (Liveness plain #3), the declared harness fault (the box reader under the C locale, '
              'fixed in the drivers on 11-15); its suite reads at HEAD. **Two cells are scored at their WORKING TREE** (`clblvs01`, `clblvs02`, '
              'both CAP-COST); their passes are floors.')
        n3 = ('⚠️ **Sonnet MaxFlow salt-diet is n = 1** (two reach losses), and that one cell (`clblxs01`) capped and fails 3 of 5 clause '
              'tests. The sign is the reading; the magnitudes are not, and the figures include the harness\'s own sandbox probe.')
        n4 = ('- **(ii) holds for Sonnet:** salt-diet capped strictly more often in Liveness and MaxFlow, and tied in three problems. '
              'LinearScan gives no comparison (no salt-diet phase-2 cell).')
    n1 = n1 + '\n' + LIVE
    doc = f'''# RESULT — O37 block NC, {name} COLUMN · `{model}` × greenfield → spec-change × extras=none × six problems · n = 3
### bench, 2026-11-17. **12 conditions, 36 condition-cells. One of block NC's two results of record (§C8: "a result of record per model").**
## 📌 The registration is `{REG}` (§C0–§C8, signed; ADDENDA 1–5: the G-rung instrument, the release, a copy's hooksPath, the fallback pool)
## 📌 The per-cell table is a FILE: `evidence/blockNC-2026-11-13/result/cells.tsv` (72 rows, both columns; made by `nc-derive.sh` beside it, README there)
## ⛔ Every figure line below is printed by `RESULT-claude-blockNC-2026-11-17-verify.py --block {b} --print` from that table, `p1-baselines.tsv` and block N's record, and `--check` asserts each one against the bytes of this document. No figure line was typed.

---
# §1 · WHAT RAN
`{model}` × **spec-change** (phase 2 on a COPY of a landed phase-1 cell) × **extras=none** × {{AES, BinomialHeap, LinearScan, Liveness, Luby, MaxFlow}} × {{plain, salt-diet}} × 3. The model
is derived per cell from its own phase-2 transcript by `served_models_v3.py check-cell`, never from the block name.
```
{s1}
```
{n1}

---
# §2 · CORRECTNESS, VERIFIED FIRST (lane B §Q6 rule 1: the withheld B suite's FULL PASS over scorable cells)
FULL PASS = the runner exits 0, TESTS passed = total, 0 of the REGRESSIONS failed and 0 of the CLAUSE_TESTS failed (the B driver prints
the last two as FAILED/total). The bracket lists each cell's TESTS in cell order.
```
{s2}
```
The lines above are the result. The Liveness failures are the one clause test named in §1, under NC §C6 item 4.

---
# §3 · COST AND THE PREMIUM (lane B §Q6 rule 3; every premium is registered UNRESOLVED-UNDERPOWERED, NC §C8)
```
{s3}
```
**Every capped cost ENTERS AT THE CAP;** the capped cells' metered COST is on its own line and used in no COST median, ratio or total. T is a metered figure for every cell, capped ones
included (kent's read of #448, 2026-11-17: the first draft said "no median, ratio or total", which is false for the T total).
{n3}

---
# §4 · THE REGISTERED PREDICTIONS (§C5 (i)–(iii)), REPORTED PER MODEL; A MISS IS A RESULT
```
{s4}
```
- **(i)** "the eligible count is lower for salt-diet than for plain": counted from `p1-baselines.tsv` restricted to block N's record
  (eligible = landed1 yes, rc 0, a full TESTS; it reproduces `read_baselines.out`'s per-model counts).
{n4}
- **(iii)** "CAP-WALL binds no cell": the line above prints the count.

---
# §5 · WHAT THIS RESULT CANNOT ESTABLISH (NC §C8, carried)
1. Any magnitude or effect size. 2. Anything about Opus versus Sonnet as models. 3. Anything about a spec-change reached from a phase 1
that did not land (none exists by construction; the reach losses are counted, never scored). 4. Anything about O37 conditions outside §C1.
**Confounds (§C6):** every reused source is also a cell of record in block N, so the two blocks are not independent; reach is
arm-correlated and the sources are filtered by it, so the eligible count travels with every figure; a reused source's phase 1 ran at
block N's export and its phase 2 at this block's (ee7450ce); one author wrote the six B/ suites (item 4). **ADDENDUM 5:** the fires after
2026-11-17 00:16 PST moved to the fallback pool; of the phase-2 cells of record only `clblrp03` ran there (its pool is in its run-cfg.tsv).
Any public sentence, and any claim about the method, is the Captain's.
'''
    out = os.path.join(repo, 'harness/systems-v3/RESULT-claude-block%s-2026-11-17.md' % b)
    open(out, 'w').write(doc)
    print('wrote', out)
