# PER-CELL TABLE OF RECORD — SALTBENCH LEVELS 1 AND 4
## bench (SaltBench lead), 2026-09-14. Commissioned by the Captain at council ③: *"Yes, please get the
## per-cell table."* Asked at the table: *"Do we have any measure? Tokens, dollars, wall time?"*
## Desk row **ME**. **Every cell carries its meter; until now the results published only selected figures.**

---

## ⛔⛔ THE READING RULES — THEY ARE IN THE HEADER BECAUSE A TABLE TRAVELS WITHOUT ITS PROSE

```
  1  NO USD ANYWHERE, AND NOT BECAUSE IT IS UNKNOWN.  Both lanes are SUBSCRIPTION agents. A dollar
     figure would be an invention, not a measurement, and the campaign's inert per-cell USD field is
     deliberately absent from every column below (§L5 rule 7).
  2  A TRUNCATED CELL'S TOKEN, WALL AND TURN FIGURES ARE NOT POOLABLE ACROSS ARMS.  They are reported
     per cell, flagged, and must never enter a premium or an arm-level average (helm ruling
     2026-09-11; level-4 freeze §L5 rule 2).
  3  NO ARM-LEVEL COST FIGURE IS DERIVED IN THIS FILE.  There is no mean, no ratio and no premium
     anywhere below. The table is a RECORD, not a comparison, and the per-arm counts that do appear
     are counts of CELLS, never of cost.
  4  AN UNMETERED CELL IS NOT AN ABSENT ONE.  Level 1's four unmetered directories are listed as rows
     with `-` in every meter column, not dropped to make the denominator tidy.
  5  `done_reason` AND `TRUNCATED` ARE DIFFERENT INSTRUMENTS (level-4 freeze ADDENDUM 4): `done_reason`
     is CELL-KILLED — did the controller stop this cell? `TRUNCATED` is TURNS-CUT — were any of its
     turns cut at the per-turn print deadline? ⛔ A cell can read LANDED and still be TRUNCATED, and
     in level 4 five cells do exactly that.
```

---

## §T0 · THE POPULATIONS, MEASURED — AND ONE CORRECTION TO THE COMMISSION'S OWN COUNT

```
  LEVEL 1 (P1 greenfield)   49 cell DIRECTORIES · 45 METERED · 4 UNMETERED
                            metered by arm: plain 24 · salt-diet 21
                            TRUNCATED: 3 (all salt-diet; 0 of the plain cells)
  LEVEL 4 (brownfield)      24 cells · 24 metered · 0 unmetered
                            by arm: plain 12 · salt-diet 12
                            TRUNCATED: 5 (all salt-diet; 0 of the plain cells)
```
⚠️ **Desk ME commissions "level 1 (P1 greenfield, 45 dirs)". There are 49 DIRECTORIES and 45 METERED
CELLS.** The 45 is right about cells and wrong about dirs — and 45 is also exactly what the level-4
freeze's §L0 table reports (`plain n=24 · salt-diet n=21`), reproduced independently here. **All 49 rows
are below.** The four unmetered cells never produced a meter or a turnloop file; three are plain and one
is salt-diet, so dropping them would have shrunk the CONTROL arm more than the treatment.
⇒ 🔑 ***"45" NAMED THE RIGHT NUMBER OF THE WRONG OBJECT, AND THE ONLY WAY TO SEE THAT WAS TO COUNT BOTH.***

---

### LEVEL 4 — BROWNFIELD: 24 CELLS

| cell | arm | problem | variant | T (tokens) | wall_s | turns | commands | done_reason | end | verdict | tests | TRUNCATED | source receipt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `b4fp01` | plain | FreeList | - | 1,879,395 | 379.1 | 4 | 21 | LANDED | LANDED | PASS | 7/7 | - | `cells-b4-freelist-plain.score.txt` |
| `b4fp02` | plain | FreeList | - | 2,600,634 | 436.3 | 3 | 30 | LANDED | LANDED | PASS | 7/7 | - | `cells-b4-freelist-plain.score.txt` |
| `b4fp03` | plain | FreeList | - | 1,774,426 | 292.8 | 3 | 21 | LANDED | LANDED | PASS | 7/7 | - | `cells-b4-freelist-plain.score.txt` |
| `b4lrp01` | plain | LRU | - | 689,672 | 160.8 | 4 | 7 | LANDED | LANDED | PASS | 16/16 | - | `cells-b4-lru-plain.score.txt` |
| `b4lrp02` | plain | LRU | - | 938,991 | 181.8 | 3 | 14 | LANDED | LANDED | PASS | 16/16 | - | `cells-b4-lru-plain.score.txt` |
| `b4lrp03` | plain | LRU | - | 1,094,683 | 242.9 | 4 | 7 | LANDED | LANDED | PASS | 16/16 | - | `cells-b4-lru-plain.score.txt` |
| `b4lzp01` | plain | LZW | - | 861,030 | 160.3 | 5 | 8 | LANDED | LANDED | PASS | 8/8 | - | `cells-b4-lzw-plain.score.txt` |
| `b4lzp02` | plain | LZW | - | 746,412 | 163.0 | 5 | 6 | LANDED | LANDED | PASS | 8/8 | - | `cells-b4-lzw-plain.score.txt` |
| `b4lzp03` | plain | LZW | - | 1,272,333 | 217.2 | 3 | 15 | LANDED | LANDED | PASS | 8/8 | - | `cells-b4-lzw-plain.score.txt` |
| `b4pp01` | plain | Paxos | - | 1,676,061 | 355.5 | 5 | 15 | LANDED | LANDED | PASS | 17/17 | - | `cells-b4-paxos-plain.score.txt` |
| `b4pp02` | plain | Paxos | - | 1,579,152 | 364.5 | 3 | 16 | LANDED | LANDED | PASS | 17/17 | - | `cells-b4-paxos-plain.score.txt` |
| `b4pp03` | plain | Paxos | - | 1,978,563 | 487.0 | 4 | 15 | LANDED | LANDED | PASS | 17/17 | - | `cells-b4-paxos-plain.score.txt` |
| `b4fs01` | salt-diet | FreeList | - | 22,415,870 | 4735.0 | 7 | 126 | LANDED | LANDED | FAIL | 3/7 | - | `cells-b4-freelist-saltdiet.score.txt` |
| `b4fs02` | salt-diet | FreeList | - | 37,315,180 | 6512.0 | 6 | 247 | LANDED | LANDED | FAIL | 3/7 | TRUNCATED | `cells-b4-freelist-saltdiet.score.txt` |
| `b4fs03` | salt-diet | FreeList | - | 70,076,140 | 9316.3 | 9 | 648 | LANDED | LANDED | PASS | 7/7 | TRUNCATED | `cells-b4-freelist-saltdiet.score.txt` |
| `b4lrs01` | salt-diet | LRU | - | 1,135,625 | 351.6 | 5 | 12 | LANDED | LANDED | PASS | 16/16 | - | `cells-b4-lru-saltdiet.score.txt` |
| `b4lrs02` | salt-diet | LRU | - | 4,709,417 | 1215.7 | 5 | 49 | LANDED | LANDED | PASS | 16/16 | - | `cells-b4-lru-saltdiet.score.txt` |
| `b4lrs03` | salt-diet | LRU | - | 6,267,951 | 1886.0 | 4 | 72 | LANDED | LANDED | FAIL | 10/16 | - | `cells-b4-lru-saltdiet.score.txt` |
| `b4lzs01` | salt-diet | LZW | tripwire | 12,582,495 | 2251.9 | 4 | 80 | LANDED | LANDED | PASS | 8/8 | TRUNCATED | `cells-b4-lzw-saltdiet-tripwire.score.txt` |
| `b4lzsb01` | salt-diet | LZW | b | 9,501,228 | 1128.7 | 4 | 80 | LANDED | LANDED | PASS | 8/8 | - | `cells-b4-lzw-saltdiet-b.score.txt` |
| `b4lzsb02` | salt-diet | LZW | b | 34,567,355 | 4346.7 | 6 | 219 | LANDED | LANDED | FAIL | 3/8 | TRUNCATED | `cells-b4-lzw-saltdiet-b.score.txt` |
| `b4ps01` | salt-diet | Paxos | - | 13,771,122 | 2812.3 | 7 | 93 | LANDED | LANDED | PASS | 17/17 | - | `cells-b4-paxos-saltdiet.score.txt` |
| `b4ps02` | salt-diet | Paxos | - | 9,357,512 | 2567.2 | 7 | 71 | LANDED | LANDED | SELF-NOT | the subject's | - | `cells-b4-paxos-saltdiet.score.txt` |
| `b4ps03` | salt-diet | Paxos | - | 16,590,636 | 4426.4 | 6 | 115 | LANDED | LANDED | FAIL | 12/17 | TRUNCATED | `cells-b4-paxos-saltdiet.score.txt` |

Receipts: `~/.fleet/executors/gemini.runs/l4-score-2026-09-14/`
---

### LEVEL 1 — P1 GREENFIELD: 49 CELL DIRECTORIES, 45 METERED

| cell | arm | problem | variant | T (tokens) | wall_s | turns | commands | done_reason | end | verdict | tests | TRUNCATED | source receipt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `s3cp01` | plain | Crc32 | - | 759,541 | 575.7 | 3 | 9 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-plain.score.txt` |
| `s3cp02` | plain | Crc32 | - | 861,120 | 217.3 | 3 | 15 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-plain.score.txt` |
| `s3cp03` | plain | Crc32 | - | 954,948 | 269.1 | 4 | 13 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-plain.score.txt` |
| `s3cpb01` | plain | Crc32 | v2 | 859,392 | 165.6 | 3 | 8 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-plain-v2.score.txt` |
| `s3cpb02` | plain | Crc32 | v2 | 1,193,654 | 206.6 | 3 | 13 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-plain-v2.score.txt` |
| `s3cpb03` | plain | Crc32 | v2 | 757,261 | 146.9 | 3 | 10 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-plain-v2.score.txt` |
| `s3cq01` | plain | Crc32 | stmt | 1,014,677 | 202.1 | 3 | 14 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-plain-stmt.score.txt` |
| `s3cq02` | plain | Crc32 | stmt | 1,222,527 | 217.5 | 3 | 24 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-plain-stmt.score.txt` |
| `s3cq03` | plain | Crc32 | stmt | 1,409,097 | 229.4 | 3 | 20 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-plain-stmt.score.txt` |
| `s3fp01` | plain | FreeList | - | 1,290,763 | 331.7 | 4 | 9 | LANDED | LANDED | PASS | 7/7 | - | `cells-s3-freelist-plain.score.txt` |
| `s3fp02` | plain | FreeList | - | - | - | - | - | - | - | - | - | - | `(not in any score receipt)` |
| `s3fp03` | plain | FreeList | - | - | - | - | - | - | - | - | - | - | `(not in any score receipt)` |
| `s3fpk01` | plain | FreeList | topup-s2k | 1,375,855 | 310.2 | 5 | 15 | LANDED | - | - | - | - | `(not in any score receipt)` |
| `s3fpk02` | plain | FreeList | topup-s2k | 1,627,758 | 316.2 | 3 | 16 | LANDED | - | - | - | - | `(not in any score receipt)` |
| `s3fq01` | plain | FreeList | stmt | 1,652,193 | 348.5 | 5 | 9 | LANDED | LANDED | PASS | 7/7 | - | `cells-s3-freelist-plain-stmt.score.txt` |
| `s3fq02` | plain | FreeList | stmt | 1,746,019 | 291.4 | 4 | 15 | LANDED | LANDED | PASS | 7/7 | - | `cells-s3-freelist-plain-stmt.score.txt` |
| `s3fq03` | plain | FreeList | stmt | - | - | - | - | - | - | - | - | - | `(not in any score receipt)` |
| `s3fqk01` | plain | FreeList | stmt-topup-s2k | 1,405,820 | 244.1 | 3 | 12 | LANDED | - | - | - | - | `(not in any score receipt)` |
| `s3lp01` | plain | LRU | - | 1,466,321 | 343.8 | 3 | 14 | LANDED | LANDED | PASS | 16/16 | - | `cells-s3-lru-plain.score.txt` |
| `s3lp02` | plain | LRU | - | 1,333,005 | 677.7 | 3 | 11 | LANDED | LANDED | PASS | 16/16 | - | `cells-s3-lru-plain.score.txt` |
| `s3lp03` | plain | LRU | - | 2,475,940 | 612.6 | 3 | 34 | LANDED | LANDED | PASS | 16/16 | - | `cells-s3-lru-plain.score.txt` |
| `s3lq01` | plain | LRU | stmt | 1,080,062 | 241.0 | 3 | 15 | LANDED | LANDED | PASS | 16/16 | - | `cells-s3-lru-plain-stmt.score.txt` |
| `s3lq02` | plain | LRU | stmt | 934,642 | 201.3 | 3 | 8 | LANDED | LANDED | PASS | 16/16 | - | `cells-s3-lru-plain-stmt.score.txt` |
| `s3lq03` | plain | LRU | stmt | 1,181,818 | 228.8 | 4 | 12 | LANDED | LANDED | PASS | 16/16 | - | `cells-s3-lru-plain-stmt.score.txt` |
| `s3pp01` | plain | Paxos | - | 1,114,181 | 214.2 | 3 | 16 | LANDED | LANDED | FAIL | 16/17 | - | `cells-s3-paxos-plain.score.txt` |
| `s3pp02` | plain | Paxos | - | 1,176,979 | 211.3 | 4 | 8 | LANDED | LANDED | FAIL | 16/17 | - | `cells-s3-paxos-plain.score.txt` |
| `s3pp03` | plain | Paxos | - | 2,315,056 | 417.2 | 3 | 20 | LANDED | LANDED | PASS | 17/17 | - | `cells-s3-paxos-plain.score.txt` |
| `s3cs01` | salt-diet | Crc32 | - | 7,155,492 | 1595.8 | 4 | 57 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-saltdiet.score.txt` |
| `s3cs02` | salt-diet | Crc32 | - | 11,502,404 | 1721.7 | 3 | 75 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-saltdiet.score.txt` |
| `s3cs03` | salt-diet | Crc32 | - | 9,675,734 | 1308.4 | 3 | 61 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-saltdiet.score.txt` |
| `s3ct01` | salt-diet | Crc32 | stmt | 22,967,361 | 1950.3 | 7 | 164 | LANDED | LANDED | PASS | 6/6 | TRUNCATED | `cells-s3-crc32-saltdiet-stmt.score.txt` |
| `s3ct02` | salt-diet | Crc32 | stmt | 11,474,133 | 1289.0 | 3 | 86 | LANDED | LANDED | PASS | 6/6 | - | `cells-s3-crc32-saltdiet-stmt.score.txt` |
| `s3ct03` | salt-diet | Crc32 | stmt | - | - | - | - | - | - | - | - | - | `(not in any score receipt)` |
| `s3ctk01` | salt-diet | Crc32 | stmt-topup-s2k | 14,646,915 | 1225.7 | 3 | 97 | LANDED | - | - | - | - | `(not in any score receipt)` |
| `s3fs01` | salt-diet | FreeList | - | 10,498,033 | 1966.1 | 8 | 78 | LANDED | LANDED | FAIL | 0/7 | - | `cells-s3-freelist-saltdiet.score.txt` |
| `s3fs02` | salt-diet | FreeList | - | 7,002,032 | 2188.9 | 6 | 33 | LANDED | LANDED | FAIL | 3/7 | - | `cells-s3-freelist-saltdiet.score.txt` |
| `s3fs03` | salt-diet | FreeList | - | 14,890,233 | 3172.9 | 5 | 102 | LANDED | LANDED | FAIL | 6/7 | - | `cells-s3-freelist-saltdiet.score.txt` |
| `s3ft01` | salt-diet | FreeList | stmt | 25,100,454 | 2508.1 | 4 | 178 | LANDED | LANDED | PASS | 7/7 | - | `cells-s3-freelist-saltdiet-stmt.score.txt` |
| `s3ft02` | salt-diet | FreeList | stmt | 12,610,137 | 5539.4 | 5 | 87 | TURN-TIMEOUT | PERSIS | NOT-LANDED | no LANDING.md: | - | `cells-s3-freelist-saltdiet-stmt.score.txt` |
| `s3ft03` | salt-diet | FreeList | stmt | 12,008,781 | 3597.6 | 5 | 69 | TURN-TIMEOUT | PERSIS | NOT-LANDED | no LANDING.md: | - | `cells-s3-freelist-saltdiet-stmt.score.txt` |
| `s3ls01` | salt-diet | LRU | - | 14,708,151 | 2578.5 | 5 | 120 | LANDED | PERSIS | PASS | 16/16 | TRUNCATED | `cells-s3-lru-saltdiet.score.txt` |
| `s3ls02` | salt-diet | LRU | - | 5,532,420 | 670.5 | 4 | 53 | LANDED | LANDED | PASS | 16/16 | - | `cells-s3-lru-saltdiet.score.txt` |
| `s3ls03` | salt-diet | LRU | - | 9,543,326 | 1317.9 | 3 | 92 | LANDED | LANDED | PASS | 16/16 | - | `cells-s3-lru-saltdiet.score.txt` |
| `s3lt01` | salt-diet | LRU | stmt | 10,360,342 | 988.8 | 4 | 106 | LANDED | LANDED | PASS | 16/16 | - | `cells-s3-lru-saltdiet-stmt.score.txt` |
| `s3lt02` | salt-diet | LRU | stmt | 13,689,750 | 2110.9 | 5 | 75 | LANDED | LANDED | PASS | 16/16 | TRUNCATED | `cells-s3-lru-saltdiet-stmt.score.txt` |
| `s3lt03` | salt-diet | LRU | stmt | 7,291,963 | 967.6 | 4 | 48 | LANDED | LANDED | PASS | 16/16 | - | `cells-s3-lru-saltdiet-stmt.score.txt` |
| `s3ps01` | salt-diet | Paxos | - | 8,572,636 | 831.9 | 4 | 71 | LANDED | LANDED | FAIL | 9/17 | - | `cells-s3-paxos-saltdiet.score.txt` |
| `s3ps02` | salt-diet | Paxos | - | 14,987,158 | 3576.9 | 6 | 71 | TURN-TIMEOUT | PERSIS | NOT-LANDED | no LANDING.md: | - | `cells-s3-paxos-saltdiet.score.txt` |
| `s3ps03` | salt-diet | Paxos | - | 23,396,293 | 3582.2 | 6 | 131 | TURN-TIMEOUT | PERSIS | NOT-LANDED | no LANDING.md: | - | `cells-s3-paxos-saltdiet.score.txt` |

Receipts: `~/.fleet/executors/gemini.runs/p1-greenfield-score-2026-09-13/`
---

## §T1 · PROVENANCE
```
  level 4   export_sha ecd3924828cb3b1255115a3094e2ceee51d62dfd (all 24, one sha)
            result of record: RESULT-gemini-brownfield-level4-2026-09-14.md
  level 1   the P1 greenfield wave, scored 2026-09-13
  meters    ctl/agy-meter-1.json      -> T, commands_run
            ctl/agy-turnloop-1.json   -> wall_seconds, turns_sent, turns_no_output, done_reason
            ⛔ the landing signal is the TURNLOOP file, never ctl/end-1, which is the PERSISTENCE
              PROBE's verdict and answers a different question.
  verdict   the per-condition score receipts named in each row's `source receipt` column
  client    agy · vendor google · gemini-3.1-pro-high (both levels)
```
**Every figure was read from the cell's own meter on the run box by this desk. No number in this file was
retyped from a bus post or from another seat's table.** The cross-checks that had to hold, and did:
level 1's metered split reproduces §L0's `plain 24 / salt-diet 21` independently; level 4's `b4lzs01`
reproduces the §L7 tripwire's banked `T=12,582,495 · wall 2251.9 · commands 80`; and the truncation
count reproduces per-receipt as 3 + 5 = 8.

## §T2 · WHAT THIS TABLE DOES NOT DO
It makes **no arm comparison at either level.** For level 1 the arm comparison is WITHHELD on the record
(token-refresh attrition, all salt-diet, n 1–4). For level 4 the comparison lives in its own result file
under a SIGN-ONLY freeze. **This file exists so that any future comparison can be audited against the
per-cell numbers rather than against a summary**, which is the whole of what was asked for.
