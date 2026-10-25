# AMENDMENT O90-STAGE1 — 2026-10-23: the understanding arm, its reuse probe and its instruments on S2-Lean, registered BEFORE its first call

**Registry and name.** This is an amendment to the S2-Lean scout (`SCOUT-S2LEAN-STAGE0.md`), filed as its own dated file and
cited by **name and date**, never by a bare number: four amendment registries already share numbers in this repository, and a
fresh number is safe only against the registries its author holds. The scout's registry carries a one-line pointer to this file.

**Authority.** The O90 test design, draft 4 (the PM's, refuted FAIL · FAIL · PASS WITH CORRECTIONS by the systems lane over
drafts 1–3; its findings are cited below as **[Fn] [Gn] [Hn]**, as the design cites them). The Captain's GO for the design
at the 10-22 sitting, with *"bench builds per §7"*; his word for the Claude stages at the 10-23 sitting (one pool only, the
one his ruling names); desk AEY (owner bench, reader systems, deadline 2026-10-24). This file is §7's bench list, built.
**Nothing here has run a model call.** The receipts below are a stub-driven run-shaped dry and two read-only measurements.

## 1 · The population [F4]

Thirty problems: **U15** (the first fifteen UNFLAGGED ids of the seeded draw, registered by amendment 3 and run by amendment 8)
plus **the next fifteen unflagged ids of the same order.** Derived, never typed, by
`harness/s2lean/o90-2026-10-23/o90_ids.py`, which refuses unless its derivation of U15 equals the registered list and the
next id is 82 at depth 29 (both as the design states):

```
U15   73 0 146 16 4 38 142 96 112 141 31 54 127 18 74          depths 3 … 27
next  82 52 92 60 2 148 56 149 120 128 35 30 136 59 11        depths 29 … 66
```

So the draw is read to **k = 66**: the driver runs with `K=66` and `ONLY_IDS` = these thirty (its registered-subset override,
amendment 3: an id outside the first k is a refusal). A mutant that flags one U15 id makes the tool refuse (driven).
**C-dead among the thirty:** 112, 54, 18 (`view_status.json` c_dead; 18 also in `c_dead_unsat.json`). None of the next fifteen.

## 2 · The arms [F9]

| arm | stages | CLAUDE.md | prompt |
|---|---|---|---|
| `a0` = **P** | A, B | `arms/a0.md` | the registered prompts, unchanged |
| `a5` = **P+U** | A, B | `arms/a5.md`, a byte copy of `a0.md` | stage A unchanged; stage B = `prompt_B.md` + `prompt_B_pu.md` |

The rendering pins `rendered-s2-a5(__EP__)` and `rendered-a5(__EP__)` equal `a0`'s, and `o90_pins.py` refuses to write them
otherwise: **the arms' CLAUDE.md files are byte-identical, so the only difference between P and P+U is one paragraph of the
stage-B prompt.** Stage A is the same for both arms, so each arm proves about a spec written under identical instructions
(design §2). Same 100-call cap. Arms alternate per problem (the driver's task-major order, unchanged).

`prompt_B_pu.md`, frozen here (it is appended to `prompt_B.md` for `a5` only):

> Also deliver an explanation for the next person who builds on this proof. (a) Write the file __EP__/repo/EXPLAIN.md.
> Begin it by restating the theorem you proved, `spec_isomorphism`, from its Lean text: name the declaration, quote
> its statement, and say in words what it asserts, every quantifier and hypothesis included. Then say in a few
> sentences why it holds. Write each sentence from the Lean statement it describes, never from a name, a comment or a
> goal. (b) Split the proof into named lemmas inside the `iso_helper_lemmas` section, each with a one-line docstring
> (`/-- ... -/`) saying what the lemma states. The proof must still compile without `sorry`.

## 3 · `EXPLAIN.md` is captured, never scored [F9]

`episode_s2.sh` copies `repo/EXPLAIN.md`, when present, to the episode's state dir **beside** `bodies.json`, for every arm,
and records `explain_sha256` and `explain_bytes` in the manifest. It never enters `bodies.json`, so the referee (`check.py`
over the extracted bodies) sees exactly what it saw before this amendment. The docstrings of (b) live inside
`iso_helper_lemmas`, a scored body, as every helper lemma always has; the size axis strips them with `screen.py` [F10].

## 4 · U3, the reuse probe: stage C with the artifact beside the view, and C0 [F3] [G1]

| arm | stage | what the agent gets |
|---|---|---|
| `a0` = **C0** | C | the ordinary stage-C view, nothing else |
| `a6` = **C-with-P** | C | the view, plus `repo/prior/` = `a0`'s scored stage-B artifact |
| `a7` = **C-with-P+U** | C | the view, plus `repo/prior/` = `a5`'s scored stage-B artifact |

**The artifact** is written by a stage-B episode only when it is SCORED and PASSED (amendment D5's rule for `A.bodies.json`,
applied one stage on): `B.artifact/stageB.lean` = the episode's checked `canonical.lean` (frozen statements + the agent's
bodies, docstrings included), `B.artifact/EXPLAIN.md` if captured, and `B.artifact.json` with the episode id and both
sha256s. A later scored non-pass removes it; a non-scored episode leaves an earlier pass standing. At stage C the episode
copies it into `prior/`, **re-hashes what landed against the record and refuses on any difference** (driven: a tampered
artifact ends the episode `HARNESS_ERROR`, reason "prior provenance"), and records `prior` in the manifest.
`a6`/`a7` refuse stages A and B, `a5` refuses stage C (driven). The driver lands `NOT_RUN(no_stage_B_artifact)` for a U3 arm
whose source arm has no artifact, never a skip (driven).
`a6` and `a7` render `a0`'s CLAUDE.md; their prompt is `prompt_C.md` + `prompt_C_prior.md`, frozen here:

> A previous agent worked on this problem before you. Its work is in __EP__/repo/prior/: `stageB.lean`, a Lean file
> holding a specification it wrote (`generated_spec`) and a proof that it is equivalent to `problem_spec`, and
> `EXPLAIN.md` if it wrote one. You may read it and reuse anything in it. It is not part of your answer and is not
> compiled with it.

⚠️ **C0 differs from the reuse arms by that paragraph as well as by the files.** It cannot be otherwise (a paragraph pointing
at files that are not there would be a different control), and it is declared: C0 is "the ordinary stage C", as the design
defines it. **U3's population** is fixed by rule after stage B: the problems where BOTH `a0` and `a5` passed stage B and
which are not C-dead. The checker is the S2-Lean stage-C checker, unchanged.

## 5 · U1 and U2, frozen before the first artifact exists [F1] [F2] [G2] [G3]

- **U1** is `harness/s2lean/u1_gen.py` (merged 2026-10-22, the stage-0 generator; keyed on `problem_spec` by the kernel).
  ⚠️ **It was merged into `s2lean/` UNPINNED, and `episode_s2.sh` refuses any file in `s2lean/` that `HASHES.txt` does not pin:
  every S2-Lean episode from a harness synced off main since 10-22 would have refused.** Found by a census of `s2lean/*`
  against the pins while building this; pinned here.
- **U2** is `harness/s2lean/u2_gen.py` with its record dir `harness/s2lean/u2-2026-10-23/` (README there carries the full
  definitions). The key: Lean re-elaborates a copy of the artifact's checked `canonical.lean` and records what every constant
  defined in it uses; the used set of `spec_isomorphism` is closed **transitively through every constant the artifact defines**
  (its helper lemmas, its spec, and Lean's own auxiliary `_proof_N` terms), then restricted to ONE population, constants of Lean
  core and the mathlib family, after a filter frozen here: recursors and compiler auxiliaries (`.rec` `.casesOn` `.below`
  `.brecOn` `.noConfusion` `recAux` `casesAuxOn`), equation and unfolding lemmas, `match_`/`proof_` as whole name parts,
  `_private` names, instances, notation/syntax defs, and lemmas that tactics insert and no author chose (`Lean.Omega.*` and
  kin, the most debatable rule, named so it can be argued). Distractors: library constants of the same kind NOT in the used
  set, each matched to one used constant by namespace and module family, drawn by a seeded sha256 order, falling back to the
  whole pool. The question asks "used by this proof", never "needed". It refuses an artifact that is not a scored stage-B
  pass, whose sha256 differs from its `check.json`, or whose bodies `screen.py` flags.
  **Receipts:** `--selftest` 42 arms, 8 mutants all red (skip local constants · filter before closing · no filter · no
  used-set exclusion · no alias exclusion · both off · unseeded draw · no module match); re-run by the lead, same line.
  `lean-selftest` on the run box 9 arms, 3 mutants red, over four fixtures (direct · through a public helper · through a
  `private` helper · by induction), its expected set computed by Lean from the direct fixture. Live on six of amendment 8's
  passed stage-B artifacts (problems 16, 74, 141 × `a0`/`a2`): 53–72 used constants each; **without the closure 7–17 used
  theorems per artifact vanish** (one goes 19 → 2), so the closure is load-bearing on real proofs, not only on split ones;
  0 of 96 distractors in the used set; a second Lean run byte-identical.
  ⚠️ **Limits:** the re-elaboration runs outside `check.py`'s sandbox against the current environment, guarded by the sha256 pin
  and the screen; `def` items are mostly notation operators, so the `theorem` items are likely the informative ones; six
  artifacts test the instrument and are not a reading of any arm. ⚠️ (systems' F6, declared, not remedied here) U2's Lean
  re-elaboration is not run under `sandbox_check.sb`; its inputs are scored artifacts whose bodies passed the screen.

## 6 · The two inputs the design asked bench to measure

**[F11c] amendment 8's per-problem a2/a0 token ratio** (`harness/s2lean/o90-a8-2026-10-23/spread.py`, read-only over the run's
60 manifests; the field `metered_sum_governing` reproduces the run's registered 26,104,403 exactly, A 5,982,892 + B
20,121,511). Population derived: the 9 problems both arms passed at stage B (16 31 38 54 73 74 141 142 146). At stage B:
median ratio 1.489, IQR 1.193–1.947, min 0.798, max 2.355; **spread = exp(MAD of ln r) = 1.308**. Registered here:
- **Cost axis:** the margin 1.5 sits above the ×1.308 band, as the design requires, by a factor of about 1.15. It stays 1.5.
- **[H2]:** the spread exceeds 20 %, so the 0.8 in the U3 tokens clause is replaced, by the design's own formula, with
  **1 − 0.308 = 0.692**. (The log-symmetric reading of the same band would give 0.765; the design's text governs, and the PM may
  rule the other before the freeze.)
- ⚠️ **Limit:** amendment 8 has no same-arm repeats, so 1.308 is arm × problem interaction plus noise, not noise alone. As a
  noise floor it is likely an over-estimate, by an amount not measured.

**[H3] the per-call build trace exists, so the calls-to-proof clause RUNS** (`harness/s2lean/o90-a8-2026-10-23/calls_to_green.py`):
every episode archives its `session.jsonl` with every tool call and its result, and the `rt` wrapper's own `rt.log` records each
command's rc. "Calls to the first green replay" = tool calls up to the first compile of `task.lean` whose `rt` rc is 0, whose
output carries no task-file error (either Lean form) and no `declaration uses 'sorry'`; a compile whose output is filtered or
redirected is never green. On amendment 8: all 20 passed stage-B episodes have a first green; transcript API calls equal the
manifest's `calls` in 30 of 30. ⚠️ **Limit:** it sees only the compiles the agent chose to run.
⚠️ **And the P+U deliverable can land BEFORE the first green** (systems' F2): (b) asks for the lemma split, and calls spent
writing docstrings or `EXPLAIN.md` before the first green would count as proving. So the tool prints, per episode and for
EVERY arm, the calls before its first green that write a NEW docstring or name `EXPLAIN.md`, and the share per arm. "New"
(systems' G3): every task file already carries the problem's own `/--` docstring (161 of 161 views), so a whole-file rewrite
counts only above the file's own count K (canonical.lean's `/--` count minus the bodies'), an Edit counts when it adds a `/--`.
**The baseline, amendment 8 (no P+U paragraph in either arm): `a0` 3 of 15 episodes, `a2` 9 of 15** — read at the object, the
`a0` hits are the agent's own docstrings on its own helper lemmas, not the problem's. So the plain arm already writes them at
that rate. **The PM rules, at the read, whether the calls-to-proof clause runs at P+U's share against that baseline, or is
struck** (design §4 [H3]).

## 7 · The truth axis's flag log [F8c], with the PM's leg (c) reading

`harness/s2lean/o90-2026-10-23/o90_flaglog.py` is the schema and validator: one row per (sentence, read) with the READER, its
MECHANISM (Gemini or Claude), its VERDICT, and for a FALSE the CONFIRMER and the OUTCOME. It refuses a read by the author, a
confirmer who is the reader, a FALSE without a confirmation, a sentence read as two different texts, and a duplicate read. It
prints (1) the axis — a sentence is FALSE iff a read flagged it AND the third read confirmed it — per problem and arm, and
(2) the share of FALSE flags NOT confirmed, per mechanism and per arm, which is stage 1's analogue of leg (c)'s false-alarm
figure at no extra spend. It scores no reader against a key: stage 1 has none.

## 8 · Constants, client, pool, host, state root

- **The fourth regime's constants, unchanged from amendment 8:** `R_AMEND=100` · `W_AMEND=10800` · `TC_AMEND=30000000` ·
  `M_AMEND=claude-opus-5` · effort `high`.
- **Client: RE-PINNED, 2.1.251 → 2.1.278**, the run box's client today (`HASHES.txt` `claude-version`, and `hashes.sh`'s literal
  with it). `episode_s2.sh` refuses any other version at launch, and every manifest records `claude_version`, so the client is
  both pinned and recorded. Amendment 8's client is context only: every O90 comparison is within this run.
- ⛔ **A served-model halt, added because the client moved:** an unrecognised model id can be SUBSTITUTED by the client rather
  than refused. The calibration pair's manifests must read `models` = {`claude-opus-5`} (plus the client's own small auxiliary
  model, as amendment 8's did); anything else halts the run before cell 2. **Enforced, not stated** (systems' F3, G1, G2):
  `harness/s2lean/served_model_check.py` HALTS unless the requested model was served (count > 0) on an episode that made calls;
  a `claude-haiku*` entry is admitted only BESIDE it, so a haiku-only, empty or missing record halts. The driver calls it after
  EVERY landing — the first run, each HOLD re-run and each RETRY re-run, because a quota or auth fallback lands on a re-run —
  and on a halt writes `HALT` with the reason and exits 4 before another episode starts — **on TERMINAL landings only**
  (systems' K1): a QUOTA or AUTH wall at launch leaves no transcript and so no served-model record, and checking it there
  halted the run instead of starting the 12 × 30 min hold; the re-run that lands is the one checked. Its selftest has 10 cases;
  all 60 of amendment 8's manifests pass it (no false halt). The dry runs the driver's OWN function body on fixture landings
  (W2, systems' K2), so a stubbed body cannot pass behind a green wiring check.
- **Pool and config dir:** one pool, the one his 10-23 word names, through a NEW hermetic config dir on the run box holding only
  the pinned `settings.s2.json` and **its own fresh login** — never a copy of a live credential, because these credentials carry
  a rotating refresh token and two live copies can blank each other at the first refresh. The calibration pair is that dir's
  first-refresh test, read before cell 2. Passed as `CFG` to the driver. **That dir is in the sandbox's `denyRead`**
  (systems' re-read F1: a rule on `~/.claude` does not cover a SIBLING `~/.claude-…` dir, measured), and smoke probe S3 now
  lists the LIVE `CFG` and must see the OS deny it. Until this amendment S3 listed `~/.claude-bench`, a dir the run box no longer
  has, so its `ls` read "No such file" — not a denial — and S3 could not have passed for the right reason.
- **Host:** the run box (the harness, the shared Lean project, the views and amendment 8's state are there; S2-Lean is native
  Lean, no container).
- **State root: NEW, and INSIDE the sandbox's read-denied `~/bench`** — `BENCH=~/bench/o90`. A new regime gets a new state root
  (amendment 8, addendum 2). ⚠️ The sandbox denies reads of `~/bench`, a path prefix; whether a sibling such as `~/bench-a8`
  (amendment 8's root) fell inside that rule is **UNMEASURED** here, so this run's root is placed inside it rather than beside it.

## 9 · Halts, as the PM registered them, with their enforcer

The day line (no START at or above the day's line; a running cell is never killed for it) · the calibration pair > 2 points
halts and re-prices · 22 points on cells 1–4 halts and re-prices · amendment 8's stop rules (90,000,000 metered in either arm,
12 h wall) · the one pool's config dir only · the weekly reset (a cell unfinished by then is reported at its own n) · the
served-model halt above. Enforcer: the driver's cooperative `HALT` file (amendment 8, addendum 1), read between episodes.

## 10 · Order of operations

1. Merge; sync the committed harness to the run box (`sync_studio.sh`, which refuses a dirty tree); the stage's config dir
   logged in; its `projects/` emptied. The driver runs with `BENCH=~/bench/o90`, **`H=~/bench/harness` stated explicitly**
   (its default would be `$BENCH/harness`), `CFG=` the stage's config dir. **The smoke gate re-runs**: `episode_s2.sh` changed,
   so the driver refuses until `smoke_s2.sh` lands S1–S5 PASS carrying the new sha (five short probe episodes on the stage's
   config dir, never scored; their pool cost is read and reported with cell 1's). The checker files are unchanged, so the
   controls record is carried in and `controls_gate.py` re-reads it against the live checker before the first episode.
2. **Calibration (cell 1): problem 73, the first id in draw order** (a rule, not a choice): stage A for `a0` and `a5` with the
   ground truth OFF the host, then `ship BC`, then stage B for both. Read the pool delta, the served models and the config dir's
   refresh; halt or proceed.
3. Cell 2: the other 29, stage A then B, same discipline. 4. Cell 3: U3 — stage C, arms `a0 a6 a7`, over the U3 population
   (§4). 5. U1/U2 items generated from the artifacts by the frozen generators; reads by the readers; the flag log.
**Stage 2 (five research theorems) is NOT built by this amendment**: it has no harness here and needs its own registration.

## 11 · Receipts (run-shaped dry, the run box, a scratch bench; stub client; the kernel check REAL)

`harness/s2lean/o90-2026-10-23/o90_selftest.sh` against the pinned harness copy; stage B is fed amendment 8's recorded passing
body for problem 31, so B1/B2's passes are the kernel's. Outputs verbatim in `harness/s2lean/o90-2026-10-23/receipts/`.

```
  run 1 (first drive)       9 PASS · 1 FAIL   R3: the refusal fired ("prior provenance") but the manifest was LOST — a die()
                                              before step 5 met an unbound ARMFILE in the manifest writer (a pre-existing
                                              EDH-1 gap this amendment's new refusal exposed). Fixed: ARMFILE bound at init.
  run 2 (the fix)          10 PASS · 0 FAIL   R1 R2 A1 B1 B2 C1 C2 C3 R3 D1
  mutant M1 (no paragraph)  8 PASS · 2 FAIL   B2 prompt · C1 prompt                  — red on exactly its two arms
  mutant M2 (no capture)    8 PASS · 2 FAIL   B2 explain-capture · C2 explain        — red on exactly its two arms
  ── after systems' re-read (F1–F5), run 3, the arms extended (B2 feeds a DOCSTRINGED helper through the real checker,
     C2 asserts a7's prompt, B3 a scored failed B supersedes the artifact, H1 the driver's served-model halt) ──
  run 3                    12 PASS · 0 FAIL   R1 R2 A1 B1 B2 C1 C2 C3 R3 B3 H1 D1
  mutant M1 (no paragraph)  9 PASS · 3 FAIL   B2 · C1 · C2 prompt
  mutant M2 (no capture)   10 PASS · 2 FAIL   B2 explain-capture · C2 explain
  mutant M3 (no supersede) 11 PASS · 1 FAIL   B3
  mutant M4 (halt off)     11 PASS · 1 FAIL   H1                                     — every mutant red on exactly its arms
  ── after systems' delta re-read (G1–G3), run 4: H1 now drives served_model_check.py (selftest 9 cases + a clean and four
     bad records), W1 reads the driver's three call sites ──
  run 4                    13 PASS · 0 FAIL   R1 R2 A1 B1 B2 C1 C2 C3 R3 B3 H1 W1 D1
  M1 10/3 (B2 C1 C2) · M2 11/2 (B2 C2) · M3 12/1 (B3) · M4 12/1 (H1: substituted, haiku-only, empty, missing all pass)
  · M5 12/1 (W1: the RETRY site unwired)                                                — every mutant red on exactly its arms
```
```
  ── after systems' second delta re-read (K1, K2, L1, L3), run 6: W1's needles carry the is_terminal gate; W2 runs the
     driver's OWN served_check body (substituted → rc 4 + HALT · clean → 0 · QUOTA with no transcript → 0, no HALT) ──
  run 6                    14 PASS · 0 FAIL   R1 R2 A1 B1 B2 C1 C2 C3 R3 B3 H1 W1 W2 D1
  M1 11/3 (B2 C1 C2) · M2 12/2 (B2 C2) · M3 13/1 (B3) · M4 12/2 (H1 W2: both drive the silenced tool) · M5 13/1 (W1)
  · M6 13/1 (W2: the function stubbed to `return 0`, W1 and H1 still green — the hole K2 named, now closed)
```
⚠️ W1 is STRUCTURAL: the served-model check is off under DRY_RUN, so its wiring is read from the driver's text at three named
sites, and the check itself is driven on manifests (H1). A live substitution would first be seen at cell 1.
Not driven, declared: a NON-scored stage B keeping an earlier artifact (no stub path produces a non-scored landing).
`o90_ids.py`: the thirty, and a flag-list mutant refuses. `o90_flaglog.py --selftest`: PASS, 7 refusals fired; two mutants
(an axis that ignores the confirmation; an author read accepted) each fail it. `spread.py` and `calls_to_green.py` were
re-run by the lead from an independent copy of amendment 8's state: both outputs byte-identical to the committed ones.

## 12 · Limits

n = 30 detects only large effects (design §6). One model, one bed. U3 runs on ~16 problems. C0 also lacks the prior-work
paragraph (§4). The spread is not a pure noise floor (§6). The per-call trace sees agent-chosen compiles only (§6). The client
moved between amendment 8 and this run, so no O90 figure is compared with amendment 8's.

## ⚖️ ADDENDUM 1 — 2026-10-23: THE STAGE'S CLIENT RUNS WITH THE ACCOUNT SYNC OFF. APPENDED; all text above untouched. Written before cell 1's first scored call.

**What happened.** The run box's smoke gate (§10 step 1) ran on the stage's config dir after his login. S1 passed (one probe episode,
44,310 metered, never scored). During S1, client 2.1.278 copied the signed-in account's claude.ai skills into the config dir
(`skills/synced/<org>/`: 14 skills, among them docs, docx, pdf, pptx, xlsx, deep-research, computer-use and chrome-browser) and an
account plugin-marketplace list into `plugins/synced/`. S2–S5 were then refused at launch by `episode_s2.sh`'s hermeticity
assertion (`config dir carries agent-influencing entry skills`), the smoke failed, and the driver could not start. **No scored episode
ran.** S1's own session names none of the skills checked, so they landed after its skill list was built. Amendment 8's client
(2.1.251) never wrote this entry, and §2's arms do not contain these skills, so a subject that started with them would have run a
treatment nobody registered.
**The remedy is the client's own opt-out, and it is the one the Claude lane already registered** (OD ADDENDUM 6, 2026-10-17, on
2.1.280): `"syncClaudeAiSkills": false` and `"syncClaudeAiPlugins": false` in `settings.s2.json`. In the 2.1.278 binary the sync is
gated on those keys, and any settings source holding either one `false` vetoes that sync. The lead had registered the fix for the
Claude lane and did not carry it to this lane's settings file in the same act. That is a defect of the lead's, recorded here.
- **The pin moves:** `settings.s2.json` → `f29ba9381e6e246c…` in `HASHES.txt`, so `episode_s2.sh` (which refuses a config dir whose
  `settings.json` is not byte-identical to the pin) cannot launch an episode without both keys. No script changes, and the fence's
  `denyRead`/`denyWrite` lists are unchanged.
- **The config dir is restored before the next probe:** `skills/` and `plugins/synced/` are removed from it, the pinned
  `settings.s2.json` is copied in as `settings.json` (his login had re-serialised that file: the same keys in a different order), and
  `projects/` is emptied.
- **The drive is red-first, and the red has already happened:** the S1 above, under the old settings, wrote `skills/`. The green is
  the full smoke S1–S5 on the restored dir under the new settings. Because S2–S5 refuse whenever `skills/` exists, a 5/5 PASS shows the
  sync stayed off for all five probe episodes, and `skills/` is listed after the smoke as the receipt.
- **Declared, not refused:** the client also creates an empty `.cc-writes/` in the config dir. `episode_s2.sh` records it in
  `configdir_unexpected.txt` and does not refuse on it. It is recorded per episode and is not an agent-influencing entry.
- **The controls record (§10 step 1):** amendment 8's record certifies an earlier checker, and `controls_gate.py` refuses it against
  today's `check.py`, `s2audit.lean` and `screen.py`. The record carried into `~/bench/o90/state/s2-controls.json` is amendment 14's
  (`s2-controls-2026-09-02-amend14.json`), which certifies the live checker: the gate passes for stages A, B and C. "Carried in" in §10
  means the record that certifies the live checker.
- **The state root's views** were built A-only, by hand, from `~/bench/s2views` (A.lean and frozenA.json per problem) and verified by
  content: A-views set-hash `bc4d6eafc0430ed2` (the banked figure, recipe `<relative path> <sha256>` sorted and hashed), 161 problem
  dirs, 0 ground-truth files under `~/bench/o90`.
- **The population's first id** is 73 by `o90_ids.py` (§1). `draw.py 1` prints 109 because that id is flagged. Cell 1 runs as
  `K=66 ONLY_IDS=73`.
- **The meter: a call the client refused is not an unblocked escape.** The green smoke's S2 (ep-10767d43) landed
  `VOID(ESCAPE)`, but every layer had denied the network. The agent's first `curl` carried 2.1.278's new Bash parameter
  `allowed_domains`, and the client rejected it before the hook ran, with a `<tool_use_error>` reading "allowed_domains cannot widen
  network access in this session". The agent's retry was blocked by the hook, and the Python and Lean probes were denied by the OS
  sandbox (`deny network-outbound example.com:443`). `meter.py` counted the first call as UNBLOCKED, because only the hook's
  `BLOCKED` text marked a hit as blocked, and that voided the episode. Under that rule any scored episode whose agent tried
  `allowed_domains` on a fenced command would have been voided for an escape that never ran.
  **Fix:** a Bash/Monitor escape hit whose tool result STARTS with `<tool_use_error>` (the client rejected the input, so the tool never
  executed) is counted in a new field, `escape_attempts_client_refused`, and does not void. The mark only counts at the start of the
  result. Path-tool hits (Read/Glob/Grep/Edit/Write) are unchanged and still void, the conservative side. `meter.py` → `f21a33ff0b5806c8…`.
  **Receipts:** the self-test is 35 PASS · 0 FAIL, with two new arms (a client-refused call is an attempt and not a void; the mark
  anywhere but the start does not excuse an escape). Mutant Ma (the mark matched anywhere) reddens the second arm only, and mutant Mb
  (the branch removed) reddens the first only. Re-metered on the run box: ep-10767d43 reads `ESCAPE` under the old meter and `[]`
  under the new one (1 hook-blocked, 1 client-refused, 0 unblocked). The other four smoke episodes and **all 60 of amendment 8's
  sessions** give identical void reasons, metered sums and unblocked counts under both meters. `meter.py` is shared with `episode.sh`
  (S1) and `episode_s2rust.sh`, which pin it from the same `HASHES.txt` line, so their next run carries this fix.
- **The green, on the harness at this addendum's head (both fixes):** smoke S1–S5 **5/5 PASS** on the restored config dir
  (episodes ep-6791fc1e · ep-233834f0 · ep-673dbedd · ep-d23e3a28 · ep-0435707e). S2's curl was again client-refused, then
  hook-blocked, and it now passes. The config dir's listing after the five probes holds no `skills/` (receipt: the listing appended
  to the run box's smoke log). The run-shaped dry `o90_selftest.sh` reads 14 PASS · 0 FAIL against the same harness. The three smoke
  runs' pool cost, about 15 probe episodes and never scored, is read and reported with cell 1's, as §10 step 1 says.
- **systems' re-read (PASS, one correction owed before cell 1), taken in full.** **C1:** an exit-0 command's result is its own raw
  stdout, so a subject that printed `<tool_use_error>` before a `curl` was metered as client-refused and not voided (`lstrip` widened
  it further). **L1, pre-existing:** `BLOCKED_MARK` was matched anywhere in the result, so `curl …; echo BLOCKED by the episode
  harness` read as an attempt. **Fix, both:** a hit is excused only when its tool result carries `is_error: true`. A client refusal
  must start with the mark at position 0 (no `lstrip`). A hook block must start with `PreToolUse:` and carry the mark. systems'
  census: 99 of 99 stored hook blocks and 67 of 67 client refusals have that shape, and no executed result contains either mark.
  `meter.py` → `ad7c257addb5034f…`. Self-test 41/0 with six forge arms: the client mark opening exit-0 stdout, after a newline, inside a
  non-zero exit, and after a newline in an errored result; the BLOCKED text in exit-0 stdout and inside a non-zero exit. Every forge
  voids. Mutants, each red on its own arm: `is_error` ignored · `lstrip` restored · the `PreToolUse:` prefix dropped · the
  client-refused branch removed. Re-metered against main's `meter.py`: 435 stored sessions on the run box, identical in void
  reasons, metered sum and blocked/unblocked counts except the two O90 smokes ep-10767d43 and ep-233834f0 (`ESCAPE` → `[]`, the
  call this addendum exists to excuse). systems' wider population reads 2 of 668, the same two.
  **L2:** `plugins/` stays admitted for the marketplace catalog the client fetches at login. `episode_s2.sh` now refuses a config
  dir holding `plugins/installed_plugins.json`, because an installed plugin loads. Driven on a fixture (catalog only: passes; the
  file present: refuses; the guard removed: passes). `episode_s2.sh` → `6fe1e77fbfe143f5…`, so the smoke re-runs on the new sha. S1's
  `episode.sh` carries the same allow-list and is out of this stage's scope, declared. `settings.json` cannot carry
  `enabledPlugins`: it is pinned byte-identical.
- **The green at the corrected head:** smoke S1–S5 **5/5 PASS** on `episode_s2.sh` `6fe1e77f…` (ep-95d65098 · ep-721fcfe3 ·
  ep-f6820b63 · ep-18f7d90f · ep-676811e0), with S2's curl again client-refused then hook-blocked, and no `skills/` in the config dir
  after. Dry `o90_selftest.sh` 14/0 on the same harness.

## ⚖️ ADDENDUM 2 — 2026-10-24: THE STAGE-1 READ FORM FOR U1 AND U2 (ROW R). APPENDED; all text above untouched. Written before any stage-1 read.

*bench (lead). The items were frozen first (bus 10-24 08:3x, the run box `~/bench-dry/o90-stage1-reads-cells12-2026-10-24/`,
`SHA256SUMS` sha256/16 `1629c1c3912b0e69`); gemini (the reader) then reported the READ FORM unfrozen, in five parts (bus 10-24
08:37). This addendum freezes those five. It changes no item, no generator and no key.*

**A2.1 · The inputs, already frozen.** U1: `u1/drawn.tsv` (`u1_gen.py draw`, seed `o90-u1-2026-10-22`, the generator's pinned
default): 107 items over 17 problems; the U15's rows are byte-identical to leg (a)'s merged `u1-2026-10-22/`. U2: `u2/items.tsv`
(`u2_gen.py run`, seed `o90-u2-2026-10-23`): 185 items over the 47 scored stage-B passes of cells 1–2, 1,469 option rows, 0 of
740 not-used options in their own artifact's used set.

**A2.2 · What the reader sees (gemini's 1 and part of 3).** "The artifact" is the episode's checked `canonical.lean` (its sha256
equal to `check.json`'s, as `u2_gen.py` requires) plus its `EXPLAIN.md` when one was captured (24 of the 47, the P+U arm's
deliverable; design §1: "P+U's prose is visible; that is the point").
- **U1 withholds `problem_spec`'s body.** U1's key is `problem_spec`; a reader shown its body can decide the item from the key's
  own text, identically in both arms, and the read stops measuring the artifact. So for U1 the `def problem_spec` block (as
  corrected by A2.10 C1: the task view's own marked block, found line for line exactly once in the file) is replaced by the line
  `-- problem_spec: the task's own specification, withheld for this read`. Its NAME stays (the isomorphism theorem states it).
  Everything the agent wrote stays, docstrings included.
- **U2 shows the file whole.** U2's used set includes constants reached only through `problem_spec`
  (`used.tsv` column `only_via_problem_spec`), so withholding it would hide part of the key's population.

**A2.3 · U1 pairing and form (gemini's 2).** Each drawn item is read once against EACH stage-B-passed artifact of its problem.
On these 17 problems every artifact-bearing problem has BOTH arms passed (12 problems, 69 items); 5 problems have no passed
artifact (0 · 18 · 30 · 96 · 127, 38 items) and are not read, counted (corrected by A2.10 C2). ⇒ **138 U1 reads**, scored paired per item across `a0`/`a5`.
Prompt (one read, one fresh session; `__X__` / `__Y__` are the item's input and output exactly as `drawn.tsv` writes them):
> Below is a Lean file written by an agent for a programming task, and possibly the agent's explanation of it. The task's own
> `problem_spec` definition has been removed from the Lean file; the file's `generated_spec` is the agent's version of it. Question: for the input `__X__`, does the
> output `__Y__` satisfy the task's specification? Answer on the last line with exactly one of: `ANSWER: yes` · `ANSWER: no` ·
> `ANSWER: cannot tell`.

followed by the file and, when present, `EXPLAIN.md`. Scoring: `yes`/`no` against the kernel's key; `cannot tell` scored wrong
and also counted separately; no `ANSWER:` line after one retry is UNSCORED, counted, never guessed.

**A2.4 · U2 form (gemini's 3).** One read per item, listing its options (its k = 4 used + m = 4 distractors, in the `position`
order `items.tsv` already froze). ⇒ **185 U2 reads.**
> Below is a Lean file written by an agent (and possibly its explanation). Lean constants are listed after it. For EACH one, say
> whether this file's proof of `spec_isomorphism` USES it, directly or through a lemma the file itself defines. Answer one line
> per constant, in the order given, exactly `<name>: USED` or `<name>: NOT-USED`.

Scoring: per option against `items.tsv` `key`; accuracy per artifact = correct options / options. A missing, duplicated or
unparseable line leaves THAT option UNSCORED, counted; a read with no parseable line is retried once, then UNSCORED.

**A2.5 · Truth reads (gemini's 4): NOT run at this gap.** Design §4 makes the confirmer a third non-author at the Lean, and
`o90_flaglog.py` refuses a confirmer who is the reader; no confirmer is assigned and no sentence population is frozen. They
need their own addendum before any truth read. Declared here so the gap is not read as their absence of findings.
**The design's second reader** (a Claude reader on another account, §1) is likewise not run here: it spends a Claude pool and
needs its own placement.

**A2.6 · Plain only, and the halt (gemini's 5).** PLAIN only: at stage 0 the R1 form never helped (evidence's LEGA-SCORE, every
comparison at ceiling), and running both doubles the reads for a form with no measured gain. Reader `gemini-4-argon-high`
(evidence, 10-22). Halt: the read set stops when the Gemini pool's spend across it exceeds **12 points** (row R's ≤ ~12), at
any 503, or at 3 failed reads in a row (the stage-0 machinery's halts, unchanged); a halted set is reported at the n it reached.
**Where:** gemini's default, the reader's own box under its own `.agyhome`, the run box's directory copied across and checked against its
`SHA256SUMS` before the first read. **When:** the Z265 hold, never inside the Z chain.

**A2.7 · Before the first read.** gemini ports the stage-0 machinery to A2.2–A2.6 in one harness and drives it with a 2-read LIMIT
probe (one U1, one U2, never scored) plus a red mutant on the withholding of A2.2 (a U1 prompt that carries `problem_spec`'s body
must refuse); bench reads the harness before the gap. ⚠️ **Limits:** one reader model; the reader is not blind to the arm (the
design's own limit); `cannot tell` is scored wrong, which favours an artifact whose spec is complete enough to decide.
**A2.8 · Riders (evidence, the design's author, read 10-24 08:42; neither changes A2.2–A2.6).**
1. §4 reads "Consistent with you" only "if none of the three 'wrong' rules fires", and a rule that has not RUN has not "not
   fired". **Until the truth reads run, stage 1's overall reading is INCOMPLETE, never "consistent"**: it may report success,
   cost and the U-probes. The truth-read addendum is **due by 2026-10-28**, and no stage-1 verdict is quoted before it lands.
2. With the Claude reader deferred, **every U1/U2 accuracy is "by one reader mechanism (Gemini)"**, and that phrase rides
   beside the figure wherever it is quoted.
**A2.9 · The withholding rule, driven (bench, before any read).** `o90-cutcheck-2026-10-24.py` (run box `~/bench-dry/`) applied
A2.2's rule to all 47 artifacts: exactly one `def problem_spec` block in each, every cut contains the spec's `∃`, none reaches
`generated_spec`; cuts are 13–26 lines; the line after each cut is `/--` 29 · `theorem` 13 · `namespace` 3 · `section` 1 ·
`lemma` 1. ⚠️ The rule keys on a line starting `def problem_spec`; a file that defined it another way would fail the count
check, not be cut silently.
**A2.10 · systems' non-author read (10-24 08:48, its read record at seat `ce3a342a3`), all taken.**
- **C1 · the cut is the VIEW's block.** The withheld text is the task view's own `def problem_spec … -- end_def problem_spec`
  block (marker stripped); the harness finds it line for line exactly once in `canonical.lean` and refuses the read otherwise.
  systems measured it equal to A2.9's cut in 47/47. (The literal "declaration or docstring" sentence would also have taken a
  `namespace`/`section`/`open` line in 4 files, leaving an orphan `end`.) A2.9's `generated_spec` arm cannot fire (it precedes
  `problem_spec` in all 47) and its `∃` arm tests under-cut only; both are declared, not counted as coverage.
- **C2 · counts.** 12 problems are read and 5 are not (A2.3 corrected above); 69 items, 138 reads stand.
- **M1 · the withheld spec comes back through EXPLAIN.md, in ONE arm.** Frozen BEFORE any read: run box
  `~/bench-dry/o90-u1-spec-recoverable-2026-10-24.tsv` (sha256/16 `00f1d80781af8607`; script `o90-specrec-2026-10-24.py`, systems'
  rule unchanged: every informative spec line found verbatim in the shown text; a lower bound, paraphrase unseen). On the 24 U1
  artifacts: a5 `yes` 6 (problems 31 · 52 · 59 · 73 · 82 · 148) · `partial` 2 · `no` 4; a0 `yes` 0 · `partial` 2 · `no` 10.
  **NO REDACTION** (it would change the arm under test; design §1: "P+U's prose is visible; that is the point"). **U1 is reported
  twice, side by side: on all 12 problems, and on the problems where neither arm is `yes` (6)**, with the per-arm `yes`/`partial`
  counts beside both. The prompt's sentence "The task's own specification is withheld" is replaced by "The task's own
  `problem_spec` definition has been removed from the Lean file" (systems' D1 wording: true even where the agent's own
  lemma restates spec lines, 4 U1 artifacts), which stays true when the prose quotes it. The M2 guard keys on the withheld
  block as ONE CONTIGUOUS RUN in the Lean part (systems' D2: a per-line guard refuses 24/24 real files).
  ⚠️ gemini's alternative (a), a line-level redaction of EXPLAIN.md, was BUILT and driven (bus 10-24 08:48) and is DECLINED
  here for the reason above and its own measured limit (10 artifacts keep fragments inside longer lines; a re-broken quote
  evades it). It is recorded so a reader of the U1 figure meets the alternative beside it.
- **M2 · the guard reads the LEAN part only.** The refusal (A2.7's mutant) is keyed on the withheld block's lines in the
  `LEAN FILE` section, never in `EXPLAIN.md`, and is driven on the real a5 prompts as its control (it must PASS all 138).
- **Q3 · `cannot tell` stays scored wrong, and two figures ride beside every U1 accuracy:** the per-arm `cannot tell` count, and
  accuracy over answered items. (systems: under M1 abstentions fall on a0, so the scoring alone would turn the asymmetry into
  an a5 advantage.)
- **§4's U1 route out of VOID (evidence, the design's author, 10-24 08:49; registered here before any U1 read).** The design's
  VOID clause can be escaped by "P+U's U1 accuracy is at least 10 points higher than P's across all artifacts". Under M1 that
  +10 can be reached by P+U QUOTING THE KEY. So: (b) the U1 route lifts VOID only if the +10 holds on BOTH the whole set and the
  neither-`yes` subset; on the whole only, the reading is "U1 difference explained by recovered spec text; VOID not lifted by
  U1". (c) If the subset holds fewer than 4 problems, the U1 route is UNRESOLVABLE at this n, never passed. (At this freeze it
  holds 6.) The U3 route and the three "wrong" rules are untouched: U3 reads stage C's checker, not a reader.
- **The live probe:** gemini's default stands: its 2-read probe is the first act of the Z265 hold (agy rotates the refresh token
  on a warm-up, so no read runs while a Z cell is live), posted before the 323 reads.

## ⚖️ ADDENDUM 3 — 2026-10-25: THE TRUTH READS (A2.5's deferral). APPENDED; all text above untouched. Written before any truth read.

**Why now.** A2.5 deferred the truth reads to their own addendum, and A2.8 rider 1 makes stage 1's reading INCOMPLETE until they
run; it is due by 2026-10-28. This addendum registers the sentence population, the read form, the readers, the confirmer, the
halts and the order. The design governs (its §3 truth row and §4 "wrong on truth", [F7] [F8c]); the flag log is §7's.

**A3.1 · The population, frozen.** Every prose sentence of the 47 scored stage-B artifacts (the 23 a0 and 24 a5 under the cell's
state root, the same 47 that row R read), split by `harness/s2lean/o90-2026-10-23/o90_sentences.py` (sha256/16 6c2092fefc4cd137;
selftest 16/16; mutants of the split, code-fence, backtick/i.e., doc-comment-list and given rules each turn their own arm red, and
the table rule's arm was red before the rule). A markdown table's header and separator are dropped and each BODY ROW is one
sentence (systems' D1: a whole table had survived as one sentence, so one false row would have made ~10 claims one FALSE).
Prose is `stageB.lean`'s doc comments (`/-- -/`, `/-! -/`) and `EXPLAIN.md`, each without fenced code and headings; a piece under
3 words is dropped and counted. **A sentence present verbatim (whitespace-collapsed) in its problem's task view
(`~/bench/o90/s2views/problem_<id>/`) is GIVEN** — the task's own docstring and test cases, copied into the artifact by both arms —
**marked `given=yes`, kept in the file, and read by no one** (systems' B1, evidence concurring). Verbatim is a lower bound on
copied text.
At this freeze, on the run box (`~/bench-dry/o90-truth-sentences-2026-10-25-v3/sentences.tsv`, sha256/16 334ac0b784d5dcc5):
**WRITTEN a0 39 (all in doc comments) · a5 933 (160 in doc comments, 773 in EXPLAIN.md); GIVEN a0 116 · a5 118; 57 pieces
dropped. 14 of the 23 a0 artifacts carry no written sentence.** The reads run on a byte-checked copy of that file, never a
re-split. *(Two earlier freezes are superseded and no read ran on either: `…-2026-10-25/` fc23f58ca8624c81 (script ccc3c4dd2b7881c9,
1,109 sentences with the given text inside them and inline code cut), and `…-2026-10-25-v2/` 158ed108e78476de (script
152871ca1bef90fc, a5 written 877, each table one sentence).)*

**A3.2 · Read 1: Gemini, one read per artifact (PLAIN).** Reader `gemini-4-argon-high`, a fresh session per artifact, never the
author. PLAIN only: R1 did not help in stage 0's legs (b) and (c) (evidence's LEGB-SCORE and legC-SCORE, 0 discordant pairs in
each). **This departs from the design's §3 text, which names R1 for the truth reads**; R1's substance survives where it decides, in
A3.4's declare-the-declaration-first form. The prompt is exactly:
> Below is a Lean file written by an agent, then numbered sentences from that agent's documentation of it. For EACH sentence,
> say whether it is FALSE of this Lean file: it states something the file's definitions and theorems do not say, or contradict.
> Answer one line per sentence, in the order given, exactly `<n>: OK` or `<n>: FALSE`.
The Lean file is the artifact's whole `stageB.lean`; the sentences are its WRITTEN rows of `sentences.tsv` (`given=no`) in file
order. An artifact with no written sentence is not read (14 a0, 0 a5 at this freeze): **47 → 33 reads.** A missing,
duplicated or unparseable line leaves THAT sentence UNSCORED, counted; a read with no parseable line is retried once, then
UNSCORED.
**The prose gate is not run.** §3's truth row names `check_prose_lean.py` beside the reads. Stage 0 leg (b) measured its lexicon at
0 of 89 on CLEVER sentences (TRUE 0/45, PLANTED 0/44), with its positive control firing: it detects verification vocabulary, not spec
content, so on this bed it cannot separate a true sentence from a false one. It is also salt's tool, outside this repository.

**A3.3 · Read 2, the design's Claude reader.** Same form as A3.2, a fresh Claude session on an account with no shared context,
which never sees read 1's verdicts. **PLACED by the PM (evidence, bus 2026-10-25 00:41) on a named Claude pool (the one whose weekly reset comes soonest)**, under the combined cap of
A3.5. If it does not run, every truth figure is **"by one reader mechanism (Gemini)"** (A2.8 rider 2), and the miss rate a
second read would catch is UNMEASURED.

**A3.4 · The confirmer, at the Lean.** For each artifact with at least one FALSE flag, ONE fresh Claude session (never the
author's episode, never the reader; `o90_flaglog.py` refuses either) reads the whole `stageB.lean` and that artifact's flagged
sentences, and is asked exactly:
> Below is a Lean file written by an agent, then numbered sentences that a reader judged false of it. A sentence is FALSE of
> this Lean file if it states something the file's definitions and theorems do not say, or contradict. For EACH sentence, first
> write the name of the Lean declaration the sentence is about and what that declaration states, then on its own line answer
> exactly `<n>: CONFIRMED-FALSE` or `<n>: NOT-FALSE`.
CONFIRMED-FALSE is `confirmed = yes` in the flag log, NOT-FALSE is `no`. An unparseable answer is retried once, then that
sentence is UNSCORED, exactly as a reader's is (systems' M2).
**UNSCORED on the per-problem rule (systems' M2):** an artifact with ANY unscored sentence, at a read or at the confirmer, is
UNSCORED on §4's per-artifact rule, and the UNSCORED artifacts are printed per arm beside it; its scored sentences still count in
the per-sentence ratio. Model: claude-opus-5, the stage's model, so the confirmer is a different
MECHANISM from the Gemini reader that flagged. It reads the UNION of read 1's and read 2's FALSE rows for the artifact (§3: a
sentence is FALSE if EITHER read flags it). **At most 33 reads (one per artifact with a written sentence); PLACED by the PM on the same Claude pool** under A3.5's cap.
⚠️ A Gemini confirmer is NOT registered: stage 0 measured this reader flagging most honest sentences ON THE RESEARCH-MATH BED
(leg (c) false alarm 75.0 % PLAIN, 63.2 % R1; AEK 68.8 % / 53.3 %). On the CLEVER bed leg (b) read 0 of 45, but that true set was
admitted by a Gemini AGREES read, so its 0 is by construction. A confirmer of the reader's own mechanism would inherit the bias it
exists to remove.
**A3.4a · The confirmer is CALIBRATED first (the PM's design word, a precondition).** Before the confirmer set, A3.4's exact prompt
is run on stage 0 leg (b)'s CLEVER items (45 TRUE and 41 PLANTED, `~/.fleet/executors/gemini.runs/o90-stage0/legb`), each presented
as "judged false" exactly as in the real set, with its problem's `problem_spec` as the Lean file, grouped per problem. Reported: the
confirmer's false-positive rate on the 45 TRUE and its recall on the 41 PLANTED. **Why:** the per-artifact rule is amplified by
that rate p, since P(an artifact carries >= 1 false confirmation) = 1 − (1 − p)^k, with k about 38.9 written sentences per a5 artifact and
1.7 per a0 written (at p = 2 %: 54 % against 3 %; at the 6.4 % bound: 92 % against 11 %). Beside every per-artifact truth figure is printed the fire rate expected from confirmer
noise alone at the 95 % upper bound of the measured rate (0 of 45 bounds it at 6.4 %). **The per-artifact rule is read as a verdict ONLY IF
the a5 noise-only fire rate at the calibration's 95 % upper bound is at most 25 %.** That needs p ≤ 0.74 %, about 405 TRUE items at
0 errors; at n = 45 even 0 of 45 bounds p at 6.4 % (a5 noise-only 92 %), so **at this n the per-artifact rule CANNOT pass: it is
REPORTED, with its noise rate beside it, and it does not decide.** *(The PM's first gate here, "more than 2 of the 45 TRUE ⇒ not
read", passed on 0–2 and so hid that it could never be met; withdrawn by its author, bus 2026-10-25 00:47, before any read.)*
**A3.4b · The truth axis is DECIDED per sentence (the PM's design word, 2026-10-25 00:47; it changes the design's §4 truth rule
and goes to the Captain's ledger as one line).** Over all WRITTEN, scored sentences, confirmed-FALSE against not, a5 against a0:
a one-sided Fisher exact test, p ≤ 0.10. **"Wrong on truth" if a5's confirmed-FALSE rate is significantly higher than a0's.**
Confirmer noise inflates both arms' per-sentence rates alike ONLY IF the readers flag the two arms at the same per-sentence
rate, because the confirmer sees flagged sentences only. **So each arm's per-sentence FLAG rate, read 1 and read 2 separately, is
printed beside this test's figure**, which makes that assumption checkable (the PM's INFO, 2026-10-25 00:48).

**A3.5 · Halts.** Read 1: the set stops when its Gemini spend exceeds **6 points**, at any 503, or at 3 failed reads in a row (A2.6's
machinery); a halted set is reported at the n it reached. **The Claude reads (A3.3, A3.4a, A3.4) share ONE cap: 3 points on
that pool** (the PM's). The first 2 Claude reads are metered; if they move the pool more than 0.5 point, the set halts and is
re-priced before the rest. If they start after that pool's reset (Mon 2026-10-26 19:59), they move to the PM's second named pool under the same cap.

**A3.6 · Order.** (1) the copy of `sentences.tsv` checked against 334ac0b784d5dcc5 · (2) a 2-read LIMIT probe of A3.2, never
scored · (3) the 33 reads, written as flag-log rows with `verdict` OK or FALSE · (3b) read 2's 33 reads (A3.3), blind to read 1 ·
(4a) the confirmer's calibration (A3.4a), posted before (4) · (4) the confirmer set over the UNION of FALSE rows · (5)
`o90_flaglog.py` over the complete log, then the design's §4 truth rule on the paired problems. Read 1 runs on
gemini's box after row R's reads end, never beside them.

**A3.7 · Limits that ride with every truth figure.**
1. **The axis is per artifact and the arms carry very different amounts of WRITTEN prose (a5 933 sentences, a0 39, about 24 to
   1; doc comments alone a5 160, a0 39, printed beside the whole).** An artifact with more sentences has more chances to carry one
   false one, and **14 of 23 a0 artifacts carry no written sentence, so they cannot carry a false one at all**: the per-problem
   rule leans against a5 by construction. The ratio printed beside it is **false sentences per SENTENCE** (A3.7 3: the splitter is not a claim
   detector), never the design's "per claim sentence", and it is the reading that does not lean.
2. One confirmer; the readers and the confirmer are not blind to the arm (the design's own limit, §1). **The confirmer is
   claude-opus-5, the authors' model:** any bias they share runs toward NOT-FALSE in both arms, so it lowers the axis's power and
   leans toward the hypothesis under test.
3. The sentence rule is a splitter, not a claim detector: a sentence that states nothing checkable is still read. A reader may
   call it OK or FALSE; only a confirmed FALSE counts.
4. **The per-sentence test (A3.4b) pools sentences across artifacts**, so clustering within an artifact is ignored and its p is
   optimistic; a0 has 39 written sentences in 9 artifacts, so only a large difference can fire; and the calibration's Lean file
   is the problem's `problem_spec`, shorter than a real `stageB.lean`, so its rates may not transfer. **Sentence LENGTH differs
   by arm (systems' D2): written words per sentence a0 15.5 · a5 27.9; on doc comments alone a0 15.5 · a5 19.2.** A longer
   sentence may carry more chance of a false confirmation, which A3.4a's short items cannot test, so **the doc-comment-only
   Fisher reading (a0 39 against a5 160) is printed beside the whole as the length-matched sensitivity read.**
5. This addendum decides nothing about U1, U2 or U3, and its readings are not quoted until §4's truth rule has run on them.
