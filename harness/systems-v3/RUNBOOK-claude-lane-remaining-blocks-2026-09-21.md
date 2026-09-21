# RUNBOOK — the five harvested Claude-lane blocks that have no result of record
### bench (lead), 2026-09-21. **Written because 43 of the pilot's 75 OWED conditions are ALREADY RUN and are waiting on analysis, not on the lane.**

## ⛔⛔ THE FACT THIS RUNBOOK EXISTS FOR
The Captain asked whether the pilot is finished. The matrix reads `DONE 109 · OWED 75 · BLOCKED 0 · INEXPR 16`.
**The 75 are not 75 runs.** Partitioned at the object 2026-09-21 03:3xZ:

```
  (a) blocked on the UM cut / SC driver    10 conditions  (30 cells)  block SC — SKIPPED in the work list
  (b) blocked on the blanked credential     1 condition   ( 2 cells)  reps 02/03 of one OS condition
  (c) the AGY lane, blocked on level 8     21 conditions              mode B unreleased; T2 under repair
  (d) RUNNABLE NOW on the lane              0 conditions
      ⇒ 43 conditions / 129 cells ARE RUN, HARVESTED AND METERED with NO RESULT OF RECORD.
  ---------------------------------------------------------------------------------------------
  10 + 1 + 21 + 43 = 75
```
⇒ 🔑 ***"THE WORK LIST IS EXHAUSTED" AND "THE CAMPAIGN HAS NOTHING RUNNABLE" PRODUCE AN IDENTICAL IDLE
CHAIN AND MEAN OPPOSITE THINGS.*** The third case is the one we are in: the list is exhausted **because the
cells ran**. What is missing is the write-up, and it costs **zero quota, no credential and no width**.

## ✅ THE FIVE BLOCKS — COUNTS AND MODELS, BOTH DERIVED, NEITHER TYPED
Cell counts from the work list's own block census; **models from `model_served_v3.py`, which reads each
cell's own `served-<cell>.out` receipt** and refuses rather than picks:

```
  block  cell-id letter  cells harvested / total  model SERVED (derived)   conditions
  O      o                30 / 30                 claude-opus-5            10
  SG     g                30 / 30                 claude-sonnet-5          10
  SS     s                24 / 24                 claude-sonnet-5           8
  SBS    u                24 / 24                 claude-sonnet-5           8
  OS     t                22 / 24                 claude-opus-5             8   (2 cells flagged, (b) above)
  ------------------------------------------------------------------------------------
                         129 cells                                         44
  (43 are fully harvested; the 44th is the OS condition holding the two flagged cells.)
⚠️ SG READS 29 IN THE RUN DIR AND IS 30: `clbglp01` was fired and harvested BY HAND (the work
  list's own header says so) and IS staged for scoring. Do not report SG at n=29.
```
⛔ **DO NOT TAKE THE MODEL FROM THE BLOCK NAME.** `ADDENDUM 12` had to correct block SB's attribution after
the fact precisely because the 24-column table carries no model column. Run the tool.

## ⚖️ THE PIPELINE, TAKEN FROM `RESULT-claude-blockSB-2026-09-19.md` §9 — THE ONLY BLOCK THAT HAS BEEN DONE
```
  scorer        score_claude_v3.py + brownfield_rewrite_class.py
                ⛔ NOT IN THIS REPO — they live in an EXPORT tree's harness/systems-v3.
                   Use the harness of the export the CELLS WERE BUILT FROM.
  --tasks       the COMPOSED export (blockSB §2b), NEVER the build export alone: the suites and the
                brownfield seeds come from DIFFERENT trees and a single --tasks root feeds BOTH consumers.
  --declared    a file listing the block's cells, one per line. ⛔ NEVER A GLOB — a glob silently admits a
                cell that was built, refused and never fired.
  --toolchain-env   ~/cells/toolchain.env
  retention     retention_decompose.py (IS in this repo) for surv/growth.
                ⛔ POINT IT AT THE BUILD EXPORT — this is the standing hazard on this step.
  meter         each cell's own frozen meter.
  join          the three receipts, with class/retained ASSERTED EQUAL across two independently
                produced sources at join time. The producing script imports the classifier and fails
                otherwise — it does not re-implement it.
  NEW           model_served_v3.py — add `model_served` as a column, and give -verify.py an arm that
                reads it against the result's prose. This is the durable fix block SB's §9c names.
```

## ⛔⛔ ⏱️ COST — **CORRECTED BEFORE THIS FILE WAS EVER COMMITTED, AND THE FIRST VERSION WAS WRONG IN THE EXPENSIVE DIRECTION**
This section first read *"~80 min per 30-cell block ⇒ roughly 5–6 hours of UNATTENDED run-box time for all
five"*, derived from block SB's two scoring executors. **THAT IS FALSE, and obeying it would have sent the
next head to fire passes that have already run.**

**MEASURED AT THE OBJECT 2026-09-21 03:4xZ, ON THIS BOX:**
```
  ~/bench-dry/clb-score/        160 staged cell dirs, mtime 02:19:54Z (when the last cell landed)
                                each holds  cells/ · declared.txt · score.out
  SCORED ROWS                   160 of 160 cells carry a scored row FOR THEMSELVES in their own score.out
                                b 30 · g 30 · o 30 · s 24 · t 22 · u 24
  ~/bench-dry/clb-score-trees/  5 staged export trees, each with 16 run_tests.sh — suites AND seeds present
```
⇒ 🔑 ***THE CORRECTNESS SCORING IS ALREADY DONE FOR EVERY HARVESTED CELL. THE REMAINING WORK IS A JOIN AND
A WRITE-UP, NOT A RUN.*** The harvest stages each cell and scores it as it lands; nobody has to re-fire
anything. **Machine time owed: ~0. What is owed is the retention decomposition, the meter join and the prose.**

⚠️ **AND THE FALSE ALARM THAT NEARLY WENT IN HERE, kept because it is the reusable part:** a probe for
`<problem>/brownfield/G/run_tests.sh` reported **suites ABSENT in all five problems**, which reads as
*"these scores were produced against a missing suite"* — the most alarming sentence this file could carry.
**The suite is at `<problem>/G/run_tests.sh`; the probe was one directory too deep**, inside the SEED
directory. ⇒ ***A WRONG PATH IS AN ACCURATE MEASUREMENT OF SOMETHING ELSE.*** The disconfirming evidence was
already in hand: `score_claude_v3.py`'s `run_suite` REFUSES a verdict whose names do not account for its
`TESTS p/t` line, so a tree without its suite yields `UNPARSED` and never `PASS 6/6` (block SB §2b drove
exactly that). **A plausible number IS the evidence the suite ran.**

## ⚓ THE ORDER, AND WHY
1. **O** — 10 conditions, 30/30 harvested, and it completes the `brownfield × none` pair against block SB
   across both Claude models. **The largest single move available and the one with a direct comparator.**
2. **SG** — 10 conditions. ⚠️ 29 of 30: name the missing cell in the result rather than reporting n=30.
3. **SS** · 4. **SBS** — 8 each.
5. **OS** — 8, but **one condition is incomplete until the credential returns**; write it as 7 + 1 declared.

## ⛔ WHAT THIS RUNBOOK DOES NOT DO, SAID PLAINLY
- **No scoring pass was fired.** At the time of writing the author judged it wrong to start an unsupervised
  5-block pass onto the Captain's stated top priority without being able to watch its first landing — a
  wrong `--tasks` root writes a *corrupted table of record*, which this repo's own CLAUDE.md distinguishes
  from a lost experiment.
- **43 is a count of conditions whose CELLS ARE HARVESTED. It is not a prediction that 43 will score DONE.**
  A result of record may find a block short, faulted or unpoolable, and that block returns to OWED with a
  reason. `ADDENDUM 6` cost four conditions exactly that way.
- **The composed-export recipe is read from block SB's §2b and was NOT re-derived here.**
