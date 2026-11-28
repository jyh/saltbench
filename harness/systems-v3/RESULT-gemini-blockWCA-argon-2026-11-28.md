# RESULT — O37 block WCA, ARGON COLUMN · the agy lane × WHT and NTT × greenfield → spec-change × extras=none · n = 3 · gemini-4-argon-high
### bench (lead), 2026-11-28, on the hand's files (gemini). **§WCA8: "a result of record per model": this is Argon's; the other is `RESULT-gemini-blockWCA-flash-2026-11-28.md`.**
## 📌 The registration is `AMENDMENT-O37-blockWCA-wht-ntt-specchange-agy-2026-11-23.md` (§WCA0–§WCA8; ADDENDA 1–3), which carries block NCA by citation.
## 📌 The per-cell table of record is `evidence/blockNCA-WCA-result-2026-11-24/cells.tsv` (96 rows: both blocks, both models), printed by `nca_cells_gen.py` beside it from the hand's score receipts, `cell_facts.json` (read on the run box by `nca_facts.py`), `ctl_census.tsv` and `web_census.tsv`. Its README says how each is made.
## ⛔ Every figure line in a code block below is printed by `nca_cells_gen.py --summary`, and `nca_result_gen.py --check` asserts that this file carries every line of its block verbatim. Bus offsets in the prose are citations to where a reader can look, not measurements.

---
# §1 · WHAT RAN, AND ON WHAT
```
WCA-argon: rows 12 · conditions 4 · counted 1 · not counted 11 [cells-wa-ntt-argon-plain-r1-wcacp1=no/UNSCORED/rc=0 LANDED cells-wa-ntt-argon-plain-r2-wcacp2=no/UNSCORED/NO-ROOT cells-wa-ntt-argon-salt-r2-wcacp2=no/UNSCORED/NO-ROOT cells-wa-ntt-argon-plain-r3-wcacp3=no/UNSCORED/NO-ROOT cells-wa-ntt-argon-salt-r3-wcacp3=no/UNSCORED/NO-ROOT cells-wa-wht-argon-plain-r1-wcacp1=no/UNSCORED/NO-ROOT cells-wa-wht-argon-salt-r2-refire2-wcacp1=no/UNSCORED/NO-ROOT cells-wa-wht-argon-plain-r2-wcacp2=no/UNSCORED/NO-ROOT cells-wa-wht-argon-salt-r2-wcacp2=no/UNSCORED/NO-ROOT cells-wa-wht-argon-plain-r3-wcacp3=no/UNSCORED/NO-ROOT cells-wa-wht-argon-salt-r3-wcacp3=no/UNSCORED/NO-ROOT]
WCA-argon phase 2: model NO-ROOT=10 UNREAD=1 gemini-4-argon-high=1 · export 88b63df9c5be=2 NO-ROOT=10 · hook NO-ROOT=10 a6e064e307a8651d=2 · done_reason LANDED=1 NO-ROOT=10 UNREAD=1
WCA-argon clients: phase 1 NO-ROOT=10 fad3628ad91fe861=2 · phase 2 62f2102784bb74b7=1 NO-ROOT=10 UNREAD=1
WCA-argon web: source_web_served CLEAN=2 NO-ROOT=10 · phase 2 CLEAN=2 NO-ROOT=10
WCA-argon phase 1: done_reason LANDED=2 NO-ROOT=10 · cut turns (cells with >= 1) 1 of 2 read
```
- **Sources: block WA's 12 Pro-slot cells of record (gemini-4-argon-high), copied** (§WCA2). Each source ran phase 1 on WA Pro's export
  `3fd5edf1`; each phase 2 runs on the release export and the pinned client (§WCA6 item 3).
- **The order** is §WCA4's: the tripwire `T-WCA-A` (NTT · salt-diet #1) first, read by the lead at the object, then the argon rest by one
  chain. Argon is removed from the client on 2026-11-30, so a cell not fired by 2026-11-30 00:00Z is unreached, never re-cut.

---
# §2 · CORRECTNESS, VERIFIED FIRST (the withheld B/ suite; PASS is the receipt's word: TESTS all passed, 0 REGRESSIONS failed, 0 CLAUSE_TESTS failed)
The bracket lists each counted cell's TESTS (passed/total), REGRESSIONS and CLAUSE_TESTS (failed/total), in cell order. A cell IN COMPARISONS is counted and does not leave comparisons (§1).
```
WCA-argon NTT plain: PASS 0 of 0 scored, of 3 registered [-] · G reach-loss 0 · cut turns - · truncated 0 of 0 scored · CTL-READ - of 0 scored · in comparisons 0 of 0 scored
WCA-argon NTT salt-diet: PASS 1 of 1 scored, of 3 registered [T15/15 R0/11 C0/4] · G reach-loss 0 · cut turns 0 · truncated 0 of 1 scored · CTL-READ UNREAD of 1 scored · in comparisons UNREAD of 1 scored
WCA-argon WHT plain: PASS 0 of 0 scored, of 3 registered [-] · G reach-loss 0 · cut turns - · truncated 0 of 0 scored · CTL-READ - of 0 scored · in comparisons 0 of 0 scored
WCA-argon WHT salt-diet: PASS 0 of 0 scored, of 3 registered [-] · G reach-loss 0 · cut turns - · truncated 0 of 0 scored · CTL-READ - of 0 scored · in comparisons 0 of 0 scored
WCA-argon FULL PASS plain 0 of 0 counted · in comparisons 0 of 0
WCA-argon FULL PASS salt-diet 1 of 1 counted · in comparisons UNREAD
```
- The figures above are this block as the run box holds it when this file is written; a row the box does not hold reads its state
  (`NO-ROOT`, `UNSCORED`), never a count.

---
# §3 · COST, AS A SIGN ONLY
```
WCA-argon NTT phase-2 T by rep (plain / salt-diet): #1 - / 4011676 · #2 - / - · #3 - / - · salt-diet > plain in 0 of 0 pairs
WCA-argon NTT phase-2 wall_s by rep (plain / salt-diet): #1 - / 781.8 · #2 - / - · #3 - / - · salt-diet > plain in 0 of 0 pairs
WCA-argon WHT phase-2 T by rep (plain / salt-diet): #1 - / - · #2 - / - · #3 - / - · salt-diet > plain in 0 of 0 pairs
WCA-argon WHT phase-2 wall_s by rep (plain / salt-diet): #1 - / - · #2 - / - · #3 - / - · salt-diet > plain in 0 of 0 pairs
```
T is the agy meter's token total for phase 2; wall is phase 2's turn-loop wall. A sign, never a premium, and no magnitude is claimed.

---
# §4 · THE REGISTERED PREDICTIONS (NCA §NCA5 (i)–(iii), carried by §WCA5); A MISS IS A RESULT
```
WCA-argon predictions: (i) ELIGIBLE plain 1/6 salt-diet 1/6 · REACHED plain 1/6 salt-diet 1/6 · (ii) cut-turn incidence plain vs salt-diet: NTT UNREAD · WHT 0/0 vs 0/0 · (iii) done_reason LANDED=1 NO-ROOT=10 UNREAD=1
WCA-argon prediction verdicts: (i) ELIGIBLE salt-diet lower: MISS · REACHED salt-diet lower: MISS · (ii) salt-diet >= plain in 0 of 0 conditions with both arms in comparisons · no comparison: WHT · unread: NTT · (iii) CELL-KILLED cells 0
```
- **(i)** "lower for salt-diet": every source was eligible by the census (ADDENDUM 3), so a MISS at a tie is what the census predicts.
- **(ii)** and **(iii)** read as their lines print.

---
# §5 · WHAT THIS RESULT CANNOT ESTABLISH
§WCA8 (NCA §NCA8, §NCA9 and §NCA10 carried, for NTT and WHT): no magnitude; nothing about gemini-3.1-pro-high; nothing Flash-versus-argon
or Claude-versus-agy. §WCA6 item 6: one author built both tasks and both B/ suites and leads this block, and NTT's reference proves less than
WHT's. Nothing here says whether the salt method helps or hurts. Any public sentence is the Captain's.
