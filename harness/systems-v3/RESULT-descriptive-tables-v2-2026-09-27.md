# RESULT: FOUR DESCRIPTIVE TABLES OVER THE COMPLETE PILOT MATRIX (arXiv v2)
## Printed by `harness/systems-v3/tables_v2.py` at repo head `084f2fe9d41d` from the cell map `harness/systems-v3/CELLMAP-descriptive-tables-v2-2026-09-27.tsv`. Registered in `REGISTRATION-descriptive-tables-v2-2026-09-27.md` (§D1–§D6 and ADDENDUM 1), which was committed before this ran.

**CHECK numbers 171 + — 16 + declared 3 = 200 (other 10) against 181 + 16 + 3 = 200 ⇒ THE CHECK FAILS, AS REGISTERED (§D2): a DONE condition with any cell lacking a tracked figure prints `unmeasured`, and nothing is recovered by hand.**

⛔ **A descriptive reading over the complete matrix: no test, no p-value, no verdict on the arms. The registered tests remain §4's.** Every number below is a median of total tokens over a condition's cells of record (n = 3 for most; the n of each condition is printed in the output-token table).

- **`T` differs between lanes, so compare arms WITHIN a row.** Claude lane: input + cache writes + cache reads + output, from the session meter, counting EVERY session under the cell, including subordinate worker sessions on another model (most Opus matrix-1 and statement cells record claude-opus-5+claude-sonnet-5); the row's model is the cell's SUBJECT model. The block cells include the harness's sandbox probe in both arms (ADDENDUM 1 A1.3). agy lane (both Gemini models): input + output + cache read, with thinking inside output, as the vendor reports it.
- **`≥`** the median is a floor, because a cell at or below the median position stopped at the cost cap (CAP-COST), carries a meter that records an under-read (FLOOR), or was cut off by a registered turn or wall deadline (DEADLINE). The reason is named per cell at the foot of this file. The cap binds the salt-diet arm more often (census §T3, §U2, §V3).
- **`—`** inexpressible: Paxos × statement, both task forms, all four models (an arm-neutral formal statement cannot exist for a proof-obligation task). **`declared`** unreached at the cap (census ADDENDUM 19). **`unmeasured`** a DONE condition some of whose cells have no tracked token figure (listed next).
- A spec-change cell's figure is phase 1 + phase 2 (ADDENDUM 1 A1.1). For the Opus spec-change cells, phase 1 is the reused matrix-1 landing, so the same phase-1 figure also appears in that landing's own row.

## The 10 unmeasured conditions and the cells with no tracked figure
| model | problem | field | arm | extras | cells with no tracked T |
|---|---|---|---|---|---|
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | l8cpss01, l8cpss03 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | l5cq01, l5cq02, l5cq03 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | l5ct01, l5ct02, l5ct03 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | l5fq01, l5fq02, l5fq03 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | l5ft01, l5ft02, l5ft03 |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | l5lq01, l5lq02, l5lq03 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | l5lsra301, l5lsra302, l5lsra303 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | l5lt01, l5lt02, l5lt03 |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | l5ppr01, l5ppr02, l5ppr03 |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | l5psra201, l5psra202, l5psra203 |

## Cells in the map but OUTSIDE a condition's population (the result of record's scored cells govern, ADDENDUM 1 A1.4)
| map row | cell | why |
|---|---|---|
| none | - | every cell of record is in its condition |

## T1 · greenfield — median total tokens per condition (n per condition in the output-token table below)

| model | problem | bare-plain | bare-salt-diet | statement-plain | statement-salt-diet |
|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | ≥ 6,113,449 | ≥ 7,397,410 | 6,324,774 | 5,927,487 |
| claude-opus-5 | LRU | ≥ 8,155,664 | 13,297,929 | 8,352,122 | 16,265,999 |
| claude-opus-5 | FreeList | ≥ 11,914,579 | ≥ 46,242,329 | 19,470,666 | 32,830,752 |
| claude-opus-5 | LZW | 11,449,608 | 22,063,541 | ≥ 8,859,916 | ≥ 21,418,493 |
| claude-opus-5 | Paxos | ≥ 17,684,598 | 49,725,838 | — | — |
| claude-sonnet-5 | Crc32 | 2,042,023 | 12,950,272 | 2,181,020 | 11,335,722 |
| claude-sonnet-5 | LRU | 2,311,374 | 16,469,774 | 2,359,212 | 20,783,719 |
| claude-sonnet-5 | FreeList | 4,448,454 | ≥ 135,942,796 | 4,524,503 | 123,975,714 |
| claude-sonnet-5 | LZW | 2,373,486 | 43,839,178 | 3,555,507 | 30,210,414 |
| claude-sonnet-5 | Paxos | 4,996,639 | ≥ 123,495,570 | — | — |
| gemini-3.1-pro-high | Crc32 | 861,120 | 9,675,734 | 1,222,527 | ≥ 17,220,747 |
| gemini-3.1-pro-high | LRU | 1,466,321 | 9,543,326 | 1,080,062 | 10,360,342 |
| gemini-3.1-pro-high | FreeList | 1,290,763 | 10,498,033 | 1,699,106 | ≥ 12,610,137 |
| gemini-3.1-pro-high | LZW | 1,232,089 | 12,471,112 | 1,598,032 | ≥ 17,892,929 |
| gemini-3.1-pro-high | Paxos | 1,176,979 | ≥ 14,987,158 | — | — |
| gemini-3.8-flash-high | Crc32 | 3,993,025 | 12,112,123 | unmeasured | unmeasured |
| gemini-3.8-flash-high | LRU | 5,413,078 | unmeasured | unmeasured | unmeasured |
| gemini-3.8-flash-high | FreeList | 6,495,950 | 24,187,669 | unmeasured | unmeasured |
| gemini-3.8-flash-high | LZW | 4,244,069 | ≥ 23,941,795 | 5,147,496 | 18,215,862 |
| gemini-3.8-flash-high | Paxos | unmeasured | unmeasured | — | — |

## T2 · brownfield — median total tokens per condition (n per condition in the output-token table below)

| model | problem | bare-plain | bare-salt-diet | statement-plain | statement-salt-diet |
|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | 6,822,910 | 7,327,378 | 10,004,941 | 7,250,392 |
| claude-opus-5 | LRU | 7,807,170 | 16,927,118 | 9,747,753 | 16,074,704 |
| claude-opus-5 | FreeList | 20,264,692 | ≥ 41,750,816 | 18,887,102 | 35,880,068 |
| claude-opus-5 | LZW | 7,003,493 | 15,647,923 | 12,724,584 | 17,558,716 |
| claude-opus-5 | Paxos | 11,771,721 | 42,126,869 | — | — |
| claude-sonnet-5 | Crc32 | 1,844,699 | 10,573,448 | 2,055,677 | 10,051,058 |
| claude-sonnet-5 | LRU | 2,030,381 | 23,514,670 | 2,113,686 | 14,564,237 |
| claude-sonnet-5 | FreeList | 5,289,799 | ≥ 129,225,268 | 5,160,232 | ≥ 140,700,178 |
| claude-sonnet-5 | LZW | 3,115,443 | 59,322,626 | 2,641,673 | 58,601,805 |
| claude-sonnet-5 | Paxos | 6,151,825 | ≥ 154,795,624 | — | — |
| gemini-3.1-pro-high | Crc32 | 1,125,906 | 9,956,601 | 1,550,082 | 7,893,713 |
| gemini-3.1-pro-high | LRU | 938,991 | 4,709,417 | 1,355,238 | ≥ 13,573,895 |
| gemini-3.1-pro-high | FreeList | 1,949,814 | 15,150,465 | 1,822,259 | 14,174,074 |
| gemini-3.1-pro-high | LZW | 1,523,409 | ≥ 26,462,763 | 1,468,162 | 18,030,505 |
| gemini-3.1-pro-high | Paxos | 1,676,061 | 13,771,122 | — | — |
| gemini-3.8-flash-high | Crc32 | 4,325,246 | 9,683,589 | 5,376,845 | 13,141,849 |
| gemini-3.8-flash-high | LRU | 3,804,355 | 14,937,746 | 4,034,404 | 16,299,438 |
| gemini-3.8-flash-high | FreeList | 5,334,389 | 21,228,941 | 7,756,505 | 20,084,774 |
| gemini-3.8-flash-high | LZW | 6,555,430 | 17,493,691 | 5,919,649 | 13,256,712 |
| gemini-3.8-flash-high | Paxos | 7,992,405 | 18,713,325 | — | — |

## T3 · spec-change (greenfield only) — median total tokens per condition (n per condition in the output-token table below)

| model | problem | plain | salt-diet |
|---|---|---|---|
| claude-opus-5 | Crc32 | ≥ 22,634,955 | ≥ 17,114,730 |
| claude-opus-5 | LRU | ≥ 25,032,923 | 27,518,804 |
| claude-opus-5 | FreeList | ≥ 30,217,718 | 65,579,395 |
| claude-opus-5 | LZW | 23,086,951 | ≥ 48,465,177 |
| claude-opus-5 | Paxos | ≥ 29,599,611 | ≥ 60,070,155 |
| claude-sonnet-5 | Crc32 | 3,986,797 | 26,391,549 |
| claude-sonnet-5 | LRU | 3,311,062 | 31,561,498 |
| claude-sonnet-5 | FreeList | 12,827,827 | declared |
| claude-sonnet-5 | LZW | 9,016,104 | declared |
| claude-sonnet-5 | Paxos | 19,088,970 | declared |
| gemini-3.1-pro-high | Crc32 | 2,214,755 | unmeasured |
| gemini-3.1-pro-high | LRU | 2,506,278 | 14,309,400 |
| gemini-3.1-pro-high | FreeList | 3,357,987 | 19,724,118 |
| gemini-3.1-pro-high | LZW | 2,828,970 | 26,732,286 |
| gemini-3.1-pro-high | Paxos | 2,986,585 | ≥ 16,149,668 |
| gemini-3.8-flash-high | Crc32 | 8,827,684 | 20,838,181 |
| gemini-3.8-flash-high | LRU | 9,343,447 | 26,945,879 |
| gemini-3.8-flash-high | FreeList | 14,103,453 | 32,423,306 |
| gemini-3.8-flash-high | LZW | 9,189,665 | 36,488,484 |
| gemini-3.8-flash-high | Paxos | 13,889,277 | 122,524,014 |

## T4 · salt-diet ÷ plain, greenfield (registration §D4)

| model | problem | bare | statement | spec-change |
|---|---|---|---|---|
| claude-opus-5 | Crc32 | bounds only (1.21) | 0.94 | bounds only (0.76) |
| claude-opus-5 | LRU | ≤ 1.63 | 1.95 | ≤ 1.10 |
| claude-opus-5 | FreeList | bounds only (3.88) | 1.69 | ≤ 2.17 |
| claude-opus-5 | LZW | 1.93 | bounds only (2.42) | ≥ 2.10 |
| claude-opus-5 | Paxos | ≤ 2.81 | — | bounds only (2.03) |
| claude-sonnet-5 | Crc32 | 6.34 | 5.20 | 6.62 |
| claude-sonnet-5 | LRU | 7.13 | 8.81 | 9.53 |
| claude-sonnet-5 | FreeList | ≥ 30.56 | 27.40 | — |
| claude-sonnet-5 | LZW | 18.47 | 8.50 | — |
| claude-sonnet-5 | Paxos | ≥ 24.72 | — | — |
| gemini-3.1-pro-high | Crc32 | 11.24 | ≥ 14.09 | — |
| gemini-3.1-pro-high | LRU | 6.51 | 9.59 | 5.71 |
| gemini-3.1-pro-high | FreeList | 8.13 | ≥ 7.42 | 5.87 |
| gemini-3.1-pro-high | LZW | 10.12 | ≥ 11.20 | 9.45 |
| gemini-3.1-pro-high | Paxos | ≥ 12.73 | — | ≥ 5.41 |
| gemini-3.8-flash-high | Crc32 | 3.03 | — | 2.36 |
| gemini-3.8-flash-high | LRU | — | — | 2.88 |
| gemini-3.8-flash-high | FreeList | 3.72 | — | 2.30 |
| gemini-3.8-flash-high | LZW | ≥ 5.64 | 3.54 | 3.97 |
| gemini-3.8-flash-high | Paxos | — | — | 8.82 |

### T4 sign counts, per model per treatment (no p-value, by ruling)

| model | treatment | k of m ratios > 1 | indeterminate | median of the ratios | bounded among them |
|---|---|---|---|---|---|
| claude-opus-5 | bare | 1 of 1 | Crc32, LRU, FreeList, Paxos | 1.93 | 4 |
| claude-opus-5 | statement | 2 of 3 | LZW | 1.82 | 1 |
| claude-opus-5 | spec-change | 1 of 1 | Crc32, LRU, FreeList, Paxos | 2.03 | 5 |
| claude-sonnet-5 | bare | 5 of 5 | none | 18.47 | 2 |
| claude-sonnet-5 | statement | 4 of 4 | none | 8.65 | 0 |
| claude-sonnet-5 | spec-change | 2 of 2 | none | 8.08 | 0 |
| gemini-3.1-pro-high | bare | 5 of 5 | none | 10.12 | 1 |
| gemini-3.1-pro-high | statement | 4 of 4 | none | 10.39 | 3 |
| gemini-3.1-pro-high | spec-change | 4 of 4 | none | 5.79 | 1 |
| gemini-3.8-flash-high | bare | 3 of 3 | none | 3.72 | 1 |
| gemini-3.8-flash-high | statement | 1 of 1 | none | 3.54 | 0 |
| gemini-3.8-flash-high | spec-change | 5 of 5 | none | 2.88 | 0 |

### brownfield ratios (in the file, not in T4)

| model | problem | bare | statement |
|---|---|---|---|
| claude-opus-5 | Crc32 | 1.07 | 0.72 |
| claude-opus-5 | LRU | 2.17 | 1.65 |
| claude-opus-5 | FreeList | ≥ 2.06 | 1.90 |
| claude-opus-5 | LZW | 2.23 | 1.38 |
| claude-opus-5 | Paxos | 3.58 | — |
| claude-sonnet-5 | Crc32 | 5.73 | 4.89 |
| claude-sonnet-5 | LRU | 11.58 | 6.89 |
| claude-sonnet-5 | FreeList | ≥ 24.43 | ≥ 27.27 |
| claude-sonnet-5 | LZW | 19.04 | 22.18 |
| claude-sonnet-5 | Paxos | ≥ 25.16 | — |
| gemini-3.1-pro-high | Crc32 | 8.84 | 5.09 |
| gemini-3.1-pro-high | LRU | 5.02 | ≥ 10.02 |
| gemini-3.1-pro-high | FreeList | 7.77 | 7.78 |
| gemini-3.1-pro-high | LZW | ≥ 17.37 | 12.28 |
| gemini-3.1-pro-high | Paxos | 8.22 | — |
| gemini-3.8-flash-high | Crc32 | 2.24 | 2.44 |
| gemini-3.8-flash-high | LRU | 3.93 | 4.04 |
| gemini-3.8-flash-high | FreeList | 3.98 | 2.59 |
| gemini-3.8-flash-high | LZW | 2.67 | 2.24 |
| gemini-3.8-flash-high | Paxos | 2.34 | — |

## Per-condition medians of OUTPUT tokens (same rule; not in the tables)

| model | problem | field | arm | extras | n | median output | bounded |
|---|---|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | brownfield | plain | none | 3 | unmeasured | - |
| claude-opus-5 | Crc32 | brownfield | plain | statement | 3 | unmeasured | - |
| claude-opus-5 | Crc32 | brownfield | salt-diet | none | 3 | unmeasured | - |
| claude-opus-5 | Crc32 | brownfield | salt-diet | statement | 3 | unmeasured | - |
| claude-opus-5 | Crc32 | greenfield | plain | none | 3 | 90,245 | ≥ |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | 3 | 248,606 | ≥ |
| claude-opus-5 | Crc32 | greenfield | plain | statement | 3 | 100,787 |  |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 3 | 103,186 | ≥ |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 3 | 218,832 | ≥ |
| claude-opus-5 | Crc32 | greenfield | salt-diet | statement | 3 | 94,376 | ≥ |
| claude-opus-5 | FreeList | brownfield | plain | none | 3 | unmeasured | - |
| claude-opus-5 | FreeList | brownfield | plain | statement | 3 | unmeasured | - |
| claude-opus-5 | FreeList | brownfield | salt-diet | none | 3 | unmeasured | - |
| claude-opus-5 | FreeList | brownfield | salt-diet | statement | 3 | unmeasured | - |
| claude-opus-5 | FreeList | greenfield | plain | none | 3 | 256,678 | ≥ |
| claude-opus-5 | FreeList | greenfield | plain | spec-change | 2 | 447,010 | ≥ |
| claude-opus-5 | FreeList | greenfield | plain | statement | 3 | 298,070 | ≥ |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | 3 | 358,321 | ≥ |
| claude-opus-5 | FreeList | greenfield | salt-diet | spec-change | 1 | 472,269 |  |
| claude-opus-5 | FreeList | greenfield | salt-diet | statement | 3 | 278,812 |  |
| claude-opus-5 | LRU | brownfield | plain | none | 3 | unmeasured | - |
| claude-opus-5 | LRU | brownfield | plain | statement | 3 | unmeasured | - |
| claude-opus-5 | LRU | brownfield | salt-diet | none | 3 | unmeasured | - |
| claude-opus-5 | LRU | brownfield | salt-diet | statement | 3 | unmeasured | - |
| claude-opus-5 | LRU | greenfield | plain | none | 3 | 128,059 | ≥ |
| claude-opus-5 | LRU | greenfield | plain | spec-change | 2 | 266,342 | ≥ |
| claude-opus-5 | LRU | greenfield | plain | statement | 3 | 149,233 |  |
| claude-opus-5 | LRU | greenfield | salt-diet | none | 3 | 162,750 |  |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | 3 | 244,455 |  |
| claude-opus-5 | LRU | greenfield | salt-diet | statement | 3 | 179,724 |  |
| claude-opus-5 | LZW | brownfield | plain | none | 3 | unmeasured | - |
| claude-opus-5 | LZW | brownfield | plain | statement | 3 | unmeasured | - |
| claude-opus-5 | LZW | brownfield | salt-diet | none | 3 | unmeasured | - |
| claude-opus-5 | LZW | brownfield | salt-diet | statement | 3 | unmeasured | - |
| claude-opus-5 | LZW | greenfield | plain | none | 3 | 207,148 | ≥ |
| claude-opus-5 | LZW | greenfield | plain | spec-change | 2 | 340,414 |  |
| claude-opus-5 | LZW | greenfield | plain | statement | 3 | 163,226 | ≥ |
| claude-opus-5 | LZW | greenfield | salt-diet | none | 3 | 229,442 |  |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 3 | 444,036 |  |
| claude-opus-5 | LZW | greenfield | salt-diet | statement | 3 | 206,592 | ≥ |
| claude-opus-5 | Paxos | brownfield | plain | none | 3 | unmeasured | - |
| claude-opus-5 | Paxos | brownfield | salt-diet | none | 3 | unmeasured | - |
| claude-opus-5 | Paxos | greenfield | plain | none | 3 | 239,296 | ≥ |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | 2 | 445,010 | ≥ |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | 3 | 309,483 | ≥ |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | 2 | 553,022 | ≥ |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | 3 | unmeasured | - |
| claude-sonnet-5 | Crc32 | brownfield | plain | statement | 3 | unmeasured | - |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | 3 | unmeasured | - |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | statement | 3 | unmeasured | - |
| claude-sonnet-5 | Crc32 | greenfield | plain | none | 3 | unmeasured | - |
| claude-sonnet-5 | Crc32 | greenfield | plain | spec-change | 3 | unmeasured | - |
| claude-sonnet-5 | Crc32 | greenfield | plain | statement | 3 | unmeasured | - |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | none | 3 | unmeasured | - |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | statement | 3 | unmeasured | - |
| claude-sonnet-5 | FreeList | brownfield | plain | none | 3 | unmeasured | - |
| claude-sonnet-5 | FreeList | brownfield | plain | statement | 3 | unmeasured | - |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | 3 | unmeasured | - |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | 3 | unmeasured | - |
| claude-sonnet-5 | FreeList | greenfield | plain | none | 3 | unmeasured | - |
| claude-sonnet-5 | FreeList | greenfield | plain | spec-change | 3 | unmeasured | - |
| claude-sonnet-5 | FreeList | greenfield | plain | statement | 3 | unmeasured | - |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | 3 | unmeasured | - |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | statement | 3 | unmeasured | - |
| claude-sonnet-5 | LRU | brownfield | plain | none | 3 | unmeasured | - |
| claude-sonnet-5 | LRU | brownfield | plain | statement | 3 | unmeasured | - |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | 3 | unmeasured | - |
| claude-sonnet-5 | LRU | brownfield | salt-diet | statement | 3 | unmeasured | - |
| claude-sonnet-5 | LRU | greenfield | plain | none | 2 | unmeasured | - |
| claude-sonnet-5 | LRU | greenfield | plain | spec-change | 3 | unmeasured | - |
| claude-sonnet-5 | LRU | greenfield | plain | statement | 3 | unmeasured | - |
| claude-sonnet-5 | LRU | greenfield | salt-diet | none | 3 | unmeasured | - |
| claude-sonnet-5 | LRU | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| claude-sonnet-5 | LRU | greenfield | salt-diet | statement | 3 | unmeasured | - |
| claude-sonnet-5 | LZW | brownfield | plain | none | 3 | unmeasured | - |
| claude-sonnet-5 | LZW | brownfield | plain | statement | 3 | unmeasured | - |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | 3 | unmeasured | - |
| claude-sonnet-5 | LZW | brownfield | salt-diet | statement | 3 | unmeasured | - |
| claude-sonnet-5 | LZW | greenfield | plain | none | 3 | unmeasured | - |
| claude-sonnet-5 | LZW | greenfield | plain | spec-change | 3 | unmeasured | - |
| claude-sonnet-5 | LZW | greenfield | plain | statement | 3 | unmeasured | - |
| claude-sonnet-5 | LZW | greenfield | salt-diet | none | 3 | unmeasured | - |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | 3 | unmeasured | - |
| claude-sonnet-5 | Paxos | brownfield | plain | none | 3 | unmeasured | - |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | 3 | unmeasured | - |
| claude-sonnet-5 | Paxos | greenfield | plain | none | 3 | unmeasured | - |
| claude-sonnet-5 | Paxos | greenfield | plain | spec-change | 3 | unmeasured | - |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | none | 3 | 12,855 |  |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | statement | 3 | 12,036 |  |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | 3 | 68,719 |  |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | statement | 3 | 62,805 |  |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | 3 | unmeasured | - |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | spec-change | 3 | unmeasured | - |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | 3 | 13,836 |  |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | 3 | 63,153 |  |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | statement | 2 | 78,836 | ≥ |
| gemini-3.1-pro-high | FreeList | brownfield | plain | none | 3 | 26,378 |  |
| gemini-3.1-pro-high | FreeList | brownfield | plain | statement | 3 | 20,171 |  |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | none | 3 | 107,906 |  |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | statement | 3 | 71,265 |  |
| gemini-3.1-pro-high | FreeList | greenfield | plain | none | 1 | 28,101 |  |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | 3 | unmeasured | - |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | 2 | 25,360 |  |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | 3 | 97,646 |  |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | 3 | 80,906 | ≥ |
| gemini-3.1-pro-high | LRU | brownfield | plain | none | 3 | unmeasured | - |
| gemini-3.1-pro-high | LRU | brownfield | plain | statement | 3 | 15,062 |  |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | statement | 3 | 72,997 | ≥ |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | 3 | 19,409 |  |
| gemini-3.1-pro-high | LRU | greenfield | plain | spec-change | 3 | unmeasured | - |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | 3 | 14,749 |  |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | 3 | 63,692 |  |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | 3 | 86,575 | ≥ |
| gemini-3.1-pro-high | LZW | brownfield | plain | none | 3 | 17,376 |  |
| gemini-3.1-pro-high | LZW | brownfield | plain | statement | 3 | 16,180 |  |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | none | 3 | 211,494 | ≥ |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | statement | 3 | 106,629 | ≥ |
| gemini-3.1-pro-high | LZW | greenfield | plain | none | 3 | unmeasured | - |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | 3 | unmeasured | - |
| gemini-3.1-pro-high | LZW | greenfield | plain | statement | 3 | unmeasured | - |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | statement | 3 | unmeasured | - |
| gemini-3.1-pro-high | Paxos | brownfield | plain | none | 3 | unmeasured | - |
| gemini-3.1-pro-high | Paxos | brownfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | 3 | 19,368 |  |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | 3 | unmeasured | - |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | 3 | 117,176 | ≥ |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | none | 3 | 39,336 |  |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | statement | 3 | 42,034 |  |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | none | 3 | 65,511 |  |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | statement | 3 | 89,524 |  |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | spec-change | 3 | unmeasured | - |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | 3 | unmeasured | - |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | 3 | unmeasured | - |
| gemini-3.8-flash-high | FreeList | brownfield | plain | none | 3 | 75,139 |  |
| gemini-3.8-flash-high | FreeList | brownfield | plain | statement | 3 | 84,825 |  |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | none | 3 | 181,281 |  |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | statement | 3 | 126,201 |  |
| gemini-3.8-flash-high | FreeList | greenfield | plain | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | 3 | unmeasured | - |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | 3 | unmeasured | - |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | 3 | unmeasured | - |
| gemini-3.8-flash-high | LRU | brownfield | plain | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | LRU | brownfield | plain | statement | 3 | 45,024 |  |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | statement | 3 | 125,981 |  |
| gemini-3.8-flash-high | LRU | greenfield | plain | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | 3 | unmeasured | - |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | 3 | unmeasured | - |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | 3 | unmeasured | - |
| gemini-3.8-flash-high | LZW | brownfield | plain | none | 3 | 67,540 |  |
| gemini-3.8-flash-high | LZW | brownfield | plain | statement | 3 | 55,895 |  |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | none | 3 | 121,149 |  |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | statement | 3 | 100,662 |  |
| gemini-3.8-flash-high | LZW | greenfield | plain | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | 3 | unmeasured | - |
| gemini-3.8-flash-high | LZW | greenfield | plain | statement | 3 | unmeasured | - |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | 3 | unmeasured | - |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | statement | 3 | unmeasured | - |
| gemini-3.8-flash-high | Paxos | brownfield | plain | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | Paxos | brownfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | 3 | unmeasured | - |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | 3 | unmeasured | - |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | 3 | unmeasured | - |

## Per-cell figures and their sources (every table number derives from these rows)

| model | problem | field | arm | extras | cell | T | output | lower bound | source |
|---|---|---|---|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | greenfield | plain | none | 2d0c65b3 | 4,238,595 | 90,245 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=2d0c65b3].T |
| claude-opus-5 | Crc32 | greenfield | plain | none | 746d7d4e | 6,113,449 | 88,076 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=746d7d4e].T |
| claude-opus-5 | Crc32 | greenfield | plain | none | a87b7740 | 7,133,992 | 105,889 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=a87b7740].T |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 11165871 | 6,103,941 | 89,361 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=11165871].T |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 3e95075c | 7,397,410 | 103,186 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=3e95075c].T |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 57a33630 | 7,800,589 | 107,238 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=57a33630].T |
| claude-opus-5 | FreeList | greenfield | plain | none | 188f422b | 11,914,579 | 256,678 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=188f422b].T |
| claude-opus-5 | FreeList | greenfield | plain | none | 9cb8ce96 | 25,853,220 | 291,975 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9cb8ce96].T |
| claude-opus-5 | FreeList | greenfield | plain | none | n301free | 10,275,502 | 220,261 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-n3-topup,cell=n301free].T |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | 161b5a34 | 51,402,855 | 358,321 | CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=161b5a34].T |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | de4de8f2 | 46,111,487 | 400,633 | CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=de4de8f2].T |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | f33c7e65 | 46,242,329 | 344,020 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f33c7e65].T |
| claude-opus-5 | LRU | greenfield | plain | none | 3bdcbcbd | 7,129,652 | 128,059 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=3bdcbcbd].T |
| claude-opus-5 | LRU | greenfield | plain | none | 69e8c2c4 | 8,155,664 | 159,767 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=69e8c2c4].T |
| claude-opus-5 | LRU | greenfield | plain | none | n302lru | 11,425,345 | 119,301 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-n3-topup,cell=n302lru].T |
| claude-opus-5 | LRU | greenfield | salt-diet | none | 011fe22f | 13,297,929 | 139,437 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=011fe22f].T |
| claude-opus-5 | LRU | greenfield | salt-diet | none | b71994e3 | 10,991,055 | 165,972 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=b71994e3].T |
| claude-opus-5 | LRU | greenfield | salt-diet | none | d6b53ee4 | 18,395,807 | 162,750 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=d6b53ee4].T |
| claude-opus-5 | LZW | greenfield | plain | none | 93323249 | 7,548,942 | 135,270 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=93323249].T |
| claude-opus-5 | LZW | greenfield | plain | none | c34012e0 | 26,616,026 | 207,148 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=c34012e0].T |
| claude-opus-5 | LZW | greenfield | plain | none | d91f137b | 11,449,608 | 227,947 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=d91f137b].T |
| claude-opus-5 | LZW | greenfield | salt-diet | none | 18fb3eed | 42,908,306 | 270,412 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=18fb3eed].T |
| claude-opus-5 | LZW | greenfield | salt-diet | none | 7ac56e4e | 22,063,541 | 229,442 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=7ac56e4e].T |
| claude-opus-5 | LZW | greenfield | salt-diet | none | eb558398 | 20,932,053 | 205,932 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=eb558398].T |
| claude-opus-5 | Paxos | greenfield | plain | none | 60a056e6 | 8,612,291 | 143,465 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=60a056e6].T |
| claude-opus-5 | Paxos | greenfield | plain | none | f6462d47 | 17,684,598 | 267,652 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f6462d47].T |
| claude-opus-5 | Paxos | greenfield | plain | none | n303paxo | 18,251,444 | 239,296 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-n3-topup,cell=n303paxo].T |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | 6fc49f7c | 52,167,761 | 309,483 | FLOOR+CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=6fc49f7c].T |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | 9e6c8d4d | 49,725,838 | 345,892 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9e6c8d4d].T |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | b22d1000 | 29,443,369 | 297,463 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=b22d1000].T |
| claude-opus-5 | Crc32 | greenfield | plain | statement | st01crc3 | 6,324,774 | 90,751 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st01crc3].T |
| claude-opus-5 | Crc32 | greenfield | plain | statement | st02crc3 | 9,099,627 | 125,953 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st02crc3].T |
| claude-opus-5 | Crc32 | greenfield | plain | statement | st03crc3 | 6,206,287 | 100,787 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st03crc3].T |
| claude-opus-5 | Crc32 | greenfield | salt-diet | statement | st04crc3 | 10,673,708 | 94,376 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st04crc3].T |
| claude-opus-5 | Crc32 | greenfield | salt-diet | statement | st05crc3 | 5,927,487 | 74,828 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st05crc3].T |
| claude-opus-5 | Crc32 | greenfield | salt-diet | statement | st06crc3 | 5,828,821 | 95,106 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st06crc3].T |
| claude-opus-5 | LRU | greenfield | plain | statement | st07lru | 8,352,122 | 149,233 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st07lru].T |
| claude-opus-5 | LRU | greenfield | plain | statement | st08lru | 8,098,356 | 135,496 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st08lru].T |
| claude-opus-5 | LRU | greenfield | plain | statement | st09lru | 16,832,223 | 180,930 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st09lru].T |
| claude-opus-5 | LRU | greenfield | salt-diet | statement | st10lru | 21,652,262 | 197,379 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st10lru].T |
| claude-opus-5 | LRU | greenfield | salt-diet | statement | st11lru | 16,081,193 | 179,724 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st11lru].T |
| claude-opus-5 | LRU | greenfield | salt-diet | statement | st12lru | 16,265,999 | 152,800 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st12lru].T |
| claude-opus-5 | FreeList | greenfield | plain | statement | sf01free | 20,122,928 | 298,070 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf01free].T |
| claude-opus-5 | FreeList | greenfield | plain | statement | sf02free | 15,520,144 | 298,709 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf02free].T |
| claude-opus-5 | FreeList | greenfield | plain | statement | sf03free | 19,470,666 | 272,883 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf03free].T |
| claude-opus-5 | FreeList | greenfield | salt-diet | statement | sf04free | 38,764,962 | 272,820 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf04free].T |
| claude-opus-5 | FreeList | greenfield | salt-diet | statement | sf05free | 21,944,368 | 278,812 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf05free].T |
| claude-opus-5 | FreeList | greenfield | salt-diet | statement | sf06free | 32,830,752 | 299,659 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf06free].T |
| claude-opus-5 | LZW | greenfield | plain | statement | 22ee7d33 | 10,003,364 | 163,226 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=22ee7d33].T |
| claude-opus-5 | LZW | greenfield | plain | statement | 922d1ff0 | 8,337,703 | 205,473 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=922d1ff0].T |
| claude-opus-5 | LZW | greenfield | plain | statement | f795e96f | 8,859,916 | 139,043 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f795e96f].T |
| claude-opus-5 | LZW | greenfield | salt-diet | statement | 6d58f1ec | 26,366,793 | 246,489 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=6d58f1ec].T |
| claude-opus-5 | LZW | greenfield | salt-diet | statement | 9aca67c5 | 16,166,097 | 192,703 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9aca67c5].T |
| claude-opus-5 | LZW | greenfield | salt-diet | statement | f5f66c47 | 21,418,493 | 206,592 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f5f66c47].T |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | 2d0c65b3 | 18,143,900 | 248,606 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=2d0c65b3].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=2d0c65b3].T |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | 746d7d4e | 22,634,955 | 228,125 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=746d7d4e].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=746d7d4e].T |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | a87b7740 | 25,602,164 | 291,875 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=a87b7740].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=a87b7740].T |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 11165871 | 17,114,730 | 218,832 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=11165871].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=11165871].T |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 3e95075c | 15,339,098 | 205,197 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=3e95075c].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=3e95075c].T |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 57a33630 | 18,963,840 | 228,578 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=57a33630].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=57a33630].T |
| claude-opus-5 | FreeList | greenfield | plain | spec-change | 188f422b | 21,379,785 | 435,293 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=188f422b].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=188f422b].T |
| claude-opus-5 | FreeList | greenfield | plain | spec-change | 9cb8ce96 | 39,055,651 | 458,728 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9cb8ce96].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=9cb8ce96].T |
| claude-opus-5 | FreeList | greenfield | salt-diet | spec-change | f33c7e65 | 65,579,395 | 472,269 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f33c7e65].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=f33c7e65].T |
| claude-opus-5 | LRU | greenfield | plain | spec-change | 3bdcbcbd | 24,337,530 | 256,121 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=3bdcbcbd].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=3bdcbcbd].T |
| claude-opus-5 | LRU | greenfield | plain | spec-change | 69e8c2c4 | 25,728,316 | 276,562 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=69e8c2c4].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=69e8c2c4].T |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | 011fe22f | 31,255,736 | 238,851 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=011fe22f].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=011fe22f].T |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | b71994e3 | 21,960,298 | 247,620 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=b71994e3].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=b71994e3].T |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | d6b53ee4 | 27,518,804 | 244,455 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=d6b53ee4].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=d6b53ee4].T |
| claude-opus-5 | LZW | greenfield | plain | spec-change | 93323249 | 18,583,586 | 305,301 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=93323249].T + harness/systems-v3/RESULT-specchange-1-verdicts-2026-09-10.tsv [cell=93323249].T |
| claude-opus-5 | LZW | greenfield | plain | spec-change | 22ee7d33 | 27,590,316 | 375,527 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=22ee7d33].T + harness/systems-v3/RESULT-specchange-1-verdicts-2026-09-10.tsv [cell=22ee7d33].T |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 7ac56e4e | 38,943,666 | 424,072 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=7ac56e4e].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=7ac56e4e].T |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 18fb3eed | 63,818,792 | 444,036 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=18fb3eed].T + harness/systems-v3/RESULT-specchange-1-verdicts-2026-09-10.tsv [cell=18fb3eed].T |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 6d58f1ec | 48,465,177 | 446,447 | CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=6d58f1ec].T + harness/systems-v3/RESULT-specchange-1-verdicts-2026-09-10.tsv [cell=6d58f1ec].T |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | 60a056e6 | 22,197,624 | 352,305 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=60a056e6].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=60a056e6].T |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | f6462d47 | 37,001,598 | 537,714 | FLOOR+CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f6462d47].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=f6462d47].T |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | 9e6c8d4d | 67,659,675 | 599,945 | CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9e6c8d4d].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=9e6c8d4d].T |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | b22d1000 | 52,480,635 | 506,098 | CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=b22d1000].T + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=b22d1000].T |
| claude-opus-5 | Crc32 | brownfield | plain | none | clbocp01 | 5,266,116 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocp01].final_T |
| claude-opus-5 | Crc32 | brownfield | plain | none | clbocp02 | 6,822,910 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocp02].final_T |
| claude-opus-5 | Crc32 | brownfield | plain | none | clbocp03 | 9,589,042 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocp03].final_T |
| claude-opus-5 | Crc32 | brownfield | salt-diet | none | clbocs01 | 7,782,203 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocs01].final_T |
| claude-opus-5 | Crc32 | brownfield | salt-diet | none | clbocs02 | 7,327,378 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocs02].final_T |
| claude-opus-5 | Crc32 | brownfield | salt-diet | none | clbocs03 | 6,335,698 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocs03].final_T |
| claude-opus-5 | FreeList | brownfield | plain | none | clbofp01 | 25,682,114 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofp01].final_T |
| claude-opus-5 | FreeList | brownfield | plain | none | clbofp02 | 13,033,840 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofp02].final_T |
| claude-opus-5 | FreeList | brownfield | plain | none | clbofp03 | 20,264,692 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofp03].final_T |
| claude-opus-5 | FreeList | brownfield | salt-diet | none | clbofs01 | 41,750,816 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofs01].final_T |
| claude-opus-5 | FreeList | brownfield | salt-diet | none | clbofs02 | 41,363,282 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofs02].final_T |
| claude-opus-5 | FreeList | brownfield | salt-diet | none | clbofs03 | 47,729,585 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofs03].final_T |
| claude-opus-5 | LRU | brownfield | plain | none | clbolp01 | 5,968,346 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbolp01].final_T |
| claude-opus-5 | LRU | brownfield | plain | none | clbolp02 | 8,180,485 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbolp02].final_T |
| claude-opus-5 | LRU | brownfield | plain | none | clbolp03 | 7,807,170 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbolp03].final_T |
| claude-opus-5 | LRU | brownfield | salt-diet | none | clbols01 | 21,632,596 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbols01].final_T |
| claude-opus-5 | LRU | brownfield | salt-diet | none | clbols02 | 10,151,831 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbols02].final_T |
| claude-opus-5 | LRU | brownfield | salt-diet | none | clbols03 | 16,927,118 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbols03].final_T |
| claude-opus-5 | Paxos | brownfield | plain | none | clbopp01 | 16,193,790 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbopp01].final_T |
| claude-opus-5 | Paxos | brownfield | plain | none | clbopp02 | 11,771,721 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbopp02].final_T |
| claude-opus-5 | Paxos | brownfield | plain | none | clbopp03 | 8,960,216 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbopp03].final_T |
| claude-opus-5 | Paxos | brownfield | salt-diet | none | clbops01 | 41,471,247 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbops01].final_T |
| claude-opus-5 | Paxos | brownfield | salt-diet | none | clbops02 | 42,126,869 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbops02].final_T |
| claude-opus-5 | Paxos | brownfield | salt-diet | none | clbops03 | 48,704,960 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbops03].final_T |
| claude-opus-5 | LZW | brownfield | plain | none | clbozp01 | 7,003,493 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozp01].final_T |
| claude-opus-5 | LZW | brownfield | plain | none | clbozp02 | 12,863,535 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozp02].final_T |
| claude-opus-5 | LZW | brownfield | plain | none | clbozp03 | 6,967,376 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozp03].final_T |
| claude-opus-5 | LZW | brownfield | salt-diet | none | clbozs01 | 15,100,563 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozs01].final_T |
| claude-opus-5 | LZW | brownfield | salt-diet | none | clbozs02 | 24,529,965 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozs02].final_T |
| claude-opus-5 | LZW | brownfield | salt-diet | none | clbozs03 | 15,647,923 | - | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozs03].final_T |
| claude-opus-5 | Crc32 | brownfield | plain | statement | clbtcp01 | 10,004,941 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcp01].final_T |
| claude-opus-5 | Crc32 | brownfield | plain | statement | clbtcp02 | 8,965,677 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcp02].final_T |
| claude-opus-5 | Crc32 | brownfield | plain | statement | clbtcp03 | 10,088,207 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcp03].final_T |
| claude-opus-5 | Crc32 | brownfield | salt-diet | statement | clbtcs01 | 7,779,504 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcs01].final_T |
| claude-opus-5 | Crc32 | brownfield | salt-diet | statement | clbtcs02 | 7,250,392 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcs02].final_T |
| claude-opus-5 | Crc32 | brownfield | salt-diet | statement | clbtcs03 | 6,758,082 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcs03].final_T |
| claude-opus-5 | FreeList | brownfield | plain | statement | clbtfp01 | 22,226,064 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfp01].final_T |
| claude-opus-5 | FreeList | brownfield | plain | statement | clbtfp02 | 18,887,102 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfp02].final_T |
| claude-opus-5 | FreeList | brownfield | plain | statement | clbtfp03 | 15,254,481 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfp03].final_T |
| claude-opus-5 | FreeList | brownfield | salt-diet | statement | clbtfs01 | 48,426,494 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfs01].final_T |
| claude-opus-5 | FreeList | brownfield | salt-diet | statement | clbtfs02 | 35,880,068 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfs02].final_T |
| claude-opus-5 | FreeList | brownfield | salt-diet | statement | clbtfs03 | 35,794,655 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfs03].final_T |
| claude-opus-5 | LRU | brownfield | plain | statement | clbtlp01 | 10,581,714 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtlp01].final_T |
| claude-opus-5 | LRU | brownfield | plain | statement | clbtlp02 | 9,747,753 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtlp02].final_T |
| claude-opus-5 | LRU | brownfield | plain | statement | clbtlp03 | 8,213,518 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtlp03].final_T |
| claude-opus-5 | LRU | brownfield | salt-diet | statement | clbtls01 | 17,007,405 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtls01].final_T |
| claude-opus-5 | LRU | brownfield | salt-diet | statement | clbtls02 | 16,074,704 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtls02].final_T |
| claude-opus-5 | LRU | brownfield | salt-diet | statement | clbtls03 | 15,643,247 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtls03].final_T |
| claude-opus-5 | LZW | brownfield | plain | statement | clbtzp01 | 17,582,989 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzp01].final_T |
| claude-opus-5 | LZW | brownfield | plain | statement | clbtzp02 | 12,724,584 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzp02].final_T |
| claude-opus-5 | LZW | brownfield | plain | statement | clbtzp03 | 10,051,429 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzp03].final_T |
| claude-opus-5 | LZW | brownfield | salt-diet | statement | clbtzs01 | 17,558,716 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzs01].final_T |
| claude-opus-5 | LZW | brownfield | salt-diet | statement | clbtzs02 | 14,894,719 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzs02].final_T |
| claude-opus-5 | LZW | brownfield | salt-diet | statement | clbtzs03 | 26,951,777 | - | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzs03].final_T |
| claude-sonnet-5 | Crc32 | greenfield | plain | none | clbgcp01 | 2,474,488 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcp01].final_T |
| claude-sonnet-5 | Crc32 | greenfield | plain | none | clbgcp02 | 2,042,023 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcp02].final_T |
| claude-sonnet-5 | Crc32 | greenfield | plain | none | clbgcp03 | 2,009,210 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcp03].final_T |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | none | clbgcs01 | 12,950,272 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcs01].final_T |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | none | clbgcs02 | 11,381,650 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcs02].final_T |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | none | clbgcs03 | 13,836,693 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcs03].final_T |
| claude-sonnet-5 | FreeList | greenfield | plain | none | clbgfp01 | 4,448,454 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfp01].final_T |
| claude-sonnet-5 | FreeList | greenfield | plain | none | clbgfp02 | 3,106,464 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfp02].final_T |
| claude-sonnet-5 | FreeList | greenfield | plain | none | clbgfp03 | 6,063,783 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfp03].final_T |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | clbgfs01 | 139,276,603 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs01].final_T |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | clbgfs02 | 127,433,176 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs02].final_T |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | clbgfs03 | 135,942,796 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs03].final_T |
| claude-sonnet-5 | LRU | greenfield | plain | none | clbglp02 | 3,058,181 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbglp02].final_T |
| claude-sonnet-5 | LRU | greenfield | plain | none | clbglp03 | 1,564,566 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbglp03].final_T |
| claude-sonnet-5 | LRU | greenfield | salt-diet | none | clbgls01 | 16,469,774 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgls01].final_T |
| claude-sonnet-5 | LRU | greenfield | salt-diet | none | clbgls02 | 12,476,238 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgls02].final_T |
| claude-sonnet-5 | LRU | greenfield | salt-diet | none | clbgls03 | 32,457,693 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgls03].final_T |
| claude-sonnet-5 | Paxos | greenfield | plain | none | clbgpp01 | 4,996,639 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgpp01].final_T |
| claude-sonnet-5 | Paxos | greenfield | plain | none | clbgpp02 | 4,868,329 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgpp02].final_T |
| claude-sonnet-5 | Paxos | greenfield | plain | none | clbgpp03 | 6,148,643 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgpp03].final_T |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | none | clbgps01 | 123,495,570 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps01].final_T |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | none | clbgps02 | 149,820,582 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps02].final_T |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | none | clbgps03 | 86,587,129 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps03].final_T |
| claude-sonnet-5 | LZW | greenfield | plain | none | clbgzp01 | 2,920,748 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzp01].final_T |
| claude-sonnet-5 | LZW | greenfield | plain | none | clbgzp02 | 2,373,486 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzp02].final_T |
| claude-sonnet-5 | LZW | greenfield | plain | none | clbgzp03 | 1,835,927 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzp03].final_T |
| claude-sonnet-5 | LZW | greenfield | salt-diet | none | clbgzs01 | 43,370,291 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzs01].final_T |
| claude-sonnet-5 | LZW | greenfield | salt-diet | none | clbgzs02 | 45,674,079 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzs02].final_T |
| claude-sonnet-5 | LZW | greenfield | salt-diet | none | clbgzs03 | 43,839,178 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzs03].final_T |
| claude-sonnet-5 | Crc32 | greenfield | plain | statement | clbscp01 | 2,401,900 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscp01].final_T |
| claude-sonnet-5 | Crc32 | greenfield | plain | statement | clbscp02 | 2,181,020 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscp02].final_T |
| claude-sonnet-5 | Crc32 | greenfield | plain | statement | clbscp03 | 1,879,690 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscp03].final_T |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | statement | clbscs01 | 10,489,614 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscs01].final_T |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | statement | clbscs02 | 11,335,722 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscs02].final_T |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | statement | clbscs03 | 15,926,283 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscs03].final_T |
| claude-sonnet-5 | FreeList | greenfield | plain | statement | clbsfp01 | 4,083,049 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfp01].final_T |
| claude-sonnet-5 | FreeList | greenfield | plain | statement | clbsfp02 | 6,054,020 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfp02].final_T |
| claude-sonnet-5 | FreeList | greenfield | plain | statement | clbsfp03 | 4,524,503 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfp03].final_T |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | statement | clbsfs01 | 123,975,714 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfs01].final_T |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | statement | clbsfs02 | 131,994,064 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfs02].final_T |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | statement | clbsfs03 | 77,734,284 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfs03].final_T |
| claude-sonnet-5 | LRU | greenfield | plain | statement | clbslp01 | 2,359,212 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbslp01].final_T |
| claude-sonnet-5 | LRU | greenfield | plain | statement | clbslp02 | 3,258,928 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbslp02].final_T |
| claude-sonnet-5 | LRU | greenfield | plain | statement | clbslp03 | 1,613,442 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbslp03].final_T |
| claude-sonnet-5 | LRU | greenfield | salt-diet | statement | clbsls01 | 13,494,723 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsls01].final_T |
| claude-sonnet-5 | LRU | greenfield | salt-diet | statement | clbsls02 | 22,909,164 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsls02].final_T |
| claude-sonnet-5 | LRU | greenfield | salt-diet | statement | clbsls03 | 20,783,719 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsls03].final_T |
| claude-sonnet-5 | LZW | greenfield | plain | statement | clbszp01 | 3,842,229 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszp01].final_T |
| claude-sonnet-5 | LZW | greenfield | plain | statement | clbszp02 | 3,148,365 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszp02].final_T |
| claude-sonnet-5 | LZW | greenfield | plain | statement | clbszp03 | 3,555,507 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszp03].final_T |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | clbszs01 | 30,210,414 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszs01].final_T |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | clbszs02 | 134,678,654 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszs02].final_T |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | clbszs03 | 25,368,840 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszs03].final_T |
| claude-sonnet-5 | Crc32 | brownfield | plain | statement | clbucp01 | 1,627,339 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucp01].final_T |
| claude-sonnet-5 | Crc32 | brownfield | plain | statement | clbucp02 | 2,055,677 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucp02].final_T |
| claude-sonnet-5 | Crc32 | brownfield | plain | statement | clbucp03 | 3,041,997 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucp03].final_T |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | statement | clbucs01 | 10,051,058 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucs01].final_T |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | statement | clbucs02 | 8,063,545 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucs02].final_T |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | statement | clbucs03 | 12,317,970 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucs03].final_T |
| claude-sonnet-5 | FreeList | brownfield | plain | statement | clbufp01 | 5,160,232 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufp01].final_T |
| claude-sonnet-5 | FreeList | brownfield | plain | statement | clbufp02 | 5,463,328 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufp02].final_T |
| claude-sonnet-5 | FreeList | brownfield | plain | statement | clbufp03 | 4,284,702 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufp03].final_T |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | clbufs01 | 142,876,385 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs01].final_T |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | clbufs02 | 140,700,178 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs02].final_T |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | clbufs03 | 136,827,691 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs03].final_T |
| claude-sonnet-5 | LRU | brownfield | plain | statement | clbulp01 | 2,113,686 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbulp01].final_T |
| claude-sonnet-5 | LRU | brownfield | plain | statement | clbulp02 | 2,460,543 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbulp02].final_T |
| claude-sonnet-5 | LRU | brownfield | plain | statement | clbulp03 | 1,785,078 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbulp03].final_T |
| claude-sonnet-5 | LRU | brownfield | salt-diet | statement | clbuls01 | 9,775,413 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuls01].final_T |
| claude-sonnet-5 | LRU | brownfield | salt-diet | statement | clbuls02 | 14,571,647 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuls02].final_T |
| claude-sonnet-5 | LRU | brownfield | salt-diet | statement | clbuls03 | 14,564,237 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuls03].final_T |
| claude-sonnet-5 | LZW | brownfield | plain | statement | clbuzp01 | 2,641,673 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzp01].final_T |
| claude-sonnet-5 | LZW | brownfield | plain | statement | clbuzp02 | 4,075,553 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzp02].final_T |
| claude-sonnet-5 | LZW | brownfield | plain | statement | clbuzp03 | 2,403,130 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzp03].final_T |
| claude-sonnet-5 | LZW | brownfield | salt-diet | statement | clbuzs01 | 22,230,424 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzs01].final_T |
| claude-sonnet-5 | LZW | brownfield | salt-diet | statement | clbuzs02 | 66,700,375 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzs02].final_T |
| claude-sonnet-5 | LZW | brownfield | salt-diet | statement | clbuzs03 | 58,601,805 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzs03].final_T |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | clbbcp01 | 1,864,663 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcp01].final_T |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | clbbcp02 | 1,136,732 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcp02].final_T |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | clbbcp03 | 1,844,699 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcp03].final_T |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | clbbcs01 | 10,573,448 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcs01].final_T |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | clbbcs02 | 17,300,243 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcs02].final_T |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | clbbcs03 | 9,111,645 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcs03].final_T |
| claude-sonnet-5 | FreeList | brownfield | plain | none | clbbfp01 | 9,510,181 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfp01].final_T |
| claude-sonnet-5 | FreeList | brownfield | plain | none | clbbfp02 | 2,659,762 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfp02].final_T |
| claude-sonnet-5 | FreeList | brownfield | plain | none | clbbfp03 | 5,289,799 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfp03].final_T |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | clbbfs01 | 139,053,716 | - | CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs01].final_T |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | clbbfs02 | 96,655,548 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs02].final_T |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | clbbfs03 | 129,225,268 | - | CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs03].final_T |
| claude-sonnet-5 | LRU | brownfield | plain | none | clbblp01 | 2,030,381 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbblp01].final_T |
| claude-sonnet-5 | LRU | brownfield | plain | none | clbblp02 | 1,960,957 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbblp02].final_T |
| claude-sonnet-5 | LRU | brownfield | plain | none | clbblp03 | 2,259,355 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbblp03].final_T |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | clbbls01 | 17,021,913 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbls01].final_T |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | clbbls02 | 23,514,670 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbls02].final_T |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | clbbls03 | 28,968,853 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbls03].final_T |
| claude-sonnet-5 | Paxos | brownfield | plain | none | clbbpp01 | 6,151,825 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbpp01].final_T |
| claude-sonnet-5 | Paxos | brownfield | plain | none | clbbpp02 | 5,907,946 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbpp02].final_T |
| claude-sonnet-5 | Paxos | brownfield | plain | none | clbbpp03 | 6,674,641 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbpp03].final_T |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | clbbps01 | 94,783,997 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps01].final_T |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | clbbps02 | 154,970,100 | - | CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps02].final_T |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | clbbps03 | 154,795,624 | - | CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps03].final_T |
| claude-sonnet-5 | LZW | brownfield | plain | none | clbbzp01 | 3,115,443 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzp01].final_T |
| claude-sonnet-5 | LZW | brownfield | plain | none | clbbzp02 | 3,989,904 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzp02].final_T |
| claude-sonnet-5 | LZW | brownfield | plain | none | clbbzp03 | 1,660,569 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzp03].final_T |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | clbbzs01 | 59,322,626 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzs01].final_T |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | clbbzs02 | 64,809,739 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzs02].final_T |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | clbbzs03 | 42,027,486 | - | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzs03].final_T |
| claude-sonnet-5 | Crc32 | greenfield | plain | spec-change | clbccp01 | 5,517,599 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp01].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp01].p2_T |
| claude-sonnet-5 | Crc32 | greenfield | plain | spec-change | clbccp02 | 3,986,797 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp02].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp02].p2_T |
| claude-sonnet-5 | Crc32 | greenfield | plain | spec-change | clbccp03 | 3,986,038 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp03].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp03].p2_T |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | spec-change | clbccs01 | 32,292,496 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs01].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs01].p2_T |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | spec-change | clbccs02 | 26,391,549 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs02].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs02].p2_T |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | spec-change | clbccs03 | 20,073,884 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs03].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs03].p2_T |
| claude-sonnet-5 | FreeList | greenfield | plain | spec-change | clbcfp01 | 8,339,514 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp01].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp01].p2_T |
| claude-sonnet-5 | FreeList | greenfield | plain | spec-change | clbcfp02 | 12,827,827 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp02].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp02].p2_T |
| claude-sonnet-5 | FreeList | greenfield | plain | spec-change | clbcfp03 | 14,323,283 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp03].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp03].p2_T |
| claude-sonnet-5 | LRU | greenfield | plain | spec-change | clbclp01 | 4,392,002 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp01].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp01].p2_T |
| claude-sonnet-5 | LRU | greenfield | plain | spec-change | clbclp02 | 3,311,062 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp02].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp02].p2_T |
| claude-sonnet-5 | LRU | greenfield | plain | spec-change | clbclp03 | 3,130,034 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp03].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp03].p2_T |
| claude-sonnet-5 | LRU | greenfield | salt-diet | spec-change | clbcls01 | 31,561,498 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls01].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls01].p2_T |
| claude-sonnet-5 | LRU | greenfield | salt-diet | spec-change | clbcls02 | 18,469,872 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls02].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls02].p2_T |
| claude-sonnet-5 | LRU | greenfield | salt-diet | spec-change | clbcls03 | 47,674,308 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls03].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls03].p2_T |
| claude-sonnet-5 | Paxos | greenfield | plain | spec-change | clbcpp01 | 19,088,970 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp01].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp01].p2_T |
| claude-sonnet-5 | Paxos | greenfield | plain | spec-change | clbcpp02 | 13,041,725 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp02].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp02].p2_T |
| claude-sonnet-5 | Paxos | greenfield | plain | spec-change | clbcpp03 | 25,411,064 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp03].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp03].p2_T |
| claude-sonnet-5 | LZW | greenfield | plain | spec-change | clbczp01 | 10,474,410 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp01].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp01].p2_T |
| claude-sonnet-5 | LZW | greenfield | plain | spec-change | clbczp02 | 9,016,104 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp02].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp02].p2_T |
| claude-sonnet-5 | LZW | greenfield | plain | spec-change | clbczp03 | 7,714,353 | - | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp03].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp03].p2_T |
| claude-sonnet-5 | LZW | greenfield | salt-diet | spec-change | clbczs01 | 79,106,739 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs01].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs01].p2_T |
| claude-sonnet-5 | LZW | greenfield | salt-diet | spec-change | clbczs02 | 61,646,533 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs02].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs02].p2_T |
| claude-sonnet-5 | LZW | greenfield | salt-diet | spec-change | clbczs03 | 58,669,381 | - | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs03].p1_T + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs03].p2_T |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | spec-change | clbcfs01 | unmeasured | - | CAP-COST | no tracked source |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | spec-change | clbcfs02 | unmeasured | - | CAP-COST | no tracked source |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | spec-change | clbcfs03 | unmeasured | - | CAP-COST | no tracked source |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | spec-change | clbcps01 | unmeasured | - | CAP-COST | no tracked source |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | spec-change | clbcps02 | unmeasured | - | CAP-COST | no tracked source |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | spec-change | clbcps03 | unmeasured | - | CAP-COST | no tracked source |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | s3cp01 | 759,541 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:85 col 'T (tokens)' |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | s3cp02 | 861,120 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:86 col 'T (tokens)' |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | s3cp03 | 954,948 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:87 col 'T (tokens)' |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | s3cs01 | 7,155,492 | 62,879 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3cs01].T |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | s3cs02 | 11,502,404 | 64,620 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3cs02].T |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | s3cs03 | 9,675,734 | 63,153 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3cs03].T |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | s3lp01 | 1,466,321 | 19,409 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3lp01].T |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | s3lp02 | 1,333,005 | 12,305 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3lp02].T |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | s3lp03 | 2,475,940 | 22,968 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3lp03].T |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | s3ls01 | 14,708,151 | 91,157 | DEADLINE | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ls01].T |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | s3ls02 | 5,532,420 | 57,344 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ls02].T |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | s3ls03 | 9,543,326 | 63,692 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ls03].T |
| gemini-3.1-pro-high | FreeList | greenfield | plain | none | s3fp01 | 1,290,763 | 28,101 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3fp01].T |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | s3fs01 | 10,498,033 | 110,900 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3fs01].T |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | s3fs02 | 7,002,032 | 71,102 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3fs02].T |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | s3fs03 | 14,890,233 | 97,646 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3fs03].T |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | s3pp01 | 1,114,181 | 19,368 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3pp01].T |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | s3pp02 | 1,176,979 | 18,636 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3pp02].T |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | s3pp03 | 2,315,056 | 40,060 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3pp03].T |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | s3ps01 | 8,572,636 | 63,331 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ps01].T |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | s3ps02 | 14,987,158 | 117,176 | DEADLINE | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ps02].T |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | s3ps03 | 23,396,293 | 132,908 | DEADLINE | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ps03].T |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | s3cq01 | 1,014,677 | 14,042 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3cq01].T |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | s3cq02 | 1,222,527 | 11,611 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3cq02].T |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | s3cq03 | 1,409,097 | 13,836 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3cq03].T |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | statement | s3ct01 | 22,967,361 | 96,763 | DEADLINE | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ct01].T |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | statement | s3ct02 | 11,474,133 | 60,909 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ct02].T |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | s3lq01 | 1,080,062 | 14,749 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3lq01].T |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | s3lq02 | 934,642 | 12,658 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3lq02].T |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | s3lq03 | 1,181,818 | 18,138 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3lq03].T |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | s3lt01 | 10,360,342 | 96,876 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3lt01].T |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | s3lt02 | 13,689,750 | 74,148 | DEADLINE | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3lt02].T |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | s3lt03 | 7,291,963 | 86,575 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3lt03].T |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | s3fq01 | 1,652,193 | 27,694 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3fq01].T |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | s3fq02 | 1,746,019 | 23,026 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3fq02].T |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | s3ft01 | 25,100,454 | 143,047 | - | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ft01].T |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | s3ft02 | 12,610,137 | 80,594 | DEADLINE | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ft02].T |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | s3ft03 | 12,008,781 | 80,906 | DEADLINE | harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [cell=s3ft03].T |
| gemini-3.1-pro-high | LRU | brownfield | plain | none | b4lrp01 | 689,672 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:56 col 'T (tokens)' |
| gemini-3.1-pro-high | LRU | brownfield | plain | none | b4lrp02 | 938,991 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:57 col 'T (tokens)' |
| gemini-3.1-pro-high | LRU | brownfield | plain | none | b4lrp03 | 1,094,683 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:58 col 'T (tokens)' |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | none | b4lrs01 | 1,135,625 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:68 col 'T (tokens)' |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | none | b4lrs02 | 4,709,417 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:69 col 'T (tokens)' |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | none | b4lrs03 | 6,267,951 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:70 col 'T (tokens)' |
| gemini-3.1-pro-high | Paxos | brownfield | plain | none | b4pp01 | 1,676,061 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:62 col 'T (tokens)' |
| gemini-3.1-pro-high | Paxos | brownfield | plain | none | b4pp02 | 1,579,152 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:63 col 'T (tokens)' |
| gemini-3.1-pro-high | Paxos | brownfield | plain | none | b4pp03 | 1,978,563 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:64 col 'T (tokens)' |
| gemini-3.1-pro-high | Paxos | brownfield | salt-diet | none | b4ps01 | 13,771,122 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:74 col 'T (tokens)' |
| gemini-3.1-pro-high | Paxos | brownfield | salt-diet | none | b4ps02 | 9,357,512 | - | - | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:75 col 'T (tokens)' |
| gemini-3.1-pro-high | Paxos | brownfield | salt-diet | none | b4ps03 | 16,590,636 | - | DEADLINE | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:76 col 'T (tokens)' |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | none | l5cp01 | 3,993,025 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:30 field 8 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | none | l5cp02 | 3,389,253 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:31 field 8 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | none | l5cp03 | 5,838,876 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:32 field 8 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | none | l5cs01 | 12,112,123 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:33 field 8 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | none | l5cs02 | 11,452,788 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:34 field 8 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | none | l5cs03 | 12,283,790 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:35 field 8 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | none | l5fp01 | 4,850,397 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:36 field 8 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | none | l5fp02 | 6,495,950 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:37 field 8 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | none | l5fp03 | 6,748,970 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:38 field 8 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | none | l5fs01 | 11,901,071 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:39 field 8 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | none | l5fs02 | 57,655,873 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:40 field 8 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | none | l5fs03 | 24,187,669 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:41 field 8 |
| gemini-3.8-flash-high | LRU | greenfield | plain | none | l5lp01 | 6,709,167 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:42 field 8 |
| gemini-3.8-flash-high | LRU | greenfield | plain | none | l5lp02 | 5,413,078 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:43 field 8 |
| gemini-3.8-flash-high | LRU | greenfield | plain | none | l5lp03 | 3,390,887 | - | - | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:44 field 8 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | l5lsra301 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | l5lsra302 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | l5lsra303 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | l5ppr01 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | l5ppr02 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | l5ppr03 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | l5psra201 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | l5psra202 | unmeasured | - | DEADLINE | no tracked source |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | l5psra203 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | l5cq01 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | l5cq02 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | l5cq03 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | l5ct01 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | l5ct02 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | l5ct03 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | l5fq01 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | l5fq02 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | l5fq03 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | l5ft01 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | l5ft02 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | l5ft03 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | l5lq01 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | l5lq02 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | l5lq03 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | l5lt01 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | l5lt02 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | l5lt03 | unmeasured | - | - | no tracked source |
| gemini-3.1-pro-high | LZW | greenfield | plain | none | l6vgpp01 | 1,311,863 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:119 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | plain | none | l6vgpp02 | 1,091,399 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:120 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | plain | none | l6vgpp03 | 1,232,089 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:121 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | none | l6vgps01 | 4,905,540 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:136 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | none | l6vgps02 | 16,759,665 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:137 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | none | l6vgps03 | 12,471,112 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:138 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | plain | statement | l6uspq01 | 1,000,293 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:109 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | plain | statement | l6vspb01 | 1,601,334 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:125 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | plain | statement | l6vspb02 | 1,598,032 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:126 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | statement | l6vspt01 | 17,892,929 | - | DEADLINE | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:142 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | statement | l6vspt02 | 7,705,397 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:143 field 5 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | statement | l6vspt03 | 18,778,063 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:144 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | plain | none | l6vgfp01 | 4,571,225 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:116 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | plain | none | l6vgfp02 | 4,244,069 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:117 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | plain | none | l6vgfp03 | 4,005,007 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:118 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | none | l6vgfs01 | 23,941,795 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:133 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | none | l6vgfs02 | 172,717 | - | DEADLINE | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:134 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | none | l6vgfs03 | 35,553,998 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:135 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | plain | statement | l6vsfq01 | 5,147,496 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:122 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | plain | statement | l6vsfq02 | 4,980,956 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:123 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | plain | statement | l6vsfq03 | 5,844,965 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:124 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | statement | l6vsft01 | 13,941,899 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:139 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | statement | l6vsft02 | 25,643,973 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:140 field 5 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | statement | l6vsft03 | 18,215,862 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:141 field 5 |
| gemini-3.8-flash-high | LRU | brownfield | plain | none | l6vblp01 | 3,971,258 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:110 field 5 |
| gemini-3.8-flash-high | LRU | brownfield | plain | none | l6vblp02 | 3,292,285 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:111 field 5 |
| gemini-3.8-flash-high | LRU | brownfield | plain | none | l6vblp03 | 3,804,355 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:112 field 5 |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | none | l6vbls01 | 15,083,897 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:127 field 5 |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | none | l6vbls02 | 14,937,746 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:128 field 5 |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | none | l6vbls03 | 13,783,042 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:129 field 5 |
| gemini-3.8-flash-high | Paxos | brownfield | plain | none | l6vbpp01 | 7,992,405 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:113 field 5 |
| gemini-3.8-flash-high | Paxos | brownfield | plain | none | l6vbpp02 | 8,133,242 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:114 field 5 |
| gemini-3.8-flash-high | Paxos | brownfield | plain | none | l6vbpp03 | 6,177,131 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:115 field 5 |
| gemini-3.8-flash-high | Paxos | brownfield | salt-diet | none | l6vbps01 | 14,891,518 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:130 field 5 |
| gemini-3.8-flash-high | Paxos | brownfield | salt-diet | none | l6vbps02 | 18,713,325 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:131 field 5 |
| gemini-3.8-flash-high | Paxos | brownfield | salt-diet | none | l6vbps03 | 24,560,143 | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:132 field 5 |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | none | l7cfbp01 | 4,399,236 | 37,981 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cfbp01].T |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | none | l7cfbp02 | 4,325,246 | 39,336 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cfbp02].T |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | none | l7cfbp03 | 4,188,400 | 42,743 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cfbp03].T |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | none | l7cfbs01 | 8,580,379 | 57,362 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cfbs01].T |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | none | l7cfbs02 | 9,683,589 | 65,511 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cfbs02].T |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | none | l7cfbs03 | 13,871,972 | 99,176 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cfbs03].T |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | statement | l7cfsp01 | 4,626,795 | 42,034 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cfsp01].T |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | statement | l7cfsp02 | 5,376,845 | 37,259 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cfsp02].T |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | statement | l7cfsp03 | 5,593,966 | 47,322 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cfsp03].T |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | statement | l7cfss01 | 13,141,849 | 89,524 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cfss01].T |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | statement | l7cfssq01 | 15,862,634 | 104,595 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-q2-cells.tsv [cell=l7cfssq01].T |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | statement | l7cfssq02 | 10,546,546 | 81,086 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-q2-cells.tsv [cell=l7cfssq02].T |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | none | l7cpbp01 | 1,125,906 | 12,855 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpbp01].T |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | none | l7cpbp02 | 1,312,489 | 15,705 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpbp02].T |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | none | l7cpbp03 | 722,895 | 10,822 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpbp03].T |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | l7cpbs01 | 11,391,627 | 68,719 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpbs01].T |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | l7cpbs02 | 7,486,137 | 45,094 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpbs02].T |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | l7cpbs03 | 9,956,601 | 71,162 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpbs03].T |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | statement | l7cpsp01 | 1,594,122 | 12,036 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpsp01].T |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | statement | l7cpsp02 | 994,856 | 10,817 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpsp02].T |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | statement | l7cpsp03 | 1,550,082 | 24,010 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpsp03].T |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | statement | l7cpssa201 | 7,893,713 | 62,805 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpssa201].T |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | statement | l7cpssa202 | 9,538,114 | 99,975 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpssa202].T |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | statement | l7cpssa203 | 2,619,898 | 24,601 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7cpssa203].T |
| gemini-3.8-flash-high | FreeList | brownfield | plain | none | l7nffp01 | 6,360,553 | 83,670 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nffp01].T |
| gemini-3.8-flash-high | FreeList | brownfield | plain | none | l7nffp02 | 4,649,180 | 74,143 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nffp02].T |
| gemini-3.8-flash-high | FreeList | brownfield | plain | none | l7nffp03 | 5,334,389 | 75,139 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nffp03].T |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | none | l7nffs01 | 22,734,954 | 181,904 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nffs01].T |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | none | l7nffs02 | 21,228,941 | 181,281 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nffs02].T |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | none | l7nffs03 | 17,804,823 | 107,729 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nffs03].T |
| gemini-3.8-flash-high | LZW | brownfield | plain | none | l7nfzp01 | 6,261,170 | 64,638 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nfzp01].T |
| gemini-3.8-flash-high | LZW | brownfield | plain | none | l7nfzp02 | 6,555,430 | 71,028 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nfzp02].T |
| gemini-3.8-flash-high | LZW | brownfield | plain | none | l7nfzp03 | 6,776,813 | 67,540 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nfzp03].T |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | none | l7nfzs01 | 18,064,205 | 134,557 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nfzs01].T |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | none | l7nfzs02 | 16,854,859 | 121,149 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nfzs02].T |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | none | l7nfzs03 | 17,493,691 | 113,937 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7nfzs03].T |
| gemini-3.1-pro-high | FreeList | brownfield | plain | none | l7npfp01 | 1,242,018 | 22,449 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npfp01].T |
| gemini-3.1-pro-high | FreeList | brownfield | plain | none | l7npfp02 | 2,596,533 | 40,232 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npfp02].T |
| gemini-3.1-pro-high | FreeList | brownfield | plain | none | l7npfp03 | 1,949,814 | 26,378 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npfp03].T |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | none | l7npfs01 | 15,150,465 | 107,906 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npfs01].T |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | none | l7npfs02 | 12,404,449 | 94,728 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npfs02].T |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | none | l7npfs03 | 16,239,561 | 115,589 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npfs03].T |
| gemini-3.1-pro-high | LZW | brownfield | plain | none | l7npzp01 | 1,523,409 | 17,376 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npzp01].T |
| gemini-3.1-pro-high | LZW | brownfield | plain | none | l7npzp02 | 1,252,000 | 14,570 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npzp02].T |
| gemini-3.1-pro-high | LZW | brownfield | plain | none | l7npzp03 | 2,097,518 | 17,675 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npzp03].T |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | none | l7npzs01 | 23,050,944 | 107,186 | DEADLINE | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npzs01].T |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | none | l7npzs02 | 26,462,763 | 232,294 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npzs02].T |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | none | l7npzs03 | 63,868,087 | 211,494 | DEADLINE | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7npzs03].T |
| gemini-3.8-flash-high | FreeList | brownfield | plain | statement | l7sffp01 | 6,354,773 | 67,685 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sffp01].T |
| gemini-3.8-flash-high | FreeList | brownfield | plain | statement | l7sffp02 | 7,756,505 | 92,762 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sffp02].T |
| gemini-3.8-flash-high | FreeList | brownfield | plain | statement | l7sffp03 | 8,522,338 | 84,825 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sffp03].T |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | statement | l7sffs01 | 34,073,898 | 218,141 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sffs01].T |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | statement | l7sffs02 | 13,351,194 | 95,483 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sffs02].T |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | statement | l7sffs03 | 20,084,774 | 126,201 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sffs03].T |
| gemini-3.8-flash-high | LRU | brownfield | plain | statement | l7sfrp01 | 4,705,974 | 45,024 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfrp01].T |
| gemini-3.8-flash-high | LRU | brownfield | plain | statement | l7sfrp02 | 3,676,567 | 44,829 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfrp02].T |
| gemini-3.8-flash-high | LRU | brownfield | plain | statement | l7sfrp03 | 4,034,404 | 58,991 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfrp03].T |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | statement | l7sfrs01 | 11,378,956 | 92,196 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfrs01].T |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | statement | l7sfrs02 | 26,417,079 | 125,981 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfrs02].T |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | statement | l7sfrs03 | 16,299,438 | 133,012 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfrs03].T |
| gemini-3.8-flash-high | LZW | brownfield | plain | statement | l7sfzp01 | 6,616,783 | 73,506 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfzp01].T |
| gemini-3.8-flash-high | LZW | brownfield | plain | statement | l7sfzp02 | 5,536,955 | 55,895 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfzp02].T |
| gemini-3.8-flash-high | LZW | brownfield | plain | statement | l7sfzp03 | 5,919,649 | 54,963 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfzp03].T |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | statement | l7sfzs01 | 13,256,712 | 100,662 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfzs01].T |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | statement | l7sfzs02 | 19,555,122 | 165,682 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfzs02].T |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | statement | l7sfzs03 | 12,230,282 | 93,661 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sfzs03].T |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | statement | l7spfb01 | 8,246,368 | 71,265 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spfb01].T |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | statement | l7spfb02 | 29,441,260 | 172,190 | DEADLINE | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spfb02].T |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | statement | l7spfwa201 | 14,174,074 | 57,347 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spfwa201].T |
| gemini-3.1-pro-high | FreeList | brownfield | plain | statement | l7spfp01 | 1,184,720 | 14,474 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spfp01].T |
| gemini-3.1-pro-high | FreeList | brownfield | plain | statement | l7spfp02 | 1,822,259 | 20,171 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spfp02].T |
| gemini-3.1-pro-high | FreeList | brownfield | plain | statement | l7spfp03 | 2,782,794 | 27,598 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spfp03].T |
| gemini-3.1-pro-high | LRU | brownfield | plain | statement | l7sprp01 | 1,355,238 | 20,042 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sprp01].T |
| gemini-3.1-pro-high | LRU | brownfield | plain | statement | l7sprp02 | 1,075,322 | 13,811 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sprp02].T |
| gemini-3.1-pro-high | LRU | brownfield | plain | statement | l7sprp03 | 1,704,567 | 15,062 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sprp03].T |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | statement | l7sprs01 | 12,346,374 | 72,997 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sprs01].T |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | statement | l7sprs02 | 13,573,895 | 68,655 | DEADLINE | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sprs02].T |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | statement | l7sprs03 | 28,284,577 | 104,126 | DEADLINE | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7sprs03].T |
| gemini-3.1-pro-high | LZW | brownfield | plain | statement | l7spzp01 | 1,468,162 | 16,180 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spzp01].T |
| gemini-3.1-pro-high | LZW | brownfield | plain | statement | l7spzp02 | 1,314,076 | 19,806 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spzp02].T |
| gemini-3.1-pro-high | LZW | brownfield | plain | statement | l7spzp03 | 1,675,129 | 14,172 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spzp03].T |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | statement | l7spzs01 | 18,030,505 | 129,851 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spzs01].T |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | statement | l7spzs02 | 10,072,157 | 106,629 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spzs02].T |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | statement | l7spzs03 | 19,782,278 | 98,747 | DEADLINE | harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv [cell=l7spzs03].T |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | spec-change | l8cfps01 | 9,522,806 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfps01,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfps01,phase=2].T |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | spec-change | l8cfps02 | 8,827,684 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfps02,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfps02,phase=2].T |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | spec-change | l8cfps03 | 7,397,222 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfps03,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfps03,phase=2].T |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | spec-change | l8cfss01 | 20,838,181 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfss01,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfss01,phase=2].T |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | spec-change | l8cfss02 | 20,087,009 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfss02,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfss02,phase=2].T |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | spec-change | l8cfss03 | 30,754,478 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfss03,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cfss03,phase=2].T |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | spec-change | l8cpps01 | 2,163,217 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cpps01,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cpps01,phase=2].T |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | spec-change | l8cpps02 | 2,552,272 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cpps02,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cpps02,phase=2].T |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | spec-change | l8cpps03 | 2,214,755 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cpps03,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cpps03,phase=2].T |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | l8cpss01 | unmeasured | - | - | no tracked source |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | l8cpss02 | 16,198,217 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cpss02,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8cpss02,phase=2].T |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | l8cpss03 | unmeasured | - | - | no tracked source |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | l8rfpb01 | 11,392,058 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rfpb01,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rfpb01,phase=2].T |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | l8rfpb02 | 9,343,447 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rfpb02,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rfpb02,phase=2].T |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | l8rfwra201 | 6,657,322 | - | - | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24.md:207 /phase 1: T ([0-9,]+)/ + harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24.md:207 /phase 2: T ([0-9,]+)/ |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | spec-change | l8rfss01 | 30,904,703 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rfss01,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rfss01,phase=2].T |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | spec-change | l8rfss02 | 26,295,576 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rfss02,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rfss02,phase=2].T |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | spec-change | l8rfss03 | 26,945,879 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rfss03,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rfss03,phase=2].T |
| gemini-3.1-pro-high | LRU | greenfield | plain | spec-change | l8rppr01 | 2,506,278 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rppr01,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rppr01,phase=2].T |
| gemini-3.1-pro-high | LRU | greenfield | plain | spec-change | l8rppr02 | 1,800,435 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rppr02,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rppr02,phase=2].T |
| gemini-3.1-pro-high | LRU | greenfield | plain | spec-change | l8rppr03 | 2,549,540 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rppr03,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rppr03,phase=2].T |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | spec-change | l8rpsra201 | 17,122,619 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rpsra201,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rpsra201,phase=2].T |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | spec-change | l8rpsra202 | 14,309,400 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rpsra202,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rpsra202,phase=2].T |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | spec-change | l8rpsra203 | 14,216,370 | - | - | evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rpsra203,phase=1].T + evidence/l8-chainD-2026-09-24/phase_facts.json [id=l8rpsra203,phase=2].T |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | l8xppr01 | 2,986,585 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xppr01,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xppr01,phase=2].T |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | l8xppr02 | 2,939,143 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xppr02,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xppr02,phase=2].T |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | l8xppr03 | 3,340,448 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xppr03,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xppr03,phase=2].T |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | l8xpsr01 | 11,717,035 | - | DEADLINE | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xpsr01,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xpsr01,phase=2].T |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | l8xpsr02 | 16,149,668 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xpsr02,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xpsr02,phase=2].T |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | l8xpsr03 | 20,827,763 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xpsr03,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xpsr03,phase=2].T |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | l8ffpr01 | 14,483,819 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffpr01,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffpr01,phase=2].T |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | l8ffpr02 | 14,103,453 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffpr02,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffpr02,phase=2].T |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | l8ffpr03 | 12,204,118 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffpr03,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffpr03,phase=2].T |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | l8ffsra201 | 58,463,610 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffsra201,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffsra201,phase=2].T |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | l8ffsra202 | 28,025,848 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffsra202,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffsra202,phase=2].T |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | l8ffsra203 | 32,423,306 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffsra203,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8ffsra203,phase=2].T |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | l8fppr01 | 4,154,307 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fppr01,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fppr01,phase=2].T |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | l8fppr02 | 3,357,987 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fppr02,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fppr02,phase=2].T |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | l8fppr03 | 2,992,320 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fppr03,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fppr03,phase=2].T |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr01 | 13,152,361 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fpsr01,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fpsr01,phase=2].T |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr02 | 36,382,801 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fpsr02,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fpsr02,phase=2].T |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr03 | 19,724,118 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fpsr03,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8fpsr03,phase=2].T |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | l8zfpra201 | 9,189,665 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfpra201,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfpra201,phase=2].T |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | l8zfpra202 | 8,618,366 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfpra202,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfpra202,phase=2].T |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | l8zfpra203 | 14,621,600 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfpra203,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfpra203,phase=2].T |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | l8zfsr01 | 38,543,805 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfsr01,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfsr01,phase=2].T |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | l8zfsr02 | 33,971,188 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfsr02,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfsr02,phase=2].T |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | l8zfsr03 | 36,488,484 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfsr03,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zfsr03,phase=2].T |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | l8zppr01 | 2,550,452 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zppr01,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zppr01,phase=2].T |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | l8zppr02 | 2,828,970 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zppr02,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zppr02,phase=2].T |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | l8zppr03 | 3,115,631 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zppr03,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zppr03,phase=2].T |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | l8zpsr01 | 36,025,851 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zpsr01,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zpsr01,phase=2].T |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | l8zpsr02 | 12,992,361 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zpsr02,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zpsr02,phase=2].T |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | l8zpsr03 | 26,732,286 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zpsr03,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8zpsr03,phase=2].T |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | l8xfp2a201 | 13,889,277 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfp2a201,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfp2a201,phase=2].T |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | l8xfp2a202 | 15,868,524 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfp2a202,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfp2a202,phase=2].T |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | l8xfp2a203 | 12,539,128 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfp2a203,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfp2a203,phase=2].T |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | l8xfs201 | 122,524,014 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfs201,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfs201,phase=2].T |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | l8xfs202 | 110,815,793 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfs202,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfs202,phase=2].T |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | l8xfs203 | 166,780,196 | - | - | evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfs203,phase=1].T + evidence/l8-chainF-2026-09-24/phase_facts.json [id=l8xfs203,phase=2].T |
