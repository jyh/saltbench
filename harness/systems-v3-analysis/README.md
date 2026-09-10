# systems-v3-analysis — the token figures beside the dollar figures

⛔⛔ **PROVENANCE CORRECTED 2026-09-10.** This file opened by quoting the Captain: *"please info bench
to produce token costs (in addition to dollar costs)."* **He never said it** — measured across his whole
pane corpus (82 projects, 681 transcripts, positive control driven), "token costs" appears in ZERO user
turns. He asked `anubis`, about the `anubis` design doc: *"can we use tokens instead of dollars?"*, and
later *"bench has calculated the tokens, can you add them?"*
✅ **RULED 2026-09-10, and this line's provenance is exact:** asked directly in this seat's pane after
the correction was published, the Captain answered **"yes dolars and tokens both"** — verbatim, in
full, to this seat, about this campaign's tables. **Dollars and tokens both stay.** The reasoning below
remains this seat's and the helm's; only the four words are his.

⇒ **A question became an order, "instead of" became "in addition to", and the addressee and subject
both changed.** The reasoning printed under it — dollars are derived, tokens are what the pools meter —
**is this seat's and the helm's, not his.** It is good reasoning and it is adopted as campaign practice
on its own merits; it is not a quotation. ⛔ **Whether dollars stay in the tables is his to answer:** he
asked *instead of*, and this work assumed *in addition to*. Found by `kent`. Registered in ADDENDUM 8
§H7 of `../systems-v3/AMENDMENT-specchange-taskshape-2026-09-09.md`.

**Why this directory is separate from `systems-v3/`.** Analysis tools live beside the harness, never
inside it: a harness directory that is checked as a set refuses any file present but unpinned, so an
analysis script dropped into it can halt every episode. Nothing here is ever run by a cell.

## What was already true, and what had to be built
`cell_meter.py` has recorded the four token counts per assistant record all along — `input`,
`cache_creation` with its 5m/1h split, `cache_read`, `output` — per model, split head vs executor,
with `T` and a modelled `COST` beside them. **The order is therefore a surfacing job, not a
measurement job.** `tokens_table.py` walks a cell population, resolves each cell's account by locating
its transcript tree under `<cfg>/projects/` and reports it as an opaque uuid prefix, never a name, runs the meter, and emits one row per cell.

## ⛔ → ✅ IT IS AN ARM COMPARISON NOW, AND THE FIX WAS TO STOP DROPPING CELLS
The meter VOIDs a cell whose transcript carries an **interrupted record**, and it is right to — its
own message says why: *"the client stops writing usage where the interrupt lands, so this sum is a
LOWER BOUND, not a price."* The first cut of this table therefore dropped 12 of 37 cells.
⛔ **That exclusion was ARM-CORRELATED, and a by-arm number computed over it compares two
differently-selected subsets:**
```
  STRICT            plain  7/16 = 44%     salt-diet 14/21 = 67%     gap 23 points
  FLOOR-INCLUSIVE   plain 15/16 = 94%     salt-diet 18/21 = 86%     gap  8 points
```
✅ **A VOID is not a gap.** The meter still computes `T` and `COST` from the 99 %+ of records that ARE
complete; what it refuses to do is call that a *price*. So those cells are **RETAINED and labelled
`FLOOR`**, never merged into the priced set — `--floors`, and `agg.py` prints both aggregates.
⇒ **Why this is safe in the direction that matters:** a floor UNDERSTATES, the understatement falls
more often on the CONTROL arm, and **a bias against the arm under test cannot manufacture a positive.**
⛔ **LIMIT, and it is not a formality: that argument licenses a NUMBER reported as a floor. It does
not license a VERDICT.** The understatement is unbounded on the one interrupted record per cell.
📌 **The exclusion-neutrality check runs BEFORE the aggregate**, not in a footnote after it — an
exclusion that is not arm-neutral has to be visible before the numbers are.

## ⭐⭐ THE FINDING THE ORDER SURFACES, AND IT IS WHY "TOKENS" IS NOT ONE NUMBER
Summed over the 21 strictly-priced cells:
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

✅ **AND THE FINDING SURVIVES THE FLOORS**, which is the check that matters — it is not an artefact of
the arm-correlated exclusion. Over 33 cells instead of 21:
```
                per million T      per million OUTPUT
  plain            $1.025               $66.62
  salt-diet        $0.805               $94.26
```
Same direction, same reversal, n up by more than half.

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

---

# ⭐⭐ EXTENDED 2026-09-10 — SEVEN ROOTS, 89 OF 93 CELLS PRICED, AND THE REVERSAL REPLICATES

The first cut walked **one** root (`cells-matrix1`) and priced 21 cells. Walking every completed
Claude root on the run box:
```
  cells-matrix1 33 · cells-placebo 16 · cells-placebo-refire 15 · cells-stmt-2026-09-09 12
  cells-stmt-free-2026-09-09 6 · cells-specchange-1 4 · cells-n3-topup 3
  ---- 89 of 93 cells priced (53 OK + 36 FLOOR), 4 with no transcript ----
```

## ⭐⭐ THE FINDING REPLICATES ACROSS INDEPENDENT POPULATIONS
`RESULT-tokens-by-root-2026-09-10.txt`, per root, never pooled:
```
  root                       plain $/M-T   salt $/M-T   plain $/M-out   salt $/M-out
  cells-matrix1                  1.025        0.805         66.62          94.26
  cells-specchange-1             1.019        0.837         76.25          96.34
  cells-stmt-2026-09-09          1.003        0.877         70.30          84.37
  cells-stmt-free-2026-09-09     0.987        0.834         62.56          91.65
```
⇒ **In every one of the four roots carrying both arms, the treatment is CHEAPER per token of total
traffic and DEARER per token produced.** ⇒ 🔑 ***THE REVERSAL IS NOT AN ARTEFACT OF ONE WAVE.*** It is
four independently-run populations — different dates, task sets and wave designs — agreeing on the
direction, which is a far stronger statement than the n of any one of them.
📌 **And the floor rule earns itself in every root**, not just the first: arm-neutrality goes 23→8,
17→0 and 33→0 points once VOID cells are retained as labelled floors.

## ⛔ THREE THINGS THIS TABLE DOES NOT DO
1. **IT DOES NOT POOL ROOTS.** They are different waves, arms, dates and task sets, and pooling them is
   the confound this campaign already cards. `agg.py` reports each separately and says so.
2. ⛔⛔ **AND THAT WAS NOT FREE: the previous `agg.py` HARD-CODED `root == "cells-matrix1"`**, so run
   over a seven-root file it produced an aggregate **byte-identical to the one-root run** — a summary
   silently describing a different population than its input. Caught only because the numbers had not
   moved when they should have. ⇒ 🔑 ***A FILTER THAT NARROWS WITHOUT SAYING SO TURNS A WIDER INPUT
   INTO A SILENT NO-OP***, and the output looks exactly as correct as before.
3. **The two placebo roots are priced but carry neither `plain` nor `salt-diet`**, so they contribute
   cells to the coverage count and nothing to this comparison. Stated rather than dropped.
