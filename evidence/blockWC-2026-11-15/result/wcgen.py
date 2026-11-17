#!/usr/bin/env python3
# wcgen.py <repo> — writes block WC's two RESULT files; every figure block is the verifier's own --print output, never typed.
import subprocess, sys, os
repo = sys.argv[1]
V = os.path.join(repo, 'harness/systems-v3/RESULT-claude-blockWC-2026-11-17-verify.py')
REG = 'AMENDMENT-O37-wht-ntt-specchange-claude-2026-11-13.md'

def pr(b):
    return subprocess.run([sys.executable, V, '--block', b, '--print'], capture_output=True, text=True, check=True).stdout.rstrip('\n').split('\n')

def sect(L, pred):
    return '\n'.join(l for l in L if pred(l))

for b, model, name in [('WCO', 'claude-opus-5', 'OPUS'), ('WCS', 'claude-sonnet-5', 'SONNET')]:
    L = pr(b)
    s1 = sect(L, lambda l: l.startswith(('rows ', 'end_2 ', 'export ', 'scored ', 'served:', 'REACH-LOSS ')))
    s2 = sect(L, lambda l: l.startswith(('NTT  plain', 'WHT  plain', 'FULL PASS')))
    s3 = sect(L, lambda l: l.startswith(('NTT  median', 'WHT  median', 'total COST', 'capped cells', 'uncapped cells')))
    s4 = sect(L, lambda l: l.startswith(('(i)', '(ii)', '(iii)')))
    if b == 'WCO':
        n1 = ('**One cell ended CAP-COST and is scored at its WORKING TREE:** `clbftp01` (NTT plain #1). Its `solution.rs` was dirty at the '
              'cap, so the scorer of record reads the working tree (score_claude_v3\'s rule, the one the lane applied at every harvest). '
              'Its pass is a floor (§3\'s rule). **One cell is ADDENDUM 3\'s:** `clbftp03` (NTT plain #3), staged from the EXIT-FORCED source '
              '`clbdtp03` by 74b1e0b4\'s stage and fire scripts; its record names d55062a6 and the two exports differ only in those scripts '
              '(ADDENDUM 4). The export line above is the record\'s, and it is printed as the record has it.')
        n3 = ('⚠️ **NTT\'s plain median is pulled up by the capped cell, which enters at the cap.** The sign is the reading; the magnitudes '
              'are not, and the figures include the harness\'s own sandbox probe (block W\'s declared limit).')
        n4 = ('- **(ii) is a MISS for Opus:** on NTT the one capped phase 2 is a PLAIN cell, so salt-diet\'s incidence is below plain\'s. '
              'A miss is a result, reported as it fell.')
    else:
        n1 = ('**Two condition-cells have no phase 2: both are Sonnet NTT salt-diet (#2, #3).** Their sources were fresh phase 1s (block W\'s '
              'own cells for those conditions capped), and both ended CAP-COST at the fresh cap without landing. By §WC2 they are REACH '
              'LOSSES: never re-run, never scored, never priced. So **Sonnet NTT salt-diet stands at n = 1**, and every figure for that '
              'condition below is over one cell.')
        n3 = ('⚠️ **Sonnet NTT salt-diet is n = 1** (the two reach losses), so its median is one cell\'s figure. The sign is the reading; '
              'the magnitudes are not, and the figures include the harness\'s own sandbox probe (block W\'s declared limit).')
        n4 = ('- **(ii) holds only as ties:** no Sonnet phase-2 cell capped. The two Sonnet NTT salt-diet sources that capped are phase-1 '
              'reach losses, which (i) and the REACH-LOSS lines carry, not (ii).')
    doc = f'''# RESULT — O37 block WC, {name} COLUMN · `{model}` × greenfield → spec-change × extras=none × NTT, WHT · n = 3
### bench, 2026-11-17. **4 conditions, 12 condition-cells. One of block WC's two results of record (§WC7 = NC §C8: "a result of record per model").**
## 📌 The registration is `{REG}` (§WC0–§WC7, signed 2026-11-13; ADDENDA 1–4: the release, the one EXIT-FORCED source, its export record)
## 📌 The per-cell table is a FILE: `evidence/blockWC-2026-11-15/result/cells.tsv` (24 rows, both columns; made by `wc-derive.sh` beside it, README there)
## ⛔ Every figure line below is printed by `RESULT-claude-blockWC-2026-11-17-verify.py --block {b} --print` from that table and `p1-baselines.tsv`, and `--check` asserts each one against the bytes of this document. No figure line was typed.

---
# §1 · WHAT RAN
`{model}` × **spec-change** (phase 2 on a COPY of a landed phase-1 cell) × **extras=none** × {{NTT, WHT}} × {{plain, salt-diet}} × 3. The model
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
**Every phase-2 cell of record passes its withheld B suite in full, in both arms.** With no FAIL in either arm, rule 2's sign is level in
both problems. ⚠️ NTT's reference proves less than WHT's at G (block W §W5 item 2; §WC6 item 4), so the two problems are not set side by side
as equals.

---
# §3 · COST AND THE PREMIUM (lane B §Q6 rule 3; every premium is registered UNRESOLVED-UNDERPOWERED, NC §C8)
```
{s3}
```
**Every capped cost ENTERS AT THE CAP;** the capped cells' metered COST is on its own line and used in no COST median, ratio or total. T is a metered figure for every cell, capped ones
included (kent's read of #448, 2026-11-17: the first draft said "no median, ratio or total", which is false for the T total).
{n3}

---
# §4 · THE REGISTERED PREDICTIONS (§WC5 = NC §C5 (i)–(iii)), REPORTED PER MODEL; A MISS IS A RESULT
```
{s4}
```
- **(i)** "the eligible count is lower for salt-diet than for plain": counted from the 24 phase-1 baselines (`p1-baselines.tsv`, block W's
  cells before any fresh phase 1).
{n4}
- **(iii)** "CAP-WALL binds no cell": the line above prints the count.

---
# §5 · WHAT THIS RESULT CANNOT ESTABLISH (NC §C8, carried)
1. Any magnitude or effect size. 2. Anything about Opus versus Sonnet as models. 3. Anything about a spec-change reached from a phase 1
that did not land (none exists by construction; the reach losses are counted, never scored). 4. Anything about O37 conditions outside §WC1.
**Confounds carried (NC §C6 items 1–3, §WC6 item 4):** every reused source is also a cell of record in block W, so the two blocks are not
independent; reach is arm-correlated and the sources are filtered by it, so the eligible count travels with every figure; a reused
source's phase 1 ran at block W's export (0916ef9a) and its phase 2 at this block's; one author wrote both tasks and both B/ suites.
Any public sentence, and any claim about the method, is the Captain's.
'''
    out = os.path.join(repo, 'harness/systems-v3/RESULT-claude-block%s-2026-11-17.md' % b)
    open(out, 'w').write(doc)
    print('wrote', out)
