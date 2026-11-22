# Block T's result of record: the per-cell table and the tools that print every figure

Block T is `harness/systems-v3/AMENDMENT-O37-statement-six-claude-2026-11-11.md`: six problems × {Opus, Sonnet} × {plain, salt-diet}
× statement, greenfield, n = 3, so 24 conditions and 72 cells. Its two results of record are `RESULT-claude-blockTO-2026-11-22.md`
and `RESULT-claude-blockTS-2026-11-22.md`. The census re-cut is ADDENDUM 49 of `CENSUS-full-matrix-2026-09-14.md`.

## What is here

| file | what it is | made by |
|---|---|---|
| `cells.tsv` | 72 rows, one per cell, every column read from the cell's objects | `t-derive.sh` |
| `categories.tsv` | the statement category per cell: a READING of the subject's code, with the post or addendum it was read in | `t-categories-harvest.py <bus file> <cell ids>` (60 rows: the last read post per cell, keyed on the first cell id in its subject) + ADDENDUM 5 and its correction (Luby, 12 rows) |
| `t_used_check.py` / `.out` | a mechanical cross-check of the salt-diet categories against the subjects' own Verus runs (0 conflicts) | — |
| `t_section_cmp.py` / `.out` | §T7's VOID row: each cell's card as built carries the export card's section byte for byte (72 of 72; a planted byte reads 12 VOID) | — |
| `t-derive.sh` | lists each condition's cells on the run box (and refuses unless every condition has 3 and the total is 72 unique ids), reads the box facts, copies each cell and scores it against the withheld G suite | — |
| `t-box.sh` | the box-side reader for one cell: end-1, the meter (`ctl/post-end-1.tsv`), the export, the served model, the born-during census, the subject's own Verus runs; read-only. ⚠️ The run of record used an earlier text of this file that wrote out the export harness's path; this text reads the same path from the cell's own `ctl/built-from.tsv` (`harness` row) | — |
| `t-sections.py` | each problem's statement section, i.e. the `rust` block under the card's `## Statement`, taken from the export's own card | — |
| `stmtuse.py`, `specdefs.py`, `tnames.sh` | the statement line: which spec fns are named, which lines are verbatim, whether each provided spec fn is defined identically, statement-derived names in tests (needle v2) | copied from the lead's drivers |
| `t_result_gen.py` | prints every figure line of both RESULTs from the two tables; `--check` asserts each line against the RESULT's bytes | — |
| `t-derive.log` | the derive run's own log | — |

## How the table was made

```
RUN_HOST=<run box ssh name> RUN_HOME=<run box home> SYSTEMS_CLONE=<saltbench-systems clone holding 7fe4ff7f> EXPORT_SHA=7fe4ff7f \
TOOLCHAIN_ENV=<suite runner toolchain env> bash t-derive.sh <out-dir outside this repo>
```
The out dir holds the withheld task trees and the cell copies, so it stays outside the public tree. Only `cells.tsv` and the log are
copied here. Scoring is BY COPY: the cell is rsynced (with `repo/target` left out) and `score_claude_v3.py` from the export decides
which object gets scored. That is the WORKING TREE when `solution.rs` is dirty (HEAD is read beside it but does not score), else HEAD.
This is the rule the lane's drivers applied at each harvest.

## Columns of `cells.tsv` worth knowing

- `end1_kind` comes from `ctl/end-1`, field 2. `capped` is `yes` exactly when that is `CAP-COST`.
- `final_COST`/`final_T` come from the last row of `ctl/post-end-1.tsv`: the meter after the client exited, the harness's own
  sandbox probe included. `at_end_COST` is the same meter at the end marker.
- `served_verdict`/`served_head` come from `served_models_v3.py check-cell` on the cell's own transcripts. The model is never taken
  from the block name.
- `born_n`/`born_hits`/`born_names` are block T ADDENDUM 3's check. They count `$HOME` entries on the run box whose BIRTH time lies in
  the cell's run, and how often each entry's name appears in the cell's transcripts. `control_own_id_hits` is the positive
  control (the cell's own id).
- `verus_last`/`verus_last_clean` list the subject's own Verus runs ordered by record timestamp: the latest run, and the latest run
  with 0 errors (`timestamp|verified|errors`).
- `specdefs` reports, per provided spec fn, whether the scored solution defines it identically (whitespace-normalised). Any
  `DIFF:` names follow.

## What the categories are, and are not

A category says what the subject did with the statement. It is not a score, and nothing in this directory derives it mechanically.
USED needs the ensures on every contracted exec fn INSIDE `verus!` (checked by line position) AND the subject's own clean run
(TA's lead ruling, bus offset 106,504,279). A plain-arm label needs every test file read, because an oracle written under
unrelated names is invisible to any needle. Each row names where it was read. A known needle limit: `tnames.sh` undercounts a
transcription written under UNPREFIXED names (clbvrp02, clbvrp03), and the categories of those cells were read from the code.
