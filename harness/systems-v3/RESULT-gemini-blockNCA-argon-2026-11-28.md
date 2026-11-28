# RESULT — O37 block NCA, ARGON COLUMN · the agy lane × the six block-N problems × greenfield → spec-change × extras=none · n = 3 · gemini-4-argon-high
### bench (lead), 2026-11-28, on the hand's files (gemini). **§NCA8: "a result of record per model": this is Argon's; the other is `RESULT-gemini-blockNCA-flash-2026-11-28.md`.**
## 📌 The registration is `AMENDMENT-O37-blockNCA-specchange-agy-2026-11-23.md` (§NCA0–§NCA10; ADDENDA 1–6).
## 📌 The per-cell table of record is `evidence/blockNCA-WCA-result-2026-11-24/cells.tsv` (96 rows: both blocks, both models), printed by `nca_cells_gen.py` beside it from the hand's score receipts, `cell_facts.json` (read on the run box by `nca_facts.py`), `ctl_census.tsv` and `web_census.tsv`. Its README says how each is made.
## ⛔ Every figure line in a code block below is printed by `nca_cells_gen.py --summary`, and `nca_result_gen.py --check` asserts that this file carries every line of its block verbatim. Bus offsets in the prose are citations to where a reader can look, not measurements.

---
# §1 · WHAT RAN, AND ON WHAT
```
NCA-argon: rows 36 · conditions 12 · counted 34 · not counted 2 [cells-nca-liveness-argon-salt-r1=no/INCOMPLETE/rc=1 NOT-LANDED tag=ABSENT receipt=9832d84cf682 cells-nca-maxflow-argon-plain-r1=no/NOT-SCORED/rc=0 LANDED]
NCA-argon phase 2: model UNREAD=2 gemini-4-argon-high=34 · export 88b63df9c5be=36 · hook FRESH=36 · done_reason LANDED=34 UNREAD=2
NCA-argon clients: phase 1 62f2102784bb74b7=36 · phase 2 62f2102784bb74b7=34 UNREAD=2
NCA-argon web: source_web_served OWN:CLEAN=36 · phase 2 CLEAN=36
NCA-argon phase 1: done_reason LANDED=36 · cut turns (cells with >= 1) 8 of 36 read
```
- **36 FRESH cells, both phases in one cell** (§NCA7 fork 1's default: argon has no source), level 8's one-cell form, every phase on the
  pinned client `62f2102784bb74b7`.
- **Two 503 discards** (the `attempts` line in this directory's README): LinearScan plain #2 and salt-diet #2 stand at attempt 2. A discarded
  attempt is a whole attempt, never pooled and never a row (L8 ADDENDUM 2 §A2.2).
- **`cells-nca-liveness-argon-salt-r1` was not reached.** Its subject deleted its own `landed-1` tag and re-landed inside phase 1, so the
  §A9.2 landed gate refused phase 2 (`tag=ABSENT`; the receipt reads INCOMPLETE because no phase 2 ran). The lead's ruling (a), bus offset
  111,293,855: a REACH LOSS. Liveness · salt-diet is n = 2.
- **`cells-nca-maxflow-argon-plain-r1` is NOT SCORED (harness).** Phase 1 LANDED; phase 2 was refused at launch by the launcher's brain
  check; ADDENDUM 5's re-fire route refused on a real copy, driven at zero spend. NCA ADDENDUM 6: phase 2 NOT-SCORED (harness), and
  MaxFlow · plain is n = 2 of 3.
- **Re-landings inside phase 1** (ADDENDUM 5 §A5.3): the hand's 21 extra G readings at P1^ each read ELIGIBLE and agree with the registered
  landed-1 reading (bus offset 112,527,193); no count moves.
- **Web.** A fresh cell's two phases share one brain, so its own reading covers both (`OWN:` in the table). Every cell read CLEAN.

---
# §2 · CORRECTNESS, VERIFIED FIRST (the withheld B/ suite; PASS is the receipt's word: TESTS all passed, 0 REGRESSIONS failed, 0 CLAUSE_TESTS failed)
The bracket lists each counted cell's TESTS (passed/total), REGRESSIONS and CLAUSE_TESTS (failed/total), in cell order. A cell IN COMPARISONS is counted and does not leave comparisons (§1).
```
NCA-argon AES plain: PASS 3 of 3 scored, of 3 registered [T14/14 R0/8 C0/6 T14/14 R0/8 C0/6 T14/14 R0/8 C0/6] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-argon AES salt-diet: PASS 3 of 3 scored, of 3 registered [T14/14 R0/8 C0/6 T14/14 R0/8 C0/6 T14/14 R0/8 C0/6] · G reach-loss 0 · cut turns 6 · truncated 2 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-argon BinomialHeap plain: PASS 3 of 3 scored, of 3 registered [T18/18 R0/13 C0/5 T18/18 R0/13 C0/5 T18/18 R0/13 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-argon BinomialHeap salt-diet: PASS 3 of 3 scored, of 3 registered [T18/18 R0/13 C0/5 T18/18 R0/13 C0/5 T18/18 R0/13 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-argon LinearScan plain: PASS 3 of 3 scored, of 3 registered [T14/14 R0/9 C0/5 T14/14 R0/9 C0/5 T14/14 R0/9 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-argon LinearScan salt-diet: PASS 3 of 3 scored, of 3 registered [T14/14 R0/9 C0/5 T14/14 R0/9 C0/5 T14/14 R0/9 C0/5] · G reach-loss 0 · cut turns 8 · truncated 2 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-argon Liveness plain: PASS 3 of 3 scored, of 3 registered [T16/16 R0/11 C0/5 T16/16 R0/11 C0/5 T16/16 R0/11 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-argon Liveness salt-diet: PASS 0 of 2 scored, of 3 registered [T15/16 R0/11 C1/5 T15/16 R0/11 C1/5] · G reach-loss 0 · cut turns 3 · truncated 1 of 2 scored · CTL-READ 0 of 2 scored · in comparisons 2 of 2 scored
NCA-argon Luby plain: PASS 3 of 3 scored, of 3 registered [T19/19 R0/12 C0/7 T19/19 R0/12 C0/7 T19/19 R0/12 C0/7] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-argon Luby salt-diet: PASS 3 of 3 scored, of 3 registered [T19/19 R0/12 C0/7 T19/19 R0/12 C0/7 T19/19 R0/12 C0/7] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-argon MaxFlow plain: PASS 2 of 2 scored, of 3 registered [T13/13 R0/8 C0/5 T13/13 R0/8 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 2 scored · CTL-READ 0 of 2 scored · in comparisons 2 of 2 scored
NCA-argon MaxFlow salt-diet: PASS 3 of 3 scored, of 3 registered [T13/13 R0/8 C0/5 T13/13 R0/8 C0/5 T13/13 R0/8 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-argon FULL PASS plain 17 of 17 counted · in comparisons 17 of 17
NCA-argon FULL PASS salt-diet 15 of 17 counted · in comparisons 15 of 17
```
- **Liveness · salt-diet: both counted cells fail one clause test each, with 0 regressions**; Liveness · plain passes 3 of 3. The
  clause figures carry census ADDENDUM 46 NOTE 1 (NCA ADDENDUM 4) and are never read as a premium.
- **Every counted cell that was truncated or cut is in salt-diet** (AES, LinearScan, Liveness): the AES and LinearScan ones PASS, and the
  Liveness ones fail one clause test each.

---
# §3 · COST, AS A SIGN ONLY
```
NCA-argon AES phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 2888839 / 10664084 · #2 2839768 / 9160066 · #3 3027203 / 7356747 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-argon AES phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 761.3 / 1987.1 · #2 647.4 / 2639.6 · #3 752.4 / 1586.0 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-argon BinomialHeap phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 2199697 / 5940342 · #2 2238817 / 4179834 · #3 2798936 / 4152385 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-argon BinomialHeap phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 620.6 / 1080.3 · #2 650.1 / 891.6 · #3 800.2 / 1129.7 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-argon LinearScan phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 6520449 / 14076599 · #2 10116225 / 10357910 · #3 11721389 / 23176432 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-argon LinearScan phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 1643.7 / 3541.3 · #2 1936.8 / 3337.9 · #3 1604.6 / 2498.3 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-argon Liveness phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 4943100 / - · #2 3331511 / 6939348 · #3 6580603 / 18962553 · salt-diet > plain in 2 of 2 pairs in comparisons
NCA-argon Liveness phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 1049.4 / - · #2 799.6 / 1245.7 · #3 1116.3 / 2492.8 · salt-diet > plain in 2 of 2 pairs in comparisons
NCA-argon Luby phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 3112644 / 5081749 · #2 2667238 / 5856923 · #3 2099273 / 6788811 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-argon Luby phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 684.0 / 1384.8 · #2 816.5 / 1232.0 · #3 615.4 / 1149.6 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-argon MaxFlow phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 - / 11035846 · #2 3297505 / 11009754 · #3 2653196 / 9449205 · salt-diet > plain in 2 of 2 pairs in comparisons
NCA-argon MaxFlow phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 - / 1651.8 · #2 1279.9 / 1584.6 · #3 878.4 / 1600.2 · salt-diet > plain in 2 of 2 pairs in comparisons
```
T is the agy meter's token total for phase 2; wall is phase 2's turn-loop wall. A rep prints only where its cell is COUNTED, and a pair
counts only when both its cells are in comparisons. A sign, never a premium (§NCA5), and no magnitude is claimed.

---
# §4 · THE REGISTERED PREDICTIONS (NCA §NCA5 (i)–(iii)); A MISS IS A RESULT
```
NCA-argon predictions: (i) ELIGIBLE plain 18/18 salt-diet 17/18 · REACHED plain 18/18 salt-diet 17/18 · (ii) cut-turn incidence plain vs salt-diet: AES 0/3 vs 2/3 · BinomialHeap 0/3 vs 0/3 · LinearScan 0/3 vs 3/3 · Liveness 0/3 vs 1/2 · Luby 0/3 vs 0/3 · MaxFlow 0/2 vs 0/3 · (iii) done_reason LANDED=34 UNREAD=2
NCA-argon prediction verdicts: (i) ELIGIBLE salt-diet lower: HOLDS · REACHED salt-diet lower: HOLDS · (ii) salt-diet >= plain in 6 of 6 conditions with both arms in comparisons · (iii) CELL-KILLED cells 0
```
- **(i)** binds REACH for argon (§NCA5): salt-diet's is lower, by `cells-nca-liveness-argon-salt-r1`. **Holds.** (`cells-nca-maxflow-argon-plain-r1`
  was reached: its §A9.2 gate fired, and the harness refused after it.)
- **(ii)** **Holds in every condition.** Salt-diet was cut more often than plain in AES, LinearScan and Liveness, and tied at 0 in the rest.
- **(iii)** CELL-KILLED binds no cell. **Holds.**

---
# §5 · WHAT THIS RESULT CANNOT ESTABLISH
§NCA8, carried: no magnitude or effect size; nothing Flash-versus-argon or Claude-versus-agy; nothing about a spec-change reached from a
phase 1 that did not land; nothing about a gemini-3.1-pro-high condition; nothing outside §NCA1. NC's reading rules (L8 §M7, NC §C8) are
carried, so every premium is UNRESOLVED-UNDERPOWERED. §NCA6 item 4 (one author for the six B/ suites, who is the lead) is carried. Nothing
here says whether the salt method helps or hurts. Any public sentence, and any claim about the method, is the Captain's.
