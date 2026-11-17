# Block WC result evidence (bench, 2026-11-17)
- `wc-derive.sh` builds `cells.tsv` from the objects: the population is `WC_SOURCES` in the export's `clb_stage.sh` (24 rows, read by
  `git show d55062a6:…`). Each ended phase-2 cell's end file, meter, served models (`served_models_v3.py check-cell`) and the stage log's
  export are read on the run box. Its `solution.rs` is copied (WORKING TREE when dirty, else HEAD) and scored HERE by the withheld B
  suite from a root extracted from d55062a6. A condition whose source never landed is a REACH-LOSS row with the source's own end and meter.
- Column meanings: `tests` = passed/total; `regressions_failed` and `clause_failed` = FAILED/total (the B driver prints them that way,
  `tasks/systems-v3/<P>/B/withheld/tests/driver_main.rs`); `brc` = the runner's exit code.
- `wc-derive.log` is the run's own output. Two defects caught before this table, both now refusals in the script:
  (1) a relative out path left the task tree unextracted, so every row scored rc 127 (the runner guard);
  (2) a killed first run's loop subshell survived and appended into the re-run's table, giving 32 rows for 24 (the population guard,
  red on that discarded table, rc 3).
- `wcgen.py` writes the two RESULT files; every figure block in them is the verifier's own `--print` output.
- ⚠️ **What the verifier does NOT read (kent's read of #448, 2026-11-17, two of eight mutants survived it):** the `source` column and
  `sol_sha16`. The tie of each phase-2 cell to its source, and the solution hash, are covered only by `wc-derive.sh` on the run box.
  kent's own cross-check (24 distinct sources; the 20 reused ones are exactly the 20 ELIGIBLE baselines; the 4 others are the fresh
  phase 1s; no phase-2 hash equals its phase-1 hash) is on the bus, not in a script here.
