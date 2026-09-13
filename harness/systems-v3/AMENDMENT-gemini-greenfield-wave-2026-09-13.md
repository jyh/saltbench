# AMENDMENT — THE GEMINI PRO 3.1 GREENFIELD WAVE, FROZEN BEFORE ITS FIRST CALL
## bench (SaltBench lead), 2026-09-13. **Ordered by the Captain, council relay 1/2 item (2):**
## *"Gemini Pro 3.1 × greenfield × 5 pilot problems × 4 arms asap"* = the 42 remaining cells,
## *"FREEZE the wave design now: arms, caps registered before the first call, n=3, per-problem briefings."*
## A runner seat `gemini` is the HAND; **bench stays lead — design, caps, scoring rules, amendments.**
## ⛔ NOTHING IN THIS FILE AUTHORISES A CALL UNTIL §G6's OPEN NUMBER IS READ AND REGISTERED.

---

## §G1 · THE POPULATION — 42 CELLS, NAMED, SO AN ERROR IS CHEAP NOW AND NOT AFTER
Model **`gemini-3.1-pro-high`** (measured live at `agy models`; ⛔ **there is no Flash at generation 3.1** —
that confound is A5.7's and does not arise here, where every cell is Pro). **n = 3.**
```
  BARE PAIR       plain-bare · salt-bare        × 4 problems × n3 = 24
  STATEMENT PAIR  plain-stmt · salt-stmt        × Crc32 · FreeList · LRU × n3 = 18
                                                                      TOTAL = 42   ✓ reconciles
```
⚠️ **THE FOUR BARE PROBLEMS ARE NOT NAMED IN THE ORDER AND I AM NOT GUESSING SILENTLY.** The five pilot
problems are **LZW · LRU · Paxos · FreeList · Crc32** and LZW already carries n=1 on all four arms (desk HC:
plain-bare $9.83 · salt-bare $19.83 · plain-stmt $11.19 · salt-stmt $16.42). **My reading: the bare pair
covers the four problems OTHER than LZW** (LRU · Paxos · FreeList · Crc32), and the statement pair the three
named. **If the intended four differ, this line is the cheapest place in the campaign to correct it.**

**ARM → FLAGS, so the hand types no interpretation:**
```
  plain-bare   cell_build.py --arm plain --field greenfield            (no --statement)
  salt-bare    cell_build.py --arm salt  --field greenfield            (no --statement)
  plain-stmt   cell_build.py --arm plain --field greenfield --statement
  salt-stmt    cell_build.py --arm salt  --field greenfield --statement
```
⛔ **`--hint` IS NOT USED IN THIS WAVE.** It is the pricing branch's, it is problem-specific, and desk HC
already dropped the hint arms as a confound in the arm being generalised.

---

## §G2 · ⛔⛔ THE CAP CANNOT BE USD ON THIS LANE, AND ON THE PRICING PROFILE THE WAVE WOULD VOID ALL 42 CELLS
**Measured at the object before writing this section:**
```
  rates.tsv          ZERO gemini rows — every row is claude-*          cell_meter.py   ZERO gemini mentions
  cell-watch.sh:607  a served model with no rates.tsv row prices as VOID(UNPRICED)
  cell-watch.sh:608  two consecutive unpriced reads -> end_session COST-BLIND, class HARNESS
  cell_build.py      --budgets pricing REFUSES without a C<phase>_USD row, and writes the registered
                     USD caps (C1 37.21 / C2 18.60) — both DERIVED FROM A CLAUDE ARM'S MEASURED COST
```
⇒ 🔑 ***A GEMINI CELL BUILT ON THE PRICING PROFILE ARMS A COST CAP THE METER CANNOT PRICE, AND ENDS
`COST-BLIND` AFTER TWO READS. THE WAVE WOULD PRODUCE 42 VOID CELLS AND A CLEAN-LOOKING LOG.***
✅ **The harness is RIGHT here and this is not a harness defect:** it refuses to invent a price. The defect
would have been mine, for carrying a Claude-derived USD cap onto a subscription lane.

### THE THREE UNITS, AND WHY NONE IS FREE
```
  USD     IMPOSSIBLE TODAY. No rate row, and the lane is a SUBSCRIPTION — there is no per-token bill to
          quote. A notional USD would be a FABRICATED NUMBER in a cost table. (Card: a quota figure is a
          BILL, not a budget, and the two conventions are exactly backwards from each other.)
  TOKENS  POSSIBLE AND ARM-BIASED BY CONSTRUCTION. This campaign's own finding: T is ~98% cache_read and
          QUADRATIC in the work, so a T cap SUBSIDISES THE ARM THAT RUNS LONGER — which is the very thing
          the experiment measures. A T cap is a TREATMENT unless it rarely binds.
  POOL %  THE LANE'S REAL SCARCE UNIT, and already enforced — agy_battery_cell.sh REFUSES below a 20%
          weekly floor. But it is a WAVE-level guard, not a per-cell cap, and it reports REMAINING while
          the Claude log reports USED.
```
### ⚖️ REGISTERED: **THE GEMINI LANE CAPS IN TOKENS, AND THE CAP IS A SAFETY STOP, NOT A BUDGET**
- **Profile: a TOKEN profile, and NO `--cost-cap`** — so `cell-watch` arms `CAP_UNIT=TOKENS` and no
  `C<phase>_USD` row exists to arm a cost it cannot price.
- ⛔ **THE T VALUE IS SET HIGH ENOUGH TO BIND RARELY, ON PURPOSE.** A cap that binds often is a treatment;
  a cap that binds rarely is a stop. **Any cell that ends `CAP-TOKENS` is reported as CUT, never as a
  result**, and its arm is named beside it — an arm-correlated cut is a finding about the cap, not the arm.
- ⛔ **NO USD FIGURE IS QUOTED FOR ANY CELL IN THIS WAVE.** Not in a result file, not in a table, not in
  prose. ⇒ **The Gemini lane and the Opus lane are NOT COMPARABLE IN DOLLARS**, and any cross-lane cost
  sentence must either use a shared unit or declare the incommensurability. Saying "$" of a subscription
  cell is inventing a bill nobody was sent.

---

## §G3 · PER-PROBLEM BRIEFINGS, AND THE ONE PROPERTY THAT MUST HOLD ACROSS THEM
The Captain's order says per-problem briefings. **The briefing is rendered from each problem's own
`card.md`; the ARM's method file is NOT per-problem and must not become so.**
⇒ **REGISTERED CHECK, the same shape §B2's N3 uses for brownfield:** for every problem, the two arms'
cells must differ **exactly by METHOD_FILES**, and each arm's `CLAUDE.md` must be **byte-identical across
problems.** `cell_manifest.py --pair` already refuses a diff outside METHOD_FILES; a per-problem method
file would surface there. **A briefing that varies by problem is a treatment that varies by problem.**

---

## §G4 · Crc32 — RUN IT AND REPORT THE CEILING (the Captain, relay 2/2 item 5, taking bench's rec)
Crc32's five withheld mutants **all fail 5 of 6 tests**, so it has no discriminating seed for BROWNFIELD.
⚠️ **That finding is about the BROWNFIELD field and does NOT transfer to greenfield**, where the subject
writes the component from the card and the mutants are not used at all. **Crc32 runs in this wave on the
same footing as the other four.** The ceiling to report is the brownfield one, when that field runs.

---

## §G5 · WHAT VOIDS A CELL (faults only — no prediction appears in this list)
```
  1  the served model differs from gemini-3.1-pro-high        VOID  (the client logs both the requested id
     and the resolved LABEL; agy REFUSES an unrecognised id, driven, so substitution is not the risk here)
  2  the cell ends COST-BLIND or METER-BLIND                  VOID(UNPRICED) — and see §G2: on this lane
                                                              that means the profile was wrong, not the cell
  3  a cancelled-build wedge                                  WALL TIME INADMISSIBLE as cost (row LK(c2));
                                                              tokens remain admissible
  4  the fence battery does not pass for the cell's PATH       DO NOT FIRE — a cell without its own fence
                                                              receipt is not evidence
  5  CAP-TOKENS                                               NOT void: reported as CUT, with the arm named
```
⛔ **My expectations about which arm costs more are NOT in this list.** A failed prediction is the
experiment working; a stop list that mixes faults with predictions is the defect the helm removed its own
trigger for.

---

## §G6 · ⛔ THE ONE OPEN NUMBER, AND IT IS A PRECONDITION OF THE FIRST CALL
**The T value, and the parallel LANE WIDTH.** The Captain (relay 2/2 item 6): *"Gemini + Opus waves run IN
PARALLEL on the run box; set each lane's width from a MEMORY reading on the first parallel wave and register
the number."*
```
  WHAT IS MISSING   a token figure for a Gemini greenfield cell on this harness. The class-C agy cells
                    carry no readable totalTokenCount, and rates/meter have no gemini support, so it
                    CANNOT be taken from a document — it must be READ.
  HOW IT IS GOT     fire ONE cell (plain-bare, one problem) as the wave's first, read its T from the
                    turnloop record, and set the cap from it. THE FIRST CELL IS ITS OWN CALIBRATION.
  LANE WIDTH        a MEMORY reading on the run box while BOTH lanes run, per the Captain. Registered as a
                    number here before the wave widens past 1 + 1.
```
⇒ **The wave may start at width 1 per lane. It may not widen, and the T cap may not be declared, until both
numbers are read and written into this file.** A width chosen from a guess is a box crash with 42 cells in it.

---

## §G7 · THE CALIBRATION CELL — WHAT THE HAND FIRES FIRST, AND UNDER WHAT CAP
⛔ **"The first cell is its own calibration" DOES NOT MEAN "fire it uncapped."** A token profile still arms
`CAP-TOKENS` from its own `T1_TOK`, so the calibration cell is capped by an **EXISTING REGISTERED PROFILE**
and not by a number invented for the occasion.
```
  CALIBRATION CELL   --arm plain --field greenfield --budgets smoke40   (T1_TOK = 40,000,000)  NO --cost-cap
  WHY smoke40        it is an ALREADY-REGISTERED profile, and it is generous: the v3 smoke's CLAUDE salt
                     arm hit CAP-TOKENS at 25.5 M against a 20 M cap, so 20 M is known to bind and 40 M
                     leaves headroom. ⛔ That is a CLAUDE datum being used to size a GEMINI cap — which is
                     exactly the cross-lane carry this amendment refuses for USD. It is admissible HERE
                     and nowhere else, because T is a COUNT the two lanes share, while USD is a BILL only
                     one of them is sent. THE CALIBRATION CELL EXISTS TO REPLACE THIS ESTIMATE.
  THEN               read its T from the turnloop record, write the wave's T cap into §G6 of this file,
                     and only then fire the remaining 41.
```
⚠️ **If the calibration cell itself ends `CAP-TOKENS` at 40 M, that is a RESULT, not a failure** — it says
a Gemini greenfield cell does not fit in 40 M, and the wave's cap must be set above it with the reason
recorded. **Do not silently raise the cap and re-fire; register the reading first.**

---
## §G8 · ⛔ A NOTE ON NAMING, ADDED BY A CI RED ON THIS FILE'S OWN FIRST PUSH
The two sentences above originally carried **the run box's NAME**, quoted verbatim from the Captain's
relay. `check_infra_names.py` refused the push: this repo is PUBLIC and a box name is infrastructure.
**The box is named in the fleet roster, which lives outside this repo, and nowhere in this tree** — say "the run box".
⇒ ⚠️ **MY LOCAL GATE RUN WAS GREEN AND IT WAS FALSE.** I ran `check_infra_names.py` while this file was
still **UNTRACKED**, and that gate scans **TRACKED** text files. **The instrument was fine; the population
I pointed it at excluded the only file I was checking.** ⇒ 🔑 ***RUN A TREE GATE AFTER `git add`, NEVER
BEFORE — an untracked file is invisible to it, and the green it returns is about everything else.***
📌 **AND THIS NOTE ITSELF WENT RED ON THE SECOND GATE, ON ITS FIRST DRAFT.** It cited the roster BY PATH,
which is a private-record shape, so the paragraph explaining the infra-name defect carried a path defect.
⇒ **A prohibition stated in prose is a counterexample to itself unless the prose is written to the rule
it is stating.** Both gates now pass with the file TRACKED.

---

# §G9 · ⚖️ THE LEAD'S RULINGS ON THE HAND'S CENSUS — 2026-09-13, bench
*`gemini` measured the lane before firing and returned three questions and one refutation. All four are
answered here. I re-drove the refutation at the object before accepting it.*

## R1 · ⛔ **§G2's CONCLUSION IS WITHDRAWN. `--budgets pricing` DOES NOT VOID A GEMINI CELL.**
My three measurements were each TRUE and I re-drove them; **the INFERENCE crossed lanes.** Re-measured:
```
  fire_agy_v3.sh   grep budgets|COST|USD|CAP_UNIT|rates   ->  0 hits. The agy fire path arms NO cost cap.
  agy_meter_v3.py  its own words: "this meter does NOT price. On a subscription ..."
                   VOID kinds present: VOID(NO-MODEL) · VOID(NON-GEMINI).   UNPRICED: 0 occurrences.
  cell-watch.sh    the CLAUDE fire path. fire_agy_v3.sh names it in HEADER COMMENTS ONLY (lines 9, 26).
  the object       41 metered cells on disk were built on `pricing`; none is COST-BLIND.
```
⇒ 🔑 ***I MEASURED `cell-watch.sh`, WHICH THIS LANE NEVER CALLS. RIGHT INSTRUMENT, WRONG POPULATION —
THE FIFTH TIME IN ONE DAY I HAVE READ A TRUE NUMBER OFF AN OBJECT THE CLAIM WAS NOT ABOUT.***
⚠️ **AND IT WAS OPERATIONALLY BLOCKING, NOT MERELY WRONG:** `agy_wave_v3.sh` HARDCODES `--budgets pricing`,
so as frozen §G2 forbade the only profile the wave driver can emit. **A hand obeying the freeze literally
would have had to edit its lead's tool.** A freeze that cannot be obeyed without editing the toolchain is
a defect in the freeze.

✅ **WHAT SURVIVES UNTOUCHED, AND IT IS THE PART THAT MATTERED:** **no USD figure is quoted for any cell of
this wave, and the Gemini and Opus lanes are NOT comparable in dollars.** That is a **REPORTING** rule and
it stands whatever the profile does. ⭐ **It is now better motivated than when I wrote it:** an agy cell's
`ctl/budgets.env` carries `C1_USD=37.21` **written and inert**, so a later reader finds a Claude-derived
number that never applied to that cell. ⇒ **REGISTERED: the USD rows on an agy cell are INERT-ON-THIS-LANE
and must never be read, quoted, or summed.**

## R2 · ✅ THE T CAP IS `pricing`'s **250,000,000**, NOT a new profile — and the reason is arm-correlation
Read from the cells on disk: `plain` max T **2,475,940** (n=18) · `salt-diet` max T **25,100,454** (n=20).
```
  smoke40  40 M   = 1.6x the largest salt-diet cell and 16x the largest plain cell
                   -> it would bind THE TREATMENT ARM FIRST, and A CAP THAT BINDS ONE ARM IS A TREATMENT
  pricing 250 M   ~ 10x the largest cell this campaign has produced -> binds NEITHER arm
```
⇒ **§G7's calibration cell is SUPERSEDED: the number it existed to obtain is already readable**, and
`smoke40` — which I chose — was the arm-biased option. **The hand's recommendation is adopted in full.**

## R3 · ⛔⛔ THE ARM IS **`salt-diet`**. §G1's `--arm salt` WAS MY TRANSCRIPTION ERROR.
`cell_build.py --arm` takes `plain | salt | salt-diet | placebo`, and **`salt` and `salt-diet` are DIFFERENT
ARMS.** Every treatment cell this campaign has run — the 20 metered on disk, the 19-row spec-change result,
stage 1 — is **`salt-diet`**. ⇒ **Typed literally, §G1 would have built an arm the campaign has never run,
against comparators that do not exist.** The flag table is corrected: `salt-bare` = `--arm salt-diet`,
`salt-stmt` = `--arm salt-diet --statement`.
📌 **The hand caught this and was right to refuse to resolve it alone** — `agy_wave_v3.sh`'s own header
carries the same warning: *a script written for one arm and reused for another will run the arm it was
written for, and the cell id will say otherwise.*

## R4 · ⚖️ THE 42 ARE ADMISSIBLE **IN PRINCIPLE**, AND THE RECEIPT GATE DECIDES EACH ONE
Same 14 conditions, same model (41 × `gemini-3.1-pro-high`, **zero substitution**), n=3, metered.
**They satisfy §G1's population exactly.** ⇒ **DO NOT RE-FIRE THE 38.** Re-running cells that already exist
spends the pool to reproduce what is on disk, and the Captain's *"asap"* is served by scoring, not by firing.
```
  ADMIT          subject to briefing_verdict_v3.py passing PER CELL — the receipt gate rules, not I
  THE REMAINDER  the 4 that never fired: crc32-saltdiet-stmt/s3ct03 · freelist-plain/s3fp02 · s3fp03
                 · freelist-plain-stmt/s3fq03   <- these are the wave's real fire list
  THE 5 metered-not-landed  REPORTED, NEVER SILENTLY DROPPED. A PERSIST-INDETERMINATE cell is UNMEASURED
                 for landing; its TOKENS remain admissible. ⚠️ The 5/5 arm-correlation is ITSELF A FINDING
                 and is reported as one — an arm-correlated exclusion is decided by its SIGN, and dropping
                 five treatment cells quietly would flatter the control.
  ⛔ THE EXPORT   they were built from export s2g `156fcb93`, NOT today's harness. That does not make them
                 inadmissible — comparability names a REFERENCE, not a date — but the export sha is
                 RECORDED with the result, and any cell fired now is fired from a NAMED export, not "latest".
  ⛔ THE FIELD    `ctl/field` is EMPTY on all 42 (they predate `--field`). Greenfield is established
                 STRUCTURALLY, which the hand correctly flagged as the weakest link in its post.
                 ⇒ ACCEPTED AS GREENFIELD, and the warrant is recorded as INFERRED, never as read —
                 the same distinction `cell_copy_v3.py` now makes for a parent's field.
```
