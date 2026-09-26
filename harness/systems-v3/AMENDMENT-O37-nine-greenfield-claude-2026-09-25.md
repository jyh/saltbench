# AMENDMENT — O37 BLOCK N: THE SIX BUILT NEW PROBLEMS, GREENFIELD × `none`, CLAUDE LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-09-25. The Captain, council 2026-09-25, in words: *"bench can start the remaining 9(?) problems. Can we
## finish in 1 month? If not let's aim for 2 months. At this point let's set the remaning problems on bench to P3 -- it can run if it does
## not use quota needed for higher priority tasks. But at this point, [the run box's pool] is full throttle, so the condition is lifted."*
## His standing objective is *"fill out the 14 problems (greenfield only)"* (2026-09-10). This freeze covers the FIRST SLICE of that
## objective: the 24 Claude conditions the harness can express TODAY. bench is lead AND hand on this lane, as in lane B.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES BEFORE §N2's ITEMS ARE DRIVEN AND A RELEASE ADDENDUM NAMES THE EXPORT SHA.**
## Signature and release are two acts, as in lane B.

**What this file does not change.** It is a new block under `AMENDMENT-claude-lane-B-2026-09-16.md`, and it CARRIES that freeze's
machinery BY CITATION: the preflight (§Q3.4, with ADDENDUM 5's one-live-cell-per-pool rule and §CLB-A's required ancestors), the caps
(§Q4), the confounds (§Q5), the reading rules (§Q6), the void table (§Q7) and the deliverables (§Q9). A clause below that differs from
lane B says so, and says why.

---

## §N0 · THE INPUTS
```
  1  MODEL IDs     claude-opus-5 · claude-sonnet-5 — the pilot's two Claude models, and the served set PER CONDITION exactly as
                   lane B §Q0 row 1 (Opus condition: HC stage 1's team; Sonnet condition: claude-sonnet-5 in EVERY role).
                   ⚖️ A newer model is NOT substituted: the nine are to join the pilot's five as ONE matrix, and a model change
                   changes what that matrix asserts, which is the Captain's word (put to him with this file; the default is this row).
  2  n             3 per condition.
  3  POPULATION    24 conditions, 72 cells (§N1). Nothing is added, dropped or substituted.
  4  EXPORT        ONE bare-master sha of saltbench-systems, named in the release addendum BEFORE the first cell, that (i) carries
                   the six tasks at the blobs §N2 item 1 drove (master e54f35a carries all six) and (ii) descends from lane B's last
                   release export, so every lane-B build item is present. One sha for all 72 cells, recorded per cell.
  5  CLIENT PIN    lane B §Q0 row 5, unchanged (the versioned client by ABSOLUTE PATH, its sha asserted per launch).
  6  TASK TREE     the EXPORT's own tasks/systems-v3, and nothing else.
  7  CAPS          lane B §Q4, unchanged: C1_USD $37.21 (cost_caps.tsv), W1_SEC 144,000; CAP-COST and CAP-WALL armed.
  8  ACCOUNT       ⚖️ THE CHANGE FROM LANE B: through Mon 2026-09-28 15:59 PDT, the run box's own pool, released at full throttle
                   by the Captain's word above, NAMED PER CELL, with `cells_account_check.sh --expect <that pool's identity>` reading
                   OK before each fire (it reads the resolved config dir's IDENTITY STRING, never its name). That pool is retired
                   at that instant, so NO cell starts after 13:30 PDT that day (≈ 2 × the pilot's ~40 min/cell proxy). After it:
                   P3 — a pool the higher lanes leave idle, named per cell under the same check. The box's DEFAULT cell env is a
                   separate matter, and this block neither waits on it nor touches it.
  9  FIRE ORDER    §N3, one cell per pool, pairs kept whole; a tripwire cell opens each model.
```

---

## §N1 · THE POPULATION — 24 CONDITIONS, 72 CELLS
Derived, not typed. O37's population is 9 problems × 4 models × 2 arms × {none, statement, spec-change} = 216 conditions. This block
takes the part the harness can express today:
```
  problems   AES · BinomialHeap · LinearScan · Liveness · Luby · MaxFlow      the six with a v3 greenfield rung (saltbench-systems,
                                                                                first commits 09c2504 … d8abefb, 2026-09-09)
  models     claude-opus-5 · claude-sonnet-5                                   the Claude lane (the agy half is a sibling freeze)
  arms       plain · salt-diet
  field      greenfield            extras   none
  ⇒ 6 × 2 × 2 = 24 conditions · × n 3 = 72 cells
```
**What is NOT in this block, and why, so a reader never takes 24 for 216:**
- `statement` × the six (48 conditions): no card carries a `## Statement` section yet. The extractor runs rc 0 on all six (read-only,
  to stdout, 0 `proof fn`), and the statement-arm amendment §2 requires the Captain to read each statement before a cell fires.
- `spec-change` × the six (48): no `B/` phase-2 tree exists for any of the six on any ref, and BinomialHeap's card carries no change
  request at all (`AMENDMENT-specchange-taskshape` §1 says what `B/` must hold).
- LU · NTT · WHT (72): no v3 rung on any ref. The 2026-09-09 "not feasible" verdicts were withdrawn, never re-judged.
- the agy lane's 24 `none` conditions: a sibling freeze, on the agy lane's own machinery.
Each of those is a later dated block, written before its own first call.

---

## §N2 · ⛔⛔ THE BUILD ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **THE SIX TASKS ARE RE-DRIVEN BY A NON-BUILDER, ON THE EXPORT'S BYTES.** Each task's README reports its builder's own validation. A
   builder's report is the subject grading itself. The lead re-drives, on a `git archive` of the export and at the pinned verifier sha:
   (a) Verus on `withheld/reference/solution.rs` (`--rlimit 250 --smt-option smt.random_seed=0`), verified with 0 errors;
   (b) `run_tests.sh` on the reference in BOTH forms, full pass;
   (c) `run_tests.sh` on EVERY mutant, with the pass count recorded, because a mutant's MARGIN (hidden tests it fails) is what makes it a
       planted defect rather than noise, and margin 1 is fragile;
   (d) `run_trace.sh`: the reference predicate is `TRACE_OK true` on each counter-trace's reference column and `false` on its mutant
       column; the TRIVIAL-PREDICATE control kills nothing (`true` on every mutant column).
   A task whose drive disagrees with its README on any of (a)–(d) is WITHDRAWN from this block by name, its three conditions reported as
   NOT-FIRED(TASK), and this file's population shrinks by an addendum, never silently.
   *Status at this writing: (a)–(d) running on master e54f35a. Luby: 67 verified / 0 errors, both references 12/12, every mutant fails
   (6–8 of 12 pass), the reference predicate reads `false` on all 6 mutant columns and `true` on all 6 reference columns. AES: 107
   verified / 0 errors. ⚠️ The trivial-predicate half of (d) is NOT YET DRIVEN: the first drive ran the reference predicate only. It is
   owed for all six before release. The full table goes in the release addendum.*
2. **THE ACCOUNT CHECK** (§N0 row 8): `cells_account_check.sh` (saltbench-systems 0da916f, selftest 11/11, including a mutant with the
   refuse test removed) is DRIVEN on the run box against the named pool, with the expected identity passed as an ARGUMENT, before the
   first cell. Its limit rides with its verdict: an OK means *the right identity, a credential present*, never *a launch authenticates*.
3. **NO LEAK INTO A VIEW:** `check_withheld_leak_v3.py` over the export, and the treatment gate on one built view per problem and arm.
   A new task is where a withheld name is most likely to reach a view.

---

## §N3 · THE ORDER, THE TRIPWIRES
```
  models    Sonnet first, then Opus — lane B ADDENDUM 3's reasoning carries: the cheaper model buys the first read of new
            problems, and nothing here compares the models.
  problems  Luby → AES → Liveness → MaxFlow → BinomialHeap → LinearScan
            (ascending reference size by `wc -l` on solution.rs: 743 · 1,104 · 1,128 · 1,193 · 1,709 · 1,885, so the draw is
            measured on the cheapest problem first, and each later problem is priced by the ones before it)
  cells     per problem: plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3
```
**Tripwires, each ONE cell, read by the lead and posted before its model continues:** `T-N-S` = Sonnet · Luby · salt-diet#1 · `T-N-O` =
Opus · Luby · salt-diet#1. The treatment arm is read first, because it is the arm the caps bind (lane B §Q4 (ii)). The reading list is
lane B §Q3.3's, with its brownfield rows dropped, plus the account-check line.
**THE FIRST COMPLETE LUBY TRIPLE REPLACES THE PRICE.** The O37 price (2026-09-25) estimated ≈ 0.45 quota points per Opus cell and ≈ 0.18
per Sonnet cell from the pilot, and said that its direction of error is LIKELY UNDER, not certain. The Luby cells measure it on these
problems, and the price is re-cut from that measurement before the second problem fires.

---

## §N4 · CAPS AND PREDICTIONS — REGISTERED BEFORE ANY DATA
Caps: lane B §Q4, unchanged. A cap-out is a RESULT and enters its median at the cap. No cap is raised.
Predictions, reported per arm and model, where a miss is a result:
(i) within a condition, salt-diet's CAP-COST incidence is ≥ plain's (the pilot's CENSUS §T3/§U2: the cap binds the treatment arm);
(ii) CAP-COST incidence rises with reference size across the six (the §N3 order is also the prediction's order);
(iii) CAP-WALL binds no cell.
⛔ **No prediction is made about pass rate or premium.** These problems have never run on any lane, so there is no prior to register one against.

---

## §N5 · CONFOUNDS — lane B §Q5 carried, plus three that are new here
1. **NEW PROBLEMS, NEW AUTHOR.** The six were ported from Lean v1 to Rust/Verus in one sitting (2026-09-09) by the systems lane's
   executors. The pilot's five had weeks of cells against them before a result of record, and these have none. A defect in a new task
   is a HARNESS finding, reported as such, and never read as an arm effect.
2. **THE CAP IS THE PILOT'S.** $37.21 was derived from one Crc32 pair (cost_caps.tsv's own caveat 1). These references run 743–1,885
   lines against the pilot's 291–2,461. A larger problem meeting the same cap is a heavier censoring of the arm that works longer.
3. **TWO POOLS, ONE BLOCK.** Cells before Mon 13:30 run on the run box's pool, and cells after it on a P3 pool. The pool is recorded per
   cell and is never the other arm of a contrast. Pairs are kept whole within one pool wherever the window allows, and a pair that
   straddles is reported as straddling.

## §N6 · READING RULES — lane B §Q6 rules 1, 2, 3, 6–9 carried. Rules 4–5 (retention, find-the-defect) are brownfield and do not apply.
The expected verdict kind for every premium is registered now as **UNRESOLVED-UNDERPOWERED** (read CENSORED where the cap's arithmetic
forbids a clearing median, NOT-SCORED where §N7 removes cells). **This block fills the matrix with signs and correctness, and cannot
produce evidence about effect size.**

## §N7 · VOIDS — lane B §Q7, with rows 6–7 (the brownfield given; W1 class) not applying, and ONE ROW ADDED
```
 11  cells_account_check.sh does not read OK against the pool named for the cell                    DO NOT FIRE
```

## §N8 · WHAT THIS BLOCK CANNOT ESTABLISH, SAID BEFORE ANY DATA
1. No magnitude and no effect size. 2. Nothing about Opus versus Sonnet as models. 3. Nothing about the 192 conditions outside §N1.
4. Nothing about whether the six are representative of the nine: they are the six that were judged feasible to port, and the three
that were not are the three still missing. **That is a selection, and it is declared here rather than discovered in a table.**

## §N9 · WHAT THE HAND DELIVERS
Lane B §Q9's per-cell list, less its brownfield columns, plus: the pool per cell · the account-check line per cell · the §N2 item 1
table (per task: verify count · both reference pass counts · per-mutant pass count · the trace matrix). ⇒ **A result of record per
model, with the census re-cut in the same commit.** O37's population joins the census as its own section, because the pilot's census
is a result of record and is not re-opened. Any public sentence, and any claim about the method, is the Captain's.

---

## ✍️ NON-AUTHOR SIGNATURE — the helm (127th head), 2026-09-25 10:10 PDT, on §N0–§N9 (transcribed by the lead from the bus, offset 69282852)
Read WHOLE at blob `4da5ad9d7080`, head `90cf4cfb2989`, matched at the forge in one command, PR #265 10/10 checks green. The three
named things were refuted and held: §N0 row 1 (the pilot's two Claude ids, a newer model not substituted) · §N0 row 8 (the run box's
pool named per cell through Mon 15:59, no start after 13:30, identity string checked before each fire, the box's default env neither
awaited nor touched) · §N8 item 4 (the selection declared before any table). *"Nothing found to withhold the signature on. RELEASE
stays a second act, as written."* Ruling on §N0 row 8: CONCUR, the helm's under the delegation, reversible by the Captain's word.
§N0 row 1 goes to the Captain as one ask, and until he answers, the row IS the default.

---

## ⚖️ ADDENDUM 1 — §N2's ITEMS AS DRIVEN. APPENDED; §N0–§N9 and the signature untouched. NOT THE RELEASE.
### A1.1 · §N2 item 1 — the six tasks, re-driven by a non-builder at the pinned verifier sha (`VERUS_SHA256` 7a7b319b…ffb36)
On a `git archive` of saltbench-systems master `e54f35a`. **The six task trees are byte-identical, by git tree hash, at `e54f35a`,
`2833621`, `eb18e5d` and `0da916f`**, so this drive covers the task bytes of any of those exports.
```
  task          Verus (reference)        hidden tests: ref · plain   mutants (tests PASSED of total; every one FAILS the suite)   trace matrix
  Luby          67 verified, 0 errors    12/12 · 12/12               7 8 8 6 8 8            of 12                                 6 × (mutant false, reference true)
  AES           107 verified, 0 errors    8/8  ·  8/8                3 3 3 3                of 8                                  4 ×
  Liveness      81 verified, 0 errors    11/11 · 11/11               3 7 6 7 6 5 6          of 11                                 7 ×
  MaxFlow       70 verified, 0 errors     8/8  ·  8/8                6 3 4 5                of 8                                  4 ×
  BinomialHeap  68 verified, 0 errors    13/13 · 13/13               6 5 7 6 8 6 8          of 13                                 7 ×
  LinearScan    130 verified, 0 errors    9/9  ·  9/9                8 7 6 6 5 4            of 9                                  6 ×
```
**Trivial-predicate control (the second half of (d)):** `TRACE_OK true` on all 34 of 34 mutant columns across the six tasks, so it
kills nothing, as required. ⇒ **No task is withdrawn; the population stays 24.**
⚠️ **One margin-1 mutant, declared:** LinearScan `AlwaysReserveScratch` passes 8 of 9, so ONE hidden test kills it. It is a valid
planted defect, and it is also the most fragile in the set. A cell that ships its defect is scored by that one test.
### A1.2 · §N2 item 2 — the account check, driven on the run box
`cells_account_check.sh` (saltbench-systems `0da916f`, selftest 11 pass / 0 fail on the build box) with the run box's pool as
`--expect` and a dead pool as `--refuse` → **`ACCOUNT-CHECK OK`**: identity == `--expect`, credential PRESENT (access and refresh
non-empty), rc 0. Its own limit rides with it: *"the FILE identity; a launch is what proves it authenticates."* **It is re-run before
EVERY fire (§N7 row 11); this is the first reading, not a standing clearance.**
### A1.3 · §N2 item 3 — leaks
`check_withheld_leak_v3.py` over the export: **CLEAN** — 186 identifiers across 11 tasks (the six new ones: AES 9 · BinomialHeap 17 ·
LinearScan 13 · Liveness 15 · Luby 13 · MaxFlow 9), every positive control fired, 668 view-file reads, 0 in any view. The treatment
gate on built views runs in the builder at each cell's stage, and it is read at the tripwires.
### A1.4 · WHAT THE DRIVE FOUND THAT THE FREEZE DID NOT PREDICT: the stager does not know this block
`clb_stage.sh` and `clb_fire.sh` at the lane's last export (`eb18e5d`) hard-code lane B's seven blocks and five problems, and
`--roots` checks lane B's registered 64. **No block-N cell can be staged on the existing export.** The change adds two blocks and six
problems, with a scope refusal in both directions, and gives `--roots` a block-N mode with its own registered 24, leaving lane B's
check unchanged. It is built red-first on a branch off `eb18e5d`. **The release addendum names the resulting export sha and that
change's receipts; no cell fires on `eb18e5d` itself.**

---

## ⚖️ ADDENDUM 2 — THE RELEASE. APPENDED; §N0–§N9, the signature and ADDENDUM 1 untouched.
### A2.1 · THE EXPORT (§N0 row 4): saltbench-systems `6087b54`
`6087b54` = lane B's last export `eb18e5d` plus ONE commit, the stager learning block N (A2.2). It descends from `eb18e5d`, and therefore
from `2833621` (Block O's result of record). Its six task trees are byte-identical, by git tree hash, to the ones ADDENDUM 1 drove.
On the run box by `studio_export.sh --ref 6087b54` into its OWN destination, so lane B's `eb18e5d` export is untouched: 367 files, 0
withheld-shaped names on either side, the Verus sha equal on both boxes (`7a7b319b170692d3`), CARGO_ROOT 633 = 633.
### A2.2 · THE STAGER (the §N2 gap ADDENDUM 1 §A1.4 found)
`clb_stage.sh` and `clb_fire.sh` gain blocks `NS` (claude-sonnet-5) and `NO` (claude-opus-5), greenfield × `none`, and the six problems.
A scope rule REFUSES any cross combination in both directions, naming both freeze files. `--roots` keeps lane B's registered 64 by
default and gains an explicit `--freeze N` with its own registered 24 (12 + 12). Letters: blocks `n` `m`, problems `a h r v y x`, none
shared with lane B, so every id and root is distinct (192 + 72 ids, 64 + 24 roots, measured).
Selftest `fixtures/clb_blockN_selftest.sh`: **5/13 on the `eb18e5d` originals · 13/13 on `6087b54` · 12/13 and 9/13 on its two
mutants** (scope refusal removed; NS served by the Opus model). **All 210 lane-B (block, problem, arm, n) derive byte-identically to
`eb18e5d`**, the 18 Paxos × statement refusals included. It was written by a delegated build agent and re-run by the lead.
The harvester's letters (`clb_harvest.py`, `08a3a41`, on the build box where scoring runs) are checked against the stager's own tables
by `fixtures/clb_harvest_tables_check.py`: DISAGREE on 8 at `eb18e5d` · AGREE 9 blocks / 11 problems · DISAGREE on a one-letter mutant.
### A2.3 · THE ACCOUNT (§N0 row 8), and what 2026-09-25 taught it
At 10:24 the pool's previous config dir on the run box read `ACCOUNT-CHECK OK` (the FILE: right identity, credential present), and the
first launch against it failed: *"OAuth session expired and could not be refreshed"*. The failed refresh then BLANKED the file (509 →
281 B). ⇒ **The account check is necessary and never sufficient, as its own verdict line says.** From this release on, the sequence
before T-N-S is: (1) `cells_account_check.sh --expect <the pool's identity>` OK on the NEW dir; (2) ONE authenticated read through the
pinned client from that dir, checked by its BODY; (3) the cell. §N7 row 11 stays per cell. The dir: **the run box pool's OWN ACCOUNT DIR on the run box**, refreshed by the Captain at 11:01 (desk YG; his words: *"I refreshed all
the accounts on [the run box]"*). ⚠️ It is the pool's EXISTING account dir, not the fresh dedicated dir the ask named, because his refresh
covered the five per-pool account dirs, while the lane's older cell-credential dir for that pool stayed blanked (kent, 11:02). (1) READ: systems' per-dir table 11:03,
OK on the file · (2) AUTHENTICATED: systems' x86 P-probe turn on this dir, rc 0, credential unchanged after · (1) again on block N's
OWN env by a derived check (`CLAUDE_CONFIG_DIR` taken from the env's `CLB_CFG`, so the check and the launch read one value):
`ACCOUNT-CHECK OK … (== --expect)`, and a wrong `--expect` reads RED, rc 1.
⛔ **ONE LIVE CELL ON THIS DIR AT A TIME, ACROSS BLOCK N AND THE x86 CLAUDE ROW, x86 FIRST** (lane B ADDENDUM 5's per-pool rule,
widened to both lanes): two lanes refreshing one credential file concurrently is how a credential gets blanked, so the dir is a
single-cell resource.
### A2.4 · THE LANE ENV (untracked, on the run box: block N's OWN lane env file, beside lane B's and never replacing it)
Keys: `CLB_CFG` = A2.3's dir · `CLB_BIN` = the 2.1.259 client by absolute path, sha256/16 `884baa38fe1a624b` read on the box ·
`CLB_EXPORT` = A2.1 · `CLB_PROBE_TRANSPARENT=1` · `CLB_PROBE_OUTSIDE` = lane B's, unchanged. Lane B's own env file is not touched.
### A2.5 · §N5 GAINS A FOURTH CONFOUND, MEASURED BY systems ON 2026-09-25 AND DECLARED RATHER THAN FIXED
**Every Claude-lane cell, the pilot's and this block's, runs with an unusable TMPDIR.** The client gives each sandboxed command
`TMPDIR=/tmp/claude-501`, and every v3 fence denies `/tmp`. A pilot transcript shows `ls -d $TMPDIR` → *Operation not permitted*, and
process substitution failing on `/dev/fd`. It is ARM-NEUTRAL (both arms, every cell). **Block N keeps the pilot's launch env on
purpose**: the nine join the five as one matrix, and fixing it here would put a harness delta on exactly the axis the matrix compares
across. A subject's workaround or failure caused by it is reported per cell, never read as an arm effect.
### A2.6 · ROOTS
`clb_stage.sh --roots --freeze N` in a window with NO Claude-lane cell live (the render-time-glob law), AFTER A2.3's dir exists,
because a fresh root is settings → fence → trust and trust is keyed to the config dir. Receipt, 18:52:11Z, in a window with NO cell of either lane live (checked by process listing on the run box): `ROOTS: 24 cells roots
present with _bin linked into export 6087b5487b97, each root's model table read back … (12 opus, 12 sonnet — … equal to the registered
24)`, after a `--dry` run of the same into `~/bench-dry` (rc 0). ⚠️ **AND THE LAW BINDS BOTH WAYS:** block NA's remaining roots are
created BEFORE T-N-S is live, or only in a window where no block N cell is live.
### A2.7 · RELEASED. T-N-S (Sonnet · Luby · salt-diet#1) is the first cell; the block continues only on its reading (§N3).

---

## ⚖️ ADDENDUM 3 — THE POOL DIR MOVES ON THE RUN BOX, WITH THE x86 ROW, BEFORE BLOCK N's NEXT CELL. APPENDED.
**What moves:** A2.3's dir only. The run box pool's own dir reaches its weekly ceiling tonight (the helm's reading, 2026-09-25 ~01:45
UTC), 2.5 days before its reset. From block N's next cell onward, `CLB_CFG` names a SECOND subscription pool dir on the same run box, the
same one the x86 Claude row moves to (x86 PoC #267 ADDENDUM 4). The single-cell rule of A2.3 carries over to it, across both lanes.
**What does NOT move:** A2.1's export, the client pin (2.1.259, `884baa38fe1a624b`), the probe mode and outside file, the budgets and caps,
the harvester and scorer. Both arms move together. An account is a billing pool, not a treatment, and A2.5's TMPDIR confound is unchanged.
**A2.3's sequence, on the new dir:**
- (1) `cells_account_check.sh` reads ACCOUNT-CHECK OK: the file identity == --expect, credential PRESENT with access and refresh
  non-empty, and a wrong --expect reads RED (2026-09-26 ~01:4x UTC).
- (2) ONE authenticated read through the pinned client from that dir, checked by its BODY. It is the first fire's own probe turn, which
  `clb_fire.sh` checks by its body and which refuses the launch unless it is GREEN, and the x86 row's first fire on the dir drives the
  same read.
- (3) the cell.
**No new $HOME entry:** both routes' per-fire trust seed creates one `~/.claude*` sibling for its config dir (`clb_fire.sh:12`), and that
sibling already exists for the new dir, because it has been a cell pool before.
**Which cell ran on which dir** is read per cell from its own `ctl/run-cfg.tsv` (`cfg`), never assumed. Every block N cell to this
addendum ran on A2.3's first dir.
