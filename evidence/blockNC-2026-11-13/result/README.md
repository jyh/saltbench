# Block NC result evidence (bench, 2026-11-17)
- `nc-derive.sh` builds `cells.tsv` from the objects. The population is `NC_SOURCES` in the export's `clb_stage.sh` (72 rows; read into
  `SOURCES_FILE` by `git show ee7450ce:…` on the lead's box). Each phase-2 cell is FOUND by its `ctl/copied-from.tsv` (`copied_from_id` =
  the source's id), never by a typed name. A row with no phase 2 is REACH-LOSS (source did not land) or REACH-LOSS-G (it landed and its G
  baseline, `gbase.sh`'s log, was not a full pass). Each scored cell's `solution.rs` (WORKING TREE when dirty, else HEAD) is run against the
  withheld B suite of a root extracted from ee7450ce.
- **It ran ON THE RUN BOX** (`RUN_HOST=local`), because the lead's box was under a disk hold (< 30 GiB free, the helm 2026-11-17 01:35).
  The suite root was built on the lead's box by `git archive` and copied over; `nc-derive.log` is the run's own output.
- ⚠️ **The run used the copy BEFORE one fix:** its runner guard read the source list before it was set (`set -u`, "SRCS: unbound variable"
  in the log), so that guard checked nothing in this run. The root held every task's B runner (all 72 rows score, none rc 127). The
  committed `nc-derive.sh` has the guard after the list, and it refuses a root without runners (rc 2) before any row.
- Column meanings as in block WC's README: `tests` passed/total; `regressions_failed`, `clause_failed` FAILED/total; `brc` the runner's rc.
- `end-census.out` (made by `nccensus.sh` on the run box at 17:32Z): the 72 rows' end kinds, read before the derive.
- `ncgen.py` (+ `ncprose.py`, its per-model prose) writes the two RESULT files; every figure block is the verifier's own `--print`.
- Harvest scores of `clblrp03` and later cells were DEFERRED at fire time (the disk hold); this table is their first score.
- ⚠️ **The Liveness clause:** every Liveness failure is `answer_is_the_count_honest_pair` (1 of 5 clause tests, 0 regressions); the
  failing test is named in each cell's `b.out` on the run box (`~/bench-dry/nc-result-2026-11-17/out/sol/<cell>/b.out`). Put to a
  non-builder read as a possible suite defect (§C6 item 4).
- What the verifier does NOT read: `source`; `sol_sha16` on a phase-2 row (as block WC's). `served_head` and `export12` are read on
  phase-2 rows (they produce the `served:` and `export` lines). On a REACH-LOSS row the four phase-2 columns (`served_verdict`,
  `served_head`, `export12`, `sol_sha16`) must read `-`, and anything else refuses (added on kent's read, 2026-11-17).
