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

---

## ⚖️ ADDENDUM 4 — ADDENDUM 3's MOVE IS NOT TAKEN; IT STANDS AS THE DECLARED FALLBACK. APPENDED.
The first pool's owner will lift its ceiling himself before the wall (the helm's relay, 2026-09-26 ~01:47 UTC), so **block N stays on
A2.3's dir.** ADDENDUM 3's second dir is the FALLBACK, on the same triggers as x86 PoC #267 ADDENDUM 5: at a fire, the first dir fails
its account check, or its probe turn does not authenticate, or the helm's all-models reading of the first pool is at or over 92 % with no
reset yet taken. Taking it gets its own addendum naming the first cell. No block N cell has run on the second dir.

---

## ⚖️ ADDENDUM 5 — A2.3's DIR HAS A NEW LOGIN; BLOCK N's NEXT CELL RUNS ON IT UNDER A2.3's SEQUENCE. APPENDED.
Block N's lane env never left A2.3's dir: ADDENDUM 3's move was not taken (ADDENDUM 4). While the x86 row ran on the fallback, A2.3's
credential blanked at a probe turn (x86 PoC ADDENDUM 6), and its owner then ran a new `/login` into it on the run box (2026-09-26
04:59 UTC). The fresh credential was backed up before any turn, and step (1) of A2.3's sequence reads OK, with a wrong --expect reading
RED. Steps (2) and (3) are block N's next fire, whose own probe turn is the authenticated read. ADDENDUM 4's fallback triggers stand
unchanged, and the single-cell rule still spans both lanes.

---

## ⚖️ ADDENDUM 6 — BLOCK N RUNS ON BOTH POOL DIRS AT ONCE, ONE CELL PER DIR: LANE B ADDENDUM 5's PROCESSING LIMIT, ADOPTED. APPENDED.
**Registered before block N's first concurrent cell.** ⛔ **No second concurrent block N cell fires before a non-author signs this addendum.**

**Why.** Council 2026-09-26 §1, the Captain: *"With the pilot done, the remainder of saltbench is P3, now I'm happy to move salt back to
the fore."* and *"Let's plan on using that quota."* The helm routed it to the lead the same morning: O37's P3 remainder is to run NOW on
ADDENDUM 3's second dir, whose weekly points are lost at its reset whatever runs on them. **This is not ADDENDUM 4's fallback.** None of
its three triggers has fired: A2.3's dir authenticates and is carrying a live cell (`clbnas01`). The second dir is added as a second,
concurrent pool, and A2.3's dir stays in use.

**The limit** is lane B ADDENDUM 5 §A5.2 (a)–(d), adopted by reference and unchanged: (a) one live cell per pool · (b) never two live
cells in one root · (c) fires serialized · (d) no config dir created or removed while a Claude-lane cell is live. It is enforced by the
export's own `clb_fire.sh` (6087b54, the quiet check and the fire lock) under `CLB_CONCURRENT=1`. That check refuses a fire if a live cell
sits in the same root or on the same pool, and it refuses (fail-closed) if a live cell's pool cannot be read. A2.3's single-cell rule is
(a) applied to each dir, and it still spans the x86 row, x86 first on either dir.

**The second dir** is used under A2.3's sequence: (1) `cells_account_check.sh` reads OK with the second pool's expected identity, and a
wrong `--expect` reads RED; (2) the fire's own probe turn authenticates, checked by its body; (3) the cell. A second block N lane env file,
beside the first and never replacing it, differs from the first in `CLB_CFG` only. Both files carry `CLB_CONCURRENT=1`.
**Budget:** before each fire on the second dir, the lead reads that pool's all-models meter. A reading at or over 95 % holds the fire on
the pool's clock (the helm's stop line), and never on the work.

**What it changes about the data, said before any concurrent cell** (lane B §A5.3 and its ADDENDUM 6's pool confound, carried):
- **Pool is recorded per cell** (`ctl/run-cfg.tsv`, `cfg`). It is read per cell and never assumed.
- **No arm is assigned by pool, but arm and pool will be CORRELATED.** §N3's list alternates plain and salt-diet inside one problem, and
  (b) keeps two cells of one root apart. So a concurrent pair is usually one cell of each arm, and the dir that frees first takes the next
  cell in list order. The pool is reported as a column beside every table and is never balanced. The served model, the pinned client,
  the settings, the fence and the caps are identical across the two dirs.
- **`claude_live_at_fire` is reported per cell**, beside the agy census. Load moves wall time directly and cost only through behaviour.
  The wall cap (W1 = 144,000 s) is 10.8× the live cell's elapsed wall at this drafting (13,350 s for `clbnas01`, from its own
  `ctl/watch.log`).

**What this does NOT change:** the export (A2.1), the client pin, the arms, the models, the caps, the fence, the P4 probe, the scorer, the
tripwires, or §N3's order as a LIST. ADDENDUM 4's fallback triggers stand for A2.3's dir. Every block N cell up to this addendum ran on
A2.3's dir alone, and `claude_live_at_fire` read 0 at the fire of each of the eight (each cell's own fire log on the run box).

## ✍️ NON-AUTHOR SIGNATURE — the helm (133rd head), 2026-09-26 10:49 PDT, on ADDENDUM 6 (transcribed by the lead from the bus, offset 70136823)
Signed at the pinned blob `98262ae5a9fb` (head `75dd39f0665f`), the addendum read whole. **Coverage, as the signer stated it:** the text; a
second non-author read of `clb_fire.sh`'s quiet check (the three refusals, read in the code, with the pin resolved); and the lead's heartbeat
measurement (maximum `watch.log` gap 61.0 s over 226 intervals, a proxy). **Not covered by any reader:** (c)'s fire lock read at the code,
the account check re-driven by a non-author, and the run box itself.
**Residue carried, not a defect:** "live" is a LEVEL test on a heartbeat (`watch.beat` younger than 180 s and no end marker), so a beat
stalled past 180 s lets a second fire pass the guard on the same pool or root. At a 61 s maximum gap that is about three missed beats.
Owed by the lead: read `watch.beat`'s mtime history once when `clbnas01` ends, and print the guard's basis beside the pool column in the
RESULT the first time a concurrent pair runs.
**Budget at signing** (all-models meter): the second dir's pool at 33 %, A2.3's dir's pool at 11 %.

---

## ⚖️ ADDENDUM 7 — THE SECOND DIR COULD NOT AUTHENTICATE AT ITS FIRST FIRE, AND ITS CREDENTIAL BLANKED. NO CELL RAN ON IT. APPENDED.
**What happened** (2026-09-26, the run box, every line from `~/bench-dry/cred-ledger.tsv` and the fire log). A2.3 step (1) read OK on the
second dir's lane env: file identity == `--expect`, credential present, and a wrong `--expect` read RED. `clbnap02` (Sonnet · AES · plain #2)
staged at 17:50:12Z. The pre-fire ledger row read a 524 B credential whose access token had expired seven hours earlier. The fire reached
A2.3 step (2), the probe turn: `P-SANDBOX INDETERMINATE (no-marker)` at 17:50:24Z, then `REFUSE … do not launch` (rc 3). The post-refusal
ledger row read the credential **BLANKED: 296 B, access and refresh both empty.** This is A2.3's 2026-09-25 failure again: a refresh the
server refused, then a blanked file.
**No subject ran.** `clbnap02` was built and never launched, and $0 was spent on it. It will fire on A2.3's dir when that dir is free, as
§N3's next cell. `claude_live_at_fire=1 (clbnas01)` was reported at the refused fire, and the concurrency guard behaved as ADDENDUM 6 says.
**What is not known, declared.** Why the server refused is in no local byte. The lead's hypothesis is that this copy shares an account
session with a live seat on another machine, whose refreshes rotate the token. It is UNMEASURED. ⛔ **The credential was not backed up
before the fire.** Had the token still been refreshable, a backup would have kept it. Because it was refused, the backup most likely would
not have mattered, but that is an inference, not a measurement.
**From here:** the second dir is OUT until its owner runs a fresh login into it on the run box. That is a person's act, and it is taken in a
quiet window (lane B §A5.2 (d)). Before the next fire on it, the credential is backed up, then A2.3's sequence runs whole. Block N
continues on A2.3's dir, one cell at a time, as it did before ADDENDUM 6. ADDENDUM 6's rules stand for when the second dir returns.

---

## ⚖️ ADDENDUM 8 — THE SECOND DIR RETURNS AFTER ITS OWNER'S FRESH LOGIN; THE FIRST CONCURRENT PAIR. APPENDED.
The owner logged the second dir in afresh on the run box at 14:44 PDT (desk YL). ADDENDUM 7's conditions for its return, in order:
- **The credential was backed up** before any turn (524 B, 21:45:40Z).
- **A2.3 (1):** ACCOUNT-CHECK OK == `--expect`, credential present with access and refresh; a wrong `--expect` reads RED, rc 1.
- **A2.3 (2):** `clbnvp01`'s probe turn: P-SANDBOX GREEN at 21:47:58Z. The ledger read the credential UNCHANGED before and after the fire.
- **A2.3 (3):** `clbnvp01` (Sonnet · Liveness · plain #1) launched at 21:50:28Z.
**The first concurrent pair:** `clbnvp01` on the second dir, beside `clbnas03` (Sonnet · AES · salt-diet #3) on A2.3's dir. The fire logged
mode ADDENDUM 5 and `claude_live_at_fire=1 (clbnas03)`. The pair crosses arm AND pool (plain on dir 2, salt-diet on dir 1), and ADDENDUM 6
declared exactly that correlation.
**The guard's basis, as the signature asked:** a 1-s sampler of every live cell's `watch.beat` age runs on the run box from 21:45:56Z
(`~/bench-dry/beat-samples-2026-09-26.tsv`). Its maximum per cell is printed beside the pool column in this block's RESULT.

---

## ⚖️ ADDENDUM 9 — A RUN-BOX FAULT WINDOW, AND THE RULE FOR THE CELLS THAT RAN THROUGH IT. APPENDED.
**The window.** From about 21:50Z to 22:08Z on 2026-09-26, an agy cell of another lane stacked orphaned builds on the run box. The box
reached load 46 on 12 CPUs, and swap got within about 1 GB of exhaustion. That cell was ended as a harness fault in its own lane.
**Block N cells live in the window:** `clbnas03` (AES · salt-diet #3, A2.3's dir) and `clbnvp01` (Liveness · plain #1, the second dir).
**The rule, stated by the lead and ruled by the helm (non-author) before either cell's reading was fixed:** a cell is VOID only on FAULT
EVIDENCE IN THE CELL, meaning a tool call that failed BECAUSE of the box. It is never voided on its outcome, and the rule is applied to both
cells alike. The author proposed this rule rather than ruling on it himself, because a void here would have removed a FAIL from the
salt-diet arm.
**The reading:** every `tool_result` in each cell's session transcript within 21:40–22:20Z was matched for timed out · timeout · killed ·
signal 9 · sigkill · cannot allocate · out of memory. `clbnas03` had 67 tool calls in the window and 0 flagged; `clbnvp01` had 39 and 0
flagged. The same detector over `clbnas03`'s whole run flags 2 (`Command timed out after 5m 0s`, at 20:19Z and 20:55Z, both before the
window), so it can see the class.
`clbnas03` sat idle twice for about 10 minutes inside the window, with its cost flat and one watcher poke each time. No tool call failed in
either span. What the subject waited on is UNMEASURED.
⇒ **Both stand as RESULTS:** `clbnas03` CAP-COST (cost 37.75 of 37.21), withheld suite FAIL 1/8; `clbnvp01` PASS 11/11. **The fault
window is a declared confound column** beside every table that holds either cell.

---

## ⚖️ ADDENDUM 10 — OPUS MOVES FORWARD: THE TWO MODEL COLUMNS RUN INTERLEAVED FROM NOW, T-N-O FIRST. §N3's MODEL ORDER AMENDED. APPENDED.
⛔ **No Opus cell fires before a non-author signs this addendum.**
**Why.** §N3 put Sonnet first "because the cheaper model buys the first read of new problems, and nothing here compares the models." That
first read has been bought for four of the six problems: Luby, AES, Liveness and MaxFlow each have Sonnet cells scored. LinearScan waits on
its card (desk YM) in both columns. The Captain's word of 2026-09-26 is to spend the week's lapsing points. Block N is the work pointed at
the two lapsing pools, and it is bounded by one cell per pool (ADDENDUM 6 (a)). So the lever left is the DOLLAR RATE per cell. Measured
from each cell's own `ctl/watch.log` (final cost ÷ wall):
```
  Opus  (the x86 Claude row, 2026-09-26, 12 cells)   plain 10.7–18.1 $/h   salt-diet 19.2–32.7 $/h
  Sonnet (block N to this addendum, 16 ended cells)  plain  4.7–12.2 $/h   salt-diet  8.7–26.6 $/h
```
These are different problems, so the rates are an ESTIMATE of the direction, not a price.
**The order, amended.**
- **T-N-O** (Opus · Luby · salt-diet #1) fires first, on whichever dir frees first. It is read by the lead under §N3's tripwire rule
  before any further Opus cell.
- After T-N-O's reading, each dir that frees takes the next cell from the model column OTHER than the one that dir last ran. Inside each
  column, the order is §N3's problem list and per-problem cell order, with ADDENDUM 6's next-free-cell rule. Alternating by dir keeps
  model from correlating with pool. It is declared anyway: nothing in this block compares the models.
- The Sonnet column continues where it stands: Liveness salt-diet #2 and #3, MaxFlow plain #2 and #3 and salt-diet #2 and #3, then
  BinomialHeap. The Opus column is §N3's list from Luby.
**What does NOT change:** the arms, the caps (the same dollar cap for both models), the export, the client pin, the fence, the probe, the
scorer, one cell per pool, or the 95 % stop on the second dir.
**The box, after 2026-09-26's hazard:** that hazard's mechanism was an agy client returning control while a build still ran, with the
subject unable to see its own processes. On this lane the Claude client KILLS a timed-out command (`Exit code 143, Command timed out
after 5m 0s`, seen twice in `clbnas03`'s transcript), so that mechanism has no measured path here. UNMEASURED: a subject's own
background job. The lead holds new fires (never kills a live cell) while the run box's `vm.swapusage` used exceeds 20,480 MB.

## ✍️ NON-AUTHOR SIGNATURE — the helm (134th head), 2026-09-26 17:19 PDT, on ADDENDUM 10 (transcribed by the lead from the bus, offset 70416508)
Signed at the pinned blob `828af7901a5b` (head `d7463acc`), the addendum read whole. **Not covered by the signer:** the dispatcher's
alternation, read at the code, and the wiring of the swap hold. Both are driven at the first Opus fire and the first alternation.
**Residue carried, not blocking:** the dollar cap is the same for both models, and Opus spends about 1.5–2× the Sonnet rate per hour, so
Opus cells will reach CAP-COST sooner on the same problems. Nothing in this block compares the models, so this is not a confound here. It
is printed beside any per-model CAP-COST count in the block's RESULT.

---

## ⚖️ ADDENDUM 11 — A2.3's DIR COULD NOT REFRESH AT A FIRE AND ITS CREDENTIAL BLANKED. NO CELL RAN. BLOCK N CONTINUES ONE-WIDE ON THE SECOND DIR. APPENDED.
**What happened** (2026-09-27, the run box; every line from `~/bench-dry/cred-ledger.tsv` and the fire logs):
- `clbnxp03` (Sonnet · MaxFlow · plain #3) staged, and its fire reached the probe turn at 04:47:15Z. It read `P-SANDBOX INDETERMINATE
  (no-marker)` and then REFUSE, rc 3. The probe session's transcript reads `authentication_failed`, "OAuth session expired and could not
  be refreshed". The post-refusal ledger row reads the credential BLANKED (296 B).
- **This time the credential WAS backed up before the fire** (ADDENDUM 7's order). The backup was restored once and the fire was retried:
  the ledger read the restored refresh token as the same one the server had just refused, with the access token 1.6 min from expiry. It
  was refused again and blanked again.
- The refresh token had been UNCHANGED since its last clean refresh (the ledger row at 23:0xZ) through six later fires and cells on
  that dir. The cells use the pool dir itself (`clb_fire.sh` exports it as the run config), not a per-cell copy.
**Why the server refused is in no local byte.** It is UNMEASURED. It is not the per-cell-copy mechanism, which this lane does not use.
**No subject ran.** `clbnxp03` was built and never launched, and $0 was spent on it. It fires as the Sonnet column's next cell when a
dir is free.
**From here:** A2.3's dir is OUT until its owner runs a fresh login on the run box. Block N runs ONE-WIDE on the second dir, under
ADDENDUM 10's order (a dir takes the column it did not last run). ADDENDUM 6's rules stand for when A2.3's dir returns.

---

## ⚖️ ADDENDUM 12 — LINEARSCAN IS RELEASED ON EXPORT 23485e5 (desk YM). EVERY OTHER PROBLEM STAYS ON 6087b54. APPENDED.
**Why.** At 6087b54, LinearScan's card said "FULL SEMANTIC PRESERVATION AS A THEOREM IS NOT ASKED FOR … a compiler-verification project",
which names a proof and a verifier to the plain arm. The neutrality gate refused every LinearScan cell at build, in both lanes, and no
subject ran. The card was re-worded (saltbench-systems `23485e5`, systems' wording, desk YM) to: *"The requirements ask that the output
compute what the input computed. A general argument that the rewrite preserves meaning for every possible function is a project of its own
and is not asked for."* It keeps R7 explicit and bounds only the general argument.
**Checked before any LinearScan call.**
- A non-builder re-drive by the lead: the diff is card-only (+3 −2).
- Each card was rendered through its own tree's renderer and neutrality scan. The old card has 1 hit (`THEOREM`, the control firing)
  and the new card has 0.
- The export `saltbench-systems-v3-export-23485e5` was proved on the run box by systems: the same figures, and the renderings are
  cmp-identical.
- The lead's `diff -rq` against the 6087b54 export lists the card, `clb_harvest.py` with one new fixture (harvest-side, reached by no
  subject), and the provenance marker. Nothing else differs.
**Each condition runs on exactly one export.** LinearScan's cells, both models and both arms, fire from 23485e5 by a lane env that differs
from the running one in `CLB_EXPORT` only. The other five problems stay on 6087b54, so no condition straddles two exports. No LinearScan
cell ran before this addendum.

---

## ⚖️ ADDENDUM 13 — A2.3's DIR LOST SERVER ACCESS MID-RUN. THE LIVE CELL IS NOT-SCORED(HARNESS) AND RE-FIRES AS A NEW CELL ID ON THE SECOND DIR. APPENDED.
⛔ **Registered BEFORE the re-fire. No re-fire before a non-author signs this addendum.**

**What happened** (2026-09-28; every line from the cell's own head transcript and `ctl/watch.log` on the run box):
- `clbmrs03` (Opus · LinearScan · salt-diet #3), block N's last cell, launched on A2.3's dir at 16:07:38Z with P-SANDBOX GREEN and the account
  check reading OK before the fire.
- Its last real assistant record is at **17:18:51Z**. From **17:18:53Z**, every model request returned a synthetic error record,
  `oauth_org_not_allowed`: five such records by 17:49:31Z, one per watcher retry. The credential file on the dir was unchanged throughout.
  **The server refused the account; the file did not change.** The account check reads the FILE's identity, so it still reads OK, and that is
  the limit it states beside its own verdict.
- This dir's pool was named in §N0 row 8 as released until **15:59 PDT that day**. The refusal began at 10:18 PDT, about 5 h 40 m earlier.
  Why the server refused is in no local byte.
- The cell was frozen at **$24.15** (its last METER line, 17:18:22Z) and spent nothing after the refusal.

**The watcher filed it as an overload, and that is a harness finding.** `cell-watch.sh`'s `last_assistant_state` maps `rate_limit`,
`authentication_failed` and `invalid_request`, and files every other error class as `HOLD OVERLOADED`. A hold freezes the caps and the stall arm
and retries every 600 s. So an account-level refusal reads as a transient overload and holds indefinitely, and the cell ends only at W1 or by hand.

**The rule for this cell, stated as a NEW CASE and not as a stretch of an old one.** Lane B §Q7 row 8, *"FAILED BOOT / a credential that did
not authenticate → NOT-SCORED(HARNESS), re-fired as a new cell id"*, names a credential that fails at BOOT. This one authenticated, and the
cell ran 70 minutes of real work before the server withdrew access. That is a second case, so it is registered here:
- **A cell whose every model call from time T onward fails on the ACCOUNT** (fault evidence in the cell: synthetic records carrying an
  account-class error, and no real record after T) **is NOT-SCORED(HARNESS)**. It is never scored on its partial tree and never enters a
  median. It is printed in its block's table with its receipts, its cost to T, and this addendum's name.
- **Its condition re-fires the missing cell as a NEW cell id**, on a pool that authenticates, under §N0 row 8's second clause (the P3 pool,
  named per cell, with the account check before the fire). The original cell is ended and never re-dispatched into (lane B §Q7 row 10).
- **This rule does not look at the outcome.** The cell had no withheld-suite reading when access ended, and none is taken before this
  addendum is signed. So the rule cannot be chosen by what the cell would have scored.

**The needle and the window, registered here before any result of this cell is read:**
- **NEEDLE:** a head-transcript assistant record that is synthetic (`isApiErrorMessage`, or model `<synthetic>`) and whose error is
  account-class. That means one of `oauth_org_not_allowed`, `authentication_failed`, or any error naming the organization, the OAuth grant or
  the account. A rate limit, an overload or a server error is NOT account-class.
- **WINDOW:** from the first such record T to the cell's end. The rule fires only if the window holds NO real (non-synthetic) assistant
  record, in the head or any sidechain. A single real record after T means access returned, and the cell is read as it ends.
- **SYMMETRIC:** the rule names no arm. It voids a plain cell exactly as it voids a salt-diet cell, and it is applied to every block N cell
  whose transcript carries the needle. On this addendum's date that is one cell, `clbmrs03`, measured by its transcript: 5 needle records and
  no real record after 17:18:51Z.

**Where the re-fire runs, and what it needs first.** It runs on the second dir after its pool's reset (Mon 20:00 PDT = Tue 03:00Z), when
the helm's tilt on that pool ends. The second dir has run block N cells since ADDENDUM 8. **The stager cannot produce the new cell id
today:** `clb_stage.sh` at 23485e5 derives a cell id from block, problem, arm and `n`, accepts `n` in 1..3 only (§Q0 row 2), and refuses a
directory that exists (a cell is evidence). So the re-fire needs a stager change that mints a re-fire id without touching the dead cell. That
change is a harness delta, and it reaches no subject. **It is named in a RELEASE line appended here BEFORE the fire: the export sha, the
new id, the stager's selftest (including a red arm that refuses re-using `clbmrs03`), and the diff against 23485e5 showing that nothing
subject-facing moved.** LinearScan salt-diet's three cells of record will then be `clbmrs01` and `clbmrs02` on A2.3's dir plus the re-fire on
the second dir. **That condition straddles two pools and is reported as straddling** (§N5.3).

**What this does NOT change:** the arms, the caps, the export, the client pin, the fence, the probe, the scorer, or any other cell.

---

## ⚖️ ADDENDUM 14 — THE RELEASE OF ADDENDUM 13's RE-FIRE. APPENDED; ADDENDUM 13 (signed at blob `27f8c21972ec`) UNTOUCHED.
**The signer's condition, met: the needle over EVERY block N cell of record** (a census script on the run box. It reads each cell's own
`ctl/run-cfg.tsv` for its config dir and scans every transcript under that cell's slug, head and sidechains, with the needle exactly as
ADDENDUM 13 registers it):
```
  cells scanned 72 (every cells-clb-n{s,o}-* cell with a ctl/run-cfg.tsv) · slug absent 0
  with the needle 1 — clbmrs03: 5 needle records, T 2026-09-28T17:18:53.273Z, 0 real records after T, 703 records read
  CONTROL  an account-class record planted in a scratch copy of clbmrs01's transcripts   → needle 1   (must match; did)
  CONTROL  an overloaded_error record planted in a second scratch copy                    → needle 0   (must NOT match; did not)
```
**So the rule applies to exactly one cell, `clbmrs03`, by its own words.**

**THE EXPORT: saltbench-systems `9d87318`** = 23485e5 + two commits, built by `studio_export.sh` (the allowlist export): 368 files,
withheld-shaped names 0 in the listing and 0 on the host. `diff -rq` against the 23485e5 export lists exactly three harness files and the
marker, and **nothing a subject reads**:
- `cell-watch.sh` (07b571f): an account-class error is its own class, `HOLD ACCOUNT`, and the session ends `ACCOUNT-REFUSED` once a RETRY
  sent inside the hold is 120 s old and still refused. QUOTA and OVERLOADED holds wait exactly as before. **Selftest 77 arms ok.** It went red
  first on 23485e5 (4 FAIL). Red backwards on two mutants: an always-end decision reddens 4 arms, and an everything-is-ACCOUNT classifier
  reddens the quota, invalid-request and overload controls. ⚠️ The pre-existing `HOLD AUTH authentication_failed` arm's expectation moved to
  `HOLD ACCOUNT` with the class, and this is declared rather than hidden.
- `clb_stage.sh` · `clb_fire.sh` (9d87318): `n` also accepts `r1..r3`, a registered re-fire, whose id is `clb…r<k>`. The original cell must
  exist AND carry `ctl/end-1`. **Driven on the run box against a fixture root, through this export, in both scripts:** plain `3` REFUSED (the
  cell exists; `clbmrs03` is never re-used), `r3` REFUSED while the original has no end marker, `r4` REFUSED (range), `r1` REFUSED (no
  original). The positive control `r2` passed the guard and derived `clbmrsr2` on export 9d873183acab.
- ⚠️ **The toolchain check was skipped for this export** (`--unreferenced-dest --no-toolchain`, because a cell was live on the box). The
  toolchain is the one 23485e5's export checked on the same box, and the cell's own launch asserts the client pin and resolves cargo and
  verus at `--check`.

**THE RE-FIRE:** `clbmrsr3`, Opus · LinearScan · salt-diet, on the second dir after its pool's reset, from a lane env that differs from the
second dir's LinearScan env in `CLB_EXPORT` only, with the account check read before the fire. **It runs under the fixed watcher; every other
LinearScan cell ran under 23485e5's.** The two differ only when a head record carries an account-class error, and no other cell's does (the
census above).

**ENDING `clbmrs03` FIRST** (the stager refuses a re-fire beside a live cell). 23485e5's watcher has no signal trap, so it cannot be ended by
its own path. At the fire, the lead signals its driver and its client **by pid** and writes `ctl/end-1` as
`<UTC> ACCOUNT-REFUSED ended by the lead under ADDENDA 13–14; the 23485e5 watcher held it as OVERLOADED`, then tags the snapshot. **No
post-end meter reading is taken, and this is declared**: the cell spent nothing after T. Its cost to T is `cell_meter.py` over its
transcripts, printed in the block's table beside NOT-SCORED(HARNESS).
