# RESULT — block SBS · `claude-sonnet-5` × brownfield × extras=statement · n=24
### bench, 2026-09-21. **8 conditions. ⭐⭐ THE SHARPEST EVIDENCE YET THAT THE PRIMARY SEPARATOR IS READING *GROWTH*: THE SALT-DIET ARM'S SURVIVAL FLOOR IS *HIGHER* THAN PLAIN'S.**
## 📌 The per-cell table is a FILE: `evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv` (24 rows, 25 columns).
## ⛔ Every figure below is derived from that table by `RESULT-claude-blockSBS-2026-09-21-verify.py`.

---
# §1 · WHAT RAN
`claude-sonnet-5` × **brownfield** × **statement** × {Crc32, FreeList, LRU, LZW} × {plain, salt-diet} × 3 reps = **8 conditions / 24 cells**, every condition at full n=3. ⛔ **Paxos × statement is INEXPRESSIBLE (§C4)** — 4 problems by design, not by loss.
```
  run_state   ENDED: LANDED 21 · ENDED: CAP-COST 3        suite   PASS 23 · BUILD-FAIL 1  (of 24)
  model       claude-sonnet-5, 24 of 24, derived per cell from its own served-*.out
  w1_fenced   COVERED 24 of 24 — every cell's W1 seed witness is fenced
```

---
# §2 · ⭐⭐ RETENTION — **`surv` DOES NOT MERELY OVERLAP HERE; THE SALT-DIET ARM'S FLOOR IS ABOVE PLAIN'S**
```
                      retained (DISJOINT)   surv                   growth (DISJOINT)    end_lines
  plain      n=12     0.611 .. 0.984        0.590 .. 0.995         0.89x ..  1.07x       50 ..  206
  salt-diet  n=12     0.101 .. 0.279        0.646 .. 0.882         4.66x .. 15.77x      263 .. 3027
```
⇒ 🔑 ***THE SALT-DIET ARM'S WORST SURVIVAL (0.646) IS HIGHER THAN THE PLAIN ARM'S WORST (0.590), AND ITS ENTIRE `surv` RANGE SITS INSIDE PLAIN'S — WHILE `retained` PUTS THE TWO ARMS IN DISJOINT BANDS AND CLASSES SIX OF ITS CELLS `REPLACED`.***
**`retained` is difflib's line-level similarity of END against SEED, symmetric in additions and deletions.** §B5's vocabulary (`REPLACED` = *"rewritten wholesale"*) is a claim about **what survived**. ⇒ ***ON THIS BLOCK THE TWO COME APART COMPLETELY: THE ARM `retained` CALLS "REWRITTEN WHOLESALE" IS THE ARM THAT PRESERVED MORE OF THE SEED.*** What it did was write **4.66×–15.77×** as much code around it — `end_lines` up to **3,027** against plain's ceiling of **206**.
⭐ **THIS IS THE STRONGEST FORM OF A SHAPE NOW SEEN IN THREE BLOCKS** — block SB §5 (Sonnet, brownfield, `none`), block O §3 (Opus, brownfield, `none`), and here (Sonnet, brownfield, `statement`). **In the first two `surv` overlapped; here it is strictly contained and its floor is higher.**
⛔ **`class` FOLLOWS `retained`, SO IT INHERITS THE SAME DEFECT:** plain is 12/12 `REPAIRED`, salt-diet splits 6 `REPAIRED` / 6 `REPLACED`. **Those six `REPLACED` cells are not cells that destroyed the seed.**

---
# §3 · CORRECTNESS AND THE CAP
```
                cells   CAPPED at $37.21   suite                       class
  plain         12      0  of 12           PASS 12 · BUILD-FAIL 0      REPAIRED 12
  salt-diet     12      3  of 12           PASS 11 · BUILD-FAIL 1      REPAIRED 6 · REPLACED 6
  all three capped cells are FreeList salt-diet, and TWO OF THEM STILL PASS 7/7:
    clbufs01  PASS 7/7 $38.58   ·   clbufs02  BUILD-FAIL 0/0 $37.46   ·   clbufs03  PASS 7/7 $37.60
```
⇒ **The arm-correlated cap appears for the THIRD time** (blocks SG, SS, and here): **3 of 12 salt-diet, 0 of 12 plain.** Direction known ⇒ salt-diet's figures are **FLOORS and LOWER BOUNDS**.
⛔ **The single non-PASS, `clbufs02`, is a CAPPED cell reading `0/0`** — a suite that never ran, not one that ran and failed. **In no correctness denominator.**
⚠️ **ONE `V1_bugs_fixed` READS `UNMEASURED`**, and that is the FreeList **MARGIN-1** rule working as designed: `RECORD-brownfield-givens` requires FreeList's single detecting test `exhaust_and_recover` to appear BY NAME in both the baseline and the end run, or V1 is UNMEASURED for that cell. **It is a declared absence, not a zero.**

---
# §4 · COST
```
                median COST   total COST   total T          capped
  plain         $1.54         $19.69        37,112,938      0 of 12
  salt-diet     $7.25         $188.69      637,280,728      3 of 12
  ratio         4.71x         9.58x         17.17x           <- ALL THREE ARE LOWER BOUNDS
```

---
# §5 · ⛔ WHAT THIS DOES **NOT** SAY
1. **It is one model, one field, one treatment.** Nothing here reaches Opus or the spec-change treatment.
2. **Salt-diet's correctness and cost are censored by an arm-correlated cap.** Both are bounds.
3. **`clbufs02` is in no correctness denominator**; 23/24 is over 23 scorable cells.
4. **`surv` is a LOWER BOUND** (matched lines only), as `retention_decompose.py` declares — which makes §2's claim *conservative*: the true survival gap can only be larger in salt-diet's favour, not smaller.
5. **Paxos is inexpressible under `statement`**, not missing.
6. **These are `plain` vs `salt-diet` arms**, not a claim about the salt METHOD.

---
# §6 · PROVENANCE
```
  cells      24, staged at ~/bench-dry/clb-score/ and scored as they landed
  scored by  score_claude_v3.py from 283362105d75's harness, --declared (never a glob), --toolchain-env
  retention  retention_decompose.py, --tasks at the BUILD export; 24 cells, 0 REFUSED; class and
             retained ASSERTED equal against the scorer's own values at join time, all 24 agreed
  meter      each cell's own ctl/post-end-1.tsv        model  model_served_v3.py, 24 of 24 claude-sonnet-5
  table      evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv
  verifier   RESULT-claude-blockSBS-2026-09-21-verify.py — re-derives every figure FROM the table and
             asserts it against the BYTES of this document. No typed expectations.
```

## §T · THE TOKEN FIGURE BESIDE EVERY DOLLAR FIGURE (desk KS, the Captain's order of 2026-09-11). Everything above is unedited.
bench (lead), 2026-10-01. The totals above already carried T. The MEDIANS and the per-cell dollars did not. `evidence/ks-tokens-2026-10-01/blocks_stepg.py`, which writes
`blocks_stepg.tsv`, reads the same rows of `evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv` this result was printed from. It
reproduces every median and total dollar figure above, and it prints each cell's T beside its final_COST. Capped cells' T is a FLOOR exactly as their dollars are (the cap stopped the session), and so is every median and total that includes them.
```
  plain      n=12   median $1.54 · 2,551,108 T      total $19.69 · 37,112,938 T
  salt-diet  n=12   median $7.25 · 18,401,035 T      total $188.69 · 637,280,728 T
```

## §C · CORRECTIONS FROM A SCORED REFUTER PASS (bench, 2026-10-19; `RESULT-argon-refuter-2026-10-19.md`, F1 · F3 · F4). Everything above is unedited.
Three defects in this file were found by a non-author refuter pass (Argon, objective O86) and confirmed by bench against
`blockSBS-cells.tsv` and `blockSBS-retention-decomp.tsv`. Each figure below is re-derived by `ratio-correction-2026-10-19-verify.py`.
1. **§2, "THE ARM `retained` CALLS 'REWRITTEN WHOLESALE' IS THE ARM THAT PRESERVED MORE OF THE SEED" is WRONG as stated.** Salt-diet
   preserved LESS of the seed: median `surv` 0.810 against plain's 0.980, and total `kept` 1027 against 1228 of 1332 seed lines each.
   What the tables support is the floor comparison in this file's title and §2's first sentence: salt-diet's worst `surv` (0.646) is
   above plain's worst (0.590). So the six `REPLACED` cells are not cells that destroyed the seed, and that point stands.
2. **§5 item 4, "the true survival gap can only be larger in salt-diet's favour, not smaller", does not follow.** `surv` is a lower bound
   in BOTH arms (the decomposition's line 5), so plain's worst cell can be undercounted too. The tables do not say which arm's undercount
   is larger. The floor comparison is a reading of two lower bounds, with no known direction for the true gap.
3. **§4's ratios are ratios of the ROUNDED figures, and two are wrong in the last digit.** Taken from the unrounded table: median COST
   ratio **4.70x** (printed 4.71x), total COST ratio **9.59x** (printed 9.58x); total T 17.17x is right. The header's "every figure below
   is derived from that table by `RESULT-claude-blockSBS-2026-09-21-verify.py`" was not true of the ratio row: that verifier derives no
   ratio. The bounds argument is unchanged.
