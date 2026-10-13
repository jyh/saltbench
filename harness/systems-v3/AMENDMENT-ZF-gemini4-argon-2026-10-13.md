# AMENDMENT — desk ZF: THE GEMINI 4 SET (`gemini-4-argon-high`) AND ITS SAME-DAY CONTROL (`gemini-3.8-flash-high`), THE PILOT'S CONDITIONS AT n = 3, agy LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-10-13. The Captain, 2026-09-30: *"Gemini 4 is released … When it arrives, we will need to test it."* and
## 2026-10-13: *"Gemini 4 Argon is now available on agy. Can we put it through the usual evaluation for whether it can join the fleet"*.
## Desk ZF (2): *"bench prices and pre-registers a Gemini 4 set on the SaltBench method at the pilot's conditions (the same problems and
## arms as the Gemini 3.x cells of record, n = 3)"*. A runner seat `gemini` is the HAND; bench is lead.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** No model call on this file before that signature and a release addendum naming the export.

**What this file carries by citation.** The lane's caps, confounds, reading rules, voids and deliverables are level 6's
(`AMENDMENT-gemini-level6-2026-09-16.md` §H3–§H8), as level 7 (`AMENDMENT-gemini-level7-2026-09-16.md`) and level 8
(`AMENDMENT-gemini-level8-2026-09-16.md`) amended them for brownfield/statement and spec-change. The fence is
`AMENDMENT-agy-ctl-fence-2026-10-13.md` + ADDENDUM 1 (binds from `95caaee`). Each holds unless a clause below says otherwise.

## §G0 · THE INPUTS
```
  1  MODEL        gemini-4-argon-high, EXACTLY as agy 1.3.4 prints it (the gemini seat's `agy models`, run box, 2026-10-13T23:17:54Z).
                  ONE id. Every Gemini 3.x cell of record is a -high variant (gemini-3.1-pro-high, gemini-3.8-flash-high), so -high is
                  the like-for-like id. -low and -medium are NOT in this file (the helm, 2026-10-13 16:18).
                  LABEL in every table: the id itself. It carries a name and an effort and no tier word, so no "Pro"/"Flash" column applies.
  1b CONTROL      gemini-3.8-flash-high, on the SAME export, the SAME 46 conditions, n = 3 (the helm, 2026-10-13 16:21). It is the one
                  3.x id agy still lists; gemini-3.1-pro is gone, so no same-day Pro control exists.
  2  SERVED       the model is DECLARED by us and corroborated by the client's echo, as on the 3.x lane (level 6 §H4). An echo is not
                  evidence of what was served, and the tables say so beside every figure.
  3  EXPORT       named in the RELEASE ADDENDUM: one saltbench-systems sha at or descending from 95caaee (the ctl/ fence), and
                  the task trees at that sha compared by tree hash with the ones the 3.x cells of record used, per problem.
  4  CHAIN        the lane's newest chains (chain-l7u, chain-l8u and the leg forms they carry), composed by the hand into one run
                  dir. WHICH chain fires each of the 46 conditions is the hand's to show in the PLAN (§G6); no level-7 cell of record
                  is greenfield, so greenfield legs are not assumed to exist in chain-l7u as it stands. desk VQ(b)+VT(b) (`APPLY.txt`, staged 2026-10-01 for exactly this chain's start) is APPLIED at that
                  start and never into a running chain. Its selftest runs in a FULL template, and its receipt goes in the release addendum.
  5  POOL         the agy subscription pool: one Google pool, separate from every Claude pool, with NO PM day line (the PM's
                  instruments carry the four Claude pools only). The pool reads as 5-hour and weekly percentages in the lane's QUOTA-LOG, and
                  agy is unthrottled by the Captain's ruling of 2026-09-17. The Claude-side cost (bench and gemini driving and scoring)
                  rides the PM's normal day lines. ONE agy supervisor at a time; the x86 lane's agy cells (O4) take the
                  pool first. The pool's cost per cell is UNMEASURED for this model, so it is priced at the tripwire (§G2), not guessed.
  6  SEQUENCING   behind O60 (the Claude lane's x86 resume and its batch score), by the helm's order.
```

## §G1 · THE POPULATION — 46 CONDITIONS × 2 MODELS, 276 CELLS
The conditions are exactly the DONE conditions of the Gemini 3.x cells of record in `CELLMAP-correctness-tables-v3-2026-10-01.tsv`:
5 problems (Crc32 · FreeList · LRU · LZW · Paxos) × greenfield/brownfield × plain/salt-diet × none/statement/spec-change, minus the
harness's brownfield × spec-change. That is **46 per model, the same 46 for both 3.x models** (each also carries 4 INEXPR rows,
which this set does not run). **n = 3 per condition per model ⇒ 138 Gemini 4 cells + 138 control cells = 276**; a spec-change cell has two phases.
**INTERLEAVED BY CONDITION:** each Gemini 4 cell is fired adjacent in time to its control cell on the same condition and replicate, so a
pair shares client, harness, pool state and time of day.

## §G2 · THE ORDER, THE TRIPWIRES AND THE PRICE
- **Tripwire 1** = Crc32 · greenfield · none · plain #1, as a PAIR (one Gemini 4 cell, one control cell). **Tripwire 2** = the same
  condition, salt-diet #1, as a pair. Four cells, and the lead reads each before the set continues: landed or not, the served-model echo, turns, wall, tokens (agy meter T), and the
  pool reading before and after. **The set's price is written into an addendum from those four cells**, and from them alone.
- Then greenfield (none · statement), brownfield (none · statement), then spec-change, condition by condition, n = 3 each.
- **The price basis this file can state now, from the 3.x cells of record** (`evidence/v3-cost-tables-2026-09-28/agy-steps-raw.tsv`):
```
  gemini-3.1-pro-high     164 phases · 60.4 h wall · 1,139 M tokens (meter T)
  gemini-3.8-flash-high   168 phases · 42.2 h wall · 2,285 M tokens
```
  ⇒ Order of magnitude: **~40 h of serial wall for the 138 control cells** (Flash's own figure) **plus 40–60 h for the 138 Gemini 4 cells**
  if it behaves like either 3.x model. That describes the 3.x models, not a prediction for Gemini 4.
- **Stop rule.** If the tripwire price puts the set past the ZF review date (2026-10-28) on the pool this lane can draw, the lead posts that
  with an order (spec-change last, then brownfield/statement) before any cell beyond the tripwires. **A cut removes WHOLE CONDITION PAIRS,
  never one model's arm alone. n is never reduced quietly**, and a condition left short is reported short.

## §G3 · PREDICTIONS — REGISTERED BEFORE ANY DATA
None about direction. The deliverable is descriptive. The PRIMARY comparison is the same-day pair: per condition, landed and scored (the
withheld suite) for Gemini 4 beside its control. The 3.x cells of record are a HISTORICAL column, labelled as such. Every figure names its file. **No p-value and no claim that the method helps or hurts.**

## §G4 · CONFOUNDS — level 6 §H4 carried, plus these, each stated wherever a comparison is
1. **(The HISTORICAL column only.) The 3.x cells of record are a PATCHWORK:** one condition's 3.x cells came from different levels with different machinery. For example,
   Pro greenfield × none is levels s3 and l6v, and Flash brownfield × none is l6v and l7. This set runs every condition on ONE export.
   ⇒ A 3.x-of-record ↔ 4 difference on a condition confounds the model with the harness version. The same-day pair does not have this
   confound, which is why it is primary.
2. **The client moved** (agy 1.3.3 → 1.3.4 on 2026-10-13, and older for the earlier levels). This is the same confound, for the historical
   column only; within a pair the client is shared. If agy moves mid-set, every pair names its client version.
3. **The fence moved:** every 3.x cell ran with ctl/ subject-writable. No 3.x subject wrote ctl/ (`evidence/agy-ctl-census-2026-10-13/`),
   so this is a difference in the possible, never in what was measured.
4. **The control is a FLASH model:** gemini-3.1-pro is no longer on agy, so the same-day control is gemini-3.8-flash-high. A pair compares
   Gemini 4 with today's Flash, never with Pro. The only Pro figures are the historical column's.

## §G5 · WHAT THIS SET CANNOT ESTABLISH
Whether Gemini 4 is better or worse than 3.x in general: the pair compares it with one Flash model on this harness, descriptively. Nothing about the
other two effort variants. Nothing about the O29 qualification (refuter, executor, prover), which is gemini's separate act.

## §G6 · WHAT THE HAND DELIVERS
Before the first call: the composed run dir, the APPLY receipt (its selftest in a full template), and a PLAN printed by the chain
naming all 276 cells in their interleaved order, with the chain that fires each, which the lead reads, checking the plan as well as the run. After each tripwire: the five reads in §G2. At
the end: the harvest in level 6 §H8's form, plus the withheld-suite score per cell.
