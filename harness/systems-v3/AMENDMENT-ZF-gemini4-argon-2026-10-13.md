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

## ⚖️ ADDENDUM 6 · RELEASE — A6.3 AT EXPORT `2f32f60`. APPENDED; all text above, signatures included, untouched.
*This is the release line A6.3 asks for. ⛔ It binds no leg until a non-author signs A6.3 and this release below. Legs fired before that
signature run on `906775a` without the stop, and their rows say so.*

**A6.5 · THE CHANGE: `906775a` → `2f32f60`** (saltbench-systems, two commits by systems, `906775a` an ancestor):
```
  a43e1d8  agy_turnloop_v3.py selftest, committed RED on the unfixed loop: 53 passed, 5 failed
  2f32f60  agy_turnloop_v3.py, the stop: once a continue turn has returned, if the last 3 results each repeat the one before on
           (conversation_id, duration_seconds, json.dumps(usage, sort_keys=True)), done_reason = WEDGED, the loop breaks, and the
           P-PERSIST probe is sent as on every stop. The key is wedge_census.py's key, character for character. The response text is
           never read. The summary gains wedge_k and wedged_at_result. rc stays 0, as for the caps.
  diff 906775a..2f32f60: 3 files, all harness/systems-v3/ (agy_turnloop_v3.py +138/-1 · fixtures/README.md +6 ·
           fixtures/zf-z019-stream-1.results.ndjson new, 12 lines)
```
**ORDER (systems' one choice, accepted by the lead):** the wedge check runs AFTER the LANDED check and BEFORE the claim and cap checks. A cell
whose artefact exists still ends LANDED, and a wedged cell is named WEDGED rather than by the cap it would reach later.

**A6.6 · THE ARMS A6.3 OWES, AS BUILT**
```
  (i)     Z019's own 12 result records, byte-exact (lines 47-58 of its ctl/stream-1.ndjson, source sha256/16 765d8284c90edabb; the
          fixture's sha256/16 27b0c2b3b2e3da4b, re-hashed by the lead against both). Replayed with --max-turns 40: WEDGED at result 4,
          after 3 continue turns, the probe sent last.
  (ii)    one repeat, then a differing result: TURN-CAP, not WEDGED. SYNTHETIC: the census's four single-repeat salt-diet streams all
          end on the repeat, so none is a repeat followed by progress (systems read all four).
  (iii-a) two repeats, then a differing result: TURN-CAP.        (iii-b) an identical envelope under a different response each turn: WEDGED at result 5.
  MUTANTS (agy_turnloop_v3.py --mutants): k-is-2 · compare-reads-response · no-stop · stop-skips-probe. All four killed.
```
The fake client now gives each turn its own duration_seconds. Otherwise its constant envelope would trip the stop on the 50 older arms,
which are unchanged and green.

**A6.7 · RECEIPTS**
```
  selftest @a43e1d8 (RED commit, unfixed loop), lead box, re-driven by the lead     53 passed · 5 failed: (i) ×4 and (iii-b)
  selftest @2f32f60, lead box, re-driven by the lead                                58 passed · 0 failed
  --mutants @2f32f60, lead box, re-driven by the lead                               4 of 4 killed (k-is-2 by 5 arms · compare-reads-response by
                                                                                    (iii-b) · no-stop by 5 · stop-skips-probe by (i))
  THE EXPORT, cut by the lead from a throwaway clone at 2f32f60:
      studio_export.sh <run box> --ref 2f32f60a06dd --no-toolchain
      dest ~/projects/claude/saltbench-systems-v3-export-2f32f60 · 378 files · listing sha256/16 dd179d14e5f23979 · withheld-shaped names 0
      required-ancestor gate OK (5 of 5; serial=3, block digest 6b3de761118f9f42, amendment read at saltbench 7cbe2153f1e5)
      diff -rq against the 906775a export: the 3 files above + EXPORTED-FROM.sha + REQUIRED-ANCESTORS.tsv (only its @amendment-commit line differs)
      agy_turnloop_v3.py on the host sha256/16 80a5ef7d6d502ba2 == git show 2f32f60
      selftest and --mutants, on the run box from that export, python 3.9.6           58 passed · 0 failed · mutants 4 of 4 killed
  --no-toolchain: the change touches no toolchain path, and ZF legs use no Verus (the host keeps none at this box's path).
```
**A6.8 · WHICH LEGS RUN ON WHICH EXPORT.** Every leg fired after the signature below runs on `2f32f60`, and its row carries that sha. A leg
already running when the signature lands finishes on `906775a`. The two exports launch a cell identically; they differ only in when the turn
loop stops, and only on a stream that repeats its envelope three times.

**A6.9 · LIMITS.** K = 3 is fitted on one census of 4 wedged streams (A6.4). Arm (ii) is synthetic, because no real stream shows a repeat
followed by progress. The stop has never fired on a live cell. Its first live firing is reported to the lead with the cell's stream, before
the next leg. The TURN-DENIED label (a LOW routed to systems from ADDENDUM 6's read) is not in this export; it comes as its own commit, with its own release.

## ✍️ NON-AUTHOR SIGNATURE — kent, 2026-10-15 02:46 PDT, of ADDENDUM 6 · RELEASE at blob `28dec268d75f` (head `4e08111bdef9`), A6.3 AT `2f32f60` ALONE
kent re-resolved both pins at the forge at 02:45:52, immediately before signing (main's file a byte prefix of the PR's, +53/−0; 12 of 12 checks
SUCCESS). He re-drove from `git archive` of the bare repo: the code diff 906775a..2f32f60 read in full · selftest @2f32f60 58/0 · @a43e1d8 53/5
((i)×4 and (iii-b)) · --mutants 4 of 4 killed · agy_turnloop_v3.py sha256/16 80a5ef7d6d502ba2 == A6.7's host sha · the fixture byte-equal to
lines 47–58 of Z019's stream. **Beyond a re-run:** he executed the loop's own wedge key and run counter, lifted from the 2f32f60 file, over all
545 recorded streams on the run box. 4 fire: l6vgfs02 at 4 · l8rpss01 at 5 · nabhfs03 at 4 · zfafgns101 at 4. These are the census's four at
the census's results. 0 results lack all three key fields. Signature file in the fleet record. **WHAT BINDS: A6.3 at `2f32f60`.** The label
commit `6993727` is not covered.
**Riders, carried as signed (none changes the signature):** (1) if a future client stamps a changing duration on repeated partial returns,
the stop goes BLIND, never false: the old wall-cap behaviour, the safe direction. (2) A result carrying none of the three fields would
repeat as (None, None, "null"). 0 of 545 do, and the code does not defend it, so the first live WEDGED row is read against that. (3) K = 3
on four streams, arm (ii) synthetic, never fired live: A6.9.
**Limits of the signature:** kent's re-drive ran on python 3.14.4; the 3.9.6 run-box receipts are the lead's. He read the turn-loop diff,
not the rest of the file, and fired nothing live.

## ⚖️ ADDENDUM 6 · RELEASE 2 — THE EMPTY-TURN LABEL AT EXPORT `6993727`. APPENDED; all text above, signatures included, untouched.
*⛔ It binds no leg until a non-author signs it. Until then legs run on `2f32f60` (A6.8), and their logs carry the old label.*

**A6.10 · THE CHANGE: `2f32f60` → `6993727`** (saltbench-systems, two commits by systems, `2f32f60` an ancestor; agy_turnloop_v3.py +46/−6):
```
  0c9c64f  selftest, committed RED on the current label: 57 passed, 3 failed
  6993727  every empty turn is logged "EMPTY-TURN n produced NO OUTPUT". A cause is printed only when the client's own stderr (the loop's
           --err file) carries the client's auto-denial sentence, `a tool required the "unsandboxed" permission`; otherwise the log says
           "cause NOT READ". The count is per run, as the new summary field empty_turn_denial_markers, because stderr is not keyed to a turn.
           turns_no_output, the existing field names and the rc-13 dead-run rule are unchanged.
```
**WHY:** the loop labelled every empty turn "TURN-DENIED … a tool needed `unsandboxed`" without reading any cause. On Z019 the 12 such
lines are the loop's own label; the client's stderr and the client log carry 0 of the client's denial sentence. Under `6993727` those turns
read "EMPTY-TURN, cause NOT READ". It changes a LOG LINE and adds one summary field. It changes no stop, cap, score or outcome.
**CONSUMERS (systems' search, git grep -F):** no code parses the old line. Public hits are prose in amendments and one RESULT, plus
cell_facts.py, whose comment says it never reads that line.

**A6.11 · RECEIPTS**
```
  selftest @0c9c64f (RED), lead box, re-driven by the lead          57 passed · 3 failed (the three empty-turn arms)
  selftest @6993727, lead box, re-driven by the lead                60 passed · 0 failed
  --mutants @6993727, lead box, re-driven by the lead               5 of 5 killed (A6.3's four, plus cause-assumed, killed by the NOT-READ arm)
  THE EXPORT, cut by the lead: studio_export.sh <run box> --ref 6993727 --no-toolchain
      dest ~/projects/claude/saltbench-systems-v3-export-6993727 · 378 files · withheld-shaped names 0 · ancestors 5 of 5, digest 6b3de761118f9f42
      diff -rq against the 2f32f60 export: agy_turnloop_v3.py + EXPORTED-FROM.sha only
      agy_turnloop_v3.py sha256/16 51ff30a6fc14eb3e · on the run box from that export, python 3.9.6: 60 passed · 0 failed · mutants 5 of 5
```
**A6.12 · LIMITS.** The marker sentence was read in one earlier cell's stderr; a client that words a denial differently is reported as
"cause NOT READ", which is the safe direction. The count is per run, so it cannot say which turn was denied.

## ✍️ NON-AUTHOR SIGNATURE — kent, 2026-10-15 02:53 PDT, of ADDENDUM 6 · RELEASE 2 at blob `3ea43f2e273d` (head `17e1a1fa188c`), THE LABEL AT `6993727`
kent re-resolved both pins at the forge at 02:52:57 (main's file a byte prefix of the PR's, +30/−0). He re-drove from `git archive` of the
bare repo: the diff 2f32f60..6993727 read in full · selftest 60/0 · RED 0c9c64f 57/3 (the three empty-turn arms) · --mutants 5/5 ·
agy_turnloop_v3.py sha256/16 51ff30a6fc14eb3e == A6.11's host sha. **The premise, at the object on the run box:** Z019's client stderr
(1,414 B) and client log carry 0 occurrences of "unsandboxed". The only file in its ctl that does is the loop's own stderr (12 lines, the old label). The
`--err` file is the client's stderr, so the new check cannot read the loop's own label. The marker sentence is real: 40 lines across earlier
pilot cells. A different denial sentence appears 3 times and is correctly not matched. **WHAT BINDS: the label at `6993727`.**
**Riders, carried as signed (none changes the signature):** (1) "cause READ" is counted per run, so one denial anywhere in a run's client
stderr prints READ over every empty turn of that run. The line says "counted per run, not attributed per turn", and it is read that way.
(2) A reworded client sentence reports NOT READ, the safe direction. (3) systems' consumer search was not re-driven.
**Limits of the signature:** python 3.14.4; the 3.9.6 run-box receipts are the lead's; nothing fired live.

## ⚖️ ADDENDUM 7 — THE 30-MINUTE PER-TURN PRINT TIMEOUT BINDS THE TREATED ARM: A DECLARED LIMIT, NOT A CHANGE. APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-10-22, on gemini's Z235 observation (bus 2026-10-22 05:39). This addendum changes nothing that any leg measures: no cap, no
export, no re-fire. It declares a limit that every ZF table carries, and it is written before the set's RESULT.*

**A7.1 · WHAT GEMINI SAW.** In Z235 (FreeList · greenfield · spec-change · salt-diet · argon · r1), agy's per-turn wall clock
(`--print-timeout 1800s`) fired: the client printed `[agy] print timeout after 30m0s with turn in progress; returning partial output` and the
turn loop sent the next continue turn. 3 hits in attempt 2 (live at count time) and 1 in the attempt discarded on a 503. gemini counted 0 in the
FreeList plain spec-change legs and the Crc32 argon salt-diet ones, and left the rest of the set uncounted.

**A7.2 · THE CENSUS OF THE WHOLE SET.** `evidence/zf-print-timeout-census-2026-10-22/`: `census.txt` is one line per ZF cell root on the run
box (`grep -c -F "print timeout"` over the concatenation of the root's `ctl/agy-stderr-*.txt`, one total per root; every root holds exactly one
such file, `files=1` on all 238 lines), and `tally.py` reads it. Output, 2026-10-22:
```
  arm        roots   roots with >= 1 hit   hits
  plain        120                     3      5
  salt-diet    115                    31     71
```
By model: argon plain 3 of 60, argon salt-diet 19 of 58; flash plain 0 of 60, flash salt-diet 12 of 57. The per-condition rows are in
`tally.py`'s output. This is the campaign's own finding again: stage 1 measured `plain 0·0·0` against `salt-diet 2·4·3·3·5`, and the level-4
amendment ruled that a per-turn wall clock cannot be made arm-neutral for an arm that runs a verifier, only non-binding
(`AMENDMENT-gemini-brownfield-level4-2026-09-13.md`). ZF registered the 1800 s value and did not declare that it binds.

**A7.3 · WHAT IT MEANS FOR A RESULT.** A hit costs the subject a partial turn: the loop counts it against the 40-turn cap and the conversation
continues. A cap that binds one arm is a treatment applied to that arm. Here it falls on salt-diet, so its sign is EXPECTED to be against the
arm under test: it is expected to lower salt-diet's rates. That direction is an expectation; the counts above are the measurement (a partial
turn followed by a continue turn is also a second prompt, and the census does not exclude that one helped a leg). **Every ZF table carries this limit beside its rates, by model and arm, with the counts
above.** It is not grounds to re-fire any leg, and the value is not changed inside the set.

**A7.4 · LIMITS.** (1) The count is per cell ROOT, not per cell of record: a root that was re-fired under another name is counted under that
name, and the 503-discarded roots are excluded. (2) A spec-change root on the run box holds phase 2's client stderr; phase 1 lives in an
aside, so the spec-change rows are phase 2 only. (3) A hit says the clock fired; whether it changed a verdict is NOT MEASURED here — a leg
that stopped at its turn cap with hits in its stderr is the case to read first. (4) The salt-diet spec-change rows are incomplete: the set is
still running (Z235 live at the count).

**A7.5 · THE TURN-CAP CASE, READ.** A7.4(3) named a leg that stopped at its turn cap with hits as the case to read first.
`evidence/zf-print-timeout-census-2026-10-22/turnloop-of-hit-roots.tsv` (by `turnloop_of_hits.py census.txt`, read 2026-10-22) is the turn
loop record of every phase of every cell in census.txt's 34 roots with a hit. The population is census.txt's, not a fresh glob of the run
box, and a phase that a spec-change harvest set aside is read from `_aside/`. All 34 roots hold a record: 35 phase records, because the
one spec-change root with a hit, `cells-l8zf-freelist-argon-salt-r1-sc-a2`, has both phases. **No hit leg stopped at its turn cap, in any
phase read.** 32 phase records LANDED, using 3 to 8 of their 40 turns. The 3 that did not land are FreeList · argon · salt-diet ·
greenfield · bare, r1 to r3: `TURN-TIMEOUT` (14 turns, 12 with no output, 21,725 s) and `WEDGED` twice (6 turns, 5 with no output, about
9,128 s each), and all three end markers read `ARM-NOT-RECEIVED`. In those three the timeout is most of what happened: the subject
produced nothing on most turns. The tsv's hits equal census.txt's for 33 roots. For r1-sc-a2 the tsv reads 4 hits (phase 1, LANDED in
8 turns; phase 2 has 0) where census.txt reads 3, because the census was taken while that leg was still running. A7.2's table is left
as counted. Limits: this reads the loop's own record, not a score; whether the lost partial turn changed any LANDED leg's score is still
NOT MEASURED; and whether those three roots are cells of record is not read here.

## ⚖️ ADDENDUM 8 — RELEASE: THE CREDENTIAL WINDOW READ FROM BOTH EXPIRY FIELDS, AT EXPORT `0b783cf` (Z240). APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-10-23, on gemini's Z240 stop report and systems' fix (bus 2026-10-23). A change to the harness that LAUNCHES a cell,
registered before the first model call it governs. Nothing a cell measures changes; the scorer stays ADDENDUM 3's. ⛔ **It binds no leg until a
non-author signs it.** Until then the chain stays stopped at Z240, because `6993727` cannot read the client's new credential file (A8.1).*

**A8.1 · WHAT HAPPENED (Z240).** Leg Z240 (FreeList · greenfield · spec-change · salt-diet · r3 · `gemini-3.8-flash-high`, cell `zfffgxs301`,
export `6993727`) stopped at zero spend: the cell was BUILT and never launched. gemini's reading of the client logs: every client start through
`cli-20261022_180604` reads agy 1.4.5, and Z240's first start, `cli-20261023_140948`, reads 1.4.6. The credential file on the run box no longer
carries an `id_token` key; its window is `token.expiry`, an ISO-8601 time. `credential_seconds_left` in `agy_wave_v3.sh` read only the
`id_token` exp and printed `0` on ANY exception, so a token with time left read "0s remaining" four times and every attempt refused: `REFUSE -
could not obtain a 2400s credential window after 4 attempts`. A `0` for "I could not read it" and a `0` for "it has expired" were the same `0`.
The driver then recorded the leg as `MODEL UNREAD`, because its refusal pattern matched only the em-dash spelling `REFUSE — ` and this line
uses an ASCII hyphen. **Which event rewrote the file is not measured here:** the commit message says the auto-update, the code comment says a
re-login. The fix does not depend on which.
**Re-driven by the lead on the live file (run box, 2026-10-23T21:48:07Z, read only through the readers, which print seconds or key names and
never a value):** the `0b783cf` reader reads **1300 s**; the `6993727` reader, on the same file a moment later, reads **0**. The defect
reproduces live, and the fix reads it.

**A8.2 · THE CHANGE: `6993727` → `0b783cf`** (saltbench-systems, six commits by systems, `69937276` an ancestor; `merge-base --is-ancestor`
holds; the branch is the NAS backup remote's `systems/warm-credential-network-2026-10-19`, head `0b783cf35902`):
```
  db1bf46b  selftest_agy_warm_v3.sh, committed RED on the current wave script: the Z145 network-error warm-up (2026-10-19)
  ab0ac100  agy_wave_v3.sh: a warm-up failure whose client log (only logs written SINCE this warm-up began) says "due to network error"
            is named CREDENTIAL-NETWORK and retried ONCE after AGY_WARM_NET_RETRY_SECONDS (default 45); a second failure refuses with
            the class named. Any other failure refuses as before, with no retry.
  7d1d01a9  gemini_drive_v3.sh: wave_refusal() returns the wave's FIRST "REFUSE — " line, and the model-unread branch consults it first
            and says "WAVE REFUSED in <root>: <line>" (same stop). gemini_canary_wave_v1.sh: CONDITION-FAILED quotes the driver's stated
            reason. agy_wave_v3.sh: one retry rm reverted to the file's own form (the driver's allowlist derivation read `${w:?}` as a
            variable the wave requires; that arm was red at ab0ac100).
  9ef62d17  gemini_drive_v3.sh selftest only: the first-refusal arm also requires exactly ONE line (a mutant dropping -m1 survived it).
  da8ee8ba  selftest_agy_warm_v3.sh, committed RED on the current wave script: the Z240 file shape (no id_token; window in token.expiry)
  0b783cf3  agy_wave_v3.sh:
            (a) credential_seconds_left reads token.expiry (a trailing Z, and 9 fraction digits, normalised for Python before 3.11) AND
                the id_token exp, and takes the EARLIER, so a disagreement is conservative;
            (b) an expiry that neither field yields prints "UNREADABLE (keys: …)" with the file's key NAMES, never a value and never 0;
                ensure_credential_window then refuses at once, "REFUSE — CREDENTIAL-UNREADABLE: …", with NO warm-up; warm_window_rescues
                treats UNREADABLE as no rescue;
            gemini_drive_v3.sh: (c) wave_refusal matches "REFUSE — " AND "REFUSE - " (the four-attempt refusal is written with a hyphen).
  diff 69937276..0b783cf3: 5 files, all harness/systems-v3/ (agy_wave_v3.sh +72/−8 · gemini_drive_v3.sh +43/−0 ·
            gemini_canary_wave_v1.sh +3/−1 · selftest_agy_warm_v3.sh +132/−10 · selftest_all_v3.sh +2/−1, a comment only)
```
**Two things in the range that the Z240 report does not describe, named here so the release covers what it ships:** (1) the Z145 carry-up is
TWO behaviour changes, not one: the CREDENTIAL-NETWORK retry in `agy_wave_v3.sh` (ab0ac100) and the verbatim REFUSE in the driver and the
canary wave (7d1d01a9), plus a selftest-only commit (9ef62d17). (2) `gemini_canary_wave_v1.sh` changes (one CONDITION-FAILED line gains the
driver's reason). Neither changes a stop, cap, score or outcome.
**Unchanged, read in the diff:** the order FENCE RENDERED → BATTERY GREEN → CREDENTIAL WINDOW → fire; the 2400 s need; the warm-up's own
rescue rule (A5.2, A5.7). A cell launches only on a window the reader READ. The new refusals stop a wave; they never launch one.

**A8.3 · CONSUMERS** (the lead's search, `grep -rF` over the `0b783cf` tree, and `git grep -F` over saltbench at `3c582142`):
```
  credential_seconds_left · CREDENTIAL-UNREADABLE · CREDENTIAL-NETWORK   agy_wave_v3.sh and selftest_agy_warm_v3.sh only (+ a comment in
                                                                          selftest_all_v3.sh). Public repo: 0 files.
  wave_refusal                                                            gemini_drive_v3.sh only. Public repo: 0 files.
  WAVE REFUSED                                                            gemini_drive_v3.sh (writes it), gemini_canary_wave_v1.sh (quotes it). Public: 0.
  MODEL UNREAD · credential window                                        the same scripts; public hits are prose (this file, the census, two RESULTs, the paper)
  control                                                                 warm_window_rescues: 1 public hit (A5.7), found
```
No script in either tree parses the credential reader's output except its two callers in the same file. **The chain (`chain-l8u.sh`, a lane
file, not tracked in either repo, md5 a689dd84b231386a4501c9bcb4768648 as read at this release) derives the export as
`saltbench-systems-v3-export-<first 7 of EXPORT.sha>` and the driver's worktree on the lead box as `saltbench-systems-v3-gemini-<same 7>`.**
So the dest below is the name the chain will look for. Its `EXPORT.sha` still reads `69937276…`, and the `-gemini-0b783cf` worktree does not
exist yet. Both are the hand's acts at the resume, after the signature, never before it.

**A8.4 · RECEIPTS** (every line re-driven by the lead; systems' own figures are not used as receipts)
```
  lead box, each commit's tree from git archive, python 3.14.4 (bash run of the selftests):
                           selftest_agy_warm_v3.sh   --mutants              gemini_drive_v3.sh --selftest
  69937276 (the export)     12 passed · 0 failed      3 of 3 killed           24 of 24
  db1bf46b (RED, Z145)      16 passed · 5 failed      (base red)              24 of 24
  ab0ac100                  22 passed · 0 failed      7 of 7 killed           23 of 24 (the allowlist arm: `${w:?}`, as 7d1d01a9 says)
  7d1d01a9                  22 passed · 0 failed      7 of 7 killed           27 of 27
  9ef62d17                  22 passed · 0 failed      7 of 7 killed           27 of 27
  da8ee8ba (RED, Z240)      22 passed · 8 failed      (base red)              27 of 27
      the 8: newfull ×2 (a readable window read as 0 s) · newadv (the four-attempt refusal) · both (the later id_token exp taken) ·
             noexp ×4 (warmed instead of refusing; not named CREDENTIAL-UNREADABLE; keys not named; printed as 0 s)
  0b783cf3                  35 passed · 0 failed      12 of 12 killed         28 of 28
      the 5 new mutants: z240-id-token-only (7 arms red) · z240-later-wins (1) · z240-unread-is-zero (5) · z240-no-unread-refusal (2) · z240-no-keys (1)
  the lead's OWN mutant of gemini_drive_v3.sh at 0b783cf3: the pattern `REFUSE (—|-) ` cut back to `REFUSE — `
                                                                                    27 of 28: the ONE red arm is "the HYPHEN spelling is a refusal too"
  selftest_all_v3.sh --runs 1, a full git worktree at 0b783cf3, the lead box's toolchain contract loaded
                                                                                    75 of 77 passed · 0 failed · 2 skipped (placebo-form,
                                                                                    placebo-arm+problem-column: PLACEBO_V2_PATH unset, as A1.2); agy-warm and canary-wave ok
  THE EXPORT, cut by the lead from that throwaway worktree:
      studio_export.sh <run box> --ref 0b783cf3 --no-toolchain --dest <the dest below>
                       --amendment AMENDMENT-gemini-level8-2026-09-16.md (as at saltbench origin/main 3c582142e726) --amendment-commit 3c582142e726…
      dest saltbench-systems-v3-export-0b783cf, beside the earlier exports on the run box · 378 files (380 with EXPORTED-FROM.sha and REQUIRED-ANCESTORS.tsv) ·
      listing sha256/16 dd179d14e5f23979 · withheld-shaped names 0 in the listing and 0 on the host · rc 0, marker written last
      required-ancestor gate OK (5 of 5; serial=3, block digest 6b3de761118f9f42, amendment read at saltbench 3c582142e726)
      diff -rq against the 6993727 export on the run box: exactly 7 files ·
          harness/systems-v3/{agy_wave_v3.sh, gemini_drive_v3.sh, gemini_canary_wave_v1.sh, selftest_agy_warm_v3.sh, selftest_all_v3.sh}
          + EXPORTED-FROM.sha + REQUIRED-ANCESTORS.tsv (only its @amendment-commit line differs: 7cbe2153 → 3c582142; rows identical)
      on the host, sha256/16 == git show 0b783cf3, file by file:
          agy_wave_v3.sh 7754e92b7eca7857 · gemini_drive_v3.sh 458bd8564691e1a8 · gemini_canary_wave_v1.sh 77fa2b49b933a9dd ·
          selftest_agy_warm_v3.sh 02b139aec8001351 · selftest_all_v3.sh 1d8dc5a1a06e4de6
      on the run box FROM THAT EXPORT, python 3.9.6, bash 3.2.57:
          selftest_agy_warm_v3.sh 35 passed · 0 failed (the five expiry spellings PASS under 3.9.6) · --mutants 12 of 12 killed
          gemini_drive_v3.sh --selftest 28 of 28 (run with WAVE_HOST=selftest-host: the run box carries no run-box name file, and the
              driver refuses rc 4 without one before any arm; the driver runs on the lead box in the chain)
          gemini_canary_wave_v1.sh --selftest 110 of 110
          the new reader on the live credential file: 1300 s · the 6993727 reader on the same file: 0 (A8.1)
  --no-toolchain: the change touches no toolchain path, and ZF legs use no Verus.
```

**A8.5 · WHICH LEGS RUN ON WHICH EXPORT.** Z001–Z239 ran on the exports A5.4, A6.8 and A6.10 name, each row carrying its sha. Z240's attempt
spent no model call and is **not a replicate**: as Z018 (A5.5), its cell is re-queued, never carried, and its replicate is the re-fire. Every leg
fired after the signature below, Z240 first, runs on `0b783cf` and its row carries that sha. Under `6993727` no leg can launch on this file
shape at all, so there is no leg the two exports would launch differently: they differ only in (i) reading `token.expiry`, (ii) refusing an
unreadable file at once instead of after four warm-ups, (iii) one bounded retry of a warm-up that failed on the network, and (iv) the label
the driver and the canary wave print for a refusal.

**A8.6 · THE CLIENT VERSION (the helm's question, bus 14:19): RECORDED, AND THE SET HAS ALREADY CROSSED SEVEN CLIENT VERSIONS BEFORE THIS ONE.**
Measured read-only on the run box, over every ZF cell root (`~/cells*zf*/*/ctl/built-from.tsv`, 243 files):
```
  (1) RECORDED, per cell, at LAUNCH: ctl/built-from.tsv rows `client_version_claim` (the client's --version label) and `client_sha256`
      (the binary's content hash, the evidence). 242 of 243 roots carry both; the one without is Z240's own cell, built and never launched.
      NOT in the root's PROVENANCE-<date>.tsv (it is written at build and reads client_sha256 "NOT MEASURED"), not in _receipts/, and in
      no public ZF table (git grep -F client_version: 0 ZF files). gemini's census is right that no RECEIPT carries it.
  (2) THE VERSIONS THE SET RAN ON, one sha each:
      1.3.5 ebd71c4db14f79fc ×25 · 1.3.6 827ba22b4aa33557 ×19 · 1.4.0 a4502aaf310b2fd6 ×48 · 1.4.1 da7e0766b076e411 ×4 ·
      1.4.2 74935642426b5bb1 ×65 · 1.4.3 836c446f6118140e ×39 · 1.4.4 9abb478686dc08d4 ×30 · 1.4.5 b89677b741d8d9d3 ×12
      the client now installed: 1.4.6, sha256/16 cab004f3c5c6cb7d (binary mtime 2026-10-22 21:27 run-box local time)
  (3) PAIRS (§G1 interleaving), keyed by cell name with the model letter masked: 120 complete pairs, 2 STRADDLE a version
      (zf?pbnp201: argon 1.4.3 · flash 1.4.2;  zf?zgns101: argon 1.3.6 · flash 1.4.0). Z240's pair will be the third: its argon half
      (zfafgxs301) ran on 1.4.5, its flash half re-fires on 1.4.6.
  (4) The Claude CLI version: no ZF cell runs a Claude client (built-from: the agy per-cell HOME), so a ZF cell has none to record.
```
**THE RELEASE DECLARES THE 1.4.5 → 1.4.6 BOUNDARY AT Z240:** every leg before Z240 ran 1.4.5 or earlier, as its built-from row says, and every leg
from Z240 on runs the client its built-from row names. §G4.2 already registers the rule this needs ("If agy moves mid-set, every pair names its
client version"), and the set had moved seven times before the boundary the bus reported. **So every ZF table row carries `client_version_claim`
and `client_sha256/16` from its cell's built-from.tsv, and every pair whose halves differ is flagged in the table.** This is the receipt gap gemini
named, closed at the harvest, not in the harness.
**A SWITCH, READ AND NOT TOUCHED:** `agy --help` lists an `update` subcommand ("Update CLI") and no flag that disables automatic updates. The
client's settings.json carries three keys (colorScheme, model, trustedWorkspaces), none about updates. The binary carries the string
`AGY_CLI_DISABLE_AUTO_UPDATE`, shaped like an environment variable; it is undocumented in --help and its effect is UNMEASURED. The updater's
status file was last written at Z240's first start and reads "Already on the latest version." **Recommendation, not done here:** pin only if the
switch is first driven to show that it holds (an unchanged client sha across a client start with it set), and only on a ruling, because setting
it changes the run box for every agy lane. Until then the set is RECORD-AND-DECLARE, per (1)–(3) above. No setting was changed by this release.

**A8.7 · LIMITS.** (1) The reader takes the EARLIER of two expiries: if a future client writes a stale `id_token` beside a fresh
`token.expiry`, the wave warms (or refuses) on a window shorter than the real one. That is the conservative direction, and it costs a warm-up,
never a cell. (2) The new shape has been read on ONE live file, at one time; the full warm-up on it (a refresh that moves `token.expiry`) is
driven in the selftest's fake client only, and has not run live. The first live warm-up on 1.4.6 is reported to the lead with its window
lines before the next leg. (3) The CREDENTIAL-NETWORK retry classifies by one sentence in the client's own log ("due to network error"); a
client that words it differently is refused as before, with no retry, which is the old behaviour. (4) The 1.4.6 client itself is a new client
for the cells that follow; nothing here measures whether it behaves like 1.4.5 inside a cell. That is what A8.6's per-row version is for.
(5) The A8.6 census reads cell ROOT names, as A7.4 did: a root re-fired under another name is counted under that name (three names are
unpaired for that reason), and a version label is the client's own claim, which is why each row also carries the sha. (6) `agy --help`,
`agy update --help` and `agy --version` were run on the run box to read the version and the switch; the client's sha, read after
`--version` and again after the two `--help` calls, was cab004f3c5c6cb7d both times, and its mtime did not move.

## ✍️ NON-AUTHOR SIGNATURE — kent, 2026-10-23 15:03 PDT, of ADDENDUM 8 · RELEASE at blob `6a08d9b6edcd` (head `6b979cebd138`), CHAIN Z AT EXPORT `0b783cf`
kent re-resolved both pins at the forge at signing (PR #392 head `6b979cebd138`, the file's blob `6a08d9b6edcd`; all the required checks success). Main's file is a byte prefix of the PR's: the first 55,567 B `cmp`-equal, the 16,415 B appended (71,982 B total), nothing above edited. He re-drove from the private tree on this box: `merge-base --is-ancestor 69937276 0b783cf3` holds; 6 commits (db1bf46b · ab0ac100 · 7d1d01a9 · 9ef62d17 · da8ee8ba · 0b783cf3); `git diff --stat` 5 files, all `harness/systems-v3/`, 252+/20−, and each file's +/− matches A8.2 (agy_wave_v3.sh 72/8 · gemini_drive_v3.sh 43/0 · gemini_canary_wave_v1.sh 3/1 · selftest_agy_warm_v3.sh 132/10 · selftest_all_v3.sh 2/1); the five files' sha256/16 from `git show 0b783cf3` equal A8.4's host figures (7754e92b7eca7857 · 458bd8564691e1a8 · 77fa2b49b933a9dd · 02b139aec8001351 · 1d8dc5a1a06e4de6). From a `git archive` of 0b783cf3, python 3.14.4: `selftest_agy_warm_v3.sh` **35 passed · 0 failed**; `--mutants` **12 of 12 killed** (the five z240-* mutants among them); `gemini_drive_v3.sh --selftest` (WAVE_HOST=selftest-host) **28 of 28**. **WHAT BINDS: the release of chain Z from export `6993727` to `0b783cf3`**, appended; the per-row client version and sha and the pair flag in every ZF table (A8.6); the 1.4.5 → 1.4.6 boundary declared at Z240.
**Riders, carried as signed (none changes the signature):** (1) A8.1 states the cause of the rewritten credential file as NOT MEASURED (commit message says auto-update, code comment says re-login), and the fix does not depend on it; this signature does not either. (2) The reader takes the EARLIER of the two expiries (A8.7 (1)): the conservative direction. (3) The auto-update switch is read and untouched; no pin is signed (A8.6).
**Limits of the signature:** python 3.14.4 here; the 3.9.6 run-box receipts, the export cut (378 files, ancestors 5/5, listing sha256/16 dd179d14e5f23979, diff -rq against the 6993727 export), selftest_all_v3 75/77, the canary-wave 110/110, the red-first runs at db1bf46b / ab0ac100 / da8ee8ba (16/5, 22/0, 22/8), the lead's own hyphen mutant (27 of 28), the live credential file's 1300 s versus 0, the grep consumer search (A8.3), the client-version census (243 roots, eight versions, 2 straddling pairs) and the chain-l8u.sh md5 are the lead's and were NOT re-driven. Nothing was fired live; I did not touch the credential file or the run box.
