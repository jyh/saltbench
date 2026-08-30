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
