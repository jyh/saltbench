# PRE-SPECIFICATION — THE POST-HOC CORRECTNESS PASS OVER MATRIX #1
## Dated 2026-09-09. ⛔ **THE COMMIT THAT FREEZES THIS FILE IS THE AUTHORISATION, AND NO SUITE HAS RUN ON ANY CELL REPO.**
Authorised by the helm on the Captain's question of 14:5x — *"Are you serious that we do not check
correctness? We do not have the test suites?"* **The suites exist. The referee was never invoked on these
cells.** This document is what makes invoking it now a measurement rather than a story.

---

## §1 · THE HONESTY CLAUSE, FIRST, BECAUSE EVERYTHING ELSE DEPENDS ON IT

⛔⛔ **MATRIX #1 WAS REGISTERED AS A COST EXPERIMENT AND I ALREADY KNOW ITS RESULT.** The sign test is 5
of 5 at p = 0.0312 on both readings, and I know which arm spent more on every problem. **Any correctness
pass I run now is run by someone who is not blind.**
⇒ 🔑 ***THAT DOES NOT MAKE THE MEASUREMENT WORTHLESS. IT MAKES THE ORDER LOAD-BEARING.*** The only thing
separating a declared post-hoc measurement from the defect this campaign exists to avoid is that **the
classes and the meanings are fixed before the first suite runs.** This file fixes them.
📌 **This pass is POST HOC and will be labelled so wherever it is reported.** It is not a pre-registered
result and may never be presented as one.

## §2 · THE POPULATION — MEASURED AT THE RUN BOX 2026-09-09, NOT ASSUMED

```
  ~/cells-matrix1     37 cells with ctl/arm   37 with repo/     ⇒ every agent output survives
  ~/cells-n3-topup     3 cells with ctl/arm    3 with repo/
  the three SS12 smoke cells (~/cells)         3 with repo/
```
⇒ **The correctness pass covers the SAME declared set the cost reading uses, on BOTH readings** —
**A = 43 cells** (matrix root + top-up + smoke) and **B = 40** (smoke out). ⛔ **A correctness column over
a different population than the cost column would be two results about two datasets printed side by
side**, which is the defect the declared-set law exists to prevent.

## §3 · THE VERDICT CLASSES — ASSIGNED BY THE HARNESS, NEVER BY JUDGEMENT

Every cell lands in exactly one class. **The class is derived from the runner's own output and the cell's
own `ctl`, never from reading the agent's code.**
```
  PASS            run_tests.sh runs and every withheld test passes
  FAIL            run_tests.sh runs and at least one withheld test fails
  NO-BUILD        the repo does not compile, on a cell whose ctl kind is LANDED
  CAP-COST        ctl kind is CAP-COST — the cell was stopped mid-work by the budget
  FAILED-BOOT     ctl kind is FAILED-BOOT — produced no subject behaviour (4 such in the matrix root)
  INTERFACE-MISS  compiles, but does not satisfy the fixed interface, so the suite cannot bind
```
⛔⛔ **THE THREE RULES THAT MAKE THESE CLASSES HONEST:**
1. **`CAP-COST` AND `FAILED-BOOT` ARE NOT FAILURES OF THE METHOD.** A cell stopped by a budget has not
   been asked the question. **They are reported in their own rows and are NEVER pooled into FAIL**, and
   never silently dropped either — **a dropped cell is a claim that it did not exist.**
2. **`NO-BUILD` ON A LANDED CELL IS A REAL ADVERSE OUTCOME AND COUNTS AS NOT-PASS.** The agent said it
   was done and it does not compile.
3. **`INTERFACE-MISS` IS NOT `FAIL`.** Missing the interface is a different error from a wrong answer,
   and pooling them would let a formatting mistake read as an incorrect algorithm. It is reported
   separately and counted as NOT-PASS.

## §4 · THE ANALYSIS, FIXED NOW

* **Primary:** per problem, the number of PASS cells in `plain-bare` and in `salt-diet-bare`. Then the
  **cross-problem sign test on the per-problem pass-count difference** — the same shape and the same
  registered reading as the cost result, so the two columns are commensurable.
* **Reported for both readings A and B, always**, exactly as the cost result is.
* ⛔ **THE UNINFORMATIVE OUTCOME IS REGISTERED IN ADVANCE:** with 3 cells per arm per problem, **it is
  entirely possible that every cell passes, or that pass counts are equal on every problem.** That is a
  **REGISTERED OUTCOME — "the instrument did not separate the arms"** — and it is not a failure, not a
  null to be spun, and not grounds for a second analysis chosen afterwards.
* ⛔ **NO SECOND ANALYSIS.** If this reading is uninformative, the answer is a larger n or a harder
  suite in v2, **not another cut of these 43 cells.**

## §5 · WHAT EACH OUTCOME MEANS — ALL THREE DIRECTIONS, WRITTEN BEFORE ANY OF THEM IS SEEN

**(a) SALT MORE CORRECT.** ⛔ **This does NOT establish that the method produces better code**, and the
reason is in the cost result itself: **the salt arm SPENT MORE on every problem.** More spend is more
turns and more work, so **method and effort are confounded by construction at this design.** The honest
statement would be *"the arm that cost more also passed more, and this design cannot say which caused
which."* ⇒ **A funding claim may not be built on it.**

**(b) SALT LESS CORRECT.** ⭐ **This is an ADVERSE finding and it is reported AHEAD OF THE COST RESULT,
in the abstract, not in a limitations paragraph.** It would mean the premium bought worse code — the
single most decision-relevant thing this dataset could say — and it is **exactly the outcome a
post-hoc pass run by a non-blind author is most likely to soften.** ⇒ **Registered here so it cannot be.**

**(c) NO DIFFERENCE.** The most likely outcome and the least quotable. It means **the premium bought no
correctness change this instrument can see.** ⇒ **It is reported in the same sentence as the premium,
every time the premium appears**, because a cost result whose correctness column is flat is a different
proposition from one with no column at all.

## §6 · WHAT A `PASS` DOES NOT MEAN

⛔ **A PASS IS NOT "CORRECT". IT IS "THE WITHHELD SUITE DID NOT FAIL IT."** The suites' measured strength
is **44 of 44 mutants killed — a CEILING, not a strength**: the mutants were authored beside the tests
and **seven of them die to a single test.** ⇒ **The suites are demonstrably not vacuous, and they are not
demonstrably hard.** Every reported pass rate carries that sentence.

## §7 · FORBIDDEN SENTENCES

1. *"The salt arm costs more and produces more correct code."* — joins two results with a causal claim
   this design cannot support, and (a) above says why.
2. *"N of 43 cells were correct."* — a pass is a suite outcome, not a correctness verdict.
3. Any ratio or range reported as the finding of the COST result, unchanged from the standing rule —
   **not "2.7×", not "1–3×"**.

## §8 · WHAT WOULD MAKE THIS UNPUBLISHABLE

Running any suite on any cell repo **before this file is committed**; choosing a class boundary **after**
seeing a result; **pooling** CAP-COST or FAILED-BOOT into FAIL; **dropping** a non-building cell
silently; or reporting a second analysis because the first was uninformative. ⇒ **Each is checkable
against this file by anyone, which is the point of freezing it.**
