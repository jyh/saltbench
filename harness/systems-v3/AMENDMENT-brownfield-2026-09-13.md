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

---

# ⛔⛔ CORRECTION TO §B1, SAME DAY, BEFORE ANY SETUP WAS BUILT ON IT
## The seeded artefact is `solution.rs`, NOT `interface.rs`. Measured at the canonical source tree
## (`saltbench-systems-v3`, branch `master`, `26cbbd4`), not at an export.

§B1 above names the third rung's content as `brownfield/interface.rs`. **That is wrong on a load-bearing
detail and would have mis-built the whole field.** The v3 executor brief says so in terms:
```
  EXECUTOR-BRIEF-v3.md:19   "The component is ONE file `solution.rs`; the fixed interface is
                             `interface.rs` (plain Rust, ONE neutral file, IDENTICAL IN BOTH ARMS)"
  EXECUTOR-BRIEF-v3.md:31   THE CONTAINMENT RULE: harness/systems-v3/containment.py <interface.rs> <solution.rs>
```
⇒ **`interface.rs` is the FIXED, ARM-NEUTRAL interface the agent is GIVEN. `solution.rs` is what the agent
WRITES and what every suite scores.** A planted defect in `interface.rs` would not be "seeded with buggy code"
at all — it would corrupt the one file the design guarantees is identical across arms, which is the opposite
of §B2's whole purpose.

## ⇒ THE RUNG, CORRECTED
```
  tasks/systems-v3/<Task>/brownfield/solution.rs      THE SEEDED, DEFECTIVE COMPONENT     <- the seed
  tasks/systems-v3/<Task>/brownfield/card-addendum.md "this component already exists"
  interface.rs        NOT copied, NOT altered — the cell takes G/interface.rs exactly as greenfield does
  SCORING             G/run_tests.sh + G/withheld/{tests,mutants,reference,controls,tags.json}
                      "seeded with buggy code, SAME REQUIREMENTS" ⇒ the same suite, by construction
  containment.py      still applies, unchanged: the seed must itself satisfy it, or the cell starts illegal
```
⛔ **CONSEQUENT EDITS elsewhere in this amendment, so it does not contradict itself:** §B3's `file` column and
`seed_sha256` are the sha of **`solution.rs`**; §B5's discriminator ("the seeded file survives at its path and
was EDITED") is about **`solution.rs`**; §B7 row 1's "G/ and B/ byte-unchanged" now also requires that
**`brownfield/` contains no `interface.rs` at all** — its presence would be the collision, and it is cheap to
assert.

## ⇒ 🔑 THE LESSON, AND IT IS THIS AMENDMENT'S OWN §B1 TURNED ON ITS AUTHOR
§B1 exists because `B/` does not mean in v3 what it meant in v2, and it says: *a name that survives a redesign
is worse than a name that breaks, because nothing announces the change.* **I then assumed what `interface.rs`
was from its name, without reading the brief that defines it** — the same error one level down, inside the
section warning against it. ⇒ ***A DOCUMENT THAT WARNS ABOUT UNREAD NAMES IS NOT THEREBY WRITTEN BY SOMEONE
WHO READ THEM.*** The correction cost ten minutes because the seed had not been authored yet; it would have
cost the field if row 1 had been built first.
📌 **And it is why §B7 row 1 is a checklist row rather than an assumption:** the recon that found this was the
first act of discharging it.

---

# ADDENDUM 2 — 2026-09-13, bench. **§B7 ROW 2 CANNOT BE DISCHARGED AS WRITTEN, BECAUSE THERE IS NO VISIBLE SUITE**

⛔⛔ **THE MEASUREMENT, taken at the builder and confirmed at a built cell.** §B3 requires
`visible_suite_detects` to be **`no` for every row** and §B7 row 2 requires that column **DRIVEN**, not
declared. Driving it requires a visible suite to run. **A v3 cell has none.**

```
  cell_build.py:636   copy(<rung>/interface.rs -> repo/interface.rs)
  cell_build.py:637   copy(<rung>/interface.rs -> repo/solution.rs)      <- solution.rs IS the stub set
  cell_build.py       os.makedirs(repo/"tests"); open(repo/"tests/.keep","w").close()   <- CREATED EMPTY
  cell_build.py:14    "At t0 solution.rs is a copy of interface.rs: the stubs compile, so bin/rt check is GREEN"
```
**A cell repo receives:** `REQUIREMENTS.md` · `interface.rs` · `solution.rs` (the stubs) · `Cargo.toml` ·
an **empty** `tests/` · `inbox/` · `memory/` · `BANK.md` · `BUS.md` · the overlay. **No withheld tests, no
visible tests, no traces, no `run_tests.sh`.**
✅ **POSITIVE CONTROL ON THE ABSENCE:** grepping `cell_build.py` for `run_tests|driver_lib|withheld|traces`
returns **nothing**, while greps for `interface.rs|copytree|card` in the same file return plenty — so the
grep works and the zero is a reading.
**And `bin/rt` offers exactly `check` · `build` · `test`, where `test` builds `tests/driver.rs` — a file
the AGENT writes** (it reports `ABSENT tests/driver.rs` when the agent has not).

⇒ 🔑 ***THE COLUMN IS VACUOUS BY CONSTRUCTION. A "DRIVEN `no`" ON AN EMPTY SUITE IS A GREEN THAT TESTS
NOTHING — AND IT WOULD BE A REGISTERED ONE, WHICH IS WORSE THAN AN ABSENT CHECK.*** This is the same
defect the parent amendment warns about in its own §B7 note ("I have written the table and that is not the
same as having run it"), one level down: **the row was written against a suite that does not exist.**

## THE REPLACEMENT — THREE CHECKS THAT CAN ACTUALLY BE DRIVEN, AND WHAT EACH PROTECTS
```
  S1  THE SEED COMPILES AND `bin/rt check` IS GREEN AT t0.
      WHY: greenfield's t0 property is that the stubs compile. A seed that does not compile starts every
      brownfield cell RED, and every arm spends its first turns FIXING THE BUILD -- which confounds
      "finds the seeded bug" with "repairs a broken given", in a form that looks like effort.
  S2  THE WITHHELD SUITE FAILS ON THE RAW SEED, AND THE FAILING TESTS ARE NAMED FROM THAT RUN.
      WHY: this is what makes `detecting_withheld_test(s) BY NAME` EVIDENCE rather than an assertion, and
      it is the only thing that makes "did not fix the bug" MEASURABLE. A seed the withheld suite does not
      catch scores identically whether the agent fixes it or ignores it.
  S3  NO COMPILER DIAGNOSTIC POINTS AT THE SEED (`rt check` / `rt build` emit no warning naming it).
      WHY: this is the TRUE analogue of the intent behind `visible_suite_detects: no`. The agent's only
      harness-supplied signal is the compiler. A seed the compiler flags is a seed POINTED AT, and V1
      stops measuring "finds a bug nobody pointed at" -- which is the original sentence's whole purpose.
```
📌 **THE INTENT OF §B3'S COLUMN IS PRESERVED AND ITS MECHANISM IS REPLACED.** Nothing here weakens the
requirement; S3 is the same requirement aimed at the signal that actually exists.

## AND THE AUTHORING METHOD THIS UNLOCKS — DERIVE THE SEED FROM THE MEASURED MUTANT SET
Each task already carries `G/withheld/mutants/` (LZW/G: `kwkwk_dropped` · `encoder_extends_before_emitting`
· `decoder_extends_before_emitting` · `dict_seeded_255`), and
`RESULT-hidden-test-strength-v3.md` **already records that all 44 are killed and at what MARGIN** — the
number of withheld tests that actually fail on each.
⇒ **A seed derived from a mutant whose kill margin is already measured arrives with S2 nearly discharged
and its detection evidenced rather than hoped for.** ⛔ **And the margin is the selection criterion, not
the kill:** a mutant killed by ONE test is a fragile seed — the whole two-sided metric would then rest on
a single test — while `LZW/G dict_seeded_255` is killed at **margin 5 of 8**. **Prefer high margin.**
⚠️ **The mutants live under `withheld/`, which no export carries, so this reuses a withheld artefact
without exposing it** — but §B7(3)'s RED arm (a cell cannot read the registry) now covers a second object
and must be driven against **both** the registry and any seed provenance note.

## SCOPE OF THIS ADDENDUM
**It changes no measurement, because no brownfield cell has fired** — it replaces a checklist row that
could not be discharged as written, before the first call, which is the form this campaign requires.
**§B7 row 2 is superseded by S1 · S2 · S3 above. Rows 1 and 3–8 stand unchanged.**

---

# ADDENDUM 3 — 2026-09-13, bench. **THE SEED SELECTION FOR ALL FIVE, REGISTERED BEFORE ANY CELL**

Derived from `results/hidden-test-strength-2026-09-04.json` — **the margin, per mutant, per task**: the
number of withheld tests that FAIL on it. Read here **forwards**, before the run, which is what the
parent result file recommended and nothing had yet done.

```
  LZW/G       5/8   dict_seeded_255          6/8  decoder_extends   6/8  kwkwk_dropped   8/8  encoder_extends ⛔LOUD
  LRU/G       5/16  put_duplicates           6/16 get_no_touch      7/16 evict_mru       9/16 capacity_off_by_one
  Paxos/G     1/17  own_value ⛔FRAGILE      2/17 accept_below_promise  4/17 forgetful_promise  6/17 small_quorum
  FreeList/G  1/7   free_leaks ⛔FRAGILE     3/7  align_ignored     6/7  trivial         7/7  header_past_end ⛔LOUD
                                                                                        7/7  split_off_by_one ⛔LOUD
  Crc32/G     5/6   ALL FIVE at 5/6 — ComplementedTable · HighByteIndex · SevenSteps · ShortTable · UnreflectedPoly
```
**THE TWO EXCLUSION RULES, and they are opposite failures of the same quantity:**
- ⛔ **MARGIN 1 IS FRAGILE.** The entire two-sided metric would rest on ONE withheld test. If that test is
  ever weakened, retired, or simply does not probe a particular rewrite, the seed becomes undetectable and
  a cell that ignored the bug scores identically to one that fixed it. **`own_value`, `free_leaks`: OUT.**
- ⛔ **MARGIN == TOTAL IS LOUD.** A defect that fails EVERY test breaks the basic round trip, so any agent
  that writes a single smoke test finds it in its first turn. That puts the field at a CEILING and
  measures nothing about method. **`encoder_extends_before_emitting`, `header_past_end`,
  `split_off_by_one`: OUT.** (The parent result file already said these say the LEAST about suite
  strength — *loud, not discriminating*. The same property disqualifies them as seeds, for the same reason.)

**THE SELECTION:**
```
  LZW        dict_seeded_255   5/8    ✅ AUTHORED AND DRIVEN THIS SHIFT (S1·S2·S3)
  Paxos      small_quorum      6/17   the ONLY comfortably robust candidate — the other three are 1, 2 and 4 of 17
  FreeList   align_ignored     3/7    the ONLY viable candidate: one fragile, two loud, one near-loud (6/7)
  LRU        get_no_touch      6/16   preferred over put_duplicates (5/16): a recency bug needs a SEQUENCING
                                      test, so it is not reachable by single-operation poking
  Crc32      ⚠️ SEE BELOW — no choice available on this axis
```
⇒ 🔑 ***IN TWO OF FIVE TASKS THE MARGIN DATA REDUCES FOUR CANDIDATES TO ONE. THE SEED CHOICE WAS NEVER
FREE; IT ONLY LOOKED FREE BECAUSE NOBODY HAD READ THE MARGINS.*** Had these been chosen by plausibility —
and `free_leaks` and `own_value` are the most natural-sounding bugs in their tasks — **two of five seeds
would have rested on a single test each**, and nothing in the pipeline would have reported it.

## ⚠️ Crc32 IS A WEAK BROWNFIELD TASK AND THAT IS A PROPERTY OF THE TASK, NOT A CHOICE I AM MAKING
All five of its mutants fail **5 of 6** tests — 83% of the suite. There is no discriminating seed available:
every defect it offers is loud. **Registered as a limitation before the run rather than discovered in the
analysis.** Options, for the helm, and I am NOT ruling between them: (a) run Crc32 and expect it to sit at
a ceiling, reporting it as such; (b) drop Crc32 from the brownfield pilot and run four problems;
(c) author a NEW non-mutant defect for Crc32 — which forfeits the measured-detection property that makes
every other row evidence, and would need S2 driven from scratch.
📌 **My recommendation is (a): run it and report the ceiling.** A task that cannot discriminate is itself a
finding about the substrate, it costs one cell per arm, and (b) silently changes the registered population
while (c) trades the one property that makes this selection method trustworthy.

## ⛔ THE STRIP IS A JUDGEMENT; THE AUDIT IS MECHANICAL. DO NOT CONFUSE THEM (method note, 2026-09-13)
Every mutant announces itself, in a leading header and often at the mutation site. Both must go.
**The rule I used for LZW — "drop everything before `===== INTERFACE REGION BEGIN =====`" — IS WRONG IN
GENERAL AND WORKED BY LUCK.** Verified after the fact: LZW's mutant header happens to run right up to
that marker, so the cut removed 7 lines all of which were tells and no legitimate content. ⛔ **`FreeList`
breaks it**: its 3-line `// MUTANT: align_ignored …` header is followed by the FILE'S OWN descriptive
header (*"a first-fit allocator over a word-addressed arena… every block carries a two-word in-band
header"*) and only then the marker. Cutting at the marker would **delete real documentation the given
should carry**, changing the artefact's character and making the brownfield rung quietly terser than the
code a caller would actually inherit.
```
  STRIP   drop the leading contiguous comment block ONLY while every line in it is a tell or an empty
          comment; STOP at the first comment line that is legitimate content. This is per-file and it is
          a JUDGEMENT — inspect the head of each mutant before cutting.
  AUDIT   then grep the ARTEFACT for  WRONG|MUTANT|<mutant-name>|reference implementation|reference verbatim
          and require ZERO. Mechanical, and it is what catches a bad strip.
```
⇒ 🔑 ***A MECHANICAL AUDIT OVER A JUDGEMENT-MADE CUT IS SOUND; A MECHANICAL CUT WITH NO AUDIT IS NOT —
AND THE TWO ARE EASY TO CONFUSE BECAUSE BOTH END IN A GREEN.*** LZW passed its audit and would have
passed it just as happily had the cut eaten four lines of real documentation.

---

# ADDENDUM 4 — 2026-09-13, bench. **S3 DISQUALIFIED FreeList's ONLY MARGIN-VIABLE SEED, AND THE COMPILER WAS THE SIGNPOST**

Addendum 3 selected `align_ignored` (margin 3/7) for FreeList as **the only candidate surviving the
margin rules**. Driving S3 on the authored artefact **failed it**, and the reason is the sharpest thing
this field has turned up so far:
```
  warning: unused variable: `a`
    --> solution.rs:80:40
  80 |  pub fn malloc(&mut self, n: usize, a: usize) -> Option<Region>
```
**`a` is the ALIGNMENT parameter, and `align_ignored` is the mutant that ignores alignment.** ⇒ 🔑 ***THE
COMPILER NAMES THE SEEDED DEFECT, BY PARAMETER, AT ITS OWN LINE — AND `rt check` IS THE FIRST THING ANY
CELL RUNS.*** A defect that rustc points at is a defect POINTED AT; V1 would stop measuring "finds a bug
nobody pointed at" for that problem entirely.
📌 **This is why S3 replaced the vacuous `visible_suite_detects` and not merely supplemented it.** The
compiler is the ONLY harness-supplied signal a v3 cell has, and it turned out to carry a real one.

## THE FULL FreeList PICTURE, EVERY CELL DRIVEN
```
  mutant              margin   S3 (no diagnostic)                            verdict
  align_ignored        3/7 ✅  ⛔ FAILS — rustc names the unused `a`          POINTED AT
  free_leaks           1/7 ⛔  ✅ passes, 0 warnings                          fragile only
  trivial              6/7     ⛔ FAILS — 4 warnings (unused `n`, …)          pointed AND absurd
                                          "malloc always refuses" as a GIVEN
  header_past_end      7/7 ⛔  —                                             LOUD
  split_off_by_one     7/7 ⛔  —                                             LOUD
```
⇒ **NO FreeList MUTANT PASSES BOTH RULES.** That is a second task, after Crc32, that the existing mutant
set cannot supply a clean seed for — **and for an entirely different reason, found by an entirely
different check.** Two of five, both found before any cell, which is what the checklist is for.

## ⚖️ THE DECISION, TAKEN AND OPEN TO REVERSAL — `free_leaks`, WITH THE EXCEPTION NAMED
**FreeList's seed is `free_leaks`.** It is subtle, plausible, builds clean, and fails **exactly one**
withheld test — `exhaust_and_recover` — driven: `TESTS 6/7`, rc 1.
**Why the margin-1 rule is waived HERE and not in general:** its rationale is that a rewrite the single
test does not probe leaves the seed undetectable. `exhaust_and_recover` tests the *property the defect
destroys* (the arena drains and cannot recover), not an incidental symptom, so **a rewrite that still
leaks still fails it.** The residual risk is suite EVOLUTION, not rewrite variety.
⛔ **MITIGATION, and it is a requirement on the scorer, not a hope:** the scorer **must assert that
`exhaust_and_recover` EXISTS and RAN** for any FreeList brownfield cell. If that test is ever renamed or
retired, FreeList's rows must go **UNMEASURED, never PASS** — which is exactly the failure mode the
margin-1 rule exists to prevent, made visible instead of prevented.
📌 **The alternatives, rejected and recorded so the choice is reviewable:** (a) `align_ignored` with the
warning silenced — ⛔ **that is me deleting a genuine compiler diagnostic to hide the defect**, and S3
would then pass BY CONSTRUCTION for that row, which is not the same evidence as the other three;
(b) drop FreeList — a real option, but it shrinks a registered population to avoid naming an exception;
(c) author a non-mutant defect — forfeits the measured-detection property that makes every other row
evidence. **If the helm prefers (b), the row is deleted and nothing else changes.**

---

# ADDENDUM 5 — 2026-09-13, bench. **§B7 ROW 3: THE RULE COVERS THE REGISTRY; THE DRIVE DOES NOT EXIST; AND THE ARM THAT LOOKS LIKE COVERAGE IS NOT**

Row 3 requires a RED arm proving **a cell cannot read `BROWNFIELD-PLANTS.tsv`**. Status, measured:

**✅ THE RULE COVERS IT.** `render_fence_v3.py` line 80 denies **`~/projects`** wholesale — *"the fleet
tree: the bus, the seat repo, every campaign checkout"* — and the registry lives at
`…/saltbench/harness/systems-v3/BROWNFIELD-PLANTS.tsv`, inside it. The class-C cells' rendered fence
agrees from the other direction: `denyRead: ["/Users/<owner>", "/Volumes", "/private/tmp",
"/private/var/folders"]`, a blanket home deny.

**⛔ THE DRIVE DOES NOT EXIST, AND THE NEAREST-LOOKING ARM IS NOT IT.** The class-C fence battery carries
an arm called **`F-harness-tree`**, which reads like coverage of "the harness". It runs:
```
  arm F-harness-tree  fail "Operation not permitted"  "cat $R/_bin/SHA256-16.txt"
```
`$R/_bin` is the **EXECUTOR ROOT's** bin — a different harness entirely from the one holding the registry.
✅ **Measured with a positive control: the battery contains ZERO occurrences of `saltbench`, against SIX of
`projects/claude`** — so its arms do use that root, and the registry's tree is simply not among them.
⇒ 🔑 ***AN ARM NAMED FOR A TREE IS NOT AN ARM FOR EVERY TREE OF THAT NAME, AND A BATTERY READING
`39 OK / 0 BAD` INVITES THE READER TO ASSUME OTHERWISE.*** This seat's own card — *an arm that names one
member of a set goes vacuous rather than failing* — arriving as a measurement rather than an aphorism.

**⇒ ROW 3 REMAINS OPEN, AND WHAT WOULD CLOSE IT IS SPECIFIC:** an arm, driven **inside a real brownfield
cell**, that attempts to read `BROWNFIELD-PLANTS.tsv` by its full path and expects `Operation not
permitted` — **in BOTH layers**, because `sandbox.filesystem.denyRead` fences SUBPROCESSES while
`permissions.deny` fences the CLI's OWN TOOLS, and historically only one was ever populated. It cannot be
driven before the first brownfield cell exists, and **a static read of the deny list is not a drive**: these
sets are globs taken at RENDER TIME, and a glob that grows after the render leaves the earlier cells
permissive.
📌 **Recorded rather than quietly deferred**, because "the fence denies `~/projects`" is exactly the kind of
true-and-undriven sentence that reads as a discharged row in a checklist.

---

# ADDENDUM 6 — 2026-09-13, bench. **§B7 ROW 4 IS DISCHARGED FOR THE FOUR SEEDED PROBLEMS**

`harness/systems-v3/BROWNFIELD-SEED-BASELINE.tsv` — **48 rows, one per withheld test per problem**, each
taken from that test's own run against the raw seed, before any cell. Not counts: the **per-test** state,
because `bugs_introduced` is defined as *any OTHER test GREEN at baseline going RED at end* and a count
cannot answer that.
```
  LZW        3 GREEN /  5 RED        LRU        10 GREEN / 6 RED
  Paxos     11 GREEN /  6 RED        FreeList    6 GREEN / 1 RED
```
The RED rows are exactly the seeded defect's detectors and they match `BROWNFIELD-PLANTS.tsv`'s
`detecting_withheld_tests` column test-for-test — **the two files are independent renderings of the same
runs, so a disagreement between them is a real alarm rather than a formatting difference.**
📌 The amendment's own warning, now concrete: **without this file `bugs_introduced` silently becomes
"tests failing at end", which counts the PLANTED DEFECT ITSELF as introduced** — the metric would report
every arm as having introduced a bug it was handed.
⛔ **And `bugs_introduced = 0` remains a FLOOR, never a zero** (suite-limited; report the margin beside it).
**Crc32 is absent from this file for the same reason it is absent from the plants registry: it awaits its ruling.**

---

# ADDENDUM 7 — 2026-09-13, bench. **§B7 ROW 5 SPLITS: N2 IS DRIVEN; N1 AND N3 CANNOT RUN BEFORE A CELL**

**✅ N2 — NO ARM VOCABULARY — DRIVEN ON ALL FOUR SEEDS: ZERO hits, against a control that fires.**
The pattern was **IMPORTED from `neutrality_grep.py`, never retyped** — the same law the fleet ruled for
its commit hooks the same morning (*every hook IMPORTS its repo's gate patterns*), because a copied
pattern list is a stale fixture the day the original moves.
```
  LZW 0 · Paxos 0 · LRU 0 · FreeList 0        CONTROL ("we prove the specification here") -> 2 hits
```
📌 **AND THE STANDING GATE ALREADY COVERS IT AT BUILD TIME, which I verified rather than assumed:**
`cell_build.py` runs `neutrality_grep.py` **over the finished tree** with METHOD_FILES excluded *by path*,
and **refuses** on a hit. A brownfield seed lands at `repo/solution.rs` — inside the scanned tree, not a
method file — **so it is scanned by construction.** The drive above is what §B2 asks for (RED-driven
*before* the first cell); the build-time gate is what keeps it true per cell afterwards. **Neither
substitutes for the other.**
⚠️ **Arm-neutrality by PROVENANCE was not accepted as evidence.** The seeds derive from mutants authored
long before any treatment existed, which is a good argument and not a measurement. It is now measured.

**⛔ N1 (seed byte-identity across arms) and N3 (the briefing diff published) CANNOT BE DRIVEN YET.**
N1's subject is `ctl/seed-sha` agreeing across a condition's four cells, and its RED is *plant a one-byte
difference in ONE cell* — there are no cells. N3's subject is the greenfield→brownfield briefing diff,
and the brownfield briefing is part of cell construction. **At the source both are byte-identical by
construction — ONE file per problem in the task tree, copied to every arm — and "by construction" is
exactly the claim N1 exists to stop anyone resting on.**
⇒ **Row 5 is therefore N2 ✅ / N1 ⏸ / N3 ⏸, and the two pauses are ORDERING, not omission.** Like row 3,
they sit after cell construction, and saying so is the difference between a deferred row and a forgotten one.

---

# ADDENDUM 8 — 2026-09-13, bench. **ROWS 6, 7, 8 SCOPED AND NOT STARTED, WITH THE REASON**

All three are **harness work needing no cell**, so they are the next available items and **nothing about
them waits on the credential rotation.** Scoped here so the next head does not re-derive it.
```
  row 6  V1/V2 as SEPARATE CELLS.tsv columns, `unmeasured` distinct from `pass`, DRIVEN.
         Touches referee_v3.py, where V1/V2 are today defined for SPEC-CHANGE (V1 GREEN iff
         regressions_failed == 0; V2 GREEN iff clause_failed == 0). Brownfield reads the same two
         columns through §B3's bugs_fixed / bugs_introduced -- and the amendment is explicit that
         bugs_fixed is V1 RENAMED, not a third number. ⇒ A VERDICT PATH.
  row 7  the REPAIRED / REPLACED / REMOVED discriminator wired to HARNESS-TAKEN hashes, RED-driven.
         ⇒ A VERDICT PATH, and the hashes must be taken by the harness precisely because a
         subject-reported hash is the subject grading itself.
  row 8  parent-key resolution + COPY-not-dispatch enforced IN THE CHILD BUILDER, with a REFUSAL on an
         unresolvable parent. ⇒ Not a verdict path, but it is the guard that stops a dispatch into a
         cell that already holds a run -- which this repo's CLAUDE.md calls a CORRUPTED RECORD, not a
         lost experiment. The cheapest of the three to get wrong invisibly.
```
⛔ **WHY THEY ARE NOT STARTED, and it is the same reasoning that was right once already today.** A5.6(b)
left FIX 3 unbuilt because *"it changes the gate's control flow on the path a verdict runs through, and a
gate that mis-runs is worse than one that visibly skips."* That judgement was correct: building it this
shift took three fixtures, a red-first baseline and five RED plants, and it surfaced a defect the
specification had not named. **Rows 6 and 7 are that same class of change**, and they deserve the same
drive from a head with a full shift in front of it rather than the tail of one.
📌 **Row 8 is the one to take first** — it is a REFUSAL, its RED is cheap to construct (an unresolvable
parent key), and it protects evidence rather than producing a verdict.

---

# ADDENDUM 9 — 2026-09-13, bench. ⛔⛔ **THE BROWNFIELD RUNG IS REGISTERED AND NOT BUILDABLE, AND THE OBVIOUS COMMAND FOR IT BUILT A SPEC-CHANGE CELL SILENTLY**

**The seeds authored this shift cannot be consumed by anything.** Measured at the builder, with a
positive control: `cell_build.py` contains **ZERO occurrences of `brownfield`** against **22 of `phase`**,
and its rung selection is a binary fork on an unvalidated `type=int` flag:
```
  rung = os.path.join(task, "G" if a.phase == 1 else "B")        # anything != 1 selects B/
```
`a.phase` is used at **five** sites and validated against a permitted set at **none**. ⇒ **`--phase 3` —
the natural reach for a third rung, now that §B1 registers one — would have built:**
```
  rung          B/interface.rs      the SPEC-CHANGE post-change interface, as the given
  requirements  rendered WITHOUT `--change`      (that flag is gated on phase == 2)
  precondition  the phase-2 end-1 check SKIPPED  (also gated on phase == 2)
  ctl/task      "<task>\t3\t<nonce>"             so a scorer keying on the phase pools it NOWHERE
```
**An incoherent cell, produced silently by the obvious command**, and every symptom of it would have
looked like a task defect rather than a builder one — which is the exact failure mode §B1 chose the
NAME `brownfield/` to avoid, arriving through the FLAG instead.
📌 **AND IT IS THE FILE'S OWN DOCUMENTED DEFECT, ONE MEMBER OVER.** `cell_build.py` already carries a long
note beginning *"A `--phase 2` BUILD ON A FRESH CELL PRODUCES A CELL THAT IS NOT A SPEC-CHANGE CELL, AND
NOTHING VALIDATED IT… `--phase` was `type=int, default=1` with no precondition at all."* That repair added
a precondition **for phase 2** and left the general hole open. ⇒ 🔑 ***A GUARD KEYED TO ONE MEMBER OF A SET
DOES NOT FAIL WHEN THE SET CHANGES — IT GOES VACUOUS, AND THE SET CHANGED THE DAY THIS AMENDMENT LANDED.***

## ✅ FIXED, FAIL-CLOSED, AND DRIVEN — `cell_build.py` REFUSES AN UNKNOWN PHASE
It names the brownfield rung as **registered but not buildable**, so the next person to reach for it is
told the truth instead of receiving a spec-change cell.
```
  --phase 3   REFUSE rc 4, naming brownfield/ as registered-but-unbuildable
  --phase 1   passes the guard, hits the pre-existing missing-card.md refusal
  --phase 2   passes the guard, hits the pre-existing end-1 precondition
```
**Each arm flips only its target; the guard shadows neither existing refusal.** Predecessor kept beside it
as `cell_build.py.pre-phase-guard`.

## ⇒ THE CRITICAL PATH FOR THIS FIELD, NAMED
**Teaching `cell_build.py` the third rung is now the blocker for every remaining brownfield row**, and it
supplies the `field` component that §B4's parent key needs and that **no cell carries today** (measured:
no harness file references `ctl/parent`, against three referencing `ctl/arm`; and n1a-pro has 34 `ctl/`
files and no `parent`). ⇒ **§B7 row 8's COPY-not-dispatch half is BUILT (`cell_copy_v3.py`, 18/18
selftest); its PARENT-KEY half cannot be built until a cell can carry a `field` at all.**
⚠️ **"The seeds are authored" is not "a brownfield cell can be built", and this amendment would have read
as though it were.**

## ⚖️ THE THIRD RUNG, SPECIFIED — so it is built once and not re-derived (bench, 2026-09-13)
Written in the shape A5.6(b) used for gate FIX 3. ⚠️ **THIS PARAGRAPH SAID "deliberately not built at the
tail of a shift" AND THAT IS NO LONGER TRUE — IT WAS BUILT AND DRIVEN THE SAME SHIFT; see ADDENDUM 10.**
The line is corrected rather than deleted because a spec that says "not built" while the thing is built is
the stale-DONE shape in the other direction, and this document has already been corrected once for a name
that outlived its object.

**IT IS A `--field`, NOT A `--phase`.** Phase is the GREENFIELD→SPEC-CHANGE axis and brownfield is
orthogonal to it: a brownfield cell can itself later take a spec-change (§B4 says so — *"a brownfield
parent yields a BROWNFIELD child"*). Overloading `--phase` would make the two axes one and make
`brownfield→spec-change` inexpressible.
```
  --field {greenfield,brownfield}   default greenfield.  Written verbatim to ctl/field.
                                    REFUSE `--field brownfield` when <task>/brownfield/solution.rs is absent.
                                    REFUSE `--field brownfield --phase 2` for now: the parent-key half of
                                      §B7 row 8 does not exist, so the child could not name its parent.
```
**WHAT CHANGES IN THE BUILD, and it is SMALLER than it looks — three lines and a refusal:**
```
  rung             UNCHANGED: G/ at phase 1.  ⛔ interface.rs is STILL G/interface.rs, copied as today —
                   §B1's corrigendum: interface.rs is the fixed, arm-neutral interface, IDENTICAL IN BOTH
                   ARMS, and a brownfield cell takes it exactly as greenfield does.
  solution.rs      <- <task>/brownfield/solution.rs      (instead of a second copy of interface.rs)
                   THIS IS THE ONLY FILE THAT DIFFERS FROM A GREENFIELD CELL AT t0.
  REQUIREMENTS.md  the card rendering, PLUS <task>/brownfield/card-addendum.md appended.
                   ⛔ THE ADDENDUM IS NOT WRITTEN YET and it is the one piece needing JUDGEMENT, not
                     plumbing: it must say "an implementation exists already" WITHOUT saying "it is
                     buggy" (that is the finding V1 measures) and WITHOUT any term from §B2's N2 list.
  ctl/field        "brownfield\n"  — the component §B4's parent key needs and no cell carries today.
  ctl/seed-sha     sha256 of the seed AS COPIED, for §B2's N1 byte-identity check across arms.
```
**THE DRIVES IT OWES, red-first:**
```
  R1  --field brownfield with no brownfield/solution.rs        -> REFUSE            (both directions)
  R2  --field brownfield --phase 2                             -> REFUSE, for now  (both directions)
  R3  a built brownfield cell: repo/solution.rs == the seed BYTE-FOR-BYTE; repo/interface.rs ==
      G/interface.rs BYTE-FOR-BYTE; ctl/field == brownfield; ctl/seed-sha == the registry's seed_sha256
  R4  a built GREENFIELD cell is BYTE-IDENTICAL to one built before this change — the no-regression arm,
      and the one that matters most, because this edits the path every existing cell is built on
  R5  the neutrality grep still passes on the finished brownfield tree (it scans repo/, so the SEED is
      in scope — verified this shift, and R5 is what keeps it verified)
```
📌 **`--field` also finally lets `CELLS.tsv` separate greenfield from brownfield rows, which §B7 row 6
needs and which is today impossible: the two fields are indistinguishable in a built cell.**

---

# ADDENDUM 10 — 2026-09-13, bench. ✅ **THE THIRD RUNG IS BUILT AND DRIVEN. `--field` IS LIVE.**
*Task tree `457443c`. The predecessor is kept beside it as `cell_build.py.pre-field`.*

**`--field {greenfield,brownfield}`, not a `--phase`** — §B4 says a brownfield parent yields a brownfield
CHILD, so overloading phase would have made `brownfield→spec-change` inexpressible and pooled two
conditions. `interface.rs` is UNCHANGED and still from `G/`; **`solution.rs` is the only file that differs
from a greenfield cell at t0**; `ctl/field` and `ctl/seed-sha` are written; the card addendum is appended
to `REQUIREMENTS.md`.

```
  R1  a missing seed or addendum         REFUSE  — "a brownfield cell without it would be a GREENFIELD
                                                   cell wearing the label, and nothing downstream could tell"
  R2  --field brownfield --phase 2       REFUSE  — row 8's parent-key half does not exist
      CONTROL: --phase 2 ALONE still hits the older state refusal ⇒ I shadowed nothing
  R3  a built brownfield cell            solution.rs == the seed BYTE-FOR-BYTE · interface.rs ==
                                         G/interface.rs BYTE-FOR-BYTE · ctl/field = brownfield ·
                                         ctl/seed-sha == the registry's seed_sha256 · addendum present
  R4  NO REGRESSION                      a greenfield cell built AFTER the change is CONTENT-IDENTICAL to
                                         one built before — tree 897c1ce0…, `diff -r` excluding .git EMPTY
  R5  neutrality                         ctl/neutrality.log: "neutrality: zero hits" on the finished tree
```
⛔ **R2 WAS DRIVEN ONCE IN THE WRONG ORDER AND PROVED NOTHING** — the older phase-2 STATE refusal fired
first and shadowed it. The check now sits **ahead** of that one, which is also where it belongs on the
merits: it is ARGUMENT VALIDITY, true or false whatever the cell's state, and it needs no toolchain, so
it can be driven. That is the same reasoning the older comment there already gives for its own placement.
⇒ 🔑 ***AN ARM THAT FIRES BEHIND AN EARLIER GATE IS NOT A WEAK ARM, IT IS AN UNTESTED ONE — AND IT LOOKS
EXACTLY LIKE A PASSING ONE, BECAUSE SOMETHING DID REFUSE.***

⭐ **R4 IS THE ONE THAT MATTERED and it needed its own correction.** It first read as a FAILURE because I
compared the `root` the builder PRINTS — **a COMMIT sha, which embeds the clock.** Two runs of the SAME
builder, one second apart, differ there by construction. The TREE is the content identity and is stable;
`cell_manifest.py` was already keyed on it. ⇒ **A no-regression arm is only as good as the object it
compares, and "root" was the wrong one.**

## ⇒ §B7 STATE
```
  row 1 ✅ 4 of 5     row 2 ✅ superseded, driven      row 4 ✅ 48 baseline rows     row 9 ✅
  row 5  N2 ✅ · N1 ⏸ · N3 ⏸        row 3 OPEN — needs a cell, AND A CELL CAN NOW BE BUILT
  rows 6, 7 OWED (verdict paths)    row 8: COPY-not-dispatch ✅ · parent-key now UNBLOCKED (ctl/field exists)
```
**The blocker named in addendum 9 is gone.** Rows 3, 5(N1), 5(N3) and row 8's parent-key half were all
waiting on a buildable cell; they are now waiting only on someone to drive them.

---

# ADDENDUM 11 — 2026-09-13, bench. **§B7 ROW 3: ONE LAYER DRIVEN, ONE NAMED. THE HALF-ANSWER IS STATED AS A HALF.**

Row 3 became drivable the moment a brownfield cell could be built (addendum 10). It has **TWO layers**, and
only one of them is now driven.

**✅ THE HOOK LAYER — `permissions.deny` / the attempt audit — IS DRIVEN.**
```
  a cell attempting  cat …/harness/systems-v3/BROWNFIELD-PLANTS.tsv   -> rc 2  BLOCK, reason on stderr
  CONTROL            cargo build --offline                            -> rc 0  ALLOW
  the hook's own selftest                                             -> 84 of 84 arms fired
```
The hook's deny set carries `~/projects`, which the registry sits inside. **The registry is not readable by
a cell through the tool surface.**

**⛔ THE SANDBOX LAYER — `sandbox.filesystem.denyRead`, which fences SUBPROCESSES — IS NOT DRIVEN, AND
CANNOT BE FROM A BUILT CELL ALONE.** A built cell carries **no `fence.json`**: the fence is rendered at
LAUNCH, not at build. Attempting to render one standalone, `render_fence_v3.py` **REFUSED**, correctly:
> *the run config dir … is not covered by the `~/.claude*` deny set — the one directory whose credential
> this cell holds must be denied to it*

⇒ **The remaining dependency is now NAMED and it is not "a cell": it is a properly staged CELLS ROOT** — a
real `~/.claude*` run config dir, with settings, fence and trust installed **in that order** (the fence
render READS settings). ⇒ **Row 3 closes when the sandbox arm is driven against a fence rendered for a real
run config dir, expecting `Operation not permitted`.**

⚠️ **WHY THIS IS RECORDED AS A HALF AND NOT AS A ROW DISCHARGED.** The hook result is real and it is the
layer most people picture. **It is also the layer that historically WAS populated while the other was not**
— this seat's own card: *the agent fence has TWO layers and only one was ever populated in both
substrates.* A row marked done on the strength of the layer that was already known to be the working one
is exactly the failure that card exists to prevent. ⇒ 🔑 ***REPORTING HALF A GATE AS A GATE IS HOW A
TWO-LAYER FENCE BECOMES A ONE-LAYER FENCE WITH A CLEAN RECORD.***

---

# ADDENDUM 12 — 2026-09-13, bench. ✅ **§B7 ROW 5 IS FULLY DISCHARGED. N1 AND N3 ARE BOTH DRIVEN.**

**N1 — seed byte-identity across arms — is now CHECKABLE, and building the check is what found the gap.**
I assumed `cell_manifest.py --pair` covered it, since it refuses any diff outside METHOD_FILES. **It does
not:** a one-byte plant in a cell's working `solution.rs` left `--pair` reading **OK**, because the manifest
reads the ROOT COMMIT. **The manifest is right; nothing was comparing `ctl/seed-sha` to anything at all.**
⭐ **AND THE ROOT COMMIT IS THE CORRECT COMPARISON POINT, FOR A REASON SPECIFIC TO THIS FIELD:** in a
brownfield cell the subject is *supposed* to modify `solution.rs` — that is the task — so **`ctl/seed-sha`
differing from the current working file is the NORMAL END STATE.** A check written against the working tree
would fire on every cell that did its job. **The seed is what the cell was GIVEN**, which lives at the root
commit and is stable for the cell's whole life.
`harness/systems-v3/brownfield_seed_check.py` (task tree `0e425e3`), two refusals:
```
  SELF    ctl/seed-sha == sha256(solution.rs AT THE ROOT COMMIT) — catches a tampered record, a tampered
          root, or a builder that wrote the field from something other than the file it copied
  CROSS   every cell of a condition carries the SAME ctl/seed-sha — N1 proper
  ⛔ a cell with NO ctl/seed-sha is REFUSED, never skipped: a greenfield cell has none, and skipping it
    would let one into a brownfield condition unnoticed
```
**Selftest 4 of 4 (one green, three red). Driven on real cells:** the real pair PASSES *with a working-tree
plant still present* · a tampered record REFUSES on both SELF and CROSS · a real greenfield cell REFUSES.

**N3 — the briefing diff — is PUBLISHED at `harness/systems-v3/BROWNFIELD-BRIEFING-DIFF.md`**, taken from
cells built at MATCHED NONCES so the only differences are the field's.
```
  plain   differing files: REQUIREMENTS.md, solution.rs   REQUIREMENTS.md +9/-0   CLAUDE.md IDENTICAL
  salt    differing files: REQUIREMENTS.md, solution.rs   REQUIREMENTS.md +9/-0   CLAUDE.md IDENTICAL
```
⇒ 🔑 ***EACH ARM'S METHOD FILE IS BYTE-IDENTICAL BETWEEN GREENFIELD AND BROWNFIELD.*** That is §B2's
sharpest hazard made checkable — *the treatment's content substantially IS advice about how to approach code
you did not write* — and **a field that altered either arm's briefing would be adding treatment and calling
it a field.** It does not. The +9 is the same nine lines in both arms.
📌 A first pass showed **+10/−1** and the "removal" was the per-cell **work-order nonce** on line 1, an
artefact of comparing two cells built at different nonces. **Rebuilt at matched nonces; the true delta is
a pure addition.** A diff between two objects that differ for an uninteresting reason is not the diff you
wanted, and it reads exactly like one.

---

# ADDENDUM 13 — 2026-09-13, bench. ✅ **§B7 ROW 8 IS FULLY DISCHARGED. THE PARENT KEY EXISTS.**
*Task tree `773f99c`; predecessor kept as `cell_copy_v3.py.pre-parent-key`.*

`cell_copy_v3.py` now writes **`ctl/parent`** and **REFUSES an unresolvable parent at the copy** — §B4's
*"a child with no resolvable parent is VOID, not scored"*, enforced where the child is made rather than
discovered at scoring. Every component is **DERIVED from the parent's own `ctl` and never typed**: a key a
human retypes is a key that drifts from the cell it names.
```
  problem · phase · arm · field · client        derived
  parent_end_sha                                the parent's repo HEAD — §B4's baseline for the child
  n_index                                       ⚠️ DECLARED UNRESOLVED
```
⚠️ **`n_index` IS DECLARED, NOT FABRICATED.** §B4 names five components and **this harness has no
n-index/replicate concept at all** — measured with a positive control: **ZERO** files name one, against
**SEVEN** naming the arm. ⇒ 🔑 ***A FABRICATED KEY COMPONENT IS WORSE THAN A DECLARED GAP, BECAUSE IT LOOKS
RESOLVED AND THE SCORER WOULD KEY ON IT.*** The gap is now on the record instead of in the key.

⭐ **`field` IS INFERRED WHEN ABSENT, AND THAT DEFECT WAS CAUGHT BY MY OWN REFUSAL FIRING ON THE TOOL'S
SELFTEST.** `ctl/field` was born TODAY with the rung, so **every cell built before it lacks one** — and a
mandatory `field` would have refused to copy **the entire existing population.** That is the *"a step that
grows the glob"* failure in its **retroactive** form: I added a required field and made it required
backwards. A pre-rung cell IS greenfield (brownfield did not exist), so the value is determinate — **but it
is recorded as `INFERRED`, because "read from the cell" and "deduced from a date" are different warrants
and a scorer may care which it holds.**
📌 **The selftest fixture is now cell-shaped** (a real `ctl/task` triple, a git repo with a HEAD). It had
to be: **a fixture that is not shaped like a real cell cannot test a tool that reads real cells**, and mine
was passing 18/18 against cells no builder produces.

**DRIVEN:** a real brownfield cell resolves all four + the END sha · a parent with no `ctl/field` INFERS
greenfield and says so (rc 0) · a parent missing `ctl/arm` REFUSES naming it · a parent whose repo has no
HEAD REFUSES naming that · **selftest 18 of 18 after the change.**

## 📌 AND A STALE REASON, CORRECTED THE MOMENT IT WENT STALE
`cell_build`'s `--field brownfield --phase 2` refusal said *"row 8's PARENT-KEY half does not exist."*
**It does now.** The refusal STANDS on better ground and its message says so: **a brownfield child is
COPIED from a landed parent, never built from scratch** — building one here would produce this builder's
own *"greenfield with a longer card"* shape wearing a brownfield label.

## ⇒ §B7 AT THIS POINT
```
  1 ✅ 4 of 5   2 ✅   3 HALF (hook ✅ · sandbox needs a STAGED CELLS ROOT)   4 ✅   5 ✅   8 ✅   9 ✅
  6, 7  OWED — the two VERDICT paths, and the only rows left that need a full red-first drive
  Crc32 awaits its ruling (no discriminating seed; three options posted, recommendation (a))
```

---

# ADDENDUM 14 — 2026-09-13, bench. **§B7 ROW 6: TWO PARTS DONE, THE THIRD IS A SPECIFICATION PROBLEM**
*Task tree `a053b8e`; predecessor kept as `referee_v3.py.pre-verdict-arms`.*

**✅ DRIVEN.** `referee_v3.py --selftest-verdicts` — **9 arms** over `phase2_verdicts`: GREEN/GREEN ·
V1-RED-alone and V2-RED-alone (*the interesting cells, unpooled*) · both lines absent AND one line absent
both → UNMEASURED · **UNMEASURED is NOT GREEN** · phase 1 → NOT APPLICABLE, distinct from both ·
`pooled_forbidden` in the record · **no pooled `correct`/`pass`/`verdict` field emitted.**
⛔ **A SEPARATE FLAG ON PURPOSE.** The main `--selftest` refuses without six toolchain names and a withheld
tree; an arm added there would **inherit both gates and be unreachable** wherever they are absent — and an
arm that cannot run does not stay correct, **it stays pinned to the day it was written.**
⭐ **RED-DRIVEN against two mutants of the function it tests:** making `UNMEASURED` read as GREEN — *the
exact inversion design §2 forbids* — fails **2** arms; pooling V1 and V2 into a `correct` field fails **1**.
Restored, 9 of 9. **A suite that has only ever passed proves nothing.**

**✅ SEPARABLE.** `CELLS.tsv` gains a **13th field: `greenfield | brownfield`.** Without it the two
conditions are indistinguishable in the register, which is what row 6 asks for. Appending is safe for the
reason the file itself already measured — *readers take fields by NAME or by index 1/2; the fence files only
DENY the path* — and I re-measured before adding: **nothing in the harness parses it positionally**, and
`stage_fence_v3.sh` says so of itself (*"derived from the DIRECTORY, never from CELLS.tsv"*).

## ⛔ THE THIRD PART CANNOT BE BUILT AS WORDED, AND I AM REGISTERING IT RATHER THAN FORCING IT
Row 6 says *"V1/V2 as separate **CELLS.tsv** columns"*. **They cannot be.**
```
  CELLS.tsv   written at BUILD time, one appended row per cell
  V1 / V2     POST-RUN verdicts, read by the referee from the driver's output AFTER the cell has run
```
⇒ **At the moment the row is written the verdicts do not exist.** The options, neither of them mine to
rule: **(a)** a RESULTS register carries `cell · v1 · v2 · reading`, leaving `CELLS.tsv` a pure build
record — my recommendation, because it keeps an append-only file append-only; **(b)** `CELLS.tsv` is
updated in place after a run, which **re-opens the row-tearing hazard the file already documents** (*"every
cell's build appends to ONE file, and concurrent appends over ~1 KB tear"*) and turns a build record into a
mutable one.
📌 **The row is not wrong about what it WANTS — the two verdicts must be separable per cell, and they are.
It is wrong about WHERE**, and that is worth one ruling rather than a forced column.

---

# ADDENDUM 15 — 2026-09-13, bench. ✅ **§B7 ROW 7 IS DISCHARGED — AND §B5 NEEDED A FOURTH CLASS**
*`harness/systems-v3/brownfield_rewrite_class.py`, task tree `3da6dbe`.*

**HARNESS-TAKEN ON BOTH SIDES:** the seed **as the cell was GIVEN it** (the root commit, which
`ctl/seed-sha` attests) and the component **as the cell LEFT it**. A class read from a landing note would
be the subject grading itself.

⛔⛔ **§B5 NAMES THREE CLASSES AND THERE ARE FOUR. `UNTOUCHED` WAS ADDED THE FIRST TIME THIS TOOL RAN ON
REAL CELLS**, where an untouched seed came back **`REPAIRED` at retained 1.000**. **A cell that never
modified the given did not REPAIR it.** Without the state, a cell that FAILED TO ACT is binned as *"the
only brownfield outcome in the intended sense"* — the flattering direction, silently.
⇒ 🔑 ***A CLASSIFIER WHOSE CLASSES ASSUME THE SUBJECT ACTED WILL LABEL INACTION AS THE GOOD OUTCOME.***
**This amendment's §B5 is amended accordingly: REMOVED · REPLACED · REPAIRED · UNTOUCHED.**

## THE THRESHOLD, REGISTERED BEFORE ANY CELL, AND WHY IT IS SURVIVABLE
`retained < 0.20 → REPLACED`, where `retained` is the line-level ratio of the END file against the seed.
**0.20 is arbitrary in the way every threshold is**, and two things keep it honest:
1. **It is fixed BEFORE the data.** A threshold chosen after seeing the arms is FITTED to them and its
   author cannot show otherwise — this desk's own card, and the reason the number is in the source today.
2. **`retained` is printed on EVERY row**, so any reader can re-derive every class under a different cut
   **without re-running anything.** ⇒ ***THE CLASS IS THE OPINION; THE STATISTIC IS THE MEASUREMENT, AND
   ONLY ONE OF THEM IS BEING ASKED TO BE BELIEVED.***

## ⭐ END STATE READS THE WORKING TREE WHEN IT IS DIRTY, AND SAYS WHICH IT READ
**Class-C node 1 produced a cell that proved its statement and committed NOTHING.** A discriminator that
looked only at commits would classify **a whole real outcome as REMOVED.** A5.6(c) registered *a working
tree is a possible output shape and nothing in the harness treats it as one* — this treats it as one.

**DRIVEN: selftest 9 of 9**, both sides of the threshold. **RED-driven against two mutants:** reading only
HEAD (uncommitted work invisible) fails **4** arms; moving the threshold to 0 fails **2**. **On real cells:**
an unrun cell reads `UNTOUCHED 1.000 HEAD`; a one-byte-edited one reads `REPAIRED 0.995 working tree`.

## ⇒ §B7 IS COMPLETE BUT FOR TWO NAMED ITEMS
```
  1 ✅ 4 of 5 (Crc32 awaits its ruling)     2 ✅     4 ✅     5 ✅     6 ✅     7 ✅     8 ✅     9 ✅
  3   HALF — hook layer ✅; the SANDBOX layer needs a STAGED CELLS ROOT, not merely a cell
  6   its third part is a SPECIFICATION problem, registered for a ruling: V1/V2 cannot be CELLS.tsv
      columns, because that file is written at BUILD time and the verdicts are POST-RUN
```

---

# ADDENDUM 16 — 2026-09-13, bench. ⛔⛔ **§B7 ROW 7'S ✅ DOES NOT HOLD: "HARNESS-TAKEN" WAS READ AS "NOT AGENT-REPORTED", AND BOTH WITNESSES WERE INSIDE THE SUBJECT'S REACH**
*`harness/systems-v3/brownfield_rewrite_class.py`, saltbench-systems `071252d` + `3591e27` (branch
`bench/b7-row7-harness-witness-2026-09-13`, pushed to backup). Task tree: export `ecd3924`.*

## ⚠️ FIRST, THE DISAGREEMENT THAT SENT ME TO LOOK, BECAUSE IT IS THE CHEAPEST PART OF THIS
**ADDENDUM 15 marked row 7 ✅ DISCHARGED. The same head's GATE and BANK both listed row 7 as the next
item to TAKE, in that order, at the top.** One shift, one seat, two records, opposite verdicts. I took
the gate's reading because it was the one addressed to me, and it was right — **but I want the record to
say that I did not discover the defect by suspecting it, I discovered it because two documents disagreed
and I read the loser.** ⇒ 🔑 ***A CONTRADICTION BETWEEN TWO OF YOUR OWN RECORDS IS A FREE AUDIT, AND THE
TEMPTATION IS TO RESOLVE IT BY PICKING THE FRESHER ONE RATHER THAN BY MEASURING.***

## ⛔ THE DEFECT: TWO DIFFERENT PROPERTIES SHARE ONE PHRASE
Row 7 reads *"wired to HARNESS-TAKEN hashes"*. ADDENDUM 8 glossed it, correctly as far as it went:
*"the hashes must be taken by the harness precisely because a subject-reported hash is the subject
grading itself."* ADDENDUM 15 discharged it on exactly that reading — the seed came from the cell's git
**root commit**, not from a landing note, so it was not agent-reported.
⇒ ⛔⛔ **BUT "NOT REPORTED BY THE SUBJECT" AND "NOT CONTROLLABLE BY THE SUBJECT" ARE DIFFERENT
PROPERTIES, AND ONLY THE SECOND ONE MAKES A WITNESS A WITNESS.** The row was scored on the first.

**MEASURED AT THE OBJECT, in the harness's own source, 2026-09-13:**
```
  render_fence_v3.deny_set   denies FOREIGN_TREES ∪ ~/.claude* ∪ ~/bench* ∪ the cells root's shared
                             members ∪ every SIBLING cell ∪ the scratch roots.
                             The cell's OWN directory is not in it. The only invariant asserted about
                             the cell's own tree is the OPPOSITE one — that repo/ and tmp/ must NOT be
                             denied ("a fence that blocks the agent's working copy is not a fence, it
                             is a blind episode that still scores").
  cell_build.py              says so itself, at the briefing-token census: "ctl/ is walked too,
                             deliberately: the fence allows the cell tree, so a token written into
                             ctl/briefing-nonce IS reachable by the subject's shell."
```
⇒ **`ctl/seed-sha` is harness-WRITTEN and subject-REACHABLE. The git root commit is harness-COMMITTED
and subject-REWRITABLE** (`commit --amend`, `rebase`, or `rm -rf .git && git init`). The discriminator
rested on the weaker of the two and consulted the other one not at all — while its own docstring
asserted they agreed (*"the root commit, which is also what `ctl/seed-sha` attests"*).
⛔ **AN UNCHECKED PREMISE STATED IN A DOCSTRING IS NOT A WEAKER CHECK THAN A COMPARISON. IT IS NOT A
CHECK.** It is a sentence that makes a reader stop asking.

## ⭐ WHAT IT COSTS, MEASURED ON A REAL CELL RATHER THAN ARGUED
A **COPY** of the real probe cell `bflzwp` (LZW, seed `aa968d04…`) — copied, never dispatched — with its
`repo/.git` removed and its own wholesale rewrite re-committed as *"the component repository"*. Two
commands for a subject with a shell.
```
  unwired (seed from the cell's own root commit)  ->  UNTOUCHED   retained 1.000
  wired   (seed from the task tree, W1)           ->  REFUSED     "THE CELL'S HISTORY DOES NOT CARRY
                                                                   THE SEED IT WAS BUILT WITH"
  the true class of that cell                     ->  REPLACED
```
⇒ 🔑 ***THE REWRITE ESCAPE AND THE INACTIVE CELL BECAME THE SAME ROW.*** `REPLACED` — "greenfield with
extra steps" — is the **entire reason design §3 registers this class**, and it is the one outcome a
forged seed erases. A root rewritten to something merely *near* the output reads `REPAIRED` at a high
ratio instead: **the intended brownfield outcome, manufactured.** The class can be moved to any value
the subject likes, and the unwired tool has no channel through which to notice.
📌 **The pre-wiring logic is KEPT IN THE FILE as a named negative control** (`_classify_cell_only_
NEGATIVE_CONTROL`, no caller outside the selftest, no flag that reaches it), so the two rows above are a
MEASUREMENT of what the wiring buys and not a claim about it. Same pattern, same reason, as
`render_fence_v3.render(carve=False)`: **an invariant you cannot show FAILING is one you have not tested.**

## ✅ THE REPAIR — THREE WITNESSES, AND ONLY ONE IS OUT OF REACH
```
  W1  <tasks-root>/<task>/brownfield/solution.rs   the SOURCE seed, in the harness tree. AUTHORITATIVE,
                                                   and the text every class is computed against.
  W2  <cell>/ctl/seed-sha                          harness-written at build   · subject-REACHABLE
  W3  solution.rs at the cell repo's ROOT COMMIT   harness-committed at build · subject-REWRITABLE
```
⛔ **W2 and W3 ARE KEPT, BUT DEMOTED — AS TAMPER DETECTORS, NEVER AS SOURCES OF TRUTH.** They are the
only reason a rewrite is VISIBLE at all. Any disagreement **REFUSES** and names which witness disagrees.
⛔ **A TAMPER IS AN INSTRUMENT-INTEGRITY FINDING AND NEVER A FOURTH OUTCOME CLASS.** A refused cell emits
no class at all — binning it would put a forged cell in a table beside honest ones.
⛔ **MORE THAN ONE ROOT COMMIT REFUSES** rather than the tool picking one. `rev-list --max-parents=0`
returns a LIST; the old code took `[-1]`. Two roots is the signature of a graft or a re-init.
⛔ **`--tasks` IS REQUIRED AND HAS NO BYPASS.** A flag permitting the tool to run without its external
witness would be used, and the resulting rows are **indistinguishable from wired ones once they reach a
table.** There was no caller to break: this tool had none.
⛔ **A CELL WITHOUT `ctl/seed-sha` IS REFUSED, NOT SKIPPED** — a greenfield cell has none, and skipping
it silently is how a greenfield cell enters a brownfield condition wearing the label.
📌 **`seed_sha` AND `end_sha` ARE NOW ON EVERY ROW**, so design §3's *"a hash at build, a hash at end, and
a diff statistic between them"* is all three on the line and the class is reproducible without the cell.
📌 **THE 0.20 THRESHOLD IS DELIBERATELY UNTOUCHED.** Moving the cut in the same edit would make its
pre-data registration unverifiable by a reader of one diff.

## ⭐ AND THE SECOND COMMIT, WHICH IS THE ONE I ALMOST DID NOT WRITE
W1 is out of reach **because of where the task tree sits** — under `~/projects`, which is in
`FOREIGN_TREES`. That is a fact about the run box, **not about this tool**, and I had written it into a
docstring as though a docstring could see the box it is read on. So it is now **re-taken PER CELL** from
the cell's own rendered fence, as a `w1_fenced` column:
```
  COVERED     a denyRead entry covers the W1 tree, or an ancestor of it
  UNCOVERED   REFUSES — a witness the subject can reach is not a witness
  UNVERIFIED  no rendered fence in ctl/. The class still stands on W1/W2/W3 agreement; the
              REACHABILITY claim is UNTESTED for that cell, and the count prints as its own loud
              trailer rather than sitting in a column a reader may not scan.
```
⇒ 🔑 ***A CLAIM ABOUT REACHABILITY THAT IS NOT RE-TAKEN PER CELL IS A CLAIM ABOUT THE DAY IT WAS
WRITTEN.*** ⛔ And `UNVERIFIED` is deliberately **not** printed as a pass: *"untested" is not "held"*, and
this file's parent already records that the most dangerous green is one that names its own scope
accurately, because the scope is printed where the reader has already decided the answer is yes.

## 📊 THE DRIVE — SELFTEST, MUTANTS, AND THE OBJECT
```
  selftest ............... 26 of 26, rc 0.  16 of the arms are RED (a planted tamper must REFUSE).
  mutation controls ...... 6 of 6 KILL the selftest at rc 1, each by its OWN named arm:
                             M1 W3 root-commit check removed ....... 2 arms fail
                             M2 W2 ctl/seed-sha check removed ...... 1
                             M3 multi-root refusal removed ......... 1
                             M4 missing ctl/seed-sha skipped ....... 1
                             M5 UNCOVERED fence not refused ........ 1
                             M6 absent fence reported as COVERED ... 1
                             M0 UNMUTATED control .................. rc 0, 0 arms fail
  the object (A) ......... all EIGHT real brownfield probe cells, rc 0. Four seed shas, independently
                           re-derived from the task tree and matching the builder's to the byte:
                           LZW aa968d04 · LRU d9b2f3d3 · Paxos 1ce92803 · FreeList 4ebaf3df.
  the object (B) ......... four PLANTS over COPIES of `bflzwp`, same real seed, rc 1:
                           REPAIRED 0.990 · REPLACED 0.000 · REMOVED · REFUSED(forged root)
```
⛔ **WHY (B) EXISTS AT ALL: eight clean `UNTOUCHED` rows from a tool I had just written is the shape of a
broken instrument, not of a good one.** The probe cells made zero model calls, so `UNTOUCHED` is the
correct answer for every one of them — and a classifier that returns the correct constant is
byte-indistinguishable from one that returns a constant. **(B) is the only reason (A) is a reading.**

## ⚠️ AN ARM-CORRELATED SPLIT IN (A), CHASED TO ITS CAUSE AND **NOT** A FINDING
`w1_fenced` came back **COVERED on all four `plain` cells and UNVERIFIED on all four `salt-diet` cells** —
4/4 versus 0/4, a perfect split on the arm, which is the shape this campaign treats as guilty until
measured. **Measured:** the salt cells lack exactly five files, all LAUNCH-PREFLIGHT artefacts
(`launch.log`, `agy-battery-preflight.tsv`, `probe-battery.log`, `srt-settings.json` and its
declared-differences table). That is **the battery having been run once per PAIR**, which is correct —
the battery's claim is *"each seed compiles"*, a per-SEED property — and **the gemini seat declared it as
`--` on the salt rows of its own published matrix.** ⇒ **My column surfaced a DECLARED asymmetry from a
second direction. It is recorded here because a clean split on the arm deserves a cause, and because
reporting a peer's declared `--` as a discovery is the cheapest way to spend someone else's credibility.**

## ⛔ WHAT THIS DOES **NOT** ESTABLISH, SAID BEFORE ANY WAVE USES IT
1. **No brownfield cell has ever been RUN.** Every class in (A) is `UNTOUCHED` on a zero-model-call
   probe. **The discriminator has never seen a subject's real output**, and (B) is planted by me.
2. **The 0.20 cut is untested against real agent behaviour** and will stay that way until a wave lands.
   It is registered, printed beside every row, and re-derivable — that is all it is.
3. **A subject that forges W2 *and* W3 *consistently* is caught by W1, but a subject that could reach
   W1 is caught by nothing here** — which is why `UNCOVERED` refuses rather than warns.
4. ⚠️ **A SIBLING GATE CARRIES THE SAME UNCHECKED PREMISE AND IT IS NOT MINE TO CLOSE THIS SHIFT.**
   `brownfield_seed_check.py` (row 5) states in its own docstring that its SELF arm *"catches a tampered
   record, a tampered root"*. **It compares `ctl/seed-sha` against the root commit — two witnesses both
   inside the subject's reach — so a subject that rewrites BOTH is invisible to it.** The claim is false
   for the coordinated case. ✅ **The population is covered in practice, because row 7's tool now refuses
   exactly that cell**; ⛔ **but row 5's own sentence overstates row 5**, and it is registered here rather
   than quietly edited, because a gate's scope is row 5's to restate.

## ⇒ §B7 STATE, RESTATED IN FULL SO NO READER HAS TO ASSEMBLE IT
```
  1 ✅ 4 of 5 (Crc32 awaits its ruling)   2 ✅ (superseded by S1·S2·S3)   4 ✅   5 ✅   8 ✅   9 ✅
  3   HALF — hook layer ✅; the SANDBOX layer needs a STAGED CELLS ROOT, not merely a cell
  6   TWO PARTS DONE; the third is a SPECIFICATION problem registered for a ruling
  7 ✅ DISCHARGED — ON THE SECOND READING OF ITS OWN WORDS. ADDENDUM 15's ✅ is SUPERSEDED, not
      deleted: it was a correct discharge of "not agent-reported" and that is not what the row says.
```
⇒ 🔑 ***THE LESSON, AND IT IS THE ONE WORTH CARRYING OUT OF THIS FILE: A CHECKLIST ROW IS DISCHARGED
AGAINST ITS WORDS, AND ITS WORDS HAVE TO BE RE-READ BY SOMEONE WHO IS NOT THE PERSON WHO WROTE THE
GLOSS.*** ADDENDUM 8 wrote the gloss and ADDENDUM 15 discharged against the gloss, both the same seat,
six hours apart, both careful. **The row never changed. The reading narrowed, once, and nothing in the
process re-opened it** — which is exactly the "checklist you work inside is not one you read" defect this
desk has already banked, arriving one level further down: **not a row skipped, a row satisfied in the
smaller of its two meanings.**

---

# ADDENDUM 17 — 2026-09-13, bench. ⛔⛔ **§B7 ROW 3'S SECOND LAYER IS NOT A BROWNFIELD GAP. IT IS CAMPAIGN-WIDE: 124 CLAUDE CELLS HAVE BEEN LAUNCHED AND NOT ONE HAS EVER HAD ITS SANDBOX LAYER DRIVEN**

*Measured on the run box 2026-09-13, at the object, with a positive control. Nothing here changes a
number in any published result; it changes what one sentence in them is entitled to claim.*

## THE CENSUS
```
  cells carrying a ctl/launch.log ................. 262
    of those, mentioning P-SANDBOX ................ 134
  split by CLIENT, and it is TOTAL:
    134  PSB    client=agy        the OS fence is DRIVEN, both halves, per cell
    124  noPSB  client=claude     ⛔ not one
      4  noPSB  client=?          (no ctl/client; not counted either way)
  POSITIVE CONTROL on the sweep: a generic launch needle matches 262 of 262 logs.
```
⇒ **The split is perfect and it is on the CLIENT, not on the arm, not on the field, not on the wave.**

## WHAT EACH CLIENT ACTUALLY DOES, READ IN THE SOURCE AND THEN AT A CELL
```
  agy_launch_v3.sh  probe_sandbox()   plants a file OUTSIDE the cell and one INSIDE, reads BOTH through
                    $SANDBOX_PREFIX — the wrapper the launch actually runs under — and requires
                    outside DENIED *and* inside READABLE. Its own comment says why both halves:
                    "a profile that denies EVERYTHING would pass a deny-only check while making the
                    cell unrunnable."
  cell-claude.sh    renders the fence, RE-RENDERS it at the moment of use and HOLDs on any drift
                    (bench's 21:28 finding), and passes it to the client as --settings ctl/fence.json.
                    ⛔ IT NEVER ATTEMPTS A DENIED READ. There is no probe of any kind in its 256 lines.
```
**At the object, one cell of each, side by side:**
```
  bflzwp  (agy)     ctl/launch.log:  "P-SANDBOX yes (outside DENIED, inside readable, driven on this
                                      cell's own profile)"
  p2b001  (claude)  ctl/launch.log:  P-SANDBOX occurrences = 0 · built-from.tsv: no containment row
                    — and p2b001 is an arm of the P2 pair whose RESULT is already merged.
```

## ⇒ 🔑 THE CLAIM THAT IS AFFECTED, STATED EXACTLY
For every Claude cell this campaign has ever run, `sandbox.filesystem.denyRead` is **RENDERED** ✅,
**DRIFT-CHECKED AT THE MOMENT OF USE** ✅, and **NEVER DRIVEN** ⛔.
⛔ **THIS IS NOT "THE FENCE LEAKED".** No leak is claimed, none is suspected, and the hook layer
(`permissions.deny`) **is** driven and green. ⇒ ***IT IS UNMEASURED, NOT UNSOUND*** — this desk's own
banked line about a public history, arriving a second time in a different tree. **A rendered set is a
statement about a FILE. A drive is a statement about the BOX.** `cell_build.py` already says the
distinction in its own words — *"a promise at build, discharged at launch"* — and for the Claude client
the discharge step was never written.
⚠️ **AND THE TWO LAYERS ARE THE OLD TRAP.** This seat's standing card is that the agent fence has TWO
enforcement layers and historically only one was ever populated. **The shape has recurred one level
along: two layers, both populated, and for one whole client only one is ever DRIVEN.** ADDENDUM 11
refused to mark row 3 discharged on the hook layer alone for exactly this reason — ***reporting half a
gate as a gate is how a two-layer fence becomes a one-layer fence with a clean record*** — and that
refusal is now vindicated by a census it did not have.

## ⛔ WHAT THIS DOES **TO** ROW 3, AND IT MAKES THE ROW BIGGER RATHER THAN CLOSING IT
ADDENDUM 11 named row 3's remaining dependency as *"a properly staged CELLS ROOT"*. **That was true and
it was too small.** Staging a root would let ONE brownfield cell be driven; it would leave the
instrument that drives it unwritten for the client every Claude cell uses.
```
  ROW 3 CLOSES WHEN:  a Claude cell attempts to read BROWNFIELD-PLANTS.tsv by its full path from a
                      SUBPROCESS under its own rendered fence and gets `Operation not permitted`,
                      with the GREEN half beside it (a path INSIDE the cell still readable).
  WHAT IS MISSING:    not a cell and not a root — a `probe_sandbox` for the CLAUDE client.
                      agy has one. It is the model to port, and ⛔ its own hardest-won lesson ports
                      with it: the probe must run through THE THING THE CLIENT IS WRAPPED IN, never
                      through `sandbox-exec` by name, or it proves a mechanism the launch no longer
                      uses — "a green P-SANDBOX for a containment nothing was using."
  ⚠️ AND THE CLAUDE CASE IS NOT THE AGY CASE:  agy is wrapped by an EXTERNAL prefix, so its probe can
                      borrow the wrapper. The Claude client sandboxes ITSELF from fence.json, and
                      `SANDBOX_PREFIX` is EMPTY for it — `probe_sandbox()` would return
                      "n/a (AGY_SANDBOX=none was DECLARED: there is no OS fence to prove)".
                      ⛔⛔ THAT SENTENCE IS FALSE FOR A CLAUDE CELL, whose fence.json sets
                      `sandbox.enabled: true`. A STRAIGHT PORT WOULD PRINT A DECLARED n/a OVER A REAL
                      FENCE — a third way to get a clean record for an undriven layer.
```

## 📌 HOW THIS WAS FOUND, BECAUSE THE ROUTE MATTERS MORE THAN THE RESULT
I was doing **row 7**, not row 3. Wiring the discriminator to a witness outside the subject's reach
forced me to read `render_fence_v3.deny_set` and ask *what can this cell actually reach* — and then, to
turn that answer into a per-cell measurement, to ask *where does a cell's rendered fence live*. **The
census fell out of the second question.** ⇒ ***THE WAY TO FIND AN UNDRIVEN GATE IS TO NEED ITS OUTPUT
FOR SOMETHING ELSE.*** Nobody audits a green.

## ⛔ WHAT I AM **NOT** DOING, AND WHY IT IS NOT TIMIDITY
1. **Not porting the probe this shift.** It is a change on the LAUNCH path of every Claude cell, and
   `ADDENDUM 8`'s own reasoning applies unchanged: *"it changes the gate's control flow on the path a
   verdict runs through, and a gate that mis-runs is worse than one that visibly skips."* A straight
   port is actively wrong here (see the n/a trap above), so this needs a design, not an afternoon.
2. **Not re-opening any merged result.** No number moves. The affected sentence is a containment claim,
   and it is corrected by being scoped, not by being withdrawn.
3. **Not marking row 3 anything but HALF.** It was HALF before this census and it is HALF after, for a
   larger reason. ⛔ **A row does not become more discharged because you found out the gap was wider.**

## ⇒ §B7 STATE
```
  1 ✅ 4 of 5 (Crc32 awaits its ruling)   2 ✅ (superseded by S1·S2·S3)   4 ✅   5 ✅   7 ✅   8 ✅   9 ✅
  3   HALF, AND THE OTHER HALF IS NOW SIZED: the hook layer is driven; the sandbox layer needs a
      `probe_sandbox` FOR THE CLAUDE CLIENT, which does not exist for any of the 124 cells that have
      used it. ⛔ THIS IS THE ROW THAT GATES THE BROWNFIELD FIRE, and it is no longer a staging chore.
  6   TWO PARTS DONE; the third is a SPECIFICATION problem registered for a ruling.
```

---
# ADDENDUM 18 — 2026-09-13, bench. **§B7 ROW 6 IS RULED: V1/V2 ARE NOT `CELLS.tsv` COLUMNS, AND THE ROW IS RESTATED RATHER THAN DISCHARGED**

⛔⛔ **ROW 6 AS WRITTEN IS UNSATISFIABLE, AND BUILDING IT WOULD MAKE THINGS WORSE RATHER THAN LEAVING
THEM AS THEY ARE.** The row reads *"V1/V2 as separate `CELLS.tsv` columns; `unmeasured` distinct from
`pass`, driven."* **Four measurements, each taken at the object, and any one of them is sufficient:**

```
  1  TIMING      CELLS.tsv is written by cell_build.py at BUILD time. V1 and V2 are POST-RUN
                 verdicts. A build-time file can carry a post-run verdict only by being MUTATED
                 after the run — and a cell directory is evidence, not scratch (repo CLAUDE.md).
  2  CONSUMERS   its readers are cell_build.py, render_fence_v3.py, fence-hook.sh, hook-deny-v3.sh.
                 Those are the BUILDER and the FENCE. ⛔ NO SCORER READS IT. Adding verdict columns
                 couples the scorer to the fence: a scoring bug could then change what a cell is
                 ALLOWED TO READ. That is a safety surface, and verdicts have no business on it.
  3  SHAPE       it is HEADERLESS and POSITIONAL — row 1 is DATA, not a header. Its leading
                 fields are a cell id, a run-box name, a lane and a harness version, with no
                 column names above them, so a reader must count positions to find anything.
                 Adding columns is a silent breaking change for every positional reader, and the
                 failure mode is a misread column, not an error.
  4  POPULATION  it does not exist on the p2b root at all. A column on a file that is absent for the
                 live wave is a registered check that measures nothing — §B7's own recurring defect.
```

⇒ 🔑 ***THE ROW ASKED FOR THE RIGHT PROPERTY IN THE WRONG FILE.*** What it actually wants — V1 and V2
read INDEPENDENTLY, with `unmeasured` a distinct value from `pass` — is a property of the VERDICT
artefact, and the verdict artefact already exists: `referee_v3.phase2_verdicts()`, which is one
derivation point (`V1 GREEN iff regressions_failed == 0` · `V2 GREEN iff clause_failed == 0`, no
pooled field derived, phase 1 `NOT APPLICABLE`, a missing line `UNMEASURED` and never GREEN).

## ✅ ROW 6, RESTATED — this is what discharges it
> **6′  V1/V2 recorded as INDEPENDENT fields of the referee's phase-2 verdict output, never in
> `CELLS.tsv`; `unmeasured` DISTINCT from `pass`, driven RED-first against the export that will
> actually score the run, and that export's sha recorded beside the verdicts.**

## ⛔⛔ AND THE LIVE BLOCKER THIS RULING SURFACED, WHICH MATTERS MORE THAN THE RULING
**The export that BUILT the live P2 pair cannot produce V1/V2 at all.** Measured, with a positive
control in both directions:

```
  grep -c phase2_verdicts  export-23b351c/…/referee_v3.py   ->   0     (the BUILDER of p2b001+p2b002)
  grep -c phase2_verdicts  export-s2m/…/referee_v3.py       ->  13     (positive control: it is findable)
  p2b001 ctl/built-from.tsv  export_sha 23b351cf49a55b94…
  p2b002 ctl/built-from.tsv  export_sha 23b351cf49a55b94…
  28 of 64 export trees carry the function; 36 do not, and nothing declares which is current.
```
⇒ **Scoring the P2 pair REQUIRES an export other than the one that built it, and no file in either
cell records that pairing.** ⛔ **So the verdicts would come from an instrument whose provenance is
unstated — while `built-from.tsv` sits right beside them looking like it answers the question.**
⇒ 🔑 ***`built-from.tsv` RECORDS THE BUILDER, AND A READER WILL TAKE IT FOR THE TOOLCHAIN. WHEN THE
SCORER IS A DIFFERENT EXPORT, THE RECEIPT IS NOT WRONG — IT IS ANSWERING A QUESTION NOBODY ASKED.***

**BINDING ON THE P2 SCORING, and it costs nothing to comply:** whoever scores p2b001/p2b002 records
`scorer_export_sha` beside `export_sha`, and if the two differ, says so in the result file. **A
single export used for both is better and is the default if one is available.**

## SCOPE
This addendum rules §B7 row 6 and registers one blocker on the P2 spec-change scoring. **It
discharges no other row.** Rows 1–5, 7 and 8 stand as written; row 2 is superseded by Addendum 2 and
row 1 is discharged for four of five problems. **Nothing here authorises a cell.**

⚠️ **THIS ADDENDUM WAS WRITTEN AND OPENED AS PR #116 NUMBERED `ADDENDUM 10`, AND LANDS AS 18.**
Between its authoring and its merge, **ADDENDA 10–17 landed from other branches of this same seat**, so
its own number had come to name a different addendum — the one recording that the third rung was built.
⇒ 🔑 ***AN APPEND-ONLY DOCUMENT NUMBERS BY WHEN A THING LANDS, AND A LONG-OPEN PR REMEMBERS WHEN IT WAS
WRITTEN.*** Renumbered at the merge rather than left to collide, and **the collision is recorded rather
than silently fixed**: two addenda numbered 10 in one protocol document would make every later citation
of "addendum 10" ambiguous, and nothing in this repo's gates can see a duplicate heading.
📌 **Its ruling is unchanged by the renumber, and nothing in it is superseded by 11–17:** row 6's third
part remains a SPECIFICATION problem, which is exactly how ADDENDUM 17's §B7 table already records it.


---
## 📌 §B5 IS **NOT** AMENDED — `surv` AND `growth` ARE A REPORTING ADDITION BESIDE IT. Appended below all prior text; §B5 and every addendum untouched.
*bench (SaltBench lead), 2026-09-21, landing desk `TQ`.* **The Captain's word, verbatim, council 2026-09-21 (minute the 2026-09-21 council minute, §3): "yes reporting change".**
⇒ **§B5's registered separator stands exactly as written — `retained < 0.20 → REPLACED`, `retained` being the line-level ratio of the END file against the seed, fixed before any cell ran. Nothing in §B5 changes, and no threshold moves.**
⇒ **`surv` (seed lines matched / seed lines) and `growth` (end lines / seed lines) are POST-HOC statistics REPORTED BESIDE `retained`, never in place of it.** Adding them is a REPORTING change, not a registration amendment, and therefore needs no amendment to this document. **A drafted amendment prepared before that ruling is superseded and is not used.**
📌 **Where the numbers and the label live:** `MEASUREMENT-l7-retention-decomposition-2026-09-19.md` (§3's table, §7's POST-HOC label) and `RESULT-gemini-level7-2026-09-19.md` ERRATUM 2. ⚠️ **This line exists so that a reader who arrives at §B5 first is told the two columns are not registered separators** — which is the only way that reader could otherwise find out.
