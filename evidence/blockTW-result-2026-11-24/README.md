# Block TW's result of record: the per-cell table and the tools that print every figure

Block TW is `harness/systems-v3/AMENDMENT-O37-statement-wht-ntt-claude-2026-11-22.md`: WHT and NTT × {Opus, Sonnet} × {plain, salt-diet}
× statement, greenfield, n = 3, so 8 conditions and 24 cells. Its two results of record are `RESULT-claude-blockTWO-2026-11-24.md` and
`RESULT-claude-blockTWS-2026-11-24.md`. The census re-cut is ADDENDUM 51 of `CENSUS-full-matrix-2026-09-14.md`.

This directory is block T's (`../blockT-result-2026-11-22/`, README there) re-cut for TW. Every block-T tool that TW uses unchanged is
called FROM THAT DIRECTORY (`t-box.sh`, `stmtuse.py`, `specdefs.py`, `tnames.sh`); the copy of `t-box.sh` on the run box was compared
with it before the derive and is identical. The files here differ from their block-T originals only where the population differs:
the problem list, the model blocks (`two`, `tws`), the population count (24), and the output names.

| file | what it is | made by |
|---|---|---|
| `cells.tsv` | 24 rows, one per cell, every column read from the cell's objects (columns: block T's README) | `tw-derive.sh` |
| `categories.tsv` | the statement category per cell: a READING of the subject's code, each row naming the lines read. Salt-diet rows come from the tally (`../blockTW-2026-11-22/tw-cells.tsv`, the lead's reads at relight 217, one corrected here); plain rows were read for this result (relight 218) | — |
| `tw_used_check.py` / `.out` | the mechanical cross-check of the salt-diet categories against the subjects' own Verus runs (0 conflicts) | — |
| `tw_section_cmp.py` / `.out` | §TW7's VOID row: each cell's card as built carries the export card's section byte for byte (24 of 24) | — |
| `tw-derive.sh` | lists each condition's cells on the run box (refuses unless each has 3 and the total is 24 unique ids), reads the box facts, copies each cell and scores it against the withheld G suite of export `e4f786fe` | — |
| `tw-sections.py` | each problem's statement section, the `rust` block under the card's `## Statement`, from the export's own card (WHT 3,466 B, NTT 3,286 B, as §TW2 item 3 registered) | — |
| `tw_result_gen.py` | prints every figure line of both RESULTs and the census line; `--check` asserts each against the document's bytes | — |
| `tw-derive.log` | the derive run's own log | — |

## How the table was made

```
RUN_HOST=<run box ssh name> RUN_HOME=<run box home> SYSTEMS_CLONE=<saltbench-systems clone holding e4f786fe> EXPORT_SHA=e4f786fe \
TOOLCHAIN_ENV=<suite runner toolchain env> bash tw-derive.sh <out-dir outside this repo>
python3 tw_section_cmp.py <out-dir>/cells <out-dir>/sections > tw_section_cmp.out
python3 tw_used_check.py > tw_used_check.out
```
The out dir holds the withheld task trees and the cell copies, so it stays outside the public tree. Scoring is BY COPY, as block T's.

## The checks, driven both ways

- `tw_result_gen.py --check` reads 30 of 30 (Opus) and 32 of 32 (Sonnet) figure lines present. Mutant: one Opus WHT plain cell's
  `final_COST` raised by $1.00 in `cells.tsv` reads 27 of 30, rc 1 (the median, the arm total and the block total go MISSING), and the
  restored table reads 30 of 30. A first mutant ($0.0001 on a non-median cell) was EQUIVALENT at two decimals and failed nothing; it
  is recorded so that nobody counts it as a pass.
- Every cost in `cells.tsv` equals the tally's `cost_final` for the same cell, and the census line's WHT spend ($162.77) equals
  ADDENDUM 4's, measured from different files.

## The categories, and two borderline reads

Block T's categories and its audit rule apply (block T README; the rule is in its RESULTs' addenda). The plain-arm reads name the lines
read. Two are BORDERLINE under the rule "a name only the Statement supplies counts as a derivation": `clbptp01` (TEST ORACLE (partial):
`winv`/`ninv` named in an oracle that computes both by Fermat) and `clbpwp01` (WEAK TRACE: the constant name `B52` and nothing else). Both
are open to a non-author read, as block T's were.

## A correction this result makes to the tally

`../blockTW-2026-11-22/tw-cells.tsv` read `clbats02`'s `op_ok` as verbatim. `specdefs` reads it DIFFERENT: the card's body is kept as
`op_ok_value`, and `op_ok` is that body plus result-length and residues conjuncts. The tally row is corrected in place with a note.
The count of salt-diet cells that strengthen the statement (8 of 12) does not move.
