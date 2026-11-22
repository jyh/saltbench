# RESULT — O37 block WC, OPUS COLUMN · `claude-opus-5` × greenfield → spec-change × extras=none × NTT, WHT · n = 3
### bench, 2026-11-17. **4 conditions, 12 condition-cells. One of block WC's two results of record (§WC7 = NC §C8: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-wht-ntt-specchange-claude-2026-11-13.md` (§WC0–§WC7, signed 2026-11-13; ADDENDA 1–4: the release, the one EXIT-FORCED source, its export record)
## 📌 The per-cell table is a FILE: `evidence/blockWC-2026-11-15/result/cells.tsv` (24 rows, both columns; made by `wc-derive.sh` beside it, README there)
## ⛔ Every figure line below is printed by `RESULT-claude-blockWC-2026-11-17-verify.py --block WCO --print` from that table and `p1-baselines.tsv`, and `--check` asserts each one against the bytes of this document. No figure line was typed.

---
# §1 · WHAT RAN
`claude-opus-5` × **spec-change** (phase 2 on a COPY of a landed phase-1 cell) × **extras=none** × {NTT, WHT} × {plain, salt-diet} × 3. The model
is derived per cell from its own phase-2 transcript by `served_models_v3.py check-cell`, never from the block name.
```
rows 12 · conditions 4 · phase-2 cells 12 · REACH-LOSS 0 · cap COST 18.60
end_2 CAP-COST 1 · LANDED 11
export d55062a62b55 12
scored HEAD 11 · WORKING-TREE 1
served: 12 of 12 phase-2 cells clean · head claude-opus-5 only
```
**One cell ended CAP-COST and is scored at its WORKING TREE:** `clbftp01` (NTT plain #1). Its `solution.rs` was dirty at the cap, so the scorer of record reads the working tree (score_claude_v3's rule, the one the lane applied at every harvest). Its pass is a floor (§3's rule). **One cell is ADDENDUM 3's:** `clbftp03` (NTT plain #3), staged from the EXIT-FORCED source `clbdtp03` by 74b1e0b4's stage and fire scripts; its record names d55062a6 and the two exports differ only in those scripts (ADDENDUM 4). The export line above is the record's, and it is printed as the record has it.

---
# §2 · CORRECTNESS, VERIFIED FIRST (lane B §Q6 rule 1: the withheld B suite's FULL PASS over scorable cells)
FULL PASS = the runner exits 0, TESTS passed = total, 0 of the REGRESSIONS failed and 0 of the CLAUSE_TESTS failed (the B driver prints
the last two as FAILED/total). The bracket lists each cell's TESTS in cell order.
```
NTT  plain 3/3 [15/15 15/15 15/15] · salt-diet 3/3 [15/15 15/15 15/15]
WHT  plain 3/3 [16/16 16/16 16/16] · salt-diet 3/3 [16/16 16/16 16/16]
FULL PASS plain 6 of 6
FULL PASS salt-diet 6 of 6
```
**Every phase-2 cell of record passes its withheld B suite in full, in both arms.** With no FAIL in either arm, rule 2's sign is level in
both problems. ⚠️ NTT's reference proves less than WHT's at G (block W §W5 item 2; §WC6 item 4), so the two problems are not set side by side
as equals.

---
# §3 · COST AND THE PREMIUM (lane B §Q6 rule 3; every premium is registered UNRESOLVED-UNDERPOWERED, NC §C8)
```
NTT  median COST plain $16.35 · salt-diet $16.63 · ratio 1.0x · CAP-COST plain 1 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
WHT  median COST plain $10.84 · salt-diet $16.65 · ratio 1.5x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
total COST (capped at the cap) plain $76.07 · total T (metered, every cell) 84,547,471
total COST (capped at the cap) salt-diet $100.98 · total T (metered, every cell) 112,564,523
capped cells METERED COST (in no COST line above): 1, $19.19 .. $19.19 against cap $18.60
uncapped cells ending above the cap: 0
```
**Every capped cost ENTERS AT THE CAP;** the capped cells' metered COST is on its own line and used in no COST median, ratio or total. T is a metered figure for every cell, capped ones
included (kent's read of #448, 2026-11-17: the first draft said "no median, ratio or total", which is false for the T total).
⚠️ **NTT's plain median is pulled up by the capped cell, which enters at the cap.** The sign is the reading; the magnitudes are not, and the figures include the harness's own sandbox probe (block W's declared limit).

---
# §4 · THE REGISTERED PREDICTIONS (§WC5 = NC §C5 (i)–(iii)), REPORTED PER MODEL; A MISS IS A RESULT
```
(i) eligible plain 6/6 · salt-diet 5/6 · HOLDS
(ii) salt-diet CAP-COST incidence >= plain in 1 of 2 problems (0 strictly, 1 ties, 1 reversed) · NTT salt-diet 0/3 plain 1/3 · WHT salt-diet 0/3 plain 0/3 · MISS
(iii) CAP-WALL cells 0
```
- **(i)** "the eligible count is lower for salt-diet than for plain": counted from the 24 phase-1 baselines (`p1-baselines.tsv`, block W's
  cells before any fresh phase 1).
- **(ii) is a MISS for Opus:** on NTT the one capped phase 2 is a PLAIN cell, so salt-diet's incidence is below plain's. A miss is a result, reported as it fell.
- **(iii)** "CAP-WALL binds no cell": the line above prints the count.

---
# §5 · WHAT THIS RESULT CANNOT ESTABLISH (NC §C8, carried)
1. Any magnitude or effect size. 2. Anything about Opus versus Sonnet as models. 3. Anything about a spec-change reached from a phase 1
that did not land (none exists by construction; the reach losses are counted, never scored). 4. Anything about O37 conditions outside §WC1.
**Confounds carried (NC §C6 items 1–3, §WC6 item 4):** every reused source is also a cell of record in block W, so the two blocks are not
independent; reach is arm-correlated and the sources are filtered by it, so the eligible count travels with every figure; a reused
source's phase 1 ran at block W's export (0916ef9a) and its phase 2 at this block's; one author wrote both tasks and both B/ suites.
Any public sentence, and any claim about the method, is the Captain's.
