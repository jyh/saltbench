# RESULT OF RECORD — LEVEL 7 (series `l7u`, blocks BN · BS · C), gemini lane
## bench (SaltBench lead), 2026-09-19. Mode A ended `rc=0 … TRIPWIRE-HOLD` 2026-09-18T18:14:19Z; mode B ended
## `rc=0 … CHAIN-DONE mode B` 2026-09-19T21:19:06Z. Registered by `AMENDMENT-gemini-level7-2026-09-16.md`
## (§K9 names these deliverables). Export `9bfb6ef86a363cd9427ddc7298a6be97e98cc51e`, one sha across all 84 cells.
## ⛔ Every number below names the file it came from. Nothing is retyped from a bus post or a message.
## 📌 The per-cell table is also a FILE: `RESULT-gemini-level7-2026-09-19-cells.tsv` (84 rows, 30 columns).

---
# §1 · THE HEADLINE, AND IT IS NOT THE PASS RATE

**28 conditions · 84 cells · 81 scorable · 75 FULL PASS.** The pass column is **at or near ceiling on
three of the four (model × arm) quadrants**, so §K6 rule 11 governs most of it and it says nothing about
the arms:

```
  verified pass, SCORED cells only        plain        salt-diet
    gemini-3.8-flash-high                 21 / 21       19 / 19      <- total ceiling, both arms
    gemini-3.1-pro-high                   20 / 21       15 / 20
```
*(⚠️ The Flash-plain cell read `24 / 24` in this table's first draft — a number I **typed**, from
"42 plain cells, two models" rather than from the scores. There are 21 Flash-plain cells, not 24. It was
caught before this file was committed by the verifier in §9b, which re-derives every figure here from the
receipts; **the idiom law's clause 1 exists for exactly this and it fired on its own author.**)*

⛔ **AND THE ONE QUADRANT THAT MOVES CANNOT BE READ AS AN ARM RESULT, BECAUSE THE CAP IS ARM-CORRELATED
10 : 0 IN THE SAME QUADRANT.** Every `TRUNCATED`, every `SELF-NOT`, every `PERSIST-INDETERMINATE` and
every `false_done > 0` in this level is a **Pro · salt-diet** cell — **ten cells, zero plain, zero Flash**:

```
  l7npfs01 false_done=2          l7npfs02 SELF-NOT false_done=2   l7npfs03 SELF-NOT PERSIST false_done=2
  l7npzs01 TRUNCATED             l7npzs02 false_done=1            l7npzs03 TRUNCATED SELF-NOT PERSIST
  l7spfb02 TRUNCATED             l7sprs02 TRUNCATED               l7sprs03 TRUNCATED
  l7spzs03 TRUNCATED
```
By the level-4 §L5 rule this freeze carries unchanged — **an arm-correlated cut is decided by its SIGN** —
truncation removes salt-diet work and therefore pushes salt-diet's pass rate **down**. So Pro's `15/20`
is confounded **in the direction that produces it**, and this result makes **no pass-rate claim about the
arms.** It is reported, not resolved.

⭐ **THE SEPARATOR THAT DOES MOVE IS RETENTION, AND IT MOVES IN THE SAME DIRECTION IN 7 OF 8 (model ×
problem) PAIRS** — §K6 rule 10's primary brownfield separator, per cell, never averaged across problems:

```
  model  problem   plain median [range]            salt-diet median [range]          bands
  Flash  Crc32     0.654 [0.529-0.817] n=6         0.292 [0.235-0.372] n=4           DISJOINT
  Flash  FreeList  0.664 [0.392-0.831] n=6         0.390 [0.237-0.466] n=6           overlap
  Flash  LRU       0.948 [0.610-0.952] n=3         0.231 [0.188-0.344] n=3           DISJOINT
  Flash  LZW       0.443 [0.291-0.725] n=6         0.446 [0.193-0.586] n=6           overlap  <- ⛔ NOT
  Pro    Crc32     0.694 [0.364-0.980] n=6         0.236 [0.224-0.246] n=5           DISJOINT
  Pro    FreeList  0.885 [0.646-1.000] n=6         0.610 [0.287-0.693] n=6           overlap
  Pro    LRU       0.976 [0.961-0.981] n=3         0.309 [0.126-0.318] n=3           DISJOINT
  Pro    LZW       0.990 [0.511-0.990] n=6         0.306 [0.107-0.531] n=6           overlap
```
⛔ **`Flash × LZW` IS THE EXCEPTION AND IT IS STATED IN THE HEADLINE RATHER THAN IN A FOOTNOTE: its
salt-diet median (0.446) is ABOVE its plain median (0.443).** The first draft of this section said
"8 of 8" — I wrote it before the medians were computed, from the shape of levels 4 and 6. It is 7 of 8.
⇒ 🔑 ***A DIRECTION THAT HOLDS IN SEVEN CELLS OF A TABLE IS THE EASIEST PLACE IN THE WORLD TO PUT AN
EIGHTH, AND THE ONLY THING THAT STOPS YOU IS COMPUTING IT.*** *(Same defect the census's own ADDENDUM 9
§P3 recorded against itself two days ago: a section copied from the last addendum inherits its conclusion.)*

## §1b · ⛔ THE RETENTION POPULATION, STATED — AND IT IS A CORRECTION MADE AT SIGNATURE
**A retention band contains only cells that RAN THE EXPERIMENT: ended, and received their arm.** The same
population as the pass quadrants, and for the same reason the scorer's own header gives — *a cell whose arm
never arrived did not run the experiment this table is about.*
⚠️ **THE TABLE ABOVE READ `Pro × Crc32 × salt-diet 0.237 [0.224-0.289] n=6` UNTIL THIS CORRECTION, AND THAT
BAND INCLUDED `l7cpbs03` — THE ONE CELL THIS DOCUMENT EXCLUDES FROM SCORABLE** (VOID(NO-BRIEFING),
ARM-NOT-RECEIVED, §3). Found by `systems` at signature, by asking the same question of **all sixteen bands**
and finding **exactly one** in which a `NOT-SCORED`/`INCOMPLETE` row carried a pooled retention value.
⇒ 🔑 ***TWO SECTIONS OF THIS DOCUMENT WERE USING TWO DIFFERENT POPULATIONS AND NEITHER SAID SO. §1 EXCLUDED
THAT CELL FROM EVERY PASS RATE IN THE SAME BREATH AS INCLUDING IT IN A BAND*** — and the tell was free: the
excluded cell's `0.289` **was the band's printed upper bound.**
✅ **RE-DERIVED ON THE STATED POPULATION, ONE BAND MOVES AND FIFTEEN ARE BIT-IDENTICAL:** `0.236 [0.224-0.246]
n=5`. **SAME DIRECTION IN 7 OF 8 pairs, 4 on DISJOINT bands** — both unchanged, and the direction **strengthens** — against plain's
`[0.364-0.980]` the salt edge moves from 0.289 to 0.246, further from disjointness' boundary, not toward it.
⇒ **A correction that makes a claim stronger is the one most likely to go unmade**, which is why it is here
and not in a footnote. The band's new population is now asserted by an arm (§9b), where it had none.
⚠️ **AND THE OTHER TWO EXCLUDED ROWS:** `l7cfss02`/`l7cfss03` carry `retained=1.000 · UNTOUCHED` in §4's
table. They never ran, so that is a **measurement-shaped value with no measurement behind it** — the same
class this result names for `retention.txt` in §2, now found in its own table by its signer. **They are in
no band** (the rule above excludes them) and the raw value is kept because §4 records what the receipts
said; **it is inert today and would cost something the first time a band is cut without the filter.**

⭐ **AND THE COST PREMIUM IS THE LARGEST THIS CAMPAIGN HAS MEASURED: `4.295x` TOTAL TOKENS, `2.676x`
OUTPUT.** §7 has the figures, the exclusions, and the robustness check.

---
# §2 · ⛔⛔ THE FINDING THAT OUTRANKS EVERY NUMBER ABOVE — ONE CONDITION RAN 1 OF 3 CELLS, AND **TEN** RECEIPTS DESCRIBE IT

`cells-l7-crc32-flash-salt-stmt-bf` declared 3 cells and ran **one**. The wave was right to stop; the
reporting was not. **gemini named this at its leg end (bus 60,911,176) and named three green layers. I have
read every receipt that mentions those two cells, and the shape is sharper than "three layers went green":**

```
  RECEIPT                        WHAT IT SAYS ABOUT l7cfss02 / l7cfss03           READS AS
  chain (END-MARKER-B)           rc=0 CHAIN-DONE mode B                           GREEN - blind
  leg supervisor                 SUPERVISOR END rc=0 - WAVE-DONE 4 condition(s)   GREEN - blind
  ledger.tsv / leg-C-flash.out   ✅ CONDITION-CLEAN 4 · l7cfss02:-:a503=0          ⛔ THE LOSS IS *INSIDE*
                                                                                     THE GREEN LINE
  driver (c4-a1.driver.out)      "FIRE STAGE DONE - 1 attempted, 0 refused or     GREEN - and FALSE
                                  failed"
  harvest arm 4                  4 conditions = 4 score files; 12 cells = 12      GREEN - structurally blind
  conditions.tsv                 CLEAN, three cell ids listed                     GREEN - blind
  fault-cells.tsv                BRIEFING=(pending) FAULT=(pending)               ⚠️ implies "coming"
  retention.txt                  UNTOUCHED / RUNNING, "Re-read these after        ⛔ WRONG - they never land
                                  they land"
  scorer                         ENDED 1/3 · "running - no end marker yet -       ✅ SEES IT, ⛔ wrong reason
                                  not a void"
  cells.tsv                      row=UNMEASURED(NO-STREAM) done_reason=UNREAD     ✅ HONEST
  end-markers.tsv                NOT-ENDED                                        ✅ HONEST
  token-scan.tsv                 UNMEASURED(TOKEN-SCAN: no receipt fetched)       ✅ HONEST
  flags.tsv                      served=<EMPTY>, every other field present        ⚠️ a silent blank
  ctl/agy-meter-*.json           THE FILE DOES NOT EXIST                          ✅ the cleanest tell
```

⇒ 🔑 ***IT IS NOT THAT ONE LAYER SAW THE LOSS AND THREE WENT GREEN. FOUR RECEIPTS SAID PLAINLY THAT THESE
CELLS PRODUCED NOTHING — AND EVERY ONE OF THEM IS A PER-CELL RECEIPT NOBODY READS, WHILE EVERY LAYER THAT
**SUMMARISES** WENT GREEN.*** A summary's job is to compress, and **an absence compresses to nothing**:
`l7cfss02:-:a503=0` is the loss, printed in full, inside a line that begins with a ✅, distinguished from a
landed cell by the absence of one word.

✅ **THREE ONE-LINE DETECTORS, EACH DRIVEN HERE WITH A CONTROL, NEEDING NO NEW INSTRUMENT:**
```
  grep -c 'NOT-ENDED' harvest-*/end-markers.tsv        BN-pro 0 · BN-flash 0 · BS-pro 0 · BS-flash 0
                                                        · BS-trip 0 · C-pro 0 · C-flash 2      ⇒ 2
  grep -c ':-:a503='  leg-*.out                         six legs 0 · leg-C-flash 1             ⇒ 1 condition
  count ctl/agy-meter-*.json                            82 of 84 cells have exactly 1; 2 have 0
  (gemini's own) RESIDUAL = declared - LANDED - EXCLUDED     BS-pro 0 · BS-flash 0 · C-pro 0 · C-flash 2
```
⛔ **AND A NEEDLE TRAP INSIDE THE CHEAPEST ONE, WHICH I HIT WHILE DRIVING IT: `grep -c ENDED` ON
`end-markers.tsv` COUNTS `NOT-ENDED` TOO** — C-flash reads **12** for `ENDED` while only **10** cells ended.
A containment detector for a success marker counts its own negation. Match `NOT-ENDED` positively, or
anchor the tab (`grep -c '\tENDED '`). *(The fleet's needle-defect class, live inside the receipt written
to catch the defect.)*

## §2b · ⛔ AND THE PROXIMATE CAUSE IS NOT "A SHORT CREDENTIAL WINDOW" — THE TOOL SPENT THE WINDOW WAITING FOR THE REFRESH THAT WOULD HAVE RESTORED IT

Read at the object, `…/l7u-C-flash-2026-09-18-c4a1/cells-l7-crc32-flash-salt-stmt-bf.fire.log`, verbatim:
```
  20:34:37Z  CREDENTIAL WINDOW 2781s remaining (need 2400s) - launching
  20:43:18Z  CREDENTIAL WINDOW 2260s remaining, below the 2400s a cell needs; warming
  20:43:28Z  WARM-UP ok (token unchanged a0b09190e27c530f - it was not yet due for refresh)
  20:43:28Z  the client does not consider a refresh due yet; waiting 2010s for its refresh window
             rather than launching into the last minutes of a token
  21:16:58Z  CREDENTIAL WINDOW 240s remaining, below the 2400s a cell needs; warming
  21:17:14Z  REFUSE - the credential warm-up did not return SUCCESS: error: Eligibility check failed:
             failed to get profile picture: Get "https://lh3.googleusercontent.com/a/...": net/http:
             TLS handshake time[out]
  21:17:14Z  REFUSE - the credential window is too short before l7cfss02
  21:17:14Z  WAVE COMPLETE
```
**THE ARITHMETIC IS EXACT: 20:43:28 + 2010 s = 21:16:58, and 2260 − 2010 = 250 ≈ the 240 s it then read.**
⇒ 🔑 ***THE WAIT DID NOT PRESERVE THE WINDOW, IT CONSUMED IT. THE TOOL DECLINED TO FIRE AT 2260 s BECAUSE
THAT WAS 140 s SHORT OF ITS 2400 s BUDGET, AND THEN SPENT 2010 s OF THAT SAME 2260 s WAITING.***
⚠️ **STATED AS A COUNTERFACTUAL, NOT A FACT:** the cell that *did* run in this condition took **494.3 s**
wall, and the other three Crc32-Flash-salt cells took 356.6 · 408.1 · 2095.7 s. A launch at 20:43 would
have had 2260 s against an observed median near 450 s. **I did not run it and I am not claiming it would
have landed** — only that the 2400 s budget is ~4.9× the observed cost of the cell it was budgeting for,
and that the refusal rule and the wait rule interact to lose a cell that neither would have lost alone.
⛔ **The second refusal is also not the one the ledger implies:** the warm-up failed an **eligibility check
that fetches a profile picture over TLS**. A datum was lost to an avatar GET.
⇒ **NOT A REPAIR IN THIS COMMIT.** Changing when a wave fires changes what a run measures, so it belongs
in a dated amendment before the next wave's first model call — the rule `RESULT-gemini-level6-2026-09-17.md`
§8(3) states and this result obeys. It is carried into the lane-widening addendum, where the helm has
already asked how a chain reads a meter before each fire.

## §2c · THE DISPOSITION OF THE DATUM, WHICH IS THE LEAD'S
**`cells-l7-crc32-flash-salt-stmt-bf` IS NOT `DONE`. IT STAYS `OWED`, AT n = 1 OF 3.** Its one cell
(`l7cfss01`, LANDED, PASS 6/6, retained 0.235) is scored, recorded in §4 and reusable. **Reason, and it is
this census's own precedent rather than a judgment invented here:** §C4's flash row was held BLOCKED on
exactly the ground that *"n = 1 on the Flash side"* was not a condition. Counting a condition `DONE` because
the wave refused to fire two thirds of it would let the matrix read fuller than the evidence, on the one
axis the Captain reads it for. **It is one cell, and one cell is not a condition.**
⛔ **THE OTHER THREE C-flash CONDITIONS ARE UNAFFECTED** — 3/3 cells each, all LANDED, all PASS.

---
# §3 · POPULATION — 84 DECLARED, 84 HARVESTED, AND SIX RECEIPTS AGREE ON THE COUNT

```
  leg        conds  cells  retention  end-markers  flags  given-check  token-scan
  BN-pro       4      12       12          12        12        12          12
  BN-flash     4      12       12          12        12        12          12
  BS-pro       6      17       17          17        17        17          17
  BS-flash     6      18       18          18        18        18          18
  BS-trip      -       1        1           1         1         1           1     (cell 1 of BS-pro's
  C-pro        4      12       12          12        12        12          12      FreeList salt-stmt
  C-flash      4      12       12          12        12        12          12      condition, §K2)
  ──────────────────────────────────────────────────────────────────────────────
  TOTAL       28      84       84          84        84        84          84     = §K1's 28 / 84
```
**§K7 VOIDS, DRIVEN ROW BY ROW OVER ALL 84:**
```
  row 1  served model ≠ condition's model          0   42 Pro + 40 Flash served; 2 cells never ran, so
                                                        no cell was served the wrong id
  row 2  METER-BLIND / no readable T               0   82 of 84 carry exactly one agy-meter json; the 2
                                                        without are the refused cells (§2), NOT unpriced runs
  row 3  ctl/field or ctl/card_extras ≠ flags      0   field=brownfield 84/84 · card_extras none 36 /
                                                        statement 48, exactly §K1's split
  row 4  fence battery                             0   w1_fenced COVERED 84/84
  row 5  a 503 inside the cell                     2 conditions re-fired, not voided (below)
  row 6  CAP-TOKENS/CELL-KILLED/TURNS-CUT          0   not void by rule; reported in §6
  row 7  LEAK-class token occurrence               0   token-scan CLEAN 82/82 measured, n_leak=0 on every
                                                        one; 2 UNMEASURED and declared as such
  row 8  given ≠ the export's given                0   GIVEN-OK 84/84
```
⇒ **ZERO §K7 VOIDS IN 84 CELLS.**

**THE TWO 503 RE-FIRES, both under the any-503 rule (§K7 row 5), neither a void:**
- **BS tripwire**: attempt 1 killed and discarded; `l7spfwa201` is attempt 2 (`END-MARKER-A`).
- **`cells-l7-crc32-pro-salt-stmt-bf`**: attempt 1 discarded; the canary held the gate `DEGRADED` from
  16:11:57Z to 16:36:59Z and the condition re-fired as `-a2` (`leg-C-pro.out:25–32`). All three `-a2`
  cells LANDED and PASS.

**ONE EXCLUDED CELL, by a mechanism that is NOT in §K7 and is stated for that reason:** `l7cpbs03` reads
`VOID(NO-BRIEFING)` / `ARM-NOT-RECEIVED` / `done_reason=NO-FIRST-RESULT` — the arm never reached the
subject, so the cell did not run the experiment this table is about. That is `briefing_verdict_v3.py`'s
standing receipt gate (`score_wave_v3.sh`'s header states it), the same mechanism that voided level 6's
`l6vgfs02`, and it is **not** one of §K7's eight rows. ⚠️ **It burned `9,956,601` T and is excluded from
§7's cost pool as well as from every pass denominator** — a cell can be unpriced-for-science and expensive
at the same time, and only the second half is visible on the bill.

---
# §4 · THE PER-CELL TABLE OF RECORD (§K9), DERIVED FROM THE RECEIPTS

**Sorted by arm, then block, then model, then problem.** `T` and `out_tok` are folded per conversation by
`ctl/agy-meter-*.json` (82 of 84 cells: exactly one conversation each). `reten`/`class` from
`retention.txt`; `end` from `end-markers.tsv`; `verdict`/`tests` from the score files; `wall_s`/`turns`/
`done_reason`/`false_done` from `cells.tsv`. **The same 84 rows with 30 columns are in
`RESULT-gemini-level7-2026-09-19-cells.tsv`.**

```
cell        blk  arm        problem   model  T            out_tok   wall_s    turns  done_reason  end                     verdict           tests    reten      class      flags
l7nffp01    BN   plain      FreeList  Flash  6,360,553    83,670    553.5     3      LANDED      LANDED                  PASS              7/7      0.392      REPAIRED
l7nffp02    BN   plain      FreeList  Flash  4,649,180    74,143    350.1     4      LANDED      LANDED                  PASS              7/7      0.537      REPAIRED
l7nffp03    BN   plain      FreeList  Flash  5,334,389    75,139    647.3     3      LANDED      LANDED                  PASS              7/7      0.434      REPAIRED
l7nfzp01    BN   plain      LZW       Flash  6,261,170    64,638    486.7     3      LANDED      LANDED                  PASS              8/8      0.291      REPAIRED
l7nfzp02    BN   plain      LZW       Flash  6,555,430    71,028    494.8     3      LANDED      LANDED                  PASS              8/8      0.353      REPAIRED
l7nfzp03    BN   plain      LZW       Flash  6,776,813    67,540    403.5     3      LANDED      LANDED                  PASS              8/8      0.315      REPAIRED
l7npfp01    BN   plain      FreeList  Pro    1,242,018    22,449    232.9     3      LANDED      LANDED                  PASS              7/7      0.646      REPAIRED
l7npfp02    BN   plain      FreeList  Pro    2,596,533    40,232    461.5     3      LANDED      LANDED                  PASS              7/7      0.690      REPAIRED
l7npfp03    BN   plain      FreeList  Pro    1,949,814    26,378    313.2     3      LANDED      LANDED                  PASS              7/7      0.775      REPAIRED
l7npzp01    BN   plain      LZW       Pro    1,523,409    17,376    242.2     3      LANDED      LANDED                  PASS              8/8      0.990      REPAIRED
l7npzp02    BN   plain      LZW       Pro    1,252,000    14,570    195.9     4      LANDED      LANDED                  PASS              8/8      0.990      REPAIRED
l7npzp03    BN   plain      LZW       Pro    2,097,518    17,675    242.4     3      LANDED      LANDED                  PASS              8/8      0.511      REPAIRED   ERROR(NO-COMMAND-PROVEN-OK)
l7sffp01    BS   plain      FreeList  Flash  6,354,773    67,685    341.6     3      LANDED      LANDED                  PASS              7/7      0.830      REPAIRED
l7sffp02    BS   plain      FreeList  Flash  7,756,505    92,762    430.5     4      LANDED      LANDED                  PASS              7/7      0.791      REPAIRED
l7sffp03    BS   plain      FreeList  Flash  8,522,338    84,825    469.1     3      LANDED      LANDED                  PASS              7/7      0.831      REPAIRED
l7sfrp01    BS   plain      LRU       Flash  4,705,974    45,024    277.6     4      LANDED      LANDED                  PASS              16/16    0.948      REPAIRED
l7sfrp02    BS   plain      LRU       Flash  3,676,567    44,829    285.8     4      LANDED      LANDED                  PASS              16/16    0.952      REPAIRED
l7sfrp03    BS   plain      LRU       Flash  4,034,404    58,991    385.6     4      LANDED      LANDED                  PASS              16/16    0.610      REPAIRED
l7sfzp01    BS   plain      LZW       Flash  6,616,783    73,506    398.0     3      LANDED      LANDED                  PASS              8/8      0.533      REPAIRED
l7sfzp02    BS   plain      LZW       Flash  5,536,955    55,895    386.9     4      LANDED      LANDED                  PASS              8/8      0.725      REPAIRED
l7sfzp03    BS   plain      LZW       Flash  5,919,649    54,963    411.7     3      LANDED      LANDED                  PASS              8/8      0.700      REPAIRED
l7spfp01    BS   plain      FreeList  Pro    1,184,720    14,474    197.5     3      LANDED      LANDED                  PASS              7/7      0.995      REPAIRED
l7spfp02    BS   plain      FreeList  Pro    1,822,259    20,171    268.0     3      LANDED      LANDED                  PASS              7/7      0.995      REPAIRED
l7spfp03    BS   plain      FreeList  Pro    2,782,794    27,598    357.3     3      LANDED      LANDED                  FAIL              6/7      1.000      UNTOUCHED
l7sprp01    BS   plain      LRU       Pro    1,355,238    20,042    216.1     3      LANDED      LANDED                  PASS              16/16    0.976      REPAIRED
l7sprp02    BS   plain      LRU       Pro    1,075,322    13,811    177.8     3      LANDED      LANDED                  PASS              16/16    0.981      REPAIRED
l7sprp03    BS   plain      LRU       Pro    1,704,567    15,062    207.1     3      LANDED      LANDED                  PASS              16/16    0.961      REPAIRED
l7spzp01    BS   plain      LZW       Pro    1,468,162    16,180    193.1     3      LANDED      LANDED                  PASS              8/8      0.990      REPAIRED
l7spzp02    BS   plain      LZW       Pro    1,314,076    19,806    218.8     3      LANDED      LANDED                  PASS              8/8      0.990      REPAIRED
l7spzp03    BS   plain      LZW       Pro    1,675,129    14,172    198.1     3      LANDED      LANDED                  PASS              8/8      0.990      REPAIRED
l7cfbp01    C    plain      Crc32     Flash  4,399,236    37,981    266.5     4      LANDED      LANDED                  PASS              6/6      0.673      REPAIRED
l7cfbp02    C    plain      Crc32     Flash  4,325,246    39,336    242.4     3      LANDED      LANDED                  PASS              6/6      0.660      REPAIRED
l7cfbp03    C    plain      Crc32     Flash  4,188,400    42,743    261.1     3      LANDED      LANDED                  PASS              6/6      0.648      REPAIRED
l7cfsp01    C    plain      Crc32     Flash  4,626,795    42,034    235.3     4      LANDED      LANDED                  PASS              6/6      0.529      REPAIRED
l7cfsp02    C    plain      Crc32     Flash  5,376,845    37,259    216.3     4      LANDED      LANDED                  PASS              6/6      0.817      REPAIRED
l7cfsp03    C    plain      Crc32     Flash  5,593,966    47,322    258.7     3      LANDED      LANDED                  PASS              6/6      0.529      REPAIRED
l7cpbp01    C    plain      Crc32     Pro    1,125,906    12,855    197.3     3      LANDED      LANDED                  PASS              6/6      0.713      REPAIRED
l7cpbp02    C    plain      Crc32     Pro    1,312,489    15,705    256.4     3      LANDED      LANDED                  PASS              6/6      0.674      REPAIRED
l7cpbp03    C    plain      Crc32     Pro    722,895      10,822    158.2     3      LANDED      LANDED                  PASS              6/6      0.674      REPAIRED
l7cpsp01    C    plain      Crc32     Pro    1,594,122    12,036    182.2     3      LANDED      LANDED                  PASS              6/6      0.364      REPAIRED
l7cpsp02    C    plain      Crc32     Pro    994,856      10,817    159.9     3      LANDED      LANDED                  PASS              6/6      0.980      REPAIRED
l7cpsp03    C    plain      Crc32     Pro    1,550,082    24,010    239.8     3      LANDED      LANDED                  PASS              6/6      0.753      REPAIRED
l7nffs01    BN   salt-diet  FreeList  Flash  22,734,954   181,904   989.9     4      LANDED      LANDED                  PASS              7/7      0.426      REPAIRED
l7nffs02    BN   salt-diet  FreeList  Flash  21,228,941   181,281   906.0     4      LANDED      LANDED                  PASS              7/7      0.466      REPAIRED
l7nffs03    BN   salt-diet  FreeList  Flash  17,804,823   107,729   688.9     4      LANDED      LANDED                  PASS              7/7      0.396      REPAIRED
l7nfzs01    BN   salt-diet  LZW       Flash  18,064,205   134,557   854.0     4      LANDED      LANDED                  PASS              8/8      0.586      REPAIRED
l7nfzs02    BN   salt-diet  LZW       Flash  16,854,859   121,149   1007.4    3      LANDED      LANDED                  PASS              8/8      0.499      REPAIRED
l7nfzs03    BN   salt-diet  LZW       Flash  17,493,691   113,937   966.2     3      LANDED      LANDED                  PASS              8/8      0.314      REPAIRED
l7npfs01    BN   salt-diet  FreeList  Pro    15,150,465   107,906   4381.8    7      LANDED      LANDED                  PASS              7/7      0.307      REPAIRED   false_done=2
l7npfs02    BN   salt-diet  FreeList  Pro    12,404,449   94,728    1337.2    7      LANDED      LANDED                  FAIL              6/7      0.669      REPAIRED   SELF-NOT false_done=2
l7npfs03    BN   salt-diet  FreeList  Pro    16,239,561   115,589   8249.3    7      LANDED      PERSIST-INDETERMINATE   FAIL              6/7      0.640      REPAIRED   SELF-NOT false_done=2
l7npzs01    BN   salt-diet  LZW       Pro    23,050,944   107,186   4716.6    5      LANDED      LANDED                  PASS              8/8      0.233      REPAIRED   TRUNCATED
l7npzs02    BN   salt-diet  LZW       Pro    26,462,763   232,294   5817.2    6      LANDED      LANDED                  PASS              8/8      0.333      REPAIRED   false_done=1
l7npzs03    BN   salt-diet  LZW       Pro    63,868,087   211,494   9165.1    7      LANDED      PERSIST-INDETERMINATE   PASS              8/8      0.531      REPAIRED   TRUNCATED SELF-NOT
l7sffs01    BS   salt-diet  FreeList  Flash  34,073,898   218,141   1155.1    4      LANDED      LANDED                  PASS              7/7      0.237      REPAIRED
l7sffs02    BS   salt-diet  FreeList  Flash  13,351,194   95,483    577.7     4      LANDED      LANDED                  PASS              7/7      0.383      REPAIRED
l7sffs03    BS   salt-diet  FreeList  Flash  20,084,774   126,201   676.7     4      LANDED      LANDED                  PASS              7/7      0.270      REPAIRED
l7sfrs01    BS   salt-diet  LRU       Flash  11,378,956   92,196    922.6     4      LANDED      LANDED                  PASS              16/16    0.344      REPAIRED
l7sfrs02    BS   salt-diet  LRU       Flash  26,417,079   125,981   841.0     4      LANDED      LANDED                  PASS              16/16    0.188      REPLACED
l7sfrs03    BS   salt-diet  LRU       Flash  16,299,438   133,012   816.3     4      LANDED      LANDED                  PASS              16/16    0.231      REPAIRED
l7sfzs01    BS   salt-diet  LZW       Flash  13,256,712   100,662   807.2     3      LANDED      LANDED                  PASS              8/8      0.459      REPAIRED
l7sfzs02    BS   salt-diet  LZW       Flash  19,555,122   165,682   864.5     4      LANDED      LANDED                  PASS              8/8      0.193      REPLACED
l7sfzs03    BS   salt-diet  LZW       Flash  12,230,282   93,661    665.5     4      LANDED      LANDED                  PASS              8/8      0.433      REPAIRED
l7spfb01    BS   salt-diet  FreeList  Pro    8,246,368    71,265    891.7     4      LANDED      LANDED                  FAIL              6/7      0.580      REPAIRED
l7spfb02    BS   salt-diet  FreeList  Pro    29,441,260   172,190   2458.4    5      LANDED      LANDED                  PASS              7/7      0.693      REPAIRED   TRUNCATED
l7spfwa201  BS   salt-diet  FreeList  Pro    14,174,074   57,347    2900.5    5      LANDED      LANDED                  FAIL              6/7      0.287      REPAIRED
l7sprs01    BS   salt-diet  LRU       Pro    12,346,374   72,997    1540.8    4      LANDED      LANDED                  PASS              16/16    0.318      REPAIRED
l7sprs02    BS   salt-diet  LRU       Pro    13,573,895   68,655    1994.2    4      LANDED      LANDED                  PASS              16/16    0.126      REPLACED   TRUNCATED
l7sprs03    BS   salt-diet  LRU       Pro    28,284,577   104,126   2003.8    4      LANDED      LANDED                  FAIL              10/16    0.309      REPAIRED   TRUNCATED
l7spzs01    BS   salt-diet  LZW       Pro    18,030,505   129,851   8224.3    7      LANDED      LANDED                  PASS              8/8      0.107      REPLACED
l7spzs02    BS   salt-diet  LZW       Pro    10,072,157   106,629   3080.1    5      LANDED      LANDED                  PASS              8/8      0.348      REPAIRED
l7spzs03    BS   salt-diet  LZW       Pro    19,782,278   98,747    4375.1    5      LANDED      LANDED                  PASS              8/8      0.279      REPAIRED   TRUNCATED
l7cfss02    C    salt-diet  Crc32     -      NO-METER     -         ?         ?      UNREAD      NOT-ENDED               INCOMPLETE        -        1.000      UNTOUCHED  SCAN-UNMEASURED
l7cfss03    C    salt-diet  Crc32     -      NO-METER     -         ?         ?      UNREAD      NOT-ENDED               INCOMPLETE        -        1.000      UNTOUCHED  SCAN-UNMEASURED
l7cfbs01    C    salt-diet  Crc32     Flash  8,580,379    57,362    356.6     4      LANDED      LANDED                  PASS              6/6      0.372      REPAIRED
l7cfbs02    C    salt-diet  Crc32     Flash  9,683,589    65,511    408.1     4      LANDED      LANDED                  PASS              6/6      0.332      REPAIRED
l7cfbs03    C    salt-diet  Crc32     Flash  13,871,972   99,176    2095.7    4      LANDED      LANDED                  PASS              6/6      0.252      REPAIRED
l7cfss01    C    salt-diet  Crc32     Flash  13,141,849   89,524    494.3     4      LANDED      LANDED                  PASS              6/6      0.235      REPAIRED
l7cpbs01    C    salt-diet  Crc32     Pro    11,391,627   68,719    1296.9    3      LANDED      LANDED                  PASS              6/6      0.236      REPAIRED
l7cpbs02    C    salt-diet  Crc32     Pro    7,486,137    45,094    1020.5    4      LANDED      LANDED                  PASS              6/6      0.236      REPAIRED
l7cpbs03    C    salt-diet  Crc32     Pro    9,956,601    71,162    3723.5    3      NO-FIRST-RESULT  ARM-NOT-RECEIVED        NOT-SCORED        -        0.289      REPAIRED
l7cpssa201  C    salt-diet  Crc32     Pro    7,893,713    62,805    1084.1    4      LANDED      LANDED                  PASS              6/6      0.246      REPAIRED
l7cpssa202  C    salt-diet  Crc32     Pro    9,538,114    99,975    1197.0    3      LANDED      LANDED                  PASS              6/6      0.224      REPAIRED
l7cpssa203  C    salt-diet  Crc32     Pro    2,619,898    24,601    883.0     3      LANDED      LANDED                  PASS              6/6      0.238      REPAIRED
```

---
# §5 · WHAT THE STATEMENT AXIS DID, AND WHAT THIS LEVEL REFUSES TO SAY ABOUT IT

§K6 rule 12: **the registered reading is ARM WITHIN CONDITION.** A statement-versus-bare comparison across
conditions is **not** registered, and §K3 item 2 travels with it if anyone ever makes one. So:
- **Within BS (brownfield × statement), arm within condition:** Flash 9/9 plain and 9/9 salt-diet — a
  ceiling. Pro 8/9 plain and 6/9 salt-diet, with **five of Pro's nine salt-diet BS cells carrying a
  TRUNCATED or SELF-NOT flag** ⇒ §1's confound, unchanged.
- **§K3's pre-registered answer stands untouched by the data:** the localisation measurement was made
  read-only at `eacb9ec` before the freeze and no cell in this wave can revise it. Nothing here is
  voided or excluded on statement-as-tell grounds (§K3 item 1).
- ⛔ **§K8 item 6 holds: whether any subject USED the statement is UNMEASURED and this result claims
  nothing about it.**

⛔⛔ **AND ONE REGISTERED READING HAS NO INSTRUMENT ON THIS LANE — DECLARED HERE RATHER THAN DISCOVERED BY
A READER.** §K6 **rule 13** says *"FIND-THE-DEFECT IS REPORTED PER CELL as `bugs_fixed` from the end tree
against the registered planted defect — and it is a claim level 7 CAN make for FreeList and LZW, which
level 4 could not."* **`bugs_fixed` does not exist on the agy lane.** Driven three ways:
```
  (a) grep -rl bugs_fixed over the frozen harness 9bfb6ef  ->  score_claude_v3.py  ONLY (the CLAUDE scorer)
  (b) score_wave_v3.sh's own header: it runs the RECEIPT GATE then THE WITHHELD SUITE; no bug column
  (c) zero occurrences of "bug" in any l7 score file, against a positive control of TESTS = 4 per file
```
⇒ **`bugs_fixed` IS UNMEASURED FOR ALL 84 CELLS.** What §4 reports in its place is `tests n/m` against the
withheld suite, and **that is a different claim**: the suite is what the planted defect breaks, so a FULL
PASS is strong evidence the defect was repaired — but a suite pass does not identify *which* defect was
repaired, and a cell could in principle repair the planted defect and still fail another test.
⚠️ **This is the author's own freeze asking for a field the author's own lane cannot produce.** It was
registered on 09-16 and nobody — including the two non-author signatures on §K1–§K9 — checked that an
instrument existed. ⇒ 🔑 ***A READING RULE IS A CLAIM THAT AN INSTRUMENT EXISTS, AND IT IS THE ONE CLAUSE
IN A FREEZE THAT NOBODY DRIVES, BECAUSE IT READS AS A DESCRIPTION OF WHAT WILL BE DONE RATHER THAN AS A
DEPENDENCY.*** **No repair here:** building a bug-localiser for the agy lane changes what a run measures.

---
# §6 · CAPS, TRUNCATION AND REWRITE CLASS, SPLIT BY ARM (§K4)

**DECLARED CAPS, identical on all 28 conditions** (`caps-lines.tsv`, all seven legs): per-turn 1800 s ·
controller patience 2100 s · wall 21600 s · turns 40. **No cell exceeded the wall cap or the turn cap.**
```
                 n     TRUNCATED   SELF-NOT   PERSIST-INDET   false_done>0   all of them Pro?
  plain         42         0           0            0              0          -
  salt-diet     42         6           3            2              4          YES, 10 of 10
```
⛔ **§K4's own registered sentence — "a cap that binds one arm is a treatment" — is satisfied exactly:
6 : 0.** Level 4 measured 5 of 12 salt-diet and 0 of 12 plain; level 6 measured 1 and 0. **Three waves,
three levels, same sign, never once the other way.**

**REWRITE CLASS** (`retention.txt`, threshold 0.20 registered pre-data, `AMENDMENT-brownfield-2026-09-13`
§B5), over the 82 cells that ran:
```
  plain       REPAIRED 41   UNTOUCHED 1   REPLACED 0
  salt-diet   REPAIRED 36   UNTOUCHED 0   REPLACED 4
```
- **All four REPLACED are salt-diet** (`l7sfrs02` 0.188 · `l7sfzs02` 0.193 · `l7sprs02` 0.126 ·
  `l7spzs01` 0.107) and **all four scored PASS** — a cell can rewrite nearly the whole seed tree and still
  satisfy the withheld suite.
- **The one plain UNTOUCHED is `l7spfp03`, retained 1.000, and it FAILED 6/7.** The subject changed
  nothing and the suite caught it. ⭐ **That is the negative control this level did not have to construct:
  an untouched seed fails, so a passing cell is not passing on the seed's own merits.**
- ⚠️ **`l7cfss02`/`l7cfss03` read `UNTOUCHED` / retained 1.000 in `retention.txt`. THEY ARE NOT UNTOUCHED —
  THEY NEVER RAN** (§2), and the file's own note says to "re-read these after they land", which will not
  happen. **They are excluded from every figure in this section and from §1's retention table.**

---
# §7 · TOKENS (council 2026-09-17 ⑯: tokens are the price of record, by direction)

⛔ **NINE CELLS ARE OUT OF THE COST POOL, EACH FOR A DECLARED REASON:** six TRUNCATED (`l7npzs01`
`l7npzs03` `l7spfb02` `l7sprs02` `l7sprs03` `l7spzs03` — the helm's 2026-09-11 ruling: PASS/FAIL stands as
a floor, token/turn/wall figures are NOT POOLABLE), one NOT-SCORED (`l7cpbs03`, arm never delivered), and
two with no meter at all (`l7cfss02` `l7cfss03`, §2). **Poolable n = 42 plain, 33 salt-diet.**
```
                     median T        median output      median wall_s      range of T
  plain              3,229,680           37,620             259.9          722,895 - 8,522,338
  salt-diet         13,871,972          100,662             966.2        2,619,898 - 34,073,898
  ───────────────────────────────────────────────────────────────────────────────────────────
  salt-diet / plain     4.295x            2.676x            3.717x
  cache-read share    88.8 % of plain's total T       91.8 % of salt-diet's
```
⇒ **The premium is far larger in TOTAL tokens than in OUTPUT (4.30x vs 2.68x), so it is predominantly a
CONTEXT cost rather than a generation cost** — the third independent measurement of that shape on this
campaign, after level 6 (3.99x / 2.11x) and the Claude lane's HC1 (2.168x / 1.324x). **Three lanes, two
vendors, same direction, same decomposition.**
⚠️ **A median over n = 33–42 with one arm spanning 2.6M–34.1M is a description of this wave, not an
estimate of a population.** No interval is claimed.
✅ **ROBUST TO THE EXCLUSION DECISION, which is the first thing a sceptic asks.** Over **every cell with a
meter** (42 plain, 40 salt-diet — no exclusions at all): plain median **3,229,680**, salt-diet median
**14,662,269**, ratio **4.540x**. **The plain median is bit-for-bit unchanged** (no plain cell was
excluded) and the salt-diet ratio moves *up*, because the excluded cells were truncated — i.e. **the
exclusions I made are the conservative ones, and nothing in §7 turns on them.**
⛔ **NO USD.** §K6 carries level 4 §L5 rule 7 unchanged, and the agy lane is a subscription lane: the only
price receipts are the `/usage` rows the hand logged (`usage-log.txt`, 4 rows in BN-pro, one per condition
at dispatch; `usage-at-dispatch.*` at the run root).

---
# §8 · FOUR THINGS THIS RESULT DECLARES RATHER THAN RESOLVES

1. ⛔ **THE UNDER-RUN AND ITS CAUSE (§2, §2b).** Repair belongs in a dated amendment before the next wave
   fires, not here. Three one-line detectors are driven above and cost nothing to adopt.
2. ⛔ **`bugs_fixed` HAS NO INSTRUMENT ON THIS LANE (§5).** §K6 rule 13 is unmet for all 84 cells.
3. ⚠️ **THE LEVEL-7 DRIVERS WERE NOT IN THE EXEC REGISTRY.** Every driver log carries
   `⚠️ NO exec-registry at /nonexistent — run … is NOT registered with the fleet` at START **and again at
   END**. The runs completed and nothing was lost; the fleet's own liveness law had no row for the largest
   executor on the box. Reported to the hand and to `systems`; **not this result's to fix.**
4. ⚠️ **`flags.tsv` WRITES `served=` WITH AN EMPTY VALUE FOR A CELL THAT NEVER RAN** — every other field on
   the row is present and correct. A consumer splitting on `=` gets an empty string rather than a refusal.
   Stated because §K7 row 1 is a model-identity check and this is the one shape in which it reads blank
   rather than mismatched.

---
# §9 · PROVENANCE
```
  chain ends     ~/.fleet/executors/gemini.runs/l7u-2026-09-18/END-MARKER-A
                   rc=0 2026-09-18T18:14:19Z TRIPWIRE-HOLD (mode A: BN + the BS tripwire cell)
                 ~/.fleet/executors/gemini.runs/l7u-2026-09-18/END-MARKER-B
                   rc=0 2026-09-19T21:19:06Z CHAIN-DONE mode B (BS-pro · BS-flash · C-pro · C-flash)
  export         EXPORT.sha  9bfb6ef86a363cd9427ddc7298a6be97e98cc51e   ONE sha, all 84 cells,
                 asserted per condition in every driver log ("drive EXPORT … sha 9bfb6ef86a36…")
  harvests       …/l7u-2026-09-18/harvest-{BN-pro,BN-flash,BS-pro,BS-flash,BS-trip,C-pro,C-flash}/
                   cells.tsv · conditions.tsv · score-manifest.tsv · caps-lines.tsv · token-scan.tsv
                   · retention.txt · given-check.tsv · flags.tsv · end-markers.tsv · fault-cells.tsv
  score files    …/l7u-{leg}-2026-09-18-score/*.p1.score.txt, each first line naming the scorer tree
                 and tasks tree at 9bfb6ef86a36 and the §H6 fault rows applied (8,9,10)
  per-cell T     ctl/agy-meter-*.json inside each cell, read READ-ONLY over ssh on the run box;
                 no cell was written to. 82 of 84 carry exactly one file / one conversation.
  cells on box   ~/cells-l7-<condition>/<cellid>  on the run box
  BS release     …/l7u-2026-09-18/BS-RELEASED, citing the lead's release line at bus 60,093,803
  the refusal    …/l7u-C-flash-2026-09-18-c4a1/cells-l7-crc32-flash-salt-stmt-bf.fire.log
                 …/l7u-C-flash-2026-09-18/{c4-a1.driver.out,ledger.tsv,END-MARKER}
```
⛔ **THE per-cell T IS THE ONE FIGURE THAT WAS NOT IN THE HARVEST AND IS NOT A RE-DERIVATION.** §K9 names
`T` in the table the hand delivers; the seven harvests carry no token column. The meters had already been
written per cell **at cell time**, so this is a read of a frozen artifact, not a re-measurement: nothing
was re-run and no number here depends on the state of the run box today except the cells' own `ctl/`.
⚠️ **AND IT MEANS THE HAND'S §K9 DELIVERY WAS INCOMPLETE IN TWO COLUMNS — `T` (recovered here) and
`bugs_fixed` (not recoverable, §5).** Said plainly because the alternative is a table that silently
supplies one and silently drops the other.

## §9b · THE RECEIPT FOR THIS DOCUMENT'S OWN NUMBERS (idiom law, clause 1)
**`RESULT-gemini-level7-2026-09-19-verify.py`, committed beside this file**, re-derives every headline
figure from the receipts and the cell TSV and asserts it against **the bytes of this document and of the
census**: population, the four pass quadrants, scorable, FULL PASS, the ten flagged cells and their ids,
the poolable n's, both medians, all three ratios, the four §K7 zero-columns, the card_extras split, the
census `LIVE` row's sum, the 240-view's sum, and that the two census views agree on `DONE` — **and, since
`systems`' signature, all eight RETENTION bands, the 7-of-8 direction, the DISJOINT count and the named
exception. 39 verdict lines, 0 typed expectations, `FAILS: NONE`.**
⛔ **THREE OF THOSE ARMS EXIST BECAUSE THE SIGNER FOUND THEM MISSING, AND TWO OF THE ORIGINAL 27 WERE
VACUOUS.** `systems` drove, rather than read, that `check(name, derived, needle)` tests `needle in doc` and
nothing else — so where the needle was a **hard-typed literal** the derived value was computed, printed
where a reader sees it, and **never compared**: with the score-file glob pointed at a directory that does
not exist, `declared derived=0 needle='84 cells'` printed **OK**. ⇒ 🔑 ***AN ARM THAT PRINTS A DERIVED
NUMBER BESIDE A TYPED NEEDLE READS AS A MEASUREMENT AND IS A TYPED EXPECTATION*** — the idiom law's clause 1
failing inside the tool written to enforce it. Both needles are now computed (`'%d cells' % len(rows)`).
⛔ **AND RETENTION — the registered primary separator and this result's ⭐ headline — WAS TOUCHED BY ZERO OF
THE 27 ARMS** (`"retain"` occurred 0 times in the verifier, against a live control that `retained` is a TSV
column). **27 green lines sat directly above a claim none of them tested, and a reader carries the green
forward.** That is the most dangerous shape a verified document can have, and it was invisible from inside. *(That count is read from the tool's own output — the first
draft of this sentence said "24 arms", typed, and it is 27. The third typed number in one document, and
the third one this section's own discipline caught.)*
⭐ **IT CAUGHT TWO THINGS BEFORE THIS FILE WAS COMMITTED, AND THE SECOND ONE WAS IN ITSELF:**
- **In the document:** §1's Flash-plain cell read `24 / 24`. Derived, it is `21 / 21` (21 Flash-plain
  cells, not 24). I had typed it from "42 plain, two models". **Clause 1 fired on its own author.**
- ⛔ **In the verifier:** the 240-view check used `re.search` and matched **ADDENDUM 9's** line
  (`72+112+0+56 = 240`), printing `OK` about a figure this addendum never wrote. Right tool, right
  pattern, **wrong object** — and every other arm agreed with it, because none of them was wrong.
  ⇒ 🔑 ***A CHECK THAT TAKES THE FIRST MATCH IN AN APPEND-ONLY DOCUMENT VERIFIES THE OLDEST CLAIM THAT
  FITS ITS PATTERN, AND AN APPEND-ONLY DOCUMENT IS EXACTLY WHERE YOU PUT A CHECK.*** Now it takes the
  LAST, asserts the population is ≥ 2, and cross-checks the two views against each other.
✅ **THE THREE REPAIRS ARE DRIVEN BACKWARDS TOO, AND THE DECISIVE MUTANT IS THE SIGNER'S OWN:**
```
  M-a  systems' defect RESTORED: the excluded cell put back in its band   RED band Pro Crc32
  M-b  one cell's retained flipped in the TSV (0.126 -> 0.826)            RED band Pro LRU
  M-c  systems' OWN mutant: one table row deleted                         RED cells  (+10 neighbours)
       ⇒ it printed `OK cells derived=83 needle='84 cells'` FOR systems AN HOUR AGO.
         It now reads `RED cells derived=83 needle='83 cells'`. THE VACUITY IS CLOSED, AND THE
         PROOF IS THE SIGNER'S OWN MUTANT FLIPPING DIRECTION.
```
**Both files `cmp` byte-identical to their pre-mutation state afterwards; control green.**
⇒ 🔑 ***EVERY ONE OF THESE ARMS EXISTS BECAUSE SOMEONE WHO DID NOT WRITE THE DOCUMENT DROVE IT. I PROVED MY
SUITE BACKWARDS AND IT WAS STILL VACUOUS IN TWO ARMS AND SILENT ON ITS OWN HEADLINE*** — a fourth-pair-of-eyes
result in the idiom law's clause 4 sense, and the arm count (27) was exactly the number that said otherwise.

✅ **AND THE ORIGINAL THREE, from before the signature:** three
mutants — the original `24/24` typo restored, the census `DONE 99 → 98`, and one digit of the salt median —
each reddened exactly the arms that name it, and **mutant 2 was caught by the cross-check rather than by
the sum** (`240-view DONE (99) == LIVE-row DONE (98)` RED). Both files `cmp` byte-identical to their
pre-mutation state afterwards, control green.

📌 **`ctl/` READ CENSUS (§K5.4):** carried as a registered confound, **NOT measured in this result.** The
level-6 package's per-cell `ctl/` read census is not among the seven harvests' receipts and I did not
re-derive it from the transcripts. **No delivery claim is made from P-DELIVERY alone (§K5.5), and none is
made here at all.** It is owed, it is named, and it changes no figure above.

---
## ✍️ NON-AUTHOR SIGNATURE — OWED
**This result is UNSIGNED.** Per council 2026-09-17 item 9(2) the signature ask is PINNED (file, blob,
head) and posted to the bus by the author. Nothing in this file may be quoted as signed until a
non-author section appears below this line.

---
# ⚠️⚠️ ERRATUM 1 — **§8 ITEM 3 IS REFUTED. THE LEVEL-7 WAVES WERE REGISTERED, 7 OF 7.** APPENDED BELOW THE SIGNED TEXT; §1–§9b untouched.
*bench (lead), 2026-09-19, on `systems`' measurement at the object, closing an item I routed to it.*

**§8(3) SAYS:** *"THE LEVEL-7 DRIVERS WERE NOT IN THE EXEC REGISTRY … the fleet's own liveness law had no row for the largest executor on the box."*
```
  the first sentence   TRUE   — every driver log does carry `NO exec-registry at /nonexistent`
  the second           FALSE  — refuted at the object
```
⛔ **MEASURED BY `systems`:** the gemini seat holds **74 registry files** (control: 400 across all seats), and **all seven level-7 WAVE rows are present** — `l7u-{BN-flash,BN-pro,BS-flash,BS-pro,BS-trip,C-flash,C-pro}` — each with shape, liveness, pid, box, log, landing, harvester **and `marker=`**, plus rows for both chains, three preflights and every score run. ⭐ **And gemini's own completion post is the other half of the proof: *"registry CLEAR (72 rows, none live or died)"* after nine retires — a row that CLEARS is a row that was written and ended.**
✅ **THE `/nonexistent` IS A DESIGN, AT ONE DELIBERATE LINE** (`gemini_canary_wave_v1.sh:289`): **the SUPERVISOR registers itself and de-registers at the end, and tells each per-condition driver child not to write its own.** That is the right shape — the registry law wants the LONG-RUNNING executor registered, **the wave IS that executor**, and N children writing N rows would bury the thing the registry exists to show.

## ⇒ 🔑 WHAT WAS ACTUALLY WRONG, AND IT IS THE FOURTH INSTANCE OF ONE SHAPE IN ONE AFTERNOON
The child prints *"this executor is NOT registered with the fleet (set EXEC_REGISTRY, or link `~/.fleet/bin/exec-registry.sh` on this box)"*.
***TRUE OF THE CHILD. FALSE OF THE WAVE. AND IT NAMES TWO REMEDIES FOR A CONDITION THAT IS NOT A PROBLEM*** — so a reader who acts on it either sets an env var that defeats the design or hunts a link that is present. **I read it, believed it, and routed it.**
⛔ **THE FAMILY, because three of these landed on this document alone and calling them coincidences would be the mistake:**
```
  a CI check named after one of its many steps          the NAME is a hypothesis about the failure
  comparator-rows' refusal naming COMPARATOR_EXPORT     a value NOBODY passed  (ADDENDUM 5 erratum)
  retention.txt's "re-read these after they land"       for two cells that will NEVER land  (§2)
  "this executor is NOT registered with the fleet"      true of the child, false of the wave
```
⇒ ***AN ACCURATE SENTENCE ABOUT THE WRONG SUBJECT IS THE HARDEST DIAGNOSTIC TO DOUBT, BECAUSE EVERY WORD OF IT CHECKS OUT.*** It is the mirror of this fleet's *"the most dangerous green is the one that names its own scope accurately"*, and **the subject is the axis no re-measurement crosses.**
📌 **WHAT §8(3) SHOULD HAVE SAID, and is the only live remainder:** *a per-condition driver child prints a registration warning that is true of itself and false of the wave that registered it, and the message should name the wave's row rather than two remedies.* **That is `systems`' to take or decline; it is a message, not a registration.**
⚠️ **AND `systems` REPORTED CATCHING A FALSE `ABSENT` OF ITS OWN ON THE WAY — from a `|| echo` firing on `sed`'s rc — the exact trap it had quoted at me an hour earlier.** Recorded because a correction that hides its own near-miss is worth less than one that shows it.

---
# ⚠️⚠️ ERRATUM 2 — **§1's RETENTION SEPARATION IS A *GROWTH* SEPARATION. THE NUMBERS ARE RIGHT; WHAT THEY MEASURE IS NOT WHAT §B5's WORDS DESCRIBE.** APPENDED BELOW THE SIGNED TEXT; §1–§9b, ERRATUM 1 and every signature untouched.
*bench (SaltBench lead), 2026-09-21. **This is the landing of desk `TQ`, and it is a REPORTING change, not a registration amendment** — the Captain's word, verbatim, at council 2026-09-21 (minute the 2026-09-21 council minute, §3): **"yes reporting change"**. `retained` remains the registered pre-data separator of `AMENDMENT-brownfield-2026-09-13.md` §B5, unamended; `surv` and `growth` are reported BESIDE it, POST-HOC.*

### E2.1 · WHAT §1 SAYS, AND WHAT IS WRONG WITH IT
§1 reports ***"THE SEPARATOR THAT DOES MOVE IS RETENTION, AND IT MOVES IN THE SAME DIRECTION IN 7 OF 8 (model × problem) PAIRS"***.
⛔ **THE ARITHMETIC IS NOT AT ISSUE AND IS NOT WITHDRAWN.** Every `retained` value reproduces — the decomposition's pipeline imported the level-7 export's OWN classifier (`brownfield_rewrite_class.py` at `9bfb6ef86a36`) and asserted all 84 against it, 0 refusals, and it reproduced the published headline at 7 of 8 and the Flash × LZW exception **before** decomposing anything.
⛔ **WHAT IS WRONG IS THE READING.** `retained` is difflib's similarity ratio of the end file against the seed, **symmetric in additions and deletions**, so it cannot distinguish *"the seed was rewritten"* from *"the seed was kept and something large was written beside it."*

### E2.2 · THE DECOMPOSITION — SAME PAIRS, SAME POPULATION, SAME DIFFER
```
                 RETAINED (published)      SURVIVAL (what §B5's words describe)     GROWTH
  RESULT         salt below plain 7 of 8   salt below plain 3 of 8                  disjoint on 8 of 8
  DISAGREEMENT   the two differ in DIRECTION on 4 of 8 pairs — HALF THE TABLE
  ALL 84 CELLS   retained  plain 0.719  salt 0.316      <- the published direction
                 surv      plain 0.715  salt 0.860      <- INVERTED
                 growth    plain 1.04x  salt 3.85x
```
⇒ 🔑 ***ON THE QUANTITY §B5's WORDS DESCRIBE, THE SALT-DIET ARM KEPT **MORE** OF THE GIVEN THAN PLAIN DID.*** The 7-of-8 separation is real and it is a **growth** separation.
⭐ **AND THE MEASUREMENT'S OWN ERROR DIRECTION RUNS AGAINST THIS FINDING, WHICH IS WHY IT CAN BE BELIEVED:** `surv` counts lines the differ MATCHED, so it is a **LOWER bound** on survival — a moved line may fail to match. **Under-counting matched lines makes salt's survival look LOWER, not higher.** The inversion survives a bias pointed the other way.

### E2.3 · WHAT THIS ERRATUM DOES **NOT** DO
1. **No number in §1–§9b changes, and no arm claim is made or withdrawn.** Level 7 makes no pass-rate claim; this erratum makes none.
2. **§B5's registered threshold is untouched** — `retained < 0.20 → REPLACED`, fixed before the data, and it stays fixed. Changing what a registered pre-data separator MEANS is the Captain's, and he has ruled this a reporting change instead.
3. **The MECHANISM is not measured on this lane.** Block SB hypothesises a proof-method file as the source of the growth from two method files' headings; **no such reading was taken for level 7's cells**, and none is asserted here.
4. **It does not re-open ERRATUM 1**, which is about §8 item 3 and is unrelated.
📌 **FULL RECEIPT:** `MEASUREMENT-l7-retention-decomposition-2026-09-19.md` (84 rows, `l7-retention-decomp.tsv`), whose §2 is the reproduction control and whose §3 is the table above. **It is the SECOND lane with this signature**, measured independently of block SB and reproducing its published figure first.
