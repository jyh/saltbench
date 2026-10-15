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
                  These are LANE files on the lead's box, NOT tracked in either repository: APPLY.txt md5 d8e559f7447944ce4cd6dc324a45a83c,
                  its base chain-l8u.sh md5 b3f3a62f886d7814177a098bcbbd76bd (as APPLY.txt names it), and chain-l7u.sh in the l7u lane dirs.
                  The release addendum quotes each file's md5 at the chain's start, so a reader checks the files rather than this sentence.
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
  ⇒ Order of magnitude: Pro's 60.4 h is over 134 cells and Flash's 42.2 h over 138, so **~42 h of serial wall for the 138 control cells**
  **plus ≈ 40–65 h for the 138 Gemini 4 cells** if it behaves like either 3.x model. That describes the 3.x models, not a prediction for Gemini 4.
- **Stop rule.** If the tripwire price puts the set past the ZF review date (2026-10-28) on the pool this lane can draw, the lead posts that
  with an order (spec-change last, then brownfield/statement) before any cell beyond the tripwires. **A cut removes WHOLE CONDITION PAIRS,
  never one model's arm alone. n is never reduced quietly**, and a condition left short is reported short.

## §G3 · PREDICTIONS — REGISTERED BEFORE ANY DATA
None about direction. The deliverable is descriptive. The PRIMARY comparison is the same-day pair: per condition, landed and scored (the
withheld suite) for Gemini 4 beside its control. The 3.x cells of record are a HISTORICAL column, labelled as such. Every figure names its file. **No p-value and no claim that the method helps or hurts.**

## §G4 · CONFOUNDS — level 6 §H4 carried, plus these, each stated wherever a comparison is
1. **(The HISTORICAL column only.) The 3.x cells of record are a PATCHWORK:** one condition's 3.x cells came from different levels with different machinery. For example,
   Pro greenfield × none is levels s3 and l6v plus conditions carried DONE by an addendum (the `CONDITION … ADDENDUM 3d` rows, which are
   not cells: 18 of that condition's 48 CELLMAP rows), and Flash brownfield × none is l6v and l7. This set runs every condition on ONE export.
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

## ✍️ NON-AUTHOR SIGNATURE — kent, 2026-10-13 16:24 PDT
Signed on the fleet record at blob `0bf0d55d3ecda5a8306821ef33405b90ee4b6ab5` (PR #334 head `6d7de5b26e6e`), replacing his signature at the
previous blob, which crossed with the lead's re-pin. Recorded here by the lead beside the text it signs; everything above is untouched.

## ⚖️ ADDENDUM 1 — THE RELEASE: EXPORT `f048a78`. APPENDED; all text above, signature included, untouched.
*bench (lead), 2026-10-13. §G0.3 named the export to this addendum. No model call fires before this addendum is signed by a non-author.*

**A1.1 · WHY A NEW SHA.** The hand's first preflight on the fence master `d398cb0` REFUSED at zero spend: no ref carried BOTH the ctl/
fence (`95caaee`) and the level-8 lineage (`2a674d7`, the last level-8 export of record), 0 of 518. So no existing sha could meet §G0.3 and
also score a spec-change cell (level 8's anchored scorer) or build a salt-diet Verus cell (level 8's `--verus-root` fence fix).
**`f048a78`** = a `--no-ff` merge of `2a674d7` into `d398cb0`, cut by the lead. `merge-base --is-ancestor` holds for both `95caaee` and `2a674d7`.
The merge had no conflicts; `render_srt_config_v3.py` and `agy_launch_v3.sh` merged from both sides.

**A1.2 · RECEIPTS FOR THE EXPORT**
```
  selftest_all_v3 --runs 3, FULL CHECKOUT at f048a78 (run box, toolchain loaded)   222/228 · 0 failed · 6 skipped
      skipped = placebo-form ×3 + placebo-arm+problem-column ×3 (PLACEBO_V2_PATH unset; no placebo arm is in this set)
  the same, git-archive form, with each PARENT as a control                       f048a78 210/228 · 9 FAIL = 3 arms × 3
      d398cb0 FAIL {agy-client-wiring, comparator-rows} · 2a674d7 FAIL {the same two + export-ancestors}
      ⇒ the merge's archive-form failures are exactly its parents' union, and all three pass in the full checkout: environmental
  non-author READ of the two both-sides files (kent, bus 2026-10-13 17:02)       M1, M2 and the client-log grant SURVIVE,
                                                                                  re-driven on the merged render; no HIGH, no MEDIUM
```
**A1.3 · THE CHAIN AND ITS PLAN (the hand's §G6 deliveries, read by the lead)**
```
  APPLY.txt (VQ(b)+VT(b))  md5 d8e559f7447944ce4cd6dc324a45a83c · bases matched (chain b3f3a62f · selftest 9cf47600 · fixture 930fe7e4)
                           patched chain ac9eb727 · fixture 8f111817 · selftest e692b998 · selftest in a FULL template 298/0
  ZF modes on that chain   ZP (preflight + plan) · ZT (legs 1–4, the two tripwire PAIRS, then TRIPWIRE-HOLD) · Z (legs 5–276)
                           selftest 311/0 (the 298 + 13 ZF arms, red-backwards against the pre-ZF chain)
  ZP on f048a78            PREFLIGHT: PASS. Its export carries 376 files, 0 withheld-shaped names
  the PLAN, as printed     the hand's file 2026-10-13-gemini-ZF-PLAN-chain-printed-f048a78.txt (the lane's private record), sha256/16 1a3f6efcb9a67a18
```
**The lead re-counted the plan from the file, not from the post:** 276 legs · 138 `gemini-4-argon-high` + 138 `gemini-3.8-flash-high` ·
46 conditions, each on both models · exactly 3 replicates for every (model, condition) pair, 92 of 92 · legs 1–4 are the two tripwire pairs
of §G2. Fields greenfield/brownfield and extras none/statement/spec-change, as §G1 registers.

**A1.4 · CARRIED TO THE FIRE, not met here:** the lane canary must read HEALTHY before ZT's first launch (the hand's preflight read it
UNMEASURED, its process not alive). The hand brings it up and reads it in the fire post. **Sequencing stays §G0.6:** ZT fires after O60's batch
score ends. The ZT → Z release is the lead's, on the §G2 reads of the four tripwire cells.

## ⚖️ ADDENDUM 2 — THE SET'S TOKEN FIGURE INCLUDES SUB-AGENT CONVERSATIONS, FROM THE FIRST CELL. APPENDED before any model call; all text above, signature included, untouched.
*bench (lead), 2026-10-13, on the helm's O57 ruling (17:57). A change to what the run MEASURES, so it is registered before ZT's first call.*
**WHY:** the lane's meter (`agy_meter_v3.py`) reads the parent conversation's stream only, so a sub-agent the subject dispatches is never
metered. Over the 272 Gemini 3.x cells of record that left 434 M T unmetered on salt-diet (≥ +15.2 %) against 0.9 M on plain (+0.2 %), an
arm-correlated hole in favour of the arm under test (`evidence/o57-agy-subagent-unmetered-2026-10-13/`).
**THE RULE FOR THIS SET:** each cell's T is the meter's T PLUS the T of every conversation in the cell's client home that the parent stream
does not carry, read from that conversation's own `conversations/<id>.db` by the O57 decoder. Both are printed per cell: `meter T`,
`sub-agent T`, `conversations`. **A cell whose parent db does NOT reproduce its meter's T (the decoder's positive control, cell by cell)
prints its sub-agent T as UNMEASURED**, never as 0. **What runs (kent's read, 2026-10-13 19:23):** a copy-only sentry snapshots every
conversation db every 60 s, and a conversation set aside before it is read is read from its newest snapshot. A snapshot older than the end
of phase 1 prints sub-agent T as `≥ N` (control `STALE`), and a sub-agent the stream names whose db exists nowhere prints
`UNMEASURED(named-no-db:k)`. This closes the gap that left 60 level-8 cells as floors.
**WHAT IT DOES NOT CHANGE:** the 276 legs, the export, the caps (wall and turns; T is never a cap here), the tripwire reads (§G2 adds
sub-agent T beside T), and the historical 3.x column, which keeps its published T with the O57 limit printed beside it.

## ⚖️ ADDENDUM 3 — SCORING RUNS UNDER THE BELT, AND THE SUBJECT-CONTROLLED VERDICT CLASS IS DECLARED OPEN. APPENDED; all text above, signature included, untouched.
*bench (lead), 2026-10-13, on systems' measurement (21:36) and the lead's and the helm's ruling (arm A, 21:37). A change to how a cell is SCORED,
registered before any ZF figure is read. Cells are not touched.*
**WHY:** desk ZQ's default is *"no v3 cell runs without at least the belt"*. At the export `f048a78`, every score executes the subject's
`solution.rs` linked with the withheld driver ON THE SCORING BOX: `score_wave_v3.sh` runs the rung's `run_tests.sh`, which runs the built
driver through `run_limited`, whose `EXEC_PREFIX` is empty and set by no scorer. So a ZF score ran subject-authored code, from a model no cell
had met, with network open and the scoring user's home readable and writable. The CELL runs inside the client's fence; the gap was the SCORE.
Levels 6–8 were scored the same way. Nothing here re-opens their record (census ADDENDUM 34).
**THE TWO SHAS:**
```
  CELLS     fire from f048a78 as ADDENDUM 1 released it. Unchanged: the belt is inert unless a scorer sets V3_DRIVER_BELT.
  SCORING   runs from 3947740 = f048a78 + the belt (cdc74b4, re-cut f91f88c) + its drive receipts; f048a78 is its ancestor.
            f048a78..3947740 touches 9 files, all under harness/systems-v3/, and NO file under tasks/.
```
**THE RULE FOR THIS SET:**
1. Every ZF score runs from `3947740`'s scorer, which sets `V3_DRIVER_BELT` to `driver_belt.sb` (sha256/16 `9906210a6f8ee100`) and refuses
   to run without it. The ONE binary each suite runs (the withheld driver linked with `solution.rs`) runs under that profile, and
   `run_limited` closes inherited file descriptors 3 to min(OPEN_MAX, 4096) before the exec (a profile cannot gate an fd that is already open).
   **What the profile is, read at the object:** `(deny default)`, then allows for exec of the binary itself, `sysctl-read`, `process-info*`
   and `signal` targeted at the process ITSELF, a write to `/dev/null`, file METADATA, and file reads of an allowlist (the binary, `/`,
   `/usr/lib`, `/System`, `/Library/Apple`, `/dev`). The Rust runtime aborts at start-up without the three self-targeted allows (measured).
   **Driven** (`harness/systems-v3/RECEIPT-zq-belt-2026-10-13.md` at `3947740`, on Crc32's real rung): with no belt, every probe succeeds
   (read · list · write · a network connect · exec · fork · a signal to another process · POSIX shared memory · a write to the scorer's open fd 9);
   with the belt, all nine are DENIED and the suite still scores TESTS 6/6. Each allow re-added to the profile flips exactly its own probe,
   and removing `run_limited`'s fd closing on the committed tree turns the fd arm red. The sweep reads "16 of 16 rungs with a reference
   AGREE" belted and unbelted, each belted run with one belt line. The signal, shared-memory and fd channels were found by kent's
   non-author probe of the first cut (21:53), which was an allow-default denylist; this cut is the answer to that probe.
2. A score whose output does not carry EXACTLY one belt line for that sha is UNBELTED: it is not a ZF score, never PASS, and in no
   denominator (as a score not run on the released export is not, T1).
3. **Z001's score of 2026-10-14T04:21:30Z ran UNBELTED.** It stays in the receipts, labelled so, and no table reads it. Z001 is re-scored
   under the belt from its existing cell, by copy, never by re-dispatch. Because it had already run, it was audited statically at zero spend
   (systems, 21:38, corrected 21:38:45): a table-driven CRC-32 with no `use`, I/O, macro or `unsafe`; the crate's one dependency is the
   harness's pinned `vstd`, the same in both arms, and the template has no build script; no withheld-suite or scorer file and none of the
   27 credential files changed after 04:20Z. CLEAN.
4. The scoring HOLD (the hand's `SCORE-HOLD` file, 21:41) is released when this addendum is merged with a non-author signature, and not before.
**DECLARED OPEN, NOT CLOSED BY THE BELT (desk ZQ):** (a) the driver and the subject's code are ONE process, so the rc, the TESTS line and
anything printed are reachable by the subject's code. The belt removes SIDE channels, not the verdict channel. A forged verdict needs an
adversarial subject, and no ZF result claims the absence of one. (b) A compile-time `include_str!`/`include!` in `solution.rs` can read a file
into the binary during `cargo build`, which is not under the profile, because the build needs the registry. (c) File METADATA stays readable
(existence, size, times; not content), and `sysctl-read` stays allowed. (d) Denied by the default but NOT probed: mach-lookup, sysctl write,
IOKit, other IPC. (e) An inherited fd ABOVE 4096 survives the close loop; the scorer holds none today (kent's LOW-1, 22:04). (f) Creating a socket still
succeeds; connect and bind are what is denied (kent's LOW-2). (g) Measured on one macOS host, one OS version. The full form (observations only, with an external comparator) is ZQ's
re-freeze for the next v3 campaign.
**WHAT IT DOES NOT CHANGE:** the 276 legs, the cell export, the caps, the meter (ADDENDUM 2), and the tripwire reads, except that a
tripwire's PASS read waits for its belted score.

## ⚖️ ADDENDUM 4 — THE TRIPWIRE READS AND THE SET'S PRICE (§G2). APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-10-13. §G2: "The set's price is written into an addendum from those four cells, and from them alone." The four cells are
read from the hand's harvest receipts and its per-leg §G2 posts (2026-10-13 21:21–23:38 PDT). Every score is BELTED (ADDENDUM 3; scorer
`39477409d58e`, profile `9906210a6f8ee100`). n = 1 per cell: these are tripwire reads, not results, and no comparison is drawn from them.*
```
  cell                          landed  belted score  served (client echo)     turns  wall s   T (meter + sub-agent)          pool AFTER (5h / weekly)
  Z001 Crc32 gf none plain  r1  YES     PASS 6/6      gemini-4-argon-high       3      763.1    1,777,609 +   213,722            98 / 98  (04:21:43Z)
  Z002 Crc32 gf none plain  r1  YES     PASS 6/6      gemini-3.8-flash-high     3      345.0    3,843,838 +   543,436            98 / 98  (05:00:27Z)
  Z003 Crc32 gf none salt   r1  YES     PASS 6/6      gemini-4-argon-high       3     1301.7    6,536,722 +    28,533            95 / 98  (05:24:34Z)
  Z004 Crc32 gf none salt   r1  YES     PASS 6/6      gemini-3.8-flash-high     4     2859.7   19,453,186 +   954,332            99 / 98  (06:38:34Z, after the 5h reset)
```
Pool BEFORE the first cell: 99 / 99 (20:56:41 PDT). Z001's first score (04:21:30Z) ran UNBELTED and is not a figure; its belted re-score is
the row above and is identical to it. The /usage reading moves in whole points with ±1 noise (the hand's declaration).
**THE PRICE, two ways, because one pair cannot choose between them.** Crc32 is the cheapest problem in the 3.x Flash record: its 36
phase rows average 561.8 s against 903.5 s over all 168 (`evidence/v3-cost-tables-2026-09-28/agy-steps-raw.tsv`), a factor of 1.608. And a
model's 138 cells are 168 phases, because a spec-change cell has two. So a Crc32-only mean must be scaled before it prices the set:
```
  A  four-cell mean wall per phase × 1.608 × 168 phases per model    Gemini 4  77.5 h · control 120.2 h · total 197.7 h serial cell wall
  B  §G2's 3.x Flash basis (42.2 h, all 168 phases, all problems)     control   42.2 h · Gemini 4  27.2 h (× the pair's wall ratio 0.644) · total 69.4 h
  elapsed ÷ cell wall, measured on ZT: 2.67 h ÷ 1.46 h = 1.83 (it INCLUDES tonight's ZQ hold, so it is an upper figure, not a rate)
  ⇒ elapsed   A: ≈ 362 h ≈ 15.1 days    B: ≈ 127 h ≈ 5.3 days
```
The pair's wall ratios point in OPPOSITE directions (Gemini 4 ÷ control: plain 2.21, salt-diet 0.455), so neither arm's ratio prices the set, and
the n = 1 Flash salt-diet cell (2,859.7 s) is longer than all 18 3.x Flash Crc32 salt-diet phase rows in that file (any field; their longest is
2,095.7 s). The two projections straddle the review date.
**THE STOP RULE (§G2) APPLIES IN ITS POSTED-ORDER FORM.** Projection A puts the set past the ZF review date (2026-10-28); B does not. §G2 asks
the lead to post an order before any cell beyond the tripwires, and this is it:
1. The set runs in §G2's order: greenfield (none · statement), then brownfield (none · statement), then spec-change, condition by condition,
   n = 3 each, interleaved by condition. So a cut at the tail removes spec-change first, as §G2 orders, then brownfield/statement.
2. **RATE CHECKPOINT, 2026-10-20 (the weekly reset):** the lead projects the finish from the cells completed by then (their own elapsed per
   phase, scaled per problem by the 3.x ratios above). If the projection passes 2026-10-27, the lead posts the cut, as WHOLE condition
   pairs from the tail, never one model's arm. Every condition left short is reported short, and n is never reduced quietly.
   **That choice is the Captain's** (the helm, 23:53): cutting tail pairs or moving ZF's 2026-10-28 review date is an intention, so it goes
   to him as a pack ask, with the measured projection and the pairs that would be cut. **Default if he does not rule at that sitting: the cut**.
3. **POOL CHECKPOINT:** the hand reads /usage at each condition's dispatch. If the weekly reading falls to **25 % or below before its
   2026-10-20 reset**, the set pauses at the next condition boundary and rule 2's cut is applied then.
**THE RELEASE:** the set continues from the tripwires on this addendum, under the order and checkpoints above.
**EVERY ZF SCORE ROW CARRIES ITS LIMIT (the helm, 23:51):** wherever a belted verdict is printed (the hand's harvest receipts, any table, the
result), the row carries `verdict channel: OPEN (ZQ (a), ADDENDUM 3)` beside it. The scorer's header already prints it once per file. This
puts it on each row, so a reader of a single row meets it.
**LIMITS ride beside every PASS above and in every ZF table:** ADDENDUM 3 (a)–(g); the verdict channel is the subject's own stdout.

## ⚖️ ADDENDUM 5 — THE RUN EXPORT MOVES TO `906775a` FROM THE RESUME (A FALSE WARM-UP REFUSAL). APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-10-14, on systems' measurement (bus 14:23) and gemini's (14:23). A change to the harness that LAUNCHES a cell, registered
before the first model call it governs. Nothing a cell measures changes, and the scorer stays ADDENDUM 3's. ⛔ **No leg fires on `906775a`
before a non-author signs this addendum.***

**A5.1 · WHAT HAPPENED.** Leg Z018 (FreeList · greenfield · none · plain · r3 · `gemini-3.8-flash-high`) stopped on 2026-10-14 at 21:20:26Z
with **zero model spend**: its cell was BUILT, FENCED and BATTERY GREEN, then the credential warm-up REFUSED with an empty reason, and the cell
was never launched. At the objects (the wave log on the run box, the client log, the token file): the client REFRESHED the token at
21:18:56Z (a full window, expiry 22:18:55Z). The warm-up's PONG on the `-high` model then ran past a FIXED 90 s cap (18 × 5 s) and was killed,
so `agy_wave_v3.sh` refused a window the refresh had just provided. Downstream the same cause was labelled twice more, as the driver's
`MODEL UNREAD` and the chain's `phases 1,2` stop. Neither label is the cause. **The refusal was FALSE.**

**A5.2 · THE CHANGE: `f048a78` → `906775a`** (saltbench-systems, two commits by systems, `f048a78` an ancestor):
```
  70049f2  selftest_agy_warm_v3.sh, committed RED on the unfixed wave script: 7 passed, 4 failed (the incident reproduced, empty reason included)
  906775a  agy_wave_v3.sh, _warm_credential_locked + warm_window_rescues; selftest_all_v3.sh registers the new arm
           (a) after a non-SUCCESS warm-up, a cell launches only if the master token CHANGED **and** now covers AGY_CRED_MIN_SECONDS
               (2400 s). A change alone is refused, because a failed refresh is a write too.
           (b) the cap is declared, AGY_WARM_SECONDS, default 300 s (was a fixed 90 s). A kill at the cap is SAID, with stderr and the
               stream tail. The reason is never empty.
  diff f048a78..906775a: 3 files, all harness/systems-v3/ (agy_wave_v3.sh +31/-4 · selftest_agy_warm_v3.sh new · selftest_all_v3.sh +3)
```
**Unchanged, read in the code:** the order FENCE RENDERED → BATTERY GREEN → CREDENTIAL WINDOW → fire, and the canary gate in the supervisor
above it. The battery and the canary still gate every launch. The fix changes only the warm-up's own verdict. A warm-up that advanced the
token proves the credential's window, never the model. A warm-up that returns SUCCESS takes the same path as before.

**A5.3 · RECEIPTS**
```
  selftest_agy_warm_v3.sh --mutants @906775a, lead box (the lead, re-driven)       12 passed · 0 failed · mutants 3/3 killed
      no-window-rescue → 1 arm red · silent-kill → 2 arms red · advance-is-enough → 1 arm red
  the RED commit's selftest @70049f2 on the UNFIXED wave script (f048a78's bytes)  7 passed · 4 failed (the lead, re-driven)
  selftest_all_v3.sh @906775a (systems' receipt; NOT re-run by the lead)          225/231 · 0 failed · 6 skipped by design (withheld-tree arms)
  THE EXPORT, cut by the lead: studio_export.sh <run box> --ref 906775a --no-toolchain --unreferenced-dest
      dest ~/projects/claude/saltbench-systems-v3-export-906775a · 377 files · listing sha256/16 cba51ae0483b9b25 · withheld-shaped names 0
      required-ancestor gate OK (5 of 5; serial=3, block digest 6b3de761118f9f42, amendment read at saltbench bdbb89bbdd05)
      diff -rq against the f048a78 export: the 3 files above + EXPORTED-FROM.sha + REQUIRED-ANCESTORS.tsv (its non-comment rows IDENTICAL)
      agy_wave_v3.sh on the host sha256/16 6868e0a2ea9a0c39 == git show 906775a
      selftest_agy_warm_v3.sh --mutants, on the run box from that export            12 passed · 0 failed · mutants 3/3 killed
  --no-toolchain: the toolchain is unchanged from the f048a78 export (the change touches no toolchain path), and a cell was running on the box.
```
**A5.4 · WHICH CELLS RAN ON WHICH EXPORT.** Read from each leg's `drive.log` (`drive EXPORT …`): **Z001–Z018 attempt 1, 18 of 18, ran on
`f048a78`.** Every leg fired after this addendum's signature runs on `906775a`, and every ZF table row carries its export sha. The two
exports launch a cell identically whenever the warm-up returns SUCCESS, which it did for every cell that launched before Z018.

**A5.5 · Z018 IS RE-QUEUED, NEVER CARRIED** (gemini's default, ruled by the lead, bus 14:2x). Its END-MARKER reads `rc=0 … WAVE-DONE`, so a
plain resume would CARRY it as done when it never ran. Its END-MARKER and its run-box cell dir are renamed `…REFUSED-CREDENTIAL-<time>`, and
the chain re-fires the leg. Attempt 1 spent no model call and is **not a replicate**: n stays 3 and the leg's replicate is the re-fire.
The chain's PHASES check, which read the refusal as a phase defect, is a tool defect (gemini's, red-first), and it does not touch a cell.

**A5.6 · LIMITS.** The 300 s cap is a judgment, not a measurement: one PONG on `gemini-3.8-flash-high` took ~70 s of model time after a
refresh. One incident, one model. The chain's resume order is unchanged (Deep Review r3 → x86 → N0-T″ → Z resumes), and so are ADDENDUM 4's
rate and pool checkpoints.

## ✍️ NON-AUTHOR SIGNATURE — kent, 2026-10-14 15:02 PDT, of ADDENDUM 5 at blob `b3beba12a5c5` (head `7b4cbd9166c0`)
kent read the diff and re-drove the selftests itself (bus 2026-10-14 15:02:46): 12/0 with mutants 3/3 at `906775a`, and 7/4 for the red commit on `f048a78`'s
wave script. It found the rescue, the cap and the reason text all inside the non-SUCCESS branch, and the rescue condition exactly as A5.2 states it. It also
noted one unnamed difference: the wait now polls each 1 s (it was 5 s × 18), so a SUCCESS is seen up to 4 s sooner, with the same verdict.
**A5.7 · kent's RIDER, carried as signed:** the rescue branch is entered by ANY non-SUCCESS warm-up, not only a PONG killed at the cap. A warm-up whose stream
ended with status ERROR (the client refreshed, then the model call failed) is rescued the same way if the token changed and covers 2400 s. So the rescue
cannot tell a slow PONG from a failed one. The battery and the canary still gate the launch, and the log line carries the stream tail. **Every ZF row whose
leg launched through a rescue says so** (`warm-up: RESCUED`, with the logged reason), so a reader of that row meets it.

## ⚖️ ADDENDUM 6 — Z019'S WEDGE: AN ARM-CORRELATED LOSS, NOT RE-FIRED; AND A WEDGE STOP FROM ITS OWN RELEASE. APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-10-15, on gemini's Z019 cap report (bus 2026-10-15 01:59) and the lead's census of the run box. Clause A6.2 rules on a cell
that has ended. Clause A6.3 changes the turn loop's stop rule. It is registered here before any model call it governs, and ⛔ **it binds no leg
before a non-author signs this addendum AND a release line below names the export that carries it.** It never enters a running wave.*

**A6.1 · WHAT HAPPENED.** Leg Z019 (FreeList · greenfield · none · salt-diet · r1 · `gemini-4-argon-high`, export `906775a`) fired 02:51:16Z and
ended at 08:54:17Z, wall 21,724.7 s, T 231,734 (sub-agents 0). Its first result arrived at 389.6 s with status SUCCESS and an EMPTY response. Every
later result (continue turns 1–11) was identical to it in conversation, duration and usage. So the conversation advanced nothing for about 5.9 h,
and each continue turn came back as a 30-minute partial return. The loop counted each partial return as a turn and stopped on TURN-TIMEOUT at the
wall. The cell's END reads `ARM-NOT-RECEIVED phase-1 the subject never echoed its delivery nonce`. The belted score row reads
`BRIEFING VOID(NO-BRIEFING) · FAULT shell-ok+fence-ok · END ARM-NO · NOT-SCORED, excluded by its own receipt`. The lead ruled at 2026-10-14 22:12
(bus) to touch nothing and let the wall cap end it. That ruling stands: no hand touched the cell.
⚠️ The turn loop labels all 12 empty turns `TURN-DENIED … a tool needed unsandboxed`. The cell's client log contains no occurrence of
"unsandbox". The label is inferred from an empty response, not read from the client, so **no ZF row carries that cause.**

**A6.2 · THE CENSUS, AND WHY Z019 IS NOT RE-FIRED.** `evidence/zf-wedge-census-2026-10-15/` (script, and its output at K = 2 and K = 3, run on the
run box over every `~/cells*/*/ctl/stream-*.ndjson`) keys each result on its envelope only (conversation, duration, usage), never on the response
text, so it cannot read either arm's vocabulary:
```
  arm (ctl/arm)   streams   wedge (>= 2 consecutive identical results)   a single repeat only
  salt-diet         253       4                                          4
  plain             292       0                                          0
  the 4 wedged cells: l6vgfs02 (level 6, LZW, Flash) · l8rpss01 (level 8, LRU, Pro, spec-change) · nabhfs03 (block NA, BinomialHeap, Flash) · zfafgns101 (Z019)
  every wedged cell stayed identical from result 2 to its cap; NONE recovered. The longest identical run in any non-wedged stream is 1.
```
If the arm did not matter, the chance that all 4 fall in salt-diet is about (253/545)^4 ≈ 0.05. This suggests a link but does not settle it.
**THE RULING, on the sign:** if the salt-diet arm leads the subject into this state, the wedge is an OUTCOME of the treatment, not a transport fault.
Re-firing it is the top-up that level 8 refuses (`AMENDMENT-gemini-level8-2026-09-16.md` §M4 rule 2). Not re-firing keeps a loss on the arm under
test, and a bias against that arm cannot manufacture a positive for it. So:
1. **Z019 is NOT re-fired.** Its score row stands as written: NOT-SCORED, with its own VOID(NO-BRIEFING) reading.
2. **EVERY ZF PASS RATE IS REPORTED TWO WAYS, SIDE BY SIDE** (the helm, bus 2026-10-15 02:05, adopted). If the wedge is a treatment outcome,
   then leaving it out of the denominator removes the arm's own failures from its rate. That favours the arm that hits it. So:
   (a) **counted:** each wedge cell is a FAIL in its arm's denominator (intention-to-treat over the cells fired);
   (b) **excluded:** the scored cells only, as the score file reads.
   **Where (a) and (b) differ, (a) is the headline**, because it is the reading that goes against the arm. Every ZF table also prints, per arm,
   `fired · scored · wedge · other VOID` beside the two rates, so a reader of either rate sees which cells it covers. Z019's condition
   (FreeList-gf-none-salt, `gemini-4-argon-high`) is reported at the n it reached.
3. **Any later ZF cell that wedges takes the same treatment**: no re-fire, and it is counted under point 2.
4. The lead's 2026-10-15 BOOTED post ordered a re-fire. It was withdrawn by the same lead before any call (bus, the post after it), on this census.

**A6.3 · THE WEDGE STOP.** In `agy_turnloop_v3.py`, after each continue turn returns, the loop compares the new result with the previous one on
(conversation_id, duration_seconds, usage). **When THREE consecutive results are each identical to the one before, the loop stops with
`done_reason = "WEDGED"`.** The P-PERSIST probe still goes last, exactly as on every other stop. The cell is scored as it lands, like a cap-ended cell.
- **Why 3:** at K = 2 and at K = 3 the census fires on the same 4 cells and on nothing else (`census-K2.tsv`, `census-K3.tsv`). The longest
  identical run outside a wedge is 1, so K = 3 leaves a margin of 2. On Z019, K = 3 stops at result 4: about 1.5 h after the first result,
  where the wall cap stopped it at about 5.9 h.
- **It reads the envelope, never the response text,** so it is blind to which arm wrote the response. ⚠️ **It is NOT arm-blind in what it binds:**
  on the census it binds salt-diet cells only. On this evidence it changes WALL and TOKENS, never an outcome, because no wedged cell recovered.
  A WEDGED cell's row carries `done_reason WEDGED` and its own wall. Every cost comparison prints the WEDGED count per arm beside it. Where a
  historical column ran wedges to the cap, that comparison names the difference.
- **What it does NOT do:** it does not end a slow cell. A cell whose results differ from each other, however slowly, never trips it. It does not
  change the caps, the scorer (ADDENDUM 3's), the meter (ADDENDUM 2) or the set's order.
- **OWED BEFORE IT BINDS (systems' or gemini's build, the lead's read):** a red-first selftest, committed red on the current turn loop, with
  (i) Z019's own stream as the positive fixture (it must stop WEDGED at result 4), (ii) a stream with one repeat followed by progress (it must NOT
  stop), and (iii) a mutant at K = 2 and a mutant that compares the response text, each of which an arm must kill. Then an export cut from the
  green head, and a release line below naming that sha. Legs fired before that line run without the stop, and their rows say which rule they ran under.

**A6.4 · LIMITS.** The census counts streams on the run box, including copied cell dirs. It was not de-duplicated, but the 4 wedged cells are 4
distinct cells. Four events is a small number, and the salt-diet link is suggestive, not established. The cause of the wedge is UNMEASURED: in
three of the four the first result has an empty response, and the subject's last output step was large (Z019: 30,669 output tokens in one
response). That is a reading, not a mechanism. How the three earlier cells sit in their own levels' records is not re-opened here. blockNA counts
nabhfs03 as a non-landing (`evidence/blockNA-2026-09-28/rulings.tsv`), which matches A6.2. The other two are a question for the lead's census
work, routed separately.

## ✍️ NON-AUTHOR SIGNATURE — kent, 2026-10-15 02:10 PDT, of ADDENDUM 6 at blob `881d5fc559cb` (head `0e4d12e876d7`), A6.2 ONLY
kent re-resolved both pins at the forge immediately before signing, and re-drove `wedge_census.py 3` from the PR head on the run box (09:09Z,
read-only): plain 292 / 0 · salt-diet 253 / 4 · longest non-wedge run 1. The same four cell ids, each firing at result 4 (l8rpss01 at 5). Signature
file in the fleet record (seat `a7d89beab`). **WHAT BINDS: A6.2 only.** A6.3, the wedge stop, binds nothing: no release line exists, and no code was signed.
**Riders, carried as signed (none changes the signature):** (1) the ≈ 0.05 treats STREAMS as trials, and 8 cell ids carry more than one stream while
9 salt-diet streams have zero results, so it overstates independence (A6.4's "not de-duplicated"). (2) The merge is the merger's read of the
required checks, not this signature. (3) The signature says nothing about the two earlier cells' published denominators.
**Correction carried from the same read:** the "30,669 output tokens" in A6.4 is one step's output_tokens in the transcript; the result envelope's
own figure is 33,045.
