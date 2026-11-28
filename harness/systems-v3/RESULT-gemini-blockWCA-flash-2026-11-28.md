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

---
# §2 · CORRECTNESS, VERIFIED FIRST (the withheld B/ suite; PASS is the receipt's word: TESTS all passed, 0 REGRESSIONS failed, 0 CLAUSE_TESTS failed)
The bracket lists each counted cell's TESTS (passed/total), REGRESSIONS and CLAUSE_TESTS (failed/total), in cell order. A cell IN COMPARISONS is counted and does not leave comparisons (§1).
```
WCA-flash NTT plain: PASS 3 of 3 scored, of 3 registered [T15/15 R0/11 C0/4 T15/15 R0/11 C0/4 T15/15 R0/11 C0/4] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ UNREAD of 3 scored · in comparisons UNREAD of 3 scored
WCA-flash NTT salt-diet: PASS 3 of 3 scored, of 3 registered [T15/15 R0/11 C0/4 T15/15 R0/11 C0/4 T15/15 R0/11 C0/4] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ UNREAD of 3 scored · in comparisons UNREAD of 3 scored
WCA-flash WHT plain: PASS 3 of 3 scored, of 3 registered [T16/16 R0/11 C0/5 T16/16 R0/11 C0/5 T16/16 R0/11 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ UNREAD of 3 scored · in comparisons UNREAD of 3 scored
WCA-flash WHT salt-diet: PASS 3 of 3 scored, of 3 registered [T16/16 R0/11 C0/5 T16/16 R0/11 C0/5 T16/16 R0/11 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ UNREAD of 3 scored · in comparisons UNREAD of 3 scored
WCA-flash FULL PASS plain 6 of 6 counted · in comparisons UNREAD
WCA-flash FULL PASS salt-diet 6 of 6 counted · in comparisons UNREAD
```
- **Every cell passes the withheld B/ suite in full, both problems and both arms.** Both conditions of each problem are at CEILING, so this
  block says nothing about a difference between the arms in pass rate (UNRESOLVED-BY-CEILING).

---
# §3 · COST, AS A SIGN ONLY
```
WCA-flash NTT phase-2 T by rep (plain / salt-diet): #1 6159835 / 13979757 · #2 8492982 / 17894490 · #3 7359098 / 16985258 · salt-diet > plain in 3 of 3 pairs
WCA-flash NTT phase-2 wall_s by rep (plain / salt-diet): #1 528.9 / 912.7 · #2 638.4 / 1015.6 · #3 594.8 / 841.5 · salt-diet > plain in 3 of 3 pairs
WCA-flash WHT phase-2 T by rep (plain / salt-diet): #1 6660527 / 17280322 · #2 4921388 / 12513746 · #3 6363806 / 16004694 · salt-diet > plain in 3 of 3 pairs
WCA-flash WHT phase-2 wall_s by rep (plain / salt-diet): #1 569.6 / 977.6 · #2 521.5 / 890.2 · #3 574.1 / 1398.5 · salt-diet > plain in 3 of 3 pairs
```
T is the agy meter's token total for phase 2; wall is phase 2's turn-loop wall. A sign, never a premium (§WCA5 carries NCA §NCA5), and no
magnitude is claimed.

---
# §4 · THE REGISTERED PREDICTIONS (NCA §NCA5 (i)–(iii), carried by §WCA5); A MISS IS A RESULT
```
WCA-flash predictions: (i) ELIGIBLE plain 6/6 salt-diet 6/6 · REACHED plain 6/6 salt-diet 6/6 · (ii) cut-turn incidence plain vs salt-diet: NTT UNREAD · WHT UNREAD · (iii) done_reason LANDED=12
WCA-flash prediction verdicts: (i) ELIGIBLE salt-diet lower: MISS · REACHED salt-diet lower: MISS · (ii) salt-diet >= plain in 0 of 0 conditions with both arms in comparisons · unread: NTT WHT · (iii) CELL-KILLED cells 0
```
- **(i)** "lower for salt-diet": **MISS**, at a tie. Every source was eligible by the census, so neither arm lost a cell before phase 2.
- **(ii)** "salt-diet's cut-turn incidence ≥ plain's": no cell was cut in either arm. The verdict reads in comparisons, so it waits on the ctl
  census of these cells where the line says `unread`.
- **(iii)** CELL-KILLED binds no cell. **Holds.**

---
# §5 · WHAT THIS RESULT CANNOT ESTABLISH
§WCA8 (NCA §NCA8, §NCA9 and §NCA10 carried, for NTT and WHT): no magnitude; nothing about gemini-3.1-pro-high; nothing Flash-versus-argon
or Claude-versus-agy. §WCA6 item 6: one author built both tasks and both B/ suites and leads this block, and NTT's reference proves less than
WHT's. Nothing here says whether the salt method helps or hurts. Any public sentence is the Captain's.
