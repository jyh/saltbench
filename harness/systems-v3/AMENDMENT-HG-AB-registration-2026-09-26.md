# AMENDMENT — HG A + B: PLANTED-DEFECT + AUTONOMY (A) AND CHANGE (B), READ FROM THE COMPLETE PILOT. REGISTERED BEFORE THE FIRST SCAN
## bench (SaltBench lead), 2026-09-26. Commissioned by the helm under its delegation (fleet desk HG, option (i); the design brief is the
## lead's HG designs of 2026-09-26). **This file's commit sha must PRECEDE the first scan's output; the RESULT names it. A reading taken
## before this sha is EXPLORATORY and is labelled so.**

## §HG0 · WHAT IS BEING TESTED
The compounding claim, directly and without new cells: does the salt method change **whether a subject notices and documents a planted
defect in its requirements** (A), and **what a requirements change costs and breaks** (B)? No model call is made. Both read cells the pilot
already ran and scored.

## §HG1 · INSTRUMENT A — `ambiguity_scan.py` (saltbench-systems `harness/systems-v3/`, at the pilot's export e54f35a)
Per cell, over ONE text: `repo/LANDING.md` (where present) followed by `repo/BUS.md` (present in every cell of the population), against
the task's own `withheld/ambiguities.json`. Requirement
quotes are stripped by the scanner, so a text that quotes a requirement has not noticed an ambiguity. Per planted id the scanner reports
`detected` · the `resolutions` that hit · `wrong`. **Classes, derived per (cell, planted id), fixed here:**
```
  DOCUMENTED   detected AND ≥ 1 resolution hit AND no wrong hit      the seat noticed, chose, and wrote the choice down
  NOTICED      detected AND no resolution hit AND no wrong hit       noticed, choice not recorded in a resolution's words
  WRONG        any wrong hit                                          a recorded reading the task marks wrong
  SILENT       not detected                                           a FLOOR on noticing: the scan reads TEXT, not code
```
**AUTONOMY** is the same scan's second reading. The share of planted items a cell resolves as DOCUMENTED (a documented default) is set
against ASKED: a (cell, planted id) that is detected, has no resolution hit, and has at least one detect-hit LINE ending in `?`. No
operator exists in any cell, so an ask is never answered.

## §HG2 · INSTRUMENT B — the pilot's spec-change cells, from scores already of record
- **cost-to-change** = phase-2 cost ÷ phase-1 cost, per cell, each from the cell's own meter record.
- **correctness-after** = the phase-2 `REGRESSIONS p/t` and `CLAUSE_TESTS p/t` already scored per cell. **These are NOT RECORDED in any
  file for the Opus spec-change cells** (only a merged `tests` count exists), so **B2 is computed on the Sonnet and agy cells only**, and
  the Opus gap is printed beside it.
- **Cost units differ by lane:** USD for the Claude lane and tokens `T` per phase for the agy lane (no USD by that lane's rule). **B1 compares
  arms WITHIN a lane only, never across.**
⚠️ **B IS NOT BLIND, AND SAYS SO.** Its inputs, the per-cell scores and costs, are published in the pilot's results, and the lead has read
some of them in earlier work. This registration fixes B's ANALYSIS (the ratio, the population, the comparison) before the ratio is
computed; the ratio itself is not in any published file. B's predictions are therefore registered as analysis commitments, not as blind
outcome forecasts.

## §HG3 · THE POPULATION
Every cell of every DONE condition in the pilot census's current addendum (**181 conditions, 535 cells**, matching census ADDENDUM 24),
plus **HC1 stage 1's 45 cells** (the only placebo cells; census ADDENDUM 8 counts HC1 +0 to the grid, but A5 needs them). All are listed by
cell id in §HG6. They were appended from a read-only enumeration that opened NO cell's text: existence and byte size only. Where a condition
lists four cells (the Opus top-up conditions), all four are scanned.
**MISSINGNESS IS NOT NEUTRAL, AND THE RULE IS FIXED HERE:** 22 grid cells and 2 HC1 cells have no `LANDING.md`, and in the Sonnet lane they
are mostly salt-diet, largely cap stops. So **A1 and A2 are each reported TWO ways, both printed**: (i) over cells WITH a `LANDING.md`, and
(ii) over all cells, scanning `BUS.md` alone where `LANDING.md` is absent. Neither reading is dropped.
**B's population** is the spec-change subset (§HG6 second table: 47 conditions, 104 cells).

## §HG4 · PREDICTIONS — REGISTERED BEFORE ANY SCAN (A) AND BEFORE THE RATIO IS COMPUTED (B)
**A (blind):**
- **A1** Pooled over all conditions, salt-diet's DOCUMENTED share of planted items EXCEEDS plain's. **Falsified if** plain's pooled
  DOCUMENTED share ≥ salt-diet's.
- **A2** salt-diet's SILENT share is BELOW plain's. **Falsified if** it is ≥.
- **A3** WRONG is rare in both arms: under 10 % of planted items in each arm, pooled. **Falsified if** either arm reaches 10 %.
- **A4** ASKED is rare in both arms: under 5 % of cells in each. **Falsified if** either arm reaches 5 %.
- **A5** (HC1, the only placebo cells) placebo's DOCUMENTED share lies BETWEEN plain's and salt-diet's. It separates "told to write
  decisions" (placebo's text says "decision" most) from the method. **Falsified if** placebo ≥ salt-diet or placebo ≤ plain.

**B (analysis commitments, not blind):**
- **B1** salt-diet's median cost-to-change is BELOW plain's, within model. **Falsified if** it is ≥ in a majority of models with both arms.
- **B2** salt-diet's pooled REGRESSIONS pass share is ≥ plain's. **Falsified if** it is below.

**No prediction about models, problems or lanes against each other**, which none of these populations was drawn to compare.

## §HG5 · WHAT IS PRINTED BESIDE EVERY A/B READING
- **A reads TEXT, not behaviour**: SILENT is a floor on noticing, never proof of not noticing.
- **Both arms receive the same `LANDING.md` template and its `## DECISIONS` section.** The arm texts mention "decision" plain 4 ·
  salt-diet 4 · placebo 9, and "ambiguity" plain 1 · salt-diet 0 · placebo 1 (v3 `render/` at e54f35a).
- **B covers only the problems with a `B/` tree**, and is not blind (§HG2).
- **The detect patterns are cues, not concepts** (the scanner's own docstring). Differences between arms are the reading; absolute rates
  are not.

## §HG6 · THE POPULATION BY CELL ID
The scan's command, fixed: per cell `cat <cell>/repo/LANDING.md <cell>/repo/BUS.md > <text>` (LANDING.md omitted where absent), then
`python3 harness/systems-v3/ambiguity_scan.py <tasks>/<Problem> <text> --packet harness/systems-v3/packet`, with `<tasks>` and the
scanner both taken from a git archive of saltbench-systems e54f35a. One JSON object per cell is kept, and the RESULT is derived from those
JSONs alone.

**TABLE 1 — the population** (verbatim from the enumeration; `landing_path` is under the run box's home; `NF` = no LANDING.md; the models are
O claude-opus-5 · S claude-sonnet-5 · P gemini-3.1-pro-high · F gemini-3.8-flash-high; the fields are g/b; the extras none/stmt/sc):
```
condition_key	lane	cell_id	result_file	landing_path	landing_bytes	bus_exists	note
O|Crc32|g|plain|none	claude	2d0c65b3	MX	cells-matrix1/2d0c65b3	12945	Y
O|Crc32|g|plain|none	claude	746d7d4e	MX	cells-matrix1/746d7d4e	14610	Y
O|Crc32|g|plain|none	claude	a87b7740	MX	cells-matrix1/a87b7740	11739	Y
O|Crc32|g|salt-diet|none	claude	11165871	MX	cells-matrix1/11165871	10015	Y
O|Crc32|g|salt-diet|none	claude	3e95075c	MX	cells-matrix1/3e95075c	9198	Y
O|Crc32|g|salt-diet|none	claude	57a33630	MX	cells-matrix1/57a33630	8464	Y
O|FreeList|g|plain|none	claude	188f422b	MX	cells-matrix1/188f422b	13211	Y
O|FreeList|g|plain|none	claude	9cb8ce96	MX	cells-matrix1/9cb8ce96	14652	Y
O|FreeList|g|plain|none	claude	ae304f63	MX	cells/ae304f63	14323	Y	SS12 smoke cell
O|FreeList|g|plain|none	claude	n301free	MX	cells-n3-topup/n301free	14971	Y	top-up (readings A/B)
O|FreeList|g|salt-diet|none	claude	161b5a34	MX	NF	-	Y	CAP-COST; harvest-v3 copy also has no LANDING
O|FreeList|g|salt-diet|none	claude	de4de8f2	MX	cells-matrix1/de4de8f2	9354	Y
O|FreeList|g|salt-diet|none	claude	f33c7e65	MX	cells-matrix1/f33c7e65	11703	Y
O|LRU|g|plain|none	claude	3bdcbcbd	MX	cells-matrix1/3bdcbcbd	15261	Y
O|LRU|g|plain|none	claude	69e8c2c4	MX	cells-matrix1/69e8c2c4	18079	Y
O|LRU|g|plain|none	claude	a69e9131	MX	cells/a69e9131	13408	Y	SS12 smoke cell
O|LRU|g|plain|none	claude	n302lru	MX	cells-n3-topup/n302lru	13510	Y	top-up
O|LRU|g|salt-diet|none	claude	011fe22f	MX	cells-matrix1/011fe22f	11475	Y
O|LRU|g|salt-diet|none	claude	b71994e3	MX	cells-matrix1/b71994e3	11155	Y
O|LRU|g|salt-diet|none	claude	d6b53ee4	MX	cells-matrix1/d6b53ee4	12464	Y
O|LZW|g|plain|none	claude	93323249	MX	cells-matrix1/93323249	12470	Y
O|LZW|g|plain|none	claude	c34012e0	MX	cells-matrix1/c34012e0	13300	Y
O|LZW|g|plain|none	claude	d91f137b	MX	cells-matrix1/d91f137b	15625	Y
O|LZW|g|salt-diet|none	claude	18fb3eed	MX	cells-matrix1/18fb3eed	12135	Y
O|LZW|g|salt-diet|none	claude	7ac56e4e	MX	cells-matrix1/7ac56e4e	11152	Y
O|LZW|g|salt-diet|none	claude	eb558398	MX	cells-matrix1/eb558398	10014	Y
O|Paxos|g|plain|none	claude	60a056e6	MX	cells-matrix1/60a056e6	12963	Y
O|Paxos|g|plain|none	claude	f6462d47	MX	cells-matrix1/f6462d47	17588	Y
O|Paxos|g|plain|none	claude	b7537006	MX	cells/b7537006	18537	Y	SS12 smoke cell
O|Paxos|g|plain|none	claude	n303paxo	MX	cells-n3-topup/n303paxo	17556	Y	top-up
O|Paxos|g|salt-diet|none	claude	6fc49f7c	MX	cells-matrix1/6fc49f7c	10194	Y
O|Paxos|g|salt-diet|none	claude	9e6c8d4d	MX	cells-matrix1/9e6c8d4d	15858	Y
O|Paxos|g|salt-diet|none	claude	b22d1000	MX	cells-matrix1/b22d1000	9340	Y
O|Crc32|g|plain|stmt	claude	st01crc3	ST	cells-stmt-2026-09-09/st01crc3	10589	Y
O|Crc32|g|plain|stmt	claude	st02crc3	ST	cells-stmt-2026-09-09/st02crc3	11000	Y
O|Crc32|g|plain|stmt	claude	st03crc3	ST	cells-stmt-2026-09-09/st03crc3	11091	Y
O|Crc32|g|salt-diet|stmt	claude	st04crc3	ST	cells-stmt-2026-09-09/st04crc3	7015	Y
O|Crc32|g|salt-diet|stmt	claude	st05crc3	ST	cells-stmt-2026-09-09/st05crc3	8694	Y
O|Crc32|g|salt-diet|stmt	claude	st06crc3	ST	cells-stmt-2026-09-09/st06crc3	8088	Y
O|LRU|g|plain|stmt	claude	st07lru	ST	cells-stmt-2026-09-09/st07lru	13508	Y
O|LRU|g|plain|stmt	claude	st08lru	ST	cells-stmt-2026-09-09/st08lru	17848	Y
O|LRU|g|plain|stmt	claude	st09lru	ST	cells-stmt-2026-09-09/st09lru	14862	Y
O|LRU|g|salt-diet|stmt	claude	st10lru	ST	cells-stmt-2026-09-09/st10lru	14792	Y
O|LRU|g|salt-diet|stmt	claude	st11lru	ST	cells-stmt-2026-09-09/st11lru	11739	Y
O|LRU|g|salt-diet|stmt	claude	st12lru	ST	cells-stmt-2026-09-09/st12lru	10861	Y
O|FreeList|g|plain|stmt	claude	sf01free	ST	cells-stmt-free-2026-09-09/sf01free	18951	Y	id from tokens-table-all-roots:58
O|FreeList|g|plain|stmt	claude	sf02free	ST	cells-stmt-free-2026-09-09/sf02free	14343	Y	id from tokens-table-all-roots:59
O|FreeList|g|plain|stmt	claude	sf03free	ST	cells-stmt-free-2026-09-09/sf03free	13216	Y	id from tokens-table-all-roots:60
O|FreeList|g|salt-diet|stmt	claude	sf04free	ST	cells-stmt-free-2026-09-09/sf04free	11127	Y
O|FreeList|g|salt-diet|stmt	claude	sf05free	ST	cells-stmt-free-2026-09-09/sf05free	13041	Y
O|FreeList|g|salt-diet|stmt	claude	sf06free	ST	cells-stmt-free-2026-09-09/sf06free	9358	Y
O|LZW|g|plain|stmt	claude	22ee7d33	MX gold pair	cells-matrix1/22ee7d33	12270	Y
O|LZW|g|plain|stmt	claude	922d1ff0	MX gold pair	cells-matrix1/922d1ff0	15122	Y
O|LZW|g|plain|stmt	claude	f795e96f	MX gold pair	cells-matrix1/f795e96f	10647	Y
O|LZW|g|salt-diet|stmt	claude	6d58f1ec	MX gold pair	cells-matrix1/6d58f1ec	11798	Y
O|LZW|g|salt-diet|stmt	claude	9aca67c5	MX gold pair	cells-matrix1/9aca67c5	11793	Y
O|LZW|g|salt-diet|stmt	claude	f5f66c47	MX gold pair	cells-matrix1/f5f66c47	9379	Y
O|Crc32|g|plain|sc	claude	2d0c65b3	PS	cells-specchange-2/2d0c65b3	25919	Y	phase-2 root; phase-1 is cells-matrix1/<id>
O|Crc32|g|plain|sc	claude	746d7d4e	PS	cells-specchange-2/746d7d4e	30882	Y	ditto
O|Crc32|g|plain|sc	claude	a87b7740	PS	cells-specchange-2/a87b7740	29861	Y	ditto
O|Crc32|g|salt-diet|sc	claude	11165871	PS	cells-specchange-2/11165871	17336	Y	ditto
O|Crc32|g|salt-diet|sc	claude	3e95075c	PS	cells-specchange-2/3e95075c	20247	Y	ditto
O|Crc32|g|salt-diet|sc	claude	57a33630	PS	cells-specchange-2/57a33630	12483	Y	ditto
O|FreeList|g|plain|sc	claude	188f422b	PS	cells-specchange-2/188f422b	21815	Y	ditto
O|FreeList|g|plain|sc	claude	9cb8ce96	PS	cells-specchange-2/9cb8ce96	21680	Y	ditto
O|FreeList|g|salt-diet|sc	claude	f33c7e65	PS	cells-specchange-2/f33c7e65	17954	Y	condition n=1
O|LRU|g|plain|sc	claude	3bdcbcbd	PS	cells-specchange-2/3bdcbcbd	29515	Y
O|LRU|g|plain|sc	claude	69e8c2c4	PS	cells-specchange-2/69e8c2c4	32214	Y
O|LRU|g|salt-diet|sc	claude	011fe22f	PS	cells-specchange-2/011fe22f	17423	Y
O|LRU|g|salt-diet|sc	claude	b71994e3	PS	cells-specchange-2/b71994e3	19163	Y
O|LRU|g|salt-diet|sc	claude	d6b53ee4	PS	cells-specchange-2/d6b53ee4	18684	Y
O|LZW|g|salt-diet|sc	claude	7ac56e4e	PS	cells-specchange-2/7ac56e4e	10451	Y
O|LZW|g|salt-diet|sc	claude	18fb3eed	S1	cells-specchange-1/18fb3eed	10484	Y	LZW pilot
O|LZW|g|salt-diet|sc	claude	6d58f1ec	S1	cells-specchange-1/6d58f1ec	11798	Y	pilot; parent is a statement cell; CAP-COST
O|LZW|g|plain|sc	claude	93323249	S1	cells-specchange-1/93323249	16172	Y	pilot
O|LZW|g|plain|sc	claude	22ee7d33	S1	cells-specchange-1/22ee7d33	15462	Y	pilot; parent is a statement cell
O|Paxos|g|plain|sc	claude	60a056e6	PS	cells-specchange-2/60a056e6	16771	Y
O|Paxos|g|plain|sc	claude	f6462d47	PS	cells-specchange-2/f6462d47	14858	Y	CAP-COST
O|Paxos|g|salt-diet|sc	claude	9e6c8d4d	PS	cells-specchange-2/9e6c8d4d	15858	Y	CAP-COST
O|Paxos|g|salt-diet|sc	claude	b22d1000	PS	cells-specchange-2/b22d1000	9340	Y	CAP-COST
O|Crc32|b|plain|none	claude	clbocp01	BO	cells-clb-o-crc32-plain/clbocp01	14120	Y
O|Crc32|b|plain|none	claude	clbocp02	BO	cells-clb-o-crc32-plain/clbocp02	15367	Y
O|Crc32|b|plain|none	claude	clbocp03	BO	cells-clb-o-crc32-plain/clbocp03	13190	Y
O|Crc32|b|salt-diet|none	claude	clbocs01	BO	cells-clb-o-crc32-saltdiet/clbocs01	9992	Y
O|Crc32|b|salt-diet|none	claude	clbocs02	BO	cells-clb-o-crc32-saltdiet/clbocs02	9630	Y
O|Crc32|b|salt-diet|none	claude	clbocs03	BO	cells-clb-o-crc32-saltdiet/clbocs03	9226	Y
O|FreeList|b|plain|none	claude	clbofp01	BO	cells-clb-o-freelist-plain/clbofp01	23928	Y
O|FreeList|b|plain|none	claude	clbofp02	BO	cells-clb-o-freelist-plain/clbofp02	12021	Y
O|FreeList|b|plain|none	claude	clbofp03	BO	cells-clb-o-freelist-plain/clbofp03	15886	Y
O|FreeList|b|salt-diet|none	claude	clbofs01	BO	cells-clb-o-freelist-saltdiet/clbofs01	13026	Y
O|FreeList|b|salt-diet|none	claude	clbofs02	BO	NF	-	Y
O|FreeList|b|salt-diet|none	claude	clbofs03	BO	cells-clb-o-freelist-saltdiet/clbofs03	15108	Y
O|LRU|b|plain|none	claude	clbolp01	BO	cells-clb-o-lru-plain/clbolp01	13818	Y
O|LRU|b|plain|none	claude	clbolp02	BO	cells-clb-o-lru-plain/clbolp02	14663	Y
O|LRU|b|plain|none	claude	clbolp03	BO	cells-clb-o-lru-plain/clbolp03	13348	Y
O|LRU|b|salt-diet|none	claude	clbols01	BO	cells-clb-o-lru-saltdiet/clbols01	12982	Y
O|LRU|b|salt-diet|none	claude	clbols02	BO	cells-clb-o-lru-saltdiet/clbols02	11355	Y
O|LRU|b|salt-diet|none	claude	clbols03	BO	cells-clb-o-lru-saltdiet/clbols03	14104	Y
O|LZW|b|plain|none	claude	clbozp01	BO	cells-clb-o-lzw-plain/clbozp01	14958	Y
O|LZW|b|plain|none	claude	clbozp02	BO	cells-clb-o-lzw-plain/clbozp02	17347	Y
O|LZW|b|plain|none	claude	clbozp03	BO	cells-clb-o-lzw-plain/clbozp03	12497	Y
O|LZW|b|salt-diet|none	claude	clbozs01	BO	cells-clb-o-lzw-saltdiet/clbozs01	11280	Y
O|LZW|b|salt-diet|none	claude	clbozs02	BO	cells-clb-o-lzw-saltdiet/clbozs02	10900	Y
O|LZW|b|salt-diet|none	claude	clbozs03	BO	cells-clb-o-lzw-saltdiet/clbozs03	11391	Y
O|Paxos|b|plain|none	claude	clbopp01	BO	cells-clb-o-paxos-plain/clbopp01	17992	Y
O|Paxos|b|plain|none	claude	clbopp02	BO	cells-clb-o-paxos-plain/clbopp02	13695	Y
O|Paxos|b|plain|none	claude	clbopp03	BO	cells-clb-o-paxos-plain/clbopp03	11961	Y
O|Paxos|b|salt-diet|none	claude	clbops01	BO	cells-clb-o-paxos-saltdiet/clbops01	14490	Y
O|Paxos|b|salt-diet|none	claude	clbops02	BO	cells-clb-o-paxos-saltdiet/clbops02	9164	Y
O|Paxos|b|salt-diet|none	claude	clbops03	BO	cells-clb-o-paxos-saltdiet/clbops03	10885	Y
O|Crc32|b|plain|stmt	claude	clbtcp01	BOS	cells-clb-os-crc32-plain/clbtcp01	20357	Y
O|Crc32|b|plain|stmt	claude	clbtcp02	BOS	cells-clb-os-crc32-plain/clbtcp02	12093	Y	re-fired 09-22, export eb18e5d7769b
O|Crc32|b|plain|stmt	claude	clbtcp03	BOS	cells-clb-os-crc32-plain/clbtcp03	20005	Y	re-fired 09-22, export eb18e5d7769b
O|Crc32|b|salt-diet|stmt	claude	clbtcs01	BOS	cells-clb-os-crc32-saltdiet/clbtcs01	9704	Y
O|Crc32|b|salt-diet|stmt	claude	clbtcs02	BOS	cells-clb-os-crc32-saltdiet/clbtcs02	10267	Y
O|Crc32|b|salt-diet|stmt	claude	clbtcs03	BOS	cells-clb-os-crc32-saltdiet/clbtcs03	9199	Y
O|FreeList|b|plain|stmt	claude	clbtfp01	BOS	cells-clb-os-freelist-plain/clbtfp01	15984	Y
O|FreeList|b|plain|stmt	claude	clbtfp02	BOS	cells-clb-os-freelist-plain/clbtfp02	19240	Y
O|FreeList|b|plain|stmt	claude	clbtfp03	BOS	cells-clb-os-freelist-plain/clbtfp03	15182	Y
O|FreeList|b|salt-diet|stmt	claude	clbtfs01	BOS	cells-clb-os-freelist-saltdiet/clbtfs01	17333	Y
O|FreeList|b|salt-diet|stmt	claude	clbtfs02	BOS	cells-clb-os-freelist-saltdiet/clbtfs02	15133	Y
O|FreeList|b|salt-diet|stmt	claude	clbtfs03	BOS	cells-clb-os-freelist-saltdiet/clbtfs03	10971	Y
O|LRU|b|plain|stmt	claude	clbtlp01	BOS	cells-clb-os-lru-plain/clbtlp01	19314	Y
O|LRU|b|plain|stmt	claude	clbtlp02	BOS	cells-clb-os-lru-plain/clbtlp02	15199	Y
O|LRU|b|plain|stmt	claude	clbtlp03	BOS	cells-clb-os-lru-plain/clbtlp03	15094	Y
O|LRU|b|salt-diet|stmt	claude	clbtls01	BOS	cells-clb-os-lru-saltdiet/clbtls01	15560	Y
O|LRU|b|salt-diet|stmt	claude	clbtls02	BOS	cells-clb-os-lru-saltdiet/clbtls02	12788	Y
O|LRU|b|salt-diet|stmt	claude	clbtls03	BOS	cells-clb-os-lru-saltdiet/clbtls03	12040	Y
O|LZW|b|plain|stmt	claude	clbtzp01	BOS	cells-clb-os-lzw-plain/clbtzp01	16153	Y
O|LZW|b|plain|stmt	claude	clbtzp02	BOS	cells-clb-os-lzw-plain/clbtzp02	15134	Y
O|LZW|b|plain|stmt	claude	clbtzp03	BOS	cells-clb-os-lzw-plain/clbtzp03	19600	Y
O|LZW|b|salt-diet|stmt	claude	clbtzs01	BOS	cells-clb-os-lzw-saltdiet/clbtzs01	13609	Y
O|LZW|b|salt-diet|stmt	claude	clbtzs02	BOS	cells-clb-os-lzw-saltdiet/clbtzs02	10302	Y
O|LZW|b|salt-diet|stmt	claude	clbtzs03	BOS	cells-clb-os-lzw-saltdiet/clbtzs03	11116	Y
S|Crc32|b|plain|none	claude	clbbcp01	BSB	cells-clb-sb-crc32-plain/clbbcp01	5158	Y
S|Crc32|b|plain|none	claude	clbbcp02	BSB	cells-clb-sb-crc32-plain/clbbcp02	4407	Y
S|Crc32|b|plain|none	claude	clbbcp03	BSB	cells-clb-sb-crc32-plain/clbbcp03	5101	Y
S|Crc32|b|salt-diet|none	claude	clbbcs01	BSB	cells-clb-sb-crc32-saltdiet/clbbcs01	4437	Y
S|Crc32|b|salt-diet|none	claude	clbbcs02	BSB	cells-clb-sb-crc32-saltdiet/clbbcs02	6517	Y
S|Crc32|b|salt-diet|none	claude	clbbcs03	BSB	cells-clb-sb-crc32-saltdiet/clbbcs03	3563	Y
S|FreeList|b|plain|none	claude	clbbfp01	BSB	cells-clb-sb-freelist-plain/clbbfp01	9481	Y
S|FreeList|b|plain|none	claude	clbbfp02	BSB	cells-clb-sb-freelist-plain/clbbfp02	7341	Y
S|FreeList|b|plain|none	claude	clbbfp03	BSB	cells-clb-sb-freelist-plain/clbbfp03	6284	Y
S|FreeList|b|salt-diet|none	claude	clbbfs01	BSB	NF	-	Y
S|FreeList|b|salt-diet|none	claude	clbbfs02	BSB	cells-clb-sb-freelist-saltdiet/clbbfs02	9093	Y
S|FreeList|b|salt-diet|none	claude	clbbfs03	BSB	NF	-	Y
S|LRU|b|plain|none	claude	clbblp01	BSB	cells-clb-sb-lru-plain/clbblp01	3647	Y
S|LRU|b|plain|none	claude	clbblp02	BSB	cells-clb-sb-lru-plain/clbblp02	4524	Y
S|LRU|b|plain|none	claude	clbblp03	BSB	cells-clb-sb-lru-plain/clbblp03	3918	Y
S|LRU|b|salt-diet|none	claude	clbbls01	BSB	cells-clb-sb-lru-saltdiet/clbbls01	4980	Y
S|LRU|b|salt-diet|none	claude	clbbls02	BSB	cells-clb-sb-lru-saltdiet/clbbls02	5877	Y
S|LRU|b|salt-diet|none	claude	clbbls03	BSB	cells-clb-sb-lru-saltdiet/clbbls03	4837	Y
S|LZW|b|plain|none	claude	clbbzp01	BSB	cells-clb-sb-lzw-plain/clbbzp01	7095	Y
S|LZW|b|plain|none	claude	clbbzp02	BSB	cells-clb-sb-lzw-plain/clbbzp02	8661	Y
S|LZW|b|plain|none	claude	clbbzp03	BSB	cells-clb-sb-lzw-plain/clbbzp03	4638	Y
S|LZW|b|salt-diet|none	claude	clbbzs01	BSB	cells-clb-sb-lzw-saltdiet/clbbzs01	7143	Y
S|LZW|b|salt-diet|none	claude	clbbzs02	BSB	cells-clb-sb-lzw-saltdiet/clbbzs02	6578	Y
S|LZW|b|salt-diet|none	claude	clbbzs03	BSB	cells-clb-sb-lzw-saltdiet/clbbzs03	5105	Y
S|Paxos|b|plain|none	claude	clbbpp01	BSB	cells-clb-sb-paxos-plain/clbbpp01	8537	Y
S|Paxos|b|plain|none	claude	clbbpp02	BSB	cells-clb-sb-paxos-plain/clbbpp02	8307	Y
S|Paxos|b|plain|none	claude	clbbpp03	BSB	cells-clb-sb-paxos-plain/clbbpp03	6295	Y
S|Paxos|b|salt-diet|none	claude	clbbps01	BSB	NF	-	Y
S|Paxos|b|salt-diet|none	claude	clbbps02	BSB	NF	-	Y
S|Paxos|b|salt-diet|none	claude	clbbps03	BSB	NF	-	Y
S|Crc32|g|plain|none	claude	clbgcp01	BSG	cells-clb-sg-crc32-plain/clbgcp01	4865	Y
S|Crc32|g|plain|none	claude	clbgcp02	BSG	cells-clb-sg-crc32-plain/clbgcp02	3839	Y
S|Crc32|g|plain|none	claude	clbgcp03	BSG	cells-clb-sg-crc32-plain/clbgcp03	4384	Y
S|Crc32|g|salt-diet|none	claude	clbgcs01	BSG	cells-clb-sg-crc32-saltdiet/clbgcs01	5263	Y
S|Crc32|g|salt-diet|none	claude	clbgcs02	BSG	cells-clb-sg-crc32-saltdiet/clbgcs02	5331	Y
S|Crc32|g|salt-diet|none	claude	clbgcs03	BSG	cells-clb-sg-crc32-saltdiet/clbgcs03	4616	Y
S|FreeList|g|plain|none	claude	clbgfp01	BSG	cells-clb-sg-freelist-plain/clbgfp01	7312	Y
S|FreeList|g|plain|none	claude	clbgfp02	BSG	cells-clb-sg-freelist-plain/clbgfp02	4720	Y
S|FreeList|g|plain|none	claude	clbgfp03	BSG	cells-clb-sg-freelist-plain/clbgfp03	6444	Y
S|FreeList|g|salt-diet|none	claude	clbgfs01	BSG	NF	-	Y
S|FreeList|g|salt-diet|none	claude	clbgfs02	BSG	NF	-	Y	BUILD-FAIL + CAP-COST, in no denominator
S|FreeList|g|salt-diet|none	claude	clbgfs03	BSG	NF	-	Y
S|LRU|g|plain|none	claude	clbglp01	BSG	cells-clb-sg-lru-plain/clbglp01	4602	Y	DECLARED-EXCLUDED (no served-*.out); condition n=2
S|LRU|g|plain|none	claude	clbglp02	BSG	cells-clb-sg-lru-plain/clbglp02	6725	Y
S|LRU|g|plain|none	claude	clbglp03	BSG	cells-clb-sg-lru-plain/clbglp03	4603	Y
S|LRU|g|salt-diet|none	claude	clbgls01	BSG	cells-clb-sg-lru-saltdiet/clbgls01	5726	Y
S|LRU|g|salt-diet|none	claude	clbgls02	BSG	cells-clb-sg-lru-saltdiet/clbgls02	4977	Y
S|LRU|g|salt-diet|none	claude	clbgls03	BSG	cells-clb-sg-lru-saltdiet/clbgls03	5545	Y
S|LZW|g|plain|none	claude	clbgzp01	BSG	cells-clb-sg-lzw-plain/clbgzp01	6006	Y
S|LZW|g|plain|none	claude	clbgzp02	BSG	cells-clb-sg-lzw-plain/clbgzp02	6127	Y
S|LZW|g|plain|none	claude	clbgzp03	BSG	cells-clb-sg-lzw-plain/clbgzp03	6718	Y
S|LZW|g|salt-diet|none	claude	clbgzs01	BSG	cells-clb-sg-lzw-saltdiet/clbgzs01	7624	Y
S|LZW|g|salt-diet|none	claude	clbgzs02	BSG	cells-clb-sg-lzw-saltdiet/clbgzs02	6036	Y
S|LZW|g|salt-diet|none	claude	clbgzs03	BSG	cells-clb-sg-lzw-saltdiet/clbgzs03	5856	Y
S|Paxos|g|plain|none	claude	clbgpp01	BSG	cells-clb-sg-paxos-plain/clbgpp01	9097	Y
S|Paxos|g|plain|none	claude	clbgpp02	BSG	cells-clb-sg-paxos-plain/clbgpp02	6175	Y
S|Paxos|g|plain|none	claude	clbgpp03	BSG	cells-clb-sg-paxos-plain/clbgpp03	9916	Y
S|Paxos|g|salt-diet|none	claude	clbgps01	BSG	NF	-	Y
S|Paxos|g|salt-diet|none	claude	clbgps02	BSG	NF	-	Y
S|Paxos|g|salt-diet|none	claude	clbgps03	BSG	cells-clb-sg-paxos-saltdiet/clbgps03	5132	Y
S|Crc32|g|plain|stmt	claude	clbscp01	BSS	cells-clb-ss-crc32-plain/clbscp01	4500	Y
S|Crc32|g|plain|stmt	claude	clbscp02	BSS	cells-clb-ss-crc32-plain/clbscp02	4557	Y
S|Crc32|g|plain|stmt	claude	clbscp03	BSS	cells-clb-ss-crc32-plain/clbscp03	5369	Y
S|Crc32|g|salt-diet|stmt	claude	clbscs01	BSS	cells-clb-ss-crc32-saltdiet/clbscs01	4996	Y
S|Crc32|g|salt-diet|stmt	claude	clbscs02	BSS	cells-clb-ss-crc32-saltdiet/clbscs02	4216	Y
S|Crc32|g|salt-diet|stmt	claude	clbscs03	BSS	cells-clb-ss-crc32-saltdiet/clbscs03	5413	Y
S|FreeList|g|plain|stmt	claude	clbsfp01	BSS	cells-clb-ss-freelist-plain/clbsfp01	7566	Y
S|FreeList|g|plain|stmt	claude	clbsfp02	BSS	cells-clb-ss-freelist-plain/clbsfp02	6544	Y
S|FreeList|g|plain|stmt	claude	clbsfp03	BSS	cells-clb-ss-freelist-plain/clbsfp03	8307	Y
S|FreeList|g|salt-diet|stmt	claude	clbsfs01	BSS	cells-clb-ss-freelist-saltdiet/clbsfs01	11985	Y
S|FreeList|g|salt-diet|stmt	claude	clbsfs02	BSS	NF	-	Y
S|FreeList|g|salt-diet|stmt	claude	clbsfs03	BSS	cells-clb-ss-freelist-saltdiet/clbsfs03	7350	Y
S|LRU|g|plain|stmt	claude	clbslp01	BSS	cells-clb-ss-lru-plain/clbslp01	5106	Y
S|LRU|g|plain|stmt	claude	clbslp02	BSS	cells-clb-ss-lru-plain/clbslp02	6119	Y
S|LRU|g|plain|stmt	claude	clbslp03	BSS	cells-clb-ss-lru-plain/clbslp03	5802	Y
S|LRU|g|salt-diet|stmt	claude	clbsls01	BSS	cells-clb-ss-lru-saltdiet/clbsls01	4336	Y
S|LRU|g|salt-diet|stmt	claude	clbsls02	BSS	cells-clb-ss-lru-saltdiet/clbsls02	6479	Y
S|LRU|g|salt-diet|stmt	claude	clbsls03	BSS	cells-clb-ss-lru-saltdiet/clbsls03	4385	Y
S|LZW|g|plain|stmt	claude	clbszp01	BSS	cells-clb-ss-lzw-plain/clbszp01	5733	Y
S|LZW|g|plain|stmt	claude	clbszp02	BSS	cells-clb-ss-lzw-plain/clbszp02	5908	Y
S|LZW|g|plain|stmt	claude	clbszp03	BSS	cells-clb-ss-lzw-plain/clbszp03	7354	Y
S|LZW|g|salt-diet|stmt	claude	clbszs01	BSS	cells-clb-ss-lzw-saltdiet/clbszs01	6389	Y
S|LZW|g|salt-diet|stmt	claude	clbszs02	BSS	NF	-	Y
S|LZW|g|salt-diet|stmt	claude	clbszs03	BSS	cells-clb-ss-lzw-saltdiet/clbszs03	5654	Y
S|Crc32|b|plain|stmt	claude	clbucp01	BSBS	cells-clb-sbs-crc32-plain/clbucp01	6043	Y
S|Crc32|b|plain|stmt	claude	clbucp02	BSBS	cells-clb-sbs-crc32-plain/clbucp02	5226	Y
S|Crc32|b|plain|stmt	claude	clbucp03	BSBS	cells-clb-sbs-crc32-plain/clbucp03	4650	Y
S|Crc32|b|salt-diet|stmt	claude	clbucs01	BSBS	cells-clb-sbs-crc32-saltdiet/clbucs01	4063	Y
S|Crc32|b|salt-diet|stmt	claude	clbucs02	BSBS	cells-clb-sbs-crc32-saltdiet/clbucs02	5850	Y
S|Crc32|b|salt-diet|stmt	claude	clbucs03	BSBS	cells-clb-sbs-crc32-saltdiet/clbucs03	5779	Y
S|FreeList|b|plain|stmt	claude	clbufp01	BSBS	cells-clb-sbs-freelist-plain/clbufp01	6630	Y
S|FreeList|b|plain|stmt	claude	clbufp02	BSBS	cells-clb-sbs-freelist-plain/clbufp02	8671	Y
S|FreeList|b|plain|stmt	claude	clbufp03	BSBS	cells-clb-sbs-freelist-plain/clbufp03	7180	Y
S|FreeList|b|salt-diet|stmt	claude	clbufs01	BSBS	NF	-	Y
S|FreeList|b|salt-diet|stmt	claude	clbufs02	BSBS	NF	-	Y
S|FreeList|b|salt-diet|stmt	claude	clbufs03	BSBS	NF	-	Y
S|LRU|b|plain|stmt	claude	clbulp01	BSBS	cells-clb-sbs-lru-plain/clbulp01	5362	Y
S|LRU|b|plain|stmt	claude	clbulp02	BSBS	cells-clb-sbs-lru-plain/clbulp02	5235	Y
S|LRU|b|plain|stmt	claude	clbulp03	BSBS	cells-clb-sbs-lru-plain/clbulp03	4426	Y
S|LRU|b|salt-diet|stmt	claude	clbuls01	BSBS	cells-clb-sbs-lru-saltdiet/clbuls01	5849	Y
S|LRU|b|salt-diet|stmt	claude	clbuls02	BSBS	cells-clb-sbs-lru-saltdiet/clbuls02	6428	Y
S|LRU|b|salt-diet|stmt	claude	clbuls03	BSBS	cells-clb-sbs-lru-saltdiet/clbuls03	5120	Y
S|LZW|b|plain|stmt	claude	clbuzp01	BSBS	cells-clb-sbs-lzw-plain/clbuzp01	7737	Y
S|LZW|b|plain|stmt	claude	clbuzp02	BSBS	cells-clb-sbs-lzw-plain/clbuzp02	8353	Y
S|LZW|b|plain|stmt	claude	clbuzp03	BSBS	cells-clb-sbs-lzw-plain/clbuzp03	6253	Y
S|LZW|b|salt-diet|stmt	claude	clbuzs01	BSBS	cells-clb-sbs-lzw-saltdiet/clbuzs01	6459	Y
S|LZW|b|salt-diet|stmt	claude	clbuzs02	BSBS	cells-clb-sbs-lzw-saltdiet/clbuzs02	5282	Y
S|LZW|b|salt-diet|stmt	claude	clbuzs03	BSBS	cells-clb-sbs-lzw-saltdiet/clbuzs03	5369	Y
S|Crc32|g|plain|sc	claude	clbccp01	BSC	cells-clb-sc-crc32-plain/clbccp01	9263	Y
S|Crc32|g|plain|sc	claude	clbccp02	BSC	cells-clb-sc-crc32-plain/clbccp02	10102	Y
S|Crc32|g|plain|sc	claude	clbccp03	BSC	cells-clb-sc-crc32-plain/clbccp03	10569	Y
S|Crc32|g|salt-diet|sc	claude	clbccs01	BSC	cells-clb-sc-crc32-saltdiet/clbccs01	8274	Y
S|Crc32|g|salt-diet|sc	claude	clbccs02	BSC	cells-clb-sc-crc32-saltdiet/clbccs02	10492	Y
S|Crc32|g|salt-diet|sc	claude	clbccs03	BSC	cells-clb-sc-crc32-saltdiet/clbccs03	10292	Y
S|FreeList|g|plain|sc	claude	clbcfp01	BSC	cells-clb-sc-freelist-plain/clbcfp01	10348	Y
S|FreeList|g|plain|sc	claude	clbcfp02	BSC	cells-clb-sc-freelist-plain/clbcfp02	10682	Y
S|FreeList|g|plain|sc	claude	clbcfp03	BSC	cells-clb-sc-freelist-plain/clbcfp03	13479	Y
S|LRU|g|plain|sc	claude	clbclp01	BSC	cells-clb-sc-lru-plain/clbclp01	8377	Y
S|LRU|g|plain|sc	claude	clbclp02	BSC	cells-clb-sc-lru-plain/clbclp02	5927	Y
S|LRU|g|plain|sc	claude	clbclp03	BSC	cells-clb-sc-lru-plain/clbclp03	6895	Y
S|LRU|g|salt-diet|sc	claude	clbcls01	BSC	cells-clb-sc-lru-saltdiet/clbcls01	9573	Y
S|LRU|g|salt-diet|sc	claude	clbcls02	BSC	cells-clb-sc-lru-saltdiet/clbcls02	8166	Y
S|LRU|g|salt-diet|sc	claude	clbcls03	BSC	cells-clb-sc-lru-saltdiet/clbcls03	9650	Y
S|LZW|g|plain|sc	claude	clbczp01	BSC	cells-clb-sc-lzw-plain/clbczp01	7464	Y
S|LZW|g|plain|sc	claude	clbczp02	BSC	cells-clb-sc-lzw-plain/clbczp02	11730	Y
S|LZW|g|plain|sc	claude	clbczp03	BSC	cells-clb-sc-lzw-plain/clbczp03	15247	Y
S|Paxos|g|plain|sc	claude	clbcpp01	BSC	cells-clb-sc-paxos-plain/clbcpp01	12882	Y
S|Paxos|g|plain|sc	claude	clbcpp02	BSC	cells-clb-sc-paxos-plain/clbcpp02	10153	Y
S|Paxos|g|plain|sc	claude	clbcpp03	BSC	cells-clb-sc-paxos-plain/clbcpp03	16078	Y
P|Crc32|g|plain|none	agy	s3cp01	L1	cells-s3-crc32-plain/s3cp01	995	Y
P|Crc32|g|plain|none	agy	s3cp02	L1	cells-s3-crc32-plain/s3cp02	896	Y
P|Crc32|g|plain|none	agy	s3cp03	L1	cells-s3-crc32-plain/s3cp03	828	Y
P|Crc32|g|salt-diet|none	agy	s3cs01	L1	cells-s3-crc32-saltdiet/s3cs01	725	Y
P|Crc32|g|salt-diet|none	agy	s3cs02	L1	cells-s3-crc32-saltdiet/s3cs02	542	Y
P|Crc32|g|salt-diet|none	agy	s3cs03	L1	cells-s3-crc32-saltdiet/s3cs03	1101	Y
P|LRU|g|plain|none	agy	s3lp01	L1	cells-s3-lru-plain/s3lp01	1037	Y
P|LRU|g|plain|none	agy	s3lp02	L1	cells-s3-lru-plain/s3lp02	1621	Y
P|LRU|g|plain|none	agy	s3lp03	L1	cells-s3-lru-plain/s3lp03	1175	Y
P|LRU|g|salt-diet|none	agy	s3ls01	L1	cells-s3-lru-saltdiet/s3ls01	307	Y	end PERSIS (not landed), scored PASS
P|LRU|g|salt-diet|none	agy	s3ls02	L1	cells-s3-lru-saltdiet/s3ls02	419	Y
P|LRU|g|salt-diet|none	agy	s3ls03	L1	cells-s3-lru-saltdiet/s3ls03	717	Y
P|FreeList|g|plain|none	agy	s3fp01	L1	cells-s3-freelist-plain/s3fp01	2351	Y	only scorable cell; condition n=1
P|FreeList|g|salt-diet|none	agy	s3fs01	L1	cells-s3-freelist-saltdiet/s3fs01	1165	Y
P|FreeList|g|salt-diet|none	agy	s3fs02	L1	cells-s3-freelist-saltdiet/s3fs02	1675	Y
P|FreeList|g|salt-diet|none	agy	s3fs03	L1	cells-s3-freelist-saltdiet/s3fs03	2442	Y
P|Paxos|g|plain|none	agy	s3pp01	L1	cells-s3-paxos-plain/s3pp01	1497	Y
P|Paxos|g|plain|none	agy	s3pp02	L1	cells-s3-paxos-plain/s3pp02	901	Y
P|Paxos|g|plain|none	agy	s3pp03	L1	cells-s3-paxos-plain/s3pp03	2909	Y
P|Paxos|g|salt-diet|none	agy	s3ps01	L1	cells-s3-paxos-saltdiet/s3ps01	871	Y
P|Paxos|g|salt-diet|none	agy	s3ps02	L1	NF	-	Y	NOT-LANDED, in the score receipt
P|Paxos|g|salt-diet|none	agy	s3ps03	L1	NF	-	Y	NOT-LANDED, in the score receipt
P|Crc32|g|plain|stmt	agy	s3cq01	L1	cells-s3-crc32-plain-stmt/s3cq01	715	Y
P|Crc32|g|plain|stmt	agy	s3cq02	L1	cells-s3-crc32-plain-stmt/s3cq02	871	Y
P|Crc32|g|plain|stmt	agy	s3cq03	L1	cells-s3-crc32-plain-stmt/s3cq03	795	Y
P|Crc32|g|salt-diet|stmt	agy	s3ct01	L1	cells-s3-crc32-saltdiet-stmt/s3ct01	1813	Y
P|Crc32|g|salt-diet|stmt	agy	s3ct02	L1	cells-s3-crc32-saltdiet-stmt/s3ct02	1142	Y	condition n=2
P|LRU|g|plain|stmt	agy	s3lq01	L1	cells-s3-lru-plain-stmt/s3lq01	1140	Y
P|LRU|g|plain|stmt	agy	s3lq02	L1	cells-s3-lru-plain-stmt/s3lq02	993	Y
P|LRU|g|plain|stmt	agy	s3lq03	L1	cells-s3-lru-plain-stmt/s3lq03	1741	Y
P|LRU|g|salt-diet|stmt	agy	s3lt01	L1	cells-s3-lru-saltdiet-stmt/s3lt01	1382	Y
P|LRU|g|salt-diet|stmt	agy	s3lt02	L1	cells-s3-lru-saltdiet-stmt/s3lt02	1486	Y
P|LRU|g|salt-diet|stmt	agy	s3lt03	L1	cells-s3-lru-saltdiet-stmt/s3lt03	1248	Y
P|FreeList|g|plain|stmt	agy	s3fq01	L1	cells-s3-freelist-plain-stmt/s3fq01	1250	Y
P|FreeList|g|plain|stmt	agy	s3fq02	L1	cells-s3-freelist-plain-stmt/s3fq02	1470	Y	condition n=2
P|FreeList|g|salt-diet|stmt	agy	s3ft01	L1	cells-s3-freelist-saltdiet-stmt/s3ft01	1936	Y
P|FreeList|g|salt-diet|stmt	agy	s3ft02	L1	NF	-	Y	NOT-LANDED, in the score receipt
P|FreeList|g|salt-diet|stmt	agy	s3ft03	L1	NF	-	Y	NOT-LANDED, in the score receipt
P|LRU|b|plain|none	agy	b4lrp01	L4	cells-b4-lru-plain/b4lrp01	1387	Y
P|LRU|b|plain|none	agy	b4lrp02	L4	cells-b4-lru-plain/b4lrp02	952	Y
P|LRU|b|plain|none	agy	b4lrp03	L4	cells-b4-lru-plain/b4lrp03	806	Y
P|LRU|b|salt-diet|none	agy	b4lrs01	L4	cells-b4-lru-saltdiet/b4lrs01	450	Y
P|LRU|b|salt-diet|none	agy	b4lrs02	L4	cells-b4-lru-saltdiet/b4lrs02	856	Y
P|LRU|b|salt-diet|none	agy	b4lrs03	L4	cells-b4-lru-saltdiet/b4lrs03	597	Y
P|Paxos|b|plain|none	agy	b4pp01	L4	cells-b4-paxos-plain/b4pp01	1043	Y
P|Paxos|b|plain|none	agy	b4pp02	L4	cells-b4-paxos-plain/b4pp02	1768	Y
P|Paxos|b|plain|none	agy	b4pp03	L4	cells-b4-paxos-plain/b4pp03	1401	Y
P|Paxos|b|salt-diet|none	agy	b4ps01	L4	cells-b4-paxos-saltdiet/b4ps01	574	Y
P|Paxos|b|salt-diet|none	agy	b4ps02	L4	cells-b4-paxos-saltdiet/b4ps02	1083	Y
P|Paxos|b|salt-diet|none	agy	b4ps03	L4	cells-b4-paxos-saltdiet/b4ps03	349	Y
P|LZW|g|plain|none	agy	l6vgpp01	L6	cells-l6v-lzw-pro-plain-bare/l6vgpp01	1241	Y
P|LZW|g|plain|none	agy	l6vgpp02	L6	cells-l6v-lzw-pro-plain-bare/l6vgpp02	1308	Y
P|LZW|g|plain|none	agy	l6vgpp03	L6	cells-l6v-lzw-pro-plain-bare/l6vgpp03	1553	Y
P|LZW|g|salt-diet|none	agy	l6vgps01	L6	cells-l6v-lzw-pro-salt-bare/l6vgps01	1108	Y
P|LZW|g|salt-diet|none	agy	l6vgps02	L6	cells-l6v-lzw-pro-salt-bare/l6vgps02	2455	Y
P|LZW|g|salt-diet|none	agy	l6vgps03	L6	cells-l6v-lzw-pro-salt-bare/l6vgps03	1546	Y
P|LZW|g|plain|stmt	agy	l6uspq01	L6	cells-l6u-lzw-pro-plain-stmt/l6uspq01	1023	Y	l6u sentry = cell 1
P|LZW|g|plain|stmt	agy	l6vspb01	L6	cells-l6v-lzw-pro-plain-stmt-b/l6vspb01	1180	Y
P|LZW|g|plain|stmt	agy	l6vspb02	L6	cells-l6v-lzw-pro-plain-stmt-b/l6vspb02	1740	Y
P|LZW|g|salt-diet|stmt	agy	l6vspt01	L6	cells-l6v-lzw-pro-salt-stmt/l6vspt01	2066	Y	TRUNCATED
P|LZW|g|salt-diet|stmt	agy	l6vspt02	L6	cells-l6v-lzw-pro-salt-stmt/l6vspt02	1013	Y
P|LZW|g|salt-diet|stmt	agy	l6vspt03	L6	cells-l6v-lzw-pro-salt-stmt/l6vspt03	1785	Y
P|Crc32|b|plain|none	agy	l7cpbp01	L7	cells-l7-crc32-pro-plain-bare-bf/l7cpbp01	1564	Y
P|Crc32|b|plain|none	agy	l7cpbp02	L7	cells-l7-crc32-pro-plain-bare-bf/l7cpbp02	1576	Y
P|Crc32|b|plain|none	agy	l7cpbp03	L7	cells-l7-crc32-pro-plain-bare-bf/l7cpbp03	1159	Y
P|Crc32|b|salt-diet|none	agy	l7cpbs01	L7	cells-l7-crc32-pro-salt-bare-bf/l7cpbs01	1835	Y
P|Crc32|b|salt-diet|none	agy	l7cpbs02	L7	cells-l7-crc32-pro-salt-bare-bf/l7cpbs02	890	Y
P|Crc32|b|salt-diet|none	agy	l7cpbs03	L7	cells-l7-crc32-pro-salt-bare-bf/l7cpbs03	445	Y	VOID(NO-BRIEFING)
P|FreeList|b|plain|none	agy	l7npfp01	L7	cells-l7-freelist-pro-plain-bare-bf/l7npfp01	2052	Y
P|FreeList|b|plain|none	agy	l7npfp02	L7	cells-l7-freelist-pro-plain-bare-bf/l7npfp02	1669	Y
P|FreeList|b|plain|none	agy	l7npfp03	L7	cells-l7-freelist-pro-plain-bare-bf/l7npfp03	1690	Y
P|FreeList|b|salt-diet|none	agy	l7npfs01	L7	cells-l7-freelist-pro-salt-bare-bf/l7npfs01	646	Y
P|FreeList|b|salt-diet|none	agy	l7npfs02	L7	cells-l7-freelist-pro-salt-bare-bf/l7npfs02	2237	Y
P|FreeList|b|salt-diet|none	agy	l7npfs03	L7	cells-l7-freelist-pro-salt-bare-bf/l7npfs03	747	Y
P|LZW|b|plain|none	agy	l7npzp01	L7	cells-l7-lzw-pro-plain-bare-bf/l7npzp01	1491	Y
P|LZW|b|plain|none	agy	l7npzp02	L7	cells-l7-lzw-pro-plain-bare-bf/l7npzp02	1410	Y
P|LZW|b|plain|none	agy	l7npzp03	L7	cells-l7-lzw-pro-plain-bare-bf/l7npzp03	2109	Y
P|LZW|b|salt-diet|none	agy	l7npzs01	L7	cells-l7-lzw-pro-salt-bare-bf/l7npzs01	1218	Y
P|LZW|b|salt-diet|none	agy	l7npzs02	L7	cells-l7-lzw-pro-salt-bare-bf/l7npzs02	927	Y
P|LZW|b|salt-diet|none	agy	l7npzs03	L7	cells-l7-lzw-pro-salt-bare-bf/l7npzs03	2458	Y
P|Crc32|b|plain|stmt	agy	l7cpsp01	L7	cells-l7-crc32-pro-plain-stmt-bf/l7cpsp01	1328	Y
P|Crc32|b|plain|stmt	agy	l7cpsp02	L7	cells-l7-crc32-pro-plain-stmt-bf/l7cpsp02	1421	Y
P|Crc32|b|plain|stmt	agy	l7cpsp03	L7	cells-l7-crc32-pro-plain-stmt-bf/l7cpsp03	1230	Y
P|Crc32|b|salt-diet|stmt	agy	l7cpssa201	L7	cells-l7-crc32-pro-salt-stmt-bf-a2/l7cpssa201	351	Y
P|Crc32|b|salt-diet|stmt	agy	l7cpssa202	L7	cells-l7-crc32-pro-salt-stmt-bf-a2/l7cpssa202	238	Y
P|Crc32|b|salt-diet|stmt	agy	l7cpssa203	L7	cells-l7-crc32-pro-salt-stmt-bf-a2/l7cpssa203	1081	Y
P|FreeList|b|plain|stmt	agy	l7spfp01	L7	cells-l7-freelist-pro-plain-stmt-bf/l7spfp01	912	Y
P|FreeList|b|plain|stmt	agy	l7spfp02	L7	cells-l7-freelist-pro-plain-stmt-bf/l7spfp02	1483	Y
P|FreeList|b|plain|stmt	agy	l7spfp03	L7	cells-l7-freelist-pro-plain-stmt-bf/l7spfp03	2017	Y
P|FreeList|b|salt-diet|stmt	agy	l7spfb01	L7	cells-l7-freelist-pro-salt-stmt-bf-b/l7spfb01	552	Y
P|FreeList|b|salt-diet|stmt	agy	l7spfb02	L7	cells-l7-freelist-pro-salt-stmt-bf-b/l7spfb02	1053	Y	TRUNCATED
P|FreeList|b|salt-diet|stmt	agy	l7spfwa201	L7	cells-l7-freelist-pro-salt-stmt-bf-tripwire-a2/l7spfwa201	501	Y	tripwire attempt 2
P|LRU|b|plain|stmt	agy	l7sprp01	L7	cells-l7-lru-pro-plain-stmt-bf/l7sprp01	1170	Y
P|LRU|b|plain|stmt	agy	l7sprp02	L7	cells-l7-lru-pro-plain-stmt-bf/l7sprp02	1417	Y
P|LRU|b|plain|stmt	agy	l7sprp03	L7	cells-l7-lru-pro-plain-stmt-bf/l7sprp03	1308	Y
P|LRU|b|salt-diet|stmt	agy	l7sprs01	L7	cells-l7-lru-pro-salt-stmt-bf/l7sprs01	1661	Y
P|LRU|b|salt-diet|stmt	agy	l7sprs02	L7	cells-l7-lru-pro-salt-stmt-bf/l7sprs02	1304	Y
P|LRU|b|salt-diet|stmt	agy	l7sprs03	L7	cells-l7-lru-pro-salt-stmt-bf/l7sprs03	1657	Y
P|LZW|b|plain|stmt	agy	l7spzp01	L7	cells-l7-lzw-pro-plain-stmt-bf/l7spzp01	790	Y
P|LZW|b|plain|stmt	agy	l7spzp02	L7	cells-l7-lzw-pro-plain-stmt-bf/l7spzp02	1198	Y
P|LZW|b|plain|stmt	agy	l7spzp03	L7	cells-l7-lzw-pro-plain-stmt-bf/l7spzp03	1533	Y
P|LZW|b|salt-diet|stmt	agy	l7spzs01	L7	cells-l7-lzw-pro-salt-stmt-bf/l7spzs01	1770	Y
P|LZW|b|salt-diet|stmt	agy	l7spzs02	L7	cells-l7-lzw-pro-salt-stmt-bf/l7spzs02	2408	Y
P|LZW|b|salt-diet|stmt	agy	l7spzs03	L7	cells-l7-lzw-pro-salt-stmt-bf/l7spzs03	1678	Y
P|Crc32|g|plain|sc	agy	l8cpps01	L8D	cells-l8-crc32-pro-plain-sc/l8cpps01	1452	Y
P|Crc32|g|plain|sc	agy	l8cpps02	L8D	cells-l8-crc32-pro-plain-sc/l8cpps02	1296	Y
P|Crc32|g|plain|sc	agy	l8cpps03	L8D	cells-l8-crc32-pro-plain-sc/l8cpps03	1469	Y
P|Crc32|g|salt-diet|sc	agy	l8cpss01	L8DA	cells-l8-crc32-pro-salt-sc-cp/l8cpss01	828	Y	phase-2 copy; original cells-l8-crc32-pro-salt-sc/l8cpss01 = 1084 B
P|Crc32|g|salt-diet|sc	agy	l8cpss02	L8D	cells-l8-crc32-pro-salt-sc/l8cpss02	2002	Y
P|Crc32|g|salt-diet|sc	agy	l8cpss03	L8DA	cells-l8-crc32-pro-salt-sc-cp/l8cpss03	1770	Y	phase-2 copy; original = 1342 B
P|LRU|g|plain|sc	agy	l8rppr01	L8D	cells-l8-lru-pro-plain-sc-rerun/l8rppr01	1016	Y
P|LRU|g|plain|sc	agy	l8rppr02	L8D	cells-l8-lru-pro-plain-sc-rerun/l8rppr02	1671	Y
P|LRU|g|plain|sc	agy	l8rppr03	L8D	cells-l8-lru-pro-plain-sc-rerun/l8rppr03	1693	Y
P|LRU|g|salt-diet|sc	agy	l8rpsra201	L8D	cells-l8-lru-pro-salt-sc-rerun-a2/l8rpsra201	2018	Y
P|LRU|g|salt-diet|sc	agy	l8rpsra202	L8D	cells-l8-lru-pro-salt-sc-rerun-a2/l8rpsra202	1094	Y
P|LRU|g|salt-diet|sc	agy	l8rpsra203	L8D	cells-l8-lru-pro-salt-sc-rerun-a2/l8rpsra203	1663	Y
P|Paxos|g|plain|sc	agy	l8xppr01	L8F	cells-l8-paxos-pro-plain-sc-rerun/l8xppr01	1396	Y
P|Paxos|g|plain|sc	agy	l8xppr02	L8F	cells-l8-paxos-pro-plain-sc-rerun/l8xppr02	1595	Y
P|Paxos|g|plain|sc	agy	l8xppr03	L8F	cells-l8-paxos-pro-plain-sc-rerun/l8xppr03	2160	Y
P|Paxos|g|salt-diet|sc	agy	l8xpsr01	L8F	cells-l8-paxos-pro-salt-sc-rerun/l8xpsr01	1783	Y
P|Paxos|g|salt-diet|sc	agy	l8xpsr02	L8F	cells-l8-paxos-pro-salt-sc-rerun/l8xpsr02	1537	Y
P|Paxos|g|salt-diet|sc	agy	l8xpsr03	L8F	cells-l8-paxos-pro-salt-sc-rerun/l8xpsr03	1900	Y
P|FreeList|g|plain|sc	agy	l8fppr01	L8F	cells-l8-freelist-pro-plain-sc-rerun/l8fppr01	1511	Y
P|FreeList|g|plain|sc	agy	l8fppr02	L8F	cells-l8-freelist-pro-plain-sc-rerun/l8fppr02	2142	Y
P|FreeList|g|plain|sc	agy	l8fppr03	L8F	cells-l8-freelist-pro-plain-sc-rerun/l8fppr03	2164	Y
P|FreeList|g|salt-diet|sc	agy	l8fpsr01	L8F	cells-l8-freelist-pro-salt-sc-rerun/l8fpsr01	1772	Y
P|FreeList|g|salt-diet|sc	agy	l8fpsr02	L8F	cells-l8-freelist-pro-salt-sc-rerun/l8fpsr02	1309	Y
P|FreeList|g|salt-diet|sc	agy	l8fpsr03	L8F	cells-l8-freelist-pro-salt-sc-rerun/l8fpsr03	1729	Y
P|LZW|g|plain|sc	agy	l8zppr01	L8F	cells-l8-lzw-pro-plain-sc-rerun/l8zppr01	3362	Y
P|LZW|g|plain|sc	agy	l8zppr02	L8F	cells-l8-lzw-pro-plain-sc-rerun/l8zppr02	1679	Y
P|LZW|g|plain|sc	agy	l8zppr03	L8F	cells-l8-lzw-pro-plain-sc-rerun/l8zppr03	2024	Y
P|LZW|g|salt-diet|sc	agy	l8zpsr01	L8F	cells-l8-lzw-pro-salt-sc-rerun/l8zpsr01	718	Y
P|LZW|g|salt-diet|sc	agy	l8zpsr02	L8F	cells-l8-lzw-pro-salt-sc-rerun/l8zpsr02	1612	Y
P|LZW|g|salt-diet|sc	agy	l8zpsr03	L8F	cells-l8-lzw-pro-salt-sc-rerun/l8zpsr03	1525	Y
F|Crc32|g|plain|none	agy	l5cp01	L5	cells-l5-crc32-plain/l5cp01	1517	Y	another l5cp01 exists in cells-l5-crc32-plain-a1 (2338 B)
F|Crc32|g|plain|none	agy	l5cp02	L5	cells-l5-crc32-plain/l5cp02	2382	Y
F|Crc32|g|plain|none	agy	l5cp03	L5	cells-l5-crc32-plain/l5cp03	2113	Y
F|Crc32|g|salt-diet|none	agy	l5cs01	L5	cells-l5-crc32-saltdiet/l5cs01	1531	Y
F|Crc32|g|salt-diet|none	agy	l5cs02	L5	cells-l5-crc32-saltdiet/l5cs02	2380	Y
F|Crc32|g|salt-diet|none	agy	l5cs03	L5	cells-l5-crc32-saltdiet/l5cs03	1533	Y
F|FreeList|g|plain|none	agy	l5fp01	L5	cells-l5-freelist-plain/l5fp01	3101	Y
F|FreeList|g|plain|none	agy	l5fp02	L5	cells-l5-freelist-plain/l5fp02	2777	Y
F|FreeList|g|plain|none	agy	l5fp03	L5	cells-l5-freelist-plain/l5fp03	3968	Y
F|FreeList|g|salt-diet|none	agy	l5fs01	L5	cells-l5-freelist-saltdiet/l5fs01	2280	Y
F|FreeList|g|salt-diet|none	agy	l5fs02	L5	cells-l5-freelist-saltdiet/l5fs02	3094	Y
F|FreeList|g|salt-diet|none	agy	l5fs03	L5	cells-l5-freelist-saltdiet/l5fs03	3185	Y
F|LRU|g|plain|none	agy	l5lp01	L5	cells-l5-lru-plain/l5lp01	3067	Y
F|LRU|g|plain|none	agy	l5lp02	L5	cells-l5-lru-plain/l5lp02	3056	Y
F|LRU|g|plain|none	agy	l5lp03	L5	cells-l5-lru-plain/l5lp03	2409	Y
F|LRU|g|salt-diet|none	agy	l5lsra301	L5	cells-l5-lru-saltdiet-refire-a3/l5lsra301	1991	Y	re-fire; id from box root
F|LRU|g|salt-diet|none	agy	l5lsra302	L5	cells-l5-lru-saltdiet-refire-a3/l5lsra302	2438	Y	re-fire; id from box root
F|LRU|g|salt-diet|none	agy	l5lsra303	L5	cells-l5-lru-saltdiet-refire-a3/l5lsra303	3962	Y	re-fire; id from box root
F|Paxos|g|plain|none	agy	l5ppr01	L5	cells-l5-paxos-plain-refire/l5ppr01	3754	Y	re-fire; id from box root
F|Paxos|g|plain|none	agy	l5ppr02	L5	cells-l5-paxos-plain-refire/l5ppr02	3310	Y	re-fire; id from box root
F|Paxos|g|plain|none	agy	l5ppr03	L5	cells-l5-paxos-plain-refire/l5ppr03	6498	Y	re-fire; id from box root
F|Paxos|g|salt-diet|none	agy	l5psra201	L5	cells-l5-paxos-saltdiet-refire-a2/l5psra201	3173	Y	re-fire; id from box root
F|Paxos|g|salt-diet|none	agy	l5psra202	L5	cells-l5-paxos-saltdiet-refire-a2/l5psra202	3588	Y	TRUNCATED
F|Paxos|g|salt-diet|none	agy	l5psra203	L5	cells-l5-paxos-saltdiet-refire-a2/l5psra203	2521	Y	re-fire; id from box root
F|Crc32|g|plain|stmt	agy	l5cq01	L5	cells-l5-crc32-plain-stmt/l5cq01	2522	Y	id from box root
F|Crc32|g|plain|stmt	agy	l5cq02	L5	cells-l5-crc32-plain-stmt/l5cq02	1754	Y	id from box root
F|Crc32|g|plain|stmt	agy	l5cq03	L5	cells-l5-crc32-plain-stmt/l5cq03	1973	Y	id from box root
F|Crc32|g|salt-diet|stmt	agy	l5ct01	L5	cells-l5-crc32-saltdiet-stmt/l5ct01	2263	Y	id from box root
F|Crc32|g|salt-diet|stmt	agy	l5ct02	L5	cells-l5-crc32-saltdiet-stmt/l5ct02	2153	Y	id from box root
F|Crc32|g|salt-diet|stmt	agy	l5ct03	L5	cells-l5-crc32-saltdiet-stmt/l5ct03	1984	Y	id from box root
F|FreeList|g|plain|stmt	agy	l5fq01	L5	cells-l5-freelist-plain-stmt/l5fq01	2386	Y	id from box root
F|FreeList|g|plain|stmt	agy	l5fq02	L5	cells-l5-freelist-plain-stmt/l5fq02	2238	Y	id from box root
F|FreeList|g|plain|stmt	agy	l5fq03	L5	cells-l5-freelist-plain-stmt/l5fq03	3349	Y	id from box root
F|FreeList|g|salt-diet|stmt	agy	l5ft01	L5	cells-l5-freelist-saltdiet-stmt/l5ft01	3005	Y	id from box root
F|FreeList|g|salt-diet|stmt	agy	l5ft02	L5	cells-l5-freelist-saltdiet-stmt/l5ft02	3283	Y	id from box root
F|FreeList|g|salt-diet|stmt	agy	l5ft03	L5	cells-l5-freelist-saltdiet-stmt/l5ft03	1531	Y	id from box root
F|LRU|g|plain|stmt	agy	l5lq01	L5	cells-l5-lru-plain-stmt/l5lq01	2265	Y	id from box root
F|LRU|g|plain|stmt	agy	l5lq02	L5	cells-l5-lru-plain-stmt/l5lq02	2447	Y	id from box root
F|LRU|g|plain|stmt	agy	l5lq03	L5	cells-l5-lru-plain-stmt/l5lq03	2107	Y	id from box root
F|LRU|g|salt-diet|stmt	agy	l5lt01	L5	cells-l5-lru-saltdiet-stmt/l5lt01	1903	Y	id from box root
F|LRU|g|salt-diet|stmt	agy	l5lt02	L5	cells-l5-lru-saltdiet-stmt/l5lt02	2747	Y	id from box root
F|LRU|g|salt-diet|stmt	agy	l5lt03	L5	cells-l5-lru-saltdiet-stmt/l5lt03	2126	Y	id from box root
F|LZW|g|plain|none	agy	l6vgfp01	L6	cells-l6v-lzw-flash-plain-bare/l6vgfp01	2923	Y
F|LZW|g|plain|none	agy	l6vgfp02	L6	cells-l6v-lzw-flash-plain-bare/l6vgfp02	2632	Y
F|LZW|g|plain|none	agy	l6vgfp03	L6	cells-l6v-lzw-flash-plain-bare/l6vgfp03	2560	Y
F|LZW|g|salt-diet|none	agy	l6vgfs01	L6	cells-l6v-lzw-flash-salt-bare/l6vgfs01	1740	Y
F|LZW|g|salt-diet|none	agy	l6vgfs02	L6	NF	-	Y	VOID (P-DELIVERY no), in no denominator
F|LZW|g|salt-diet|none	agy	l6vgfs03	L6	cells-l6v-lzw-flash-salt-bare/l6vgfs03	2967	Y
F|LZW|g|plain|stmt	agy	l6vsfq01	L6	cells-l6v-lzw-flash-plain-stmt/l6vsfq01	2175	Y
F|LZW|g|plain|stmt	agy	l6vsfq02	L6	cells-l6v-lzw-flash-plain-stmt/l6vsfq02	2913	Y
F|LZW|g|plain|stmt	agy	l6vsfq03	L6	cells-l6v-lzw-flash-plain-stmt/l6vsfq03	2395	Y
F|LZW|g|salt-diet|stmt	agy	l6vsft01	L6	cells-l6v-lzw-flash-salt-stmt/l6vsft01	2213	Y
F|LZW|g|salt-diet|stmt	agy	l6vsft02	L6	cells-l6v-lzw-flash-salt-stmt/l6vsft02	1650	Y
F|LZW|g|salt-diet|stmt	agy	l6vsft03	L6	cells-l6v-lzw-flash-salt-stmt/l6vsft03	1890	Y
F|LRU|b|plain|none	agy	l6vblp01	L6	cells-l6v-lru-flash-plain-bf/l6vblp01	3490	Y
F|LRU|b|plain|none	agy	l6vblp02	L6	cells-l6v-lru-flash-plain-bf/l6vblp02	3191	Y
F|LRU|b|plain|none	agy	l6vblp03	L6	cells-l6v-lru-flash-plain-bf/l6vblp03	2824	Y
F|LRU|b|salt-diet|none	agy	l6vbls01	L6	cells-l6v-lru-flash-salt-bf/l6vbls01	2517	Y
F|LRU|b|salt-diet|none	agy	l6vbls02	L6	cells-l6v-lru-flash-salt-bf/l6vbls02	2736	Y
F|LRU|b|salt-diet|none	agy	l6vbls03	L6	cells-l6v-lru-flash-salt-bf/l6vbls03	2213	Y
F|Paxos|b|plain|none	agy	l6vbpp01	L6	cells-l6v-paxos-flash-plain-bf/l6vbpp01	4047	Y
F|Paxos|b|plain|none	agy	l6vbpp02	L6	cells-l6v-paxos-flash-plain-bf/l6vbpp02	4679	Y
F|Paxos|b|plain|none	agy	l6vbpp03	L6	cells-l6v-paxos-flash-plain-bf/l6vbpp03	5068	Y
F|Paxos|b|salt-diet|none	agy	l6vbps01	L6	cells-l6v-paxos-flash-salt-bf/l6vbps01	2439	Y
F|Paxos|b|salt-diet|none	agy	l6vbps02	L6	cells-l6v-paxos-flash-salt-bf/l6vbps02	3054	Y
F|Paxos|b|salt-diet|none	agy	l6vbps03	L6	cells-l6v-paxos-flash-salt-bf/l6vbps03	2877	Y
F|Crc32|b|plain|none	agy	l7cfbp01	L7	cells-l7-crc32-flash-plain-bare-bf/l7cfbp01	2763	Y
F|Crc32|b|plain|none	agy	l7cfbp02	L7	cells-l7-crc32-flash-plain-bare-bf/l7cfbp02	2742	Y
F|Crc32|b|plain|none	agy	l7cfbp03	L7	cells-l7-crc32-flash-plain-bare-bf/l7cfbp03	2551	Y
F|Crc32|b|salt-diet|none	agy	l7cfbs01	L7	cells-l7-crc32-flash-salt-bare-bf/l7cfbs01	1626	Y
F|Crc32|b|salt-diet|none	agy	l7cfbs02	L7	cells-l7-crc32-flash-salt-bare-bf/l7cfbs02	1582	Y
F|Crc32|b|salt-diet|none	agy	l7cfbs03	L7	cells-l7-crc32-flash-salt-bare-bf/l7cfbs03	2194	Y
F|FreeList|b|plain|none	agy	l7nffp01	L7	cells-l7-freelist-flash-plain-bare-bf/l7nffp01	5975	Y
F|FreeList|b|plain|none	agy	l7nffp02	L7	cells-l7-freelist-flash-plain-bare-bf/l7nffp02	4951	Y
F|FreeList|b|plain|none	agy	l7nffp03	L7	cells-l7-freelist-flash-plain-bare-bf/l7nffp03	5232	Y
F|FreeList|b|salt-diet|none	agy	l7nffs01	L7	cells-l7-freelist-flash-salt-bare-bf/l7nffs01	3871	Y
F|FreeList|b|salt-diet|none	agy	l7nffs02	L7	cells-l7-freelist-flash-salt-bare-bf/l7nffs02	3981	Y
F|FreeList|b|salt-diet|none	agy	l7nffs03	L7	cells-l7-freelist-flash-salt-bare-bf/l7nffs03	2317	Y
F|LZW|b|plain|none	agy	l7nfzp01	L7	cells-l7-lzw-flash-plain-bare-bf/l7nfzp01	3600	Y
F|LZW|b|plain|none	agy	l7nfzp02	L7	cells-l7-lzw-flash-plain-bare-bf/l7nfzp02	3796	Y
F|LZW|b|plain|none	agy	l7nfzp03	L7	cells-l7-lzw-flash-plain-bare-bf/l7nfzp03	3249	Y
F|LZW|b|salt-diet|none	agy	l7nfzs01	L7	cells-l7-lzw-flash-salt-bare-bf/l7nfzs01	1697	Y
F|LZW|b|salt-diet|none	agy	l7nfzs02	L7	cells-l7-lzw-flash-salt-bare-bf/l7nfzs02	2330	Y
F|LZW|b|salt-diet|none	agy	l7nfzs03	L7	cells-l7-lzw-flash-salt-bare-bf/l7nfzs03	2325	Y
F|Crc32|b|plain|stmt	agy	l7cfsp01	L7	cells-l7-crc32-flash-plain-stmt-bf/l7cfsp01	2860	Y
F|Crc32|b|plain|stmt	agy	l7cfsp02	L7	cells-l7-crc32-flash-plain-stmt-bf/l7cfsp02	2200	Y
F|Crc32|b|plain|stmt	agy	l7cfsp03	L7	cells-l7-crc32-flash-plain-stmt-bf/l7cfsp03	3443	Y
F|Crc32|b|salt-diet|stmt	agy	l7cfss01	L7	cells-l7-crc32-flash-salt-stmt-bf/l7cfss01	1799	Y
F|Crc32|b|salt-diet|stmt	agy	l7cfssq01	L7A	cells-l7-crc32-flash-salt-stmt-bf-q2/l7cfssq01	1948	Y
F|Crc32|b|salt-diet|stmt	agy	l7cfssq02	L7A	cells-l7-crc32-flash-salt-stmt-bf-q2/l7cfssq02	1705	Y
F|FreeList|b|plain|stmt	agy	l7sffp01	L7	cells-l7-freelist-flash-plain-stmt-bf/l7sffp01	2864	Y
F|FreeList|b|plain|stmt	agy	l7sffp02	L7	cells-l7-freelist-flash-plain-stmt-bf/l7sffp02	3982	Y
F|FreeList|b|plain|stmt	agy	l7sffp03	L7	cells-l7-freelist-flash-plain-stmt-bf/l7sffp03	4767	Y
F|FreeList|b|salt-diet|stmt	agy	l7sffs01	L7	cells-l7-freelist-flash-salt-stmt-bf/l7sffs01	2420	Y
F|FreeList|b|salt-diet|stmt	agy	l7sffs02	L7	cells-l7-freelist-flash-salt-stmt-bf/l7sffs02	1714	Y
F|FreeList|b|salt-diet|stmt	agy	l7sffs03	L7	cells-l7-freelist-flash-salt-stmt-bf/l7sffs03	2370	Y
F|LRU|b|plain|stmt	agy	l7sfrp01	L7	cells-l7-lru-flash-plain-stmt-bf/l7sfrp01	3112	Y
F|LRU|b|plain|stmt	agy	l7sfrp02	L7	cells-l7-lru-flash-plain-stmt-bf/l7sfrp02	3528	Y
F|LRU|b|plain|stmt	agy	l7sfrp03	L7	cells-l7-lru-flash-plain-stmt-bf/l7sfrp03	3291	Y
F|LRU|b|salt-diet|stmt	agy	l7sfrs01	L7	cells-l7-lru-flash-salt-stmt-bf/l7sfrs01	2293	Y
F|LRU|b|salt-diet|stmt	agy	l7sfrs02	L7	cells-l7-lru-flash-salt-stmt-bf/l7sfrs02	2740	Y
F|LRU|b|salt-diet|stmt	agy	l7sfrs03	L7	cells-l7-lru-flash-salt-stmt-bf/l7sfrs03	2627	Y
F|LZW|b|plain|stmt	agy	l7sfzp01	L7	cells-l7-lzw-flash-plain-stmt-bf/l7sfzp01	3297	Y
F|LZW|b|plain|stmt	agy	l7sfzp02	L7	cells-l7-lzw-flash-plain-stmt-bf/l7sfzp02	3350	Y
F|LZW|b|plain|stmt	agy	l7sfzp03	L7	cells-l7-lzw-flash-plain-stmt-bf/l7sfzp03	3050	Y
F|LZW|b|salt-diet|stmt	agy	l7sfzs01	L7	cells-l7-lzw-flash-salt-stmt-bf/l7sfzs01	2324	Y
F|LZW|b|salt-diet|stmt	agy	l7sfzs02	L7	cells-l7-lzw-flash-salt-stmt-bf/l7sfzs02	2197	Y
F|LZW|b|salt-diet|stmt	agy	l7sfzs03	L7	cells-l7-lzw-flash-salt-stmt-bf/l7sfzs03	2721	Y
F|Crc32|g|plain|sc	agy	l8cfps01	L8D	cells-l8-crc32-flash-plain-sc/l8cfps01	3771	Y
F|Crc32|g|plain|sc	agy	l8cfps02	L8D	cells-l8-crc32-flash-plain-sc/l8cfps02	3076	Y
F|Crc32|g|plain|sc	agy	l8cfps03	L8D	cells-l8-crc32-flash-plain-sc/l8cfps03	3168	Y
F|Crc32|g|salt-diet|sc	agy	l8cfss01	L8D	cells-l8-crc32-flash-salt-sc/l8cfss01	2907	Y
F|Crc32|g|salt-diet|sc	agy	l8cfss02	L8D	cells-l8-crc32-flash-salt-sc/l8cfss02	3255	Y
F|Crc32|g|salt-diet|sc	agy	l8cfss03	L8D	cells-l8-crc32-flash-salt-sc/l8cfss03	3873	Y
F|LRU|g|plain|sc	agy	l8rfpb01	L8D	cells-l8-lru-flash-plain-sc-b/l8rfpb01	2558	Y
F|LRU|g|plain|sc	agy	l8rfpb02	L8D	cells-l8-lru-flash-plain-sc-b/l8rfpb02	2995	Y
F|LRU|g|plain|sc	agy	l8rfwra201	L8DE	cells-l8-lru-flash-plain-sc-tripwire-rerun-a2/l8rfwra201	2890	Y	mode-E tripwire, attempt 2
F|LRU|g|salt-diet|sc	agy	l8rfss01	L8D	cells-l8-lru-flash-salt-sc/l8rfss01	3836	Y
F|LRU|g|salt-diet|sc	agy	l8rfss02	L8D	cells-l8-lru-flash-salt-sc/l8rfss02	2765	Y
F|LRU|g|salt-diet|sc	agy	l8rfss03	L8D	cells-l8-lru-flash-salt-sc/l8rfss03	4427	Y
F|FreeList|g|plain|sc	agy	l8ffpr01	L8F	cells-l8-freelist-flash-plain-sc-rerun/l8ffpr01	4146	Y
F|FreeList|g|plain|sc	agy	l8ffpr02	L8F	cells-l8-freelist-flash-plain-sc-rerun/l8ffpr02	4599	Y
F|FreeList|g|plain|sc	agy	l8ffpr03	L8F	cells-l8-freelist-flash-plain-sc-rerun/l8ffpr03	2939	Y
F|FreeList|g|salt-diet|sc	agy	l8ffsra201	L8F	cells-l8-freelist-flash-salt-sc-rerun-a2/l8ffsra201	4107	Y
F|FreeList|g|salt-diet|sc	agy	l8ffsra202	L8F	cells-l8-freelist-flash-salt-sc-rerun-a2/l8ffsra202	3242	Y
F|FreeList|g|salt-diet|sc	agy	l8ffsra203	L8F	cells-l8-freelist-flash-salt-sc-rerun-a2/l8ffsra203	3157	Y
F|LZW|g|plain|sc	agy	l8zfpra201	L8F	cells-l8-lzw-flash-plain-sc-rerun-a2/l8zfpra201	4008	Y
F|LZW|g|plain|sc	agy	l8zfpra202	L8F	cells-l8-lzw-flash-plain-sc-rerun-a2/l8zfpra202	4261	Y
F|LZW|g|plain|sc	agy	l8zfpra203	L8F	cells-l8-lzw-flash-plain-sc-rerun-a2/l8zfpra203	4616	Y
F|LZW|g|salt-diet|sc	agy	l8zfsr01	L8F	cells-l8-lzw-flash-salt-sc-rerun/l8zfsr01	5292	Y
F|LZW|g|salt-diet|sc	agy	l8zfsr02	L8F	cells-l8-lzw-flash-salt-sc-rerun/l8zfsr02	4182	Y
F|LZW|g|salt-diet|sc	agy	l8zfsr03	L8F	cells-l8-lzw-flash-salt-sc-rerun/l8zfsr03	4252	Y
F|Paxos|g|plain|sc	agy	l8xfp2a201	L8F	cells-l8-paxos-flash-plain-sc-rerun2-a2/l8xfp2a201	5312	Y
F|Paxos|g|plain|sc	agy	l8xfp2a202	L8F	cells-l8-paxos-flash-plain-sc-rerun2-a2/l8xfp2a202	5657	Y
F|Paxos|g|plain|sc	agy	l8xfp2a203	L8F	cells-l8-paxos-flash-plain-sc-rerun2-a2/l8xfp2a203	4102	Y
F|Paxos|g|salt-diet|sc	agy	l8xfs201	L8F	cells-l8-paxos-flash-salt-sc-rerun2/l8xfs201	7628	Y
F|Paxos|g|salt-diet|sc	agy	l8xfs202	L8F	cells-l8-paxos-flash-salt-sc-rerun2/l8xfs202	5473	Y
F|Paxos|g|salt-diet|sc	agy	l8xfs203	L8F	cells-l8-paxos-flash-salt-sc-rerun2/l8xfs203	3889	Y
O|Crc32|g|plain|none	claude-hc1	hc1cp01	HC1	cells-hc1-crc32-plain/hc1cp01	13588	Y	HC1 stage 1 (placebo = off-grid arm)
O|Crc32|g|plain|none	claude-hc1	hc1cp02	HC1	cells-hc1-crc32-plain/hc1cp02	11134	Y	HC1 stage 1 (placebo = off-grid arm)
O|Crc32|g|plain|none	claude-hc1	hc1cp03	HC1	cells-hc1-crc32-plain/hc1cp03	13532	Y	HC1 stage 1 (placebo = off-grid arm)
O|Crc32|g|salt-diet|none	claude-hc1	hc1cs01	HC1	cells-hc1-crc32-saltdiet/hc1cs01	11643	Y	HC1 stage 1 (placebo = off-grid arm)
O|Crc32|g|salt-diet|none	claude-hc1	hc1cs02	HC1	cells-hc1-crc32-saltdiet/hc1cs02	9952	Y	HC1 stage 1 (placebo = off-grid arm)
O|Crc32|g|salt-diet|none	claude-hc1	hc1cs03	HC1	cells-hc1-crc32-saltdiet/hc1cs03	9988	Y	HC1 stage 1 (placebo = off-grid arm)
O|Crc32|g|placebo|none	claude-hc1	hc1cb01	HC1	cells-hc1-crc32-placebo/hc1cb01	14738	Y	HC1 stage 1 (placebo = off-grid arm)
O|Crc32|g|placebo|none	claude-hc1	hc1cb02	HC1	cells-hc1-crc32-placebo/hc1cb02	10667	Y	HC1 stage 1 (placebo = off-grid arm)
O|Crc32|g|placebo|none	claude-hc1	hc1cb03	HC1	cells-hc1-crc32-placebo/hc1cb03	14337	Y	HC1 stage 1 (placebo = off-grid arm)
O|FreeList|g|plain|none	claude-hc1	hc1fp01	HC1	cells-hc1-freelist-plain/hc1fp01	14535	Y	HC1 stage 1 (placebo = off-grid arm)
O|FreeList|g|plain|none	claude-hc1	hc1fp02	HC1	cells-hc1-freelist-plain/hc1fp02	15904	Y	HC1 stage 1 (placebo = off-grid arm)
O|FreeList|g|plain|none	claude-hc1	hc1fp03	HC1	cells-hc1-freelist-plain/hc1fp03	13856	Y	HC1 stage 1 (placebo = off-grid arm)
O|FreeList|g|salt-diet|none	claude-hc1	hc1fs01	HC1	cells-hc1-freelist-saltdiet/hc1fs01	13056	Y	HC1 stage 1 (placebo = off-grid arm)
O|FreeList|g|salt-diet|none	claude-hc1	hc1fs02	HC1	NF	-	Y	HC1 stage 1 (placebo = off-grid arm)
O|FreeList|g|salt-diet|none	claude-hc1	hc1fs03	HC1	cells-hc1-freelist-saltdiet/hc1fs03	13326	Y	HC1 stage 1 (placebo = off-grid arm)
O|FreeList|g|placebo|none	claude-hc1	hc1fb01	HC1	cells-hc1-freelist-placebo/hc1fb01	10827	Y	HC1 stage 1 (placebo = off-grid arm)
O|FreeList|g|placebo|none	claude-hc1	hc1fb02	HC1	cells-hc1-freelist-placebo/hc1fb02	9745	Y	HC1 stage 1 (placebo = off-grid arm)
O|FreeList|g|placebo|none	claude-hc1	hc1fb03	HC1	cells-hc1-freelist-placebo/hc1fb03	9594	Y	HC1 stage 1 (placebo = off-grid arm)
O|LRU|g|plain|none	claude-hc1	hc1lp01	HC1	cells-hc1-lru-plain/hc1lp01	14828	Y	HC1 stage 1 (placebo = off-grid arm)
O|LRU|g|plain|none	claude-hc1	hc1lp02	HC1	cells-hc1-lru-plain/hc1lp02	14100	Y	HC1 stage 1 (placebo = off-grid arm)
O|LRU|g|plain|none	claude-hc1	hc1lp03	HC1	cells-hc1-lru-plain/hc1lp03	14654	Y	HC1 stage 1 (placebo = off-grid arm)
O|LRU|g|salt-diet|none	claude-hc1	hc1ls01	HC1	cells-hc1-lru-saltdiet/hc1ls01	10078	Y	HC1 stage 1 (placebo = off-grid arm)
O|LRU|g|salt-diet|none	claude-hc1	hc1ls02	HC1	cells-hc1-lru-saltdiet/hc1ls02	11959	Y	HC1 stage 1 (placebo = off-grid arm)
O|LRU|g|salt-diet|none	claude-hc1	hc1ls03	HC1	cells-hc1-lru-saltdiet/hc1ls03	11411	Y	HC1 stage 1 (placebo = off-grid arm)
O|LRU|g|placebo|none	claude-hc1	hc1lb01	HC1	cells-hc1-lru-placebo/hc1lb01	11382	Y	HC1 stage 1 (placebo = off-grid arm)
O|LRU|g|placebo|none	claude-hc1	hc1lb02	HC1	cells-hc1-lru-placebo/hc1lb02	14408	Y	HC1 stage 1 (placebo = off-grid arm)
O|LRU|g|placebo|none	claude-hc1	hc1lb03	HC1	cells-hc1-lru-placebo/hc1lb03	13732	Y	HC1 stage 1 (placebo = off-grid arm)
O|LZW|g|plain|none	claude-hc1	hc1zp01	HC1	cells-hc1-lzw-plain/hc1zp01	13834	Y	HC1 stage 1 (placebo = off-grid arm)
O|LZW|g|plain|none	claude-hc1	hc1zp02	HC1	cells-hc1-lzw-plain/hc1zp02	13389	Y	HC1 stage 1 (placebo = off-grid arm)
O|LZW|g|plain|none	claude-hc1	hc1zp03	HC1	cells-hc1-lzw-plain/hc1zp03	16057	Y	HC1 stage 1 (placebo = off-grid arm)
O|LZW|g|salt-diet|none	claude-hc1	hc1zs01	HC1	cells-hc1-lzw-saltdiet/hc1zs01	8418	Y	HC1 stage 1 (placebo = off-grid arm)
O|LZW|g|salt-diet|none	claude-hc1	hc1zs02	HC1	cells-hc1-lzw-saltdiet/hc1zs02	10058	Y	HC1 stage 1 (placebo = off-grid arm)
O|LZW|g|salt-diet|none	claude-hc1	hc1zs03	HC1	cells-hc1-lzw-saltdiet/hc1zs03	13487	Y	HC1 stage 1 (placebo = off-grid arm)
O|LZW|g|placebo|none	claude-hc1	hc1zb01	HC1	cells-hc1-lzw-placebo/hc1zb01	9460	Y	HC1 stage 1 (placebo = off-grid arm)
O|LZW|g|placebo|none	claude-hc1	hc1zb02	HC1	cells-hc1-lzw-placebo/hc1zb02	17207	Y	HC1 stage 1 (placebo = off-grid arm)
O|LZW|g|placebo|none	claude-hc1	hc1zb03	HC1	cells-hc1-lzw-placebo/hc1zb03	13510	Y	HC1 stage 1 (placebo = off-grid arm)
O|Paxos|g|plain|none	claude-hc1	hc1pp01	HC1	cells-hc1-paxos-plain/hc1pp01	20831	Y	HC1 stage 1 (placebo = off-grid arm)
O|Paxos|g|plain|none	claude-hc1	hc1pp02	HC1	cells-hc1-paxos-plain/hc1pp02	18358	Y	HC1 stage 1 (placebo = off-grid arm)
O|Paxos|g|plain|none	claude-hc1	hc1pp03	HC1	cells-hc1-paxos-plain/hc1pp03	13993	Y	HC1 stage 1 (placebo = off-grid arm)
O|Paxos|g|salt-diet|none	claude-hc1	hc1ps01	HC1	NF	-	Y	HC1 stage 1 (placebo = off-grid arm)
O|Paxos|g|salt-diet|none	claude-hc1	hc1ps02	HC1	cells-hc1-paxos-saltdiet/hc1ps02	12037	Y	HC1 stage 1 (placebo = off-grid arm)
O|Paxos|g|salt-diet|none	claude-hc1	hc1ps03	HC1	cells-hc1-paxos-saltdiet/hc1ps03	17339	Y	HC1 stage 1 (placebo = off-grid arm)
O|Paxos|g|placebo|none	claude-hc1	hc1pb01	HC1	cells-hc1-paxos-placebo/hc1pb01	12141	Y	HC1 stage 1 (placebo = off-grid arm)
O|Paxos|g|placebo|none	claude-hc1	hc1pb02	HC1	cells-hc1-paxos-placebo/hc1pb02	11922	Y	HC1 stage 1 (placebo = off-grid arm)
O|Paxos|g|placebo|none	claude-hc1	hc1pb03	HC1	cells-hc1-paxos-placebo/hc1pb03	15760	Y	HC1 stage 1 (placebo = off-grid arm)
```
**TABLE 2 — B's spec-change cells, where each input is recorded** (verbatim from the enumeration):
```
condition_key	cell_id	phase1_cost_at	phase2_cost_at	REGRESSIONS/CLAUSE_TESTS_at
O|Crc32|g|plain|sc	2d0c65b3	matrix1-tokens.tsv:8	PS.tsv:5	NOT RECORDED (PS.tsv has merged `tests` only)
O|Crc32|g|plain|sc	746d7d4e	matrix1-tokens.tsv:17	PS.tsv:11	NOT RECORDED
O|Crc32|g|plain|sc	a87b7740	matrix1-tokens.tsv:27	PS.tsv:15	NOT RECORDED
O|Crc32|g|salt-diet|sc	11165871	matrix1-tokens.tsv:3	PS.tsv:3	NOT RECORDED
O|Crc32|g|salt-diet|sc	3e95075c	matrix1-tokens.tsv:10	PS.tsv:7	NOT RECORDED
O|Crc32|g|salt-diet|sc	57a33630	matrix1-tokens.tsv:11	PS.tsv:8	NOT RECORDED
O|FreeList|g|plain|sc	188f422b	matrix1-tokens.tsv:5	PS.tsv:4	NOT RECORDED
O|FreeList|g|plain|sc	9cb8ce96	matrix1-tokens.tsv:25	PS.tsv:13	NOT RECORDED
O|FreeList|g|salt-diet|sc	f33c7e65	matrix1-tokens.tsv:35	PS.tsv:19	NOT RECORDED
O|LRU|g|plain|sc	3bdcbcbd	matrix1-tokens.tsv:9	PS.tsv:6	NOT RECORDED
O|LRU|g|plain|sc	69e8c2c4	matrix1-tokens.tsv:14	PS.tsv:10	NOT RECORDED
O|LRU|g|salt-diet|sc	011fe22f	matrix1-tokens.tsv:2	PS.tsv:2	NOT RECORDED
O|LRU|g|salt-diet|sc	b71994e3	matrix1-tokens.tsv:29	PS.tsv:17	NOT RECORDED
O|LRU|g|salt-diet|sc	d6b53ee4	matrix1-tokens.tsv:31	PS.tsv:18	NOT RECORDED
O|LZW|g|salt-diet|sc	7ac56e4e	matrix1-tokens.tsv:18	PS.tsv:12	NOT RECORDED
O|LZW|g|salt-diet|sc	18fb3eed	matrix1-tokens.tsv:6	S1-verdicts.tsv:3	NOT RECORDED
O|LZW|g|salt-diet|sc	6d58f1ec	matrix1-tokens.tsv:15	S1-verdicts.tsv:5	NOT RECORDED
O|LZW|g|plain|sc	93323249	matrix1-tokens.tsv:23	S1-verdicts.tsv:2	NOT RECORDED
O|LZW|g|plain|sc	22ee7d33	matrix1-tokens.tsv:7	S1-verdicts.tsv:4	NOT RECORDED
O|Paxos|g|plain|sc	60a056e6	matrix1-tokens.tsv:13	PS.tsv:9	NOT RECORDED
O|Paxos|g|plain|sc	f6462d47	matrix1-tokens.tsv:37	PS.tsv:20	NOT RECORDED
O|Paxos|g|salt-diet|sc	9e6c8d4d	matrix1-tokens.tsv:26	PS.tsv:14	NOT RECORDED
O|Paxos|g|salt-diet|sc	b22d1000	matrix1-tokens.tsv:28	PS.tsv:16	NOT RECORDED
S|Crc32|g|plain|sc	clbccp01/02/03	blockSC-cells.tsv:9/10/11 col12	same lines col24	same lines col19/col20
S|Crc32|g|salt-diet|sc	clbccs01/02/03	blockSC-cells.tsv:12/13/14 col12	col24	col19/col20
S|FreeList|g|plain|sc	clbcfp01/02/03	blockSC-cells.tsv:15/16/17 col12	col24	col19/col20
S|LRU|g|plain|sc	clbclp01/02/03	blockSC-cells.tsv:18/19/20 col12	col24	col19/col20
S|LRU|g|salt-diet|sc	clbcls01/02/03	blockSC-cells.tsv:21/22/23 col12	col24	col19/col20
S|Paxos|g|plain|sc	clbcpp01/02/03	blockSC-cells.tsv:24/25/26 col12	col24	col19/col20
S|LZW|g|plain|sc	clbczp01/02/03	blockSC-cells.tsv:27/28/29 col12	col24	col19/col20
F|Crc32|g|plain|sc	l8cfps01/02/03	chainD phase_facts.json:3/31/59	:17/45/73	chainD-cells.tsv:2/3/4
F|Crc32|g|salt-diet|sc	l8cfss01/02/03	phase_facts:87/115/143	:101/129/157	chainD-cells.tsv:5/6/7
P|Crc32|g|plain|sc	l8cpps01/02/03	phase_facts:171/199/227	:185/213/241	chainD-cells.tsv:8/9/10
P|Crc32|g|salt-diet|sc	l8cpss02	phase_facts:275	:289	chainD-cells.tsv:12
P|Crc32|g|salt-diet|sc	l8cpss01	phase_facts:255	NOT IN REPO (the :269 record is phase 2 NOT FIRED); on the box at ~/cells-l8-crc32-pro-salt-sc-cp/l8cpss01/ctl/agy-meter-2.json	chainD md:223 (ADDENDUM A); chainD-cells.tsv:11 reads UNREAD
P|Crc32|g|salt-diet|sc	l8cpss03	phase_facts:303	NOT IN REPO (:317 is NOT FIRED); on the box, same path pattern	chainD md:224; chainD-cells.tsv:13 reads UNREAD
F|LRU|g|plain|sc	l8rfpb01/02	phase_facts:323/351	:337/365	chainD-cells.tsv:14/15
F|LRU|g|plain|sc	l8rfwra201	chainD md:207 (ERRATUM 1 §E6)	chainD md:207	chainD md:206
F|LRU|g|salt-diet|sc	l8rfss01/02/03	phase_facts:379/407/435	:393/421/449	chainD-cells.tsv:16/17/18
P|LRU|g|plain|sc	l8rppr01/02/03	phase_facts:463/491/519	:477/505/533	chainD-cells.tsv:19/20/21
P|LRU|g|salt-diet|sc	l8rpsra201/02/03	phase_facts:547/575/603	:561/589/617	chainD-cells.tsv:22/23/24
P|Paxos|g|plain|sc	l8xppr01/02/03	chainF phase_facts.json:1 (id, phase 1)	:1 (id, phase 2)	chainF-cells.tsv:2/3/4
P|Paxos|g|salt-diet|sc	l8xpsr01/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:5/6/7
F|FreeList|g|plain|sc	l8ffpr01/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:8/9/10
F|FreeList|g|salt-diet|sc	l8ffsra201/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:11/12/13
P|FreeList|g|plain|sc	l8fppr01/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:14/15/16
P|FreeList|g|salt-diet|sc	l8fpsr01/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:17/18/19
F|LZW|g|plain|sc	l8zfpra201/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:20/21/22
F|LZW|g|salt-diet|sc	l8zfsr01/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:23/24/25
P|LZW|g|plain|sc	l8zppr01/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:26/27/28
P|LZW|g|salt-diet|sc	l8zpsr01/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:29/30/31
F|Paxos|g|plain|sc	l8xfp2a201/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:32/33/34
F|Paxos|g|salt-diet|sc	l8xfs201/02/03	chainF phase_facts:1	:1	chainF-cells.tsv:35/36/37
```
