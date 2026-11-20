# The cut-turns unit correction (bench row 11, 2026-11-20, gemini)

**The defect.** `wa_facts.py` (`cut_turns_all`), block NA's `cell_facts.py` (`cut_turns`) and the scorer's TRUNCATED figure
(`score_wave_v3.sh:281`, private harness tree) count stderr LINES that contain `print timeout`. They report those counts as turns.
The client of blocks WA and TA (agy 1.5.x) writes three such lines per timeout, so there the count is three times the number of turns cut.

**The instrument, read first.** `pt_shapes.sh` (run read-only on the run box, output `pt_shapes.tsv`) classifies every stderr file
with a hit:

| reading | command | result |
|---|---|---|
| shape by month | `python3 cut_unit_gen.py --eras` | 2026-09: 1-line, 54 files · 2026-10: 1-line, 40 · 2026-11: 3-line, 11 · MIXED 0 |
| line counts reproduce the cell facts | `python3 cut_unit_gen.py --control` | NA 73/73 (`cut_turns`), WA Flash 12/12 and WA Pro 12/12 (`cut_turns_all`) |
| corrected WA figures | `python3 cut_unit_gen.py --summary` | WA Pro salt-diet: WHT 2 of 11 and NTT 2 of 10 (printed as 6 and 6); every other WA figure 0 |
| corrected lines present in the RESULTs | `cut_unit_gen.py --check <file>` | red before the addenda (0 of 10 in the Pro RESULT), green after |

`cut_units.sh` → `cut_units.tsv` is the first, narrower read: the 97 NA and WA cells of record in `cells-in.txt`. Block NA's
client writes no `AGY_ERROR` line, so there the event is the one `[agy] print timeout` line.

**Limits.** Files deleted from the run box before 2026-11-20 are not in the census. An events count is recovered only where the stderr
file survives, and every figure below that moved had its file present.

## The copies census

Scope: saltbench at `c78261ff` (`git grep -i` for `cut turn`, `turns cut`, `turns-cut`, `cut_turns`, `print timeout`, `TURNS-CUT`,
`turn(s) cut`, `N turns were cut`, on flattened text where it was prose), the paper, the private harness tree, and the bus from 11/13.

| surface | figure | unit | action |
|---|---|---|---|
| RESULT-gemini-blockWA-pro-2026-11-15 §2 | cut turns 6 of 11, 6 of 10 (salt-diet) | lines | **MOVED**: addendum, 2 of 11, 2 of 10 |
| RESULT-gemini-blockWA-flash-2026-11-14 §2 | cut turns 0 (all four) | lines = events at 0 | annotated by addendum; no figure moves |
| AMENDMENT-O37-wht-ntt ADDENDUM 4 | `wawas1r01` "6 turns were cut" | lines | **MOVED**: ADDENDUM 7, 2 turns (cell not of record) |
| AMENDMENT-O37-wht-ntt §WA, :33 | "cut turns ÷ turns" (rule) | — | ADDENDUM 7 fixes the unit as events |
| AMENDMENT-O37-nine-greenfield ADDENDUM 4 | the rule; `nalbpst01` 7; `nabhfs03` 12 | events (1-line era) | ADDENDUM 6: correct as printed; the rule counts `[agy]` lines from now on |
| RESULT-gemini-blockNA-2026-09-28 | 26 of 104, 18 of 72, `naaeps01` 6 of 7 | events (1-line era, control 73/73) | not moved; NA's own `nabhfs03` denominator note stands |
| AMENDMENT-O37-statement-six §TA3 (i) | TURNS-CUT incidence | not stated | ADDENDUM 9: TA read cells, events beside; same sign; unit for the future is the lead's |
| RESULT-gemini-blockTA-2026-11-20 | truncated cells / events / lines | already events | none |
| levels 4–8, ZF, x86, stage and pilot documents | per-turn cut counts | events (all pre-11-15 hits are 1-line) | not this defect |
| AMENDMENT/RESULT O90 stage 1 | `UNSCORED(print timeout)` | a cause class, not a count | not this sense |
| paper/saltbench-v1.tex | ZF "20 of 66 salt-diet roots" | roots | not this sense |
| `wa_facts.py`, `wa_pro_cells_gen.py`, cell facts | `cut_turns(_all)` | lines (documented as lines at `wa_facts.py:9`) | not edited: the RESULTs' frozen lines still check green; the corrected lines are checked by `cut_unit_gen.py` |
| `score_wave_v3.sh:281` (private harness tree) | "N turn(s) cut" per cell; the truncated-cell count | lines; cells | the lead's tool, not edited. Remedy: count `^\[agy\] print timeout` |
| bus @103149014, @103173999 | `wawas1r01` "6 turns cut" | lines | covered by wht-ntt ADDENDUM 7 (2 turns) |
| bus @103288042, @103291991 | `wawas1r201` "3 turns cut" | lines | covered by the Pro addendum (1 turn) |
| bus @106346546 | `tabfs101` "TRUNCATED 3 turn(s)" | lines | corrected on the bus at @106386366 (1 turn) |
