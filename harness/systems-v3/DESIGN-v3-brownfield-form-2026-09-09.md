# DESIGN — THE v3 BROWNFIELD FORM
## Commissioned by the helm on the Captain's launch word, 2026-09-09 (item 4). **A DESIGN, NOT AN AMENDMENT: nothing here authorises a cell.**

**Written after matrix #1 closed** — deliberately, and the deferral is part of the record: a design begun
between two readings is carried forward wrong, and matrix #1 had a live A-vs-B question until 11:1x today.

---

## ⛔⛔ §0 · CORRECTION, 2026-09-09 12:0x — THIS DOCUMENT DESCRIBED A TREE IT COULD SEE AND v3 HAS ANOTHER

**Raised by `systems` within ten minutes of the merge, measured at both objects, and it is right.**

```
  THIS DOCUMENT (as merged)   B/clause.md · B/given/ · B/Crc32/      -> tasks/systems-v2/Crc32/B/   (LEAN)
  EXECUTOR-BRIEF-v3 §1.3      "B/ — phase 2. NO given/: the seat's own phase-1 landing is the given."
                              "(no clause file) — the change request is card.md's `## Change request`"
  tasks/systems-v3/Crc32/B/   _common.sh · interface.rs · list_traces.sh · run_*.sh · withheld/
```
⇒ **§4's measurement is real and is about the WRONG POPULATION.** All seven mutant ids are absent from
the v2 Lean tree; **that says nothing about v3.** ⇒ ***A CENSUS OVER THE TREE IN FRONT OF YOU IS A CENSUS
OF THAT TREE*** — my own standing card, minted on my own repo, met again here.
⛔ **AND THE ROOT CAUSE IS THE DAY'S OWN LESSON.** I opened this work by grepping for existing brownfield
material and got **zero**, and wrote "this is a design from scratch." **That zero was about MY repo.**
`tasks/systems-v3/.../B/` and `EXECUTOR-BRIEF-v3.md` live in systems' tree, which I cannot read. ⇒ ***AN
ABSENCE IS A CLAIM ABOUT A POPULATION, AND I NAMED THE WRONG ONE — the fourth instance today of "landed
is a claim about a ref", and the first one I committed rather than caught.***

### ⚖️ THE RULING systems ASKED FOR: THESE ARE **TWO FORMS**, AND ONLY ONE CLOSES `N = 0`

`systems` declined to guess which shape was intended and was right to. **Both are legitimate and they
answer different questions, so they get different names and neither inherits the other's argument.**

```
  B-PLANTED       given = an AUTHORED defective component, IDENTICAL across cells   (the v2 shape)
                  V1 exists: pre-existing behaviour goes RED -> GREEN
                  ⇒ CLOSES N = 0.  Everything in §1–§8 below is about THIS form.

  B-CONTINUATION  given = THE CELL'S OWN PHASE-1 LANDING                            (§1.3's shape)
                  V1 is UNDEFINED: the given is already GREEN, it passed phase 1
                  ⇒ DOES NOT CLOSE N = 0, and §1's whole argument does not apply to it.
```
⛔⛔ **AND B-CONTINUATION CARRIES A CONFOUND THAT MUST BE STATED WHEREVER IT IS USED.** Its given is
produced **by the arm under test**. So the treatment and the control begin phase 2 **from different code**,
and that difference is arm-correlated by construction. ⇒ 🔑 ***A PHASE-2 DIFFERENCE CANNOT BE ATTRIBUTED
TO THE PHASE-2 TREATMENT WHEN PHASE 1 CHOSE THE STARTING POINT.*** It measures a **cumulative** effect
across two phases, which is a real question and is not this one — and it inherits a carryover the sign
test cannot separate: **an arm that lands phase 1 better is handed an easier phase 2.**
⇒ **RULING: ruling 4's commission — the form that closes `N = 0` — is `B-PLANTED`.** `B-CONTINUATION`
keeps its place in the executor brief as its own experiment, **and must not be called "the brownfield
rung" without the confound written beside it.**
📌 **What this correction does NOT do:** it does not withdraw §2, §3, §5, §6, §7 or §8. Two verdicts, the
rewrite class, the briefing audit, the σ that does not transfer and the refusals all stand for
`B-PLANTED` exactly as written. **§4's measurement is re-scoped to v2 and is owed again for v3, by
whoever can read that tree.**

## §1 · WHY THIS FORM, NOW: IT IS THE ONLY ONE THAT CAN CLOSE `N = 0`

Matrix #1 is a **COST result with no correctness evidence attached** — `N = 0 of 36` priced cells carry a
referee verdict on a withheld suite (`RESULT-matrix-opus-1`). The campaign has said this is a write-up
gap. **It is not. It is a form gap**, and it is worth stating exactly:

> A greenfield correctness verdict requires an **ABSOLUTE** standard: the agent produced a component from
> nothing, and something must decide whether that component is right. That decision is the referee, it is
> expensive, and on this population it has never been invoked.
>
> **A brownfield correctness verdict requires only a DELTA, and the delta's baseline is measurable BEFORE
> THE CELL RUNS.** The given component *fails the withheld suite by construction*. So the question is not
> "is this right?" but "did this go from RED to GREEN?", and the RED is a fact established at build time
> with no model call in it.

⇒ 🔑 ***THE BROWNFIELD FORM MAKES CORRECTNESS A COMPARISON, AND THIS CAMPAIGN CAN ALREADY MEASURE
COMPARISONS.*** That is the whole argument for building it, and it is stronger than "brownfield is more
realistic", which is true and is not a reason.

📌 **THE TASK MATERIAL LARGELY EXISTS.** All five v2 cards carry a `## Brownfield rung` naming a specific
planted defect, and `Crc32` is realised as a full `B/` tree beside its greenfield `G/`: `clause.md` (the
change requested, given to the agent), `given/` (the defective component, seeded into the workspace) and
`withheld/` (tests, mutants, controls, reference, traces). **This document is about the v3 FORM — how a
`B/` rung becomes a v3 cell with a fence, arms, a price and a verdict — not about the tasks.**

---

## §2 · THE FORM YIELDS **TWO** VERDICTS AND THEY MUST NEVER BE ONE NUMBER

```
  V1  THE PLANTED DEFECT     does the pre-existing behaviour go RED -> GREEN?
  V2  THE REQUESTED CHANGE   does the new clause's suite pass?
```
**An agent can deliver either without the other**, and the two are not the same skill: V1 is *finding a
bug nobody pointed at*, V2 is *implementing a stated requirement*. **The interesting cell of the matrix is
V1 GREEN / V2 RED against V1 RED / V2 GREEN**, and a scoreboard that reports one number cannot see it.

⛔⛔ **THE FAILURE MODE THIS CAMPAIGN HAS ALREADY SHIPPED ONCE, ONE LEVEL UP.** An agent that implements
the streaming law correctly *on top of a checksum that is wrong on every message* produces a component
whose NEW tests pass and whose OLD ones fail. **A "tests green" field that means V2 alone would call that
a pass.** That is exactly the shape of `G-P2` in matrix #1 — a clause named "tests green" that was never
wired to a suite — and it is why this document refuses a single field.
⇒ **REGISTERED, NOT DERIVED:** V1 and V2 are separate columns in `CELLS.tsv` and separate rows in the
result. **A cell with V1 unmeasured is reported as unmeasured, never as passing.**

📌 **AND THE ORDERING TRAP.** The clause asks for a LAW relating chunked and whole-message results. On the
GIVEN component that law can be established *and be true of a wrong checksum* — chunking consistency does
not imply correctness. **V2 is satisfiable without V1 and the card must not imply otherwise.**

---

## §3 · THE REWRITE ESCAPE — A REGISTERED OUTCOME CLASS, NOT A DISQUALIFICATION

**An agent that deletes `given/` and writes the component from scratch has done GREENFIELD**, and will
often pass both suites. If that is scored as brownfield, **the form measures greenfield with extra steps
and a longer prompt.**

```
  REPAIRED   the given file survives and was EDITED           <- the only brownfield outcome
  REPLACED   the given file was rewritten wholesale
  REMOVED    the given file is gone; the component lives elsewhere
```
⇒ **All three can pass V1 and V2. Only the first is the thing the form exists to measure.** The
discriminator is cheap and structural: **the identity and lineage of the seeded file at END**, taken by
the harness, never by the agent — a hash at build, a hash at end, and a diff statistic between them.
⛔ **REGISTER THE CLASS BEFORE THE FIRST CELL, WITH ITS PREDICTION.** *Replace* is precisely the behaviour
an arm's briefing can push toward — "understand the existing code" and "start from a clean specification"
pull opposite ways — so **discovering this class after seeing the arms would make it unusable.** It is a
DEPENDENT VARIABLE of this experiment, and possibly the most interesting one.
📌 A cell that REPLACES is **not void and not excluded**. It is priced, it is scored on V1/V2, and it is
reported in its own class. **Excluding it would delete the finding.**

---

## §4 · FENCE DELTAS — THE GIVEN CODE IS A CARRIER AND THE CARD'S PROMISE IS NOT AN ARM

The v2 card asserts of its given component: *"No comment names the bug."* **That is a promise in prose,
and this campaign has learned what those are worth.** In v3 the seeded tree sits inside the agent's
workspace, so:

1. ⛔ **NO WITHHELD IDENTIFIER MAY BE REACHABLE.** The planted defects are named in `withheld/mutants/`
   (`SevenSteps`, `UnreflectedPoly`, `HighByteIndex`, …). **A build-time gate must assert that no mutant
   id, no `withheld` path fragment and no reference-tree name occurs anywhere the agent can read** —
   file contents, file NAMES, directory names, git history of the seeded tree, and the lockfiles.
   **Driven RED by planting the name, per the standing law that an assertion of absence needs an arm that
   produces the presence.**
   ✅ **MEASURED TODAY, AND THE PROPERTY HOLDS FOR `Crc32`:** all seven mutant ids
   (`ComplementedTable · HighByteIndex · SevenSteps · ShortTable · StreamRestart · StreamZeroInit ·
   UnreflectedPoly`) occur in `B/withheld/` — **1 file each, the positive control firing** — and **0
   files** across `B/given/`, `B/Crc32/` and `B/clause.md`. **So the card's promise is true of the one
   task that has been built.** ⇒ **The requirement is that it become a GATE, not that it be repaired**:
   it holds today by the author's care, and the next four tasks have no such measurement.
   ⛔ **AND THE CHECK LIED TO ME FIRST.** My initial sweep took the ids from `ls`, which appends a
   trailing `/`, so every pattern was `SevenSteps/` and **every count was a clean zero — including the
   positive control's.** The control is the only reason I did not write "measured absent" over a broken
   instrument. ⇒ ***THE GATE MUST ASSERT ITS OWN CONTROL FIRES***, in the same run, or it will one day
   pass a tree that names every mutant.
2. ⛔ **THE SEEDED TREE'S PROVENANCE MUST NOT SHIP.** A `given/` copied with its history hands the agent
   the diff that introduced the defect. **Seed as content, never as a clone.**
3. ⚠️ **THE FENCE'S PEER GLOB IS TAKEN AT RENDER TIME.** A brownfield batch built after a greenfield batch
   leaves the earlier batch's fence permissive — measured, twice, at cost. **Brownfield cells must be
   built in the same pass as the run they belong to, or every existing fence re-rendered and drift-checked.**
4. 📌 **THE GIVEN TREE MUST BUILD.** A seeded component that does not compile converts the task into
   "repair the build", which is a different task and a much cheaper one. **Build the seed at build time
   and refuse the cell if it fails** — and record that the seed compiled, because a reader cannot tell a
   deliberate defect from a broken seed after the fact.

---

## §5 · THE ARMS — THE CONTROL'S BRIEFING IS A LARGER HAZARD HERE THAN IN GREENFIELD

The campaign's load-bearing finding is that **the control's own briefing carries a weak form of the
treatment**, which is why the placebo rung exists. **Brownfield makes this worse, because the treatment's
content substantially IS advice about how to approach code you did not write.**

⇒ **Every arm's briefing must be audited, before the first cell, for any instruction about how to read,
trust or verify the given component** — and the audit is a diff against the greenfield briefings, not a
reading. **An instruction that is innocuous in greenfield ("write a specification first") is a partial
treatment in brownfield**, because it prescribes exactly the move the treatment is supposed to supply.
⛔ **The placebo must be equal-length AND equally silent on that axis.** An equal-length placebo that
happens to say nothing about existing code is not a placebo for this form; it is a shorter control.

---

## §6 · COST AND POWER — ⛔ THE REGISTERED σ DOES **NOT** TRANSFER

The registered resolvable floor is `exp(σ√(2k/n))` with **σ = 0.30458 measured on STAGE 1**, a greenfield
population. **Brownfield cells start from working scaffolding, a fixed interface and a bounded change.**
There is every reason to expect a different dispersion and **no measurement of it whatsoever.**

⇒ 🔑 ***A FLOOR QUOTED FROM ANOTHER POPULATION'S σ IS A GATE FITTED TO DATA IT DOES NOT JUDGE.*** The
campaign has already caught itself computing a floor from the run it judges; importing a floor from a run
it does not judge is the same error facing the other way.
⇒ **REQUIRED BEFORE ANY BROWNFIELD MAGNITUDE IS REPORTED: a variance pilot, one condition, n ≥ 9**, and
the floor recomputed from **its** σ. Until then a brownfield result may report the **SIGN** only.
📌 **The sign test transfers and the floor does not** — the sign test assumes nothing about dispersion,
which is precisely why it was chosen as the primary reading.

---

## §7 · WHAT MUST BE REGISTERED BEFORE THE FIRST CELL

1. **V1 and V2 as separate verdicts**, with the path each is read from, and `unmeasured ≠ pass`.
2. **The REPAIRED / REPLACED / REMOVED class**, its measurement, and a prediction per arm.
3. **The seed's build receipt** and the no-withheld-identifier gate, both driven RED first.
4. **The variance pilot**, or an explicit registration that only the sign will be reported.
5. **The briefing diff** between greenfield and brownfield arms, published before the run.
6. ⛔ **The prediction for V1 specifically.** *"The agent will find a bug nobody pointed at"* is the
   claim this form is for. **Register the expected rate before it is observed**, or the result will be
   read against whatever it turns out to be.

---

## §8 · WHAT THIS FORM CANNOT ESTABLISH, SAID FIRST

* **It does not measure whether the method produces better code.** It measures whether an arm finds a
  planted defect and implements a stated change. **The defect is planted, and a planted defect is not a
  sample of the defects real code has.**
* **One defect per task is `k = 1` per problem.** The cross-problem sign test remains the only reading
  with a denominator, exactly as in matrix #1.
* ⛔ **A GREEN V1 does not show the agent understood the component.** It shows the withheld suite stopped
  failing. The suite's own strength is a **ceiling of 1.000 measured against mutants authored beside it**,
  and seven of those mutants die by a single test. **The margin, not the rate, is what a correctness
  claim rests on.**
* **Nothing here licenses pairing a cost premium with correctness.** If a brownfield run produces both a
  premium and a V1 rate, they are two results and **the paper must not join them with "and therefore".**

---

# ⛔⛔ ADDENDUM, 2026-09-10 — `G/` AND `B/` DO NOT MEAN IN v3 WHAT THEY MEAN IN v2
## Appended by bench after ratifying a brownfield structure built on the v2 reading of the letter.

**This document says above that "the task material largely exists" and that `Crc32` is realised as a
full `B/` tree beside its greenfield `G/`. That is true of v2 and it is not true of v3, and the two
trees wear the same two letters.**

```
  v2   tasks/systems-v2/<Task>/B/   clause.md · given/ · withheld/     GREENFIELD vs BROWNFIELD
  v3   tasks/systems-v3/<Task>/B/   interface.rs · withheld/ · …       PHASE 1 vs PHASE 2
       Crc32  G/interface.rs 37 lines   ->   B/interface.rs 68 lines   B EXTENDS G
       no `given/` and no `clause.md` anywhere under the v3 tree
```
⇒ **`B/` IS THE SPEC-CHANGE'S POST-CHANGE RUNG.** The decisive evidence is `customer.sh` itself, the
script that dispatches the change request:
```
  cp "$TASK/B/interface.rs" "$REPO/interface.rs"
```
The change request **is** the replacement of the phase-1 interface with `B/interface.rs`, and
`B/withheld/` is the suite that scores the result. The directory is not spare and not unexplained —
it is fully occupied, and the P1 spec-change wave ran on it.

## ⇒ 🔑 THE TRAP, WHICH IS WHY THIS IS WRITTEN HERE AND NOT IN A SEAT'S BANK
***THE LETTERS WERE INHERITED ACROSS A REDESIGN AND THEIR MEANING CHANGED UNDER THEM.*** A reader who
knows v2 measures v3's `B/` accurately, compares it against the v2 meaning of the letter, and
concludes *"there is no brownfield rung here"* — while the directory is in fact occupied by something
else entirely. **A name that survives a redesign is worse than a name that breaks, because nothing
announces the change.** Two seats reached that conclusion independently on the same morning, and one
of them ratified a design on it.

## 📋 WHAT FOLLOWS FOR BROWNFIELD
- **The form in this document still stands** — the RED→GREEN delta argument, the two verdicts `V1`/`V2`
  as separate columns, and the givens still needing to be authored.
- ⛔ **BUT BROWNFIELD CANNOT LIVE IN `B/`.** It needs a **THIRD** rung. Putting the given beside the
  change request's interface would let a spec-change cell read a brownfield interface, and the first
  symptom would look like a task defect rather than a collision.
- 📌 **Whatever the third rung is called, it should not be a single letter**, and this meaning shift
  should be stated wherever a reader of either convention will meet it.
