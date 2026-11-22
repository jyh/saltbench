# RESULT — O37 block NC, SONNET COLUMN · `claude-sonnet-5` × greenfield → spec-change × extras=none × six problems · n = 3
### bench, 2026-11-17. **12 conditions, 36 condition-cells. One of block NC's two results of record (§C8: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-blockNC-specchange-claude-2026-11-13.md` (§C0–§C8, signed; ADDENDA 1–5: the G-rung instrument, the release, a copy's hooksPath, the fallback pool)
## 📌 The per-cell table is a FILE: `evidence/blockNC-2026-11-13/result/cells.tsv` (72 rows, both columns; made by `nc-derive.sh` beside it, README there)
## ⛔ Every figure line below is printed by `RESULT-claude-blockNC-2026-11-17-verify.py --block NCS --print` from that table, `p1-baselines.tsv` and block N's record, and `--check` asserts each one against the bytes of this document. No figure line was typed.

---
# §1 · WHAT RAN
`claude-sonnet-5` × **spec-change** (phase 2 on a COPY of a landed phase-1 cell) × **extras=none** × {AES, BinomialHeap, LinearScan, Liveness, Luby, MaxFlow} × {plain, salt-diet} × 3. The model
is derived per cell from its own phase-2 transcript by `served_models_v3.py check-cell`, never from the block name.
```
rows 36 · conditions 12 · phase-2 cells 31 · reach losses 5 · cap COST 18.60
end_2 CAP-COST 4 · EXIT-FORCED 1 · LANDED 26 · REACH-LOSS 4 · REACH-LOSS-G 1
export ee7450ce4ba7 31
scored HEAD 29 · WORKING-TREE 2
served: 31 of 31 phase-2 cells clean · head claude-sonnet-5 only
REACH-LOSS-G LinearScan salt-diet n=1 source clbzrs01 end-1 LANDED, metered $32.85 of $37.21
REACH-LOSS LinearScan salt-diet n=2 source clbzrs02 end-1 CAP-COST, metered $37.30 of $37.21
REACH-LOSS LinearScan salt-diet n=3 source clbzrs03 end-1 CAP-COST, metered $37.40 of $37.21
REACH-LOSS MaxFlow salt-diet n=2 source clbzxs02 end-1 CAP-COST, metered $37.63 of $37.21
REACH-LOSS MaxFlow salt-diet n=3 source clbzxs03 end-1 CAP-COST, metered $37.89 of $37.21
```
**Five condition-cells have no phase 2.** Sonnet LinearScan salt-diet #1–#3: #1's fresh source LANDED but its G baseline read 6 of 9 (REACH-LOSS-G: the code changed what the program computes), #2 and #3 ended CAP-COST. Sonnet MaxFlow salt-diet #2 and #3: both fresh sources ended CAP-COST. So **Sonnet LinearScan salt-diet stands at n = 0 and Sonnet MaxFlow salt-diet at n = 1**. **One cell ended EXIT-FORCED:** `clblvp03` (Liveness plain #3), the declared harness fault (the box reader under the C locale, fixed in the drivers on 11-15); its suite reads at HEAD. **Two cells are scored at their WORKING TREE** (`clblvs01`, `clblvs02`, both CAP-COST); their passes are floors.
⚠️ **EVERY LIVENESS FAILURE IS ONE CLAUSE TEST, `answer_is_the_count_honest_pair`, IN BOTH ARMS AND BOTH MODELS** (each failing cell: 0 regressions failed, 1 of 5 clause tests failed; the failing test named in each cell's B-suite output beside cells.tsv on the run box). The B suite's author (the lead) declared two readings of that card's count when building it (2026-11-09). Under NC §C6 item 4 a defect in a suite is a HARNESS finding, never an arm effect, so these failures are reported as they fell and the clause is put to a non-builder read; no arm reading rests on them.

---
# §2 · CORRECTNESS, VERIFIED FIRST (lane B §Q6 rule 1: the withheld B suite's FULL PASS over scorable cells)
FULL PASS = the runner exits 0, TESTS passed = total, 0 of the REGRESSIONS failed and 0 of the CLAUSE_TESTS failed (the B driver prints
the last two as FAILED/total). The bracket lists each cell's TESTS in cell order.
```
AES          plain 3/3 [14/14 14/14 14/14] · salt-diet 3/3 [14/14 14/14 14/14]
BinomialHeap plain 3/3 [18/18 18/18 18/18] · salt-diet 3/3 [18/18 18/18 18/18]
LinearScan   plain 3/3 [14/14 14/14 14/14] · salt-diet 0/0 []
Liveness     plain 2/3 [16/16 15/16 16/16] · salt-diet 1/3 [15/16 16/16 15/16]
Luby         plain 3/3 [19/19 19/19 19/19] · salt-diet 3/3 [19/19 19/19 19/19]
MaxFlow      plain 3/3 [13/13 13/13 13/13] · salt-diet 0/1 [10/13]
FULL PASS plain 17 of 18
FULL PASS salt-diet 10 of 13
```
The lines above are the result. The Liveness failures are the one clause test named in §1, under NC §C6 item 4.

---
# §3 · COST AND THE PREMIUM (lane B §Q6 rule 3; every premium is registered UNRESOLVED-UNDERPOWERED, NC §C8)
```
AES          median COST plain $2.37 · salt-diet $10.96 · ratio 4.6x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
BinomialHeap median COST plain $2.53 · salt-diet $3.60 · ratio 1.4x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
LinearScan   median COST plain $11.48 · salt-diet - · ratio - · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 0 · UNRESOLVED-UNDERPOWERED
Liveness     median COST plain $3.56 · salt-diet $18.60 · ratio >= 5.2x · CAP-COST plain 0 salt-diet 3 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
Luby         median COST plain $2.25 · salt-diet $10.18 · ratio 4.5x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
MaxFlow      median COST plain $3.96 · salt-diet $18.60 · ratio >= 4.7x · CAP-COST plain 0 salt-diet 1 · n plain 3 n salt-diet 1 · UNRESOLVED-UNDERPOWERED
total COST (capped at the cap) plain $78.89 · total T (metered, every cell) 177,845,753
total COST (capped at the cap) salt-diet $143.32 · total T (metered, every cell) 458,195,593
capped cells METERED COST (in no COST line above): 4, $18.67 .. $18.98 against cap $18.60
uncapped cells ending above the cap: 0
```
**Every capped cost ENTERS AT THE CAP;** the capped cells' metered COST is on its own line and used in no COST median, ratio or total. T is a metered figure for every cell, capped ones
included (kent's read of #448, 2026-11-17: the first draft said "no median, ratio or total", which is false for the T total).
⚠️ **Sonnet MaxFlow salt-diet is n = 1** (two reach losses), and that one cell (`clblxs01`) capped and fails 3 of 5 clause tests. The sign is the reading; the magnitudes are not, and the figures include the harness's own sandbox probe.

---
# §4 · THE REGISTERED PREDICTIONS (§C5 (i)–(iii)), REPORTED PER MODEL; A MISS IS A RESULT
```
(i) eligible plain 16/18 · salt-diet 12/18 · HOLDS
(ii) salt-diet CAP-COST incidence >= plain in 5 of 5 problems (2 strictly, 3 ties, 0 reversed) · HOLDS
(ii) AES salt-diet 0/3 plain 0/3
(ii) BinomialHeap salt-diet 0/3 plain 0/3
(ii) LinearScan salt-diet 0/0 plain 0/3 (no comparison: an arm has no phase-2 cell)
(ii) Liveness salt-diet 3/3 plain 0/3
(ii) Luby salt-diet 0/3 plain 0/3
(ii) MaxFlow salt-diet 1/1 plain 0/3
(iii) CAP-WALL cells 0
```
- **(i)** "the eligible count is lower for salt-diet than for plain": counted from `p1-baselines.tsv` restricted to block N's record
  (eligible = landed1 yes, rc 0, a full TESTS; it reproduces `read_baselines.out`'s per-model counts).
- **(ii) holds for Sonnet:** salt-diet capped strictly more often in Liveness and MaxFlow, and tied in three problems. LinearScan gives no comparison (no salt-diet phase-2 cell).
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

---
# ADDENDUM 1 (2026-11-17, bench) — THE LIVENESS CLAUSE FAILURES ARE A SUITE DEFECT (§C6 item 4 answered). NO FIGURE MOVES. APPENDED.
The non-builder read §1 and §C6 item 4 asked for (systems, who built none of the B/ suites; bus offset 105,218,390, 2026-11-17 10:55)
answers YES: `answer_is_the_count_honest_pair` fixes ONE reading of the card's "a sweep is one pass in which every block's two sets are
brought up to date from the sets as they stood at the start of that pass", the PAIR pass (in(b) from the old out(b), out(b) from the old
in). It is neither of the two count readings the suite's README declares. Every failing cell counted a COMPOSED pass the sentence also
admits (a block's own two sets made consistent within the pass), and each one cites the card's sentence in its own comment. Three
pieces of the suite admit that reading too: mutant InPlaceSweeps' own comment, phase 1's oracle `d_solve`, and the README's "no test
compares `sweeps` against a number other than the bound". On `loop` the first stable iterate is 5 under the pair pass and 3 under either
composed pass, all three on the same least pair. The cells report 3 or 4, which is b.out's "after 3 / after 4 sweeps the pair is still
changing". Each passes `counted_answer_is_least` and the other three clause tests, with 0 regressions. Read on the copied sources and
b.out lines; the k* figures come from systems' hand simulation, not from a compile.
**RULED (the lead), on systems' recommendation:** (a) the cells stand as they fell (this block's rule): a FULL PASS figure here does not
move, and no cell is re-scored. In this model the three Liveness cells that failed this one test (`clblvp02` plain, `clblvs01` and `clblvs03` salt-diet) failed it
by this defect, not by a wrong answer, so Liveness's FULL PASS gap in §2 is the suite's, in both arms. (b) For any later run on Liveness, the CARD is amended before that run's first model call, with a
sentence that settles the pass (systems': "in(b) is computed from out(b) as it stood at the start of the pass, not from the out(b)
computed in the same pass"), and the test is NOT widened: a black-box count test that accepts any reading would also pass CountOneShort
and lose that kill. (c) With the card amended, InPlaceSweeps stays a valid mutant. Not read by systems: the reference solution, the
Verus cells' verifier output, the other five clause mutants under the composed pass.
