# Which way each arm of the 11-25 fork moves the matrix comparisons (read-only; it decides nothing)

The helm asked for this table (bus 2026-11-25 07:58) before his word on the fork in `../README.md`. It moves no table of
record and is not the source of any figure in the paper.

**The arms, each against the RULED state** (the record without the 10 WEB-SERVED cells, which already leave every
comparison):
- **(b)**: the RULED state without the 52 OTHER-RECORD cells (`set-other.txt`, read from `../census.tsv`).
- **(c)**: the RULED state without the 133 cells that are CTL-NAMED or OTHER-RECORD (`set-ctl-or-other.txt`). This arm
  would reverse the signed 10-13 ruling on ctl/ reads (`AMENDMENT-agy-ctl-fence-2026-10-13.md` §5).
- **(b′)** (added 2026-11-25 after kent's read): the RULED state without only the 2 cells another record's CONTENT reached
  (`set-content.txt`, the CONTENT rows of `../other_seen.tsv`, derived by `awk -F'\t' '$4=="CONTENT"{print $2}'`).

**The instrument:** `recut_sets.py`, a copy of `../../o37-agy-web-served-2026-11-20/recut/recut.py` changed only in
which cells it takes out (the WEB-SERVED cells plus a set file). It changes no instrument of record.
- **Controls:** with no set (`-`), every `*-moved.txt` is SAME as the tracked 11-20 one (`out-ruled/run.log`). In every
  run, each OLD reproduces its RESULT of record's rows (descriptive v2 864/864, v2 + O57 864/864, cost v3 922/922,
  correctness v3 781/781, ZF check green).
- **Diffs:** `out-<arm>/<label>-moved-vs-ruled.txt` is `recut_diff.py` run on the RULED NEW against the arm's NEW.
- **Headline tables:** `out-*/headline-signs.md` holds correctness P4 and descriptive T4, printed by `headline_signs.py
  OUTDIR` (cut verbatim from OUTDIR's NEW tables). The 08:1x files were cut by hand; `headline_signs.py --check` reproduces
  `out-other` and `out-ctl-or-other` byte for byte, and `out-ruled` from its NEW run (SAME, 2026-11-25).
- **Route ledger** (kent's question 3): `recut_sets.py` prints, per run, the distinct ids each route took out and the ids NO
  route took (`#TAKEN-OUT-NOWHERE`). Every run reads 0 nowhere: ruled 0 of 10, (b′) 0 of 12, (b) 0 of 60, (c) 0 of 141.
  The gaps between "map rows marked" and the ids out are the cells taken by the block-NA cells TSV and the ZF cells TSV
  (ruled 5 + 2, (b) and (c) 6 + 3), which are not in either cell map.
- **Verdicts by arm and level:** `out-<arm>/verdicts-by-arm.md`, from `verdicts_by_arm.py` over the correctness per-cell
  rows.

**Where an instrument's guard reads a removal as missing data (declared):** under (b), whole conditions lose every cell.
For example, Flash × FreeList × brownfield × salt-diet and Flash × LRU × spec-change × salt-diet print `missing`, and the
tools exit 1 on their own arithmetic checks (`out-*/run.log`). That is the removal, not a fault.

**Limits:** NONE-NAMED is a lower bound on contact (`../README.md` limit 1), so the cells that "stay" are not shown to be
uncontaminated. OTHER-RECORD counts literal paths only (TILDE is not in either set).

## (b′): what taking out only the 2 CONTENT cells moves (`out-content/`, against the RULED NEW)

Read from `out-content/correctness-v3-moved-vs-ruled.txt` and `out-content/headline-signs.md` against
`out-ruled/headline-signs.md`:
- **Correctness P4:** one Flash sign leaves salt-diet: Flash × FreeList × greenfield goes from `−` to `—`. It is not a
  measured pass. The condition is scored by condition (0 / 3), and with `l5fs02` out the instrument's ADDENDUM 3d guard
  prints it `unmeasured` (printed n 3 against 2 cells of record). Flash bare P4 counts go from `0 2 1 1 1` to `0 2 0 1 2`.
- **Correctness P3:** Flash × LRU × spec-change, salt-diet phase 2, goes from 3 / 3 to 2 / 2 (`l8rfss03` was a PASS).
- **Descriptive T4:** every k-of-m sign holds. Two Flash medians move: bare 3.72 → 3.03 and spec-change 2.88 → 3.06.
- **Verdicts of the 2 cells** (`out-content/verdicts-by-arm.md`): salt-diet l5 1 by condition, salt-diet l8 1 PASS.

