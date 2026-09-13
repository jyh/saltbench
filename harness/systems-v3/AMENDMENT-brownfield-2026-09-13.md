# AMENDMENT — THE BROWNFIELD FIELD, REGISTERED
## bench (SaltBench lead), 2026-09-13. **Ordered by the Captain at council 2026-09-12**, his order of work:
## *"Once the brownfield setup is available, go ahead and start it, preapproved"* — with the amendment FIRST,
## and its three named contents: **an arm-neutral seed · a REGISTERED planted-defect list with a
## bugs-fixed/introduced metric · the parent→child rule for spec-change.**
## ⛔ NOTHING IN THIS FILE AUTHORISES A CELL UNTIL §B7's CHECKLIST IS DISCHARGED AND ITS REDs ARE DRIVEN.

**PARENT DOCUMENTS, and this amendment does not restate them:** `DESIGN-v3-brownfield-form-2026-09-09.md`
(the form: the RED→GREEN delta argument, §2's two verdicts, §3's rewrite-escape classes, §4's fence deltas,
§5's briefing audit, §6's σ non-transfer, §8's limits) and its **2026-09-10 addendum**, which is the reason
§B1 exists. Desk row **HG** is the design family this draws on; ⛔ **HG itself remains CARRIED, NOT
COMMISSIONED** (helm ruling 09-11, re-based on the Captain's full-pilot condition at council 1730 §6) —
**brownfield is commissioned as a FIELD of the 48-condition matrix; HG's four cell designs are not.**
Conflating them would commission four designs nobody ruled on.

**THE FIELD, as the Captain defined it at council 09/12:** BROWNFIELD = *seeded with buggy code, same
requirements.* Four arms — `brownfield-plain`, `brownfield-salt-diet`, and both `+spec`. Pilot five problems,
n = 3. The five are **LZW · LRU · Paxos · FreeList · Crc32**, which is the set named in
`PREREGISTRATION-matrix-opus-1-2026-09-08.md` and no others (measured: those five appear, the other six of
the eleven task directories do not).

---

## §B1 · THE THIRD RUNG IS NAMED `brownfield/`, AND IT IS NOT A LETTER
The 09-10 addendum established that **brownfield cannot live in `B/`**: in v3, `B/interface.rs` is the
SPEC-CHANGE's post-change interface, and `customer.sh` dispatches the change request by
`cp "$TASK/B/interface.rs" "$REPO/interface.rs"`. A brownfield given placed there would be read by a
spec-change cell, and **the first symptom would look like a task defect rather than a collision.**
```
  tasks/systems-v3/<Task>/G/interface.rs           phase 1, greenfield          UNCHANGED
  tasks/systems-v3/<Task>/B/interface.rs           spec-change, post-change     UNCHANGED
  tasks/systems-v3/<Task>/brownfield/interface.rs  THE SEEDED GIVEN             NEW
  tasks/systems-v3/<Task>/brownfield/card-addendum.md   the same requirements, plus "this exists already"
```
⛔ **The word, not a letter, is deliberate and is the addendum's own instruction** ("whatever the third rung
is called, it should not be a single letter"). ⇒ 🔑 ***A NAME THAT SURVIVES A REDESIGN IS WORSE THAN A NAME
THAT BREAKS, BECAUSE NOTHING ANNOUNCES THE CHANGE*** — two seats reached the wrong conclusion about `B/` on
one morning and one of them ratified a design on it. `brownfield/` cannot be reached by either convention's
reflex.
⛔⛔ **THE PLANT REGISTRY DOES NOT LIVE IN THE TASK TREE.** It lives at
`harness/systems-v3/BROWNFIELD-PLANTS.tsv`, because the harness is never copied into a cell's repo. I
considered placing it beside the withheld suites on the reasoning that exports already strip those — and I
am NOT relying on that: **measured, the export tree I read (`…-export-79dbbc1`) carries no `withheld/` at
all, which tells me the strip happens but not WHAT RULE strips it.** A registry whose secrecy depends on a
mechanism I have not read is a leak channel I have merely not found yet. ⇒ **§B7(3) drives a RED arm that a
cell cannot read the registry, and until that arm is green the registry is not secret, it is unexamined.**

---

## §B2 · THE SEED IS ARM-NEUTRAL, AND "NEUTRAL" IS A DRIVEN CLAIM, NOT AN INTENTION
The seeded defect for each problem is authored **from the task's `card.md` alone**, before and without
reading any arm's briefing. That is a procedural claim and procedural claims rot, so it carries three
mechanical checks, each RED-driven before the first cell:
```
  N1  BYTE IDENTITY ACROSS ARMS   the four arms receive the SAME seed bytes. sha256 of brownfield/interface.rs
                                  recorded at build into ctl/seed-sha, and the scorer REFUSES a condition
                                  whose cells disagree. RED: plant a one-byte difference in one cell.
  N2  NO ARM VOCABULARY           the seed and its card-addendum contain zero tokens from the treatment's
                                  vocabulary list (the salt-diet briefing's distinctive terms, enumerated in
                                  the amendment's appendix at authoring time). RED: plant one term.
  N3  BRIEFING DIFF PUBLISHED     the greenfield->brownfield briefing diff for EVERY arm is published before
                                  the run (§5 of the design: an audit is a diff, never a reading).
```
⛔ **§5's hazard is sharper here than anywhere in the campaign and I am restating it because it is the one
that can void the field:** the treatment's content substantially IS advice about how to approach code you
did not write. **"Write a specification first" is innocuous in greenfield and is a PARTIAL TREATMENT in
brownfield.** ⇒ **The placebo must be equal-length AND equally silent on that axis.** An equal-length
placebo that merely happens not to mention existing code is **a shorter control, not a placebo for this
form** — and it would bias toward the treatment, which is the direction that flatters us.

---

## §B3 · THE PLANTED-DEFECT LIST, AND THE TWO-SIDED METRIC
`harness/systems-v3/BROWNFIELD-PLANTS.tsv`, one row per problem, **registered before any cell**, columns:
```
  problem · file · behaviour_broken · detecting_withheld_test(s) BY NAME · visible_suite_detects (MUST be no)
  · seed_sha256 · author · authored_at
```
⛔ **`visible_suite_detects` MUST BE `no` FOR EVERY ROW, and it is a DRIVEN column, not a declared one.** A
defect the visible suite catches is a defect *pointed at*, and V1 stops measuring "finds a bug nobody
pointed at" — which §7(6) of the design names as the whole claim this form exists for.

**THE METRIC. The Captain asked for bugs-fixed AND bugs-introduced, and the second one needs a baseline the
campaign has never run.** Both are read from the withheld suite at two points:
```
  BASELINE   the withheld suite run against the SEED, per problem, recorded BEFORE any cell   <- NEW, OWED
  END        the withheld suite run against the cell's end tree

  bugs_fixed        = detecting_withheld_test(s)  RED at baseline  ->  GREEN at end       (this is V1)
  bugs_introduced   = any OTHER withheld test    GREEN at baseline ->  RED at end
```
⇒ **The seed baseline is a deliverable, not a derivation.** Without it `bugs_introduced` has no reference
and would silently become "tests failing at end", which counts the planted defect itself as introduced.
⛔⛔ **AND `bugs_introduced = 0` IS A FLOOR, NEVER A ZERO.** The withheld suites' strength is a **CEILING of
1.000 measured against mutants authored beside them, with seven of those mutants dying by a SINGLE test**
(`RESULT-hidden-test-strength-v3.md`). A suite that cannot separate its own mutants by more than one test
cannot be quoted as evidence that nothing was broken. ⇒ **Report it as `bugs_introduced ≥ 0 (suite-limited)`
and quote the MARGIN beside it.** The rate is the part that reassures and the margin is the part that informs.
⛔ **V1 and V2 remain SEPARATE COLUMNS and separate result rows, and `V1 unmeasured` is reported as
unmeasured and never as passing** (design §2). `bugs_fixed` is V1 renamed for the Captain's metric, not a
third number.

---

## §B4 · THE PARENT→CHILD RULE FOR SPEC-CHANGE, AND THE BASELINE TRAP INSIDE IT
Spec-change is an **addendum on a landed cell**, so it is not a separate field: every `→spec-change` cell has
exactly one PARENT cell, and brownfield doubles the parents.
```
  PARENT KEY   (problem, model, arm, field, n-index) — written into the child's ctl/parent, and the parent's
               END sha recorded beside it. A child with no resolvable parent is VOID, not scored.
  THE TREE     the child's repo is a COPY of the parent's END tree. ⛔ NEVER a dispatch into the parent's
               cell: customer.sh commits and tags inside $CELL/repo, so dispatching into a cell that holds a
               run REWRITES that run's history, and where the cell backs a published result that is a
               CORRUPTED RECORD, not a lost experiment. (This repo's CLAUDE.md, standing law.)
  FIELD        a brownfield parent yields a BROWNFIELD child. greenfield->spec-change and
               brownfield->spec-change are different conditions and are never pooled.
```
⭐⭐ **THE TRAP, AND IT WOULD HAVE PRODUCED A FALSE FINDING AT EVERY BROWNFIELD CHILD:** `bugs_introduced` is
defined against a baseline, and **a child's baseline is its PARENT's END — not the SEED.** If the parent never
fixed the planted defect, the child inherits it still present; scored against the seed baseline the child
looks clean, and scored against nothing at all the child would be charged with a defect **it did not
introduce and its parent did not fix.** ⇒ **REGISTERED: a child's `bugs_introduced` is measured against its
parent's END, and its INHERITED V1 state is carried as its own column (`v1_inherited`).** A child cannot be
credited with `bugs_fixed` for a defect its parent already fixed.
📌 And the mirror, worth one line: a child whose parent REPLACED the given (design §3) is **not a brownfield
child in any meaningful sense** — its starting tree contains none of the seeded code. It is scored, priced and
reported, in its parent's class, and **never pooled with REPAIRED children.**

---

## §B5 · THE REWRITE-ESCAPE CLASSES ARE REGISTERED HERE WITH THEIR DISCRIMINATOR
Design §3's three classes — **REPAIRED · REPLACED · REMOVED** — are registered as a dependent variable with a
structural, harness-taken discriminator (never agent-reported): `seed_sha256` at build, the file's hash and
path at end, and a diff statistic between them.
```
  REPAIRED   the seeded file survives at its path and was EDITED      <- the only brownfield outcome
  REPLACED   the seeded file was rewritten wholesale
  REMOVED    the seeded file is gone; the component lives elsewhere
```
⛔ **A REPLACED cell is NOT void and NOT excluded** — it is priced, scored on V1/V2, and reported in its own
class. **Excluding it would delete the finding**, and "REPLACE" is exactly the behaviour an arm's briefing can
push toward, so the class is arm-correlated BY CONSTRUCTION and that is the point of measuring it.
**PREDICTION, REGISTERED BEFORE THE FIRST CELL, because a class discovered after seeing the arms is
unusable:** I predict `REPLACED` is **more common in the salt-diet arms than in plain**, on the reasoning that
a briefing which prescribes specifying-before-coding pulls toward starting clean. **I am recording this as a
prediction that runs AGAINST the treatment's convenience, and it is falsifiable at n = 3 × 5 only as a sign.**

---

## §B6 · MAGNITUDE IS NOT REPORTABLE YET, AND THE REASON IS σ
The registered resolvable floor uses **σ = 0.30458, measured on STAGE 1 — a GREENFIELD population.**
Brownfield cells start from working scaffolding, a fixed interface and a bounded change; there is every
reason to expect a different dispersion and **no measurement of it whatsoever.**
⇒ **REGISTERED: until a variance pilot (one condition, n ≥ 9) is run and the floor recomputed from ITS σ, a
brownfield result reports the SIGN ONLY.** The sign test assumes nothing about dispersion, which is why it is
the primary reading. ⇒ 🔑 ***A FLOOR QUOTED FROM ANOTHER POPULATION'S σ IS A GATE FITTED TO DATA IT DOES NOT
JUDGE*** — this campaign has already caught itself computing a floor from the run it judges, and importing one
from a run it does not judge is the same error facing the other way.
📌 **DEFAULT-IF-SILENT, so this cannot become an indefinite block:** if the variance pilot is not run, the
brownfield result ships **sign-only**, labelled so, rather than waiting. Nothing here blocks the field.

---

## §B7 · THE CHECKLIST. NO CELL FIRES UNTIL EVERY ROW IS DISCHARGED OR DEFAULTED IN WRITING
```
  1  brownfield/ rung created for all five problems; G/ and B/ byte-unchanged (driven, both directions)
  2  BROWNFIELD-PLANTS.tsv authored; visible_suite_detects DRIVEN `no` on every row
  3  RED: a cell CANNOT read BROWNFIELD-PLANTS.tsv (§B1 — the registry's secrecy is unexamined until this)
  4  the SEED BASELINE withheld-suite run, per problem, recorded (§B3 — bugs_introduced has no reference without it)
  5  N1 seed byte-identity across arms, RED-driven; N2 arm-vocabulary, RED-driven; N3 briefing diff published
  6  V1/V2 as separate CELLS.tsv columns; `unmeasured` distinct from `pass`, driven
  7  REPAIRED/REPLACED/REMOVED discriminator wired to harness-taken hashes, RED-driven
  8  parent-key resolution + COPY-not-dispatch enforced in the child builder, with a REFUSAL on an unresolvable parent
  9  the §B5 prediction and the §B6 sign-only registration, both in writing before the first cell  <- this file
```
⛔ **I HAVE WRITTEN NINE ROWS AND DISCHARGED ONE (row 9, this file).** Rows 1–8 are owed, and this amendment
is **not** the brownfield setup the Captain's preapproval attaches to — it is the registration that setup must
satisfy. **Saying "the amendment is done" and firing would be the checklist-you-work-inside defect**: I have
written the table and that is not the same as having run it.

---

## §B8 · WHAT THIS FIELD CANNOT ESTABLISH, SAID BEFORE ANY DATA
Design §8 stands in full and is not restated. The one line that must travel with every brownfield number:
**a planted defect is not a sample of the defects real code has**, one defect per problem is `k = 1`, and if a
brownfield run yields both a cost premium and a V1 rate **they are two results and the paper must not join
them with "and therefore."**
