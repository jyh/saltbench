# systems-v3-analysis — the token figures beside the dollar figures

**Standing order, the Captain, 2026-09-10 09:3x:** *"please info bench to produce token costs (in
addition to dollar costs)."* Registered as ADDENDUM 8 §H7 of
`../systems-v3/AMENDMENT-specchange-taskshape-2026-09-09.md`.

**Why this directory is separate from `systems-v3/`.** Analysis tools live beside the harness, never
inside it: a harness directory that is checked as a set refuses any file present but unpinned, so an
analysis script dropped into it can halt every episode. Nothing here is ever run by a cell.

## What was already true, and what had to be built
`cell_meter.py` has recorded the four token counts per assistant record all along — `input`,
`cache_creation` with its 5m/1h split, `cache_read`, `output` — per model, split head vs executor,
with `T` and a modelled `COST` beside them. **The order is therefore a surfacing job, not a
measurement job.** `tokens_table.py` walks a cell population, resolves each cell's account by locating
its transcript tree under `<cfg>/projects/`, runs the meter, and emits one row per cell.

## ⛔ THE TABLE IS NOT YET AN ARM COMPARISON, AND THE REASON IS IN THE TABLE
Over `cells-matrix1`, the phase-1 greenfield landings:
```
  arm        total   priced   VOID   no-transcript   priced-rate
  plain         16        7      8               1          44%
  salt-diet     21       14      4               3          67%
```
Every VOID is the same verdict — `VOID(UNDERSTATED) N record(s) carry stop` — the meter's §33 refusal
to report a number it knows is understated, because an interrupted record reports output tokens far
low **and not zero**. The instrument is behaving correctly.
⇒ **But the exclusion is arm-correlated, 44% against 67%.** Any by-arm figure below is computed over
differently-selected subsets of the two arms, so it is **a per-cell instrument's output, not an arm
comparison.** Closing this needs the §33 interrupted-record treatment applied to the 12 VOID cells.

## ⭐⭐ THE FINDING THE ORDER SURFACES, AND IT IS WHY "TOKENS" IS NOT ONE NUMBER
Summed over the 21 priced cells:
```
  cache_read      469,610,681    97.50% of T
  output            4,700,618     0.98% of T
  cache_write_1h    4,882,288     1.01% of T
  cache_write_5m    2,465,973     0.51% of T
  input                 6,308     0.00% of T
  T               481,665,868
  cost_usd             406.99     modelled at list rates, NOT an invoice
```
**`T` is 97.5 % cache reads.** So the token figure that answers *"what did this draw from the quota"*
and the token figure that answers *"how much did the agent actually write"* differ by two orders of
magnitude — and they **rank the arms in opposite directions**:
```
              per million T      per million OUTPUT
  plain          $1.074               $65.66
  salt-diet      $0.803               $93.92
```
⇒ 🔑 ***A COST NORMALISED PER TOKEN IS ARM-DEPENDENT, SO "TOKENS" WITHOUT SAYING WHICH TOKENS IS
WORSE THAN DOLLARS, NOT BETTER.*** Reporting `$/T` alone makes the treatment look cheaper; reporting
`$/output` alone makes it look dearer; both are arithmetically correct. ⛔ **A cap expressed in `T`
therefore subsidises whichever arm runs longer** — which is the very quantity the experiment measures.
⇒ **Every token figure this campaign publishes names its denominator.**

## Provenance
Every number above is produced by the scripts in this directory over
`RESULT-tokens-table-matrix1-2026-09-10.tsv`, which is `tokens_table.py`'s own output over
`~/cells-matrix1` on the run box, 2026-09-10. Nothing is retyped from a message, and no dollar figure
is derived backwards from a token count or the reverse. A cell whose account cannot be resolved reads
`UNRESOLVED`; a cell the meter voids reads `VOID`; neither is ever reported as 0.

## Rebuild
```
  python3 tokens_table.py ~/cells-matrix1 > RESULT-tokens-table-matrix1-<date>.tsv
  python3 agg.py <that file>          # the aggregate, with the exclusion-neutrality check first
  python3 void_by_arm.py <that file>  # why cells are unpriced, by arm
```
