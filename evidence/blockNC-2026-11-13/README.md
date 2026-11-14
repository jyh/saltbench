# Block NC — the 72 P1 baselines (§C3 item 2, §C2 step 1 as ADDENDUM 1 registers it)

Run 2026-11-13 on the run box, zero model tokens, after ADDENDUM 1 reached origin (`6da31ba0`).
Driver `ncbase.sh` (in this directory): the export's `G/run_tests.sh` (export candidate saltbench-systems `36ca596b`) on a git CLONE of
each block-N source's `landed-1`, never in the cell; each source's tree hash recorded before and after.

- `p1-baselines.tsv` — the table as the driver wrote it: 73 rows, because the cells root also holds `clbmrs03`, the cell block N VOIDED
  and re-fired as `clbmrsr3` (block N ADDENDUM 14). It is not in block N's record and is not in this block's population.
- `read_baselines.py` — reads the table against block N's record (`evidence/claude-lane-blockN-2026-09-28/blockN{O,S}-cells.tsv`)
  and ADDENDUM 1's eligibility rule; its output is `read_baselines.out`.

Readings (from `read_baselines.out`):
- 62 sources carry `landed-1`, and every one of their G figures equals block N's recorded `tests` column (no mismatch). That is the
  positive control on the instrument.
- 60 ELIGIBLE of 72; eligible per model × arm: Opus plain 17, Opus salt-diet 15, Sonnet plain 16, Sonnet salt-diet 12 (rule 5:
  arm-correlated, reported beside every phase-2 figure).
- 12 shortfalls, so 12 fresh phase 1s under rule 4: Opus LinearScan plain 1, Opus LinearScan salt-diet 3, Sonnet AES salt-diet 1,
  Sonnet LinearScan plain 2 (clbnrp01, clbnrp03, both 8/9, as ADDENDUM 1 expected before the data), Sonnet LinearScan salt-diet 3,
  Sonnet MaxFlow salt-diet 2.
- No source changed (tree hash and HEAD equal before and after, all 73).
- CONTROL (ADDENDUM 1): `B/run_tests.sh` on clbmap01's `landed-1` exited 3 with no REGRESSIONS line and `TESTS 0/0` (a compile
  error naming the clause's functions), so the premise of ADDENDUM 1 holds.

Run-box receipts (sha256/16): `baselines.tsv` 5f3aaa85fcdb86ae, `drive.log` 2a4c8d10ae105c6d, `ncbase.sh` 33996336ecb28d48.
