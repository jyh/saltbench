# `cell_tokens.py` — the ⑯ reading, and the drive that proves it on live cells

bench, 2026-09-17. Implements ADDENDUM 3 §A3.5(e) of the Claude-lane (B) freeze.

## Why it is not a call to `clb_harvest.py`
`clb_harvest.py` derives a cell's session slug from **`CLB_CFG`** — the lane env, a **mutable** key. When the lane
moves, it prints `VOID(UNMETERED) — no session dir for this cell` for cells whose sessions are on the same box.
**Measured 2026-09-17 on three landed cells: 3 of 3 VOID by that path, 3 of 3 metered from the `cfg` the cell
records for itself** in `ctl/run-cfg.tsv`. ⇒ ***A CELL IS METERED FROM THE `cfg` IT RECORDS, NEVER FROM THE
AMBIENT ENV*** — and the cell records `phase` in the same file, which is ⑯'s phase dimension for free.

⛔ **It changes no harness byte.** The export is frozen and named by the release addendum, so the `slug_of` repair
in `clb_harvest.py` is **named and parked to the pilot's completion per ⑱**. This is the bench-side reader that
makes ⑯ executable meanwhile, and it lives in `scripts/`, which the export does not carry.

## What it refuses rather than printing a zero
An absence here would be **manufactured** — the tokens exist and the path was wrong — so every failure names the
path it looked at and exits non-zero: `rc 2` no `ctl/run-cfg.tsv` · `rc 3` the recorded cfg has no slug dir ·
`rc 4` the meter produced no RECEIPT rows · `rc 5` the meter could not be run. A cell whose meter declares a
**VOID is still printed**, with the void carried **verbatim beside the numbers** — *"unmetered is not zero"* and
*"understated is not a price"* are different claims and both must reach the reader.

## The self-test: 10 arms, red first
Four RED arms (each refusal driven), a VOID-carrying arm, three GREEN arms whose expected values are **derived
from the fixture's own bytes** (idiom law clause 1), and a **MUTANT arm that proves the GREEN arms can fail** —
a changed fixture must move the total.
⚠️ **Two of the GREEN arms were written as `rc == 0 and X or Y` and were rewritten.** That shape passes on the
`or` alone: it would have gone green with a broken tool. ⇒ ***AN ARM WITH AN `or` IN IT IS AN ARM THAT CAN PASS
WITHOUT TESTING ANYTHING*** — one conjunction per arm, and a mutant to prove the conjunction bites.

## `live-drive-hc1-lru-plain.out`
The self-test run **on the run box** (a different box and a different interpreter), then the tool over the three
landed `hc1lp0*` cells in **one command**, `rc 0`.
⭐ **Its `ALL` row agrees with the independent capture in `evidence/claude-lane-b-addendum3-2026-09-17/`** —
`T` 9,322,934 · 8,143,625 · 6,651,048 — **two instruments, one object, same numbers.**
Home paths and config-directory names are replaced by role words, as in the ADDENDUM 3 evidence, for the tree's
own `check_infra_names` / `check_private_paths` gates.
