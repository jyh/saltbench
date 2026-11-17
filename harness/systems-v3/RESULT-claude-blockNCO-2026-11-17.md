# RESULT — O37 block NC, OPUS COLUMN · `claude-opus-5` × greenfield → spec-change × extras=none × six problems · n = 3
### bench, 2026-11-17. **12 conditions, 36 condition-cells. One of block NC's two results of record (§C8: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-blockNC-specchange-claude-2026-11-13.md` (§C0–§C8, signed; ADDENDA 1–5: the G-rung instrument, the release, a copy's hooksPath, the fallback pool)
## 📌 The per-cell table is a FILE: `evidence/blockNC-2026-11-13/result/cells.tsv` (72 rows, both columns; made by `nc-derive.sh` beside it, README there)
## ⛔ Every figure line below is printed by `RESULT-claude-blockNC-2026-11-17-verify.py --block NCO --print` from that table, `p1-baselines.tsv` and block N's record, and `--check` asserts each one against the bytes of this document. No figure line was typed.

---
# §1 · WHAT RAN
`claude-opus-5` × **spec-change** (phase 2 on a COPY of a landed phase-1 cell) × **extras=none** × {AES, BinomialHeap, LinearScan, Liveness, Luby, MaxFlow} × {plain, salt-diet} × 3. The model
is derived per cell from its own phase-2 transcript by `served_models_v3.py check-cell`, never from the block name.
```
rows 36 · conditions 12 · phase-2 cells 32 · reach losses 4 · cap COST 18.60
end_2 CAP-COST 14 · LANDED 18 · REACH-LOSS 4
export ee7450ce4ba7 32
scored HEAD 30 · WORKING-TREE 2
served: 32 of 32 phase-2 cells clean · head claude-opus-5 only
REACH-LOSS LinearScan plain n=3 source clbyrp03 end-1 CAP-COST, metered $37.84 of $37.21
REACH-LOSS LinearScan salt-diet n=1 source clbyrs01 end-1 CAP-COST, metered $38.03 of $37.21
REACH-LOSS LinearScan salt-diet n=2 source clbyrs02 end-1 CAP-COST, metered $38.01 of $37.21
REACH-LOSS LinearScan salt-diet n=3 source clbyrs03 end-1 CAP-COST, metered $37.24 of $37.21
```
**Four condition-cells have no phase 2, all Opus LinearScan:** plain #3 and salt-diet #1–#3. Each source was a fresh phase 1 (block N's cells for those conditions were not eligible, `read_baselines.out`), and each ended CAP-COST at the fresh cap without landing. By §C2 they are REACH LOSSES: never re-run, never scored, never priced. So **Opus LinearScan salt-diet stands at n = 0** and plain at n = 2. **Two cells are scored at their WORKING TREE** (`clbfas02`, `clbfvs02`, both CAP-COST): their `solution.rs` was dirty at the cap, and score_claude_v3's rule reads the working tree. Their passes are floors.
⚠️ **EVERY LIVENESS FAILURE IS ONE CLAUSE TEST, `answer_is_the_count_honest_pair`, IN BOTH ARMS AND BOTH MODELS** (each failing cell: 0 regressions failed, 1 of 5 clause tests failed; the failing test named in each cell's B-suite output beside cells.tsv on the run box). The B suite's author (the lead) declared two readings of that card's count when building it (2026-11-09). Under NC §C6 item 4 a defect in a suite is a HARNESS finding, never an arm effect, so these failures are reported as they fell and the clause is put to a non-builder read; no arm reading rests on them.

---
# §2 · CORRECTNESS, VERIFIED FIRST (lane B §Q6 rule 1: the withheld B suite's FULL PASS over scorable cells)
FULL PASS = the runner exits 0, TESTS passed = total, 0 of the REGRESSIONS failed and 0 of the CLAUSE_TESTS failed (the B driver prints
the last two as FAILED/total). The bracket lists each cell's TESTS in cell order.
```
AES          plain 3/3 [14/14 14/14 14/14] · salt-diet 3/3 [14/14 14/14 14/14]
BinomialHeap plain 3/3 [18/18 18/18 18/18] · salt-diet 3/3 [18/18 18/18 18/18]
LinearScan   plain 2/2 [14/14 14/14] · salt-diet 0/0 []
Liveness     plain 2/3 [16/16 16/16 15/16] · salt-diet 1/3 [15/16 16/16 15/16]
Luby         plain 3/3 [19/19 19/19 19/19] · salt-diet 3/3 [19/19 19/19 19/19]
MaxFlow      plain 3/3 [13/13 13/13 13/13] · salt-diet 3/3 [13/13 13/13 13/13]
FULL PASS plain 16 of 17
FULL PASS salt-diet 13 of 15
```
The lines above are the result. The Liveness failures are the one clause test named in §1, under NC §C6 item 4.

---
# §3 · COST AND THE PREMIUM (lane B §Q6 rule 3; every premium is registered UNRESOLVED-UNDERPOWERED, NC §C8)
```
AES          median COST plain $15.17 · salt-diet $13.21 · ratio 0.9x · CAP-COST plain 0 salt-diet 1 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
BinomialHeap median COST plain $15.23 · salt-diet $14.11 · ratio 0.9x · CAP-COST plain 1 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
LinearScan   median COST plain $18.60 · salt-diet - · ratio - · CAP-COST plain 2 salt-diet 0 · n plain 2 n salt-diet 0 · UNRESOLVED-UNDERPOWERED
Liveness     median COST plain $17.84 · salt-diet $18.60 · ratio >= 1.0x · CAP-COST plain 1 salt-diet 2 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
Luby         median COST plain $17.85 · salt-diet $14.14 · ratio 0.8x · CAP-COST plain 1 salt-diet 1 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
MaxFlow      median COST plain $18.60 · salt-diet $18.60 · ratio >= 1.0x · CAP-COST plain 3 salt-diet 2 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
total COST (capped at the cap) plain $283.36 · total T (metered, every cell) 321,249,751
total COST (capped at the cap) salt-diet $243.71 · total T (metered, every cell) 277,462,043
capped cells METERED COST (in no COST line above): 14, $18.66 .. $19.86 against cap $18.60
uncapped cells ending above the cap: 1 (clbfxs01)
```
**Every capped cost ENTERS AT THE CAP;** the capped cells' metered COST is on its own line and used in no COST median, ratio or total. T is a metered figure for every cell, capped ones
included (kent's read of #448, 2026-11-17: the first draft said "no median, ratio or total", which is false for the T total).
⚠️ **Opus caps often in BOTH arms** (the CAP-COST counts above); a median at the cap is censored, and its ratio prints `>=`. The sign is the reading; the magnitudes are not, and the figures include the harness's own sandbox probe.

---
# §4 · THE REGISTERED PREDICTIONS (§C5 (i)–(iii)), REPORTED PER MODEL; A MISS IS A RESULT
```
(i) eligible plain 17/18 · salt-diet 15/18 · HOLDS
(ii) salt-diet CAP-COST incidence >= plain in 3 of 5 problems (2 strictly, 1 ties, 2 reversed) · MISS
(ii) AES salt-diet 1/3 plain 0/3
(ii) BinomialHeap salt-diet 0/3 plain 1/3
(ii) LinearScan salt-diet 0/0 plain 2/2 (no comparison: an arm has no phase-2 cell)
(ii) Liveness salt-diet 2/3 plain 1/3
(ii) Luby salt-diet 1/3 plain 1/3
(ii) MaxFlow salt-diet 2/3 plain 3/3
(iii) CAP-WALL cells 0
```
- **(i)** "the eligible count is lower for salt-diet than for plain": counted from `p1-baselines.tsv` restricted to block N's record
  (eligible = landed1 yes, rc 0, a full TESTS; it reproduces `read_baselines.out`'s per-model counts).
- **(ii) is a MISS for Opus:** in BinomialHeap and MaxFlow plain capped more often than salt-diet. LinearScan has no salt-diet phase-2 cell, so it gives no comparison. A miss is a result, reported as it fell.
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
