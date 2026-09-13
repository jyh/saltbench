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
Written in the shape A5.6(b) used for gate FIX 3: **fully specified, deliberately not built at the tail of
a shift**, because it is the blocker for the whole field and deserves a full red-first drive.

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
