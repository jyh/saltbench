# HC stage 1: three instruments and their receipts

## bench (SaltBench lead), 2026-09-16. Registered design: `harness/systems-v3/PREDICTIONS-HC-stage1-2026-09-13.md`.

These three instruments feed the stage-1 result's columns and limitations. Each output is a **snapshot of a named
population, taken while stage 1 was still firing.** ⛔ **The result re-runs each one over the final 45 cells before it
quotes any of them.** A figure below is a statement about the population printed beside it, not about the stage.

---

## 1 · `budget-read-column/`: the §3b column, scored by what came back

**What §3b needs:** whether the subject *saw* the `BUDGET.md` countdown. Without that, a NEAR-CAP landing cannot be
told apart from pacing.

**The defect, found on `hc1ps02` and censused over 42 ended cells:** the column counted the read *action*. The
watcher writes the file at its first 60-second tick. Every subject reads it early: the first read came 7 to 221
seconds in (median 12), and 38 of those 42 first reads returned nothing. All of these figures are computed from the
per-read offsets in `census.out`.
```
  arm        cells   column said READ   a read returned the countdown   READ, but never saw it
  placebo     14          14                      4                            10
  plain       14          14                      1                            13
  salt-diet   14          14                      5                             9
```
Source: `census.out` (`budget_read_content_census.py`). It agrees with a second method, id-paired reads
(`redrive_method2.py` → `redrive.out`), on 42 of 42 cells. Over all 66 `BUDGET.md` tool uses, the countdown regex was
also cross-tabulated against the file's own header line (`xtab.out`): no tool result carries the header without the
countdown.

**The fix:** `budget_read_column.py` now reports `READ-SAW` / `READ-NOT-SEEN` / `NO-READ` from content. The pre-fix
file is kept as `budget_read_column.py.orig-2026-09-16`.
```
  drive-before.out   5 real cells, pre-fix column     5 of 5 FAIL (every one reads READ)
  drive-after.out    same 5 cells, fixed column       5 of 5 PASS
  drive-mut1.out     mutant: never SAW                fails exactly its 3 SAW arms
  drive-mut2.out     mutant: always SAW               fails exactly its 2 NOT-SEEN arms
```
**No §3b verdict moves:** the outcome is decided by the cost band, and this column is reported beside it.
⚠️ **The defect's sign flattered §3a:** a constant READ makes the NEAR-CAP exemption look load-bearing.
⚠️ **Scope:** the head transcript only. Sub-agent transcripts are not read.

## 2 · `lk-wait-census/`: build-wedge exposure, by arm

**The worry (desk LK):** a cancelled build wedges the next build, which inflates that cell's cost. Salt-diet cells
build more, so exposure could be arm-correlated in the direction that enlarges a premium.

**Measured over 40 ended HC1 cells, plus 1 live cell that is listed but not counted.** Source: `census.out`,
`lk_wait_census.py`.
- **The fleet build wrapper is mentioned in 0 of 40 transcripts.** HC1 cells never call it.
- **The in-cell analogue is real.** `bin/rt` serialises builds on its own lock and prints a wait line. That needle is
  present in every cell's `bin/rt` (the `rt_control` column).
```
  arm        cells   cells with >= 1 wait   wait lines
  plain       14             12                 34
  placebo     13              9                 24
  salt-diet   13              5                 10
```
⇒ **The exposure runs opposite to the worry: the control arms wait more.** A wait adds cost only through extra turns,
which is UNMEASURED. Whatever it adds falls mostly on plain, and that *shrinks* a salt-diet premium.

## 3 · `concurrency/`: the registered preflight versus the fire script

**Registered:** PREDICTIONS §6.3 item 3, *"THE RUN BOX IS QUIET — no cell of any wave running"*, and §6.1, *"Never two
cells concurrently."*
**Enforced until 2026-09-16:** the fire script only checked for a live HC1 cell. An agy cell has no heartbeat file, so
that check could not see one.

**Census (`hc1_concurrency.py` → `census.out`):**
- **Population:** 428 cell directories, 411 with a readable window, 44 HC1 cells (rows 1–44).
- **Window:** the earliest `ctl/launch.log` stamp to the latest `end-N` stamp. A cell with no `end-N` uses the newest
  `ctl/` mtime and is flagged `NOEND` (9 such cells).
```
  HC1 cells sharing the box with >= 1 other cell   23 of 44
  HC1 cells NOT quiet at fire                      19 of 44
  overlapping cells that are agy                   73 of 73

  arm        shared minutes / window minutes        overlapped   not quiet at fire
  plain       235.1 / 540.9  = 43.5 %                  8 of 15            7
  placebo     186.7 / 407.7  = 45.8 %                  8 of 15            7
  salt-diet   249.4 / 598.4  = 41.7 %                  7 of 14            5
```
⇒ **Balanced by arm across the stage.** Box load changes wall time directly, and cost only through the subject's
behaviour, which is UNMEASURED.
⚠️ **Paxos is the exception.** Its plain and placebo cells were exposed and its salt-diet cells (so far) were not. *If*
load raises cost, that inflates the denominators, which shrinks the salt-diet premium and raises the placebo ratio.
That is a sign, not a size.

**The guard, wired into the fire script before row 45:** `box_quiet_all_waves.sh`. A non-HC1 cell counts as live if it
has a launch log, no end marker, and a `ctl/` write within 2400 s (the agy print timeout of 1800 s plus 600 s). The
guard fails toward refusal.
- `drive_quiet.sh` → `drive_quiet.out`: 7 of 7 arms, including a mutant.
- **On the real box it refused, naming the one agy cell then running.**

---

## What is NOT here, declared

- **The wave harvester, the per-cell meter and the fire order are not tracked.** They are run-environment files that
  name run-environment and account detail. The per-cell meter output is the authority for every cost.
- **Rewritten for this public tree:** the home prefix → `$HOME`, the run config directory → `<run-config-dir>`, and the
  account token → `<account>`. **Nothing else was changed.**
- `MANIFEST.tsv` gives each file's sha256/16 as run and as tracked, and marks which files were rewritten (8 of 23).
