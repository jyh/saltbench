# HG A + B — READING against the registration

Registration: `AMENDMENT-HG-AB-registration-2026-09-26.md`, last commit touching it `d7ef5bdf0b647331b7a22a861a8accbbbccbcaf5 2026-09-26T07:01:02-07:00`. Every number below is printed by `hg_scan.py read` from the per-cell scanner JSONs (A) and from TABLE 2's recorded locations (B).

Scan output written 2026-09-26T14:08:47Z → 2026-09-26T14:08:49Z (the registration commit must precede it).

## POPULATION — registered vs scanned

- TABLE 1 rows: 580 (grid 535 cells in 181 conditions; HC1 45 cells). Registered: 535 grid cells in 181 conditions + 45 HC1.
- NF (no LANDING.md) per TABLE 1: grid 22 · HC1 2. Registered: 22 · 2.
- Texts fetched: 580 of 580; scanned: 580 of 580; not scanned: 0.
- Manifest rows with a status other than OK: 0
- NF cell directories derived under C9: 24
  - `O_FreeList_g_salt-diet_none__161b5a34` → `cells-matrix1/161b5a34` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 944 B)
  - `O_FreeList_b_salt-diet_none__clbofs02` → `cells-clb-o-freelist-saltdiet/clbofs02` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 148 B)
  - `S_FreeList_b_salt-diet_none__clbbfs01` → `cells-clb-sb-freelist-saltdiet/clbbfs01` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 1058 B)
  - `S_FreeList_b_salt-diet_none__clbbfs03` → `cells-clb-sb-freelist-saltdiet/clbbfs03` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 470 B)
  - `S_Paxos_b_salt-diet_none__clbbps01` → `cells-clb-sb-paxos-saltdiet/clbbps01` (opposite-arm root, -plain -> -saltdiet; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `S_Paxos_b_salt-diet_none__clbbps02` → `cells-clb-sb-paxos-saltdiet/clbbps02` (opposite-arm root, -plain -> -saltdiet; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `S_Paxos_b_salt-diet_none__clbbps03` → `cells-clb-sb-paxos-saltdiet/clbbps03` (opposite-arm root, -plain -> -saltdiet; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 184 B)
  - `S_FreeList_g_salt-diet_none__clbgfs01` → `cells-clb-sg-freelist-saltdiet/clbgfs01` (opposite-arm root, -plain -> -saltdiet; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `S_FreeList_g_salt-diet_none__clbgfs02` → `cells-clb-sg-freelist-saltdiet/clbgfs02` (opposite-arm root, -plain -> -saltdiet; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 54 B)
  - `S_FreeList_g_salt-diet_none__clbgfs03` → `cells-clb-sg-freelist-saltdiet/clbgfs03` (opposite-arm root, -plain -> -saltdiet; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `S_Paxos_g_salt-diet_none__clbgps01` → `cells-clb-sg-paxos-saltdiet/clbgps01` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `S_Paxos_g_salt-diet_none__clbgps02` → `cells-clb-sg-paxos-saltdiet/clbgps02` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 54 B)
  - `S_FreeList_g_salt-diet_stmt__clbsfs02` → `cells-clb-ss-freelist-saltdiet/clbsfs02` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 282 B)
  - `S_LZW_g_salt-diet_stmt__clbszs02` → `cells-clb-ss-lzw-saltdiet/clbszs02` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `S_FreeList_b_salt-diet_stmt__clbufs01` → `cells-clb-sbs-freelist-saltdiet/clbufs01` (opposite-arm root, -plain -> -saltdiet; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 1155 B)
  - `S_FreeList_b_salt-diet_stmt__clbufs02` → `cells-clb-sbs-freelist-saltdiet/clbufs02` (opposite-arm root, -plain -> -saltdiet; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 251 B)
  - `S_FreeList_b_salt-diet_stmt__clbufs03` → `cells-clb-sbs-freelist-saltdiet/clbufs03` (opposite-arm root, -plain -> -saltdiet; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `P_Paxos_g_salt-diet_none__s3ps02` → `cells-s3-paxos-saltdiet/s3ps02` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `P_Paxos_g_salt-diet_none__s3ps03` → `cells-s3-paxos-saltdiet/s3ps03` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `P_FreeList_g_salt-diet_stmt__s3ft02` → `cells-s3-freelist-saltdiet-stmt/s3ft02` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `P_FreeList_g_salt-diet_stmt__s3ft03` → `cells-s3-freelist-saltdiet-stmt/s3ft03` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 33 B)
  - `F_LZW_g_salt-diet_none__l6vgfs02` → `cells-l6v-lzw-flash-salt-bare/l6vgfs02` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 12 B)
  - `O_FreeList_g_salt-diet_none__hc1fs02` → `cells-hc1-freelist-saltdiet/hc1fs02` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 1073 B)
  - `O_Paxos_g_salt-diet_none__hc1ps01` → `cells-hc1-paxos-saltdiet/hc1ps01` (sibling root; LANDING.md cat rc 1, BUS.md cat rc 0, BUS.md 2631 B)
- Scanner failures: 0
- Detect-hit lines stored at the scanner's 120-character truncation (C3): 1046
- (cell, id) pairs where JSON-alone ASKED and full-line ASKED differ: 0

## §HG5 — printed beside every reading (verbatim from the registration)

## §HG5 · WHAT IS PRINTED BESIDE EVERY A/B READING
- **A reads TEXT, not behaviour**: SILENT is a floor on noticing, never proof of not noticing.
- **Both arms receive the same `LANDING.md` template and its `## DECISIONS` section.** The arm texts mention "decision" plain 4 ·
  salt-diet 4 · placebo 9, and "ambiguity" plain 1 · salt-diet 0 · placebo 1 (v3 `render/` at e54f35a).
- **B covers only the problems with a `B/` tree**, and is not blind (§HG2).
- **The detect patterns are cues, not concepts** (the scanner's own docstring). Differences between arms are the reading; absolute rates
  are not.

## A — the two missingness readings side by side

### Reading (i) cells WITH a LANDING.md

| grid arm | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 272 | 816 | 369 (45.2 %) | 160 (19.6 %) | 3 (0.4 %) | 284 (34.8 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 241 | 723 | 251 (34.7 %) | 126 (17.4 %) | 2 (0.3 %) | 344 (47.6 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

| HC1 arm | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 15 | 45 | 32 (71.1 %) | 10 (22.2 %) | 2 (4.4 %) | 1 (2.2 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 13 | 39 | 27 (69.2 %) | 7 (17.9 %) | 0 (0.0 %) | 5 (12.8 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| placebo | 15 | 45 | 31 (68.9 %) | 10 (22.2 %) | 0 (0.0 %) | 4 (8.9 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

- **A1: FALSIFIED** — DOCUMENTED plain 45.2 % · salt-diet 34.7 %
- **A2: FALSIFIED** — SILENT plain 34.8 % · salt-diet 47.6 %
- **A3: HOLDS** — WRONG plain 0.4 % · salt-diet 0.3 % (threshold 10 %)
- **A4: HOLDS** — ASKED cells plain 0.0 % · salt-diet 0.0 % (threshold 5 %)
- **A5: FALSIFIED** — HC1 DOCUMENTED plain 71.1 % · placebo 68.9 % · salt-diet 69.2 %

### Reading (ii) ALL cells, BUS.md alone where LANDING.md is absent

| grid arm | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 272 | 816 | 369 (45.2 %) | 160 (19.6 %) | 3 (0.4 %) | 284 (34.8 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 263 | 789 | 251 (31.8 %) | 126 (16.0 %) | 2 (0.3 %) | 410 (52.0 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

| HC1 arm | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 15 | 45 | 32 (71.1 %) | 10 (22.2 %) | 2 (4.4 %) | 1 (2.2 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 15 | 45 | 27 (60.0 %) | 7 (15.6 %) | 0 (0.0 %) | 11 (24.4 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| placebo | 15 | 45 | 31 (68.9 %) | 10 (22.2 %) | 0 (0.0 %) | 4 (8.9 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

- **A1: FALSIFIED** — DOCUMENTED plain 45.2 % · salt-diet 31.8 %
- **A2: FALSIFIED** — SILENT plain 34.8 % · salt-diet 52.0 %
- **A3: HOLDS** — WRONG plain 0.4 % · salt-diet 0.3 % (threshold 10 %)
- **A4: HOLDS** — ASKED cells plain 0.0 % · salt-diet 0.0 % (threshold 5 %)
- **A5: FALSIFIED** — HC1 DOCUMENTED plain 71.1 % · placebo 68.9 % · salt-diet 60.0 %

### A verdicts, the two readings side by side

| prediction | reading (i) | reading (ii) |
|---|---|---|
| A1 | FALSIFIED — DOCUMENTED plain 45.2 % · salt-diet 34.7 % | FALSIFIED — DOCUMENTED plain 45.2 % · salt-diet 31.8 % |
| A2 | FALSIFIED — SILENT plain 34.8 % · salt-diet 47.6 % | FALSIFIED — SILENT plain 34.8 % · salt-diet 52.0 % |
| A3 | HOLDS — WRONG plain 0.4 % · salt-diet 0.3 % (threshold 10 %) | HOLDS — WRONG plain 0.4 % · salt-diet 0.3 % (threshold 10 %) |
| A4 | HOLDS — ASKED cells plain 0.0 % · salt-diet 0.0 % (threshold 5 %) | HOLDS — ASKED cells plain 0.0 % · salt-diet 0.0 % (threshold 5 %) |
| A5 | FALSIFIED — HC1 DOCUMENTED plain 71.1 % · placebo 68.9 % · salt-diet 69.2 % | FALSIFIED — HC1 DOCUMENTED plain 71.1 % · placebo 68.9 % · salt-diet 60.0 % |

### A sensitivities (declared, not predictions)

- C4, grid + HC1 plain/salt-diet, reading (i): A1 FALSIFIED (DOCUMENTED plain 46.6 % · salt-diet 36.5 %) · A2 FALSIFIED (SILENT plain 33.1 % · salt-diet 45.8 %) · A3 HOLDS (WRONG plain 0.6 % · salt-diet 0.3 % (threshold 10 %)) · A4 HOLDS (ASKED cells plain 0.0 % · salt-diet 0.0 % (threshold 5 %))
- C4, grid + HC1 plain/salt-diet, reading (ii): A1 FALSIFIED (DOCUMENTED plain 46.6 % · salt-diet 33.3 %) · A2 FALSIFIED (SILENT plain 33.1 % · salt-diet 50.5 %) · A3 HOLDS (WRONG plain 0.6 % · salt-diet 0.2 % (threshold 10 %)) · A4 HOLDS (ASKED cells plain 0.0 % · salt-diet 0.0 % (threshold 5 %))
- C3, A4 with full-line ASKED, reading (i): plain 0/272 = 0.0 % · salt-diet 0/241 = 0.0 %
- C3, A4 with full-line ASKED, reading (ii): plain 0/272 = 0.0 % · salt-diet 0/263 = 0.0 %
- C8, dropping LRU get_miss_effect from spec-change cells, reading (i): A1 FALSIFIED (DOCUMENTED plain 45.3 % · salt-diet 34.6 %) · A2 FALSIFIED (SILENT plain 34.7 % · salt-diet 48.0 %) · A3 HOLDS (WRONG plain 0.2 % · salt-diet 0.1 % (threshold 10 %))
- C8, dropping LRU get_miss_effect from spec-change cells, reading (ii): A1 FALSIFIED (DOCUMENTED plain 45.3 % · salt-diet 31.7 %) · A2 FALSIFIED (SILENT plain 34.7 % · salt-diet 52.4 %) · A3 HOLDS (WRONG plain 0.2 % · salt-diet 0.1 % (threshold 10 %))

### Descriptive only — per lane and per model (no predictions; reading (ii), all cells)

| lane claude | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 137 | 411 | 246 (59.9 %) | 92 (22.4 %) | 3 (0.7 %) | 70 (17.0 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 126 | 378 | 167 (44.2 %) | 85 (22.5 %) | 2 (0.5 %) | 124 (32.8 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

| lane agy | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 135 | 405 | 123 (30.4 %) | 68 (16.8 %) | 0 (0.0 %) | 214 (52.8 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 137 | 411 | 84 (20.4 %) | 41 (10.0 %) | 0 (0.0 %) | 286 (69.6 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

| lane claude-hc1 | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 15 | 45 | 32 (71.1 %) | 10 (22.2 %) | 2 (4.4 %) | 1 (2.2 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 15 | 45 | 27 (60.0 %) | 7 (15.6 %) | 0 (0.0 %) | 11 (24.4 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| placebo | 15 | 45 | 31 (68.9 %) | 10 (22.2 %) | 0 (0.0 %) | 4 (8.9 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

| grid model O | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 68 | 204 | 157 (77.0 %) | 36 (17.6 %) | 3 (1.5 %) | 8 (3.9 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 66 | 198 | 116 (58.6 %) | 59 (29.8 %) | 1 (0.5 %) | 22 (11.1 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

| grid model S | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 69 | 207 | 89 (43.0 %) | 56 (27.1 %) | 0 (0.0 %) | 62 (30.0 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 60 | 180 | 51 (28.3 %) | 26 (14.4 %) | 1 (0.6 %) | 102 (56.7 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

| grid model P | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 66 | 198 | 26 (13.1 %) | 25 (12.6 %) | 0 (0.0 %) | 147 (74.2 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 68 | 204 | 18 (8.8 %) | 11 (5.4 %) | 0 (0.0 %) | 175 (85.8 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

| grid model F | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |
|---|---|---|---|---|---|---|---|---|---|
| plain | 69 | 207 | 97 (46.9 %) | 43 (20.8 %) | 0 (0.0 %) | 67 (32.4 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |
| salt-diet | 69 | 207 | 66 (31.9 %) | 30 (14.5 %) | 0 (0.0 %) | 111 (53.6 %) | 0 | 0 (0.0 %) | 0 (0.0 %) |

Per planted id (grid, reading (ii)), counts of DOCUMENTED / NOTICED / WRONG / SILENT per arm:

| problem | id | plain D/N/W/S | salt-diet D/N/W/S |
|---|---|---|---|
| Crc32 | convention | 16/31/0/13 | 10/41/0/8 |
| Crc32 | empty_message | 29/6/0/25 | 27/0/0/32 |
| Crc32 | table_literal | 32/0/0/28 | 20/2/0/37 |
| FreeList | degenerate_requests | 37/0/0/20 | 12/0/0/43 |
| FreeList | free_nonlive | 38/0/0/19 | 18/0/0/37 |
| FreeList | min_remainder | 28/16/0/13 | 14/8/0/33 |
| LRU | capacity_zero | 24/21/0/15 | 36/4/0/20 |
| LRU | get_miss_effect | 11/27/3/19 | 19/14/2/25 |
| LRU | observer_out_of_range | 30/2/0/28 | 35/3/0/22 |
| LZW | code_sequence_pinned | 14/21/0/24 | 2/20/0/35 |
| LZW | empty_input | 9/19/0/31 | 5/16/0/36 |
| LZW | invalid_code | 40/0/0/19 | 38/0/0/19 |
| Paxos | accept_without_promise | 30/2/0/4 | 9/3/0/20 |
| Paxos | ballot_ownership | 20/11/0/5 | 4/9/0/19 |
| Paxos | proposed_meaning | 11/4/0/21 | 2/6/0/24 |

## B — change (analysis commitments, NOT blind: §HG2)

Inputs read with `git show d489eda93b4a213b5a5beca467c1caaa2e7587fa:<path>` (origin/main). Units: Opus and Sonnet in USD, agy (P, F) in tokens T; B1 never compares across units.

TABLE 2 expands to 104 (condition, cell) records in 37 distinct condition keys (registered in §HG3: 104 cells, 47 conditions). TABLE 1 carries 37 distinct spec-change condition keys.
TABLE 1 spec-change cells not in TABLE 2: [] · TABLE 2 cells not in TABLE 1: []

### B1 — cost-to-change = phase-2 ÷ phase-1 per cell; median per arm within model

| model | unit | plain n | plain median | salt-diet n | salt-diet median | salt-diet < plain? |
|---|---|---|---|---|---|---|
| O claude-opus-5 | USD | 11 | 1.530 | 12 | 0.823 | yes |
| S claude-sonnet-5 | USD | 15 | 0.980 | 6 | 0.526 | yes |
| P gemini-3.1-pro-high | T | 15 | 1.088 | 13 | 0.374 | yes |
| F gemini-3.8-flash-high | T | 15 | 1.368 | 15 | 0.611 | yes |

**B1: HOLDS** — salt-diet median ≥ plain median in 0 of 4 models with both arms (falsified if in a strict majority).

Sensitivity (declared, not the registered reading) — dropping every cell whose phase-1 or phase-2 cost is flagged as a floor (FLOOR, CAP-COST, capped):

- O: plain n 5 median 1.674 · salt-diet n 7 median 0.783 · dropped 11
- S: plain n 15 median 0.980 · salt-diet n 6 median 0.526 · dropped 0
- P: plain n 15 median 1.088 · salt-diet n 13 median 0.374 · dropped 0
- F: plain n 15 median 1.368 · salt-diet n 15 median 0.611 · dropped 0

Descriptive — the ratio's two terms, median per arm within model (same unit as the row); a ratio falls when phase 1 rises, so read B1 beside these:

| model | unit | plain p1 | plain p2 | salt-diet p1 | salt-diet p2 |
|---|---|---|---|---|---|
| O | USD | 9.49 | 13.68 | 16.91 | 13.70 |
| S | USD | 1.96 | 2.26 | 6.49 | 3.17 |
| P | T | 1,142,407 | 1,472,734 | 12,570,233 | 4,946,127 |
| F | T | 5,352,442 | 6,971,055 | 20,204,557 | 12,292,336 |

B1 missing ratios: 2 — l8cpss01 (phase-2 cost NOT IN REPO (missing)); l8cpss03 (phase-2 cost NOT IN REPO (missing))

Descriptive (C12) — problem-matched medians, only problems where the model has both arms:

| model | problem | plain n / median | salt-diet n / median |
|---|---|---|---|
| O | Crc32 | 3 / 2.201 | 3 / 1.270 |
| O | FreeList | 2 / 0.653 | 1 / 0.418 |
| O | LRU | 2 / 1.565 | 3 / 0.783 |
| O | LZW | 2 / 1.573 | 3 / 0.817 |
| O | Paxos | 2 / 1.354 | 2 / 0.663 |
| S | Crc32 | 3 / 0.862 | 3 / 0.589 |
| S | LRU | 3 / 1.113 | 3 / 0.404 |
| P | Crc32 | 3 / 1.726 | 1 / 0.289 |
| P | FreeList | 3 / 0.962 | 3 / 0.374 |
| P | LRU | 3 / 1.232 | 3 / 0.374 |
| P | LZW | 3 / 1.027 | 3 / 0.615 |
| P | Paxos | 3 / 1.068 | 3 / 0.471 |
| F | Crc32 | 3 / 0.894 | 3 / 0.674 |
| F | FreeList | 3 / 1.689 | 3 / 0.605 |
| F | LRU | 3 / 1.368 | 3 / 0.698 |
| F | LZW | 3 / 1.463 | 3 / 0.691 |
| F | Paxos | 3 / 1.263 | 3 / 0.223 |

### B2 — pooled REGRESSIONS pass share per arm, Sonnet + agy (C10: recorded f/t is FAILED of t)

| scope | arm | cells with a value | missing | Σ(t−f)/Σt | cells with f = 0 |
|---|---|---|---|---|---|
| POOLED S+P+F | plain | 45 | 0 | 472/477 = 99.0 % | 40/45 |
| POOLED S+P+F | salt-diet | 35 | 1 | 358/377 = 95.0 % | 30/35 |
| S | plain | 15 | 0 | 157/159 = 98.7 % | 13/15 |
| S | salt-diet | 6 | 0 | 66/66 = 100.0 % | 6/6 |
| P | plain | 15 | 0 | 157/159 = 98.7 % | 13/15 |
| P | salt-diet | 14 | 1 | 138/152 = 90.8 % | 12/14 |
| F | plain | 15 | 0 | 158/159 = 99.4 % | 14/15 |
| F | salt-diet | 15 | 0 | 154/159 = 96.9 % | 12/15 |

Descriptive (C12) — B2 on problem-matched cells only (model × problem with both arms valued):

| arm | cells | Σ(t−f)/Σt |
|---|---|---|
| plain | 36 | 381/384 = 99.2 % |
| salt-diet | 35 | 358/377 = 95.0 % |

**B2: FALSIFIED** — pooled pass share salt-diet 95.0 % vs plain 99.0 % (falsified if salt-diet is below).

Opus gap (§HG2): 23 Opus spec-change cells carry NO REGRESSIONS record (plain 11, salt-diet 12); B2 does not cover them.
B2 missing (Sonnet + agy): 1 — l8fpsr03 [ABSENT]

B lookup failures: 0

### B per-cell record

| condition | cell | unit | phase 1 | phase 2 | ratio | REGRESSIONS (f/t, src) | notes |
|---|---|---|---|---|---|---|---|
| O|Crc32|g|plain|sc | 2d0c65b3 | USD | 5.358154900000001 | 12.42 | 2.318 | None  | REGRESSIONS NOT RECORDED |
| O|Crc32|g|plain|sc | 746d7d4e | USD | 6.214880000000001 | 13.68 | 2.201 | None  | phase-1 FLOOR (a lower bound, so the ratio is an upper bound); REGRESSIONS NOT RECORDED |
| O|Crc32|g|plain|sc | a87b7740 | USD | 7.635044449999998 | 15.52 | 2.033 | None  | REGRESSIONS NOT RECORDED |
| O|Crc32|g|salt-diet|sc | 11165871 | USD | 6.194189599999999 | 10.29 | 1.661 | None  | phase-1 FLOOR (a lower bound, so the ratio is an upper bound); REGRESSIONS NOT RECORDED |
| O|Crc32|g|salt-diet|sc | 3e95075c | USD | 7.211073900000002 | 7.83 | 1.086 | None  | phase-1 FLOOR (a lower bound, so the ratio is an upper bound); REGRESSIONS NOT RECORDED |
| O|Crc32|g|salt-diet|sc | 57a33630 | USD | 7.6284383999999985 | 9.69 | 1.270 | None  | REGRESSIONS NOT RECORDED |
| O|FreeList|g|plain|sc | 188f422b | USD | 13.0171976 | 10.19 | 0.783 | None  | phase-1 FLOOR (a lower bound, so the ratio is an upper bound); REGRESSIONS NOT RECORDED |
| O|FreeList|g|plain|sc | 9cb8ce96 | USD | 23.379875499999997 | 12.24 | 0.524 | None  | REGRESSIONS NOT RECORDED |
| O|FreeList|g|salt-diet|sc | f33c7e65 | USD | 35.414077999999996 | 14.81 | 0.418 | None  | REGRESSIONS NOT RECORDED |
| O|LRU|g|plain|sc | 3bdcbcbd | USD | 7.7499179 | 13.36 | 1.724 | None  | phase-1 FLOOR (a lower bound, so the ratio is an upper bound); REGRESSIONS NOT RECORDED |
| O|LRU|g|plain|sc | 69e8c2c4 | USD | 9.730732500000002 | 13.69 | 1.407 | None  | phase-1 FLOOR (a lower bound, so the ratio is an upper bound); REGRESSIONS NOT RECORDED |
| O|LRU|g|salt-diet|sc | 011fe22f | USD | 11.188329799999996 | 12.58 | 1.124 | None  | REGRESSIONS NOT RECORDED |
| O|LRU|g|salt-diet|sc | b71994e3 | USD | 11.206316400000002 | 8.78 | 0.783 | None  | REGRESSIONS NOT RECORDED |
| O|LRU|g|salt-diet|sc | d6b53ee4 | USD | 14.632604600000008 | 7.7 | 0.526 | None  | REGRESSIONS NOT RECORDED |
| O|LZW|g|salt-diet|sc | 7ac56e4e | USD | 19.177816399999998 | 15.66 | 0.817 | None  | REGRESSIONS NOT RECORDED |
| O|LZW|g|salt-diet|sc | 18fb3eed | USD | 31.69753024999999 | 17.28 | 0.545 | None  | REGRESSIONS NOT RECORDED |
| O|LZW|g|salt-diet|sc | 6d58f1ec | USD | 22.53159649999999 | 18.71 | 0.830 | None  | phase-2 CAP-COST (censored; cost is a floor); REGRESSIONS NOT RECORDED |
| O|LZW|g|plain|sc | 93323249 | USD | 8.152814700000002 | 12.0 | 1.472 | None  | REGRESSIONS NOT RECORDED |
| O|LZW|g|plain|sc | 22ee7d33 | USD | 10.24462115 | 17.15 | 1.674 | None  | REGRESSIONS NOT RECORDED |
| O|Paxos|g|plain|sc | 60a056e6 | USD | 9.494318000000002 | 14.53 | 1.530 | None  | phase-1 FLOOR (a lower bound, so the ratio is an upper bound); REGRESSIONS NOT RECORDED |
| O|Paxos|g|plain|sc | f6462d47 | USD | 16.78305569999999 | 19.78 | 1.179 | None  | phase-1 FLOOR (a lower bound, so the ratio is an upper bound); phase-2 CAP-COST (censored; cost is a floor); REGRESSIONS NOT RECORDED |
| O|Paxos|g|salt-diet|sc | 9e6c8d4d | USD | 37.64788035000001 | 18.62 | 0.495 | None  | phase-2 CAP-COST (censored; cost is a floor); REGRESSIONS NOT RECORDED |
| O|Paxos|g|salt-diet|sc | b22d1000 | USD | 23.516636099999996 | 19.56 | 0.832 | None  | phase-2 CAP-COST (censored; cost is a floor); REGRESSIONS NOT RECORDED |
| S|Crc32|g|plain|sc | clbccp01 | USD | 0.78 | 1.71 | 2.192 | 0/6 blockSC-cells.tsv:9 col19 |  |
| S|Crc32|g|plain|sc | clbccp02 | USD | 1.09 | 0.94 | 0.862 | 0/6 blockSC-cells.tsv:10 col19 |  |
| S|Crc32|g|plain|sc | clbccp03 | USD | 1.03 | 0.83 | 0.806 | 0/6 blockSC-cells.tsv:11 col19 |  |
| S|Crc32|g|salt-diet|sc | clbccs01 | USD | 7.22 | 3.73 | 0.517 | 0/6 blockSC-cells.tsv:12 col19 |  |
| S|Crc32|g|salt-diet|sc | clbccs02 | USD | 5.76 | 3.39 | 0.589 | 0/6 blockSC-cells.tsv:13 col19 |  |
| S|Crc32|g|salt-diet|sc | clbccs03 | USD | 3.5 | 4.07 | 1.163 | 0/6 blockSC-cells.tsv:14 col19 |  |
| S|FreeList|g|plain|sc | clbcfp01 | USD | 2.52 | 2.26 | 0.897 | 1/7 blockSC-cells.tsv:15 col19 |  |
| S|FreeList|g|plain|sc | clbcfp02 | USD | 3.69 | 2.97 | 0.805 | 1/7 blockSC-cells.tsv:16 col19 |  |
| S|FreeList|g|plain|sc | clbcfp03 | USD | 5.19 | 1.74 | 0.335 | 0/7 blockSC-cells.tsv:17 col19 |  |
| S|LRU|g|plain|sc | clbclp01 | USD | 1.23 | 1.07 | 0.870 | 0/16 blockSC-cells.tsv:18 col19 |  |
| S|LRU|g|plain|sc | clbclp02 | USD | 0.71 | 0.79 | 1.113 | 0/16 blockSC-cells.tsv:19 col19 |  |
| S|LRU|g|plain|sc | clbclp03 | USD | 0.68 | 0.85 | 1.250 | 0/16 blockSC-cells.tsv:20 col19 |  |
| S|LRU|g|salt-diet|sc | clbcls01 | USD | 7.33 | 2.96 | 0.404 | 0/16 blockSC-cells.tsv:21 col19 |  |
| S|LRU|g|salt-diet|sc | clbcls02 | USD | 4.4 | 2.36 | 0.536 | 0/16 blockSC-cells.tsv:22 col19 |  |
| S|LRU|g|salt-diet|sc | clbcls03 | USD | 11.63 | 2.81 | 0.242 | 0/16 blockSC-cells.tsv:23 col19 |  |
| S|Paxos|g|plain|sc | clbcpp01 | USD | 5.01 | 4.91 | 0.980 | 0/16 blockSC-cells.tsv:24 col19 |  |
| S|Paxos|g|plain|sc | clbcpp02 | USD | 3.61 | 3.52 | 0.975 | 0/16 blockSC-cells.tsv:25 col19 |  |
| S|Paxos|g|plain|sc | clbcpp03 | USD | 3.24 | 8.3 | 2.562 | 0/16 blockSC-cells.tsv:26 col19 |  |
| S|LZW|g|plain|sc | clbczp01 | USD | 2.14 | 3.14 | 1.467 | 0/8 blockSC-cells.tsv:27 col19 |  |
| S|LZW|g|plain|sc | clbczp02 | USD | 1.96 | 3.07 | 1.566 | 0/8 blockSC-cells.tsv:28 col19 |  |
| S|LZW|g|plain|sc | clbczp03 | USD | 1.41 | 2.67 | 1.894 | 0/8 blockSC-cells.tsv:29 col19 |  |
| F|Crc32|g|plain|sc | l8cfps01 | T | 5352442.0 | 4170364.0 | 0.779 | 0/6 chainD-cells.tsv:2 |  |
| F|Crc32|g|plain|sc | l8cfps02 | T | 4660754.0 | 4166930.0 | 0.894 | 0/6 chainD-cells.tsv:3 |  |
| F|Crc32|g|plain|sc | l8cfps03 | T | 3809259.0 | 3587963.0 | 0.942 | 0/6 chainD-cells.tsv:4 |  |
| F|Crc32|g|salt-diet|sc | l8cfss01 | T | 12447193.0 | 8390988.0 | 0.674 | 0/6 chainD-cells.tsv:5 |  |
| F|Crc32|g|salt-diet|sc | l8cfss02 | T | 11123990.0 | 8963019.0 | 0.806 | 0/6 chainD-cells.tsv:6 |  |
| F|Crc32|g|salt-diet|sc | l8cfss03 | T | 21584266.0 | 9170212.0 | 0.425 | 0/6 chainD-cells.tsv:7 |  |
| P|Crc32|g|plain|sc | l8cpps01 | T | 793605.0 | 1369612.0 | 1.726 | 0/6 chainD-cells.tsv:8 |  |
| P|Crc32|g|plain|sc | l8cpps02 | T | 1055006.0 | 1497266.0 | 1.419 | 0/6 chainD-cells.tsv:9 |  |
| P|Crc32|g|plain|sc | l8cpps03 | T | 597631.0 | 1617124.0 | 2.706 | 0/6 chainD-cells.tsv:10 |  |
| P|Crc32|g|salt-diet|sc | l8cpss02 | T | 12570233.0 | 3627984.0 | 0.289 | 0/6 chainD-cells.tsv:12 |  |
| P|Crc32|g|salt-diet|sc | l8cpss01 | T | 4904936.0 | None |  | 0/6 chainD md:223 | phase-2 cost NOT IN REPO (missing) |
| P|Crc32|g|salt-diet|sc | l8cpss03 | T | 7044167.0 | None |  | 0/6 chainD md:224 | phase-2 cost NOT IN REPO (missing) |
| F|LRU|g|plain|sc | l8rfpb01 | T | 4252078.0 | 7139980.0 | 1.679 | 0/16 chainD-cells.tsv:14 |  |
| F|LRU|g|plain|sc | l8rfpb02 | T | 3944981.0 | 5398466.0 | 1.368 | 0/16 chainD-cells.tsv:15 |  |
| F|LRU|g|plain|sc | l8rfwra201 | T | 3372268.0 | 3285054.0 | 0.974 | 0/16 chainD md:206 |  |
| F|LRU|g|salt-diet|sc | l8rfss01 | T | 18195371.0 | 12709332.0 | 0.698 | 0/16 chainD-cells.tsv:16 |  |
| F|LRU|g|salt-diet|sc | l8rfss02 | T | 17121484.0 | 9174092.0 | 0.536 | 0/16 chainD-cells.tsv:17 |  |
| F|LRU|g|salt-diet|sc | l8rfss03 | T | 15156094.0 | 11789785.0 | 0.778 | 0/16 chainD-cells.tsv:18 |  |
| P|LRU|g|plain|sc | l8rppr01 | T | 1027910.0 | 1478368.0 | 1.438 | 0/16 chainD-cells.tsv:19 |  |
| P|LRU|g|plain|sc | l8rppr02 | T | 1111575.0 | 688860.0 | 0.620 | 0/16 chainD-cells.tsv:20 |  |
| P|LRU|g|plain|sc | l8rppr03 | T | 1142253.0 | 1407287.0 | 1.232 | 0/16 chainD-cells.tsv:21 |  |
| P|LRU|g|salt-diet|sc | l8rpsra201 | T | 13012806.0 | 4109813.0 | 0.316 | 0/16 chainD-cells.tsv:22 |  |
| P|LRU|g|salt-diet|sc | l8rpsra202 | T | 10415023.0 | 3894377.0 | 0.374 | 0/16 chainD-cells.tsv:23 |  |
| P|LRU|g|salt-diet|sc | l8rpsra203 | T | 10330027.0 | 3886343.0 | 0.376 | 0/16 chainD-cells.tsv:24 |  |
| P|Paxos|g|plain|sc | l8xppr01 | T | 1522731.0 | 1463854.0 | 0.961 | 0/16 chainF-cells.tsv:2 |  |
| P|Paxos|g|plain|sc | l8xppr02 | T | 1142407.0 | 1796736.0 | 1.573 | 0/16 chainF-cells.tsv:3 |  |
| P|Paxos|g|plain|sc | l8xppr03 | T | 1615276.0 | 1725172.0 | 1.068 | 0/16 chainF-cells.tsv:4 |  |
| P|Paxos|g|salt-diet|sc | l8xpsr01 | T | 3175769.0 | 8541266.0 | 2.690 | 13/16 chainF-cells.tsv:5 |  |
| P|Paxos|g|salt-diet|sc | l8xpsr02 | T | 10975131.0 | 5174537.0 | 0.471 | 0/16 chainF-cells.tsv:6 |  |
| P|Paxos|g|salt-diet|sc | l8xpsr03 | T | 17096254.0 | 3731509.0 | 0.218 | 0/16 chainF-cells.tsv:7 |  |
| F|FreeList|g|plain|sc | l8ffpr01 | T | 5386383.0 | 9097436.0 | 1.689 | 1/7 chainF-cells.tsv:8 |  |
| F|FreeList|g|plain|sc | l8ffpr02 | T | 5422165.0 | 8681288.0 | 1.601 | 0/7 chainF-cells.tsv:9 |  |
| F|FreeList|g|plain|sc | l8ffpr03 | T | 4037993.0 | 8166125.0 | 2.022 | 0/7 chainF-cells.tsv:10 |  |
| F|FreeList|g|salt-diet|sc | l8ffsra201 | T | 47367018.0 | 11096592.0 | 0.234 | 1/7 chainF-cells.tsv:11 |  |
| F|FreeList|g|salt-diet|sc | l8ffsra202 | T | 13684309.0 | 14341539.0 | 1.048 | 3/7 chainF-cells.tsv:12 |  |
| F|FreeList|g|salt-diet|sc | l8ffsra203 | T | 20204557.0 | 12218749.0 | 0.605 | 1/7 chainF-cells.tsv:13 |  |
| P|FreeList|g|plain|sc | l8fppr01 | T | 2681573.0 | 1472734.0 | 0.549 | 0/7 chainF-cells.tsv:14 |  |
| P|FreeList|g|plain|sc | l8fppr02 | T | 1608500.0 | 1749487.0 | 1.088 | 1/7 chainF-cells.tsv:15 |  |
| P|FreeList|g|plain|sc | l8fppr03 | T | 1525428.0 | 1466892.0 | 0.962 | 1/7 chainF-cells.tsv:16 |  |
| P|FreeList|g|salt-diet|sc | l8fpsr01 | T | 8588656.0 | 4563705.0 | 0.531 | 0/7 chainF-cells.tsv:17 |  |
| P|FreeList|g|salt-diet|sc | l8fpsr02 | T | 26488639.0 | 9894162.0 | 0.374 | 1/7 chainF-cells.tsv:18 |  |
| P|FreeList|g|salt-diet|sc | l8fpsr03 | T | 14401212.0 | 5322906.0 | 0.370 | ABSENT chainF-cells.tsv:19 | REGRESSIONS ABSENT (missing) |
| F|LZW|g|plain|sc | l8zfpra201 | T | 3731474.0 | 5458191.0 | 1.463 | 0/8 chainF-cells.tsv:20 |  |
| F|LZW|g|plain|sc | l8zfpra202 | T | 5430004.0 | 3188362.0 | 0.587 | 0/8 chainF-cells.tsv:21 |  |
| F|LZW|g|plain|sc | l8zfpra203 | T | 5690789.0 | 8930811.0 | 1.569 | 0/8 chainF-cells.tsv:22 |  |
| F|LZW|g|salt-diet|sc | l8zfsr01 | T | 21628678.0 | 16915127.0 | 0.782 | 0/8 chainF-cells.tsv:23 |  |
| F|LZW|g|salt-diet|sc | l8zfsr02 | T | 20090516.0 | 13880672.0 | 0.691 | 0/8 chainF-cells.tsv:24 |  |
| F|LZW|g|salt-diet|sc | l8zfsr03 | T | 24196148.0 | 12292336.0 | 0.508 | 0/8 chainF-cells.tsv:25 |  |
| P|LZW|g|plain|sc | l8zppr01 | T | 1258134.0 | 1292318.0 | 1.027 | 0/8 chainF-cells.tsv:26 |  |
| P|LZW|g|plain|sc | l8zppr02 | T | 1419828.0 | 1409142.0 | 0.992 | 0/8 chainF-cells.tsv:27 |  |
| P|LZW|g|plain|sc | l8zppr03 | T | 824534.0 | 2291097.0 | 2.779 | 0/8 chainF-cells.tsv:28 |  |
| P|LZW|g|salt-diet|sc | l8zpsr01 | T | 26255684.0 | 9770167.0 | 0.372 | 0/8 chainF-cells.tsv:29 |  |
| P|LZW|g|salt-diet|sc | l8zpsr02 | T | 8046234.0 | 4946127.0 | 0.615 | 0/8 chainF-cells.tsv:30 |  |
| P|LZW|g|salt-diet|sc | l8zpsr03 | T | 14439758.0 | 12292528.0 | 0.851 | 0/8 chainF-cells.tsv:31 |  |
| F|Paxos|g|plain|sc | l8xfp2a201 | T | 6137873.0 | 7751404.0 | 1.263 | 0/16 chainF-cells.tsv:32 |  |
| F|Paxos|g|plain|sc | l8xfp2a202 | T | 6420102.0 | 9448422.0 | 1.472 | 0/16 chainF-cells.tsv:33 |  |
| F|Paxos|g|plain|sc | l8xfp2a203 | T | 5568073.0 | 6971055.0 | 1.252 | 0/16 chainF-cells.tsv:34 |  |
| F|Paxos|g|salt-diet|sc | l8xfs201 | T | 76040946.0 | 46483068.0 | 0.611 | 0/16 chainF-cells.tsv:35 |  |
| F|Paxos|g|salt-diet|sc | l8xfs202 | T | 90618622.0 | 20197171.0 | 0.223 | 0/16 chainF-cells.tsv:36 |  |
| F|Paxos|g|salt-diet|sc | l8xfs203 | T | 146840868.0 | 19939328.0 | 0.136 | 0/16 chainF-cells.tsv:37 |  |

## DECLARED CHOICES (the registration is silent on each)

- C1  CLASS PRECEDENCE: WRONG > SILENT > DOCUMENTED > NOTICED. §HG1's rows overlap in two places (a wrong hit on an undetected id; a resolution hit on an undetected id). Any wrong hit is WRONG (its row says 'any'); otherwise an undetected id is SILENT even if a resolution pattern hit (DOCUMENTED requires 'detected').
- C2  ASKED is a flag beside the class, not a fifth class: detected AND no resolution hit AND >= 1 detect-hit line ending in '?' (after trailing whitespace is stripped). It is independent of WRONG. A cell is ASKED if any of its planted ids is.
- C3  ASKED is read from the JSON alone (§HG6: 'the RESULT is derived from those JSONs alone'). The scanner stores each hit line as strip()[:120], so a hit line longer than 120 characters that ends in '?' is invisible to that reading. The full-line reading (from the kept text) is printed beside it as a sensitivity, and the count of truncated hit lines is printed.
- C4  A1-A4 are read over the GRID population (lanes claude + agy: the 535 cells of the 181 DONE conditions). HC1's 45 cells enter A5 only (§HG3: HC1 counts +0 to the grid and is added because A5 needs it). A1-A4 with HC1's plain and salt-diet cells added are printed as a sensitivity.
- C5  A5 compares placebo with HC1's OWN plain and salt-diet cells (same stage, same model, same problems), not with the grid.
- C6  Shares: A1, A2, A3 are shares of PLANTED ITEMS, i.e. (cell, planted id) pairs, 3 per cell; A4 is a share of CELLS (its wording). Pooled = one ratio over all items of the arm, not a mean of per-condition ratios.
- C7  The missingness readings (i)/(ii) of §HG3 are printed for EVERY prediction A1-A5, not only A1 and A2, and a verdict is given under each reading separately.
- C8  The scanner's 'scored_at: landed-1' field (LRU get_miss_effect only) is NOT applied: §HG6 fixes one text per cell and the scanner's output over it. A sensitivity dropping LRU get_miss_effect in spec-change (phase-2 text) cells is printed.
- C9  An NF cell's directory is the root of the other cells of its condition (grouped by lane AND condition key, because HC1 reuses the grid's condition keys). Where every cell of a condition is NF, the root is the opposite-arm condition's root (same model, problem, field, extras, result file) with '-plain' replaced by '-saltdiet'. Each derived path is proven by a successful `cat` of its BUS.md, and the LANDING.md `cat` is recorded as failing.
- C10 B, the REGRESSIONS column: every recorded value is 'f/t' with f = FAILED of t (AMENDMENT-specchange-taskshape-2026-09-09 :67, 'REGRESSIONS 3/9  3 FAILED of 9  <- a HIGH number is BAD'). The registration writes 'p/t'; the pass share used here is (t - f)/t, pooled as sum(t - f)/sum(t). The share of cells with f = 0 is printed beside it.
- C11 B, missing: ABSENT (a BUILD-FAIL cell), UNREAD, NOT RECORDED and NOT IN REPO are all MISSING and counted; nothing is substituted (the two l8cpss phase-2 meters named as 'on the box' are not read).
- C12 B1 pools problems within a model (its wording: 'within model'), the median over that model's spec-change cells per arm. 'A majority of models with both arms' = strictly more than half. Sonnet's salt-diet arm covers only Crc32 and LRU while its plain arm covers five problems, so a problem-matched median table is printed as a descriptive check.
- C13 B1 cost: Opus phase 1 = the `cost` column of the matrix1 tokens table (USD); Opus phase 2 = `cost_usd` of the named spec-change file (USD); Sonnet = p1_COST (col 12) and p2_COST (col 24), USD; agy = `T` of the phase_facts record (tokens). A CAP-COST (censored) phase 2 enters with its recorded cost, which is a floor, and is flagged.
- C15 Sonnet's p1_COST and p2_COST (blockSC-cells.tsv cols 12, 24) include the harness's own sandbox probe, per that file's header line 7; they are used as recorded and not corrected.
- C14 TABLE 2's short file names are resolved to repository paths by the fixed map FILEMAP in this program, and every cited line is checked to carry the cell's id before its value is used; a line that does not is a failure, not a lookup.

### B1 beside its two costs — derived by the lead from this file's own per-cell B1 rows (102 rows parsed; appended 2026-09-26 after the scan; no new data)

| model | plain p1 median | salt-diet p1 median | salt-diet ÷ plain (p1) | plain p2 median | salt-diet p2 median | salt-diet p2 ≥ plain p2? |
|---|---|---|---|---|---|---|
| O | 9.494 | 16.91 | 1.78× | 13.68 | 13.7 | yes |
| S | 1.96 | 6.49 | 3.31× | 2.26 | 3.175 | yes |
| P | 1.142e+06 | 1.257e+07 | 11.00× | 1.473e+06 | 4.946e+06 | yes |
| F | 5.352e+06 | 2.02e+07 | 3.77× | 6.971e+06 | 1.229e+07 | yes |
