# RESULT — desk OD, THE EFFORT MATRIX (§D9) · 3 configurations × 3 problems × n = 3 · greenfield × extras=none × plain
### bench (lead), 2026-10-24. **The block's result of record, as §D9 asks for it: §D4's rows per configuration per problem and §D5's predictions MET / NOT MET / NOT SCORED. It is offered for a non-author read and is not of record until that read is merged.**
## 📌 The registration is `AMENDMENT-OD-effort-matrix-2026-10-16.md` (§D0–§D9, ADDENDA 1–9). The configurations are FX (Fable/xhigh), FH (Fable/high) and OX (Opus/xhigh), as the head's `--model` and `--effort` in argv.
## 📌 The per-cell table is a FILE: `evidence/od-effort-matrix/od-d9-cells.tsv`, 27 registered rows keyed on ROOT + CELL, all HARVESTED. It is built by the lead's extractor from the run's own records (`evidence/od-effort-matrix/README.md`).
## ⛔ Every line in §1 is printed by `od_d9_result.py --print` from that table, and `od_d9_result.py --check` on this file reads rc 0 only if each of those lines occurs here byte for byte. No number in §1 was typed from a message or from memory. The figures quoted in §2–§4 are read from the same table, and each one names its column.

---
# §1 · THE DERIVED LINES (per cell, then §D4's rows per configuration per problem, then R1, then §D5)
```
registered 27 · harvested 27 · owed 0
Crc32    FX#2 cells-clb-fx-crc32-plain/clbxcp02  PASS  --effort xhigh  head claude-fable-5-1=96 clean  T 3,966,280  output 106,224  list-USD $7.96  wall 1111s  escape 0
Crc32    FX#3 cells-clb-fx-crc32-plain/clbxcp03  PASS  --effort xhigh  head claude-fable-5-1=114 clean  T 4,066,600  output 138,686  list-USD $9.84  wall 1534s  escape 0
Crc32    FX#4 cells-clb-fx-crc32-plain/clbxcp04  PASS  --effort xhigh  head claude-fable-5-1=91 clean  T 3,328,498  output 90,798  list-USD $6.81  wall 990s  escape 0
Crc32    FH#2 cells-clb-fh-crc32-plain/clbhcp02  PASS  --effort high  head claude-fable-5-1=87 clean  T 2,381,690  output 62,720  list-USD $4.66  wall 749s  escape 0
Crc32    FH#3 cells-clb-fh-crc32-plain/clbhcp03  PASS  --effort high  head claude-fable-5-1=91 clean  T 2,617,108  output 64,673  list-USD $4.93  wall 688s  escape 0
Crc32    FH#4 cells-clb-fh-crc32-plain/clbhcp04  PASS  --effort high  head claude-fable-5-1=68 clean  T 2,043,399  output 55,335  list-USD $4.31  wall 568s  escape 0
Crc32    OX#1 cells-clb-ox-crc32-plain/clbwcp01  PASS  --effort xhigh  head claude-opus-5-5=118 clean  T 4,219,849  output 116,039  list-USD $4.79  wall 810s  escape 0
Crc32    OX#2 cells-clb-ox-crc32-plain/clbwcp02  PASS  --effort xhigh  head claude-opus-5-5=129 clean  T 5,352,777  output 105,105  list-USD $4.83  wall 991s  escape 0
Crc32    OX#3 cells-clb-ox-crc32-plain/clbwcp03  PASS  --effort xhigh  head claude-opus-5-5=98 clean  T 4,826,978  output 132,546  list-USD $5.02  wall 990s  escape 0
LZW      FX#1 cells-clb-fx-lzw-plain/clbxzp01  PASS  --effort xhigh  head claude-fable-5-1=117 clean  T 5,219,249  output 210,178  list-USD $11.53  wall 1776s  escape 0
LZW      FX#2 cells-clb-fx-lzw-plain/clbxzp02  PASS  --effort xhigh  head claude-fable-5-1=105 clean  T 4,285,819  output 156,417  list-USD $9.70  wall 1655s  escape 0
LZW      FX#3 cells-clb-fx-lzw-plain/clbxzp03  PASS  --effort xhigh  head claude-fable-5-1=109 clean  T 3,807,534  output 160,936  list-USD $9.13  wall 1232s  escape 0
LZW      FH#1 cells-clb-fh-lzw-plain/clbhzp01  PASS  --effort high  head claude-fable-5-1=106 clean  T 4,951,916  output 137,893  list-USD $7.89  wall 1112s  escape 0
LZW      FH#2 cells-clb-fh-lzw-plain/clbhzp02  PASS  --effort high  head claude-fable-5-1=107 clean  T 3,839,686  output 100,534  list-USD $7.11  wall 990s  escape 0
LZW      FH#3 cells-clb-fh-lzw-plain/clbhzp03  PASS  --effort high  head claude-fable-5-1=77 clean  T 4,716,082  output 158,471  list-USD $7.75  wall 1292s  escape 0
LZW      OX#1 cells-clb-ox-lzw-plain/clbwzp01  PASS  --effort xhigh  head claude-opus-5-5=111 clean  T 5,084,047  output 198,258  list-USD $6.84  wall 1595s  escape 0
LZW      OX#2 cells-clb-ox-lzw-plain/clbwzp02  PASS  --effort xhigh  head claude-opus-5-5=129 clean  T 7,731,423  output 209,594  list-USD $7.74  wall 1655s  escape 0
LZW      OX#3 cells-clb-ox-lzw-plain/clbwzp03  PASS  --effort xhigh  head claude-opus-5-5=149 clean  T 8,320,053  output 224,864  list-USD $9.26  wall 2137s  escape 0
FreeList FX#1 cells-clb-fx-freelist-plain/clbxfp01  PASS  --effort xhigh  head claude-fable-5-1=240 clean  T 18,562,155  output 429,328  list-USD $27.79  wall 4191s  escape 0
FreeList FX#2 cells-clb-fx-freelist-plain/clbxfp02  PASS  --effort xhigh  head claude-fable-5-1=115 clean  T 5,979,691  output 210,622  list-USD $12.97  wall 2138s  escape 0
FreeList FX#3 cells-clb-fx-freelist-plain/clbxfp03  PASS  --effort xhigh  head claude-fable-5-1=122 clean  T 7,484,675  output 283,703  list-USD $17.63  wall 2500s  escape 0
FreeList FH#1 cells-clb-fh-freelist-plain/clbhfp01  PASS  --effort high  head claude-fable-5-1=110 clean  T 4,689,655  output 151,341  list-USD $10.24  wall 1835s  escape 0
FreeList FH#2 cells-clb-fh-freelist-plain/clbhfp02  PASS  --effort high  head claude-fable-5-1=155 clean  T 6,959,255  output 175,157  list-USD $11.57  wall 1957s  escape 0
FreeList FH#3 cells-clb-fh-freelist-plain/clbhfp03  PASS  --effort high  head claude-fable-5-1=296 clean  T 11,996,021  output 152,554  list-USD $12.22  wall 1655s  escape 0
FreeList OX#1 cells-clb-ox-freelist-plain/clbwfp01  PASS  --effort xhigh  head claude-opus-5-5=114 clean  T 5,187,605  output 203,866  list-USD $7.01  wall 1594s  escape 0
FreeList OX#2 cells-clb-ox-freelist-plain/clbwfp02  PASS  --effort xhigh  head claude-opus-5-5=139 clean  T 8,092,328  output 342,695  list-USD $10.69  wall 2380s  escape 0
FreeList OX#3 cells-clb-ox-freelist-plain/clbwfp03  PASS  --effort xhigh  head claude-opus-5-5=248 clean  T 19,347,719  output 432,521  list-USD $17.41  wall 3829s  escape 0
Crc32    FX  PASS 3/3  interval [1, 1]  median T 3,966,280  median output 106,224  median list-USD $7.96  median wall 1111s  CAP-COST 0
Crc32    FH  PASS 3/3  interval [1, 1]  median T 2,381,690  median output 62,720  median list-USD $4.66  median wall 688s  CAP-COST 0
Crc32    OX  PASS 3/3  interval [1, 1]  median T 4,826,978  median output 116,039  median list-USD $4.83  median wall 990s  CAP-COST 0
LZW      FX  PASS 3/3  interval [1, 1]  median T 4,285,819  median output 160,936  median list-USD $9.70  median wall 1655s  CAP-COST 0
LZW      FH  PASS 3/3  interval [1, 1]  median T 4,716,082  median output 137,893  median list-USD $7.75  median wall 1112s  CAP-COST 0
LZW      OX  PASS 3/3  interval [1, 1]  median T 7,731,423  median output 209,594  median list-USD $7.74  median wall 1655s  CAP-COST 0
FreeList FX  PASS 3/3  interval [1, 1]  median T 7,484,675  median output 283,703  median list-USD $17.63  median wall 2500s  CAP-COST 0
FreeList FH  PASS 3/3  interval [1, 1]  median T 6,959,255  median output 152,554  median list-USD $11.57  median wall 1835s  CAP-COST 0
FreeList OX  PASS 3/3  interval [1, 1]  median T 8,092,328  median output 342,695  median list-USD $10.69  median wall 2380s  CAP-COST 0
ability Crc32    FX vs FH: NO INFORMATION (ceiling, R1)
ability Crc32    OX vs FX: NO INFORMATION (ceiling, R1)
ability LZW      FX vs FH: NO INFORMATION (ceiling, R1)
ability LZW      OX vs FX: NO INFORMATION (ceiling, R1)
ability FreeList FX vs FH: NO INFORMATION (ceiling, R1)
ability FreeList OX vs FX: NO INFORMATION (ceiling, R1)
P1 FX median output > FH's on 3 of 3 problems: MET
P2 NOT SCORED (no problem where FX or FH falls below 3/3; R1 per pair, ADDENDUM 8)
P4 NOT SCORED (no problem where OX or FX falls below 3/3; R1 per pair, ADDENDUM 8)
P3 FX/FH median output ratio Crc32 1.69 · LZW 1.17 · FreeList 1.86: NOT MET
P5 CAP-COST bound 0 cell(s): MET
```
- **Which cells count.** Crc32 FX and FH are cells #2–#4: their #1 ran on client 2.1.259 and is an identity reading only (ADDENDA 5 and 7). Every
  other condition is #1–#3. All 27 ran on client 2.1.280. The nine Crc32 cells ran on harness export `9f42a53548a0` or `eb50811fe861`, whose
  stagers differ only in the n bound (ADDENDUM 7); all 18 LZW and FreeList cells ran on `eb50811fe861`.
- **Rows per configuration per problem** carry the median of 3 for T (input + output + cache reads + cache writes), OUTPUT tokens beside it,
  list-USD at `rates.tsv`'s dated rows, and wall time printed beside, never as a cost. No figure is pooled across problems (rule 3).
- **`clean`** is printed only when the served-set check reads the set clean against the configuration's head table, the served head id is
  the registered one, and argv's `--model` is that same id. The sub-agents served the pilot's Opus table in every cell (§D0 row 1c).
- **All 27 cells PASS** the withheld suite (`score_claude_v3`, on a copy). So every pair is at 3 / 3 on every problem, R1 makes all six
  ability readings NO INFORMATION, and P2 and P4 are NOT SCORED by ADDENDUM 8. §D4 registered this outcome as the expected one.

---
# §2 · WHAT THE PREDICTIONS SAY, AND WHAT THEY DO NOT
- **P1 MET.** FX's median OUTPUT is above FH's on all three problems.
- **P3 NOT MET**, on LZW alone: the FX/FH median-output ratio is 1.17 there, against the registered 1.2. It is above 1.2 on Crc32 and
  FreeList. §D5 calls P3 "the direct test of 'the same price'", so on these three problems xhigh did not cost a fixed multiple of high's
  output on every problem. This is a descriptive reading at n = 3 with no test.
- **P5 MET.** No cell reached its USD cap.
- **P2 and P4 NOT SCORED.** No configuration fell below 3 / 3 on any problem, so these problems cannot show an ability difference between
  any pair (§D7 3, §D8 1).

---
# §3 · DECLARED, BESIDE THE FIGURES
1. **One cell is far above its siblings.** FreeList OX#3 (`clbwfp03`) reads T 19,347,719, against 5,187,605 and 8,092,328 for OX#1 and OX#2
   (column `T`), with 248 served head turns against 114 and 139 (`served_head`). It PASSED 7/7 like the other two. It sets the condition's
   maximum and does not move the median, which is OX#2's. It fired a day after OX#1 and OX#2, after two refused fires at zero spend (the
   account's stored credential had stopped refreshing; ADDENDUM 9's limit). No cause for the length is claimed here.
2. **Roots born inside a cell's window, and named by none.** Four cells had one other lane's cell root born inside their window
   (`roots_born_in_window` 1): Crc32 FH#2 and FH#3, LZW FH#2, and FreeList OX#3. Each root's name occurs 0 times in that cell's transcripts and
   logs (`root_name_hits`). **This is exposure, not use.** The other 23 cells read 0.
3. **The config dir varies with the problem, never with the configuration within one.** All nine Crc32 cells ran on the pool's v3 config
   dir; all 18 LZW and FreeList cells ran on its account config dir (ADDENDUM 9). P1–P5 are read per problem, so no prediction crosses that
   boundary. A comparison of one problem's figures with another's carries it as a declared difference beside the problem itself.
4. **The Fable meter per Fable cell is not measured.** The pool's quota meter is a weekly percent with one-point resolution, read about hourly
   for the whole pool, which other seats share. The readings the PM priced the block's steps from are pool readings around a fire, not a
   reading per cell, and none is reproduced here as one.
5. **The account check, and where its record is incomplete.** The identity read of the pool account (`cells_account_check.sh`, §D2 4(e))
   occurs once in each of 22 staging logs in the lead's run record: Crc32 FX#2–#3, FH#2–#3 and OX#1–#3, LZW #1 and #3, and FreeList #1–#3,
   all three configurations. ⚠️ **It is absent from 2 and unlocated for 3:** the staging logs of Crc32 FX#4 and FH#4 carry no such line, and
   LZW #2's three staging logs are not in either record directory. Those five cells are not shown to have had the check. Each of the 18 LZW
   and FreeList fire logs reads RUN-DIR READY once before launch. The account's name is not printed here (the infra-name gate).
6. **The cells were fired one at a time**, by the chain for Crc32 and by hand on the chain's harvest steps for LZW and FreeList (the lead's
   run record). The order of ADDENDUM 7 held, with the LZW tripwire after the first LZW triple and the PM's re-price at each.

---
# §4 · WHAT THIS RESULT CANNOT ESTABLISH (§D8, carried)
1. **Ability against effort on these problems.** Every cell passed, so every ability reading is NO INFORMATION. 2. **The effort the client
applied**: only the effort it was asked for, from argv. No transcript field records it (§D7 1). 3. **A tier result**: FX against OX moves
model and generation together and is "these two configurations", never "Opus vs Fable" (§D7 2). 4. **Anything about salt-diet or the
method.** 5. **A price**: list-USD is a list price at a date, and the subscription meter is the fleet's real cost. 6. **Anything beyond
these three problems**, which are ceiling-prone by construction (§D7 3).

Desk OD is re-read against this file. Any public sentence, and any claim about the method, is the Captain's.
