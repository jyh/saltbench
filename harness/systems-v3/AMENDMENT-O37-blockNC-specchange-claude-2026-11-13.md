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
  estimate                  36 × 13.36 + 36 × 2.515 = 480.96 + 90.54 = $571.50 for phase 2 (Sonnet's median is 2.515 unrounded)
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

---
# ✍️ SIGNED — the helm (210th head), 2026-11-13 21:29 PST, bus offset 101,918,579: blob 7ff00c7bfe82 at head ac515f783927, read whole (142 lines):
COMPLETE WITH ONE LOW AND LIMITS. The LOW (§C5's printed factors gave $571.32) is fixed above by printing Sonnet's median to the precision used,
no clause moved. The limits it named: price.py not run by the signer; step g, the rule, block N and lane B not read; the CAP-COST ids, the 72
cells and export 36ca596b not checked. §C7 stands on its default (the helm, XF; a ledger line in the 11-14 pack).

---
# ADDENDUM 1 (2026-11-13, bench) — §C2 STEP 1's INSTRUMENT IS THE G RUNG (taskshape B3). WRITTEN BEFORE ANY BASELINE IS RUN.
**The defect.** §C2 step 1 cites "the rule's §4" and glosses it as "a cargo build and B/'s REGRESSIONS on the source's landed-1", and step 2
reads `p1_regressions_failed == 0`. The rule's §4 first sentence was REPLACED by its own ADDENDUM B3 (taskshape, "THE CORRECTED INSTRUMENT"):
on a phase-1 tree `B/run_tests.sh` cannot build, because the clause tests name functions a phase-1 landing does not define. Measured at the
export candidate 36ca596b, each of the six `B/run_tests.sh` builds ONE crate from the submission and the whole B driver, and on a build
failure prints `TESTS 0/0` and exits 3 with no REGRESSIONS line. So the gloss as signed can produce no `p1_regressions_failed` at all, and a
reader that took the absent line as 0 would make every cell eligible by accident (B3's own finding).
The baseline drive runs `B/run_tests.sh` on ONE source as its control and must read exit 3 with no REGRESSIONS line; if it builds, this
addendum's premise is wrong and the drive stops.
**Registered, replacing step 1's gloss and step 2's field (the citation already resolves here, since §4 as amended IS B3):**
```
  1  The P1 baseline is the G rung's run_tests.sh (the EXPORT's tasks/systems-v3/<T>/G/run_tests.sh) on the source's landed-1 tree,
     run on a COPY, zero model tokens. Recorded per cell: p1_base_passed / p1_base_total from its `TESTS <passed>/<total>` line
     (⛔ POLARITY: PASSED, not the B runner's FAILED), the runner's exit code, and p1_solution_sha256.
  2  ELIGIBLE iff landed-1 exists AND the runner exits 0 AND p1_base_passed == p1_base_total > 0. An exit 3 or 4, a missing TESTS line, or
     a 0/0 is UNMEASURED and NOT ELIGIBLE, never a pass.
```
**What this changes in the expected outcome, said before the data:** §C2 already names two landed cells that fail their own G suite at block
N (Sonnet LinearScan plain clbnrp01, clbnrp03, 8/9). Under this instrument they are expected INELIGIBLE, so that condition expects two
fresh phase 1s under rule 4. The upper bound on fresh phase 1 (§C5) is unchanged in form: it is re-priced from the 72 baselines in the
release addendum, and §C7's ask is untouched.
**Why not the literal gloss with a separate build:** the B/ base suite is not always G's verbatim (LinearScan's B regressions call
`allocate(prog, k, 0)` against B's widened interface), so B's REGRESSIONS cannot be compiled against a phase-1 tree for every task. The G rung
is the phase-1 landing's own base suite, the reading step g ADDENDUM 1 item 2 took for its seven cells.
**Signature.** This changes the instrument of a signed clause, so it is put to a non-author. The baselines are zero-token reads on copies
whose eligibility rule is registered here first. They run after this addendum is on origin, and a reader who rejects it gets them re-read
from the same run logs (each log carries the full runner output).

**✍️ ADDENDUM 1 SIGNED** — the helm (210th head), 2026-11-13 21:50 PST, bus offset 101,940,703: blob 61e3fe810d50 at head 6da31ba03f81 (also
at 23ccd261, which adds only evidence/), COMPLETE WITH LIMITS. It verified at the object that 6da31ba0 is an ancestor of the baselines
commit 23ccd261 and did not open the baseline results before signing. Its limits: taskshape B3 and step g ADDENDUM 1 taken as cited; the
control's run not read; the push time of 6da31ba0 against the drive's start not checked.

---
# ADDENDUM 2 (2026-11-13, bench) — RELEASE, ⛔ DRAFT: NOT A RELEASE UNTIL ITEMS 4a AND 5 ARE FILLED AND THE POOL IS NAMED
**Export: saltbench-systems `ee7450ce`** (the NC stager: block W's stager 0916ef9a + the B-suite + NCO/NCS copy blocks + NFO/NFS fresh blocks,
`NC_SOURCES` 72 rows, `--roots --freeze NC` = 30 roots). Its tasks/ tree is byte-identical to 36ca596b's (git diff empty; the six tasks'
trees AES 00b919ce · BinomialHeap df6427a9 · LinearScan a3c8ae15 · Liveness 143296d6 · Luby 6db3c763 · MaxFlow 5b89c4df at both), so
items driven on 36ca596b's task bytes hold for this export.
**§C3 receipts:**
1. MET — systems (built none of the six), bus offset 102,018,867, on ee7450ce: Verus reference 0 errors for all six; tests on the reference
   in both forms full pass; every mutant fails with its pass count, 46 of 46 equal to the builder's RUN files; run_trace rejects every
   mutant column and accepts every reference column. Nothing withdrawn. Reported as stated: the margin-1 mutants (AES AcceptsBadPadding;
   Liveness InPlaceSweeps; BinomialHeap DeleteRefusesMax; LinearScan AlwaysReservesScratch, ArgsReversed, ResultFromR1; MaxFlow's five
   checker mutants), each killed by its own clause test; Verus panics on the plain-Rust TRIVIAL control of five tasks (never a Verus file;
   its only role is (d), where it kills 0 everywhere).
2. MET — `evidence/blockNC-2026-11-13/` (commit 23ccd261, after ADDENDUM 1 at 6da31ba0): 72 baselines, 62 reproduce block N's G figures
   exactly; 60 eligible (Opus plain 17, salt-diet 15; Sonnet plain 16, salt-diet 12); 12 shortfalls ⇒ 12 fresh phase 1s; no source changed;
   the B-runner control exited 3.
3. MET — the copy form dry on 36ca596b (ncdry001 from clbmap01, ncdry002 from clbnap01; change-1.md = preamble + the card's section;
   interface == B/interface.rs; sources' tree hashes unchanged), and the stager driven dry through ee7450ce on the run box
   (`~/bench-dry/nc-stagedry-2026-11-13/`: 30 roots; NCO copy + phase-2 dispatch; NFS fresh build; NFS n=1 refused; source unchanged).
   `clb_blockNC_selftest.sh` 31/31 at ee7450ce, the reference fails 14/14, a mutant reddens 8.
4. (b) NO LEAK — MET at ee7450ce: `check_withheld_leak_v3.py` CLEAN, 343 identifiers across 13 tasks, every positive control fired,
   1,372 view reads, 0 in any view; its --selftest 3/3 (run-box `~/bench-dry/nc-leak-ee7450ce-2026-11-13/leak.out` sha256/16
   61232087f298b393).
   (a) THE ACCOUNT CHECK — ⛔ OPEN: owed on the pool the PM names.
5. THE ZERO-CELL PROBE — ⛔ OPEN: owed on that pool.
**Pool:** ⛔ OPEN (the PM's cut). **Order:** §C4 as registered. Nothing fires before this heading loses its DRAFT mark.
