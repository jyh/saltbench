# O37: agy tools that failed on an unwritable /tmp/claude, by arm (2026-11-15)

**Finding.** Our agy turn-loop launcher hands the sandbox a complete environment that omits `CLAUDE_CODE_TMPDIR` (791 of the run box's
792 srt turn-loop env files; the one that carries it is block WA's arm-L battery). Without it the subject's shell has `TMPDIR=/tmp/claude`
(measured in block WA's F2 battery), which the sandbox does not let it write. The shell itself started; the TOOLS
inside it that make a temp file failed (`mktemp: mkdtemp failed on /tmp/claude/...: Operation not permitted`, `patch: can't create
/tmp/claude/...`, rustc `Operation not permitted ... at path "/tmp/claude/rustc..." ... error: aborting due to`). Block WA ADDENDUM 3
found the cause and fixed it from export 3796e6b4 (arm L, the variable carried per cell).

**Method.** `census_tmpclaude.py` (run on the run box at zero spend over every agy stream, `streams.tsv`, 801 streams with the
phase): a stream is a HIT when a `/tmp/claude/` mention sits within 200 characters of "not permitted". `census-hits.tsv` is its
106 hits, labelled by arm from the cell directory's name. `cellmap_join.py` joins those hits to the complete matrix's cells of record
(`harness/systems-v3/CELLMAP-descriptive-tables-v2-2026-09-27.tsv`, arm as REGISTERED there) → `cellmap-join.tsv`, one row per cell,
and `cellmap-join.out`:

```
  model                  arm         HIT   HIT (ambiguous id)   clean   no stream   cells of record
  gemini-3.1-pro-high    plain         2          0               64        2          68
  gemini-3.1-pro-high    salt-diet    21          2               45        2          70
  gemini-3.8-flash-high  plain         0          0               69        2          71
  gemini-3.8-flash-high  salt-diet    11          0               58        2          71
```
Over both models: **salt-diet 32 of 141 cells of record (34 counting the two ambiguous ids), plain 2 of 139.**
`result_files_map.py` lists, for every hit, the RESULT files that name its cell → `result-files-map.tsv` (per-file counts at its foot).

**Controls.** Empty hit set (the mutant): every HIT column reads 0. One plant (a clean plain cell, s3cp01, added to the hits): Pro
plain HIT 2 → 3, nothing else moves. A re-run from these files reproduces the first run's join row for row.

**The defect is arm-correlated.** Salt-diet cells are hit far more often than plain ones; the salt-diet method runs more of its own
tooling (the `mktemp` hits name its gate-test files). The author's reading, NOT measured here: a defect that fails the treatment's tools
is not expected to manufacture a salt-diet advantage. Its sign on cost and outcome is not measured, and nothing here re-reads one. In
block WA's own cells (client 1.5.9, before arm L) both arms are hit (plain 6 of 6, salt 7 of 8): there it is symmetric.

**Limits.** A HIT is a failure the stream PRINTED, not a changed outcome: a subject can retry or work around it, and no cell's score
or cost is re-read here. The 200-character window and the dir-name arm label in `census-hits.tsv` are the census's choices. The matrix
cell map names no root for agy cells, so the join is by cell id: two salt-diet ids exist in two families with only one hit (marked
ambiguous), and 8 cells of record have no stream on the run box. Which fence arm (srt or seatbelt) each cell of record
ran is not shown here, so the cause is established for srt cells only; the hits are printed failures whatever the cause. Streams were read on the run box only. **The Claude lane is NOT
MEASURED here** (a different client and transcript format); the same signature in its cells is a separate census, owed.
