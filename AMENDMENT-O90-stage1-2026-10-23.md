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
  artifacts test the instrument and are not a reading of any arm.

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
  model, as amendment 8's did); anything else halts the run before cell 2.
- **Pool and config dir:** one pool, the one his 10-23 word names, through a NEW hermetic config dir on the run box holding only
  the pinned `settings.s2.json` and **its own fresh login** — never a copy of a live credential, because these credentials carry
  a rotating refresh token and two live copies can blank each other at the first refresh. The calibration pair is that dir's
  first-refresh test, read before cell 2. Passed as `CFG` to the driver.
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
```
`o90_ids.py`: the thirty, and a flag-list mutant refuses. `o90_flaglog.py --selftest`: PASS, 7 refusals fired; two mutants
(an axis that ignores the confirmation; an author read accepted) each fail it. `spread.py` and `calls_to_green.py` were
re-run by the lead from an independent copy of amendment 8's state: both outputs byte-identical to the committed ones.

## 12 · Limits

n = 30 detects only large effects (design §6). One model, one bed. U3 runs on ~16 problems. C0 also lacks the prior-work
paragraph (§4). The spread is not a pure noise floor (§6). The per-call trace sees agent-chosen compiles only (§6). The client
moved between amendment 8 and this run, so no O90 figure is compared with amendment 8's.
