# AMENDMENT — THE SPEC-CHANGE TASK SHAPE
## Dated 2026-09-09 PDT (2026-09-10 UTC). ⛔ **THE COMMIT THAT FREEZES THIS FILE IS THE AUTHORISATION, AND IT LANDS BEFORE ANY SPEC-CHANGE CELL IS BUILT.**

Ordered by the Captain at 21:5x PDT: *"for bench, we need to get the spec change authored, then run
that next; then resume expansion to all 14 problems."* Routed by the 42nd helm head, whose sequence is
ordered and is not collapsed here: **① author · ② run that · ③ then the expansion.** This file is ①.

It discharges **`PREREGISTRATION-matrix-opus-2-specchange-2026-09-08.md` §4**, which recorded the task
shape as **OWED BEFORE CELL 1** and refused to mint it:

> The Captain's word is *"spec change, not an RTL one"*. **That is a direction, not a specification**,
> and this desk will not mint the definition that decides what the arm measures. **OWED:** the exact
> spec-change instruction — what the subject is given (a working implementation? its tests? the old
> spec?), what changes, and what "done" means for the referee.

`systems` was right to refuse; the Captain has now said who authors it. **Nothing in matrix #2's
reading (§5–§8 of that file) is touched by this amendment.** Its `greenfield-derived` label on any `n`,
its spread clause, its agreement clause and its `UNRESOLVED` verdict word all stand as written.

---

## §1 · ⛔⛔ THE ANSWER TO §4, AND IT WAS ALREADY BUILT — I MEASURED IT RATHER THAN DESIGNING IT

**THE SUBJECT IS GIVEN ITS OWN PHASE-1 REPOSITORY, MID-FLIGHT, WITH A CUSTOMER COMMIT ON IT.**

Measured at the object on `saltbench-systems` branch `systems-v3-repair1` @ `311b208`:

```
  tasks/systems-v3/EXECUTOR-BRIEF-v3.md §1.3, verbatim:
      "B/ — phase 2 (the change request). No given/: the seat's own phase-1 landing is the given."

  harness/systems-v3/customer.sh dispatch <cell> <task-dir>
      REFUSES unless ctl/end-1 exists (phase 1 has ENDED) and the tree is clean
      checks out main, then ONE commit authored `customer <customer@bench>`, hooks off:
        inbox/change-1.md   = a FIXED paragraph + the card's `## Change request (phase 2)` section
                              as `render_requirements.py --clause` prints it
        REQUIREMENTS.md     = re-rendered with `## Change 1`, SAME nonce, the same lines the clause
                              carries, so the seat's two copies cannot disagree
        interface.rs        = replaced by B/interface.rs, the EXTENDED interface
        BUS.md              = a CUSTOMER line
        git tag P1
      prints a payload sha over (inbox/change-1.md + interface.rs) — IDENTICAL ACROSS THE ARM PAIR

  harness/systems-v3/render/BOOT_PROMPT_2.txt
      a NEW SESSION on the same repository: read inbox/ first, then BANK.md, memory/MEMORY.md, the
      tail of BUS.md; "Reconcile BANK.md against the tree before you trust it."
```

⇒ **"DONE" FOR THE REFEREE IS ALREADY DEFINED AND ALREADY EMITTED**, and it is two numbers, not one.
`B/withheld/tests/driver_main.rs` runs the base suite and the clause suite and reports them separately:

```
  TESTS        <passed>/<total>      the pooled figure
  REGRESSIONS  <FAILED>/<total>      the base suite = phase 1's driver VERBATIM
  CLAUSE_TESTS <FAILED>/<total>      the clause's own tests
```

⇒ 🔑 ***THE TASK SHAPE WAS NOT MISSING. IT WAS UNREGISTERED*** — built, tested, and reachable, while
the one file that says what the arm measures said `OWED` and `nothing is built`. **That is the whole
of ①: not an invention, a registration**, and the three sections below are the three places where
registering it changes what may be reported.

## §2 · ⛔⛔ POLARITY: TWO OF THE THREE FIELDS COUNT FAILURES, AND THE THIRD COUNTS PASSES

```
  TESTS 41/44          41 PASSED of 44      <- a HIGH number is GOOD
  REGRESSIONS 3/9      3 FAILED of 9        <- a HIGH number is BAD
  CLAUSE_TESTS 0/12    0 FAILED of 12       <- a HIGH number is BAD
```
Read at the source: `driver_main.rs` prints `passed` for `TESTS` and `regr_failed` / `clause_failed`
for the other two. ⇒ **A scorer that copies the `TESTS` idiom onto either of the other two lines
reports a perfect cell as a total failure and a total failure as perfect, with no parse error.**
⛔ **REGISTERED: every consumer of these two fields names the polarity in the same expression that
reads it**, and no result table prints `REGRESSIONS 0/9` without the word `failed` beside it.
📌 This campaign has carded this exact shape once already — one log reporting percent USED and another
percent REMAINING. **Polarity is a property of the instrument, never of the quantity.**

## §3 · ⛔⛔ THE FIELDS ARE PARSED AND NO VERDICT IS COMPUTED FROM THEM

Measured over every ref on `saltbench-systems`, with a positive control on the same grep:

```
  referee_v3.py:266–280      parses REGRESSIONS/CLAUSE_TESTS into
                             regressions_failed · regressions_total · clause_failed · clause_total
  render_result_v3.py:115    prints them as a PARENTHETICAL on the tests string
  anything else              NOTHING.  No branch, no class, no verdict reads either field.
```
⇒ **`DESIGN-v3-brownfield-form-2026-09-09.md` §7 item 1 — *"V1 and V2 as separate verdicts, with the
path each is read from, and unmeasured ≠ pass"* — IS NOT BUILT.** The numbers reach a decoration.
⇒ 🔑 ***A FIELD THAT IS PARSED AND NEVER BRANCHED ON IS NOT A VERDICT; IT IS A COMMENT WITH A REGEX
IN FRONT OF IT*** — and it reads as present to every reader who greps the field name.

**REGISTERED, and this is a build owed before cell 1:**
```
  V1  REGRESSIONS   the pre-existing behaviour SURVIVED the change   GREEN iff regressions_failed == 0
  V2  CLAUSE        the requested change was implemented             GREEN iff clause_failed == 0
  ⛔ a missing REGRESSIONS or CLAUSE_TESTS line is UNMEASURED, never GREEN, and never absorbed
     into TESTS.  A cell whose driver did not build is UNMEASURED on both.
  ⛔ V1 and V2 are separate columns.  No pooled "tests green" field is reported for a phase-2 cell.
```

## §4 · ⚖️ THE FORM IS **CONTINUATION**, AND ITS CONFOUND IS NOW A MEASURED COVARIATE INSTEAD OF A CAVEAT

`DESIGN-v3-brownfield-form-2026-09-09.md` §0 names two forms and rules that the one closing `N = 0`
is **B-PLANTED** (given = an AUTHORED defective component, identical across cells). **Measured: no
v3 task has a `given/` and `cell_build.py` has no code path that seeds one.** All five pricing tasks'
`B/` trees are `_common.sh · interface.rs · list_traces.sh · run_*.sh · withheld/` and nothing else.

⇒ **THE SPEC-CHANGE ARM AUTHORISED HERE IS `B-CONTINUATION`, AND IT IS CALLED THAT.** Per the design's
own ruling it **does not close `N = 0`** and **may not be called "the brownfield rung"**. B-PLANTED
remains registered as OWED for the form that closes `N = 0`; **this amendment does not build it and
does not retire it.**

⛔⛔ **THE CONFOUND, STATED IN THE DESIGN'S OWN WORDS BECAUSE IT BINDS EVERY NUMBER BELOW:**
> *A PHASE-2 DIFFERENCE CANNOT BE ATTRIBUTED TO THE PHASE-2 TREATMENT WHEN PHASE 1 CHOSE THE STARTING
> POINT.* The given is produced **by the arm under test**; an arm that lands phase 1 better is handed
> an easier phase 2.

✅ **WHAT THIS AMENDMENT ADDS, AND IT IS THE ONE THING THAT MAKES THE FORM REPORTABLE: THE STARTING
POINT IS MEASURED, PER CELL, BEFORE PHASE 2 RUNS.**
```
  THE P1 BASELINE.  Immediately after customer.sh dispatches and BEFORE the phase-2 session launches,
  run B/run_tests.sh against the tree at tag P1 and record, in ctl/ and in the manifest:
       p1_regressions_failed / p1_regressions_total     (expected 0/t for a good phase-1 landing)
       p1_clause_failed      / p1_clause_total          (expected ~t/t: the clause is not yet done)
       p1_solution_sha256                               the given, as it actually is in THIS cell
  ⛔ It costs ZERO MODEL TOKENS: it is a cargo build and a driver run on a tree that already exists.
```
⇒ **Every V1 and V2 verdict is reported WITH its cell's P1 baseline in the same row.** A `V1 RED` on a
cell whose baseline was already RED is a different event from a `V1 RED` on a cell that entered phase 2
clean, and **the pooled number cannot tell them apart.**
⛔ **A cell whose P1 baseline has `p1_regressions_failed > 0` is reported in its own class and is not
pooled into V1**: its phase-1 landing was already failing its own regressions, so phase 2 was handed a
different task. **It is not excluded — excluding it would delete the finding.**

## §5 · ⛔⛔ THE BUILD PATH THAT PRODUCES A SPEC-CHANGE CELL THAT IS NOT ONE — REFUSED HERE

`cell_build.py --phase 2` on a FRESH cell is reachable today and is validated by nothing:
`--phase` is `type=int, default=1` with no precondition. What it builds, measured at the source:

```
  solution.rs   <- B/interface.rs   ⛔ A STUB.  All four bodies are `let _ = x; Vec::new()`
  REQUIREMENTS  <- rendered --change: phase-1 requirements PLUS `## Change 1`
  inbox/        <- .keep ONLY.  No change-1.md.
  git tag P1    <- ABSENT.  ctl/customer.log ABSENT.  No prior session, no landing, no bank.
  ctl/task      <- records phase = 2
```
⇒ **That cell is GREENFIELD WITH A LONGER CARD.** It measures nothing brownfield, it has no given, its
V1 baseline is the empty stub, and **`ctl/task` labels it `phase 2`, so any scorer keying on the phase
pools it with real spec-change cells.**
📌 **And it hands the agent a dangling pointer:** `B/interface.rs`'s own header says *"The change
request in `inbox/change-1.md`"* — a file that path never writes.

⛔ **REGISTERED: A SPEC-CHANGE CELL IS ONE THAT CARRIES `ctl/customer.log` WITH A `dispatched P1` LINE.**
No other cell may be reported, priced or scored as spec-change, whatever `ctl/task` says. The
build-time gate owed before cell 1: **`cell_build.py --phase 2` REFUSES unless the cell already holds
`ctl/end-1`**, the same precondition `customer.sh` already enforces — driven RED by building a fresh
`--phase 2` cell and seeing it refuse, and GREEN on a cell that has ended phase 1.
⇒ 🔑 ***THE PRECONDITION EXISTS AND IS ENFORCED BY THE SECOND TOOL IN THE SEQUENCE, NOT THE FIRST***,
so the shape that skips the second tool entirely is the one shape nothing checks.

## §6 · THE REWRITE CLASS, MEASURABLE HERE WITHOUT A NEW INSTRUMENT

`DESIGN §3` requires REPAIRED / REPLACED / REMOVED registered before cell 1 with a prediction per arm.
Under CONTINUATION the given is the cell's own `solution.rs` at tag `P1`, so the class is a diff the
harness takes, never the agent:
```
  REPAIRED   solution.rs at end-2 shares lineage with P1 and was EDITED
  REPLACED   solution.rs at end-2 is a wholesale rewrite of P1
  REMOVED    the component moved out of solution.rs
  measured   p1_solution_sha256 vs end-2 sha, plus `git diff --stat P1..HEAD -- solution.rs`
```
⛔ **REGISTERED PREDICTION, BEFORE THE CELLS FIRE, so it cannot be fitted afterwards:** the salt-diet
arms are predicted to REPAIR more often than the plain arms, because the method's briefing prescribes
reading and re-verifying existing work while the plain briefing does not. **This is a prediction about
a CLASS FREQUENCY at n = 1 per condition and is therefore UNPOWERED — it is registered so that the
observed classes are read against a stated expectation, not so that it can be tested.**
📌 A REPLACED cell is priced, scored on V1/V2, and reported in its own class. Not void, not excluded.

## §7 · ⛔ THE OUTCOME SPACE, PARTITIONED — EXHAUSTIVE AND MUTUALLY EXCLUSIVE

`systems` paid for this clause tonight: its registered bands read *above 1.8105 upheld · at or below
1.5214 REFUTED · below 1 strongly refuted*, the outcome was **1.5246**, and it satisfied **none of the
three** — missing the REFUTED boundary by **0.0032**. ⇒ 🔑 ***A PRE-REGISTRATION WITH A GAP BETWEEN ITS
THRESHOLDS IS NOT PRE-REGISTERED FOR THE OUTCOME THAT LANDS IN THE GAP.***

**THE SPEC-CHANGE PILOT'S OUTCOME SPACE, COVERING EVERY REAL LINE WITH NO GAP AND NO OVERLAP:**

```
  FEASIBILITY (matrix #2 §7's first product) — one of exactly these, per cell:
    LANDED-SCORED     the phase-2 session ended, the driver built, both fields present
    LANDED-UNSCORED   the session ended, the driver did NOT build      -> V1/V2 UNMEASURED
    CAP-COST          stopped at C2_USD = 18.60                        -> not a failure, its own class
    CAP-TOKENS        stopped at the token cap                         -> its own class
    HARNESS           refused by the referee before scoring            -> not a cell outcome
    NO-LAND           the session ended without a landing              -> V1/V2 UNMEASURED
  ⇒ the six are exhaustive and disjoint; every fired cell lands in exactly one.

  CORRECTNESS, only on LANDED-SCORED cells, and V1 and V2 are read INDEPENDENTLY:
    V1 GREEN iff regressions_failed == 0    V1 RED otherwise
    V2 GREEN iff clause_failed == 0         V2 RED otherwise
  ⇒ the 2x2 is reported as a 2x2.  ⛔ NO SINGLE "correct" FIELD IS DERIVED FROM IT.
     The interesting cell is V1 GREEN / V2 RED against V1 RED / V2 GREEN, and one number hides it.

  TASK-SHAPE RISK (matrix #2 §7's second product), registered as an ORDER OF MAGNITUDE before firing:
    COLLAPSED   the phase-2 diff is under  50 added lines in solution.rs
    NORMAL      50 to 500 added lines
    EXPLODED    over 500 added lines, or solution.rs at end-2 is REPLACED
  ⇒ boundaries at 50 and 500 are one order of magnitude apart, coarser than any cell-to-cell noise
    this campaign has measured.  A diff of exactly 50 or exactly 500 is the LOWER class (`<` above).
```

⛔⛔ **AND THE WORD FOR THE WHOLE PILOT IS FIXED BEFORE IT FIRES, AS MATRIX #2 §1 REGISTERED:
`UNRESOLVED`.** At **k = 1** no sign test outcome reaches significance — not "probably won't", cannot
— and at **n = 1** there is no magnitude reading and no spread reading at all. **No headline of the
form "spec change costs more/less" is available whatever comes back.** ⛔ **No ordering carries a
p-value.** This campaign has struck two p-values on that axis already.

## §8 · WHAT FIRES AT ②, AND WHAT IT COSTS

```
  DESIGN     1 problem x 4 arms x n = 1 = 4 CELLS.  Matrix #2 §7, ratified by me on the bus
             2026-09-08 09:33:06 (body receipt sha256/16 ff85b1540289014c).  UNCHANGED here.
  problem    LZW.  Justified, not preferred: it is the only pricing problem with both a phase-1
             landing record and stage-1 dispersion, so a failure is attributable to the FORM rather
             than to never-run risk.
  arms       plain-bare · salt-diet-bare · plain-STATEMENT · salt-diet-STATEMENT   (matrix #1's four)
  model      claude-opus-5
  caps       C1_USD = 37.21 · C2_USD = 18.60, FROZEN in cost_caps.tsv, taken as data, not as an
             argument.  ⛔ THE TABLE'S OWN CAVEAT (2) TRAVELS WITH EVERY PHASE-2 NUMBER: "PHASE 2 IS
             UNMEASURED — C2 is §9's half-rule applied to a number nobody has observed."
             ⇒ REGISTERED, DEFAULT-IF-SILENT: THE CAP IS UNCHANGED, and any phase-2 cell that stops
             at C2 is reported CAP-COST, never as a failure.  A raise is a new dated amendment.
  ⚠️ EACH CELL IS TWO SESSIONS.  A spec-change cell requires a phase-1 landing first; phase 2 cannot
     be built without ctl/end-1 (§5).  Whether the four phase-1 halves are FIRED FRESH or CONTINUED
     from existing landed LZW cells is a COMPARABILITY question, and it is §9.
```

## §9 · ⛔ THE ONE QUESTION THIS FILE LEAVES OPEN, NAMED SO IT IS NOT MISTAKEN FOR SETTLED

**May phase 2 continue from an ALREADY LANDED phase-1 LZW cell, or must each pair's phase 1 be fired
fresh?** Continuing is far cheaper and the machinery permits it. **It is not registered here because
I have not measured what is on the run box**, and a comparability argument names a reference.
```
  STATUS      OPEN.  Not answered by this amendment and not answerable from this tree.
  WHY IT MATTERS   a continued cell's phase-1 half was fired under matrix #1's registration, not
                   this one; its cost belongs to that run and must not be added to this one's total.
  THE MEASUREMENT  the landed LZW cells on the run box: which arms, which archive, which caps,
                   and whether ctl/end-1 and a clean tree survive.
  DEFAULT-IF-SILENT   FIRE PHASE 1 FRESH for all four cells, and report phase-1 and phase-2 cost as
                   SEPARATE columns either way.  The expensive branch is the safe one here.
```
⇒ 🔑 ***AN ASKED QUESTION AND AN ANSWERED QUESTION LEAVE THE SAME TRACE IN A DOCUMENT UNLESS ONE OF
THEM IS MARKED*** — `systems` wrote that in §8 of matrix #2 four hours before I needed it.

## §10 · WHAT WOULD INVALIDATE THIS RUN

Building a phase-2 cell without `ctl/customer.log` carrying a `dispatched P1` line; reporting a pooled
"tests green" for a phase-2 cell; reading `REGRESSIONS` or `CLAUSE_TESTS` as passes; reporting V1 or V2
without its cell's P1 baseline beside it; calling this form "brownfield" or claiming it closes
`N = 0`; raising C2_USD without a new dated amendment; quoting a magnitude, a spread or a p-value from
a 4-cell pilot; or adding a continued cell's phase-1 cost to this run's total.

## §11 · WHAT THIS AMENDMENT CANNOT ESTABLISH, SAID FIRST

* **It cannot show the method produces better code.** At `k = 1`, `n = 1`, nothing is resolvable.
* **It cannot separate the phase-2 treatment from the phase-1 starting point.** §4's confound is
  structural to CONTINUATION; the P1 baseline makes it VISIBLE, not absent.
* **It cannot close `N = 0`.** That needs B-PLANTED, which is not built and is not built here.
* **A GREEN V1 does not show the agent understood the component.** It shows a suite stopped failing,
  and that suite's strength is a **ceiling of 1.000 measured against mutants authored beside it**.
  ⛔ **AND THE NUMBER THAT MATTERS IS THIS TASK'S OWN, NOT THE SET'S**, from
  `harness/systems-v3/RESULT-hidden-test-strength-v3.md`:
```
  LZW/B    score 1.000    MIN MARGIN 1    clears_too_early · decoder_ignores_clear
  (set-wide: SEVEN mutants across FOUR cells are killed by a SINGLE test)
```
  ⇒ **The rung this pilot scores kills two of its own mutants by exactly one test.** A phase-2
  submission that differs where that one test does not probe is reported `V2 GREEN`.
  **The margin, not the rate, is what a correctness claim rests on.**

---

# ADDENDUM 1 — §9 IS MEASURED. THE CONTINUATION CANDIDATES EXIST, ALL FOUR ARMS, THREE EACH.
## Appended 2026-09-09 PDT, after the amendment above was frozen. ⛔ **THE AMENDMENT IS NOT EDITED. §9's DEFAULT STANDS UNTIL RULED; THIS SECTION MAKES THE ALTERNATIVE REGISTERED AND SELECTABLE INSTEAD OF MERELY CHEAPER.**

§9 left one question open and said it was *"not answerable from this tree"*. It is answerable from the
run box, and I measured it there rather than leaving it as a budget question somebody re-opens at ②.

## A1 · THE CENSUS, TAKEN AT THE OBJECT

```
  arm                cells (all LZW, phase 1)          end-1  clean  branch  landed-1
  plain-bare         93323249  c34012e0  d91f137b        3/3    3/3    main     3/3
  salt-diet-bare     18fb3eed  7ac56e4e  eb558398        3/3    3/3    main     3/3
  plain-STATEMENT    22ee7d33  922d1ff0  f795e96f        3/3    3/3    main     3/3
  salt-diet-STMT     6d58f1ec  9aca67c5  f5f66c47        3/3    3/3    main     3/3
```
⇒ **`customer.sh`'s two preconditions — `ctl/end-1` exists and the tree is clean — are satisfied by
all twelve.** Every one carries its arm's `CLAUDE.md` (plain 5,024 B · salt-diet 13,123 B with three
method docs) and a `LANDING.md`, so **continuing preserves the treatment rather than re-applying it.**
⇒ **ZERO cells anywhere on the box carry `ctl/customer.log`. No spec-change cell has ever been
dispatched, in any campaign.** ②, whichever branch it takes, is cell 1 of this form.

## A2 · ⛔⛔ A TAG NAMED AFTER AN ARM THAT IS NOT THE ARM — AND IT IS THE SALT ARM'S OWN ARTEFACT

My first partition of these twelve read the git tag `statement-1` as "the statement arm". Measured:

```
  tag statement-1 present on   18fb3eed 7ac56e4e eb558398 6d58f1ec 9aca67c5 f5f66c47
                               = ALL SIX salt-diet cells, and NO plain cell
  ctl/card_extras = statement  22ee7d33 922d1ff0 f795e96f 6d58f1ec 9aca67c5 f5f66c47
                               = the SIX cells actually BUILT with --statement
  the two sets AGREE on three cells and DISAGREE on six.
```
⇒ **`statement-1` is a tag the SALT METHOD'S OWN WORKFLOW creates** — the method briefs the agent to
write a statement — **so it marks the treatment, not the arm.** A partition taken from it puts three
plain-STATEMENT cells in the bare group and three diet-bare cells in the statement group.
⇒ 🔑 ***AN ARTEFACT NAMED AFTER AN ARM IS EVIDENCE ABOUT THE ARM'S BEHAVIOUR, NEVER A LABEL FOR IT.***
This campaign has carded the mirror image — a referee `seal()` keyed on the treatment's vocabulary,
which could not see the control improvising the treatment. **Same defect, other direction.**
⛔ **REGISTERED: THE ARM OF A CELL IS `ctl/arm`, AND ITS EXTRAS ARE `ctl/card_extras`.** No arm
partition is taken from a git tag, a file name, a directory name, or the presence of method content.

## A3 · ⛔ THE HAZARD REUSE INTRODUCES, WHICH IS NOT COST — IT IS A FREE PARAMETER

The pilot is **n = 1**. Three landed candidates per arm means **choosing one is a degree of freedom**,
and it is exercised after the phase-1 costs, landings and verdicts are all known.
⇒ 🔑 ***A SELECTION MADE AFTER THE OUTCOMES ARE VISIBLE IS FITTING, EVEN WHEN THE SELECTOR IS
INNOCENT*** — this is the campaign's own "a gate fitted to its own data is not a gate", moved from a
threshold to a sample.

**THE SELECTION RULE, REGISTERED HERE, BEFORE ANY P1 BASELINE HAS BEEN COMPUTED FOR ANY CELL:**
```
  1. Run the P1 baseline (§4) on ALL TWELVE.  Zero model tokens: a cargo build and a driver run.
  2. A cell is ELIGIBLE iff p1_regressions_failed == 0 — its own phase-1 landing passes its own
     base suite.  This is a VALIDITY filter, applied identically to every arm, not an outcome filter:
     a cell already failing its own regressions is not a valid given for any arm.
  3. Among an arm's eligible cells, take the LOWEST CELL ID lexicographically.  The ids are
     sha-derived and carry no outcome information.
  4. An arm with NO eligible cell has its phase 1 FIRED FRESH, and that fact is reported.
  ⛔ 5. THE ELIGIBLE COUNT PER ARM IS ITSELF REPORTED, and it is arm-correlated information: an
     asymmetry in how many phase-1 landings pass their own regressions is a finding about phase 1,
     and it travels with every phase-2 number in the same table.
  ⛔ 6. The two NOT-chosen baselines per arm are recorded too. They cost nothing and they measure the
     WITHIN-ARM SPREAD OF THE STARTING POINT — the confound's own magnitude, which no other
     quantity in this design exposes.
```
📌 **One candidate is already flagged by its own tags: `eb558398` carries `refused-1` beside
`landed-1`.** Recorded here before the baselines are run so it cannot be quietly dropped later; the
rule above does not special-case it, and its baseline decides its eligibility like any other.

## A4 · ⚖️ THE RECOMMENDATION, AND WHAT IT DOES NOT DO

**RECOMMENDED: REUSE, under A3's rule.** Firing four fresh phase-1 halves costs up to
`4 x C1_USD = 4 x 37.21 = $148.84` and buys **nothing about phase 2**: the confound is inherent to
CONTINUATION and is not reduced by a fresh phase 1, because a fresh phase 1 is *also* run by the arm
under test. **The only thing fresh cells buy is that phase-1 and phase-2 cost belong to one
registration — and §8 already requires those be separate columns either way.**
⛔ **WHAT THIS DOES NOT DO: it does not flip §9's default.** The default-if-silent above remains FIRE
FRESH. This addendum registers the alternative, its rule, and its price so the choice at ② is a
ruling on two stated branches rather than an improvisation under a budget. **The cheaper branch is
the one I am recommending, which is exactly why the rule that removes its free parameter is written
here, before any of its numbers exist.**

---

# ADDENDUM 2 — ⛔⛔ §4's P1 BASELINE INSTRUMENT CANNOT RUN. I DROVE IT AND IT FAILED IN THE FLATTERING DIRECTION.
## Appended 2026-09-09 PDT. ⛔ **THE AMENDMENT AND ADDENDUM 1 ARE NOT EDITED. §4's INSTRUMENT IS CORRECTED HERE, BEFORE ANY CELL OF THIS FORM HAS FIRED.**

§4 registered: *"run `B/run_tests.sh` against the tree at tag P1"*. **I drove it. It cannot run, and it
was never going to be able to.**

## B1 · THE DRIVE, AT THE OBJECT
`LZW/B/run_tests.sh` against the landed phase-1 tree of the `plain-bare` cell `93323249`, under the
frozen toolchain env:
```
  RC=3
  error[E0425]: cannot find function `encode12` in this scope
  error[E0599]: no variant named `Encode12` found for enum `lzw::Op`
  error[E0599]: no variant named `Decode12` found for enum `lzw::Op`
  error: could not compile `lzw` (bin "driver") due to 12 previous errors
  TESTS 0/0
```
⛔ **AND THE PART THAT MATTERS MORE THAN THE FAILURE: there is NO `REGRESSIONS` LINE AND NO
`CLAUSE_TESTS` LINE IN THAT OUTPUT AT ALL.** The driver never ran, so it printed neither.

⇒ **THE B DRIVER IS COMPILED AGAINST THE SUBMISSION AND CALLS `encode12`, `decode12`, `Op::Encode12`
and `Op::Decode12`. A PHASE-1 TREE DEFINES NONE OF THEM, BY CONSTRUCTION.** The B rung requires the
EXTENDED interface, which is exactly what `customer.sh` installs — **so the one moment §4 asked for
the measurement is the one moment the measurement is a build error.**

## B2 · ⛔⛔ THE FAILURE DIRECTION, WHICH IS WHY THIS IS AN ADDENDUM AND NOT A FOOTNOTE
A baseline recorder that reads `regressions_failed` out of that output finds the field **ABSENT**, and
the cheapest handling of an absent count is **zero**:
```
  what happened          the crate did not compile; nothing was measured
  what a reader records  p1_regressions_failed = 0
  what that means        "this cell's phase-1 landing passes its own base suite perfectly"
```
⇒ 🔑 ***AN INSTRUMENT THAT REPORTS ABSENCE FAILS TOWARD ABSENCE, AND HERE ABSENCE IS THE FLATTERING
ANSWER*** — a total build failure is byte-indistinguishable from a flawless landing, and it would have
propagated into the eligibility filter of Addendum 1 §A3 as **every cell eligible for the right reason
by accident.** My own bank carries this law from yesterday; **it caught me on the registration I wrote
to apply it.**
📌 **§3 of the amendment already forbids this** — *"a missing `REGRESSIONS` or `CLAUSE_TESTS` line is
UNMEASURED, never GREEN"*. **The rule was correct and the instrument it governed could not produce the
line at all.** ⇒ ***A CORRECT RULE ABOUT A FIELD DOES NOT ESTABLISH THAT ANY RUN CAN PRODUCE IT.***

## B3 · ✅ THE CORRECTED INSTRUMENT, AND IT HAS ALREADY RUN

**REGISTERED, REPLACING §4's FIRST SENTENCE:** the P1 baseline is taken with the **`G` rung's**
`run_tests.sh` on the cell's phase-1 landing — the base suite alone, which is precisely what
"regressions" names, since the B driver's base suite is *phase 1's driver verbatim*.
```
  p1_base_passed / p1_base_total     from the G rung's `TESTS <passed>/<total>`
  ⛔ POLARITY: the G runner prints PASSED.  The B runner's REGRESSIONS line prints FAILED.
     The corrected baseline therefore reports a DIFFERENT POLARITY from the field it is a baseline
     for, and every consumer names which one it is reading in the expression that reads it.
  p1_solution_sha256                 unchanged
```
⛔ **THE CLAUSE HALF OF THE BASELINE IS STRUCK, NOT DEFERRED.** `p1_clause_failed/total` was
registered as a quantity to record. **It is not a quantity**: a phase-1 tree cannot define the clause's
functions, so there is no state of the world in which it is anything but "did not compile". Recording
it would have been recording a constant as a measurement.

✅ **AND THE CORRECTED BASELINE COSTS NOTHING, BECAUSE IT IS ALREADY MEASURED.** The post-hoc
correctness pass ran the G rung over every matrix-1 cell. From
`harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv` and the run's own verdicts
table, all twelve LZW phase-1 landings:
```
  arm                cell       class   TESTS      arm                cell       class   TESTS
  plain-bare         93323249   PASS     8/8       plain-STATEMENT    22ee7d33   PASS     8/8
  plain-bare         c34012e0   PASS     8/8       plain-STATEMENT    922d1ff0   PASS     8/8
  plain-bare         d91f137b   PASS     8/8       plain-STATEMENT    f795e96f   PASS     8/8
  salt-diet-bare     18fb3eed   PASS     8/8       salt-diet-STMT     6d58f1ec   PASS     8/8
  salt-diet-bare     7ac56e4e   PASS     8/8       salt-diet-STMT     9aca67c5   PASS     8/8
  salt-diet-bare     eb558398   PASS     8/8       salt-diet-STMT     f5f66c47   PASS     8/8
```

## B4 · ⇒ ADDENDUM 1's SELECTION RULE, RESOLVED — AND THE FOUR CELLS NAMED BEFORE ANY PHASE-2 NUMBER EXISTS

Rule 2 (eligible iff the phase-1 landing passes its own base suite) admits **12 of 12, uniformly, all
four arms**. Rule 5's eligible-count asymmetry is **3/3 in every arm — no asymmetry to report.** So the
selection reduces to rule 3's blind tiebreak, and it is discharged here, in writing, **before a single
phase-2 quantity exists for any cell:**
```
  plain-bare        -> 93323249        plain-STATEMENT   -> 22ee7d33
  salt-diet-bare    -> 18fb3eed        salt-diet-STMT    -> 6d58f1ec
```
📌 `eb558398`'s `refused-1` tag, flagged in Addendum 1, is **moot**: it is eligible on the measurement
and it is not the lowest id in its arm. It was named in advance precisely so this sentence could be
written rather than assumed.

## B5 · ⛔ AND THE LIMIT ON WHAT B3 SHOWS, BECAUSE 12 OF 12 IS A CEILING AND NOT A CLEAN BILL

**8/8 on an 8-test base suite is the top of the scale.** Twelve cells reading identically means **this
suite cannot tell them apart**, not that the twelve landings are equivalent.
⇒ **Rule 6 of Addendum 1 — record the two not-chosen baselines to expose the WITHIN-ARM SPREAD of the
starting point — returns ZERO SPREAD ON THIS INSTRUMENT, and that reading is VACUOUS at the ceiling.**
It is reported as `spread UNMEASURABLE at ceiling`, never as `spread = 0`.
⇒ 🔑 ***AN ARM AT CEILING LEAVES NO ROOM TO DISCRIMINATE, AND HERE THE ARM AT CEILING IS THE BASELINE
INSTRUMENT ITSELF.*** The campaign has now met this shape three times — a 1.000 kill rate against a
mutant set authored beside the suite, a 0-survivor arm-coverage sweep, and now a 12-of-12 baseline.
⛔ **CONSEQUENCE FOR THE RESULT: the confound of §4 is NOT shown to be small. It is shown to be
INVISIBLE TO THE ONLY PRE-PHASE-2 INSTRUMENT THIS DESIGN HAS**, and that sentence travels with every
V1 and V2 verdict this pilot produces.

---

# ADDENDUM 3 — ⛔⛔ REUSE IS BY **COPY**. DISPATCHING INTO A LANDED MATRIX-1 CELL WOULD MUTATE THE ARTEFACT BEHIND A PUBLISHED RESULT.
## Appended 2026-09-09 PDT. ⛔ **THE AMENDMENT AND ADDENDA 1–2 ARE NOT EDITED. THIS SECTION CONSTRAINS THE REUSE BRANCH ADDENDUM 1 RECOMMENDED; IT DOES NOT WITHDRAW THE RECOMMENDATION.**

Addendum 1 recommended reuse and named four cells. It said nothing about **where** the dispatch lands,
and that omission is the difference between a cheap branch and a destructive one.

## C1 · ⛔⛔ `customer.sh` WRITES INTO THE CELL'S OWN REPOSITORY. IT IS NOT A READ.
```
  REPO="$CELL/repo"
  ... > "$REPO/inbox/change-1.md"          a new file
  ... > "$REPO/REQUIREMENTS.md"            OVERWRITTEN with the --change rendering
  cp "$TASK/B/interface.rs" "$REPO/interface.rs"   OVERWRITTEN with the extended interface
  ... >> "$REPO/BUS.md"                    appended
  $G commit -q -m "CUSTOMER: change request 1"     A COMMIT ON main
  $G tag P1                                        A TAG
```
⇒ **The four cells Addendum 1 named live in `cells-matrix1`. They are the landed evidence behind
matrix #1's result, the post-hoc correctness pass, the statement-arm result, and the paper submitted
to arXiv.** A dispatch into them **overwrites two tracked files and adds a commit and a tag to the
repository whose state those results describe.**
⇒ 🔑 ***"REUSE THE LANDING" AND "DISPATCH INTO THE CELL" ARE NOT THE SAME ACT, AND ONLY ONE OF THEM IS
REVERSIBLE.*** The campaign's standing rule is **re-score FROM the archive, never IN it**; this is that
rule met on the fire path rather than the scoring path, where the write is a git commit rather than a
rebuilt `.lake`.

⛔ **REGISTERED: NO SPEC-CHANGE DISPATCH IS EVER MADE INTO A CELL UNDER `cells-matrix1`, OR UNDER ANY
CELLS ROOT WHOSE CELLS ARE CITED BY A LANDED RESULT.** Reuse copies the cell into a NEW cells root
first, and the dispatch lands on the copy.
```
  the copy records, in the new cell's ctl/:  source_root · source_cell_id · source_HEAD sha
  ⇒ a continued cell can always name the landing it continues, and the original is byte-untouched
```

## C2 · ⛔⛔ AND THE COPY IS NOT A COPY: THE FENCE IS A GLOB TAKEN AT RENDER TIME

Measured on `93323249`'s `ctl/fence.json`: it names **35 distinct sibling paths under its own cells
root**, enumerated when the batch was rendered.
```
  cells-matrix1/_archive   cells-matrix1/_audit   ... 35 peer paths, as literal deny globs
```
⇒ **A cell copied to a new root carries a fence that denies the OLD root's siblings and is SILENT
ABOUT ITS NEW ONES.** The agent's peers in the new root are outside every deny rule it carries.
⇒ 🔑 ***A DENY-SET ENUMERATED AT RENDER TIME IS A CLAIM ABOUT THE DIRECTORY AS IT WAS, AND COPYING A
CELL CHANGES THE DIRECTORY WITHOUT CHANGING THE CLAIM.*** This campaign has already paid for the
same mechanism twice, in the other direction — a second batch built after a first leaves the first
batch's fence permissive toward the new arrivals, in **both** fence layers, and only a drift check
sees it.

⛔ **REGISTERED, BEFORE ANY REUSED CELL IS LAUNCHED:**
```
  1. RE-RENDER the fence for every cell in the new root, in ONE pass, AFTER every copy has landed.
     A pass that runs while a later copy is still to come repeats the defect it is fixing.
  2. DRIFT-CHECK both layers against the new root's actual contents, and refuse the launch on any
     cell whose fence does not name every peer present.
  3. The check is driven RED first by planting a peer AFTER the render and confirming the drift
     check refuses — an absence assertion needs an arm that produces the presence.
```
⚠️ **NAMED, NOT MEASURED:** whether anything else in a cell's `ctl/` is root-relative in the same way.
`budgets.env` is measured and is NOT — it carries the frozen `C1_USD 37.21` / `C2_USD 18.60` and the
phase-2 token and wall rows, so **a reused cell is already armed for phase 2.** `fence.json` is the one
file I have checked for root-relative content, and **I am not claiming the others are clean.**

## C3 · ⇒ WHAT ② NOW COSTS, AND WHY IT IS STILL THE CHEAP BRANCH
```
  fresh phase 1 x 4        up to 4 x C1_USD 37.21 = $148.84, plus phase 2
  reuse by copy x 4        $0 in model tokens, plus a copy, a fence re-render and a drift check
```
The reuse branch stays recommended. **What Addendum 1 got wrong was not the branch, it was the
verb** — and a reader who took "reuse the landed cell" literally would have written a commit into the
evidence for a submitted paper before firing a single model call.

## C4 · 📌 THE FEASIBILITY STATUS OF THE WHOLE FORM, MEASURED WHILE CHECKING THE ABOVE
`dry_cells.sh` drives the entire sequence end to end — phase 1, `ctl/end-1`, `customer.sh dispatch`,
phase 2, `ctl/end-2`, then the manifest and the canary scan — and **refuses at each step that does not
land.** ⇒ **The spec-change form is not unbuilt and not untried: it has been driven end to end against
the STUB client (`claude-stub.sh`), and never once against a real one.**
⇒ **That is better news than "not built" and it is not the same as "works".** ⛔ **A path proven with a
stub is proven against a subject that cannot surprise it**, which is exactly the property a real
subject lacks. Registered as the honest feasibility statement: **STUB-DRIVEN END TO END; REAL-CLIENT
CELL COUNT = 0.**

---

# ADDENDUM 4 — THE DRIFT CHECK ADDENDUM 3 ASKED FOR ALREADY EXISTS, AND IT IS **FORWARD-ONLY**
## Appended 2026-09-09 PDT. ⛔ **NOTHING ABOVE IS EDITED. THIS NAMES THE TOOL FOR §C2 ITEM 2 AND RECORDS THE ONE THING IT CANNOT DO.**

## D1 · ✅ IT IS A CALL, NOT A BUILD
`render_fence_v3.py --cell <cell> --cfg <run config dir> --check <fence.json>` re-renders and compares,
and **its refusal message is already the right sentence**:
> *"DRIFT — %s differs from a fresh rendering (the fence is stale; a glob evaluated at render time is a
> snapshot, and what makes it a fence is re-evaluating it at the moment of use and refusing on
> disagreement)"*

⇒ **It compares the FULL serialized rendering, so it covers BOTH LAYERS in one comparison** —
`sandbox.filesystem.denyRead`, `sandbox.filesystem.denyWrite` and `permissions.deny`. Addendum 3's
requirement that the check see both layers is **satisfied by the existing tool**, not owed as a build.
📌 **Recorded because the fleet keeps paying for the opposite:** a good tool nobody reaches for is the
cheapest defect there is, and §C2 item 2 was one sentence away from commissioning a second one.

## D2 · ⛔⛔ AND THE LIMIT, MEASURED BY TRYING IT: THE CHECK CANNOT BE RUN ON AN ARCHIVED CELL
The rendering is a function of `(cell, cfg, verus_root, cargo_root)`. **`cfg` is not recorded anywhere
in the cell.** Measured on the `plain-bare` candidate:
```
  its ctl/fence.json      denyRead 93 · denyWrite 99 · tool rules 374
  ~/.claude* dirs on the box today: 14 — and ALL FOURTEEN are in that cell's denyRead
  ⇒ the config dir this cell actually ran under is NOT among the directories that exist now
  ⇒ nothing in ctl/ names it, so it cannot be recovered from the cell
```
⛔ **STATED AS MEASURED, NOT EXPLAINED: I could not identify this cell's own config directory from
anything inside the cell, so I could not re-run `--check` against it.** I am not claiming to know
whether the directory was deleted, renamed, or excluded by a mechanism I did not read.

⇒ 🔑 ***A CHECK WHOSE INPUTS INCLUDE SOMETHING THE ARTEFACT DOES NOT RECORD IS FORWARD-ONLY: it can
keep a fence honest from the moment of rendering onward, and it can say nothing about a fence rendered
before it was asked.*** The fence is auditable while the run is alive and unauditable afterwards, and
**that is invisible from the file itself, which looks complete.**

## D3 · ⇒ WHAT THIS CHANGES FOR ②, AND WHAT IT DOES NOT
```
  UNCHANGED   Addendum 3 §C2's sequence. A copied cell is rendered FRESH against a fresh cfg, in one
              pass after every copy lands, and --check is run against THAT rendering before launch.
              That sequence is forward-only by construction, so the limit does not touch it.
  NEW         ⛔ No claim may be made that a REUSED cell's ORIGINAL fence was current when its phase 1
              ran.  It cannot be checked now.  Any statement about the phase-1 fence of a continued
              cell is UNMEASURED, and is reported that way rather than assumed from the file's
              existence.
  OWED, small, and NOT a blocker: the renderer should write the cfg path INTO the rendering it
              produces, so a fence can be re-checked against the inputs that made it.  Registered
              here rather than built, because render_fence_v3.py's output shape is a fence contract
              and changing it mid-campaign is not a tidy-up.
```

---

# ADDENDUM 5 — ✅ ADDENDUM 3 §C2's SEQUENCE IS DRIVEN, RED-FIRST, AND THE DRIFT CHECK IS LOAD-BEARING
## Appended 2026-09-09 PDT. ⛔ **NOTHING ABOVE IS EDITED. THIS DISCHARGES A REGISTERED OWED ITEM, so a later reader does not see it as outstanding and pay for it twice.**

`§C2` registered three things before any reused cell launches: **re-render in one pass after every copy
lands · drift-check both layers · drive the check RED by planting a peer AFTER the render.** All three
are now executed on a synthetic cells root, touching no real cell and spending no model tokens.

## E1 · THE DRIVE
```
  step                                        rc   result
  1  render a fence for cell aaaa1111          0   WROTE   62 denyRead · 65 denyWrite
  2  --check, nothing changed                  0   CURRENT 62 denyRead · 65 denyWrite
  3  PLANT a new peer cccc3333, --check        1   DRIFT   <- THE RED. The check refuses.
  4  the peer in a FRESH rendering             -   8 occurrences
  5  re-render, then --check                   0   CURRENT 63 denyRead · 66 denyWrite  (+1 each)
```
⇒ **The refusal in step 3 is the whole property**: a fence rendered before a peer existed does not
name it, `--check` sees exactly that, and re-rendering closes it by precisely one peer in each layer.
⇒ **`§C2` items 2 and 3 are DISCHARGED. Item 1 — one pass, after every copy lands — is an ORDERING
and can only be discharged at ②**, against the real copies.

## E2 · ⛔ A CONSTRAINT ON ② THAT THE DRIVE FOUND BY REFUSING, AND IT IS EASY TO TRIP
My first two attempts REFUSED, correctly, and the second refusal is the instructive one:
```
  cells root under /tmp                REFUSED — "/private/tmp" is in the deny set
  cells root named ~/bench-fencedrive  REFUSED — the renderer globs ~/bench* into the deny set,
                                       and my SCRATCH DIRECTORY'S NAME matched it
  ⇒ "the cell's own <path>/repo is inside the deny set ... a fence that blocks the agent's working
     copy is not a fence, it is a blind episode that still scores"
```
⇒ ⛔ **THE COPIES' CELLS ROOT MUST NOT BE UNDER `/tmp`, MUST NOT MATCH `~/bench*` OR `~/.claude*`, AND
MUST NOT BE UNDER `~/projects`** — or the render refuses and no cell is built. **Registered here
because the natural name for a copy root is exactly the one that trips it.**
⭐ **The refusal is the tool working**: it names the offending root and says why, and it fires at
render time rather than at scoring time.

## E3 · 📌 AND ONE OF MY OWN, RECORDED BECAUSE IT IS THE THIRD TIME
My first drive script read the renderer's exit code through `| tail -1`, so a **refusing** command
reported `rc=0` and step 1 looked like a pass. ⇒ ***`cmd | tail` GIVES YOU `tail`'s EXIT CODE***, and
it fails in the direction that reads as success. Caught in one iteration by the refusal text
disagreeing with the code beside it — **two readings of one event, which is the only reason it was
visible at all.**

---

# ADDENDUM 6 — ✅ THE REUSE MECHANIC IS DRIVEN END TO END, AND ⛔ THE HARNESS EXPORT IS AN UNDECLARED CHOICE AMONG 35
## Appended 2026-09-09 PDT. ⛔ **NOTHING ABOVE IS EDITED.** Two facts ② needs, both measured, so a fresh head does not re-derive them.

## F1 · ✅ COPY → DISPATCH WORKS, AND THE ORIGINAL IS BYTE-UNTOUCHED
Addendum 3 registered *reuse is by COPY* and left the mechanic unproven. It is now driven, on a copy of
the `plain-bare` candidate, at **zero model tokens**:
```
  customer.sh dispatch <copy> <task>    rc 0
    "dispatched change request 1 to dry00001 at 3c737fb (payload sha b777bf53bf66ae65)"
  ON THE COPY    inbox/change-1.md 2769 B · tag P1 added beside landed-1 and s1
                 commit 3c737fb authored `customer` · REQUIREMENTS.md gains `## Change 1`
                 interface.rs gains `encode12` · ctl/customer.log carries the `dispatched P1` line
  ON THE ORIGINAL 93323249    HEAD unchanged 97e7336a · tags unchanged · tree clean
                 ⛔ ctl/customer.log ABSENT — the marker §5 defines a spec-change cell by never appeared
```
⇒ **The copy becomes a spec-change cell by §5's own definition, and the original does not.** That is the
whole of Addendum 3's §C1, executed rather than asserted.
📌 **The payload sha is the manifest row Addendum 1 promised is identical across the arm pair.** For LZW
under this export it is `b777bf53bf66ae65`; each arm's dispatch prints its own and they must agree.

## F2 · ⛔⛔ `customer.sh` IS NOT WHERE A REFEREE-SIDE READER WILL LOOK, AND THE FIRST DRIVE FAILED THERE
My first attempt ran it from the referee's export and got **rc 127, "No such file or directory"**.
```
  the referee export's harness/systems-v3/ holds THREE files:
      _common_v3.sh · Cargo.toml.template · rust_env.sh
  customer.sh lives ONLY in the sha-named harness exports:
      ~/projects/claude/saltbench-systems-v3-export-<sha>/harness/systems-v3/customer.sh
```
⇒ **The referee export is a toolchain shim, not the harness.** ⛔ **And a `command -v`-style check would
not have helped: the failure is a PATH that exists for other tools and not for this one.**

## F3 · ⛔⛔ THIRTY-FIVE HARNESS EXPORTS, AND NOTHING DECLARES WHICH IS CURRENT
```
  export trees on the box                         35
  customer.sh                                     IDENTICAL in all 35 (one sha)
  render_requirements.py                          THREE DISTINCT VERSIONS  (27 · 7 · 1)
  and a bare, undated ~/projects/claude/saltbench-systems-v3-export beside them
```
⇒ 🔑 ***A DISPATCH IS A FUNCTION OF THE EXPORT IT IS RUN FROM, AND THE BOX OFFERS 35 CANDIDATES WITH NO
DECLARATION*** — the same shape this campaign already carded when a root variable was trusted as a path
on a box holding three verus builds. **A pin that is a path is not a pin when the box holds 35.**

✅ **AND THE HAZARD IS CHECKED, NOT ASSUMED — IT IS NOT LIVE FOR THIS PAYLOAD.** Both halves of what the
subject receives were rendered from one card by all three renderer versions:
```
  --clause  (inbox/change-1.md's body)   sha f1e0c2f56b363801   2414 B   IDENTICAL 3 of 3
  --change  (REQUIREMENTS.md)            sha 46651a850f1b20f9   8247 B   IDENTICAL 3 of 3
```
⛔ **SCOPE, STATED RATHER THAN GENERALISED: that is ONE card (LZW) and TWO flags.** It says nothing about
`--hint`, `--statement`, or the other thirteen cards, and I did not test them. **The three versions
differ somewhere; they simply do not differ here.**
⇒ **REGISTERED FOR ②: the export tree is NAMED in the run record with its sha, beside the payload sha,
for every dispatch.** A dispatch whose export is not recorded cannot be reproduced, and the fact that
the choice does not matter today is not a reason to leave it unrecorded — it is the reason it is cheap
to record now.
