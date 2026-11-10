# RESULT — O37's LEAN ARM ON A SECOND PROBLEM: SIX CLAUDE CELLS, LZW × GREENFIELD × LEAN-AENEAS × {OPUS, SONNET} × n = 3
## bench (SaltBench lead), 2026-11-09. Registration `AMENDMENT-O37-aeneas-lzw-2026-11-09.md` (signed by paris; released in its ADDENDUM 2).
## Every figure below names its source: a file in this repository, or, where marked, a run-box log or a bus post. The cell table is DERIVED by `evidence/o37-aeneas-lzw-2026-11-09/o37-derive.sh`
## (the pilot's derivation script with three changes: the cell list, the task, the header) into
## `evidence/o37-aeneas-lzw-2026-11-09/cells.tsv` (sha256/16 862c7886409efa98). Nothing in it was typed.

---

## §R1 · THE SIX CELLS: OPUS 2 OF 3 ARE A LEAN-ARM PASS, SONNET 0 OF 3
A Lean-arm PASS (§A3) is: hidden suite FULL PASS ∧ the Lean half GREEN from the harness's bytes ∧ the statement UNCHANGED.
CAP-COST is an outcome of record on the cost axis (§A3): a capped cell is scored as it stands at the cap.
```
  cell      model            end       dirty  suite  tests  Lean half  axioms (kernel replay, then walked)                  statement  PASS  proof lines  final $
  clbqza01  claude-opus-5    LANDED    0      PASS   8/8    GREEN      Classical.choice · Quot.sound · propext              UNCHANGED  PASS  1338         27.3904
  clbqza02  claude-opus-5    CAP-COST  2      PASS   8/8    RED        - (the proof module does not build)                  UNCHANGED  NO    894          37.4443
  clbqza03  claude-opus-5    LANDED    0      PASS   8/8    GREEN      Classical.choice · Quot.sound · propext              UNCHANGED  PASS  1398         36.5068
  clbjza01  claude-sonnet-5  CAP-COST  2      PASS   8/8    RED        Classical.choice · Quot.sound · propext · sorryAx    UNCHANGED  NO    547          37.7316
  clbjza02  claude-sonnet-5  CAP-COST  1      PASS   8/8    RED        Classical.choice · Quot.sound · propext · sorryAx    UNCHANGED  NO    664          37.8090
  clbjza03  claude-sonnet-5  CAP-COST  2      PASS   8/8    RED        - (the proof module does not build)                  UNCHANGED  NO    1112         37.6578
```
- **Two rows carry a declaration (§R4), and neither voids its verdict:** clbqza01 (two failed boots before launch, zero spend; §R4 first
  item) · clbqza02 (another lane's test suite on the run box at the cell's start; §R4 second item). The table is the derivation's output
  unchanged, so the marker is this line, not a column.
- Every cell: export 3ea54f5d9f13 (registration ADDENDUM 2), client 2.1.259, served models `clean` (only the condition's model; Sonnet's
  sidechains Sonnet in clbjza02 and clbjza03; no Opus cell spawned a sidechain). `final $` is the post-end meter (`ctl/post-end-1.tsv` col 5),
  the pilot's instrument. `dirty` counts uncommitted paths in the end tree; a capped cell is scored on its working tree (the scorer's rule).
- The hidden suite ran over a COPY of each cell's `solution.rs` with `tasks/systems-v3/LZW/G/run_tests.sh` (runner sha16 7c6d2cea42891fab,
  `cells.tsv`). The Lean half ran through the export's own `o37/o37_score.sh` in scoring mode: confined, every constant the module declares
  replayed through the kernel, the type checked as exactly `O37Spec.Statement`.
- **Spend: $214.54** over six cells (Opus $101.34 · Sonnet $113.20; sums of the `final $` column). §A8's ceiling was $223.26 plus overrun.
  Each Sonnet cell and one Opus cell overran the $37.21 cap by $0.23–$0.60; the overrun is printed, never clipped.
- Tokens beside every dollar figure: `cells.tsv` column `final_T` (Opus 30.8 M · 52.4 M · 49.0 M; Sonnet 155.3 M · 145.6 M · 137.6 M).

## §R2 · BESIDE THE COMPARISON CONDITION (§A2: LZW × greenfield × salt-diet × statement, the Verus cells whose statement is given)
```
                 Verus × statement (of record)                      Lean-aeneas (this block, cells in order 01 · 02 · 03)
  claude-opus-5  cells 6d58f1ec · 9aca67c5 · f5f66c47                 cells clbqza01 · clbqza02 · clbqza03
                 3 of 3 PASS (suite 8/8 each)                       2 of 3 PASS (02 CAP-COST, Lean RED)
                 $22.53 · $15.34 (FLOOR) · $18.54; median ≥ $18.54   $27.39 · $37.44 (CAP) · $36.51; median $36.51
  claude-sonnet-5 cells clbszs01 · clbszs02 · clbszs03                cells clbjza01 · clbjza02 · clbjza03
                 2 of 3 PASS (01, 03 PASS 8/8;                      0 of 3 PASS (all three CAP-COST, suite 8/8 each,
                   02 CAP-COST, suite BUILD-FAIL)                     Lean RED: 01, 02 sorryAx · 03 does not build)
                 $10.48 · $37.31 (CAP) · $12.36; median $12.36       $37.73 · $37.81 · $37.66, all at the cap
```
Sources: the Opus Verus verdicts are `harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv`, as tabled in
`AMENDMENT-specchange-taskshape-2026-09-09.md` §B3 (class PASS, 8/8). Their costs are `evidence/ks-tokens-2026-10-01/statement_arm.tsv`,
and the FLOOR is `CELLMAP-descriptive-tables-v2-2026-09-27.tsv`'s lower_bound. The Sonnet Verus cells are
`evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv` (final_COST, verdict). The Lean column is §R1.
**Reading, sign only, n = 3 per model, one problem (no rate, no p-value, §A9):**
- **Opus:** the Verus arm passed 3 of 3; the Lean arm passed 2 of 3 at the same cap and cost more at the median: at most 1.97× (36.51 ÷ 18.54,
  an UPPER bound, because the Verus median is bounded below by a FLOOR cell).
- **Sonnet:** the Verus arm passed 2 of 3 (one CAP-COST); the Lean arm passed none. All three Lean cells reached the cap with the hidden suite
  passing 8/8 and the Lean half RED: two with the proof unfinished (sorryAx: clbjza01, clbjza02), one whose proof module does not build
  (clbjza03).
- **Against the CRC-32 pilot** (`RESULT-O37-aeneas-pilot-2026-09-30.md`, 6 of 6 PASS, no cell near the cap), LZW is the harder problem for
  this arm at this cap, as §A8 priced it.

## §R3 · THE PRICE, AGAINST §A8's PROJECTION
§A8 projected every cell to end CAP-COST (Opus ≥ $41.2, Sonnet ≥ $61.9 per cell). **Measured: 4 of 6 did** (all three Sonnet, one Opus).
Two Opus cells landed under the cap ($27.39, $36.51), so the Opus projection (the pilot's ×2.22 Lean ÷ Verus) was HIGH for 2 of 3 cells.
The first one (clbqza01) fired the registration's re-price stop (§A7). The price went back to the helm, who read it and ruled the block on at
the registered terms (bus, 2026-11-09 13:20). For Sonnet the projection is not contradicted: every cell was cap-bound.
**Points:** one delta measured, around clbjza01 (source: the meter readings in bench's bus post of 2026-11-09 14:58:13, not a file in
this repository): the pool's all-models meter read 61 before and 62 after, an UPPER bound of ≈ 1 point for
that cell (an integer percent; other work drew on the pool in the window). The last cell (clbjza03) ran in the pool's next weekly window, after
that window's day-line check read LAUNCH.

## §R4 · WHAT THE RUN DECLARES BESIDE ITS VERDICTS
- **The run box had no tmux server at the first fire.** clbqza01's watcher failed boots 1 and 2 (`tmux new-window` into a missing session; no
  client started, zero spend) and boot 3 launched after the session was created. This is within the watcher's six-boot bound (the export's
  `harness/systems-v3/cell-watch.sh` lines 464–467 at 3ea54f5d9f13: six consecutive fast deaths end the cell FAILED-BOOTS), so the cell stands. The fire script checks that tmux is on PATH, not that the box session exists; that fix belongs to a later export.
- **Box concurrency at clbqza02's start:** another lane's UI test suite ran on the run box from 14:52 to 14:58 PST (its owner's bus post
  of 2026-11-09 14:59:14); the cell fired at 22:55:00Z = 14:55:00 PST (the run box's `~/bench-dry/o37z-fire-ZO2.out`), so the overlap was
  about 3 min, as the helm's note of 15:30:00 says. The cell's transcript carries exactly two user-text messages (the harness's sandbox probe and the boot
  prompt) and no interrupt. It can have touched wall time and box load only; the token meter and the verdict cannot be moved by it.
- **Receipt (5)'s probe turns** ($0.0574, one per model) ran outside every cell's meter. Each cell's own sandbox probe is metered apart
  (`clb_harvest.py`'s PROBE TURNS line) and is included in `final $`, as in the pilot.

## §R5 · WHAT THIS CANNOT ESTABLISH (carried from §A9, plus what the run showed)
- Two problems, n = 3 per model: no rate, no p-value, and nothing about Lean vs SMT in general.
- **A CAP-COST row says the arm did not finish inside the pilot's budget; it says nothing about whether it would have** (§A9). In every
  cap-bound cell the hidden suite passed 8/8 and the Lean half was RED at the cap: the proof unfinished (sorryAx) in two cells, a proof
  module that does not build in two. Whether more budget would have turned any of them GREEN is not measured. A higher cap for the Lean arm
  is NOT registered here (§A8 (B)); it changes what a Lean verdict asserts, so it is the Captain's word.
- The pairing's ceiling is §A6's (transcription + an 8-row vector check + a non-author read); the bounded decode half (deviation 4) is a
  declared difference from the Verus statement.
- One trust base with x86lean is not met at this pin (Lean 4.31.0 here), as in the pilot.
- Nothing here makes a claim about the salt method.

---
*Read by kent at dcd1d60f0a93 (bus 2026-11-09 21:28:28, findings, not a verdict: the document against its named tables, not the cells).
Its five points are taken in this revision; a delta read is asked before this file is cited.*
