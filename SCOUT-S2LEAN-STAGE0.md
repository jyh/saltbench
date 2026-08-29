# SCOUT — S2-LEAN STAGE 0: the CONTROL protocol on CLEVER (plain · placebo) — DRAFT v2 AFTER REFUTER PASS 1 (not yet the freeze: pass 2, the run-shaped dry and the Studio controls are owed before the dated freeze commit)

**To be frozen 2026-08-29, bench seat, BEFORE any model call on this substrate.** Authorised by the scout's decision
rules (`seat/briefs/2026-08-28-DELEGATION-morning-council-only.md` §1, in force on the Captain's word 20:3x):
**F1** resolved the S1 fork to S2-Lean / CLEVER first; **F2** — the dated freeze commit IS the authorization,
controls before treatment, treatment arms as dated amendments before their own first call; **F3** reads the
control result; **F4** Sonnet first; **F5** an uncovered result is a HOLD with a fallback row, never an
improvised arm. Everything not stated here is inherited from `SCOUT-STAGE0.md` (S1) as amended — the agent,
the metering, the termination typing, the driver rules — **except where S1's sentence presumes the container**
(see §4: the S1 container sentences — `--network none`, `docker exec` scoring, "CHECK 2b in every container" —
do not hold on this substrate and are replaced here). `harness/` is the normative form. The source read behind
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
  its unflagged subset AND without the NL-leaked id — only the first is read against the band (§2).
- **The isomorphism shape is strict**: a docstring-faithful spec that is strictly stronger than the human's (the
  human spec has a don't-care region) is provably NON-isomorphic (kernel-checked on problem_0, unflagged). F3 thus
  measures "reproduced the human's exact boundary". §2 pre-registers a blind B-failure TRIAGE so a low rate can be
  read as a tier floor only if the failures are the agent's.
- **The axiom audit and the kernel replay are the scout's, not CLEVER's** — the reference checker accepts any
  axiom and never re-checks the module.

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
- **A problem file is a FULL SOLUTION** (natural-language spec, the human `problem_spec`, the `generated_spec`
  header with body `sorry`, the `spec_isomorphism` theorem with proof `sorry` — in EVERY file; no isomorphism
  proof ships — the `implementation` and its `correctness` proof, `#test` cases). **The agent never sees a raw
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
   by a word list); then **collect the axioms** of the stage's audited declarations from the replayed environment:
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
`s2-landings.log`; the driver's synthetic rows use `<none>` and 0. The artifact adds `task.lean`, `bodies.json`,
`canonical.lean`, `check.json` (with its `class`), `env_probe.txt`, `rt.log`; the manifest adds `substrate`, `stage`,
`lean_toolchain`, `leanproj_sha`, `view_sha256`, `frozen_sha256`, `check`, `passed`, and for stage B `a_episode`,
`a_bodies_sha256`, `a_termination`.

## 7 · Order of operations (the runbook, as the operator runs it from tmux over ssh)

1. This text + `harness/` committed; refuter pass 2 (closure of pass 1 + fresh lenses on the repaired files);
   `--dry` and the RUN-SHAPED dry (stub claude that writes bodies, so extract → assemble → check → audit RUN) on
   the seat and on the Studio; then the **dated freeze commit** (retitle from DRAFT) = the authorization (F2).
2. Studio prep (no model): `lean_shared_build.sh` (export → `~/lean-shared/clever`, cache, `Imports` build, the
   assertions, the three shas); `sync_studio.sh` (views excluded; receipt over the S2 pinned files); the control kit
   shipped, `s2_controls.sh` → `~/bench/state/s2-controls.json` (CONTROLS PASS required), the kit deleted and its
   absence asserted; `~/.claude-bench/settings.json` = `settings.s2.json` (sha asserted per episode).
3. `stage_views.sh ship A` (A.lean + frozenA.json only; `check` shows frozen = 0, C = 0). Smoke probes
   `smoke_s2.sh` (arm `s0`, `SMOKE(…)`, never scored): S1 canary + PATH · S2 network (curl, a written `fetch.py`, a
   Lean `#eval IO.Process.run curl` through `rt` — all must FAIL) · S3 reads (`~/bench/harness/arms/a1.md` and
   `~/.claude-bench` DENIED; `~/lean-shared/clever/lakefile.lean` readable) · S4 writes (`.lake/probe` DENIED; cwd
   writable) · S5 the compile through `rt` from the agent (wall recorded). Five `SMOKE PASS` lines carrying this
   freeze's `episode_s2.sh` sha are asserted by the driver before it starts.
4. `run_s2_stage0.sh A 30` (60 episodes) · when every A has landed (`has_terminal` over the 60 (task, arm) pairs),
   `stage_views.sh ship BC` · `run_s2_stage0.sh B 30` · `run_s2_stage0.sh C 30` (C-dead skipped) — each under
   caffeinate in tmux `bench:run`; the seat's watch emits a liveness line per landing.
5. `s2_morning_line.py ~/bench/state 30`: per stage and arm, passed / landed / k; **the F3 line** (plain, stage B,
   over k) with its band; beside it the unflagged rate, the rate without problem_90, the recall instrument
   (`f_high` and whether the band is read), the C line over the C-eligible subset, orphan/superseded/view-dead rows,
   failure classes (KERNEL_REJECTED, STATEMENT_ALTERED, AXIOMS_FAIL, COMPILE, SCREEN), the per-stage `a0` p90 the cap
   rule consumes; the B-failure triage follows from the seat. **No p-value, by design.**

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

---

*Nothing below this line existed before this substrate's first model call. Amendments are appended,
dated, with their reason — never edited into the text above. The salt arm registers here.*

---
