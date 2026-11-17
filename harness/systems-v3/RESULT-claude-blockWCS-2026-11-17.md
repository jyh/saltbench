# RESULT — O37 block WC, SONNET COLUMN · `claude-sonnet-5` × greenfield → spec-change × extras=none × NTT, WHT · n = 3
### bench, 2026-11-17. **4 conditions, 12 condition-cells. One of block WC's two results of record (§WC7 = NC §C8: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-wht-ntt-specchange-claude-2026-11-13.md` (§WC0–§WC7, signed 2026-11-13; ADDENDA 1–4: the release, the one EXIT-FORCED source, its export record)
## 📌 The per-cell table is a FILE: `evidence/blockWC-2026-11-15/result/cells.tsv` (24 rows, both columns; made by `wc-derive.sh` beside it, README there)
## ⛔ Every figure line below is printed by `RESULT-claude-blockWC-2026-11-17-verify.py --block WCS --print` from that table and `p1-baselines.tsv`, and `--check` asserts each one against the bytes of this document. No figure line was typed.

---
# §1 · WHAT RAN
`claude-sonnet-5` × **spec-change** (phase 2 on a COPY of a landed phase-1 cell) × **extras=none** × {NTT, WHT} × {plain, salt-diet} × 3. The model
is derived per cell from its own phase-2 transcript by `served_models_v3.py check-cell`, never from the block name.
```
rows 12 · conditions 4 · phase-2 cells 10 · REACH-LOSS 2 · cap COST 18.60
end_2 LANDED 10 · REACH-LOSS 2
export d55062a62b55 10
scored HEAD 10
served: 10 of 10 phase-2 cells clean · head claude-sonnet-5 only
REACH-LOSS NTT salt-diet n=2 source clbzts02 end-1 CAP-COST, metered $37.60 of $37.21
REACH-LOSS NTT salt-diet n=3 source clbzts03 end-1 CAP-COST, metered $38.17 of $37.21
```
**Two condition-cells have no phase 2: both are Sonnet NTT salt-diet (#2, #3).** Their sources were fresh phase 1s (block W's own cells for those conditions capped), and both ended CAP-COST at the fresh cap without landing. By §WC2 they are REACH LOSSES: never re-run, never scored, never priced. So **Sonnet NTT salt-diet stands at n = 1**, and every figure for that condition below is over one cell.

---
# §2 · CORRECTNESS, VERIFIED FIRST (lane B §Q6 rule 1: the withheld B suite's FULL PASS over scorable cells)
FULL PASS = the runner exits 0, TESTS passed = total, 0 of the REGRESSIONS failed and 0 of the CLAUSE_TESTS failed (the B driver prints
the last two as FAILED/total). The bracket lists each cell's TESTS in cell order.
```
NTT  plain 3/3 [15/15 15/15 15/15] · salt-diet 1/1 [15/15]
WHT  plain 3/3 [16/16 16/16 16/16] · salt-diet 3/3 [16/16 16/16 16/16]
FULL PASS plain 6 of 6
FULL PASS salt-diet 4 of 4
```
**Every phase-2 cell of record passes its withheld B suite in full, in both arms.** With no FAIL in either arm, rule 2's sign is level in
both problems. ⚠️ NTT's reference proves less than WHT's at G (block W §W5 item 2; §WC6 item 4), so the two problems are not set side by side
as equals.

---
# §3 · COST AND THE PREMIUM (lane B §Q6 rule 3; every premium is registered UNRESOLVED-UNDERPOWERED, NC §C8)
```
NTT  median COST plain $2.05 · salt-diet $4.40 · ratio 2.2x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 1 · UNRESOLVED-UNDERPOWERED
WHT  median COST plain $1.84 · salt-diet $12.03 · ratio 6.5x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
total COST (capped at the cap) plain $11.54 · total T (metered, every cell) 26,542,012
total COST (capped at the cap) salt-diet $40.32 · total T (metered, every cell) 132,425,352
capped cells METERED COST (in no COST line above): 0
uncapped cells ending above the cap: 0
```
**Every capped cost ENTERS AT THE CAP;** the capped cells' metered COST is on its own line and used in no COST median, ratio or total. T is a metered figure for every cell, capped ones
included (kent's read of #448, 2026-11-17: the first draft said "no median, ratio or total", which is false for the T total).
⚠️ **Sonnet NTT salt-diet is n = 1** (the two reach losses), so its median is one cell's figure. The sign is the reading; the magnitudes are not, and the figures include the harness's own sandbox probe (block W's declared limit).

---
# §4 · THE REGISTERED PREDICTIONS (§WC5 = NC §C5 (i)–(iii)), REPORTED PER MODEL; A MISS IS A RESULT
```
(i) eligible plain 6/6 · salt-diet 3/6 · HOLDS
(ii) salt-diet CAP-COST incidence >= plain in 2 of 2 problems (0 strictly, 2 ties, 0 reversed) · NTT salt-diet 0/1 plain 0/3 · WHT salt-diet 0/3 plain 0/3 · HOLDS
(iii) CAP-WALL cells 0
```
- **(i)** "the eligible count is lower for salt-diet than for plain": counted from the 24 phase-1 baselines (`p1-baselines.tsv`, block W's
  cells before any fresh phase 1).
- **(ii) holds only as ties:** no Sonnet phase-2 cell capped. The two Sonnet NTT salt-diet sources that capped are phase-1 reach losses, which (i) and the REACH-LOSS lines carry, not (ii).
- **(iii)** "CAP-WALL binds no cell": the line above prints the count.

---
# §5 · WHAT THIS RESULT CANNOT ESTABLISH (NC §C8, carried)
1. Any magnitude or effect size. 2. Anything about Opus versus Sonnet as models. 3. Anything about a spec-change reached from a phase 1
that did not land (none exists by construction; the reach losses are counted, never scored). 4. Anything about O37 conditions outside §WC1.
**Confounds carried (NC §C6 items 1–3, §WC6 item 4):** every reused source is also a cell of record in block W, so the two blocks are not
independent; reach is arm-correlated and the sources are filtered by it, so the eligible count travels with every figure; a reused
source's phase 1 ran at block W's export (0916ef9a) and its phase 2 at this block's; one author wrote both tasks and both B/ suites.
Any public sentence, and any claim about the method, is the Captain's.
