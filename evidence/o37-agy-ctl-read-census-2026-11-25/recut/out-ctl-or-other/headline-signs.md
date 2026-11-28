## correctness P4 counts (tables_correctness_v3.py NEW)
| model | treatment | + | = | − | ? | no sign (—) |
|---|---|---|---|---|---|---|
| claude-opus-5 | bare | 0 | 4 | 1 | 0 | 0 |
| claude-opus-5 | statement | 0 | 4 | 0 | 0 | 1 |
| claude-opus-5 | spec-change | 0 | 3 | 1 | 1 | 0 |
| claude-sonnet-5 | bare | 0 | 4 | 0 | 1 | 0 |
| claude-sonnet-5 | statement | 0 | 2 | 0 | 2 | 1 |
| claude-sonnet-5 | spec-change | 0 | 2 | 0 | 0 | 3 |
| gemini-3.1-pro-high | bare | 0 | 3 | 1 | 1 | 0 |
| gemini-3.1-pro-high | statement | 0 | 3 | 0 | 1 | 1 |
| gemini-3.1-pro-high | spec-change | 1 | 3 | 0 | 1 | 0 |
| gemini-3.8-flash-high | bare | 0 | 1 | 0 | 0 | 4 |
| gemini-3.8-flash-high | statement | 0 | 0 | 1 | 0 | 4 |
| gemini-3.8-flash-high | spec-change | 0 | 0 | 0 | 0 | 5 |

## descriptive T4 sign counts (tables_v2.py NEW)
| model | treatment | k of m ratios > 1 | indeterminate | median of the ratios | bounded among them |
|---|---|---|---|---|---|
| claude-opus-5 | bare | 1 of 1 | Crc32, LRU, FreeList, Paxos | 1.93 | 4 |
| claude-opus-5 | statement | 2 of 3 | LZW | 1.82 | 1 |
| claude-opus-5 | spec-change | 1 of 1 | Crc32, LRU, FreeList, Paxos | 2.03 | 5 |
| claude-sonnet-5 | bare | 5 of 5 | none | 18.47 | 2 |
| claude-sonnet-5 | statement | 4 of 4 | none | 8.65 | 0 |
| claude-sonnet-5 | spec-change | 2 of 2 | none | 8.08 | 0 |
| gemini-3.1-pro-high | bare | 5 of 5 | none | 8.13 | 1 |
| gemini-3.1-pro-high | statement | 4 of 4 | none | 11.42 | 2 |
| gemini-3.1-pro-high | spec-change | 4 of 4 | none | 5.79 | 1 |
| gemini-3.8-flash-high | bare | 1 of 1 | none | 8.62 | 0 |
| gemini-3.8-flash-high | statement | 1 of 1 | none | 3.85 | 0 |
| gemini-3.8-flash-high | spec-change | 0 of 0 | none | — | 0 |
