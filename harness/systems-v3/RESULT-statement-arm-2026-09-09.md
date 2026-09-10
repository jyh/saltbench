# RESULT — THE STATEMENT ARM ON THE PILOT (AMENDMENT statement-arm-pilot 2026-09-09)
## **COMPLETE: wave 1 (Crc32, LRU) and wave 2 (FreeList) both landed, harvested and scored. 18 of 24 cells. Nothing is running.**
Every number is derived from the verdicts table beside it and from each cell's harvested `METER.txt`
(§23(e)). ⛔ **`METER.txt` and "the ARCHIVE" are ONE source, not two** — `~/harvest-v3/<cell>-*/METER.txt`
is the archive. The header and §3 name the same file, and `paper` was right to ask which was meant.
⛔ **The price is `final_COST`, never `ctl/post-end-1.tsv` field 3 (`at_end_COST`).** The gap is spend
during the §31 grace, after `END` is declared. No figure in this file has ever come from `post-end`.

## §1 · WHAT FIRED, AND WHAT DID NOT
```
  18 of 24 cells fired.  Crc32 x6 + LRU x6 (wave 1) + FreeList x6 (wave 2).
  PAXOS x6 NEVER FIRE, and that is a RESULT rather than a shortfall:
    an arm-neutral formal statement CANNOT EXIST for a proof-obligation task -- Paxos's
    extracted statement names `proof fn` because its specification IS proof obligations, and
    the rendered REQUIREMENTS.md is read by the PLAIN arm too. The harness's neutrality gate
    refuses those cells. A plain+statement Paxos cell would be a control told to write proofs.
```

## §2 · CORRECTNESS — pre-registered for these cells by `PRESPEC …437ea70`
```
  wave 1 (12 cells): PASS 12
  wave 2 ( 6 cells): PASS  6   (TESTS 7/7 each, rc 0)
  ------------------------------------------------------------
  18 of 18 LANDED cells PASS   ·  0 NO-BUILD  ·  0 MISSING-INPUT  ·  0 CAP-COST
```
⇒ **Every statement-arm cell passes its withheld suite.** ⛔ A PASS is *the withheld suite did not fail
it*, and that suite's 44/44 mutant score is a **CEILING, not a strength**.

## §3 · COST, from the ARCHIVE (`METER.txt`)
```
  problem   arm            n   cells                        median
  Crc32     plain         3   $6.36 $6.66 $8.64           $6.6600
  Crc32     salt-diet     3   $5.65 $6.25 $8.56           $6.2500
  FreeList  plain         3   $17.72 $18.26 $18.42        $18.2600
  FreeList  salt-diet     3   $21.18 $27.84 $29.00        $27.8400
  LRU       plain         3   $8.92 $9.36 $15.12          $9.3600
  LRU       salt-diet     3   $13.65 $14.24 $18.65        $14.2400
  LZW       plain         3   $9.82 $10.24 $11.39         $10.2400   (pilot)
  LZW       salt-diet     3   $15.34 $18.54 $22.53        $18.5400   (pilot)
```

## §4 · ⛔⛔ THE GOLD PAIR — THE SIGN IS NOT UNANIMOUS AND NO MAGNITUDE SURVIVES
```
  problem    (e)/(d) premium      bare premium      change
  Crc32     0.9384x              1.1610x           -0.2226   attenuated, PAST 1
  FreeList  1.5246x              2.8070x           -1.2824   attenuated
  LRU       1.5214x              1.2826x           +0.2388   AMPLIFIED
  LZW       1.8105x              1.3749x           +0.4356   AMPLIFIED
  3 of 4 above 1   p = 0.3125   -> NO VERDICT
```
⚠️ **Bare premiums are reading A** (the continuity reading, smoke cells IN). FreeList's bare premium is
the one figure that moves between readings: **2.8070x reading A, 2.8879x reading B.** The gold-pair
column is identical under both readings — no statement-arm condition contains a borrowed smoke cell.

⇒ 🔑 ***THE BARE ARMS WERE 5 OF 5 ABOVE 1. THE STATEMENT ARM IS NOT UNANIMOUS:*** `Crc32` comes in
**BELOW 1** at 0.9384x.
⇒ 🔑 ***AND THE CHANGE IS NOT UNIFORM IN SIGN — two attenuated, two AMPLIFIED.*** In the statement arm
**both** sides receive the statement, so a shared-input (dose) account requires attenuation toward 1
**everywhere**. Two problems moved the other way. That refutation was recorded by `systems` before
FreeList landed and is not new here; FreeList's cell adds a second attenuation and does not disturb it.

⛔⛔ **THE FINDING WAVE 2 ADDS, AND IT IS THE COSTLIEST ONE IN THIS FILE:**
```
  registered resolvable floor (G3, sd(ln cost)=0.3046, n=3)      2.0072x
  BARE arm       CLEARS the floor on 2 of 5 problems   FreeList 2.8070x · Paxos 2.4306x
  STATEMENT arm  CLEARS the floor on 0 of 4 problems   the largest is LZW at 1.8105x
```
**FreeList is the problem that carried the bare arm's largest magnitude, and it is the problem whose
premium the statement arm cuts most (−1.2824).** ⇒ ***THE STATEMENT ARM RESOLVES NO MAGNITUDE AT ALL,
WHERE THE BARE ARM RESOLVED TWO.*** That is a **WEAKER** position than the bare arm's, not a friendlier
one, and it is the direction a reader looking for support will most want to misread.

## §4b · ⚖️ THE ONE REGISTERED PREDICTION ON THIS AXIS, SCORED — AND THE OUTCOME LANDS IN ITS GAP
`systems` registered this before FreeList's cells landed, after retiring an earlier prediction of its
own whose sign was inverted. Quoted verbatim from the record:
> **FreeList's statement-arm premium comes in ABOVE LZW's 1.8105× (the selection account).**
> **Refuted** at or below LRU's 1.5214×. **Strongly refuted** below 1, which is what a dose account needs.
```
  the outcome            FreeList (e)/(d) = 1.5246x
  the CLAIM              "ABOVE 1.8105x"        -> FALSE.  1.5246 < 1.8105 by 0.2859
  its "refuted" band     "at or below 1.5214x"  -> NOT MET.  1.5246 > 1.5214 by 0.0032
  its "strongly refuted" "below 1"              -> NOT MET
```
⇒ **The claim is FALSE: the premium did not come in above LZW.** ⛔ **But the registration's own severity
vocabulary has no word for where it landed** — the interval `(1.5214x, 1.8105x)` is named by neither
branch, and the outcome sits **0.0032 inside it**, three thousandths above the refutation threshold.
⇒ 🔑 ***A PREDICTION THAT NAMES A CLAIM AND TWO SEVERITY BANDS, WITH A GAP BETWEEN THEM, IS FINISHED BY
WHOEVER SCORES IT — AND WHOEVER SCORES IT WILL SUPPLY THE MISSING LABEL FROM THEIR OWN EXPECTATION.***
**This file reports the number and the miss and supplies no label.** The registration is `systems`' and
so is any grading of it.
⛔ **AND IT WOULD NOT HAVE DISCRIMINATED EITHER WAY.** `A3.3` registered, before these cells fired, that
statement size and bare premium are both downstream of problem difficulty, so **the dose account and the
selection account make the same prediction for every outcome FreeList can produce.** A sixth problem that
ranks with the other five adds a data point and no information. **That limit was registered in advance
and it still binds.**

## §5 · ⛔ WHAT THIS CANNOT DELIVER, REGISTERED BEFORE THE FIRST CELL FIRED
```
  one-sided sign test, k of k:  k=3 p=0.1250 · k=4 p=0.0625 · k=5 p=0.0312
```
**k = 5 is the minimum for significance and Paxos is one of the five.** ⇒ **THE GOLD PAIR CANNOT REACH A
VERDICT IN THIS DESIGN.** With `Crc32` below 1 the best attainable at k = 4 was **3 of 4, p = 0.3125** —
and **3 of 4 is exactly what landed.** ⇒ **The arm delivered its own ceiling, and the ceiling is not a
verdict.** These cells buy magnitudes, correctness verdicts and a fourth problem. They cannot buy a
verdict, and that was registered in ADDENDUM 2 before any of them fired.

## §6 · ⛔ THE CAVEAT THAT TRAVELS WITH EVERY NUMBER HERE
**BUDGET STOPS ARE ARM-CORRELATED.** In the pilot all three CAP-COST cells were `salt-diet` and none
were `plain`; the correctness column scored **18 plain against 12 salt**. The dropped salt cells are the
ones that ran long enough to hit the cap — **the hard ones** — so **the treatment arm's pass rate is
biased UP by construction.**

## §7 · ⭐⭐ THE REGISTERED CAP PREDICTION FAILED IN THE OPEN, ON THE FULL n IT DECLARED
`§3` registered `C1_USD = 37.21` and, against the pilot's own tracked medians, declared **FreeList's
diet+statement cells EXPECTED TO CAP** (diet-bare median **$37.60**, max **$37.95**, both above the cap).
`A2.3` restated it unchanged. Paxos never fires, so **FreeList is the only problem on which it can be
scored at all.** The default-if-silent branch — **CAP UNCHANGED** — was taken. The outcome:
```
  sf04free  $29.00   UNDER     sf05free  $21.18   UNDER     sf06free  $27.84   UNDER
  the cap was NOT raised.  worst cell is 78% of it.  0 CAP-COST cells in 18.
```
⇒ **THE PREDICTION FAILED, ON ALL THREE CELLS, AND ITS DIRECTION IS THAT THE CELLS CAME IN UNDER.**
It is recorded here as a **failure** and reported as a **result**, per `A4.2`'s second branch, which was
registered while two of these three cells were still running. ⛔ **A registered prediction that fails is
a result of this instrument, not an embarrassment to be dropped.**

### §7b · ⛔⛔ THE COMPARISON THIS FAILURE INVITES IS NOT THE REGISTERED READING (`A4.3`)
The arithmetic invites *"the statement made the treatment's dearest condition cheaper"* — FreeList diet
went from a **bare** median of `$37.60` to a **statement** median of `$27.84`.
⛔ ***THAT IS A BARE-vs-STATEMENT COMPARISON. THE REGISTERED READING OF THIS ARM IS (d) vs (e) — the two
STATEMENT conditions on the same problem*** (`§5`). They are different comparisons over different
populations **and they are not pooled.** The registered reading for FreeList is `§4`'s **1.5246x**.
**What may be said of the bare-vs-statement line, and it is deliberately narrow:**
1. **One problem at `n = 3`** — an OBSERVATION, not a direction. The `2.0072x` resolvable floor applies
   to it exactly as to every other premium in this file.
2. Admissible **only because the cap was NOT raised**, so both sides were measured under the same budget.
   ⛔ **Had the cap been raised this comparison would be barred outright**, and that condition travels
   with any quotation of it.
3. The two sides differ in **more than the statement**: the diet-bare cells are matrix cells, the
   diet+statement cells are amendment cells fired later. `A3.1`'s selection effect and `A3.2`'s confound
   both bind. **Nothing in this design licenses reading a capability or a mechanism from it.**
⛔ **No probability is attached to the rank ordering** — two p-values have already been struck on this
axis for pricing a pattern found by inspection.

## §8 · PROVENANCE
```
  scorer      harness/systems-v3/score_matrix1.py at this branch
              sha256 3ba8a165b66b1210263964300bf1d2b989f2783954fdb55c4417882a9ab8119e
              run on the run box as ~/score_matrix1-main-2026-09-09.py (copied from this tree)
  ⛔ the box's own ~/score_matrix1.py is STALE (2026-09-08) and declares NO statement roots:
     it would have scored 0 of the 18 cells and said nothing about it.  Not used.
  correctness ~/referee-posthoc-2026-09-09/tasks/systems-v3/FreeList/G/run_tests.sh <cell>/repo
              under the six-name toolchain contract; rc 0 and "TESTS 7/7" on all six
  cells       run box  ~/cells-stmt-2026-09-09 (wave 1, export aaf570e)
                       ~/cells-stmt-free-2026-09-09 (wave 2, export 311b208)
  archive     run box  ~/harvest-v3/<cell>-*/METER.txt
  frozen      PRESPEC 437ea70 · AMENDMENT + addenda 1-2 7180387 · score_matrix1.py d31e482
```
