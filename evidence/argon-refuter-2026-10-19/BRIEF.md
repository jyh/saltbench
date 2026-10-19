# BRIEF — a non-author read of one result file

You are reading a result file you did not write. Your job is to check it against its own data.

## The files (use ONLY these files, in this directory)

- `harness/systems-v3/RESULT-claude-blockSBS-2026-09-21.md` — the result file under review.
- `evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv` — the per-cell table the result says every figure comes from (24 rows; lines starting with `#` are comments).
- `evidence/claude-lane-blocks-2026-09-21/blockSBS-retention-decomp.tsv` — a second table it cites for retention.

Do not consult any other copy of these files, any repository, or any network source. If a figure cannot be checked from these files, say so; do not guess.

## What to do

1. For EVERY numeric figure in §1, §2, §3, §4 and §T of the result file, re-derive it from the tables and give one row:

   `FIGURE | WHERE (section, row/line) | STATED | DERIVED | VERDICT | HOW (one line: the rows/columns and the operation)`

   VERDICT is one of:
   - `CONFIRMED` — your derivation gives the stated value.
   - `WRONG` — your derivation gives a different value (put yours in DERIVED).
   - `NOT DERIVABLE` — the tables do not carry what is needed (say what is missing).

   Medians over an even count are the mean of the two middle values. Keep the file's own rounding.

2. Then list every prose CLAIM (not a figure) that the tables contradict, one per line, with the rows that contradict it. If there are none, write `NO CONTRADICTED CLAIMS`.

3. End with one line: `SUMMARY: <n> figures checked · <n> CONFIRMED · <n> WRONG · <n> NOT DERIVABLE · <n> contradicted claims`.

Report what you find. A finding you are not sure of goes in with your reason; an empty WRONG list is a valid answer if that is what the data says.
