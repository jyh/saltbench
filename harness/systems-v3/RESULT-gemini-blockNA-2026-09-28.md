# RESULT — O37 block NA · the agy lane × greenfield × extras=none × the six new problems · n = 3 · BOTH MODELS
### bench (lead), 2026-09-28, on the hand's files (gemini, `dc8610c0a0f5`). **24 conditions, 72 cells in n. §NA6: "a result of record per model" — §2 is Pro's and §3 is Flash's, each self-contained, and no sentence here compares them.**
## 📌 The registration is `AMENDMENT-O37-nine-greenfield-agy-2026-09-25.md` (§NA0–§NA6, ADDENDA 1–5), carried on saltbench PR #265.
## 📌 The per-cell table of record is the hand's: `RESULT-gemini-blockNA-2026-09-28-cells.tsv` (level 6 §H8's list, plus the tree-hash line and the x86-concurrency column, §NA6), built by `RESULT-gemini-blockNA-cells-gen.py` and checked against every score receipt by `RESULT-gemini-blockNA-2026-09-28-verify.py` (73 receipts, 0 problems, selftest 6/6).
## ⛔ Every figure line below is printed by `RESULT-gemini-blockNA-2026-09-28-prose-verify.py --print` from that table, and asserted against this document's bytes. No number here was typed from a message.

---
# §1 · WHAT RAN, AND ON WHAT
```
cells in n 72 · outside n 1 (nabhfsr01) · conditions 24
exports 59508ac 8ed8cb3 e10f420 · task trees vs e54f35a DIFFERENT 12 SAME 60 · x86-concurrent cells 0
done_reason LANDED 69 · TURN-TIMEOUT 3
```
- **One outside-n cell, printed and counted nowhere:** `nabhfsr01`, a re-fire of `nabhfs03` (BinomialHeap · Flash · salt-diet #3). The helm ruled
  on 2026-09-26 (desk XF) that the re-fire "never replaces" the original, and the non-author read under that ruling classified `nabhfs03` as
  a RESULT. No registered clause admits an extra cell into a condition's n, so `nabhfsr01` (PASS 13/13, truncated) is in the table with its
  receipt and in no denominator here.
- **Exports, each registered:** `59508ac` carries one cell, T-NA-F (ADDENDUM 2). `8ed8cb3` carries all 12 LinearScan cells (ADDENDUM 5): their
  task tree DIFFERS from e54f35a's only in the re-worded card (desk YM), and it equals 23485e5's, block N's LinearScan export. The other 59
  cells ran on `e10f420` (ADDENDUM 3). **Every other tree is SAME by git tree hash**, and each condition sits on one interface hash.
- **x86 concurrency (§NA4):** no NA cell straddled an x86 agy cell.

---
# §2 · gemini-3.1-pro-high — THE RESULT OF RECORD
```
== gemini-3.1-pro-high: 36 cells
  Luby         plain 3/3 scored of 3 fired [12/12 12/12 12/12] trunc 0 · salt-diet 2/3 scored of 3 fired [12/12 8/12 12/12] trunc 2
  AES          plain 3/3 scored of 3 fired [8/8 8/8 8/8] trunc 0 · salt-diet 2/2 scored of 3 fired [NOT-LANDED 8/8 8/8] trunc 2 non-landing 1
  Liveness     plain 3/3 scored of 3 fired [11/11 11/11 11/11] trunc 0 · salt-diet 1/3 scored of 3 fired [2/11 11/11 2/11] trunc 1
  MaxFlow      plain 3/3 scored of 3 fired [8/8 8/8 8/8] trunc 0 · salt-diet 1/3 scored of 3 fired [2/8 2/8 8/8] trunc 1
  BinomialHeap plain 3/3 scored of 3 fired [13/13 13/13 13/13] trunc 0 · salt-diet 1/3 scored of 3 fired [9/13 13/13 6/13] trunc 1
  LinearScan   plain 2/3 scored of 3 fired [9/9 7/9 9/9] trunc 0 · salt-diet 0/3 scored of 3 fired [4/9 8/9 4/9] trunc 2
  gemini-3.1-pro-high plain FULL PASS 17 of 18 scored · cut turns 0 of 54 sent · truncated cells 0 of 18 · cells with any cut 0
  gemini-3.1-pro-high salt-diet FULL PASS 7 of 17 scored · cut turns 26 of 104 sent · truncated cells 9 of 18 · cells with any cut 10
```

**Verified first (level 6 §H5 rule 9): FULL PASS over scored cells, and a truncated PASS is a floor (level 5 §F4 rule 2).**
- **The sign favours plain on five of six problems in this model** (plain 17 of 18; salt-diet 7 of 17 scored). **AES is level on scored
  cells** (3/3 against 2/2), with one salt-diet non-landing beside it. Plain's one FAIL is LinearScan (7/9, not truncated).
- **The per-turn deadline bound the salt-diet arm and never bound plain:** 26 of 104 salt-diet turns cut, against 0 of 54. This is ADDENDUM 4's
  registered outcome, measured on the whole model. **So salt-diet's FAILs and floors are read beside that cut, never without it** (ADDENDUM 4:
  an arm-correlated cut is printed beside every NA table).
- **One non-landing, `naaeps01`** (AES salt-diet #1): TURN-TIMEOUT at 11,524 s, 6 of 7 sent turns cut, no LANDING.md. It is **NOT-LANDED in
  its own column and NOT CUT-BOUND**: no ruling names it, and 6 of 7 is not every turn. It is in no pass denominator (AES salt-diet reads 2 of 2
  scored, of 3 fired).
```
  (i) gemini-3.1-pro-high: salt-diet cells-with-a-cut >= plain in 6 of 6 problems (6 strictly)
  (ii) gemini-3.1-pro-high plain cells-with-a-cut in reference-size order 0 0 0 0 0 0 · non-decreasing yes
  (ii) gemini-3.1-pro-high salt-diet cells-with-a-cut in reference-size order 2 3 1 1 1 2 · non-decreasing NO
```

---
# §3 · gemini-3.8-flash-high — THE RESULT OF RECORD
```
== gemini-3.8-flash-high: 36 cells
  Luby         plain 3/3 scored of 3 fired [12/12 12/12 12/12] trunc 0 · salt-diet 3/3 scored of 3 fired [12/12 12/12 12/12] trunc 0
  AES          plain 3/3 scored of 3 fired [8/8 8/8 8/8] trunc 0 · salt-diet 3/3 scored of 3 fired [8/8 8/8 8/8] trunc 0
  Liveness     plain 3/3 scored of 3 fired [11/11 11/11 11/11] trunc 0 · salt-diet 3/3 scored of 3 fired [11/11 11/11 11/11] trunc 1
  MaxFlow      plain 3/3 scored of 3 fired [8/8 8/8 8/8] trunc 0 · salt-diet 3/3 scored of 3 fired [8/8 8/8 8/8] trunc 0
  BinomialHeap plain 3/3 scored of 3 fired [13/13 13/13 13/13] trunc 0 · salt-diet 2/2 scored of 3 fired [13/13 13/13 NOT-SCORED] trunc 0 non-landing 1
  LinearScan   plain 3/3 scored of 3 fired [9/9 9/9 9/9] trunc 0 · salt-diet 2/3 scored of 3 fired [9/9 8/9 9/9] trunc 3
  gemini-3.8-flash-high plain FULL PASS 18 of 18 scored · cut turns 0 of 55 sent · truncated cells 0 of 18 · cells with any cut 0
  gemini-3.8-flash-high salt-diet FULL PASS 16 of 17 scored · cut turns 18 of 72 sent · truncated cells 4 of 18 · cells with any cut 5
```

- **Plain passes every cell; salt-diet 16 of 17 scored.** The one scored FAIL is LinearScan salt-diet #2 (8/9), a truncated cell: all three
  LinearScan salt-diet cells were cut, so that condition's two passes are floors too.
- **The deadline bound salt-diet only here too:** 18 of 72 salt-diet turns cut, against 0 of 55.
- **`nabhfs03`, the one non-landing, is a RESULT** (the XF non-author read, 2026-09-26: the briefing was in context). ADDENDUM 4 registers it as
  CUT-BOUND and describes it as "12 of 12 turns cut". ⚠️ **The table does not reproduce that count:** it reads 14 turns sent (11 continue
  turns and the persist turn among them), 12 cut. So "every turn cut", the premise of the CUT-BOUND label, holds only if two of the 14 sent
  turns are not counted as work turns, and this table cannot say which two. **Its classification as a RESULT does not rest on that count and
  is unchanged. The label is printed as registered, with this discrepancy beside it.** Which turns ADDENDUM 4's "12" counted is the one reading
  here that a non-author should take at the cell's turn loop.
```
  (i) gemini-3.8-flash-high: salt-diet cells-with-a-cut >= plain in 6 of 6 problems (3 strictly)
  (ii) gemini-3.8-flash-high plain cells-with-a-cut in reference-size order 0 0 0 0 0 0 · non-decreasing yes
  (ii) gemini-3.8-flash-high salt-diet cells-with-a-cut in reference-size order 0 0 1 0 1 3 · non-decreasing NO
```

---
# §4 · THE THREE REGISTERED PREDICTIONS (§NA3), PER MODEL AND ARM; A MISS IS A RESULT
Incidence is counted as **cells with at least one cut turn**, from each cell's client-stderr cut count (ADDENDUM 4's source, never the turn
loop's TURN-DENIED line). (i) also names CAP-TOKENS, which **cannot occur on this lane**: level 6 ADDENDUM 7 (A7.2) records
that no agy script enforces `T1_TOK` and that the turn loop has no token-cap end.
- **(i) HELD in both models:** salt-diet ≥ plain in 6 of 6 problems each. It holds strictly in all 6 for Pro and in 3 for Flash, with the
  other 3 tied at zero.
- **(ii) MISSED in both models for salt-diet:** incidence does not rise with reference size (the §2 and §3 lines). For plain it holds only
  vacuously, at zero.
- **(iii) HELD BY LABEL:** no cell ended `CELL-KILLED`. ⚠️ **Declared beside it:**
```
not LANDED by done_reason: naaeps01 TURN-TIMEOUT 11524 s NOT-LANDED · naaeps02 TURN-TIMEOUT 21725 s PASS · nabhfs03 TURN-TIMEOUT 21724 s NOT-SCORED
```
  **The caps in force are level 6 ADDENDUM 7's A7.2, not the §H3 list that §NA0 row 5 copied.** §NA0 row 5 says "level 6 §H3, unchanged"
  and lists `T1_TOK`, the 1800 s print deadline and the 2100 s turn patience. That is §H3 as it stood BEFORE A7 corrected it. A7.2 registers
  the caps the lane enforces: `AGY_MAX_TURNS` 40 (ends TURN-CAP), **`AGY_MAX_WALL` 21,600 s (ends WALL-CAP)**, the 1800 s print deadline and
  the 2100 s turn timeout (ends TURN-TIMEOUT). It also strikes `T1_TOK` as a cap. *(This section first called the 21,600 s wall
  "unregistered", from the pre-A7 list. kent's non-author read of 2026-09-28 found A7.2. The reading below is re-derived from it.)*
  - **TURN-CAP and WALL-CAP incidence, the split A7.3 asks for:** by `done_reason`, **0 and 0** in both models and both arms.
  - ⚠️ **But two salt-diet cells reached the wall's VALUE:** `naaeps02` (21,725 s) and `nabhfs03` (21,724 s). Both carry `done_reason`
    TURN-TIMEOUT, not WALL-CAP. **Either the turn timeout fired in the same window as the wall, or the end kind was recorded under the wrong
    name.** This result does not decide which. It needs each cell's turn loop and the wave's `CAPS` line, which A7.2 asks the hand to file
    with the receipts (a wave whose line differs from A7.2 is reported as such). **Neither has been read for NA.** Until it is, the wall's
    incidence by arm reads **0 recorded · 2 salt-diet cells at the wall's value · 0 plain**. A7.3 names the wall as the cap most likely to
    bind one arm, and here it bound only salt-diet cells, whichever name the end carries.
  - `naaeps02` LANDED before it stopped (PASS 8/8, truncated, a floor). `nabhfs03` did not.
  - **(iii) itself is about CELL-KILLED, and by label it HELD** (0 cells).

---
# §5 · ⛔ WHAT THIS DOES **NOT** SAY
1. **No effect size and no premium** (§NA3, §NA5). This lane has no USD pricing (level 6 §H3), and a truncated cell's T and wall are not
   poolable. T and wall are per cell in the table, and no median is quoted here.
2. **Nothing Claude-versus-agy** (§NA5, level 6's cross-lane rule). Block N's two results are a separate lane on separate machinery.
3. **Nothing Pro-versus-Flash.** Each model's section is its own result.
4. **Nothing outside the 24 conditions, and the six are a SELECTION** (block N §N8 items 3–4, carried).
5. **New problems, new author** (block N §N5.1). A task defect is a harness finding, never an arm effect.
6. **The per-turn deadline is the pilot's, and it binds the treatment** (ADDENDUM 4). Every salt-diet FAIL and floor here is read with it.
7. **Nothing here is a claim about the salt METHOD.** Any public sentence, and any claim about the method, is the Captain's (§NA6).

---
# §6 · PROVENANCE
```
  hand         gemini: cells fired through the wave supervisor on the exports above; each condition scored to a receipt FILE
  table        RESULT-gemini-blockNA-2026-09-28-cells.tsv, from RESULT-gemini-blockNA-cells-gen.py over the receipts and each
               cell's own ctl/ (evidence/blockNA-2026-09-28/: cell facts, tree hashes, x86 windows, the /usage dispatch rows, rulings)
  table check  RESULT-gemini-blockNA-2026-09-28-verify.py (the hand's): 73 cells, 73 receipts re-read, 0 problems; selftest 6/6
  prose check  RESULT-gemini-blockNA-2026-09-28-prose-verify.py (the lead's): every figure line above re-derived from the table and
               asserted against this document; --selftest requires RED on a PASS turned FAIL and on the outside-n cell admitted
```
