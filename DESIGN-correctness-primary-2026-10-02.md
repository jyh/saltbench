# DESIGN: CORRECTNESS AS THE PRIMARY OUTCOME. The referee's verdict decides what a cell is before anything is counted about it.
## bench (SaltBench lead), 2026-10-02. Objectives O57 · O60. Commissioned at council 2026-10-02 (minute seat `865727d77`, item 9).
## Statistics: evidence. Text: paper. A refuter pass precedes any wave run under it.
## ⛔ DRAFT, REVISION 3. Not a registration. It binds nothing until a dated AMENDMENT freezes it (§D8), before the first model call of the run it governs.
## Revision 2 took refuter round 1 (blob `e1c16efcfd3f`, PR #311 comment 5955729360). Revision 3 takes round 2 (blob `32b0d219b6a4`, comment 5956165509).
## Every repair is mapped in §D10 and §D11.

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

**The classifier:**
- Classification is a pure function, implemented once: saltbench-systems `harness/analysis/classify_cell.py`.
- It is invoked by the harvest step (§D5), never by hand.
- Its inputs are the referee's record, target.py's own record (salt-diet), the watcher's end kind, the task's `inputs.txt` (N is
  derived from it), a FORM verdict for REFUSED-TRANSLATE, and whether this is the re-referee.
- It prints the CLASS and, beside it, the CHARGE (`ARM` or `SUNK`, §D3 2).
- A token, rider, end kind or record it does not map is a REFUSAL (exit 3). It is never a default class.

**The END decides which question the referee answers:**
- A **DECLARED** end (LANDED · DONE · EXIT-FORCED) is the subject saying it finished. It takes the referee's class.
- A **HALT** end (CAP-TOKENS · CAP-COST · CAP-WALL · POKED-OUT · STALLED) is the harness stopping the subject. The referee is asked only
  whether the stopped tree is ACCEPTED.
- An **INSTRUMENT** end (CRASH · METER-BLIND · COST-BLIND · FAILED-BOOTS · BOX-UNREADABLE · QUOTA-BLOCKED · DIALOG) is UNSCORABLE.
- The 15 kinds are read from `cell-watch.sh`'s `end_session` emitters, never from its header comment.
- **The tree the referee reads:**
  - for LANDED, the landing tag `landed-N`;
  - for every other end, HEAD of the cell's `main` at the end.
  - The harness refuses work left uncommitted. It is a reported column, never refereed.
  - The tree is always read from a COPY, never by dispatching into the cell.

| referee reading | from the record |
|---|---|
| **ACC** | `class == PASS`, the agreement field reads exactly `AGREE=N` (N = the task's withheld inputs), no harness finding |
| **REJ** | `PASS` with any footprint/ABI rider (MODEL-OUTSIDE · MODEL-CLOBBERED · MODEL-FAULT · NATIVE-OUTSIDE), and any such rider dominates every UNS rider · TESTS_FAIL · NO_SOLUTION · ASSEMBLE-FAIL · REFUSED-LINK · SCREEN · AXIOMS · COMPILE/TARGET with a non-zero rc other than 75 or 124, unless its positioned diagnostic is in a harness file (`Submission/` is the subject's, and so is `Probe.lean` for TARGET) · REFUSED-TRANSLATE whose instance the cut's `forms.py` reads OUTSIDE the allowed list |
| **UNS** | `PASS` with INCONCLUSIVE-(b) · DISAGREE · MISSING, a count ≠ N, or no agreement field · COMPILE/TARGET rc 75 (the lock's wait-abort), rc 124 on the FIRST referee run, a diagnostic in a harness file, or no target record · REFUSED-TRANSLATE on an ALLOWED form (a translator gap) or not yet split · HARNESS · no referee record on the FIRST run |
| **TREE** | on the RE-REFEREE of the same tree, with the lock measured free: rc 124 again, or no record again (the tree crashes or hangs the referee). It is the subject's |

| end | ACC | REJ / TREE | UNS |
|---|---|---|---|
| declared | **ACCEPTED** | **REJECTED** | **UNSCORABLE**, charge SUNK |
| halt | **ACCEPTED** | **HALTED** | **UNSCORABLE**, charge ARM (a halt's spend is always the arm's) |
| instrument | **UNSCORABLE**, charge SUNK | | |

**Re-referee and re-fire are different acts:**
- The harvest re-referees ONCE: on rc 124, and on no record.
- A cell is RE-FIRED only for a zero-spend instrument end (FAILED-BOOTS, QUOTA-BLOCKED, BOX-UNREADABLE at boot), per lane B §CLB-R.2 5
  (`harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md:1319`: no top-up re-fires).
- Every other UNSCORABLE is reported, by name, at the n it reached.

## §D3 · THE OUTCOME HIERARCHY

### 1. THE PRIMARY: a pair per arm per task, printed together
- **(i) THE DECLARED RATE:** ACCEPTED-declared / (ACCEPTED-declared + REJECTED). It is the rate among cells whose subject said it had
  finished.
  - Halted trees that pass are printed BESIDE it as `+s accepted at the cap`, never inside it.
  - With no declared cell, it prints `NO ENDED CELL`.
- **(ii) THE PER-ATTEMPT RATE:** every ACCEPTED / (ACCEPTED + REJECTED + HALTED). This is the rate at the registered cap, and a floor on the
  rate at any larger budget.
- **When (i) and (ii) order the arms differently, the row prints `DISCORDANT`, and no sentence quotes (i)'s order.**
  - The reason: the arm texts instruct different declaration policies (salt-diet lands only on a clean `VERIFIED`), so declaring is
    arm-correlated by construction. (i) alone measures a stopping policy. (ii) charges every halt to the arm that produced it.
- Both are reported per task first. A pooled figure appears only beside the per-task table, with UNSCORABLE `u` in the same row.

### 2. COST: one row that cannot be printed without its denominators
- **The row, per arm per task:** `ACCEPTED a · REJECTED r · HALTED h · UNSCORABLE u`, then three figures:
  - **(c0)** spend(a + r + h + charged u) / (a + r + h + charged u): defined wherever any cell was charged;
  - **(c1)** the mean spend of the a accepted cells;
  - **(c2)** spend(a + r + h + charged u) / a.
- **Rule 1, CLASS IS NOT CHARGE.**
  - A cell charged `ARM` enters the spend whatever its class: every halt end, and every declared end that reads ACC or REJ.
  - A cell charged `SUNK` is excluded and printed as `sunk: $x over u cells (instrument k · unattributed m)`: every instrument end, and every
    declared end whose reading is UNS.
  - A cell the meter could not price prints `VOID`, never `$0`.
- **Rule 2:** when `a = 0`, (c1) and (c2) print `NO ACCEPTED CELL (spend $x over r + h cells)`. They are never 0, never blank and never
  dropped, and no ratio or sign is formed from them. When `r + h = 0` as well, the row prints `NO SCORABLE CELL (u cells, sunk $x)` and is
  never counted against an arm.
- **Rule 3:** no cost figure is pooled across tasks. evidence's paired readings (§D7) are two, and each is labelled:
  - **(c0) paired with (ii)** over every task with a verdict;
  - **(c2) paired** over tasks where both arms have `a > 0`, labelled *conditional on acceptance*, with each arm's spend on the excluded
    tasks printed beside it in the same act.
- **A halted cell's spend enters as METERED.** It is never clipped to the cap. This overrides lane B §Q6 6's "at the cap"
  (`harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md:229`).
- **REFUSED-TRANSLATE is arm-asymmetric by toolbox.**
  - Plain meets an operand-form refusal at the referee.
  - Salt-diet meets it inside the cell, at its own TRANSLATE stage.
  - Each row prints `refused-translate: $x over k cells` per arm.

### 3. DESCRIPTIVE ONLY
- The declaration verb.
- The landing claim against the class.
- The halted cells' run states.
- **spec_strength.** It is a DIAGNOSTIC printed beside REJECTED(TARGET) rows, and it is not an outcome.
  - On the x86 lane it is N/N by construction on every ACCEPTED cell where it is available (Adler32 · BignumSub · Crc32) and UNAVAILABLE on
    the rest (`REGISTRATION-O60-…:410-413`).

## §D4 · REFEREE ADEQUACY: THE DEGENERATE BATTERY

**How the battery runs:**
- Before any wave fires under this design, every task's referee is driven on the members below.
- It is driven from the cut the cells receive, through the classifier with end `battery`, by a hand that did not build it.
- **A member's reading is the §D2 class AND, beside it, the referee's token, `tests=` and the agreement field**, wherever the row names a
  gate or a column (G5 names TARGET; G4 and G6 read agreement).
- A member that reads UNSCORABLE is re-driven, and it is never counted as a pass or a failure. A task on which a member cannot be driven to a
  verdict is named **G-UNDRIVEN** and excluded.
- A task failing a row is EXCLUDED before the wave. The exclusion is arm-independent.
- **The amendment prints the class per member per task.**
  - Margins, published shares, G3-WEAK's basis, and every limit that describes how a withheld set was built stay in the private tree beside
    the drive.
  - They are printed with the result file after the run, because this repository is public before it.

| # | degenerate submission | expected reading | what it catches |
|---:|---|---|---|
| G1 | the stub: return 0, write nothing | REJECTED (TESTS_FAIL) | a referee that checks only the build |
| G2 | a constant equal to the answer on withheld input 0, and separately the most common answer | REJECTED | a suite one input dominates |
| G3 | G1 plus a lookup that answers every PUBLISHED vector. The vectors are read from a machine-readable `published.txt` (index, source) that each generator writes; it is a FLOOR, since no file enumerates a model's weights | REJECTED, margin "at least M" | memorisation. **G3-WEAK** = the driver can NAME a rule that answers the non-published inputs without computing the function, and writes it beside the label. A G3-WEAK task is regenerated before the wave, or rides as a declared limit |
| G4 | the reference with ONE mutation per class (add↔sub · adc↔sbb · shift · rotate · xor→or · immediate+1 · inverted jcc · inverted cmov), up to 2 sites per class | REJECTED, or EQUIVALENT shown by reading. The margin is read from the class AND the agreement column | a weak suite. A margin of 1 is named fragile |
| G5 | **salt-diet only:** the reference routine, `Submission.spec := fun … => c` (c = G2's constant in the SpecShape codomain), and NO `Submission.correct` | `tests=PASS`, `AGREE=N`, token TARGET with `target_unknown = [Submission.correct]` ⇒ REJECTED. A REJECTED at COMPILE, SCREEN or AXIOMS is a MIS-BUILT member | a TARGET reached by a spec that constrains nothing. The harness's planted `pre := False` is the call module's own red-first, not G5 |
| G6 | the reference plus ONE write outside its footprint: a byte into each guard, a word past the stack band K, a callee-saved register left moved | REJECTED on both arms | a class that reads only executor (a) |
| G7 | the reference with each pointer argument replaced by its frame constant | **expected ACCEPTED on plain, REJECTED(TARGET) on salt-diet.** Its reading is the MEASURED size of the limit below, not a pass/fail | the constant-pointer limit, measured rather than asserted |

**Declared limits.** They ride with every result table, and they are printed by `classify_cell.py --limits` and beside each row.
- **Every pointer the referee passes is a per-task CONSTANT.** It is the same address on every input, 64-byte aligned, and the cell's own
  `tools/frame.py` states it; `bin/rt` confirms it locally.
  - A plain routine that ignores its pointer arguments, or whose misaligned-head path is wrong, is ACCEPTED. The first is REJECTED at TARGET
    on salt-diet, so the primary pair is biased toward PLAIN by exactly this class, and every result table says so.
  - The remedy, a per-frame window offset in `frame.py` identical in both executors, is a referee change. It is named for the n = 3 run.
- **Reads are observed by nothing.** Neither executor nor the Target sees a read outside the declared regions. A routine whose over-read does
  not reach its result is ACCEPTED on both arms. Two cards admit a bounded over-read by contract; no other card does.
- **Footprint checks are final-state.** A write outside the footprint that is undone before the return is ACCEPTED on both arms.
- **A spec that transcribes the routine** reaches TARGET and scores N/N, and no battery row detects it (`CARD-TARGET.md:61`, *"full agreement
  means only not refuted"*). Its detector, the kernel-equality spec method, is owed (§D7).
- **`tests=FAIL(native-crash)` is REJECTED whatever killed the native executor.** The kill's rc is not read.
- The population limits that describe one task's withheld set are in the private tree (see "How the battery runs").

## §D5 · WHAT CHANGES FOR A RUN, AND WHAT DOES NOT

- **Arms, cards, caps and the fence are untouched.**
- **The referee changes in ONE place**, and that move is declared, with its own red-first:
  - `target.py`'s `run()` now starts the build in its own session and, on timeout, kills the whole process GROUP.
  - The old form left the `lake` grandchild holding the FLEET-WIDE build lock (refuter round 2, K2; the helm's order of 2026-10-02 08:58:56).
  - So the export moves, and ADDENDUM 10 names the re-cut.
- **THE HARVEST STEP — a freeze condition (§D8). It exists before the first model call, or this design does not govern the run.** For every
  cell it:
  1. copies the tree §D2 names;
  2. runs `referee_o60.sh` on the copy, into a fresh work dir, after removing any prior record so a stale record cannot be read as current;
  3. runs the cut's `forms.py` on the retained `sub.elf` when the token is REFUSED-TRANSLATE;
  4. classifies, re-referees once where §D2 says to, and writes one row per cell.
  - The result table REFUSES to print while any non-instrument cell has no referee record.
- **OWED, each a referee change that would move an export again:**
  - a referee wall bound that emits `REFEREE-TIME` (`translate_and_test.sh` runs the model executor with no bound);
  - `check_x86.py` copying `build_rc`/`probe_rc` into its own record;
  - a stat-before-open screen that emits `TREE-UNREADABLE`.
  - Until they land, the classifier's conservative and re-referee rules above stand.

## §D6 · THE FIRST RUN UNDER IT

**O60's first run: 20 tasks × 2 arms at n = 1.**
- At n = 1 per condition, §D3's figures are a description of the classes, never a per-task result.
- (c2) equals (c1) when the one cell is accepted. Otherwise rule 2 prints `NO ACCEPTED CELL`.
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
  - `classify_cell.py` (done: v2, selftest 69/69);
  - the harvest step (§D5);
  - the G2–G7 drives through the classifier;
  - `published.txt` per generator;
  - the regenerated boundary rows (before n = 3).
- **bench, owed instruments (each moves an export, so after O60's first run unless a cut is re-made for it):**
  - `REFEREE-TIME`;
  - `check_x86.py` copying `build_rc`/`probe_rc`;
  - `TREE-UNREADABLE`;
  - the per-frame window offset;
  - an instrument tell for POKED-OUT/STALLED on the x86 kit (`.rt/lean-build.log`'s mtime);
  - the kernel-equality spec method (`CARD-TARGET.md:61`).
- **systems (the helm's order of 08:58:56):** a census of every caller that wraps saltbuild in a timeout, and a saltbuild-side group guard.
- **The OWED driven runs the refuters named:**
  - the lock-wait COMPILE;
  - the footprint PASS;
  - the allowed-form translator refusal;
  - the constant-pointer routine (G7).
  - Each goes through the real referee.

## §D8 · FREEZE

- **Target:** a dated AMENDMENT frozen BEFORE the first model call of O60's 40-cell run, riding Monday 10-05's ADDENDUM 10 step.
- **It needs all five of these:**
  1. the re-fired refuter pass on this revision's blob;
  2. `classify_cell.py` at a named blob, with its selftest;
  3. THE HARVEST STEP (§D5) at a named blob, driven once end to end on a real cell record;
  4. the battery's readings through the classifier;
  5. `target.py`'s group-kill in the cut (red-first, `test_target_run_group.py`).
- **Default if any is missing at that step:** O60's first run fires as registered and is read under O60's own registration, and this design
  first governs O60's n = 3 run.
  - Item 5 is ALSO a release condition of the fire itself (the helm, 08:58:56). It is not only this design's.
- It never governs a run after that run's first model call.

## §D9 · THE KILL-CHECKS (revision 1's, kept for the record)

- K1 · ACCEPTED-AND-WRONG
- K2 · CLASS FROM ANYTHING BUT THE CODE
- K3 · HALT AS AN ESCAPE
- K4 · THE BIAS GUARD
- K5 · MEMORISATION (G3)
- K6 · VACUOUS SPEC (G5)
- K7 · CLASS BOUNDARIES

The full text and the verdicts are in PR #311, comment 5955729360. The re-fires use the same seven, plus **K8: try to find
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

## §D11 · THE REFUTER PASS ON REVISION 2 (PR #311, comment 5956165509), AND WHERE EACH REPAIR WENT

| check | verdict | taken into |
|---|---|---|
| K1 | REFUTED: pointers are per-task CONSTANTS the cell can read; reads are unobserved; footprint checks are final-state | §D4 G7 and three declared limits |
| K2 | REFUTED: "no diagnostic ⇒ instrument" is the wrong tell, and the rc exists one layer down; the orphaned lake holds the fleet lock | §D2 rc rules from target.json · TREE on the re-referee · §D5 `target.py` group-kill, landed red-first (e34db16, read by kent) |
| K3 | REFUTED: `declare done` was a free escape into HALTED; nothing referees halted trees | §D2 DECLARED ends take the referee's class · §D3 1 (i) is the declared rate, with DISCORDANT · §D5 the harvest step is a freeze condition |
| K4 | REFUTED: an unreadable halt left the charge; the re-fire selected; cost had no unconditional form | §D3 2 CLASS IS NOT CHARGE · (c0) · re-fire only zero-spend instrument ends |
| K5 | HOLDS-WITH-LIMIT | G3 is a FLOOR · G3-WEAK by a named rule · withheld-shape figures move to the private tree |
| K6 | HOLDS-WITH-LIMIT: G5's reading needs its token, not only its class | §D4 the member reads class, token, `tests=` and agreement · G5 rewritten · spec_strength is descriptive |
| K7 | REFUTED: DONE and EXIT-FORCED; a diagnostic outside `Submission/`; REFUSED-TRANSLATE splittable now | §D2 diagnostic path · `--forms` · end kinds from the emitters |
| K8 | REFUTED: the crash-on-tree clause had no instrument; unreadable records | §D2 TREE by re-referee · an unreadable record REFUSES · SCREEN(spec) is not a token |
