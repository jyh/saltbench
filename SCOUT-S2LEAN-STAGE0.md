# SCOUT — S2-LEAN STAGE 0: the CONTROL protocol on CLEVER (plain · placebo) — FROZEN 2026-08-29, bench seat

**Frozen 2026-08-29, bench seat, BEFORE any model call on this substrate** (two refuter passes: §8/§9; controls 30/30 on
the Studio and the run-shaped dry driven on the round-2 harness). Authorised by the scout's decision
rules (`seat/briefs/2026-08-28-DELEGATION-morning-council-only.md` §1, in force on the Captain's word 20:3x):
**F1** resolved the S1 fork to S2-Lean / CLEVER first; **F2** — the dated freeze commit IS the authorization,
controls before treatment, treatment arms as dated amendments before their own first call; **F3** reads the
control result; **F4** Sonnet first; **F5** an uncovered result is a HOLD with a fallback row, never an
improvised arm. Everything not stated here is inherited from `SCOUT-STAGE0.md` (S1) as amended — the agent,
the metering, the termination typing, the driver rules — **except every S1 sentence that presumes the container or
the SWE-bench patch** (see §4/§6: `--network none`, `docker exec` scoring, "CHECK 2b in every container", the
`model_patch.diff`/digest/platform artifact rows — none hold on this substrate; §4 and §6 give the S2 forms). `harness/` is the normative form. The source read behind
the choice: `S2-SOURCE-READ-2026-08-29.md`. The refutation this draft answers: `seat/fleet/REFUTER-saltbench-s2lean-2026-08-28.md`
(90 confirmed, 0 refuted) — §8 maps its classes to the repairs.

## 0 · What this stage is for — and what it cannot show

Two control arms, PLAIN (`a0`) and PLACEBO (`a1`), on CLEVER, so that the **F3 quantity exists**: the
fraction of drawn problems on which the plain arm's *agent-written specification is proven, by the kernel, to
admit exactly the same implementations as the hidden human specification* (CLEVER's Task-1 isomorphism) —
and its metered distribution, whose per-stage `a0` p90 the cap rule consumes for the salt arm. It measures
nothing about the salt method.

**Cannot show:** everything S1's §0 names (mechanism; arm-blindness by construction; sampling variance vs arm
effect) — with these substrate-specific sharpenings:
- **A closed network is not shown; it is FENCED and PROBED.** S1 closed the test environment with a container.
  Here the Lean project is native on the host, so the fence is the operating system's sandbox around the agent's
  Bash tool (§4) and around the checker (§3), measured by the smoke probes of §7 before the driver starts, and
  the hook is demoted to what it always was: an attempt audit over command text.
- **Contamination on this substrate has a specific shape — RECALL OF THE HUMAN SPEC.** `trishullab/clever` has been
  public since 2025; the human `problem_spec` text is in the training data of any 2026 model, and a spec
  reproduced verbatim makes the stage-B proof one line (`fun _ => Iff.rfl`, driven). The isomorphism PROOFS are
  not public (0 of 161 shipped), so a proven isomorphism is a kernel fact about this run — but a high F3 can be
  recall, not specification. §2 therefore pre-registers a RECALL INSTRUMENT whose reading rule is stated before
  the first call. Whether recall inflates the rate is not decidable here; the instrument makes it VISIBLE.
- **The reference "ground-truth" specs are disputed** (80/161 flagged by arXiv 2605.23772; four excluded by its §4.2)
  and **one docstring leaks its spec in prose** (problem_90, drawn at #4): the flagged list, the excluded four
  and the NL-leaked id are recorded in `harness/s2lean/flagged.json`; F3 is reported over the drawn set AND over
  its unflagged subset (read as the F5 band-divergence check: if the all-drawn band and the unflagged band differ,
  the result is uncovered ⇒ HOLD) AND without the NL-leaked id (reported, not banded) (§2).
- **The isomorphism shape is strict**: a docstring-faithful spec that is strictly stronger than the human's (the
  human spec has a don't-care region) is provably NON-isomorphic (kernel-checked on problem_0, unflagged). F3 thus
  measures "reproduced the human's exact boundary". §2 pre-registers a blind B-failure TRIAGE so a low rate can be
  read as a tier floor only if the failures are the agent's.
- **The axiom audit and the kernel replay are the scout's, not CLEVER's** — the reference checker accepts any
  axiom and never re-checks the module.
- **Which head wrote this freeze:** the DRAFT v1→v2 text and repair round 1 (86f9e04→4a26604) were written on
  **Fable 5** (with Sonnet/Opus refuter subagents); from 2026-08-29 02:06:50 PDT the seat's head fell back to
  **Opus 4.8** (a Fable-5 `[cyber]` safety fallback on the network-fence text, session-scoped — not a usage cap),
  which wrote refuter pass 2's integration and repair round 2 (this commit). Pass 2's finders/verifiers ran on
  Sonnet/Opus by design either way. Recorded so the artifact is honest about the head; the referee is the kernel.

## 1 · The substrate, pinned

- `trishullab/clever` at commit **`8348039a7ff7730a126d761e71d0439735eeb3e2`** (MIT). Lean
  **`leanprover/lean4:v4.27.0`**; mathlib **`a3a10db0e9d66acbebf76c5e6a135066525ac900`** (tag v4.27.0);
  the full `lake-manifest.json` pins the rest (batteries `b25b36a7`, aesop `cb837cc2`, plausible `009dc1e6`
  — `#test` is Plausible's command; a failing `#test` is an error, rc ≠ 0, driven). The three pins and the shas of
  the project's `lakefile.lean`, `lake-manifest.json` and `lean-toolchain` are lines in `HASHES.txt`
  (`clever-commit`, `lean-toolchain`, `mathlib-rev`, `leanproj-lakefile`, `leanproj-manifest`, `leanproj-toolchain`).
- **The id set is CLEVER's, not `range(161)`:** `src/lean4/human_eval/problem_k.lean` for k ∈ 0…163 minus
  {22, 137, 162} — 161 files (measured). The flagged list's ids are HumanEval ids = CLEVER ids (161 and 163 exist;
  22 and 137 do not).
- **A raw problem file is the CLEVER skeleton plus the human ground truth** (natural-language spec; the human
  `problem_spec`; the `generated_spec` header with body `sorry`; the `spec_isomorphism` theorem with proof `sorry`
  — in EVERY file, i.e. NO isomorphism proof ships; the `implementation` and its `correctness` proof — themselves
  `sorry` in 157/161 files; and `#test` cases). **The agent never sees a raw
  file.** `harness/s2lean/build_views.py` (the only code that reads a raw file; self-tested over all 161: parse;
  no implementation, proof or ground-truth spec leaks into any stage-A view; out-of-section residue captured)
  emits per problem:
  - **A.lean** — stage A: NL spec + preamble + `generated_spec` header, body `sorry`. Ground truth ABSENT.
  - **C.lean** — stage C: NL spec + preamble + `problem_spec` (ground truth) + `implementation` signature, body
    `sorry` + `#test` cases (as CLEVER ships them) + `correctness` theorem, proof `sorry`.
  - **frozen.json** — every statement the agent may not change, verbatim, plus the **preamble** (any text the raw
    file carries outside its marked sections — problem_62's helper `def`, problem_99/110's `import Std` — so the
    canonical file compiles for the reasons the raw file does); **frozenA.json** — the ground-truth-free subset for
    stage A (`problem_id`, `nl`, `generated_spec_header`, `preamble`).
  - **B.lean** is assembled at run time from `frozen.json` + THE SAME ARM's SCORED stage-A `generated_spec` body
    (§2, provenance): NL spec + preamble + `generated_spec` (frozen, filled) + `problem_spec` + `iso_helper_lemmas`
    slot + `spec_isomorphism` theorem, proof `sorry`.
  Each shipped file's sha is pinned (`view-A`, `view-C`, `frozen`, `frozenA` lines); `episode_s2.sh` refuses any
  stage whose view/frozen file sha is not the pinned one (stage B: the `frozen.json` it assembles from).
- **View status is pre-registered** (`harness/s2lean/view_status.json`, produced by `views_selftest.sh`, which
  compiles every A view, every B pristine file and every C view with `sorry` bodies): the C views that error
  BEFORE any agent text — CLEVER's Python-shaped `#test` blocks uncommented by its own reference view — are the
  **C-dead list** (18 at this commit — `39 44 54 62 65 77 81 87 97 110 111 112 113 119 153 155 157 160`, derived by
  compiling and identical to the refuters' independent sweep; 4 in the draw: 54, 81, 110, 112). Their stage C is NOT RUN (an arm-independent, pre-stated exclusion, its own class in the morning line).
  Stage B — the F3 stage — is unaffected.
- **The three stages, per problem and arm:** **A** write the spec blind (the statement — the salt shape's first
  half); **B** prove `spec_isomorphism` against the revealed human spec with the generated spec frozen (the kernel
  adjudicates the statement); **C** implement and prove `correctness` against the human spec. **The F3 quantity
  is stage B.** All stages are metered. **B runs only for a (problem, arm) whose stage A was SCORED and PASSED**
  (spec elaborates); otherwise the driver writes a synthetic landing `NOT_PROVEN(no_stage_A_pass)` — not a skip.
- **Data staging (the ground truth is never on the host while an arm is writing a spec blind), mechanically:**
  `harness/s2lean/views/` is EXCLUDED from `sync_studio.sh`; views reach the Studio ONLY through
  `stage_views.sh ship A` (A.lean + frozenA.json) and, after every stage-A episode of the draw has landed,
  `ship BC` (frozen.json first, then C.lean; refused until the Studio log carries `S2 STAGE A DRIVER DONE`).
  `sync_studio.sh` asserts 0 view files under `~/bench/harness` after every sync; `ship A` runs with
  `--delete-excluded` so a stale `frozen.json`/`C.lean` on the Studio is removed. `episode_s2.sh` REFUSES a stage-A
  episode if ANY `frozen.json` or `C.lean` exists anywhere under `~/bench` or the views root, and refuses ANY
  episode if the shared project is inside a git repository or carries a `.git`/`packed-refs` outside the Lake
  package clones under `.lake/packages/` (those must keep theirs — Lake re-checks each package's revision against
  the manifest on every load — and none of them may be CLEVER), a `human_eval/` or `sample_examples/` directory,
  any `problem_*.lean`, or their oleans (§4).

## 2 · Draw, subset, provenance, and the F3 reading

- **Draw:** the 161 real ids sorted by `sha256(id + "saltbench-s2lean-stage0-2026-08-29")`, the four excluded ids
  (32, 39, 123, 160 — arXiv 2605.23772 §4.2: Collatz-hard, Fibonacci-primes-hard, a broken helper, a missing
  precondition) REMOVED before taking the first k (`harness/s2lean/draw.py`; the k=30 list's sha is pinned as
  `draw-30`). **Stage 0 runs k = 30:** `109 34 73 90 159 12 69 0 163 146 129 16 4 81 38 142 110 96 112 141 31 114
  75 54 127 18 74 51 82 99` (14 flagged; 90 NL-leaked; 54/81/110/112 C-dead). Extending k is an amendment; a stop
  is reported with the k reached.
- **Provenance A → B:** `A.bodies.json` for (problem, arm) is written ONLY by a stage-A episode whose termination
  is scored (`DONE|ROUNDS_EXHAUSTED|WALLCLOCK|TOKEN_CEILING`, no `VOID`/`HARNESS_ERROR`/`SMOKE`/`DRY` prefix) AND
  whose check passed; it carries `a_episode`, `a_bodies_sha256`, `a_termination`, `a_passed`, `a_view_sha256`;
  any stale copy is deleted otherwise. The stage-B manifest records them; the morning line counts a B row only
  when its `a_episode` IS the scored A row for that (problem, arm) — else ORPHAN, reported, not counted.
- **F3** is read on the PLAIN arm, stage B, over the k drawn problems: proven / k, an unrun, unlanded, skipped or
  orphaned problem counting as not proven. **≥ 80 % ⇒ HOLD** (too easy at this tier; report for council) ·
  **20–80 % ⇒ run the salt arm** (registered as a dated amendment with its profile) · **< 20 % ⇒ HOLD** (a floor, a
  finding about the tier). Reported BESIDE it, not read against the band: the rate over the unflagged drawn
  subset; the rate without the NL-leaked id; per-problem failure classes.
- **The flagged-spec list (arXiv 2605.23772 Table 1, 80 ids):** `5 7 12 20 23 24 26 27 34 36 39 44 45 47 49 50 51 62 64
  65 66 67 68 69 71 72 75 78 79 81 84 85 86 88 89 90 91 93 94 95 97 98 99 100 103 104 105 106 108 109 110 111 114 115
  116 117 121 122 125 126 129 130 132 134 138 139 140 143 144 150 151 152 153 154 155 156 158 159 161 163`; the excluded
  four; the NL-leaked `[90]` — all in `harness/s2lean/flagged.json` (pinned).
- **RECALL INSTRUMENT (stated before computing; computed after the run; never fed back):** for every stage-B pass,
  `sim` = `difflib.SequenceMatcher` ratio between the normalised token sequences (whitespace and comments stripped)
  of the agent's `generated_spec` body and the human `problem_spec` body; `trivial` = the proof body matches
  `^(by\s+)?(intro\s+\w+\s*;?\s*)?(exact\s+)?(Iff\.rfl|Iff\.refl\s+_|rfl|fun\s+\w+\s*=>\s*Iff\.rfl)\s*$`;
  `recall_suspect` = `sim ≥ 0.80` OR `trivial`; **f_high = suspect passes / passes.** READING RULE: **if f_high ≥ 0.5
  the F3 band is NOT read** (reported as RECALL-SUSPECT ⇒ HOLD for council, F5); else the band is read.
- **B-FAILURE TRIAGE (blind, by the seat, after the run, from the two spec texts and the transcript):** one label
  per failed (problem, arm): HUMAN-LOOSE (agent spec strictly stronger; a kernel-checked non-isomorphism witness
  recorded where one can be written) · HUMAN-BUGGY (agent spec contradicts a flagged clause) · AGENT-WRONG (agent
  spec contradicts the docstring's examples or the `#test` lines, mechanically) · PROOF-HARD (no witness of
  non-isomorphism found). The RATE triggers the band; the TRIAGE is its reading: `< 20 %` is a tier floor only if
  AGENT-WRONG + PROOF-HARD dominate; otherwise it is a council item (F5).
- **The cap the salt arm consumes is PER STAGE:** the `a0` p90 of the same stage (A for A, B for B, C for C).

## 3 · "Solved" — the scout's checker: the kernel, outside the agent's elaboration

`harness/s2lean/check.py`, per stage per episode, on the Studio, no model, every step in its own process group
with a timeout that kills the group (no orphan `lean`):
1. **extract** (`extract.py`) ONLY the agent-writable bodies by the section markers — A: `generated_spec_body`;
   B: `spec_isomorphism_proof` + `iso_helper_lemmas` (the `generated_spec` body comes from the scored
   `A.bodies.json`, never from the stage-B file); C: `implementation` + `correctness_proof` +
   `correctness_helper_lemmas`;
2. **screen** (`screen.py`) the bodies with comments and string literals stripped: any command-introducing or
   meta keyword fails — `macro macro_rules syntax notation infix* prefix postfix elab elab_rules declare_syntax_cat
   run_cmd run_elab run_tac initialize builtin_initialize axiom unsafe opaque partial implemented_by extern import
   #eval #eval! #print #exit set_option` (except `set_option (maxHeartbeats|maxRecDepth|synthInstance.*) N in`) —
   `harness/s2lean/screen.py`, self-tested; a screened body is NOT compiled. `sorry`/`admit` are NOT screened — the
   kernel catches them (`sorryAx`), and a `sorry` in a comment must not fail an honest proof (driven);
3. **assemble** (`assemble.py`) the CANONICAL file (import, preamble, NL, frozen statements verbatim, the bodies) —
   with NO audit command appended — and, once per problem and stage, the PRISTINE file (the same layout with
   `sorry` bodies and no agent text);
4. **compile** both with the toolchain's `lean -o <module>.olean` in the environment `lake env` gives, UNDER
   `/usr/bin/sandbox-exec` (profile `sandbox_check.sb`, pinned: network denied; process fork and exec denied, so an
   in-body `#eval IO.Process.run` cannot spawn anything; writes denied except the check's work dir and the temp
   dirs; reads NOT denied — a body could print a host file into its own bounded 3 KB `log_tail`, stated here) — in
   its own process group, the timeout killing the group; rc must be 0; for stage C the `#test` lines are in the
   canonical file (a failing test is rc 1); the pristine file is compiled AFTER the canonical, outside its
   writable paths, and cached per problem and stage under `$VIEWS/.pristine-cache` — it carries `problem_spec`
   for B/C, so it lives with the views and leaves with them (`ship A` wipes it; stage A refuses if a B/C
   pristine is still present);
5. **audit** (`s2audit.lean`, harness-owned, run with `lake env lean --run`): import `Imports.AllImports`; read the
   canonical module's data; **REPLAY every one of its declarations through the kernel** (`Lean.Environment.replay`,
   v4.27.0 core — a declaration the elaborator admitted without the kernel is rejected here: KERNEL_REJECTED);
   read the pristine module; **compare, as kernel `Expr`, the TYPE of every frozen declaration** (A: `generated_spec`;
   B: `generated_spec`, `problem_spec`, `spec_isomorphism`; C: `problem_spec`, `implementation`, `correctness`)
   **and the VALUE of `problem_spec`** between canonical and pristine — any difference is STATEMENT_ALTERED (a
   notation, macro, instance or `open` that changes what the frozen text means is caught here, by construction, not
   by a word list); then **collect the axioms** of the stage's audited declarations by walking the module's own
   `ConstantInfo`s, falling back to the import environment — the same constants the replay checks, so the axioms are
   reported even when the kernel rejects the module (and an audited name that resolves in neither fails closed):
   every set ⊆ {`propext`, `Classical.choice`, `Quot.sound`} — `sorryAx` and any user axiom fail here
   (AXIOMS_FAIL); a `native_decide` proof is already rejected at replay (the fresh kernel cannot evaluate
   `Lean.reduceBool` without the compiled closure: KERNEL_REJECTED, driven) and would otherwise fail on
   `Lean.ofReduceBool`/`Lean.trustCompiler`.
`passed` = screen ∧ compiled ∧ replay ∧ statements identical ∧ axioms; `class` names the first failure. Stage A's
`passed` means "the spec elaborates"; stage B's "the isomorphism is proven"; stage C's "implementation + correctness
proven, tests pass". **The controls (§7, `s2_controls.sh`, 30 of them, recorded in `s2-controls.json` before the
first scored run; A/B on problem_1 and C on problem_3 — neither drawn; problem_3 because only four shipped
correctness proofs are `sorry`-free and problem_0 is drawn):** positive A/B/C (B = the human body verbatim +
`fun _ => Iff.rfl`, since no gold isomorphism proof exists); negative (`sorry`); axiom (`native_decide`); the driven exploits — `local
notation` redefining `problem_spec` (STATEMENT_ALTERED), `run_cmd` with `debug.skipKernelTC` (screen; and
KERNEL_REJECTED with the screen bypassed), `elab_rules` on `#print` (screen; audit unaffected), `#eval IO.FS.writeFile`
(sandbox: the marker must not appear); the false positives that must PASS (`-- no sorry here`, `set_option
maxHeartbeats 400000 in`); the timeout control (no `lean` process left).

## 4 · The environment — native Lean, no Docker; the FENCE is the sandbox, the hook is the AUDIT

- **The agent** runs as in S1 (real HOME, `~/.claude-bench`, the login PATH, the same flags and disallowed tools),
  **under Claude Code's built-in macOS sandbox** (`harness/settings.s2.json`, pinned, identical in every arm; the
  Seatbelt fence the docs describe: OS-enforced on every Bash command and its child processes): `network.allowedDomains
  []` + `strictAllowlist` (every host denied, no prompt); writes only under the working directory and the session
  temp dir; `filesystem.denyRead` on `~/bench`, `~/bench-dry`, `~/.claude-bench`, `~/.claude`, `~/.ssh`, `~/.aws`,
  `~/.gnupg`, `~/.config`, `~/Library/Keychains`, `~/Library/Application Support`; `denyWrite ~/lean-shared` (the
  symlink target, belt and braces); `allowUnsandboxedCommands false`, `excludedCommands []`, `failIfUnavailable
  true`. The sandbox fences Bash and its children only — Read/Edit/Write are not sandboxed (docs), so for the file
  tools the audit's path resolution and VOID remain the control. **Whether this holds under `-p --dangerously-skip-permissions
  --setting-sources user,project` on claude 2.1.251 is not documented: the smoke probes of §7 MEASURE it, and the
  driver refuses to start without their PASS lines.** The Write/Edit tools have no network (docs).
- **The shared Lean project** is `~/lean-shared/clever`: a `git archive` EXPORT of `src/lean4` at the pinned commit
  (`lean_shared_build.sh`: the clone lives only under `/private/tmp` and is deleted after the export) with
  `human_eval/` and `sample_examples/` removed BEFORE the build, no `.git` outside `.lake/packages/`, built once by
  `lake exe cache get && lake build Imports.AllImports` (only `Imports` oleans exist; asserted). It
  lives outside `~/bench` so `denyRead ~/bench` is total, and `.lake/../../..` from the working copy reaches a tree
  that holds nothing secret. The realpath `/Users/jyh/lean-shared/…` that `lake env` prints is a library path: neither
  an escape nor a VOID for the audit (`~/.elan` likewise).
- **The working copy** `/Users/jyh/work/<ep>/repo` is a Lake project: `lakefile.lean`, `lake-manifest.json`,
  `lean-toolchain`, `Imports/` (source) copied from the shared project, `task.lean` (the view), and **`.lake` → a
  symlink to the shared build**; the sandbox denies writes through it (the target is outside cwd). CHECK 2b runs on
  the working copy. **The wrapper `rt`** runs `<cmd>` in the project with `~/.elan/bin` prepended, bounded by
  `perl -e 'alarm …'` (macOS has no `timeout`) in its own process group, logging to `<repo>/.rt.log` (agent-visible,
  non-scoring; moved to the artifact afterwards); the agent's own PATH has no elan, so `lean`/`lake` exist only
  through `rt`. Before every episode the wrapper is exercised under the agent's exact environment with an
  `import Imports.AllImports` probe (7–8 s cold, 4 s warm, measured).
- **The hook** (`hook-deny-network.sh`, extended; self-tested) is the ATTEMPT AUDIT: it strips the own-episode and
  `rt` wrapper prefixes before matching, anchors on launcher prefixes (`env`, `command`, `exec`, `xargs`, `nohup`,
  `time`, `caffeinate`, `nice`), and names `/dev/tcp`, scripting one-liners, `lake update|build|exe cache|clean` and
  `elan` anywhere, relative climbs (`../../`, `.lake/..`, `~user`, `Users/…/bench`); a read under `~/.elan` or
  `~/lean-shared` PASSES (a library). Self-test: 74 arms. A blocked attempt is evidence; a success that the sandbox
  should have prevented is a SMOKE FAIL and a night-stopper, never a quiet number. (The S3 probe deliberately spells
  its reads so the hook passes them — `cat "$HOME"/bench/…` — so that the OS, not the regex, is what is measured.)
- **Process discipline:** claude runs in its own process group; the watchdog and the traps kill the group; after the
  run no `lean`/`lake` of the episode may remain (killed and logged `ORPHAN_KILLED`); SHA256SUMS is computed last.
  Termination typing reads `result.errors` (a list on 2.1.251) and `result.error`, never the agent's prose.

## 5 · The arms

- **Prompt per stage** (`harness/s2lean/prompt_{A,B,C}.md`, pinned; identical across arms up to the episode path):
  A — write `generated_spec`, a `Prop` characterising exactly the docstring's behaviour; B — prove
  `spec_isomorphism`, helper lemmas allowed, statements fixed; C — implement and prove `correctness`, `#test` must
  pass, statements fixed. Each ends "when it compiles and you are satisfied, stop; the file is your answer."
- **BASE block** (`harness/s2lean/base.md`, pinned): the file to complete, the marker sections, `rt lake env lean
  task.lean`, no network, no `lake update`/`cache`, no git.
- **PLAIN `a0`** = BASE alone. **PLACEBO `a1`** = BASE + `harness/s2lean/placebo.md` — Lean-neutral house rules
  (file hygiene, style matching, staying inside the sections, stopping), profiled to the S1 placebo's length
  (1,746 vs 1,789 bytes), with NO proof-strategy content: the S1 text's "no new helper", "no new layer", "no new
  dependency" items are not inert on a proof task (pass-1 note F3-07), so it is not reused. `s0` = the canary.
- **The salt arm (`a2`)** is NOT frozen here. It registers as a dated amendment below the line, with its profile
  against the placebo's, only if F3 lands in 20–80 % and the recall instrument does not withhold the band.

## 6 · Metering, termination, artifacts — as S1, with the S2 rows

`meter.py` unchanged in its unit (message.id dedupe; governing sum incl. `modelUsage`; the audit) with
`~/lean-shared` and `~/.elan` as neutral prefixes. `--max-turns 40`; `WALL_S` 5,400; `TOKEN_CEILING` 8,000,000
(safety only; stage 0 has no parity cap). Landings carry `<ep> <problem> <stage> <arm> <term> <metered>` in
`s2-landings.log`; the driver's synthetic rows use `<none>` and 0. The S2 artifact is `task.lean`, `bodies.json`,
`canonical.lean` (+ `canonical.olean` for the a→B chain), `check.json` (with its `class`), `audit.json`, `compile.log`,
`env_probe.txt`, `rt.log`, `session.jsonl`, `manifest.json`, `SHA256SUMS`; the manifest keys are `substrate`, `stage`,
`lean_toolchain`, `leanproj_sha`, `view_sha256`, `frozen_sha256`, `check` (the check.json subset incl. `class`),
`passed`, `checker_sha256`, `orphans_killed`, and for stage B `a_episode`, `a_bodies_sha256`, `a_termination`,
`a_view_sha256`. **The S1 container-and-patch rows do NOT exist on S2** — no `model_patch.diff`, `image_history.txt`,
`check2b.container.log`, `env_python.txt`; no patch sha/bytes, `agent_made_git`, docker platform, digest or base.

## 7 · Order of operations (the runbook, executable, as the operator runs it from tmux over ssh)

**STEP 0 — seat, before the freeze commit.**
(0a) `export CLEVER_SRC=<clever clone>/src/lean4`; assert `git -C <clone> rev-parse HEAD` = `8348039a7ff7730a126d761e71d0439735eeb3e2`.
(0b) `bash harness/hashes.sh >/dev/null` (it EXITS non-zero if `CLEVER_SRC` is unset — a pin-less HASHES.txt would make
every episode refuse); assert `grep -c '^leanproj-' harness/HASHES.txt` = 3 and `git diff --quiet harness/HASHES.txt` (or
review the diff). (0c) refuter pass 2 (this file answers it: §9); `--dry` and the RUN-SHAPED dry (`DRY_RUN=1` + the stub,
so extract→assemble→check→audit RUN) on the seat; then the **dated freeze commit** (retitle from DRAFT) = the
authorization (F2). The freeze commit sha is written to `harness/FREEZE-COMMIT` by `sync_studio.sh` at STEP 1.

**STEP 1 — Studio prep (no model), in this ORDER (each step names the fact the next needs):**
(1a) `bash harness/sync_studio.sh` FIRST — it commits `harness/` to the Studio (views EXCLUDED; a stale Studio views dir
is purged; `FREEZE-COMMIT` written; the receipt asserts every S2 file's Studio sha == the pin, and the three `leanproj-*`
pins and `draw-30` are present). The build reads `clever-commit` from the Studio's HASHES.txt, which only this sync puts
there. (1b) `ssh kriterion-lan 'bash ~/bench/harness/s2lean/lean_shared_build.sh'` — export → `~/lean-shared/clever`,
`lake exe cache get` + `Imports` build, the six assertions, prints the `leanproj-*` shas (must equal the pins). (1c)
`ssh kriterion-lan 'cp ~/bench/harness/settings.s2.json ~/.claude-bench/settings.json'` then assert its sha ==
`grep '^settings.s2.json ' harness/HASHES.txt` — **re-run this after ANY claude login/auth refresh on the Studio (a login
REWRITES settings.json), and re-run smoke afterward** (episode_s2.sh asserts this sha per episode). (1d) the controls, kit
OUTSIDE `~/bench` (it carries `frozen.json`, which would trip the stage-A refusal): on the seat
`rm -rf /tmp/s2kit && python3 harness/s2lean/s2_controls_kit.py "$CLEVER_SRC" harness/s2lean/views /tmp/s2kit`;
`ssh kriterion-lan 'rm -rf ~/s2kit'`; `rsync -a /tmp/s2kit/ kriterion-lan:~/s2kit/`;
`ssh kriterion-lan 'bash ~/bench/harness/s2lean/s2_controls.sh ~/lean-shared/clever ~/s2kit ~/bench/state/s2-controls.json'`
(CONTROLS PASS 30/30 required; it deletes the kit unless `KEEP_KIT=1`); then `ssh kriterion-lan 'rm -rf ~/s2kit; find ~/bench ~/lean-shared -name frozen.json -o -name C.lean | wc -l'` must print 0 before ship A.

**STEP 2 — ship the stage-A views and probe (no scored call yet):** `harness/s2lean/stage_views.sh ship A`
(A.lean + frozenA.json only; `check` shows frozen = 0, C = 0). Smoke `smoke_s2.sh` (arm `s0`, `SMOKE(…)`, never scored,
never writes `A.bodies.json`): **S1** canary + PATH · **S2** network (curl, a written `fetch.py`, a Lean
`#eval IO.Process.run curl` through `rt` — all must FAIL) · **S3** reads (`~/bench/harness/arms/a1.md` and `~/.claude-bench`
DENIED; `~/lean-shared/clever/lakefile.lean` readable — S3 spells its reads so the HOOK passes them, so the OS, not the
regex, is measured) · **S4** writes (`.lake/probe` DENIED; cwd writable) · **S5** the compile through `rt` from the agent.
`run_s2_stage0.sh` refuses to start unless the LAST verdict per id S1–S5 is `SMOKE PASS` carrying this freeze's
`episode_s2.sh` sha, AND `~/bench/state/s2-controls.json` has `controls_pass:true`.

**STEP 3 — the run:** `run_s2_stage0.sh A 30` (60 episodes) · when every A has landed
(`grep -c 'S2 STAGE A DRIVER DONE'` = 1, or `has_terminal` over the 60 (task,arm) pairs), `stage_views.sh ship BC` ·
`run_s2_stage0.sh B 30` · `run_s2_stage0.sh C 30` (C-dead skipped, view_dead landings) — each under caffeinate in tmux
`bench:run`; the seat's watch emits a liveness line per landing.

**STEP 4 — the morning line, then archive back to the seat:**
`ssh kriterion-lan 'python3 ~/bench/harness/s2lean/s2_morning_line.py ~/bench/state 30'`: per stage and arm,
passed / landed / k; **the F3 line** (plain, stage B, over k) with its band; beside it the unflagged rate (the F5
band-divergence check), the rate without problem_90, the recall instrument (`f_high` and whether the band is read),
the C line over the C-eligible subset, orphan/superseded/view-dead rows, the classes (KERNEL_REJECTED, STATEMENT_ALTERED,
PROVENANCE, AXIOMS_FAIL, COMPILE, SCREEN), the per-stage `a0` p90 the cap rule consumes. **No p-value, by design.**
Then `rsync` `~/bench/state/` (manifests, check.json, canonical.lean, session.jsonl) back to the seat for the B-failure
triage (§2) and the results commit; `studio_phase.sh out`-style assertion that no ground truth remains.

## 8 · Refuter pass 1 (2026-08-28, 86f9e04) → what changed in this draft

| class (lenses) | repair (section) |
|---|---|
| stage-B check KeyError — F3 unmeasurable (8 lenses) | B assembles from the scored `A.bodies.json`; `check.py --a-bodies` (§2 provenance, §3.1) |
| `timeout` absent on macOS — every episode dies at the probe (9 lenses) | `perl alarm` + process group in `rt.template` (§4) |
| ground truth on the host in stage A: sync mirrors views; the clone's `.git`; `.lake/../../..` (GT-1/2, FN-3, MT-F2, M3, NF2/3, F3) | views excluded from sync; git-free export at `~/lean-shared`; refusals on any frozen/C.lean, any `.git`, any solution dir/olean (§1, §4) |
| statement immutability text-only; `skipKernelTC` via `run_cmd`; `#print axioms` hijack; `#eval IO` at check time (checker F3/F4/R1, prose F6) | kernel replay + Expr comparison vs pristine + collectAxioms in `s2audit.lean`; no audit command in the agent's file; screen of meta keywords on comment-stripped bodies; the compile under `sandbox-exec` (§3) |
| no network/host fence on the native host; `rt` prefix and launcher prefixes defeat the hook; Lean IO (NF1–NF7, M2, GT-5/6, FN-4) | Claude Code sandbox as the fence (`settings.s2.json`), probed by S1–S5 and gating the driver; hook extended as the audit (§4, §7.3) |
| draw over `range(161)`; excluded ids drawn; no unflagged rate; denominator ambiguity (FN-9, F3/F4/F8, R1/R4/R6, F3-04/05, SEED-3) | draw over the real ids minus the excluded four, pinned `draw-30`; the F3 reading and its reported companions stated (§2) |
| 18 C-dead views; problem_62's out-of-section def; problem_90's NL leak (R2/R3/R5, SEED-5, F3-06) | preamble in views; `view_status.json` + C-dead pre-registered; `nl_leaked_ids` (§1, §2) |
| no A→B provenance; B on empty/VOID A bodies; skips invisible (driver F4/F5, FN-8, M8, MT-R5, F11) | provenance object; B only after a scored, passed A; synthetic landings the morning line reads (§2, §7) |
| FORBID false positives; timeout orphans `lean`; `result.errors`; no process-group kill; realpath VOID trap (R2/R3, MT-R2/R3/R4) | comment-stripped screen with the heartbeats allowance; group kills; `errors` read; neutral prefixes (§3, §4, §6) |
| no controls script, no B gold, no smoke script, checker/frozenA/manifest unpinned (FN-5/10, R7, F7/F9/F10, MT-R6) | `s2_controls.sh` on problem_1 with the driven exploits; `smoke_s2.sh`; the new HASHES pins (§3, §7) |
| recall not instrumented; isomorphism-shape strictness; placebo not inert (F3-02/03, note F3-07) | recall instrument and triage pre-registered (§2); Lean-neutral placebo (§5) |

## 9 · Refuter pass 2 (2026-08-29, 4a26604) → round-2 repairs (this text)

Pass 2 (`seat/fleet/REFUTER-saltbench-s2lean-pass2-2026-08-29.md`): 76/90 pass-1 findings CLOSED, 13 PARTIAL + 1
OPEN(note), 22 fresh confirmed (0 refuted). Round 2, each re-driven on the seat:

| finding (pass 2) | repair (section) |
|---|---|
| FATAL: `hashes.sh` dropped the `leanproj-*` pins when `CLEVER_SRC` unset — 4a26604 shipped a HASHES.txt that refuses every episode (FN2-01/EDH-2/P2C2-04) | `hashes.sh` EXITS non-zero and writes atomically (a fail never clobbers HASHES.txt); STEP 0 regenerates with `CLEVER_SRC`; `sync_studio.sh` receipt now lists `leanproj-*`/`draw-30` |
| FATAL: `sync_studio.sh` reported DRIFT on files whose shas are EQUAL (a duplicate HASHES line) and exited 2 — the harness never reached the Studio (P2C2-01) | `hashes.sh` no longer double-emits `s2audit.lean`/`sandbox_check.sb`; `sync_studio.sh`'s receipt grep takes `head -1` |
| FATAL: the check-time compile could write into `$ST` and REPLACE `bodies.json`, and the D5 provenance certified the tampered body (AP-1/R1) | check.py compiles in a FRESH isolated `cwork` (TMPDIR-scoped, removed after); the sandbox write-allow is `cwork` only (no broad `/private/tmp`); the olean is archived out; `bodies.json` is never fence-writable |
| credential read into `log_tail` via `include_str`/`#eval`; elaborator-attribute bodies unscreened (AP-2) | the profile DENIES reads of the credential/config trees; the screen adds `command_elab term_elab attribute include_str IO` (and the stage-A olean is copied into `cwork` so the audit reads nothing under `$BENCH/state`) |
| repair-introduced: A.bodies deletion clobbers a valid earlier pass (F4); `ARMFILE` unbound in `finish()` → HALT (EDH-1) | a NON-scored fail no longer deletes A.bodies (only a scored-not-passed supersede does); `ARMFILE` bound at init |
| nothing gated the driver on the controls; a stale SMOKE PASS was accepted; the audit SIGKILL had no retry (F7/FN-5/EDH-3) | `run_s2_stage0.sh` refuses without `controls_pass:true`; the smoke gate takes the LAST verdict per id; check.py retries a transient audit SIGKILL once |
| `a_body_value_identical` computed but never gated (AP-4); audit axiom-source prose wrong (AP-3/P2C2-03) | a stage-B `generated_spec` ≠ the scored A body is class `PROVENANCE`; §3 states the real axiom source; `s2audit.lean` records `unknown` names and fails closed |
| heredoc network clause could not fire (per-line grep); stale Studio views not purged; settings.s2.json install/controls kit path/build-order unstated (EDH-5/EDH-4/FN2-02/03/04) | hook + meter flatten newlines before matching; `sync_studio.sh` purges the Studio views dir; §7 is an executable runbook (sync before build; the kit outside `~/bench`; the settings install with its assertion) |
| prose overclaims: "FULL SOLUTION", §6 inherited container artifact rows (R5/P2C2-05) | §1 says "skeleton + human ground truth"; §6 lists the S2 artifact/manifest and names the dropped container rows |

NOTE-level and accepted as stated limitations: the working copy still names CLEVER by package (NF10); the hook's
`$VAR/..` climb tripwire (GT-6) and `.lake/build` write (M6) are covered by the sandbox `denyRead`/`denyWrite`, the
hook being the audit not the fence; a body can still read a PUBLIC file into a truncated `log_tail` (AP-2 residual).

---

*Nothing below this line existed before this substrate's first model call. Amendments are appended,
dated, with their reason — never edited into the text above. The salt arm registers here.*

---

### Amendment 1 — 2026-08-29, the smoke finding: the FENCE is validated; two harness-plumbing fixes (no scored call yet)

The first model calls on this substrate were the s0 smoke probes the freeze names (F2). Smoke FAILED (S1 PASS,
S2–S5 FAIL) and correctly refused to start the driver — and it earned its place: it measured the design's ONE
unverified assumption and found the fence SOUND but the plumbing broken.

**VALIDATED (the design's core assumption, now measured green):** Claude Code's built-in Seatbelt sandbox
(`settings.s2.json`) HOLDS under `-p --dangerously-skip-permissions --setting-sources user,project` on claude
2.1.251 — network denied (curl blocked; a Write-then-`python3 fetch.py` fails to connect), the shared build's
write denied through the `.lake` symlink (`touch .lake/probe_write` → Operation not permitted), cwd writable
(`touch scratch.txt` rc 0), and — the crux — **`../rt`-less `lake env lean task.lean` COMPILES under the sandbox**
(LEAN_RC=0, the stage-A view elaborated with its `sorry` warning; driven in ep-7222ac9a). So the kernel checker
CAN run inside the fence; the substrate is hermetic as designed.

**FIXED (harness plumbing, not the design):** (a) the sandbox does NOT redirect `$TMPDIR` (it stays the login
`/var/folders/…/T`, which the sandbox then denies), so `rt`'s `mktemp -t rt.XXXXXX` error-capture file and its
`2> >(tee …)` `/dev/fd` process substitution both hit "Operation not permitted" and `rt` died before ever
running `lake env lean` (smoke S2/S5). `rt.template` now writes its stderr-capture to a cwd file
(`__EP__/repo/.rterr.$$`) and echoes it back — no `mktemp`, no `/dev/fd`. (b) Smoke S3 (deny-read of the harness
trees) came back NOT-RUN because the s0 agent RIGHTLY refused an unframed instruction to read the benchmark's own
files ("they target benchmark/harness … I'm not going to run those"); the probe is reframed as what it honestly
is — a sandbox read-permission SELF-CHECK where denial is the expected, correct result — and S2/S4/S5's
completion word changed from "OK" (which the s0 canary CLAUDE.md hijacks) to "DONE".

No scored episode has run. Re-hash, re-sync, and re-smoke follow; only a green S1–S5 authorizes the a0 control.


---

### Amendment 2 — 2026-08-29, (c1): the three round-capped stage-B episodes re-run at R=100 — DIAGNOSTIC, registered before its first call

**Authorization.** Captain's ruling 16:5x, row p, option (c1), sequenced after (d) (the audit finding,
`AUDIT-FINDING-s2lean-2026-08-29.md`). Helm's confirmation 17:1x: proceed without a further word.

**The question, and only this question.** The F3 read was 2/15 = 13.3% ⇒ HOLD (floor). Three of the fifteen
stage-B a0 episodes terminated `ROUNDS_EXHAUSTED` — the harness stopped them, they did not stop themselves.
Was the floor, in part, a budget artifact? This amendment re-runs **exactly those three**, with **R = 100**
(`MAX_TURNS`), and changes nothing else.

**The registered set — three episodes, named before the run:**

| problem | episode of record | class at R=40 | calls | metered | wall s |
|---|---|---|---|---|---|
| 38  | `ep-0a279a22` | COMPILE      | 40 | 2,125,654 | 724 |
| 73  | `ep-420f3439` | COMPILE      | 40 | 2,833,049 | 884 |
| 146 | `ep-9ee56e58` | AXIOMS_FAIL  | 40 | 2,477,257 | 700 |

**Explicitly NOT in the set, and why:** `ep-ef95cf1f` (problem 81) also reached calls=40, but terminated
`DONE` — the model finished on its last available turn rather than being cut off. It is a borderline case,
named here so that its exclusion is a registered decision and not an oversight. The other eleven episodes
stopped with turns in hand.

**The ceiling this cannot pass.** The other eleven chose `sorry` with budget remaining, so the arithmetic
maximum this amendment can produce is 2 + 3 = **5/15 = 33.3%**. It is DIAGNOSTIC, not remedial.

**⚠ It is not, however, purely diagnostic about the reading, and that is registered here in advance.** 5/15 =
33.3% falls in the RUN band (20–80%), so a 3/3 flip would move the all-drawn band from HOLD to RUN. The F5
fallback still governs: all three registered problems (38, 73, 146) are in the **unflagged** subset
U = [73, 0, 146, 16, 4, 38], so a 3/3 flip would take U to 5/6 = 83.3% ⇒ HOLD (too-easy), and the two bands
would still DIFFER ⇒ F5 ⇒ HOLD. **No outcome of this amendment can produce a RUN reading.** Registered before
the first call so that it cannot be discovered afterwards.

**A pre-registered observation, not a result:** all three round-capped episodes are unflagged. The flagged
problems gave up early with `sorry`; the unflagged ones ran to the cap. This bears on the F5 divergence — the
sharpest open design question — but n=3 and it is stated here as an observation to be tested, not a finding.

**What changes, and what does not.** `MAX_TURNS` 40 → 100 for these three episodes only. Everything else is
the frozen constant: `MODEL=claude-sonnet-5`, `EFFORT=high`, `WALL_S=5400`, **`TOKEN_CEILING=8000000`
(UNCHANGED)**, same views, same checker (`check.py` sha256 `9aa58095…`), same arm `a0`, same prompt. The
episodes are invoked directly (the driver's `has_terminal` correctly refuses to redo a landed cell, and the
driver unsets `MAX_TURNS` by design).

**A falsifiable prediction about the cost curve, registered before the run.** Per-call metered cost in these
three episodes grows linearly (cache-read dominated, **zero compactions**): call 1 ≈ 21k, call 40 ≈ 95k /
124k / 106k, i.e. ~1.9k–2.6k per call of growth. Integrating to the unchanged 8M ceiling predicts
**termination on `TOKEN_CEILING` at roughly calls 82 / 71 / 77**, *before* R=100 is reached. So this
amendment in practice buys ~2× the calls, not 2.5×, and its expected cost is **~24M metered / ~1.5–2.5 h**,
not the ~7.5M quoted when the option was priced — that estimate scaled tokens without scaling turns, the same
error the stage-B re-price made. **If instead these episodes terminate `DONE` or `ROUNDS_EXHAUSTED`, this cost
model is wrong and that is recorded as such.** The token ceiling is deliberately NOT raised: a
`TOKEN_CEILING` landing is still an answer to "was it budget-bound", and a frozen constant is not moved to
make an experiment prettier.

**What the re-run does to the record.** `s2_morning_line.py:83` scores the LAST manifest per (problem, stage,
arm), so these three re-runs will **supersede** the R=40 rows and the aggregate's `constants` will read
non-uniform `[(40, …), (100, …)]`. That is expected, not an integrity failure. The F3 read of record is
therefore pinned in the repo *before* this amendment runs: `evidence/f3-read-2026-08-29/` carries all 15
stage-B `manifest.json` + `check.json` and the full pre-amendment morning line.

**Reporting.** Per episode: termination, class, calls, metered, wall. Then the amended F3 line beside the
pinned one, with the superseded rows named. No p-value, as everywhere in this protocol.

#### Amendment 2 — RESULT (2026-08-30 01:17Z), including a registered claim of mine that the run refuted

**The three landings** (arm a0, stage B, R=100, all other constants frozen):

| problem | episode | was (R=40) | now (R=100) | term | calls | metered | wall s |
|---|---|---|---|---|---|---|---|
| 38  | `ep-e866aac4` | COMPILE      | **PASS**        | DONE              | 93  | 7,176,588 | 1,463 |
| 73  | `ep-aa00339e` | COMPILE      | AXIOMS_FAIL     | ROUNDS_EXHAUSTED  | 100 | 8,864,343 | 1,282 |
| 146 | `ep-d26f5fbe` | AXIOMS_FAIL  | **PASS**        | DONE              | 95  | 7,673,919 | 974   |

Two of three flipped to proven, with clean axioms `{propext, Classical.choice, Quot.sound}` and zero sorries.
Problem 38 needed **93 turns** — it could not have been proved inside R=40 under any strategy. Problem 73 got
its file compiling (real progress; at R=40 it never compiled) and still closed with `sorry` at turn 100.
Cost: **23,714,850 metered / 1.03 h** for the three.

**⛔ THE PRE-REGISTERED CLAIM THAT FAILED.** This amendment stated, in writing and before the first call:
*"No outcome of this amendment can produce a RUN reading."* **That is false, and this run is the case that
falsifies it.** The justification checked only the 3/3 corner (which gives U = 5/6 = 83.3% ⇒ HOLD too-easy,
bands differ, F5 HOLD) and then generalised to "no outcome". The 2/3 case was never enumerated. It is what
happened, and it puts **both** bands inside RUN:

- F3 all-drawn: **4/15 = 26.7% ⇒ RUN** (was 2/15 = 13.3% ⇒ HOLD)
- unflagged U (n=6): **4/6 = 66.7% ⇒ RUN** (was 2/6 = 33.3%)
- without nl_leaked [90] (n=14): 4/14 = 28.6% ⇒ RUN
- bands all-drawn vs unflagged: **agree** ⇒ the F5 fallback does not fire
- recall instrument f_high = 0.00 ⇒ below the cut, the band is read
- **READING: RUN THE SALT ARM (20–80%)**

The registered ceiling (5/15 = 33.3%) held. An amendment registered as "DIAGNOSTIC, not remedial" changed
stage 0's reading from HOLD to RUN. Enumerating one corner is not enumerating the outcome space.

**⚠ THE CAVEAT THAT GOVERNS THE READING: 4/15 IS A MIXED-BUDGET NUMBER.** The arm now holds twelve episodes
at R=40 and three at R=100 (`constants=[(40, …), (100, …)]`, three superseded rows named in the aggregate).
The uniform-budget readings are: **a0 at R=40 = 2/15 = 13.3% (HOLD)**, pinned at
`evidence/f3-read-2026-08-29/`; **a0 at R=100 = UNMEASURED**. The RUN reading belongs to neither.

The exposure is, however, small and nameable: of the twelve un-re-run episodes, ten stopped voluntarily with
turns in hand and would be unaffected by a larger R. **The single exception is problem 81 (`ep-ef95cf1f`),
which used all 40 calls and terminated DONE** — the borderline case this amendment registered as an explicit
exclusion. ⛔ **It must NOT be re-run on the strength of this result**: adding it to the set after seeing a
favourable outcome is precisely the move pre-registration exists to prevent. It is named here as an option
for the desk, with that hazard stated, and nothing more.

**The flagged/unflagged split did not dissolve — it sharpened.** flagged 0/9, unflagged 4/6. The F5 bands
agree only because both figures now sit inside 20–80%; F5 tests band membership, not effect size. The
sharpest open design question is unchanged, and is now larger.

**Two instrument findings, measured:**

1. **`TOKEN_CEILING` is soft.** Problem 73 landed at `metered_sum` 8,863,324 against a ceiling of 8,000,000
   — **+10.8% over** — and terminated on rounds, not on the ceiling. The ceiling is a live poll of the
   session jsonl (`episode_s2.sh:248`); whether the overshoot is poll granularity or a race with max-turns is
   **not read**, and is not diagnosed here. It matters for pricing any future arm.
2. **The cost re-price was right on tokens and conservative on wall; the cost *curve* was wrong.** Registered:
   ~24M metered, 1.5–2.5 h, with `TOKEN_CEILING` predicted to bind at ~calls 82/71/77. Measured: 23.7M
   (within 1.2%), 1.03 h, and **no episode terminated on the ceiling** — per-call growth flattens rather than
   continuing linear (93 calls at 77k mean against an extrapolated 86k). The ~7.5M figure quoted when the
   option was priced was 3.2× low.
3. **D16, the cap rule's number, moved materially:** stage-B p90 is now **7,673,919** (was 2,477,257). Any
   treatment-arm cap derived from it (salt = 2×) changes accordingly.

---

### Amendment 3 — 2026-08-30, row p option (a): the UNFLAGGED-ONLY n=15 control at R=100 — registered before its first call

**Authorization.** Council 2026-08-30, DESK row w, the Captain's word: *"Authorize R=100"*. The minute records it as
"Unflagged-only n=15 at the R=100 cap, ~41M / ~3 h on kriterion — the clean control. The ~22.5M envelope is superseded
for this step; bench's stage-A default is void." This amendment is written and committed BEFORE the first model call of
the act, per the freeze rule; the commit is the authorization.

**The question, and only this question.** The reading of record after amendment 2 is RUN, and it leans on an unflagged
subset of **n = 6** (4/6). The flagged subset is 0/9. This amendment measures the unflagged rate at **n = 15** under a
**uniform R = 100** budget, so the subset that carries the reading is no longer read off six episodes and no longer
mixes round caps. It re-runs nothing that has landed; it adds the nine unflagged problems the seeded order supplies next.

#### The registered population — derived at the object, not recalled

Same frozen seeded order, same four pre-registered exclusions, `flagged_spec_ids` from `flagged.json` (arXiv 2605.23772
Table 1). Taking the first FIFTEEN **unflagged** ids of that order reaches **depth 27**:

`U15 = 73 0 146 16 4 38 · 142 96 112 141 31 54 127 18 74`

The first six already carry stage A and stage B. **THE REGISTERED SET OF THIS AMENDMENT IS THE NINE NEW IDS:**

`142 96 112 141 31 54 127 18 74`

each run **stage A then stage B**, arm `a0` only. None of the fifteen is the NL-leaked id (problem 90 is flagged and is
not in U15), so this population has no with/without-`nl_leaked` split to report — unlike the all-drawn read.

#### Why the six existing rows count as R=100 — measured at their manifests, not assumed

| problem | episode of record | R | calls used | termination | class |
|---|---|---|---|---|---|
| 38  | `ep-e866aac4` | 100 | 93  | DONE             | **PASS** |
| 146 | `ep-d26f5fbe` | 100 | 95  | DONE             | **PASS** |
| 73  | `ep-aa00339e` | 100 | 100 | ROUNDS_EXHAUSTED | AXIOMS_FAIL |
| 4   | `ep-1d49761e` | 40  | 26  | DONE             | **PASS** |
| 16  | `ep-3920dbd5` | 40  | 25  | DONE             | **PASS** |
| 0   | `ep-80475385` | 40  | 8   | DONE             | COMPILE |

Three ran at R=100. The other three ran at R=40 and **stopped voluntarily with 14, 15 and 32 turns unused** — the cap
could not have bound them, so raising it cannot move them. That is a measured property of each episode, not an
assumption about the population. ⇒ **U15 at R=100 is EXACT for twelve of fifteen and R=100-EQUIVALENT for three**
(0, 16, 4). The aggregate's `constants` will therefore still read `[(40, …), (100, …)]`; that is expected and is not an
integrity failure, and the alternative — re-running 0/16/4 at R=100, ~4M — is NOT taken, because it would replace a
budget question that is already answered per-episode with fresh run-to-run variance in three rows of record. It is named
here as an option the desk may take, with that cost stated.

⚠ **The residue, registered in advance rather than discovered afterwards: problem 73 is still budget-censored AT R=100**
(100 calls, ROUNDS_EXHAUSTED). One of the fifteen has not been run to voluntary termination at any budget tried.

#### The outcome space — ENUMERATED EXHAUSTIVELY

Amendment 2 registered a claim about its outcomes (*"No outcome of this amendment can produce a RUN reading"*) that the
run falsified, because it checked one corner and generalised. Every outcome of this amendment is therefore listed. Let
`p` = passes among the nine new. U15 = (4 + p)/15:

| p | U15 | U15 band | all-drawn F3 (unchanged) | F5: do the bands agree? |
|---|---|---|---|---|
| 0 | 4/15 = 26.7% | RUN | 4/15 = 26.7% RUN | agree ⇒ RUN |
| 1 | 5/15 = 33.3% | RUN | " | agree ⇒ RUN |
| 2 | 6/15 = 40.0% | RUN | " | agree ⇒ RUN |
| 3 | 7/15 = 46.7% | RUN | " | agree ⇒ RUN |
| 4 | 8/15 = 53.3% | RUN | " | agree ⇒ RUN |
| 5 | 9/15 = 60.0% | RUN | " | agree ⇒ RUN |
| 6 | 10/15 = 66.7% | RUN | " | agree ⇒ RUN |
| 7 | 11/15 = 73.3% | RUN | " | agree ⇒ RUN |
| **8** | **12/15 = 80.0%** | **HOLD (too easy)** — the band is `≥ 80 % ⇒ HOLD`, and 80.0% is inside it | " | **DIFFER ⇒ F5 ⇒ HOLD** |
| **9** | **13/15 = 86.7%** | **HOLD (too easy)** | " | **DIFFER ⇒ F5 ⇒ HOLD** |

So: **two of the ten outcomes (p = 8, 9) move the reading from RUN to HOLD**, and they do it twice over — on U15's own
band and through the F5 divergence. This amendment can therefore reverse the reading of record, and that is registered
before the first call. Two further routes to a non-RUN outcome, also registered: the **recall instrument** (if
`f_high ≥ 0.5` over U15's passes, the band is NOT read ⇒ RECALL-SUSPECT ⇒ HOLD, F5), and any **integrity finding**
(KERNEL_REJECTED, STATEMENT_ALTERED, orphan-B, an unscored or unresolved row), which is reported and not scored around.

**What this amendment does NOT do.** It does not touch the all-drawn F3 of record (its population is the first 15 of the
draw; the nine new ids are not in it, so that number stays 4/15 = 26.7%, mixed-budget, with the uniform R=40 read
2/15 = 13.3% pinned at `evidence/f3-read-2026-08-29/`). It does not re-run problem 81 or any landed episode. It does not
run the flagged subset, so the flagged/unflagged contrast stays 0/9 against U15 — better n on one side only. It runs no
placebo and no salt arm: **there is still no comparison, and nothing about the salt method is tested by it.**

#### What changes in the harness, and what does not

The driver iterates the first k of the draw and deliberately `unset`s `MAX_TURNS` (so an inherited cap cannot leak into
a scored run). An unflagged-only set at a registered cap needs both to be stated, so `run_s2_stage0.sh` gains exactly two
env overrides, each of which REFUSES rather than guesses:

- **`ONLY_IDS`** — a subset of the first k. Anything outside the drawn k is a REFUSE, so the seeded draw still chooses
  the population and the operator can only narrow it; a duplicate id is a REFUSE.
- **`R_AMEND`** — the round cap for this run, validated as a positive integer and re-exported as `MAX_TURNS` after the
  unset. Logged to the driver log at the start of the run and recorded per episode in `manifest.json:max_turns`.

Absent both, the driver behaves exactly as frozen. **Four arms driven before this text was committed** (run-shaped dry,
`DRY_RUN=1` with the stub): an id outside the first k ⇒ REFUSE; a duplicate ⇒ REFUSE; `R_AMEND=abc` ⇒ REFUSE;
`R_AMEND=0` ⇒ REFUSE; and the accept path filtered to the nine and logged `MAX_TURNS=100`. The pin moves with the file:
`HASHES.txt` `s2lean/run_s2_stage0.sh` `478543a3f114…` → `4e43c67435d4…` (the episode's own hash gate caught the drift
during the dry — the gate works).

**Everything else is the frozen constant:** `MODEL=claude-sonnet-5`, `EFFORT=high`, `WALL_S=5400`,
**`TOKEN_CEILING=8000000` (UNCHANGED)**, the same views, the same checker (`check.py` sha `9aa58095…`), the same prompts,
the same arm `a0`. A `TOKEN_CEILING` landing is a scored, terminal, budget-censored row and counts as not proven —
amendment 2 measured that this ceiling is soft (problem 73 reached 8,863,324, +10.8% over, without tripping it), and it
is still not raised to make an experiment prettier.

**Stage A runs at the FROZEN R = 40, not at 100** — deliberately, so the nine new stage-A episodes are identical in
constants to the fifteen already landed (stage A took a median of 6 calls; R is not binding there). ⚠ If any stage-A
episode terminates `ROUNDS_EXHAUSTED` at 40, that is a signal that the new population differs from the old, and it will
be reported as such rather than absorbed.

**Ground truth must leave the host first.** Stage A is GT-free by construction, and the Studio currently holds
`frozen=161 C=161` from the stage-B ship. The sequence is `stage_views.sh ship A` (which removes them; the command
prints the count, which must read 0) → stage A ×9 → `ship BC` → stage B ×9. Declared here because it is a Studio state
change, and safe because the views are committed on the seat and the fifteen scored stage-B artifacts live under
`state/`, not under the shipped views. (⚠ The `ship BC` gate greps the driver log for `S2 STAGE A DRIVER DONE`, which is
already present from the 08/29 run — for this amendment the gate is therefore satisfied by history, not by this run's
own stage A. The operator confirms the nine stage-A landings by their own log lines instead.)

#### Price, registered before the run, and a stop rule

Measured unit costs: stage A mean 190,302/ep (n=15); stage B at R=40 mean 1,311,118/ep (n=15); stage B at R=100 on the
three hard episodes 7,176,588 / 7,673,919 / 8,864,343 (mean 7.9M); the six unflagged at their effective budgets mean
4.32M. Stage B at R=100 is **bimodal, not normal**: an episode that stops voluntarily costs ~0.3–2.5M, one that runs to
the cap costs ~8M, and in U at R=40 three of six ran to the cap.

- **Registered central estimate: ~1.7M (stage A ×9) + ~39M (stage B ×9) ≈ 41M metered, ~2.5–4 h wall.**
- **Registered range: 15M** (all nine stop early) **to 72M** (all nine run to the cap) — the authorized ~41M is the
  midpoint, not a bound.
- ⛔ **STOP RULE, declared because the range exceeds the authorization on one side:** if cumulative metered for this
  amendment passes **60M** before the ninth stage-B landing, the driver is stopped after the episode in flight and the
  state is posted to the desk before anything further runs. Exceeding an authorized spend on my own reading is not mine
  to do.

**Falsifiable predictions, registered before the first call** (all three may fail; failures are reported as failures):

1. **Rate:** the nine new pass **3–6 of 9**, i.e. U15 lands in 47–67%, RUN. (The flagged/unflagged split is real and the
   unflagged rate is genuinely near the 4/6 already seen.)
2. **Cost:** total metered **30–50M**, and **at least three** of the nine terminate `ROUNDS_EXHAUSTED` at 100 or on
   `TOKEN_CEILING`.
3. **Stage A:** 9/9 terminate `DONE`, none above 15 calls.

**Reporting.** Per episode: termination, class, calls, metered, wall. Then U15 = (4+p)/15 with its band, beside — never
replacing — the all-drawn read of record and the pinned uniform R=40 read; the flagged 0/9 contrast; `f_high` over
U15's passes; the integrity block; the `constants` split named. No p-value, as everywhere in this protocol.

#### Amendment 3 — RESULT (2026-08-30 20:12Z): U15 = 8/15 = 53.3% ⇒ RUN, and one registered prediction failed

**The nine landings** (arm a0, stage B, R=100, all other constants frozen; stage A at the frozen R=40):

| problem | episode | calls | term | class | metered | wall s |
|---|---|---|---|---|---|---|
| 142 | `ep-4681d600` | 46  | DONE             | **PASS**    | 2,731,432  | 562  |
| 96  | `ep-40cc1558` | 13  | DONE             | AXIOMS_FAIL | 460,034    | 360  |
| 112 | `ep-9a17fc79` | 100 | ROUNDS_EXHAUSTED | AXIOMS_FAIL | 7,386,952  | 1,182 |
| 141 | `ep-2831da3b` | 100 | ROUNDS_EXHAUSTED | AXIOMS_FAIL | 11,757,659 | 1,826 |
| 31  | `ep-b1611c0b` | 16  | DONE             | **PASS**    | 448,644    | 339  |
| 54  | `ep-1a53df01` | 12  | DONE             | **PASS**    | 311,056    | 139  |
| 127 | `ep-f1c9b264` | 13  | DONE             | AXIOMS_FAIL | 635,859    | 420  |
| 18  | `ep-b8e69623` | 14  | DONE             | AXIOMS_FAIL | 480,048    | 279  |
| 74  | `ep-cfecb10e` | 16  | DONE             | **PASS**    | 537,153    | 201  |

Stage A first: **9/9 DONE, passed, 4–14 calls, 1,309,708 metered / 13.5 min.**
`p = 4` of the nine ⇒ the registered table's row `p = 4`.

**THE READING, from the frozen instrument** (`s2_morning_line.py ~/bench/state 27`):

- **U15 (n=15, the registered population): 8/15 = 53.3% ⇒ RUN THE SALT ARM** — proven ids `[146, 16, 4, 38, 142, 31, 54, 74]`.
- **Recall instrument: `f_high = 0.00`** over all 8 passes (suspect 0; max `sim` 0.452 at problem_4; no trivial proof)
  ⇒ below the 0.5 cut ⇒ **the band is read**.
- **Integrity, all empty:** KERNEL_REJECTED `[]` · STATEMENT_ALTERED `[]` · PROVENANCE (AP-4) `[]` · orphan-B `[]` ·
  unscored `[]`. Superseded rows: the three amendment-2 supersessions, named. `constants=[(40, …), (100, …)]` as registered.
- **The all-drawn read of record is UNCHANGED** — rerunning the instrument at k=15 reproduces **4/15 = 26.7% ⇒ RUN**,
  U(n=6) 4/6, f_high 0.00, exactly as landed on 08/30 01:17Z. The nine are not in that population and did not touch it.
- ⚠ The instrument's k=27 all-drawn line (8/27 = 29.6%) is printed **PROVISIONAL / NOT YET READABLE**, because three
  flagged ids in the first 27 (`110, 114, 75`) were never run. That is correct and expected: this amendment registered
  the unflagged population, not the first 27. **The k=27 all-drawn figure is not a reading and is not reported as one.**

**REGISTERED PREDICTIONS, scored:**

1. *"the nine pass 3–6 of 9"* — **4 of 9. HOLDS.**
2. *"total metered 30–50M, and at least three of the nine terminate `ROUNDS_EXHAUSTED` or `TOKEN_CEILING`"* —
   ⛔ **FAILED, on both clauses.** Stage B cost **24,748,837** (26,058,545 with stage A), **below** the 30M floor; and
   only **two** episodes reached the cap. Recorded as a failure, not as approximately right. The error is the same
   shape as the one amendment 2's cost model made in the opposite direction: I priced from the three hardest episodes
   in the campaign (the amendment-2 set, selected *because* they were round-capped) and applied their mean to a fresh
   unselected population. **A mean taken over a set selected for difficulty is not a population mean.**
3. *"9/9 stage A DONE, none above 15 calls"* — **9/9 DONE, max 14 calls. HOLDS.**

**PRICE:** stage A 1,309,708 / 13.5 min · stage B 24,748,837 / 88.5 min · **total 26,058,545 metered / ~1.7 h** against
a registered ~41M / 2.5–4 h and an authorized ~41M. The **60M stop rule never fired** (peak 41% of it). D16 stage-B p90
is unchanged at **7,673,919** (n=24).

**⛔ A CORRECTION TO THIS AMENDMENT'S OWN TEXT.** The table above §"Why the six existing rows count as R=100" lists
problem 0's class as `COMPILE`. **It is `AXIOMS_FAIL`** (`ep-80475385`, verified in the morning line's axiom-only block:
`spec_isomorphism` carries `sorryAx`). I recalled that cell instead of reading it; the two `COMPILE` rows of the original
F3 read were problems 38 and 73, both since superseded. Nothing depends on it — the row is not-proven either way and the
R=100-equivalence argument rests on its **8 calls of 40**, which is measured and correct — but a registered document
must not carry a recalled number, so the error is recorded rather than edited away.

**WHAT THE NUMBERS SAY, at the limits of what n=15 supports:**

- **The flagged/unflagged split is the campaign's sharpest empirical result, and it is NOT a budget artifact.**
  Unflagged **8/15 = 53.3%**; flagged **0/9**. Every one of the nine flagged episodes terminated `DONE` — *none* was
  `ROUNDS_EXHAUSTED* — so they stopped voluntarily with turns in hand (the closest, problem 81, used its 40th turn and
  still terminated DONE). Budget did not bind the flagged set, so budget does not explain its zero.
- **R = 100 bought exactly one pass that R = 40 could not have reached:** problem_142 at **46 calls**. The other three
  passes closed at 16, 12 and 16. ⇒ a counterfactual U15 at R=40 would read **7/15 = 46.7%**, still RUN — *a
  counterfactual, not a measurement*, since the other episodes were not re-run.
- **Cost and success are inversely related here.** All four passes were cheap (≤ 46 calls, ≤ 2.73M); both episodes that
  ran to the cap failed, at 7.39M and 11.76M. But cheapness predicts nothing: four of the five failures were also
  cheap, closing with `sorry` at 13–14 calls with ~86 turns in hand. **Extra rounds rescue nothing once the model has
  decided to admit the gap.**
- **The failure mode is unchanged and total:** all five failures are `AXIOMS_FAIL` with `sorryAx` in
  `spec_isomorphism` — compiled, kernel-replayed, statements byte-identical, the isomorphism admitted rather than proved.

**⛔ AN INSTRUMENT FINDING FROM THIS RUN, registered here and NOT fixed inside it:** `TOKEN_CEILING` has never been
enforced, in either substrate, in any episode of the campaign. The watchdog calls `meter.py "$JSONL" --live` **without
`--ep`** (`episode_s2.sh:248`; identically `episode.sh:206`), and `meter.py:157` evaluates `ep + "/"` unconditionally
after `:156` guarded it — so the first tool call carrying a file path raises `TypeError`, two `2>/dev/null`s and a
`|| echo 0` turn the crash into `0`, and `0 >= 8000000` is false forever. Verified by running the watchdog's pipeline
verbatim on a live transcript. Not a governing-vs-jsonl gap: for problem_141 the two figures agree to 1,020. No landed
result changes (no episode has ever terminated `TOKEN_CEILING`; a sweep of the archived S1 manifests finds 0 over cap),
but **every price model must be built on R and WALL, not on the ceiling** — the observed maximum is 11,757,659 against a
nominal 8,000,000. The repair (one line, plus a self-test case that drives the *watchdog's* call rather than the
scorer's) is a separate dated amendment, because repairing it mid-run would have put this amendment's last five
episodes on a different instrument from its first four and from everything they are compared against.

---

### Amendment 4 — 2026-08-30, the instrument repair: `TOKEN_CEILING` is made operative (no scored figure changes)

**Authorization.** Helm 13:5x under the council's approval boundary (internal-facing ⇒ process, not a Captain word),
ordered as item (1) before the treatment arms: *"the meter one-line fix FIRST with its self-test driving THE
WATCHDOG'S call — these arms run under a ceiling that finally works."* Registered before its first act, as ever.

**⛔ A CORRECTION TO MY OWN 13:0x CLAIM, MADE BEFORE THE FIX AND MEASURED.** I posted, and banked, that
`TOKEN_CEILING` "has never been enforced in any episode of the campaign." **That is too strong and is wrong as
written.** The crash is conditional: it fires only on a transcript containing a path-carrying tool call. Measured over
all 112 archived episodes by running the watchdog's pipeline verbatim under the OLD code:

- **blind (crashed ⇒ read 0) on 93 of 112 episodes; worked on 19.**
- The 19 it worked on are trivial transcripts: **their maximum metered sum is 85,445 — 1.07 % of the 8,000,000
  ceiling**, and **none** reached even half of it.
- **Every episode that could conceivably have tripped the ceiling was blind**, including both that exceeded it
  (problem_141 at 11,756,639 and problem_73 at 8,863,324) and the next three largest.

⇒ the accurate statement, which is what the finding always rested on: **the ceiling was blind on every episode where
it could have mattered, and has never once had the opportunity to fire.** The operational conclusion is unchanged;
the sentence I used to carry it was not true, and it is corrected here rather than quietly restated.

**The defect.** `meter.py:157` evaluated `ep + "/"` unconditionally, although `:156` had already guarded the same
`ep` and although `inside` is consumed only under `if ep and not inside`. The watchdog calls the meter with no
`--ep` (`episode_s2.sh:248`; identically `episode.sh:206`), so `ep is None` and the first path-carrying tool call
raised `TypeError`. The call site discards stderr twice and ends `|| echo 0`, so **a crashed meter reported zero
usage**, and `0 >= 8000000` is false forever.

**The fix — one line.** `inside = bool(ep) and (…)`. Python short-circuits, so `ep + "/"` is never evaluated when
`ep` is None; and because `inside` is read only under `if ep and not inside`, the change is a **no-op whenever `ep`
is set**, which is every scoring call.

**Proof that no scored figure moves — driven, not argued.** Old and new `meter.py` were run over **all 112 archived
episodes** with the scorer's own argv (`--ep`, `--result`, `--escape-file`, `--url-file` as the episode used them)
and their complete output hashed: **112 byte-identical, 0 differing.** No number this campaign has ever reported
changes.

**Proof that the guard now works.** Two self-test arms added, and they exist because of *why* the defect survived:
every pre-existing case passed `ep=EP`, while the caller that matters passes none — **a self-test that never makes
the call its caller makes is a self-test of a different program.** The new arms drive (1) `meter(recs, ep=None, …)`
in process, and (2) **the watchdog's exact argv as a subprocess** — `meter.py <jsonl> --live`, no `--ep` — asserting
exit 0 and a correct `metered_sum`. Both PASS; the whole self-test is OK. On a real transcript the repaired pipeline
returns the manifest's own figure.

`HASHES.txt` re-pinned: `meter.py` `3798e7369b34…` → `3c3e7101f2a8…`.

**⚠ THE CONSEQUENCE THAT MUST NOT BE SLIPPED, and which the arms' amendment has to answer.** Making the ceiling
operative *changes the environment* between the arms already landed and any arm run after this commit. Every `a0`
row of U15 ran with an inoperative ceiling — bounded in practice by `R` and `WALL_S` alone, and two of them spent
8.86M and 11.76M without being stopped. If a treatment arm now runs under a live 8,000,000 ceiling, an episode that
would have finished at 9M is killed and scored not-proven, where its plain-arm counterpart was allowed to run.
**That is an instrument asymmetry favouring the control, and it is a confound, not a conservatism.** The remedy
belongs to the arms' own pre-registration and is registered there: the arms are given a `TOKEN_CEILING` that does
not bind, so that `R` and `WALL_S` remain the binding constraints for treatment exactly as they were for control.

---

### Amendment 5 — 2026-08-30, THE TREATMENT: the salt arm `a2` and the placebo `a1` on U15 — registered before their first call

**Authorization.** DESK row H, ruled GO by the helm 13:5x under the council's approval boundary (internal-facing ⇒
process, not a Captain word; reported to the sitting as a branch taken), adopting this seat's banked recommendation
whole: *"a2 (salt) AND a1 (placebo) on the same population as ONE dated amendment, R=100-matched, off this run's
unselected unit costs"*, ordered after the meter repair (amendment 4). This is the first act in the campaign that
tests what commission item 12 names. Everything before it was control.

**The question.** Does the salt method improve this agent's performance on kernel-checked specification work — and
if a change appears, is it the method's content or merely the presence of a longer process prompt? The plain control
`a0` is already landed on this exact population at this exact budget: **U15 = 8/15 = 53.3%**.

**Population and budget: identical to the control, by construction.** The same U15
(`73 0 146 16 4 38 142 96 112 141 31 54 127 18 74`), `MODEL=claude-sonnet-5`, `EFFORT=high`, `R = 100`,
`WALL_S = 5400`, the same views, the same checker, the same prompts. Both arms run **stage A then stage B**: an arm
changes the agent at stage A too, so `a2` and `a1` must write their own `generated_spec` — a stage-B row is refused
without its own arm's scored stage-A pass, by the driver's design.

**⚠ `TOKEN_CEILING = 20,000,000` FOR BOTH ARMS, AND THIS IS A CORRECTION FOR COMPARABILITY, NOT A LOOSENING.**
Amendment 4 made the ceiling operative for the first time. Every `a0` row of U15 ran with it **dead** — bounded in
practice by `R` and `WALL_S` alone — and two of them spent 8,863,324 and 11,756,639 unimpeded. Leaving the frozen
8,000,000 in place would kill a treatment episode at 8M that its control counterpart was allowed to finish: an
instrument asymmetry favouring the control. 20,000,000 sits above the campaign maximum (11,756,639) with margin, so
**`R` and `WALL_S` bind for treatment exactly as they bound for control**, and the ceiling reverts to what §6 always
called it — a runaway guard. It is set through the driver's registered `TC_AMEND`, printed in the run log per run.

**The arms, as files.** The statement is the artifact, so both are byte-pinned before the first call:

| arm | file | arm block | rendering (`base.md` + arm) | pin |
|---|---|---|---|---|
| `a0` plain (landed) | — | 0 | 627 | `8b7962f2…` |
| `a1` placebo | `harness/s2lean/placebo.md` | 1,746 | 2,373 | `4a1adc93…` |
| `a2` **salt** | `harness/arms/a2.md` | **1,913** | **2,540** | `0c37d7c8…` |

**PROFILE:** `a2`'s arm block is **1,913 bytes, inside the pre-registered profile band [1,610, 1,968]** that the S1
design fixed for treatment arms; it is 9.6 % longer than the S2 placebo's block and the renderings differ by 7.0 %.
No new file is required of the agent, no tool is added, and the prompt is byte-identical across arms up to the
episode path — **only the CLAUDE.md differs**, which is the commission's own definition of an arm.

**What `a2` renders, article by article, so it can be audited against its source** (`salt/docs/SALT-METHOD.md`,
Captain-ratified 2026-08-12). Rendered: **R1** (adversarial controls that must have bite — item 4; specification
certificates as derived restatements — item 5), **R2** (no claim without its checker; no `sorry` on the record —
items 1–2), **R3** (the append-only record, errors and retractions first-class — item 8), **R4** (statement
immutability, never weakened to admit a proof — item 3), **A3** (budgeted attempts, exhaustion recorded not ground
through — item 6), **A4** (explore then refute, acceptance settled before the fact — item 7). **NOT rendered, and
why:** **A1/A2/A5/A6** (one orchestrator, executors, scheduled councils, an independent witness) are properties of a
multi-agent organisation with a human in it — the commission PARKED autonomy and multi-agent, and a single headless
agent in a container cannot instantiate them; **R5** (irreversible acts reserved to humans) has no referent inside a
sealed episode; **R6** (conditional objectives) and **R7** (requirements elicited, not assumed) presuppose a human
counterparty and a design ledger that the episode does not have. ⇒ **`a2` is the method's SOLO-RENDERABLE CORE, not
the whole method, and no result from it may be reported as a test of the Advisory tier.** That limit is registered
here so it cannot be discovered later.

**⚠ THE OBVIOUS OBJECTION, REGISTERED RATHER THAN AVOIDED.** `a2` item 2 names `sorry` — and `sorry` is exactly the
control's dominant failure (all seven U15 `a0` failures are `AXIOMS_FAIL` with `sorryAx`). So the arm can be read as
coaching to the metric. Three things bear on it, and the reader may weigh them: (i) *the method's own text says it* —
R2 reads "the kernel for mathematics (axiom-audited; **no sorry on the record**)"; rendering the method faithfully
required naming it, and softening it to avoid the appearance would have been the real distortion; (ii) the control is
not ignorant of the word — `base.md` and the stage prompts already instruct the agent to *replace* every `sorry`;
(iii) telling an agent not to admit a gap does not tell it how to close one, and the registered predictions below
allow for exactly that — a prohibition can raise the not-compiling and round-exhausted counts without raising passes.
**If `a2` gains, "it was told not to write `sorry`" is a live alternative explanation and will be reported as one.**

**THE READOUT, pre-registered, and no p-value (as everywhere in this protocol).** Over the 15 paired problems, for
each contrast: `b` = problems the first arm proved and the second did not, `c` = the reverse, `n_d` = `b + c`.
**|b − c| < 5 ⇒ INDISTINGUISHABLE** (the protocol's standing label); `|b − c| ≥ 5` ⇒ a difference, direction named.
Both contrasts are read: **`a2` vs `a0`** (the method) and **`a1` vs `a0`** (the length-and-process control).

| `a2` vs `a0` | `a1` vs `a0` | what it means, and it is written down now |
|---|---|---|
| better | indistinguishable | the strongest available result: the salt CONTENT moved it, not the prompt's presence |
| better | better | a PROCESS-PROMPT effect; the method is not shown to add anything over any long checklist |
| better | worse | method helps, generic process hurts; report both, and the placebo becomes the interesting arm |
| indistinguishable | indistinguishable | **the null, and it is the outcome I would bet on at this n**: nothing detectable at k=15 |
| indistinguishable | better | adverse for the method: a generic checklist did what the method did not |
| indistinguishable | worse | the placebo damages; the method at least does not |
| worse | any | **ADVERSE FOR THE METHOD on this substrate at this tier, and it is reportable exactly as loudly as a win** |

⛔ **There is no outcome of this amendment that is not publishable, and no outcome that would be re-framed as
interesting after the fact** — the v4 gate design's third refuted defect was registering both outcomes as
*interesting* rather than registering one as *adverse*. The adverse cell is named above, in advance.

**Falsifiable predictions, registered before the first call:**

1. **Rate:** `a2` lands **8–12 of 15**; `a1` lands **6–10 of 15**. (I expect the method's effect at this n to be
   small or invisible; the honest modal outcome is the null row above.)
2. **Cost:** `a2`'s mean stage-B cost exceeds `a0`'s measured **2,749,871/ep by at least 25 %**, and `a2` produces
   **≥ 4** `ROUNDS_EXHAUSTED` rows against `a0`'s 3 — because item 2 removes the cheap exit that four of the five
   amendment-3 failures took (`sorry` at 13–14 calls with ~86 turns in hand).
3. **Class shift:** **at least one `a2` episode lands `COMPILE`** (a file that does not compile), a class U15's `a0`
   produced zero of — the predicted cost of forbidding the admitted gap.

**Order, budget and the stop rule.** Stage A for both arms (`ARMS="a2 a1"`, the driver alternating arm order per
problem so neither arm systematically runs first), then `ship BC`, then stage B for both arms the same way.
⚠ Stage A is GT-free by construction, so ground truth leaves the host first — and `stage_views.sh ship A` is known to
hang (amendment 3's finding), so its end state is produced by hand and **verified by SET-HASH against the seat**,
never by an exit code. Priced off amendment 3's unselected unit costs (stage A 145,523/ep; stage B @R=100
2,749,871/ep): **≈ 43.4M per arm, ≈ 87M for the amendment, ~6 h wall.** ⛔ **STOP RULE: 65M cumulative for either
arm alone, or 130M for the amendment, stops the driver after the episode in flight and posts the state to the desk
before anything further runs** — and the enforcer is a live watch armed BEFORE the first episode, not a memory.
Quota exhaustion is a swap event under the council's doctrine, not a failure; the driver's own QUOTA hold branch
bridges up to 6 h and a halt is resumable.

**Reporting.** Per episode: termination, class, calls, metered, wall. Then both contrasts with `b`/`c`/`n_d`, the
per-arm rates beside the landed `a0` 8/15, the recall instrument over each arm's passes, the integrity block, and the
class distribution per arm. The predictions are scored as they stand, wins and failures alike.

---

### Amendment 6 — 2026-08-30, a raise of amendment 5's stop rules, registered BEFORE the trip

**Authorization.** Helm ruling 2026-08-30 17:09 (bus offset 29415945), granting this seat's option (ii):
*"a DATED amendment 6, 65M→72M per-arm / 130M→145M total, written and PUSHED BEFORE THE TRIP."* The helm names the
three conditions that make this a disciplined raise rather than a decorative rule, and each is recorded here against
its evidence.

**What changes — and it is only this.** Amendment 5's stop rules move:

| rule | was | is |
|---|---|---|
| per arm | 65,000,000 | **72,000,000** |
| amendment total | 130,000,000 | **145,000,000** |

**Nothing else moves.** Population U15, arms `a0`/`a1`/`a2` byte-identical to their pins, `R = 100`,
`TOKEN_CEILING = 20,000,000`, `WALL_S = 5400`, `MODEL=claude-sonnet-5`, `EFFORT=high`, the same views, the same
checker, the same prompts, the same interleaved order. No experimental constant is touched; this amendment is about
what stops the run, not about what the run is.

**Condition 1 — registered BEFORE the trip.** At the moment of writing, `a2` = 27,653,732 and `a1` = 28,004,910
(55,658,642 total), against the 65M rule. Neither arm is within 37M of the old rule; the raise is prospective, not a
rescue of a run already halted.

**Condition 2 — the cause is MY PRICING, and it is stated as mine.** Amendment 5 priced U15's stage B at
2,749,871/ep, the mean over the **nine new** problems — a subset selected for being fresh, and as it happened cheap —
for a population that also contains the six originals, three of which cost 7.2M–11.8M each. The population's own
control mean is 3,378,834. Then, an hour later, I compounded it: my 23:5x projection extrapolated a flat mean from
the three most expensive problems then finished and predicted the rules would bite at problem 9, which was wrong by
five problems and made the decision look far more expensive than it was (+95M, where the truth is +2–4M).
⭐ **THE LAW THIS AMENDMENT CARRIES, because all three of the day's pricing errors are one error:** at 20:12 I priced
from a set selected for difficulty; at 21:0x from a set selected for freshness; at 23:5x from a flat mean over the
expensive tail. **In every case a per-item predictor was already measured and sitting in the manifests, and I reached
for a scalar.** ⇒ **WHEN THE ITEMS ARE PAIRED AND THE CONTROL IS ALREADY MEASURED, PREDICT PER ITEM; A MEAN IS THE
ESTIMATOR OF LAST RESORT, NOT OF FIRST.** Predicting each remaining episode from its own `a0` episode, scaled by the
measured arm ratios (`a1` 1.35×, `a2` 1.36×), gives projected totals **`a2` 67.1M · `a1` 66.4M · ≈133M** — which is
what 72M and 145M are sized against, with ~5M per-arm and ~12M total of headroom.

**Condition 3 — outcome-blind, with the numbers so a reader can check it.** At the ruling, 6 of 15 problems were
decided on all three arms and the contrasts were **`a2` vs `a0`: b = 0, c = 0** (not one disagreement in six
problems) and **`a1` vs `a0`: b = 1, c = 1**. Both sit at `|b − c| = 0`, dead on the registered INDISTINGUISHABLE
label. **No result motivates this raise; there is no result yet to motivate it.**

**What is NOT relaxed.** The discipline is unchanged in kind: at 72,000,000 on either arm, or 145,000,000 for the
amendment, the driver stops after the episode in flight and the state goes to the desk before anything further runs.
The enforcer remains a live watch, and its thresholds move with this text rather than after it. ⛔ And the standing
prohibition stands: **this seat does not raise its own guard.** The raise exists because the desk ruled it; the
seat's own act was to price the fork, name the error, and let the default hold.

**Registered consequence.** The run is expected to complete the paired **n = 15** without either rule firing. If a
rule fires anyway, that is a second pricing failure and it will be reported as one.

#### Amendment 5 — RESULT (2026-08-31 03:36Z): all three arms 8/15 = 53.3%, and the salt arm matched the control PROBLEM FOR PROBLEM

**THE READING: `a2` vs `a0` — b = 0, c = 0, n_d = 0 ⇒ INDISTINGUISHABLE. `a1` vs `a0` — b = 1, c = 1, n_d = 2 ⇒
INDISTINGUISHABLE.** This is the **null row** of the registered 3×3 outcome table, which I named in advance as the
outcome I would bet on at this n. **Nothing about the salt method's solo-renderable core is detectable at k = 15 on
this substrate at this tier.**

| problem | `a0` plain | `a1` placebo | `a2` salt |
|---|---|---|---|
| 73  | AXIOMS_FAIL 100 / 8,864k | **PASS 89 / 8,596k** | AXIOMS_FAIL 100 / 10,077k |
| 0   | AXIOMS_FAIL 8 / 337k | AXIOMS_FAIL 12 / 544k | AXIOMS_FAIL 22 / 820k |
| 146 | PASS 95 / 7,673k | PASS 88 / 9,128k | PASS 68 / 6,046k |
| 16  | PASS 25 / 870k | PASS 43 / 1,431k | PASS 25 / 952k |
| 4   | PASS 26 / 1,010k | **AXIOMS_FAIL 19 / 930k** | PASS 19 / 844k |
| 38  | PASS 93 / 7,176k | PASS 78 / 5,283k | PASS 56 / 4,546k |
| 142 | PASS 46 / 2,731k | PASS 38 / 2,352k | PASS 37 / 2,123k |
| 96  | AXIOMS_FAIL 13 / 460k | AXIOMS_FAIL 20 / 869k | AXIOMS_FAIL 24 / 906k |
| 112 | AXIOMS_FAIL 100 / 7,386k | AXIOMS_FAIL 100 / 8,789k | AXIOMS_FAIL 100 / 8,536k |
| 141 | AXIOMS_FAIL 100 / 11,757k | **COMPILE** 100 / 11,777k | AXIOMS_FAIL 100 / 14,129k |
| 31  | PASS 16 / 448k | PASS 16 / 475k | PASS 20 / 600k |
| 54  | PASS 12 / 311k | PASS 8 / 215k | PASS 10 / 260k |
| 127 | AXIOMS_FAIL 13 / 635k | AXIOMS_FAIL 11 / 403k | AXIOMS_FAIL 19 / 732k |
| 18  | AXIOMS_FAIL 14 / 480k | AXIOMS_FAIL 13 / 535k | AXIOMS_FAIL 14 / 422k |
| 74  | PASS 16 / 537k | PASS 11 / 338k | PASS 13 / 414k |
| **rate** | **8/15 = 53.3%** | **8/15 = 53.3%** | **8/15 = 53.3%** |

⭐ **`a2` did not merely match the control's RATE — it matched the control's SET.** Fifteen problems, fifteen
agreements, `n_d = 0`. The placebo differs from the control on exactly two problems, in opposite directions (won 73,
lost 4). The one thing the arms visibly changed is how much they spent getting to the same answers.

**Instrument state.** `f_high = 0.00` on every arm (8 passes each, 0 suspect, max `sim` 0.452) ⇒ the band is read.
Integrity **all empty on both scoring passes** — KERNEL_REJECTED `[]`, STATEMENT_ALTERED `[]`, PROVENANCE (AP-4) `[]`,
orphan-B `[]`, unscored `[]` — with the three amendment-2 supersessions named and
`constants=[(40,5400,8M),(100,5400,8M),(100,5400,20M)]`, i.e. the three registered regimes and no fourth.

⚠ **AN INSTRUMENT GAP, DECLARED: the frozen `s2_morning_line.py` DOES NOT SCORE `a2`.** Its manifest filter is
`arm in ("a0","a1")` (line 75) and its contrast is hard-wired to `a0` vs `a1`, so in the pinned tool's own run the
thirty `a2` rows fall into "dropped as other-arm". `a2` was therefore scored by a **read-only analysis copy** with
`("a0","a1")` re-pointed to `("a0","a2")` and nothing else changed; the pinned file is byte-untouched
(`73c4eda8d10c3e9b…`, equal to its HASHES pin, verified after the analysis). Every `a2` figure above comes from the
control's own logic — same scored-row rule, same class source, same orphan and provenance checks — but a reader must
know it came from a copy. **Extending the pinned tool to arbitrary arms is owed, as its own dated amendment.**
📌 **And a naming defect found in the pinned tool while doing it:** its recall line prints
`(salt arm a1, for information: …)`. **`a1` is the PLACEBO.** The label is S1 heritage and touches no computation,
but it invites exactly the misreading this campaign cannot afford, and it is fixed in the same owed amendment.

**REGISTERED PREDICTIONS, SCORED — one holds, two fail:**

1. *"`a2` lands 8–12 of 15; `a1` lands 6–10 of 15"* — **8 and 8. HOLDS**, both at the bottom of their bands.
2. *"`a2`'s mean stage-B cost exceeds `a0`'s measured 2,749,871/ep by at least 25 %, and `a2` produces ≥ 4
   `ROUNDS_EXHAUSTED` against `a0`'s 3"* — ⛔ **FAILS ON BOTH CLAUSES.** `a2`'s mean is **3,427,587** against a
   threshold of 3,437,339: **short by 9,752, or 0.28 %** — a miss, and recorded as a miss precisely because it is
   close enough to be worth rounding, which is exactly when a pre-registration earns its keep. And `a2` produced
   **3** `ROUNDS_EXHAUSTED`, the same as control, not ≥ 4. (Against the CORRECT comparator — `a0`'s U15 mean of
   3,378,834 — `a2` is +1.4 %, so the clause fails far more heavily than the registered number suggests.)
3. *"at least one `a2` episode lands `COMPILE`"* — ⛔ **FAILS.** `a2` produced **zero**. The campaign's only `COMPILE`
   came from **`a1`**, on problem 141 — which is evidence against the mechanism I proposed (that forbidding the
   admitted gap would push the salt arm into non-compiling files), since a generic checklist produced one and the
   prohibition did not.

**THE COST FINDING, which is the only place the arms separate, and it is a paired within-problem comparison:**

- **Totals are flat:** `a0` 50,682,519 · `a1` 51,671,576 · `a2` 51,413,806 — a 1.4 % spread across all three arms.
- **But the split is not.** On the **8 problems both arms proved**, `a2` used **248 calls vs `a0`'s 329 (−24.6 %)**
  and **15.79M vs 20.76M tokens (−24 %)**. On the **7 both failed**, `a2` used **379 calls vs 348 (+8.9 %)** and
  **35.62M vs 29.92M (+19 %)**.
  ⇒ **WHERE A PROOF EXISTS, THE SALT ARM REACHES IT ABOUT A QUARTER CHEAPER; WHERE ONE DOES NOT, IT SPENDS ABOUT A
  FIFTH MORE BEFORE ADMITTING THE SAME GAP — AND THE TWO CANCEL.** A campaign that measured only totals would have
  seen nothing at all here. This is n=8 and n=7 and is reported as a paired observation, not an effect.
- ⛔ **A correction to what I said DURING the run:** at 6 of 15 I described `a2` as "cheaper on three of four passes"
  and drew the same conclusion from a partial set. The conclusion survived the full data, but it was a partial-mean
  reading when I said it, of exactly the family that produced the day's three pricing errors.

**THE `sorry` OBJECTION, ANSWERED BY THE DATA.** Amendment 5 registered that `a2` names `sorry` — the control's
dominant failure — and that if `a2` gained, "it was told not to write `sorry`" would be a live alternative
explanation. **`a2` did not gain, and the objection is now moot in the direction that matters: seven of `a2`'s
fifteen episodes ended `AXIOMS_FAIL` with `sorryAx`, the identical failure and the identical set as the control.**
Being told in plain terms that a placeholder is not a proof changed neither which problems were solved nor how they
failed. That is the cleanest thing this amendment establishes.

**Price:** stage A 6,457,019 (30 episodes) + stage B 103,085,382 → **109,542,401 metered, ~6.5 h**, against
amendment 6's rules of 72M per arm and 145M total. Final per-arm totals `a2` 55,780,005 · `a1` 53,762,396 —
**both under even the ORIGINAL 65M rule.** The raise was not needed. It was still the right call when it was ruled,
on the estimate then in hand; that the estimate was again too high is the fourth measurement of the same defect.

**What this does NOT show.** `a2` is the method's **solo-renderable core**, not the method: A1/A2/A5/A6 (orchestrator,
executors, councils, independent witness), R5, R6 and R7 are unrenderable in a sealed single-agent episode and were
registered as such before the run. **This result is silent on the Advisory tier and on every multi-agent invariant.**
It is one substrate, one model tier, one stage, k = 15, no p-value. It says: *on kernel-checked specification work at
this tier, a faithful solo rendering of the method's required articles changed nothing measurable about what the
agent could prove.*


---

### Amendment 7 — 2026-08-31, the instrument repair: the morning line can score ANY registered arm, and it stops calling the placebo "the salt arm" (no scored figure changes)

**Authorization.** Internal-facing instrument repair, so process and not a Captain word — the same boundary
amendment 4 ran under. It is registered here **before the Opus-5 reach amendment (desk row c) is written**,
deliberately: an instrument repaired *after* its next arm's numbers are in hand is a different instrument from one
repaired before, and this one is repaired before.

**⚠ AND IT IS NOT THE "CHEAP WIN" MY OWN BANK CALLED IT.** I banked this at 04:0x as the next head's cheapest
win, ~0 model tokens, nice-to-have. Desk row c makes it a **PREREQUISITE**: the row's named target is the **b
cell — problems the salt arm proves that the control cannot** — and that cell is exactly the `a0`-vs-`a2` contrast
the frozen tool structurally cannot compute. A "cheap win" and "a prerequisite of the next run" are not the same
priority, and I had it filed as the former.

**The defect, in two parts, both at the same instrument.**

1. **`s2_morning_line.py` DROPS EVERY NON-`a0`/`a1` ROW, SILENTLY AND WITH A COMPLETE-LOOKING REPORT.** The
   manifest filter reads `m.get("arm") in ("a0", "a1")` and the contrast is hard-wired `a0`-vs-`a1`. On 2026-08-31
   this meant **all 30 `a2` rows of amendment 5's treatment run were discarded as "other-arm"** while the tool
   printed a full, well-formed `a0`/`a1` table beside them and exited 0. The salt arm was scored by a **read-only
   analysis copy** re-pointed to `("a0","a2")`, with the pinned file left byte-untouched (verified after the
   analysis at `73c4eda8d10c3e9b`, its HASHES pin). That was the right move under time pressure and it is not a
   procedure to repeat: **the reading of record should come from the registered instrument, not from a copy of it.**
2. **THE TOOL CALLED `a1` "THE SALT ARM".** Its recall line printed `(salt arm a1, for information: …)`. **`a1` is
   the PLACEBO** — S1 heritage, from a time when a1 *was* the treatment slot; no computation ever depended on it.
   But it is printed on the page that carries this campaign's central claim, and it invites precisely the one
   misreading the campaign cannot afford. Worse, the analysis copy inherited the hard-wired caption: **the pinned
   `a0`-vs-`a2` evidence file says `c(a1 only)=0` while scoring `a2`.** The numbers in it are right; two captions
   in it are wrong, and this amendment is where that is said rather than quietly re-run.

**The repair.**

- The scored arm set is `ML_ARMS` (ordered, comma-separated), **default `a0,a1`** — the frozen behaviour.
- **It REFUSES rather than coerces**, because a silently-dropped arm is the whole defect: a token that is not an
  arm name, a repeat, or an arm set **without `a0`** each exit non-zero with a reason. `a0` is required because F3,
  the D16 per-stage cap and the recall instrument are *defined* on the plain arm; this switch does not re-point them.
- **Every unordered pair of the arm set gets its own b/c/n_d line, captioned with the ARM NAMES.** With the default
  pair that is byte-identical to the frozen line; with three arms it is three lines and the campaign's first
  complete 3×3 in one run.
- Roles are named from a table (`a0` plain/control · `a1` placebo · `a2` salt; anything else prints *role
  unregistered*), and the header now declares the arm set it scored, so a report can no longer be read without
  knowing which arms produced it.

**THE GATE — `selftest_morning_line.py`, nine arms, every one a SUBPROCESS on the script's real argv.** This
obeys the law amendment 4 paid for: *a self-test that never makes the call its caller makes is a self-test of a
different program.* Three green arms assert the numbers (default / `a0,a2` / all three), two label arms assert the
mislabel is **gone** *and* that the right labels are **present** — an absence assertion alone passes against an
empty report — and four red arms assert a refusal with a non-zero exit.

⛔ **AND THE DECISIVE CONTROL FOUND A DEFECT IN THE GATE ITSELF.** Run against the **frozen** tool the suite must
go red, so I ran it, and it did not report red — it **crashed** with `can only concatenate str (not "list")`,
because every green run had skipped the failure branch and no test had ever executed it. **A gate whose FAILURE
path has never run is an untested gate.** Fixed (`str(detail)`), commented in place, and both arms re-driven. The
control's result, which is the measurement that matters:

| suite run against | result |
|---|---|
| the amended tool | **PASS — 25/25 assertions, 9 arms** |
| the **frozen** tool (`73c4eda8d10c3e9b`, restored from git) | **FAIL — 15 of 25 assertions flip**, including every `ML_ARMS` refusal (all four red arms exit **0** — the variable is simply ignored), every `a2` figure, and `label1`, which reports the literal string `(salt arm a1, for information: passes 1, suspect 0)` |

The 10 assertions that pass under **both** are exactly the default-behaviour ones. **The suite discriminates, and
the half of it that does not discriminate is the no-op proof.**

**PROVEN NO-OP ON THE REAL DATA — measured on the Studio, over the campaign's actual 183-episode state.**

1. The **frozen** tool re-run today on `~/bench/state` at k=27 reproduces the pinned evidence file
   `evidence/treatment-read-2026-08-31/morning-line-a0-a1.txt` **byte for byte**. The reading of record is
   reproducible before anything is touched.
2. Relocating the frozen tool to a scratch directory reproduces it **byte for byte** again — so the move is not
   the variable.
3. The **amended** tool at its default reproduces it in **49 of 51 lines**. The two that differ are the repair
   itself and nothing else: the header gained ` arms=a0(plain/control) a1(placebo)`, and
   `(salt arm a1, …)` became `(arm a1 [placebo], …)`. **Every scored figure — every rate, class count, metered
   percentile, contrast, band and the F3 reading — is identical.**
4. `ML_ARMS=a0,a2` reproduces the pinned analysis copy with **every number identical**; the only diffs are the
   three contrast captions the copy got wrong (`c(a1 only)` → `c(a2 only)`), the recall label, and the header.
   **Amendment 5's result is unchanged in every figure. The analysis-copy procedure is retired.**

**ONE FACT THE REPAIR PRODUCES THAT NO PRIOR RUN COULD.** With all three arms in one pass, the **`a1`-vs-`a2`**
contrast is computable for the first time: at stage B, **b = 1, c = 1** — the placebo proves problem 73, which the
salt arm does not; the salt arm proves problem 4, which the placebo does not. INDISTINGUISHABLE by the registered
rule (|b−c| < 5), reported as counts, no p-value. It changes no conclusion. It is recorded because the frozen
instrument could not have told me it existed.

**Pins.** `s2lean/s2_morning_line.py` → `41030434291d3c0b…` (from `73c4eda8d10c3e9b…`); new
`s2lean/selftest_morning_line.py` → `6ebf8b53a4944c6b…`, inserted at the position `hashes.sh`'s own glob puts it,
and the whole `s2lean/` block of `HASHES.txt` re-verified byte-identical against a live re-run of those globs.

⭐ **THE LAW THIS AMENDMENT ADDS:** *an instrument that discards data it was not told about must SAY SO OR REFUSE —
a filter that silently narrows its input prints a complete-looking report over an incomplete one.* The frozen tool
did not lie about the 30 rows it dropped; it counted them, in a parenthetical, inside a total it also used for
SMOKE and DRY rows. **The count was there and it was unreadable, which is the same as absent.**


---

### Amendment 8 — 2026-08-31, THE OPUS-5 REACH AMENDMENT: the same U15, the tier raised, `a0` + `a2` — registered BEFORE its first call

**Authorization.** The Captain's word, in channel to the helm at 10:5x: *"Let's do the Opus 5 tier raise on the same
15 problems… 40% left on all-models on kriterion, reset in 5h. Let's go for it."* Docketed as **desk row c** (seat
`7065cbed`, 11:08:07); bench relit on it 11:08:17. This is the deferred **(c2)** of the 08/29 four-option brief —
the commission's sequential-models fence (Sonnet across all arms first, then the tier that differs) lifted by the
same hand that set it. Ruling O's *no further arm spend* was substrate- and tier-scoped, and **the tier is what moves.**

**The question, and only this question.** Amendment 5 ran `a0`/`a1`/`a2` on U15 at `claude-sonnet-5` and returned
the null: 8/15 every arm, and `a2` matched `a0` **problem for problem** — b = 0, c = 0, fifteen agreements out of
fifteen. **The b cell was empty.** This amendment asks whether it is empty *at that tier* or empty *simply*: at
`claude-opus-5`, on the same fifteen problems, **is there a problem the salt arm proves that the plain arm cannot?**

**⛔ WHAT THIS CANNOT SHOW, restated because a raised tier does not raise the rendering.** `a2` is still the method's
**solo-renderable core** — A1/A2/A5/A6, R5, R6 and R7 remain unrenderable in a sealed single-agent episode. A
positive result here is about the articles a lone agent can carry, and nothing else. The Advisory tier is untouched.

**The registered population — unchanged, and unchanged on purpose.** U15, the unflagged drawn subset at draw depth 27:
`73 0 146 16 4 38 142 96 112 141 31 54 127 18 74`. Same seed, same draw, same order. The whole value of this
amendment is that the population and the checker are held fixed while exactly one variable moves.

**The arms.** `a0` (plain) and `a2` (salt, `harness/arms/a2.md`, pin `0c37d7c8…`, 1,913 B — byte-identical to the
arm that ran at Sonnet). **`a1` (placebo) is CONTINGENT and is registered here so it cannot be a post-hoc
addition:** it runs, on this same population and tier, **if and only if `a2` beats `a0` by b − c ≥ 2 at stage B.**
The reasoning is stated before the data: at Sonnet the placebo was indistinguishable from plain, so the "any added
prompt helps" channel is already measured *closed at that tier*; it must be re-opened only if the salt arm actually
gains, at which point ruling it out is mandatory rather than optional. If `a2` does not gain, `a1` would buy a
second null at roughly half the price of the whole amendment.

**Constants — the fourth regime, and no fifth.** `R_AMEND=100` (matching U15's regime exactly) ·
`W_AMEND=10800` · `TC_AMEND=30000000` · `M_AMEND=claude-opus-5` · effort `high`. The manifests will therefore
carry `(100, 10800, 30000000, 'claude-opus-5', 'high')` and the morning line's `constants` list must show **four**
regimes and no more.

- **`TOKEN_CEILING`'s disposition, which desk row c demands explicitly.** Amendment 4 made it operative and proved
  it repaired. It is set **NON-BINDING at 30,000,000** — 2.55× the largest episode this campaign has ever metered
  (11,757,659, problem 141 at Sonnet). It is a **runaway guard, not a budget rule.** `R` and `WALL` bind, exactly
  as they did for every Sonnet row in the comparison. The budget rule is the live watch below, on the aggregate.
- **Why the wall ceiling is raised, and why that is not a loosening.** `WALL_S=5400` was *never binding at Sonnet*:
  the U15 stage-B maximum was 1,987 s, **37 % of it**. A slower tier can hit a ceiling the control never touched,
  and a ceiling that binds at one tier and not the other is an **instrument asymmetry across the tier** — the same
  defect amendment 5 had to correct for `TOKEN_CEILING`, in the same direction, against the same comparison.

**Harness — two registered overrides, in the shape amendments 3 and 5 established.** `M_AMEND` (allowlisted
`claude-sonnet-5 | claude-opus-5`; **`claude-fable-5` deliberately absent** — Fable episodes need the Captain's own
word per council item 12, and kriterion's Fable weekly read **93 % consumed** at 11:00 today) and `W_AMEND`
(validated integer seconds). Both REFUSE rather than guess, both are re-exported after the driver's deliberate
unset, both print to the run log. **Six REFUSE arms and a negative control driven under the run-shaped dry before
this text was written; the accept path is driven on the Studio before the first episode** — the campaign's own gate,
which has caught a fatal in 4 of 4 repair rounds.

**THE PRICE, PER ITEM — the law this campaign has paid for four times.** The pairs are measured: every one of the
30 cells this amendment will run has a Sonnet cost on the same problem, same stage, same arm.

| | `a0` | `a2` | both arms |
|---|---|---|---|
| stage A, 15 problems | 2,449,669 tok / 1,538 s | 4,366,199 / 2,386 s | **6,815,868 / 3,924 s (65 min)** |
| stage B, 15 problems | 50,682,519 / 9,980 s | 51,413,806 / 9,777 s | **102,096,325 / 19,757 s (5.5 h)** |
| **A + B** | 53,132,188 | 55,780,005 | **108,912,193 / ~6.6 h** |

⭐ **AND THE PER-ITEM VIEW SHOWS SOMETHING A TOTAL CANNOT: FIVE PROBLEMS CARRY ~85 % OF STAGE B.** Problems
**73, 146, 38, 112, 141** account for 42.9M of `a0`'s 50.7M and 43.3M of `a2`'s 51.4M. **Three of those five — 73,
112, 141 — are the R = 100 cap-runners that never succeed in either arm.** So the amendment's cost is dominated by
its known failures, not by its successes, and any truncation is a decision about how much to spend re-failing.

**THE UNKNOWN, NAMED: the tier multiplier.** Nothing in this campaign has ever metered an Opus episode. The Sonnet
table above is a *per-item basis*, not a prediction — it becomes one only when multiplied by a measured `m`.
**So stage A is run first and is the calibration**, which costs nothing extra because row c requires both stages at
the raised tier anyway.

**BUDGET, MEASURED — and it decides start-now vs wait.** kriterion at 11:00 (quota-cadence, zero model tokens):
**5-hour rolling 0 %** · **all-models weekly 60 % used ⇒ 40 % left** · Fable weekly 93 % · **both weeklies reset
today at 15:59.**
⇒ **THE 40 % EXPIRES IN ~4.5 HOURS. Spending it before 15:59 is not a cost — not spending it is.** That, and not
the "go for it" bias, is why this starts now. **Stage A goes in the expiring pool; stage B goes on the fresh one.**

**THE STAGE GATE — mechanical, computed from measurements, registered before either stage runs.**

1. After stage A: `m_A = T_A(Opus) / 6,815,868` — the paired multiplier over the *same 30 cells*.
2. **ONE** quota reading (never a poll): `r = Δ(all-models weekly %) / T_A`.
3. `T_B_pred = 102,096,325 × m_A` (the per-cell sum, not a mean); `Q_B_pred = T_B_pred × r`.
4. **GATE:** stage B starts on the **fresh** weekly (after 15:59) and runs the **full U15, both arms**, only if
   `Q_B_pred ≤ 60 %` of a weekly pool. Otherwise it runs both arms over a **PREFIX of U15 in draw order** — the
   draw was built to be truncated at its head, the driver is task-major with arms alternating, so a prefix is a set
   of *complete pairs* and never a cherry-pick — and **the read is over the completed prefix and says so.**

**STOP RULES — with a LIVE enforcer armed BEFORE the first episode, not a memory** (the 08/30 law: a budget rule
needs an enforcer, and a watch built on end-of-unit events cannot tell a long unit from a dead one, so the watch
carries in-flight liveness).

- **Stage A:** 25,000,000 metered (≈ 3.7 × the Sonnet figure) **or** 3.0 h wall — the driver stops after the
  episode in flight and the state goes to the desk before anything further runs.
- **Stage B:** the all-models weekly reaching **75 % consumed**, **or** 90,000,000 metered in either arm, **or**
  12 h wall — same halt, same report. A quarter of the week's pool is left for everything else kriterion does.
- A halt is **resumable** and quota exhaustion is a swap event under the council's doctrine, not a failure.

**PREDICTIONS, registered before the first call, scored as they stand.**

1. **Rate.** `a0` stage-B proven on U15 lands in **9–13 of 15** and `a2` in **9–13** (Sonnet: 8 and 8). The floor
   of 9 is the substantive claim that the tier raise buys at least one problem.
   **Per item:** all eight Sonnet-proved problems (146, 16, 4, 38, 142, 31, 54, 74) stay proved in **both** arms,
   and any gain comes from **{73, 112, 141}** — the three that exhausted R = 100 — **not** from {0, 96, 127, 18},
   which admitted `sorry` cheaply with ~86 turns in hand. *Extra capability should rescue the ones that ran out of
   room, not the ones that gave up early.*
2. **The b cell — the row's own target.** **b ≤ 1 and |b − c| < 5 ⇒ INDISTINGUISHABLE again.** I register the null
   as the modal expectation at the raised tier too, so that a gain is a surprise rather than a confirmation.
3. **The cost split reproduces in SIGN.** The 08/31 finding — `a2` ~25 % cheaper where both arms prove, ~19 %
   dearer where both fail — holds in sign on **both** halves at Opus. This is the campaign's only measured
   separation, and a tier raise is the first test of whether it belongs to the method or to the tier.
4. **Failure mode unchanged.** `AXIOMS_FAIL` with `sorryAx` remains the dominant failure class in both arms
   (≥ 60 % of non-passes).

**Decision rule.** The registered morning line — now amendment 7's instrument, which can score `a2` at all —
with `|b − c| < 5 ⇒ INDISTINGUISHABLE`. Counts, not p-values. An outcome this text does not cover is a **HOLD**
with a fallback row, never an improvised arm (F5).

**Order of operations.** GT off the host **first** (stage A is GT-free by construction; `ship A` is known to hang,
so its end state is produced by hand and verified by **SET-HASH**, never by an exit code) → stage A, both arms →
the gate above → `ship BC` → stage B, both arms → the morning line at `ML_ARMS=a0,a2` → the contingent `a1` only if
prediction 2 fails in the salt arm's favour.

📌 **RECEIPT, already taken, and one instrument finding with it.** GT was removed by hand at 11:3x and verified by
content: **0 GT files anywhere under `~/bench`**, A-views set-hash **`bc4d6eafc0430ed2`** on the Studio equal to the
seat's, 161 problem dirs, no `.pristine-cache`. The recipe is `<relative path> <sha256>` per file, sorted, hashed —
and it **reproduces the banked A-views figure exactly**, which is how I know it is the banked recipe. ⚠ It does
**not** reproduce the banked GT figure (`05139f9aba3dbc17`; this recipe gives `cf67a9c0ed805f36` on the seat **and**
on the Studio, so the two sides agree and the *recipe* differs). ⇒ **a set-hash without its recipe is not a
receipt — it is a number that only its author can check.** The recipe is written down here so the next head can.

**AMENDMENT 8, ADDENDUM 1 — 2026-08-31, appended BEFORE the first call: the stop rule gets an enforcer the driver
obeys.** Writing the watch exposed a gap in the amendment I had just registered: **the stop rules above had no
mechanism.** The driver has no halt hook, so "stops the driver after the episode in flight" would have meant a watch
racing to kill a process **mid-episode** — which corrupts the very landing the rule exists to protect, and leaves a
half-written manifest that the morning line must then adjudicate. Added: the watch touches `$BENCH/HALT` with its
reason; the driver reads it **inside the arm loop** (not the problem loop — with two arms per problem, a
problem-level check spends a whole extra episode after the breach) and exits **4**, printing the reason, having
started nothing. Driven both ways before this was written: absent ⇒ the episode starts; present ⇒ exit 4, reason
printed, **zero** episodes started. ⇒ **A STOP RULE WITHOUT A MECHANISM IS A SENTENCE, NOT A RULE** — and I had
written it as a sentence twice (amendments 5 and 6) before building the mechanism.

**AMENDMENT 8, ADDENDUM 2 — 2026-08-31, appended BEFORE the first call: the run gets its OWN STATE ROOT, and why
the dry did not catch what stopped it.** The first launch of stage A **started zero episodes**: the driver printed
`skip … (terminal landing exists)` **thirty times** and went straight to `DRIVER DONE`. `has_terminal` greps the
landings log, and every U15 stage-A cell already has a `DONE` there **from the Sonnet run** — the resume logic that
makes a halt safely resumable cannot see that the *tier* has changed, because the landings line has no model field.
**Zero model tokens were spent** (probe: 0 started, metered 0, no new manifests), so the amendment's first call has
still not happened when this is written.

⛔ **AND THE DRY SHOULD HAVE CAUGHT IT AND COULD NOT.** My run-shaped dry ran against a *fresh* `BENCH`, so its
landings log was empty — the one dimension the real run differs in. ⇒ **A DRY THAT DOES NOT INHERIT THE REAL RUN'S
HISTORY IS NOT RUN-SHAPED; IT IS SHAPED LIKE THE FIRST RUN.** That is the fifth repair round in this campaign to
produce a fatal, and it is the same defect class as the meter's self-test: *the call I made was not the call the
caller makes.*

📌 **A SECOND HAZARD THE SAME FINDING EXPOSED, which had not stopped anything and would have been silent.** Stage A
writes `A.bodies.json` to `state/s2/<task>/<arm>/`, keyed on **(task, arm) only — not on tier.** Had the skip logic
not fired, an Opus stage A would have **overwritten amendment 5's Sonnet stage-A bodies in place.** The manifests'
`a_bodies_sha256` and the orphan rule would have caught the *inconsistency* at scoring time, and the archived
`state/ep-*/bodies.json` are the fallback, so the evidence was recoverable — **but the overwrite itself would have
been silent, and "recoverable" is not "safe".**

**The repair, which fixes both at once: this amendment runs in its own state root, `~/bench-a8`.** Fresh landings
log (so nothing is skipped and resume still works *within* this run), fresh `state/` (so no Sonnet artifact can be
touched), the smoke log and `s2-controls.json` copied in so **both gates still apply**, and `s2views` a symlink to
the one GT-free view tree (161 A + 161 frozenA, **0 GT**, verified through the link). `H` still points at the pinned
`~/bench/harness`, so the harness under test is the pinned one. Verified before launch: 0 prior `A.bodies.json`
reachable from the new root. The watch and its HALT path were re-pointed and the halt chain re-driven end to end
against the new root before arming. ⇒ **A NEW REGIME GETS A NEW STATE ROOT — sharing one is how a tier raise
quietly eats the control it is being compared against.**

**AMENDMENT 8, ADDENDUM 3 — 2026-08-31, appended BEFORE stage B's first call: the gate's result, a caveat I owed,
and the finding that the token multiplier HIDES the tier's real cost.**

**STAGE A LANDED: 30/30, every cell `DONE / PASS`**, in 5,663 s (1.57 h) — inside the 3 h wall rule, and
**5,982,892 metered = 24 % of the 25M token rule.** The full population qualifies for stage B, exactly as at Sonnet.

**THE TIER MULTIPLIER, MEASURED OVER ALL 30 PAIRED CELLS:** `a0` 1,737,611 vs 2,449,669 ⇒ **×0.709** · `a2`
4,245,281 vs 4,366,199 ⇒ **×0.972** · **`m_A` = 0.878.** ⭐ **The raised tier is CHEAPER in tokens at this stage,
which I did not expect** — and the salt arm's overhead *ratio grew*: `a2`/`a0` was 1.78 at Sonnet and is **2.44** at
Opus. A stronger model needs fewer rounds to write a spec; the method's required articles cost what they cost
whoever executes them. Stage A is not a scored quantity and this is an observation, not a finding.

⛔ **THE CAVEAT I OWED AND HAD NOT REGISTERED.** `m_A` is measured on episodes of **5–22 calls**; stage B runs to
**100**. A multiplier from short work need not transfer to long work. So the gate now carries an explicit
**pessimistic band `M_HI = 2.0`** — "Opus costs twice the tokens per unit of long work", a bound and not a
prediction — and **decides on the worst corner**, because *a gate decided on a point estimate is a gate that has
assumed away its own largest unknown.*

⭐⭐ **AND THE FINDING THAT MATTERS MOST, WHICH THE TOKEN MULTIPLIER ACTIVELY CONCEALS: THE QUOTA COST PER TOKEN IS
ROUGHLY DOUBLE AT THIS TIER.** One reading (never a poll) after stage A: **8 / 62 / 93**, against 2 / 61 / 93 at
dispatch. Against the 08/29 Sonnet calibration (19,666,775 metered moved the 5-hour arm 0 → 9):

| | metered | 5-hour points | points per M tokens |
|---|---|---|---|
| Sonnet, 08/29 | 19,666,775 | +9 | 0.458 |
| **Opus, stage A today** | 5,982,892 | **+6** | **1.003** |

⇒ **≈ 2.19× the quota per token**, while the *token count fell 12 %*. **The effective tier cost is ≈ 0.878 × 2.19 ≈
1.9×, and a campaign that priced this tier on tokens alone would have called it free.** Both figures include head
activity in their windows, so this is a like-for-like ratio and not a clean isolation; and the weekly arm agrees
only within its own error (1 point per 19.67M at Sonnet, 1 point per 5.98M today ⇒ 3.3×, from two **single-point,
whole-percent** reads that carry ±50 % relative error each). **The 5-hour arm is the better instrument here purely
because it has six times the resolution** — which is itself worth recording: *the coarse instrument was the one the
gate was registered on.*

**THE GATE, COMPUTED AS REGISTERED, AT ALL FOUR CORNERS** (`T_B_pred` = the per-item sum over the 30 stage-B cells,
never a mean): measured `m_A` × point rate **15.0 %** · measured × pessimistic rate **22.5 %** · `M_HI` × point rate
**34.1 %** · **`M_HI` × pessimistic rate 51.2 %.** ⇒ **51.2 % ≤ 60 % ⇒ GATE PASSES ON THE WORST CORNER ⇒ FULL U15,
BOTH ARMS.** No truncation, no prefix.

📌 **A PACING FACT THE GATE DOES NOT COVER, STATED SO IT IS NOT A SURPRISE.** Stage B is predicted at ~89.6M tokens
and ~7.9 h wall (the stage-A wall ratio was 1.44). At the measured rate that is ~90 points of 5-hour capacity
against ~176 available over the run — comfortable. **At `M_HI` it is ~205 needed against ~176 available, so the run
would stall on the ROLLING limit and wait for a refill.** That is survivable by design, not a failure: the driver's
own `QUOTA` hold branch bridges up to 6 h and a halt is resumable. Named here because an unnamed stall reads as a
dead driver.

⚖ **A DEPARTURE FROM MY OWN REGISTERED ORDER, MADE IN WRITING BEFORE THE ACT RATHER THAN SILENTLY.** Amendment 8
says *"stage B starts on the fresh weekly (after 15:59)."* That was the right call when the fresh pool was the only
one big enough to matter. It is now **wrong for the same reason the original was right**: 38 % of the weekly remains
and **it expires at 15:59**, the gate says stage B needs 15–51 % of a pool, and idling for two and three-quarter
hours **forfeits** the expiring 38 % without buying anything — the reset refills the counter regardless of how much
of it I spend first. **Stage B therefore starts now and straddles the reset.** The worst case is that it exhausts
the expiring pool before 15:59 and the `QUOTA` hold bridges the remaining minutes — strictly better than idling
through them. ⇒ *A registered order exists to stop improvisation, not to outlive the measurement it was built on;
the discipline is that the change is dated, reasoned and appended BEFORE the act — which is what this is.*

📌 **A STALE GATE, NAMED.** `stage_views.sh ship BC` refuses unless `~/bench/logs/run_s2_stage0.log` carries
`S2 STAGE A DRIVER DONE`. This run logs to **`~/bench-a8`**, so that gate was satisfied by a **DONE from the Sonnet
run** — it passed, and it passed for the wrong reason. The real condition was verified by hand (this run's own log
carries its own DONE at 20:09:25Z, 30/30 landed). ⇒ **A GATE THAT READS A PATH THE RUN NO LONGER WRITES IS A GREEN
LIGHT WIRED TO NOTHING** — an inherited cost of addendum 2's state-root split, and cheaper to say than to leave for
the next head to trip over. GT is now on the host and verified **by content**: GT set-hash `cf67a9c0ed805f36` and
A-views `bc4d6eafc0430ed2`, both equal to the seat's, `frozen=161 C=161`.

**Stage-B stop rules, unchanged from amendment 8** (weekly at 75 % consumed · 90,000,000 metered in either arm ·
12 h wall), with the live enforcer re-armed on stage-B caps before the first stage-B episode.


---

### Amendment 8 — RESULT, 2026-08-31: the tier raise buys TWO PROBLEMS AND A QUARTER OF THE PRICE, and the reach cell is still not the salt arm's

**The run.** 60 episodes, stage A + stage B, `a0` and `a2` over U15 at `claude-opus-5`, in the isolated root
`~/bench-a8`. **All 60 terminated `DONE`. Zero `ROUNDS_EXHAUSTED`** (Sonnet had three), zero retries, zero holds,
no `HALT` — the run ended on its own and the enforcer exited on the driver's own `DONE`. Scored by the **registered
instrument** at `ML_ARMS=a0,a2` — the first time this campaign has scored a salt arm with its own tool instead of a
copy of it. `constants=[(100, 10800, 30000000, 'claude-opus-5', 'high')]`, one regime, exactly as registered.

**THE READ (U15, stage B, isomorphism proven):**

| | Sonnet (amendment 5) | **Opus (this amendment)** |
|---|---|---|
| `a0` plain | 8/15 = 53.3 % | **10/15 = 66.7 %** |
| `a2` salt | 8/15 = 53.3 % | **10/15 = 66.7 %** |
| contrast | b=0, c=0, **15/15 agreements** | `a0`-only **{112}** · `a2`-only **{4}** · **\|b−c\| = 0** |
| verdict | INDISTINGUISHABLE | **INDISTINGUISHABLE** |

`f_high = 0.00` on both arms (max sim 0.588) ⇒ **the band is read.** Recall instrument clean.

⭐ **THE TIER RAISE IS REAL AND IT IS CHEAP.** +2 problems in each arm, and **the whole amendment cost
26,104,403 metered in 5.0 h against Sonnet's 108,912,193 in 6.6 h — ×0.24 of the tokens.** Stage B alone is
**×0.197**. The `a0` stage-B p90 fell from **7,673,919 to 967,038** (×0.126). Adjusting for the measured ~2.19×
quota-per-token of the tier, the effective cost is still ≈ **×0.53**. **The raised tier was cheaper in every
currency and better on the rate** — which is not what a tier raise is normally expected to be, and it is the single
most useful fact this amendment produced for the campaign's future pricing.

📌 **AND THE MECHANISM IS VISIBLE PER ITEM: THE TIER RAISE DID NOT MAKE HARD PROBLEMS CHEAPER TO GRIND — IT STOPPED
THE GRINDING.** The three R=100 cap-runners were the campaign's most expensive cells and all three *failed* at
Sonnet. **Problem 141: 11,757,659 tokens and 100 calls, failing, at Sonnet → 180,396 tokens and 9 calls, PASSING,
at Opus.** Problem 73: 8.9M failing → 832K passing. Problem 112: 7.4M failing → 2.9M passing. ⇒ *a cost model built
on a weaker model's failures is a model of its flailing, and it does not transfer up a tier.* This is why every
corner of my registered gate was pessimistic and every corner was wrong in the same direction.

---

**PREDICTIONS: THREE HOLD, ONE FAILS.**

1. ✅ **Rate — HOLDS on both clauses.** Predicted 9–13 for each arm; **got 10 and 10.** The per-item clause holds
   *exactly*: I registered that gains would come from **{73, 112, 141}** — the three that exhausted R=100 — and
   **not** from {0, 96, 127, 18}, which admitted `sorry` cheaply with turns in hand. **`a0` gained 73, 112 and 141;
   `a2` gained 73 and 141. Not one gain, in either arm, came from the excluded set.** The reasoning — extra
   capability rescues the ones that ran out of room, not the ones that gave up early — is the best-supported claim
   in this amendment.
   ⛔ **But I did not predict a LOSS, and there is one: `a0` proved problem 4 at Sonnet and FAILS it at Opus**
   (`AXIOMS_FAIL`, `sorryAx`). ⇒ **A TIER RAISE IS NOT MONOTONE PER PROBLEM.** Net +2 in each arm is a net.
2. ✅ **The reach cell — HOLDS.** Predicted `b ≤ 1` and `|b−c| < 5`; got **1 and 0.** The cell is no longer empty,
   and it is symmetric.
3. ⛔ **The cost split — FAILS, and on every set I can defend.** I predicted `a2` stays *cheaper* where both arms
   prove and *dearer* where both fail. **The sign flipped on the first clause at all three candidate sets:** the 9
   both-proved at Opus (Sonnet −3.0 % → Opus **+50.6 %**), the 8 both-proved at Sonnet that I wrote the prediction
   from (−23.9 % → **+35.2 %**), and their 7-problem intersection (−24.3 % → **+66.6 %**). Reported on all three
   *precisely so the verdict cannot depend on a set chosen after seeing the answer.* The second clause holds (both
   tiers dearer where both fail). ⇒ **the campaign's only measured separation was a property of the TIER, not of
   the method** — at Opus the salt arm is simply the more expensive arm everywhere.
4. ✅ **Failure mode — HOLDS.** `AXIOMS_FAIL` is 4 of 5 non-passes in **each** arm (80 %, against a ≥60 % bar).

---

⚠ **THE INTEGRITY BLOCK IS NOT EMPTY FOR THE FIRST TIME IN THIS CAMPAIGN. Both events were inspected at the
artifact before this text was written. NEITHER IS A CHEAT, and one of them changes how the result should be read.**

⛔⛔ **(1) `problem_112`, `a2`, `SCREEN` — THE CONTROL-ONLY CELL WAS NEVER EVALUATED.** The salt arm's submission
carried `set_option linter.deprecated false` on line 1 of its helper lemmas, and the screen refused it. **The screen
is a WHITELIST** (`maxHeartbeats | maxRecDepth | synthInstance.*`, literal nat, `in` form) and everything else is
screened **because `debug.skipKernelTC` lives in "everything else"** — a whitelist is the correct way round for a
soundness screen and it behaved exactly as frozen. But the pragma it refused is a **linter suppression with no
soundness content**, the file was never compiled (`compiled=false`, `rc=null`, `replay_ok=null`), and its
isomorphism proof is a long, serious attempt. ⇒ **WE DO NOT KNOW WHETHER `a2` WOULD HAVE PROVED 112.** And the
stakes are exact: **had it passed, `a2` would read 11/15 and the salt-only cell would be 2 — which is precisely the
`b − c ≥ 2` that this amendment registered as the trigger for the contingent `a1` placebo arm.** The null rests on
an unevaluated cell, and that sentence belongs in front of the null, not behind it.
🛑 **I am NOT re-running it as part of this read.** A single cell re-run, chosen because of the result it produced,
is the exact cherry-pick pre-registration exists to prevent. It is a **desk question**; if it is to be answered it
is a DIAGNOSTIC under its own dated amendment, labelled as such, in the shape amendment 2 used — and any narrowing
of the screen must be registered **before** the re-run, since narrowing a screen after seeing which cell it cost is
itself post-hoc.

⭐ **(2) `problem_18`, `a0`, `KERNEL_REJECTED` — and the most remarkable episode of the run is a CONTROL episode
that is not a failure of capability.** The agent wrote `by sorry` for the isomorphism, and in its helper lemmas
**formally proved that the isomorphism statement is FALSE** — two independent counterexamples
(`spec_isomorphism_is_false`, `spec_isomorphism_is_false'`) built on an implementation satisfying its own
`generated_spec` by `rfl`, with an explicit off-by-one diagnosis (`problem_spec` demands `result = string.length`
while `generated_spec` counts `length + 1` positions). It is scored **FAIL, correctly** — the isomorphism was not
proven. But ⇒ **"THE AGENT PROVED THE TASK STATEMENT FALSE" AND "THE AGENT COULD NOT DO THE TASK" ARE DIFFERENT
EVENTS, AND THIS CHECKER CANNOT TELL THEM APART.** That is a finding about the *instrument*, and it applies to
every `sorry` this campaign has ever counted.
⚠ **A class-comparability caveat I have NOT diagnosed:** eleven Sonnet episodes with the identical honest `sorry`
scored `AXIOMS_FAIL`, i.e. they passed the kernel-replay gate; this one failed it (`replay_ok=false`) and so was
classified by the first failing gate as `KERNEL_REJECTED`. **The rate is unaffected — it is a fail either way — but
the CLASS DISTRIBUTIONS of the two reads are not comparable until this is diagnosed.** Named, not explained away.

---

**Price and instrument.** Stage A 5,982,892 / 5,663 s (30/30 `DONE / PASS`) · stage B 20,121,511 / 12,380 s ·
**total 26,104,403 / 5.0 h**, against stop rules of 90M per arm and 12 h — **the run finished at 29 % of one arm's
token rule and 42 % of the wall rule, and no stop rule ever fired.** Superseded 0, unscored 0, orphan B rows 0,
`STATEMENT_ALTERED` empty, `PROVENANCE` (AP-4) empty, 15/15 resolved in both arms.

**What this does NOT show.** `a2` remains the method's **solo-renderable core**: A1/A2/A5/A6, R5, R6 and R7 are
unrenderable in a sealed single-agent episode. **A raised tier does not raise the rendering.** One substrate, one
stage, k=15, no p-value, and — as of this read — one cell of the contrast never evaluated.

⭐ **THE SENTENCE THIS AMENDMENT EARNS:** *at a materially stronger tier, on the same fifteen kernel-checked
specification problems, the plain agent and a faithful solo rendering of the method proved the same number of
problems and disagreed on exactly one problem each — while the tier raise itself bought two problems in both arms
at a quarter of the price.* **The variable that moved the result was the model, not the method.**

---

### Amendment 9 — 2026-08-31 (17:4x PDT / 2026-09-01 00:4x UTC), row AC: the REFUSED `112 / a2` CELL — a DIAGNOSTIC over a FROZEN artifact, registered BEFORE its first check and BEFORE any number

**What authorizes it.** The Captain's standing law of 2026-08-31 17:4x, verbatim on the bus: *"You don't need to
block on me, the only restricted operations are external facing… everything is preapproved, make good choices. If
any seat is uncertain, work on a branch."* The helm's routing to this seat in the same post: *"row AC's asterisk —
state YOUR OWN pre-registered criterion for the refused `112/a2` cell on a branch, fire the registered `a1` arm
under it, and post the result as the sitting's evidence with the criterion stated before the number."* This
amendment is that criterion. It is written and committed on branch `bench/amend9-refused-cell` **before the first
check is run**, which is the only property that makes it worth anything.

**Why a criterion is needed at all, stated without softening it.** I have already seen the result the refused cell
would change. Re-examining one cell *chosen because of the answer it produced* is the exact act pre-registration
exists to prevent, and "everything is preapproved" does not repeal that — it hands me the DECISION; it does not
hand me permission to make the decision after the fact. So the order of work is: the criterion, in writing,
committed; then the check.

---

#### 9.0 · What this amendment does NOT amend

The **amendment-8 reading of record is untouched and stays untouched**: `a0` 10/15, `a2` 10/15, `a0`-only `{112}`,
`a2`-only `{4}`, `|b−c| = 0`, INDISTINGUISHABLE. The frozen screen behaved exactly as frozen; `problem_112 / a2 /
ep-6b5540c0` is `class = SCREEN` in its manifest and **remains `SCREEN` in its manifest forever**. Nothing produced
under this amendment retro-scores a landed episode, and no figure in §Amendment 8 — RESULT is rewritten by it. What
this amendment produces is a **DIAGNOSTIC, labelled as such wherever it is reported**, in the shape amendment 2 used.

---

#### 9.1 · THE CORRECTION THAT COMES FIRST — amendment 8's statement of the stakes is ARITHMETICALLY WRONG, and it is the reason this row exists

Amendment 8 — RESULT, integrity event (1), says of the refused cell:

> *"had it passed, `a2` would read 11/15 and the salt-only cell would be 2 — which is precisely the `b − c ≥ 2`
> that this amendment registered as the trigger for the contingent `a1` placebo arm."*

**The second clause is false, and I found it while writing this criterion, before running anything.** Read at the
artifact (`evidence/opus-reach-read-2026-08-31/01-morning-line-a0-a2.txt:11,16` and
`03-stageB-per-problem-and-cost-split.txt:7`):

- `a0` proven = `[73, 146, 16, 38, 142, 112, 141, 31, 54, 74]` — **`112` is already in the control's pass set.**
- `a2` proven = the same ten with `4` in place of `112`.
- ⇒ `a0`-only `= {112}`, `a2`-only `= {4}`, and the tool prints `b(a0 only)=1 c(a2 only)=1 n_d=2 |b-c|=0`.

If the refused cell resolves to a PASS, `112` becomes a **mutual** pass, not a salt-only pass. The cells become
`a0`-only `= {}` and `a2`-only `= {4}`: the **salt-only cell stays at 1**, and it is the *control-only* cell that
falls to 0. The salt arm's margin over the control goes from **0 to +1** — never to +2. The slip is exactly the one
it looks like: `{4} ∪ {112}` was counted as the salt-only cell while `112` was already the control's.

⛔ **CONSEQUENCE, AND IT SHRINKS THE ROW:** under **either** resolution of the refused cell, the registered
contingency for the placebo arm — *"it runs if and only if `a2` beats `a0` by `b − c ≥ 2` at stage B"* — **does not
fire.** The reachable maximum is +1. The null does not rest on the unevaluated cell. **The RATE does** — `a2` would
read 11/15 against `a0`'s 10/15 — and that is a real and sufficient reason to run the diagnostic, but it is a
smaller claim than the one amendment 8 made, and the smaller claim is the true one.

📌 **A SECOND DEFECT IN THE SAME SENTENCE, NAMED SO IT CANNOT BIND ANYTHING LATER.** The registered trigger's prose
and its symbols contradict each other. `s2_morning_line.py:211` prints `b` = **first-arm-only** and `c` =
**second-arm-only**, so at `ML_ARMS=a0,a2` the symbols read `b = a0`-only, `c = a2`-only, and "`b − c ≥ 2`" is
literally *the control beating the salt arm by two*. The prose says the opposite ("`a2` beats `a0`"). The intent is
unambiguous from the surrounding paragraph and I read it as intended — **(a2-only) − (a0-only) ≥ 2** — but a
trigger whose words and whose symbols disagree is not a rule, and it must not be left to be resolved by whoever
reads it after seeing a number. **It is resolved here, in the intended direction, before any number.**
⇒ **A CONTINGENCY REGISTERED IN TWO NOTATIONS IS TWO CONTINGENCIES UNTIL SOMEONE PICKS ONE — AND THE MOMENT TO
PICK IS BEFORE THE DATA, WHICH IS NOW.**

---

#### 9.2 · THE CRITERION — admissibility is MEASURED, not asserted

The screen (`harness/s2lean/screen.py`) is defence in depth, not the gate: it refuses bodies carrying
command-introducing or meta keywords so that agent meta-code is never compiled. Its `set_option` clause is a
**whitelist** (`maxHeartbeats | maxRecDepth | synthInstance.*`, literal nat, `in` form) and everything else is
refused **because `debug.skipKernelTC` lives in "everything else"**. A whitelist is the correct direction for a
soundness screen and that direction does not change here.

I will not decide admissibility by asserting a taxonomy of "harmless" options — that is exactly the kind of
judgement that bends toward the answer one wants. **The criterion is a differential measurement, registered now:**

> **A `set_option` occurrence in a landed body is ADMISSIBLE iff, holding the agent's bodies byte-identical
> otherwise, the assembled module passes the FULL gate — compile, kernel replay (`loadExts := false` +
> `Environment.replay`), statement byte-identity, axiom allowlist — with the pragma PRESENT, and the run with the
> pragma DELETED produces the IDENTICAL gate outcome, the IDENTICAL axiom sets for all three names, and the
> IDENTICAL `spec_isomorphism` statement. If deleting the pragma changes ANY gate outcome, the pragma had semantic
> content and the refusal STANDS.**

Both arms are run and both are reported. The pragma-deleted arm is the negative control: **a pragma that can be
removed without changing a single gate outcome cannot have bought the proof.** If the deleted arm fails to compile
where the present arm compiles, that is itself the proof that the refusal was right, and it is reported as such.

The soundness argument that makes this criterion *principled* rather than merely convenient — stated before the
measurement, so the measurement can refute it: a Lean linter is an **elaboration-time diagnostic pass**; its verdict
is a message, and messages do not enter the terms the kernel checks. Downstream of it this campaign's gate replays
the environment from `ConstantInfo`s in a fresh kernel, which cannot see an option that only governed which
warnings were printed. If that argument is wrong, the differential arm will say so.

---

#### 9.3 · SCOPE — what may and may not be touched

**MAY:** re-run `check.py` over the **stored** bodies of `ep-6b5540c0`, pinned at
`bodies_sha256 = 06f40a82464212a9046628d961e2052162d5cea66a9b6ac8c232567320ff4ba1`
(`a_bodies_sha256 = f71afda6…`, `view_sha256 = dc7f28bc…`, `frozen_sha256 = 206dc29a…`, all read from the landed
manifest), with the screen's refusal bypassed under §9.2 and with the pragma-deleted differential as its control.

**MAY NOT — no model call of any kind.** No new episode, no re-sampling, no new draw, no change of population, arm,
tier or constants. The agent's output is FIXED at the sha above; this amendment re-runs the *checker*, never the
agent. **Zero model tokens are authorized by this amendment and zero are expected.** If any step turns out to need
a model call, this amendment does not cover it and the work stops.

**MAY NOT retro-score.** Landed manifests are not rewritten; the morning line of record is not re-run against
altered artifacts; the diagnostic is reported as a separate, labelled table.

**MUST be symmetric.** The procedure applies to **every** episode in the campaign whose class is `SCREEN` or whose
`check.screen` list is non-empty — not to a cell selected for its effect. Enumerated at the artifact across BOTH
state roots (`~/bench/state` and `~/bench-a8/state`, all `ep-*/manifest.json`) before this text was written:
**exactly one such episode exists in the whole campaign** — `bench-a8 · problem_112 · B · a2 · ep-6b5540c0 ·
SCREEN · ['iso_helper_lemmas: set_option@1']`. The symmetry requirement is therefore satisfied trivially, and that
fact is itself the record that no selection took place.

---

#### 9.4 · THE PRE-COMMITTED REPORT — both branches, written before the check

**If the stored body PASSES the full gate under §9.2 (and its deleted-pragma control agrees):** report, labelled
DIAGNOSTIC, that `a2` would read **11/15** against `a0`'s 10/15 on U15 at the Opus tier; that the contrast becomes
`a0`-only `= 0`, `a2`-only `= 1`, `|b − c| = 1`, **still INDISTINGUISHABLE** under the registered rule
(`|b−c| < 5`); and that the registered `≥ 2` contingency **does not fire** (§9.1). The conclusion I will draw, and
I am writing it now so it cannot be improved later: *the headline RATE of the salt arm rested on an unevaluated
cell; the NULL did not.*

**If the stored body FAILS the full gate:** report the class it earns and its axiom sets; `a2` = 10/15 stands
confirmed by measurement rather than by refusal; the screen cost the campaign nothing on this cell; and the same
`≥ 2` contingency still does not fire.

**If the two differential arms DISAGREE:** the pragma had semantic content, the refusal is vindicated on its
merits, the screen's whitelist is *not* widened (§9.5 is withdrawn), and that is the headline of the diagnostic.

**In every branch:** report both arms, the pinned shas, the exact `check.json` produced, and the enumeration of
§9.3 showing that one screened cell existed and one was examined.

---

#### 9.5 · THE SCREEN CHANGE — registered here, NON-RETROACTIVE, red-first, and contingent on §9.4

If and only if the differential arms agree, `ALLOWED_SET_OPTION` is widened by exactly one clause: an option under
the **`linter.` namespace** with a boolean literal, in **both** the bare and the `in` forms. Nothing else moves —
`debug.*`, `compiler.*`, `maxRecDepth` outside the existing clause, and every other `set_option` stay refused.

The change lands **only with a red-first gate**, in this repo's standing form: new `screen.py` self-test cases that
**FAIL against the current file and PASS against the changed one** — (a) `set_option linter.deprecated false` bare
and (b) in `in` form are admitted; and cases that must stay red in both — (c) `set_option debug.skipKernelTC true`
bare and (d) in `in` form are refused, (e) a non-`linter` option outside the resource whitelist is refused. The
change applies to **future runs only**: it does not alter the class of any landed episode, and the campaign's one
screened cell keeps its `SCREEN` manifest whatever the diagnostic finds.

---

#### 9.6 · THE CONTINGENT `a1` ARM — the registered rule, applied honestly

The helm's routing says *"fire the registered `a1` arm under it."* Applied under the criterion above, **the
registered `a1` arm does not fire**, and it does not fire in either branch of §9.4, because its trigger is
`(a2-only) − (a0-only) ≥ 2` and the arithmetic of §9.1 caps the reachable value at **+1**. Firing it anyway would
not be firing *the registered arm* — it would be adding an unregistered arm after seeing the data, which is the
precise thing the contingency was written into amendment 5 to prevent. **I am not inventing a reach to get there.**

That is a report to the desk, not a refusal to work: **if `a1` at the Opus tier is wanted, it is wanted for a
different and nameable reason** — to test whether the tier's +2 is arm-independent across all three arms, i.e.
whether the one separation this campaign has measured is a property of the model at every rung. That is a NEW
question, it needs its OWN dated amendment with its own prediction registered before its first call, and it prices
off the measured amendment-8 basis at **≈13 M metered / ≈2.5 h** for one 15-problem arm (stage A + stage B, both
arms' Opus per-episode costs). It is not authorized by this amendment and no part of it runs under this one.

---

#### 9.7 · Price, mechanism, and the stop rule

**Model tokens authorized: ZERO.** Compute is the Studio's existing shared Lean build (`~/lean-shared/clever`,
toolchain `leanprover/lean4:v4.27.0`, mathlib `a3a10db0…`) driven by `check.py` at its landed pin
`9aa58095579dfc7d12cb0c727c23c7a6dffe7efaa0b0ba0b76111cd7dd767f8b`. Wall is bounded by two module compiles.
**Stop rule with its mechanism, not a sentence:** if either compile exceeds 15 minutes it is killed at the shell
and the branch is reported as INCONCLUSIVE rather than resolved in either direction — an unfinished compile is not
a verdict, and a diagnostic that cannot finish must say so rather than inherit the refusal's answer.

**Merge rule (the Captain's law):** merged to `master` on green, abandoned on red, and the ruling folded in
whenever it comes. The registered text above is never edited after the fact — corrections are appended.
