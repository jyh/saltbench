# DESIGN: CORRECTNESS AS THE PRIMARY OUTCOME. The referee's verdict decides what a cell is before anything is counted about it.
## bench (SaltBench lead), 2026-10-02. Objectives O57 · O60. Commissioned at council 2026-10-02 (minute seat `865727d77`, item 9).
## Statistics: evidence. Text: paper. A refuter pass precedes any wave run under it.
## ⛔ DRAFT, REVISION 2. Not a registration. It binds nothing until a dated AMENDMENT freezes it (§D8), before the first model call of the run it governs.
## Revision 2 takes the non-author refuter pass on revision 1 (blob `e1c16efcfd3f`; PR #311, comment 5955729360). Every repair is mapped in §D10.

The Captain's question at the table: *"How is it that we know the agent doesn't just submit an arbitrary program, like a constant function?
We should have put correctness in as a primary criterion, so let's commission a design phase."*

---

## §D0 · WHAT IS TRUE TODAY, AND WHERE IT FALLS SHORT

**A constant function fails every referee we run.**
- O60's builder seeds every cell with a stub whose body is `xor eax, eax; ret`, a function that returns 0
  (saltbench-systems `harness/systems-x86/x86_cell_build.py:86-88`).
- O60's release condition L5 requires that stub to read TESTS_FAIL on every task, and it did, on 22 of 22
  (`harness/systems-x86/REGISTRATION-O60-scalar-population-2026-10-01.md:172,441`).
- The Rust referee runs a withheld suite after the build; a build alone never passes
  (saltbench-systems `harness/systems-v3/referee_v3.py:52,356`).

**What was missing is the ORDER.** No registration in this repository makes the referee's verdict the primary outcome:
- Matrix #1 was registered as a COST experiment, and its correctness pass was declared post hoc
  (`harness/systems-v3/PRESPEC-posthoc-correctness-matrix1-2026-09-09.md:11-18`).
- The v3 correctness tables are post hoc and descriptive (`harness/systems-v3/REGISTRATION-correctness-tables-v3-2026-10-01.md:6-9`).
- O4 #1 and O60 register no pass-rate outcome.
- Lane B reports cost and pass rate as two separate results (`harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md:215,232`).

**AND THE REFUTER PASS FOUND THAT THE x86 REFEREE'S CLASS IS NARROWER THAN THE REGISTRATION'S WORDS.**
- `check_x86.py` decides PASS from executor (a) against the expected values alone.
- It reports the two executors' agreement BESIDE the class, never in it (its own docstring).
- So a routine that returns the right bytes while writing outside its declared footprint, or clobbering a callee-saved register, reads
  `CLASS PASS` today. The registration's *"AGREEMENT required per input"* is a statement about the registration, not about the class.
- §D2 is what makes agreement required.

## §D1 · THE PRINCIPLE, AND WHAT "THE CODE UNDER TEST" IS

***A cell is CLASSIFIED from the referee's record before it is MEASURED by anything else.*** Every other quantity is a property of a class
of cells and is never pooled across classes. That covers cost, tokens, wall time, turns, the landing claim and spec_strength.

**The unit under test:**
- **On plain:** the card's one assembly file.
- **On salt-diet:** the triple (routine, spec, proof). Every `.lean` the cell leaves under `Submission/` is part of it. A Lean-gate failure
  is the subject's, and its `tests=` result is reported beside it.

## §D2 · THE FOUR CLASSES — mapped from what the instruments EMIT, each token exactly once

**The classifier.**
- Classification is a pure function over three inputs: the referee's JSON record, the watcher's end kind, and whether the subject declared.
- It is implemented once (`classify_cell.py`, §D5), with a selftest arm for every token below. It is never applied by hand.
- A token the instruments emit that the table does not map is a classifier REFUSAL. It is never a default class.

| class | the record reads | notes |
|---|---|---|
| **ACCEPTED** | referee `class == PASS` **and** agreement reads `AGREE=n` with `n` = the number of withheld inputs (no other rider) **and** no harness finding | whether or not the cell declared: a tree stopped by a cap that the referee passes is ACCEPTED, and its run state is a reported column |
| **REJECTED** | referee `class` ∈ {TESTS_FAIL, NO_SOLUTION, ASSEMBLE-FAIL, REFUSED-LINK, SCREEN, SCREEN(spec), AXIOMS} · or `COMPILE`/`TARGET` **with** a Lean diagnostic (`build_first_error` non-null) · or `PASS` with any of MODEL-OUTSIDE · MODEL-CLOBBERED · MODEL-FAULT · NATIVE-OUTSIDE (which dominates any UNSCORABLE rider) · or a referee crash caused by the cell's own tree | a footprint or ABI violation is a failing verdict. MISSING is not here, against K7's suggestion: an input absent from one executor's output cannot say whose fault it is |
| **HALTED** | the cell ended without a landing (watcher end kinds DONE · CAP-TOKENS · CAP-COST · CAP-WALL · POKED-OUT · STALLED · EXIT-FORCED) **and** the referee, run on the stopped tree, read REJECTED. A stopped tree the referee cannot score is UNSCORABLE: re-referee | the referee is ALWAYS run on a halted tree, by the harvest and not by hand |
| **UNSCORABLE** | `COMPILE`/`TARGET` with no Lean diagnostic (`build_first_error` null, or `target_errors` empty). This covers a timeout (rc 124) and the build lock's wait-abort (rc 75). The referee's record carries no rc, so the diagnostic is the tell · `PASS` with INCONCLUSIVE-(b) (fuel), DISAGREE or MISSING, or an AGREE count short of the inputs · `REFUSED-TRANSLATE` (see below) · `CLASS HARNESS` · `REFEREE REFUSE` · no CLASS line within the referee's wall bound (`REFEREE-TIME`) · watcher CRASH · METER-BLIND · COST-BLIND · BOX-UNREADABLE · QUOTA-BLOCKED · FAILED-BOOTS · DIALOG | the instrument failed, or the record cannot say whose fault it was |

**The rules that the table needs.**
- **The subject's claim never classifies.** LANDED, `LANDING.md` and `false_done_claims` are reported beside the class. Declaring routes a
  cell to the referee; it does not decide the class.
- **REFUSED-TRANSLATE is UNSCORABLE until it is split by mechanism.**
  - The translator refuses some instances of forms the allowed list admits. The refuter drove a 32-bit address register in a listed form:
    `rt check` reads `FORMS OK` while the pinned translator refuses.
  - So "the subject used a forbidden form" and "the translator lacks an allowed instance" emit the same token.
  - The split, which needs the cut's FORM screen run on the refused instance, is OWED. Until it exists, the registration's own word holds:
    a non-scoring outcome (`REGISTRATION-O60-…:345`).
- **A fault the record cannot attribute is UNSCORABLE, not REJECTED.**
  - DIALOG (the client's own dialog) is an instrument end.
  - POKED-OUT and STALLED are filed as the subject's halts, because no instrument tell for them exists yet. That tell is OWED (§D7),
    and the limit is printed beside the classifier's verdicts.
- **UNSCORABLE cells are RE-REFEREED or RE-FIRED, and the two are distinct.**
  - A referee re-run on the same tree is not a new cell.
  - A re-fire is a new cell and is counted as one.
  - An unrepaired UNSCORABLE is counted and named, never imputed.

## §D3 · THE OUTCOME HIERARCHY

1. **PRIMARY: TWO FIGURES PER ARM PER TASK, NEVER ONE WITHOUT THE OTHER.**
   - (i) ACCEPTED / (ACCEPTED + REJECTED): the rate among cells that reached a verdict.
   - (ii) ACCEPTED / (ACCEPTED + REJECTED + HALTED): the rate per attempt at the registered cap.
   - (ii) charges every halt to the arm that produced it, and it is a floor on the rate at any larger budget. A HALTED cell is
     *"not accepted at the cap"* and is never written REJECTED.
   - **Why (ii) exists:** `bin/declare` is the only act that produces a verdict-bearing end, and its absence produces a halt. The arm texts
     instruct different declaration policies: salt-diet lands only on a clean `VERIFIED`; plain lands when it believes the routine correct.
     So HALTED is arm-correlated by construction, and (i) alone measures a stopping policy.
   - Both figures are reported per task first, because the tasks are not exchangeable. A pooled figure is printed only beside the per-task
     table. The UNSCORABLE count rides in the same row.
2. **COST, AS ONE ROW THAT CANNOT BE PRINTED WITHOUT ITS DENOMINATORS:**
   - Per arm, per task, the row reads `ACCEPTED a · REJECTED r · HALTED h · UNSCORABLE u`, then two figures:
     - **(c1)** the mean spend over the `a` accepted cells;
     - **(c2)** the spend of the `a + r + h` cells, divided by `a`.
   - **Rule 1:** UNSCORABLE spend is EXCLUDED from (c2). It is printed beside the row as `sunk by instrument: $x over u cells`, because an
     instrument failure is not the arm's.
   - **Rule 2:** when `a = 0`, both figures print `NO ACCEPTED CELL (spend $x over r + h cells)`. They are never 0, never blank, never dropped,
     and no ratio or sign is formed from that row.
   - **Rule 3:** no cost figure is pooled across tasks. The only cross-task reading of cost is evidence's per-task PAIRED reading (§D7),
     over the tasks where both arms have `a > 0`. It prints how many tasks rule 2 excluded, and for which arm.
   - **A HALTED cell's spend enters as METERED.** It overruns the cap by whatever was spent between two watcher reads, and it is never clipped.
     This overrides lane B §Q6 6's "at the cap" (`harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md:229`), and is said here because
     it is a change.
3. **spec_strength IS A DIAGNOSTIC, NOT A SECONDARY.**
   - On the x86 lane it is N/N by construction on every ACCEPTED cell where it is available (Adler32 · BignumSub · Crc32), and UNAVAILABLE on
     the rest (`REGISTRATION-O60-…:411-413`).
   - It is printed beside REJECTED(TARGET) rows.
   - A hidden-input metric cannot tell an abstract spec from a transcription of the routine. The transcription reaches TARGET and no battery
     row detects it: that is the known bound of `CARD-TARGET.md:61`, *"full agreement means only not refuted"*.
4. **DESCRIPTIVE ONLY:** the landing-claim column, the agreement between the claim and the class, and the halted cells' run states.

## §D4 · REFEREE ADEQUACY: THE DEGENERATE BATTERY

**How the battery runs:**
- Before any wave fires under this design, every task's referee is driven on the members below.
- It is driven from the cut the cells receive, by a hand that did not build it.
- **Each member's reading is the §D2 CLASS from the classifier, never the referee's raw token**, so G4 and G6 read the agreement column.
- A task failing a row is EXCLUDED before the wave. The exclusion is arm-independent and decided before any cell exists.
- Every member reports its KILL MARGIN: the number of withheld inputs on which it fails, or on which agreement fails.

| # | degenerate submission | expected class | what it catches |
|---:|---|---|---|
| G1 | the stub: return 0, write nothing (O60 L5) | REJECTED | a referee that checks only the build |
| G2 | a CONSTANT equal to the answer on withheld input 0 (and, separately, the MOST COMMON answer) | REJECTED | a suite one input dominates |
| G3 | a LOOKUP routine that answers every PUBLISHED vector and returns 0 elsewhere. The published vectors come from a machine-readable `published.txt` that each generator writes beside `inputs.txt` (index, source), never from prose | REJECTED | memorisation. A task is named **G3-WEAK** when its non-published inputs share one key, one seed or one length, or carry no seeded-random content in an argument the function keys on, because a lookup plus a cheap rule could pass it |
| G4 | the reference with ONE mutation per class (add↔sub · adc↔sbb · shift direction · rotate direction · xor→or · immediate+1 · inverted jcc · inverted cmov), up to 2 sites per class | REJECTED, or EQUIVALENT shown by reading | a weak suite. A margin of 1 is named fragile |
| G5 | **salt-diet only:** the reference routine with `Submission.spec := fun … => c`, where `c` is G2's constant (a type-correct SpecShape; `True` is ill-typed) | REJECTED at TARGET | a TARGET reached by a spec that constrains nothing. The harness's planted `pre := False` is the CALL-MODULE mutant (`REGISTRATION-O60-…:371-374`) and is reported as the frame's red-first, not as G5 |
| G6 | the reference plus ONE write outside its declared footprint: a byte into each guard, a word past the stack band K, a callee-saved register left moved | REJECTED on both arms (plain via the agreement column, salt-diet at TARGET) | the class reading only executor (a) |

**Declared population limits.** These are not battery rows, and they ride with every result table.
- **Every pointer the referee passes is 64-byte aligned on every input.** `frame.py` places each region at a fixed offset, and both executors
  map it there. A routine whose misaligned-head path is wrong is ACCEPTED. Eight cards say their buffer has no alignment.
- **One task's deferred-modulo boundary rows start from a fresh state rather than a running one.** A routine wrong only on a running state is
  ACCEPTED. The regeneration is bench's, before the n = 3 run.

## §D5 · WHAT CHANGES FOR A RUN, AND WHAT DOES NOT

- **No cell changes, and no export changes.** Arms, cards, caps, the fence and the referee are untouched.
- **What is new is a CLASSIFIER over records the referee and the watcher already write:**
  - saltbench-systems `harness/analysis/classify_cell.py`: a selftest of 46 arms, one per emitted token, plus a refusal for any unmapped
    token. The end-kind population is READ from `cell-watch.sh`, never typed.
  - It lives OUTSIDE the export allowlist, so the cut's sha does not move.
  - It runs at the harvest, and it runs the referee on every halted tree.
- **Two instrument additions are OWED, and each is a referee change that would move an export:**
  - the FORM split of REFUSED-TRANSLATE (§D2);
  - a referee wall bound that emits `REFEREE-TIME`.
  - Until they exist, the classifier's conservative mappings stand: REFUSED-TRANSLATE is UNSCORABLE, and a missing CLASS line is UNSCORABLE.
    Neither is assumed done.
- Each run's release addendum names this design's freeze sha and the classifier's blob. Its result file prints §D3's rows in §D3's order.

## §D6 · THE FIRST RUN UNDER IT

**O60's first run: 20 tasks × 2 arms at n = 1.**
- At n = 1 per condition, §D3's figures are a description of the classes, never a per-task result.
- (c2) equals (c1), or is undefined.
- The n = 3 run is the first to which evidence attaches statistics.
- CRC-32's smoke cell is never quoted (O60 §Z4).

## §D7 · OWED, AND TO WHOM

- **evidence:**
  - the per-task paired reading at n = 3, for the primary pair and for cost;
  - intervals, borrowing the form of `harness/systems-v3/REGISTRATION-correctness-tables-v3-2026-10-01.md:42-43,55-61`
    (`k / n (+c censored, +u unscorable)`), so that a halt can never manufacture a sign.
- **paper:**
  - how the v3 paper's post-hoc correctness tables are described relative to this design;
  - the sentence that answers the Captain's question for a reader.
- **bench:**
  - `classify_cell.py` with an arm per token;
  - the G2–G6 drives;
  - `published.txt` per generator;
  - the regenerated boundary rows (before n = 3).
- **The OWED driven runs the refuters named (K1, K2, K6, K7):** the lock-wait COMPILE, the footprint PASS and the allowed-form translator
  refusal, each through the real referee.

## §D8 · FREEZE

- **Target:** a dated AMENDMENT frozen BEFORE the first model call of O60's 40-cell run, riding Monday 10-05's ADDENDUM 10 step.
  - It needs the re-fired refuter pass on this revision's blob.
  - It needs `classify_cell.py` with its selftest.
  - It needs the battery's readings through the classifier.
- **Default if any of the three is missing at that step:** O60's first run fires as registered and is read under O60's own registration,
  and this design first governs O60's n = 3 run.
- It never governs a run after that run's first model call.

## §D9 · THE KILL-CHECKS (revision 1's, kept for the record)

- K1 · ACCEPTED-AND-WRONG
- K2 · CLASS FROM ANYTHING BUT THE CODE
- K3 · HALT AS AN ESCAPE
- K4 · THE BIAS GUARD
- K5 · MEMORISATION (G3)
- K6 · VACUOUS SPEC (G5)
- K7 · CLASS BOUNDARIES

The full text and the verdicts are in PR #311, comment 5955729360. The re-fire on this revision uses the same seven, plus **K8: try to find
a token one of the instruments emits that the classifier maps to no class or to two.**

## §D10 · THE REFUTER PASS ON REVISION 1, AND WHERE EACH REPAIR WENT

| check | verdict | taken into |
|---|---|---|
| K1 ACCEPTED-AND-WRONG | REFUTED: PASS ignores the agreement column on all 22 tasks | §D0 · §D2 ACCEPTED requires full AGREE · G6 · the two population limits in §D4 |
| K2 CLASS FROM THE BOX'S LOAD | REFUTED: a lock-wait or timeout reads COMPILE | §D2 UNSCORABLE (rc 124/75, no Lean diagnostic) · §D1 unit under test · a referee crash caused by the tree is REJECTED |
| K3 HALT AS AN ESCAPE | REFUTED: the primary measured the stopping policy | §D3 1 primary pair · §D2 a stopped tree the referee passes is ACCEPTED |
| K4 THE BIAS GUARD | REFUTED: a = 0, UNSCORABLE spend, pooling | §D3 2 rules 1–3 · metered halted spend · §D6 |
| K5 MEMORISATION | HOLDS-WITH-LIMIT | G3 from `published.txt`, with a kill margin and the G3-WEAK label |
| K6 VACUOUS SPEC | HOLDS-WITH-LIMIT: G5 was undrivable | G5 rewritten · §D3 3 spec_strength demoted to a diagnostic |
| K7 CLASS BOUNDARIES | REFUTED: TRANSLATE, PASS riders, unmapped end kinds | §D2 mapped from EMITTED tokens · REFUSED-TRANSLATE UNSCORABLE until split · REFEREE-TIME owed |

**Refused:** K1's alternative of offsetting regions in `frame.py`. It is a referee change that moves the export the night before a fire, so it
is declared as a limit (§D4) instead.
