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
