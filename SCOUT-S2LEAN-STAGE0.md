# SCOUT — S2-LEAN STAGE 0: the CONTROL protocol on CLEVER (plain · placebo) — DRAFT FOR REFUTATION (not yet the freeze: refuter pass, Studio checker controls and smoke probes owed before the dated freeze commit)

**Frozen 2026-08-29, bench seat, BEFORE any model call on this substrate.** Authorised by the scout's decision
rules (`seat/briefs/2026-08-28-DELEGATION-morning-council-only.md` §1, in force on the Captain's word 20:3x):
**F1** resolved the S1 fork to S2-Lean / CLEVER first; **F2** — this dated freeze commit IS the authorization,
controls before treatment, treatment arms as dated amendments before their own first call; **F3** reads the
control result; **F4** Sonnet first; **F5** an uncovered result is a HOLD with a fallback row, never an
improvised arm. Everything not stated here is inherited from `SCOUT-STAGE0.md` (S1) as amended — the agent,
the hermeticity assertions, the hook and audit, the metering, the termination typing, the driver rules —
and `harness/` is the normative form. The source read behind the choice: `S2-SOURCE-READ-2026-08-29.md`.

## 0 · What this stage is for — and what it cannot show

Two control arms, PLAIN (`a0`) and PLACEBO (`a1`), on CLEVER, so that the **F3 quantity exists**: the
fraction of drawn problems on which the plain arm's *agent-written specification is proven isomorphic to
the hidden human specification*, kernel-adjudicated — and its metered distribution, whose `a0` p90 the cap
rule consumes for the salt arm. It measures nothing about the salt method.

**Cannot show:** everything S1's §0 names (mechanism; arm-blindness by construction; a closed network;
sampling variance vs arm effect; contamination — HumanEval is memorised and CLEVER's skeleton is public,
but **the isomorphism proofs are not** — 0 of 161 published per the source read, so a proven isomorphism is a
kernel fact about this run, not a recalled artifact); plus: **the reference "ground-truth" specs are
disputed** (80/161 flagged buggy by arXiv 2605.23772 — the flagged list is recorded in §2 if obtainable and
the F3 quantity is reported over the drawn set AND over its unflagged subset); and **the axiom audit is the
scout's, not CLEVER's** — the reference checker accepts any axiom.

## 1 · The substrate, pinned

- `trishullab/clever` at commit **`8348039a7ff7730a126d761e71d0439735eeb3e2`** (MIT). Lean
  **`leanprover/lean4:v4.27.0`**; mathlib **`a3a10db0e9d66acbebf76c5e6a135066525ac900`** (tag v4.27.0);
  the full `lake-manifest.json` pins the rest (batteries `b25b36a7`, aesop `cb837cc2`, plausible `009dc1e6`
  — `#test` is Plausible's command). All three pins are lines in `HASHES.txt`.
- **A problem** (`src/lean4/human_eval/problem_k.lean`, 161 files, k = 0…160) is a FULL SOLUTION: the
  natural-language spec (signature + docstring + examples), the human `problem_spec`, a `generated_spec`
  header with body `sorry`, the `spec_isomorphism` theorem with proof `sorry`, the `implementation`
  signature and body, `#test` cases, the `correctness` theorem and its proof. **The agent never sees a raw
  file.** `harness/s2lean/build_views.py` (self-tested: 161 parse; no implementation, proof or
  ground-truth spec leaks into any stage-A view) emits per problem:
  - **A.lean** — stage A: NL spec + `generated_spec` header, body `sorry`. Ground truth ABSENT.
  - **C.lean** — stage C: NL spec + `problem_spec` (ground truth) + `implementation` signature, body
    `sorry` + `#test` cases + `correctness` theorem, proof `sorry`.
  - **frozen.json** — every statement the agent may not change, verbatim; **frozenA.json** — the
    ground-truth-free subset for stage A.
  - **B.lean** is assembled at run time from `frozen.json` + THE SAME ARM's stage-A `generated_spec` body:
    NL spec + `generated_spec` (frozen, filled) + `problem_spec` + `iso_helper_lemmas` slot +
    `spec_isomorphism` theorem, proof `sorry`.
  Each view's sha is pinned (`view-A`, `view-C`, `frozen` lines in `HASHES.txt`); `episode_s2.sh` refuses a
  view whose sha is not the pinned one.
- **The three stages, per problem and arm:** **A** write the spec blind (the statement — the salt shape's
  first half); **B** prove `spec_isomorphism` against the revealed human spec with the generated spec
  frozen (the kernel adjudicates the statement); **C** implement and prove `correctness` against the human
  spec. **The F3 quantity is stage B.** A and B are both metered; a problem's stage-B episode runs only if
  its stage-A body exists (a stage A that produced no body is a stage-B NOT PROVEN, not a skip).
- **Data staging (the ground truth is never on the host while an arm is writing a spec blind):** the seat
  ships `A.lean` + `frozenA.json` only (`stage_views.sh ship A`); every stage-A episode of the draw lands;
  then the seat ships `frozen.json` + `C.lean` (`ship BC`); `episode_s2.sh` REFUSES a stage-A episode if a
  `frozen.json` exists on the host, and refuses ANY episode if `human_eval/` or `sample_examples/` (the
  full solutions) exist in the shared project or their oleans in its build.

## 2 · Draw, subset, and the F3 reading

- **Draw:** the 161 ids sorted by `sha256(id + "saltbench-s2lean-stage0-2026-08-29")`
  (`harness/s2lean/draw.py`); **stage 0 runs the first k = 30** (the first five: `problem_109, 34, 73,
  90, 159`). Extending k is an amendment; a stop is reported with the k reached.
- **F3** is read on the PLAIN arm over the k drawn problems: proven / k, an unrun or unlanded problem
  counting as not proven. **≥ 80 % ⇒ HOLD** (too easy at this tier; report for council) · **20–80 % ⇒ run
  the salt arm** (registered as a dated amendment with its profile) · **< 20 % ⇒ HOLD** (a floor, a
  finding about the tier). The same rate over the unflagged subset is reported beside it; if the two
  fall in different bands, that is an uncovered result ⇒ **HOLD with the fallback row** (F5).
- **The flagged-spec list, from the source (arXiv 2605.23772 Table 1, read from the PDF; 80 unique ids):**
  5 7 12 20 23 24 26 27 34 36 39 44 45 47 49 50 51 62 64 65 66 67 68 69 71 72 75 78 79 81 84 85 86 88 89 90
  91 93 94 95 97 98 99 100 103 104 105 106 108 109 110 111 114 115 116 117 121 122 125 126 129 130 132 134
  138 139 140 143 144 150 151 152 153 154 155 156 158 159 161 163 (48 Lean-encoding hazards, 34 semantic;
  5 double-typed). **The leaderboard's four excluded ids are not published on the page; the paper §4.2 names
  them: 32, 39, 123, 160** (Collatz-conjecture-hard, infinitely-many-Fibonacci-primes-hard, a broken fixed
  helper, a missing rational-root precondition). Recorded in `harness/s2lean/flagged.json`. The F3 quantity
  is reported over the drawn k AND over the drawn unflagged subset; the four excluded ids are EXCLUDED from
  the draw's denominator only if drawn (a pre-stated exclusion, arm-independent, recorded).

## 3 · "Solved" — the scout's checker, kernel-decided, axiom-audited

`harness/s2lean/check.py`, per stage per episode, on the Studio, no model:
1. **extract** (`extract.py`) ONLY the agent-writable bodies from the agent's `task.lean` by the section
   markers — A: `generated_spec_body`; B: `spec_isomorphism_proof` + `iso_helper_lemmas`; C:
   `implementation` + `correctness_proof` + `correctness_helper_lemmas`. Every STATEMENT is taken from
   `frozen.json` at assembly, so an edit outside the bodies is structurally discarded (statement
   immutability by construction, not by diff);
2. **forbidden tokens in the bodies:** `axiom unsafe implemented_by extern opaque sorry admit set_option`;
3. **assemble** (`assemble.py`) the canonical file and append `#print axioms` for the stage's
   declarations (A: `generated_spec`; B: `generated_spec`, `spec_isomorphism`; C: `implementation`,
   `correctness`);
4. **`lake env lean <file>`** in the shared project (timeout 900 s); rc must be 0;
5. no `declaration uses 'sorry'` for this file;
6. **every `#print axioms` line ⊆ {`propext`, `Classical.choice`, `Quot.sound`}** — `native_decide`'s
   `Lean.ofReduceBool` and any user axiom fail here.
`passed` = all six. Stage A's `passed` means "the spec elaborates"; stage B's means "the isomorphism is
proven"; stage C's "implementation + correctness proven". **This is the reference checker (`lake lean` +
sorry-grep) plus the axiom audit F1 requires, plus statement immutability plus the token screen.** The
positive control (the shipped gold bodies of `problem_0` pass B and C), the negative control (a `sorry`
body fails), and the axiom control (a `native_decide` proof fails) are driven on the Studio before the
first scored run and recorded (§7).

## 4 · The environment — native Lean, no Docker (the 13:3x ruling's consequence for S2-Lean)

The agent runs as in S1 (real HOME, `~/.claude-bench`, the login PATH, the same flags and disallowed
tools). **The working copy** `/Users/jyh/work/<ep>/repo` is a Lake project: `lakefile.lean`,
`lake-manifest.json`, `lean-toolchain`, `Imports/` (source) copied from the shared project, `task.lean`
(the view), and **`.lake` → a symlink to the shared prebuilt build** at `~/bench/lean/clever/src/lean4/.lake`
(mathlib + `Imports` oleans; built once by `lake exe cache get && lake build Imports.AllImports` — the
human_eval and sample_examples targets are NEVER built, so no solution olean can be imported). CHECK 2b runs
on the working copy (no `.git` anywhere). The wrapper `rt` runs `<cmd>` in the project with `~/.elan/bin`
prepended and `timeout 590`; the agent's own PATH has no elan, so `lean`/`lake` exist only through `rt`.
The hook and the audit gain: `lake update`, `lake build`, `lake exe cache`, `elan`, and any path into
`~/.elan` are ESCAPE tokens (29-arm self-test). Before every episode the wrapper is exercised under the
agent's exact environment with an `import Imports.AllImports` probe, so the slow first Mathlib load is
the harness's, not the agent's.

## 5 · The arms

- **Prompt per stage** (`harness/s2lean/prompt_{A,B,C}.md`, pinned; identical across arms up to the
  episode path): A — write `generated_spec`, a `Prop` characterising exactly the docstring's behaviour;
  B — prove `spec_isomorphism`, helper lemmas allowed, statements fixed; C — implement and prove
  `correctness`, `#test` must pass, statements fixed. Each ends "when it compiles and you are satisfied,
  stop; the file is your answer."
- **BASE block** (`harness/s2lean/base.md`, 627 bytes rendered): the file to complete, the marker
  sections, `rt lake env lean task.lean`, no network, no `lake update`/`cache`, no git.
- **PLAIN `a0`** = BASE alone. **PLACEBO `a1`** = BASE + the SAME `arms/a1.md` as S1 (1,789 bytes, house
  conventions, no tool-mandating step, no verification vocabulary; profile registered in S1 §4) —
  reused unchanged so the placebo's price is comparable across substrates. `s0` = the canary.
- **The salt arm (`a2`)** is NOT frozen here. It registers as a dated amendment below the line, with its
  profile against the placebo's, only if F3 lands in 20–80 %.

## 6 · Metering, termination, artifacts — as S1

`meter.py` unchanged (message.id dedupe; governing sum incl. `modelUsage`; the audit). `--max-turns 40`;
`WALL_S` 5,400; `TOKEN_CEILING` 8,000,000 (safety only; stage 0 has no parity cap). Landings carry
`<ep> <problem> <stage> <arm> <term> <metered>` in `s2-landings.log`. The artifact adds `task.lean`
(the agent's file), `bodies.json`, `canonical.lean` (what the kernel judged), `check.json`, `env_probe.txt`;
the manifest adds `substrate`, `stage`, `lean_toolchain`, `view_sha256`, `check`, `passed`.

## 7 · Order of operations

1. This freeze + `harness/s2lean/` committed (HASHES pins views, arms, pins); one refuter pass
   (REPAIR-THEN-FIRE, amendments dated); the run-shaped dry (stub claude) and `--dry` on the Studio.
2. Studio prep (no model): elan → v4.27.0; CLEVER at the pinned commit; `lake exe cache get`;
   `lake build Imports.AllImports`; **remove `human_eval/` and `sample_examples/` from the shared
   project**; the three checker controls of §3, recorded in `s2-controls.json`.
3. Smoke probes through `episode_s2.sh` (arm `s0`, `SMOKE(…)`, never scored): A1 canary + PATH on a
   stage-A view; C-probe: `../rt lake env lean task.lean` from inside the agent (the wrapper and the
   Mathlib import from the agent's Bash tool). Asserted mechanically before the driver starts.
4. `stage_views.sh ship A` · `run_s2_stage0.sh A 30` (60 episodes) · `stage_views.sh ship BC` ·
   `run_s2_stage0.sh B 30` · `run_s2_stage0.sh C 30` — each under caffeinate in tmux `bench:run`.
5. `s2_morning_line.py`: per stage and arm, passed / landed / k; pairs with b, c, n_d and the sign-test
   null; **the F3 line** (plain, stage B, over k) with its band; the unflagged-subset rate beside it; the
   a0 stage-B p90 the cap rule consumes; removed rows; axiom-only failures (compiled, no sorry, axioms
   outside the allowlist — reported as their own class). **No p-value, by design.**

---

*Nothing below this line existed before this substrate's first model call. Amendments are appended,
dated, with their reason — never edited into the text above. The salt arm registers here.*

---
