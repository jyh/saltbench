# RESULT — O37 block WCA, ARGON COLUMN · the agy lane × WHT and NTT × greenfield → spec-change × extras=none · n = 3 · gemini-4-argon-high
### bench (lead), 2026-11-28, on the hand's files (gemini). **§WCA8: "a result of record per model": this is Argon's; the other is `RESULT-gemini-blockWCA-flash-2026-11-28.md`.**
## 📌 The registration is `AMENDMENT-O37-blockWCA-wht-ntt-specchange-agy-2026-11-23.md` (§WCA0–§WCA8; ADDENDA 1–3), which carries block NCA by citation.
## 📌 The per-cell table of record is `evidence/blockNCA-WCA-result-2026-11-24/cells.tsv` (96 rows: both blocks, both models), printed by `nca_cells_gen.py` beside it from the hand's score receipts, `cell_facts.json` (read on the run box by `nca_facts.py`), `ctl_census.tsv` and `web_census.tsv`. Its README says how each is made.
## ⛔ Every figure line in a code block below is printed by `nca_cells_gen.py --summary`, and `nca_result_gen.py --check` asserts that this file carries every line of its block verbatim. Bus offsets in the prose are citations to where a reader can look, not measurements.

---
# §1 · WHAT RAN, AND ON WHAT
```
WCA-argon: rows 12 · conditions 4 · counted 12 · not counted 0 [-]
WCA-argon phase 2: model gemini-4-argon-high=12 · export 88b63df9c5be=12 · hook a6e064e307a8651d=12 · done_reason LANDED=12
WCA-argon clients: phase 1 fad3628ad91fe861=12 · phase 2 62f2102784bb74b7=12
WCA-argon harness-side over 12 counted: run_verdict ERROR(NO-COMMAND-PROVEN-OK)=3 OK=9 · P-PERSIST by the registered reader indeterminate=2 yes=10 · PROBE-CUT-AT-EXIT-TIMEOUT 2 [cells-wa-wht-argon-plain-r2-wcacp2 cells-wa-wht-argon-salt-r3-wcacp3] · token after the probe at the object (a hand read beside the reader) yes=12 · other events -
WCA-argon web: source_web_served CLEAN=12 · phase 2 CLEAN=12
WCA-argon phase 1: done_reason LANDED=12 · cut turns (cells with >= 1) 4 of 12 read
```
- **Sources: block WA's 12 Pro-slot cells of record (gemini-4-argon-high), copied** (§WCA2; all 24 WCA sources were eligible, ADDENDUM 3).
  Each source ran phase 1 on WA Pro's export `3fd5edf1`; each phase 2 ran on the release export and the pinned client (§WCA6 item 3).
- **The order** was §WCA4's: the tripwire `T-WCA-A` (NTT · salt-diet #1) first, read by the lead at the object (bus offset 112,695,555), then
  the argon rest by one chain. After each cell, the chain's stop check judged the lead's five standing conditions. Argon is removed from the
  client on 2026-11-30, so a cell not fired by 2026-11-30 00:00Z is unreached, never re-cut.
- **One stop, lifted.** The stop check stopped the chain after WHT · plain #2 (`wawap201`) on one AGY_ERROR (bus offset 112,911,273). The lead
  read the cell at the object (bus offset 112,917,943): none of the five conditions held. The error was written after the cell's end, by its
  orphaned client, and the persistence probe had been answered (the harness-side paragraph below). The ruling was CONTINUE, and the chain went
  on (bus offset 112,922,934).
- **Web.** Every source read CLEAN in the 11-20 census, and no phase 2 was served a search.
- **Harness-side events** (the `harness-side` line; `cells.tsv` columns `p2_results` … `p2_harness`). `run_verdict` is the launcher's
  own word on its phase-2 SERVED line; `ERROR(NO-COMMAND-PROVEN-OK)` marks a cell whose code is still scored, so §2's verdicts are the
  receipts' either way. `P-PERSIST` is the registered reader's (`agy_probes_v3.py`). Beside it, **as a hand read and not the registered
  instrument**, `nca_facts.py` reads whether the subject gave its ack token (validated against `launch.log`'s hash) AFTER the probe, in its own
  transcript or stream. **`PROBE-CUT-AT-EXIT-TIMEOUT`** names a cell that the reader read `indeterminate` although its subject DID answer the
  probe. The turn loop (`agy_turnloop_v3.py` at export `88b63df9`, lines 228-233 and 301-326) writes the probe after the FIRST opening
  result, so the second opening turn's result satisfied the probe's wait, and `--exit-timeout` (line 869) killed a subject still working
  after it had answered. L8 §A9.5's persistence cap did not bind. In each such cell the code landing predates the probe (read by hand: bus
  @112,925,340 for `cells-nca-linearscan-argon-plain-r1` and `cells-wa-wht-argon-plain-r2-wcacp2`, bus @112,991,853 for
  `cells-wa-wht-argon-salt-r3-wcacp3`), so no verdict or count moves. Their cost figures do: the kill ended a subject still working, so
  each such cell's phase-2 T and wall are FLOORS, and §3 does not mark them. Where a cut cell is the smaller side of a printed
  `salt-diet > plain` pair (the first two named above), that pair's sign is not established by its figures; where it is the larger
  (`cells-wa-wht-argon-salt-r3-wcacp3`), the sign stands (kent's read of #479, LOW R3). The turn-loop fix belongs to the next export;
  every cell of record ran this one (bus @112,917,943).

---
# §2 · CORRECTNESS, VERIFIED FIRST (the withheld B/ suite; PASS is the receipt's word: TESTS all passed, 0 REGRESSIONS failed, 0 CLAUSE_TESTS failed)
The bracket lists each counted cell's TESTS (passed/total), REGRESSIONS and CLAUSE_TESTS (failed/total), in cell order. A cell IN COMPARISONS is counted and does not leave comparisons (§1).
```
WCA-argon NTT plain: PASS 3 of 3 scored, of 3 registered [T15/15 R0/11 C0/4 T15/15 R0/11 C0/4 T15/15 R0/11 C0/4] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
WCA-argon NTT salt-diet: PASS 3 of 3 scored, of 3 registered [T15/15 R0/11 C0/4 T15/15 R0/11 C0/4 T15/15 R0/11 C0/4] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
WCA-argon WHT plain: PASS 3 of 3 scored, of 3 registered [T16/16 R0/11 C0/5 T16/16 R0/11 C0/5 T16/16 R0/11 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
WCA-argon WHT salt-diet: PASS 3 of 3 scored, of 3 registered [T16/16 R0/11 C0/5 T16/16 R0/11 C0/5 T16/16 R0/11 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
WCA-argon FULL PASS plain 6 of 6 counted · in comparisons 6 of 6
WCA-argon FULL PASS salt-diet 6 of 6 counted · in comparisons 6 of 6
```
- **Every counted cell passes the withheld B/ suite in full, both problems and both arms.** Both conditions of each problem are at CEILING, so this
  block says nothing about a difference between the arms in pass rate (UNRESOLVED-BY-CEILING).
- **The counted cells whose launcher `run_verdict` reads `ERROR(NO-COMMAND-PROVEN-OK)`** (the `harness-side` line gives their number) are
  scored like any other cell, and each passes in full (`cells.tsv`, columns `p2_run_verdict` and `verdict`).

---
# §3 · COST, AS A SIGN ONLY
```
WCA-argon NTT phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 1779387 / 4011676 · #2 3745421 / 5428205 · #3 2427752 / 7073286 · salt-diet > plain in 3 of 3 pairs in comparisons
WCA-argon NTT phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 619.8 / 781.8 · #2 645.2 / 953.2 · #3 554.0 / 1404.2 · salt-diet > plain in 3 of 3 pairs in comparisons
WCA-argon WHT phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 1823565 / 5784277 · #2 1514383 / 6783624 · #3 2458338 / 4384354 · salt-diet > plain in 3 of 3 pairs in comparisons
WCA-argon WHT phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 502.2 / 1016.7 · #2 707.0 / 1093.3 · #3 610.9 / 1281.5 · salt-diet > plain in 3 of 3 pairs in comparisons
```
T is the agy meter's token total for phase 2; wall is phase 2's turn-loop wall. A rep prints only where its cell is COUNTED, and a pair
counts only when both its cells are in comparisons. A sign, never a premium (§WCA5 carries NCA §NCA5), and no magnitude is claimed.

---
# §4 · THE REGISTERED PREDICTIONS (NCA §NCA5 (i)–(iii), carried by §WCA5); A MISS IS A RESULT
```
WCA-argon predictions: (i) ELIGIBLE plain 6/6 salt-diet 6/6 · REACHED plain 6/6 salt-diet 6/6 · (ii) cut-turn incidence plain vs salt-diet: NTT 0/3 vs 0/3 · WHT 0/3 vs 0/3 · (iii) done_reason LANDED=12
WCA-argon prediction verdicts: (i) ELIGIBLE salt-diet lower: MISS · REACHED salt-diet lower: MISS · (ii) salt-diet >= plain in 2 of 2 conditions with both arms in comparisons · (iii) CELL-KILLED cells 0
```
- **(i)** "lower for salt-diet": **MISS**, at a tie. Every source was eligible by the census (ADDENDUM 3), so neither arm lost a cell before
  phase 2.
- **(ii)** "salt-diet's cut-turn incidence ≥ plain's": no counted cell was cut in either arm. **Holds, trivially, at 0 ≥ 0**, so (ii) was not
  tested in the direction it was registered to watch.
- **(iii)** CELL-KILLED binds no cell. **Holds.**

---
# §5 · WHAT THIS RESULT CANNOT ESTABLISH
§WCA8 (NCA §NCA8, §NCA9 and §NCA10 carried, for NTT and WHT): no magnitude; nothing about gemini-3.1-pro-high; nothing Flash-versus-argon
or Claude-versus-agy. §WCA6 item 6: one author built both tasks and both B/ suites and leads this block, and NTT's reference proves less than
WHT's. Nothing here says whether the salt method helps or hurts. Any public sentence is the Captain's.
