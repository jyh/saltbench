# PRICE — CAMPAIGN MATRIX #1 (OPUS, 5 PROBLEMS × 4 ARMS × n=3 = 60 CELLS)

bench, 2026-09-08, desk row HV. **The Captain: "#1 + #2 for Opus are the minimum to be publishable …
asap, by tomorrow if possible … results in the range 1–3× for salt are actually quite amazing, we
should not be shy of that."** This prices #1 and states what it can and cannot deliver. Every cost is
read from a harvested `METER.txt` in the stage-1 archive (§23(e)); nothing is retyped from a message.

## 1. ⭐ THE PREMISE THE HELM COULD NOT SETTLE, MEASURED AT THE OBJECT — #1 IS A RUN, NOT A BUILD
The helm's feasibility read says *"all 5 problems built"*; council 09/07 recorded *"the v3 harness has
**TWO** built problems"*. **They are both right about different things, and the difference decides the
schedule**, so I measured it on the run box rather than picking one.

    frozen export …-5873cf8 / tasks/systems-v3/ :  Crc32  FreeList  LRU  LZW  Paxos
    every one:  B · card.md · G · verify.names   (identical shape)
    total bytes: 9,141 · 12,917 · 14,643 · 20,861 · 16,037   (none is a stub)

⇒ **All five problems ARE built and frozen in the export. Council's "two" was true of the CELLS that
have RUN, not of the problems that exist.** #1 is a RUN. ⛔ **But three of the five — FreeList, LRU,
Paxos — have never produced a v3 cell**, and **36 of the 60 sit on them** (§5).

## 2. THE PRICE, FROM THE ARCHIVE
    per-cell, 12 bare stage-1 cells      mean $11.82   median $10.95
    per-cell, incl. the 2 stmt anchors   mean $12.10
    pessimistic (per-condition maxima)   mean $15.57

    60 cells   CENTRAL  $726        PESSIMISTIC  $934        (+ §5 smoke $35)

**Quota:** the council pack's stage-1 figure was ~14 points for ~12 cells. **I am quoting that as a
BAND and not a number**, per the standing finding that the metered→point rate is a band: **~60–90
points for 60 cells.** ⛔ **This is exactly why the switch-on-cap mechanism is the precondition and not
a nicety** — at 4-wide the run spans a reset boundary on any plausible rate, and a cap hit mid-flight
without rotation costs the cells in flight, not merely the queue.

## 3. PARALLELISM AND THE CLOCK (stage 1 measured ≈35 min/cell serialized)
    1-wide 35.0 h · 2-wide 17.5 h · 3-wide 11.7 h · **4-wide 8.8 h** · 6-wide 5.8 h
⇒ **"By tomorrow" is feasible at ≥3-wide and comfortable at 4-wide**, and the binding constraint is
quota, not wall clock. **Recommend 4-wide**: it clears the day with margin and matches the width the
box has already carried.

## 4. ⭐⭐ WHAT 60 CELLS BUYS — AND IT IS NOT MORE PRECISION, IT IS THE FIRST POSSIBLE VERDICT
The row says *"report by cross-problem consistency (5 problems is the power that 2 could not give)."*
That is exactly right, and here is why, as arithmetic:

    P(all k problems show premium > 1 | H0: no effect) = 2^-k
      k=2  p=0.2500   <- STAGE 1. A PERFECT 2/2 SWEEP CAN NEVER REACH .05
      k=4  p=0.0625   still cannot
      k=5  p=0.0312   ** SIGNIFICANT **

⇒ 🔑 ***k = 5 IS THE SMALLEST PROBLEM COUNT AT WHICH A CLEAN SWEEP IS SIGNIFICANT. THE CAPTAIN'S FIVE
IS NOT "MORE DATA" — IT IS THE FIRST k THAT CAN PRODUCE A VERDICT AT ALL.*** Stage 1 was not merely
thin; at k=2 it was **structurally incapable** of the claim, whatever the cells had said.
📌 **And what it still does not buy, stated with it (G3):** n stays 3 per condition, so the resolvable
floor is unchanged at **2.0072×** and every individual premium (1.1655–1.3560) stays **UNRESOLVED**.
⇒ **The design is powered on SIGN across problems (G1) and unpowered on MAGNITUDE within one (G2).**
⇒ ⛔ **REPORT IT AS: "salt costs more on all five problems, p = 0.031" — NOT as "salt costs 1.36×".**
The ratio is the honest headline only with the floor beside it, and the Captain's *"1–3× is amazing"*
is a statement about the RANGE, which the sign test supports and a point estimate does not.

## 5. ⛔ THE ONE THING I WOULD DO BEFORE FIRING 60: A 3-CELL SMOKE
FreeList, LRU and Paxos are frozen, complete and **never once driven end to end.**
    insurance: 1 `plain-bare` cell each = 3 cells, ~$35, ~35 min at 3-wide
    exposure without it: a build defect surfacing at cell 13 wastes up to 36 cells, ~$426
⇒ **12× the cost to skip it.** A problem that has never produced a cell is pinned to the day it was
authored; this is the cheapest possible arm against that.

## 6. THE GOLD, AND ITS PRESENT EVIDENCE BASE
The row: *"the gold of #1 is the stmt pair — (d) plain+stmt vs (e) salt+stmt: if (e) beats (d), THE
METHOD IS THE STATEMENT."* Across 5 problems that is **5 paired signs, p = 0.031 for a clean sweep.**
⛔ **Today it rests on ONE cell each** — LZW plain+stmt `d14d9d05` $11.19 vs salt+stmt `ec9e1106`
$16.42 — i.e. **k=1, p=0.50, no verdict whatever.** #1 is what turns the gold from an anecdote into a
test, which is the strongest argument for firing it as specified rather than trimming it.

## 7. THE PLAN I WILL FIRE
1. **Precondition (systems, row HV):** the quota switch-on-cap mechanism, driven red→green on the run
   box. Per the row's DEFAULT-IF-SILENT I fire as soon as that receipt exists — nothing else waits.
2. **Smoke (§5):** 3 cells, the never-run problems, `plain-bare`.
3. **Fire 60 at 4-wide**, registering predictions BEFORE the first cell, with each ordering carrying
   the sampling behaviour of its own statistic at this n — the stage-1 defect, not inherited.
4. **Report** by cross-problem consistency and the gold pair, by name, with G1/G2/G3 on every line.
