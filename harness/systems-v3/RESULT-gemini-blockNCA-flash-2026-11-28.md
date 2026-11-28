# RESULT — O37 block NCA, FLASH COLUMN · the agy lane × the six block-N problems × greenfield → spec-change × extras=none · n = 3 · gemini-3.8-flash-high
### bench (lead), 2026-11-28, on the hand's files (gemini). **§NCA8: "a result of record per model": this is Flash's; the other is `RESULT-gemini-blockNCA-argon-2026-11-28.md`.**
## 📌 The registration is `AMENDMENT-O37-blockNCA-specchange-agy-2026-11-23.md` (§NCA0–§NCA10; ADDENDA 1–6).
## 📌 The per-cell table of record is `evidence/blockNCA-WCA-result-2026-11-24/cells.tsv` (96 rows: both blocks, both models), printed by `nca_cells_gen.py` beside it from the hand's score receipts, `cell_facts.json` (read on the run box by `nca_facts.py`), `ctl_census.tsv` and `web_census.tsv`. Its README says how each is made.
## ⛔ Every figure line in a code block below is printed by `nca_cells_gen.py --summary`, and `nca_result_gen.py --check` asserts that this file carries every line of its block verbatim. Bus offsets in the prose are citations to where a reader can look, not measurements.

---
# §1 · WHAT RAN, AND ON WHAT
```
NCA-flash: rows 36 · conditions 12 · counted 34 · not counted 2 [cells-nca-binomialheap-flash-salt-r3=REACH-LOSS(G)/FAIL/rc=0 LANDED cells-nca-linearscan-flash-salt-r2=REACH-LOSS(G)/FAIL/rc=0 LANDED]
NCA-flash phase 2: model gemini-3.8-flash-high=36 · export 88b63df9c5be=36 · hook FRESH=2 a6e064e307a8651d=34 · done_reason LANDED=36
NCA-flash clients: phase 1 42e76bedafb5896b=29 62f2102784bb74b7=2 6f4785c17acc4b8b=5 · phase 2 62f2102784bb74b7=36
NCA-flash harness-side over 34 counted: run_verdict OK=34 · P-PERSIST by the registered reader yes=34 · PROBE-CUT-AT-EXIT-TIMEOUT 0 [-] · token after the probe at the object (a hand read beside the reader) yes=34 · other events -
NCA-flash web: source_web_served CLEAN=30 OWN:CLEAN=2 WEB-SERVED=4 · phase 2 CLEAN=36
NCA-flash phase 1: done_reason LANDED=36 · cut turns (cells with >= 1) 4 of 36 read
```
- **Sources: block NA's Flash cells of record, copied** under §NCA2's Flash rule (a copy owes no fresh G baseline; its source was made
  eligible by the census, ADDENDUM 1). **Two cells are FRESH**, where NA had no eligible source (§NCA2): BinomialHeap · salt-diet #3
  (`cells-nca-binomialheap-flash-salt-r3`; NA's `nabhfs03` never landed) and LinearScan · salt-diet #2 (`cells-nca-linearscan-flash-salt-r2`;
  NA's `nalsfs202` failed its own G suite). Both fresh cells LANDED phase 1, and both G baselines on landed-1 read short of a full pass, so each
  is a **REACH LOSS under NC rule 4**: its phase 2 is listed in §2 and never counted (one attempt each, never re-run).
- **Two clients per copy** (§NCA9, §H-CLIENT: declared, and not a treatment): every phase 2 ran on the pinned client
  `62f2102784bb74b7`; each copy's phase 1 is NA's, on the client NA ran (the `clients` line). The two fresh cells ran both phases on the pin.
- **The hook.** The 34 copies carry the replaced web-deny hook whose hash is ADDENDUM 1's census value (`a6e064e307a8651d`); the two fresh cells
  were built by the release export with its own hook (`FRESH` in the table).
- **Web.** Four copies continue WEB-SERVED sources (census ADDENDUM 47): LinearScan · plain #1–#3 (`nalsfp201`–`nalsfp203`) and LinearScan ·
  salt-diet #3 (`nalsfs203`). Each keeps its verdict and leaves every comparison exactly as its source did (§NCA6 item 5). No phase 2 was
  served a search: the 11-20 census instrument (`web_brain_census.py`, unchanged) read every brain transcript of every standing cell
  (`web_census.tsv`, `web_transcripts.tsv`); its one `search_web` call in this block, `naaefp02`'s, was DENIED. Its positive control on the
  same box read NA's `nalsfp201`–`nalsfp203` at 7, 16 and 22 served, the 11-20 figures.
- **CTL-READ: `naaefs01`** (AES · salt-diet #1) read the harness's `ctl/` in its phase 2 (`ctl_census.tsv`, 8 calls). The lead's ruling (bus
  offset 110,731,568): the verdict stands, the cell leaves every comparison, and its briefing and P-PERSIST read UNMEASURED.
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
NCA-flash AES plain: PASS 3 of 3 scored, of 3 registered [T14/14 R0/8 C0/6 T14/14 R0/8 C0/6 T14/14 R0/8 C0/6] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-flash AES salt-diet: PASS 3 of 3 scored, of 3 registered [T14/14 R0/8 C0/6 T14/14 R0/8 C0/6 T14/14 R0/8 C0/6] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 1 of 3 scored · in comparisons 2 of 3 scored
NCA-flash BinomialHeap plain: PASS 3 of 3 scored, of 3 registered [T18/18 R0/13 C0/5 T18/18 R0/13 C0/5 T18/18 R0/13 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-flash BinomialHeap salt-diet: PASS 2 of 2 scored, of 3 registered [T18/18 R0/13 C0/5 T18/18 R0/13 C0/5] · G reach-loss 1 [ncabhfs01 G 7/13, phase 2 FAIL T7/18] · cut turns 0 · truncated 0 of 2 scored · CTL-READ 0 of 2 scored · in comparisons 2 of 2 scored
NCA-flash LinearScan plain: PASS 3 of 3 scored, of 3 registered [T14/14 R0/9 C0/5 T14/14 R0/9 C0/5 T14/14 R0/9 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 0 of 3 scored
NCA-flash LinearScan salt-diet: PASS 1 of 2 scored, of 3 registered [T14/14 R0/9 C0/5 T13/14 R1/9 C0/5] · G reach-loss 1 [ncalsfs01 G 6/9, phase 2 FAIL T9/14] · cut turns 3 · truncated 1 of 2 scored · CTL-READ 0 of 2 scored · in comparisons 1 of 2 scored
NCA-flash Liveness plain: PASS 0 of 3 scored, of 3 registered [T15/16 R0/11 C1/5 T15/16 R0/11 C1/5 T15/16 R0/11 C1/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-flash Liveness salt-diet: PASS 1 of 3 scored, of 3 registered [T15/16 R0/11 C1/5 T16/16 R0/11 C0/5 T15/16 R0/11 C1/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-flash Luby plain: PASS 3 of 3 scored, of 3 registered [T19/19 R0/12 C0/7 T19/19 R0/12 C0/7 T19/19 R0/12 C0/7] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-flash Luby salt-diet: PASS 3 of 3 scored, of 3 registered [T19/19 R0/12 C0/7 T19/19 R0/12 C0/7 T19/19 R0/12 C0/7] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-flash MaxFlow plain: PASS 3 of 3 scored, of 3 registered [T13/13 R0/8 C0/5 T13/13 R0/8 C0/5 T13/13 R0/8 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-flash MaxFlow salt-diet: PASS 3 of 3 scored, of 3 registered [T13/13 R0/8 C0/5 T13/13 R0/8 C0/5 T13/13 R0/8 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 3 of 3 scored
NCA-flash FULL PASS plain 15 of 18 counted · in comparisons 12 of 15
NCA-flash FULL PASS salt-diet 13 of 16 counted · in comparisons 12 of 14
```
- **Liveness: five of six cells fail exactly one clause test each, with 0 regressions** (the bracket). NCA ADDENDUM 4: §NCA6 item 4 (the
  Liveness card amended before any later Liveness run) was not met by the release, so the six Flash Liveness cells stand as they fell (the
  helm's CONCUR, bus offset 110,631,802). These figures carry census ADDENDUM 46 NOTE 1 and are never read as a premium. Which clause test
  fails is not read here (the receipt counts failures; it does not name them).
- **LinearScan has no comparison:** its plain arm's three cells all continue WEB-SERVED sources, so 0 of 3 are in comparisons. The salt-diet
  cell `nalsfs203` (truncated, 13 of 14) also continues a WEB-SERVED source.

---
# §3 · COST, AS A SIGN ONLY
```
NCA-flash AES phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 8337000 / 23383693* · #2 12695638 / 23229074 · #3 7431158 / 27621518 · salt-diet > plain in 2 of 2 pairs in comparisons
NCA-flash AES phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 621.1 / 1493.6* · #2 856.0 / 1252.4 · #3 625.3 / 1359.8 · salt-diet > plain in 2 of 2 pairs in comparisons
NCA-flash BinomialHeap phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 7525931 / 17305710 · #2 8483309 / 19204118 · #3 8418538 / - · salt-diet > plain in 2 of 2 pairs in comparisons
NCA-flash BinomialHeap phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 739.1 / 1125.2 · #2 830.7 / 1098.7 · #3 896.9 / - · salt-diet > plain in 2 of 2 pairs in comparisons
NCA-flash LinearScan phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 9636308* / 25868693 · #2 10364368* / - · #3 15612450* / 26396583* · salt-diet > plain in 0 of 0 pairs in comparisons
NCA-flash LinearScan phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 1032.0* / 2188.9 · #2 874.9* / - · #3 1139.8* / 2222.2* · salt-diet > plain in 0 of 0 pairs in comparisons
NCA-flash Liveness phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 9360351 / 11614879 · #2 10602600 / 28993042 · #3 12550300 / 15388971 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-flash Liveness phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 856.8 / 780.0 · #2 804.9 / 1788.4 · #3 1127.1 / 1376.8 · salt-diet > plain in 2 of 3 pairs in comparisons
NCA-flash Luby phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 6235559 / 17899439 · #2 7295968 / 13946145 · #3 4641341 / 13713628 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-flash Luby phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 646.3 / 1247.7 · #2 752.2 / 1077.6 · #3 503.1 / 912.7 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-flash MaxFlow phase-2 T by rep (plain / salt-diet; * leaves comparisons): #1 6996448 / 24746965 · #2 9772413 / 17878752 · #3 6327535 / 20329864 · salt-diet > plain in 3 of 3 pairs in comparisons
NCA-flash MaxFlow phase-2 wall_s by rep (plain / salt-diet; * leaves comparisons): #1 741.2 / 1506.4 · #2 848.9 / 1611.8 · #3 696.6 / 1593.3 · salt-diet > plain in 3 of 3 pairs in comparisons
```
T is the agy meter's token total for phase 2; wall is phase 2's turn-loop wall. A rep prints only where its cell is COUNTED; a value
marked `*` leaves comparisons (§1), and a pair counts only when both its cells are in comparisons (kent's read of #479). A sign, never a
premium (§NCA5: no premium is registered), and no magnitude is claimed.

---
# §4 · THE REGISTERED PREDICTIONS (NCA §NCA5 (i)–(iii)); A MISS IS A RESULT
```
NCA-flash predictions: (i) ELIGIBLE plain 18/18 salt-diet 16/18 · REACHED plain 18/18 salt-diet 16/18 · (ii) cut-turn incidence plain vs salt-diet: AES 0/3 vs 0/2 · BinomialHeap 0/3 vs 0/2 · LinearScan 0/0 vs 0/1 · Liveness 0/3 vs 0/3 · Luby 0/3 vs 0/3 · MaxFlow 0/3 vs 0/3 · (iii) done_reason LANDED=36
NCA-flash prediction verdicts: (i) ELIGIBLE salt-diet lower: HOLDS · REACHED salt-diet lower: HOLDS · (ii) salt-diet >= plain in 5 of 5 conditions with both arms in comparisons · no comparison: LinearScan · (iii) CELL-KILLED cells 0
```
- **(i)** binds the ELIGIBLE count for Flash (§NCA5): salt-diet's is lower, by the two fresh cells' G baselines. **Holds.**
- **(ii)** compares the arms within a condition, so it reads cells IN COMPARISONS only; LinearScan gives no comparison (above). **Holds,
  trivially, at 0 ≥ 0** in all five conditions that give one: no cell in comparisons was cut in either arm. The one counted cell with cut
  turns, `nalsfs203` (LinearScan · salt-diet #3), leaves comparisons with its WEB-SERVED source. So (ii) was not tested in the direction it
  was registered to watch.
- **(iii)** CELL-KILLED binds no cell. **Holds.**

---
# §5 · WHAT THIS RESULT CANNOT ESTABLISH
§NCA8, carried: no magnitude or effect size; nothing Flash-versus-argon or Claude-versus-agy; nothing about a spec-change reached from a
phase 1 that did not land; nothing about a gemini-3.1-pro-high condition; nothing outside §NCA1. NC's reading rules (L8 §M7, NC §C8) are
carried, so every premium is UNRESOLVED-UNDERPOWERED. §NCA6 item 4 (one author for the six B/ suites, who is the lead) is carried. Nothing
here says whether the salt method helps or hurts. Any public sentence, and any claim about the method, is the Captain's.
