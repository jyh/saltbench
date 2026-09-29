# AMENDMENT — STEP g: SEVEN OPUS SPEC-CHANGE CELLS BRING SIX CONDITIONS FROM n < 3 TO n = 3. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-09-29. The Captain, council 2026-09-29, ask 2 (v3 step g), as he typed it: *"pleae fire"*. The ask put to
## him: *"bring the 10 conditions at n < 3 to n = 3 … This is the ONLY quota spend in v3, about 9 points"* (the helm's council pack for that sitting, ask 2).
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES BEFORE §G2's ITEMS ARE DRIVEN AND A RELEASE ADDENDUM NAMES THE EXPORT SHA.**
## Signature and release are two acts, as in lane B and block N.

**What this file is.** A new block under `AMENDMENT-claude-lane-B-2026-09-16.md`, carrying that freeze's machinery BY CITATION: the
preflight (§Q3.4, with ADDENDUM 5's one-live-cell-per-pool rule), the confounds (§Q5), the reading rules (§Q6), the void table (§Q7) and
the deliverables (§Q9). The FORM of each cell is the one the cells it pools with used: `AMENDMENT-specchange-taskshape-2026-09-09.md`
(B-CONTINUATION: phase 2 on a COPY of a landed phase-1 cell, the P1 baseline taken before phase 2). A clause below that differs from
either says so and says why.

---

## §G0 · WHICH OF THE TEN THIS BLOCK FIRES, AND WHY ONLY SEVEN CELLS
Census ADDENDUM 25 §AE2 lists ten DONE conditions at n < 3. Four of them close on records that already exist, at zero spend, and are
NOT in this block (the helm concurred, bus 2026-09-29 10:54:01):
```
  gemini-3.1-pro-high  Crc32 × salt-diet × statement     s3ct01 · s3ct02 · s3ctk01          n = 3   RESULT-stage3-2026-09-12.md ADDENDUM 1
                       FreeList × plain × none           s3fp01 · s3fpk01 · s3fpk02         n = 3     §R2–§R3 (signed 2026-09-17); limit §R6.5:
                       FreeList × plain × statement      s3fq01 · s3fq02 · s3fqk01          n = 3     the top-ups ran on export s2k and another client
  claude-sonnet-5      LRU × plain × none                clbglp01 · clbglp02 · clbglp03     n = 3   clbglp01 RAN and was SCORED (blockSG :15);
                                                                                                    restored by its own dated addendum (served model
                                                                                                    read from its transcripts, 62 of 62 claude-sonnet-5)
```
The census addendum that records those four is its own act, with those records beside it. **This block is the other six.**

## §G0′ · THE INPUTS
```
  1  MODEL          claude-opus-5, served per condition as the P1 spec-change wave's cells were (head claude-opus-5; the client's own
                    subagents as the client chooses). Read per cell from the transcripts' message.model, head and sidechain apart.
  2  n              the six conditions' shortfall only: 7 cells (§G1). Nothing is added, dropped or substituted.
  3  FORM           B-CONTINUATION on a COPY (`cell_copy_v3.py`), `customer.sh dispatch`, then phase 2 under the watcher. ⛔ NOT
                    `clb_fire --phase 2` on the source cell: block SC measured that its C2 cap is compared against the WHOLE cell's
                    meter (RESULT-claude-blockSC-2026-09-21.md §4), and an Opus phase 1 alone costs $10–38, so an in-cell phase 2
                    would cap before its first turn. A copy has its own path, so its own meter slug, and C2 meters phase 2 alone,
                    which is how the P1 wave ran (RESULT-p1-specchange-2026-09-10.tsv: capped cells stopped at $18.62–$19.78).
  4  EXPORT         ONE bare-master sha of saltbench-systems, named in the release addendum BEFORE the first cell, that descends from
                    9d87318 (block N ADDENDUM 14's export) and carries §G2 item 1. One sha for all 7 cells, recorded per cell.
  5  CLIENT PIN     lane B §Q0 row 5, unchanged: 2.1.259 by absolute path, its sha asserted per launch. ✅ MEASURED: every one of
                    the 19 P1-wave phase-2 transcripts and all six §G1 gf-topup-1 sources carry version 2.1.259.
  6  TASK TREE      the EXPORT's own tasks/systems-v3/<T>/B. ✅ MEASURED at the run box: the B trees of FreeList · LRU · LZW ·
                    Paxos hash IDENTICALLY in export 912c787 (the P1 wave's `_bin`) and export 9d87318 (c61a47d8f364b387 ·
                    7e25be8d6dbc1a7e · d4d148b23bc71d14 · 1232ceca1f5c2028, sha256 over the sorted file hashes).
  7  CAPS           the P1 wave's, unchanged: C2_USD $18.60 on the copy's own meter; no turn cap (the Claude lane arms none).
  8  ACCOUNT        a pool the Captain's ruling names (one of the two new-week pools it names), NAMED PER CELL, `cells_account_check.sh --expect
                    <that pool's identity>` reading OK before each fire. Chosen at each fire from the pools' day lines.
  9  FIRE ORDER     §G3, one live cell at a time.
```

---

## §G1 · THE POPULATION — 7 CELLS, SOURCES CHOSEN BY THE REGISTERED RULE BEFORE ANY OF THEM IS SCORED
The rule is `AMENDMENT-specchange-taskshape-2026-09-09.md:333–348`, applied with steps 2–6 unchanged. What is new is step 1's POPULATION: the rule's step 1 names the twelve LZW landings
of 2026-09-09, and here it is every candidate below, from three roots. (2) a phase-1 landing is ELIGIBLE iff its own
base suite passes (the G rung, B3); (3) among an arm's eligible UNUSED landings, the LOWEST CELL ID lexicographically; (4) an arm with no
eligible landing has its phase 1 fired fresh, and says so; (5) the eligible count per arm is reported; (6) the not-chosen are recorded.
**The candidate pool is every Opus greenfield × none LANDED phase-1 cell on the run box for the task × arm, not already a phase-2 source**,
censused at the object 2026-09-29 over `~/cells-matrix1`, `~/cells-n3-topup`, `~/cells-gf-topup-1`:
```
  condition (all greenfield)        need   unused LANDED candidates (id order)       eligibility (G rung)            chosen, if eligible
  FreeList × plain     × spec-chg    1     db0847aa · n301free                        n301free PASS 7/7 ; db0847aa §G2   db0847aa
  FreeList × salt-diet × spec-chg    2     783df512 · c17630f0                        both §G2                          c17630f0 · 783df512
  LRU      × plain     × spec-chg    1     61d2fda3 · n302lru                         n302lru PASS 16/16 ; 61d2fda3 §G2  61d2fda3
  LZW      × plain     × spec-chg    1     c34012e0 · d91f137b                        both PASS 8/8 (taskshape B4)      c34012e0
  Paxos    × plain     × spec-chg    1     bc7997bd · n303paxo                        n303paxo PASS 17/17 ; bc7997bd §G2 bc7997bd
  Paxos    × salt-diet × spec-chg    1     d9998c97                                   §G2                               d9998c97
```
Eligibility figures are from `RESULT-posthoc-correctness-verdicts-2026-09-09.tsv` (lines 30, 39–41) and taskshape B4. The six
`gf-topup-1` candidates carry no G-rung verdict on any ref, so the baseline is §G2 item 2, and **if a chosen candidate is INELIGIBLE the
next eligible id in the same row is taken, by the same rule, and the release addendum says so.** A row with no eligible candidate fires
its phase 1 fresh (rule 4), under a release addendum of its own; this block does not pre-build that path.
📌 **The gf-topup-1 cells are Opus (requested `claude-opus-5` · effort `high` in the root's CELLS.tsv, the same two values as the matrix1 and
n3 top-up rows; served head `claude-opus-5` in all six transcripts), card_extras `none`, ENDED LANDED, and have NEVER been dispatched
(no `ctl/customer.log`, no `end-2`).** Their `statement-1` git tag on the three salt-diet cells is the salt arm's own artefact, not a
statement build (taskshape A2). They appear in no result of record in this repository (0 hits for any of the six ids on origin/main,
against a positive control, `n301free`, that fires).

## §G2 · BUILD ITEMS, ALL DRIVEN BEFORE THE RELEASE ADDENDUM (zero model spend)
1. **The stager and the fire script learn this block.** `clb_stage.sh` and `clb_fire.sh` gain one block row (Opus, greenfield, the copy
   form) whose staging is `cell_copy_v3.py --src <§G1 source> --dst-root <this block's root> --dst-id <its clb id>` rather than a fresh
   build, and whose fire is `--phase 2` on that copy. Red-first: a mutant that stages a FRESH build for this block, and one that fires
   phase 2 on the SOURCE path, each refused. The block's root is created by `--roots` in a quiet window (the render-time-glob law).
2. **The P1 baseline on every chosen source** (the G rung's `run_tests.sh` on the landing, zero tokens), and on the not-chosen
   candidates in each row (rule 6). Results in the release addendum, per cell.
3. **The pooling control.** The scorer that scores these 7 re-scores ONE P1-wave cell per task (FreeList `188f422b`, LRU `3bdcbcbd`,
   LZW `93323249`, Paxos `60a056e6`) under the same environment and must reproduce each one's published verdict and test count. The
   pooling claim is that measurement, and the B-tree identity of §G0′ row 6, never an assertion.
4. **The price** (below) re-read against the chosen pool's day line on the morning of the first fire.

## §G3 · FIRE ORDER
One cell at a time; the next fires when the previous has an end marker. The first cell is the TRIPWIRE: its launch, its sandbox probe,
its served model and its first meter read are read before the second fires. Order: `c34012e0` (LZW plain; the one source already in the
record as eligible) → `61d2fda3` → `db0847aa` → `bc7997bd` → `d9998c97` → `c17630f0` → `783df512`.

## §G4 · THE PRICE, AND WHAT IT IS BOUNDED BY
Phase 2 alone is metered. P1-wave medians, uncensored cells only: plain $13.52, salt-diet $9.99 (RESULT-p1-specchange-2026-09-10.md §4);
the cap binds at $18.60 and the P1 wave's capped cells stopped at $18.62–$19.78. **Worst case: 7 × $19.78 = $138.46.** At the measured
0.02794–0.03172 pt per USD (the lead's block-N price re-cut of 2026-09-26) that is **3.9–4.4 points**, inside the
~9-point line he ruled. No fresh phase 1 is priced here; rule 4, if it fires, is its own addendum and its own price.

## §G5 · CONFOUNDS, DECLARED BEFORE ANY CELL
1. **PHASE-1 SELECTION, AND THIS IS THE ONE THAT MATTERS.** Lane B §CLB-R.2 clause 5 forbids top-up re-fires for block SC because
   re-firing until n selects again on the property that stopped it. **This block is a top-up, ordered by the Captain's word, and it does
   select: every source is a phase 1 that LANDED.** That is true of every phase-2 cell in the pilot (phase 2 needs a landing), and it
   falls harder on salt-diet. In cells-matrix1, FreeList salt-diet fired 4 phase-1 cells: 2 CAP-COST (161b5a34 · de4de8f2), 1
   FAILED-BOOTS (823de693), 1 LANDED (f33c7e65). Paxos salt-diet fired 4: 1 CAP-COST (6fc49f7c), 1 FAILED-BOOTS (7fa6c322), 2 LANDED.
   The plain rows of the same tasks lost no cell to the cap there. ⇒ **Each of the six conditions reports, beside its n = 3, the phase-1 REACH of its arm on this task across
   all three roots** (landed / fired), per clause 1 and 4 of §CLB-R.2. A reader then sees the selection, not a clean n.
2. **THREE SOURCE ROOTS AND TWO DATES.** Sources from `gf-topup-1` (built 2026-09-11) sit beside P1-wave sources from `cells-matrix1`
   (2026-09-08) in the same condition. Same model, effort, client, B tree; different phase-1 export and date. Declared per cell.
3. **THE ACCOUNT.** The P1 wave's phase 2 ran on one run account (`ctl/account.tsv`); these run on the pool named per cell. The pilot's
   cells already span accounts (RESULT-n3-topup-2026-09-09.md §1b). Declared per cell.
4. **THE WATCHER.** `cell-watch.sh` differs between export 912c787 and 9d87318 (154 diff lines: the ACCOUNT class, the phase-aware
   liveness census, later end classes). The subject never sees the watcher, and it decides when a cell ENDS. Any cell whose end class
   exists only in the newer watcher is reported with that class named. `customer.sh` differs only by an opt-in `--fold-bus` (the agy
   driver's, not passed here) and a refusal for card extras (none here), so its Claude-lane behaviour is unchanged.
5. **THE LZW CONDITION'S OWN COMPOSITION, INHERITED AND NOT REPAIRED HERE.** Its two cells of record are `93323249` (plain-bare phase 1)
   and `22ee7d33` (plain-STATEMENT phase 1): the specchange-1 wave pooled both builds under "plain" (CELLMAP rows 70–71). This block adds
   a plain-bare source; the condition's three cells will be two bare and one statement-built, and the result says so.
6. **INTERRUPTED TURNS IN THE SOURCES' PHASE 1.** Three of the six gf-topup-1 cells carry an interrupted turn (the helm's 67th bank,
   2026-09-15). That bears on their PHASE-1 cost reading, which this block does not use; phase 2 is metered on the copy alone.

## §G6 · READING RULES
Scored with each task's `B/run_tests.sh` (the post-change suite), against a copy, archives hash-checked before and after, as the P1
wave. Each cell's row carries: end class, phase-2 cost, the P1 baseline, served model (head and sidechain apart), client version, the
source cell and root, the account, and the export. A CAP-COST cell is a cell of record at its suite result (§CLB-R.2 clause 2). The
condition's figure is reported at the n it reaches, with the other cells of record beside it, never as an arm comparison.

## §G7 · VOIDS AND RE-FIRES
A cell VOID before its first model call (a held launch, a fence or trust refusal, ACCOUNT-REFUSED) is re-fired from a FRESH copy under
an `r<k>` id (block N ADDENDUM 14), and the void stays in the record. **A cell that ran is the cell**: no re-fire for an outcome,
including CAP-COST, BUILD-FAIL and a phase 2 that never lands.

## §G8 · WHAT THIS BLOCK CANNOT ESTABLISH
It moves six conditions from DONE at n < 3 to DONE at n = 3 of record. It makes no claim that either arm is better or cheaper, no
p-value, no pooling across tasks, and nothing about phase 1. It does not change the matrix's DONE count (181), which already counts
all six.

## §G9 · DELIVERABLES
The release addendum (export, stager change, §G2 results, pool) · the 7 cells · a RESULT file with its verify script and cells TSV ·
a census addendum moving the six to n = 3 · the census addendum for §G0's four, filed beside it.
