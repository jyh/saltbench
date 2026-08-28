# Wave 1 — the gate: design block (v4)

**Status: DESIGN, NOT BUILT.** Re-frozen 2026-08-27 21:1x after a 6/6 REPAIR-THEN-FIRE
refuter pass on v1 (`saltbench 59660c0`; verdicts at `seat
fleet/REFUTER-saltbench-wave1-gate-2026-08-27.md`). Amended before any model call, which
the pre-registration's own rule permits and which it forbids afterwards.

## Amendment record — what v1, v2 and v3 got wrong (each item tagged)

v1's bones survived (shared gate code path, scoring refused patches, deterministic draw).
Four things did not, and **all four were things I would have defended**:

1. **§3.4 was mechanically biased AGAINST my own treatment arm** — the gate's regression
   baseline was `C`, the grader's is `C + T`, and `T` rewrites test expectations.
   **Re-measured at this hand on the CURRENT measured-50: 21/50 = 42%** have a gold test patch
   that deletes a line of an existing test file; **9/50 = 18%** delete a line containing
   `assert`/`==`/`expected`. ⛔ **v2 still said "≥9.5%", computed on the 42-task draw that cap 9
   REPLACED — I re-froze the draw and never re-derived the figure that motivated this very
   rewrite, understating the bias 2–4× in the sentence a write-up would quote.** I had asked
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
   ┌───────────────┐  REFUSE(typed reason) ──► round 2 (the treatment runs AT MOST TWO rounds, §7)
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
- **I3 — TREATMENT ARM ONLY.** Identical **`gate_input_sha256`** within a task never receives
  differing verdicts. ⛔ *FALSE BY CONSTRUCTION in the other two arms, and asserted by code: the
  sham's verdict is a function of ROUND INDEX (REFUSE at 1, ACCEPT at 2), so an agent
  resubmitting byte-identical bytes after a content-free refusal yields ONE input hash with TWO
  verdicts — a hard assertion failure on a reachable episode.* Control and sham verdicts are
  pre-registered functions of round index and asserted as such.
  ⛔ *v2 keyed this on `patch_sha256`, which forbade the redeclare-and-resubmit recovery §3.4
  exists to enable — the declaration is not part of the patch.*

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
**correct** patch. **21/50 = 42% (broad) / 9/50 = 18% (narrow) of the CURRENT measured-50** are in this class;
⚠️ **THE TWO PROXIES DIFFER BY 2.3× AND THE NARROW ONE MISSES MY OWN WORKED EXAMPLE** — so
`rewrites_existing_test` MUST be given a normative implementation in `analyse.py`, committed
BEFORE the first call, or it is a researcher degree of freedom in the one variable used to
detect the confound. ⚠️ *And stratifying a 50-task screen whose MDE is 15.7–28.7 points into
9/41 or 21/29 leaves NEITHER stratum powered: the stratification is a DIAGNOSTIC, not a
control, and says so.*
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
- **It removes the mechanical bias** — the 18–42% class is exactly the case where a correct
  patch must change a test's expectation, and the agent can now say so.
- **It is symmetric.** The declaration channel exists in *both* arms (the control's gate
  accepts regardless), so it is not a capability handed only to the treatment arm.
- **It moves the gate closer to the actual claim** — not "nothing may change" but "state
  what you changed and why", which is the discipline the method is about.

⛔⛔ **PASS 2 HOLED THIS CHANNEL THREE INDEPENDENT WAYS AND ALL THREE REPAIRS ARE BINDING.**
It is my own replacement rule, so it gets the harshest statement:
- **THE TYPED REASON IS A SELF-DEFEATING ORACLE.** `UndeclaredExpectationChange(ids)` names
  precisely the ids whose declaration makes that refusal impossible next round — **the gate
  hands the agent the list to echo.** The control never receives a reason and so can never
  echo, which makes the channel *symmetric in form and asymmetric in effect*; calling it
  symmetric was a category error.
- **BLANKET DECLARATION WAS FREE.** No cap, no plausibility test, and nothing evaluated the
  "one-line justification". `PASS_TO_PASS` per task on the measured-50 runs **median 94, max
  875** — declaring everything currently failing bought total immunity from the regression arm.
  ⇒ **`|declared| ≤ 5`, AND every declared id must be CURRENTLY FAILING under the candidate
  patch** (the gate has this in `post_test_report`). Measured justification: over the
  measured-50 the per-task count of deleted-line hunks in existing test files is
  `{0:29, 1:14, 2:4, 3:1, 20:1, 30:1}` — **so 19 of the 21 rewriting tasks need ≤ 5.**
- **I3 FORBADE THE RECOVERY THE CHANNEL EXISTS FOR.** The declaration is not part of the patch,
  so a redeclare-and-resubmit leaves `patch_sha256` unchanged and I3 demanded the identical
  verdict — REFUSE again. ⇒ **I3 is RE-KEYED on `gate_input_sha256`**, so a redeclared
  identical patch is a different adjudication rather than an invariant violation.
⚠️ **AND THE NAMED RESIDUAL MEASURED THE WRONG ERROR.**
`refusals_on_undeclared_expectation_change` counts only UNDER-declaration — **the
over-declaration exploit drives it to ZERO, and a zero there reads as "no residual bias".**
*The quiet failure reads as good news.* ⇒ companions, all computable post hoc from `T`:
`declared_not_in_T` · declaration precision and recall against `T` · the `|declared|`
distribution · `regression_refusals_averted_by_declaration` · and, for capability-vs-voice,
**`frac_declared_ids_echoed_from_prior_reason`** — ⛔ **compared against a WITHIN-TREATMENT
PERMUTATION NULL** (each task's round-2 declaration scored against *another* task's round-1
reason ids, under a seeded permutation committed here), **not across arms.** *v3 called the
cross-arm distribution "the only empirical test of the symmetry claim"; that is vacuous — `P₁`
is SHARED, so the round-1 declaration set is the SAME OBJECT in all three arms and comparing it
across them compares a shared artifact to itself, returning equality by construction. It is the
placebo-inherits-the-targeting shape, reappearing in the declaration channel.* The control's and
sham's values are **0 by construction and are not comparators.**
📌 **FIRING RULE, because v2 left two constructors with identical payloads and no rule:**
`UndeclaredExpectationChange` fires **iff** every failing id is outside the declared set and at
least one lies in an existing test file; `RegressionDetected` otherwise. *Unspecified, an
implementer emitting only the latter would have driven my named residual to exactly 0 with no
defect visible anywhere.*
⚠️ **Direction, stated honestly: over-declaration attenuates toward the null** — a fully
declaring agent converges on the control — **so the exploit is conservative for §1's claim, and
that is exactly what makes it dangerous: it voids the mechanism while every named quantity
reads clean, and it corrupts ADVERSE-1, because a gate that never got to judge is not a gate
that judged badly.**

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
- **CHECK 2** — ⛔ **v2'S PREDICATE WAS THE WRONG TEST AND IS REPLACED.** It asserted
  `git -C repo_snapshot rev-parse HEAD` returns non-zero — which **passes on a nested `.git`,
  on an unborn HEAD, and on a worktree-pointer state, every one of them holding the full
  object store.** ⇒ **The snapshot is BUILT by copying the worktree WITHOUT git metadata (no
  `.git` at any depth, no `GIT_DIR`, no worktree pointer file), and the check asserts NO
  REACHABLE OBJECT STORE:** `git -C snapshot rev-parse --git-dir` fails, `find snapshot -name
  .git` is empty, and `GIT_DIR`/`GIT_COMMON_DIR` are unset in the gate's environment.
  ⛔⛔ **THIS IS NOT HYPOTHETICAL AND IT LEAKS TO BOTH ARMS, NOT JUST THE GATE:** the official
  image recipe leaves **162 tags** behind after `git remote remove origin`, and
  `git log --all -S<f2p-name>` returns the commit whose diff **IS** the dataset's `patch` and
  `test_patch`. **The harness version that fixed this is PINNED in the pre-registration** —
  v2 pinned no harness version at all, so the fix was not in force.
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
- **(c) ⛔ DELETED — v2 claimed "a fixed K = 3 rounds per task in BOTH arms … equal by
  construction". THE CONTROL COULD NOT HAVE K ROUNDS**: ACCEPT ends the episode, its gate is
  hard-wired ACCEPT, and §5(d) invokes that gate each round, so the control terminated at
  round 1 — and I1 made any later round unsubmittable anyway. *Parity in count, zero in
  opportunity.* **The round structure now lives in §7 and the arms differ in stopping rule BY
  NECESSITY; that difference is what the SHAM exists to price, which is what a placebo is
  for.** ⚠️ **And the cap gets a NUMBER: `TOKEN_CAP_PER_TASK` is stated in the
  pre-registration, because v2 wrote the cap as a relation with no value — so realised rounds
  were `min(K, ⌊cap ÷ per-round cost⌋)` and the gate's measured benefit still depended
  silently on a growing quantity (context and repo size).**
- **(d) RETIRED 08/27 — TOMBSTONE, NOT A DELETION** (helm's instruction; the clause number stays
  so a wave-2 reader finds it where it was): **"RETIRED 08/27: the gate makes no model calls in
  wave 1 (helm ruling), so there is no gate spend to equalise; REINSTATE VERBATIM if wave 2 adds
  a model-backed gate."** ⛔ *It could not have worked as written either: a synthesis call over a
  `GateInput` whose test-report fields are deliberately EMPTY in the sham is not the identical
  call, and 4 / 0 / unspecified container suite runs are not matching latency.*

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
       | RegressionDetected(ids, n_more)            # ids ⊆ base_test_report.ids, |ids| ≤ 20
       | UndeclaredExpectationChange(ids, n_more)   # same bound: ≤ 20 ids + a count
       | SynthCheckFailed(check_id, observed, expected)
       | ContentFree                      # the SHAM's only legal reason (fixed literal)
```
⛔ *v2's enum had no content-free constructor while §7 required the sham to emit one, and
gave the sham "no test execution" while `RegressionDetected` required `ids ⊆ base_test_report`
— **the sham could not be CONSTRUCTED as specified.** The sham's `base_test_report` and
`post_test_report` are explicitly EMPTY, and `ContentFree` carries a pre-registered literal.*

Enforced at construction: a `RegressionDetected` carrying an id absent from
`base_test_report` **must raise** — that is the positive control. Every emitted reason is
logged verbatim for post-hoc audit.

*Why a type and not a policy: "the maintainer's suggestion is to route the method kwarg
there" (lifted from `hints_text`) and "test_config.py::test_csv_regex_error still fails"
(recoverable from the visible suite) are indistinguishable from outside the gate. Only the
first is a leak, and no amount of reviewing free text separates them reliably.*

---

## 7 · The arms — v3, after pass 2 killed v2's version

| arm | round 1 | round 2 | submits |
|---|---|---|---|
| **control** | shared `P₁`, no gate | — | `P₁`. **Single submission.** |
| **sham** | `P₁` refused, **content-free, on EVERY task** | agent revises → accepted unconditionally | `P₂` |
| **treatment** | `P₁` adjudicated by the live gate | only if REFUSED: revise → adjudicated again | the accepted proposal, else **empty** |

⛔⛔ **v2's "EQUAL PROPOSAL ROUNDS BY CONSTRUCTION — a fixed K = 3 in both arms" IS DELETED, NOT
ADJUSTED, because the mechanism it asserted did not exist.** Three of v2's own sentences forced
the control to terminate at round 1 — ACCEPT ends the episode · the control's gate is
hard-wired ACCEPT · §5(d) invokes that gate every round — and **I1 made its later rounds
unsubmittable by invariant.** ⇒ ***PARITY IN COUNT AND PROVABLY ZERO IN OPPORTUNITY.*** Three
refuters reached that independently. *The repair is removal: a claim whose mechanism does not
exist is not weakened by qualification.*

⭐ **THE SHAM IS NOW LITERAL REFUSE-ONCE** — content-free refusal of round 1 on **every** task,
then unconditional acceptance. **No per-task matching, no sequencing, all three arms run in
parallel.**
⛔ **v2's matched sham was worse than no sham.** With `P₁` shared and ACCEPT terminating, a
matched sham with count ≥1 *must* refuse from round 1 — **so its first refusal landed on the
byte-identical `P₁` the treatment refused, on exactly the treatment's refusal set.** Its
task-level refusal precision was therefore **identically equal to the treatment's on every
run**. ***A PLACEBO THAT INHERITS THE TREATMENT'S TARGETING CANNOT CALIBRATE TARGETING.***
And it was not the counterfactual it was named for: REFUSE-ONCE refuses everywhere; the matched
sham refused only where the treatment did.

**THE CONTRASTS, AND WHAT EACH ONE IS ALLOWED TO MEAN:**
- **`treatment − control` — PRIMARY.** *"Does the gate beat a single submission?"* This is the
  claim in §1 and the only contrast the MDE table, the discordance precondition and the adverse
  outcomes are written for.
- `sham − control` — secondary: **the value of one forced revision, on every task, carrying no
  information.** This is the REFUSE-ONCE / best-of-2 effect, measured rather than argued.
- `treatment − sham` — secondary. ⛔ **It may NOT be called "the gate's information content."**
  The gate's information has two parts — *which* patches to refuse and *what* to say — and this
  contrast confounds them with a dose difference (the sham refuses every task, the treatment
  only where it judges).
🔑 **THE READING THAT MATTERS: if `treatment − control` ≈ `sham − control`, the gate's
SELECTIVITY added nothing beyond the retry**, whatever the refusal table says.

⛔ **v3 CLAIMED THE SHAM "MEASURES THE CHANCE LEVEL INSTEAD OF IT BEING COMPUTED" — STRUCK AS A
TAUTOLOGY WITH A FALSE CONSEQUENT.** The sham refuses exactly the shared `P₁`, so its realised
precision equals **`base_fail_rate_round1`** identically — and §2 already computes that from the
very same scored blobs the control submits. *Two names, one number, one population, zero extra
information.* ⇒ **ADVERSE-1 fires against `base_fail_rate_round1`; the sham's realised precision
reproduces it as an IMPLEMENTATION CROSS-CHECK.** The sham's warrant is `sham − control`, the
forced-revision effect — never ADVERSE-1.

⭐ **HOW `P₁` IS PRODUCED — RESTORED, AND MADE PRECISE.** ⛔ *The v3 §7 rewrite DELETED the
sentence that specified this ("the first proposal `P₁` is generated once per task and SHARED
across all three arms") while the pre-registration went on citing §7 as its source — a dangling
citation into a location the same edit emptied. My own repair removed the thing my own binding
document points at.*
> `P₁`, with its §3.4 declaration set, is generated **ONCE per task**, under a round-1 system
> prompt that is **byte-identical across arms and ARM-BLIND** — the agent is not told which arm
> it is in, and **is not told whether a gate exists** — and the identical bytes are replayed as
> round 1 of all three arms.

⚠️ **THE FRAMING CHOICE IS A CONFOUND EITHER WAY AND IS NAMED RATHER THAN LEFT OPEN.** *Gate-aware
framing* would make the control's only submission the first draft of an agent that expected
review — so "the same agent without the gate" would be false of the arm it names. *Neutral
framing* (chosen) means the round-1 declaration set comes from an agent with no reason to
declare anything, so **the treatment's round-1 refusal rate carries a framing artifact.** The
neutral branch is taken, and the artifact is listed in PRE-REG §1's cannot-show list.
📌 **`P₁`'s tokens are generated once and charged to EACH arm's cap** (it is round 1 of all
three), and **ADVERSE-3's cost-per-solved uses that same convention in both numerator and
denominator** — v3 left this unstated while ADVERSE-3 fires on a ratio the ambiguity moves.

⚠️ **Dose is NOT equalised and the freeze says so rather than implying otherwise:** the sham
refuses on 100% of tasks, the treatment on the fraction it judges. Realised rounds are logged
per arm and the result is decomposed by them. **Compute matching (§5d) extends to ALL THREE
arms**, including the sham.

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
