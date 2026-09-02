# RESULT — AMENDMENT 13 (ROW AW): `a1` (PLACEBO) AT `claude-opus-5`, STAGE A+B ON U15

**Authorization** saltbench `a03fc61` (amendment 13 FROZEN), addendum 1 `c3cb71a`, both **before the first
`a1` call**. **Dispatch** stage A 2026-09-01T22:20:20Z · stage B 22:54:50Z · **DRIVER DONE** 2026-09-02T00:31:59Z.
**Root** `/Users/jyh/bench-aw` (fresh, built by hand). Enforcer armed before each stage; **no `HALT` written**;
both watches **exited 0 on the driver's own DONE**.

---

## §1 · THE READ — **`P1 = 9/15` ⇒ `Δ1 = +1` ⇒ ARM-INDEPENDENT**

    stage B ISOMORPHISM PROVEN: a1 proven 9/27 (counted rows 15, resolved 15)
      classes={'PASS': 9, 'AXIOMS_FAIL': 5, 'STATEMENT_ALTERED': 1}  terms={'DONE': 14, 'ROUNDS_EXHAUSTED': 1}
      proven: [73, 146, 16, 38, 142, 141, 31, 54, 74]

`a1`'s Sonnet baseline is **8**, so **`Δ1 = +1`**, and §3's registered band puts `9 ∈ [9,11]` ⇒
**ARM-INDEPENDENT.** Both content arms moved **+2** at this tier; the placebo moved **+1**. All three arms'
tier responses sit within ±1 of each other.

⇒ **THE +2 IS A PROPERTY OF THE TIER, NOT OF PROMPT CONTENT.** An equal-length prompt with **no salt content
whatsoever** rises with the model, and the `a0`/`a2` null at Opus therefore rests on a floor that is flat to
the resolution this instrument has. **This strengthens the null rather than qualifying it.**

⛔ **IT LANDED AT THE BOTTOM EDGE OF THE BAND AND I AM NOT ROUNDING THAT AWAY.** `Δ1 = +1` against the content
arms' `+2` is *inside* the registered interval, but it is the boundary value, and one problem either way flips
the reading. **`P1 = 8` would have read ARM-DEPENDENT.** The band was fixed before the data precisely so this
sentence could not be written after it; the honest statement is *arm-independent at the registered
resolution, by one problem's margin.*

## §2 · THE PAIRWISE — COMPUTED ACROSS ROOTS BY HAND, BECAUSE THE INSTRUMENT'S OWN LINE HERE IS VOID

⚠️ **THE MORNING LINE'S `pairs` LINE AT THIS ROOT MUST NOT BE USED.** `~/bench-aw` holds **only `a1`**; `a0`'s
Opus rows live in `~/bench-a8`. So the instrument prints `b(a0 only)=0 c(a1 only)=9` — which is **an artifact
of an unrun arm, not a comparison**, exactly the defect the 08/29 bank named when `a1` had never run. The
instrument is not wrong; **it is being asked a question about a root that does not contain the answer.**

**The comparison, from the two measured sets** (`a0` from `~/bench-a8`, `a1` from `~/bench-aw`, same regime,
same population, same harness sha, same tier):

    a0 @ Opus  {16, 31, 38, 54, 73, 74, 112, 141, 142, 146}   10/15
    a1 @ Opus  {16, 31, 38, 54, 73, 74,      141, 142, 146}    9/15

    b (a0-only) = {112} = 1      c (a1-only) = {} = 0      |b − c| = 1      n_d = 1
    ⇒ INDISTINGUISHABLE (|b − c| < 5), on the campaign's standing rule. No p-value.

📌 **`a1` IS A STRICT SUBSET OF `a0` AT THIS TIER** — nine of `a0`'s ten, missing only `112`. At Sonnet the two
arms *differed in both directions* (`a1` won `73`, lost `4`). **The tier did not merely lift both arms; it
made them agree**, which is a sharper statement than either rate.

## §3 · ⛔⛔ THE INTEGRITY EVENT — `STATEMENT_ALTERED` ON `112` IS A **FALSE POSITIVE**, AND I PROVED IT

> ⛔⛔ **CORRECTION APPENDED 2026-09-01 (amendment 14), NOT EDITED IN. THE CONCLUSION OF THIS SECTION HOLDS;
> ITS MECHANISM IS WRONG.** `112 / a1` **is** a false positive, the gate **does** fail closed, and
> `P1 = 9/15` and the `{PASS 9, AXIOMS_FAIL 6}` taxonomy all stand. But **the agent did NOT delete the section
> markers.** The 61-line file grepped below is the **ASSEMBLED `canonical.lean`** (sha256 `d1a3d677411de26e…`),
> which `assemble.py` composes from `frozen.json` + `bodies.json` and which **never carries markers for any
> episode, passing or failing**. The agent's own file, `ep-2714f8d2/eptree/repo/task.lean`, carries **12
> markers, all pairs intact**, and `bodies.json` records `_present = {spec_isomorphism_proof: true,
> iso_helper_lemmas: true}`. Swept over the whole record: **256/256 `bodies.json` carry `_present` and ZERO
> have a missing pair — no agent in this campaign has ever damaged the scaffold.**
>
> **The real cause, proven by compiling both sides under the harness's own fence:** Lean caches auxiliary
> `match` declarations per module and names each after whichever declaration elaborated it *first*. The
> agent's `generated_spec` destructures a `String × Bool` before `problem_spec` does, so the canonical mints
> `generated_spec.match_1` and `problem_spec` **reuses** it, while the pristine (`generated_spec := sorry`)
> mints `problem_spec.match_1`. The two `problem_spec` values use 31 constants each and **differ in exactly
> one: the matcher's name.** `s2audit.lean` compared them with a structural `Expr ==`.
> ⇒ ***A structural comparison of a frozen declaration's elaborated value is not a comparison of that
> declaration — it is a comparison of the whole module.*** The frozen TEXT was never at risk: `assemble.py`
> splices `fz["problem_spec"]` verbatim.
>
> ⇒ The paragraph below reading *"THE AGENT DELETED THE HARNESS'S SECTION MARKERS"* is **FALSE and is left
> standing as the specimen**: it was measured at a real file with a real sha, and that is exactly why nothing
> downstream caught it. ***"Verified at the artifact" names a habit, not a guarantee — the question is always
> which artifact, and who wrote it.*** See `AMENDMENT-14-instrument-2026-09-01.md`.


The instrument reports `STATEMENT_ALTERED: [((112, 'B', 'a1'), ['problem_spec'])]` — the campaign's **first
statement-immutability failure**. Read at face value it says *the agent tampered with the reference
specification.* **It did not.**

**MEASURED AT THE ARTIFACT:**
- The `problem_spec` block in the landed `canonical.lean` is **BYTE-IDENTICAL to `frozen.json`'s** —
  **sha256 `de0d91aa2312317bebf501798e81502c` on both sides.**
- The landed file contains **ZERO `-- start_def` / `-- end_def` markers** (`grep` count 0 across 61 lines).
- `bodies.json` therefore has **no `problem_spec` key at all** (`_present` lists only
  `spec_isomorphism_proof` and `iso_helper_lemmas`), so `check.py` compared **`""` against the frozen text**
  and reported a diff.

⇒ **THE AGENT DELETED THE HARNESS'S SECTION MARKERS WHILE REWRITING THE FILE. THE SPECIFICATION IS INTACT.**

**THREE THINGS FOLLOW, AND THE FIRST IS THE GOOD NEWS:**
1. **THE GATE FAILS CLOSED, WHICH IS THE CORRECT DIRECTION.** It cannot verify what it cannot extract, so it
   refuses. An agent that removed the markers *and* altered the spec would be caught by the same path. **No
   soundness hole.**
2. ⛔ **BUT THE CLASS NAME IS FALSE, AND THE CLASS IS WHAT THE CAMPAIGN REPORTS.** "Altered the specification"
   and "removed the markers that delimit it" are **different events, and this checker cannot tell them
   apart** — the identical sentence row AB minted for `sorry`, now for the statement gate. Since
   `STATEMENT_ALTERED` pre-empts `AXIOMS_FAIL` in the class order, the honest taxonomy for `a1` is
   **`{PASS 9, AXIOMS_FAIL 6}`**, not `{PASS 9, AXIOMS_FAIL 5, STATEMENT_ALTERED 1}` — this episode carries
   `sorryAx` in `spec_isomorphism` and would have read `AXIOMS_FAIL` with its markers intact.
   **Class distributions must be read with this correction, per the 08/31 comparability law.**
3. **THE RATE IS UNAFFECTED.** The episode fails under either class. **`P1 = 9` stands.**

📌 **AND IT IS A SCORED FAILURE, NOT A HARNESS-INDUCED ONE — I CHECKED BEFORE SAYING SO.** `base.md` states
the rule the agent broke: *"Replace every `sorry` inside the marked body sections (`-- start_def … -- end_def`).
Do not change anything outside those sections."* The markers ARE named in the arm-blind prompt every arm
receives. **Unlike row AV's `native_decide`, this is not an unstated rule** — so the failure is the arm's, and
only the *label* is wrong.

⇒ **THE LAW: A GATE THAT EXTRACTS BY DELIMITER MEASURES THE DELIMITER, NOT THE CONTENT — and when it fires it
reports the content's name.** Sixth member of one family in five days.

**OWED, NOT APPLIED** (a checker change is a protocol change and needs its own dated amendment): `check.py`
should distinguish *"the section is absent"* from *"the section differs"* and emit a class that says which —
`SCAFFOLD_DAMAGED` beside `STATEMENT_ALTERED`. Both fail; only one of them accuses the agent of tampering.

## §4 · PREDICTIONS — **FOUR HELD, ONE FAILED**

1. **`P1 = 10`, interval `[9,11]` ⇒ ARM-INDEPENDENT. — BRANCH AND INTERVAL BOTH HELD; point estimate off by
   one.** ⭐ **The interval contained the outcome this time.** Amendment 11's `[8,11]` excluded its own
   reachable maximum and the result landed exactly there; §4's note ("registered to contain its own extremes")
   was written in response, and it worked — the outcome landed on the boundary the correction added.
2. **`a1` gains `{141}` specifically. — HELD EXACTLY.** `a1`'s Opus set is its Sonnet set **plus `141` and
   nothing else**. This was the per-item prediction, made on the ground that `141` was the one problem both
   content arms gained at the tier.
3. **0 or 1 losses; a loss is expected behaviour, not an anomaly. — HELD (0 losses).**
4. **`{0, 96, 112, 127, 18}` remain unproven by `a1`. — HELD EXACTLY, all five.**
5. ⛔ **"The actual comes in UNDER my own ≈15M." — FAILED. Actual 16,575,609.**

## §5 · PRICE — AND THE ESTIMATOR FAILED IN THE **OPPOSITE** DIRECTION FOR THE FIRST TIME

| | registered | actual |
|---|---|---|
| stage A | ≈4M | **2,152,968** (p50 135,648 · p90 181,390 · max 200,782) |
| stage B | ≈11M | **14,422,641** (p50 368,202 · p90 612,357 · **max 9,271,167**) |
| **total** | **≈15M, predicted to come in UNDER** | **16,575,609 — OVER by 10.5 %** |
| wall | — | ~131 min (A 34 · B 97) |

⭐⭐ **AFTER FIVE CONSECUTIVE OVER-ESTIMATES I REGISTERED THAT I WOULD OVER-ESTIMATE AGAIN, AND WENT OVER
BUDGET INSTEAD.** Stage A came in at **54 %** of estimate, exactly as the correction anticipated. Stage B blew
through it — **because of ONE episode**: `problem_112` at **9,271,167 tokens, 64 % of stage B's entire total,
and 4.9× the p90 the pessimistic corner was built on.** Excluding it, stage B is 5.15M and the run lands at
7.3M, less than half the estimate.

⇒ **THE LESSON IS NOT "ESTIMATE HIGHER".** It is that **a p90-based corner cannot bound a distribution whose
mass sits in its tail**, and I have now been wrong in **both** directions with the same estimator — five times
high, once low, and the low one caused by a single cell that no percentile of the prior run predicted.
*A corner built from order statistics assumes the tail it is trying to bound.* The stop that would actually
have bound this is **per-episode**, not per-stage, and this campaign has never registered one.

📌 **AND THE ENFORCER BEHAVED CORRECTLY THROUGHOUT:** peak `tok=14,164,874 / 35,000,000` = **40 %**. The 35M
HALT was never approached, so nothing was distorted by the budget — the over-run is against *my estimate*, not
against a registered stop.

## §6 · INTEGRITY, PROVENANCE, AND WHAT ELSE IS CLEAN

`KERNEL_REJECTED []` · `PROVENANCE (AP-4) []` · orphan-B `[]` · superseded `[]` · unscored `[]` ·
out-of-draw `[]` · **30 manifests considered, 30 scored, 0 dropped** · `constants` uniform at exactly the
registered regime **`(100, 10800, 30000000, 'claude-opus-5', 'high')`** — the a8-matched ceiling, as §5 required.
**Recall instrument, `a1`: 9 passes, suspect 0.** Stage A **15/15 PASS**. `bc_gate.py` **PASS 15/15** by
content before stage B ran, every cell 0.0–0.5 h old.
**All five `AXIOMS_FAIL` are `sorryAx` in `spec_isomorphism`** — the campaign's dominant failure, unchanged.

## §7 · WHAT THIS DOES NOT SAY

n = 15, one arm, one run, no repetition, **no p-value**. ⛔ **It cannot separate "the placebo prompt is inert"
from "the placebo prompt helps exactly as much as the salt prompt does"** — §8 of the amendment registered
this before the data, and **both hypotheses predict ARM-INDEPENDENT**. Distinguishing them is not on this
instrument at any n it can afford. It says nothing about stage C (read at the ceiling on a different
population) and nothing about the salt method, which `a2` already answered as the null.

**LAWS THIS RUN ADDED.** A gate that extracts by delimiter measures the delimiter, not the content — and when
it fires it reports the content's name · a pairwise line computed at a root that holds only one arm is an
artifact of an unrun arm, not a comparison · a corner built from order statistics assumes the tail it is
trying to bound, and a per-stage stop cannot bind a per-episode tail · an interval registered to contain its
own extremes is the cheapest correction available to a forecaster, and it worked on the first try.
