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
>   ADDENDUM 8        DONE 60 · OWED 124 · BLOCKED   0 · INEXPR 16     HC stage 1 complete: +0 (a replication; §J3)
>   ADDENDUM 9        DONE 72 · OWED 112 · BLOCKED   0 · INEXPR 16     level 6 complete: +12
>   ADDENDUM 10       DONE 99 · OWED  85 · BLOCKED   0 · INEXPR 16     level 7 complete: +27 (§Q1)
>   LIVE (ADDENDUM 11) DONE 109 · OWED 75 · BLOCKED   0 · INEXPR 16    block SB complete: +10 (§R1)
> ```
> ⛔⛔ **THE `ADDENDUM 9` ROW ABOVE WAS ADDED ON 2026-09-19 BY ADDENDUM 10, TWO DAYS LATE. FOR THOSE TWO DAYS
> THIS BOX'S `LIVE` ROW READ `DONE 60` WHILE THE FILE'S LIVE FIGURE WAS `DONE 72`** — a whole level behind,
> in the one table this section declares to be the only current figure in the document.
> ⇒ 🔑 ***THE INSTRUMENT BUILT TO STOP A STALE HEADLINE WENT STALE, AND THE SENTENCE THAT WAS SUPPOSED TO
> PREVENT IT — "Any future addendum to this file updates the box above, in the same edit" — IS THE
> INSTRUCTION ITS OWN AUTHOR DID NOT FOLLOW IN THE VERY NEXT ADDENDUM.***
> ⚠️ **AND THE SELF-DESCRIPTION IS WHAT MADE IT INVISIBLE: the paragraph below claims the `LIVE` row is
> always current "as a property of the FORM rather than of anyone remembering to re-point a sentence."
> It is not. The row is appended BY HAND, so it is exactly as reliable as remembering — and the claim that
> it is structural is what stops a reader checking it.** ⇒ ***A FORM THAT DEPENDS ON A HABIT WHILE
> ADVERTISING THAT IT DOES NOT IS WORSE THAN A HABIT, BECAUSE IT SPENDS THE READER'S SUSPICION.***
> ✅ **The trajectory rows are now DERIVABLE: each addendum's own headline states its before→after, so a
> reader who distrusts this box can rebuild it from the `ADDENDUM n` headings alone.** That is the check
> this box should have had, and it does not require anyone to remember anything.
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


---

# ✅ ADDENDUM 9 — **LEVEL 6 COMPLETES: `DONE 60 → 72`, `OWED 124 → 112`**
## bench, 2026-09-17. **Landed in the SAME COMMIT as its result of record** (`RESULT-gemini-level6-2026-09-17.md`),
## per council 2026-09-16 ⑤d, so this census never reads ahead of its evidence.

## §P1 · THE ARITHMETIC, MAPPED CONDITION BY CONDITION ONTO §C4 RATHER THAN ASSERTED
Level 6 fired **12 conditions × n=3 = 36 cells** (35 in series `l6v` + the `l6u` sentry cell `l6uspq01`,
which the 09-16 18:56 ruling kept as cell 1). **Every one of the twelve was `OWED` in §C4 — none was
already `DONE`, and none was inexpressible:**
```
  gemini-3.1-pro-high    greenfield x LZW x {plain,salt-diet} x none        §C4 "LZW OWED 2"        +2
                         greenfield x LZW x {plain,salt-diet} x statement   §C4 "LZW OWED 2"        +2
  gemini-3.8-flash-high  greenfield x LZW x {plain,salt-diet} x none        of §C4 flash "LZW 4"    +2
                         greenfield x LZW x {plain,salt-diet} x statement   of §C4 flash "LZW 4"    +2
                         brownfield x LRU x {plain,salt-diet} x none        of §C4 flash "bf 18"    +2
                         brownfield x Paxos x {plain,salt-diet} x none      of §C4 flash "bf 18"    +2
  ------------------------------------------------------------------------------------------------------
                                                                                                   +12
  per model      gemini-3.1-pro-high  DONE +4       gemini-3.8-flash-high  DONE +8
  MATRIX         DONE 72 · OWED 112 · BLOCKED 0 · INEXPR 16  = 200
```
⇒ **72 + 112 + 0 + 16 = 200.** The 240-view differs only by the 40 inexpressible `brownfield × spec-change`
conditions, exactly as §J4 published: **240-view `DONE 72 · OWED 112 · BLOCKED 0 · INEXPR 56`.**
📌 **No per-model TOTAL is restated here, only the delta.** §C4's per-model rows annotate some conditions
as both `OWED` and `INEXPRESSIBLE`, so a per-model total derived from them is a new claim — and §J4's own
rule is that a derived view inherits the citation without inheriting the check.

## §P2 · ⛔ `DONE` HERE MEANS A RESULT OF RECORD, AND ONE OF THE TWELVE CARRIES A VOID CELL
`gemini-3.8-flash-high × greenfield × LZW × salt-diet × none` is `DONE` on **2 of its 3 cells**:
`l6vgfs02` is VOID — `P-DELIVERY no`, the arm never reached the subject, 0 shell calls in 14 turns, no
`LANDING.md`, and the untouched starting `solution.rs`. **It is not a failure and enters no pass/fail
denominator.** By §C6(4)'s rule the condition is `DONE` — it has a result of record — and the result
names the void. ⇒ **The column cannot show it, so it is written here.**

## §P3 · ⚠️ THESE STATEMENT CONDITIONS **DO** DISCRIMINATE — WHICH IS THE OPPOSITE OF ADDENDUM 7 §M2
Four of the twelve are `statement` conditions (block S). **Unlike level 5's six, they are NOT at the
pass ceiling:**
```
  block S (statement)        plain 6/6    salt-diet 4 of 6
  block B (brownfield)       plain 6/6    salt-diet 6 of 6
  block G (greenfield bare)  plain 6/6    salt-diet 4 of 5   <- l6vgfs02 is VOID and is in no denominator
```
⛔ **The denominator is SCORABLE cells, never declared cells.** Block G's salt-diet condition declared 3 cells of
which `l6vgfs02` is VOID (the arm was never delivered), so its rate is **4 of 5**. **This table's first draft
printed `4/6` and its block denominators then summed to 18 against the result's own 17** — a void ruled in prose
and spent in a table. *(Found by the 90th helm head at signature; the direction was conservative.)*
⇒ **Level 6 is the first wave in this census whose `DONE` conditions carry an arm contrast on pass rate
rather than a shared ceiling.** ADDENDUM 7 §M2 recorded that level 5's statement conditions counted
toward coverage and could not discriminate; **that is a fact about those cells, not about the statement
axis**, and this addendum is the counter-example. ⛔ **n = 3 per condition: this is a contrast in the
record, not an estimate, and no interval is claimed.**
⚠️ **The first draft of this section said "at or near the pass ceiling (block S: 11 of 12)". Both halves
were wrong** — the count is 10 of 12, and the failures are entirely on one arm, which is the opposite
of a ceiling. It was carried forward from §M2's shape instead of being measured. ⇒ ***A SECTION COPIED
FROM THE LAST ADDENDUM INHERITS ITS CONCLUSION, AND THE NUMBER GETS FITTED TO IT.***

## §P4 · WHAT THIS DOES NOT DO
1. **It authorises no spend.** What fires next is the Captain's call.
2. **It re-verifies no other row.** Every row but the twelve above is CARRIED from ADDENDUM 8, and
   §K2's RE-VERIFIED/CARRIED column is still owed and still not built.
3. **It does not make the matrix read `FULL`:** 112 conditions are owed.
4. **It does not revisit** the level-4 void of ADDENDUM 6, which stands.

---
# ✅✅ ADDENDUM 10 — **LEVEL 7 COMPLETES: `DONE 72 → 99`, `OWED 112 → 85`. THE LARGEST SINGLE MOVE THIS CENSUS HAS MADE.**
## bench, 2026-09-19. **Landed in the SAME COMMIT as its result of record** (`RESULT-gemini-level7-2026-09-19.md`),
## per council 2026-09-16 ⑤d, so this census never reads ahead of its evidence.
## ⚠️ It also repairs the `§C5` trajectory box, whose `LIVE` row had been two days and one whole level stale. See the box.

## §Q1 · THE ARITHMETIC, MAPPED CONDITION BY CONDITION ONTO §C4 RATHER THAN ASSERTED
Level 7 fired **28 conditions / 84 cells** (blocks BN · BS · C, export `9bfb6ef86a36`). **Twenty-seven of
the twenty-eight move to `DONE`; one does not, and §Q2 is why.** Every one of the twenty-seven was `OWED`
in §C4 — **none was already `DONE`, none was inexpressible, and none is a replication**:
```
  gemini-3.1-pro-high    brownfield x FreeList x {plain,salt} x none      §C4 + ADDENDUM 6's revert   +2
                         brownfield x LZW      x {plain,salt} x none      §C4 + ADDENDUM 6's revert   +2
                         brownfield x Crc32    x {plain,salt} x none      §C4 "Crc32 OWED 2"          +2
                         brownfield x FreeList x {plain,salt} x statement of §C4 "bf x stmt OWED 10"  +2
                         brownfield x LRU      x {plain,salt} x statement          "                  +2
                         brownfield x LZW      x {plain,salt} x statement          "                  +2
                         brownfield x Crc32    x {plain,salt} x statement          "                  +2
  gemini-3.8-flash-high  brownfield x FreeList x {plain,salt} x none      of §C4 flash "bf 18"        +2
                         brownfield x LZW      x {plain,salt} x none               "                  +2
                         brownfield x Crc32    x {plain,salt} x none               "                  +2
                         brownfield x FreeList x {plain,salt} x statement          "                  +2
                         brownfield x LRU      x {plain,salt} x statement          "                  +2
                         brownfield x LZW      x {plain,salt} x statement          "                  +2
                         brownfield x Crc32    x {plain}      x statement          "                  +1
                         brownfield x Crc32    x {salt-diet}  x statement  ⛔ STAYS OWED — §Q2         +0
  ---------------------------------------------------------------------------------------------------------
                                                                                                     +27
  per model      gemini-3.1-pro-high  DONE +14      gemini-3.8-flash-high  DONE +13
  MATRIX         DONE 99 · OWED 85 · BLOCKED 0 · INEXPR 16  = 200
```
⇒ **99 + 85 + 0 + 16 = 200.** The 240-view differs only by the 40 inexpressible `brownfield × spec-change`
conditions, exactly as §J4 published: **240-view `DONE 99 · OWED 85 · BLOCKED 0 · INEXPR 56`** (= 240).
📌 **No per-model TOTAL is restated**, for ADDENDUM 9 §P1's reason: §C4's per-model rows annotate some
conditions as both `OWED` and `INEXPRESSIBLE`, so a per-model total derived from them is a new claim.

## §Q2 · ⛔ THE TWENTY-EIGHTH CONDITION RAN **1 OF 3 CELLS** AND IS NOT `DONE`
`gemini-3.8-flash-high × brownfield × Crc32 × salt-diet × statement` declared 3 cells and ran one. The wave
**refused** to launch the other two on a credential window and said so correctly in its own log; the chain,
the leg supervisor, the driver and harvest arm 4 all reported GREEN (`RESULT-…-level7…` §2 has all ten
receipts, three one-line detectors, and the mechanism).
⇒ **IT STAYS `OWED`, AT n = 1 OF 3.** The scored cell (`l7cfss01`, LANDED, PASS 6/6) is recorded and reusable.
⛔ **THE PRECEDENT IS THIS FILE'S OWN, NOT A JUDGMENT INVENTED TODAY:** §C4's flash row was held on exactly
the ground that *"⛔ n = 1 on the Flash side"* was not a condition. **Counting it `DONE` would let the matrix
read fuller than the evidence on the one axis the Captain reads it for.** One cell is not a condition.
⚠️ **AND IT IS THE CHEAP KIND OF OWED:** it needs two cells, not a wave. Whoever fires them re-cuts this row.

## §Q3 · ⭐ WHAT IS NOW STRUCTURALLY TRUE, AND IT IS A *DERIVED* VIEW — CITED, NOT ASSERTED
**Both Gemini models' BROWNFIELD halves are now essentially complete**, which no model's was before today.
Per model the 200-view carries 20 brownfield conditions (5 problems × 2 arms × {none, statement}), of which
Paxos × statement (2) is `INEXPRESSIBLE` ⇒ **18 expressible**:
```
  gemini-3.1-pro-high    none      LRU · Paxos      level 4      (§C4; ADDENDUM 6 kept these four)    4
                                   FreeList · LZW · Crc32   level 7                                   6
                         statement FreeList · LRU · LZW · Crc32  level 7                              8
                                                                              ⇒ 18 of 18   COMPLETE
  gemini-3.8-flash-high  none      LRU · Paxos      level 6      (ADDENDUM 9 §P1)                      4
                                   FreeList · LZW · Crc32   level 7                                   6
                         statement FreeList · LRU · LZW   level 7                                     6
                                   Crc32 plain      level 7 · Crc32 salt-diet OWED (§Q2)              1
                                                                              ⇒ 17 of 18
```
⚠️ **STATED AS DERIVED, AND THE REASON MATTERS:** §J4's own rule is that *a derived view inherits the
citation without inheriting the check*. This one rests on §C4 + ADDENDUM 6 + ADDENDUM 9 §P1 + §Q1, each
named above, **and I have not re-verified level 4's or level 6's conditions at their own objects today.**
It is a map of where the matrix now stands, not a re-audit of the rows it stands on.

## §Q4 · ⛔ `DONE` MEANS A RESULT OF RECORD, AND THREE OF THE TWENTY-SEVEN CARRY A NAMED LOSS
Per §C6(4) a condition with a result of record is `DONE` and the result names its voids. **The column
cannot show these, so they are written here:**
```
  gemini-3.1-pro-high x brownfield x Crc32 x salt-diet x none       DONE on 2 of 3 cells — l7cpbs03 is
    VOID(NO-BRIEFING): the arm never reached the subject (done_reason NO-FIRST-RESULT, ARM-NOT-RECEIVED).
    ⚠️ It burned 9,956,601 T and is in no pass denominator and no cost pool. Same mechanism as level 6's
    l6vgfs02 (ADDENDUM 9 §P2) — the standing receipt gate, NOT one of the amendment's §K7 void rows.
  gemini-3.1-pro-high x brownfield x FreeList x salt-diet x none    3 of 3 SCORABLE; 2 cells LANDED.
  gemini-3.1-pro-high x brownfield x LZW      x salt-diet x none    3 of 3 SCORABLE; 2 cells LANDED,
    2 TRUNCATED by the per-turn deadline (pass/fail stands as a floor; token/turn/wall not poolable).
```
⛔ **AND A STANDING CONFOUND THAT TRAVELS WITH EVERY ONE OF THESE 27 ROWS:** all ten TRUNCATED / SELF-NOT /
PERSIST-INDETERMINATE / false_done cells in level 7 are **Pro · salt-diet** — ten of ten, zero plain, zero
Flash. **The cap is arm-correlated, so no pass-rate contrast on the Pro row survives it**, and the result
of record makes none. `DONE` here means *measured and written down*, never *resolved*.

## §Q5 · WHAT THIS ADDENDUM DOES NOT DO
1. **It authorises no spend.** What fires next is the Captain's call; level 8 is 20 conditions / 60 cells
   and is gated on its export being named, not on this file.
2. **It re-verifies no other row.** Every row but the twenty-seven above is CARRIED from ADDENDUM 9, and
   §K2's RE-VERIFIED/CARRIED column is still owed and still not built — **four addenda running.**
3. **It does not make the matrix read `FULL`:** **85 conditions are owed**, and every one of them is
   greenfield × spec-change, a Flash or Pro greenfield gap, the unnamed fourth model's 50, or §Q2's one cell-pair.
4. **It does not revisit** the level-4 void of ADDENDUM 6, which stands.
5. **It claims no arm result.** §1 and §Q4 say why: three of the four (model × arm) quadrants are at the
   pass ceiling and the fourth is confounded by an arm-correlated cap.

---
# ✅✅ ADDENDUM 11 — **BLOCK SB COMPLETES: `DONE 99 → 109`, `OWED 85 → 75`. THE CLAUDE LANE'S FIRST BROWNFIELD CONDITIONS.**
## bench, 2026-09-19. **Landed in the SAME COMMIT as its result of record** (`RESULT-claude-blockSB-2026-09-19.md`),
## per council 2026-09-16 ⑤d, so this census never reads ahead of its evidence.
## ⚠️ The `§C5` trajectory box is appended to in this same edit — ADDENDUM 10's own finding, applied to itself.

## §R1 · THE ARITHMETIC, MAPPED CONDITION BY CONDITION ONTO §C4 RATHER THAN ASSERTED
Block SB fired **10 conditions / 30 cells** (`claude-opus-5`, export `283362105d75`). **All ten move to `DONE`.**
Every one was `OWED` in §C4 — **none was already `DONE`, none is inexpressible, and none is a replication**:
```
  claude-opus-5   brownfield x Crc32    x {plain,salt-diet} x none    §C4 "brownfield x everything" 30,   +2
                  brownfield x FreeList x {plain,salt-diet} x none    BLOCKED until ADDENDUM 3 lifted     +2
                  brownfield x LRU      x {plain,salt-diet} x none    §B7 row 3, then OWED                +2
                  brownfield x LZW      x {plain,salt-diet} x none              "                        +2
                  brownfield x Paxos    x {plain,salt-diet} x none              "                        +2
  ---------------------------------------------------------------------------------------------------------
                                                                                                        +10
  MATRIX         DONE 109 · OWED 75 · BLOCKED 0 · INEXPR 16  = 200
```
⇒ **109 + 75 + 0 + 16 = 200.** The 240-view differs only by the 40 inexpressible `brownfield × spec-change`
conditions, exactly as §J4 published: **240-view `DONE 109 · OWED 75 · BLOCKED 0 · INEXPR 56`** (= 240).
✅ **CHECKED RATHER THAN ASSUMED, because HC stage 1 is the near-miss:** ADDENDUM 8 moved **+0** for
`claude-opus-5` on §J3's replication rule. **Its 45 cells were `greenfield × none` (§N1, verbatim), not
brownfield** — so these ten are not that population and are not a replication of it.
📌 **No per-model TOTAL is restated**, for ADDENDUM 9 §P1's reason: §C4's per-model rows annotate some
conditions as both `OWED` and `INEXPRESSIBLE`, so a per-model total derived from them is a new claim.

## §R2 · ⭐ WHAT IS NOW STRUCTURALLY TRUE — AND IT IS A *DERIVED* VIEW, CITED, NOT ASSERTED
`claude-opus-5` carries 20 brownfield conditions in the 200-view (5 problems × 2 arms × {none, statement}).
**Block SB completes the `none` half: 10 of 10.** The `statement` half — 10 conditions — **stays `OWED`.**
⇒ **This is the first BROWNFIELD evidence of any kind on the Claude lane**, whose row was BLOCKED in its
entirety from §C4 until ADDENDUM 3.
⚠️ **STATED AS DERIVED:** it rests on §C4 + ADDENDUM 3 + §R1, each named, **and I have not re-verified the
Claude lane's greenfield conditions at their own objects today.** §J4's rule applies — *a derived view
inherits the citation without inheriting the check.*

## §R3 · ⛔⛔ `DONE` HERE MEANS A RESULT OF RECORD, AND ALL TEN CARRY THE SAME NAMED LIMIT
Per §C6(4) a condition with a result of record is `DONE`, and the result names its limits. **The column
cannot show these, so they are written here:**
```
  ALL TEN    the suite pass rate is a TOTAL CEILING (30/30) and V1 bugs_fixed is ALSO at ceiling (30/30)
             ⇒ NEITHER DISCRIMINATES THE ARMS. These ten conditions are DONE and they RESOLVE NOTHING
               about plain vs salt-diet on correctness. `DONE` is a claim about EVIDENCE EXISTING.
  ALL TEN    `bugs_introduced` is a FLOOR on every row (`>=0 (suite-limited)`), never a measurement.
  4 CELLS    across the FreeList and Paxos salt-diet conditions, CENSORED at the cost cap; 0 plain cells
             were. Every cost figure in the result is a LOWER BOUND, and a cap that binds one arm is
             part of that arm's treatment (result §6).
  ALL TEN    the registered brownfield primary separator (§B5 `retained`) separates the arms DISJOINTLY
             on 5 of 5 problems, and the result's §5 establishes it is reading GROWTH rather than
             rewriting. ⛔ NO ARM CLAIM RESTS ON IT HERE, and whether the separator's MEANING changes
             is the Captain's, not this census's.
```
⛔ **AND ONE THING THAT DID *NOT* HAPPEN, RECORDED BECAUSE IT NEARLY DID:** the first scoring pass returned
18 of these 30 cells as `class REFUSED`, which reading rule §241 item 6 would have entered here as
`VOID(GIVEN)` — a finding **against the harness**. **It was the scoring invocation's seed tree, not the
cells** (result §2). ⇒ 🔑 ***A CENSUS IS DOWNSTREAM OF AN INVOCATION, AND AN INVOCATION DEFECT ARRIVES
WEARING THE CLOTHES OF A FINDING ABOUT THE SUBJECT.***

## §R4 · WHAT THIS ADDENDUM DOES NOT DO
1. **It authorises no spend.** What the Claude lane fires next — its 10 owed `brownfield × statement`
   conditions — is not decided here.
2. **It re-verifies no other row.** Every row other than `claude-opus-5 × brownfield × none` is CARRIED
   from ADDENDUM 10, and §K2's RE-VERIFIED/CARRIED column is still owed and still not built.
3. **It does not make the matrix read `FULL`:** **75 conditions are owed.**
4. **It does not touch level 7's rows.** The `surv`/`growth` question the result's §8 item 6 raises about
   level 7 is UNMEASURED; if it lands, it changes that result's §1 wording and not these counts.

## ⚠️ RIDER TO ADDENDUM 11 — **THE CENSUS IS APPEND-ONLY APART FROM §C5's SINGLE `LIVE` MARKER LINE, AND IT CANNOT BE OTHERWISE.** APPENDED BELOW THE SIGNED TEXT; §R1–§R4 and every figure untouched.
*bench (lead), 2026-09-19, on `systems`' finding (A) at its non-author signature of block SB. **It moves no number.**
Recorded because the next non-author to run the byte-prefix test gets a ⛔ and must re-derive all of this — `systems` did,
and it was the most expensive thing in its shift.*
```
  the byte-prefix test FAILS at char 9,527, line 122, and the whole delta is ONE RELABELLED LINE:
     OLD  >   LIVE (ADDENDUM 10) DONE 99 · OWED 85 · ...
     NEW  >   ADDENDUM 10       DONE 99 · OWED  85 · ...     <- relabelled, length delta 0 bytes
     NEW  >   LIVE (ADDENDUM 11) DONE 109 · OWED 75 · ...    <- appended
  100 % BYTE CUSTODY OF THE OLD FILE:  prefix 9,521 B + the relabelled line 102 B + suffix 43,812 B
                                       + 2 newlines = 53,437 B = the old file, EXACT
  NUMERIC CONTENT OF THE RELABELLED LINE: identical both sides — ['10','99','85','0','16','7','27','1']
```
⇒ 🔑 ***THE APPEND-ONLY CLAIM HOLDS FOR EVERY FIGURE AND NOT FOR THE FILE — AND IT CANNOT HOLD FOR THE FILE, BECAUSE
THE `LIVE` MARKER IS BY CONSTRUCTION A MOVING LABEL.*** §C5 exists to guarantee that *the `LIVE` row is always last and
always current*; a marker that never moved would be the defect §C5 was written to prevent. **The document's
self-description ("appended to at every addendum") and the invariant its own verifier needs are both working as
intended and they contradict each other**, which is exactly why no author would find it.
✅ **THE FORM FOR ANY FUTURE ADDENDUM TO THIS FILE:** the byte-prefix test is expected to fail at, and ONLY at, §C5's
`LIVE` line. **A failure anywhere else is a real one.** State it that way rather than claiming append-only bare.

# ⚠️⚠️ ADDENDUM 12 — **ADDENDUM 11 ATTRIBUTED BLOCK SB'S TEN CONDITIONS TO THE WRONG MODEL. THEY ARE `claude-sonnet-5`, NOT `claude-opus-5`. THE MATRIX TOTALS DO NOT MOVE.**
## bench, 2026-09-20, on the 109th helm head's routed finding, re-driven at my own receipts before acceptance.

**ADDENDUM 11 reads:** *"Block SB fired 10 conditions / 30 cells (`claude-opus-5`, export `283362105d75`)"*, and names `claude-opus-5` on each of its condition rows. **Every one of those should read `claude-sonnet-5`.**
```
  MEASURED, each at the object
    served-clbb*.out          30 of 30 carry claude-sonnet-5 · 0 carry claude-opus-5
    CONTROL                   the O block's 17 served files DO carry claude-opus-5 (the needle works)
    clb_chain.v5.sh:69        case "$1" in O|OS) m=opus;; *) m=sonnet;; esac  ⇒ SB fires Sonnet BY CONSTRUCTION
    AMENDMENT-claude-lane-B   :279 "Sonnet 46 = SG+SB+SS+SBS+SC" · :712 "SB = Sonnet brownfield none"
```
✅ **WHAT DOES NOT MOVE, AND IT IS MOST OF THE ADDENDUM:** `DONE 99 → 109` and `OWED 85 → 75` **STAND**; the matrix line stays **`DONE 109 · OWED 75 · BLOCKED 0 · INEXPR 16 = 200`** and the 240-view stays `DONE 109 · OWED 75 · BLOCKED 0 · INEXPR 56`. **Ten conditions are done either way** — the correction moves which MODEL ROW they are counted in, and changes no total, no cell, and no verdict.
✅ **`THE CLAUDE LANE'S FIRST BROWNFIELD CONDITIONS` also stands** — that claim was never about the model.
⚠️ **The fleet-wide per-model split that follows from this (`Opus 28 · Sonnet 10` in place of `38 · 0`) is the helm's derivation and is quoted, not re-derived by me.** My measurement is confined to block SB's 30 cells.

⛔⛔ **WHY IT SURVIVED, AND WHY THE REMEDY IS A COLUMN RATHER THAN CARE:** the result's `-cells.tsv` carries **24 columns and no model column**, so its `verify.py` re-derives every published figure from a table in which the subject model does not appear. The result was also **never signed** (`NON-AUTHOR SIGNATURE — OWED`). ⇒ 🔑 ***THE MODEL WAS STATED ONLY IN PROSE, AND EVERY INSTRUMENT WE BUILT READS THE TABLE.*** ✅ **Owed: a `model_served` column derived from the `served-*.out` receipts, plus a `verify.py` arm reading it against the prose — landed BEFORE the SG · SS · SBS results are written, which is while they are still cheap.**
📌 **The erratum on the result itself is `RESULT-claude-blockSB-2026-09-19.md` §E1, appended below its prior text; nothing above it was edited, here or there.**

---
# ✅✅ ADDENDUM 13 — **BLOCK O COMPLETES: `DONE 109 → 119`, `OWED 75 → 65`. THE OPUS BROWNFIELD ROW OPENS.**
## bench, 2026-09-21. **Landed in the SAME COMMIT as its result of record** (`RESULT-claude-blockO-2026-09-21.md`),
## per council 2026-09-16 ⑤d, so this census never reads ahead of its evidence.

## §S1 · THE ARITHMETIC, MAPPED CONDITION BY CONDITION RATHER THAN ASSERTED
Block O fired **10 conditions / 30 cells** (`claude-opus-5`, export `283362105d75`). **All ten move to `DONE`.**
Every one was `OWED`; none was already `DONE`, none is inexpressible, and none is a replication:
```
  claude-opus-5   brownfield x Crc32    x {plain,salt-diet} x none    §C4 "brownfield x everything" 30,   +2
                  brownfield x FreeList x {plain,salt-diet} x none    BLOCKED until ADDENDUM 3 lifted     +2
                  brownfield x LRU      x {plain,salt-diet} x none    then OWED                           +2
                  brownfield x LZW      x {plain,salt-diet} x none              "                        +2
                  brownfield x Paxos    x {plain,salt-diet} x none              "                        +2
  ---------------------------------------------------------------------------------------------------------
                                                                                                        +10
  MATRIX         DONE 119 · OWED 65 · BLOCKED 0 · INEXPR 16  = 200
```
⇒ **119 + 65 + 0 + 16 = 200.** The 240-view is `DONE 119 · OWED 65 · BLOCKED 0 · INEXPR 56` (= 240).

## §S2 · ⛔ THE MODEL IS DERIVED, NOT TAKEN FROM THE BLOCK NAME — AND THAT IS ADDENDUM 12's REMEDY IN USE
`model_served_v3.py` reads each cell's own `served-<cell>.out`: **30 of 30 served `claude-opus-5`**, and the
model is **column 25 of the table of record**. ⇒ **ADDENDUM 12 had to correct block SB's attribution after the
fact because the 24-column table carried no model column and the verifier could not see the one field that was
wrong.** Block O's verifier carries an arm that reddens on a wrong model, driven.
⚠️ **The cells' SIDECHAIN is mixed by the subject's own choice** (a `worker-sonnet` role appears in several
receipts). **The attribution above is the HEAD model**, which is what a condition's model row means.

## §S3 · WHAT THE BLOCK FOUND, IN ONE LINE EACH — THE ARGUMENT IS IN THE RESULT, NOT HERE
```
  correctness  suite PASS 30 of 30, both arms, every problem; V1 fixes the FULL complement everywhere.
               ⚠️ A SATURATED MEASURE: it cannot rank the arms, and that is its limit, not a finding.
  retention    `retained` separates the arms with NO overlap (plain 0.263–0.872 · salt-diet 0.041–0.222)
               while `surv` OVERLAPS (0.305–0.958 · 0.360–0.755) and `growth` is DISJOINT (≤3.00x · ≥5.16x).
               ⇒ the separator is reading GROWTH, not survival — block SB's §5 shape, at a second model.
  cost         salt-diet median $19.07 vs plain $10.11 (1.89x), and it is a LOWER BOUND: one cell is
               CAP-COST censored at the $37.21 cap and still passes 7/7.
```

## §S4 · WHAT THIS ADDENDUM DOES NOT DO
- **It does not touch any other block.** SG · SS · SBS · OS are harvested, scored and have tables of record,
  and each still owes its own result. They are **not** moved here.
- **It makes no claim about the salt METHOD.** These are `plain` vs `salt-diet` arms on brownfield givens.
- **It does not re-verify any earlier block**, and it does not restate a per-model total (ADDENDUM 9 §P1's rule).

---
# ✅✅ ADDENDUM 14 — **BLOCK SG COMPLETES: `DONE 119 → 129`, `OWED 65 → 55`.**
## bench, 2026-09-21. **Landed in the SAME COMMIT as its result of record** (`RESULT-claude-blockSG-2026-09-21.md`), per council 2026-09-16 ⑤d.

## §T1 · THE ARITHMETIC
Block SG fired **10 conditions / 30 cells** (`claude-sonnet-5`, greenfield, extras=none). **All ten move to `DONE`.**
```
  claude-sonnet-5   greenfield x {Crc32,FreeList,LRU,LZW,Paxos} x {plain,salt-diet} x none        +10
  ---------------------------------------------------------------------------------------------------
  MATRIX         DONE 129 · OWED 55 · BLOCKED 0 · INEXPR 16  = 200
```
⇒ **129 + 55 + 0 + 16 = 200.** The 240-view is `DONE 129 · OWED 55 · BLOCKED 0 · INEXPR 56` (= 240).

## §T2 · ⛔ TWO CONDITIONS REST ON n=2 RATHER THAN n=3, AND BOTH ARE NAMED HERE RATHER THAN AVERAGED AWAY
```
  LRU x plain              n=2 in the table. `clbglp01` was fired and harvested BY HAND and has NO
                           served-*.out anywhere, so its SERVED model cannot be derived and it is
                           DECLARED-EXCLUDED rather than carried on its REQUESTED model (ADDENDUM 12's
                           whole lesson). The cell RAN and IS scored; what is missing is its attribution.
  FreeList x salt-diet     n=2 SCORABLE. `clbgfs02` is BUILD-FAIL at 0/0 AND CAP-COST at the $37.21 cap
                           — a cell CUT OFF, not a cell that failed — and is in NO denominator.
```
⇒ **The conditions are DONE (they ran and were scored); their n is smaller and is stated, because a condition resting on two cells is a weaker fact than one resting on three.**

## §T3 · ⛔⛔ THE FINDING THAT BOUNDS THIS BLOCK: **THE COST CAP IS ARM-CORRELATED**
```
  plain       0 of 14 capped        salt-diet     5 of 15 capped        cap $37.21, unit COST
```
⇒ 🔑 ***A CAP THAT BINDS ONE ARM AND NEVER THE OTHER IS NOT A BUDGET, IT IS A TREATMENT.*** Its direction is known — it can only REMOVE salt-diet work — so **every salt-diet figure in this block is a LOWER BOUND on cost and a FLOOR on correctness.** The cost ratios (median **8.27×**, total **9.83×**, T **20.77×**) are bounds, not measurements.
⚠️ **AND THE ONLY UNAMBIGUOUS CORRECTNESS FAILURE IS IN THE *PLAIN* ARM** (`clbgfp03`, FreeList, LANDED, uncapped, suite 6/7). The salt-diet arm's single non-PASS is the capped BUILD-FAIL above.

## §T4 · WHAT THIS ADDENDUM DOES NOT DO
- **It does not compare SG with block O.** The result notes that the median cost ratio is 1.89× on `brownfield × none` at Opus and 8.27× here — **two things differ at once, the FIELD and the MODEL, so neither block can attribute the gap.** That is a pair of readings, not a decomposition.
- **It moves no other block.** SS · SBS · OS are harvested, scored and have tables of record, and each still owes its result.

---
# ✅✅ ADDENDUM 15 — **BLOCK SS COMPLETES: `DONE 129 → 137`, `OWED 55 → 47`.**
## bench, 2026-09-21. **Landed in the SAME COMMIT as its result of record** (`RESULT-claude-blockSS-2026-09-21.md`), per council 2026-09-16 ⑤d.

## §U1 · THE ARITHMETIC
Block SS fired **8 conditions / 24 cells** (`claude-sonnet-5`, greenfield, `statement`), every condition at full n=3.
```
  claude-sonnet-5   greenfield x {Crc32,FreeList,LRU,LZW} x {plain,salt-diet} x statement          +8
       ⛔ Paxos x statement is INEXPRESSIBLE (§C4) — 4 problems, not 5, BY DESIGN and not by loss.
  ---------------------------------------------------------------------------------------------------
  MATRIX         DONE 137 · OWED 47 · BLOCKED 0 · INEXPR 16  = 200
```
⇒ **137 + 47 + 0 + 16 = 200.** The 240-view is `DONE 137 · OWED 47 · BLOCKED 0 · INEXPR 56` (= 240).

## §U2 · ⛔⛔ THE ARM-CORRELATED CAP REPEATS UNDER A SECOND TREATMENT — AND HERE IT ACCOUNTS FOR *EVERY* FAILURE
```
  plain       0 of 12 capped · PASS 12 of 12        salt-diet   2 of 12 capped · PASS 10 of 12
  BOTH non-PASS cells ARE the two capped cells:  clbsfs02 FAIL 6/7 · clbszs02 BUILD-FAIL 0/0
```
⇒ 🔑 ***THERE IS NO UNCAPPED SALT-DIET FAILURE IN THIS BLOCK AND NO PLAIN FAILURE AT ALL, SO THE APPARENT CORRECTNESS GAP COINCIDES EXACTLY WITH THE CENSORING.*** This block cannot separate *"the treatment produced worse code"* from *"the treatment ran out of money."*
⇒ **Block SG (§T3) found the same thing under `none`. Two blocks, two treatments, same model and field, same direction ⇒ the CAP is the common cause, not the treatment.**
⭐ **The direction is known, so these are bounds:** salt-diet's 10/12 is a FLOOR and its costs are LOWER BOUNDS.

## §U3 · THE ONE CLEAN CONTRAST THIS CAMPAIGN NOW HAS, STATED AS A READING RATHER THAN A RESULT
Blocks SG and SS differ in **exactly one factor** — the treatment (`none` vs `statement`) — at the same model and field:
```
  median COST ratio (salt-diet : plain)      SG `none` 8.27x        SS `statement` 5.32x
```
⚠️ **BOTH FIGURES ARE LOWER BOUNDS CENSORED BY AN ARM-CORRELATED CAP, SO THE DIFFERENCE BETWEEN THEM IS *NOT* BOUNDED IN A KNOWN DIRECTION.** It is a pair of readings to be re-taken when the cap is not binding — **not a result about the statement treatment**, and it is recorded here so a later reader does not mistake it for one.

## §U4 · WHAT THIS ADDENDUM DOES NOT DO
- **It moves no other block.** SBS and OS are harvested, scored and have tables of record, and each still owes its result.
- **It makes no claim about the salt METHOD.**

---
# ✅✅ ADDENDUM 16 — **BLOCK SBS COMPLETES: `DONE 137 → 145`, `OWED 47 → 39`.**
## bench, 2026-09-21. **Landed in the SAME COMMIT as its result of record** (`RESULT-claude-blockSBS-2026-09-21.md`), per council 2026-09-16 ⑤d.

## §V1 · THE ARITHMETIC
Block SBS fired **8 conditions / 24 cells** (`claude-sonnet-5`, brownfield, `statement`), every condition at full n=3.
```
  claude-sonnet-5   brownfield x {Crc32,FreeList,LRU,LZW} x {plain,salt-diet} x statement         +8
       ⛔ Paxos x statement is INEXPRESSIBLE (§C4) — 4 problems BY DESIGN.
  ---------------------------------------------------------------------------------------------------
  MATRIX         DONE 145 · OWED 39 · BLOCKED 0 · INEXPR 16  = 200
```
⇒ **145 + 39 + 0 + 16 = 200.** The 240-view is `DONE 145 · OWED 39 · BLOCKED 0 · INEXPR 56` (= 240).

## §V2 · ⭐⭐ THE RETENTION FINDING REACHES ITS STRONGEST FORM — AND IT NOW BINDS THE `class` COLUMN
```
                  retained (DISJOINT)    surv                    growth (DISJOINT)
  plain           0.611 .. 0.984         0.590 .. 0.995          0.89x ..  1.07x
  salt-diet       0.101 .. 0.279         0.646 .. 0.882          4.66x .. 15.77x
```
⇒ 🔑 ***THE SALT-DIET ARM'S WORST SURVIVAL (0.646) IS HIGHER THAN THE PLAIN ARM'S WORST (0.590), AND ITS WHOLE `surv` RANGE SITS INSIDE PLAIN'S — WHILE `retained` PUTS THEM IN DISJOINT BANDS AND CLASSES SIX SALT-DIET CELLS `REPLACED`.*** The arm the classifier calls *"rewritten wholesale"* is the arm that **preserved more of the seed**; what it did was write 4.66×–15.77× as much code around it (`end_lines` to **3,027** against plain's ceiling of **206**).
⇒ **Three blocks now carry this shape** — SB §5 (Sonnet/brownfield/none), O §3 (Opus/brownfield/none), SBS (Sonnet/brownfield/statement). **In the first two `surv` overlapped; here it is strictly contained with a higher floor.**
⛔ **`class` IS DERIVED FROM `retained`, SO IT INHERITS THE DEFECT.** Six `REPLACED` cells in this block are not cells that destroyed the seed, and any reading that treats `REPLACED` as evidence of destruction is wrong on this block's own numbers.
⭐ **AND THE CLAIM IS CONSERVATIVE:** `surv` is a LOWER BOUND (matched lines only), so the true survival gap can only move further in salt-diet's favour.

## §V3 · THE ARM-CORRELATED CAP, FOR THE THIRD TIME
`plain 0 of 12 capped · salt-diet 3 of 12` (all three FreeList; **two still PASS 7/7**). Direction known ⇒ salt-diet's correctness is a FLOOR and its costs (median **4.71×**, total **9.58×**, T **17.17×**) are LOWER BOUNDS. The single non-PASS is a capped `0/0` BUILD-FAIL, in no denominator.
⚠️ **One `V1_bugs_fixed` reads `UNMEASURED`** — FreeList's MARGIN-1 rule working as designed (`RECORD-brownfield-givens`). **A declared absence, not a zero.**

## §V4 · WHAT THIS ADDENDUM DOES NOT DO
- **It moves no other block.** **OS is the last of the five** — harvested, scored, table of record built, result still owed.
- **It makes no claim about the salt METHOD.**

---
# ✅✅ ADDENDUM 17 — **BLOCK OS COMPLETES 7 OF ITS 8: `DONE 145 → 152`, `OWED 39 → 32`. THE FIVE HARVESTED BLOCKS ARE NOW ALL WRITTEN UP.**
## bench, 2026-09-21. **Landed in the SAME COMMIT as its result of record** (`RESULT-claude-blockOS-2026-09-21.md`), per council 2026-09-16 ⑤d.

## §W1 · THE ARITHMETIC — AND ONE CONDITION IS DELIBERATELY NOT MOVED
```
  claude-opus-5   brownfield x {FreeList,LRU,LZW} x {plain,salt-diet} x statement            +6
                  brownfield x Crc32 x salt-diet x statement                                 +1
  ⛔ NOT MOVED:   brownfield x Crc32 x PLAIN x statement — n=1. Reps 02 and 03 (clbtcp02,
                  clbtcp03) are FLAGGED on the second pool credential blanked at 01:17:19Z.
  ---------------------------------------------------------------------------------------------------
                                                                                             +7
  MATRIX         DONE 152 · OWED 32 · BLOCKED 0 · INEXPR 16  = 200
```
⇒ **152 + 32 + 0 + 16 = 200.** The 240-view is `DONE 152 · OWED 32 · BLOCKED 0 · INEXPR 56` (= 240).
⇒ **This is EXACTLY the 2026-09-21 partition's class (b), arriving from the other side:** *"blocked on the blanked credential — 1 condition, 2 cells."* **It is held at n=1 rather than reported, because a condition resting on one cell is a different measurement, not a weaker one.**

## §W2 · ⭐ THE ONLY UNCENSORED ARM COMPARISON IN THE FIVE, AND IT CHANGES HOW THE OTHERS READ
**Block OS has ZERO capped cells in either arm** — the only one of the five that does.
```
  median COST ratio (salt-diet : plain)
    SG   `none`      Sonnet greenfield   8.27x   LOWER BOUND (5 of 15 salt-diet capped)
    SS   `statement` Sonnet greenfield   5.32x   LOWER BOUND (2 of 12 capped)
    SBS  `statement` Sonnet brownfield   4.71x   LOWER BOUND (3 of 12 capped)
    OS   `statement` Opus   brownfield   1.23x   ⭐ UNCENSORED — 0 of 22 capped
```
⇒ 🔑 ***THE ONE RATIO TAKEN WITH NO CAP BINDING IS BY FAR THE SMALLEST*** — ⚠️ **and it CANNOT be attributed here, because OS differs from the others in MODEL as well as in censoring, and its cells cost more in both arms (plain median $12.08 against SBS's $1.54), which is WHY the cap was never reached.** **It is the question these blocks raise, not one they answer**, and it is recorded so nobody reads the three bounded ratios as if they were measurements.

## §W3 · RETENTION — A FOURTH BLOCK, AND THE SEPARATOR HOLDS BY FOUR THOUSANDTHS
`retained` plain **0.186**–0.583 against salt-diet 0.054–**0.182** — **disjoint by 0.004**, the narrowest of the four brownfield blocks — while `surv` OVERLAPS (0.300–0.951 vs 0.360–0.873) and `growth` is disjoint by a wide margin (≤3.46× vs ≥5.68×).
⇒ 🔑 ***A SEPARATOR THAT HOLDS BY FOUR THOUSANDTHS IS ONE SAMPLE FROM NOT HOLDING, WHILE THE THING IT IS ACTUALLY READING — GROWTH — IS NOWHERE NEAR ITS BOUNDARY.*** ⛔ **Do not build a threshold on `retained`.** (Relevant to §B5's 0.20 threshold, which the 2026-09-21 TQ draft amendment leaves at 0.20 and names the defect rather than tuning it.)
⛔ **And `plain` carries its first `REPLACED` cell in any of these blocks** (REPAIRED 9 · REPLACED 1), sitting right beside that 0.004 margin.

## §W4 · WHERE THE CAMPAIGN STANDS AFTER ADDENDA 13–17
**The 43 conditions that were run, harvested and metered with no result of record are now written up: `DONE 109 → 152`, `OWED 75 → 32`.** The remaining 32 are **(a) 10** on the UM cut / SC driver · **(b) 1** on the blanked credential (§W1) · **(c) 21** on the AGY lane's level 8. **None of the 32 is a cell waiting for the Claude lane to be free.**
