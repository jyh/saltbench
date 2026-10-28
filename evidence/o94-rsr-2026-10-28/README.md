# The review-surface ratio over the pilot's 181 conditions (O94 candidate; a read, not a result of record)

bench, 2026-10-28. Commissioned at council 2026-10-27 as the lead's own instrument: over SaltBench's 181 conditions
of record, spec lines : (implementation + proof) lines per cell, from the artifacts on disk, reported as a
distribution per arm and problem.

**It is declared as a PROXY for review attention and is not a measure of it.** It counts physical lines. A line of
specification is not a unit of a reviewer's time, and nothing here says a reviewer read any of these lines. No claim
is made that the salt method helps or hurts review.

## What was measured

- **Population:** the cells of record for all 181 conditions, n = 3 each: 543 rows (cell × condition) over 520
  distinct cells, because 23 cells are the record for two conditions. The cell list and each cell's record root
  are the join from census ADDENDUM 37 (`evidence/midcell-gap-2026-10-17/`). Every row's repo and source was found
  on the run box: 0 missing.
- **Subject:** each cell's Rust files **on disk at the end of the run** (`solution.rs`, any other subject `.rs`
  file, and `tests/**.rs`). The harness's own files (`interface.rs`, `bin/`, `docs/`, `.seat/`, `target/`) are
  excluded. 20 rows have a source file that differs from the cell's HEAD commit; the disk copy is the one counted.
- **Classes**, one per line, by `harness/systems-v3/rsr.py` (its docstring gives every rule):
  SPEC (spec fns, an exec fn's requires/ensures, ghost fields) · PROOF (proof fns whole, proof blocks, Verus asserts,
  loop invariants and decreases) · IMPL (all other code) · TEST · COMMENT · BLANK.
- **ratio = SPEC / (IMPL + PROOF)**, over the final source (`all`) and over the lines the subject wrote (`sub`:
  lines not matched to the seed commit by difflib). The two differ most in brownfield, where the seed holds code.

## The distribution (`report.tsv`, from `rsr.py --report rsr-cells.tsv`)

Five-number summaries (min / q1 / median / q3 / max). Line medians are for the final source.

| arm | problem | n | ratio, all | ratio, subject-written | SPEC med | PROOF med | IMPL med | TEST/IMPL med | PROOF = 0 |
|---|---|---|---|---|---|---|---|---|---|
| plain | Crc32 | 60 | 0 (all) | 0 (all) | 0 | 0 | 36 | 5.068 | 60 |
| plain | FreeList | 60 | 0 (all) | 0 (all) | 0 | 0 | 161 | 3.250 | 60 |
| plain | LRU | 60 | 0 (all) | 0 (all) | 0 | 0 | 74 | 5.252 | 60 |
| plain | LZW | 60 | 0 (all) | 0 (all) | 0 | 0 | 90.5 | 3.215 | 60 |
| plain | Paxos | 36 | 0 (all) | 0 (all) | 0 | 0 | 230 | 2.187 | 36 |
| salt-diet | Crc32 | 60 | 0.031 / 0.192 / 0.257 / 0.286 / 0.591 | 0.031 / 0.208 / 0.274 / 0.329 / 0.867 | 50 | 131 | 75.5 | 1.945 | 0 |
| salt-diet | FreeList | 57 | 0.012 / 0.261 / 0.364 / 0.532 / 1.384 | 0.017 / 0.302 / 0.402 / 0.598 / 1.529 | 298 | 133 | 471 | 0.465 | 9 |
| salt-diet | LRU | 60 | 0.188 / 0.304 / 0.406 / 0.486 / 0.939 | 0.195 / 0.333 / 0.445 / 0.595 / 1.227 | 142.5 | 150 | 212 | 1.106 | 1 |
| salt-diet | LZW | 57 | 0.000 / 0.179 / 0.221 / 0.421 / 0.986 | 0.102 / 0.188 / 0.246 / 0.446 / 2.649 | 144 | 372 | 209 | 0.844 | 3 |
| salt-diet | Paxos | 33 | 0.140 / 0.222 / 0.239 / 0.305 / 1.265 | 0.143 / 0.238 / 0.256 / 0.455 / 1.871 | 243 | 619 | 420 | 0.564 | 0 |

Row counts are 60 per problem and arm (4 models × 5 field-and-extras conditions × n 3) except where the matrix has
none: Paxos has no statement arm (36 and 33), and the census's 3 DECLARED conditions — claude-sonnet-5 × greenfield ×
salt-diet × spec-change on FreeList, LZW and Paxos — have no cells, so those three salt-diet rows read 57, 57 and 33.
The table holds 181 conditions; 200 − 16 inexpressible − 3 declared = 181. Per-cell rows, including the model, field
and extras columns this table pools over, are in `rsr-cells.tsv`.

## The limits, beside the numbers

1. **A plain arm reads 0 by construction.** The instrument's SPEC is Verus specification, and a plain arm writes no
   Verus. Its tests are counted as TEST and are not folded into SPEC, so the plain ratio says nothing about how a
   plain cell is reviewed. TEST/IMPL is printed beside it for that reason; it is a different quantity and the two
   columns are not comparable across arms.
2. **The classifier is lexical, not a Verus parser.** A line is classed by how it starts: a clause on its fn's header
   line is IMPL, and an assert after other code on the same line is IMPL. It is validated only by `--selftest`
   against two hand-labelled fixtures (below).
3. **Where a lemma's statement goes is a choice.** A proof fn is PROOF in whole, its own requires/ensures included,
   because a lemma's statement is scaffolding for the proof and not the component's specification. Counting lemma
   statements as SPEC would raise every salt-diet ratio.
4. **"Subject-written" is a line match against the seed**, so a line the subject rewrote to the seed's exact text
   counts as seed.
5. **13 salt-diet rows have PROOF = 0, all in the Gemini lane** (gemini-3.1-pro-high 7, gemini-3.8-flash-high 6; no
   Claude row). They wrote spec fns and ensures clauses with no proof constructs. Two were read at the object
   (`l5ft01`: every `decreases` in it is inside a recursive spec fn; `s3fs01`: no proof construct at all). One
   (`l6vgfs02`, LZW) wrote a 49-line file with no Verus, so SPEC is 0 too. Those rows are in the table as measured.
6. Counted over the cells of record only. A cell's correctness is not an input: a failed cell's lines are counted
   like a passing cell's.

## How the instrument was checked

- **Red first, by hand:** before `rsr.py` existed, lines 1–150 of one real cell (`s3cs01`, Gemini Pro, Crc32
  salt-diet) were labelled line by line (`rsr-fixtures/s3cs01-head150.labels`: SPEC 41, PROOF 22, IMPL 66,
  COMMENT 6, BLANK 15). A synthetic fixture covers the constructs that cell lacks (proof fns, multi-line requires,
  ghost fields, block comments, unbalanced braces and parens inside a string, a test module, code outside
  `verus!`). Its first labels were wrong against its own bytes (57 lines for a 56-line file, and `} // verus!`
  labelled a comment); they were corrected before the tool ran.
- **Mutants:** ten single-rule mutants of the classifier, each run against both fixtures. Nine failed at once. The
  string-blanking mutant passed, because the fixture's string held a balanced brace. The string now holds an
  unbalanced `{` and `(`, and the mutant fails on 15 lines.
- **The population found a defect the fixtures missed:** the first full run read 11 plain cells with PROOF > 0.
  The statement rule matched Rust's runtime `assert!` macro. A fixture line was added and went red on that line
  alone; the rule was fixed and the population re-run. The plain arm now reads PROOF 0 in all 276 rows.

## Reproduce

On the run box, from a directory holding `rsr.py`, `rsr-fixtures/` and the ADDENDUM 37 join:
`python3 rsr.py --selftest` (both PASS), then for each join row
`python3 rsr.py --cell ~/<root>/<cell>/repo --id <cell>`, then `python3 rsr.py --report rsr-cells.tsv`.
