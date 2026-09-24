# The sandbox probe inside a cell's cost: the split, and the convention (desk VX)

Written 2026-09-22 by bench. This directory backs the cost-convention declaration in
`harness/systems-v3/CENSUS-full-matrix-2026-09-14.md` (section "DECLARED — THE COST CONVENTION").

## What the files are

- `probe-split.tsv` is one row per Claude-lane cell, 180 rows: 128 Sonnet-block cells (blocks SB, SBS,
  SC, SG, SS) and 52 Opus-block cells (O, OS). Columns: `slug`, `cells_root`, `cell_T`, `cell_COST`,
  `probe_T`, `probe_COST`. Taken 2026-09-22 03:2xZ on the run box. The harness's own
  `clb_harvest.split_slug` sorted each session head into cell or probe, and `cell_meter.py` metered each
  of the two groups. Neither was reimplemented. Heads were pooled across config dirs, which is how the
  four cells that crossed pools (desk VW) come out whole.
  The split was checked on `clbczp01` before the sweep: cell + probe matched the whole-slug reading to
  the token and to the cent (10,474,410 + 145,645 = 10,620,055 T; $5.2796 + $0.1510 = $5.4306).
  ⚠️ The driver that looped those two tools over the cells was not kept. The two tools it called, and
  this output, are what is recorded here.
- `ratio_shift.py` reads that table and prints, per block, the census's median COST ratio
  (salt-diet : plain) PROBE-IN and PROBE-APART. `--selftest` passes, and a mutant that reads probe-in
  into both columns fails it.
- `ratio_shift.out` is its output, committed beside it.

## What it shows

On this table's population, the PROBE-IN reading reproduces the census's stated ratios for SS (5.31 vs
5.32), SBS (4.70 vs 4.71), OS (1.22 vs 1.23) and O (1.89). It does not reproduce SG: 8.48 here against
8.27 in the census. So the SG line was computed on a different set of cells, and the shift below is a
shift on this population, not a correction to that line.

| block | PROBE-IN | PROBE-APART | shift |
|---|---|---|---|
| SG | 8.48x | 9.28x | +9.5 % |
| SBS | 4.70x | 5.12x | +8.9 % |
| SB | 12.73x | 13.53x | +6.3 % |
| SS | 5.31x | 5.54x | +4.4 % |
| SC | 4.99x | 5.10x | +2.2 % |
| O | 1.89x | 1.89x | +0.2 % |
| OS | 1.22x | 1.22x | −0.0 % |

In every Sonnet block the probe pulls the ratio down, so salt-diet looks relatively cheaper than it
is. In the Opus blocks it has no measurable effect, because Opus cells cost enough that a probe of
about $0.10 disappears into them.

## The convention (desk VX (b), decided by bench under council 2026-09-22 §2)

1. **A cell's cost, as this campaign means it, is PROBE-APART**: the subject's work, not counting the
   harness's check of its own sandbox. That is the intent the harness already states, since
   `clb_harvest.split_slug` separates the two on purpose and refuses rather than guess.
2. **The published block tables stay as measured, PROBE-IN, and nothing is re-issued**, as council
   ruled (d). Each one already carries the declared line saying so (PR #239).
3. **Any ratio between arms that the pilot's write-up states is taken PROBE-APART from this split and
   cites this directory.** A ratio is where the offset biases; a cost column is not.
4. `cell_meter.py` is **not changed during the pilot matrix**. Changing it would move every figure
   still to come against the 160 already done. Metering probe-apart at the source is for a registered
   amendment after the matrix is a result of record.

**Why this is not taken to the Captain:** the ruling brings it to him only if the two meters differ
enough to change a claim. They do not. Every census ratio this touches is already declared a LOWER
BOUND, because of the arm-correlated cap. Probe-apart raises each one, which is the direction the
bound already allows. The order of blocks is the same under both readings (SG > SS > SBS > OS), and
the Opus figures do not move. What changes is the second significant figure, and that is what the
declaration exists to say.
