# RESULT — P1, THE GEMINI PRO 3.1 GREENFIELD WAVE
## bench (SaltBench lead), 2026-09-13. Run by the `gemini` seat as the HAND; scored by it; **authored here.**
## ⛔ NO ARM COMPARISON IS PUBLISHED IN THIS FILE, AND §4 IS THE REASON.

**PROVENANCE — every number below was read by me from a named file and none was retyped from a message**
(this repo's CLAUDE.md). Source: `~/.fleet/executors/gemini.runs/p1-greenfield-score-2026-09-13/`, one
`<condition>.score.txt` per condition, each carrying `score_wave_v3.sh`'s own per-cell table and summary
line, unedited. I re-derived every total from those files rather than accepting the hand's summary; the
two agree. `crc32-plain-v2` is a separate 3-cell re-run and is **excluded from every count below.**

---

## 1 · THE POPULATION AND THE GATE
```
  45 cell directories censused   41 SCORED · 4 VOID(NO-RECEIPT)
  the 4 VOID are cell-for-cell the 4 that never fired — the receipt reader and the meter agree independently
  model served: 41 x gemini-3.1-pro-high · ZERO substitution · 4 never fired
  built from export s2g 156fcb93 — RECORDED, because comparability names a REFERENCE, not a date
```

## 2 · PER CONDITION — FULL PASS of SCORABLE, and the per-cell test counts beside it
```
  crc32-plain          3 of 3    6/6 6/6 6/6        crc32-saltdiet          3 of 3    6/6 6/6 6/6
  crc32-plain-stmt     3 of 3    6/6 6/6 6/6        crc32-saltdiet-stmt     2 of 2    6/6 6/6
  lru-plain            3 of 3    16/16 x3           lru-saltdiet            3 of 3    16/16 x3
  lru-plain-stmt       3 of 3    16/16 x3           lru-saltdiet-stmt       3 of 3    16/16 x3
  freelist-plain       1 of 1    7/7                freelist-saltdiet       0 of 3    0/7 3/7 6/7
  freelist-plain-stmt  2 of 2    7/7 7/7            freelist-saltdiet-stmt  1 of 1    7/7
  paxos-plain          1 of 3    16/17 16/17 17/17  paxos-saltdiet          0 of 1    9/17
```
⭐ **THE PER-CELL COUNTS ARE THE HONEST SHAPE AND THE FULL-PASS COLUMN HIDES THEM.** `freelist-saltdiet`
is **0/7 · 3/7 · 6/7** — three cells failing by three different margins, not a uniform failure. And
`paxos-plain`, the CONTROL, misses that problem's last test **twice** (16/17 · 16/17 · 17/17) — a "1 of 3"
that is nothing like a collapse.

## 3 · ⛔ THE TWO ARMS, WITH ATTRITION — WHICH IS THE FINDING, NOT THE PASS RATE
```
  arm         conds  SCORABLE  FULL PASS  LANDED  NOT-LANDED  TRUNCATED
  plain          7        18         16      18           0          0
  salt-diet      7        16         12      15           4          3
```
⇒ 🔑 ***THE CONTROL ARM HAS ZERO ATTRITION OF ANY KIND. THE TREATMENT ARM LOSES CELLS AT THREE SEPARATE
MECHANISMS — 4 never produced a landing, 1 scored without landing, 3 were truncated by the per-turn
deadline — AND ALL THREE ARE DRIVEN BY DURATION.*** Measured wall: salt-diet **3,635–13,700 s** against
plain's **738–798 s**.

## 4 · ⛔⛔ WHY NO PASS-RATE COMPARISON IS PUBLISHED
`16 of 18` against `12 of 16` is arithmetically available and it is **not a comparison**:
1. **THE DENOMINATORS ARE NOT NEUTRAL.** They differ (18 vs 16) and **every missing cell is salt-diet.**
   Per `cbd13ea`, a cell dies at the token refresh **only if it outlives its ~1 h access token** — so the
   missing cells are **not a random sample of the treatment arm, they are its LONGEST cells, removed by a
   harness defect whose incidence IS the property that distinguishes the arms.** A rate over those
   denominators is measured on a treatment arm with its hardest cells deleted.
2. **n IS 1–4 PER CONDITION, NOT 3.** `freelist-plain` contributes **one** scorable cell and
   `paxos-saltdiet` **one** — and FreeList, which carries the largest apparent gap, has the thinnest control.
3. **LANDED AND PASSED ARE DIFFERENT RATES AND THIS WAVE SEPARATES THEM.** `lru-saltdiet/s3ls01` ended
   `PERSIS`, **never landed, and passes 16/16.** ⇒ the same shape class-C node 1 produced — *correct and
   not recorded* — occurring again here. **A FULL-PASS column that mixes landed and non-landed cells is an
   upper bound on a verified rate, never the rate.**
4. **3 TRUNCATED CELLS' PASSES STAND AS A FLOOR** and their cost figures are not poolable (helm ruling
   2026-09-11) — **all 3 are salt-diet.**

## 5 · ⭐ WHAT THE WAVE DOES ESTABLISH: TWO OF FOUR PROBLEMS DISCRIMINATE NOTHING
```
  Crc32   11 of 11 scorable cells pass 6/6      LRU   12 of 12 scorable cells pass 16/16
          across BOTH arms and BOTH briefings          across BOTH arms and BOTH briefings
```
⇒ **Half the pilot's problems separate no arm from any other.** ⚠️ **This is a DIFFERENT MECHANISM from
Crc32's brownfield ceiling** — there the withheld mutants do not separate; here the problem is simply
solved by everything — and it must not be reported as the same fact.
📌 **AND THE SUITE SIZES BELONG BESIDE IT, because a ceiling is a claim about an instrument:** Crc32 is a
**6-test** suite, FreeList **7**, LRU **16**, Paxos **17**. **The two problems at ceiling are not the two
largest suites**, so suite size alone does not explain it — but a 6-test suite is the thinnest instrument
in the set, and *the margin is the finding the rate discards.*

## 6 · WHAT THIS FILE DOES NOT ESTABLISH
- **No premium, no cost table, and no dollar figure.** The lane is a SUBSCRIPTION: `rates.tsv` carries no
  Gemini row, and an agy cell's `ctl/budgets.env` carries an **inert** Claude-derived `C1_USD=37.21`.
  **Quoting "$" of a subscription cell invents a bill nobody was sent.**
- **No method effect.** See §4. Whatever this wave shows about arms, it is not shown by these denominators.
- **Nothing about brownfield.** Those seeds exist and have never run.
