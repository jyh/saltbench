# RESULT — O37 block WCA, FLASH COLUMN · the agy lane × WHT and NTT × greenfield → spec-change × extras=none · n = 3 · gemini-3.8-flash-high
### bench (lead), 2026-11-28, on the hand's files (gemini). **§WCA8: "a result of record per model": this is Flash's; the other is `RESULT-gemini-blockWCA-argon-2026-11-28.md`.**
## 📌 The registration is `AMENDMENT-O37-blockWCA-wht-ntt-specchange-agy-2026-11-23.md` (§WCA0–§WCA8; ADDENDA 1–3), which carries block NCA by citation.
## 📌 The per-cell table of record is `evidence/blockNCA-WCA-result-2026-11-24/cells.tsv` (96 rows: both blocks, both models), printed by `nca_cells_gen.py` beside it from the hand's score receipts, `cell_facts.json` (read on the run box by `nca_facts.py`), `ctl_census.tsv` and `web_census.tsv`. Its README says how each is made.
## ⛔ Every figure line in a code block below is printed by `nca_cells_gen.py --summary`, and `nca_result_gen.py --check` asserts that this file carries every line of its block verbatim. Bus offsets in the prose are citations to where a reader can look, not measurements.

---
# §1 · WHAT RAN, AND ON WHAT
```
WCA-flash: rows 12 · conditions 4 · counted 12 · not counted 0 [-]
WCA-flash phase 2: model gemini-3.8-flash-high=12 · export 88b63df9c5be=12 · hook a6e064e307a8651d=12 · done_reason LANDED=12
WCA-flash clients: phase 1 fad3628ad91fe861=12 · phase 2 62f2102784bb74b7=12
WCA-flash harness-side over 12 counted: run_verdict OK=12 · P-PERSIST by the registered reader yes=12 · PROBE-CUT-AT-EXIT-TIMEOUT 0 [-] · token after the probe at the object (a hand read beside the reader) yes=12 · other events -
WCA-flash web: source_web_served CLEAN=12 · phase 2 CLEAN=12
WCA-flash phase 1: done_reason LANDED=12 · cut turns (cells with >= 1) 0 of 12 read
```
- **Sources: block WA's 12 Flash cells of record, copied** (§WCA2: NCA §NCA2's Flash rule; all 24 WCA sources were eligible, ADDENDUM 3).
- **Two exports and two clients per pair** (§WCA6 item 3): each source ran phase 1 on WA's export `6413289d` and its client, before WA
  ADDENDUM 3's per-cell environment fix and ADDENDUM 5's `agentMode ""`; each phase 2 ran on the release export and the pinned client. So the
  client's own sandbox setting differs between a pair's phases. Nothing here compares a Flash figure with an argon one.
- **The order** was §WCA4's: the tripwire `T-WCA-F` (NTT · salt-diet #1) first, read by the lead at the object (bus offset 112,541,157), then the
  Flash rest by one chain (the hand's completion post, bus offset 112,670,115).
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
WCA-flash NTT plain: PASS 3 of 3 scored, of 3 registered [T15/15 R0/11 C0/4 T15/15 R0/11 C0/4 T15/15 R0/11 C0/4] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
WCA-flash NTT salt-diet: PASS 3 of 3 scored, of 3 registered [T15/15 R0/11 C0/4 T15/15 R0/11 C0/4 T15/15 R0/11 C0/4] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
WCA-flash WHT plain: PASS 3 of 3 scored, of 3 registered [T16/16 R0/11 C0/5 T16/16 R0/11 C0/5 T16/16 R0/11 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
WCA-flash WHT salt-diet: PASS 3 of 3 scored, of 3 registered [T16/16 R0/11 C0/5 T16/16 R0/11 C0/5 T16/16 R0/11 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
WCA-flash FULL PASS plain 6 of 6 counted · in comparisons 6 of 6
WCA-flash FULL PASS salt-diet 6 of 6 counted · in comparisons 6 of 6
```
- **Every cell passes the withheld B/ suite in full, both problems and both arms.** Both conditions of each problem are at CEILING, so this
  block says nothing about a difference between the arms in pass rate (UNRESOLVED-BY-CEILING).

---
# §3 · COST, AS A SIGN ONLY
```
WCA-flash NTT phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 6159835 / 13979757 · #2 8492982 / 17894490 · #3 7359098 / 16985258 · salt-diet > plain in 3 of 3 pairs in comparisons
WCA-flash NTT phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 528.9 / 912.7 · #2 638.4 / 1015.6 · #3 594.8 / 841.5 · salt-diet > plain in 3 of 3 pairs in comparisons
WCA-flash WHT phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 6660527 / 17280322 · #2 4921388 / 12513746 · #3 6363806 / 16004694 · salt-diet > plain in 3 of 3 pairs in comparisons
WCA-flash WHT phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 569.6 / 977.6 · #2 521.5 / 890.2 · #3 574.1 / 1398.5 · salt-diet > plain in 3 of 3 pairs in comparisons
```
T is the agy meter's token total for phase 2; wall is phase 2's turn-loop wall. A rep prints only where its cell is COUNTED, and a pair
counts only when both its cells are in comparisons. A sign, never a premium (§WCA5 carries NCA §NCA5), and no magnitude is claimed.

---
# §4 · THE REGISTERED PREDICTIONS (NCA §NCA5 (i)–(iii), carried by §WCA5); A MISS IS A RESULT
```
WCA-flash predictions: (i) ELIGIBLE plain 6/6 salt-diet 6/6 · REACHED plain 6/6 salt-diet 6/6 · (ii) cut-turn incidence plain vs salt-diet: NTT 0/3 vs 0/3 · WHT 0/3 vs 0/3 · (iii) done_reason LANDED=12
WCA-flash prediction verdicts: (i) ELIGIBLE salt-diet lower: MISS · REACHED salt-diet lower: MISS · (ii) salt-diet >= plain in 2 of 2 conditions with both arms in comparisons · (iii) CELL-KILLED cells 0
```
- **(i)** "lower for salt-diet": **MISS**, at a tie. Every source was eligible by the census, so neither arm lost a cell before phase 2.
- **(ii)** "salt-diet's cut-turn incidence ≥ plain's": no counted cell was cut in either arm. **Holds, trivially, at 0 ≥ 0**, so (ii) was not
  tested in the direction it was registered to watch.
- **(iii)** CELL-KILLED binds no cell. **Holds.**

---
# §5 · WHAT THIS RESULT CANNOT ESTABLISH
§WCA8 (NCA §NCA8, §NCA9 and §NCA10 carried, for NTT and WHT): no magnitude; nothing about gemini-3.1-pro-high; nothing Flash-versus-argon
or Claude-versus-agy. §WCA6 item 6: one author built both tasks and both B/ suites and leads this block, and NTT's reference proves less than
WHT's. Nothing here says whether the salt method helps or hurts. Any public sentence is the Captain's.
