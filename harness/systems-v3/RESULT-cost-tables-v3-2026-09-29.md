# RESULT: THE COMPLETE PILOT MATRIX IN DOLLARS AND WALL TIME (arXiv v3)
## Printed by `harness/systems-v3/tables_v3.py` over the working tree at repo head `a2d28c036944`, from `harness/systems-v3/CELLMAP-descriptive-tables-v2-2026-09-27.tsv` and `evidence/v3-cost-tables-2026-09-28`. Registered in `REGISTRATION-cost-tables-v3-2026-09-29.md` (§V1–§V6, ADDENDA 1–3), committed before this ran. The instrument and its inputs may be newer than that head, so they are named by CONTENT (git blob ids, checkable at any commit with `git hash-object <file>`): `tables_v3.py` 636d91092996 · `CELLMAP-descriptive-tables-v2-2026-09-27.tsv` 27c8f4ec4bc0 · `cellroots.tsv` 6d37b2c23049 · `claude-cost-raw.tsv` 145040287173 · `claude-wall-raw.tsv` c87c69df47dd · `claude-wall-raw-allroots.tsv` 2ef4a5f77a63 · `agy-steps-raw.tsv` b033e71f9eb0 · `opus-split-raw.tsv` 938dc0af806b · `rates-gemini-2026-09-29.tsv` 78092ada6219.

**$ CHECK numbers 178 + — 16 + declared 3 + unmeasured 3 = 200 (other 0) against 200**
**W CHECK numbers 181 + — 16 + declared 3 + unmeasured 0 = 200 (other 0) against 200**
**Second methods: 0 disagreement(s).**

⛔ **A descriptive reading over the complete matrix: no test, no p-value, no verdict on the arms; the registered tests remain §4's.** A cheaper arm is cheaper, not better.

- **Dollars are MODELLED at list prices, not invoices** (every cell ran on a subscription): one schedule per vendor, both pages read 2026-09-29 (`rates-gemini-2026-09-29.tsv`; Claude `rates.tsv` rows re-read and agreeing). Claude: every record at its served model's rates, so an Opus cell's Sonnet subagents are priced at Sonnet's. agy: per request at the tier of its prompt (input + cache read), thinking inside output and priced once (ADDENDUM 2 A2.1). Context-caching STORAGE is not priced.
- **The Pro upper price tier (prompts over 200k) is selected by NO request in these data** (largest Pro prompt 144,717); only the selftest exercises that arm (A2.4).
- **Wall includes the box.** It depends on what else the run box was doing and on the vendor's service at that hour. Not extracted per cell here: the records that carry the concurrency (`claude_live_at_fire` in the Claude fire logs, the agy concurrency column, the one-heavy-job lock). A wall `≥` set by timing (within one turn timeout of the wall cap) errs toward the floor (A2.5).
- **`≥`** a floor (CAP-COST, FLOOR, DEADLINE by the record; a meter `VOID(UNDERSTATED)`; a wall at its cap). A CAP-COST cell's dollars are the larger of its metered cost and the cap its end marker names (A1.3). **`—`** inexpressible. **`declared`** unreached at the cap.
- **Priced from per-request records larger than the meter's fold (EXCEEDS-METER, flagged):** l6vbls01, l6vgps01, l6vgps02, l7npfs03, l7npzs03, l8cpss01, l8cpss03, l8xpsr01.
- Rule 1's reproduction differences have two causes, both shown at the object (ADDENDUM 3 A3.2): the SC cells' probe-separated tracked columns, and the copy-root cells' re-run of the landing's slug alone.

## Unmeasured cells in DONE conditions, per currency
| currency | model | problem | field | arm | extras | cell | why |
|---|---|---|---|---|---|---|---|
| usd | gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | s3ft02 | agy-steps-raw.tsv: p1 a tiered price and PARTIAL per-request records |
| usd | gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | l7cpbs03 | agy-steps-raw.tsv: p1 a tiered price and PARTIAL per-request records |
| usd | gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr02 | agy-steps-raw.tsv: p1 a tiered price and PARTIAL per-request records; p2 per request, tiered (COMPLETE) |

## $1 · greenfield — median modelled list-price dollars per condition

| model | problem | bare-plain | bare-salt-diet | statement-plain | statement-salt-diet |
|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | ≥ $6.21 | ≥ $7.21 | $6.66 | $6.25 |
| claude-opus-5 | LRU | ≥ $9.73 | $11.21 | $9.36 | $14.24 |
| claude-opus-5 | FreeList | ≥ $13.02 | ≥ $37.60 | ≥ $18.26 | $27.84 |
| claude-opus-5 | LZW | $13.95 | $19.18 | ≥ $10.24 | ≥ $18.54 |
| claude-opus-5 | Paxos | ≥ $16.78 | $37.65 | — | — |
| claude-sonnet-5 | Crc32 | $1.14 | $4.79 | $0.98 | $4.16 |
| claude-sonnet-5 | LRU | ≥ $1.23 | ≥ $5.75 | $1.38 | ≥ $6.67 |
| claude-sonnet-5 | FreeList | $2.92 | ≥ $37.72 | $2.81 | ≥ $35.08 |
| claude-sonnet-5 | LZW | $1.70 | $14.39 | $1.89 | ≥ $12.36 |
| claude-sonnet-5 | Paxos | $3.38 | ≥ $37.61 | — | — |
| gemini-3.1-pro-high | Crc32 | $0.65 | $5.35 | $0.80 | ≥ $6.38 |
| gemini-3.1-pro-high | LRU | $1.21 | $4.42 | $0.72 | $4.58 |
| gemini-3.1-pro-high | FreeList | $0.83 | $4.91 | $0.94 | unmeasured |
| gemini-3.1-pro-high | LZW | $0.73 | $5.27 | $0.84 | $7.29 |
| gemini-3.1-pro-high | Paxos | $0.69 | ≥ $6.84 | — | — |
| gemini-3.8-flash-high | Crc32 | $0.82 | $2.15 | $0.80 | $2.95 |
| gemini-3.8-flash-high | LRU | $1.17 | $2.78 | $0.72 | $2.61 |
| gemini-3.8-flash-high | FreeList | $1.18 | $3.48 | $1.03 | $3.59 |
| gemini-3.8-flash-high | LZW | $0.89 | ≥ $3.81 | $1.12 | $3.08 |
| gemini-3.8-flash-high | Paxos | $1.29 | $4.57 | — | — |

## $2 · brownfield — median modelled list-price dollars per condition

| model | problem | bare-plain | bare-salt-diet | statement-plain | statement-salt-diet |
|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | $6.70 | $7.62 | ≥ $9.69 | ≥ $7.06 |
| claude-opus-5 | LRU | $8.17 | $15.03 | $10.36 | $14.59 |
| claude-opus-5 | FreeList | ≥ $18.66 | ≥ $37.30 | ≥ $19.57 | ≥ $29.62 |
| claude-opus-5 | LZW | $10.11 | $15.99 | ≥ $13.47 | $17.90 |
| claude-opus-5 | Paxos | $13.14 | $32.22 | — | — |
| claude-sonnet-5 | Crc32 | ≥ $0.90 | $4.11 | $1.01 | $3.94 |
| claude-sonnet-5 | LRU | $0.94 | $7.74 | $1.09 | ≥ $5.27 |
| claude-sonnet-5 | FreeList | $2.41 | ≥ $37.43 | $2.34 | ≥ $37.60 |
| claude-sonnet-5 | LZW | $1.52 | ≥ $19.30 | $1.79 | ≥ $18.14 |
| claude-sonnet-5 | Paxos | ≥ $3.05 | ≥ $37.92 | — | — |
| gemini-3.1-pro-high | Crc32 | $0.67 | unmeasured | $0.80 | $3.64 |
| gemini-3.1-pro-high | LRU | $0.54 | $2.35 | $0.76 | ≥ $4.97 |
| gemini-3.1-pro-high | FreeList | $1.03 | $6.83 | $0.92 | $6.06 |
| gemini-3.1-pro-high | LZW | $0.86 | ≥ $13.81 | $0.86 | ≥ $7.39 |
| gemini-3.1-pro-high | Paxos | $0.95 | ≥ $6.58 | — | — |
| gemini-3.8-flash-high | Crc32 | $0.78 | $1.63 | $0.86 | $2.21 |
| gemini-3.8-flash-high | LRU | $0.77 | $2.69 | $0.79 | $2.33 |
| gemini-3.8-flash-high | FreeList | $0.92 | $3.26 | $1.42 | $2.93 |
| gemini-3.8-flash-high | LZW | $1.25 | $2.77 | $0.93 | $1.91 |
| gemini-3.8-flash-high | Paxos | $1.32 | $3.33 | — | — |

## $3 · spec-change (greenfield only) — median modelled list-price dollars per condition

| model | problem | plain | salt-diet |
|---|---|---|---|
| claude-opus-5 | Crc32 | ≥ $19.89 | ≥ $16.48 |
| claude-opus-5 | LRU | ≥ $22.27 | $22.33 |
| claude-opus-5 | FreeList | ≥ $29.41 | $50.22 |
| claude-opus-5 | LZW | $23.77 | ≥ $41.24 |
| claude-opus-5 | Paxos | ≥ $30.29 | ≥ $49.67 |
| claude-sonnet-5 | Crc32 | ≥ $2.03 | ≥ $9.15 |
| claude-sonnet-5 | LRU | $1.53 | $10.29 |
| claude-sonnet-5 | FreeList | $6.66 | declared |
| claude-sonnet-5 | LZW | ≥ $5.03 | declared |
| claude-sonnet-5 | Paxos | ≥ $9.92 | declared |
| gemini-3.1-pro-high | Crc32 | $1.29 | $6.01 |
| gemini-3.1-pro-high | LRU | $1.43 | $6.19 |
| gemini-3.1-pro-high | FreeList | $1.96 | unmeasured |
| gemini-3.1-pro-high | LZW | $1.65 | $10.73 |
| gemini-3.1-pro-high | Paxos | $1.80 | ≥ $7.29 |
| gemini-3.8-flash-high | Crc32 | $1.61 | $2.89 |
| gemini-3.8-flash-high | LRU | $1.57 | $3.55 |
| gemini-3.8-flash-high | FreeList | $2.20 | $4.15 |
| gemini-3.8-flash-high | LZW | $1.67 | $4.97 |
| gemini-3.8-flash-high | Paxos | $2.28 | $16.16 |

## $4 · salt-diet ÷ plain, greenfield, modelled list-price dollars (v2 §D4's rule)

| model | problem | bare | statement | spec-change |
|---|---|---|---|---|
| claude-opus-5 | Crc32 | bounds only (1.16) | 0.94 | bounds only (0.83) |
| claude-opus-5 | LRU | ≤ 1.15 | 1.52 | ≤ 1.00 |
| claude-opus-5 | FreeList | bounds only (2.89) | ≤ 1.53 | ≤ 1.71 |
| claude-opus-5 | LZW | 1.37 | bounds only (1.81) | ≥ 1.73 |
| claude-opus-5 | Paxos | ≤ 2.24 | — | bounds only (1.64) |
| claude-sonnet-5 | Crc32 | 4.19 | 4.25 | bounds only (4.51) |
| claude-sonnet-5 | LRU | bounds only (4.68) | ≥ 4.82 | 6.73 |
| claude-sonnet-5 | FreeList | ≥ 12.93 | ≥ 12.50 | — |
| claude-sonnet-5 | LZW | 8.48 | ≥ 6.55 | — |
| claude-sonnet-5 | Paxos | ≥ 11.14 | — | — |
| gemini-3.1-pro-high | Crc32 | 8.24 | ≥ 7.98 | 4.66 |
| gemini-3.1-pro-high | LRU | 3.66 | 6.39 | 4.34 |
| gemini-3.1-pro-high | FreeList | 5.88 | — | — |
| gemini-3.1-pro-high | LZW | 7.25 | 8.68 | 6.51 |
| gemini-3.1-pro-high | Paxos | ≥ 9.85 | — | ≥ 4.05 |
| gemini-3.8-flash-high | Crc32 | 2.61 | 3.70 | 1.80 |
| gemini-3.8-flash-high | LRU | 2.38 | 3.62 | 2.26 |
| gemini-3.8-flash-high | FreeList | 2.96 | 3.49 | 1.88 |
| gemini-3.8-flash-high | LZW | ≥ 4.28 | 2.75 | 2.98 |
| gemini-3.8-flash-high | Paxos | 3.53 | — | 7.07 |

### $4 sign counts, per model per treatment (no p-value)

| model | treatment | k of m ratios > 1 | indeterminate | median of the ratios | bounded among them |
|---|---|---|---|---|---|
| claude-opus-5 | bare | 1 of 1 | Crc32, LRU, FreeList, Paxos | 1.37 | 4 |
| claude-opus-5 | statement | 1 of 2 | FreeList, LZW | 1.52 | 2 |
| claude-opus-5 | spec-change | 1 of 1 | Crc32, LRU, FreeList, Paxos | 1.64 | 5 |
| claude-sonnet-5 | bare | 4 of 4 | LRU | 8.48 | 3 |
| claude-sonnet-5 | statement | 4 of 4 | none | 5.68 | 3 |
| claude-sonnet-5 | spec-change | 1 of 1 | Crc32 | 5.62 | 1 |
| gemini-3.1-pro-high | bare | 5 of 5 | none | 7.25 | 1 |
| gemini-3.1-pro-high | statement | 3 of 3 | none | 7.98 | 1 |
| gemini-3.1-pro-high | spec-change | 4 of 4 | none | 4.50 | 1 |
| gemini-3.8-flash-high | bare | 5 of 5 | none | 2.96 | 1 |
| gemini-3.8-flash-high | statement | 4 of 4 | none | 3.56 | 0 |
| gemini-3.8-flash-high | spec-change | 5 of 5 | none | 2.26 | 0 |

### $ brownfield ratios (in the file, not in $4)

| model | problem | bare | statement |
|---|---|---|---|
| claude-opus-5 | Crc32 | 1.14 | bounds only (0.73) |
| claude-opus-5 | LRU | 1.84 | 1.41 |
| claude-opus-5 | FreeList | bounds only (2.00) | bounds only (1.51) |
| claude-opus-5 | LZW | 1.58 | ≤ 1.33 |
| claude-opus-5 | Paxos | 2.45 | — |
| claude-sonnet-5 | Crc32 | ≤ 4.56 | 3.89 |
| claude-sonnet-5 | LRU | 8.20 | ≥ 4.84 |
| claude-sonnet-5 | FreeList | ≥ 15.52 | ≥ 16.06 |
| claude-sonnet-5 | LZW | ≥ 12.73 | ≥ 10.11 |
| claude-sonnet-5 | Paxos | bounds only (12.43) | — |
| gemini-3.1-pro-high | Crc32 | — | 4.53 |
| gemini-3.1-pro-high | LRU | 4.34 | ≥ 6.53 |
| gemini-3.1-pro-high | FreeList | 6.61 | 6.58 |
| gemini-3.1-pro-high | LZW | ≥ 16.07 | ≥ 8.61 |
| gemini-3.1-pro-high | Paxos | ≥ 6.89 | — |
| gemini-3.8-flash-high | Crc32 | 2.10 | 2.56 |
| gemini-3.8-flash-high | LRU | 3.49 | 2.95 |
| gemini-3.8-flash-high | FreeList | 3.55 | 2.07 |
| gemini-3.8-flash-high | LZW | 2.21 | 2.05 |
| gemini-3.8-flash-high | Paxos | 2.53 | — |

## W1 · greenfield — median wall seconds per condition

| model | problem | bare-plain | bare-salt-diet | statement-plain | statement-salt-diet |
|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | ≥ 864 s | ≥ 1,104 s | ≥ 803 s | ≥ 1,044 s |
| claude-opus-5 | LRU | ≥ 1,105 s | 1,647 s | 1,526 s | ≥ 1,768 s |
| claude-opus-5 | FreeList | ≥ 2,190 s | ≥ 3,938 s | 2,490 s | 2,973 s |
| claude-opus-5 | LZW | ≥ 1,286 s | 2,371 s | ≥ 1,225 s | ≥ 2,491 s |
| claude-opus-5 | Paxos | ≥ 2,431 s | ≥ 3,336 s | — | — |
| claude-sonnet-5 | Crc32 | 321 s | 1,347 s | 261 s | 1,045 s |
| claude-sonnet-5 | LRU | 352 s | 1,769 s | 382 s | 1,709 s |
| claude-sonnet-5 | FreeList | 1,347 s | ≥ 7,864 s | 1,045 s | 7,382 s |
| claude-sonnet-5 | LZW | 623 s | 4,002 s | 744 s | 4,062 s |
| claude-sonnet-5 | Paxos | 1,468 s | ≥ 6,476 s | — | — |
| gemini-3.1-pro-high | Crc32 | 269 s | 1,596 s | 218 s | ≥ 1,620 s |
| gemini-3.1-pro-high | LRU | 613 s | 1,318 s | 229 s | 989 s |
| gemini-3.1-pro-high | FreeList | 332 s | 2,189 s | 320 s | ≥ 3,598 s |
| gemini-3.1-pro-high | LZW | 218 s | 3,806 s | 235 s | 2,044 s |
| gemini-3.1-pro-high | Paxos | 214 s | ≥ 3,577 s | — | — |
| gemini-3.8-flash-high | Crc32 | 281 s | 516 s | 242 s | 766 s |
| gemini-3.8-flash-high | LRU | 394 s | 864 s | 374 s | 913 s |
| gemini-3.8-flash-high | FreeList | 374 s | 986 s | 337 s | 772 s |
| gemini-3.8-flash-high | LZW | 308 s | 1,156 s | 339 s | 739 s |
| gemini-3.8-flash-high | Paxos | 385 s | 1,207 s | — | — |

## W2 · brownfield — median wall seconds per condition

| model | problem | bare-plain | bare-salt-diet | statement-plain | statement-salt-diet |
|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | 804 s | 1,227 s | 1,106 s | 985 s |
| claude-opus-5 | LRU | 1,106 s | 1,769 s | 1,045 s | 1,649 s |
| claude-opus-5 | FreeList | 1,890 s | ≥ 4,848 s | 2,252 s | 3,338 s |
| claude-opus-5 | LZW | 1,347 s | 2,855 s | 1,769 s | 2,131 s |
| claude-opus-5 | Paxos | 2,674 s | 3,277 s | — | — |
| claude-sonnet-5 | Crc32 | 261 s | 1,407 s | 382 s | 1,166 s |
| claude-sonnet-5 | LRU | 261 s | 2,071 s | 321 s | 1,528 s |
| claude-sonnet-5 | FreeList | 684 s | ≥ 6,657 s | 925 s | ≥ 7,623 s |
| claude-sonnet-5 | LZW | 442 s | 4,847 s | 562 s | 4,122 s |
| claude-sonnet-5 | Paxos | 1,227 s | ≥ 5,632 s | — | — |
| gemini-3.1-pro-high | Crc32 | 197 s | 1,297 s | 182 s | 1,084 s |
| gemini-3.1-pro-high | LRU | 182 s | 1,216 s | 207 s | ≥ 1,994 s |
| gemini-3.1-pro-high | FreeList | 313 s | 4,382 s | 268 s | ≥ 2,458 s |
| gemini-3.1-pro-high | LZW | 242 s | ≥ 5,817 s | 198 s | ≥ 4,375 s |
| gemini-3.1-pro-high | Paxos | 364 s | 2,812 s | — | — |
| gemini-3.8-flash-high | Crc32 | 261 s | 408 s | 235 s | 900 s |
| gemini-3.8-flash-high | LRU | 299 s | 657 s | 286 s | 841 s |
| gemini-3.8-flash-high | FreeList | 554 s | 906 s | 430 s | 677 s |
| gemini-3.8-flash-high | LZW | 487 s | 966 s | 398 s | 807 s |
| gemini-3.8-flash-high | Paxos | 413 s | 662 s | — | — |

## W3 · spec-change (greenfield only) — median wall seconds per condition

| model | problem | plain | salt-diet |
|---|---|---|---|
| claude-opus-5 | Crc32 | ≥ 2,270 s | ≥ 2,871 s |
| claude-opus-5 | LRU | ≥ 2,601 s | 2,511 s |
| claude-opus-5 | FreeList | ≥ 4,288 s | 5,164 s |
| claude-opus-5 | LZW | 2,480 s | ≥ 4,801 s |
| claude-opus-5 | Paxos | ≥ 4,620 s | ≥ 6,037 s |
| claude-sonnet-5 | Crc32 | 522 s | 2,333 s |
| claude-sonnet-5 | LRU | 521 s | 2,996 s |
| claude-sonnet-5 | FreeList | 2,212 s | declared |
| claude-sonnet-5 | LZW | 1,789 s | declared |
| claude-sonnet-5 | Paxos | 4,082 s | declared |
| gemini-3.1-pro-high | Crc32 | 389 s | 4,863 s |
| gemini-3.1-pro-high | LRU | 400 s | 1,961 s |
| gemini-3.1-pro-high | FreeList | 592 s | 4,089 s |
| gemini-3.1-pro-high | LZW | 512 s | 4,677 s |
| gemini-3.1-pro-high | Paxos | 560 s | ≥ 3,207 s |
| gemini-3.8-flash-high | Crc32 | 913 s | 1,330 s |
| gemini-3.8-flash-high | LRU | 717 s | 1,768 s |
| gemini-3.8-flash-high | FreeList | 809 s | 1,654 s |
| gemini-3.8-flash-high | LZW | 793 s | 2,072 s |
| gemini-3.8-flash-high | Paxos | 1,064 s | 8,482 s |

## W4 · salt-diet ÷ plain, greenfield, wall seconds (v2 §D4's rule)

| model | problem | bare | statement | spec-change |
|---|---|---|---|---|
| claude-opus-5 | Crc32 | bounds only (1.28) | bounds only (1.30) | bounds only (1.26) |
| claude-opus-5 | LRU | ≤ 1.49 | ≥ 1.16 | ≤ 0.97 |
| claude-opus-5 | FreeList | bounds only (1.80) | 1.19 | ≤ 1.20 |
| claude-opus-5 | LZW | ≤ 1.84 | bounds only (2.03) | ≥ 1.94 |
| claude-opus-5 | Paxos | bounds only (1.37) | — | bounds only (1.31) |
| claude-sonnet-5 | Crc32 | 4.20 | 4.00 | 4.47 |
| claude-sonnet-5 | LRU | 5.03 | 4.47 | 5.75 |
| claude-sonnet-5 | FreeList | ≥ 5.84 | 7.06 | — |
| claude-sonnet-5 | LZW | 6.42 | 5.46 | — |
| claude-sonnet-5 | Paxos | ≥ 4.41 | — | — |
| gemini-3.1-pro-high | Crc32 | 5.93 | ≥ 7.45 | 12.49 |
| gemini-3.1-pro-high | LRU | 2.15 | 4.32 | 4.90 |
| gemini-3.1-pro-high | FreeList | 6.60 | ≥ 11.24 | 6.91 |
| gemini-3.1-pro-high | LZW | 17.46 | 8.69 | 9.13 |
| gemini-3.1-pro-high | Paxos | ≥ 16.70 | — | ≥ 5.72 |
| gemini-3.8-flash-high | Crc32 | 1.84 | 3.16 | 1.46 |
| gemini-3.8-flash-high | LRU | 2.19 | 2.44 | 2.47 |
| gemini-3.8-flash-high | FreeList | 2.63 | 2.29 | 2.04 |
| gemini-3.8-flash-high | LZW | 3.75 | 2.18 | 2.61 |
| gemini-3.8-flash-high | Paxos | 3.14 | — | 7.97 |

### W4 sign counts, per model per treatment (no p-value)

| model | treatment | k of m ratios > 1 | indeterminate | median of the ratios | bounded among them |
|---|---|---|---|---|---|
| claude-opus-5 | bare | 0 of 0 | Crc32, LRU, FreeList, LZW, Paxos | 1.49 | 5 |
| claude-opus-5 | statement | 2 of 2 | Crc32, LZW | 1.25 | 3 |
| claude-opus-5 | spec-change | 1 of 2 | Crc32, FreeList, Paxos | 1.26 | 5 |
| claude-sonnet-5 | bare | 5 of 5 | none | 5.03 | 2 |
| claude-sonnet-5 | statement | 4 of 4 | none | 4.97 | 0 |
| claude-sonnet-5 | spec-change | 2 of 2 | none | 5.11 | 0 |
| gemini-3.1-pro-high | bare | 5 of 5 | none | 6.60 | 1 |
| gemini-3.1-pro-high | statement | 4 of 4 | none | 8.07 | 2 |
| gemini-3.1-pro-high | spec-change | 5 of 5 | none | 6.91 | 1 |
| gemini-3.8-flash-high | bare | 5 of 5 | none | 2.63 | 0 |
| gemini-3.8-flash-high | statement | 4 of 4 | none | 2.36 | 0 |
| gemini-3.8-flash-high | spec-change | 5 of 5 | none | 2.47 | 0 |

### W brownfield ratios (in the file, not in W4)

| model | problem | bare | statement |
|---|---|---|---|
| claude-opus-5 | Crc32 | 1.53 | 0.89 |
| claude-opus-5 | LRU | 1.60 | 1.58 |
| claude-opus-5 | FreeList | ≥ 2.57 | 1.48 |
| claude-opus-5 | LZW | 2.12 | 1.20 |
| claude-opus-5 | Paxos | 1.23 | — |
| claude-sonnet-5 | Crc32 | 5.39 | 3.05 |
| claude-sonnet-5 | LRU | 7.93 | 4.76 |
| claude-sonnet-5 | FreeList | ≥ 9.73 | ≥ 8.24 |
| claude-sonnet-5 | LZW | 10.97 | 7.33 |
| claude-sonnet-5 | Paxos | ≥ 4.59 | — |
| gemini-3.1-pro-high | Crc32 | 6.57 | 5.95 |
| gemini-3.1-pro-high | LRU | 6.69 | ≥ 9.63 |
| gemini-3.1-pro-high | FreeList | 13.99 | ≥ 9.17 |
| gemini-3.1-pro-high | LZW | ≥ 24.02 | ≥ 22.09 |
| gemini-3.1-pro-high | Paxos | 7.72 | — |
| gemini-3.8-flash-high | Crc32 | 1.56 | 3.82 |
| gemini-3.8-flash-high | LRU | 2.19 | 2.94 |
| gemini-3.8-flash-high | FreeList | 1.64 | 1.57 |
| gemini-3.8-flash-high | LZW | 1.99 | 2.03 |
| gemini-3.8-flash-high | Paxos | 1.60 | — |

## S1 · Opus: the share of each cell's T and dollars OUTSIDE the head session (median over the condition's cells)

| problem | field | arm | extras | n | median share of T | median share of $ |
|---|---|---|---|---|---|---|
| Crc32 | brownfield | plain | none | 3 | 20.3 % | 24.8 % |
| Crc32 | brownfield | plain | statement | 3 | 22.2 % | 26.1 % |
| Crc32 | brownfield | salt-diet | none | 3 | 8.7 % | 5.1 % |
| Crc32 | brownfield | salt-diet | statement | 3 | 5.8 % | 5.0 % |
| Crc32 | greenfield | plain | none | 3 | 25.3 % | 31.3 % |
| Crc32 | greenfield | plain | spec-change | 3 | 25.3 % | 31.3 % |
| Crc32 | greenfield | plain | statement | 3 | 15.5 % | 22.3 % |
| Crc32 | greenfield | salt-diet | none | 3 | 9.4 % | 5.6 % |
| Crc32 | greenfield | salt-diet | spec-change | 3 | 9.4 % | 5.6 % |
| Crc32 | greenfield | salt-diet | statement | 3 | 5.6 % | 4.9 % |
| FreeList | brownfield | plain | none | 3 | 32.7 % | 40.0 % |
| FreeList | brownfield | plain | statement | 3 | 29.0 % | 38.1 % |
| FreeList | brownfield | salt-diet | none | 3 | 5.5 % | 13.9 % |
| FreeList | brownfield | salt-diet | statement | 3 | 5.6 % | 9.2 % |
| FreeList | greenfield | plain | none | 3 | 24.3 % | 35.1 % |
| FreeList | greenfield | plain | spec-change | 2 | 24.8 % | 36.2 % |
| FreeList | greenfield | plain | statement | 3 | 31.1 % | 38.9 % |
| FreeList | greenfield | salt-diet | none | 3 | 1.4 % | 6.2 % |
| FreeList | greenfield | salt-diet | spec-change | 1 | 1.4 % | 6.2 % |
| FreeList | greenfield | salt-diet | statement | 3 | 2.6 % | 7.7 % |
| LRU | brownfield | plain | none | 3 | 15.6 % | 24.6 % |
| LRU | brownfield | plain | statement | 3 | 36.7 % | 34.3 % |
| LRU | brownfield | salt-diet | none | 3 | 4.4 % | 8.7 % |
| LRU | brownfield | salt-diet | statement | 3 | 5.1 % | 11.8 % |
| LRU | greenfield | plain | none | 3 | 27.8 % | 36.0 % |
| LRU | greenfield | plain | spec-change | 2 | 30.5 % | 36.6 % |
| LRU | greenfield | plain | statement | 3 | 21.9 % | 31.3 % |
| LRU | greenfield | salt-diet | none | 3 | 3.0 % | 4.2 % |
| LRU | greenfield | salt-diet | spec-change | 3 | 3.0 % | 4.2 % |
| LRU | greenfield | salt-diet | statement | 3 | 4.8 % | 10.0 % |
| LZW | brownfield | plain | none | 3 | 24.9 % | 36.6 % |
| LZW | brownfield | plain | statement | 3 | 23.6 % | 28.8 % |
| LZW | brownfield | salt-diet | none | 3 | 11.9 % | 22.6 % |
| LZW | brownfield | salt-diet | statement | 3 | 6.2 % | 13.8 % |
| LZW | greenfield | plain | none | 3 | 22.2 % | 28.8 % |
| LZW | greenfield | plain | spec-change | 2 | 21.3 % | 27.8 % |
| LZW | greenfield | plain | statement | 3 | 20.4 % | 34.2 % |
| LZW | greenfield | salt-diet | none | 3 | 2.1 % | 5.7 % |
| LZW | greenfield | salt-diet | spec-change | 3 | 3.7 % | 8.6 % |
| LZW | greenfield | salt-diet | statement | 3 | 7.3 % | 13.5 % |
| Paxos | brownfield | plain | none | 3 | 21.5 % | 34.1 % |
| Paxos | brownfield | salt-diet | none | 3 | 2.2 % | 6.4 % |
| Paxos | greenfield | plain | none | 3 | 26.4 % | 30.9 % |
| Paxos | greenfield | plain | spec-change | 2 | 23.1 % | 29.4 % |
| Paxos | greenfield | salt-diet | none | 3 | 5.6 % | 6.8 % |
| Paxos | greenfield | salt-diet | spec-change | 2 | 5.7 % | 8.8 % |

## Rule 1's reproduction (ADDENDUM 2 A2.3): tracked cost of record against the cell_meter re-run

262 cells carry both; 46 differ by a cent or more (listed; they do NOT stop the run); 0 of them have no registered cause.

| cell | tracked (of record) | re-run | difference | cause (ADDENDUM 3 A3.2) |
|---|---|---|---|---|
| 2d0c65b3 | 17.7782 | 5.3582 | -12.4200 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 746d7d4e | 19.8949 | 6.2149 | -13.6800 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| a87b7740 | 23.1550 | 7.6350 | -15.5200 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 11165871 | 16.4842 | 6.1942 | -10.2900 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 3e95075c | 15.0411 | 7.2111 | -7.8300 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 57a33630 | 17.3184 | 7.6284 | -9.6900 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 188f422b | 23.2072 | 13.0172 | -10.1900 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 9cb8ce96 | 35.6199 | 23.3799 | -12.2400 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| f33c7e65 | 50.2241 | 35.4141 | -14.8100 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 3bdcbcbd | 21.1099 | 7.7499 | -13.3600 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 69e8c2c4 | 23.4207 | 9.7307 | -13.6900 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 011fe22f | 23.7683 | 11.1883 | -12.5800 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| b71994e3 | 19.9863 | 11.2063 | -8.7800 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| d6b53ee4 | 22.3326 | 14.6326 | -7.7000 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 93323249 | 20.1528 | 8.1528 | -12.0000 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 22ee7d33 | 27.3946 | 10.2446 | -17.1500 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 7ac56e4e | 34.8378 | 19.1778 | -15.6600 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 18fb3eed | 48.9775 | 31.6975 | -17.2800 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 6d58f1ec | 41.2416 | 22.5316 | -18.7100 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 60a056e6 | 24.0243 | 9.4943 | -14.5300 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| f6462d47 | 36.5631 | 16.7831 | -19.7800 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| 9e6c8d4d | 56.2679 | 37.6479 | -18.6200 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| b22d1000 | 43.0766 | 23.5166 | -19.5600 | A3.1 copy root: the re-run metered the landing's slug (phase 1) only |
| clbccp01 | 2.4900 | 2.6766 | +0.1866 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbccp02 | 2.0300 | 2.1706 | +0.1406 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbccp03 | 1.8600 | 1.9992 | +0.1392 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbccs01 | 10.9500 | 11.1224 | +0.1724 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbccs02 | 9.1500 | 9.3446 | +0.1946 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbccs03 | 7.5700 | 7.7512 | +0.1812 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbcfp01 | 4.7800 | 4.9200 | +0.1400 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbcfp02 | 6.6600 | 6.8254 | +0.1654 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbcfp03 | 6.9300 | 7.2164 | +0.2864 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbclp01 | 2.3000 | 2.4805 | +0.1805 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbclp02 | 1.5000 | 1.6579 | +0.1579 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbclp03 | 1.5300 | 1.6932 | +0.1632 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbcls01 | 10.2900 | 10.5232 | +0.2332 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbcls02 | 6.7600 | 7.0384 | +0.2784 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbcls03 | 14.4400 | 14.7180 | +0.2780 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbcpp01 | 9.9200 | 10.0679 | +0.1479 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbcpp02 | 7.1300 | 7.3051 | +0.1751 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbcpp03 | 11.5400 | 11.6891 | +0.1491 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbczp01 | 5.2800 | 5.4306 | +0.1506 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbczp02 | 5.0300 | 5.1938 | +0.1638 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbczp03 | 4.0800 | 4.2397 | +0.1597 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbczs01 | 24.0300 | 24.2912 | +0.2612 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |
| clbczs02 | 21.7300 | 22.0034 | +0.2734 | SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it |

## The CAP-COST cells (A1.3): the cap, the metered dollars and which entered

| cell | condition | cap named by its end marker | figure entered | source |
|---|---|---|---|---|
| 161b5a34 | claude-opus-5/FreeList/greenfield/salt-diet/none | 37.21 | 37.9488 | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=161b5a34].cost |
| de4de8f2 | claude-opus-5/FreeList/greenfield/salt-diet/none | 37.21 | 37.5957 | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=de4de8f2].cost |
| 6d58f1ec | claude-opus-5/LZW/greenfield/salt-diet/spec-change | - | 41.2416 | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=6d58f1ec].cost + harness/systems-v3/RESULT-specchange-1-verdicts-2026-09-10.tsv [cell=6d58f1ec].cost_usd |
| 9e6c8d4d | claude-opus-5/Paxos/greenfield/salt-diet/spec-change | - | 56.2679 | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9e6c8d4d].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=9e6c8d4d].cost_usd |
| b22d1000 | claude-opus-5/Paxos/greenfield/salt-diet/spec-change | - | 43.0766 | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=b22d1000].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=b22d1000].cost_usd |
| clbofs02 | claude-opus-5/FreeList/brownfield/salt-diet/none | 37.21 | 37.5792 | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofs02].final_COST |
| clbgfs01 | claude-sonnet-5/FreeList/greenfield/salt-diet/none | 37.21 | 37.7207 | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs01].final_COST |
| clbgfs02 | claude-sonnet-5/FreeList/greenfield/salt-diet/none | 37.21 | 37.6969 | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs02].final_COST |
| clbgfs03 | claude-sonnet-5/FreeList/greenfield/salt-diet/none | 37.21 | 37.9785 | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs03].final_COST |
| clbgps01 | claude-sonnet-5/Paxos/greenfield/salt-diet/none | 37.21 | 37.8011 | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps01].final_COST |
| clbgps02 | claude-sonnet-5/Paxos/greenfield/salt-diet/none | 37.21 | 37.6062 | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps02].final_COST |
| clbsfs02 | claude-sonnet-5/FreeList/greenfield/salt-diet/statement | 37.21 | 37.4618 | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfs02].final_COST |
| clbszs02 | claude-sonnet-5/LZW/greenfield/salt-diet/statement | 37.21 | 37.3123 | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszs02].final_COST |
| clbufs01 | claude-sonnet-5/FreeList/brownfield/salt-diet/statement | 37.21 | 38.5807 | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs01].final_COST |
| clbufs02 | claude-sonnet-5/FreeList/brownfield/salt-diet/statement | 37.21 | 37.4583 | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs02].final_COST |
| clbufs03 | claude-sonnet-5/FreeList/brownfield/salt-diet/statement | 37.21 | 37.5983 | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs03].final_COST |
| clbbfs01 | claude-sonnet-5/FreeList/brownfield/salt-diet/none | 37.21 | 37.8501 | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs01].final_COST |
| clbbfs03 | claude-sonnet-5/FreeList/brownfield/salt-diet/none | 37.21 | 37.4300 | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs03].final_COST |
| clbbps02 | claude-sonnet-5/Paxos/brownfield/salt-diet/none | 37.21 | 37.9576 | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps02].final_COST |
| clbbps03 | claude-sonnet-5/Paxos/brownfield/salt-diet/none | 37.21 | 37.9185 | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps03].final_COST |
| clbczs01 | claude-sonnet-5/LZW/greenfield/salt-diet/spec-change | 18.60 | 24.0300 | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs01].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs01].p2_COST |
| clbczs02 | claude-sonnet-5/LZW/greenfield/salt-diet/spec-change | 18.60 | 21.7300 | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs02].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs02].p2_COST |
| clbczs03 | claude-sonnet-5/LZW/greenfield/salt-diet/spec-change | 18.60 | 18.6000 | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs03].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs03].p2_COST -> the cap 18.60 entered (A1.3) |
| clbcfs01 | claude-sonnet-5/FreeList/greenfield/salt-diet/spec-change | 37.21 | 37.6942 | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) |
| clbcfs02 | claude-sonnet-5/FreeList/greenfield/salt-diet/spec-change | 37.21 | 37.4995 | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) |
| clbcfs03 | claude-sonnet-5/FreeList/greenfield/salt-diet/spec-change | 37.21 | 37.2789 | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) |
| clbcps01 | claude-sonnet-5/Paxos/greenfield/salt-diet/spec-change | 37.21 | 37.6169 | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) |
| clbcps02 | claude-sonnet-5/Paxos/greenfield/salt-diet/spec-change | 37.21 | 37.4009 | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) |
| clbcps03 | claude-sonnet-5/Paxos/greenfield/salt-diet/spec-change | 37.21 | 37.3077 | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) |

## Per-cell figures and their sources (every table number derives from these rows)

| model | problem | field | arm | extras | cell | dollars | wall s | lower bound | dollar source | wall source |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | greenfield | plain | none | 2d0c65b3 | 5.3582 | 924.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=2d0c65b3].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | plain | none | 746d7d4e | ≥ 6.2149 | ≥ 804.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=746d7d4e].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | plain | none | a87b7740 | 7.6350 | 864.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=a87b7740].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 11165871 | ≥ 6.1942 | ≥ 1045.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=11165871].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 3e95075c | ≥ 7.2111 | ≥ 1527.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=3e95075c].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 57a33630 | 7.6284 | 1104.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=57a33630].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | plain | none | 188f422b | ≥ 13.0172 | ≥ 2190.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=188f422b].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | plain | none | 9cb8ce96 | 23.3799 | 2913.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9cb8ce96].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | plain | none | n301free | ≥ 13.0111 | ≥ 1888.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-n3-topup,cell=n301free].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | 161b5a34 | ≥ 37.9488 | ≥ 4119.0 | CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=161b5a34].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | de4de8f2 | ≥ 37.5957 | ≥ 3938.0 | CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=de4de8f2].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | f33c7e65 | 35.4141 | 3637.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f33c7e65].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | plain | none | 3bdcbcbd | ≥ 7.7499 | ≥ 1105.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=3bdcbcbd].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | plain | none | 69e8c2c4 | ≥ 9.7307 | ≥ 1888.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=69e8c2c4].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | plain | none | n302lru | 9.8657 | 924.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-n3-topup,cell=n302lru].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | salt-diet | none | 011fe22f | 11.1883 | 1466.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=011fe22f].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | salt-diet | none | b71994e3 | 11.2063 | 1647.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=b71994e3].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | salt-diet | none | d6b53ee4 | 14.6326 | 1708.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=d6b53ee4].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | plain | none | 93323249 | 8.1528 | 924.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=93323249].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | plain | none | c34012e0 | ≥ 20.9513 | ≥ 1286.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=c34012e0].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | plain | none | d91f137b | 13.9489 | 2190.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=d91f137b].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | salt-diet | none | 18fb3eed | 31.6975 | 2974.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=18fb3eed].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | salt-diet | none | 7ac56e4e | 19.1778 | 2370.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=7ac56e4e].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | salt-diet | none | eb558398 | 18.1610 | 2371.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=eb558398].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | greenfield | plain | none | 60a056e6 | ≥ 9.4943 | ≥ 2189.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=60a056e6].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | greenfield | plain | none | f6462d47 | ≥ 16.7831 | ≥ 2431.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f6462d47].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | greenfield | plain | none | n303paxo | 20.1567 | 6527.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-n3-topup,cell=n303paxo].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | 6fc49f7c | ≥ 37.9302 | ≥ 3335.0 | FLOOR+CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=6fc49f7c].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | 9e6c8d4d | 37.6479 | 3336.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9e6c8d4d].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | b22d1000 | 23.5166 | 3697.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=b22d1000].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | plain | statement | st01crc3 | 6.3556 | 743.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st01crc3].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | plain | statement | st02crc3 | ≥ 8.6406 | ≥ 803.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st02crc3].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | plain | statement | st03crc3 | 6.6632 | 803.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st03crc3].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | salt-diet | statement | st04crc3 | ≥ 8.5561 | ≥ 1044.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st04crc3].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | salt-diet | statement | st05crc3 | 5.6526 | 863.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st05crc3].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | salt-diet | statement | st06crc3 | 6.2530 | 1044.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st06crc3].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | plain | statement | st07lru | 9.3579 | 1526.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st07lru].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | plain | statement | st08lru | 8.9224 | 1225.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st08lru].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | plain | statement | st09lru | 15.1175 | 1827.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st09lru].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | salt-diet | statement | st10lru | ≥ 18.6538 | ≥ 1768.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st10lru].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | salt-diet | statement | st11lru | 14.2378 | 2069.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st11lru].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | greenfield | salt-diet | statement | st12lru | 13.6535 | 1707.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-2026-09-09,cell=st12lru].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | plain | statement | sf01free | ≥ 17.7225 | ≥ 2852.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf01free].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | plain | statement | sf02free | 18.2564 | 2490.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf02free].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | plain | statement | sf03free | 18.4248 | 2310.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf03free].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | salt-diet | statement | sf04free | 29.0007 | 2792.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf04free].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | salt-diet | statement | sf05free | 21.1760 | 3334.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf05free].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | greenfield | salt-diet | statement | sf06free | 27.8449 | 2973.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-stmt-free-2026-09-09,cell=sf06free].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | plain | statement | 22ee7d33 | 10.2446 | 1225.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=22ee7d33].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | plain | statement | 922d1ff0 | 11.3897 | 1708.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=922d1ff0].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | plain | statement | f795e96f | ≥ 9.8206 | ≥ 1165.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f795e96f].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | salt-diet | statement | 6d58f1ec | 22.5316 | 2491.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=6d58f1ec].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | salt-diet | statement | 9aca67c5 | ≥ 15.3447 | ≥ 2431.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9aca67c5].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | greenfield | salt-diet | statement | f5f66c47 | 18.5380 | 2672.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f5f66c47].cost | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | 2d0c65b3 | 17.7782 | 2330.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=2d0c65b3].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=2d0c65b3].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | 746d7d4e | ≥ 19.8949 | ≥ 2089.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=746d7d4e].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=746d7d4e].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | a87b7740 | 23.1550 | 2270.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=a87b7740].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=a87b7740].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 11165871 | ≥ 16.4842 | ≥ 2752.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=11165871].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=11165871].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 3e95075c | ≥ 15.0411 | ≥ 3716.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=3e95075c].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=3e95075c].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 57a33630 | 17.3184 | 2871.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=57a33630].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=57a33630].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | FreeList | greenfield | plain | spec-change | 188f422b | ≥ 23.2072 | ≥ 3836.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=188f422b].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=188f422b].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | FreeList | greenfield | plain | spec-change | 9cb8ce96 | 35.6199 | 4740.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9cb8ce96].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=9cb8ce96].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | FreeList | greenfield | salt-diet | spec-change | f33c7e65 | 50.2241 | 5164.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f33c7e65].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=f33c7e65].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | LRU | greenfield | plain | spec-change | 3bdcbcbd | ≥ 21.1099 | ≥ 2149.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=3bdcbcbd].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=3bdcbcbd].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | LRU | greenfield | plain | spec-change | 69e8c2c4 | ≥ 23.4207 | ≥ 3053.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=69e8c2c4].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=69e8c2c4].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | 011fe22f | 23.7683 | 2450.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=011fe22f].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=011fe22f].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | b71994e3 | 19.9863 | 2511.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=b71994e3].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=b71994e3].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | d6b53ee4 | 22.3326 | 2572.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=d6b53ee4].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=d6b53ee4].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | LZW | greenfield | plain | spec-change | 93323249 | 20.1528 | 2089.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=93323249].cost + harness/systems-v3/RESULT-specchange-1-verdicts-2026-09-10.tsv [cell=93323249].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-1 (ADDENDUM 3) |
| claude-opus-5 | LZW | greenfield | plain | spec-change | 22ee7d33 | 27.3946 | 2872.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=22ee7d33].cost + harness/systems-v3/RESULT-specchange-1-verdicts-2026-09-10.tsv [cell=22ee7d33].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-1 (ADDENDUM 3) |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 7ac56e4e | 34.8378 | 4620.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=7ac56e4e].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=7ac56e4e].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 18fb3eed | 48.9775 | 5103.0 | - | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=18fb3eed].cost + harness/systems-v3/RESULT-specchange-1-verdicts-2026-09-10.tsv [cell=18fb3eed].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-1 (ADDENDUM 3) |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 6d58f1ec | ≥ 41.2416 | ≥ 4801.0 | CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=6d58f1ec].cost + harness/systems-v3/RESULT-specchange-1-verdicts-2026-09-10.tsv [cell=6d58f1ec].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-1 (ADDENDUM 3) |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | 60a056e6 | ≥ 24.0243 | ≥ 4680.0 | FLOOR | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=60a056e6].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=60a056e6].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | f6462d47 | ≥ 36.5631 | ≥ 4560.0 | FLOOR+CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=f6462d47].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=f6462d47].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | 9e6c8d4d | ≥ 56.2679 | ≥ 6429.0 | CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=9e6c8d4d].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=9e6c8d4d].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | b22d1000 | ≥ 43.0766 | ≥ 5645.0 | CAP-COST | harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv [root=cells-matrix1,cell=b22d1000].cost + harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=b22d1000].cost_usd | claude-wall-raw-allroots.tsv, the copy at cells-specchange-2 (ADDENDUM 3) |
| claude-opus-5 | Crc32 | brownfield | plain | none | clbocp01 | 6.6224 | 985.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | plain | none | clbocp02 | 6.7005 | 804.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | plain | none | clbocp03 | 9.0653 | 804.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | salt-diet | none | clbocs01 | 8.4311 | 1407.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | salt-diet | none | clbocs02 | 7.6199 | 1227.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | salt-diet | none | clbocs03 | 6.5096 | 925.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | plain | none | clbofp01 | 20.9870 | 1890.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | plain | none | clbofp02 | ≥ 14.7874 | 2312.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | plain | none | clbofp03 | ≥ 18.6555 | 1408.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | salt-diet | none | clbofs01 | ≥ 35.3441 | 4726.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | salt-diet | none | clbofs02 | ≥ 37.5792 | ≥ 4848.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | salt-diet | none | clbofs03 | ≥ 37.3049 | 5632.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | plain | none | clbolp01 | 7.1139 | 1166.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbolp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | plain | none | clbolp02 | 8.1666 | 985.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbolp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | plain | none | clbolp03 | 8.3049 | 1106.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbolp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | salt-diet | none | clbols01 | 19.0664 | 2252.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbols01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | salt-diet | none | clbols02 | 9.5249 | 1287.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbols02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | salt-diet | none | clbols03 | 15.0337 | 1769.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbols03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | brownfield | plain | none | clbopp01 | 15.8614 | 2674.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbopp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | brownfield | plain | none | clbopp02 | 12.8456 | 4665.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbopp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | brownfield | plain | none | clbopp03 | 13.1354 | 2373.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbopp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | brownfield | salt-diet | none | clbops01 | 32.2214 | 3277.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbops01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | brownfield | salt-diet | none | clbops02 | 30.3463 | 2915.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbops02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Paxos | brownfield | salt-diet | none | clbops03 | 36.1362 | 4183.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbops03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | plain | none | clbozp01 | 10.1071 | 1226.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | plain | none | clbozp02 | ≥ 12.5415 | 1347.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | plain | none | clbozp03 | 8.0831 | 1347.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | salt-diet | none | clbozs01 | 15.9898 | 2372.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | salt-diet | none | clbozs02 | 23.2002 | 2855.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | salt-diet | none | clbozs03 | 14.8291 | 2856.0 | - | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | plain | statement | clbtcp01 | ≥ 9.6926 | 1407.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | plain | statement | clbtcp02 | 8.3509 | 743.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | plain | statement | clbtcp03 | 9.8684 | 1106.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | salt-diet | statement | clbtcs01 | ≥ 7.0576 | 1529.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | salt-diet | statement | clbtcs02 | 7.2653 | 985.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | Crc32 | brownfield | salt-diet | statement | clbtcs03 | 6.5712 | 925.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | plain | statement | clbtfp01 | ≥ 23.0588 | 1770.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | plain | statement | clbtfp02 | ≥ 19.5729 | 2373.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | plain | statement | clbtfp03 | 14.9115 | 2252.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | salt-diet | statement | clbtfs01 | 36.2217 | 3338.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | salt-diet | statement | clbtfs02 | 29.6196 | 3701.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | FreeList | brownfield | salt-diet | statement | clbtfs03 | ≥ 27.8217 | 3278.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | plain | statement | clbtlp01 | 10.3596 | 1408.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtlp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | plain | statement | clbtlp02 | 10.6956 | 1045.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtlp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | plain | statement | clbtlp03 | 8.0443 | 985.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtlp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | salt-diet | statement | clbtls01 | ≥ 15.0002 | 2010.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtls01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | salt-diet | statement | clbtls02 | 14.1448 | 1589.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtls02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LRU | brownfield | salt-diet | statement | clbtls03 | 14.5941 | 1649.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtls03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | plain | statement | clbtzp01 | 16.5588 | 1769.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | plain | statement | clbtzp02 | ≥ 13.4688 | 1649.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | plain | statement | clbtzp03 | ≥ 10.4423 | 1769.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | salt-diet | statement | clbtzs01 | 17.8990 | 2131.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | salt-diet | statement | clbtzs02 | 13.9543 | 1649.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-opus-5 | LZW | brownfield | salt-diet | statement | clbtzs03 | 23.3102 | 2313.0 | - | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | plain | none | clbgcp01 | 1.1441 | 382.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | plain | none | clbgcp02 | 1.1857 | 321.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | plain | none | clbgcp03 | 0.9107 | 261.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | none | clbgcs01 | 4.7903 | 1467.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | none | clbgcs02 | 4.4955 | 1106.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | none | clbgcs03 | 5.0968 | 1347.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | plain | none | clbgfp01 | 2.9173 | 1347.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | plain | none | clbgfp02 | 1.8239 | 804.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | plain | none | clbgfp03 | 4.0542 | 1890.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | clbgfs01 | ≥ 37.7207 | ≥ 5632.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | clbgfs02 | ≥ 37.6969 | ≥ 8710.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | clbgfs03 | ≥ 37.9785 | ≥ 7864.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | plain | none | clbglp02 | 1.5657 | 503.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbglp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | plain | none | clbglp03 | ≥ 0.8940 | 201.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbglp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | salt-diet | none | clbgls01 | ≥ 5.7545 | 1769.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgls01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | salt-diet | none | clbgls02 | 4.6801 | 1347.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgls02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | salt-diet | none | clbgls03 | 10.2738 | 2132.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgls03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | greenfield | plain | none | clbgpp01 | 3.3769 | 1468.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgpp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | greenfield | plain | none | clbgpp02 | 3.3142 | 1468.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgpp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | greenfield | plain | none | clbgpp03 | 3.6489 | 1769.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgpp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | none | clbgps01 | ≥ 37.8011 | ≥ 6839.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | none | clbgps02 | ≥ 37.6062 | ≥ 6476.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | none | clbgps03 | 25.8810 | 4123.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | plain | none | clbgzp01 | 1.7755 | 502.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | plain | none | clbgzp02 | 1.6974 | 623.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | plain | none | clbgzp03 | 1.4864 | 623.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | salt-diet | none | clbgzs01 | ≥ 15.8936 | 4002.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | salt-diet | none | clbgzs02 | 14.3901 | 4062.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | salt-diet | none | clbgzs03 | 12.8070 | 2554.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | plain | statement | clbscp01 | 1.1939 | 261.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | plain | statement | clbscp02 | 0.9779 | 261.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | plain | statement | clbscp03 | 0.8430 | 200.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | statement | clbscs01 | 3.7965 | 925.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | statement | clbscs02 | 4.1607 | 1045.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | statement | clbscs03 | 5.5165 | 1528.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | plain | statement | clbsfp01 | 2.7284 | 1045.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | plain | statement | clbsfp02 | 3.3273 | 1227.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | plain | statement | clbsfp03 | 2.8059 | 985.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | statement | clbsfs01 | ≥ 35.0810 | 7382.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | statement | clbsfs02 | ≥ 37.4618 | ≥ 9976.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | statement | clbsfs03 | 23.3558 | 5872.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | plain | statement | clbslp01 | 1.3835 | 382.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbslp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | plain | statement | clbslp02 | 1.5949 | 382.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbslp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | plain | statement | clbslp03 | 0.8539 | 201.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbslp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | salt-diet | statement | clbsls01 | ≥ 4.8285 | 1226.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsls01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | salt-diet | statement | clbsls02 | 7.2774 | 2072.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsls02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | greenfield | salt-diet | statement | clbsls03 | 6.6651 | 1709.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsls03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | plain | statement | clbszp01 | 1.8862 | 744.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | plain | statement | clbszp02 | 1.7492 | 744.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | plain | statement | clbszp03 | 2.2932 | 865.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | clbszs01 | 10.4782 | 2433.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | clbszs02 | ≥ 37.3123 | ≥ 5210.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | clbszs03 | ≥ 12.3552 | 4062.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | plain | statement | clbucp01 | 0.9366 | 201.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | plain | statement | clbucp02 | 1.0121 | 382.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | plain | statement | clbucp03 | 1.5639 | 382.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | statement | clbucs01 | 3.9395 | 1287.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | statement | clbucs02 | 3.3458 | 1166.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | statement | clbucs03 | 4.3831 | 1166.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | plain | statement | clbufp01 | 2.3408 | 864.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | plain | statement | clbufp02 | 2.9368 | 925.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | plain | statement | clbufp03 | 2.2493 | 925.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | clbufs01 | ≥ 38.5807 | ≥ 6356.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | clbufs02 | ≥ 37.4583 | ≥ 7986.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | clbufs03 | ≥ 37.5983 | ≥ 7623.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | plain | statement | clbulp01 | 1.0875 | 322.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbulp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | plain | statement | clbulp02 | 1.1020 | 321.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbulp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | plain | statement | clbulp03 | 0.9325 | 201.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbulp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | salt-diet | statement | clbuls01 | 4.0008 | 1287.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuls01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | salt-diet | statement | clbuls02 | ≥ 5.2670 | 1528.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuls02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | salt-diet | statement | clbuls03 | 5.5829 | 1588.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuls03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | plain | statement | clbuzp01 | 1.7949 | 562.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | plain | statement | clbuzp02 | 2.2099 | 1045.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | plain | statement | clbuzp03 | 1.5196 | 562.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | salt-diet | statement | clbuzs01 | 8.9140 | 2313.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | salt-diet | statement | clbuzs02 | ≥ 21.4795 | 5209.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | salt-diet | statement | clbuzs03 | ≥ 18.1427 | 4122.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | clbbcp01 | ≥ 0.9014 | 261.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | clbbcp02 | 0.5513 | 141.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | clbbcp03 | 0.9124 | 262.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | clbbcs01 | 4.1133 | 1227.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | clbbcs02 | 5.7492 | 1407.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | clbbcs03 | 3.5780 | 1407.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | plain | none | clbbfp01 | 4.7537 | 1709.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | plain | none | clbbfp02 | 1.5851 | 563.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | plain | none | clbbfp03 | 2.4125 | 684.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | clbbfs01 | ≥ 37.8501 | ≥ 5933.0 | CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | clbbfs02 | 28.9152 | 6657.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | clbbfs03 | ≥ 37.4300 | ≥ 8287.0 | CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | plain | none | clbblp01 | 0.9246 | 140.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbblp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | plain | none | clbblp02 | 0.9443 | 262.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbblp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | plain | none | clbblp03 | 1.0246 | 261.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbblp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | clbbls01 | 6.4961 | 2192.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbls01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | clbbls02 | 7.7427 | 1649.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbls02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | clbbls03 | 9.0527 | 2071.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbls03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | brownfield | plain | none | clbbpp01 | ≥ 3.0502 | 1227.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbpp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | brownfield | plain | none | clbbpp02 | 3.4601 | 1649.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbpp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | brownfield | plain | none | clbbpp03 | 2.8717 | 864.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbpp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | clbbps01 | ≥ 28.3143 | 5632.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | clbbps02 | ≥ 37.9576 | ≥ 5511.0 | CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | clbbps03 | ≥ 37.9185 | ≥ 6115.0 | CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | plain | none | clbbzp01 | 1.5162 | 442.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzp01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | plain | none | clbbzp02 | ≥ 2.1726 | 683.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzp02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | plain | none | clbbzp03 | 1.0126 | 261.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzp03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | clbbzs01 | ≥ 19.2957 | 4847.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzs01].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | clbbzs02 | ≥ 20.5363 | 4847.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzs02].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | clbbzs03 | 14.1849 | 3278.0 | - | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzs03].final_COST | claude-wall-raw.tsv phases 1 |
| claude-sonnet-5 | Crc32 | greenfield | plain | spec-change | clbccp01 | ≥ 2.4900 | 582.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp01].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp01].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | Crc32 | greenfield | plain | spec-change | clbccp02 | 2.0300 | 462.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp02].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp02].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | Crc32 | greenfield | plain | spec-change | clbccp03 | ≥ 1.8600 | 522.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp03].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp03].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | spec-change | clbccs01 | 10.9500 | 3358.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs01].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs01].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | spec-change | clbccs02 | ≥ 9.1500 | 2333.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs02].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs02].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | spec-change | clbccs03 | 7.5700 | 2031.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs03].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs03].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | FreeList | greenfield | plain | spec-change | clbcfp01 | 4.7800 | 1669.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp01].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp01].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | FreeList | greenfield | plain | spec-change | clbcfp02 | 6.6600 | 2212.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp02].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp02].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | FreeList | greenfield | plain | spec-change | clbcfp03 | ≥ 6.9300 | 4263.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp03].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp03].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LRU | greenfield | plain | spec-change | clbclp01 | 2.3000 | 582.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp01].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp01].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LRU | greenfield | plain | spec-change | clbclp02 | 1.5000 | 521.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp02].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp02].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LRU | greenfield | plain | spec-change | clbclp03 | 1.5300 | 342.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp03].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp03].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LRU | greenfield | salt-diet | spec-change | clbcls01 | 10.2900 | 2996.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls01].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls01].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LRU | greenfield | salt-diet | spec-change | clbcls02 | 6.7600 | 1910.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls02].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls02].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LRU | greenfield | salt-diet | spec-change | clbcls03 | 14.4400 | 4505.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls03].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls03].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | Paxos | greenfield | plain | spec-change | clbcpp01 | ≥ 9.9200 | 5349.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp01].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp01].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | Paxos | greenfield | plain | spec-change | clbcpp02 | ≥ 7.1300 | 2695.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp02].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp02].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | Paxos | greenfield | plain | spec-change | clbcpp03 | 11.5400 | 4082.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp03].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp03].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LZW | greenfield | plain | spec-change | clbczp01 | 5.2800 | 1789.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp01].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp01].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LZW | greenfield | plain | spec-change | clbczp02 | 5.0300 | 1789.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp02].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp02].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LZW | greenfield | plain | spec-change | clbczp03 | ≥ 4.0800 | 1307.0 | - | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp03].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp03].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LZW | greenfield | salt-diet | spec-change | clbczs01 | ≥ 24.0300 | ≥ 4143.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs01].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs01].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LZW | greenfield | salt-diet | spec-change | clbczs02 | ≥ 21.7300 | ≥ 7401.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs02].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs02].p2_COST | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | LZW | greenfield | salt-diet | spec-change | clbczs03 | ≥ 18.6000 | ≥ 4625.0 | CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs03].p1_COST + evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczs03].p2_COST -> the cap 18.60 entered (A1.3) | claude-wall-raw.tsv phases 1,2 |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | spec-change | clbcfs01 | ≥ 37.6942 | unmeasured | CAP-COST | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) | unmeasured: phase 2 not in this root and 0 copy root(s) pass the copy check |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | spec-change | clbcfs02 | ≥ 37.4995 | unmeasured | CAP-COST | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) | unmeasured: phase 2 not in this root and 0 copy root(s) pass the copy check |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | spec-change | clbcfs03 | ≥ 37.2789 | unmeasured | CAP-COST | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) | unmeasured: phase 2 not in this root and 0 copy root(s) pass the copy check |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | spec-change | clbcps01 | ≥ 37.6169 | unmeasured | CAP-COST | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) | unmeasured: phase 2 not in this root and 0 copy root(s) pass the copy check |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | spec-change | clbcps02 | ≥ 37.4009 | unmeasured | CAP-COST | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) | unmeasured: phase 2 not in this root and 0 copy root(s) pass the copy check |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | spec-change | clbcps03 | ≥ 37.3077 | unmeasured | CAP-COST | claude-cost-raw.tsv (cell_meter re-run; no tracked source row) | unmeasured: phase 2 not in this root and 0 copy root(s) pass the copy check |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | s3cp01 | 0.6889 | 575.7 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | s3cp02 | 0.5450 | 217.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | s3cp03 | 0.6497 | 269.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | s3cs01 | 5.3547 | 1595.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | s3cs02 | 6.2464 | 1721.7 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | s3cs03 | 4.9188 | 1308.4 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | s3lp01 | 0.9811 | 343.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | s3lp02 | 1.2061 | 677.7 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | s3lp03 | 1.4490 | 612.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | s3ls01 | ≥ 7.0197 | ≥ 2578.5 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | s3ls02 | 2.5509 | 670.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | s3ls03 | 4.4192 | 1317.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | greenfield | plain | none | s3fp01 | 0.8347 | 331.7 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | s3fs01 | 4.9121 | 1966.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | s3fs02 | 3.4557 | 2188.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | s3fs03 | 6.6847 | 3172.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | s3pp01 | 0.6892 | 214.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | s3pp02 | 0.6943 | 211.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | s3pp03 | 1.2920 | 417.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | s3ps01 | 3.5283 | 831.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | s3ps02 | ≥ 6.8380 | ≥ 3576.9 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | s3ps03 | ≥ 9.0688 | ≥ 3582.2 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | s3cq01 | 0.6763 | 202.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | s3cq02 | 0.8186 | 217.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | s3cq03 | 0.7993 | 229.4 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | statement | s3ct01 | ≥ 8.3277 | ≥ 1950.3 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | statement | s3ct02 | 4.4231 | 1289.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | s3lq01 | 0.7159 | 241.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | s3lq02 | 0.6806 | 201.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | s3lq03 | 0.8048 | 228.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | s3lt01 | 4.5779 | 988.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | s3lt02 | ≥ 5.7716 | ≥ 2110.9 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | s3lt03 | 3.3126 | 967.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | s3fq01 | 0.9475 | 348.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | s3fq02 | 0.9380 | 291.4 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | s3ft01 | 9.2301 | 2508.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | s3ft02 | unmeasured | ≥ 5539.4 | DEADLINE | agy-steps-raw.tsv: p1 a tiered price and PARTIAL per-request records | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | s3ft03 | ≥ 4.8531 | ≥ 3597.6 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | plain | none | b4lrp01 | 0.4315 | 160.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | plain | none | b4lrp02 | 0.5426 | 181.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | plain | none | b4lrp03 | 0.6925 | 242.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | none | b4lrs01 | 0.8999 | 351.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | none | b4lrs02 | 2.3541 | 1215.7 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | none | b4lrs03 | 2.8122 | 1886.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | brownfield | plain | none | b4pp01 | 0.9545 | 355.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | brownfield | plain | none | b4pp02 | 0.9273 | 364.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | brownfield | plain | none | b4pp03 | 1.0529 | 487.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | brownfield | salt-diet | none | b4ps01 | 6.6018 | 2812.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | brownfield | salt-diet | none | b4ps02 | 3.8251 | 2567.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Paxos | brownfield | salt-diet | none | b4ps03 | ≥ 6.5788 | ≥ 4426.4 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | none | l5cp01 | 0.8235 | 280.9 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | none | l5cp02 | 0.6569 | 205.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | none | l5cp03 | 1.0601 | 313.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | none | l5cs01 | 1.9051 | 483.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | none | l5cs02 | 2.1520 | 516.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | none | l5cs03 | 2.4040 | 2092.8 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | plain | none | l5fp01 | 1.0820 | 374.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | plain | none | l5fp02 | 1.3501 | 415.2 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | plain | none | l5fp03 | 1.1784 | 352.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | none | l5fs01 | 2.2155 | 611.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | none | l5fs02 | 9.7424 | 5112.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | none | l5fs03 | 3.4829 | 985.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | plain | none | l5lp01 | 1.1911 | 394.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | plain | none | l5lp02 | 1.1695 | 401.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | plain | none | l5lp03 | 0.7321 | 273.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | l5lsra301 | 2.7819 | 1130.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | l5lsra302 | 2.9685 | 863.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | l5lsra303 | 2.5514 | 581.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | l5ppr01 | 0.9452 | 345.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | l5ppr02 | 1.2949 | 413.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | l5ppr03 | 1.4112 | 384.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | l5psra201 | 4.5720 | 1207.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | l5psra202 | ≥ 11.2678 | ≥ 2863.0 | DEADLINE | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | l5psra203 | 3.2491 | 713.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | l5cq01 | 0.7971 | 259.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | l5cq02 | 0.6997 | 229.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | l5cq03 | 0.9299 | 242.2 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | l5ct01 | 2.6636 | 612.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | l5ct02 | 2.9531 | 789.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | l5ct03 | 3.4254 | 766.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | l5fq01 | 1.0290 | 332.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | l5fq02 | 1.0187 | 336.9 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | l5fq03 | 1.2705 | 430.2 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | l5ft01 | 3.5944 | 771.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | l5ft02 | 5.8988 | 1426.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | l5ft03 | 2.3894 | 669.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | l5lq01 | 0.6971 | 375.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | l5lq02 | 1.0640 | 374.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | l5lq03 | 0.7196 | 331.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | l5lt01 | 2.6080 | 1038.2 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | l5lt02 | 2.9971 | 912.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | l5lt03 | 2.3536 | 798.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | plain | none | l6vgpp01 | 0.7262 | 217.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | plain | none | l6vgpp02 | 0.6857 | 199.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | plain | none | l6vgpp03 | 0.7330 | 231.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | none | l6vgps01 | 2.6506 | 3805.5 | - | agy-steps-raw.tsv: p1 per request, tiered (EXCEEDS-METER) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | none | l6vgps02 | 8.5345 | 5522.7 | - | agy-steps-raw.tsv: p1 per request, tiered (EXCEEDS-METER) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | none | l6vgps03 | 5.2674 | 1787.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | plain | statement | l6uspq01 | 0.5844 | 170.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | plain | statement | l6vspb01 | 0.8400 | 235.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | plain | statement | l6vspb02 | 0.8772 | 235.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | statement | l6vspt01 | ≥ 7.3558 | ≥ 3943.4 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | statement | l6vspt02 | 3.4662 | 872.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | statement | l6vspt03 | 7.2924 | 2043.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | plain | none | l6vgfp01 | 0.9504 | 310.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | plain | none | l6vgfp02 | 0.8715 | 295.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | plain | none | l6vgfp03 | 0.8904 | 308.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | none | l6vgfs01 | 3.8140 | 833.8 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | none | l6vgfs02 | ≥ 0.1097 | ≥ 21723.8 | DEADLINE | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | none | l6vgfs03 | 5.4756 | 1155.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | plain | statement | l6vsfq01 | 1.0131 | 335.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | plain | statement | l6vsfq02 | 1.1199 | 338.8 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | plain | statement | l6vsfq03 | 1.2745 | 358.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | statement | l6vsft01 | 2.2038 | 604.8 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | statement | l6vsft02 | 3.9111 | 892.9 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | statement | l6vsft03 | 3.0830 | 739.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | plain | none | l6vblp01 | 0.9359 | 299.2 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | plain | none | l6vblp02 | 0.7041 | 265.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | plain | none | l6vblp03 | 0.7686 | 303.2 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | none | l6vbls01 | 2.6963 | 790.6 | - | agy-steps-raw.tsv: p1 per request (EXCEEDS-METER) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | none | l6vbls02 | 2.6862 | 572.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | none | l6vbls03 | 2.3840 | 656.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | brownfield | plain | none | l6vbpp01 | 1.4515 | 413.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | brownfield | plain | none | l6vbpp02 | 1.3184 | 461.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | brownfield | plain | none | l6vbpp03 | 1.1044 | 390.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | brownfield | salt-diet | none | l6vbps01 | 2.4338 | 595.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | brownfield | salt-diet | none | l6vbps02 | 3.3301 | 662.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Paxos | brownfield | salt-diet | none | l6vbps03 | 4.0515 | 1026.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | none | l7cfbp01 | 0.7765 | 266.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | none | l7cfbp02 | 0.7879 | 242.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | none | l7cfbp03 | 0.7203 | 261.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | none | l7cfbs01 | 1.3540 | 356.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | none | l7cfbs02 | 1.6292 | 408.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | none | l7cfbs03 | 2.0562 | 2095.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | statement | l7cfsp01 | 0.9284 | 235.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | statement | l7cfsp02 | 0.8195 | 216.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | statement | l7cfsp03 | 0.8644 | 258.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | statement | l7cfss01 | 2.2879 | 494.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | statement | l7cfssq01 | 2.2098 | 1059.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | statement | l7cfssq02 | 1.4598 | 899.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | none | l7cpbp01 | 0.6664 | 197.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | none | l7cpbp02 | 0.7635 | 256.4 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | none | l7cpbp03 | 0.4600 | 158.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | l7cpbs01 | 4.4718 | 1296.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | l7cpbs02 | 3.0280 | 1020.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | l7cpbs03 | unmeasured | 3723.5 | - | agy-steps-raw.tsv: p1 a tiered price and PARTIAL per-request records | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | statement | l7cpsp01 | 0.8037 | 182.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | statement | l7cpsp02 | 0.5887 | 159.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | statement | l7cpsp03 | 0.8677 | 239.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | statement | l7cpssa201 | 3.6424 | 1084.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | statement | l7cpssa202 | 4.3040 | 1197.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | statement | l7cpssa203 | 1.3391 | 883.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | plain | none | l7nffp01 | 1.0701 | 553.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | plain | none | l7nffp02 | 0.8715 | 350.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | plain | none | l7nffp03 | 0.9172 | 647.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | none | l7nffs01 | 3.3226 | 989.9 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | none | l7nffs02 | 3.2561 | 906.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | none | l7nffs03 | 2.2111 | 688.9 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | plain | none | l7nfzp01 | 1.3152 | 486.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | plain | none | l7nfzp02 | 1.2240 | 494.8 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | plain | none | l7nfzp03 | 1.2524 | 403.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | none | l7nfzs01 | 2.7652 | 854.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | none | l7nfzs02 | 3.0395 | 1007.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | none | l7nfzs03 | 2.4100 | 966.2 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | plain | none | l7npfp01 | 0.7789 | 232.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | plain | none | l7npfp02 | 1.4497 | 461.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | plain | none | l7npfp03 | 1.0327 | 313.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | none | l7npfs01 | 6.8265 | 4381.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | none | l7npfs02 | 4.9329 | 1337.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | none | l7npfs03 | 8.7307 | 8249.3 | - | agy-steps-raw.tsv: p1 per request, tiered (EXCEEDS-METER) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | plain | none | l7npzp01 | 0.8594 | 242.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | plain | none | l7npzp02 | 0.7279 | 195.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | plain | none | l7npzp03 | 0.9601 | 242.4 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | none | l7npzs01 | ≥ 10.3133 | ≥ 4716.6 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | none | l7npzs02 | 13.8109 | 5817.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | none | l7npzs03 | ≥ 23.8616 | ≥ 9165.1 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (EXCEEDS-METER) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | plain | statement | l7sffp01 | 1.3302 | 341.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | plain | statement | l7sffp02 | 1.6026 | 430.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | plain | statement | l7sffp03 | 1.4166 | 469.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | statement | l7sffs01 | 4.7158 | 1155.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | statement | l7sffs02 | 1.7648 | 577.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | statement | l7sffs03 | 2.9311 | 676.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | plain | statement | l7sfrp01 | 0.8604 | 277.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | plain | statement | l7sfrp02 | 0.6894 | 285.8 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | plain | statement | l7sfrp03 | 0.7906 | 385.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | statement | l7sfrs01 | 1.5815 | 922.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | statement | l7sfrs02 | 3.4810 | 841.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | statement | l7sfrs03 | 2.3327 | 816.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | plain | statement | l7sfzp01 | 1.1346 | 398.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | plain | statement | l7sfzp02 | 0.9130 | 386.9 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | plain | statement | l7sfzp03 | 0.9303 | 411.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | statement | l7sfzs01 | 1.9071 | 807.2 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | statement | l7sfzs02 | 2.6632 | 864.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | statement | l7sfzs03 | 1.6512 | 665.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | statement | l7spfb01 | 3.4430 | 891.7 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | statement | l7spfb02 | ≥ 11.0195 | ≥ 2458.4 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | statement | l7spfwa201 | 6.0646 | 2900.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | plain | statement | l7spfp01 | 0.6500 | 197.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | plain | statement | l7spfp02 | 0.9218 | 268.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | FreeList | brownfield | plain | statement | l7spfp03 | 1.2901 | 357.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | plain | statement | l7sprp01 | 0.7611 | 216.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | plain | statement | l7sprp02 | 0.6320 | 177.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | plain | statement | l7sprp03 | 0.8032 | 207.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | statement | l7sprs01 | 4.8645 | 1540.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | statement | l7sprs02 | ≥ 4.9699 | ≥ 1994.2 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | statement | l7sprs03 | ≥ 10.3955 | ≥ 2003.8 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | plain | statement | l7spzp01 | 0.8578 | 193.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | plain | statement | l7spzp02 | 0.8443 | 218.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | plain | statement | l7spzp03 | 0.8667 | 198.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | statement | l7spzs01 | 8.1062 | 8224.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | statement | l7spzs02 | 4.8014 | 3080.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | statement | l7spzs03 | ≥ 7.3882 | ≥ 4375.1 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | spec-change | l8cfps01 | 1.6668 | 1070.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | spec-change | l8cfps02 | 1.6064 | 912.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | spec-change | l8cfps03 | 1.2988 | 571.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | spec-change | l8cfss01 | 2.8525 | 1166.8 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | spec-change | l8cfss02 | 2.8922 | 1329.8 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | spec-change | l8cfss03 | 3.8557 | 1587.9 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | spec-change | l8cpps01 | 1.2904 | 389.4 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | spec-change | l8cpps02 | 1.4574 | 409.7 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | spec-change | l8cpps03 | 1.2600 | 374.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | l8cpss01 | 6.0118 | 4863.3 | - | agy-steps-raw.tsv: p1 per request, tiered (EXCEEDS-METER); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | l8cpss02 | 7.1782 | 1673.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | l8cpss03 | 5.7504 | 6099.2 | - | agy-steps-raw.tsv: p1 per request, tiered (EXCEEDS-METER); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | l8rfpb01 | 1.7704 | 717.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | l8rfpb02 | 1.5730 | 733.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | l8rfwra201 | 1.4835 | 626.9 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 no phase_facts record |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | spec-change | l8rfss01 | 4.0021 | 1829.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | spec-change | l8rfss02 | 3.3339 | 1636.8 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | spec-change | l8rfss03 | 3.5484 | 1768.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LRU | greenfield | plain | spec-change | l8rppr01 | 1.4270 | 400.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LRU | greenfield | plain | spec-change | l8rppr02 | 1.1100 | 376.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LRU | greenfield | plain | spec-change | l8rppr03 | 1.4554 | 406.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | spec-change | l8rpsra201 | 6.7460 | 1825.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | spec-change | l8rpsra202 | 6.1936 | 2277.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | spec-change | l8rpsra203 | 5.7615 | 1960.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-a9-probe-cap-2026-09-24/phase_facts.json, p1 = evidence/l8-chainD-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | l8xppr01 | 1.8030 | 560.4 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | l8xppr02 | 1.7001 | 535.4 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | l8xppr03 | 1.9773 | 642.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | l8xpsr01 | ≥ 5.6557 | ≥ 3031.6 | DEADLINE | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (EXCEEDS-METER) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | l8xpsr02 | 7.2933 | 3328.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | l8xpsr03 | 9.0239 | 3207.2 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | l8ffpr01 | 2.2091 | 812.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | l8ffpr02 | 2.2015 | 808.0 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | l8ffpr03 | 2.1289 | 808.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | l8ffsra201 | 7.4946 | 2748.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | l8ffsra202 | 3.7932 | 1452.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | l8ffsra203 | 4.1487 | 1653.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | l8fppr01 | 2.2188 | 681.7 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | l8fppr02 | 1.9648 | 591.5 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | l8fppr03 | 1.7154 | 519.9 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr01 | 5.4851 | 1618.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr02 | unmeasured | 5426.8 | - | agy-steps-raw.tsv: p1 a tiered price and PARTIAL per-request records; p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr03 | 8.3521 | 4089.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | l8zfpra201 | 1.6407 | 793.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | l8zfpra202 | 1.6656 | 746.3 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | l8zfpra203 | 2.2641 | 989.7 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | l8zfsr01 | 4.9666 | 2072.1 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | l8zfsr02 | 4.3602 | 1922.8 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | l8zfsr03 | 5.2198 | 2268.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | l8zppr01 | 1.4734 | 452.1 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | l8zppr02 | 1.6897 | 546.7 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | l8zppr03 | 1.6484 | 512.3 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | l8zpsr01 | 14.7978 | 5025.0 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | l8zpsr02 | 5.4037 | 1968.6 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | l8zpsr03 | 10.7301 | 4676.8 | - | agy-steps-raw.tsv: p1 per request, tiered (COMPLETE); p2 per request, tiered (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | l8xfp2a201 | 2.2848 | 998.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | l8xfp2a202 | 2.5691 | 1064.4 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | l8xfp2a203 | 2.1888 | 1108.2 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | l8xfs201 | 16.1554 | 11401.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | l8xfs202 | 14.0587 | 5512.6 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | l8xfs203 | 21.6983 | 8482.5 | - | agy-steps-raw.tsv: p1 per request (COMPLETE); p2 per request (COMPLETE) | agy-steps-raw.tsv wall_s; second method: p1 = evidence/l8-chainF-2026-09-24/phase_facts.json |
