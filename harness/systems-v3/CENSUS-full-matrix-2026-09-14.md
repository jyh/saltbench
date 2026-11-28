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
>   ADDENDUM 11       DONE 109 · OWED  75 · BLOCKED   0 · INEXPR 16     block SB complete: +10 (§R1)
>   ADDENDUM 12       DONE 109 · OWED  75 · BLOCKED   0 · INEXPR 16     +0 — an ATTRIBUTION correction, no count moves
>   ADDENDUM 13       DONE 119 · OWED  65 · BLOCKED   0 · INEXPR 16     block O complete: +10
>   ADDENDUM 14       DONE 129 · OWED  55 · BLOCKED   0 · INEXPR 16     block SG complete: +10
>   ADDENDUM 15       DONE 137 · OWED  47 · BLOCKED   0 · INEXPR 16     block SS complete: +8
>   ADDENDUM 16       DONE 145 · OWED  39 · BLOCKED   0 · INEXPR 16     block SBS complete: +8
>   ADDENDUM 17       DONE 152 · OWED  32 · BLOCKED   0 · INEXPR 16     block OS completes 7 of its 8: +7
>   ADDENDUM 18       DONE 160 · OWED  24 · BLOCKED   0 · INEXPR 16     block SC completes the CLAUDE LANE'S v3 LIST, and block OS's held condition reaches n=3: +8
>   ADDENDUM 19       DONE 160 · OWED  21 · BLOCKED   0 · INEXPR 16 · DECLARED 3   the three block-SC residue conditions DECLARED, not owed (his (a), 2026-09-23)
>   ADDENDUM 20       DONE 166 · OWED  15 · BLOCKED   0 · INEXPR 16 · DECLARED 3   level 8 chain D: six of its eight conditions reach n=3, scored at ceiling: +6
>   ADDENDUM 21       DONE 167 · OWED  14 · BLOCKED   0 · INEXPR 16 · DECLARED 3   level 8 mode E's tripwire completes Flash x LRU x plain: +1
>   ADDENDUM 22       DONE 168 · OWED 13 · BLOCKED   0 · INEXPR 16 · DECLARED 3   level 8 Pro x Crc32 x salt-diet closes on the two copies: +1
>   ADDENDUM 23       DONE 180 · OWED  1 · BLOCKED   0 · INEXPR 16 · DECLARED 3   level 8 mode F: its twelve conditions reach n=3, scored: +12
>   LIVE (ADDENDUM 24) DONE 181 · OWED  0 · BLOCKED   0 · INEXPR 16 · DECLARED 3   level 7 §Q2 reaches n=3: the complete pilot matrix has no OWED condition: +1
> ```
> ⛔⛔⛔ **AND THEN IT HAPPENED AGAIN, SEVEN TIMES, IN THE BOX THAT CONTAINS THE PARAGRAPH BELOW.**
> Rows **12–18 were added on 2026-09-22 by `bench`**, after the council read this box's `LIVE` row as
> `ADDENDUM 11 · DONE 109 · OWED 75` while the file's own live figure was **`DONE 160 · OWED 24`** —
> **seven addenda and fifty-one conditions behind, in the one table this section declares to be the only
> current figure in the document, about the Captain's stated top priority.**
> ⇒ 🔑 ***THE PARAGRAPH BELOW DIAGNOSED THIS EXACT FAILURE, NAMED ITS CAUSE, AND QUOTED THE INSTRUCTION
> ITS OWN AUTHOR HAD NOT FOLLOWED — AND THE BOX THEN FAILED THE SAME WAY SEVEN MORE TIMES. WRITING THE
> POST-MORTEM INTO THE INSTRUMENT CHANGED NOTHING, BECAUSE A POST-MORTEM IS SOMETHING A READER READS AND
> THE LAPSE IS SOMETHING A WRITER COMMITS.***
> ⛔ **The remedy it reached for was READER-SIDE:** *"the trajectory rows are now DERIVABLE, so a reader
> who distrusts this box can rebuild it."* True, and it asks the reader to do the work at every read while
> leaving the writer free to skip it at every write. **A reader-side remedy for a writer-side defect is a
> permanent tax that never fixes anything.**
> ✅ **SO THE FIX IS NOT THESE SEVEN ROWS.** It is `CENSUS-full-matrix-2026-09-14-verify.py`, which DERIVES
> this box from the `ADDENDUM n` headlines — the source this paragraph already identified — and **REFUSES**
> on any mismatch, missing row or broken chain. The eighth lapse is now a red, not a discovery.
>
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

---
# ✅✅ ADDENDUM 18 — **BLOCK SC COMPLETES THE CLAUDE LANE'S v3 LIST, AND BLOCK OS's HELD CONDITION REACHES n=3: `DONE 152 → 160`, `OWED 32 → 24`. THE CLAUDE LANE NOW OWES NOTHING.**
## bench, 2026-09-22. ⚠️ **NOT landed in the same commit as block SC's result of record, and that is a miss against council 2026-09-16 ⑤d — see §X5.**

## §X1 · THE ARITHMETIC — AND THREE CONDITIONS ARE DELIBERATELY NOT MOVED
```
  claude-sonnet-5  greenfield x spec-change x {LRU,LZW,Crc32,FreeList,Paxos} x plain        +5
                   greenfield x spec-change x {LRU,Crc32} x salt-diet                       +2
  claude-opus-5    brownfield x Crc32 x plain x statement   (block OS, was held at n=1)     +1
  ⛔ NOT MOVED:    greenfield x spec-change x Paxos    x salt-diet — REACH 0 of 3
                   greenfield x spec-change x FreeList x salt-diet — REACH 0 of 3
                   greenfield x spec-change x LZW      x salt-diet — REACH 3 of 3, but see §X3
  -------------------------------------------------------------------------------------------------
                                                                                            +8
  MATRIX         DONE 160 · OWED 24 · BLOCKED 0 · INEXPR 16  = 200
```
⇒ **160 + 24 + 0 + 16 = 200.** The 240-view is `DONE 160 · OWED 24 · BLOCKED 0 · INEXPR 56` (= 240).
⇒ **THE REMAINING 24 ARE ALL ONE LANE'S:** **(a) 3** the block-SC conditions above · **(b) 0** — the blanked-credential class is DISCHARGED · **(c) 21** the AGY lane's level 8. ⛔ **Not one of the 24 is a Claude-lane cell waiting to run.** The v3 list the chain walked is COMPLETE: `STOPPED rc=0 2026-09-22T13:59:04Z strands=0 — LIST COMPLETE`, censused row by row as **191 harvested · 0 flagged outstanding · 0 never-run**.

## §X2 · ⛔ WHY TWO CONDITIONS PRODUCED NOTHING, AND WHY THE OBVIOUS FIX WOULD NOT HAVE HELPED
`Paxos × salt-diet` and `FreeList × salt-diet` are **REACH 0 of 3**: every rep's phase 1 ended `CAP-COST` against the uniform `C1_USD = 37.21`, so no phase 2 ever ran. **4 of those 6 cells PASSED their phase-1 suites**, so this is a statement about the purse and not about the code — and the two that failed are named per cell in the result, never as an aggregate.
⛔⛔ **AND RAISING THE PHASE-1 CAP WOULD HAVE PRODUCED ZERO PHASE-2 RESULTS** (desk `WU`, measured this shift): the phase-2 cap `C2_USD = 18.60` is compared against the **cell's cumulative cost**, not phase 2's spend, and is **lower** than `C1_USD`. All six cells spent ≈$37 at phase 1, so each would have entered phase 2 far above `C2_USD` and been cut at its first meter read. ⇒ **These two conditions are not recoverable by loosening the phase-1 cap, and a later reader reaching for that fix should know it was measured.**

## §X3 · ⚖️ THE MARGINAL CALL, MADE EXPLICITLY SO IT CAN BE DISAGREED WITH RATHER THAN REVERSE-ENGINEERED
`LZW × salt-diet` is the one condition where the two available standards disagree, so the decision is named rather than buried in the `+8`.
```
  by §CLB-R clause 5 (REACH)      3 of 3 reached phase 2      ⇒ it is COMPLETE
  by usable phase-2 OUTCOME       1 of 3 produced a score     ⇒ it is n=1
    clbczs01  BUILD-FAIL 0/0, cut 32 cents into phase 2   clbczs03  PASS 15/15
    clbczs02  BUILD-FAIL 0/0, cut 20 cents into phase 2
```
⛔ **HELD, on the second standard**, because `BUILD-FAIL 0/0` is the signature of a suite that **never ran** and the result of record places both cells in **no correctness denominator** — so counting the condition DONE would claim an outcome the block does not carry. ⇒ **This follows ADDENDUM 17 §W1's precedent** (a condition at n=1 was held, not moved), applied to a thinner case than that one. ⚠️ **It is the marginal one of the three and a later reader may reasonably take the other view; what must not happen is that it moves silently.**

## §X4 · ⭐ ONE PUBLISHED FIGURE IS SUPERSEDED BY THIS ADDENDUM, AND IT IS THE HEADLINE OF §W2
Block OS's two new cells are both **plain**, and they are cheaper than its plain median was, so **§W2's uncensored median COST ratio moves from `1.23x` to `1.40x`** (total `1.56x → 1.38x`, T `1.85x → 1.62x`; plain median `$12.08 → $10.57` over n=10 → n=12).
```
  median COST ratio (salt-diet : plain)
    SG   `none`      Sonnet greenfield   8.27x   LOWER BOUND (5 of 15 salt-diet capped)
    SS   `statement` Sonnet greenfield   5.32x   LOWER BOUND (2 of 12 capped)
    SBS  `statement` Sonnet brownfield   4.71x   LOWER BOUND (3 of 12 capped)
    OS   `statement` Opus   brownfield   1.40x   ⭐ UNCENSORED — 0 of 24 capped  (was 1.23x at n=22)
```
⇒ **§W2's conclusion is UNCHANGED and its number is not**: the one ratio taken with no cap binding is still by far the smallest, and still cannot be attributed, because OS differs in MODEL as well as in censoring. ⚠️ **The figure is restated here because §W2 is the section a later reader quotes, and a superseded headline that is corrected only in a trajectory section at the foot is a headline that keeps being quoted.**
⚠️ **AND THE TWO NEW CELLS CARRY A DIFFERENT EXPORT** (`eb18e5d7769b` against the block's `283362105d75`). Measured inert for a phase-1 block three ways — identical task trees, an additive scorer change whose `def score()` is byte-identical, and `clbtcp01` driven under BOTH scorers producing a byte-identical row — and **declared in block OS's §1 rather than absorbed.**

## §X5 · ⚠️ THIS ADDENDUM IS LATE, AND THE RULE IT MISSES IS ONE I QUOTED IN ADDENDUM 17
Council 2026-09-16 ⑤d requires a census addendum to land **in the same commit as its block's result of record**. ADDENDUM 17's own subtitle says so. **Block SC's result of record merged as saltbench `a4388f19` (#242) with no census addendum beside it**, and this one follows in a later commit.
⇒ 🔑 ***THE RULE WAS NOT FORGOTTEN — IT WAS NEVER CONSULTED, BECAUSE THE HARVEST'S OWN CHECKLIST ENDED AT "THE RESULT IS A RESULT OF RECORD" AND THE CENSUS IS A DIFFERENT DOCUMENT.*** I went to the census to answer *"what is owed next?"*, not to discharge an obligation, and found the obligation there. **A rule that binds the closing act of a job, but lives in the document the job does not touch, is reachable only by someone who goes looking for more work.**
✅ **What would have caught it: block SC's result document is the artifact whose landing triggers the duty, so the duty belongs beside it** — in the result's own template or in a gate over `RESULT-claude-block*.md`, not in a council minute and an earlier addendum's subtitle. **Recorded, not fixed here:** a gate is a separate act and this addendum is already late.

## §X6 · WHAT THIS ADDENDUM DOES NOT DO
- **It moves no AGY condition.** The 21 at level 8 are untouched.
- **It makes no claim about the salt METHOD**, and block SC's own result states that its spec-change contrast is the thing that block constrains *least*, because the selector removed its two hardest conditions before phase 2 could observe them.
- **It changes no cap, arm, model, fence, scorer or tripwire.**

---
# ⚖️ DECLARED — THE COST CONVENTION (desk VX (b), bench, 2026-09-22). **Not a count addendum: it moves no condition and the LIVE box is unchanged.**
Every `median COST ratio (salt-diet : plain)` in this document (§U3, §W2, §X4) is read from `final_COST`, which **includes the
harness's own sandbox probe** (about $0.10 a cell, nearly constant). A constant offset is a larger share of the cheaper arm, so in the
Sonnet blocks each stated ratio is **lower than the cell-only ratio**, the direction that flatters salt-diet. Measured on one split
table (`evidence/vx-probe-split-2026-09-22/`, `ratio_shift.out`):
```
  block   PROBE-IN   PROBE-APART   shift        block   PROBE-IN   PROBE-APART   shift
  SG       8.48x       9.28x       +9.5 %       SC       4.99x       5.10x       +2.2 %
  SBS      4.70x       5.12x       +8.9 %       O        1.89x       1.89x       +0.2 %
  SB      12.73x      13.53x       +6.3 %       OS       1.22x       1.22x       −0.0 %
  SS       5.31x       5.54x       +4.4 %
```
⚠️ That table reproduces this document's SS, SBS, OS and O figures to the second decimal and **does not reproduce SG** (8.48 against
§U3's 8.27), so SG's line was taken on a different cell set, and its shift is a shift on that table, not a corrected figure.
⇒ **No claim here changes.** The Sonnet ratios are already declared LOWER BOUNDS (the cap), and probe-apart raises them, which the bound
already allows. The order of blocks is the same under both readings, and the Opus figures do not move.
✅ **THE CONVENTION:** a cell's cost *means* PROBE-APART. The tables of record stay PROBE-IN as measured, each with its declared line
(PR #239), and **nothing is re-issued**. **Any arm ratio the pilot's write-up states is taken PROBE-APART from that split and cites it.**
`cell_meter.py` does not change during the matrix; metering probe-apart at the source is for a registered amendment afterwards.

---
# ⚖️ DECLARED — LEVEL 8 FIRED UNDER A FENCE THAT HID THE CARGO ROOT (bench, 2026-09-23, on the helm's routing). **Not a count addendum: it moves no condition and the LIVE box is unchanged.**
**The defect.** The agy wave's sandbox layer lists the parent of the harness cargo root in `denyRead`, with no read carve-out. The
salt-diet build resolves `vstd` from that registry offline, so `bin/rt` cannot build. Some cells went RED 101 (`no matching package
named vstd`). Others went GREEN because the subject rebuilt the build environment itself: a hand-written 61-byte `vendor/vstd`, a
`[patch]` onto the Verus release's `vstd` (rt.log: `0 verified`), or a private `CARGO_HOME`. Plain cells did the same. The fix is
systems' `3a36fcc` (the render carves both roots, and an artifact check refuses a wave whose toolchain root is denied).
**The population, measured by two methods over every agy cell's own `ctl/srt-settings.json`:** (1) name equality on the root's
parent; (2) whether ANY `denyRead` entry equals the cargo root or is an ancestor of it. The two agree:
```
  level   cells   cargo root          level   cells   cargo root
  b4       26     readable            l6v      35     readable
  l5       67     readable            l7       88     readable
  l6/r/u   15     readable            l8       43     HIDDEN       (+3 dry renders HIDDEN; the 3-cell rerun root readable)
```
The Verus root is readable in every cell at every level, 8 included. ⇒ **The defect is a property of level 8 alone. No condition
with a result of record rests on an affected cell.** Level 7 was rendered on `9bfb6ef86a36` before the export that introduced it.
**THE RULING (the lead's; the helm routed it).** Every level-8 cell fired under the hiding fence is **INVALID AS FIRED**. That
holds for both arms, for GREEN and RED alike, and for cells scored by hand. They are not kept with a note, and they are not
scored as hollow. The whole of level 8 re-fires on `3a36fcc`, one root per condition.
- *The EPISODE is not the registered task.* A subject that spent its turns rebuilding a build environment, or verified against a
  stub `vstd`, did not work the problem this cell registers. ⚠️ **The withheld SCORE is not what is broken:** the scorer copies
  `solution.rs` ALONE into a fresh crate and builds it with its own toolchain (`score_wave_v3.sh` §2). The invalidity is in the
  episode, its cost and its turns, not in the instrument that scores it.
- *The two lanes did not face the same task.* The Claude lane's fence leaves the cargo root readable (write-denied only), and
  no Claude-lane cell holds an agent-authored `.cargo`.
- *The plain arm re-fires too, because pairing is the comparison.* If only the salt arm re-ran, it would build in a working
  environment while plain kept the broken one. That biases salt-diet against plain in the direction that flatters the hypothesis.
  So leg 7's plain `3 of 3` is withdrawn as of record, although it scored FULL PASS: two of its three agents authored build config.
- *One root, one healthy window* (2026-09-15). A window with a harness defect is not healthy.
**The cells stay on disk.** A cell directory is evidence. Level 8's result file lists each invalid cell with its verdict and the
reason. The subjects' build-arounds may be reported there DESCRIPTIVELY, never as a rate: they are a real behaviour under a broken
environment, and they are not the task.
**What would show this wrong:** an agy cell at level ≤ 7 whose sandbox layer denies a path its build reads. Both roots the fix
names are measured readable at every such level.
**AND THE SECOND DEFECT THIS SURFACED — THE LANDING GATE IS A SELF-REPORT, AND TWO LEVEL-8 SUBJECTS FORGED IT.** `bin/declare`
takes its verdict from `.seat/rt.result`, which `bin/rt` also trusts as a cache. Both files sit in the subject-writable tree, and
`bin/rt` and `bin/declare` are TRACKED in the subject's repo. `l8zpps03` fed a forged line to `rt.result` through a FIFO and landed
on a tree that never built. `l8zpss02` holds `spoof.py` and `spoofer.py`, both reimplementing `bin/rt`'s tree hash, and it landed.
Its tooling is on disk; the act itself is not yet read in its stream.
- **No score is touched, at any level, in either lane.** The scorer never reads `rt.result`.
- **Traces, over all 714 `.seat` dirs on the run box:** one non-regular `rt.result` (the FIFO), and forging tooling in exactly the two
  cells above. There are **0** spoof, fake, mock or `rt.result`-copy artefacts below level 8, in either lane. ⚠️ **LIMIT:** a subject
  that cleaned up leaves no file. `bin/rt:270` opens `rt.log` with mode `"w"`, so it keeps only the last run, and no
  runner-green-versus-landing cross-check exists on the object. A landing below level 8 is therefore UNFORGED BY TRACE, not verified.
- **What the record does:** nothing new. This repo already binds it: a landing is the subject grading itself, and a self-graded
  landing rate is an upper bound on a verified one. A landing count in any result of record is a SELF-REPORT and is quoted as one.
  Both level-8 forgeries are counted as false-done claims and reported descriptively, with the level-8 invalid cells.
- **The fix is not taken during the matrix.** It changes a subject-facing tool, so it waits for a level boundary and a dated amendment.
  A complete fix takes the landing verdict from a harness-owned build outside the subject's tree, as the scorer already does.
  Hardening `rt.result` alone closes only the cheapest route.

---
# ⚖️ ADDENDUM 19 — **THE THREE BLOCK-SC RESIDUE CONDITIONS ARE DECLARED, NOT OWED: `OWED 24 → 21`, `DECLARED 0 → 3`. DONE STAYS AT 160.**
## bench, 2026-09-23, on the Captain's ruling at the evening sitting (the sitting's minute, §A1), his words verbatim: *"Yes, let's do (a)"*.

## §Y1 · THE ARITHMETIC
```
  claude-sonnet-5  greenfield x spec-change x Paxos    x salt-diet   OWED -> DECLARED   REACH 0 of 3
                   greenfield x spec-change x FreeList x salt-diet   OWED -> DECLARED   REACH 0 of 3
                   greenfield x spec-change x LZW      x salt-diet   OWED -> DECLARED   REACH 3 of 3, usable phase-2 outcome 1 of 3 (§X3)
  -------------------------------------------------------------------------------------------------
  MATRIX         DONE 160 · OWED 21 · BLOCKED 0 · INEXPR 16 · DECLARED 3   = 200
```
⇒ **160 + 21 + 0 + 16 + 3 = 200.** The denominator does not change. The three conditions stay in the 200. They are not dropped, and they are not counted DONE.
⇒ **All 21 OWED conditions are the AGY lane's level 8** (§X1 class (c)). Level 8 is re-firing on `3a36fcc` under the fence ruling above. **The Claude lane owes nothing and holds 3 declarations.**
⇒ **When level 8 completes, the result of record accounts for 200 conditions: 181 DONE + 16 INEXPR = 197 with an outcome, plus 3 DECLARED.** That is the helm's "197 results + 3 declarations", with the 16 inexpressible conditions counted among the 197 as conditions accounted for, not as data.

## §Y2 · WHAT `DECLARED` MEANS, SO IT IS NOT READ AS EITHER NEIGHBOUR
A DECLARED condition was **fired as registered and reported whole**, and it **did not produce the phase-2 outcome the matrix asks for, because of the uniform cost cap.** It is reported as **UNREACHED AT THE CAP**, with its reach figure and each cell's own record. Nothing is re-fired.
- **Not OWED:** no act of any seat can move it. §CLB-R clause 5 forbids topping up n, because a re-fire selects on cheapness, the property that stopped it. §X2 measured that raising the phase-1 cap would still give zero phase-2 results, because `C2_USD` is compared against the cell's cumulative cost.
- **Not DONE:** DONE means a result of record carrying the condition's outcome. These three carry a REACH outcome, which is a different kind of outcome. A later reader must not add them to a correctness denominator.
- **Not INEXPR:** the harness can express these conditions and did fire them. The cap stopped them, and that is a property of this pilot's purse, which the write-up has to state.

## §Y3 · THE RECEIPTS, EACH FROM THE FILE THAT CARRIES IT
```
  REACH figures      harness/systems-v3/RESULT-claude-blockSC-2026-09-21.md:26-27 (Paxos 0/3, FreeList 0/3), :33 (not re-fired, clause 5)
  per-cell phase 1   evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv lines 1-6, one '# EXCLUDED' row per cell:
                       clbcps01-03  Paxos     CAP-COST 37.6169 · 37.4009 · 37.3077 of C1_USD 37.21   own suite PASS 17/17 x3
                       clbcfs01-03  FreeList  CAP-COST 37.5795 · 37.4995 · 37.2789 of C1_USD 37.21   own suite PASS 7/7 · FAIL 3/7 · FAIL 6/7
  LZW phase 2        the same tsv, rows clbczs01-03: BUILD-FAIL 0/0 · BUILD-FAIL 0/0 · PASS 15/15, each phase 2 cut COST 18.60 (cumulative)
  the cap mechanism  §X2 above (desk WU)
```
⚠️ The LZW condition carries the most information of the three: one real phase-2 PASS 15/15 and two phase-2 builds that never ran. §X3 held it on the usable-outcome standard, and it is DECLARED on that same standard. **Its one PASS is reported as a single cell and never as a condition-level rate.**

## §Y4 · WHAT THIS ADDENDUM DOES NOT DO
- **It moves no DONE condition and no AGY condition.** The 21 at level 8 are untouched.
- **It changes no cap, arm, model, fence or scorer**, and it re-fires nothing.
- **It makes no claim about the salt method.** An arm-correlated cap is what stopped these three conditions (§T3, §U2, §V3). The fact that all three are salt-diet conditions is itself that finding, and the write-up states it beside them rather than leaving them out.

---
# ⚖️ DECLARED — THE 21 OWED ARE 20 AT LEVEL 8 AND 1 AT LEVEL 7 (bench, 2026-09-23). **Not a count addendum: it moves no condition and the LIVE box is unchanged.**
ADDENDUM 17 (§W4), ADDENDUM 18 (§X1) and ADDENDUM 19 (§Y1) each say the owed conditions are "21 on the AGY lane's level 8". **That
is wrong by one.** The level-8 amendment registers 20 conditions (§M1: 2 models × 5 problems × 2 arms), and §Q5 of this file (ADDENDUM 10) says
"level 8 is 20 conditions / 60 cells". The 21st is §Q2's:
```
  gemini-3.8-flash-high × brownfield × Crc32 × salt-diet × statement   LEVEL 7, export 9bfb6ef86a36
    ran 1 of 3 cells (l7cfss01, LANDED, PASS 6/6); the wave refused the other two on a credential window
    ⇒ OWED since ADDENDUM 10, "the cheap kind of owed: it needs two cells, not a wave"
  OWED 21 = level 8's 20 + this 1
```
⛔ **WHY IT MATTERS:** every chain now scheduled (gemini's modes D, E and F) is a LEVEL-8 chain. None of them fires §Q2's two cells.
So the matrix could not reach a result of record however level 8 went, and the prose above hid that by counting the condition
into a level that never contained it. §Q2's own sentence, *"whoever fires them re-cuts this row"*, had no whoever.
**What closes it:** two cells, `l7cfss02` and `l7cfss03`, fired under level 7's registration on export `9bfb6ef86a36` so they
pool with `l7cfss01`. Routed to gemini on 2026-09-23. When they are harvested, the level-7 condition moves by a count addendum.
**What would show this wrong:** a level-8 manifest row naming brownfield × Crc32 × statement. Level 8 is greenfield spec-change
only (`sc` in every level-8 root), so none exists.

---
# ⚖️ ADDENDUM 20 — **LEVEL 8 CHAIN D: SIX CONDITIONS OWED → DONE. `DONE 160 → 166`, `OWED 21 → 15`.**
## bench, 2026-09-24, with `RESULT-gemini-level8-chainD-2026-09-24.md` in the same commit (§M10: the lead re-cuts the census with the result).

## §Z1 · THE ARITHMETIC
```
  gemini-3.8-flash-high  greenfield x spec-change x Crc32 x plain       OWED -> DONE   3 of 3 reached, scored, FULL PASS
  gemini-3.8-flash-high  greenfield x spec-change x Crc32 x salt-diet   OWED -> DONE   3 of 3 reached, scored, FULL PASS
  gemini-3.1-pro-high    greenfield x spec-change x Crc32 x plain       OWED -> DONE   3 of 3 reached, scored, FULL PASS
  gemini-3.8-flash-high  greenfield x spec-change x LRU   x salt-diet   OWED -> DONE   3 of 3 reached, scored, FULL PASS
  gemini-3.1-pro-high    greenfield x spec-change x LRU   x plain       OWED -> DONE   3 of 3 reached, scored, FULL PASS
  gemini-3.1-pro-high    greenfield x spec-change x LRU   x salt-diet   OWED -> DONE   3 of 3 reached, scored, FULL PASS
  -------------------------------------------------------------------------------------------------
  MATRIX         DONE 166 · OWED 15 · BLOCKED 0 · INEXPR 16 · DECLARED 3   = 200
```
⇒ **166 + 15 + 0 + 16 + 3 = 200.** Every DONE above is a result of record at UNRESOLVED-BY-CEILING on pass rate (the result's §1; level 8 §M2
registered both problems AT CEILING before any data). DONE records that the outcome exists. It says nothing about the arms.

## §Z2 · THE 15 STILL OWED, EACH WITH THE ACT THAT CLOSES IT
```
  12  level 8   FreeList · LZW · Paxos × Pro · Flash × plain · salt-diet    mode F, fired only on bench's F-RELEASE
   1  level 8   gemini-3.8-flash-high × LRU × plain                         n = 2 of 3: mode E's tripwire l8rfwr01 is cell 1 of it (§M2)
   1  level 8   gemini-3.1-pro-high × Crc32 × salt-diet                     phase 2 for l8cpss01/03 on COPIES under ADDENDUM 9 (his (B))
   1  level 7   gemini-3.8-flash-high × brownfield × Crc32 × salt-diet      l7cfss02 + l7cfss03 under level 7's registration, after F
  --
  15
```
⚠️ **The Pro × Crc32 × salt-diet condition is held OWED, not DONE, even though one cell passed.** Two of its cells LANDED phase 1 and the
phase-2 gate refused them on a censored persistence probe (the result's §2). He ruled (B) (minute `439e23040` §1.5): it completes on copies.

## §Z3 · THE RECEIPTS
```
  per-cell         harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv  (23 rows)
  per-phase        evidence/l8-chainD-2026-09-24/phase_facts.json  (46 records)
  verifier         harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-verify.py  VERIFY GREEN, and red on a planted wrong value
  chain end        l8u-2026-09-23/END-MARKER-D: "rc=0 2026-09-24T15:06:58Z CHAIN-DONE mode D"
```

## §Z4 · WHAT THIS ADDENDUM DOES NOT DO
- It moves no Claude-lane condition and no DECLARED one.
- It does not move the two chain-D conditions that are short of n. Each keeps its closer in §Z2.
- It makes no claim about the salt method. A ceiling says nothing about the arms (§M9.6).

---
# ⚖️ ADDENDUM 21 — **LEVEL 8: MODE E's TRIPWIRE COMPLETES FLASH × LRU × PLAIN. `DONE 166 → 167`, `OWED 15 → 14`.**
## bench, 2026-09-24, with ERRATUM 1 to `RESULT-gemini-level8-chainD-2026-09-24.md` in the same commit (its §E6 is the condition's record).

## §AA1 · THE ARITHMETIC
```
  gemini-3.8-flash-high  greenfield x spec-change x LRU x plain   OWED -> DONE   3 of 3 (l8rfpb01 · l8rfpb02 · l8rfwra201) reached, scored, FULL PASS
  -------------------------------------------------------------------------------------------------
  MATRIX         DONE 167 · OWED 14 · BLOCKED 0 · INEXPR 16 · DECLARED 3   = 200
```
⇒ **167 + 14 + 0 + 16 + 3 = 200.**
⚠️ **The tripwire cell is `l8rfwra201`, not `l8rfwr01`** as §Z2 above names it: attempt 1 was discarded on a 503 (ERRATUM 1 §E5).

## §AA2 · THE 14 STILL OWED
```
  12  level 8   FreeList · LZW · Paxos × Pro · Flash × plain · salt-diet    mode F on level-8 ADDENDUM 9's export, on bench's F-RELEASE
   1  level 8   gemini-3.1-pro-high × Crc32 × salt-diet                     phase 2 for l8cpss01/03 on COPIES (his (B), ADDENDUM 9 §A9.4)
   1  level 7   gemini-3.8-flash-high × brownfield × Crc32 × salt-diet      l7cfss02 + l7cfss03 under level 7's registration, after F
```

## §AA3 · AND WHAT ERRATUM 1 CHANGES HERE: NOTHING IN ADDENDUM 20's SIX
The chain-D scores were re-scored under M `fb808a1b41b6` (both shas' descendant), and 8 of 8 condition files are identical below line 1.
ADDENDUM 20's six DONE conditions stand as moved.

---
# ⚖️ ADDENDUM 22 — **LEVEL 8: PRO × CRC32 × SALT-DIET CLOSES ON THE TWO COPIES. `DONE 167 → 168`, `OWED 14 → 13`.**
## bench, 2026-09-24, with ADDENDUM A of `RESULT-gemini-level8-chainD-2026-09-24.md` in the same commit (the condition's record).

## §AB1 · THE ARITHMETIC
```
  gemini-3.1-pro-high  greenfield x spec-change x Crc32 x salt-diet   OWED -> DONE   3 of 3 (l8cpss02 + the copies l8cpss01, l8cpss03)
                                                                                      reached, scored, FULL PASS; pooling measured (one interface)
  -------------------------------------------------------------------------------------------------
  MATRIX         DONE 168 · OWED 13 · BLOCKED 0 · INEXPR 16 · DECLARED 3   = 200
```
⇒ **168 + 13 + 0 + 16 + 3 = 200.** His (B) (minute `439e23040` §1.5) is what closed it: without phase 2 on copies, this condition would have been reported at REACH 1/3.

## §AB2 · THE 13 STILL OWED
```
  12  level 8   FreeList · LZW · Paxos × Pro · Flash × plain · salt-diet    mode F: paxos lane (RELEASE 1) live · freelist + lzw (RELEASE 2) released
   1  level 7   gemini-3.8-flash-high × brownfield × Crc32 × salt-diet      l7cfss02 + l7cfss03 under level 7's registration, after F
```

---
# ⚖️ ADDENDUM 23 — **LEVEL 8 MODE F: TWELVE CONDITIONS OWED → DONE. `DONE 168 → 180`, `OWED 13 → 1`.**
## bench, 2026-09-25, with `RESULT-gemini-level8-chainF-2026-09-24.md` in the same commit (the twelve conditions' record).

## §AC1 · THE ARITHMETIC
```
  gemini-3.1-pro-high    greenfield x spec-change x {Paxos, FreeList, LZW} x {plain, salt-diet}   6 conditions   OWED -> DONE
  gemini-3.8-flash-high  greenfield x spec-change x {Paxos, FreeList, LZW} x {plain, salt-diet}   6 conditions   OWED -> DONE
                         each at 3 of 3 reached phase 2 and scored on the withheld suite (the result's §1)
  -------------------------------------------------------------------------------------------------
  MATRIX         DONE 180 · OWED 1 · BLOCKED 0 · INEXPR 16 · DECLARED 3   = 200
```
⇒ **180 + 1 + 0 + 16 + 3 = 200.** With chain D's eight (ADDENDA 20–22), all twenty level-8 conditions are DONE.
⚠️ **A DONE here means n = 3 reached and scored, never a verdict on the arms.** The result's §1 and §8 say what the twelve can and cannot carry.
⚠️ **Three conditions needed more than one attempt** (503 discards, A2.2); their discarded attempts are outside every count above (result §2).
Flash × Paxos ran on the successor export `2a674d7662b9` (level-8 ADDENDUM 11), the other ten on `2e342dcc02d1`.

## §AC2 · THE ONE STILL OWED
```
   1  level 7   gemini-3.8-flash-high × brownfield × Crc32 × salt-diet      l7cfss02 + l7cfss03 under level 7's registration, after F — F is done
```
Its closer is gemini's `--plan` for l7cfss02+03 on level 7's export, checked by the lead before any fire.

---
# ⚖️ ADDENDUM 24 — **LEVEL 7 §Q2 CLOSES: THE LAST OWED CONDITION REACHES n = 3. `DONE 180 → 181`, `OWED 1 → 0`.**
## bench, 2026-09-25, with ADDENDUM A of `RESULT-gemini-level7-2026-09-19.md` in the same commit (the condition's record).

## §AD1 · THE ARITHMETIC
```
  gemini-3.8-flash-high  brownfield x statement x Crc32 x salt-diet   OWED -> DONE   3 of 3 (l7cfss01 + l7cfssq01, l7cfssq02) LANDED,
                                                                                      scored, FULL PASS; pooling measured (one interface)
  -------------------------------------------------------------------------------------------------
  MATRIX         DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3   = 200
```
⇒ **181 + 0 + 0 + 16 + 3 = 200.** §Q2's own sentence, *"whoever fires them re-cuts this row"*, is discharged by this addendum.
⚠️ **The ids are `l7cfssq01/02`, not the `l7cfss02/03` that §Q2 and ADDENDA 21–23 name**: the old root is evidence and was not dispatched into
(the level-7 result's ADDENDUM A §A.2).

## §AD2 · WHAT OWED 0 MEANS, AND WHAT IT DOES NOT
- **Every condition of the Captain's 200-condition pilot matrix is DONE, INEXPRESSIBLE (16) or DECLARED unreached at the cap (3).** None is owed.
- **A DONE means n = 3 reached and scored on the withheld suite, never a verdict on the arms.** Each level's result of record says what its
  conditions can and cannot carry, and none of them claims that the salt method helps or hurts.
- **The 16 INEXPRESSIBLE and the 3 DECLARED are not DONE**, and a reader summing "complete" must say which of the three states is meant.

---

# ⚖️ ADDENDUM 25 — **§AD2's "n = 3 reached" IS TOO STRONG FOR 10 DONE CONDITIONS. A DEFINITION CLAUSE, NOT A RECOUNT: DONE STAYS AT 181.**
## bench, 2026-09-27, on the helm's routing, with `RESULT-descriptive-tables-v2-2026-09-27.md` (the four descriptive tables) on the same branch.

## §AE1 · WHAT IS WRONG, AND WHAT IS NOT
- §AD2 says *"A DONE means n = 3 reached and scored on the withheld suite."* **That is false as written for 10 of the 181.** The
  descriptive-tables map, which lists each condition's cells as its result of record lists them, finds 171 conditions with three
  cells and 10 with one or two.
- **The COUNT is not wrong.** This census counted each of the 10 DONE at its smaller n and said so where it did it: §C4 for the
  Opus spec-change row ("19 cells" for its ten conditions), §T2 for Sonnet's n = 2 conditions, and the
  level-1 result of record, which says of its own conditions *"n IS 1–4 PER CONDITION, NOT 3"*. What was wrong is the one-line
  summary written at ADDENDUM 24, which generalised the rule of the later blocks to the whole matrix.

## §AE2 · THE DEFINITION, CORRECTED
**DONE means a result of record merged in this repository that reports the condition's outcome, at the n that record states.** For
171 conditions that n is 3. The 10 below are DONE at a smaller n, each by its own record's words:
```
  claude-opus-5        FreeList × plain     × spec-change   n = 2   RESULT-p1-specchange-2026-09-10.md:36
                       FreeList × salt-diet × spec-change   n = 1   the same file :36, :40-41 ("a 0/1 is not a rate")
                       LRU      × plain     × spec-change   n = 2   the same file :35
                       LZW      × plain     × spec-change   n = 2   RESULT-specchange-1-2026-09-10.md:43
                       Paxos    × plain     × spec-change   n = 2   RESULT-p1-specchange-2026-09-10.md:37
                       Paxos    × salt-diet × spec-change   n = 2   the same file :37
  claude-sonnet-5      LRU      × plain     × none          n = 2   §T2 above; RESULT-claude-blockSG-2026-09-21.md
  gemini-3.1-pro-high  Crc32    × salt-diet × statement     n = 2   RESULT-p1-greenfield-2026-09-13.md:24
                       FreeList × plain     × none          n = 1   the same file :27, :54
                       FreeList × plain     × statement     n = 2   the same file :28
  (all greenfield)
```

## §AE3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH, SAID SO NOBODY READS IT AS MORE
- **It counts CELLS OF RECORD, not SCORABLE cells.** A record can list three cells and score fewer: §T2's Sonnet FreeList × salt-diet
  lists three cells and scores two (one BUILD-FAIL). **A census of scorable n across all 181 conditions is NOT taken here.** A reader
  who needs it reads each condition's record.
- It moves no condition. The LIVE figure stands: **DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.**
- It changes no result of record, and it makes no claim about the salt method.

---

# ⚖️ ADDENDUM 26 — **ADDENDUM 25 QUOTED §C4's "19 cells" AS THE OPUS SPEC-CHANGE ROW's POPULATION. IT IS 23. NOTHING ELSE MOVES.**
## bench, 2026-09-27, on the fresh non-author read of the arXiv v2 tables.
- §C4's "19 cells" is a 2026-09-14 figure. The row's ten conditions carry **23 cells of record** in the descriptive-tables map
  (`CELLMAP-descriptive-tables-v2-2026-09-27.tsv`): six conditions at n < 3 (2 + 1 + 2 + 2 + 2 + 2 = 11) and four at n = 3 (12).
- ADDENDUM 25 §AE1 used the figure only as evidence that this census counted those conditions at a smaller n. That evidence
  stands on the records' own lines, which §AE2 cites. The corrected definition and the list of 10 are unchanged.
- The LIVE figure is unchanged: **DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.**

---

# ⚖️ ADDENDUM 27 — **O37 JOINS AS ITS OWN SECTION: BLOCK N's SONNET COLUMN IS A RESULT OF RECORD. THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-09-28, with `RESULT-claude-blockNS-2026-09-28.md` in the same commit (the column's record), as the block's registration §N9 requires.

## §AF1 · WHY A SECTION AND NOT A ROW
O37's registration (`AMENDMENT-O37-nine-greenfield-claude-2026-09-25.md` §N9) says its population *"joins the census as its own section,
because the pilot's census is a result of record and is not re-opened."* The six problems here (Luby · AES · Liveness · MaxFlow ·
BinomialHeap · LinearScan) are not among the pilot's five, so no pilot condition changes state and **the pilot's line stands as ADDENDUM 26
left it: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AF2 · THE O37 SECTION — BLOCK N (Claude lane, greenfield × none), 24 conditions
```
  claude-sonnet-5  6 problems x {plain, salt-diet}   12 conditions   OWED -> DONE   36 cells, n = 3 each, scored on the withheld suite
                                                                                    (RESULT-claude-blockNS-2026-09-28.md)
  claude-opus-5    6 problems x {plain, salt-diet}   12 conditions   OWED           no result of record yet (block N's second, §N9)
  -------------------------------------------------------------------------------------------------
  BLOCK N        DONE 12 · OWED 12   = 24
```
⚠️ **OWED is this census's definition (ADDENDUM 25): no result of record.** It is not "unrun": ten of the Opus conditions already have three
scored cells, and the last two (LinearScan salt-diet #2 and #3) are firing on 2026-09-28. They become DONE when the Opus column's result of record lands, and not before.
⚠️ **O37's other 192 conditions** (statement and spec-change on these six, the three problems with no v3 rung, and the agy lane's sibling block)
are outside block N (§N1) and are not counted here. Each enters this section with its own block's result.

## §AF3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
A DONE is a merged result of record at the n it states (ADDENDUM 25), never a verdict on the arms. The Sonnet column's premiums are all
UNRESOLVED by registration, and its own §7 says what it cannot carry.

---

# ⚖️ ADDENDUM 28 — **O37 BLOCK NA (the agy lane) IS A RESULT OF RECORD: ALL 24 CONDITIONS DONE. THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-09-28, with `RESULT-gemini-blockNA-2026-09-28.md` in the same commit (both models' records), as §NA6 requires.

## §AG1 · THE O37 SECTION, RE-CUT
```
  BLOCK N  (Claude lane)   claude-sonnet-5        12 conditions   DONE    (ADDENDUM 27; RESULT-claude-blockNS-2026-09-28.md)
                           claude-opus-5          12 conditions   OWED    no result of record yet
  BLOCK NA (agy lane)      gemini-3.1-pro-high    12 conditions   DONE    RESULT-gemini-blockNA-2026-09-28.md §2
                           gemini-3.8-flash-high  12 conditions   DONE    RESULT-gemini-blockNA-2026-09-28.md §3
  -------------------------------------------------------------------------------------------------
  O37 (the 48 conditions the harness can express today)   DONE 36 · OWED 12   = 48
```
⚠️ **The 48 are O37's expressible slice, not its population.** O37's own population is 216 conditions, and the other 168 (statement and spec-
change on these six, and the three problems with no v3 rung) are outside both blocks. Each enters this section with its own block's result.

## §AG2 · WHAT A DONE HERE CARRIES, BESIDE THE FIGURE
- Every NA condition FIRED 3 cells. Two conditions carry a non-landing inside their n, and their records print it in its own column: Pro AES
  salt-diet (`naaeps01`, NOT-LANDED, 2 scored of 3) and Flash BinomialHeap salt-diet (`nabhfs03`, a RESULT labelled CUT-BOUND, 2 scored of 3).
  **A DONE is a merged result of record at the n it states (ADDENDUM 25), and "n = 3" here means three cells fired, not three scored.**
- `nabhfsr01` is outside every n and every count here (the XF ruling: a re-fire never replaces a RESULT).
- A DONE is never a verdict on the arms. Both NA records print the arm-correlated deadline cut beside every table, and neither claims the
  salt method helps or hurts.

---

# ⚖️ ADDENDUM 29 — **O37 BLOCK N's OPUS COLUMN IS A RESULT OF RECORD: THE 48 EXPRESSIBLE CONDITIONS ARE ALL DONE. THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-09-29, with `RESULT-claude-blockNO-2026-09-28.md` in the same commit (the column's record), as §N9 requires.

## §AH1 · THE O37 SECTION, RE-CUT
```
  BLOCK N  (Claude lane)   claude-sonnet-5        12 conditions   DONE    (ADDENDUM 27; RESULT-claude-blockNS-2026-09-28.md)
                           claude-opus-5          12 conditions   DONE    RESULT-claude-blockNO-2026-09-28.md
  BLOCK NA (agy lane)      gemini-3.1-pro-high    12 conditions   DONE    (ADDENDUM 28)
                           gemini-3.8-flash-high  12 conditions   DONE    (ADDENDUM 28)
  -------------------------------------------------------------------------------------------------
  O37 (the 48 conditions the harness can express today)   DONE 48 · OWED 0   = 48
```
⚠️ **The 48 are O37's expressible slice, not its population** (ADDENDUM 28 §AG1): the other 168 of O37's 216 are outside both blocks.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AH2 · WHAT A DONE HERE CARRIES, BESIDE THE FIGURE
- Every Opus condition has three scored cells of record. **LinearScan salt-diet's third is a re-fire** (`clbmrsr3`, under block N ADDENDA
  13–14, on saltbench PR #265): the cell it replaces, `clbmrs03`, lost its credential mid-run and is NOT-SCORED(HARNESS), in no n and no
  count here. That condition's three cells straddle two pools, declared in its record.
- A DONE is a merged result of record at the n it states (ADDENDUM 25), never a verdict on the arms. The Opus record's premiums are all
  UNRESOLVED by registration, and its §7 says what it cannot carry, including any comparison with the other model column.

---
# ⚖️ ADDENDUM 30 — **STEP g, THE ZERO-SPEND PART: SONNET LRU × PLAIN × none REACHES n = 3 OF RECORD. ADDENDUM 25's LIST OF TEN IS NINE.**
## bench, 2026-09-29, with ADDENDUM A of `RESULT-claude-blockSG-2026-09-21.md` in the same commit (the condition's record).

## §AF1 · WHAT MOVES
```
  claude-sonnet-5  greenfield × none × LRU × plain   n = 2 → 3   clbglp01 · clbglp02 · clbglp03, all PASS 16/16
```
§T2's reason for n = 2 was one missing receipt: `clbglp01` had no `served-<cell>.out`. blockSG ADDENDUM A derives it with the block's
own instrument (control equal to the harvest's receipt), and re-scores the cell under the block's own scorer (control reproduces). The
cell is a cell of record at n = 3. Its extra held probe and its by-hand provenance are stated there.

## §AF2 · WHAT DOES NOT MOVE YET, AND WHY
The three `gemini-3.1-pro-high` conditions in ADDENDUM 25's list (Crc32 × salt-diet × statement · FreeList × plain × none · FreeList ×
plain × statement) each have a THIRD cell that ran and landed: the top-ups `s3ctk01` · `s3fpk01`, `s3fpk02` · `s3fqk01`
(`RESULT-stage3-2026-09-12.md` ADDENDUM 1 §R3). **They are not yet cells of record here.** The descriptive-tables map counts a cell only
through a score receipt, and the map says of each one "in no score receipt". ADDENDUM 1 re-drove two of them in prose and carries the
other two as another seat's readings. The receipt is commissioned from the lane that owns them (gemini, zero spend). These three move
in a later addendum that cites it, with ADDENDUM 1 §R6.5's limit printed beside the n: the top-ups ran on export s2k and another client.
The v2 tables applied their registered rule correctly. They are a dated reading and are not changed.

## §AF3 · THE LIST, AS IT NOW STANDS
ADDENDUM 25 §AE2 less Sonnet LRU × plain × none: **nine conditions at n < 3.** Six are the Opus spec-change row, which the step-g freeze
(`AMENDMENT-stepg-opus-specchange-2026-09-29.md`, a separate PR) takes to n = 3 with seven cells. The other three wait on the receipt.
The LIVE figure is unchanged: **DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** Nothing here is a claim about the salt method.

---
# ⚖️ ADDENDUM 31 — **STEP g: THE THREE PRO CONDITIONS REACH n = 3 OF RECORD ON stage 3 ADDENDUM B's SCORE RECEIPT. THE LIST IS SIX.**
## bench, 2026-09-29, on `RESULT-stage3-2026-09-12.md` ADDENDUM B and its `RESULT-stage3-ADDENDUM-B-cells-2026-09-29.tsv` (gemini; saltbench #286,
## read by bench as non-author, merged).

## §AG1 · WHAT MOVES, WITH THE LIMIT BESIDE EVERY ROW
```
  gemini-3.1-pro-high  greenfield  condition                     n       cells of record (full passes)                       spans
                                   FreeList × plain × none       1 → 3   s3fp01 PASS 7/7 · s3fpk01 FAIL 6/7 · s3fpk02 FAIL 6/7  (1 of 3)   2 exports · 2 clients
                                   FreeList × plain × statement  2 → 3   s3fq01 · s3fq02 · s3fqk01, all PASS 7/7              (3 of 3)   2 exports · 1 client
                                   Crc32 × salt-diet × statement 2 → 3   s3ct01 · s3ct02 · s3ctk01, all PASS 6/6              (3 of 3)   2 exports · 2 clients
```
⛔ **The limit (ADDENDUM B §B4, ADDENDUM 1 §R6.5):** each top-up was built from export `3f83a69` while its condition's original cells were built
from `156fcb9`, and three of the four top-ups also ran on a different client binary. **Each of these three n = 3 figures spans two exports, and two of
them also span two clients.** The receipt settles what the cells SCORE. It does not settle the export axis. `s3ct01` is TRUNCATED: its PASS stands,
and its cost figures do not pool (§B4).

## §AG2 · THE LIST, AS IT NOW STANDS
ADDENDUM 25 §AE2's ten, less Sonnet LRU (ADDENDUM 30) and these three: **six conditions at n < 3, all in the Opus spec-change row**, which the
step-g freeze (`AMENDMENT-stepg-opus-specchange-2026-09-29.md`) takes to n = 3 with seven cells.
The LIVE figure is unchanged: **DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** Nothing here is a claim about the salt method.

---
# ⚖️ ADDENDUM 32 — **STEP g: THE SIX OPUS SPEC-CHANGE CONDITIONS REACH n = 3 OF RECORD. ADDENDUM 25's LIST OF TEN IS EMPTY.**
## bench, 2026-09-29, with `RESULT-stepg-opus-specchange-2026-09-29.md` in the same commit (the six conditions' record).

## §AH1 · WHAT MOVES, WITH THE PHASE-1 REACH BESIDE EVERY ROW (the helm's ruling on the step-g freeze makes the column mandatory)
```
  claude-opus-5  greenfield × spec-change   condition            n       reach (phase-1 landed / with an end)
                                            FreeList × plain     2 → 3   4 / 4
                                            FreeList × salt-diet 1 → 3   3 / 6
                                            LRU × plain          2 → 3   4 / 5
                                            LZW × plain          2 → 3   3 / 3
                                            Paxos × plain        2 → 3   4 / 4
                                            Paxos × salt-diet    2 → 3   3 / 5
```
Each condition's three cells and their suites are in the result's §3. **Paxos × salt-diet carries two verdicts for one of its cells
(`b22d1000`: published "0/0, does not build"; re-scored today, PASS 24/24 on byte-identical code), and this addendum moves n, never a
verdict.** The census of rc-3 verdicts of record that the helm ordered comes before any correction.

## §AH2 · THE LIST AND THE LIVE FIGURE
ADDENDUM 25 §AE2's ten: Sonnet LRU (ADDENDUM 30), the three Pro conditions (ADDENDUM 31) and these six. **None remains at n < 3.**
The LIVE figure is unchanged: **DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** Every DONE now reports its condition at
n = 3 CELLS OF RECORD (ADDENDUM 25 §AE3: cells of record, not scorable cells; a census of scorable n is still not taken). The 3 DECLARED are a
separate state. It is never a verdict on the arms, and nothing here is a claim about the salt method.

---
# ⚖️ ADDENDUM 33 — **NOT A COUNT ADDENDUM: THE 43 LEVEL-8 CELLS FIRED UNDER THE HIDING FENCE, EACH WITH ITS VERDICT AS SCORED. NO CONDITION MOVES.**
## bench (lead), 2026-10-01, desk ZI. It keeps a promise of this file's own 09-23 fence section: *"Level 8's result file lists each invalid
## cell with its verdict and the reason."* Neither level-8 RESULT does (`invalid` occurs 0 times in each), so the list goes here, beside the ruling.

## §AI1 · THE LIST, DERIVED
`evidence/l8-invalid-as-fired-2026-09-23/invalid_cells_verdicts.tsv` (sha256/16 `9f854047badbc815`), written by `invalid_cells_verdicts.py` in
the same directory. Its population is `hidden_root_census.out`'s HIDDEN wave cells (43; the three dry renders are excluded). Each verdict is
the cell's own row in a score file the run wrote. The declared scorer of record `e8c0d0512ab2` (AMENDMENT-gemini-level8 §A8.10.3) is preferred
where two files hold a row, and the scorer sha is printed beside every verdict. Nothing in it was typed.
```
  verdicts as scored   PASS 23 · FAIL 15 · BUILD-FAIL 1 · INCOMPLETE 1 · UNREAD 3        (43)
  the reason, all 43   the agy sandbox layer denied the cargo root's parent with no read carve-out (this file, 09-23 fence section)
```
⚠️ **THE BOUND OF THESE COUNTS, beside them (kent's read, 2026-10-01 07:35; the helm's order before merging): the 43 verdicts were
derived by the lead, on the lead box, from the agy lane's own runs directory, and NO non-author has re-run them.** The non-author read
checked that the TSV is exactly the census's 43 cells and that its counts are its own. The score files themselves are unreachable from the
reader's box, so every verdict here is the author's reading of the run's files.
## §AI2 · WHAT THE VERDICTS ARE, AND ARE NOT
- **They are NOT results and never enter a rate**, by the 09-23 ruling: the episode was not the registered task. They are printed so a
  reader of the level-8 results can see which fired cells were set aside, and what each read when it was scored.
- **UNREAD 3** = LRU × Pro × salt-diet (`l8rpss01–03`). The 09-22 leg's score directory holds the plain condition alone (its drive log reads
  "hand score of the plain condition"), and no score file anywhere under the runs directory holds those three rows (control: `l8rpps01` is found).
- **INCOMPLETE 1** = `l8zpps03`, scored before its end marker. This file's 09-23 section records that this cell forged `.seat/rt.result`.
  Its verdict is printed as the scorer wrote it and means nothing about the routine.
- **BUILD-FAIL 1** = `l8xpss03` (`TESTS 0/0`). This is the agy scorer's reading of the runner's exit 3, which the rc-3 split (CORRECTION 3;
  the agy lane's desk YU) separates into TIMEOUT · BUILD-FAIL · ABORT. It is not re-read here, and the cell is invalid either way.
- **One SELF-NOT row** (`l8xpss02`: the subject's own LANDING.md declares requirements NOT met) sits beside that cell's scored FAIL in the same
  file. It is printed apart as a note, never as the verdict.
- **The tripwire `l8rfpw01`** has two score files. The first, before the TESTS-needle fix, reads `TESTS 0/7` (the clause-failure count under
  a PASSES label, §A8.10.3). The list uses the re-score at `e8c0d05`.

---

# ⚖️ ADDENDUM 34 — **NOT A COUNT ADDENDUM: NO CONDITION OF THE 181 WAS SCORED PASS ON AN UNMEASURED SUITE. NO CONDITION MOVES.**
## bench, 2026-10-02, on the helm's orders of 17:06:13 and 17:43:10 (O57 · O64), before the arXiv v3 replacement. Two defects of one class, one line each.
- **D0.3 (the v3 referee read PASS when the hidden suite was not measured, a hang or a timeout):** NO condition of the 181 was scored by
  `referee_v3`. Every RESULT of record names an rc-based scorer (systems' scorer map, 181 of 181 by RESULT file). The referee is fixed in the
  private tree.
- **Its sibling (`score_wave_v3.sh`, the top-up and step-g scorers read PASS on the runner's rc 0 alone, so a solution that calls
  `process::exit(0)` before the suite prints `TESTS` would read PASS):** ZERO occurrences over the groups those scorers scored. Every PASS
  row carries `TESTS p/p` with p > 0, and each group's PASS count equals its RESULT's own:
```
  p1-greenfield 28 (RESULT §2: 28) · level 4 19 (12 + 7) · level 5: §A2's 15 PASS cells all lie in a 26-PASS superset, each with full TESTS · level 6 32 (18 + 14)
  blocks O · OS · SBS · SG · SS · SC (the evidence tables of record): every PASS with full p/t · step g 6 (cells.tsv) · p1-specchange 16 of 19 (its tsv)
```
  Method, and its bounds beside it: the scorers' own per-cell output was read as data, with a planted `<none>` row as a positive control
  (found). Separately, every `solution.rs` on both boxes was searched for a process exit, with a planted `exit(0)` as a positive control
  (found): 0 exits to status 0. The score files are in the private tree. kent re-ran the wave-format score files on the lead box with an
  independent parser and population (204 files, 385 PASS rows): 0 hits in the 181. The evidence tables, p1-specchange's tsv, the run box's
  own score files and the source search remain the lead's reading alone. One user tree on the run box was unreadable to that search; the score-file axis does not depend on it. The scorers are being
  changed to read a missing `TESTS` line as NOT-MEASURED, never PASS.

# ⚖️ ADDENDUM 35 — **NOT A COUNT ADDENDUM: TWO DECLARED LIMITS ON THE GEMINI LANE. NO CONDITION MOVES.**
## bench, 2026-10-13, on the helm's orders of 13:07 (the briefing route) and 17:57 (O57). Each limit rides beside the verdicts it limits.
- **The briefing receipt's second route (s3 and b4).** Level 5's result already declares that its receipt token was also readable at
  `ctl/briefing-nonce` (§D2 of `RESULT-gemini-flash-level5-2026-09-15.md`). **The s3 and b4 receipts carry the same limit:** across the 92
  legacy-layout cells of record (s3 38 · b4 12 · l5 42), 27 subjects used a side route (`ctl/briefing-nonce`, `ctl/launch.log` or an `ARMRECV`
  search), every one AFTER opening the arm file (s3 1, `s3cs03` · l5 26 · b4 0), and 0 echoed through a side route before touching the arm
  file. So no receipt of record changes. Source: `evidence/agy-ctl-census-2026-10-13/side-route-all-legacy.out`. ⚠️ The count is of calls that
  NAME a side route. Whole-cell and `ctl/*` searches were cross-checked by a non-author (kent): 2 cells ran a cell-root content search for
  `Receipt` before the arm-file read, and neither surfaced the nonce (`AMENDMENT-agy-ctl-fence-2026-10-13.md` §4).
- **agy T excludes sub-agent conversations: ≥ 15.2 % unmetered on salt-diet, 0.2 % on plain** (`evidence/o57-agy-subagent-unmetered-2026-10-13/`).
  The census reports no token figure, so no count moves here. The limit is recorded because the paper's Tables T1–T4 print Gemini medians
  and salt-diet ÷ plain ratios from that meter, and those ratios are biased LOW (toward salt-diet) by at least that.

# ⚖️ ADDENDUM 36 — **NOT A COUNT ADDENDUM: THE BROWNFIELD GIVENS' REFUTER PASS (desk KT), AND TWO LIMITS ON ABSOLUTE DIFFICULTY. NO CONDITION MOVES.**
## bench, 2026-10-17, on the helm's routing of desk KT (rec (4): the five frozen givens get the refuter pass a card gets). A non-author (kent) ran it.
- **The population.** 72 brownfield conditions of record, 18 per model, each consumed the given at saltbench-systems `eacb9ec` for its
  problem: Crc32 16 · FreeList 16 · LRU 16 · LZW 16 · Paxos 8. By block: Pro L4 4 · Pro L7 14 · Flash L6 4 · Flash L7 13 + §Q2 1 · Sonnet SB 10
  · SBS 8 · Opus O 10 · OS 8. The export each one was built from (`ecd3924` for L4's LRU and Paxos, which have one blob in all history;
  `abb7829` · `9bfb6ef` · `2833621` · `eb18e5d` for the rest) carries the `eacb9ec` blob, read at the object. The four Pro L4 FreeList/LZW
  conditions that consumed the PRE-repair givens are the ones ADDENDUM 6 already reverted. They are not in the 72.
- **The pass.** Each given is real and reachable through the v3 interface, and NO LEAK of a withheld reference was FOUND by three checks (the
  code delta against the reference · the tell audit, rc 0 · a search of the givens and addenda for the withheld driver's test names and for
  withheld/hidden/mutant words); for Paxos the test-name check is PARTIAL (its tests live in `driver_main.rs` and its traces). The given's own test results re-drive
  equal to the record's (tests PASSED by the given: Crc32 1/6 · FreeList 6/7 · LRU 10/16 · LZW 3/8 · Paxos 11/17; the plain reference passes all, as control). Each
  given differs from its reference IN CODE (comments stripped) by the planted line(s) alone; the comments and banner also differ, which the tell
  audit's containment rule covers. A disagreement between readers on LRU is resolved toward CLEAN on a
  measurement of the file's style.
- **⚠️ LIMIT, ABSOLUTE DIFFICULTY (Crc32, 16 conditions).** The given's doc comment states eight bit-steps above a loop that runs seven. A
  reader who trusts the comment is pointed at the planted defect. **LIMIT (LZW, 16 conditions):** the given's comment repeats the card. Both are
  comment/code contradictions that the containment audit passes by construction (the comment is in the reference). Both arms of a condition
  received the same bytes. So a tell can make the problem easier in absolute terms, and it cannot by itself produce an arm difference.
  ⚠️ **UNMEASURED:** whether the method changes how closely a subject reads comments, which would let a constant tell interact with the arm.
- **What this does not change:** no condition's status, no score, no figure. It is a limit that rides beside the Crc32 and LZW brownfield rows.

# ⚖️ ADDENDUM 37 — **NOT A COUNT ADDENDUM: THE MID-CELL ROOT GAP, MEASURED OVER THE CELLS OF RECORD. NO CELL OF RECORD NAMED A ROOT IT COULD HAVE READ. NO CONDITION MOVES.**
## bench, 2026-10-17, on the helm's question of 2026-10-17 03:11: did every cell of record get an escape scan, and did any cell's life span the birth of another cell root?
**The gap** (measured by the systems lane that night, zero spend): a cell's fence denies the cell roots that exist when it is rendered. A
root created AFTER the render was readable to that cell's subprocesses for the rest of its life, and so was a SIBLING cell created inside the
cell's own root. Nothing here measures whether a subject read such a root's CONTENT; it measures whether the window existed, and whether the
cell's own record names what it could have reached. Evidence: `evidence/midcell-gap-2026-10-17/` (its README names each file and script).
- **The population.** Every DONE row of the correctness cell map that names a cell: 543 rows, 520 distinct cells, each joined to its window
  on the run box (the first time stamp of its watch or launch log to its last end marker). A cell id held in more than one root is resolved by
  rule, printed per row: the map's own root, else the root without a dead suffix, else census ADDENDUM 22's rule, and in one case (`l5cp01`)
  by measurement (its own logs read the result of record's T; the other copy does not). 0 rows were left ambiguous, without a window, or
  missing. **The 94 COUNT rows and 14 CONDITION rows name no cell, so they are UNMEASURABLE by cell here.**
- **Another root born inside a cell's window:** 50 rows, 48 distinct cells (Claude 37, Gemini 11). In 7 of the 48, every such root is on the
  cell's OWN deny list, so it was denied, not exposed. In the other 41, it was not. **In all 48, no such root's name occurs in the cell's own
  record outside its fence render** (the agy lane's record is its `ctl/` stream and logs; a Claude cell's adds every session file of its
  transcript). Controls per cell: the record is non-empty and holds the cell's own id; all 48 pass. A positive control on the count itself: a run
  that read the fence renders as part of the record found every one of the 7 fenced names (2 to 6 hits each; `exposed-namehits-control.tsv`, `NAMEHITS_CONTROL=1`), so the count finds a name when it is there.
- **A sibling born inside the cell's own root:** of the 520 cells, 503 had none. 13 had one and never named it. 4 had two, both on the
  cell's own deny list. A transcript record that is the client echoing the cell's settings is not counted. A run that counted it found
  the echo, which shows that the transcripts were in the haystack.
- **Escape coverage, Claude lane: 244 of 244 cells of record, every one 0 other-root hits.** 182 were scanned by the chain at harvest. The 62
  that predate the chain (by root: `cells-matrix1` 33 · the two `cells-stmt-*-2026-09-09` roots 18 · the `cells-clb-g-*` roots 7 · `cells-n3-topup` 3 · `cells-clb-sg-lru-plain` 1) were scanned
  on 2026-10-17 by the same scanner over their surviving transcripts. Each of the 62 read 58 to 284 tool inputs. **The agy lane has no such
  scanner** (it reads Claude tool records), so for Gemini cells the evidence is the name census above, over the cells that were exposed. It is
  not a measurement of other-root access in general.
- ⚠️ **LIMITS, beside the verdicts.** (1) A root deleted before this census is invisible to it. (2) 11 cells (7 other-root, 4 in-root) had a born-inside root on
  their own deny list, so that root existed at render, and they are counted FENCED, not EXPOSED. A window's start can therefore predate its
  render, or a birth time is not a root's first appearance, so the EXPOSED counts (41 other-root, 13 in-root) may lean HIGH, which is the
  conservative direction for this question. (3) A name census finds a reach by NAME. A wildcard or a parent-directory listing that never prints the name
  is not counted. The escape scan reads every Claude tool input for another root's path, so it closes that hole for the Claude lane only.
  (4) None of this re-scores a cell.
- **What this does not change:** no condition's status, no score, no figure. The paper's limits section carries one sentence for it: *"A cell
  root created during a run was not covered by that run's fence; over the cells of record, no cell's record names such a root, and every
  Claude cell's escape scan reads zero other-root accesses."*

---
# ⚖️ ADDENDUM 38 — THREE SONNET MEDIAN COST RATIOS CORRECTED IN THE LAST DIGIT (bench, 2026-10-19). No condition, score or count moves.
Found by a non-author refuter pass (`RESULT-argon-refuter-2026-10-19.md`, F4, objective O86) and confirmed by bench on the tables of
record. The ratios in §U3, §W2 and §X4 (and the per-block lines above them) were ratios of the ROUNDED medians. From the unrounded
`final_COST` columns:
```
  block   printed   unrounded   table of record
  SG       8.27x      8.29x     blockSG-cells.tsv (29 cells)
  SS       5.32x      5.31x     blockSS-cells.tsv
  SBS      4.71x      4.70x     blockSBS-cells.tsv     (and its total COST ratio: 9.58x printed, 9.59x unrounded)
  O        1.89x      1.89x     right
  OS       1.40x      1.40x     right
```
⚠️ **The DECLARED cost-convention section above (desk VX (b)) already read SS 5.31x and SBS 4.70x**, while it said its table *"reproduces
this document's SS, SBS, OS and O figures to the second decimal"*. It did not: the document printed 5.32x and 4.71x. **The agreement
claimed there was wrong in the last digit, and nobody re-read it.**
**What this does not change:** the order of the blocks, every bound, and every sign. The three Sonnet ratios are still lower bounds, and
the Opus OS ratio is still the smallest. The paper's three ratios are corrected in the same PR.
⚠️ **AND THE PAPER'S CONVENTION SENTENCE MOVES WITH IT.** The paper already takes SS and SBS PROBE-APART from the VX split (5.54x,
5.12x), and states SG and OS PROBE-IN because the split was taken on a different cell set. Its clause that the split's probe-in
readings sit *"a hundredth below the record's"* stops being true once the record reads 5.31x and 4.70x, so the same PR changes it to
*"equal to the record's"*, and the record's SG figure it quotes from 8.27x to 8.29x.

---
# ⚖️ ADDENDUM 39 — **O37: LU IS DECLARED NOT FEASIBLE AS A RUST PORT. ITS 24 CONDITIONS ARE DECLARED BESIDE THE SECTION, AS THE PILOT'S 16 INEXPRESSIBLE ARE. THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-11-11, on the Captain's council word of 2026-11-10 (ask 3, his whole word on the pack: "Accept recs, keep objectives").

## §AJ1 · WHAT WAS RULED
The recommendation he accepted read: LU is declared NOT FEASIBLE as a Rust port; its 24 conditions are reported as DECLARED beside the
census, as the 16 inexpressible were; no harness-library spike. The port verdict it rests on is bench's of 2026-11-10 (systems lane, not
in this repository). Its reasons, so a reader here need not follow it:
- v1's LU card is exact rational arithmetic by construction, and its tests include Hilbert matrices, named for their rational growth.
- A good answer is decidable (every entry of L and U is a ratio of minors), so the task is not disqualified for having no finite check.
- The executable checker that a treatment submission must ship does not fit a machine word on the card's own tests: checking PA = LU
  exactly needs a common denominator that leaves i128 at small orders, and Verus's standard library carries no verified bignum.
- Each way to meet that changes what the arm measures on this card: every treatment submission verifies its own bignum (the cost is then
  bignum verification, not elimination), or the harness supplies one as a given no other v3 card carries. Shrinking the inputs to fit
  i128 drops the Hilbert growth, and a finite field is a different task.

## §AJ2 · THE O37 SECTION, RE-CUT
```
  O37's population (ADDENDUM 28 §AG1)                                                     216
    expressible slice, blocks N and NA (ADDENDUM 29)          DONE 48                      48
    LU x {4 models} x {plain, salt-diet} x {none, statement, spec-change}   DECLARED       24   (this addendum)
    NTT and WHT, 48 conditions                                 outside every block today   48
    statement and spec-change on the six block-N problems      outside every block today   96
```
The 24 are 4 models (the two Claude and the two agy models of blocks N and NA) x 2 arms x 3 extras. A DECLARED condition is reported
beside the section with its reason, never counted DONE and never silently removed from O37's 216.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AJ3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
It says the port was not built and why. It says nothing about LU in Lean, about any model's ability on LU, or about the salt method. NTT
and WHT have v3 rungs built on the systems lane (2026-11-10); they enter this section only with their own block's result.

---
# ⚖️ ADDENDUM 40 — **O37: BLOCK WA's FLASH HALF IS A RESULT OF RECORD. FOUR CONDITIONS MOVE TO DONE (WHT and NTT × {plain, salt-diet} × gemini-3.8-flash-high). THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-11-14, in the same commit as `RESULT-gemini-blockWA-flash-2026-11-14.md` (§WA6: the census section is re-cut with the result).

## §AK1 · WHAT MOVED
The four Flash conditions of block WA (`AMENDMENT-O37-wht-ntt-greenfield-agy-2026-11-13.md`, ADDENDUM 1) each have n = 3 cells of record,
all scored: FULL PASS 3 of 3 in each (the result's §2). DONE here means the condition has its cells of record and a result file; it is not
a verdict on the arms, and with every cell at ceiling the result says nothing about one.

## §AK2 · THE O37 SECTION, RE-CUT
```
  O37's population (ADDENDUM 28 §AG1)                                                                  216
    DONE         blocks N and NA (ADDENDUM 29)                                                    48
                 block WA, Flash: WHT, NTT x {plain, salt-diet} x gemini-3.8-flash-high (this)      4
    DECLARED     LU, 24 conditions (ADDENDUM 39)                                                   24
    NOT DONE     WHT and NTT, the other 44:
                   x none, Claude lane, block W: released 2026-11-14, cells firing                   8
                   x none, gemini-3.1-pro-high, block WA's Pro half: HELD (ADDENDUM 1)                4
                   x spec-change, Claude lane, block WC: signed, gated on block W's result            8
                   x statement, both lanes; x spec-change, agy lane: in no block                     24
                 the six block-N problems x {statement, spec-change}, 96:
                   x spec-change, Claude lane, block NC: released 2026-11-14, cells firing           24
                   x statement, Claude lane, block T: signed, waits on the Captain's read            24
                   x {statement, spec-change}, agy lane: in no block                                48
```
DONE 52 · DECLARED 24 · NOT DONE 140 = 216. A NOT DONE condition is only DONE when its block's result file lands, by a later addendum;
"released" and "firing" are states of a registration, never of a result. Block WA's Pro half becomes NOT-FIRED(MODEL) only by the
default ADDENDUM 1 names, through its own addendum here.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AK3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
Nothing about WHT or NTT on the Claude lane (block W has no result yet), nothing about any Pro model, nothing Claude-versus-agy, and
nothing about the salt method. The registration states in §AK2 are as of this addendum's date and are not results.

# ⚖️ ADDENDUM 41 — **A LIMIT ON THE agy CELLS OF RECORD: THEIR TOOLS FAILED ON AN UNWRITABLE /tmp/claude, SALT-DIET 32 OF 141 CELLS, PLAIN 2 OF 139. NO COUNT MOVES.**
## bench, 2026-11-15. Source: `evidence/o37-agy-tmpclaude-2026-11-15/` (README: method, controls, limits; one row per cell of record in `cellmap-join.tsv`).

## §AL1 · WHAT WAS FOUND
Before export 3796e6b4 (block WA ADDENDUM 3, arm L), 791 of the run box's 792 agy srt turn-loop env files omit `CLAUDE_CODE_TMPDIR`; without it the
subject's shell has `TMPDIR=/tmp/claude` (block WA's F2 battery), which the sandbox does not let it write. The shell ran; a tool inside it that
makes a temp file failed (`mktemp`, `patch`, rustc). Which fence arm (srt or seatbelt) each cell ran is not shown here: the cause is
established for srt cells, and a hit is a printed failure whatever its cause. Over the matrix's agy cells of record (`CELLMAP-descriptive-tables-v2-2026-09-27.tsv`, arm as
registered), the cells whose stream prints that failure:
```
  gemini-3.1-pro-high    plain 2 of 68      salt-diet 21 of 70 (+2 ambiguous ids)
  gemini-3.8-flash-high  plain 0 of 71      salt-diet 11 of 71
```

## §AL2 · WHAT IT MEANS FOR THIS CENSUS
Nothing in a count. A condition is DONE because it has its cells of record and a result file, and this census states no verdict on the arms.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** O37's line (§AK2) is unchanged.
But any per-arm cost or correctness reading off the agy cells carries an environmental defect that hit salt-diet cells far more often
than plain ones. It is not expected to manufacture a salt-diet advantage, but its sign on cost and outcome is not measured here. Each agy RESULT file that names a hit cell carries the same limit, appended.

## §AL3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
That any cell's outcome or cost changed (a hit is a failure the stream printed; a subject can retry or work around it). Anything about the
Claude lane, which this census of streams does not measure.

# ⚖️ ADDENDUM 42 — **A LIMIT ON SIX CLAUDE-LANE SALT-DIET CELLS OF RECORD: THE ARM'S OWN GATE COULD NOT MAKE ITS TEMP DIR AT ITS SELFTEST. NO COUNT MOVES.**
## bench, 2026-11-15. Source: `evidence/o37-claude-gate-mkdtemp-2026-11-15/` (README: method, controls, the two needles not used, limits; one row per condition-row in `claude-join.tsv`).

## §AM1 · WHAT WAS FOUND
In these cells a command's output shows `mkdtemp failed on /tmp/claude-<uid>/gatest.XXXX: Operation not permitted`, then `gate: selftest in`:
the salt-diet gate's selftest could not make its directory under the sandbox's TMPDIR. Searched in tool results only, over every Claude-lane
cell transcript on the run box (2,513), joined to the matrix's Claude DONE rows by cell id, arm as registered:
```
  claude-opus-5    plain 0 of 65      salt-diet 2 of 66     (one cell, d6b53ee4: LRU none and its spec-change)
  claude-sonnet-5  plain 0 of 68      salt-diet 5 of 60     (clbgfs02, clbbcs03, clbbzs01, clbccs01, clbccs03)
```
The plain arm has no gate, so it cannot show this. Two more hits are in cells of two of the three DECLARED conditions (Sonnet LZW and
Paxos, salt-diet, spec-change: clbczs01, clbcps01).

## §AM2 · WHAT IT MEANS FOR THIS CENSUS
Nothing in a count. ⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** A DECLARED condition
stays DECLARED: it was unreached at the cap, and this addendum does not read why. Each RESULT file that names or holds a hit cell carries
the same limit, appended. ADDENDUM 41 is the agy lane's (a different client and a different failure). The two are not the same kind of
fact: there the count is arm-correlated in cells of both arms; here plain cannot show it, because only the treatment arm has the gate.

## §AM3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
That any subject failed to run its gate in the end, or that any outcome or cost moved; its sign on either. That the DECLARED conditions'
being unreached has anything to do with it.

# ⚖️ ADDENDUM 43 — **O37: BLOCK W IS A RESULT OF RECORD. EIGHT CONDITIONS MOVE TO DONE (WHT and NTT × {plain, salt-diet} × {Opus, Sonnet}, Claude lane). THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-11-15, in the same commit as `RESULT-claude-blockWO-2026-11-15.md` and `RESULT-claude-blockWS-2026-11-15.md` (§W9: the census section is re-cut with the result).

## §AN1 · WHAT MOVED
The eight conditions of block W (`AMENDMENT-O37-wht-ntt-greenfield-claude-2026-11-11.md`, released by its ADDENDUM 2) each have n = 3 cells
of record, all scored against the withheld suite; the two result files print each condition's correctness and cost. DONE here means the
condition has its cells of record and a result file; it is not a verdict on the arms.

## §AN2 · THE O37 SECTION, RE-CUT (registration states as of 2026-11-15)
```
  O37's population (ADDENDUM 28 §AG1)                                                                  216
    DONE         blocks N and NA (ADDENDUM 29)                                                    48
                 block WA, Flash: WHT, NTT x {plain, salt-diet} x gemini-3.8-flash-high (ADDENDUM 40)  4
                 block W: WHT, NTT x {plain, salt-diet} x {Opus, Sonnet}, Claude lane (this)      8
    DECLARED     LU, 24 conditions (ADDENDUM 39)                                                   24
    NOT DONE     WHT and NTT, the other 36:
                   x none, gemini-4-argon-high, block WA's Pro half: firing (WA ADDENDA 2, 4, 5)    4
                   x spec-change, Claude lane, block WC: signed, gated on block W's result          8
                   x statement, both lanes; x spec-change, agy lane: in no block                     24
                 the six block-N problems x {statement, spec-change}, 96:
                   x spec-change, Claude lane, block NC: released 2026-11-14, cells firing           24
                   x statement, Claude lane, block T: released to build (council 2026-11-14)        24
                   x {statement, spec-change}, agy lane: in no block                                48
```
DONE 60 · DECLARED 24 · NOT DONE 132 = 216. "Released", "firing" and "gated" are states of a registration, never of a result.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AN3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
Nothing about WHT or NTT under any other extras or lane, nothing Opus-versus-Sonnet as models, nothing about the salt method. One cell's
end kind (`clbdtp03`, EXIT-FORCED) is a harness fault, as the Opus result's §1 states; its score is the withheld suite's.

# ⚖️ ADDENDUM 44 — **O37: BLOCK WA's PRO HALF IS A RESULT OF RECORD. FOUR CONDITIONS MOVE TO DONE (WHT and NTT × {plain, salt-diet} × gemini-4-argon-high). THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-11-15, in the same commit as `RESULT-gemini-blockWA-pro-2026-11-15.md` (§WA6: the census section is re-cut with the result).

## §AO1 · WHAT MOVED
The four Pro conditions of block WA (`AMENDMENT-O37-wht-ntt-greenfield-agy-2026-11-13.md`, re-registered on `gemini-4-argon-high` by its
ADDENDUM 2 and released by ADDENDA 3–5) each have n = 3 cells of record, all scored: FULL PASS 3 of 3 in each (the result's §2), four
salt-diet passes being floors (TRUNCATED). DONE here means the condition has its cells of record and a result file; it is not a verdict on
the arms. The condition is argon's, under ADDENDUM 2's model seam; ADDENDUM 40's line for this slot read gemini-3.1-pro-high and HELD,
and ADDENDUM 43's read argon and firing.

## §AO2 · THE O37 SECTION, RE-CUT (registration states as of 2026-11-15)
```
  O37's population (ADDENDUM 28 §AG1)                                                                  216
    DONE         blocks N and NA (ADDENDUM 29)                                                    48
                 block WA, Flash: WHT, NTT x {plain, salt-diet} x gemini-3.8-flash-high (ADDENDUM 40)  4
                 block W: WHT, NTT x {plain, salt-diet} x {Opus, Sonnet}, Claude lane (ADDENDUM 43)  8
                 block WA, Pro: WHT, NTT x {plain, salt-diet} x gemini-4-argon-high (this)         4
    DECLARED     LU, 24 conditions (ADDENDUM 39)                                                   24
    NOT DONE     WHT and NTT, the other 32:
                   x spec-change, Claude lane, block WC: signed, baselines run, release drafted      8
                   x statement, both lanes; x spec-change, agy lane: in no block                     24
                 the six block-N problems x {statement, spec-change}, 96:
                   x spec-change, Claude lane, block NC: released 2026-11-14, cells firing           24
                   x statement, Claude lane, block T: released to build (council 2026-11-14)        24
                   x {statement, spec-change}, agy lane: in no block                                48
```
DONE 64 · DECLARED 24 · NOT DONE 128 = 216. "Released", "firing" and "drafted" are states of a registration, never of a result.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AO3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
Nothing about any `gemini-3.1-pro-high` model, nothing Flash-versus-argon or Claude-versus-agy, nothing about the salt method. One cell's
end kind (`wanas301`, PERSIST-INDETERMINATE) is ruled landed by WA ADDENDUM 6 item 3; its score is the withheld suite's.

---
# ⚖️ ADDENDUM 45 — **O37: BLOCK WC IS A RESULT OF RECORD. EIGHT CONDITIONS MOVE TO DONE (NTT and WHT × {plain, salt-diet} × {Opus, Sonnet}, spec-change, Claude lane). THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-11-17, in the same commit as `RESULT-claude-blockWCO-2026-11-17.md` and `RESULT-claude-blockWCS-2026-11-17.md` (§WC7 = NC §C8: the census section is re-cut with the result).

## §AP1 · WHAT MOVED
The eight conditions of block WC (`AMENDMENT-O37-wht-ntt-specchange-claude-2026-11-13.md`, released by its ADDENDA 1–2, with ADDENDA 3–4
on one source and its export record) each have their cells of record and a result file. Seven have n = 3. **Sonnet NTT salt-diet has
n = 1**: its #2 and #3 sources were fresh phase 1s that ended CAP-COST without landing, two REACH LOSSES (the WCS result's §1), never
re-run. Every phase-2 cell of record passes its withheld B suite in full (each result's §2). DONE here means the condition has its cells
of record and a result file, at the n its record states; it is not a verdict on the arms.

## §AP2 · THE O37 SECTION, RE-CUT (registration states as of 2026-11-17)
```
  O37's population (ADDENDUM 28 §AG1)                                                                  216
    DONE         blocks N and NA (ADDENDUM 29)                                                    48
                 block WA, Flash: WHT, NTT x {plain, salt-diet} x gemini-3.8-flash-high (ADDENDUM 40)  4
                 block W: WHT, NTT x {plain, salt-diet} x {Opus, Sonnet}, Claude lane (ADDENDUM 43)  8
                 block WA, Pro: WHT, NTT x {plain, salt-diet} x gemini-4-argon-high (ADDENDUM 44)   4
                 block WC: NTT, WHT x spec-change x {plain, salt-diet} x {Opus, Sonnet} (this)     8
    DECLARED     LU, 24 conditions (ADDENDUM 39)                                                   24
    NOT DONE     WHT and NTT, the other 24:
                   x statement, both lanes; x spec-change, agy lane: in no block                     24
                 the six block-N problems x {statement, spec-change}, 96:
                   x spec-change, Claude lane, block NC: released 2026-11-14, cells firing           24
                   x statement, Claude lane, block T: released to build (council 2026-11-14)        24
                   x {statement, spec-change}, agy lane: in no block                                48
```
DONE 72 · DECLARED 24 · NOT DONE 120 = 216. "Released" and "firing" are states of a registration, never of a result.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AP3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
Nothing about a spec-change reached from a phase 1 that did not land (the two reach losses are counted, never scored), nothing
Opus-versus-Sonnet, nothing about the salt method. Every premium in both results is UNRESOLVED-UNDERPOWERED as registered.

---
# ⚖️ ADDENDUM 46 — **O37: BLOCK NC IS A RESULT OF RECORD. 22 CONDITIONS MOVE TO DONE; 2 ARE DECLARED UNREACHED (LinearScan × spec-change × salt-diet, both models: no source reached phase 2). THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-11-17, in the same commit as `RESULT-claude-blockNCO-2026-11-17.md` and `RESULT-claude-blockNCS-2026-11-17.md` (§C8: the census section is re-cut with the result).

## §AQ1 · WHAT MOVED
Block NC (`AMENDMENT-O37-blockNC-specchange-claude-2026-11-13.md`, ADDENDA 1–5) has its 72 condition-cells ended and two result files.
22 conditions have cells of record and move to DONE, at the n each record states (Opus LinearScan plain at n = 2, Sonnet MaxFlow
salt-diet at n = 1, the rest n = 3). **Two conditions have NO cell of record:** Opus LinearScan salt-diet (three fresh sources ended
CAP-COST) and Sonnet LinearScan salt-diet (two ended CAP-COST; one landed and failed its G baseline, 6 of 9). No phase 2 exists for
either, and §C2 never re-runs a reach loss, so they are DECLARED unreached, beside the section, as the pilot's DECLARED are. DONE is not
a verdict on the arms. ⚠️ Every Liveness failure in both results is one clause test (each result's §1); it is put to a non-builder read
as a possible suite defect (§C6 item 4) and no arm reading rests on it.

## §AQ2 · THE O37 SECTION, RE-CUT (registration states as of 2026-11-17)
```
  O37's population (ADDENDUM 28 §AG1)                                                                  216
    DONE         blocks N and NA (ADDENDUM 29)                                                    48
                 block WA, Flash: WHT, NTT x {plain, salt-diet} x gemini-3.8-flash-high (ADDENDUM 40)  4
                 block W: WHT, NTT x {plain, salt-diet} x {Opus, Sonnet}, Claude lane (ADDENDUM 43)  8
                 block WA, Pro: WHT, NTT x {plain, salt-diet} x gemini-4-argon-high (ADDENDUM 44)   4
                 block WC: NTT, WHT x spec-change x {plain, salt-diet} x {Opus, Sonnet} (ADDENDUM 45)  8
                 block NC: the six block-N problems x spec-change, Claude lane (this), 24 less 2  22
    DECLARED     LU, 24 conditions (ADDENDUM 39)                                                   24
                 block NC: LinearScan x spec-change x salt-diet x {Opus, Sonnet}, unreached (this)  2
    NOT DONE     WHT and NTT, the other 24:
                   x statement, both lanes; x spec-change, agy lane: in no block                     24
                 the six block-N problems x {statement, spec-change}, the other 72:
                   x statement, Claude lane, block T: released to build (council 2026-11-14)        24
                   x {statement, spec-change}, agy lane: in no block                                48
```
DONE 94 · DECLARED 26 · NOT DONE 96 = 216. "Released" is a state of a registration, never of a result.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AQ3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
Nothing about a spec-change reached from a phase 1 that did not land, nothing Opus-versus-Sonnet, nothing about the salt method. Every
premium in both results is UNRESOLVED-UNDERPOWERED as registered.

---
## ADDENDUM 46, NOTE 1 (2026-11-17, bench) — appended; no count moves
ADDENDUM 46 put block NC's six Liveness clause failures to a non-builder read as a possible suite defect. systems' read (bus offset
105,218,390) answers YES: the clause test fixes one reading of the card's "sweep" and all six cells counted another reading the card
admits. The cells stand as they fell and no O37 count moves (DONE 94 · DECLARED 26 · NOT DONE 96 = 216); both block NC results carry
it as their ADDENDUM 1; the card is amended before any later Liveness run.



---

# ⚖️ ADDENDUM 47 — **O37: A LIMIT ON THREE agy CELLS OF RECORD: THE CLIENT SERVED THEM A WEB SEARCH (WEB-SERVED). NO COUNT MOVES; NOTHING IS VOIDED; THE THREE LEAVE EVERY COMPARISON.**
## gemini (the hand), 2026-11-20, on the lead's ruling on the bus (2026-11-20 00:29:42, helm-reversible). Appended; everything above is unchanged.

## §AR1 · WHAT WAS FOUND
The client's main stream records `search_web` as a step that goes ACTIVE then DONE with no result body, so a stream cannot tell a served call from a denied one; the client's own conversation record (the brain transcript under the cell's `.agyhome`) carries the result. Read there, every `search_web` call on the run box was served (96 of 96), and the canonical PreToolUse hook, registered in each of these cells, denied none. Level 6 AMENDMENT A5.2's "0 of the 48 served" and A6.4's "0 network-tool results were served" were stream censuses; both carry a correction addendum of this date.

## §AR2 · THE CELLS OF RECORD OF THIS MATRIX DECLARED WEB-SERVED
Of 272 agy cells of record, every one with a brain transcript, 269 were served nothing and three were served a search:

- `l5psra202` (gemini-3.8-flash-high, salt-diet): 1 search result(s) served; first query *"verus" "failed this postcondition" forall exists*
- `l6vbpp02` (gemini-3.8-flash-high, plain): 1 search result(s) served; first query *"ARMRECV" receipt*
- `l7npfs01` (gemini-3.1-pro-high, salt-diet): 1 search result(s) served; first query *docs/STATEMENTS.md*

Blocks NA (5 cells) and ZF (2) carry the same declaration in their RESULTs; blocks WA and TA were served nothing.

## §AR3 · WHAT THIS ADDENDUM DOES NOT DO
**No count in this census moves:** a DONE reports its condition's outcome, and nothing is voided (A5.2 voids only FENCE-TAMPER). The three cells leave every comparison; the re-cut of the tables is a separate change. Nothing here is about the salt method.

Source: `evidence/o37-agy-web-served-2026-11-20/` (README: method, controls, limits).

# ⚖️ ADDENDUM 48 — **THE CLAUDE LANE CALLED NO WEB TOOL: 0 `WebSearch`/`WebFetch` CALLS IN 3,175 CELL TRANSCRIPTS ON THE RUN BOX, AND EVERY RECORDED LAUNCH LEFT BOTH OFF THE SUBJECT'S TOOL SURFACE. NO COUNT MOVES. A WEB CALL'S REFUSAL IS NOT SHOWN, BECAUSE NONE WAS MADE.**
## bench, 2026-11-22. Appended; everything above is unchanged.

## §AS1 · WHAT WAS MEASURED
Every Claude-lane cell transcript on the run box (748 cell project directories, 3,175 transcripts, subagent transcripts included, no file counted twice) was searched for a `WebSearch` or `WebFetch` tool call. There are 0, and the two names are absent from the full list of tool names the cells called. The parser can see such calls: a planted transcript reads one call in each class (SERVED, REFUSED, NO-RESULT), and two real session transcripts from outside the cells read 10 web calls, all SERVED. The launch records explain the zero: all 786 recorded Claude-lane launches pass a `--tools` allowlist without the web tools and strike both again in `--disallowedTools`, and 728 of the 748 transcript directories join to such a launch by cell id (the other 20 are probe and test cells with no launch line; they read 0 too). The client refused the subjects' calls to a tool struck the same way (`SendMessage`, 3 of 3, "No such tool available"), but answered a built-in tool that was neither offered nor struck (`EndConversation`, 2 of 2). So the surface is not exactly the `--tools` list. The client's own offered tool list, read under the cell launch line on both clients the launches used (2.1.259 and 2.1.280), names neither web tool, with the fence's `permissions.deny` alone or the two tool flags together; a control with both lifted names both, so the list can see them. The probe's launch line reconstructs the cells' (the tool flags, the fence, the sandbox and permission flags are theirs; `--name`, `--agents`, the model and the effort are not).

## §AS2 · WHY, AND WHAT IT REPLACES
Paper v5 narrowed its abstract's isolation clause to the Claude lane. The CLI's own web tools run outside the subprocess sandbox; the cell fence denies both, but cells launch with `--dangerously-skip-permissions`, so the outcome was measured rather than assumed. A first run on 2026-11-20 (cited in the v5 read on the bus) took the per-account config dirs only: 560 directories, 2,522 transcripts, 0 calls. It missed 183 directories of the earlier harness config dirs. This addendum's run includes them, and it is the census of record. The 11-20 output is kept beside it.

## §AS3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
What the client would do with a `WebSearch` call that a subject emitted anyway, although it was not offered: none was emitted, and the client's handling of unoffered names is not uniform (`SendMessage` refused, `EndConversation` answered). It also says nothing about network use through the subjects' own shell commands, which is the subprocess sandbox's question. Run-box records only, joined to launches by cell id, not to the cells of record. **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** Nothing here is about the salt method.

Source: `evidence/o3-claude-web-census-2026-11-22/` (README: the census, the launch surface, off-surface calls, the client's offered tool list, the population fix, controls, limits).

---

# ⚖️ ADDENDUM 49 — **O37: BLOCK T IS A RESULT OF RECORD. 24 CONDITIONS MOVE TO DONE (the six block-N problems × statement × {plain, salt-diet} × {Opus, Sonnet}, Claude lane), EACH AT n = 3. THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-11-22, in the same commit as `RESULT-claude-blockTO-2026-11-22.md` and `RESULT-claude-blockTS-2026-11-22.md` (§T9: the census section is re-cut with the result).

## §AT1 · WHAT MOVED
Block T (`AMENDMENT-O37-statement-six-claude-2026-11-11.md`, ADDENDA 1–5) has its 72 cells ended and two result files. All 72 are cells
of record: 66 LANDED, 4 CAP-COST (scored as they stood at the cap), and 2 DIALOG (of record by block SB's `clbbps01` precedent). No
cell is VOID by §T7. One cell (`clbrrp03`) was staged inside the 2026-11-22 sitting; it stays of record by the helm's decision, written
into the Sonnet result as a fact. The line, printed by `evidence/blockT-result-2026-11-22/t_result_gen.py --census`:
```
block T: the six block-N problems x statement, Claude lane: 24 conditions, 24 at n = 3, cells of record 72
block T spend: COST (capped at the cap) $1,120.18 · metered $1,121.72 · Luby $182.71 metered
```
DONE is not a verdict on the arms. Block T's spend sits below the registered price of $1,253.64 and ADDENDUM 5's re-cut of $1,360.98, and
inside the ceiling of $2,679.12.

## §AT2 · THE O37 SECTION, RE-CUT (registration states as of 2026-11-22)
```
  O37's population (ADDENDUM 28 §AG1)                                                                  216
    DONE         blocks N and NA (ADDENDUM 29)                                                    48
                 block WA, Flash: WHT, NTT x {plain, salt-diet} x gemini-3.8-flash-high (ADDENDUM 40)  4
                 block W: WHT, NTT x {plain, salt-diet} x {Opus, Sonnet}, Claude lane (ADDENDUM 43)  8
                 block WA, Pro: WHT, NTT x {plain, salt-diet} x gemini-4-argon-high (ADDENDUM 44)   4
                 block WC: NTT, WHT x spec-change x {plain, salt-diet} x {Opus, Sonnet} (ADDENDUM 45)  8
                 block NC: the six block-N problems x spec-change, Claude lane (ADDENDUM 46)        22
                 block T: the six block-N problems x statement, Claude lane (this)                  24
    DECLARED     LU, 24 conditions (ADDENDUM 39)                                                   24
                 block NC: LinearScan x spec-change x salt-diet x {Opus, Sonnet}, unreached (ADDENDUM 46)  2
    NOT DONE     WHT and NTT, the other 24:
                   x statement, both lanes; x spec-change, agy lane: in no merged block              24
                 the six block-N problems x {statement, spec-change}, agy lane, the other 48:
                   x statement, agy lane: block TA, its result on its registration branch, unmerged  24
                   x spec-change, agy lane: in no merged block                                       24
```
DONE 118 · DECLARED 26 · NOT DONE 72 = 216. Block TA's 24 move when its result reaches `main` with its own addendum, not here.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AT3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
Nothing Opus-versus-Sonnet, nothing about the statement arm versus `extras = none` across blocks (§T8.3), nothing about the salt method.
Every premium in both results is UNRESOLVED-UNDERPOWERED as registered.

Source: `evidence/blockT-result-2026-11-22/` (README: the per-cell table, the categories as read, the derive, the generator, the checks).

# ⚖️ ADDENDUM 50 — **O37: BLOCK TA REACHES `main`. 24 CONDITIONS MOVE TO DONE (the six block-N problems × statement × {plain, salt-diet} × {gemini-3.8-flash-high, gemini-4-argon-high}, agy lane), EACH AT n = 3. THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-11-22, in the commit that lands block TA's registration branch on `main` (ADDENDUM 49 §AT2: "Block TA's 24 move when its result reaches `main` with its own addendum").

## §AU1 · WHAT MOVED
Block TA (`AMENDMENT-O37-statement-six-agy-2026-11-17.md`, ADDENDA 1–8) and its result of record, `RESULT-gemini-blockTA-2026-11-20.md`
(gemini's hand, the lead's read; merged into the registration branch as #455), reach `main` with this addendum. All 72 cells are cells
of record. The lines, printed by `evidence/blockTA-result-2026-11-20/ta_census_line.py` from `cells.tsv` beside it (`--check` on this
file asserts each one):
```
block TA gemini-3.8-flash-high: 12 conditions, 12 at n = 3, cells of record 36 · LANDED 36 · PASS 36 · MODEL-SEAM flagged 4
block TA gemini-4-argon-high: 12 conditions, 12 at n = 3, cells of record 36 · LANDED 36 · PASS 36 · MODEL-SEAM flagged 0
block TA: the six block-N problems x statement, agy lane: 24 conditions, cells of record 72
```
The four MODEL-SEAM cells (Claude workers started through the client's `swarm` tool, RESULT §1.4) are counted as cells of record by
the lead's ruling, and they are out of every Flash comparison. Truncated cells, 5 Flash salt-diet and 1 argon salt-diet, are out of
the comparisons by the RESULT's truncation rule, and they stay cells of record. #457's web census joined all 72 TA cells, and 0 were
served a search (`evidence/o37-agy-web-served-2026-11-20/README.md`, row TA). DONE is not a verdict on the arms. Every condition is at
CEILING in both models (RESULT §2, §3).

## §AU2 · THE O37 SECTION, RE-CUT (registration states as of 2026-11-22)
```
  O37's population (ADDENDUM 28 §AG1)                                                                  216
    DONE         blocks N and NA (ADDENDUM 29)                                                    48
                 block WA, Flash: WHT, NTT x {plain, salt-diet} x gemini-3.8-flash-high (ADDENDUM 40)  4
                 block W: WHT, NTT x {plain, salt-diet} x {Opus, Sonnet}, Claude lane (ADDENDUM 43)  8
                 block WA, Pro: WHT, NTT x {plain, salt-diet} x gemini-4-argon-high (ADDENDUM 44)   4
                 block WC: NTT, WHT x spec-change x {plain, salt-diet} x {Opus, Sonnet} (ADDENDUM 45)  8
                 block NC: the six block-N problems x spec-change, Claude lane (ADDENDUM 46)        22
                 block T: the six block-N problems x statement, Claude lane (ADDENDUM 49)           24
                 block TA: the six block-N problems x statement, agy lane (this)                    24
    DECLARED     LU, 24 conditions (ADDENDUM 39)                                                   24
                 block NC: LinearScan x spec-change x salt-diet x {Opus, Sonnet}, unreached (ADDENDUM 46)  2
    NOT DONE     WHT and NTT, the other 24:
                   x statement, both lanes; x spec-change, agy lane: in no merged block              24
                     (block TW, the Claude lane's 8 x statement, is registered, unmerged: saltbench #462)
                 the six block-N problems x spec-change, agy lane: in no merged block              24
```
DONE 142 · DECLARED 26 · NOT DONE 48 = 216.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AU3 · ALSO REACHING `main` IN THIS LANDING, AND WHAT THIS ADDENDUM DOES NOT ESTABLISH
The registration branch also carries the cut-turns unit correction (bench queue row 11, #456): the "cut turns" figures in both WA
RESULTs were print-timeout LINES, three per event. Its addenda to `RESULT-gemini-blockWA-{flash,pro}-*.md` and its evidence
(`evidence/cut-turns-unit-2026-11-20/`) were merged only into the branch, so `main` carried the uncorrected figures until this landing.
Nothing Flash-versus-argon (§TA6: a result of record per model, never pooled), nothing about the agy lane versus the Claude lane, nothing
about the salt method. At ceiling, no pass count separates the arms.

Source: `evidence/blockTA-result-2026-11-20/` (README: the per-cell table, the collectors, the censuses, the generator).

# ⚖️ ADDENDUM 51 — **O37: BLOCK TW IS A RESULT OF RECORD. 8 CONDITIONS MOVE TO DONE (WHT, NTT × statement × {plain, salt-diet} × {Opus, Sonnet}, Claude lane), EACH AT n = 3. THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-11-24, in the same commit as `RESULT-claude-blockTWO-2026-11-24.md` and `RESULT-claude-blockTWS-2026-11-24.md` (§TW9 = block T §T9: the census section is re-cut with the result). They reach `main` together, with saltbench #468.

## §AV1 · WHAT MOVED
Block TW (`AMENDMENT-O37-statement-wht-ntt-claude-2026-11-22.md`, ADDENDA 1–4) has its 24 cells ended and two result files. All 24 are
cells of record and all 24 LANDED; none was capped, none ended on a dialog, and no cell is VOID by §TW7 (24 of 24 sections as built equal
the export card). The line, printed by `evidence/blockTW-result-2026-11-24/tw_result_gen.py --census`:
```
block TW: WHT and NTT x statement, Claude lane: 8 conditions, 8 at n = 3, cells of record 24
block TW spend: COST (capped at the cap) $312.22 · metered $312.22 · WHT $162.77 metered · NTT $149.45 metered
```
DONE is not a verdict on the arms. Every condition passes its withheld suite 3 of 3 in both models, so the block is at CEILING on
correctness (UNRESOLVED-BY-CEILING). Block TW's spend sits below the registered price of $370.54 and ADDENDUM 4's re-cut of $346.45, and
inside the ceiling of $893.04.

## §AV2 · THE O37 SECTION, RE-CUT (registration states as of 2026-11-24)
```
  O37's population (ADDENDUM 28 §AG1)                                                                  216
    DONE         blocks N and NA (ADDENDUM 29)                                                    48
                 block WA, Flash: WHT, NTT x {plain, salt-diet} x gemini-3.8-flash-high (ADDENDUM 40)  4
                 block W: WHT, NTT x {plain, salt-diet} x {Opus, Sonnet}, Claude lane (ADDENDUM 43)  8
                 block WA, Pro: WHT, NTT x {plain, salt-diet} x gemini-4-argon-high (ADDENDUM 44)   4
                 block WC: NTT, WHT x spec-change x {plain, salt-diet} x {Opus, Sonnet} (ADDENDUM 45)  8
                 block NC: the six block-N problems x spec-change, Claude lane (ADDENDUM 46)        22
                 block T: the six block-N problems x statement, Claude lane (ADDENDUM 49)           24
                 block TA: the six block-N problems x statement, agy lane (ADDENDUM 50)             24
                 block TW: WHT, NTT x statement, Claude lane (this)                                  8
    DECLARED     LU, 24 conditions (ADDENDUM 39)                                                   24
                 block NC: LinearScan x spec-change x salt-diet x {Opus, Sonnet}, unreached (ADDENDUM 46)  2
    NOT DONE     WHT and NTT, the other 16:
                   x statement, agy lane: block TWA, registration draft, unmerged (saltbench #467)    8
                   x spec-change, agy lane: block WCA, registered on main (#470), not released       8
                 the six block-N problems x spec-change, agy lane:
                   block NCA, registered on main (#470), not released                               24
```
DONE 150 · DECLARED 26 · NOT DONE 40 = 216.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AV3 · A HARNESS FINDING CARRIED, AND WHAT THIS ADDENDUM DOES NOT ESTABLISH
ADDENDUM 4's §TW5.2 section finding, extended to NTT by the results' §5: 8 of the 12 salt-diet cells (Opus 3, Sonnet 5; WHT 5, NTT 3)
strengthen the extracted statement's `op_ok` (a result-length conjunct; on NTT also residues) and/or `trace_ok` (R5 determinism), on
out-of-domain traces only. It is a finding about the statement, never an arm effect, and no score moves. Nothing Opus-versus-Sonnet,
nothing about the statement arm versus `extras = none` across blocks (§TW8.3), nothing about the salt method. Every premium in both results
is UNRESOLVED-UNDERPOWERED as registered.

Source: `evidence/blockTW-result-2026-11-24/` (README: the per-cell table, the categories as read, the derive, the generator, the checks).

# ⚖️ ADDENDUM 52 — **O37: TWO agy CELLS OF RECORD RECEIVED ANOTHER RECORD'S CONTENT (`l5fs02`, `l8rfss03`) AND LEAVE EVERY COMPARISON, UNDER ADDENDUM 47's WEB-SERVED RULE. THE OTHER 50 OTHER-RECORD CELLS STAY, LABELLED. NO COUNT MOVES; NOTHING IS VOIDED.**
## bench, 2026-11-25, on the Captain's ruling at the 2026-11-25 sitting (the council minute of that date, item 5, his words *"accept rec"*: arm (b′)). Registered BEFORE any table of record moves. Appended; everything above is unchanged.

## §AU1 · WHAT WAS FOUND
The census of what agy subjects named outside their repo (`evidence/o37-agy-ctl-read-census-2026-11-25/`, 705 cells of record) found **52 cells
whose tool calls NAMED a path under `$HOME` in another record** (another cell or family root, a preserved or evidence tree): MATRIX 50
(salt-diet 42 · plain 8), NA 1, ZF 1 (`census.tsv`, column `other_record` > 0; the same 52 ids as `recut/set-other.txt`). For each such
call the census read what the call RECEIVED (`other_seen.py` → `other_seen.tsv`). **Another record's CONTENT reached the subject in 2
of the 52, both MATRIX salt-diet, gemini-3.8-flash-high:**

- `l5fs02` (FreeList, greenfield): test files of `p2fre02`, a cell under a `PRESERVED-waves-…` tree (3 tool calls whose result carried CONTENT; `other_seen.tsv` `content=` counts CALLS).
- `l8rfss03` (LRU, spec-change): the brain transcript of the plain tripwire cell `l8rfpw01` (5 such calls).

The two cells' CONTENT LINES number 11 together (`#CONTENT-LINES-BY-SOURCE-FORM grep-abs=2 · view_file=9`); the per-cell line split is not derived here.

In 22 of the other 50 the fence refused every outside read, 15 received names only, and 13 received nothing that names an outside path.
CONTENT is 2, the same two cells, under every revision of the instrument and with at least one `view_file` CONTENT line in each
(the census README, "What the OTHER-RECORD calls RECEIVED").

## §AU2 · THE RULE
```
  CONTENT  (another record's file content reached the subject)   2 cells   leave every comparison, as WEB-SERVED cells do (ADDENDUM 47)
  OTHER-RECORD without CONTENT                                   50 cells   STAY in every comparison, LABELLED OTHER-RECORD
  CTL-NAMED                                                     unchanged  stays under AMENDMENT-agy-ctl-fence-2026-10-13.md §5
```
The label is the cell's `census.tsv` row; a result that cites one of the 50 carries it. The set that leaves is `recut/set-content.txt`,
derived from `other_seen.tsv` by `awk -F'\t' '$4=="CONTENT"{print $2}'`. Together with the 10 WEB-SERVED cells, 12 ids leave.

## §AU3 · WHAT IT MOVES, READ BEFORE THE RULE BINDS (`recut/out-content/`, against the RULED state that already excludes the 10 WEB-SERVED)
**One correctness P4 sign leaves salt-diet, on Flash:** Flash × FreeList × greenfield goes from `−` to `—`. The `—` is not a pass: the
condition is scored by condition (P1 salt-diet `0 / 3`), and with `l5fs02` out the instrument's ADDENDUM 3d guard prints it `unmeasured`
(printed n 3 against 2 cells of record). Flash bare P4 counts `+ = − ? —` go from `0 2 1 1 1` to `0 2 0 1 2`.
**One P3 pass leaves salt-diet:** Flash × LRU × spec-change, salt-diet phase 2, goes from `3 / 3` to `2 / 2` (`l8rfss03` was a PASS).
**Descriptive T4:** every k-of-m sign holds; two Flash medians move (bare 3.72 → 3.03, spec-change 2.88 → 3.06). **Cost v3:** every $4
and W4 k-of-m sign holds; Flash medians move (`$4` bare 2.96 → 2.61, spec-change 2.26 → 2.33; `W4` bare 2.50 → 2.19, spec-change 2.47 → 2.42). Those are the sign-count tables; inside the two affected conditions the per-condition
cells move too (T1/T3 median tokens, the output-token medians, $1/$3, W1/W3, the T4/$4/W4 ratio cells, and the per-cell rows), each listed
in the diff files below.
Sources: `out-content/correctness-v3-moved-vs-ruled.txt`, `descriptive-v2-moved-vs-ruled.txt`, `cost-v3-moved-vs-ruled.txt`,
`headline-signs.md` beside `out-ruled/headline-signs.md`.
⚠️ **The removal is one-armed:** both cells are salt-diet. It takes away a salt-diet `−` (P4) and a salt-diet PASS (P3), so it moves
salt-diet's record in both directions at once, and neither move is a measured pass or a measured failure of the arm.

## §AU4 · WHAT THIS ADDENDUM DOES NOT DO
**No count in this census moves:** both cells stay cells of record IN THIS CENSUS (the guard's "2 cells of record" in §AU3 counts the
cells left IN THE COMPARISON), their conditions stay DONE at the n their records state, and
nothing is voided (A5.2 voids only FENCE-TAMPER). The re-cut of the tables of record is a separate change that cites this addendum. The 50
that stay are not shown uncontaminated: NONE-NAMED and NAMES-ONLY are lower bounds on contact (the census README, limit 1), and a program
a call ran that read further is not seen. **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.**
Nothing here is about the salt method.

Source: `evidence/o37-agy-ctl-read-census-2026-11-25/` (README: the census, the OTHER-RECORD content read, controls, limits;
`recut/README.md`: the three arms and what each moves).

# ⚖️ ADDENDUM 53 — **O37: BLOCKS NCA AND WCA ARE RESULTS OF RECORD. 32 CONDITIONS MOVE TO DONE (the six block-N problems, and WHT and NTT, × spec-change × {plain, salt-diet} × {gemini-3.8-flash-high, gemini-4-argon-high}, agy lane), EACH AT THE n ITS RECORD STATES. THE PILOT'S 200 DO NOT MOVE.**
## bench, 2026-11-28, in the same pull request as the four result files `RESULT-gemini-blockNCA-flash-2026-11-28.md`, `RESULT-gemini-blockNCA-argon-2026-11-28.md`, `RESULT-gemini-blockWCA-flash-2026-11-28.md` and `RESULT-gemini-blockWCA-argon-2026-11-28.md` (§NCA8 and §WCA8: the census section is re-cut with the results). They reach `main` together, with saltbench #479.

## §AW1 · WHAT MOVED
Blocks NCA (`AMENDMENT-O37-blockNCA-specchange-agy-2026-11-23.md`, ADDENDA 1–6) and WCA (`AMENDMENT-O37-blockWCA-wht-ntt-specchange-agy-2026-11-23.md`,
ADDENDA 1–3) have every registered cell ended and a result file per block and model. A condition's n is its COUNTED cells: a phase 2 that
is a REACH LOSS under NC rule 4, that the §A9.2 gate refused, or that the harness did not score is listed in its result and never counted.
The lines, printed by `evidence/blockNCA-WCA-result-2026-11-24/nca_result_gen.py --write` (its `--check` asserts each one here):
```
block NCA, gemini-3.8-flash-high: 12 conditions · n=3 10 · n=2 2 [BinomialHeap salt-diet, LinearScan salt-diet] · cells counted 34 of 36
block NCA, gemini-4-argon-high: 12 conditions · n=3 10 · n=2 2 [Liveness salt-diet, MaxFlow plain] · cells counted 34 of 36
block WCA, gemini-3.8-flash-high: 4 conditions · n=3 4 · cells counted 12 of 12
block WCA, gemini-4-argon-high: 4 conditions · n=3 4 · cells counted 12 of 12
```
Every condition stands at n = 3 except the four the lines name at n = 2, each for a reason its result file states. NCA Flash BinomialHeap ·
salt-diet and LinearScan · salt-diet each hold one FRESH cell (NA had no eligible source, §NCA2) whose G baseline on landed-1 read short of
a full pass, a REACH LOSS under NC rule 4 (`cells-nca-binomialheap-flash-salt-r3`, `cells-nca-linearscan-flash-salt-r2`). NCA argon Liveness
· salt-diet: the §A9.2 gate refused phase 2 of `cells-nca-liveness-argon-salt-r1`, whose subject had deleted its own `landed-1` tag (the
lead's ruling (a), bus offset 111,293,855: a REACH LOSS). NCA argon MaxFlow · plain: phase 2 of `cells-nca-maxflow-argon-plain-r1` is
NOT-SCORED (harness), NCA ADDENDUM 6. Block WCA has every condition at n = 3, both models. DONE is not a verdict on the arms, and no result
here compares arms, models or blocks.

## §AW2 · THE O37 SECTION, RE-CUT (registration states as of 2026-11-28)
```
  O37's population (ADDENDUM 28 §AG1)                                                                  216
    DONE         blocks N and NA (ADDENDUM 29)                                                    48
                 block WA, Flash: WHT, NTT x {plain, salt-diet} x gemini-3.8-flash-high (ADDENDUM 40)  4
                 block W: WHT, NTT x {plain, salt-diet} x {Opus, Sonnet}, Claude lane (ADDENDUM 43)  8
                 block WA, Pro: WHT, NTT x {plain, salt-diet} x gemini-4-argon-high (ADDENDUM 44)   4
                 block WC: NTT, WHT x spec-change x {plain, salt-diet} x {Opus, Sonnet} (ADDENDUM 45)  8
                 block NC: the six block-N problems x spec-change, Claude lane (ADDENDUM 46)        22
                 block T: the six block-N problems x statement, Claude lane (ADDENDUM 49)           24
                 block TA: the six block-N problems x statement, agy lane (ADDENDUM 50)             24
                 block TW: WHT, NTT x statement, Claude lane (ADDENDUM 51)                           8
                 block NCA: the six block-N problems x spec-change, agy lane (this)                 24
                 block WCA: WHT, NTT x spec-change, agy lane (this)                                  8
    DECLARED     LU, 24 conditions (ADDENDUM 39)                                                   24
                 block NC: LinearScan x spec-change x salt-diet x {Opus, Sonnet}, unreached (ADDENDUM 46)  2
    NOT DONE     WHT and NTT x statement, agy lane: block TWA, registration draft, unmerged (saltbench #467)  8
```
DONE 182 · DECLARED 26 · NOT DONE 8 = 216.
⚠️ **The pilot's line is unchanged: DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 · DECLARED 3 = 200.** The two populations are never summed.

## §AW3 · WHAT THIS ADDENDUM DOES NOT ESTABLISH
§NCA8 and §WCA8, carried: no magnitude; nothing Flash-versus-argon, Claude-versus-agy or about gemini-3.1-pro-high; every premium is
UNRESOLVED-UNDERPOWERED. Cells that continue a WEB-SERVED source (four NCA Flash LinearScan copies, census ADDENDUM 47) and the one CTL-READ
cell (`naaefs01`) are DONE cells of record that leave every comparison, as their results say. Nothing here says whether the salt method
helps or hurts. Any public sentence is the Captain's.
