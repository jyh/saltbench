# Block WC — the 24 P1 baselines (§WC3 item 2, §WC2 = NC §C2 step 1 with NC ADDENDUM 1's instrument)

Run 2026-11-15 on the lead's box, zero model tokens, after block W's result of record reached main (`eb7248a0`, saltbench #445) and with
this registration signed (the helm, 2026-11-13). Driver `wcbase.sh` (in this directory): export 0916ef9a's `G/run_tests.sh` (the export
block W fired on, which carries both B/ trees, WHT 17d0b93b and NTT c5cdaed5, as §WC0 row 4 records) on a git CLONE of each block-W source's
`landed-1`. The sources are COPIES of block W's 24 cells of record, taken after each end marker (repo/target excluded), so the withheld
trees never reach the run box. Each copy's tree hash and HEAD are recorded before and after.

- `p1-baselines.tsv` — the table as the driver wrote it, 24 rows; `drive.log` — its output (scratch paths masked).
- `eligible-by-model-arm.out` — ELIGIBLE (rc 0 and passed == total > 0) per model × arm: Opus plain 6/6, Opus salt-diet 5/6, Sonnet plain 6/6,
  Sonnet salt-diet 3/6.
- `control-vs-blockW.out` — the positive control on the instrument: every one of the 20 sources with a `landed-1` reproduces block W's
  recorded `tests` figure (0 differ); the 4 without one are exactly block W's 4 CAP-COST cells.

Readings:
- **20 of 24 ELIGIBLE; 4 shortfalls, all salt-diet** (Opus WHT 1: clbdws02; Sonnet NTT 2: clbits01, clbits02; Sonnet WHT 1: clbiws01). Each is
  a capped block-W cell that never tagged `landed-1`. By §WC2 each shortfall is ONE fresh phase 1 (greenfield × none at this block's
  export and C1 $37.21), recorded beside block W and never in its n. The shortfall is arm-correlated (NC rule 5), reported beside every
  phase-2 figure.
- `clbdtp03` (block W's EXIT-FORCED harness fault) carries `landed-1` and is ELIGIBLE.
- No copy changed (tree hash and HEAD equal before and after, 24 of 24).
- CONTROL (NC ADDENDUM 1): `B/run_tests.sh` on clbdtp01's `landed-1` exited 3 with no REGRESSIONS line and `TESTS 0/0`, so the premise
  holds for NTT. It was not driven for WHT.
- LIMIT: the positive control compares the baseline at `landed-1` with block W's score at HEAD; every source here reads 11/11 on both, so
  the comparison cannot tell those two refs apart.
