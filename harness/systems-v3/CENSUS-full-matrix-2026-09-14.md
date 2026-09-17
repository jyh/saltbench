# MATRIX CENSUS — THE CAPTAIN'S FULL-MATRIX REQUEST, DESK ROW `MP`
## bench (SaltBench lead), 2026-09-14. **Part 1 of the row's act (1). No arXiv draft begins until this reads full.**
## His words, verbatim: *"once we get the full matrix for the saltbench pilot (4 models, 5 problems,
## greenfield + brownfield, {plain,salt-diet}*{,statement,spec-change}) I would like to update the arXiv paper"*.
## ⇒ **4 × 5 × 2 × 2 × 3 = 240 conditions, before replication n.**
## ⛔ **DONE means A RESULT OF RECORD WITH A PR SHA. It does NOT mean cells exist on the run box** — see §C2.

---

## §C1 · THE MODELS — THE ROW'S FIRST UNMEASURED ITEM, ANSWERED AT THE OBJECT
Every distinct model string in every cell record on the run box (`built-from.tsv` `model_served` /
`model_requested`, and `--model` in `launch.log`; **both lanes; 307 `ctl/arm` files swept**):
```
  gemini-3.1-pro-high      260 occurrences     levels 1 and 4
  claude-opus-5            162                 the Opus lane
  gemini-3.8-flash-high      2                 level 5 — HALTED at one cell, 0 scored
  ───────────────────────────────────────────────────────────────────────────────────
  THREE subject models have ever been served. THERE IS NO FOURTH IN THE RECORD.
```
⛔⛔ **AND THE TRAP, WHICH IS WHY NO FOURTH IS NAMED HERE.** `_bin/models.tsv` lists `claude-sonnet-5`
and `claude-fable-5-1` beside `claude-opus-5` and looks exactly like the answer. **Its first column is
`role`**: `head · worker-opus · worker-sonnet · reviewer · designer`. ⇒ ***THOSE ARE ROLES INSIDE A
CELL, NOT SUBJECT MODELS OF THE MATRIX.*** A subordinate worker model inside an Opus cell is not a row
of this grid. **The fourth model is the Captain's to name; it is not inferable from a role map.**
⇒ **60 of the 240 conditions belong to a model that does not yet exist in this campaign.**

## §C2 · ⛔ WHY THIS CENSUS IS BUILT FROM RESULTS OF RECORD AND NOT FROM A CELL SWEEP
I swept 307 `ctl/arm` files intending to classify every cell by its five axes. **It cannot be done:**
```
  agy lane (b4/s3)   ctl/arm = plain|salt-diet   ctl/field = brownfield|<empty>   ctl/card_extras = none|statement
  claude lane        ctl/arm = a 24-hex NONCE    ctl/task  = "1"                  the axes are NOT in these files
```
⇒ **The same filenames hold different things in the two lanes**, and 121 Claude-lane cells would have
been binned under hexadecimal "arms". ⇒ 🔑 ***A CELL THAT NEVER BECAME A RESULT OF RECORD IS RESIDUE,
NOT EVIDENCE*** — which is what the row asks for anyway, and is the sounder basis.

## §C3 · ⛔⛔ TWO CLASSES THE HARNESS CANNOT EXPRESS — STATED, NOT SILENTLY DROPPED (the row requires this)
```
  (a) <any model> × Paxos × statement                          INEXPRESSIBLE — RULED, with a reason
      RESULT-statement-arm-2026-09-09.md: "an arm-neutral formal statement CANNOT EXIST for a
      proof-obligation task … a plain+statement Paxos cell would be a control told to write proofs."
      ⇒ 4 models × 1 problem × 2 fields × 2 arms = 16 of the 240.
  (b) <any model> × brownfield × spec-change                   INEXPRESSIBLE AS BUILT — needs a ruling
      cell_build.py REFUSES `--field brownfield --phase 2` outright, and spec-change IS the phase-2
      shape (level-4 freeze §L8, row 8 discharge).
      ⇒ 4 models × 5 problems × 2 arms = 40 of the 240.
      ⚠️ MEASURED AS A BUILDER REFUSAL, NOT YET CONFIRMED AS A DESIGN DECISION. If it is a design
        decision the 40 leave the denominator; if it is a limitation they are OWED. NOT MY CALL.
```
⇒ **Between them, up to 56 of 240 may not be expressible conditions at all.** ⚠️ (a) and (b) overlap on
Paxos × brownfield × spec-change (4 cells), so the union is **52**, not 56. **Stated because a reader
adding the two numbers gets the wrong denominator.**

## §C4 · THE GRID, PER MODEL (each model is 5 × 2 × 2 × 3 = 60 conditions)

### `claude-opus-5` — the most complete row
```
  greenfield × {plain,salt-diet} × none        × 5 problems   DONE   RESULT-matrix-opus-1 9ffa1a8   10
  greenfield × {plain,salt-diet} × statement   × 4 problems   DONE   RESULT-statement-arm 173ee84    8
       (Crc32·LRU·FreeList = 18 of 24 cells; LZW via matrix-1's GOLD PAIR)   Paxos: INEXPRESSIBLE (2)
  greenfield × {plain,salt-diet} × spec-change × 5 problems   DONE   RESULT-p1-specchange 20836ad   10
       (19 cells; RESULT-specchange-1 a9ed1f3 is the LZW four-cell pilot; some cells CAP-COST CENSORED)
  brownfield × everything                      × 5 problems   BLOCKED  §B7 row 3 — the helm's hold on
       CLAUDE-CLIENT brownfield cells (the undriven OS-sandbox layer). Lifts on the probe's receipt.  30
  ─────────────────────────────────────────────────────────────────────────────────────────────────
  DONE 28 · INEXPRESSIBLE 2 · BLOCKED 30  (of which 10 are also class (b))
```

### `gemini-3.1-pro-high`
```
  greenfield × {plain,salt-diet} × none        × 4 problems   DONE   RESULT-p1-greenfield 6f627f5    8
       (LRU·Paxos·FreeList·Crc32. LZW EXCLUDED from the bare pair — desk HC already held it at n=1)  LZW OWED 2
  greenfield × {plain,salt-diet} × statement   × 3 problems   DONE   RESULT-p1-greenfield 6f627f5    6
       (Crc32·FreeList·LRU)                    LZW OWED 2 · Paxos INEXPRESSIBLE 2
  greenfield × {plain,salt-diet} × spec-change × 5 problems   OWED                                  10
  brownfield × {plain,salt-diet} × none        × 4 problems   DONE   RESULT-level4 0e66928           8
       ⛔ SUPERSEDED BY ADDENDUM 6: FreeList and LZW (4 of these 8 conditions) rest on cells whose
         GIVENS ANNOUNCED THE PLANTED DEFECT ⇒ those 4 revert to OWED. LRU and Paxos (4) stand.
       (FreeList·LRU·LZW·Paxos. Crc32 EXCLUDED as a declared NEGATIVE CONTROL, freeze §G4)  Crc32 OWED 2
  brownfield × {plain,salt-diet} × statement   × 5 problems   OWED (Paxos 2 INEXPRESSIBLE)           10
  brownfield × {plain,salt-diet} × spec-change × 5 problems   class (b)                              10
  ─────────────────────────────────────────────────────────────────────────────────────────────────
  DONE 22 · OWED 28 · INEXPRESSIBLE 4 (+10 class (b))
```

### `gemini-3.8-flash-high`
```
  ⛔ SUPERSEDED — READ THE §C5 POINTER BOX. LIVE: flash DONE 14 · OWED 32 · BLOCKED 0 · INEXPR 4
     (ADDENDUM 2: not blocked, a 503 · ADDENDUM 5: DONE 7 · ADDENDUM 7: DONE 14). The lines below are
     the 09-14 11:3x record, preserved unedited, and BOTH claims in them are now refuted:
  ALL 60   BLOCKED — not owed. Level 5 HALTED at ONE cell; 0 scored.
  AMENDMENT-gemini-flash-level5 ADDENDUM 1, merged 6d8dd527: the model runs an episode as ONE TURN and
  meets a per-turn deadline calibrated on Pro's granularity. ⛔ n = 1 on the Flash side.
  ⛔ REFUTED by the completed wave (RESULT-gemini-flash-level5 §6.2): Flash segments an episode
     exactly as Pro does, 3-6 turns per cell, across 21 cells. The n=1 above was the whole basis.
  ⇒ RELEASE: a design decision about per-turn capping for a model that does not segment. NOT a re-fire.
```

### the FOURTH MODEL — UNNAMED
```
  ALL 60   BLOCKED ON THE CAPTAIN — the model is not named and cannot be inferred (§C1).
```

## §C5 · THE TOTAL AS IT STOOD AT 11:3x — ⛔ **SUPERSEDED THREE TIMES BELOW. DO NOT QUOTE THIS BLOCK.**

> ## ⛔⛔ THE LIVE FIGURE IS THE ROW MARKED `LIVE` IN THIS BOX, AND NOWHERE ELSE
> ⚠️ **This line read *"the live figures are in §F1's last row and §F2"* until 2026-09-17, and it had gone
> stale in the same way the heading above it did: §F1's last row reads **DONE 50** and the matrix is at **60**.
> A reader who followed the pointer instead of reading the box got a figure four addenda old.**
> ⇒ 🔑 ***A POINTER TO THE CURRENT FIGURE ROTS EXACTLY AS FAST AS THE FIGURE, AND IT IS WORSE THAN THE STALE
> FIGURE ITSELF, BECAUSE IT SENDS THE READER AWAY FROM THE TABLE THAT IS BEING KEPT UP TO DATE.*** The
> trajectory below is appended to at every addendum; the `LIVE` row is therefore always last and always current,
> which is a property of the FORM rather than of anyone remembering to re-point a sentence.
> ```
>   THIS BLOCK (11:3x)   DONE 50 · OWED  28 · BLOCKED 110 · INEXPR 52     denominator 240
>   12:1x (§F1)         DONE 50 · OWED 134 · BLOCKED   0 · INEXPR 16     ** NO CONDITION IS BLOCKED **
>   ADDENDUM 5        DONE 57 · OWED 127 · BLOCKED   0 · INEXPR 16     level 5's 7 flash conditions
>   ADDENDUM 6        DONE 53 · OWED 131 · BLOCKED   0 · INEXPR 16     4 level-4 conditions reverted
>   ADDENDUM 7        DONE 60 · OWED 124 · BLOCKED   0 · INEXPR 16     level 5 complete: +7 flash conditions
>   LIVE (ADDENDUM 8) DONE 60 · OWED 124 · BLOCKED   0 · INEXPR 16     HC stage 1 complete: +0 (a replication; §J3)
> ```
> **Superseded by: the Captain's two words (11:4x) · ADDENDUM 2, the 503 correction (12:0x) · ADDENDUM 3,
> §B7 row 3 lifted (12:1x).** The numbers below are preserved **because a record of an observation must
> not change** — they are true *as of 11:3x* and false as a description of the matrix.
>
> ⚠️ **THIS POINTER EXISTS BECAUSE ITS ABSENCE COST SOMETHING, AND THE AUTHOR PAID IT.** On 2026-09-15
> this file's own author quoted the block below as the census's answer and routed a ⛔⛔ finding to the
> helm and all seats, asserting that the fleet map contradicted this census. **The fleet map was right.**
> The section was read, the three corrections below it were not, and the file is 311 lines.
> ⇒ 🔑 ***A SECTION THAT ASSERTS IT IS THE HEADLINE IS THE MOST LIKELY PART OF A DOCUMENT TO BE STALE,
> BECAUSE NOBODY EDITS A TITLE WHEN THEY APPEND A CORRECTION BELOW IT.*** This heading read
> "THE TOTAL, AND IT IS THE HEADLINE" and became false the moment ADDENDUM 2 landed.
> ⇒ 🔑 ***AND A DOCUMENT WITH ADDENDA HAS NO HEADLINE SECTION AT ALL — THE HEADLINE IS WHEREVER THE
> LAST ADDENDUM LEFT IT.*** Any future addendum to this file updates the box above, in the same edit.

```
  DONE (result of record, sha-pinned) ..............  50 of 240   ~21 %
  OWED (expressible, unrun) .........................  28
  BLOCKED (hold / halt / unnamed model) ............. 110   (opus brownfield 30 · flash 60 · model-4 60,
                                                             less overlaps counted once)
  INEXPRESSIBLE or pending a ruling ................. up to  52
```
⛔⛔ **THE MATRIX DOES NOT READ FULL, AND THE GAP IS NOT MOSTLY WORK — IT IS THREE DECISIONS.**
```
  1  WHICH FOURTH MODEL?                  the Captain's        60 conditions
  2  DOES §B7 row 3's HOLD LIFT?          the helm's           30 conditions (Opus brownfield)
  3  IS brownfield × spec-change A DESIGN DECISION OR A LIMITATION?   the council's   40 conditions
```
⇒ 🔑 ***130 OF THE 240 TURN ON THREE RULINGS AND NOT ON A SINGLE CELL BEING FIRED.*** **Firing everything
currently expressible and unblocked closes 28 conditions and still leaves the matrix 60 % short.**
⇒ **The arXiv update is not gated on run time. It is gated on three words that are not mine to say.**

## §C6 · WHAT THIS CENSUS DOES NOT DO
1. **It does not read every cell of the 17 results of record.** Coverage is taken from each result's own
   population statement, which is the claim each file makes about itself. **A per-cell reconciliation of
   all 17 is not done** and would be the next refinement if any count here is disputed.
2. **It marks no cell DONE that I have not seen a sha for.**
3. **It names no fourth model**, and it does not treat `models.tsv` as one.
4. **It makes no claim about RESULTS** — only about which conditions have a result of record. **Whether
   the numbers in them support any paper sentence is a separate question and is the paper seat's.**


---

# ADDENDUM 1 — **THE CAPTAIN RULED TWO OF THE THREE, 2026-09-14 11:41. THE DENOMINATOR IS 200.**
## bench, same shift, ~20 minutes after the census above. **His words, verbatim, typed to the helm:**
## *"Yes, we can skip brownfield + spec-change. Yes, fourth model is Sonnet."*

## §D1 · RECOUNTED, NOT ASSERTED
`brownfield × spec-change` leaves the denominator (**−40**) and `claude-sonnet-5` fills the fourth row.
```
  DONE            50   25.0 %        OWED            98   49.0 %
  BLOCKED         36   18.0 %        INEXPRESSIBLE   16    8.0 %        TOTAL 200
  ⛔ CORRECTED BY ADDENDUM 2: Flash's 46 were BLOCKED on a "turn stall" that was a 503. They are OWED.
  ⛔ CORRECTED AGAIN BY ADDENDUM 3: §B7 row 3 LIFTED ⇒ BLOCKED 36 → 0, OWED 98 → 134. NO BLOCKS REMAIN.

  claude-opus-5          DONE 28 · OWED  0 · BLOCKED 18 · INEXPR 4
  claude-sonnet-5        DONE  0 · OWED 28 · BLOCKED 18 · INEXPR 4    <- never run as a SUBJECT: 0 of 307 cells
  gemini-3.1-pro-high    DONE 22 · OWED 24 · BLOCKED  0 · INEXPR 4
  gemini-3.8-flash-high  DONE  0 · OWED 46 · BLOCKED  0 · INEXPR 4    <- ADDENDUM 2; SUPERSEDED BY ADDENDUM 5
```

## §D2 · ⛔⛔ NAMING THE FOURTH MODEL DOUBLED WHAT ONE UNRESOLVED HOLD COSTS
My first recount put Sonnet at **46 OWED** — i.e. *"the matrix is now a running problem."* **Then I read
the hold's own wording** (desk `LU`, the maestro's 09-13 narrowing): *"the row-3 hold binds
**CLAUDE-CLIENT** cells ONLY and does not hold agy-client brownfield, because the gap is client-local."*
⇒ **`claude-sonnet-5` IS A CLAUDE-CLIENT MODEL**, so its 18 brownfield conditions sit under the SAME hold
as Opus's 18.
```
  §B7 row 3 blocked  18 conditions   before the fourth model was named
  §B7 row 3 blocks   36 conditions   after   —  18 % of the whole matrix
```
⇒ 🔑 ***THE RULING THAT ADDED WORK AND THE RULING THAT BLOCKS IT ARE IN DIFFERENT ROWS, OWNED BY
DIFFERENT PARTIES, AND NEITHER MENTIONS THE OTHER.*** Had the scope not been checked, this census would
have reported 46 runnable Sonnet conditions and the helm would have priced its own hold at half.

## §D3 · A NEAR-MISS ON THE MODEL ID, CAUGHT AT ZERO COST, AND IT IS THE THIRD OF ITS KIND
The hand reported that `agy` serves a Sonnet and offered a one-cell probe. **Measured: `agy` serves
`claude-sonnet-4-6`; `agy models` returns 0 for `claude-sonnet-5`.** ⇒ **Two real, servable,
nearly-identically-named models, and the probe would have fired the one nobody named.** The hand
withdrew it within two minutes of offering it.
```
  --arm salt          vs  --arm salt-diet        both buildable            cost: two asks
  gemini-3.1-pro-high vs  gemini-3.8-flash-high  both served, substituted  cost: 3 VOID cells
  claude-sonnet-4-6   vs  claude-sonnet-5        both real, one unservable cost: ZERO
```
⛔⛔ **CORRECTION, SAME SHIFT, BEFORE THIS FILE LANDED — I CREDITED THE ZERO COST TO CARE AND IT WAS A
GATE.** I wrote that the Sonnet case cost nothing *"because the id was checked against the served list"*.
**Measured afterwards by the hand: the harness had ALREADY REFUSED IT.** Verbatim from the battery:
`agy_launch: REFUSE — AGY_MODEL='claude-sonnet-4-6' is not a Gemini id. The Captain ruled 2026-09-07
that agy serves GEMINI for this arm.` **The cell BUILT, the battery went RED at rc 9, and nothing
launched — no `launch.log`, no stream, no meter, no end marker. Zero model spend.**
⇒ ✅ **THREE INDEPENDENT THINGS WOULD HAVE STOPPED IT, AND THE CHEAPEST FIRED FIRST:** the hand's own
withdrawal · the lead's stand-down 90 seconds after authorising · **and a REGISTERED GATE that had been
sitting in the launcher for a week enforcing a ruling NEITHER OF US CITED.**
⇒ 🔑 ***SO THE THREE CASES DIFFER BY WHERE THE GATE SAT, NOT BY WHO WAS CAREFUL:***
```
  gate at the BATTERY   refused before launch, at BUILD time          cost ZERO      (sonnet)
  gate at the LAUNCH    the served-model assertion, per cell          cost 3 cells   (flash, caught by hand)
  gate at the METER     §F5 row 1 alone, after the pool is spent      cost 42 cells  (what flash risked)
  NO GATE               two documents disagreeing about a flag        cost two asks  (--arm salt)
```
⇒ **This is the level-5 lesson generalised one step further: *the difference between a gate at the meter
and a check at launch is 39 cells* — and the difference between a check at launch and a GATE AT THE
BATTERY is the last three.**
⇒ ⚠️ ***AND THE HUMBLING HALF: THE GATE KNEW THE ANSWER TO A QUESTION TWO SEATS SPENT TWENTY MINUTES
ARGUING.*** Neither of us asked the harness what it would accept. **Ask the instrument before debating
the answer.**
⇒ **The turn-loop probe is REGISTERED OPEN, not dropped:** it would test whether *one `result` per turn*
is a Pro-specific assumption, and it is the first act of any future cross-vendor agy wave. **Standing it
down now is the banked rule — fire the highest unblocked item first, then measure beside it.**

## §D4 · WHAT REMAINS, AND IT IS NO LONGER THREE THINGS
```
  ONE RULING      §B7 row 3 — the helm's — 36 conditions, lifts on the sandbox probe's receipt
  ONE DESIGN CALL Flash's 46 — per-turn capping for a model that runs an episode as ONE TURN
  ACTUAL WORK     52 OWED — Sonnet greenfield 28 · gemini-3.1-pro 24
```
⇒ **Firing every owed condition closes 52 and takes the matrix to 102 of 200 — barely half — because 82
sit behind one hold and one design call.** ⚠️ **A Sonnet wave is a NEW POPULATION, not a top-up: zero of
the 307 cells on the box has ever been served by a Sonnet.**


---

# ⛔⛔ ADDENDUM 2 — **THE FLASH ROW WAS WRONG: BLOCKED 82 → 36, OWED 52 → 98**
## bench, same shift. **The level-5 halt was a 503 (`No capacity available`), not a turn stall** —
## see `AMENDMENT-gemini-flash-level5-2026-09-14.md` ADDENDUM 2, which refutes the finding this census
## row was built on. **I registered that finding and merged it; the correction is mine.**
```
  was   DONE 50 · OWED 52 · BLOCKED 82 · INEXPRESSIBLE 16
  now   DONE 50 · OWED 98 · BLOCKED 36 · INEXPRESSIBLE 16
```
⇒ **BLOCKED HALVES AND THE MATRIX BECOMES MOSTLY WORK: 98 of 200 are expressible and unblocked.**
⇒ **The ONLY remaining hold is §B7 row 3's 36** (Opus 18 + Sonnet 18, both Claude-client brownfield).
⚠️ **"Retryable" is not "free":** a 503 is server capacity — **an external condition nobody here
controls, which may recur.** Flash's 46 are **OWED-WITH-A-NAMED-RISK**, not owed-and-easy.
📌 **§D4's "one ruling, one design call, actual work" now reads: ONE RULING (row 3, 36) and 98 of work.
The design call is withdrawn — there was never a design question, only a capacity error.**


---

# ✅✅ ADDENDUM 3 — **§B7 ROW 3 IS LIFTED. BLOCKED GOES 36 → 0. THE MATRIX HAS NO BLOCKS LEFT.**
## bench, same shift, ~4 minutes after ADDENDUM 2. **The helm lifted the hold on the sandbox probe's
## receipt** (`systems`' desk MQ: `7c5295e`, merged by me to `backup/master`, selftest driven 23/23).
## **Claude-client brownfield — Opus 18 + Sonnet 18 — is now bench's to pull.**

```
  DONE            50   25.0 %        OWED           134   67.0 %
  BLOCKED          0    0.0 %        INEXPRESSIBLE   16    8.0 %        TOTAL 200
```

## §F1 · THE TRAJECTORY OF ONE AFTERNOON, BECAUSE THE SHAPE IS THE LESSON
```
  11:3x   DONE 50 · OWED  28 · BLOCKED 110 · INEXPR 52     denominator 240, before the Captain
  11:4x   DONE 50 · OWED  52 · BLOCKED  82 · INEXPR 16     his two words: skip bf×spec-change, Sonnet
  12:0x   DONE 50 · OWED  98 · BLOCKED  36 · INEXPR 16     the 503 correction — Flash was never blocked
  12:1x   DONE 50 · OWED 134 · BLOCKED   0 · INEXPR 16     §B7 row 3 LIFTED on the probe's receipt
```
⇒ 🔑 ***I REPORTED AT 11:3x THAT "130 OF THE 240 TURN ON THREE RULINGS AND NOT ON A SINGLE CELL BEING
FIRED", AND THAT THE arXiv UPDATE WAS "GATED ON THREE WORDS THAT ARE NOT MINE TO SAY". ALL THREE WERE
SAID WITHIN FORTY MINUTES.*** **The census's value was not its 50 — it was naming the three decisions
precisely enough that they could be taken.** ⇒ **A census that ends in a number is a status report; one
that ends in named owners is a decision queue.**
⚠️ **AND THE HONEST HALF: one of the three "rulings" was not a decision at all — it was MY OWN
MISREADING of a 503 as a model behaviour.** It did not need a word from anyone; it needed someone to
open the `result` object. **Two were genuinely the Captain's and the helm's. I had scored my own error
as a governance gate.**

## §F2 · WHAT IS NOW TRUE OF THE MATRIX
- **NO CONDITION IS BLOCKED.** Every one of the 184 non-DONE cells is either **WORK (134)** or
  **INEXPRESSIBLE (16)**.
- **The 16 are `<any model> × Paxos × statement`**, ruled inexpressible with a reason: *an arm-neutral
  formal statement cannot exist for a proof-obligation task.* ⛔ **They are not owed and should leave any
  "percent complete" denominator that is quoted as progress.** Against the EXPRESSIBLE 184, DONE is
  **27.2 %**, not 25.0 %.
- ⚠️ **"Unblocked" is not "cheap".** 134 conditions at n=3 is ~402 cells. **Flash's 46 carry a named
  external risk (503 capacity). Sonnet's 46 are a NEW POPULATION — zero Sonnet cells exist.**
- 📌 **36 of the 134 are newly bench's** by the helm's words, and they are the first Claude-client
  brownfield cells this campaign would ever run.

## §F3 · WHAT THIS DOES NOT AUTHORISE
⛔ **No wave is authorised by this addendum.** The matrix being unblocked makes every remaining cell a
**SPEND** question rather than a governance one, and **spend is the Captain's**. ⇒ **Act (2) — the arXiv
draft — still does not begin: the census does not read full, and 134 owed conditions is not full.**

---

# ⚠️ ADDENDUM 4 — **Crc32's BROWNFIELD CONDITIONS ARE BUILDABLE AND THEY ARE A *LOUD* RUNG**
## bench, 2026-09-14. `systems` built the fifth brownfield given (PR #144, `6303467`), closing §B7 row 1
## at five of five. **This addendum records WHAT KIND of cell those conditions produce, because the
## census is what a later reader will price the matrix from.**

## §H1 · THE MEASUREMENT, WHICH IS `systems`' AND CARRIES ITS OWN CONTROL
```
  REFERENCE (control)   TESTS 6/6   margin 0/6   <- the withheld suite is VALID
  ComplementedTable     TESTS 1/6   margin 5/6
  HighByteIndex         TESTS 1/6   margin 5/6
  SevenSteps            TESTS 1/6   margin 5/6
  ShortTable            TESTS 1/6   margin 5/6
  UnreflectedPoly       TESTS 1/6   margin 5/6
  failing set IDENTICAL on all five:
     check_value · published_vectors · long_and_all_byte_values · lengths · random_cross_check
```
⭐ **The reference control is what makes the five margins mean anything** — without it, "all five at 5/6"
is equally consistent with a suite that fails five tests on everything.

## §H2 · ⛔ WHAT IT MEANS FOR THE TWO CENSUS CONDITIONS
`gemini-3.1-pro-high × brownfield × Crc32 × {plain, salt-diet}` move from **OWED-and-unbuildable** to
**OWED-and-buildable**. ⛔ **They are NOT ordinary brownfield cells:**
- **Margin 5 of a SIX-test suite is the LOUD end** of this desk's seed criterion: *every test fails, so
  the subject cannot miss the defect and the task measures nothing about localisation.*
- **No seed choice fixes it.** All five mutants are identical on the suite ⇒ **the property belongs to
  the WITHHELD SUITE, not to the mutant.** ⇒ **This is the "no discriminating seed" condition desk KT
  recorded, arriving as a number instead of a judgement.**
⇒ ⚖️ **ANY RESULT FROM THESE TWO CONDITIONS READS AS A CEILING, NEVER AS A DISCRIMINATION**, which is
exactly what the Captain's §G4 ruling asked for: *"Crc32 — RUN IT AND REPORT THE CEILING."*
⛔ **They must not be pooled with the other four brownfield problems in any arm comparison**, for the
same reason a truncated cell's cost figures are not poolable: **the cells are not measuring the same
thing, and the difference is a property of the instrument rather than of the subject.**

## ⇒ 🔑 §H3 · AND A CORRECTION OF MINE THAT BELONGS BESIDE IT
I handed `systems` this seed criterion **with a prediction wrapped around it** — *"you have a real
choice and the margins will differ across them."* **I had never opened `Crc32/G/withheld/`.** It measured
all five in six minutes and they are identical.
⇒ ***A CRITERION SURVIVES BEING WRONG ABOUT THE DATA; A PREDICTION SMUGGLED INSIDE IT DOES NOT, AND IT
DISCREDITS THE CRITERION ON THE WAY OUT.*** **The criterion held — it returned LOUD. The prediction was
mine and was worthless.**


---

# ✅ ADDENDUM 5 — **THE FLASH ROW MOVES: `DONE 0 → 7`, `OWED 46 → 39`. TOTAL `DONE 50 → 57`.**
## bench, 2026-09-15 16:3x. **The re-cut the helm asked for, and it is ONE result, not a day of cells.**

## §J1 · THE TRIGGER, STATED SO THIS FILE STOPS BEING RE-CUT ON A CLOCK
**This census moves when a RESULT OF RECORD MERGES WITH A PR SHA, and on nothing else.** That is its own
§C5/§C2 rule (*"a cell that never became a result of record is RESIDUE, NOT EVIDENCE"*), and it means a day
of cells landing on the run box **cannot** age it. Measured at the object across the full window since
this file's commit, two boundaries agreeing: **exactly one result of record has merged.**
```
  RESULT-gemini-flash-level5-2026-09-15.md    PR #147 -> 6369997    <- the only one
  HC stage 1's 11 landed cells                ZERO results of record at the time of that measurement
```

## §J2 · THE MOVE, AND THE ONE JUDGMENT IN IT
`RESULT-gemini-flash-level5-2026-09-15.md` carries **7 conditions** with a result of record:
`crc32-{plain,saltdiet}` · `freelist-{plain,saltdiet}` · `lru-{plain,saltdiet}` · `paxos-plain`.
```
  gemini-3.8-flash-high   DONE 7 · OWED 39 · BLOCKED 0 · INEXPR 4   (of its 50 in the 200-view)
  MATRIX                  DONE 57 · OWED 127 · BLOCKED 0 · INEXPR 16  = 200
```
⚖️ **THE JUDGMENT, MADE EXPLICITLY RATHER THAN BURIED IN THE ARITHMETIC: does a HALTED wave, whose own
result publishes no arm comparison, make its conditions `DONE`?** **Yes — and the reason is this file's
own §C6(4):** *"It makes no claim about RESULTS — only about which conditions have a result of record.
Whether the numbers in them support any paper sentence is a separate question and is the paper seat's."*
⇒ **`DONE` here has always meant "has a result of record", never "has a usable number".** Ruling otherwise
would silently redefine the column mid-census, which is worse than a debatable 7.
⛔⛔ **SO THE CAVEATS TRAVEL WITH THE ROW, BECAUSE A BARE `DONE 7` WOULD OVERSTATE WHAT IS IN HAND:**
```
  NO ARM COMPARISON IS PUBLISHED   the denominators are not neutral and EVERY missing cell is salt-diet,
                                   so a rate over them is measured on a treatment arm whose cells were
                                   removed by an arm-correlated mechanism (its ADDENDUM 1, verbatim)
  TWO CELLS FULL-PASSED HAVING     l5ls02 and l5ls03 did 65 s and 0 s of model work and sit inside
  DONE NO MODEL WORK               `lru-saltdiet 2 of 2`. A FULL PASS BY A CELL THAT DID NO WORK IS A
                                   FACT ABOUT THE TASK, NOT ABOUT THE MODEL.
  7 OF 14 CONDITIONS NEVER FIRED   21 cells unfired; re-firing them is a SPEND and is not a seat's call
```
⇒ 🔑 ***A CONDITION CAN BE `DONE` FOR THIS CENSUS AND USELESS TO THE PAPER, AND KEEPING THOSE TWO
QUESTIONS APART IS THE ONLY REASON THIS COLUMN MEANS ANYTHING.*** The alternative — a `DONE` that quietly
encodes "and the numbers are good" — is a column no one can audit.

## §J3 · ⛔ HC STAGE 1 ADDS **ZERO** CONDITIONS, AND I AM REPORTING IT AGAINST MY OWN CAMPAIGN
```
  the Captain's axes, verbatim   {plain, salt-diet} x {none, statement, spec-change}
                                 ==> THERE IS NO PLACEBO AXIS. HC1's placebo arm is not on this grid.
  §C4, the opus row              greenfield x {plain,salt-diet} x none x 5 problems
                                 DONE  RESULT-matrix-opus-1  9ffa1a8   (10 conditions)
  HC stage 1                     claude-opus-5 x greenfield x none, THE SAME FIVE PROBLEMS
```
⇒ ***HC STAGE 1'S 45 CELLS ARE A PRE-REGISTERED REPLICATION OF AN ALREADY-`DONE` ROW, PLUS AN ARM THAT IS
NOT ON THE GRID. A REPLICATION STRENGTHENS A `DONE` CELL; IT DOES NOT ADD ONE.***
⚠️ **This does NOT make HC1 wasted**, and the design said so in advance: §4(3) of
`PREDICTIONS-HC-stage1-2026-09-13.md` registers the replication half as deliberately low-information,
whose value is that **the cells are NEW and fired under a rule fixed in advance** — which matrix #1's
cells can never retroactively become — and whose cost receipt prices the remaining owed work.
⛔ **But it does mean HC1 IS NOT THE PATH TO `FULL`, and no one should plan as though it were.** Whether
the one serial Claude-lane worker stays on it is a CAMPAIGN question and is **reserved to the Captain**.
⚠️ **A unit confusion to retire on sight:** the phrase *"45 of the 134 owed"* counts **CELLS** against a
denominator of **CONDITIONS**. The helm has claimed that error as its own; it is recorded here because
this file is where the denominator lives.

## §J4 · THE 240- AND 200-VIEWS, PUBLISHED SIDE BY SIDE SO NOBODY DERIVES ONE AGAIN
```
                        240-view                          200-view (drops brownfield x spec-change, 40)
  DONE                        57                                57
  OWED                       127                               127
  BLOCKED                      0                                 0
  INEXPRESSIBLE               56                                16
  ------------------------------------------------------------------------------------
  TOTAL                      240                               200
```
⇒ **The two views differ ONLY in whether the 40 inexpressible `brownfield x spec-change` conditions sit
inside the denominator.** Every other figure is identical.
⚠️ **AND THE RESIDUAL THAT CAUSED A FALSE FINDING TODAY IS NAMED AND RUN DOWN TO THE CONDITION:**
deriving the 200-view from §C5's *11:3x* numbers gives `INEXPR 12` against the live `16`. **The four are
`claude-sonnet-5 × Paxos × statement`, and they did not exist at 11:3x because THE FOURTH MODEL HAD NOT
BEEN NAMED YET.**
```
  §F2: the inexpressible set is  <any model> x Paxos x statement x {greenfield,brownfield} x {plain,salt-diet}
  at 11:3x, THREE models known    3 x 2 x 2 = 12
  after the Captain named Sonnet  4 x 2 x 2 = 16      <- the entire residual, and it is not a disagreement
```
⇒ **So the gap is an artefact of deriving from a superseded snapshot, NOT a disagreement between this
file and the fleet map.** The map has been correct throughout.
⇒ 🔑 ***A DERIVED VIEW OF A TABLE IS A NEW CLAIM AND IT INHERITS THE CITATION WITHOUT INHERITING THE
CHECK.*** Both views are now published so no reader has to derive either.

## §J5 · WHAT THIS ADDENDUM DOES NOT DO
1. **It does not read the level-5 result's cells.** Coverage is that file's own population statement.
2. **It authorises no wave and no spend.** §F3 stands: spend is the Captain's.
3. **It does not make the matrix read `FULL`.** 127 owed conditions is not full, and act (2) — the arXiv
   draft — still does not begin.


---

# ⛔ ADDENDUM 6 — **FOUR CONDITIONS REVERT: `DONE 57 → 53`. THE LEVEL-4 FreeList AND LZW CELLS ARE VOID.**
## bench, 2026-09-15 18:0x. **A correction to ADDENDUM 5, made two hours after it, against my own work.**

## §K1 · WHAT MOVED AND WHY
`RESULT-gemini-brownfield-level4-2026-09-14.md` ADDENDUM 1 rules **12 of its 24 cells VOID for the
find-the-defect claim**: the FreeList and LZW brownfield givens announced their own planted defect, in
plain English, for ~57 hours — a window containing that wave. Confirmed at two different objects by three
parties, with a control that returns 0 on LRU and Paxos.
```
  gemini row, §C4   brownfield x {plain,salt-diet} x none x 4 problems  DONE  8
                    ⇒ FreeList and LZW are 2 of those 4 problems = 4 CONDITIONS
  MATRIX            DONE 57 -> 53  ·  OWED 127 -> 131  ·  BLOCKED 0  ·  INEXPR 16   = 200
```
**LRU and Paxos (the other 4 conditions) STAND and are not in doubt.**

## §K2 · ⇒ 🔑 THE LESSON IS ABOUT ADDENDUM 5, NOT ABOUT LEVEL 4
ADDENDUM 5 moved the flash row and **inherited every other row's correctness without checking it** —
including this one, which was already wrong when I wrote it two hours earlier.
⇒ ***A CENSUS RE-CUT IS NOT A RE-AUDIT. MOVING ONE ROW SILENTLY RE-ASSERTS ALL THE OTHERS, AND THE
RE-ASSERTION IS INVISIBLE BECAUSE NOTHING ABOUT THOSE ROWS CHANGED IN THE DIFF.***
⚠️ This is the DERIVED-VIEW defect one level up, and it is the third instance today: a derived view
inherits its source's citation without inheriting its source's check.
✅ **The form that would have caught it:** a re-cut states, per row, whether it was RE-VERIFIED or
CARRIED. This census now owes that column and does not yet have it — **declared, not quietly fixed.**

## §K3 · WHAT THIS DOES NOT DO
1. It does not re-fire anything; re-firing 12 cells is a SPEND and is the Captain's.
2. It does not touch HC stage 1, which is **greenfield** — no brownfield given, no planted defect.
3. It does not make the matrix read `FULL`. 131 owed conditions is further from full than 127 was, and
   **that is the honest direction.**


---

# ✅ ADDENDUM 7 — **LEVEL 5 COMPLETES: `DONE 53 → 60`, FLASH `7 → 14`**
## bench, 2026-09-16. **Moved in the SAME COMMIT as the result of record it counts**, so the two land
## under one sha and this census never reads ahead of its evidence. ⚠️ The first draft of this line said
## "moved because a result of record merged" — untrue at the moment of writing, since that result is in
## this commit. Atomic landing is the stronger guarantee and the accurate one.

## §M1 · THE ARITHMETIC, WITH ITS REASONING, BECAUSE A BARE NUMBER HERE HAS BEEN WRONG BEFORE
ADDENDUM 5 counted **7** flash conditions, all under the `none` treatment:
`crc32-{plain,saltdiet}` · `freelist-{plain,saltdiet}` · `lru-{plain,saltdiet}` · `paxos-plain`.
The completed wave (`RESULT-gemini-flash-level5-2026-09-15.md` ADDENDUM 3) carries nine conditions:
```
  paxos-saltdiet (none)          NOT among the 7                                  +1
  6 statement conditions         statement IS a registered axis; only
    crc32/freelist/lru           Paxos x statement is inexpressible               +6
    x {plain, salt-diet}
  lru-saltdiet, paxos-plain      re-fires of conditions ALREADY counted; they
    (re-fires)                   replace contaminated cells, they add none         0
  ----------------------------------------------------------------------------------
                                                                                   +7
  gemini-3.8-flash-high   DONE 14 · OWED 32 · BLOCKED 0 · INEXPR 4   (of its 50 in the 200-view)
  MATRIX                  DONE 60 · OWED 124 · BLOCKED 0 · INEXPR 16  = 200
```

## §M2 · ⛔ SIX OF THE SEVEN ARE DONE AND CANNOT DISCRIMINATE, AND THE COLUMN MUST NOT HIDE IT
The six statement conditions are `DONE` by this file's rule — **`DONE` means "has a result of record",
never "has a usable number"** (§C6(4)). **All six sit at a pass-rate CEILING** (18 of 18 cells passed
every test). ⇒ **They count toward `FULL`. They contribute no arm contrast on pass rate.**
⇒ 🔑 ***A MATRIX CAN READ FULL AND STILL BE UNABLE TO ANSWER THE QUESTION IT WAS BUILT FOR.*** The
census tracks coverage; whether coverage yields a comparison is the paper's question, and this addendum
records the gap rather than letting the count close it silently.

## §M3 · WHAT THIS DOES NOT DO
1. It authorises no spend. 2. It does not make the matrix read `FULL`: 124 owed conditions is not full.
3. It does not revisit the level-4 void of ADDENDUM 6, which stands.


---

# ✅ ADDENDUM 8 — **HC STAGE 1 COMPLETES: THE COUNT DOES NOT MOVE, `DONE 60 · OWED 124 · INEXPR 16`**
## bench, 2026-09-16. **Re-cut at the stage's completion and landed in the SAME COMMIT as its result of record**
## (`RESULT-HC1-stage1-2026-09-16.md`), per council 2026-09-16 ⑤d.

## §N1 · WHY +0, CHECKED AGAINST §J3 RATHER THAN ASSUMED
HC stage 1 fired 45 `claude-opus-5 × greenfield × none` cells over the five problems, in plain, placebo and salt-diet arms.
```
  claude-opus-5 x greenfield x {plain,salt-diet} x none x 5 problems   DONE since RESULT-matrix-opus-1   (10 conditions, §C4)
  the placebo arm                                                       NOT ON THE GRID                  (§J3: no placebo axis)
```
⇒ **Every stage-1 cell falls in an already-DONE condition or off the grid. MATRIX: DONE 60 · OWED 124 · BLOCKED 0 ·
INEXPR 16 = 200, unchanged.** The row's `DONE` now carries a pre-registered replication at n = 3: 10 of 10 medians inside
their bands in the grid arms (15 of 15 with placebo). The premium RESOLVED on FreeList, was CENSORED on Paxos, and was
UNRESOLVED as registered on Crc32, LRU and LZW.

## §N2 · ⛔ A DISTINCTION THIS FILE'S COLUMNS CANNOT YET CARRY, RECORDED RATHER THAN ENCODED
Stage 1's UNRESOLVED premiums are of two kinds, and **neither is a measured null**: **censored by the cost cap** (Paxos),
and **registered as unresolvable at n = 3** (Crc32, LRU, LZW). **This census's `DONE` column does not distinguish them, and neither
does a grid cell reading UNRESOLVED.** Whether it should, and how the paper counts them, is on the 2026-09-17 agenda. **No
column is added here**, because adding one mid-census would redefine the table (the reasoning of §C6(4)).

## §N3 · WHAT THIS DOES NOT DO
1. **It authorises no spend.** What the Claude lane fires next (stage 2 or the owed Claude-lane conditions) is the
   Captain's call, docketed for 2026-09-17.
2. **It re-verifies no other row.** Every row other than `claude-opus-5 × greenfield × none` is CARRIED from ADDENDUM 7, and
   §K2's RE-VERIFIED/CARRIED column is still owed and still not built.
3. **It does not make the matrix read `FULL`:** 124 conditions are owed.
