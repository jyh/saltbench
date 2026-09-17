# ADDENDUM 3 evidence — the ⑯ per-cell token record, and the harvest's VOID(UNMETERED)

bench, 2026-09-17. Backs §A3.5 and §A3.6 of `harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md`.

| file | what it is |
|---|---|
| `token_table.sh` | the driver, fed to the run box on **stdin** (`ssh <run box> 'bash -s' < token_table.sh`) so **nothing was written to that box**. For each `hc1lp0*` cell it prints the cell's own `ctl/run-cfg.tsv` cfg rows, then meters the cell TWICE: **ARM A** at the slug `clb_harvest.py` derives from the lane env (`CLB_CFG`), **ARM B** at the slug the cell itself records. |
| `hc1-lru-plain-token-table.txt` | the capture. Three cells, both arms each, `cell_meter.py` full stdout. |
| `derive_table.py` | reads the capture and prints **every figure §A3.5/§A3.6 quote**. Nothing in the addendum is typed. It **REFUSES (rc 1)** on fewer than three cells or a cell with no `head` RECEIPT row — an absence is never silently a smaller n. |

## What was read, and what was not written
`cell_meter.py` from the release export tree, **sha256/16 `faf81afbbd7062c0`**, taken 2026-09-17T21:15:22Z.
The meter opens session `jsonl` files read-only. **No cell, no slug, no config dir and no lane env was written**, and
no harness byte was changed — the export is frozen and named by the release addendum.

## The redaction, declared rather than silent
The capture is passed through a documented substitution before it is tracked, because the raw output carries a home path
and two account-directory names, which the tree's own gate forbids (`scripts/check_infra_names.py`,
`scripts/check_private_paths.py`):

    /Users/jyh                   -> <HOME>
    -Users-jyh-                  -> -<HOME>-        (the slug form: a path with '/' turned into '-')
    <the lane's current cfg dir> -> <THE LANE'S CURRENT CONFIG DIR>
    <the dir HC1 fired under>    -> <THE CONFIG DIR HC1 FIRED UNDER>

⚠️ **The second rule exists because the first one missed it.** A first pass checked for the residual home path in its
**slashed** form, read 0, and was wrong: a session slug is the path with every `/` replaced by `-`, so `-Users-jyh-`
survived a check whose positive control (`RECEIPT`) only ever proved the file readable. ⇒ ***A POSITIVE CONTROL PROVES
THE HAYSTACK, NEVER THE NEEDLE*** — the residual check was re-run in both forms, each against a control.

## The reading, in one line each
- **ARM A is `VOID(UNMETERED)` on 3 of 3** — a manufactured absence: the slug is derived from a mutable env key that has
  already moved, while the cell records its own `cfg`, `run_at` and `phase` in `ctl/run-cfg.tsv` and the tool does not read it.
- **ARM B meters all 3** — `T` 6,651,048 … 9,322,934, with the `RECEIPT` rows giving every direction per (bucket × model).
- **`hc1lp03` carries one interrupted turn**, so its `T` is a LOWER BOUND the instrument declares itself ⇒ the registered
  median over n=3 is a **BAND**, `[8,143,625 , 9,322,934]`, not a number.
