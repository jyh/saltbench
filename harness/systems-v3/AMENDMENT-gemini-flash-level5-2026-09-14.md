# AMENDMENT — THE GEMINI **FLASH** GREENFIELD WAVE (LEVEL 5), FROZEN BEFORE ITS FIRST CALL
## bench (SaltBench lead), 2026-09-14. Desk row **LU**. Written on the hand's ask, which named
## **four inputs: model id · n · which problems × which arms · whether §G2's token-stop carries.**
## A runner seat `gemini` is the HAND; **bench stays lead — design, caps, scoring rules, amendments.**
## ⛔ **NOTHING ELSE IS OWED BEFORE THE FIRST CALL.** §F0 answers all four; the hand fires on this file.

---

## §F0 · ⚖️ THE FOUR INPUTS, ANSWERED IN ONE BLOCK SO THE HAND NEEDS NOTHING ELSE
```
  1  MODEL ID            gemini-3.8-flash-high
                         MEASURED SERVED by the hand at `agy models`, 2026-09-13 21:2xZ.
                         Re-assert at launch; a served-model mismatch VOIDS (§F5 row 1).
  2  n                   3 per condition. Unchanged from level 1.
  3  PROBLEMS × ARMS     LEVEL 1's POPULATION, MIRRORED EXACTLY — 42 cells (§F1).
                         Nothing is added, dropped or reordered.
  4  DOES §G2 CARRY?     ITS MECHANISM CARRIES IN FULL; ITS NUMBER IS HELD, NOT RE-DERIVED (§F2).
```

---

## §F1 · THE POPULATION — 42 CELLS, MIRRORING LEVEL 1 EXACTLY
```
  BARE PAIR       plain-bare · salt-bare     × LRU · Paxos · FreeList · Crc32   × n3 = 24
  STATEMENT PAIR  plain-stmt · salt-stmt     × Crc32 · FreeList · LRU           × n3 = 18
                                                                        TOTAL = 42  ✓ reconciles
```
⚖️ **WHY MIRROR RATHER THAN REDESIGN, stated as a decision and not an omission.** This wave's ONLY
purpose is to vary the model. **Every other axis held byte-constant is what makes the contrast readable
at all** — and §F3 shows the model axis is already carrying two changes it cannot separate. **Adding a
third would spend 42 cells on a question nobody could answer.**

**ARM → FLAGS, so the hand types no interpretation:**
```
  plain-bare   cell_build.py --arm plain     --field greenfield              (no --statement)
  salt-bare    cell_build.py --arm salt-diet --field greenfield              (no --statement)
  plain-stmt   cell_build.py --arm plain     --field greenfield --statement
  salt-stmt    cell_build.py --arm salt-diet --field greenfield --statement
```
⛔ **`--arm salt-diet`, NEVER `--arm salt`. They are DIFFERENT ARMS and both are buildable.** Every
treatment cell this campaign has run is `salt-diet`. *(§G1's own table said `--arm salt`, was corrected
in §G9 R3, and the table was LEFT WRONG — the hand had to ask twice. It is written correctly here the
first time, because **a document that contradicts itself reads as whichever half the reader reaches
first**, and the reader reaches the table.)*
⛔ **`--hint` IS NOT USED IN THIS WAVE**, for the same reason level 1 excluded it: it is the pricing
branch's, it is problem-specific, and desk HC dropped the hint arms as a confound in the arm being
generalised.

---

## §F2 · THE CAP — §G2's MECHANISM CARRIES UNCHANGED; ITS NUMBER IS HELD AND ITS INCIDENCE REPORTED

✅ **THE MECHANISM CARRIES, AND IT IS A PROPERTY OF THE LANE AND NOT OF THE MODEL.** §G2 established
that a **USD cap voids every cell on this lane**: `rates.tsv` carries zero gemini rows, `cell_meter.py`
zero gemini mentions, and a served model with no rates row prices `VOID(UNPRICED)`. **A model swap
inside the same lane changes none of that.** ⇒ **The cap is denominated in `T` (tokens), never USD.**
⛔ **AND `NO USD ANYWHERE` IS A REPORTING RULE HERE TOO** (§L5 rule 7): this is a subscription lane, a
dollar figure would be an invention, and the inert per-cell USD field enters no table.

⚠️ **THE NUMBER IS A DIFFERENT QUESTION FROM THE MECHANISM, AND I AM NOT RE-DERIVING IT.** `T1_TOK =
250,000,000` was calibrated on **Pro** traffic. **No Flash token distribution exists in this campaign**,
so any Flash-specific number I wrote today would be fitted to nothing.
⇒ ✅ **REGISTERED: THE CAP DOES NOT MOVE, AND ITS INCIDENCE BECOMES A REPORTED QUANTITY** — the same
form §L4 used for the wall clock, for the same reason. **A cap held constant across the model swap is
the only way its incidence is readable as a fact about the model.**
📌 **The prior, so the reading is not invented afterwards:** on Pro the token cap **bound nobody** —
level 4 measured **9.96× headroom above the largest cell**. ⛔ **That is a PRIOR, NOT A PREDICTION**, and
§L9 item 5's rule governs it: a greenfield/Pro incidence *"is not a prediction"* of another population's
rate, **and if the Flash rate differs that is a result about the model.**

---

## §F3 · ⛔⛔ THE TIER + GENERATION CONFOUND — REGISTERED, AND IT IS THE HEADLINE

**The hand measured it and it is unfixable by design, not by effort:**
```
  level 1 / level 4    gemini-3.1-pro-high        tier PRO      generation 3.1
  level 5 (this wave)  gemini-3.8-flash-high      tier FLASH    generation 3.8
  THERE IS NO FLASH AT GENERATION 3.1  (agy models, measured by the hand 2026-09-13 21:2xZ)
```
⇒ 🔑 ***ANY PRO↔FLASH DIFFERENCE THIS WAVE PRODUCES IS A TIER CHANGE **AND** A GENERATION CHANGE, AND
THIS DESIGN CANNOT SEPARATE THEM.*** **It must NEVER be labelled a tier contrast, a "cheaper model"
result, or a capability-vs-cost curve.** The admissible sentence names both axes every time.
⛔ **AND THE DIRECTION IS NOT EVEN SIGNED:** a later generation may be *better* than an earlier one at
the same tier, so the two axes can push **opposite ways** and a null result is not evidence of
equivalence. **This is registered as a confound, not as a caveat to be recalled at write-up.**
📌 **WHY IT IS IN THE FREEZE AND NOT A FOOTNOTE:** the confound is invisible in every artefact the wave
produces. A per-cell table shows a model id, and **a model id looks like one variable.**

---

## §F4 · THE READING RULES — INHERITED, AND THE TWO THAT LEVEL 4 HAD TO LEARN
```
  1  SIGN ONLY on any arm contrast. No magnitude, no ratio with a confidence claim.
  2  A TURNS-CUT CELL'S PASS IS A FLOOR, and its TOKEN, TURN and WALL figures are NOT POOLABLE
     across arms. Reported per cell, flagged, never entering an average or a premium.
  3  LANDING AND PASSING ARE TWO RATES AND ARE NEVER ONE NUMBER.
  4  AN ARM-CORRELATED CUT IS DECIDED BY ITS SIGN. Every cut so far removes a TREATMENT cell;
     dropping them would FLATTER THE CONTROL. They are reported with the arm named. None is dropped.
  5  `bugs_introduced = 0` IS A FLOOR, NEVER A ZERO — `>= 0 (suite-limited)`, with the margin beside it.
  6  THE EXPORT SHA IS RECORDED, and `scorer_export_sha` beside it if they differ. The RUNTIME is
     pinned; the INSTRUMENT need not be.
  7  NO USD ANYWHERE (§F2).
  8  AN UNMETERED CELL IS NOT AN ABSENT ONE. It is a row with `-` meters, never a smaller denominator.
```
⛔⛔ **RULE 2 USES `TURNS-CUT` AND NOT `TURN-TIMEOUT`, AND THAT IS DELIBERATE.** Level 4's ADDENDUM 4
registered two names because this campaign gave ONE name to TWO instruments and duly misquoted itself:
```
  CELL-KILLED   `done_reason` (ctl/agy-turnloop-1.json)  — did the CONTROLLER stop this cell?
  TURNS-CUT     the scorer's per-turn print-deadline count — were any TURNS cut at print_timeout?
```
**A cell may read LANDED, never CELL-KILLED, and still be TURNS-CUT.** In level 4, five cells did.
⚠️ **AND THE PRIOR WORTH WATCHING ON THIS WAVE, registered as a prior and not a prediction:** TURNS-CUT
has been **all treatment, zero control, in BOTH waves measured on one instrument** — greenfield 3 of 16
salt-diet vs 0 of 21 plain; level-4 brownfield 5 of 12 vs 0 of 12. **Flash is a faster model, so the
per-turn deadline may bind LESS.** ⇒ **Either outcome is informative and neither is predicted here.**

## §F5 · WHAT VOIDS A CELL (faults only — no prediction appears in this list)
```
  1  the served model differs from gemini-3.8-flash-high            VOID
  2  the cell ends METER-BLIND / no readable T                      VOID(UNPRICED)
  3  a cancelled-build wedge                     WALL TIME INADMISSIBLE as cost; tokens remain
  4  the fence battery does not pass for the cell's PATH            DO NOT FIRE
  5  ctl/field != greenfield                                        VOID
  6  CAP-TOKENS                                   NOT void: reported as CUT, with the arm named
  7  CELL-KILLED                                  NOT void: reported per arm, V1 read as a FLOOR
  8  TURNS-CUT                                    NOT void: reported per arm, cost figures unpoolable
```
⛔ **My expectations about which arm or which model costs more are NOT in this list**, and neither is
the §F2 prior. **A failed prediction is the experiment working, never a stop.**

## §F6 · WHAT THIS WAVE CANNOT ESTABLISH, SAID BEFORE ANY DATA
1. ⛔ **Anything about TIER alone.** §F3. The model axis carries two changes.
2. **No magnitude.** Sign only, until a variance pilot re-derives a floor from THIS model's dispersion.
3. **Nothing about brownfield.** This is a greenfield wave; level 4's field is a different object.
4. **No cross-lane comparison.** The Claude lane is not comparable to this one in dollars or in tokens.
5. **n = 3 per condition.** At this n the design resolves only a very large effect.
6. **A cost premium and a V1 rate are TWO RESULTS** and must never be joined with "and therefore".

## §F7 · WHAT THE HAND DELIVERS
```
  one export_sha across all 42 cells, recorded; scorer_export_sha beside it if newer
  per-condition score receipts as FILES, never a summary typed into a post
  the PER-CELL TABLE OF RECORD — arm · problem · T · wall · turns · commands · done_reason ·
    end · verdict · tests · TURNS-CUT flag · source receipt      (the standing form, council ③)
  TURNS-CUT incidence reported as a SPLIT BY ARM, never pooled
```
⇒ **The lead scores and writes the result of record. Any public sentence, and any claim about the
method, is the Captain's.**

---

# ADDENDUM 1 — **LEVEL 5 IS HALTED AT ONE CELL. THIS ADDENDUM IS ITS RESULT OF RECORD.**
## bench (lead), 2026-09-14, ~2 h after the freeze. **The wave produced ONE cell and NO scored data.**
## ⛔ **It produced a finding anyway, and the finding is about THIS HARNESS AND THAT MODEL AS A PAIR —
## never about the model's capability.** Cost: 1 cell, ~2 % of a five-hour pool.

## §A1 · WHAT HAPPENED
The hand fired condition 1 and halted after **one cell**: `gemini-3.8-flash-high` reached the **1,800 s
per-turn print deadline on every turn**, with no turn completing. It quarantined the root by cause,
scored nothing, and handed the fork up as a design call rather than re-capping. **That was correct**:
⇒ 🔑 ***A CAP THAT BINDS OCCASIONALLY IS A MEASUREMENT; A CAP THAT BINDS ON EVERY TURN IS THE
INSTRUMENT, NOT THE SUBJECT.*** §F2 registered the cap's incidence as a reported quantity — **incidence,
not saturation.** A wave of 42 cells whose every figure is a floor would have cost the pool and said
nothing about Flash.

## §A2 · ⛔⛔ THE CHARACTERISATION WAS WRONG, AND IT IS THE HALF THAT MATTERS
The halt came with a proposed finding: *"`gemini-3.8-flash-high` does not complete turns under this
harness at the registered caps."* **Measured at the object, that is FALSE.** Two hypotheses died and one
survived:
```
  ⛔ REFUTED   "the turn loop misses a differently-named terminal event"
               Flash's stream:  init 1 · step_update 100 · result 1   — THREE types, no others
               Pro's stream:    init 1 · step_update  97 · result 5   — THE SAME THREE
               (and b4fs03, a long Pro cell: init 1 · step_update 2193 · result 9)
               ⇒ identical event vocabulary. The loop parses everything it is sent.
  ✅ MEASURED   WHERE the `result` events sit, which is the entire finding:
               FLASH   init at line 1 ............... result at line 102 of 102   <- THE LAST LINE
               PRO     results at lines 17 · 56 · 90 · 95 · 103 of 103            <- spread through
```
⇒ 🔑 ***FLASH DID NOT FAIL TO COMPLETE A TURN. IT RAN THE WHOLE EPISODE AS ONE TURN AND EMITTED ITS
`result` AT THE END.*** `agy_turnloop_v3.py:115` terminates a turn on `event == "result"` and waits per
turn against the deadline. **A model that returns one `result` per EPISODE meets a deadline built for a
model that returns one per TURN.**

## §A3 · ✅ THE FINDING, IN THE ONLY FORM THE EVIDENCE SUPPORTS
> **Under the v3 agy turn loop — which terminates a turn on a `result` event and applies an 1,800 s
> per-turn print deadline — `gemini-3.8-flash-high` emitted ONE `result`, at the end of the episode,
> across 100 `step_update`s in 34 minutes, where `gemini-3.1-pro-high` emitted FIVE, spread throughout,
> across 97 in 160 s. The two models segment an episode into turns differently, and the per-turn cap is
> calibrated on Pro's granularity.**

⛔ **WHAT THIS IS NOT, stated because the false version is the quotable one:** it is **not** a claim that
Flash is slow, incapable, or worse at the task; **not** a capability comparison; and **not** a result
about the tier, which §F3 already forbids on a separate ground.

## ⛔⛔ §A3a · THE DENOMINATOR, AND IT SITS HERE RATHER THAN IN A FOOTNOTE
**THE FLASH SIDE IS `n = 1`.** Measured in the quarantined root by the hand, after the halt:
```
  l5cp01   102 lines   init 1 · step_update 100 · result 1   result at line 102 of 102   <- the trace
  l5cp02   NO STREAM   launched, killed before emitting a byte
  l5cp03   NO STREAM   launched, killed before emitting a byte
```
⇒ **The halt landed between launch and first emission for two of the three, which is why it was cheap
and also why it bought NO CORROBORATION.** There is no further Flash evidence on the box.
⚠️ **So "the two models segment an episode differently" rests on ONE Flash trace against several Pro
cells.** The signature is structural — a POSITION, not a rate — and a second cell would likely confirm
rather than refine it. ⛔ **"Would likely confirm" IS A PREDICTION, and it is not evidence.** The
sentence carries its `n` wherever it travels.
📌 **AND WHAT REMAINS UNMEASURED BY ANYONE:** *why* the two segment differently — client stream framing
for this model, a thinking mode, or the model's own behaviour. **Nobody measured it; the finding does not
rest on it; it is registered OPEN rather than guessed.**

## §A4 · ⚖️ THE REGISTERED LIMITATION — THE PART WORTH MORE THAN THE 42 CELLS
⇒ ***A PER-TURN CAP IS ARM-NEUTRAL ONLY BETWEEN MODELS THAT SEGMENT AN EPISODE THE SAME WAY.*** It is not
a cap on WORK; it is a cap on an INTERVAL whose length is a property of the model.
⛔⛔ **AND THE TWO HALVES OF THIS SECTION HAVE DIFFERENT EVIDENCE, WHICH IS WHY THEY ARE NAMED APART:**
```
  THE DESIGN PRINCIPLE   "if two models segment differently, a per-turn cap measures different
                         things in each"     — TRUE BY CONSTRUCTION. It needs no n at all, and it
                         binds whether or not Flash turns out to be such a model.
  THE EMPIRICAL CLAIM    "gemini-3.8-flash-high and gemini-3.1-pro-high DO segment differently"
                         — n = 1 ON THE FLASH SIDE (§A3a). This is the half that can be wrong.
```
⇒ **The principle is what binds future waves. The empirical claim is what this wave measured, once.**
📌 **A reader who takes §A4's first line as MEASURED has read a design statement as a result** — the
same conflation this addendum exists to correct, one level up.
⇒ **This generalises §G2's law rather than replacing it: a cap that DIFFERS between arms is a treatment —
and so is a cap that is IDENTICAL between arms but MEASURES A DIFFERENT THING in each.**
📌 **Binding on any future cross-model wave in this campaign.** A cross-model design must either
demonstrate equal turn granularity or cap on the per-CELL wall, never the per-turn one.

## §A5 · THE RULINGS
```
  (A) RAISE print_timeout FOR THE FLASH ARM ..... REJECTED. A cap that differs between arms is a
      treatment, and the Pro↔Flash contrast already carries TIER+GENERATION (§F3).
      ⛔ It would also not work as intended: Flash's turn IS the episode, so the honest cap for it
        is the per-CELL wall (max_wall 21,600 s), not a larger per-turn one.
  (B) DO NOT RUN THE 42 ........................ ACCEPTED, with §A3's claim replacing the proposed one.
  (C) RE-CAP / RE-CUT / RE-FIRE ................. NOT AUTHORISED. Nothing further fires on level 5.
  QUARANTINE .................................... RATIFIED. Both roots kept, named by cause, nothing
      scored, nothing in any denominator. The 3 earlier Pro-under-Flash-ids cells stay VOID (§F5 row 1).
  LEVELS 1 AND 4 ................................ UNTOUCHED and complete.
```

## ⇒ 🔑 §A6 · THE ONE TO CARRY
***THE INSTRUMENT PRODUCED A STATEMENT ABOUT A VENDOR'S MODEL, AND ONLY OPENING THE INSTRUMENT SHOWED IT
WAS A STATEMENT ABOUT THE INSTRUMENT.*** The halt was right, the recommendation was right, and the claim
attached to them was wrong in the one direction that costs something — **a capability sentence about
somebody else's model, from one cell, generated by our own turn loop's assumption.**
📌 **The hand declined to open `agy_turnloop_v3.py` because the client boundary is the lead's. That was
the correct refusal and it is why the error reached a reader who could check it.**

---

# ⛔⛔ ADDENDUM 2 — **ADDENDUM 1'S CENTRAL FINDING IS REFUTED. FLASH DID NOT STALL; IT GOT A 503.**
## bench (lead), 2026-09-14, ~2 h after ADDENDUM 1 MERGED at `6d8dd527`. **Found by the hand, verified
## independently by me at the same object.** ⛔ **This corrects a claim about a VENDOR'S MODEL that this
## repo had already published.**

## §E1 · THE OBJECT, WHICH NEITHER OF US OPENED
ADDENDUM 1 read the **POSITION** of `result` records — Flash's one at line 102 of 102, Pro's five at
17 · 56 · 90 · 95 · 103 — and concluded *"Flash ran the whole episode as ONE TURN."* **The `result`
object's own fields say otherwise:**
```
  status            ERROR
  duration_seconds  965.561196        <- the 1800 s per-turn print deadline NEVER FIRED
  num_turns         1
  error             API error (attempt 1): UNAVAILABLE (code 503):
                    No capacity available for model gemini-3.8-flash-high on the server
```
⇒ **The cell did real work first** (the hand's read: `output_tokens 20,043 · thinking 16,495 · total
368,457`) **and then the server ran out of capacity at ~16 minutes.** **Nothing about turn structure was
observed at all.**

## §E2 · ⇒ 🔑 HOW A CHECK CONFIRMED THE WRONG THING
ADDENDUM 1 was not unchecked. It ran an event-type census on Flash **and a Pro control**, found the same
three types in both, and read that as *"the loop parses everything it is sent."*
⇒ ***IT DOES — AND A `result` WITH `status=ERROR` IS PARSED, COUNTED AND POSITIONED EXACTLY LIKE A
SUCCESS.*** ⇒ **A CONTROL THAT MATCHES ON THE AXIS YOU CHOSE CONFIRMS YOUR AXIS, NOT YOUR CONCLUSION.**
⛔ **The axis was `event` type and `result` POSITION. The answer was one field deeper, in plain English,
written by the server.**

## §E3 · WHAT DIES AND WHAT STANDS
```
  DIES    "gemini-3.8-flash-high runs an episode as ONE TURN"        REFUTED
  DIES    §A4's EMPIRICAL half — "THESE two models segment differently"  no evidence remains
  DIES    "level 5 is BLOCKED"                                       a 503 is RETRYABLE
  DIES    §A5's rulings (A) REJECTED and (B) DO-NOT-RUN-THE-42       their basis is gone
  STANDS  §A4's DESIGN half — "if two models segment differently, a per-turn cap measures different
          things in each" — TRUE BY CONSTRUCTION. ⚠️ It now has NO KNOWN INSTANCE.
  STANDS  the HALT. Stopping at one cell was right, and it is why this cost one cell.
  STANDS  §A3a's denominator discipline (n = 1 on the Flash side) — which is what kept the damage to
          one refutable sentence instead of a wave.
```
⭐ **§A4 WAS SPLIT INTO A DESIGN HALF AND AN EMPIRICAL HALF BEFORE THIS REFUTATION ARRIVED**, on the
hand's insistence about the denominator. ⇒ **The refutation lands entirely on the empirical half.** **Had
they stayed welded, a 503 would have taken a true-by-construction principle down with it.**

## §E4 · LEVEL 5's STANDING, RESTATED
**NOT BLOCKED — OWED, with a named external risk.** A 503 is server capacity: **an external condition
nobody in this fleet controls, which may recur.** ⇒ **A re-fire is legitimate and needs no new design
ruling**; it needs capacity. ⛔ **No re-fire is authorised in this addendum** — the wave's scope is the
council's and the pool is the Captain's. **This addendum only removes a block that was never real.**

## ⇒ 🔑 §E5 · THE ONE TO CARRY
***I WROTE "ASK THE INSTRUMENT BEFORE DEBATING THE ANSWER" FIFTEEN MINUTES BEFORE FAILING TO ASK IT OF MY
OWN FINDING.*** The instrument had already answered: the error string was in the stream the whole time,
in a field nobody read, on the very cell both seats were reasoning about.
📌 **AND THE SHAPE THAT MADE IT SURVIVE A CHECK: the check and the claim shared an axis.** An
event-type census and a position census both measure the ENVELOPE. **A 503 lives in the PAYLOAD.**

---

# ✅ ADDENDUM 3 — **THE RETRY LANDED. THE TURN-STRUCTURE CLAIM IS NOW *POSITIVELY* REFUTED, AND THE TURN-LOOP QUESTION IS CLOSED.**
## bench (lead), 2026-09-14. **The Captain authorised one retry, up to 3 attempts, on the capacity error.
## Attempt 1 succeeded.** Reading frame registered by the lead BEFORE it ran, so nothing here is fitted.

## §G1 · THE RESULT OBJECTS — ALL THREE, PAYLOAD FIRST
```
  line 210 of 347   status=SUCCESS  duration_seconds=527.934851  num_turns=1  error=-
  line 305 of 347   status=SUCCESS  duration_seconds=696.151821  num_turns=2  error=-
  line 347 of 347   status=SUCCESS  duration_seconds=758.690128  num_turns=3  error=-
  ctl/end-1   2026-09-14T19:50:35Z LANDED   ·   model_requested == model_served == gemini-3.8-flash-high
  attempt 1 of up to 3 · reader VERIFIED against the known 503 cell BEFORE any spend
```
⇒ **Flash emits ONE `result` PER TURN, SPREAD THROUGH THE STREAM — 210 · 305 · 347 — exactly as Pro
does.** ⇒ **`duration_seconds` is CUMULATIVE (527.9 → 696.2 → 758.7), not per-turn.**

## §G2 · ⇒ 🔑 THE CLEAN STATEMENT OF ADDENDUM 1's ERROR
ADDENDUM 2 said the empirical half of §A4 had *"no evidence remaining"*. **It now has evidence, and it
points the other way.** The 09-14 cell's single `result` sat at **line 102 of 102**, and ADDENDUM 1 read
*"terminal position"* as *"one long turn"*.
```
  a result at the LAST line is what ONE LONG TURN would look like
  a result at the LAST line is ALSO what an ERROR ON TURN 1 looks like
  ⇒ THE POSITION CANNOT TELL THEM APART.  `status` CAN, and it was one field away.
```
⇒ ***CAUSE AND EFFECT WERE REVERSED: THE END OF THE STREAM WAS TREATED AS EVIDENCE ABOUT TURN STRUCTURE
WHEN IT WAS EVIDENCE THAT THE RUN HAD ENDED.*** ⛔ **And the Pro "control" could not have caught it: a Pro
cell that SUCCEEDS also has its last `result` on its last line — 103 of 103. Both models put a result at
the end. The difference was never positional.**

## §G3 · THE TURN-LOOP QUESTION IS CLOSED FOR BOTH MEASURED MODELS
*Is "one `result` per turn" a PRO-SPECIFIC assumption in the v3 turn loop?* — **NO.**
**Flash 3 turns / 3 results · Pro 5 turns / 5 results.** ⇒ **The loop's assumption holds for both.**
⚠️ **Untested for any other client or vendor**, so the probe stays registered OPEN for a genuinely new
lane. ⛔ **§A4's DESIGN half still has NO KNOWN INSTANCE**, and is now less likely to acquire one.

## §G4 · ⛔⛔ CAPACITY: WHAT IS KNOWN, AND IT IS WEAKER THAN TWO EARLIER STATEMENTS OF MINE
```
  UNAVAILABLE at   2026-09-14T16:57:07Z   (503, last stream byte of the failed cell)
  AVAILABLE by     2026-09-14T19:37:23Z   (the retry's LAUNCH; it then ran clean)
  RECOVERY TIME    UNMEASURED. Upper bound 2 h 40 m 16 s. n = 1 outage. INTERIOR UNPROBED.
```
⛔ **I twice called this "~3 h recovery". BOTH STATEMENTS WERE WRONG, IN TWO DIFFERENT WAYS:**
1. **My anchor was the retry's LANDING, not its LAUNCH** — charging the outage for 13 minutes 12 seconds
   during which the model was demonstrably WORKING. ⇒ *I measured "time until the retry finished" and
   called it "time until capacity returned".*
2. ⭐ **And even the corrected 2:40:16 is NOT a recovery time — NOBODY PROBED THE INTERIOR.** Capacity may
   have returned at 16:58. **The interval holds two observations, one failure and one success, and no
   information about what lies between them.** ⇒ **A RIGHT-CENSORED UPPER BOUND.**
⇒ **A wave scheduled on "~3 h recovery" would be scheduled on a bound the data cannot distinguish from
one minute.** ✅ **A recovery estimate costs a cheap poll during an outage, never a wave. Not proposed.**

## §G5 · STANDING
**Flash's 46 census conditions: OWED, with an INTERMITTENT capacity risk of UNKNOWN duration.** ⛔ **The
42-cell wave remains UNAUTHORISED — it was always a SPEND question and the Captain's.** ✅ **Attempts 2
and 3 are unnecessary: they were authorised against a capacity error, and attempt 1 landed clean.**
