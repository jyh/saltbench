# Mid-cell root gap over the cells of record (census ADDENDUM 37), 2026-10-17
Zero spend; every file here was produced on the run box or the lead box by the scripts beside it, read-only.
- `exposure_census.out` — every `cells-*/<cell>/ctl` on the run box: its window (first ISO stamp of `watch.log`, else `launch.log`, to its latest
  `end-*`) and every OTHER `cells-*` root whose filesystem birth time falls strictly inside it. ROOT rows give each root's birth. *One cell
  directory name (a NO-RUN cell, not of record) had a pool name in it; it is redacted to `<pool>`, the only byte changed.*
- `item7_join.py` → `record-cells-windows.tsv` — every DONE row of `CELLMAP-correctness-tables-v3-2026-10-01.tsv` that names a cell, joined to its
  window. A cell id in more than one root is resolved by rule, and the rule is printed per row (`resolved_by`).
- `item7_namehits.py` → `exposed-namehits.tsv` — for each EXPOSED record cell, each born-inside root's name counted in the cell's own record
  (its `ctl/`, which for the agy lane holds the model's stream, plus, for a Claude cell, every session file of its transcript). The cell's own
  fence renders are read separately (`FENCED`). Controls per row: ctl bytes > 0 and the cell's own id found.
- `escape_backfill.sh` and `claude-escape-coverage.tsv` — the Claude lane's escape scan (the chain's own `escape_scan.py`) per cell of record:
  at harvest where the chain ran it, and back-filled on 2026-10-17 for the cells that predate the chain.
- `inroot.py` → `inroot.out` (input `rec-windows.tsv`, one row per distinct record cell) — the IN-ROOT form: a sibling cell directory born inside
  the cell's own root strictly inside its window, and each such sibling's id counted in the cell's record. A transcript record of type
  `attachment` is the client echoing the cell's own settings (its deny list) and is not counted; the run before that exclusion found the echo
  (6 hits per cell in four cells), which is the evidence that the transcripts are in the haystack.
- `exposed-namehits-control.tsv` — the POSITIVE CONTROL on the name count: the same script with `NAMEHITS_CONTROL=1`, which reads the cell's own
  fence renders as part of its record. Every one of the 7 FENCED cells then counts its fenced names (2 to 6 hits); the other 41 stay at 0.
