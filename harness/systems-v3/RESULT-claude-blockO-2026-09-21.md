# RESULT — block O · `claude-opus-5` × brownfield × extras=none · n=30
### bench, 2026-09-21. **10 conditions. The Opus counterpart of block SB, and the first time both Claude models have brownfield evidence on the same field.**
## 📌 The per-cell table is also a FILE: `evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv` (30 rows, 25 columns).
## ⛔ Every figure below is derived from that table by `RESULT-claude-blockO-2026-09-21-verify.py`. No number in this document was typed from a message or from memory.

---
# §1 · WHAT RAN
`claude-opus-5` × **brownfield** × **extras=none** × {Crc32, FreeList, LRU, LZW, Paxos} × {plain, salt-diet} × 3 reps = **30 cells / 10 conditions.** Cells built from export `283362105d75`. **Model derived per cell from its own `served-*.out` receipt** by `model_served_v3.py`: `claude-opus-5` for all 30, never taken from the block name.

```
  run_state    ENDED: LANDED 29 · ENDED: CAP-COST 1
  w1_fenced    COVERED 30 of 30
  end_from     HEAD 29 · working tree 1
```

---
# §2 · ⭐⭐ THE HEADLINE — **CORRECTNESS IS IDENTICAL AND THE ARMS ARE NOT**
```
  suite        PASS 30 of 30        plain 15/15 · salt-diet 15/15
  per problem  Crc32 6/6 · FreeList 6/6 · LRU 6/6 · LZW 6/6 · Paxos 6/6
  tests        6/6 · 7/7 · 8/8 · 16/16 · 17/17     (every declared test, every cell)
  V1 fixed     the FULL complement in every problem: Crc32 5 of 5 · FreeList 1 of 1 ·
               LRU 6 of 6 · LZW 5 of 5 · Paxos 6 of 6
  introduced   `>=0 (suite-limited)` for all 30 — A FLOOR, NEVER A ZERO
```
⇒ 🔑 ***ON THIS FIELD, AT THIS MODEL, THE TREATMENT DOES NOT MOVE CORRECTNESS: BOTH ARMS REPAIR EVERY PLANTED DEFECT AND PASS EVERY TEST. WHAT THEY DIFFER IN IS HOW MUCH CODE THEY WRITE AND WHAT IT COSTS.***
⛔ **`bugs_introduced` IS A FLOOR AND IS REPORTED AS ONE.** It counts tests PASSING at baseline that FAIL at end, by name — **the suite can only see what the suite tests.** A cell may have introduced a defect no declared test names. **Nothing here says "no bugs introduced."**
⚠️ **AND THE CEILING IS THE REAL LIMIT ON §2: 30 of 30 is a SATURATED MEASURE.** A measure everything passes cannot rank the arms, and its most likely reading is that **these givens are too easy to separate Opus's two arms on correctness** — not that the arms are equivalent. **The discriminating evidence in this block is §3, not §2.**

---
# §3 · ⛔⛔ RETENTION — **THE ARMS SEPARATE PERFECTLY, AND THE SEPARATOR IS READING *GROWTH***
```
                      retained (disjoint)   surv (OVERLAPPING)    growth (disjoint)      class
  plain      n=15     0.263 .. 0.872        0.305 .. 0.958        0.69x ..  3.00x        REPAIRED 15
  salt-diet  n=15     0.041 .. 0.222        0.360 .. 0.755        5.16x .. 16.55x        REPLACED 13 · REPAIRED 2
```
⇒ 🔑 ***`retained` SEPARATES THE TWO ARMS WITH NO OVERLAP AT ALL — AND `surv` OVERLAPS HEAVILY WHILE `growth` IS DISJOINT. SO THE THING THE PRIMARY SEPARATOR IS MEASURING IS HOW MUCH CODE THE ARM ADDED, NOT HOW MUCH OF THE SEED IT DESTROYED.***
**`retained` is difflib's line-level similarity ratio of END against SEED — symmetric in additions and deletions.** §B5's language (`REPLACED` = *"rewritten wholesale"*, `REPAIRED` = *"EDITED"*) is a claim about **what survived**, and a similarity ratio cannot see survival separately from growth.
⭐ **THE SALT-DIET ARM IS NOT DESTROYING THE SEED — IT IS BURYING IT.** Its `surv` (0.360–0.755) sits *inside* plain's range (0.305–0.958): **a comparable fraction of the original lines is still there.** What differs is everything written around them — `end_lines` **300–2,632** against plain's **70–451**, from seeds of 50–377.
⇒ **This is block SB's §5 finding appearing again at a different model.** ⚠️ **Stated as a COMPARISON, not as a passed prediction:** block O's prior was BROKEN by the ⑤(a) re-order (the freeze's A3.2), so this block never carried a registered prediction, and *"the same shape appears at Opus"* is an observation about two blocks, not a confirmed hypothesis.

---
# §4 · COST — THE SALT-DIET ARM COSTS ABOUT TWICE AS MUCH FOR THE SAME SUITE RESULT
```
               median COST   total COST    total T         median T
  plain        $10.11        $172.98       166,374,846      8,960,216
  salt-diet    $19.07        $329.14       388,582,034     21,632,596
  ratio        1.89x         1.90x         2.34x            2.41x
```
⛔ **`cap_unit` IS `COST` FOR ALL 30 AND THE CAP IS $37.21 — SO `T` IS READ AND PRINTED, NEVER THE CUTTER.** The one capped cell is the tell that this is a real ceiling and not a formality.
⚠️ **THE ONE CAPPED CELL, NAMED:** `clbofs02` (FreeList, salt-diet) ended `CAP-COST` at **$37.58** — **and it still passes 7/7 and fixes 1 of 1.** Its cost is **CENSORED AT THE CAP**, so the salt-diet totals above are a **LOWER BOUND**, and the true ratio is *at least* 1.89×. ⛔ **A capped cell's cost is not poolable with an uncapped one** (helm ruling 2026-09-11); it is in the table and named here rather than dropped.

---
# §5 · THE TABLE OF RECORD
`evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv` — 30 rows, 25 columns, built by `join_cells_table.py`: a mechanical join of the scoring pass, the retention decomposition and each cell's own frozen meter. **`class` and `retained` are produced INDEPENDENTLY by the scorer and by the retention decomposition, and the join ASSERTS they are equal rather than preferring one — all 30 agreed.**

---
# §6 · ⛔ WHAT THIS DOES **NOT** SAY
1. **It is one model on one field with extras=none.** It says nothing about Sonnet, about greenfield, or about the statement and spec-change treatments.
2. **`bugs_introduced` is suite-limited.** See §2.
3. **The suite result is saturated at 30/30** and therefore cannot rank the arms — §2's own limit.
4. **No cell was re-run.** Every number is a re-reading of artifacts that existed before this shift.
5. **`surv` is a LOWER BOUND** (matched lines only), as `retention_decompose.py` declares.
6. **Nothing here is a claim about the salt METHOD.** These are `plain` vs `salt-diet` arms on brownfield givens; the method's own claim is not on trial in this block.

---
# §7 · PROVENANCE
```
  cells        30, built from export 283362105d75, staged at ~/bench-dry/clb-score/ and scored as they landed
  scored by    score_claude_v3.py from 283362105d75's harness, --declared (never a glob), --toolchain-env
  retention    retention_decompose.py, --tasks pointed at the BUILD export; 30 cells, 0 REFUSED
  meter        each cell's own ctl/post-end-1.tsv (final_T, final_COST, cap_unit, cap)
  model        model_served_v3.py, from each cell's own served-<cell>.out; 30 of 30 claude-opus-5
  table        evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv
  verifier     RESULT-claude-blockO-2026-09-21-verify.py — re-derives every figure above FROM the table
               and asserts it against the BYTES of this document. No typed expectations.
```
