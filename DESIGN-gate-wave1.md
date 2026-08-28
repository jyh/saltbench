# Wave 1 — the gate: design block

**Status: DESIGN, NOT BUILT. Refuter-gated per the verify posture before any executor
builds it** (promotion charter, SB-3 shape). Written 2026-08-27, after the
pre-registration and before any model call.

This block exists to be attacked. If a reviewer can show the gate can win without being
right, the experiment is void and better void now than after the money is spent.

---

## 1 · What the gate is, precisely

The treatment arm is **the same agent, same model, same budget, plus a gate**. The gate
sits between "the agent proposes a patch" and "the patch is submitted for scoring":

```
        agent proposes patch P
                │
                ▼
        ┌───────────────┐   REFUSE + reason ──► agent may revise (budget permitting)
        │   THE GATE    │
        └───────────────┘
                │ ACCEPT
                ▼
     submitted for held-out scoring (FAIL_TO_PASS + PASS_TO_PASS)
```

⛔ **The gate never sees the held-out tests.** If it did, the experiment would be
measuring test leakage and nothing else. This is the single constraint that the harness
must make structurally impossible, not merely avoid by convention — see §4.

---

## 2 · The failure mode this design exists to prevent

***A gate that refuses everything looks excellent on any metric computed over accepted
patches.*** It is the same shape as this seat's banked defect: a check whose metric is
pinned by a constraint cannot fail, and reports ✅ while testing nothing.

So the primary statistic is deliberately **not** "solve rate among accepted patches." It
is solve rate over **all attempted tasks**, where a refused-and-never-revised task scores
as **unsolved**. A gate that refuses everything therefore scores **zero**, not perfect.

Reported alongside, because the ratio is what makes the mechanism legible rather than
magical:

| Quantity | Why it is reported |
|---|---|
| refusals issued | the gate's activity level |
| refusals **correct** (patch would have failed held-out) | the gate earning its place |
| refusals **incorrect** (patch would have passed) | the gate's cost, in solved tasks destroyed |
| accepted-and-failed | what the gate let through — its miss rate |

⚠️ **Correct/incorrect refusal can only be computed AFTER the fact, by scoring the
refused patch too.** The harness must therefore score every patch it ever saw, including
refused ones — **and must not show that score to the gate or the agent.** Scoring the
refused patch is what turns "the gate refused a lot" into "the gate refused the right
things."

---

## 3 · What the gate may look at

Available to it, all derivable inside the repo under test without held-out knowledge:

1. **The patch applies cleanly** and the project still imports/builds.
2. **The visible tests** the agent could already run.
3. **Properties the agent did not have to satisfy**: the gate may synthesize additional
   checks from the issue text and the touched code — the analogue of "a property the
   proof states and a test samples."
4. **Regression surface**: tests that passed before the patch must still pass. This is
   the cheapest and most defensible arm, and it is the one that catches the classic
   false green — a patch that fixes the reported issue by breaking something else.

⛔ **Not available: FAIL_TO_PASS / PASS_TO_PASS identities, the gold patch, or anything
derived from them.**

---

## 4 · The structural separation (not a convention)

Convention is what fails silently. The harness must be built so that the leak is
*impossible to express*, not merely *against the rules*:

- The scoring harness runs in a **separate process with a separate working copy**, and
  the gate is never passed the held-out test identifiers at all — it cannot leak what it
  was never given.
- The gate's inputs are a fixed, enumerated struct. **Adding a field to it is a diff that
  a reviewer sees**, which is the point.
- **Both arms run the same gate code path**, with the control arm's gate hard-wired to
  ACCEPT. This kills a whole class of confound: any difference caused by the harness's
  plumbing, retry behaviour, or prompt scaffolding is present in both arms and cancels.
  *Only the accept/refuse decision differs.*

🔑 **That last point is the most important line in this document.** If the control arm is
"the agent, plain" and the treatment arm is "the agent inside a wrapper", then the wrapper
is a confound and the experiment measures scaffolding, not gating.

---

## 5 · Budget parity — the other confound

The treatment arm gets to revise after a refusal. **That is more model calls, so a naive
design gives the treatment arm more compute and the result is uninterpretable.**

Pre-stated: **both arms receive an identical token/call budget per task.** The treatment
arm spends part of its budget on revision; the control arm may spend its whole budget on
one attempt or on self-directed retries. If the treatment arm wins, it wins *at equal
spend*, which is the only comparison worth showing a colleague.

⚠️ Cost-per-solved-task is still reported separately, because equal budget is not equal
*consumption*.

---

## 6 · What a refuter should attack

Stated so the review has a target, and so a reviewer is not reduced to guessing what I
was worried about:

1. Can the gate see anything that correlates with the held-out tests? Trace every field.
2. Does the control arm differ from the treatment arm in any way other than the
   accept/refuse decision? Diff the two code paths.
3. Is budget parity real in tokens, or only in call count?
4. Can a task be scored "solved" without the held-out suite actually passing?
5. Does any statistic in §2 become undefined or misleading when refusals are 0 or 100%?
6. **Is there a cheaper explanation for a win than "gating helps"?** Name it before the
   run, not after.

---

## 7 · What is NOT designed here

The task runner, the container strategy, and the dataset plumbing. Those are mechanical
and follow the above; they are not where the experiment's validity lives, and designing
them now would be motion rather than progress.
