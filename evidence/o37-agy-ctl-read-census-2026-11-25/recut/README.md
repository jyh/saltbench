# Which way each arm of the 11-25 fork moves the matrix comparisons (read-only; it decides nothing)

The helm asked for this table (bus 2026-11-25 07:58) before his word on the fork in `../README.md`. It moves no table of
record and is not the source of any figure in the paper.

**The arms, each against the RULED state** (the record without the 10 WEB-SERVED cells, which already leave every
comparison):
- **(b)**: the RULED state without the 52 OTHER-RECORD cells (`set-other.txt`, read from `../census.tsv`).
- **(c)**: the RULED state without the 133 cells that are CTL-NAMED or OTHER-RECORD (`set-ctl-or-other.txt`). This arm
  would reverse the signed 10-13 ruling on ctl/ reads (`AMENDMENT-agy-ctl-fence-2026-10-13.md` §5).

**The instrument:** `recut_sets.py`, a copy of `../../o37-agy-web-served-2026-11-20/recut/recut.py` changed only in
which cells it takes out (the WEB-SERVED cells plus a set file). It changes no instrument of record.
- **Controls:** with no set (`-`), every `*-moved.txt` is SAME as the tracked 11-20 one (`out-ruled/run.log`). In every
  run, each OLD reproduces its RESULT of record's rows (descriptive v2 864/864, v2 + O57 864/864, cost v3 922/922,
  correctness v3 781/781, ZF check green).
- **Diffs:** `out-<arm>/<label>-moved-vs-ruled.txt` is `recut_diff.py` run on the RULED NEW against the arm's NEW.
- **Headline tables:** `out-*/headline-signs.md` holds correctness P4 and descriptive T4.
- **Verdicts by arm and level:** `out-<arm>/verdicts-by-arm.md`, from `verdicts_by_arm.py` over the correctness per-cell
  rows.

**Where an instrument's guard reads a removal as missing data (declared):** under (b), whole conditions lose every cell.
For example, Flash × FreeList × brownfield × salt-diet and Flash × LRU × spec-change × salt-diet print `missing`, and the
tools exit 1 on their own arithmetic checks (`out-*/run.log`). That is the removal, not a fault.

**Limits:** NONE-NAMED is a lower bound on contact (`../README.md` limit 1), so the cells that "stay" are not shown to be
uncontaminated. OTHER-RECORD counts literal paths only (TILDE is not in either set).
