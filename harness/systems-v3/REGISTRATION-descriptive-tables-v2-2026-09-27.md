# REGISTRATION: FOUR DESCRIPTIVE TABLES OVER THE COMPLETE PILOT MATRIX (arXiv v2), DECLARED POST HOC
## bench (SaltBench lead), 2026-09-27, written before any table number is computed. Council 2026-09-27 second sitting (the sitting's minute, in the private record), the Captain's words: *"great, yes to all"*.

⛔ **THIS READING IS POST HOC, AND IT IS DECLARED AS SUCH.** Every one of the 181 DONE conditions already has a result of
record. Some per-condition token figures have appeared in those files (for example the Opus matrix-1 cost tables), and the
lead has read many of them. What is fixed here, before the instrument runs, is the METHOD: which figure each cell
contributes, how a condition's cell is summarised, how the marks are assigned, and how the ratios and sign counts are
formed. Nothing below is chosen after seeing the tables it produces.

⛔ **IT IS DESCRIPTIVE. There is no test, no p-value and no verdict on the arms.** The registered tests remain §4's (one
model, one task form, metered dollars, one-sided sign test). A p-value across the other models would be the post-hoc test
the paper's discipline refuses, so none is computed (the Captain's ruling, minute §1).

## §D1 · THE POPULATION: THE 200 CONDITIONS OF THE CENSUS OF RECORD
`CENSUS-full-matrix-2026-09-14.md` at ADDENDUM 24 (saltbench `3aebf116`): **DONE 181 · OWED 0 · BLOCKED 0 · INEXPR 16 ·
DECLARED 3 = 200**. 4 models × 5 problems × {greenfield, brownfield} × {plain, salt-diet} × {none, statement, spec-change},
minus brownfield × spec-change (40, which left the denominator on 2026-09-14). Each condition's cells are the cells its
result of record names, including pooled cells where the record pools them. **No cell is added, dropped or re-fired for
this reading.**

## §D2 · THE CELL FIGURE: TOTAL TOKENS, AS THE LANE'S OWN METER RECORDS IT
- One figure per cell: the total-tokens column (`T`) of the TRACKED per-cell record the condition's result of record cites
  or carries. Output tokens are read from the same row where the record carries them.
- **The composition of `T` is the lane's, not this reading's.** The Claude lane meters the session transcript, and there
  T is input + cache writes + cache reads + output. The agy lane records the vendor's reported tokens. The result file
  prints each source's own definition beside its figures, quoted from the source rather than restated.
- ⇒ **A table row compares arms within ONE model and ONE problem, where the definition is shared.** Figures in different
  rows of the same column are not like-for-like across lanes, and the captions say so.
- ⛔ **NO FIGURE IS HAND-RECOVERED.** A DONE cell with no tracked per-cell token figure prints `unmeasured`, its condition
  prints `unmeasured`, and the 181 check below FAILS VISIBLY. It is never filled from a message, a bus post, a transcript
  read by hand, or a figure retyped from memory. §4 stopped printing medians for exactly this reason.

## §D3 · THE CONDITION CELL: THE MEDIAN OVER ITS CELLS OF RECORD
- The median of the condition's cells of record (n = 3 at the census; where a record pools more than 3, all of them, and n
  is printed beside the median in the result file).
- **The lower-bound mark `≥`.** A cell that ended at the cost cap (CAP-COST, as its record classifies it) contributes its
  recorded figure as a LOWER BOUND. Sort the condition's recorded figures ascending. The median is marked `≥` if ANY
  lower-bound cell sits at or below the median position; on a tie, `≥` is applied. Otherwise it is exact, because raising
  a value above the median cannot move the median.
- `—` : the 16 INEXPRESSIBLE conditions (Paxos × statement, both task forms, all four models, both arms; the reason is in
  `RESULT-statement-arm-2026-09-09.md`: an arm-neutral formal statement cannot exist for a proof-obligation task).
- `declared` : the 3 DECLARED conditions (census ADDENDUM 19: unreached at the cap). No median is printed for them in the
  tables. Their cells' figures are printed in the result file with the DECLARED label.

## §D4 · THE FOUR TABLES (the Captain's design, minute §1)
```
  T1  greenfield    20 rows (model × problem) × {bare-plain, bare-salt-diet, statement-plain, statement-salt-diet}   80
  T2  brownfield    the same 20 rows × the same 4 columns                                                          80
  T3  spec-change   greenfield only; 20 rows × {plain, salt-diet}                                                  40
      ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
      CHECK  numbers + "—" + "declared" = 181 + 16 + 3 = 200, or a cell is wrong and the instrument exits non-zero.
  T4  ratios        20 rows × {bare, statement, spec-change}, each = salt-diet median ÷ plain median, same row.
```
- **T4's task form is GREENFIELD**, the one form all three treatments share (spec-change exists only there). The brownfield
  bare and statement ratios are computed by the same rule and printed in the result file, not in T4. *This is the lead's
  reading of "20 rows × 3 ratios"; it is stated so it can be reversed with one word, not reverse-engineered.*
- **Ratio marks.** A `≥` numerator makes the ratio `≥`. A `≥` denominator makes it `≤`. Both bounded makes it `bounds
  only`, and it is printed but not signed. Either side `—`, `declared` or `unmeasured` gives no ratio.
- **The sign count, per model per treatment:** `k of m ratios > 1`, where m counts that model's five problems with a
  ratio. A `≥ x` ratio with x > 1 counts as > 1. A `≤ x` ratio with x ≤ 1 counts as not > 1. Any other bounded ratio is
  INDETERMINATE for the sign: it is named and counted in neither k nor m − k. The median of the model's ratios is printed
  beside the count, together with how many of them are bounded.
- **Output tokens** go in the result file (per cell, and the per-condition median by the same rule), not in the tables.

## §D5 · THE INSTRUMENT AND THE FILE OF RECORD
- ONE instrument run, ONE result file, ONE sha. The instrument reads a tracked condition map (200 rows: condition →
  record → cell ids → the tracked source of each cell's figure) and the tracked sources it names, and prints T1–T4, the
  output-token medians, and the check to `RESULT-descriptive-tables-v2-2026-09-27.md`. Every table cell there cites its
  source rows.
- The condition map and the instrument land in the SAME COMMIT as the result, so every number is reproducible from
  recorded shas.
- **Captions (minute §1):** *a descriptive reading over the complete matrix; no test, no verdict on the arms; the
  registered tests remain §4's.* Each caption also states that `T` differs between lanes (§D2), and what `≥`, `—` and
  `declared` mean.

## §D6 · WHAT THIS READING CANNOT ESTABLISH, SAID BEFORE ANY NUMBER
- It cannot say the salt method helps or hurts, in tokens or otherwise. A token ratio is a cost description, not a
  quality comparison.
- A `≥` median is a floor set by the uniform dollar cap. The cap binds the salt-diet arm more often (census §T3, §U2, §V3),
  so every `≥` is an arm-correlated censoring. A capped salt-diet numerator makes its ratio an UNDERSTATEMENT: the true
  ratio is at least the printed one.
- n = 3 per condition. A median of three is one cell's figure.

---

## ⚖️ ADDENDUM 1 — FOUR DEFINITIONS THE SOURCES REQUIRE, FIXED BEFORE THE RUN. APPENDED; §D1–§D6 untouched.
The coverage census of the tracked per-cell sources, taken before any median was computed, found four questions §D2–§D3
did not answer. Each is fixed here, still before the instrument runs.
- **A1.1 · A spec-change cell's figure is the SUM of its phases.** Spec-change cells are metered per phase (phase 1, the
  greenfield landing, and phase 2, the change). The cell's total tokens is phase 1 + phase 2, each read from its own
  tracked source. A cell missing either phase is `unmeasured`.
- **A1.2 · A figure is a lower bound for any of three recorded reasons, not only the cap.** The first is CAP-COST: the
  cell ended at the cost cap. The second is FLOOR: the meter itself records the figure as an under-read (the all-roots
  table's status column). The third is DEADLINE: a registered turn or wall deadline cut the cell off before it finished,
  as its record classifies it (the agy lane has no binding cost cap, so its stops are deadlines). All three are marked `≥`
  by §D3's rule, and the result file names the reason per cell.
- **A1.3 · The Claude lane's block figures include the harness's own sandbox probe**, in both arms alike (`final_T`, as
  each block's cells file states in its header). A file that splits the probe out exists for most cells but not all, so
  the uniform choice is the figure every cell has. Matrix-1 and the specchange-1 cells predate the probe.
- **A1.4 · Where two records disagree on a condition's cells, the result of record's scored cells govern.** This happens
  once: Pro × Crc32 × plain × none.
- **The census's count, stated before the run:** of the 181 DONE conditions, 171 have every cell covered by a tracked
  figure, 1 is partly covered, and 9 have none (every level-5 Flash condition whose cells come from level-5 ADDENDUM 3). By
  §D2 those 10 print `unmeasured`, and the check then fails visibly. Nothing is recovered by hand for this run.

---

## ⚖️ ADDENDUM 2 — THE FIRST PRINTED FILE DROPPED FOUR CELLS THIS REGISTRATION DOES NOT LET IT DROP. REPRINTED WITH EVERY CELL OF RECORD. APPENDED; §D1–§D6 and ADDENDUM 1 untouched.
**What happened.** The first file of record (saltbench `643cac00`, merged at `084f2fe9`) left four fired cells out of their
conditions: `s3ps02`, `s3ps03` (Pro × Paxos × salt-diet × none) and `s3ft02`, `s3ft03` (Pro × FreeList × salt-diet × statement).
The lead did it under A1.4, on the ground that the level-1 record scores a smaller population for those two conditions. **A1.4
does not say that.** It says the record's scored cells govern where two records DISAGREE, and it names the one condition where
that happens (Pro × Crc32 × plain × none). §D1 says no cell is added or dropped. The fresh non-author read found it (verdict
REPAIR), and the helm ruled that the registration governs as written.
**Why it matters.** All four dropped cells are salt-diet cells, and all four were cut off by the per-turn deadline. Dropping them
removed lower bounds from the treatment arm only: the arm-correlated removal §D6 warns about. The rule was also uneven, because
Sonnet's BUILD-FAIL cells stayed in.
**The reprint.** Every cell of record is in its condition. The four are lower bounds (DEADLINE, A1.2). The reader's recomputation
and the reprint agree: Pro × Paxos × salt-diet (T1) reads `≥ 14,987,158`, and Pro × FreeList × statement × salt-diet reads
`≥ 12,610,137`. No sign in T4 changes. The check is unchanged: 171 + 16 + 3 + 10 unmeasured = 200. Conditions with fewer than 3
cells of record: 10.
**The order of events, stated exactly** (the reader's question). §D1–§D6 were committed at 14:25 PDT (`368d925`), before any
map existed. ADDENDUM 1 was committed at 14:32 (`ad1b6b2`). It came after a coverage census that located each cell's source and
computed no median. The instrument's first run, a scratch dry run, came after ADDENDUM 1. The first file of record was printed
at 14:39 (`643cac00`). So the registration was written before any median was computed, and ADDENDUM 1 followed a coverage
census, not a result.
**One definition the captions must carry** (the reader's question, measured). A Claude-lane cell's `T` counts every session
under the cell, including subordinate worker sessions on another model. Most Opus matrix-1 and statement cells record
`claude-opus-5+claude-sonnet-5` in the all-roots table. The row's model is the cell's SUBJECT model. The result file's header now
says so.
