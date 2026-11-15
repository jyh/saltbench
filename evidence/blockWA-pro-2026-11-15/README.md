# Block WA, Pro half (gemini-4-argon-high): the table of record and its generator

- `cell_facts.json`: the hand's `wa_facts.py` output for the 12 cells of record, the WHT file (`facts-wht.json`, 6 cells including
  T-WA-P's `wawas1r201`) and the NTT file (`facts-ntt.json`, 6 cells) concatenated unchanged (keys sorted).
- `wa_pro_cells_gen.py`: the Flash half's `evidence/blockWA-2026-11-14/wa_cells_gen.py`, changed as its docstring lists. It reads the
  hand's score receipts in three named run dirs (not in this repository; the hand's private run record) and writes `cells.tsv`;
  `--summary` prints every figure line the result quotes; `--check <result>` asserts each occurs there (16 of 16).
- `mutant-rowcount.out`: **a defect in the inherited parser, found here and fixed, shown by going red backwards.** The Flash generator
  counted a receipt's ROWS to decide it held one cell, and a TRUNCATED cell's receipt names the cell on three rows, so every truncated cell
  read `truncated` UNREAD and each salt-diet condition's line read `truncated 0` (a false zero). With the old line restored as a mutant,
  both salt-diet lines read `truncated 0` and the four truncated cells read UNREAD; with the fix they read `truncated 2` and `yes`.
  No Flash figure moves: no Flash cell was cut, so every Flash receipt holds one row per cell.
