# Block TA (O37, agy lane × block N's six × statement): the table of record and its generator

The result is `harness/systems-v3/RESULT-gemini-blockTA-2026-11-20.md`. The registration is
`harness/systems-v3/AMENDMENT-O37-statement-six-agy-2026-11-17.md`; its price files are in `evidence/blockTA-2026-11-17/`.

**Tracked copies of the hand's record** (written by `ta_collect.py` from the hand's private run record, two score dirs it names; nothing computed):
- `flash-tally.tsv`, `argon-tally.tsv`: the hand's tallies, byte copies. One row per cell; the last column holds the cell's statement CATEGORY
  and the hand's reading behind it, with every correction and the lead's ruling cited on the row.
- `cell_facts.json`: `wa_facts.py` per cell (read on the run box from each cell's own `ctl/`), the 72 files concatenated, sorted by id.
  Flash's T-TA-F cell `talfs101` comes from the file the hand wrote under the tripwire's name (`facts-ttaf.json`).
  ⚠️ Its `cut_turns` and `cut_turns_all` count `print timeout` LINES (3 per timeout event), not turns; the result reads events from `events.tsv`.
- `receipts.tsv`: per cell, from its `score_wave_v3.sh` receipt: verdict, TESTS, the scorer's TRUNCATED figure (also LINES), interface hash,
  and the receipt's sha256/16. The receipts themselves are not copied (their first line names the scorer's private tool paths).
- `meters.tsv`: per cell, from `agy_meter_v3.py`: requested model, served models (main conversation only), meter verdict, T.
- `sextets/`: the hand's per-problem sextet files and per-wave total lines, as posted on the bus during the waves (byte copies).
- `ct-sweep-2026-11-20.txt`: the THE LINE sweep's instrument output over the 36 plain cells.

**Read-only censuses taken on the run box for this result** (each script is here; each output names every TA cell dir, 73, including the
one 503-discarded attempt):
- `events.tsv` by `ta_events.sh`: per cell dir, `^AGY_ERROR` lines (timeout EVENTS) and `print timeout` lines in `ctl/agy-stderr-1.txt`.
- `swarm.tsv` by `ta_swarm_census.py`: per cell dir, the client's `swarm` tool steps in the main stream, the models of each worker the
  subject ADDED, and the last status read's posts per member. A worker's own conversation is not in the main stream; see the next file.
- `workers.txt` by `ta_worker_read.py`: the six workers' OWN records, which the client keeps in the cell's agy home
  (`.agyhome/.gemini/antigravity-cli/brain/<worker id>/`): window, response models, tokens, every tool call, every argument naming a source
  file, commits inside the window, and the final tree's files under `tests/refute` and `docs/reviews` with the commit that added each.

**The generator:** `ta_result_gen.py` reads the files above (and `../blockTA-2026-11-17/ta_price.out`, `ta_recut_argon.out`) and nothing else.
`python3 ta_result_gen.py > cells.tsv` writes the per-cell table; `--summary` prints every figure line the result quotes; `--check <result>`
asserts each occurs there verbatim (72 of 72; a control with one digit changed reads one MISSING, rc 1). A cell missing from any input REFUSES.

`mutant-partial.out`: **a defect in this generator's first draft, fixed and shown by going red backwards.** The category reader tried the
qualifier `USED (partial: k of n …)` after the plain `USED` prefix, so both partial Flash cells read USED (salt-diet `USED 17`). With the old
order restored as a mutant the line reads `USED 17`; with the fix, `USED 15 · USED (partial) 2`.

**The census lines** (added 2026-11-22, bench, when the branch landed on `main`): `ta_census_line.py` prints census ADDENDUM 50's three
block TA lines from `cells.tsv` (conditions, n per condition, cells of record, LANDED, PASS, MODEL-SEAM flagged). `--check <census>`
exits 1 unless each occurs there verbatim. A mutant of one figure fails it (2 of 3, rc 1).

**The 2026-11-22 category audit** (`audit-2026-11-22/`): `tnames.sh` (block T's needle v2) and its run-box driver `ta-tnames.sh`, the 36-cell
output, and the 7 non-author verdicts. Nothing moved; the RESULT's addendum says why.
