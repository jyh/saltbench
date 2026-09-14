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
       (FreeList·LRU·LZW·Paxos. Crc32 EXCLUDED as a declared NEGATIVE CONTROL, freeze §G4)  Crc32 OWED 2
  brownfield × {plain,salt-diet} × statement   × 5 problems   OWED (Paxos 2 INEXPRESSIBLE)           10
  brownfield × {plain,salt-diet} × spec-change × 5 problems   class (b)                              10
  ─────────────────────────────────────────────────────────────────────────────────────────────────
  DONE 22 · OWED 28 · INEXPRESSIBLE 4 (+10 class (b))
```

### `gemini-3.8-flash-high`
```
  ALL 60   BLOCKED — not owed. Level 5 HALTED at ONE cell; 0 scored.
  AMENDMENT-gemini-flash-level5 ADDENDUM 1, merged 6d8dd527: the model runs an episode as ONE TURN and
  meets a per-turn deadline calibrated on Pro's granularity. ⛔ n = 1 on the Flash side.
  ⇒ RELEASE: a design decision about per-turn capping for a model that does not segment. NOT a re-fire.
```

### the FOURTH MODEL — UNNAMED
```
  ALL 60   BLOCKED ON THE CAPTAIN — the model is not named and cannot be inferred (§C1).
```

## §C5 · THE TOTAL, AND IT IS THE HEADLINE
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

  claude-opus-5          DONE 28 · OWED  0 · BLOCKED 18 · INEXPR 4
  claude-sonnet-5        DONE  0 · OWED 28 · BLOCKED 18 · INEXPR 4    <- never run as a SUBJECT: 0 of 307 cells
  gemini-3.1-pro-high    DONE 22 · OWED 24 · BLOCKED  0 · INEXPR 4
  gemini-3.8-flash-high  DONE  0 · OWED 46 · BLOCKED  0 · INEXPR 4    <- see ADDENDUM 2 below
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
