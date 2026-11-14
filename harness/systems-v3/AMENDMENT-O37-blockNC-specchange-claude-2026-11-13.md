# AMENDMENT — O37 BLOCK NC: BLOCK N's SIX × SPEC-CHANGE, CLAUDE LANE, B-CONTINUATION ON COPIES. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-13. The form of each cell is step g's (`AMENDMENT-stepg-opus-specchange-2026-09-29.md`, cited as "step g"):
## phase 2 on a COPY of a landed phase-1 cell, by `cell_copy_v3.py` then `customer.sh dispatch`, sources chosen by the rule of
## `AMENDMENT-specchange-taskshape-2026-09-09.md` §A3 (cited as "the rule"). The block's frame is block N's
## (`AMENDMENT-O37-nine-greenfield-claude-2026-09-25.md`, signed, cited as "block N"), carried BY CITATION as block N carries lane B's.
## A clause below that differs from either says so, and says why.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO PHASE-1 BASELINE IS RUN BEFORE IT IS SIGNED** (the rule is registered before the data
## it selects on). ⛔ **NO CELL FIRES BEFORE §C3's ITEMS ARE DRIVEN AND A RELEASE ADDENDUM NAMES THE EXPORT SHA, THE POOL AND EACH RECEIPT.**

**Why now.** The 11-09 remainder plan (seat brief `2026-11-09-bench-O37-REMAINDER-census-and-price.md` §4) put spec-change × the six FIRST
once their `B/` suites existed, ahead of the statement block (block T, which waits on the Captain's read of the six statements). As of
2026-11-13 all six `B/` suites have both halves, each read by a non-author (saltbench-systems branch `bench/o37-B-suite-fixes-2026-11-13`,
head db48cd51). The authority is block N's: the Captain's council word of 2026-09-25 (P3, quota no higher-priority work needs) and his
objective "fill out the 14 problems (greenfield only)".

---

## §C0 · THE INPUTS
```
  1  MODEL IDs     claude-opus-5 · claude-sonnet-5, block N row 1 unchanged (the served set per condition as there), read per cell from
                   message.model, head and sidechain apart. The release re-measures both with a zero-cell probe (block W §W2 item 5's form).
  2  n             3 per condition.
  3  POPULATION    24 conditions, 72 cells (§C1). Nothing is added, dropped or substituted.
  4  EXPORT        ONE bare sha of saltbench-systems, named in the release addendum, that (i) descends from both block-N release exports
                   (6087b54, 23485e5) and (ii) carries the six B/ trees at the blobs §C3 item 1 drives. One sha for every phase 2 and every
                   fresh phase 1, recorded per cell. CANDIDATE: 36ca596b (backup branch bench/o37-S-export-candidate-2026-11-13) = block W's
                   candidate 6615a7f8 + the B-suite branch db48cd51; each B/ tree equals that branch's, each G/ tree equals 3ea54f5's, and
                   no harness file differs from 6615a7f8. LinearScan's card is a merge of two disjoint edits: desk YM's scope line (in
                   23485e5, so in what block N's subjects read) and the B/ change-request edits (rows 42 and 58).
                   (Block W §W0 row 4 says "bare-master". That cannot hold here, because block N's exports are not on master.)
  5  CLIENT PIN    block N row 5 (lane B §Q0 row 5): the versioned client by absolute path, its sha asserted per launch. The release names
                   the version. If it differs from the version that ran a source's phase 1, the pair is reported with both versions.
  6  TASK TREE     the EXPORT's own tasks/systems-v3/<T>/B for phase 2, and <T>/G for any fresh phase 1 (§C2 rule 4).
  7  CAPS          phase 2: C2_USD $18.60 on the COPY's own slug (step g row 3; WU (a), AMENDMENT-OD-effort-matrix-2026-10-16.md:51:
                   C2 is compared against the whole slug's meter, and a copy's slug is its own path, so it meters phase 2 plus the
                   harness's sandbox probe). Fresh phase 1: C1_USD $37.21, W1_SEC 144,000. Both from the export's cost_caps.tsv (blob 80bd5d96
                   at 36ca596b). No cap is raised.
  8  ACCOUNT       P3: a pool the PM names for this block at release, from the day lines and never ahead of P1/P2 work, named per cell,
                   with `cells_account_check.sh --expect <that pool's identity>` reading OK before each fire (block N row 8's check).
  9  FIRE ORDER    §C4, one live cell per pool dir; a tripwire opens each model.
```

## §C1 · THE POPULATION — 24 CONDITIONS, 72 CELLS
Derived, not typed. Of O37's 216 conditions (census ADDENDUM 28 §AG1), 48 are spec-change × block N's six across four models; the Claude
lane's half is:
```
  problems   AES · BinomialHeap · LinearScan · Liveness · Luby · MaxFlow     block N's six, each with a B/ rung (both halves, read)
  models     claude-opus-5 · claude-sonnet-5
  arms       plain · salt-diet         field greenfield → spec-change         extras none
  ⇒ 6 × 2 × 2 = 24 conditions · × n 3 = 72 cells
```
**NOT in this block:** WHT and NTT × spec-change (16 conditions; no greenfield landing of either exists until block W runs), and the agy
lane's 24 (a sibling freeze). Each is a later dated block.

## §C2 · ⛔⛔ THE SOURCES — THE RULE, REGISTERED HERE BEFORE ANY BASELINE IS RUN
Each phase 2 continues a COPY of one of block N's cells of the SAME problem, model and arm (block N's cells root, the run box's
`~/cells-clb-n{o,s}-<problem>-<arm>/`; all 72 present, measured 2026-11-13 read-only). The rule, steps 1–6, applied per condition:
```
  1  The P1 baseline (the rule's §4: a cargo build and B/'s REGRESSIONS on the source's landed-1, zero model tokens) is run on ALL THREE of
     the condition's block-N cells.
  2  A cell is ELIGIBLE iff it carries landed-1 and p1_regressions_failed == 0. This is a validity filter, the same for every arm.
  3  n = 3 and each condition has exactly three block-N cells, so EVERY eligible cell is used, once, in ascending cell-id order (the
     rule's lowest-id step). No choice among eligible landings remains, so the rule's hazard (A3) has nothing to act on.
  4  ⚖️ Each SHORTFALL (3 − eligible) is filled by a FRESH PHASE 1: a new greenfield × none cell of that problem, model and arm, under
     block N's form at this block's export and C1. It gets ONE attempt. If it lands and its baseline passes, its phase 2 runs on a copy.
     If not, that cell is a REACH LOSS (lane B §CLB-R.2 clause 1), reported with the fresh cell's own end marker, and never retried.
     A fresh phase 1 is recorded beside block N, NEVER in block N's n, because block N's conditions are results of record at n = 3.
  5  The eligible count per arm is reported in every table that carries a phase-2 figure. It is arm-correlated (§C6 item 2).
  6  (No cell goes unchosen, so the rule's "not-chosen baselines" row is empty and says so.)
```
**What is already public, recorded so it cannot be quietly dropped later:** 10 of the 72 have no landed-1 tag (each is a block-N CAP-COST
cell): Opus LinearScan plain clbmrp01, Opus LinearScan salt-diet clbmrs01 · clbmrs02 · clbmrsr3, Sonnet AES salt-diet clbnas03, Sonnet
LinearScan salt-diet clbnrs01–03, Sonnet MaxFlow salt-diet clbnxs01 · clbnxs02. Two landed cells fail their own G/ suite at block N
(Sonnet LinearScan plain clbnrp01, clbnrp03, 8/9). Their baselines decide them like any other. Two conditions start with NO tagged
source (Opus and Sonnet LinearScan × salt-diet), so rule 4 fires three fresh phase 1s for each.

## §C3 · ⛔⛔ THE BUILD ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **THE SIX B/ SUITES RE-DRIVEN BY A NON-BUILDER ON THE EXPORT'S BYTES.** The lead built all six (block W §W2 item 1's change applies).
   Per task: Verus on `B/withheld/reference/solution.rs` at 0 errors; `run_tests.sh` on the reference in both forms (full pass); every
   clause and regression mutant run, with its pass count; `run_trace.sh` rejects every mutant column and accepts every reference column.
   The builder's figures are in each B/ README and its RUN file. A task whose drive disagrees is WITHDRAWN by name and its conditions are
   reported NOT-FIRED(TASK) by an addendum.
2. **THE 72 BASELINES** (§C2 step 1), after the signature, on the run box, read-only on the sources (each baseline runs on a COPY, never in
   a block-N cell: this repo's CLAUDE.md, a cell directory is evidence). The table of 72, its eligible count per arm, and the shortfall list
   are written into the release addendum.
3. **THE COPY FORM ON A DRY CELL PER MODEL:** `cell_copy_v3.py` then `customer.sh dispatch` on a copy of one eligible source, no model
   call. Read: `inbox/change-1.md` present and equal to the card's change-request section, B/'s interface in place, the copy's slug distinct
   from its source's, and the source cell byte-unchanged (a tree hash before and after).
4. **THE ACCOUNT CHECK** and **NO LEAK INTO A VIEW** (block N §N2 items 2 and 3): `check_withheld_leak_v3.py` over the export, which must
   now screen the six B/ withheld trees.
5. **THE ZERO-CELL PROBE** (block W §W2 item 5).

## §C4 · THE ORDER, THE TRIPWIRES
```
  models     interleaved as block N ADDENDUM 10's form; Opus's tripwire first.
  problems   ascending B/ reference size, the release's own `wc -l` of each B/withheld/reference/solution.rs.
  cells      per condition pair: plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3; a fresh phase 1 runs immediately
             before the phase 2 it feeds, in the same pool dir.
```
Tripwires, each ONE phase-2 cell, read by the lead and posted before its model continues: `T-NC-O` = Opus · first problem · salt-diet#1,
`T-NC-S` = Sonnet · first problem · salt-diet#1. The reading list is step g's (end-2 class, suite, regressions, clause tests, phase-2 $ on
the copy's slug, served head).

## §C5 · CAPS, PREDICTIONS AND THE PRICE — REGISTERED BEFORE ANY DATA
A cap-out is a RESULT and enters its median at the cap with `>=` (the rule's ADDENDUM 9, §J2).
Predictions, per model, where a miss is a result: (i) the eligible count is lower for salt-diet than for plain (block N's cap-outs fall
on salt-diet 9 of 10 times); (ii) within a condition, salt-diet's phase-2 CAP-COST incidence is ≥ plain's; (iii) CAP-WALL binds no cell.
⛔ No prediction about the phase-2 pass rate or a premium.
**The price**, derived by `AMENDMENT-O37-blockNC-specchange-claude-2026-11-13-price.py --caps <the export's cost_caps.tsv>`:
```
  phase-2 median per cell   Opus $13.36 (n = 19, the P1 wave, RESULT-p1-specchange-2026-09-10.tsv)
                            Sonnet $2.51 (n = 24, block SC, evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv p2_COST)
  estimate                  36 × 13.36 + 36 × 2.51 = $571.50 for phase 2
  fresh phase 1             at most 10 cells before the baselines (the 10 untagged) × C1 $37.21 = $372.10; more if a baseline fails
  ceiling                   72 × $18.60 + 10 × $37.21 = $1,711.30, plus each cell's overrun past its cap, plus $37.21 per further shortfall
```
The medians come from the pilot's five problems, not these six. Their direction of error is unknown. The first problem's six phase-2
cells per model re-cut the estimate before the rest fire.

## §C6 · CONFOUNDS
1. **A PHASE 1 SHARED ACROSS TWO CONDITIONS.** Every reused source is also a cell of record in block N's `none` condition. The two
   conditions are not independent, and no table sets them against each other as if they were.
2. **REACH IS ARM-CORRELATED, AND THE SOURCES ARE FILTERED BY IT.** Phase 2 exists only on a landing that passes its own regressions, so
   a phase-2 figure is over the cells that reached it (lane B §CLB-R.2 clause 1). The eligible count travels with every figure.
3. **TWO EXPORTS AND POSSIBLY TWO CLIENTS PER PAIR.** A reused source's phase 1 ran at block N's export and client, and its phase 2 runs
   at this block's. A fresh phase 1 runs at this block's for both. The pair's two shas and versions are recorded per cell, and fresh
   pairs are marked.
4. **ONE AUTHOR FOR THE SIX B/ SUITES, WHO IS THE LEAD.** §C3 item 1's non-builder re-drive is the control. A defect in a suite is a
   HARNESS finding, never an arm effect.

## §C7 · THE ONE FORK THIS FILE TAKES ON ITS DEFAULT (put to the Captain through the helm's pack)
Rule 4 fires three fresh phase 1s for each LinearScan × salt-diet condition, where block N's own three all capped. That is up to
6 × $37.21 = $223.26, likely spent for REACH losses. The alternative is to DECLARE those two conditions unreached at the cap, from block N's
record, without firing. That changes what the block asserts (a condition DECLARED on another block's cells), so it is his word.
**DEFAULT, written above: the registered rule unchanged (fire fresh, one attempt each).**

## §C8 · READING RULES, VOIDS, WHAT THIS BLOCK CANNOT ESTABLISH, DELIVERABLES
Reading rules: lane B §Q6 and §CLB-R, carried. Every premium is registered UNRESOLVED-UNDERPOWERED. Voids: block N §N7.
It cannot establish: 1. any magnitude or effect size; 2. anything about Opus versus Sonnet as models; 3. anything about a spec-change
reached from a phase 1 that did not land (none exists by construction); 4. anything about the O37 conditions outside §C1.
Deliverable (block N §N9): a result of record per model, with the census's O37 section re-cut in the same commit. Any public sentence,
and any claim about the method, is the Captain's.
