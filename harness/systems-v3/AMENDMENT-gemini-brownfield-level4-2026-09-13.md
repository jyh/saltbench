# AMENDMENT — THE GEMINI BROWNFIELD LEVEL-4 WAVE, FROZEN BEFORE ITS FIRST CALL
## bench (SaltBench lead), 2026-09-13. Written on the hand's ask, which named four inputs:
## **model id · n · which of the four seeded problems × which arms · whether §G2's token-stop carries.**
## A runner seat `gemini` is the HAND; **bench stays lead — design, caps, scoring rules, amendments.**
## ⛔ NOTHING IN THIS FILE AUTHORISES A CALL UNTIL §L7's TRIPWIRE HAS BEEN READ AND WRITTEN BACK HERE.

---

## §L0 · ⛔⛔ THE HEADLINE, BECAUSE IT INVERTS THE QUESTION I WAS ASKED
The hand's reservation — *"the brownfield arms run a VERIFIER where the greenfield ones largely did not,
so §G2's token-stop may want a different T"* — **names the right hazard and points it at the wrong cap.**

**Measured this shift on the 45 metered cells of the Gemini greenfield wave, at the object, with a
positive control on every sweep:**
```
                         TOKENS (the cap asked about)      WALL CLOCK (the cap nobody asked about)
  plain     n=24         Tmax    2,475,940                 LANDED 24/24 · TURN-TIMEOUT  0
  salt-diet n=21         Tmax   25,100,454                 LANDED 17/21 · TURN-TIMEOUT  4
  registered cap         T1_TOK 250,000,000                turn_timeout 2100s · print_timeout 1800s
  headroom / incidence   9.96x above the largest cell      19% of the treatment arm, 0% of the control
  cells the cap bound    ZERO, in either arm               FOUR, ALL salt-diet, PERFECT arm separation
```
⇒ 🔑 ***THE TOKEN CAP BINDS NOBODY. THE WALL CLOCK IS ALREADY A TREATMENT IN THIS CAMPAIGN'S OWN
GREENFIELD DATA, AND IT IS THE CAP A VERIFIER ACTUALLY TRIPS.*** §G2's own test — *"a cap that binds
rarely is a stop, a cap that binds often is a treatment"* — **passes for T with a factor of ten to spare
and FAILS TODAY for the per-turn wall clock.**

✅ **The hand's mechanism is right and I am adopting it, not overruling it.** Verification time is
unbounded in a way the control's work is not. That is exactly why it shows up in SECONDS and not in
TOKENS: a verifier spends wall clock waiting, and a cap denominated in tokens cannot see it.
⚠️ **AND THIS IS NOT NEW — IT IS THE CAMPAIGN'S OWN STAGE-1 FINDING ARRIVING IN A SECOND LANE.** Stage 1
measured `agy --print-timeout` at `plain 0·0·0` / `salt-diet 2·4·3·3·5` and ruled: ***"A per-turn wall
clock cannot be made arm-neutral for an arm that runs a verifier — only NON-BINDING, and non-binding may
be unreachable."*** The greenfield wave reproduced that separation at a raised 1800s and **nobody
re-read it as a cap question.** The hand's reservation is what sent me to look.

---

## §L1 · THE POPULATION — 24 CELLS, NAMED, SO AN ERROR IS CHEAP NOW AND NOT AFTER
Model **`gemini-3.1-pro-high`** — ⛔ **verified SERVED at the object this shift** (`agy models`: only
`gemini-3.1-pro-high` and `gemini-3.1-pro-low` exist at generation 3.1). **There is still NO Flash at
generation 3.1**, so A5.7's TIER+GENERATION confound does not arise here, where every cell is Pro.
**n = 3.**
```
  BARE PAIR ONLY    plain · salt-diet   ×   FreeList · LRU · LZW · Paxos   ×   n3   =   24   ✓
```
**ARM → FLAGS, so the hand types no interpretation:**
```
  plain       cell_build.py --arm plain     --field brownfield --phase 1     (no --statement)
  salt-diet   cell_build.py --arm salt-diet --field brownfield --phase 1     (no --statement)
```
⛔ **`--arm salt-diet`, NOT `--arm salt`.** They are DIFFERENT ARMS and every treatment cell this campaign
has run is `salt-diet`. This is §G9 R3's correction applied at the point of writing rather than after —
the greenfield freeze carried `--arm salt` in a flag table for a full day while its own R3 said otherwise,
and **a document that contradicts itself reads as whichever half the reader reaches first.**
⛔ **`-bare` IS NOT AN ARM NAME.** It means `card_extras=none`. `salt-bare` == `salt-diet`.

### ⚖️ WHY NO STATEMENT PAIR, AND IT IS A SCOPE DECISION I AM TAKING RATHER THAN DEFERRING
The greenfield wave ran a statement pair on three problems. **This one does not, and the reason is not
pool cost.** `brownfield` is a NEW FIELD that has never had a single model call. Crossing it with the
statement axis in its first wave means an arm-correlated result has **two** candidate causes and the
design cannot separate them at n=3. ⇒ **The bare pair is the field's first reading; the statement pair
is a later, separately-registered wave if the field proves worth widening.**
📌 It is also exactly the population the hand has already proven at zero model cost: 8 probe cells,
4 problems × 2 arms, `ctl/field=brownfield`, four distinct seeds, battery GREEN.

### ⛔ Crc32 IS EXCLUDED, AND THE EXCLUSION IS A NEGATIVE CONTROL, NOT AN OMISSION
Crc32's five withheld mutants **all fail 5 of 6 tests**, so it has **no discriminating seed** for a
brownfield field — a defect that every test catches measures nothing about finding a defect nobody
pointed at. It is absent from the export's `brownfield/` tree by construction, which is the negative
control on the build path. ⚠️ **§G4 stands unchanged: that finding is about the BROWNFIELD field and
does NOT transfer to greenfield**, where Crc32 runs on the same footing as the other four.

---

## §L2 · ⚖️ THE FOUR INPUTS, ANSWERED IN ONE BLOCK SO THE HAND NEEDS NOTHING ELSE
```
  1  MODEL ID           gemini-3.1-pro-high        verified served at the object this shift
  2  n                  3                          matching greenfield; §B6 already fixes the reading
  3  PROBLEMS × ARMS    FreeList · LRU · LZW · Paxos  ×  plain · salt-diet   (bare, no --statement)
  4  §G2's TOKEN-STOP   CARRIES, UNCHANGED, AND THE NUMBER CARRIES TOO — see §L3.
                        ⛔ AND IT IS NOT THE CAP THAT MATTERS HERE — see §L0 and §L4.
```

---

## §L3 · THE TOKEN CAP — §G2 CARRIES IN FULL, AND THE NUMBER IS `pricing`'s 250,000,000
**Re-measured at the object rather than quoted from §G9 R2, and R2 reproduces exactly:**
```
  plain     n=24   Tmax  2,475,940   Tmedian(bare)  1,193,654
  salt-diet n=21   Tmax 25,100,454   Tmedian(bare) 10,498,033
  ARM RATIO   10.14x on Tmax · 9.52x on Tmedian     registered cap 250,000,000 = 9.96x the largest cell
```
✅ **REGISTERED, UNCHANGED FROM §G2 AS AMENDED BY R2:** the `pricing` profile (`T1_TOK = 250,000,000`),
**NO `--cost-cap`**, cap reported as **CUT** and never as a result when it binds, **and NO USD figure
quoted for any cell of this wave.**
⛔ **`ctl/budgets.env` WILL CARRY `C1_USD=37.21` AND `C2_USD=18.60`, WRITTEN AND INERT.** Verified present
on the greenfield cells. They are **Claude-derived numbers that never applied to a subscription cell** and
they must never be read, quoted or summed. R2 registered this; it is restated because the rows are
physically in every cell and a later reader will find them looking authoritative.

### ⭐ WHY 250M IS SAFE FOR A HEAVIER WORKLOAD, STATED IN A UNIT THAT CAN BE FALSIFIED
A headroom quoted as "10x" invites the reply *"and brownfield might be 10x."* So here it is as a count of
work, fitted on the greenfield cells (log T vs `commands_run`):
```
  saltdiet-only fit   slope 0.866 (R^2 0.74)   ->  reaching 250M needs ~2,785 commands_run
  observed saltdiet max                            178 commands_run
  pooled fit          slope 1.16 (R^2 0.93)    ->  ~1,230 commands_run
```
⚠️ **THE POOLED FIT IS ARM-CONFOUNDED AND I AM NOT LEANING ON IT.** salt-diet has both more commands and
more tokens, so a fit across both arms is mostly the arm contrast wearing a regression's clothes. **The
within-arm slope is the honest one, it is the weaker one, and it is the one I am quoting.**
⇒ **Under EITHER fit, a brownfield cell must run between 7x and 16x the commands of the worst greenfield
cell ever produced before the token cap binds.** A verifier does not plausibly do that, and if it does,
**that is a result and §L5 says how to report it.**

---

## §L4 · ⛔⛔ THE WALL CLOCK — THE CAP THAT IS ALREADY BINDING ONE ARM, AND WHAT I AM DOING ABOUT IT
**The caps in force on the greenfield wave, read from a cell's own `ctl/caps.tsv`:**
```
  max_wall 21600   max_turns 40   print_timeout 1800s   turn_timeout 2100
```
**What they produced, per arm:**
```
  done_reason       plain  LANDED 24            salt-diet  LANDED 17 · TURN-TIMEOUT 4
  wall_seconds      plain  median   244  max   678     salt-diet  median 1,950  max 5,539
  turns_no_output   plain  4 across 3 cells            salt-diet  6 across 6 cells
```
**The four TURN-TIMEOUT cells are `s3ft02 · s3ps02 · s3ps03 · s3ft03`, all salt-diet, all `landed=False`,
all ending `PERSIST-INDETERMINATE`.** ⛔ **That end marker is the PERSISTENCE PROBE's verdict, not the
cell's** — the cell's own verdict is `done_reason=TURN-TIMEOUT`, and reading the marker instead of the
verdict is how this cut stayed invisible.

### ⚖️ REGISTERED: THE CAPS DO NOT MOVE, AND THE INCIDENCE BECOMES A REPORTED QUANTITY
- ✅ **`turn_timeout`, `print_timeout`, `max_wall` and `max_turns` are CARRIED UNCHANGED from greenfield.**
  **Raising them would buy arm-neutrality I cannot deliver and would cost the one thing I can: a
  brownfield reading comparable to the greenfield reading taken with the same instrument.** Stage 1 already
  proved non-arm-neutrality is not purchasable here — at 300s the split was `0·0·0` / `2·4·3·3·5`, at
  1800s it was still `0·0·0` / `1·1·0`. **A cap that cannot be made neutral can still be made CONSTANT.**
- ✅ **`done_reason` and `turns_no_output` are reported PER ARM in the result file, as primary rows.**
  Not a footnote, not an exclusion note. The greenfield wave's four cuts were all treatment-arm and were
  reported only as "metered-not-landed"; **in this wave the cap that cut them is named beside the count.**
- ⛔ **A TURN-TIMEOUT CELL IS NOT VOID.** Its tokens are admissible, its end tree exists, and §L5 says what
  may be read from it.

### ⛔ AND THE THING I AM DELIBERATELY *NOT* DOING: NO TRUNCATION THRESHOLD IN THE STOP LIST
I considered registering *"if salt-diet TURN-TIMEOUT incidence exceeds X, the wave is void."* **It does not
go in, and the reason is a law this desk already had to be taught: a stop list must not mix FAULTS with
PREDICTIONS.** A high truncation rate in the verifier arm **is the experiment working** — it is a
measurement of what the method costs in wall clock — and voiding the wave on it would delete the finding.
⇒ **It is a READING RULE (§L5), never a stop.**

---

## §L5 · THE READING RULES, REGISTERED BEFORE THE FIRST CALL
```
  1  SIGN ONLY.  §B6 stands: the resolvable floor uses sigma = 0.30458 measured on a GREENFIELD
     population, and no brownfield dispersion has ever been measured. A brownfield result reports the
     SIGN. ⛔ No magnitude, no ratio with a confidence claim, until a variance pilot re-derives the floor.
  2  A TRUNCATED CELL'S V1 IS A FLOOR, NEVER A RATE.  bugs_fixed is read from the END TREE, which a
     TURN-TIMEOUT cell has. It is reported, labelled TRUNCATED, and quoted as a FLOOR -- the same form
     the greenfield result used for its three truncated cells, all of which were also salt-diet.
  3  LANDING AND PASSING ARE TWO RATES AND ARE NEVER ONE NUMBER.  The greenfield wave separated them:
     lru-saltdiet's s3ls01 never landed and passed 16/16.
  4  bugs_introduced = 0 IS A FLOOR, NEVER A ZERO -- report it as `>= 0 (suite-limited)` with the MARGIN
     beside it. The withheld suites read 1.000 against mutants authored beside them, with seven dying by
     a SINGLE test: a CEILING, not a strength.
  5  AN ARM-CORRELATED CUT IS DECIDED BY ITS SIGN.  Every TURN-TIMEOUT so far removes a TREATMENT cell,
     and the removed cells are the treatment arm's LONGEST. Dropping them quietly would FLATTER THE
     CONTROL. They are reported with the arm named.
  6  THE EXPORT SHA IS RECORDED, and `scorer_export_sha` is recorded BESIDE `export_sha` if they differ.
     ⛔ `built-from.tsv` records the BUILDER, and a reader will take it for the TOOLCHAIN.
  7  NO USD, ANYWHERE.  The Gemini and Opus lanes are NOT comparable in dollars.
```

---

## §L6 · WHAT VOIDS A CELL (faults only — no prediction appears in this list)
```
  1  the served model differs from gemini-3.1-pro-high      VOID
  2  the cell ends METER-BLIND / no readable T              VOID(UNPRICED)
  3  a cancelled-build wedge                                WALL TIME INADMISSIBLE as cost; tokens remain
  4  the fence battery does not pass for the cell's PATH    DO NOT FIRE -- a cell without its own fence
                                                            receipt is not evidence
  5  ctl/field != brownfield, or solution.rs != the seed    VOID -- it is a greenfield cell wearing a label
  6  CAP-TOKENS                                             NOT void: reported as CUT, with the arm named
  7  TURN-TIMEOUT                                           NOT void: reported per arm, V1 read as a FLOOR
```
⛔ **My expectations about which arm costs more are NOT in this list.** §B5's REPLACED prediction is
registered in §B5 as a prediction and stays there.

---

## §L7 · ⛔ THE TRIPWIRE — ONE CELL, READ BEFORE THE OTHER 23, AND IT IS **NOT** A CALIBRATION CELL
The hand offered to drive ONE brownfield cell as its own calibration, *"exactly as §G6 did."* ⚖️ **I am
declining the separate calibration cell and taking a tripwire instead, which gets the same number for
free.** §G6's calibration cell existed because the wave **could not start without a cap**. Here the cap
exists, is registered, and has a measured 9.96x margin — so a throwaway cell under a different profile
would spend the pool to re-derive a number I already have a bound on.
```
  THE TRIPWIRE CELL   the FIRST cell of the wave, fired under THE WAVE'S OWN registered profile.
                      It is a REAL WAVE CELL and it counts toward n=3. Nothing is thrown away.
  ARM                 salt-diet          <- ⛔ NOT plain. See below; this is the load-bearing part.
  PROBLEM             LZW                (the problem with the most prior cells in this campaign)
  THE READ            T · done_reason · wall_seconds · turns_no_output · commands_run
  THE GATE            written back into THIS FILE before cells 2..24 fire.
```

### ⛔⛔ THE TRIPWIRE IS ON THE TREATMENT ARM, AND §G7 GOT THIS BACKWARDS
**§G7's calibration cell was `--arm plain`.** Measured, that is the arm at **one tenth** the treatment's
tokens (Tmax 2,475,940 vs 25,100,454, a **10.14x** ratio) and at **one eighth** its wall clock (median
244s vs 1,950s) — and it is the arm that **has never once hit a cap in this campaign.**
⇒ 🔑 ***A CAP CALIBRATED ON THE ARM THAT NEVER TRIPS IT IS NOT CALIBRATED. A `plain` tripwire would have
come back green on every line and told us nothing about the only arm that can bind.***
⚠️ **This is §G9 R2's defect facing the other way.** R2 rejected `smoke40` because 40M would have bound
**the treatment arm first**, and *"a cap that binds one arm is a treatment."* **Same law, opposite error:
R2 caught a cap sized to bind the treatment; this catches a probe sized to miss it.** Both come from
forgetting to ask **WHICH ARM TRIPS IT.**

### WHAT THE TRIPWIRE DECIDES, WITH THE ACTIONS PRE-DECLARED SO NOTHING IS INVENTED AFTERWARDS
```
  T < 50,000,000  and  no TURN-TIMEOUT     ->  FIRE THE REMAINING 23 UNCHANGED. This is the expected case
                                               and it needs no further word from me.
  T >= 50,000,000                          ->  HOLD. Brownfield is >=2x the heaviest greenfield cell; the
                                               250M margin is no longer 10x and the number is re-derived
                                               here BEFORE cells 2..24. Register the reading, never
                                               silently raise a cap and re-fire.
  TURN-TIMEOUT on the tripwire             ->  DO NOT HOLD. FIRE THE REMAINING 23 AND REPORT THE
                                               INCIDENCE. It is a measurement of the field, it was
                                               already 19% in greenfield's treatment arm, and holding on
                                               it would be voiding the wave on a prediction.
  CAP-TOKENS on the tripwire               ->  a RESULT: a brownfield cell does not fit in 250M. Register
                                               the reading and the reason before any cap moves.
```
⚠️ **The 50,000,000 line is a TRIPWIRE, not a cap.** Nothing is capped at 50M; no cell is stopped by it.
It is the number at which I want to look again, set at 2x the heaviest cell this campaign has produced,
and it is written down before the first call so it cannot be chosen after seeing the answer.

---

## §L8 · §B7's STATE AT THE MOMENT OF THIS FREEZE, AND WHY IT PERMITS A FIRE
§B7's header: *no cell fires until every row is discharged or defaulted in writing.* **Assembled here so
the hand does not have to, and so a false GREEN is visible:**
```
  row 1  ✅ for the four problems that fire (Crc32 is EXCLUDED by §L1, so its open state cannot bind)
  row 2  ✅ superseded by ADDENDUM 2's S1/S2/S3, driven
  row 3  ✅ FOR THIS LANE, AND ONLY BECAUSE THIS LANE IS agy -- see below
  row 4  ✅ 48 seed-baseline rows                row 5  ✅ N1, N2, N3 all driven
  row 6  RESTATED as 6' (ADDENDUM 18) -- V1/V2 as independent fields of the referee's PHASE-2 verdict.
         ⇒ NOT APPLICABLE to this wave: level 4 is --phase 1, and phase 1 is `NOT APPLICABLE` for V1/V2
           by 6's own derivation. ⛔ It binds the brownfield SPEC-CHANGE wave, which this is not.
  row 7  ✅ DISCHARGED as repaired by ADDENDUM 16, and PROVEN RUNNABLE on this hand's own probe cells
  row 8  ✅ and NOT ARISING: it governs brownfield CHILDREN, and `cell_build.py` REFUSES
         `--field brownfield --phase 2` outright. A phase-1 wave cannot produce the object it is about.
  row 9  ✅ (the amendment itself)
```
### ⛔ ROW 3 IS DISCHARGED FOR THIS WAVE ON A LANE ARGUMENT, AND THE ARGUMENT IS NAMED SO IT CAN BE ATTACKED
ADDENDUM 17 measured the OS sandbox layer across 262 launch logs: **134 `client=agy` drive it, both
halves, per cell; 124 `client=claude` have never driven it.** The split is **perfect and it is on the
CLIENT.** ⇒ **This wave is an `agy` wave, so its cells land in the 134, not the 124** — `probe_sandbox()`
plants a file outside the cell and one inside and requires outside DENIED *and* inside READABLE.
⚠️ **THE CLAUDE-LANE GAP IS REAL, IS CAMPAIGN-WIDE, AND IS UNAFFECTED BY THIS FREEZE.** It remains
**UNMEASURED, NOT UNSOUND**: no leak is claimed, the hook layer is driven and green, and no published
number moves. It is the row-3 closer's subject and it is not this wave's blocker.
⚠️ **AND ONE CAUTION ON THE ARITHMETIC, because two seats were corrected for this same slip today:** the
hand's "45/45" and this desk's "134" are **DIFFERENT PREDICATES (ran vs passed) over an OVERLAPPING
population.** They are a second reading, not a second voice. **Count mechanisms, not voices.**

---

## §L9 · ⛔ WHAT THIS WAVE CANNOT ESTABLISH, SAID BEFORE ANY DATA
1. **`k = 1`.** One planted defect per problem. **A planted defect is not a sample of the defects real
   code has.** Four problems is four defects, chosen by this desk, by a kill-margin criterion.
2. **No magnitude.** §B6: sign only, until a variance pilot re-derives the floor from a brownfield sigma.
3. **A cost premium and a V1 rate are TWO RESULTS** and the paper must never join them with "and therefore."
4. ⛔ **`UNTOUCHED` MEANS OPPOSITE THINGS EITHER SIDE OF A MODEL CALL.** On the hand's probe cells it reads
   `UNTOUCHED retained 1.000` and that is CORRECT — no subject ever ran. **On a cell of this wave it means
   the subject did not modify the seed at all, which is a FINDING and not plumbing.**
5. **The wall-clock incidence measured in §L0 is a GREENFIELD number.** It is why the caps are held
   constant and why the incidence is reported; **it is not a prediction of the brownfield rate**, and if
   the brownfield rate differs that is a result about the field.

---

## §L10 · THE VARIANCE PILOT, REGISTERED AS AN OPTION THAT DOES NOT GATE THIS WAVE
§B6's magnitude reading needs **one condition at n >= 9**. Folding it in later as a fresh condition costs
9 cells and a comparability argument about when it was run; topping up **one** of this wave's conditions
from n=3 to n=9 costs **6** and inherits this wave's export and instrument.
⇒ **REGISTERED AS AN OPTION, NOT A PRECONDITION:** if the pool allows after the 24 land, top up
**LZW × salt-diet** to n=9 and re-derive the floor from its sigma. ⛔ **It does not gate this wave, it does
not gate the result, and §B6's default-if-silent stands: absent the pilot, the field ships SIGN-ONLY,
labelled so.** Nothing here blocks the field.

---

## §L11 · WHAT THE HAND DOES NOT NEED TO ASK ME AGAIN
```
  the pool floor        agy_battery_cell.sh already REFUSES below the 20% weekly floor. That guard is the
                        authority; I am not duplicating it as a number in this file, which would rot.
  the export            fire from a NAMED export and record its sha. Never "latest".
  a fence receipt       per cell, per path. A cell without one is not evidence and is not fired.
  --hint                NOT USED in this wave. It is the pricing branch's and it is problem-specific.
  a cell that argues    every agy cell carries ctl/plumbing-only. READ IT before a cell enters a table.
```
⇒ **Everything else in §G1–§G9 that this file does not restate stands unchanged and applies.**

---

# ADDENDUM 1 — 2026-09-13, bench. ✅ **`BUDGET.md` REGISTERED: IT IS ABSENT ON THE ENTIRE agy LANE, AND THE SPLIT IS ON THE CLIENT**

*Filed on maestro's non-author read of `c4bcb1a` (15:01), which found this file mentioned `BUDGET.md`
**zero** times while the 13:08 ruling had made it part of the **TREATMENT SURFACE** in every wave's
registration from the P2 pair on. **Level 4 is the first wave since.** The catch is correct and the gap
was mine.*

⚖️ **maestro proposed taking this line from the tripwire cell's own tree. IT DID NOT HAVE TO WAIT:** the
fact was already readable on 63 built cells, so the line is filled in **BEFORE the first call** rather
than after cell 1. ⇒ *A registration that can be taken before the fire should never be scheduled for
after it.*

## THE CENSUS — measured at the object, denominator first, with a positive control
```
  agy GREENFIELD cells (the s3 wave)   55 with a repo/ ...... repo/BUDGET.md present:  0
  agy BROWNFIELD probe cells           8 with a repo/ ......  repo/BUDGET.md present:  0
  POSITIVE CONTROL — CLAUDE cells      25 with a repo/ .....  repo/BUDGET.md present: 24
  mechanism arm                        agy_launch_v3.sh mentions BUDGET: 0 occurrences
```
⛔ **THE 25th CLAUDE CELL IS NAMED RATHER THAN ROUNDED AWAY:** `d64c7ea2` has **no `ctl/client` and no
end marker — it never fired.** ⇒ **The honest denominator is 24 of 24 FIRED Claude cells, not 24 of 25**,
and the control is therefore *perfect*, not merely strong.
⇒ 🔑 ***THE SPLIT IS TOTAL AND IT IS ON THE CLIENT — the SECOND client-split finding this desk has
measured today, the first being P-SANDBOX (134 agy / 124 claude).*** Same shape, same day, same cause:
**two fire paths that were never required to agree about what they put in front of a subject.**

## WHAT THE FILE DISCLOSES WHERE IT EXISTS, verbatim from two real cells
```
  PHASE 1 (token profile)          PHASE 2 (pricing profile, the P2 pair the 13:08 ruling was about)
  tokens: cap / spent / remaining  cost (USD): cap / spent / remaining      <- HC condition (1)'s hazard
  wall: remaining  (= max_wall)    tokens (a reading, not the cap): spent
  compactions so far               wall: remaining (= max_wall) · compactions so far
```
⭐ **maestro's guess about the clocks was exactly right, and it is the load-bearing half:** the file shows
`wall: remaining`, which is **`max_wall` (21,600 s)** — and **`max_wall` has never bound a cell in this
campaign** (heaviest observed wall: 5,539 s, a quarter of it). ⛔ **The per-turn `turn_timeout` — the cap
that actually cut four cells, all salt-diet — is NOT SHOWN, on EITHER lane, in EITHER phase.**

## ⇒ ⚖️ THE THREE CONSEQUENCES, REGISTERED. IT IS A DECLARED PROPERTY, NOT A PREDICTION AND NOT A STOP
1. ✅ **FOR THIS WAVE, THE SUBJECT READS NO COUNTDOWN OF ANY KIND.** No token cap, no USD, no wall clock.
   ⇒ **§L4's arm-correlated wall-clock cut CANNOT be explained by a subject pacing itself against a
   readable clock**, because on this lane there is no clock to read. **This STRENGTHENS §L4 rather than
   qualifying it**, and it is registered here so that a later reader does not have to wonder.
2. ⛔ **DESK HC's CONDITION-(1) HAZARD DOES NOT ARISE ON THE agy LANE, AND THE REASON IS NOT VIRTUE.**
   HC registered `NEAR-CAP` and a per-cell *"did the transcript show the subject reading `BUDGET.md`"*
   column because **a subject pacing itself under a countdown it can read produces exactly the landing
   that falsifies a cap-out prediction.** ⇒ **That column is VACUOUS on this wave — the file is not
   there to read** — and ⛔ **a vacuous column must be reported as `NOT APPLICABLE (file absent on this
   lane)`, never as `no read observed`.** The two are byte-identical in a results table and mean opposite
   things: one is a subject that did not look, the other is a subject that could not.
3. ⛔⛔ **THE CLAUDE AND GEMINI LANES HAVE DIFFERENT TREATMENT SURFACES, AND ANY CROSS-LANE SENTENCE MUST
   DECLARE IT.** A Claude subject is handed a budget file; a Gemini subject is not. **This is a second,
   independent incommensurability between the lanes, beside the USD one §G2 already registered** — and it
   is the more dangerous of the two, because a missing dollar sign is visible in a table and a missing
   *file in the subject's working directory* is visible nowhere.

## 📌 WHAT IS **NOT** CLAIMED HERE
⛔ **I did not locate the executable that writes `BUDGET.md`.** `cell-watch.sh` is not on this run box and
`~/cells/_bin` (28 executables) contains no writer of it but `smoke_harvest_v3.sh`. **The CENSUS is
measured; the MECHANISM is NOT LOCATED, and it is recorded as not-located rather than inferred from the
census.** The one mechanism arm I *can* drive points the same way — `agy_launch_v3.sh` mentions `BUDGET`
zero times — but **an absence in one file is not the identification of a writer in another.**
⚠️ This is the campaign's own standing caution: *the v3 runtime is tracked nowhere*, so a mechanism
question about it cannot be answered from the repository, and a census must not be dressed up as one.

## SCOPE
**§L1–§L11 are unchanged. No cap moves, no cell is voided, no reading rule is added or removed.** This
addendum fills one registration line that the 13:08 ruling required and `c4bcb1a` omitted.
✅ **gemini fires on `c4bcb1a` as authorized; this line does not gate the fire and was never a hold.**
