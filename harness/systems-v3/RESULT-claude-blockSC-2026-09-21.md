# RESULT — block SC · `claude-sonnet-5` × greenfield × spec-change × n=24 PAIRS (+6 declared REACH losses)
### bench, 2026-09-22. **⛔ THE FIRST THING TO READ IS NOT A CONTRAST, IT IS A *REACH* TABLE: two whole conditions produced no phase-2 data at all, and both are salt-diet.**
## 📌 The per-cell table is a FILE: `evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv` (24 rows, 29 columns, + SIX declared exclusions in its header).
## ⛔ Every figure below is derived from that table by `RESULT-claude-blockSC-2026-09-21-verify.py`.
## ⚖️ This document is written under **`§CLB-R`** of `AMENDMENT-claude-lane-B-2026-09-16.md`, which was **registered before this block finished and before any phase-2 contrast existed** (desk `WJ` rec (e)). Its six clauses are what shape §2 and §3.

---
# §1 · WHAT RAN
`claude-sonnet-5` × **greenfield** × **spec-change** × 5 problems × {plain, salt-diet} × 3 reps = **30 cells.**
A spec-change cell is a **PAIR**: phase 1 builds to a statement, phase 2 answers a changed spec. **Phase 2 exists only on a phase 1 that LANDED.**
```
  rows in the table   n=24         each row is ONE cell's TWO phases, metered and scored APART
  model               claude-sonnet-5, derived per cell from its own served-*.out, 24 of 24
  phase 1 run state   ENDED: LANDED 24        phase 2 run state   ENDED 24
  p1 suite            p1 PASS 22 of 24        p2 suite            p2 PASS 19 of 24
  w1_fenced           `-` for all 24 — GREENFIELD HAS NO SEED, so there is no W1 witness to fence
```
⛔ **24 PAIRS OUT OF 30 CELLS. THE MISSING SIX ARE NOT MISSING DATA — THEY ARE §2, AND THEY ARE THE RESULT.**

---
# §2 · ⛔⛔ REACH — PER ARM **AND** PER PROBLEM (`§CLB-R.2` clause 1)
**REACH = cells whose phase 1 LANDED / cells fired.** Every phase-2 figure in this document is a figure over the cells that reached phase 2, never over all cells of the condition.
```
                plain        salt-diet
  LRU           3/3          3/3
  Paxos         3/3          0/3     ⛔ a whole condition with NO phase-2 data
  FreeList      3/3          0/3     ⛔ a whole condition with NO phase-2 data
  LZW           3/3          3/3
  Crc32         3/3          3/3
  TOTAL         plain n=15   salt-diet n=9
```
⇒ 🔑 ***PER-ARM ALONE WOULD SAY "salt-diet REACHED 9 OF 15" AND INVITE THE READER TO BLAME THE ARM. THE ENTIRE LOSS IS TWO PROBLEMS.*** LRU, LZW and Crc32 salt-diet reached 3/3 — **9 of the 9 salt-diet pairs that exist come from three problems, and the two that produced nothing produced nothing at all.** That is a PROBLEM × ARM interaction, and clause 1 exists so this table is printed beside every number below rather than reconstructed by a reader who may not know to try.
⛔ **`Paxos salt-diet` and `FreeList salt-diet` ARE REPORTED AT REACH 0 OF 3 AND ARE NOT RE-FIRED** (clause 5). Re-firing a condition until it reaches n selects again on the very property that stopped it, so a topped-up n would be drawn from whichever repetitions happened to be cheap.

---
# §3 · ⛔ THE SELECTOR IS THE COST CAP, AND THE SIX LOSSES ARE DECLARED PER CELL WITH THEIR OWN SUITE RESULTS (clauses 2, 3, 4)
**`cap_unit` is `COST`. `C1_USD = 37.21` for every phase-1 cell in this block — ONE distinct value, re-verified at the object over 29 of the 30 stage receipts.** The cap's VALUE is identical across arms; its INCIDENCE is not.
```
  cell       problem   arm        phase-1 end   cost vs cap 37.21   ITS OWN withheld suite
  clbcfs01   FreeList  salt-diet  CAP-COST      37.5795             PASS 7/7
  clbcfs02   FreeList  salt-diet  CAP-COST      37.4995             FAIL 3/7
  clbcfs03   FreeList  salt-diet  CAP-COST      37.2789             FAIL 6/7
  clbcps01   Paxos     salt-diet  CAP-COST      37.6169             PASS 17/17
  clbcps02   Paxos     salt-diet  CAP-COST      37.4009             PASS 17/17
  clbcps03   Paxos     salt-diet  CAP-COST      37.3077             PASS 17/17
  incidence: 6 of 15 salt-diet · 0 of 15 plain
```
⇒ 🔑 ***A CAP THAT BINDS ONE ARM AND NEVER THE OTHER IS NOT A BUDGET, IT IS A TREATMENT*** — however even-handedly it is written, and the identical value is exactly how an arm-correlated selector hides.
⚖️ **NONE OF THESE SIX IS A PHASE-2 FAILURE** (clause 4). Each is a **REACH loss**, reported with its phase-1 end kind. `CAP-COST` is a statement about the purse; whether the code also worked is a **separate** fact, and it is the last column.
⛔⛔ **AND THAT LAST COLUMN IS WHY CLAUSE 2 SAYS *PER CELL, NEVER AS AN AGGREGATE*. THE AGGREGATE FORM HAS NOW BEEN FALSE TWICE.** Desk `WJ` recorded a true sentence on 2026-09-21 — *"all four capped cells passed their suites"* — at a moment when four had capped and four had passed. A fifth capped and **FAILED**; a sixth capped and **FAILED**. The final figure is **4 of 6**. ⇒ ***THE SUMMARY ROTTED TWICE IN TWO DAYS WHILE EVERY PER-CELL ROW STAYED TRUE, AND NOTHING ABOUT THE SUMMARY ANNOUNCED THAT IT HAD GONE STALE.***
⭐ **THE DIRECTION IS KNOWN, WHICH MAKES THIS A BOUND AND NOT A DOUBT.** The selection runs AGAINST the treatment: it can only ever REMOVE salt-diet work. **So it cannot manufacture a salt-diet advantage** — a surviving one is conservative — **but it can manufacture a null or a loss, and it can hide a real effect entirely.**
⛔ **THE CAP IS NOT CHANGED** (clause 6). Raising it mid-block is arm-correlated in the other direction and is a registration change, not a lead's act.

---
# §4 · ⛔⛔ THE PHASE-2 CAP IS NOT A PHASE-2 BUDGET — IT IS A CAP ON THE **WHOLE CELL**, AND IT IS PHASE-1 EXPENSE SELECTING A SECOND TIME
**`C2_USD = 18.60`, one distinct value across the block. `capped 3` in the table refers to three `LZW salt-diet` cells and to nothing else.** But the quantity it is compared against is **not** phase 2's spend.
⛔ **READ AT THE SOURCE** (`cell-watch.sh`, the METER branch): `cost` is `cell_meter.py "$SLUG"`, **the per-cell meter over the whole slug — every session of BOTH phases** — and phase 2 compares *that* against `C2_USD`. The phase only selects **which cap**; it never narrows **what is measured**.
```
  cell        p1_COST   p2_COST   CUMULATIVE at end-2  cap   what actually happened
  clbczs01     23.71      0.32        24.2912         18.60  ALREADY over C2 on entering phase 2
  clbczs02     21.53      0.20        22.0034         18.60  ALREADY over C2 on entering phase 2
  clbczs03     16.31      2.02        18.6136         18.60  crossed DURING phase 2, after real work
```
⇒ 🔑 ***`clbczs01` WAS CUT AFTER SPENDING 32 CENTS IN PHASE 2, AND `clbczs02` AFTER 20 CENTS.*** Their `BUILD-FAIL 0/0` is not a phase-2 outcome in any sense — **it is the signature of a suite that never ran**, on a phase that was over budget before its first meter read.
⛔⛔ **AND THE STRUCTURAL CONSEQUENCE, WHICH IS THE FINDING: `C2_USD` (18.60) IS **LOWER** THAN `C1_USD` (37.21), SO THERE IS A BAND — a phase-1 spend between them — IN WHICH A CELL PASSES PHASE 1 LEGALLY AND IS THEN GUARANTEED TO CAP AT PHASE 2 HAVING DONE NO WORK.** Measured over this block:
```
  cells in the band [18.60, 37.21)   salt-diet 2 of 9   ·   plain 0 of 15
  highest PLAIN phase-1 spend in the entire block:  $5.19   — not within $13 of the band
```
⇒ ***THE TWO SELECTORS IN §3 AND §4 ARE NOT INDEPENDENT. THEY ARE ONE QUANTITY — PHASE-1 EXPENSE — ACTING TWICE***, once as a phase-1 cut and once as a phase-2 cut, and it falls on one arm both times.
⭐ **AND IT DISPOSES OF THE OBVIOUS REMEDY, WHICH IS WHY CLAUSE 6 IS MORE THAN CONSERVATISM.** The six REACH losses of §3 each spent ≈ $37 at phase 1. **Raising `C1_USD` to let them through would not have produced a single phase-2 result**: every one of them would have entered phase 2 far above `C2_USD` and been cut at its first meter read, exactly as `clbczs01` and `clbczs02` were. ⇒ **The condition is not recoverable by loosening the phase-1 cap, and a reader reaching for that fix should know it was measured and does not work.**
⚠️ **`clbczs03` IS THE ONE THAT WAS GENUINELY CUT MID-WORK**, its CUMULATIVE cell cost crossing at `18.6136` against `18.60` — **1.4 cents over** — and it still returned `PASS 15/15`. A cap hit is not evidence that the work was unfinished, which is why the suite result travels per cell (clause 2).
✅ **ALL THREE ARE COUNTED IN NO CORRECTNESS DENOMINATOR AND ARE NAMED HERE**, and clause 3 is read as binding on **both** caps.

## ⛔⛔ §4.1 · THE INSTRUMENT DEFECT UNDERNEATH IT, AND THIS DOCUMENT'S FIRST DRAFT COMMITTED IT
The harvest's terminal marker reads, verbatim — and the number in it is the CUMULATIVE cell cost:
```
  CAP-COST cost 24.2912 of 18.60 USD (overrun printed, never clipped; T 79269505 read beside it, never the cap)
```
**`24.2912` is the CELL's cumulative cost. `18.60` is the PHASE's cap. Two different scopes in one sentence, with no word marking the change** — and that sentence is the most-quoted line in any harvest receipt.
⇒ 🔑 ***THE FIRST DRAFT OF THIS VERY SECTION PRINTED THOSE THREE CUMULATIVE FIGURES — 24.2912, 22.0034 AND 18.6136 — IN A COLUMN HEADED "phase-2 cost", WHICH IS EXACTLY THE DEFECT DESK `VV` NAMES AND EXACTLY THE ONE `RESULT-claude-blockSC-2026-09-21-verify.py` SAYS IN ITS OWN DOCSTRING IT EXISTS TO MAKE IMPOSSIBLE.***
⛔ **AND THE VERIFIER PASSED IT, CORRECTLY.** It asserts the 21 figures it derives **from the table**, and deliberately asserts no cumulative figure; these three numbers came from the **harvest marker**, a source outside its coverage. **Its green was accurate and its scope was accurately stated, and the document was still wrong.** ⇒ ***A GREEN THAT NAMES ITS OWN SCOPE HONESTLY IS STILL READ AS AN ALL-CLEAR, AND IS TRUSTED MORE FOR HAVING NAMED IT.***
✅ **WHAT CAUGHT IT: a second check, run against a DIFFERENT population — every `cell_*_at_end2` value in the table, searched for in the document's bytes.** That check is three lines, it is not the verifier, and it is the only reason this section is right. **A figure a verifier does not derive is a figure nothing checks.**

# §5 · CORRECTNESS OVER THE 24 PAIRS THAT EXIST
```
  phase 1   p1 PASS 22 of 24        phase 2   p2 PASS 19 of 24
  phase-2 suite PASS, per problem x arm, over cells that REACHED phase 2:
                plain      salt-diet
    LRU         3/3        3/3
    Paxos       2/3        —  (REACH 0/3)
    FreeList    1/3        —  (REACH 0/3)
    LZW         3/3        1/3   (2 of the 3 are the BUILD-FAILs of §4)
    Crc32       3/3        3/3
  phase-2 verdicts   V1 GREEN 20 · RED 2 · UNMEASURED 2      V2 GREEN 21 · RED 1 · UNMEASURED 2
  phase-2 regressions   0 on 22 of 24 rows; `1/7` on clbcfp01 and clbcfp02 (both FreeList PLAIN)
```
⛔ **THE ONLY MEASURED PHASE-2 REGRESSIONS IN THIS BLOCK ARE IN THE PLAIN ARM**, both FreeList, and they are what carries `V1 RED` ×2. `clbcpp03` is the single `V2 RED` (`1/8` clause tests, Paxos plain).
⚠️ **FreeList is hard for BOTH arms and it is the problem to watch, not an arm effect:** FreeList plain is `p1 PASS 1/3` and `p2 PASS 1/3` *without any cap being involved*, while FreeList salt-diet never reached phase 2 at all. ⇒ **A reader must not read FreeList's REACH 0/3 as "salt-diet cannot do FreeList" when the plain arm, unconstrained, also fails it 2 times in 3.**

---
# §6 · COST AND TOKENS, PER ARM PER PHASE — AND THE ONE FIGURE THIS DOCUMENT MAY NOT QUOTE
```
             phase 1                                    phase 2
  plain      n=15   63,850,620 T   $34.29   median $1.96     80,710,162 T   $38.77   median $2.26
  salt-diet  n=9   320,562,627 T  $101.39   median $7.33     55,323,633 T   $21.86   median $2.81
```
⛔⛔ **THESE ARE PER-PHASE FIGURES FROM EACH PHASE'S OWN HARVEST. THE `cell_*_at_end2` COLUMN IS *NOT* QUOTED ANYWHERE IN THIS DOCUMENT, AND THAT IS DESK `VV`.** That column is CUMULATIVE for a cell whose two phases ran on one pool and PHASE-2-ONLY for a cell that crossed pools — **2 of these 24 rows (`clbclp03`, `clbcls02`) carry a non-cumulative one** — so summing it across the block understates the block, and **every value in it is a believable number.** The verifier prints those two row names and asserts no cumulative figure.
⚠️ **AND THE PER-ARM COST COMPARISON AT PHASE 1 IS NOT A LIKE-FOR-LIKE ONE, BY CONSTRUCTION:** the plain column is 15 cells and the salt-diet column is 9, and the 6 missing salt-diet cells are **the six most expensive cells in the block** — each one spent past $37.21. ⇒ ***THE SALT-DIET PHASE-1 TOTAL IS A LOWER BOUND THAT EXCLUDES ITS OWN MOST EXPENSIVE MEMBERS***, which is the arithmetic form of §3's selection and is why the two numbers must never be put in a ratio.
📌 `final_T` / `final_COST` as emitted by `cell_meter` include the harness's own sandbox probe; the per-phase `p1_*`/`p2_*` columns used above come from each phase's harvest, which separates probe heads from cell heads (desk `VX`, declared in the table's own header).

---
# §7 · WHAT THIS RESULT DOES AND DOES NOT CLAIM
1. It reports **24 pairs**, names **6 REACH losses** with their costs and their own suite results, and names **3 phase-2 cap hits** with theirs. **No cell is silently excluded and no denominator is padded.**
2. It makes **no claim** about `Paxos salt-diet` or `FreeList salt-diet` at phase 2. Those conditions have **no phase-2 data**, and clause 5 forbids manufacturing some.
3. It tests **no cross-producer agreement** — there is no retention on a greenfield block — and `V1`/`V2` are **phase 2's** verdicts, not phase 1's `V1_bugs_fixed`.
4. It changes **no arm, cap, model, fence, P4 probe, scorer, tripwire or list order**, and alters no other recorded result.
5. ⚠️ **The comparison a reader most wants — "does salt-diet answer a changed spec better?" — is exactly the one this block constrains least**, because the arm-correlated selector removed its two hardest conditions before phase 2 could observe them. **The honest summary is that on the two problems where both arms reached phase 2 and neither was cut, they are level (LRU 3/3 vs 3/3, Crc32 3/3 vs 3/3); on the third the salt-diet arm was cut by its own phase-1 expense acting a second time (LZW 3/3 vs 1/3, and two of those three did no phase-2 work at all); and the two problems that would have separated them produced nothing.**
