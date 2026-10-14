# O57 (b): THE DESCRIPTIVE TABLES, OLD (result of record) vs NEW (re-metered with sub-agent T). Every changed row; no Claude row changes.
## OLD = `RESULT-descriptive-tables-v2-2026-09-27.md` (reproduced byte for byte by the tool without `--add-T`) · NEW = `RESULT-descriptive-tables-v2-O57-remeter-2026-10-13.md`.
Reading: every Gemini change raises the salt-diet arm or bounds a cell. Ratios go UP, so the published salt-diet ÷ plain ratios understated the salt-diet arm's cost.
`bounds only (x)`: both arms of the ratio are floors (the 60 level-8 cells whose phase-1 conversation left no record), so no ratio is printed; x is the ratio of the floors.

## T1 greenfield, median total tokens
| | model | problem | bare-plain | bare-salt-diet | statement-plain | statement-salt-diet |
|---|---|---|---|---|---|---|
| OLD  gemini-3.1-pro-high | Crc32 | 861,120 | 9,675,734 | 1,222,527 | ≥ 17,220,747 |
| **NEW**  gemini-3.1-pro-high | Crc32 | 861,120 | 9,675,734 | 1,222,527 | ≥ 17,700,944 |
| OLD  gemini-3.1-pro-high | LRU | 1,466,321 | 9,543,326 | 1,080,062 | 10,360,342 |
| **NEW**  gemini-3.1-pro-high | LRU | 1,466,321 | 11,728,188 | 1,080,062 | 11,097,896 |
| OLD  gemini-3.1-pro-high | FreeList | 1,290,763 | 10,498,033 | 1,699,106 | ≥ 12,610,137 |
| **NEW**  gemini-3.1-pro-high | FreeList | 1,290,763 | 18,111,487 | 1,699,106 | ≥ 30,037,849 |
| OLD  gemini-3.1-pro-high | LZW | 1,232,089 | 12,471,112 | 1,598,032 | ≥ 17,892,929 |
| **NEW**  gemini-3.1-pro-high | LZW | 1,232,089 | 16,675,231 | 1,598,032 | 23,814,589 |
| OLD  gemini-3.1-pro-high | Paxos | 1,176,979 | ≥ 14,987,158 | — | — |
| **NEW**  gemini-3.1-pro-high | Paxos | 1,176,979 | ≥ 19,688,273 | — | — |

## T2 brownfield
| | model | problem | bare-plain | bare-salt-diet | statement-plain | statement-salt-diet |
|---|---|---|---|---|---|---|
| OLD  gemini-3.1-pro-high | Crc32 | 1,125,906 | 9,956,601 | 1,550,082 | 7,893,713 |
| **NEW**  gemini-3.1-pro-high | Crc32 | 1,125,906 | 10,407,416 | 1,550,082 | 8,796,037 |
| OLD  gemini-3.1-pro-high | LRU | 938,991 | 4,709,417 | 1,355,238 | ≥ 13,573,895 |
| **NEW**  gemini-3.1-pro-high | LRU | 938,991 | 8,687,059 | 1,355,238 | ≥ 16,581,493 |
| OLD  gemini-3.1-pro-high | FreeList | 1,949,814 | 15,150,465 | 1,822,259 | 14,174,074 |
| **NEW**  gemini-3.1-pro-high | FreeList | 1,949,814 | 17,298,225 | 1,822,259 | 34,282,120 |
| OLD  gemini-3.1-pro-high | LZW | 1,523,409 | ≥ 26,462,763 | 1,468,162 | 18,030,505 |
| **NEW**  gemini-3.1-pro-high | LZW | 1,523,409 | ≥ 35,151,779 | 1,468,162 | ≥ 30,795,640 |
| OLD  gemini-3.1-pro-high | Paxos | 1,676,061 | 13,771,122 | — | — |
| **NEW**  gemini-3.1-pro-high | Paxos | 1,676,061 | 17,401,238 | — | — |
| OLD  gemini-3.8-flash-high | LRU | 3,804,355 | 14,937,746 | 4,034,404 | 16,299,438 |
| **NEW**  gemini-3.8-flash-high | LRU | 3,804,355 | 14,937,746 | 4,034,404 | 17,138,719 |
| OLD  gemini-3.8-flash-high | LZW | 6,555,430 | 17,493,691 | 5,919,649 | 13,256,712 |
| **NEW**  gemini-3.8-flash-high | LZW | 6,555,430 | 18,064,205 | 5,919,649 | 13,256,712 |

## T3 spec-change
| | model | problem | plain | salt-diet |
|---|---|---|---|---|
| OLD  gemini-3.1-pro-high | Crc32 | 2,214,755 | unmeasured |
| **NEW**  gemini-3.1-pro-high | Crc32 | ≥ 2,214,755 | unmeasured |
| OLD  gemini-3.1-pro-high | LRU | 2,506,278 | 14,309,400 |
| **NEW**  gemini-3.1-pro-high | LRU | ≥ 2,506,278 | ≥ 15,320,783 |
| OLD  gemini-3.1-pro-high | FreeList | 3,357,987 | 19,724,118 |
| **NEW**  gemini-3.1-pro-high | FreeList | ≥ 3,357,987 | ≥ 19,724,118 |
| OLD  gemini-3.1-pro-high | LZW | 2,828,970 | 26,732,286 |
| **NEW**  gemini-3.1-pro-high | LZW | ≥ 2,828,970 | ≥ 33,881,993 |
| OLD  gemini-3.1-pro-high | Paxos | 2,986,585 | ≥ 16,149,668 |
| **NEW**  gemini-3.1-pro-high | Paxos | ≥ 2,986,585 | ≥ 20,827,763 |
| OLD  gemini-3.8-flash-high | Crc32 | 8,827,684 | 20,838,181 |
| **NEW**  gemini-3.8-flash-high | Crc32 | ≥ 8,827,684 | ≥ 20,838,181 |
| OLD  gemini-3.8-flash-high | LRU | 9,343,447 | 26,945,879 |
| **NEW**  gemini-3.8-flash-high | LRU | ≥ 9,343,447 | ≥ 26,945,879 |
| OLD  gemini-3.8-flash-high | FreeList | 14,103,453 | 32,423,306 |
| **NEW**  gemini-3.8-flash-high | FreeList | ≥ 14,103,453 | ≥ 32,423,306 |
| OLD  gemini-3.8-flash-high | LZW | 9,189,665 | 36,488,484 |
| **NEW**  gemini-3.8-flash-high | LZW | ≥ 9,189,665 | ≥ 36,488,484 |
| OLD  gemini-3.8-flash-high | Paxos | 13,889,277 | 122,524,014 |
| **NEW**  gemini-3.8-flash-high | Paxos | ≥ 13,889,277 | ≥ 127,713,529 |

## T4 salt-diet ÷ plain, and its sign counts
| | model | problem | bare | statement | spec-change |
|---|---|---|---|---|---|
| OLD  gemini-3.1-pro-high | Crc32 | 11.24 | ≥ 14.09 | — |
| **NEW**  gemini-3.1-pro-high | Crc32 | 11.24 | ≥ 14.48 | — |
| OLD  gemini-3.1-pro-high | LRU | 6.51 | 9.59 | 5.71 |
| **NEW**  gemini-3.1-pro-high | LRU | 8.00 | 10.28 | bounds only (6.11) |
| OLD  gemini-3.1-pro-high | FreeList | 8.13 | ≥ 7.42 | 5.87 |
| **NEW**  gemini-3.1-pro-high | FreeList | 14.03 | ≥ 17.68 | bounds only (5.87) |
| OLD  gemini-3.1-pro-high | LZW | 10.12 | ≥ 11.20 | 9.45 |
| **NEW**  gemini-3.1-pro-high | LZW | 13.53 | 14.90 | bounds only (11.98) |
| OLD  gemini-3.1-pro-high | Paxos | ≥ 12.73 | — | ≥ 5.41 |
| **NEW**  gemini-3.1-pro-high | Paxos | ≥ 16.73 | — | bounds only (6.97) |
| OLD  gemini-3.8-flash-high | Crc32 | 3.03 | — | 2.36 |
| **NEW**  gemini-3.8-flash-high | Crc32 | 3.03 | — | bounds only (2.36) |
| OLD  gemini-3.8-flash-high | LRU | — | — | 2.88 |
| **NEW**  gemini-3.8-flash-high | LRU | — | — | bounds only (2.88) |
| OLD  gemini-3.8-flash-high | FreeList | 3.72 | — | 2.30 |
| **NEW**  gemini-3.8-flash-high | FreeList | 3.72 | — | bounds only (2.30) |
| OLD  gemini-3.8-flash-high | LZW | ≥ 5.64 | 3.54 | 3.97 |
| **NEW**  gemini-3.8-flash-high | LZW | ≥ 5.64 | 3.54 | bounds only (3.97) |
| OLD  gemini-3.8-flash-high | Paxos | — | — | 8.82 |
| **NEW**  gemini-3.8-flash-high | Paxos | — | — | bounds only (9.20) |
| OLD  gemini-3.1-pro-high | bare | 5 of 5 | none | 10.12 | 1 |
| **NEW**  gemini-3.1-pro-high | bare | 5 of 5 | none | 13.53 | 1 |
| OLD  gemini-3.1-pro-high | statement | 4 of 4 | none | 10.39 | 3 |
| **NEW**  gemini-3.1-pro-high | statement | 4 of 4 | none | 14.69 | 2 |
| OLD  gemini-3.1-pro-high | spec-change | 4 of 4 | none | 5.79 | 1 |
| **NEW**  gemini-3.1-pro-high | spec-change | 0 of 0 | LRU, FreeList, LZW, Paxos | 6.54 | 4 |
| OLD  gemini-3.8-flash-high | spec-change | 5 of 5 | none | 2.88 | 0 |
| **NEW**  gemini-3.8-flash-high | spec-change | 0 of 0 | Crc32, LRU, FreeList, LZW, Paxos | 2.88 | 5 |
| OLD  gemini-3.1-pro-high | Crc32 | 8.84 | 5.09 |
| **NEW**  gemini-3.1-pro-high | Crc32 | 9.24 | 5.67 |
| OLD  gemini-3.1-pro-high | LRU | 5.02 | ≥ 10.02 |
| **NEW**  gemini-3.1-pro-high | LRU | 9.25 | ≥ 12.24 |
| OLD  gemini-3.1-pro-high | FreeList | 7.77 | 7.78 |
| **NEW**  gemini-3.1-pro-high | FreeList | 8.87 | 18.81 |
| OLD  gemini-3.1-pro-high | LZW | ≥ 17.37 | 12.28 |
| **NEW**  gemini-3.1-pro-high | LZW | ≥ 23.07 | ≥ 20.98 |
| OLD  gemini-3.1-pro-high | Paxos | 8.22 | — |
| **NEW**  gemini-3.1-pro-high | Paxos | 10.38 | — |
| OLD  gemini-3.8-flash-high | LRU | 3.93 | 4.04 |
| **NEW**  gemini-3.8-flash-high | LRU | 3.93 | 4.25 |
| OLD  gemini-3.8-flash-high | LZW | 2.67 | 2.24 |
| **NEW**  gemini-3.8-flash-high | LZW | 2.76 | 2.24 |
