# DESIGN: CORRECTNESS AS THE PRIMARY OUTCOME. The referee's verdict decides what a cell is before anything is counted about it.
## bench (SaltBench lead), 2026-10-02. Objectives O57 · O60. Commissioned at council 2026-10-02 (minute seat `865727d77`, item 9).
## Statistics: evidence. Text: paper. A refuter pass precedes any wave run under it.
## ⛔ DRAFT. This is not a registration and binds nothing until a dated AMENDMENT freezes it (§D8), before the first model call of the run it governs.

The Captain's question at the table: *"How is it that we know the agent doesn't just submit an arbitrary program, like a constant function?
We should have put correctness in as a primary criterion, so let's commission a design phase."*

---

## §D0 · WHAT IS TRUE TODAY, AND WHERE IT FALLS SHORT

**The direct answer is that a constant function fails every referee we run.** It is the reason the population's stub exists:
- O60's builder seeds every cell with a stub whose body is `xor eax, eax; ret`, a function that returns 0
  (saltbench-systems `harness/systems-x86/x86_cell_build.py:86-88`).
- O60's release condition L5 requires that stub to read TESTS_FAIL on every task. It read TESTS_FAIL on 22 of 22
  (`harness/systems-x86/REGISTRATION-O60-scalar-population-2026-10-01.md:172,441`).

The Rust referee runs a withheld suite after the build. A build alone never passes. For CRC-32 that suite covers:
- the published check value and the vectors;
- long inputs and all 256 byte values;
- every card length against a bit-serial reference;
- repeated calls;
- seeded random inputs.

(saltbench-systems `harness/systems-v3/referee_v3.py:52,356`; `tasks/systems-v3/Crc32/G/withheld/tests/driver_lib.rs:146-273`.)
The x86 referee requires native execution and the x86lean model to agree on all 82 withheld inputs
(`harness/systems-x86/AMENDMENT-x86-crc32-poc-2026-09-25.md:26-29`, item 8).

**What is missing is the ORDER, not the referee.** No registration in this repository makes the referee's verdict the primary outcome:
- Matrix #1 was registered and priced as a COST experiment. Its referee was never invoked at pricing time, and its correctness pass
  was declared post hoc (`harness/systems-v3/PRESPEC-posthoc-correctness-matrix1-2026-09-09.md:11-18`; `paper/saltbench-v1.tex:84,132`).
- The v3 correctness tables are post hoc and descriptive (`harness/systems-v3/REGISTRATION-correctness-tables-v3-2026-10-01.md:6-9`).
- O4 #1 and O60 register no pass-rate prediction (`AMENDMENT-x86-crc32-poc-2026-09-25.md:83`; `REGISTRATION-O60-…:128`).
- Lane B came closest. It puts VERIFIED FIRST, but it reports cost and pass rate as two separate results
  (`harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md:215,232`), so a cost figure can still be read over cells that did not pass.

⇒ **A reader of a cost table today cannot tell, from the table, whether the cheap cells were the correct ones.** That is the defect
this design removes. *"The agent submitted a constant function"* is one way to land in that table, and *"the agent submitted a
routine that is wrong on one input class"* is another.

---

## §D1 · THE PRINCIPLE

***A cell is CLASSIFIED by the referee before it is MEASURED by anything else.*** Every other quantity is a property of a CLASS of cells,
and is never pooled across classes. Cost, tokens, wall time, turns, the landing claim and spec_strength all fall under this rule.

## §D2 · THE FOUR CLASSES (exhaustive and exclusive, decided by the referee and the harness, never by the subject)

| class | meaning | decided by | sources it absorbs (existing vocabulary) |
|---|---|---|---|
| **ACCEPTED** | the referee ran to the end and returned PASS | referee | PASS · RESOLVED · FULL PASS |
| **REJECTED** | the referee ran and returned a failing verdict | referee | TESTS_FAIL · COMPILE · VERIFY_FAIL · GUARD · SPEC_ALTERED · NO_SOLUTION · TRANSLATE · SCREEN · TARGET · AXIOMS · NO-BUILD · INTERFACE-MISS |
| **HALTED** | the cell was stopped by a registered limit before the subject finished; the referee's verdict on the halted tree is reported beside the class and never moves the cell out of it | harness | CAP-COST · CAP-WALL · CAP-TOKENS · STALL · TURNS-CUT · CELL-KILLED · MEM-CAP · CENSORED |
| **UNSCORABLE** | the instrument failed, not the subject | harness or referee | NOT-SCORED(HARNESS) · REFEREE-FUEL · FAILED-BOOT · VOID(*) · VOID_NO_BRIEFING · VOID_NOT_SCORABLE · DISCARD(503) |

- **The subject's own claim never classifies a cell.** LANDED, a `LANDING.md`, and `false_done_claims: 0` are reported as a column
  beside the class and never decide it (this repo's `CLAUDE.md`: *"A landing is the subject grading itself"*).
- **A REJECTED cell is never re-tried into ACCEPTED.** A re-run is a new cell.
- ⚠️ **HALTED is a class, never a failure and never a floor on the pass rate.** A halted cell enters neither the numerator nor the
  denominator of §D3's primary. Its own rate (HALTED / all fired) is reported beside the primary in the same row.
  - *Why:* folding halts into REJECTED would make a cap a correctness verdict. On O60's largest tasks the cap is expected to bind
    salt-diet first (`REGISTRATION-O60-…:126`), so the fold would bias against one arm.
  - ⚠️ **This is a deliberate change from lane B**, where *"a capped cell's pass result is a floor and its cost enters at the cap"*
    (`harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md:229`). A floor is a cost rule. Under this design a halted cell has no
    correctness verdict, so it contributes no floor to the primary. Its spend is still charged in §D3 3's unconditional figure.
- **UNSCORABLE cells are re-fired** where the instrument is repaired before the run closes. Otherwise they are counted and named,
  and never imputed.

## §D3 · THE OUTCOME HIERARCHY

1. **PRIMARY: the acceptance rate, per arm, per task** = ACCEPTED / (ACCEPTED + REJECTED).
   - It is reported per task first, because the tasks are not exchangeable (O60 §Z6 1).
   - The pooled figure is printed only beside the per-task table.
   - The HALTED rate and the UNSCORABLE count ride in the same row.
2. **SECONDARY, READ OVER ACCEPTED CELLS ONLY:** cost, tokens, wall time and turns per accepted cell; spec_strength for accepted
   salt-diet cells.
3. **THE SELECTION-BIAS GUARD, which is the half of "cost over accepted cells" that a reader will skip.**
   - If the arms' acceptance rates differ, the two cost distributions describe different populations of task-attempts.
   - An arm that only succeeds on easy attempts looks cheap.
   - ⇒ **Every per-accepted cost figure is printed beside COST PER ACCEPTED CELL OVER ALL FIRED CELLS** = total spend of the arm on
     that task / number accepted. That figure is unconditional and charges failures and halts to the arm that produced them.
   - Neither figure is printed without the other.
4. **DESCRIPTIVE ONLY:** the landing-claim column, the agreement between the subject's claim and the referee, and the halted cells'
   referee verdicts.

## §D4 · REFEREE ADEQUACY, WHICH IS THE CAPTAIN'S QUESTION MADE INTO A GATE

The four classes are only as good as the referee's ability to REJECT. So before any wave fires under this design, every task's
referee passes a **degenerate battery**.

- The battery is driven from the cut the cells receive, by a hand that did not build it.
- Every member must read REJECTED, and the reference must read ACCEPTED.
- A task failing any row is EXCLUDED before the wave. The exclusion is arm-independent and decided before any cell exists.

| # | degenerate submission | what it catches |
|---:|---|---|
| G1 | the stub: return 0, write nothing (exists: O60 L5) | a referee that only checks the build |
| G2 | return a CONSTANT equal to the reference's output on the FIRST withheld input; for a WRITE task, write that output's bytes | a referee whose first input dominates |
| G3 | a LOOKUP routine that returns the right answer on every PUBLISHED vector of the function (the card's own vectors and the upstream test vectors) and 0 elsewhere | **memorisation of public vectors.** The withheld inputs must include inputs outside every public vector, and G3 proves they do |
| G4 | the reference with ONE mutation in each registered mutation class (constant tweak, off-by-one bound, wrong shift, dropped carry, swapped operands), one per class, where the form exists in that routine | a weak suite. Report the KILL MARGIN (inputs failing per mutant). A margin of 1 is a fragile pass and is named |
| G5 | **salt-diet only:** a reference routine whose Lean `spec` is vacuous (`True`, or `pre := False`); the existing planted-mutant refusal (`REGISTRATION-O60-…:360-374`) | a TARGET reached by an empty specification. ⚠️ Because spec_strength is a METRIC and not a gate, G5 must show the BEHAVIOURAL suite still decides ACCEPTED. A vacuous spec on a correct routine is ACCEPTED by behaviour with spec_strength 0, and that is reported, never hidden |

- G1 exists, and G5 exists in part.
- G2 to G4 are new. They are cheap: every member is generated mechanically from the reference and the vectors, at zero model spend.
- For the Rust (v3) families, G1 to G4 map onto the existing mutant set and `test_strength.py`'s margin
  (`harness/systems-v3/RESULT-hidden-test-strength-v3.md`). The new rows there are G2 and G3.

## §D5 · WHAT CHANGES FOR A RUN, AND WHAT DOES NOT

- **No cell changes.** Arms, cards, caps, the fence and the referee are untouched. This design changes what is COUNTED and in what
  order, plus a pre-wave referee check at zero model spend.
- ⇒ It can freeze in front of a run that is already staged without moving that run's export.
- Each run's release addendum names this design's freeze sha, and its result file prints §D3's table in §D3's order.

## §D6 · THE FIRST RUN UNDER IT

**The x86 lane's scalar population (O60), whose first run is 20 tasks × 2 arms at n = 1.**
- Its referee already has G1 and the two-executor agreement.
- G2, G3 and G4 are generated from the same withheld sets and references bench holds.
- CRC-32's smoke cell is never quoted (O60 §Z4), so it stays outside the table.
- ⚠️ At n = 1 per condition, §D3's primary is a population DESCRIPTION, never a per-task result. The first run reads the shape of the
  classes. The n = 3 run is the first to which evidence attaches statistics.

## §D7 · OWED, AND TO WHOM

- **evidence (statistics):**
  - the per-task paired reading at n = 3;
  - how HALTED is reported when it is arm-correlated;
  - whether the pooled acceptance rate gets an interval or stays descriptive;
  - the selection-bias guard's exact form (§D3 3).
- **paper (text):**
  - how the v3 paper's existing post-hoc correctness tables are described relative to this design;
  - the sentence that answers the Captain's question for a reader.
- **refuter (non-author, before any wave):**
  - try to construct a submission that is ACCEPTED and wrong;
  - try to construct a cell whose class depends on anything the subject wrote other than the code under test.

## §D8 · FREEZE

- **Target:** a dated AMENDMENT frozen BEFORE the first model call of O60's 40-cell run. Monday 10-05's chain has an ADDENDUM 10
  step before the smoke pairs, so the freeze rides there.
- **The default if the refuter pass has not returned by then:** O60's first run fires as registered and is read under O60's own
  registration (descriptive). This design first governs O60's n = 3 run.
  - It never governs a run after that run's first model call. Writing it afterwards would make it post hoc, which is the defect it
    exists to remove.
