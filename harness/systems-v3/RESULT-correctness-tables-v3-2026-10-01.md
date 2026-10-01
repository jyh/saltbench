# RESULT: CORRECTNESS OVER THE COMPLETE PILOT MATRIX (arXiv v3), DECLARED POST HOC
## Printed by `harness/systems-v3/tables_correctness_v3.py` over the working tree at repo head `c4ad5bacec4c`, from `harness/systems-v3/CELLMAP-correctness-tables-v3-2026-10-01.tsv`. Registered in `REGISTRATION-correctness-tables-v3-2026-10-01.md` (§P1–§P6, ADDENDA 1–3; ADDENDA 1–2 merged and ADDENDUM 3 committed (`7da02bb`) before this ran, in the same PR as this file). The instrument and its map are named by CONTENT (git blob ids, checkable with `git hash-object <file>`): `tables_correctness_v3.py` 864a0a782dfb · `CELLMAP-correctness-tables-v3-2026-10-01.tsv` 1a39b0678d7d.

**CHECK conditions with a k/n 181 + — 16 + declared 3 + unmeasured 0 = 200 (other 0) against 181 + 16 + 3 = 200**
**Cells: PASS 447 · FAIL 40 · CENSORED 10 · UNSCORABLE 4 · by condition 42.**
**Second method (§P5): 94 printed count(s) compared, 19 disagreement(s); 51 of the 181 DONE conditions have at least one printed count that agrees, 8 have a printed count and none agrees, 122 have no printed count.**
**Every disagreement's cause, verified by the instrument: REPRODUCED over another population 18 · SUPERSEDED 1; with NO verified cause: 0.**

⛔ **A descriptive reading, declared post hoc (§P6): no test, no p-value, no verdict on the arms; the registered tests remain §4's.** n = 3 per condition, so a rate moves in thirds. A PASS is the withheld suite's verdict and is bounded by that suite's strength (mutant scores are ceilings, not strengths). The agy and Claude lanes have different scorers of record; a row compares arms within one model and one problem.

- **k / n** full passes over n = PASS + FAIL. **(+c censored)** cells that halted at a registered budget without a pass on the record; **(+u unscorable)** cells the suite gave no verdict on. Neither enters k or n. **`n = 0`** every cell censored or unscorable (ADDENDUM 2). **`†`** the record prints only the condition's count, read under ADDENDUM 3d. **`—`** inexpressible. **`declared`** unreached at the cap.
- **Signs** (§P4, ADDENDUM 1): each arm's interval [k/(n+c+u), (k+c+u)/(n+c+u)]; `+` / `−` only when the intervals are strictly apart, `=` only when both are the same single point, otherwise `?`. Censoring cannot make a sign, and every `?` has a censored or unscorable cell on at least one side (counted below by arm).
- **The map** is v2's cell map plus `verdict_source` and `verdict_why`, plus the twelve cells census ADDENDA 30–32 made cells of record after v2's map was cut (ADDENDUM 3e), plus one `CONDITION` row per ADDENDUM 3d condition and the `COUNT` rows of the second method. The pointers were authored by the lead, and by three extraction passes it commissioned, all read-only. The instrument re-reads every cited line on every run, so a pointer that does not hold prints `unmeasured`.
- **The second method's disagreements are listed, never resolved** (ADDENDUM 3). Each row carries its source's own description of the population it counts: a landed-only reading, one wave's share of a condition, a figure an addendum superseded, the first-run cells a re-fire replaced.


## P1 · greenfield — full passes k / n per condition (n = PASS + FAIL; censored and unscorable beside)

| model | problem | bare-plain | bare-salt-diet | statement-plain | statement-salt-diet |
|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-opus-5 | LRU | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-opus-5 | FreeList | 3 / 3 | 2 / 3 | 3 / 3 | 3 / 3 |
| claude-opus-5 | LZW | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-opus-5 | Paxos | 3 / 3 | 3 / 3 | — | — |
| claude-sonnet-5 | Crc32 | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-sonnet-5 | LRU | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-sonnet-5 | FreeList | 2 / 3 | 2 / 2 (+1 censored) | 3 / 3 | 2 / 2 (+1 censored) |
| claude-sonnet-5 | LZW | 3 / 3 | 3 / 3 | 3 / 3 | 2 / 2 (+1 censored) |
| claude-sonnet-5 | Paxos | 3 / 3 | 3 / 3 | — | — |
| gemini-3.1-pro-high | Crc32 | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| gemini-3.1-pro-high | LRU | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| gemini-3.1-pro-high | FreeList | 1 / 3 | 0 / 3 | 3 / 3 | 1 / 1 (+2 censored) |
| gemini-3.1-pro-high | LZW | 3 / 3 | 2 / 3 | 3 / 3 | 2 / 3 |
| gemini-3.1-pro-high | Paxos | 1 / 3 | 0 / 1 (+2 censored) | — | — |
| gemini-3.8-flash-high | Crc32 | 3 / 3 † | 3 / 3 † | 3 / 3 † | 3 / 3 † |
| gemini-3.8-flash-high | LRU | 3 / 3 † | 3 / 3 † | 3 / 3 † | 3 / 3 † |
| gemini-3.8-flash-high | FreeList | 1 / 3 † | 0 / 3 † | 3 / 3 † | 3 / 3 † |
| gemini-3.8-flash-high | LZW | 3 / 3 | 2 / 2 (+1 unscorable) | 3 / 3 | 2 / 3 |
| gemini-3.8-flash-high | Paxos | 2 / 3 † | 2 / 3 † | — | — |

## P2 · brownfield — full passes k / n per condition

| model | problem | bare-plain | bare-salt-diet | statement-plain | statement-salt-diet |
|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-opus-5 | LRU | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-opus-5 | FreeList | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-opus-5 | LZW | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-opus-5 | Paxos | 3 / 3 | 3 / 3 | — | — |
| claude-sonnet-5 | Crc32 | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-sonnet-5 | LRU | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-sonnet-5 | FreeList | 3 / 3 | 3 / 3 | 3 / 3 | 2 / 2 (+1 censored) |
| claude-sonnet-5 | LZW | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| claude-sonnet-5 | Paxos | 3 / 3 | 3 / 3 | — | — |
| gemini-3.1-pro-high | Crc32 | 3 / 3 | 2 / 2 (+1 unscorable) | 3 / 3 | 3 / 3 |
| gemini-3.1-pro-high | LRU | 3 / 3 | 2 / 3 | 3 / 3 | 2 / 3 |
| gemini-3.1-pro-high | FreeList | 3 / 3 | 1 / 3 | 2 / 3 | 1 / 3 |
| gemini-3.1-pro-high | LZW | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| gemini-3.1-pro-high | Paxos | 3 / 3 | 2 / 3 | — | — |
| gemini-3.8-flash-high | Crc32 | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| gemini-3.8-flash-high | LRU | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| gemini-3.8-flash-high | FreeList | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| gemini-3.8-flash-high | LZW | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| gemini-3.8-flash-high | Paxos | 3 / 3 | 3 / 3 | — | — |

## P3 · spec-change (greenfield only) — phase-2 full passes k / n per condition

| model | problem | plain | salt-diet |
|---|---|---|---|
| claude-opus-5 | Crc32 | 3 / 3 | 3 / 3 |
| claude-opus-5 | LRU | 3 / 3 | 3 / 3 |
| claude-opus-5 | FreeList | 3 / 3 | 2 / 3 |
| claude-opus-5 | LZW | 3 / 3 | 3 / 3 |
| claude-opus-5 | Paxos | 2 / 2 (+1 censored) | 2 / 2 (+1 unscorable) |
| claude-sonnet-5 | Crc32 | 3 / 3 | 3 / 3 |
| claude-sonnet-5 | LRU | 3 / 3 | 3 / 3 |
| claude-sonnet-5 | FreeList | 1 / 3 | declared |
| claude-sonnet-5 | LZW | 3 / 3 | declared |
| claude-sonnet-5 | Paxos | 2 / 3 | declared |
| gemini-3.1-pro-high | Crc32 | 3 / 3 | 3 / 3 |
| gemini-3.1-pro-high | LRU | 3 / 3 | 3 / 3 |
| gemini-3.1-pro-high | FreeList | 1 / 3 | 0 / 2 (+1 unscorable) |
| gemini-3.1-pro-high | LZW | 3 / 3 | 3 / 3 |
| gemini-3.1-pro-high | Paxos | 0 / 3 | 1 / 2 (+1 censored) |
| gemini-3.8-flash-high | Crc32 | 3 / 3 | 3 / 3 |
| gemini-3.8-flash-high | LRU | 3 / 3 | 3 / 3 |
| gemini-3.8-flash-high | FreeList | 2 / 3 | 0 / 3 |
| gemini-3.8-flash-high | LZW | 3 / 3 | 3 / 3 |
| gemini-3.8-flash-high | Paxos | 0 / 3 | 3 / 3 |

## P4 · signs, greenfield: salt-diet's pass-rate interval against plain's (ADDENDUM 1: STRICT)

| model | problem | bare | statement | spec-change |
|---|---|---|---|---|
| claude-opus-5 | Crc32 | = | = | = |
| claude-opus-5 | LRU | = | = | = |
| claude-opus-5 | FreeList | − | = | − |
| claude-opus-5 | LZW | = | = | = |
| claude-opus-5 | Paxos | = | — | ? |
| claude-sonnet-5 | Crc32 | = | = | = |
| claude-sonnet-5 | LRU | = | = | = |
| claude-sonnet-5 | FreeList | ? | ? | — |
| claude-sonnet-5 | LZW | = | ? | — |
| claude-sonnet-5 | Paxos | = | — | — |
| gemini-3.1-pro-high | Crc32 | = | = | = |
| gemini-3.1-pro-high | LRU | = | = | = |
| gemini-3.1-pro-high | FreeList | − | ? | ? |
| gemini-3.1-pro-high | LZW | − | − | = |
| gemini-3.1-pro-high | Paxos | ? | — | + |
| gemini-3.8-flash-high | Crc32 | = | = | = |
| gemini-3.8-flash-high | LRU | = | = | = |
| gemini-3.8-flash-high | FreeList | − | = | − |
| gemini-3.8-flash-high | LZW | ? | − | = |
| gemini-3.8-flash-high | Paxos | = | — | + |

### P4 counts, per model per treatment (no test, no p-value)

| model | treatment | + | = | − | ? | no sign (—) |
|---|---|---|---|---|---|---|
| claude-opus-5 | bare | 0 | 4 | 1 | 0 | 0 |
| claude-opus-5 | statement | 0 | 4 | 0 | 0 | 1 |
| claude-opus-5 | spec-change | 0 | 3 | 1 | 1 | 0 |
| claude-sonnet-5 | bare | 0 | 4 | 0 | 1 | 0 |
| claude-sonnet-5 | statement | 0 | 2 | 0 | 2 | 1 |
| claude-sonnet-5 | spec-change | 0 | 2 | 0 | 0 | 3 |
| gemini-3.1-pro-high | bare | 0 | 2 | 2 | 1 | 0 |
| gemini-3.1-pro-high | statement | 0 | 2 | 1 | 1 | 1 |
| gemini-3.1-pro-high | spec-change | 1 | 3 | 0 | 1 | 0 |
| gemini-3.8-flash-high | bare | 0 | 3 | 1 | 1 | 0 |
| gemini-3.8-flash-high | statement | 0 | 3 | 1 | 0 | 1 |
| gemini-3.8-flash-high | spec-change | 1 | 3 | 1 | 0 | 0 |

### Where each `?` comes from (§P6): every `?` has a censored or unscorable cell on at least one side

| treatment | censoring on salt-diet only | on plain only | on both |
|---|---|---|---|
| bare | 3 | 0 | 0 |
| statement | 3 | 0 | 0 |
| spec-change | 1 | 0 | 1 |

### Brownfield signs, by the same rule (in the file, not in P4)

| model | problem | bare | statement |
|---|---|---|---|
| claude-opus-5 | Crc32 | = | = |
| claude-opus-5 | LRU | = | = |
| claude-opus-5 | FreeList | = | = |
| claude-opus-5 | LZW | = | = |
| claude-opus-5 | Paxos | = | — |
| claude-sonnet-5 | Crc32 | = | = |
| claude-sonnet-5 | LRU | = | = |
| claude-sonnet-5 | FreeList | = | ? |
| claude-sonnet-5 | LZW | = | = |
| claude-sonnet-5 | Paxos | = | — |
| gemini-3.1-pro-high | Crc32 | ? | = |
| gemini-3.1-pro-high | LRU | − | − |
| gemini-3.1-pro-high | FreeList | − | − |
| gemini-3.1-pro-high | LZW | = | = |
| gemini-3.1-pro-high | Paxos | − | — |
| gemini-3.8-flash-high | Crc32 | = | = |
| gemini-3.8-flash-high | LRU | = | = |
| gemini-3.8-flash-high | FreeList | = | = |
| gemini-3.8-flash-high | LZW | = | = |
| gemini-3.8-flash-high | Paxos | = | — |

## Second method: every count a result of record already prints, against the instrument's k

| model | problem | field | arm | extras | printed | instrument | verdict | source |
|---|---|---|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | greenfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:34 posthoc §2 "registered reading, LANDED cells, bare arms" (reading A incl. SS12 smoke; LANDED only, CAP-COST/FAILED-BOOT excluded); plain column |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:34 posthoc §2 "registered reading, LANDED cells, bare arms" (reading A incl. SS12 smoke; LANDED only, CAP-COST/FAILED-BOOT excluded); salt-diet column |
| claude-opus-5 | FreeList | greenfield | plain | none | 4/4 | 3 / 3 | DISAGREES — cause: printed 4/4 REPRODUCED from harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [task=FreeList,arm=plain,extras=none,kind=LANDED]; in that count, not a cell of record: ae304f63; cells of record outside it: none; read differently: none | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:35 posthoc §2 "registered reading, LANDED cells, bare arms" (reading A incl. SS12 smoke; LANDED only, CAP-COST/FAILED-BOOT excluded); plain column |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | 0/1 | 2 / 3 | DISAGREES — cause: printed 0/1 REPRODUCED from harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [task=FreeList,arm=salt-diet,extras=none,kind=LANDED]; in that count, not a cell of record: none; cells of record outside it: 161b5a34 (PASS), de4de8f2 (PASS); read differently: none | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:35 posthoc §2 "registered reading, LANDED cells, bare arms" (reading A incl. SS12 smoke; LANDED only, CAP-COST/FAILED-BOOT excluded); salt-diet column |
| claude-opus-5 | LRU | greenfield | plain | none | 4/4 | 3 / 3 | DISAGREES — cause: printed 4/4 REPRODUCED from harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [task=LRU,arm=plain,extras=none,kind=LANDED]; in that count, not a cell of record: a69e9131; cells of record outside it: none; read differently: none | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:36 posthoc §2 "registered reading, LANDED cells, bare arms" (reading A incl. SS12 smoke; LANDED only, CAP-COST/FAILED-BOOT excluded); plain column |
| claude-opus-5 | LRU | greenfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:36 posthoc §2 "registered reading, LANDED cells, bare arms" (reading A incl. SS12 smoke; LANDED only, CAP-COST/FAILED-BOOT excluded); salt-diet column |
| claude-opus-5 | LZW | greenfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:37 posthoc §2 "registered reading, LANDED cells, bare arms" (reading A incl. SS12 smoke; LANDED only, CAP-COST/FAILED-BOOT excluded); plain column |
| claude-opus-5 | LZW | greenfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:37 posthoc §2 "registered reading, LANDED cells, bare arms" (reading A incl. SS12 smoke; LANDED only, CAP-COST/FAILED-BOOT excluded); salt-diet column |
| claude-opus-5 | Paxos | greenfield | plain | none | 4/4 | 3 / 3 | DISAGREES — cause: printed 4/4 REPRODUCED from harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [task=Paxos,arm=plain,extras=none,kind=LANDED]; in that count, not a cell of record: b7537006; cells of record outside it: none; read differently: none | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:38 posthoc §2 "registered reading, LANDED cells, bare arms" (reading A incl. SS12 smoke; LANDED only, CAP-COST/FAILED-BOOT excluded); plain column |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | 2/2 | 3 / 3 | DISAGREES — cause: printed 2/2 REPRODUCED from harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [task=Paxos,arm=salt-diet,extras=none,kind=LANDED]; in that count, not a cell of record: none; cells of record outside it: 6fc49f7c (PASS); read differently: none | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:38 posthoc §2 "registered reading, LANDED cells, bare arms" (reading A incl. SS12 smoke; LANDED only, CAP-COST/FAILED-BOOT excluded); salt-diet column |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | 0/1 | 2 / 3 | DISAGREES — cause: printed 0/1 REPRODUCED from harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [task=FreeList,arm=salt-diet,extras=none,kind=LANDED]; in that count, not a cell of record: none; cells of record outside it: 161b5a34 (PASS), de4de8f2 (PASS); read differently: none | harness/systems-v3/RESULT-posthoc-correctness-2026-09-09.md:55 posthoc §2 "registered reading, LANDED cells, bare arms" restated in §3 prose |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:35 RESULT-p1-specchange §3 as published (P1 wave share of the condition only) |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:35 RESULT-p1-specchange §3 as published (P1 wave share of the condition only) |
| claude-opus-5 | LRU | greenfield | plain | spec-change | 2/2 | 3 / 3 | DISAGREES — cause: printed 2/2 REPRODUCED from harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [task=LRU,arm=plain]; in that count, not a cell of record: none; cells of record outside it: clbklp01 (PASS); read differently: none | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:35 RESULT-p1-specchange §3 as published (P1 wave share of the condition only) |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:35 RESULT-p1-specchange §3 as published (P1 wave share of the condition only) |
| claude-opus-5 | FreeList | greenfield | plain | spec-change | 2/2 | 3 / 3 | DISAGREES — cause: printed 2/2 REPRODUCED from harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [task=FreeList,arm=plain]; in that count, not a cell of record: none; cells of record outside it: clbkfp01 (PASS); read differently: none | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:36 RESULT-p1-specchange §3 as published (P1 wave share of the condition only) |
| claude-opus-5 | FreeList | greenfield | salt-diet | spec-change | 0/1 | 2 / 3 | DISAGREES — cause: printed 0/1 REPRODUCED from harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [task=FreeList,arm=salt-diet]; in that count, not a cell of record: none; cells of record outside it: clbkfs01 (PASS), clbkfs02 (PASS); read differently: none | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:36 RESULT-p1-specchange §3 as published (P1 wave share of the condition only) |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 1/1 | 3 / 3 | DISAGREES — cause: printed 1/1 REPRODUCED from harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [task=LZW,arm=salt-diet]; in that count, not a cell of record: none; cells of record outside it: 18fb3eed (PASS), 6d58f1ec (PASS); read differently: none | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:36 RESULT-p1-specchange §3 as published (P1 wave share of the condition only) (7ac56e4e only; 18fb3eed/6d58f1ec are in RESULT-specchange-1) |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | 1/2 | 2 / 2 (+1 censored) | DISAGREES — cause: printed 1/2 REPRODUCED from harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [task=Paxos,arm=plain]; in that count, not a cell of record: none; cells of record outside it: clbkpp01 (PASS); read differently: f6462d47 (FAIL there, CENSORED here) | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:37 RESULT-p1-specchange §3 as published (P1 wave share of the condition only) |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | 1/2 | 2 / 2 (+1 unscorable) | DISAGREES — cause: printed 1/2 REPRODUCED from harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [task=Paxos,arm=salt-diet]; in that count, not a cell of record: none; cells of record outside it: clbkps01 (UNSCORABLE); read differently: b22d1000 (no class there, PASS here) | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:37 RESULT-p1-specchange §3 as published (P1 wave share of the condition only); SUPERSEDED by ADDENDUM A (b22d1000) |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | 1/2 | 2 / 2 (+1 censored) | DISAGREES — cause: printed 1/2 REPRODUCED from harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [task=Paxos,arm=plain]; in that count, not a cell of record: none; cells of record outside it: clbkpp01 (PASS); read differently: f6462d47 (FAIL there, CENSORED here) | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:87 RESULT-p1-specchange ADDENDUM A, "with b22d1000 re-scored" column (governs) |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | 2/2 | 2 / 2 (+1 unscorable) | agrees | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:87 RESULT-p1-specchange ADDENDUM A, "with b22d1000 re-scored" column (governs) |
| claude-opus-5 | FreeList | greenfield | plain | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stepg-opus-specchange-2026-09-29.md:56 RESULT-stepg §3, the condition at n = 3 of record (pooled P1/specchange-1 + step g cells) |
| claude-opus-5 | FreeList | greenfield | salt-diet | spec-change | 2/3 | 2 / 3 | agrees | harness/systems-v3/RESULT-stepg-opus-specchange-2026-09-29.md:57 RESULT-stepg §3, the condition at n = 3 of record (pooled P1/specchange-1 + step g cells) |
| claude-opus-5 | LRU | greenfield | plain | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stepg-opus-specchange-2026-09-29.md:58 RESULT-stepg §3, the condition at n = 3 of record (pooled P1/specchange-1 + step g cells) |
| claude-opus-5 | LZW | greenfield | plain | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stepg-opus-specchange-2026-09-29.md:59 RESULT-stepg §3, the condition at n = 3 of record (pooled P1/specchange-1 + step g cells) |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | 2/3 | 2 / 2 (+1 censored) | agrees | harness/systems-v3/RESULT-stepg-opus-specchange-2026-09-29.md:60 RESULT-stepg §3, the condition at n = 3 of record (pooled P1/specchange-1 + step g cells) |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | 2/3 | 2 / 2 (+1 unscorable) | agrees | harness/systems-v3/RESULT-stepg-opus-specchange-2026-09-29.md:92 RESULT-stepg ADDENDUM A (governs §3:61 "1 or 2 of 3") |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:23 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 3/3] |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:23 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 3/3] |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:24 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 3/3] |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | statement | 2/2 | 3 / 3 | DISAGREES — cause: printed 2/2 REPRODUCED from harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [task=Crc32,arm=salt-diet+stmt,landed=True]; in that count, not a cell of record: none; cells of record outside it: s3ctk01 (PASS); read differently: none | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:24 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 2/2] |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:25 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 3/3] |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:25 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 3/3] |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:26 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 3/3] |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:26 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 3/3] |
| gemini-3.1-pro-high | FreeList | greenfield | plain | none | 1/1 | 1 / 3 | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:27 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 1/1] |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | 0/3 | 0 / 3 | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:27 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 0/3] |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | 2/2 | 3 / 3 | DISAGREES — cause: printed 2/2 REPRODUCED from harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [task=FreeList,arm=plain+stmt,landed=True]; in that count, not a cell of record: none; cells of record outside it: s3fqk01 (PASS); read differently: none | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:28 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 2/2] |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | 1/1 | 1 / 1 (+2 censored) | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:28 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 1/1] |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | 1/3 | 1 / 3 | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:29 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 1/3] |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | 0/1 | 0 / 1 (+2 censored) | agrees | harness/systems-v3/RESULT-p1-greenfield-2026-09-13.md:29 result of record p1-greenfield §2 FULL PASS of SCORABLE [reads 0/1] |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:25 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells); ⚠ this row is the v2 re-run s3cpb01-03, NOT the map cells s3cp01-03 (p1-greenfield:9 excludes v2) [reads 3/3] |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:27 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 3/3] |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:26 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 3/3] |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | statement | 2/2 | 3 / 3 | DISAGREES — cause: printed 2/2 REPRODUCED from harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [task=Crc32,arm=salt-diet+stmt,landed=True]; in that count, not a cell of record: none; cells of record outside it: s3ctk01 (PASS); read differently: none | harness/systems-v3/RESULT-stage3-2026-09-12.md:28 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 2/2] |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:29 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 3/3] |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:31 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 3/3] |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:30 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 3/3] |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:32 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 3/3] |
| gemini-3.1-pro-high | FreeList | greenfield | plain | none | 1/1 | 1 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:33 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 1/1] |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | 0/3 | 0 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:35 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 0/3] |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | 2/2 | 3 / 3 | DISAGREES — cause: printed 2/2 REPRODUCED from harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [task=FreeList,arm=plain+stmt,landed=True]; in that count, not a cell of record: none; cells of record outside it: s3fqk01 (PASS); read differently: none | harness/systems-v3/RESULT-stage3-2026-09-12.md:34 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 2/2] |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | 1/3 | 1 / 1 (+2 censored) | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:36 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells); ⚠ counts the 2 TURN-TIMEOUT NOT-LANDED cells as scored, unlike p1-greenfield [reads 1/3] |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | 1/3 | 1 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:37 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells) [reads 1/3] |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | 2/3 | 0 / 1 (+2 censored) | DISAGREES — cause: printed 2/3 REPRODUCED from harness/systems-v3/RESULT-stage3-cells-2026-09-12.tsv [task=Paxos,arm=salt-diet]; in that count, not a cell of record: none; cells of record outside it: none; read differently: s3ps02 (PASS there, CENSORED here), s3ps03 (PASS there, CENSORED here) | harness/systems-v3/RESULT-stage3-2026-09-12.md:38 RESULT-stage3-2026-09-12.md §① condition table, n = fired cells, k = full (pre-dates p1-greenfield on the same cells); ⚠ counts the 2 TURN-TIMEOUT NOT-LANDED cells as scored, unlike p1-greenfield [reads 2/3] |
| gemini-3.1-pro-high | FreeList | greenfield | plain | none | 1/3 | 1 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:242 RESULT-stage3 ADDENDUM 1 §R3 (supersedes §②); ⚠ includes top-up cell(s) s3fpk01/02 or s3fqk01 that are NOT map rows [reads 1/3] |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:243 RESULT-stage3 ADDENDUM 1 §R3 (supersedes §②); ⚠ includes top-up cell(s) s3fpk01/02 or s3fqk01 that are NOT map rows [reads 3/3] |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | 0/3 | 0 / 3 | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:244 RESULT-stage3 ADDENDUM 1 §R3 (supersedes §②) [reads 0/3] |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | 1/3 | 1 / 1 (+2 censored) | agrees | harness/systems-v3/RESULT-stage3-2026-09-12.md:245 RESULT-stage3 ADDENDUM 1 §R3 (supersedes §②); ⚠ scores the 2 TURN-TIMEOUT cells 3/7 [reads 1/3] |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | 3/3 | 2 / 3 † | DISAGREES — cause: SUPERSEDED by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:204 | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:156 RESULT-gemini-flash-level5 ADDENDUM 1 §A2 (re-run whole; ADDENDUM 2 reproduces identically); ⚠ these are the FIRST-RUN cells (l5ls01-03 / l5pp01-03), replaced in the map by the ADDENDUM-3 re-fire cells [reads 3/3] |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | 0/3 | 0 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:21 chainF RESULT §1 table, FULL PASS column |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | 1/3 | 1 / 2 (+1 censored) | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:22 chainF RESULT §1 table, FULL PASS column |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | 1/3 | 1 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:23 chainF RESULT §1 table, FULL PASS column |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | 0/3 | 0 / 2 (+1 unscorable) | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:24 chainF RESULT §1 table, FULL PASS column |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:25 chainF RESULT §1 table, FULL PASS column |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:26 chainF RESULT §1 table, FULL PASS column |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | 0/3 | 0 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:27 chainF RESULT §1 table, FULL PASS column |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:28 chainF RESULT §1 table, FULL PASS column |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | 2/3 | 2 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:29 chainF RESULT §1 table, FULL PASS column |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | 0/3 | 0 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:30 chainF RESULT §1 table, FULL PASS column |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:31 chainF RESULT §1 table, FULL PASS column |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:32 chainF RESULT §1 table, FULL PASS column |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | 0/3 | 0 / 2 (+1 unscorable) | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:155 chainF ADDENDUM A §A.4 |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | 0/3 | 0 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:40 chainF §1 prose, Flash × Paxos |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:40 chainF §1 prose, Flash × Paxos |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | 0/3 | 0 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:41 chainF §1 prose ("the same arm" = salt-diet) |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | 2/3 | 2 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:41 chainF §1 prose, Flash × FreeList |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:42 chainF §1 prose, one figure for all four LZW conditions |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:42 chainF §1 prose, one figure for all four LZW conditions |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:42 chainF §1 prose, one figure for all four LZW conditions |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:42 chainF §1 prose, one figure for all four LZW conditions |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24.md:211 chainD ERRATUM 1 §E6 (l8rfpb01-02 + l8rfwra201); phrase is "k of n reached, scored, FULL PASS" |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24.md:226 chainD ADDENDUM A (l8cpss02 + the two copies); phrase is "k of n reached, scored, FULL PASS" |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-claude-blockSB-2026-09-19.md:12 block SB §1: one line stating every one of its ten conditions at 3/3 |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-claude-blockSB-2026-09-19.md:12 block SB §1: one line stating every one of its ten conditions at 3/3 |
| claude-sonnet-5 | LRU | brownfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-claude-blockSB-2026-09-19.md:12 block SB §1: one line stating every one of its ten conditions at 3/3 |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-claude-blockSB-2026-09-19.md:12 block SB §1: one line stating every one of its ten conditions at 3/3 |
| claude-sonnet-5 | FreeList | brownfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-claude-blockSB-2026-09-19.md:12 block SB §1: one line stating every one of its ten conditions at 3/3 |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-claude-blockSB-2026-09-19.md:12 block SB §1: one line stating every one of its ten conditions at 3/3 |
| claude-sonnet-5 | LZW | brownfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-claude-blockSB-2026-09-19.md:12 block SB §1: one line stating every one of its ten conditions at 3/3 |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-claude-blockSB-2026-09-19.md:12 block SB §1: one line stating every one of its ten conditions at 3/3 |
| claude-sonnet-5 | Paxos | brownfield | plain | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-claude-blockSB-2026-09-19.md:12 block SB §1: one line stating every one of its ten conditions at 3/3 |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | 3/3 | 3 / 3 | agrees | harness/systems-v3/RESULT-claude-blockSB-2026-09-19.md:12 block SB §1: one line stating every one of its ten conditions at 3/3 |

## The rc-3 census's cells (§P2): the record's class, and the census's beside it

| model | problem | field | arm | extras | cell | class of record | census (variant class tests) |
|---|---|---|---|---|---|---|---|
| claude-opus-5 | Paxos | greenfield | salt-diet | none | b22d1000 | PASS | head PASS 24/24 |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | b22d1000 | PASS | head PASS 24/24 |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | clbgfs02 | CENSORED | head FAIL 3/7 · wt BUILD-FAIL 0/0 |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | clbszs02 | CENSORED | head PASS 8/8 · wt BUILD-FAIL 0/0 |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | clbufs02 | CENSORED | head PASS 7/7 · wt BUILD-FAIL 0/0 |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr03 | UNSCORABLE | head TIMEOUT 0/0 |

## Unmeasured cells

| model | problem | field | arm | extras | cell | why |
|---|---|---|---|---|---|---|
| none | | | | | | |

## Per-cell verdicts and their sources (every table entry derives from these rows)

| model | problem | field | arm | extras | cell | class | V | K | E | source |
|---|---|---|---|---|---|---|---|---|---|---|
| claude-opus-5 | Crc32 | greenfield | plain | none | 2d0c65b3 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=2d0c65b3] |
| claude-opus-5 | Crc32 | greenfield | plain | none | 746d7d4e | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=746d7d4e] |
| claude-opus-5 | Crc32 | greenfield | plain | none | a87b7740 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=a87b7740] |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 11165871 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=11165871] |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 3e95075c | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=3e95075c] |
| claude-opus-5 | Crc32 | greenfield | salt-diet | none | 57a33630 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=57a33630] |
| claude-opus-5 | FreeList | greenfield | plain | none | 188f422b | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=188f422b] |
| claude-opus-5 | FreeList | greenfield | plain | none | 9cb8ce96 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=9cb8ce96] |
| claude-opus-5 | FreeList | greenfield | plain | none | n301free | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=n301free] |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | 161b5a34 | PASS | PASS | 7/7 | CAP-COST | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=161b5a34] |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | de4de8f2 | PASS | PASS | 7/7 | CAP-COST | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=de4de8f2] |
| claude-opus-5 | FreeList | greenfield | salt-diet | none | f33c7e65 | FAIL | FAIL | 6/7 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=f33c7e65] |
| claude-opus-5 | LRU | greenfield | plain | none | 3bdcbcbd | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=3bdcbcbd] |
| claude-opus-5 | LRU | greenfield | plain | none | 69e8c2c4 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=69e8c2c4] |
| claude-opus-5 | LRU | greenfield | plain | none | n302lru | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=n302lru] |
| claude-opus-5 | LRU | greenfield | salt-diet | none | 011fe22f | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=011fe22f] |
| claude-opus-5 | LRU | greenfield | salt-diet | none | b71994e3 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=b71994e3] |
| claude-opus-5 | LRU | greenfield | salt-diet | none | d6b53ee4 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=d6b53ee4] |
| claude-opus-5 | LZW | greenfield | plain | none | 93323249 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=93323249] |
| claude-opus-5 | LZW | greenfield | plain | none | c34012e0 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=c34012e0] |
| claude-opus-5 | LZW | greenfield | plain | none | d91f137b | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=d91f137b] |
| claude-opus-5 | LZW | greenfield | salt-diet | none | 18fb3eed | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=18fb3eed] |
| claude-opus-5 | LZW | greenfield | salt-diet | none | 7ac56e4e | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=7ac56e4e] |
| claude-opus-5 | LZW | greenfield | salt-diet | none | eb558398 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=eb558398] |
| claude-opus-5 | Paxos | greenfield | plain | none | 60a056e6 | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=60a056e6] |
| claude-opus-5 | Paxos | greenfield | plain | none | f6462d47 | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=f6462d47] |
| claude-opus-5 | Paxos | greenfield | plain | none | n303paxo | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=n303paxo] |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | 6fc49f7c | PASS | PASS | 17/17 | CAP-COST | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=6fc49f7c] |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | 9e6c8d4d | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=9e6c8d4d] |
| claude-opus-5 | Paxos | greenfield | salt-diet | none | b22d1000 | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=b22d1000] |
| claude-opus-5 | Crc32 | greenfield | plain | statement | st01crc3 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st01crc3] |
| claude-opus-5 | Crc32 | greenfield | plain | statement | st02crc3 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st02crc3] |
| claude-opus-5 | Crc32 | greenfield | plain | statement | st03crc3 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st03crc3] |
| claude-opus-5 | Crc32 | greenfield | salt-diet | statement | st04crc3 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st04crc3] |
| claude-opus-5 | Crc32 | greenfield | salt-diet | statement | st05crc3 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st05crc3] |
| claude-opus-5 | Crc32 | greenfield | salt-diet | statement | st06crc3 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st06crc3] |
| claude-opus-5 | LRU | greenfield | plain | statement | st07lru | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st07lru] |
| claude-opus-5 | LRU | greenfield | plain | statement | st08lru | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st08lru] |
| claude-opus-5 | LRU | greenfield | plain | statement | st09lru | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st09lru] |
| claude-opus-5 | LRU | greenfield | salt-diet | statement | st10lru | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st10lru] |
| claude-opus-5 | LRU | greenfield | salt-diet | statement | st11lru | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st11lru] |
| claude-opus-5 | LRU | greenfield | salt-diet | statement | st12lru | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-statement-arm-verdicts-2026-09-09.tsv [cell=st12lru] |
| claude-opus-5 | FreeList | greenfield | plain | statement | sf01free | PASS | PASS | 7/7 | - | harness/systems-v3/RESULT-statement-arm-2026-09-09.md:22 (pool 'wave 2' = cells-stmt-free-2026-09-09, bound at :155; evidence/v3-cost-tables-2026-09-28/cellroots.tsv) |
| claude-opus-5 | FreeList | greenfield | plain | statement | sf02free | PASS | PASS | 7/7 | - | harness/systems-v3/RESULT-statement-arm-2026-09-09.md:22 (pool 'wave 2' = cells-stmt-free-2026-09-09, bound at :155; evidence/v3-cost-tables-2026-09-28/cellroots.tsv) |
| claude-opus-5 | FreeList | greenfield | plain | statement | sf03free | PASS | PASS | 7/7 | - | harness/systems-v3/RESULT-statement-arm-2026-09-09.md:22 (pool 'wave 2' = cells-stmt-free-2026-09-09, bound at :155; evidence/v3-cost-tables-2026-09-28/cellroots.tsv) |
| claude-opus-5 | FreeList | greenfield | salt-diet | statement | sf04free | PASS | PASS | 7/7 | - | harness/systems-v3/RESULT-statement-arm-2026-09-09.md:22 (pool 'wave 2' = cells-stmt-free-2026-09-09, bound at :155; evidence/v3-cost-tables-2026-09-28/cellroots.tsv) |
| claude-opus-5 | FreeList | greenfield | salt-diet | statement | sf05free | PASS | PASS | 7/7 | - | harness/systems-v3/RESULT-statement-arm-2026-09-09.md:22 (pool 'wave 2' = cells-stmt-free-2026-09-09, bound at :155; evidence/v3-cost-tables-2026-09-28/cellroots.tsv) |
| claude-opus-5 | FreeList | greenfield | salt-diet | statement | sf06free | PASS | PASS | 7/7 | - | harness/systems-v3/RESULT-statement-arm-2026-09-09.md:22 (pool 'wave 2' = cells-stmt-free-2026-09-09, bound at :155; evidence/v3-cost-tables-2026-09-28/cellroots.tsv) |
| claude-opus-5 | LZW | greenfield | plain | statement | 22ee7d33 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=22ee7d33] |
| claude-opus-5 | LZW | greenfield | plain | statement | 922d1ff0 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=922d1ff0] |
| claude-opus-5 | LZW | greenfield | plain | statement | f795e96f | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=f795e96f] |
| claude-opus-5 | LZW | greenfield | salt-diet | statement | 6d58f1ec | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=6d58f1ec] |
| claude-opus-5 | LZW | greenfield | salt-diet | statement | 9aca67c5 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=9aca67c5] |
| claude-opus-5 | LZW | greenfield | salt-diet | statement | f5f66c47 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-posthoc-correctness-verdicts-2026-09-09.tsv [cell=f5f66c47] |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | 2d0c65b3 | PASS | - | 10/10 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=2d0c65b3] |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | 746d7d4e | PASS | - | 10/10 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=746d7d4e] |
| claude-opus-5 | Crc32 | greenfield | plain | spec-change | a87b7740 | PASS | - | 10/10 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=a87b7740] |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 11165871 | PASS | - | 10/10 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=11165871] |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 3e95075c | PASS | - | 10/10 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=3e95075c] |
| claude-opus-5 | Crc32 | greenfield | salt-diet | spec-change | 57a33630 | PASS | - | 10/10 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=57a33630] |
| claude-opus-5 | FreeList | greenfield | plain | spec-change | 188f422b | PASS | - | 9/9 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=188f422b] |
| claude-opus-5 | FreeList | greenfield | plain | spec-change | 9cb8ce96 | PASS | - | 9/9 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=9cb8ce96] |
| claude-opus-5 | FreeList | greenfield | salt-diet | spec-change | f33c7e65 | FAIL | - | 8/9 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=f33c7e65] |
| claude-opus-5 | LRU | greenfield | plain | spec-change | 3bdcbcbd | PASS | - | 23/23 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=3bdcbcbd] |
| claude-opus-5 | LRU | greenfield | plain | spec-change | 69e8c2c4 | PASS | - | 23/23 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=69e8c2c4] |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | 011fe22f | PASS | - | 23/23 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=011fe22f] |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | b71994e3 | PASS | - | 23/23 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=b71994e3] |
| claude-opus-5 | LRU | greenfield | salt-diet | spec-change | d6b53ee4 | PASS | - | 23/23 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=d6b53ee4] |
| claude-opus-5 | LZW | greenfield | plain | spec-change | 93323249 | PASS | - | 15/15 | - | harness/systems-v3/RESULT-specchange-1-2026-09-10.md:74 |
| claude-opus-5 | LZW | greenfield | plain | spec-change | 22ee7d33 | PASS | - | 15/15 | - | harness/systems-v3/RESULT-specchange-1-2026-09-10.md:74 |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 7ac56e4e | PASS | - | 15/15 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=7ac56e4e] |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 18fb3eed | PASS | - | 15/15 | - | harness/systems-v3/RESULT-specchange-1-2026-09-10.md:74 |
| claude-opus-5 | LZW | greenfield | salt-diet | spec-change | 6d58f1ec | PASS | - | 15/15 | - | harness/systems-v3/RESULT-specchange-1-2026-09-10.md:74 |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | 60a056e6 | PASS | - | 24/24 | LANDED | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=60a056e6] |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | f6462d47 | CENSORED | - | 23/24 | CAP-COST | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=f6462d47] |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | 9e6c8d4d | PASS | - | 24/24 | CAP-COST | harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv [cell=9e6c8d4d] |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | b22d1000 | PASS | PASS | 24/24 | - | harness/systems-v3/RESULT-p1-specchange-2026-09-10.md:77 |
| claude-opus-5 | Crc32 | brownfield | plain | none | clbocp01 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocp01] |
| claude-opus-5 | Crc32 | brownfield | plain | none | clbocp02 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocp02] |
| claude-opus-5 | Crc32 | brownfield | plain | none | clbocp03 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocp03] |
| claude-opus-5 | Crc32 | brownfield | salt-diet | none | clbocs01 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocs01] |
| claude-opus-5 | Crc32 | brownfield | salt-diet | none | clbocs02 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocs02] |
| claude-opus-5 | Crc32 | brownfield | salt-diet | none | clbocs03 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbocs03] |
| claude-opus-5 | FreeList | brownfield | plain | none | clbofp01 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofp01] |
| claude-opus-5 | FreeList | brownfield | plain | none | clbofp02 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofp02] |
| claude-opus-5 | FreeList | brownfield | plain | none | clbofp03 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofp03] |
| claude-opus-5 | FreeList | brownfield | salt-diet | none | clbofs01 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofs01] |
| claude-opus-5 | FreeList | brownfield | salt-diet | none | clbofs02 | PASS | PASS | 7/7 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofs02] |
| claude-opus-5 | FreeList | brownfield | salt-diet | none | clbofs03 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbofs03] |
| claude-opus-5 | LRU | brownfield | plain | none | clbolp01 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbolp01] |
| claude-opus-5 | LRU | brownfield | plain | none | clbolp02 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbolp02] |
| claude-opus-5 | LRU | brownfield | plain | none | clbolp03 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbolp03] |
| claude-opus-5 | LRU | brownfield | salt-diet | none | clbols01 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbols01] |
| claude-opus-5 | LRU | brownfield | salt-diet | none | clbols02 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbols02] |
| claude-opus-5 | LRU | brownfield | salt-diet | none | clbols03 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbols03] |
| claude-opus-5 | Paxos | brownfield | plain | none | clbopp01 | PASS | PASS | 17/17 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbopp01] |
| claude-opus-5 | Paxos | brownfield | plain | none | clbopp02 | PASS | PASS | 17/17 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbopp02] |
| claude-opus-5 | Paxos | brownfield | plain | none | clbopp03 | PASS | PASS | 17/17 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbopp03] |
| claude-opus-5 | Paxos | brownfield | salt-diet | none | clbops01 | PASS | PASS | 17/17 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbops01] |
| claude-opus-5 | Paxos | brownfield | salt-diet | none | clbops02 | PASS | PASS | 17/17 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbops02] |
| claude-opus-5 | Paxos | brownfield | salt-diet | none | clbops03 | PASS | PASS | 17/17 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbops03] |
| claude-opus-5 | LZW | brownfield | plain | none | clbozp01 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozp01] |
| claude-opus-5 | LZW | brownfield | plain | none | clbozp02 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozp02] |
| claude-opus-5 | LZW | brownfield | plain | none | clbozp03 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozp03] |
| claude-opus-5 | LZW | brownfield | salt-diet | none | clbozs01 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozs01] |
| claude-opus-5 | LZW | brownfield | salt-diet | none | clbozs02 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozs02] |
| claude-opus-5 | LZW | brownfield | salt-diet | none | clbozs03 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockO-cells.tsv [cell=clbozs03] |
| claude-opus-5 | Crc32 | brownfield | plain | statement | clbtcp01 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcp01] |
| claude-opus-5 | Crc32 | brownfield | plain | statement | clbtcp02 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcp02] |
| claude-opus-5 | Crc32 | brownfield | plain | statement | clbtcp03 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcp03] |
| claude-opus-5 | Crc32 | brownfield | salt-diet | statement | clbtcs01 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcs01] |
| claude-opus-5 | Crc32 | brownfield | salt-diet | statement | clbtcs02 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcs02] |
| claude-opus-5 | Crc32 | brownfield | salt-diet | statement | clbtcs03 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtcs03] |
| claude-opus-5 | FreeList | brownfield | plain | statement | clbtfp01 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfp01] |
| claude-opus-5 | FreeList | brownfield | plain | statement | clbtfp02 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfp02] |
| claude-opus-5 | FreeList | brownfield | plain | statement | clbtfp03 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfp03] |
| claude-opus-5 | FreeList | brownfield | salt-diet | statement | clbtfs01 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfs01] |
| claude-opus-5 | FreeList | brownfield | salt-diet | statement | clbtfs02 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfs02] |
| claude-opus-5 | FreeList | brownfield | salt-diet | statement | clbtfs03 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtfs03] |
| claude-opus-5 | LRU | brownfield | plain | statement | clbtlp01 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtlp01] |
| claude-opus-5 | LRU | brownfield | plain | statement | clbtlp02 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtlp02] |
| claude-opus-5 | LRU | brownfield | plain | statement | clbtlp03 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtlp03] |
| claude-opus-5 | LRU | brownfield | salt-diet | statement | clbtls01 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtls01] |
| claude-opus-5 | LRU | brownfield | salt-diet | statement | clbtls02 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtls02] |
| claude-opus-5 | LRU | brownfield | salt-diet | statement | clbtls03 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtls03] |
| claude-opus-5 | LZW | brownfield | plain | statement | clbtzp01 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzp01] |
| claude-opus-5 | LZW | brownfield | plain | statement | clbtzp02 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzp02] |
| claude-opus-5 | LZW | brownfield | plain | statement | clbtzp03 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzp03] |
| claude-opus-5 | LZW | brownfield | salt-diet | statement | clbtzs01 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzs01] |
| claude-opus-5 | LZW | brownfield | salt-diet | statement | clbtzs02 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzs02] |
| claude-opus-5 | LZW | brownfield | salt-diet | statement | clbtzs03 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv [cell=clbtzs03] |
| claude-sonnet-5 | Crc32 | greenfield | plain | none | clbgcp01 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcp01] |
| claude-sonnet-5 | Crc32 | greenfield | plain | none | clbgcp02 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcp02] |
| claude-sonnet-5 | Crc32 | greenfield | plain | none | clbgcp03 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcp03] |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | none | clbgcs01 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcs01] |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | none | clbgcs02 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcs02] |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | none | clbgcs03 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgcs03] |
| claude-sonnet-5 | FreeList | greenfield | plain | none | clbgfp01 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfp01] |
| claude-sonnet-5 | FreeList | greenfield | plain | none | clbgfp02 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfp02] |
| claude-sonnet-5 | FreeList | greenfield | plain | none | clbgfp03 | FAIL | FAIL | 6/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfp03] |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | clbgfs01 | PASS | PASS | 7/7 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs01] |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | clbgfs02 | CENSORED | BUILD-FAIL | 0/0 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs02] |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | none | clbgfs03 | PASS | PASS | 7/7 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgfs03] |
| claude-sonnet-5 | LRU | greenfield | plain | none | clbglp02 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbglp02] |
| claude-sonnet-5 | LRU | greenfield | plain | none | clbglp03 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbglp03] |
| claude-sonnet-5 | LRU | greenfield | salt-diet | none | clbgls01 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgls01] |
| claude-sonnet-5 | LRU | greenfield | salt-diet | none | clbgls02 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgls02] |
| claude-sonnet-5 | LRU | greenfield | salt-diet | none | clbgls03 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgls03] |
| claude-sonnet-5 | Paxos | greenfield | plain | none | clbgpp01 | PASS | PASS | 17/17 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgpp01] |
| claude-sonnet-5 | Paxos | greenfield | plain | none | clbgpp02 | PASS | PASS | 17/17 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgpp02] |
| claude-sonnet-5 | Paxos | greenfield | plain | none | clbgpp03 | PASS | PASS | 17/17 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgpp03] |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | none | clbgps01 | PASS | PASS | 17/17 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps01] |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | none | clbgps02 | PASS | PASS | 17/17 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps02] |
| claude-sonnet-5 | Paxos | greenfield | salt-diet | none | clbgps03 | PASS | PASS | 17/17 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgps03] |
| claude-sonnet-5 | LZW | greenfield | plain | none | clbgzp01 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzp01] |
| claude-sonnet-5 | LZW | greenfield | plain | none | clbgzp02 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzp02] |
| claude-sonnet-5 | LZW | greenfield | plain | none | clbgzp03 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzp03] |
| claude-sonnet-5 | LZW | greenfield | salt-diet | none | clbgzs01 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzs01] |
| claude-sonnet-5 | LZW | greenfield | salt-diet | none | clbgzs02 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzs02] |
| claude-sonnet-5 | LZW | greenfield | salt-diet | none | clbgzs03 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv [cell=clbgzs03] |
| claude-sonnet-5 | Crc32 | greenfield | plain | statement | clbscp01 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscp01] |
| claude-sonnet-5 | Crc32 | greenfield | plain | statement | clbscp02 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscp02] |
| claude-sonnet-5 | Crc32 | greenfield | plain | statement | clbscp03 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscp03] |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | statement | clbscs01 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscs01] |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | statement | clbscs02 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscs02] |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | statement | clbscs03 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbscs03] |
| claude-sonnet-5 | FreeList | greenfield | plain | statement | clbsfp01 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfp01] |
| claude-sonnet-5 | FreeList | greenfield | plain | statement | clbsfp02 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfp02] |
| claude-sonnet-5 | FreeList | greenfield | plain | statement | clbsfp03 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfp03] |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | statement | clbsfs01 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfs01] |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | statement | clbsfs02 | CENSORED | FAIL | 6/7 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfs02] |
| claude-sonnet-5 | FreeList | greenfield | salt-diet | statement | clbsfs03 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsfs03] |
| claude-sonnet-5 | LRU | greenfield | plain | statement | clbslp01 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbslp01] |
| claude-sonnet-5 | LRU | greenfield | plain | statement | clbslp02 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbslp02] |
| claude-sonnet-5 | LRU | greenfield | plain | statement | clbslp03 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbslp03] |
| claude-sonnet-5 | LRU | greenfield | salt-diet | statement | clbsls01 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsls01] |
| claude-sonnet-5 | LRU | greenfield | salt-diet | statement | clbsls02 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsls02] |
| claude-sonnet-5 | LRU | greenfield | salt-diet | statement | clbsls03 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbsls03] |
| claude-sonnet-5 | LZW | greenfield | plain | statement | clbszp01 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszp01] |
| claude-sonnet-5 | LZW | greenfield | plain | statement | clbszp02 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszp02] |
| claude-sonnet-5 | LZW | greenfield | plain | statement | clbszp03 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszp03] |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | clbszs01 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszs01] |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | clbszs02 | CENSORED | BUILD-FAIL | 0/0 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszs02] |
| claude-sonnet-5 | LZW | greenfield | salt-diet | statement | clbszs03 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv [cell=clbszs03] |
| claude-sonnet-5 | Crc32 | brownfield | plain | statement | clbucp01 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucp01] |
| claude-sonnet-5 | Crc32 | brownfield | plain | statement | clbucp02 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucp02] |
| claude-sonnet-5 | Crc32 | brownfield | plain | statement | clbucp03 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucp03] |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | statement | clbucs01 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucs01] |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | statement | clbucs02 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucs02] |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | statement | clbucs03 | PASS | PASS | 6/6 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbucs03] |
| claude-sonnet-5 | FreeList | brownfield | plain | statement | clbufp01 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufp01] |
| claude-sonnet-5 | FreeList | brownfield | plain | statement | clbufp02 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufp02] |
| claude-sonnet-5 | FreeList | brownfield | plain | statement | clbufp03 | PASS | PASS | 7/7 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufp03] |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | clbufs01 | PASS | PASS | 7/7 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs01] |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | clbufs02 | CENSORED | BUILD-FAIL | 0/0 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs02] |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | statement | clbufs03 | PASS | PASS | 7/7 | ENDED: CAP-COST | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbufs03] |
| claude-sonnet-5 | LRU | brownfield | plain | statement | clbulp01 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbulp01] |
| claude-sonnet-5 | LRU | brownfield | plain | statement | clbulp02 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbulp02] |
| claude-sonnet-5 | LRU | brownfield | plain | statement | clbulp03 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbulp03] |
| claude-sonnet-5 | LRU | brownfield | salt-diet | statement | clbuls01 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuls01] |
| claude-sonnet-5 | LRU | brownfield | salt-diet | statement | clbuls02 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuls02] |
| claude-sonnet-5 | LRU | brownfield | salt-diet | statement | clbuls03 | PASS | PASS | 16/16 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuls03] |
| claude-sonnet-5 | LZW | brownfield | plain | statement | clbuzp01 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzp01] |
| claude-sonnet-5 | LZW | brownfield | plain | statement | clbuzp02 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzp02] |
| claude-sonnet-5 | LZW | brownfield | plain | statement | clbuzp03 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzp03] |
| claude-sonnet-5 | LZW | brownfield | salt-diet | statement | clbuzs01 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzs01] |
| claude-sonnet-5 | LZW | brownfield | salt-diet | statement | clbuzs02 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzs02] |
| claude-sonnet-5 | LZW | brownfield | salt-diet | statement | clbuzs03 | PASS | PASS | 8/8 | ENDED: LANDED | evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv [cell=clbuzs03] |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | clbbcp01 | PASS | PASS | 6/6 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcp01] |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | clbbcp02 | PASS | PASS | 6/6 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcp02] |
| claude-sonnet-5 | Crc32 | brownfield | plain | none | clbbcp03 | PASS | PASS | 6/6 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcp03] |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | clbbcs01 | PASS | PASS | 6/6 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcs01] |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | clbbcs02 | PASS | PASS | 6/6 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcs02] |
| claude-sonnet-5 | Crc32 | brownfield | salt-diet | none | clbbcs03 | PASS | PASS | 6/6 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbcs03] |
| claude-sonnet-5 | FreeList | brownfield | plain | none | clbbfp01 | PASS | PASS | 7/7 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfp01] |
| claude-sonnet-5 | FreeList | brownfield | plain | none | clbbfp02 | PASS | PASS | 7/7 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfp02] |
| claude-sonnet-5 | FreeList | brownfield | plain | none | clbbfp03 | PASS | PASS | 7/7 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfp03] |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | clbbfs01 | PASS | PASS | 7/7 | ENDED: CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs01] |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | clbbfs02 | PASS | PASS | 7/7 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs02] |
| claude-sonnet-5 | FreeList | brownfield | salt-diet | none | clbbfs03 | PASS | PASS | 7/7 | ENDED: CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbfs03] |
| claude-sonnet-5 | LRU | brownfield | plain | none | clbblp01 | PASS | PASS | 16/16 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbblp01] |
| claude-sonnet-5 | LRU | brownfield | plain | none | clbblp02 | PASS | PASS | 16/16 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbblp02] |
| claude-sonnet-5 | LRU | brownfield | plain | none | clbblp03 | PASS | PASS | 16/16 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbblp03] |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | clbbls01 | PASS | PASS | 16/16 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbls01] |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | clbbls02 | PASS | PASS | 16/16 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbls02] |
| claude-sonnet-5 | LRU | brownfield | salt-diet | none | clbbls03 | PASS | PASS | 16/16 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbls03] |
| claude-sonnet-5 | Paxos | brownfield | plain | none | clbbpp01 | PASS | PASS | 17/17 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbpp01] |
| claude-sonnet-5 | Paxos | brownfield | plain | none | clbbpp02 | PASS | PASS | 17/17 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbpp02] |
| claude-sonnet-5 | Paxos | brownfield | plain | none | clbbpp03 | PASS | PASS | 17/17 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbpp03] |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | clbbps01 | PASS | PASS | 17/17 | ENDED: DIALOG | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps01] |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | clbbps02 | PASS | PASS | 17/17 | ENDED: CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps02] |
| claude-sonnet-5 | Paxos | brownfield | salt-diet | none | clbbps03 | PASS | PASS | 17/17 | ENDED: CAP-COST | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbps03] |
| claude-sonnet-5 | LZW | brownfield | plain | none | clbbzp01 | PASS | PASS | 8/8 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzp01] |
| claude-sonnet-5 | LZW | brownfield | plain | none | clbbzp02 | PASS | PASS | 8/8 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzp02] |
| claude-sonnet-5 | LZW | brownfield | plain | none | clbbzp03 | PASS | PASS | 8/8 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzp03] |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | clbbzs01 | PASS | PASS | 8/8 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzs01] |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | clbbzs02 | PASS | PASS | 8/8 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzs02] |
| claude-sonnet-5 | LZW | brownfield | salt-diet | none | clbbzs03 | PASS | PASS | 8/8 | ENDED: LANDED | harness/systems-v3/RESULT-claude-blockSB-2026-09-19-cells.tsv [cell=clbbzs03] |
| claude-sonnet-5 | Crc32 | greenfield | plain | spec-change | clbccp01 | PASS | PASS | 10/10 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp01] |
| claude-sonnet-5 | Crc32 | greenfield | plain | spec-change | clbccp02 | PASS | PASS | 10/10 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp02] |
| claude-sonnet-5 | Crc32 | greenfield | plain | spec-change | clbccp03 | PASS | PASS | 10/10 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccp03] |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | spec-change | clbccs01 | PASS | PASS | 10/10 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs01] |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | spec-change | clbccs02 | PASS | PASS | 10/10 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs02] |
| claude-sonnet-5 | Crc32 | greenfield | salt-diet | spec-change | clbccs03 | PASS | PASS | 10/10 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbccs03] |
| claude-sonnet-5 | FreeList | greenfield | plain | spec-change | clbcfp01 | FAIL | FAIL | 8/9 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp01] |
| claude-sonnet-5 | FreeList | greenfield | plain | spec-change | clbcfp02 | FAIL | FAIL | 8/9 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp02] |
| claude-sonnet-5 | FreeList | greenfield | plain | spec-change | clbcfp03 | PASS | PASS | 9/9 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcfp03] |
| claude-sonnet-5 | LRU | greenfield | plain | spec-change | clbclp01 | PASS | PASS | 23/23 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp01] |
| claude-sonnet-5 | LRU | greenfield | plain | spec-change | clbclp02 | PASS | PASS | 23/23 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp02] |
| claude-sonnet-5 | LRU | greenfield | plain | spec-change | clbclp03 | PASS | PASS | 23/23 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbclp03] |
| claude-sonnet-5 | LRU | greenfield | salt-diet | spec-change | clbcls01 | PASS | PASS | 23/23 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls01] |
| claude-sonnet-5 | LRU | greenfield | salt-diet | spec-change | clbcls02 | PASS | PASS | 23/23 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls02] |
| claude-sonnet-5 | LRU | greenfield | salt-diet | spec-change | clbcls03 | PASS | PASS | 23/23 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcls03] |
| claude-sonnet-5 | Paxos | greenfield | plain | spec-change | clbcpp01 | PASS | PASS | 24/24 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp01] |
| claude-sonnet-5 | Paxos | greenfield | plain | spec-change | clbcpp02 | PASS | PASS | 24/24 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp02] |
| claude-sonnet-5 | Paxos | greenfield | plain | spec-change | clbcpp03 | FAIL | FAIL | 23/24 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbcpp03] |
| claude-sonnet-5 | LZW | greenfield | plain | spec-change | clbczp01 | PASS | PASS | 15/15 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp01] |
| claude-sonnet-5 | LZW | greenfield | plain | spec-change | clbczp02 | PASS | PASS | 15/15 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp02] |
| claude-sonnet-5 | LZW | greenfield | plain | spec-change | clbczp03 | PASS | PASS | 15/15 | ENDED | evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv [cell=clbczp03] |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | s3cp01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:85 |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | s3cp02 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:86 |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | none | s3cp03 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:87 |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | s3cs01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:112 |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | s3cs02 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:113 |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | none | s3cs03 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:114 |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | s3lp01 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:103 |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | s3lp02 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:104 |
| gemini-3.1-pro-high | LRU | greenfield | plain | none | s3lp03 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:105 |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | s3ls01 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:125 |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | s3ls02 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:126 |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | none | s3ls03 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:127 |
| gemini-3.1-pro-high | FreeList | greenfield | plain | none | s3fp01 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:94 |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | s3fs01 | FAIL | FAIL | 0/7 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:119 |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | s3fs02 | FAIL | FAIL | 3/7 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:120 |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | none | s3fs03 | FAIL | FAIL | 6/7 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:121 |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | s3pp01 | FAIL | FAIL | 16/17 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:109 |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | s3pp02 | FAIL | FAIL | 16/17 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:110 |
| gemini-3.1-pro-high | Paxos | greenfield | plain | none | s3pp03 | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:111 |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | s3ps01 | FAIL | FAIL | 9/17 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:131 |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | s3ps02 | CENSORED | NOT-LANDED | - | TURN-TIMEOUT | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:132 |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | none | s3ps03 | CENSORED | NOT-LANDED | - | TURN-TIMEOUT | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:133 |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | s3cq01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:91 |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | s3cq02 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:92 |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | statement | s3cq03 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:93 |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | statement | s3ct01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:115 |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | statement | s3ct02 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:116 |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | s3lq01 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:106 |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | s3lq02 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:107 |
| gemini-3.1-pro-high | LRU | greenfield | plain | statement | s3lq03 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:108 |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | s3lt01 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:128 |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | s3lt02 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:129 |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | statement | s3lt03 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:130 |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | s3fq01 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:99 |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | s3fq02 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:100 |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | s3ft01 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:122 |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | s3ft02 | CENSORED | NOT-LANDED | - | TURN-TIMEOUT | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:123 |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | statement | s3ft03 | CENSORED | NOT-LANDED | - | TURN-TIMEOUT | harness/systems-v3/RESULT-per-cell-table-levels-1-and-4-2026-09-14.md:124 |
| gemini-3.1-pro-high | LRU | brownfield | plain | none | b4lrp01 | PASS | - | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:42 |
| gemini-3.1-pro-high | LRU | brownfield | plain | none | b4lrp02 | PASS | - | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:43 |
| gemini-3.1-pro-high | LRU | brownfield | plain | none | b4lrp03 | PASS | - | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:44 |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | none | b4lrs01 | PASS | - | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:45 |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | none | b4lrs02 | PASS | - | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:46 |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | none | b4lrs03 | FAIL | - | 10/16 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:47 |
| gemini-3.1-pro-high | Paxos | brownfield | plain | none | b4pp01 | PASS | - | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:54 |
| gemini-3.1-pro-high | Paxos | brownfield | plain | none | b4pp02 | PASS | - | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:55 |
| gemini-3.1-pro-high | Paxos | brownfield | plain | none | b4pp03 | PASS | - | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:56 |
| gemini-3.1-pro-high | Paxos | brownfield | salt-diet | none | b4ps01 | PASS | - | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:57 |
| gemini-3.1-pro-high | Paxos | brownfield | salt-diet | none | b4ps02 | PASS | - | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:58 |
| gemini-3.1-pro-high | Paxos | brownfield | salt-diet | none | b4ps03 | FAIL | - | 12/17 | LANDED | harness/systems-v3/RESULT-gemini-brownfield-level4-2026-09-14.md:59 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | none | l5cp01 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:30 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | none | l5cp02 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:31 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | none | l5cp03 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:32 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | none | l5cs01 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:33 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | none | l5cs02 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:34 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | none | l5cs03 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:35 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | none | l5fp01 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:36 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | none | l5fp02 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:37 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | none | l5fp03 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:38 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | none | l5fs01 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:39 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | none | l5fs02 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:40 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | none | l5fs03 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:41 |
| gemini-3.8-flash-high | LRU | greenfield | plain | none | l5lp01 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:42 |
| gemini-3.8-flash-high | LRU | greenfield | plain | none | l5lp02 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:43 |
| gemini-3.8-flash-high | LRU | greenfield | plain | none | l5lp03 | by condition | - | - | LANDED | harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:44 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | l5lsra301 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | l5lsra302 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | none | l5lsra303 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | l5ppr01 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | l5ppr02 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Paxos | greenfield | plain | none | l5ppr03 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | l5psra201 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | l5psra202 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | none | l5psra203 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | l5cq01 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | l5cq02 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | statement | l5cq03 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | l5ct01 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | l5ct02 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | statement | l5ct03 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | l5fq01 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | l5fq02 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | statement | l5fq03 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | l5ft01 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | l5ft02 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | statement | l5ft03 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | l5lq01 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | l5lq02 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | LRU | greenfield | plain | statement | l5lq03 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | l5lt01 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | l5lt02 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | statement | l5lt03 | by condition | - | - | - | landed by harness/systems-v3/RESULT-gemini-flash-level5-2026-09-15.md:213 |
| gemini-3.1-pro-high | LZW | greenfield | plain | none | l6vgpp01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:119 |
| gemini-3.1-pro-high | LZW | greenfield | plain | none | l6vgpp02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:120 |
| gemini-3.1-pro-high | LZW | greenfield | plain | none | l6vgpp03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:121 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | none | l6vgps01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:136 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | none | l6vgps02 | FAIL | FAIL | 0/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:137 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | none | l6vgps03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:138 |
| gemini-3.1-pro-high | LZW | greenfield | plain | statement | l6uspq01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:109 |
| gemini-3.1-pro-high | LZW | greenfield | plain | statement | l6vspb01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:125 |
| gemini-3.1-pro-high | LZW | greenfield | plain | statement | l6vspb02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:126 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | statement | l6vspt01 | FAIL | FAIL | 0/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:142 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | statement | l6vspt02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:143 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | statement | l6vspt03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:144 |
| gemini-3.8-flash-high | LZW | greenfield | plain | none | l6vgfp01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:116 |
| gemini-3.8-flash-high | LZW | greenfield | plain | none | l6vgfp02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:117 |
| gemini-3.8-flash-high | LZW | greenfield | plain | none | l6vgfp03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:118 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | none | l6vgfs01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:133 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | none | l6vgfs02 | UNSCORABLE | NOT-SCORED | - | - | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:134 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | none | l6vgfs03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:135 |
| gemini-3.8-flash-high | LZW | greenfield | plain | statement | l6vsfq01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:122 |
| gemini-3.8-flash-high | LZW | greenfield | plain | statement | l6vsfq02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:123 |
| gemini-3.8-flash-high | LZW | greenfield | plain | statement | l6vsfq03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:124 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | statement | l6vsft01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:139 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | statement | l6vsft02 | FAIL | FAIL | - | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:140 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | statement | l6vsft03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:141 |
| gemini-3.8-flash-high | LRU | brownfield | plain | none | l6vblp01 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:110 |
| gemini-3.8-flash-high | LRU | brownfield | plain | none | l6vblp02 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:111 |
| gemini-3.8-flash-high | LRU | brownfield | plain | none | l6vblp03 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:112 |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | none | l6vbls01 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:127 |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | none | l6vbls02 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:128 |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | none | l6vbls03 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:129 |
| gemini-3.8-flash-high | Paxos | brownfield | plain | none | l6vbpp01 | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:113 |
| gemini-3.8-flash-high | Paxos | brownfield | plain | none | l6vbpp02 | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:114 |
| gemini-3.8-flash-high | Paxos | brownfield | plain | none | l6vbpp03 | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:115 |
| gemini-3.8-flash-high | Paxos | brownfield | salt-diet | none | l6vbps01 | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:130 |
| gemini-3.8-flash-high | Paxos | brownfield | salt-diet | none | l6vbps02 | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:131 |
| gemini-3.8-flash-high | Paxos | brownfield | salt-diet | none | l6vbps03 | PASS | PASS | 17/17 | LANDED | harness/systems-v3/RESULT-gemini-level6-2026-09-17.md:132 |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | none | l7cfbp01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:262 |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | none | l7cfbp02 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:263 |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | none | l7cfbp03 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:264 |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | none | l7cfbs01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:306 |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | none | l7cfbs02 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:307 |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | none | l7cfbs03 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:308 |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | statement | l7cfsp01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:265 |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | statement | l7cfsp02 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:266 |
| gemini-3.8-flash-high | Crc32 | brownfield | plain | statement | l7cfsp03 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:267 |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | statement | l7cfss01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:309 |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | statement | l7cfssq01 | PASS | PASS | 6/6 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:582 |
| gemini-3.8-flash-high | Crc32 | brownfield | salt-diet | statement | l7cfssq02 | PASS | PASS | 6/6 | - | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:583 |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | none | l7cpbp01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:268 |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | none | l7cpbp02 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:269 |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | none | l7cpbp03 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:270 |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | l7cpbs01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:310 |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | l7cpbs02 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:311 |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | none | l7cpbs03 | UNSCORABLE | NOT-SCORED | - | NO-FIRST-RESULT | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:312 |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | statement | l7cpsp01 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:271 |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | statement | l7cpsp02 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:272 |
| gemini-3.1-pro-high | Crc32 | brownfield | plain | statement | l7cpsp03 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:273 |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | statement | l7cpssa201 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:313 |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | statement | l7cpssa202 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:314 |
| gemini-3.1-pro-high | Crc32 | brownfield | salt-diet | statement | l7cpssa203 | PASS | PASS | 6/6 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:315 |
| gemini-3.8-flash-high | FreeList | brownfield | plain | none | l7nffp01 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:232 |
| gemini-3.8-flash-high | FreeList | brownfield | plain | none | l7nffp02 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:233 |
| gemini-3.8-flash-high | FreeList | brownfield | plain | none | l7nffp03 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:234 |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | none | l7nffs01 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:274 |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | none | l7nffs02 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:275 |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | none | l7nffs03 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:276 |
| gemini-3.8-flash-high | LZW | brownfield | plain | none | l7nfzp01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:235 |
| gemini-3.8-flash-high | LZW | brownfield | plain | none | l7nfzp02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:236 |
| gemini-3.8-flash-high | LZW | brownfield | plain | none | l7nfzp03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:237 |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | none | l7nfzs01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:277 |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | none | l7nfzs02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:278 |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | none | l7nfzs03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:279 |
| gemini-3.1-pro-high | FreeList | brownfield | plain | none | l7npfp01 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:238 |
| gemini-3.1-pro-high | FreeList | brownfield | plain | none | l7npfp02 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:239 |
| gemini-3.1-pro-high | FreeList | brownfield | plain | none | l7npfp03 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:240 |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | none | l7npfs01 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:280 |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | none | l7npfs02 | FAIL | FAIL | 6/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:281 |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | none | l7npfs03 | FAIL | FAIL | 6/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:282 |
| gemini-3.1-pro-high | LZW | brownfield | plain | none | l7npzp01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:241 |
| gemini-3.1-pro-high | LZW | brownfield | plain | none | l7npzp02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:242 |
| gemini-3.1-pro-high | LZW | brownfield | plain | none | l7npzp03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:243 |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | none | l7npzs01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:283 |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | none | l7npzs02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:284 |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | none | l7npzs03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:285 |
| gemini-3.8-flash-high | FreeList | brownfield | plain | statement | l7sffp01 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:244 |
| gemini-3.8-flash-high | FreeList | brownfield | plain | statement | l7sffp02 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:245 |
| gemini-3.8-flash-high | FreeList | brownfield | plain | statement | l7sffp03 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:246 |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | statement | l7sffs01 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:286 |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | statement | l7sffs02 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:287 |
| gemini-3.8-flash-high | FreeList | brownfield | salt-diet | statement | l7sffs03 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:288 |
| gemini-3.8-flash-high | LRU | brownfield | plain | statement | l7sfrp01 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:247 |
| gemini-3.8-flash-high | LRU | brownfield | plain | statement | l7sfrp02 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:248 |
| gemini-3.8-flash-high | LRU | brownfield | plain | statement | l7sfrp03 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:249 |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | statement | l7sfrs01 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:289 |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | statement | l7sfrs02 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:290 |
| gemini-3.8-flash-high | LRU | brownfield | salt-diet | statement | l7sfrs03 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:291 |
| gemini-3.8-flash-high | LZW | brownfield | plain | statement | l7sfzp01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:250 |
| gemini-3.8-flash-high | LZW | brownfield | plain | statement | l7sfzp02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:251 |
| gemini-3.8-flash-high | LZW | brownfield | plain | statement | l7sfzp03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:252 |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | statement | l7sfzs01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:292 |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | statement | l7sfzs02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:293 |
| gemini-3.8-flash-high | LZW | brownfield | salt-diet | statement | l7sfzs03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:294 |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | statement | l7spfb01 | FAIL | FAIL | 6/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:295 |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | statement | l7spfb02 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:296 |
| gemini-3.1-pro-high | FreeList | brownfield | salt-diet | statement | l7spfwa201 | FAIL | FAIL | 6/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:297 |
| gemini-3.1-pro-high | FreeList | brownfield | plain | statement | l7spfp01 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:253 |
| gemini-3.1-pro-high | FreeList | brownfield | plain | statement | l7spfp02 | PASS | PASS | 7/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:254 |
| gemini-3.1-pro-high | FreeList | brownfield | plain | statement | l7spfp03 | FAIL | FAIL | 6/7 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:255 |
| gemini-3.1-pro-high | LRU | brownfield | plain | statement | l7sprp01 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:256 |
| gemini-3.1-pro-high | LRU | brownfield | plain | statement | l7sprp02 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:257 |
| gemini-3.1-pro-high | LRU | brownfield | plain | statement | l7sprp03 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:258 |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | statement | l7sprs01 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:298 |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | statement | l7sprs02 | PASS | PASS | 16/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:299 |
| gemini-3.1-pro-high | LRU | brownfield | salt-diet | statement | l7sprs03 | FAIL | FAIL | 10/16 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:300 |
| gemini-3.1-pro-high | LZW | brownfield | plain | statement | l7spzp01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:259 |
| gemini-3.1-pro-high | LZW | brownfield | plain | statement | l7spzp02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:260 |
| gemini-3.1-pro-high | LZW | brownfield | plain | statement | l7spzp03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:261 |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | statement | l7spzs01 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:301 |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | statement | l7spzs02 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:302 |
| gemini-3.1-pro-high | LZW | brownfield | salt-diet | statement | l7spzs03 | PASS | PASS | 8/8 | LANDED | harness/systems-v3/RESULT-gemini-level7-2026-09-19.md:303 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | spec-change | l8cfps01 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:2 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | spec-change | l8cfps02 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:3 |
| gemini-3.8-flash-high | Crc32 | greenfield | plain | spec-change | l8cfps03 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:4 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | spec-change | l8cfss01 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:5 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | spec-change | l8cfss02 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:6 |
| gemini-3.8-flash-high | Crc32 | greenfield | salt-diet | spec-change | l8cfss03 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:7 |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | spec-change | l8cpps01 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:8 |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | spec-change | l8cpps02 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:9 |
| gemini-3.1-pro-high | Crc32 | greenfield | plain | spec-change | l8cpps03 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:10 |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | l8cpss01 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24.md:223 |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | l8cpss02 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:12 |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | spec-change | l8cpss03 | PASS | PASS | 10/10 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24.md:224 |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | l8rfpb01 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:14 |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | l8rfpb02 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:15 |
| gemini-3.8-flash-high | LRU | greenfield | plain | spec-change | l8rfwra201 | PASS | - | 23/23 | - | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24.md:206 (anchor :204) |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | spec-change | l8rfss01 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:16 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | spec-change | l8rfss02 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:17 |
| gemini-3.8-flash-high | LRU | greenfield | salt-diet | spec-change | l8rfss03 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:18 |
| gemini-3.1-pro-high | LRU | greenfield | plain | spec-change | l8rppr01 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:19 |
| gemini-3.1-pro-high | LRU | greenfield | plain | spec-change | l8rppr02 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:20 |
| gemini-3.1-pro-high | LRU | greenfield | plain | spec-change | l8rppr03 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:21 |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | spec-change | l8rpsra201 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:22 |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | spec-change | l8rpsra202 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:23 |
| gemini-3.1-pro-high | LRU | greenfield | salt-diet | spec-change | l8rpsra203 | PASS | PASS | 23/23 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv:24 |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | l8xppr01 | FAIL | FAIL | 23/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:2 |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | l8xppr02 | FAIL | FAIL | 23/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:3 |
| gemini-3.1-pro-high | Paxos | greenfield | plain | spec-change | l8xppr03 | FAIL | FAIL | 23/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:4 |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | l8xpsr01 | CENSORED | FAIL | 5/24 | per-turn deadline | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:72 |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | l8xpsr02 | FAIL | FAIL | 23/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:6 |
| gemini-3.1-pro-high | Paxos | greenfield | salt-diet | spec-change | l8xpsr03 | PASS | PASS | 24/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:7 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | l8ffpr01 | FAIL | FAIL | 8/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:8 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | l8ffpr02 | PASS | PASS | 9/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:9 |
| gemini-3.8-flash-high | FreeList | greenfield | plain | spec-change | l8ffpr03 | PASS | PASS | 9/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:10 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | l8ffsra201 | FAIL | FAIL | 8/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:11 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | l8ffsra202 | FAIL | FAIL | 6/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:12 |
| gemini-3.8-flash-high | FreeList | greenfield | salt-diet | spec-change | l8ffsra203 | FAIL | FAIL | 8/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:13 |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | l8fppr01 | PASS | PASS | 9/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:14 |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | l8fppr02 | FAIL | FAIL | 8/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:15 |
| gemini-3.1-pro-high | FreeList | greenfield | plain | spec-change | l8fppr03 | FAIL | FAIL | 8/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:16 |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr01 | FAIL | FAIL | 8/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:17 |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr02 | FAIL | FAIL | 8/9 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:18 |
| gemini-3.1-pro-high | FreeList | greenfield | salt-diet | spec-change | l8fpsr03 | UNSCORABLE | TIMEOUT | 0/0 | - | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24.md:141 |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | l8zfpra201 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:20 |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | l8zfpra202 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:21 |
| gemini-3.8-flash-high | LZW | greenfield | plain | spec-change | l8zfpra203 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:22 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | l8zfsr01 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:23 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | l8zfsr02 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:24 |
| gemini-3.8-flash-high | LZW | greenfield | salt-diet | spec-change | l8zfsr03 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:25 |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | l8zppr01 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:26 |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | l8zppr02 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:27 |
| gemini-3.1-pro-high | LZW | greenfield | plain | spec-change | l8zppr03 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:28 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | l8zpsr01 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:29 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | l8zpsr02 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:30 |
| gemini-3.1-pro-high | LZW | greenfield | salt-diet | spec-change | l8zpsr03 | PASS | PASS | 15/15 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:31 |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | l8xfp2a201 | FAIL | FAIL | 23/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:32 |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | l8xfp2a202 | FAIL | FAIL | 23/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:33 |
| gemini-3.8-flash-high | Paxos | greenfield | plain | spec-change | l8xfp2a203 | FAIL | FAIL | 23/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:34 |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | l8xfs201 | PASS | PASS | 24/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:35 |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | l8xfs202 | PASS | PASS | 24/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:36 |
| gemini-3.8-flash-high | Paxos | greenfield | salt-diet | spec-change | l8xfs203 | PASS | PASS | 24/24 | LANDED | harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv:37 |
| claude-opus-5 | LZW | greenfield | plain | spec-change | clbkzp01 | PASS | PASS | 15/15 | LANDED | evidence/stepg-2026-09-29/cells.tsv [cell=clbkzp01] |
| claude-opus-5 | LRU | greenfield | plain | spec-change | clbklp01 | PASS | PASS | 23/23 | LANDED | evidence/stepg-2026-09-29/cells.tsv [cell=clbklp01] |
| claude-opus-5 | FreeList | greenfield | plain | spec-change | clbkfp01 | PASS | PASS | 9/9 | LANDED | evidence/stepg-2026-09-29/cells.tsv [cell=clbkfp01] |
| claude-opus-5 | Paxos | greenfield | plain | spec-change | clbkpp01 | PASS | PASS | 24/24 | CAP-COST | evidence/stepg-2026-09-29/cells.tsv [cell=clbkpp01] |
| claude-opus-5 | Paxos | greenfield | salt-diet | spec-change | clbkps01 | UNSCORABLE | TIMEOUT | 0/0 | LANDED | evidence/stepg-2026-09-29/cells.tsv [cell=clbkps01] |
| claude-opus-5 | FreeList | greenfield | salt-diet | spec-change | clbkfs01 | PASS | PASS | 9/9 | LANDED | evidence/stepg-2026-09-29/cells.tsv [cell=clbkfs01] |
| claude-opus-5 | FreeList | greenfield | salt-diet | spec-change | clbkfs02 | PASS | PASS | 9/9 | LANDED | evidence/stepg-2026-09-29/cells.tsv [cell=clbkfs02] |
| claude-sonnet-5 | LRU | greenfield | plain | none | clbglp01 | PASS | PASS | 16/16 | - | harness/systems-v3/RESULT-claude-blockSG-2026-09-21.md:81 |
| gemini-3.1-pro-high | FreeList | greenfield | plain | none | s3fpk01 | FAIL | FAIL | - | LANDED | harness/systems-v3/RESULT-stage3-ADDENDUM-B-cells-2026-09-29.tsv [role=TARGET,cell=s3fpk01] |
| gemini-3.1-pro-high | FreeList | greenfield | plain | none | s3fpk02 | FAIL | FAIL | - | LANDED | harness/systems-v3/RESULT-stage3-ADDENDUM-B-cells-2026-09-29.tsv [role=TARGET,cell=s3fpk02] |
| gemini-3.1-pro-high | FreeList | greenfield | plain | statement | s3fqk01 | PASS | PASS | - | LANDED | harness/systems-v3/RESULT-stage3-ADDENDUM-B-cells-2026-09-29.tsv [role=TARGET,cell=s3fqk01] |
| gemini-3.1-pro-high | Crc32 | greenfield | salt-diet | statement | s3ctk01 | PASS | PASS | - | LANDED | harness/systems-v3/RESULT-stage3-ADDENDUM-B-cells-2026-09-29.tsv [role=TARGET,cell=s3ctk01] |
