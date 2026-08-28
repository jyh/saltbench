# Wave 1 — the gate: design block (v2)

**Status: DESIGN, NOT BUILT.** Re-frozen 2026-08-27 21:1x after a 6/6 REPAIR-THEN-FIRE
refuter pass on v1 (`saltbench 59660c0`; verdicts at `seat
fleet/REFUTER-saltbench-wave1-gate-2026-08-27.md`). Amended before any model call, which
the pre-registration's own rule permits and which it forbids afterwards.

## Amendment record — what v1 got wrong

v1's bones survived (shared gate code path, scoring refused patches, deterministic draw).
Four things did not, and **all four were things I would have defended**:

1. **§3.4 was mechanically biased AGAINST my own treatment arm** — the gate's regression
   baseline was `C`, the grader's is `C + T`, and `T` rewrites test expectations.
   Measured: ≥9.5% of the drawn set fail a *correct* patch under v1's rule. I had asked
   refuters for a cheaper explanation of a **win**; this is a cheaper explanation of a
   **loss**, and I never asked for that direction. Rewritten in §3 below.
2. **"Only the accept/refuse decision differs" was false**, refuted by two other lines in
   v1 itself. At least four things differed, and the cheapest non-mechanism explanation —
   **REFUSE-ONCE**, a content-free gate that refuses the first patch and buys a second
   draw — reproduces the entire effect this screen is powered to see. §5 and §7.
3. **§6's "win-either-way" had no adverse outcome.** Every terminal state read
   favourable. I had congratulated myself for registering both outcomes as *interesting*;
   registering both as interesting is not registering one as **adverse**. Now in
   PRE-REGISTRATION §6.
4. **The enumerated input struct was never enumerated**, so the leak control I named did
   not exist; and the REFUSE reason was unconstrained free text — a one-way channel into
   the treatment arm, wider than the input struct and entirely unaudited. §4 and §6.

📌 One gap in the pass itself, recorded because it is now mine: R1 marked §3.4 FATAL "with
the replacement rule spelled out below" and no rule follows. The replacement in §3 is
therefore my design, not a refuter's, and should be attacked as such.

---

## 1 · What the gate is

The treatment arm is the same agent, same model, same **enforced token budget**, plus a
gate between "the agent proposes a patch" and "the patch is submitted for scoring".

```
   agent proposes patch P_k
          │
          ▼
   ┌───────────────┐  REFUSE(typed reason) ──► round k+1, up to a FIXED K (§5)
   │   THE GATE    │
   └───────────────┘
          │ ACCEPT  ── ends the episode; P_k is the submitted patch
          ▼
   held-out scoring (official SWE-bench harness, pinned)
```

⛔ **The gate is never GIVEN held-out test identities, the gold patch, the gold test
patch, `hints_text`, or any held-out status.** It can *re-derive* some test identities by
running the repo's visible suite — **so can the control agent, from the identical
checkout, and that symmetry, not ignorance, is the protection.** v1 claimed ignorance and
was wrong: measured over the 500-row split, 99.55% of `PASS_TO_PASS` ids name a function
that already exists at base commit.

---

## 2 · The failure mode this design exists to prevent

***A gate that refuses everything looks excellent on any metric computed over accepted
patches.*** So the outcome is defined over **all attempted tasks**:

> **`solved(task, arm)` := the episode ended with an ACCEPTED proposal, and the official
> harness reports `resolved=true` for THAT proposal.** If the episode ends with no
> accepted proposal — however many revisions occurred — the submitted patch is **empty**
> and the task scores **unsolved**, in both arms.

A gate that refuses everything therefore scores **zero**, not perfect.

⛔ **Only the submitted attempt enters the primary statistic.** Every other scored
proposal is *shadow*. v1 mandated scoring every patch and never said which score counted;
two implementers would have built "the submitted one resolved" and "any one resolved" from
the same text, and the second gives the treatment arm k lottery tickets to the control's
one.

⛔ **Enforced structurally, not by convention:** on every REFUSE the harness reverts the
working copy before the next round, and the string handed to the scorer is built from the
recorded accepted-patch slot — **never from a terminal `git diff`**. A refused edit left
in the tree would otherwise BE the exhaustion diff, and it would score with no error and
no warning.

### The ledger (one record per `(task_id, arm)` episode, written before any scoring)

```
{task_id, arm ∈ {control, treatment, sham}, run_id, model_snapshot_id, temperature,
 harness_commit, image_digest,
 attempts: [ {k, patch_sha256, agent_tokens_in/out, budget_consumed_at_proposal,
              gate_input_sha256, gate_verdict ∈ {ACCEPT, REFUSE}, gate_reason (typed, §6),
              gate_tokens_in/out, gate_verdict_time,
              submitted: bool,
              held_out: {resolved, f2p_pass[], f2p_fail[], p2p_pass[], p2p_fail[],
                         harness_exit, report_path, scored_at}} ],
 terminal: {reason ∈ {ACCEPTED, BUDGET_EXHAUSTED, ROUNDS_EXHAUSTED, NO_PATCH, HARNESS_ERROR},
            submitted_attempt_index}}
```

**Invariants asserted by the analysis script, not by convention:**
- **I1** exactly one attempt has `submitted=true`, or `submitted_attempt_index` is null.
- **I2** `gate_verdict_time < held_out.scored_at` for every attempt — all held-out scoring
  runs in a **post-episode batch** over stored blobs. *This ordering is the structural,
  checkable proof that no score reached the gate; v1 stated the requirement with no
  mechanism.*
- **I3** identical `patch_sha256` within a task never receives differing verdicts.

### The refusal table, with the denominator v1 omitted

| quantity | why |
|---|---|
| refusals issued (attempt-level **and** deduped by `patch_sha256`) | activity, not inflatable by a stubborn agent re-proposing |
| attempts refused **that would have resolved** | the gate's cost — *relabelled: v1 called these "solved tasks destroyed", but a refusal followed by an accepted resolving revision destroyed nothing* |
| `tasks_destroyed` := tasks with a correct refusal that ended unsolved | the task-level cost the old label falsely promised |
| **`base_fail_rate`** := proposals that would NOT resolve ÷ **proposals the gate ADJUDICATED in the treatment arm** | ⭐ free (§2 scores every patch), and it is the EXACT chance level for a rate-matched content-blind refuser on the same stream |
| **`base_fail_rate_round1`** := the same over the SHARED `P₁` proposals only | unconditioned by the gate and identical across arms — the non-circular reference |
| **`lift`** := refusal precision ÷ `base_fail_rate` | ⛔ **THE KILL v1 MISSED: a content-blind gate attains precision equal to the base failure rate, which on this substrate exceeds ½ — so a coin-flip gate reports "most of my refusals were correct".** Precision is reported **only** alongside `base_fail_rate` and `lift`. |

⛔⛔ **THE DENOMINATOR WAS WRONG IN v2 AND IT WAS WRONG IN BOTH DOCUMENTS, DIFFERENTLY**
(helm, 21:22, while the second pass ran). DESIGN v2 defined the base over **both arms'**
scored attempts; PRE-REGISTRATION §6 compared precision to the **control arm's**
patch-failure rate. Different denominators, different populations — **and neither is the
right one, so "change one of the two sentences" would have left a wrong definition
standing.**
🔑 ***THE GATE ONLY EVER ADJUDICATES TREATMENT-ARM PROPOSALS, SO THE CHANCE LEVEL IS THE
FAILURE RATE OF THE STREAM IT ACTUALLY SAW.*** A pooled rate mixes in control proposals the
gate never judged; the control's own rate is a different population generated under a
different round structure after round 1.
⚠️ **Two words also removed an ambiguity that invited the error: `base_rate` never said
whether it counted RESOLVES or FAILURES, and `lift` was written as `precision ÷ (1 −
base_rate)` — so the reader had to infer the polarity. It is `base_fail_rate` now, and
lift divides by it directly.**
📌 A residual, named rather than smoothed: the adjudicated stream is itself shaped by the
gate, because round-2+ proposals exist only where it refused. `base_fail_rate_round1` is
reported beside it precisely because `P₁` is shared and unconditioned — if the two
disagree materially, the conditioning is visible instead of silent.

Refusal precision is reported **both** patch-level (pooled) and **task-level** (first
refusal only), with the refusals-per-task distribution, so one pathological task cannot
drive the ratio. Intervals are task-level or cluster-robust; never a naive binomial on
pooled patches.

---

## 3 · What the gate may look at — and the regression rule, REWRITTEN

1. **The patch applies** and the project still builds/imports.
2. **The visible tests** the agent could already run.
3. **Synthesized checks** from the issue text and touched code (§5 meters their cost).
4. **Regression surface** — see the rewrite immediately below.

### ⛔ §3.4 REWRITTEN — v1's rule refused correct patches

**The defect, measured:** SWE-bench applies the gold test patch `T` and *then* the
prediction. Where `T` rewrites an existing test's expectations, the base-commit copy of
that test encodes the **old** behaviour — so the very fix the issue asks for makes it
fail, and v1's rule ("tests that passed before the patch must still pass") fires on a
**correct** patch. ≥4 of the 42 then-drawn tasks (≥9.5%) are in this class;
`pytest-dev__pytest-5809` is fully worked: the base test asserts `lexer=python3`, `T`
replaces it with `lexer=text`, and the correct fix sends `text`.

**The gate cannot simply adopt the grader's baseline — `T` is held-out.** So the rule
changes shape instead:

> **A regression failure is a refusal only if it is UNDECLARED.** With each proposal the
> agent may declare a set of tests whose current expectations it believes the issue
> requires it to change, each with a one-line justification. The gate refuses on:
> patch-does-not-apply, build failure, a failed synthesized check, or a regression in a
> test **outside** the declared set. A failure **inside** the declared set is recorded,
> never refused.

Three properties, stated because they are what make this defensible rather than
convenient:
- **It removes the mechanical bias** — the ~9.5% class is exactly the case where a correct
  patch must change a test's expectation, and the agent can now say so.
- **It is symmetric.** The declaration channel exists in *both* arms (the control's gate
  accepts regardless), so it is not a capability handed only to the treatment arm.
- **It moves the gate closer to the actual claim** — not "nothing may change" but "state
  what you changed and why", which is the discipline the method is about.

⚠️ **The residual, named rather than hidden:** an agent that changes behaviour and fails
to declare it is still refused, correctly by this rule and incorrectly by intent. That is
now a **measured quantity** (`refusals_on_undeclared_expectation_change`), not an unnamed
bias.

📊 **And the class is measured post hoc regardless.** For every drawn task, compute — from
`T`, in the analysis only, never shown to gate or agent — `rewrites_existing_test ∈
{0,1}`, and report the primary result **stratified on it**. If the gate's effect lives
entirely in one stratum, that is visible instead of confounding.

⛔ **Not available to the gate, as an ALLOWLIST (v1 had a denylist and it admitted
`hints_text` — non-empty in 71% of drawn tasks, up to 9,699 chars):** the gate receives
exactly the struct in §4 and nothing else.

---

## 4 · Structural separation — the struct v1 promised and never wrote

```python
@dataclass(frozen=True)
class GateInput:
    instance_id: str          # opaque label only
    problem_statement: str    # byte-identical to the agent's
    candidate_patch: str
    declared_expectation_changes: tuple[DeclaredChange, ...]   # §3.4
    repo_snapshot: Path       # worktree ONLY — no .git, no remotes, no refs
    build_ok: bool
    build_log_tail: str       # bounded, 4 KiB
    base_test_report: TestReport
    post_test_report: TestReport
    synth_checks: tuple[CheckResult, ...]   # produced INSIDE the gate
    budget_remaining: Budget
```

Three executable checks, because an enumeration without a failing input is decoration:

- **CHECK 1** — `__post_init__` asserts the field set equals a frozen literal, and
  `GateInput` is constructible **only** by a builder whose sole dataset argument is
  `instance_id`. *The dataset record never enters the gate process.* v1's "adding a field
  is a diff a reviewer sees" was the wrong control: the upstream record is one flat dict
  carrying `patch`, `test_patch`, `hints_text` and both id lists together, so
  "pass the instance to the gate" leaks everything **without adding a field**.
- **CHECK 2** — `git -C repo_snapshot rev-parse HEAD` must return **non-zero**. The
  snapshot carries no history. *SWE-bench mirrors retain full history and branches, and
  `base_commit` is an ancestor of the merged PR in that same object store, so a plain
  checkout hands `git log --all -p` the gold patch and the gold test patch.*
- **CHECK 3** — the positive control: a test that builds a `GateInput` carrying
  `test_patch`, `hints_text`, or a `.git` directory and asserts the builder **RAISES**.

---

## 5 · Compute parity — by construction, not by permission

⛔ **v1 said "identical token/call budget" — two units joined by a slash, picking
neither — and then conceded "equal budget is not equal consumption", which is the
confound, reported rather than controlled.**

- **(a) Parity is a HARD TOKEN CAP:** input + cache-write + cache-read + output, per task,
  enforced by the harness, identical across arms. The call cap is secondary and also
  stated. *These cannot both bind: a cache read costs ~0.1× and a cache write 1.25×, a
  12.5× spread, and the treatment arm's revision loop re-sends a long stable prefix every
  round — so an equal token cap systematically buys it cheaper tokens, and an equal dollar
  cap systematically buys it more of them. The enforced invariant is TOKENS; dollars are
  reported.*
- **(b) Every model call made inside the gate is metered to the arm that made it.**
- **(c) EQUAL PROPOSAL ROUNDS BY CONSTRUCTION.** A fixed **K = 3** rounds per task in
  **both** arms. The treatment arm's rounds after the first are gate-triggered with a
  typed reason; the control arm's are self-directed with a **fixed, content-free** prompt.
  ⭐ **This is the same-code-path doctrine applied to the revision loop instead of only to
  the accept/refuse call, and it is what makes the comparison mean anything: attempt count
  is then equal by construction, and the ONLY difference is whether the revision trigger
  carries information — which is the claim under test.**
- **(d)** If the gate is model-backed, the control arm's ACCEPT-wired gate **runs the
  identical synthesis call and discards the result**, so tokens and latency match.

Reported always, as distributions and never only as means: per-task tokens by class, tool
calls, wall-clock, **fraction of the ceiling actually consumed**, and a typed
**termination reason** per task per arm. *That single field settles whether "equal budget"
was parity in permission or in behaviour.*

---

## 6 · The REFUSE channel is typed — no free text

v1 governed what the gate could *look at* and left its **output** unconstrained: free text
from a model, delivered to the agent, in the treatment arm only.

```
Reason = PatchDidNotApply
       | BuildFailed(log_tail)                     # must be a suffix of build_log_tail
       | RegressionDetected(ids)                   # ids ⊆ base_test_report.ids
       | UndeclaredExpectationChange(ids)          # ids ⊆ base_test_report.ids
       | SynthCheckFailed(check_id, observed, expected)
```

Enforced at construction: a `RegressionDetected` carrying an id absent from
`base_test_report` **must raise** — that is the positive control. Every emitted reason is
logged verbatim for post-hoc audit.

*Why a type and not a policy: "the maintainer's suggestion is to route the method kwarg
there" (lifted from `hints_text`) and "test_config.py::test_csv_regex_error still fails"
(recoverable from the visible suite) are indistinguishable from outside the gate. Only the
first is a leak, and no amount of reviewing free text separates them reliably.*

---

## 7 · The arms — and the sham that v1 lacked

| arm | gate | rounds |
|---|---|---|
| **control** | hard-wired ACCEPT (runs and discards any synthesis, §5d) | K, self-directed |
| **treatment** | the live gate | K, gate-triggered |
| **sham** | refuses with a **content-free** reason, at a per-task count matched to the treatment arm's realised refusals, **no test execution** | K, sham-triggered |

**`treatment − sham` is the gate's information content. `sham − control` is the
forced-revision effect.** Without the sham arm, REFUSE-ONCE explains the whole result, and
a best-of-2 gain on this substrate is the same magnitude as the only effect this screen is
powered to detect — *the alternative explanation is not merely unexcluded, it is sized to
fully produce the finding.*

⭐ **The first proposal `P₁` is generated once per task and SHARED across all three arms.**
Exact pairing, no sampling noise in the discordance, and the arms differ only from round 2.

⛔ **If the sham arm is unaffordable, the headline claim is DOWNGRADED in advance** to
*"gating-or-forced-revision beats a single submission"*, and the decomposition is deferred
— the same discipline the pre-registration already applies to the capability floor.

---

## 8 · What a refuter should attack next

1. Trace every `GateInput` field for correlation with held-out identities.
2. Diff control/treatment/sham code paths for any difference beyond the verdict.
3. Is the token cap enforced on the sum, including gate calls?
4. Can a task score solved without the official harness reporting `resolved`?
5. Does any statistic go undefined at 0% or 100% refusal? (`accepted-and-failed` has an
   empty denominator at 100% and must print `n/a`, never `0%`.)
6. **Is there a cheaper explanation for a win than "gating helps"** — and, the question v1
   forgot, **for a LOSS?**
7. Does the §3.4 declaration channel hand the treatment arm a capability, or only a voice?

---

## 9 · What is NOT designed here

The container image build and the task-runner plumbing.

⛔ **v1 also deferred "the scorer" and "the container strategy" as places where validity
does not live. That was false on this substrate and is struck:** the scorer *is* the
definition of the dependent variable, and the container is exactly where the git-history
leak lives. Both are now specified — the official harness pinned by commit and image
digest in the pre-registration, and the no-history snapshot in §4 CHECK 2.
