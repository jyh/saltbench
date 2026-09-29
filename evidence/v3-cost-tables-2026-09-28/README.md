# v3 cost tables, step a (desk YP): every cell of record resolved to one cells root on the run box

- `cellroots-inventory.tsv`: one row per (cell, root) on the run box whose `<root>/<cell>/ctl` exists, for the 517 distinct ids in
  `CELLMAP-descriptive-tables-v2-2026-09-27.tsv`, with the artifact shape: CLAUDE (a watch.log METER line), AGY (an agy turn loop), or NONE.
  It was listed on the run box on 2026-09-28 and is a snapshot of that day.
- `cellroots-resolved.tsv`: the three cells the rule REFUSED as ambiguous, each settled by a cited record (`l5cp01` by its meter's T
  matching level 5's line 30; `l8cpss01`/`03` by chain D ADDENDUM A's copy note).
- `cellroots.tsv`: `harness/systems-v3/cellroots_v3.py --map … --inventory … --resolved …`, rc 0: SOURCE-ROOT 54 · UNIQUE 453 ·
  DEAD-SUFFIX-EXCLUDED 7 · RECORD 3 · AMBIGUOUS 0 · ABSENT 0. Every resolved cell carries an artifact (none reads NONE).
- The tool's selftest has 13 arms. A pick-the-first-candidate mutant reddens 3 of them.

Nothing here is a registration, and no figure is printed from it. It is the input steps c and d read.

## Step d (Claude wall), raw: `claude-wall-raw.tsv`, produced on the run box by `claude-wall-raw.sh`
For each CLAUDE-shape cell in `cellroots.tsv` (245) and each phase with an end marker, the last `METER … wall N/CAP` line of that phase
in the cell's own `ctl/watch.log`. There are 269 phase readings (245 phase 1, 24 phase 2) and none is missing. **Limits, beside the figure:**
the watcher computes `wall` NET of held time (`t - T0 - hold_total`), so a hold is printed in its own column (1 cell). The last METER line
precedes the end marker by up to one tick (about 60 s), so the figure understates a cell's wall by at most one tick. It is a raw
extraction, not the registered reading.

## Step e (the Opus head-vs-subagent split), raw: `opus-split-raw.tsv`, produced on the run box by `opus-split-raw.sh`
`cell_meter.py` (export `9d873183acab`) `--json` over every CLAUDE-shape cell in `cellroots.tsv`, one row per (cell, config dir). The tracked script differs from the one run in its line 4 only: the meter's path is taken from `CELL_METER` rather than written out, because that path names a private tree. A cell
without `ctl/run-cfg.tsv` (the 09-09/09-10 roots) is metered from the one config dir that holds its slug; none was missing or ambiguous.
The tracked file keeps the 108 Opus-headed cells and drops the config-dir column. **Second method:** for the 54 cells it shares with
`harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv`, T agrees exactly in 54 of 54. Each row's
`T_head + T_exec_opus + T_exec_sonnet + T_wf == T` is asserted as it is written.
Over the 108 cells (computed from the file, not typed): 11.65 % of T is outside the head session; 90 cells carry Opus subagent tokens and
74 carry Sonnet subagent tokens; no cell has no subagent. **Limits, beside the figures:** 30 rows carry `VOID(UNDERSTATED)` (an interrupted
turn whose usage the client never finished writing), so their T and COST are LOWER BOUNDS. COST is modelled at list rates from `rates.tsv`
read on 2026-09-05, not an invoice, and the rates page is owed a re-read before any dollar is registered. Block N (#274, and the Opus column
still running) is not in this population. It is a raw extraction, not the registered reading.
