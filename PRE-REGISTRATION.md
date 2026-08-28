# SaltBench Wave 1 — PRE-REGISTRATION

**Written 2026-08-27, BEFORE any model call.** Nothing in this document may be revised
after the first API request of either arm; revisions are appended below the line at the
bottom, dated, with the reason. The point of writing it first is that the criteria cannot
be fitted to a result that has not happened yet.

Owner: silicon seat (staffing closed by the Captain, 2026-08-27 20:1x).
Governing documents: council minute 2026-08-27 (docket `72928e04` + addendum `93130077`)
and the promotion charter `seat/briefs/2026-08-20-saltbench-promotion.md`.

---

## 0 · The status of this document

⛔ **PRIVATE.** Nothing here publishes until the IARC ruling lands and the Captain says
go (promotion charter, binding). This repo has **zero git remotes** by construction.

⛔ **Personal lane.** This harness is built fresh, reimplementing only field-standard
methodology. **No employer-lane code enters this repo, ever** (portfolio `CLAUDE.md` lane
law). It touches no tape-out resource, never takes a P1 build ticket, and pulls no
tape-out seat.

---

## 1 · The claim, stated narrowly enough to be wrong

**Claim under test:** an agent whose patches must pass a *gate* solves more tasks
correctly than the same agent without the gate, at a stated cost.

**What "the gate" is:** a mechanism that independently checks a candidate patch and
refuses it when the evidence does not support acceptance. The demo arm is **the gated
harness — a mechanism, not an exhortation.** No prompt-level "please be careful" arm is
part of wave 1.

### ⛔ What this experiment CANNOT show, stated up front

Wave 1 runs on Python repository-repair tasks scored by held-out tests. On that
substrate:

- **It does NOT test machine-checked proof.** The kernel is not in this loop. No claim
  about proof-carrying code, kernel scoring, or verification may be drawn from wave 1,
  and any later write-up that cites wave 1 for such a claim is misusing it.
- **It tests the GATING DISCIPLINE only** — the value of refusing a patch that looks
  green but is not.
- A null result here does not refute the Salt method; it bounds where the *gating
  discipline alone*, stripped of proof, is worth its cost.

*This section exists because the most likely way this demo does damage is by being
quoted for the claim it did not test.*

---

## 2 · Substrate — MY call, and deliberately adverse

**Chosen: SWE-bench Verified (the human-validated split), a subset selected per §3.**

The Captain delegated substrate to this seat. The alternative was our own corpus (salt
lemma-ports, saltworks organ-level nodes), which is kernel-scorable and plays to the
method's strength. **I am not choosing it, and the reason is the whole argument:**

> The one sharp question this demo must survive is *"you built the benchmark to win."*
> The strongest available answer is a substrate **we did not design, whose scoring we do
> not control, and where our method's best feature is unavailable.**

So the substrate is chosen *against* us on three axes at once. If the gate still helps
there, the result is believable in a way a home-corpus win could never be. If it does
not help there, that is a real and reportable bound.

⚠️ **The honest tension, named rather than buried:** SaltBench's own tech report argues
that hidden-test suites sample properties where proofs state them. That argument is about
what makes a good *benchmark*. Here we are not proposing SWE-bench as a yardstick — we
are borrowing a neutral one to test a mechanism. Using a substrate whose methodology we
criticize, and winning on it anyway, is stronger evidence than winning on our own.

---

## 3 · Task selection — the criteria, fixed before either arm runs

**Selection uses instance METADATA ONLY. No task is inspected, no solution is read, and
no arm is run before the task list is frozen and committed to this repo.**

Predicate, applied to SWE-bench Verified:

1. `len(FAIL_TO_PASS) >= 1` — there must be a failing test that a correct patch fixes,
   or the task carries no solvable signal.
2. `len(PASS_TO_PASS) >= 1` — there must be a regression signal the gate can act on.
   *(This is the discriminating one: it is what makes a false green detectable.)*
3. Gold-patch scope band: touches **1–3 files**. A metadata proxy for tasks that are
   neither trivial nor sprawling. Read from the patch's file list only — the patch
   content is not read.
4. Problem statement length ≥ 500 characters — excludes underspecified issues where
   failure is a reading-comprehension artifact rather than an engineering one.
5. **Repo-diversity cap: at most 4 tasks per source repository**, so no single codebase's
   idiom dominates the estimate.

**Deterministic draw, so the selection is auditable rather than trusted:** candidates
meeting 1–5 are sorted by `sha256(instance_id + SEED)` and the first **N = 50** taken.

```
SEED = saltbench-wave1-2026-08-27
N    = 50   (inside the ruled 40–60 band)
```

The seed and predicate are committed **in this document, before any run**. Anyone may
re-derive the exact task list from the public dataset plus this page. A selection that
can be re-derived cannot be quietly re-drawn.

⛔ **If the frozen list must change for a mechanical reason** (a task fails to build in
both arms for environment reasons unrelated to the patch), the exclusion is logged with
its cause in `EXCLUSIONS.md` **and the pair is dropped from both arms**, never from one.

---

## 4 · Model — one mid model, and the band is MEASURED, not quoted

Ruled shape: **ONE mid model** in a 45–55% baseline band.

**Candidate: `claude-sonnet-5`** ($2/MTok in, $10/MTok out) — the tier that leaves the
most room inside the ruled $150–400 budget for a paired run plus a pilot.

⛔ **THE BAND IS A PROPERTY OF `model × substrate × harness`, NOT OF A MODEL.** A
published leaderboard figure was produced by a different scaffold and does not transfer to
this one. **No baseline percentage is asserted in this pre-registration**, and none may be
cited from memory or from a table.

**Pilot, run before the paired run:** the control arm alone on **10 tasks drawn by the
same predicate and seed but explicitly excluded from the 50** (offsets 50–59 of the
sorted draw, so the pilot never contaminates the measured set).

- Pilot solve rate lands in **40–60%** → proceed with `claude-sonnet-5`.
- Pilot lands **above 60%** → step down one tier and re-pilot (ceiling effects hide the
  effect we are looking for).
- Pilot lands **below 40%** → step up one tier and re-pilot (floor effects do the same).
- **Pre-stated cap: at most two re-pilots.** If no tier lands in band, wave 1 reports
  *"no model in the affordable range sits in the measurable band on this substrate"* —
  **which is a result, and it is reported as one, not quietly retried until something
  fits.**

---

## 5 · Design and scoring

**Paired, within-task.** Both arms attempt the identical task list. The unit of analysis
is the **pair**, not the task.

- **Control arm:** the agent, unmodified.
- **Treatment arm:** the same agent, same model, same budget, behind **the gate**.
- Both arms are scored by the **held-out** SWE-bench harness (FAIL_TO_PASS +
  PASS_TO_PASS). Neither arm sees the scoring tests.

**Primary statistic: McNemar's test on discordant pairs.** Concordant pairs carry no
information about a difference and are reported but not tested. **Pre-stated: two-sided,
α = 0.05.**

⚠️ **n = 50 is a SCREEN, not a measurement.** It can see a large effect and is blind to a
modest one. **A non-significant result will be reported as "this screen could not see an
effect of this size," never as "there is no effect."** With a lopsided discordant split a
large effect is visible at this n; anything subtle requires an extension that is not
budgeted here.

**Also reported, always:**
- **Cost per solved task**, both arms, in dollars — the compute objection, retired at
  demo grade or conceded honestly.
- Wall-clock per task, both arms.
- **Gate refusal count, and how many refusals were correct** (the patch would indeed
  have failed held-out tests) versus incorrect (the patch would have passed). *A gate
  that refuses everything scores well on solve-rate-of-accepted and is worthless; this
  ratio is what stops that reading.*

---

## 6 · The capability-floor hypothesis — pre-registered as win-either-way

**Hypothesis:** the gate's benefit depends on the agent being capable enough to act on a
refusal. Below some capability floor, the gate refuses and the agent cannot recover, so
gating costs money and buys nothing.

This is registered **before** the run so that either outcome is a finding:

- Gate helps at the mid tier → the mechanism works where it is affordable.
- Gate does not help → **evidence for the floor**, which is the house tier table's own
  prediction and a result worth reporting.

⛔ **Registering both outcomes as interesting is exactly the move that makes a
pre-registration cheap to write and expensive to violate.** It is written down so that a
null cannot be quietly reframed after the fact.

---

## 7 · Stopping rule

Fixed n = 50 per arm. **No optional stopping**, no peeking-then-extending.

If a batch-sequential extension is ever wanted, it requires a pre-stated boundary
committed to this repo *before* the extension runs, and the analysis changes accordingly.
**Extending a fixed-n design after seeing the result is how a screen becomes a fiction.**

---

## 8 · The persuasion artifact

**3–5 discordant-pair case studies**, chosen after scoring by a pre-stated rule: the
discordant pairs with the **largest held-out-test delta**, ties broken by the deterministic
draw order.

Each case study shows the gate refusing a patch that looked green and did not hold —
**the mechanism on camera**, which is what a colleague remembers. Case studies are
illustration, not evidence; the statistic is the evidence, and the write-up will say so.

---

## 9 · What would make me abandon or amend this

Stated now, so it is not decided under pressure later:

- Both arms score identically on every pair → the harness is not exercising the gate;
  fix the harness, discard the run, report the discarded run.
- Gate refusal rate is 0% or 100% → the gate is inert or vacuous; not a result about the
  method.
- Cost exceeds the ruled $150–400 before the paired run completes → **stop and report**,
  rather than quietly reducing n.

---

*Nothing below this line existed before the first model call. Amendments are appended,
dated, with their reason — never edited into the text above.*

---
