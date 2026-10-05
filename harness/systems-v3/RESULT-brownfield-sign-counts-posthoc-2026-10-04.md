# RESULT (POST HOC): brownfield salt-diet ÷ plain dollars, summarised by the "$4 sign counts" rule

**Post hoc.** The registered summary (`REGISTRATION-cost-tables-v3-2026-09-29.md`, printed as "$4 sign counts" in
`RESULT-cost-tables-v3-2026-09-29.md`) covers greenfield only. This file applies the same rule to the brownfield
bare and statement ratios that the result file already lists under "$ brownfield ratios (in the file, not in $4)".
Nothing here was registered. It is a descriptive reading with no test and no p-value, and it gives no verdict on
either arm. Brownfield × spec-change is not in the matrix.

## How it was printed

`harness/systems-v3/brownfield_signs_posthoc.py` (blob c248e9df5824) imports `tables_v3.py` (blob 636d91092996)
and `tables_v2.py` (blob 5044625fb47e) unchanged. It reuses their `build`, `summarise`, `ratio`, `sign` and the
`$4` block's median, so the rule comes from the code, not from a re-derivation. The inputs are the ones the
published file names: `CELLMAP-descriptive-tables-v2-2026-09-27.tsv` and `evidence/v3-cost-tables-2026-09-28`, at
repo head `01e1ae5b32de`, with every input blob equal to the ones in the published header.

    python3 harness/systems-v3/brownfield_signs_posthoc.py \
      harness/systems-v3/CELLMAP-descriptive-tables-v2-2026-09-27.tsv \
      evidence/v3-cost-tables-2026-09-28 \
      harness/systems-v3/RESULT-cost-tables-v3-2026-09-29.md

**Control, run in the same process before any brownfield row is printed:** the same function over the
GREENFIELD grid must reproduce all 12 published "$4 sign counts" rows exactly, or the script exits 1 and prints
nothing. It printed `CONTROL greenfield $4 rows reproduced: 12 of 12`. Separately, `tables_v3.py` re-run over the
same inputs reproduced `RESULT-cost-tables-v3-2026-09-29.md` byte for byte below its header line.

## The rule, stated because a plain median of the determinate ratios does not reproduce it

The median is taken over **every ratio that has a value**, including ratios whose sign is indeterminate ("bounds
only (x)", printed in the table as the value in parentheses) and bounded ones (`≥ x`, `≤ x`). A cell is `—` when
either condition is inexpressible, declared or unmeasured. The `k of m` column counts only ratios whose sign is
determinate. So a median can rest on more ratios than `m`. Example: greenfield claude-opus-5 bare is
"1 of 1" with a median of 1.37 over five values.

## Brownfield sign counts, per model per treatment (modelled list-price dollars)

| model | treatment | k of m ratios > 1 | indeterminate | median of the ratios | bounded among them |
|---|---|---|---|---|---|
| claude-opus-5 | bare | 4 of 4 | FreeList | 1.84 | 1 |
| claude-opus-5 | statement | 1 of 1 | Crc32, FreeList, LZW | 1.37 | 3 |
| claude-sonnet-5 | bare | 3 of 3 | Crc32, Paxos | 12.43 | 4 |
| claude-sonnet-5 | statement | 4 of 4 | none | 7.48 | 3 |
| gemini-3.1-pro-high | bare | 4 of 4 | none | 6.75 | 2 |
| gemini-3.1-pro-high | statement | 4 of 4 | none | 6.55 | 2 |
| gemini-3.8-flash-high | bare | 5 of 5 | none | 2.53 | 0 |
| gemini-3.8-flash-high | statement | 4 of 4 | none | 2.31 | 0 |

Ratios that are `—` and so not in any median: Paxos × statement for all four models (inexpressible in brownfield),
and gemini-3.1-pro-high Crc32 × bare (the salt-diet condition's dollars are unmeasured; see the published file's
"Unmeasured cells" table). Each ratio is listed per problem in the published file under "$ brownfield ratios".

## In one table (median salt-diet ÷ plain dollars over the 5 problems)

| model | brownfield no spec (bare) | brownfield spec given (statement) |
|---|---|---|
| claude-opus-5 | 1.84× | 1.37× † |
| claude-sonnet-5 | 12.43× | 7.48× |
| gemini-3.1-pro-high | 6.75× | 6.55× |
| gemini-3.8-flash-high | 2.53× | 2.31× |

† fewer than 3 determinate ratios (claude-opus-5 statement: 1 of 1). Every other cell rests on 3 to 5. The
statement medians are over 4 problems (Paxos is `—`), as is gemini-3.1-pro-high bare (Crc32 is `—`). A `≥` ratio is a lower bound (its salt-diet arm is at a floor) and a `≤` ratio an
upper bound (its plain arm is); the medians carry them at their printed values. claude-sonnet-5 bare has 4 bounded
ratios of 5 (one `≤`, two `≥`, one bounds only), so read that median as the least certain in the table.
