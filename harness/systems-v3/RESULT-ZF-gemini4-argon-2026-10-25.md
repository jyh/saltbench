# RESULT — ZF: gemini-4-argon-high beside gemini-3.8-flash-high on the pilot's 46 conditions (desk ZF)

**OF RECORD ON MERGE.** The set ended at Z264 (2026-10-24 23:53 PDT) by the rate checkpoint's cut (§3). 264 of 276 registered cells were
fired and harvested; the 12 not fired are one whole condition, reported SHORT at n = 0. Every figure in the code block below is printed by
`harness/systems-v3/zf_result.py --print` from the inputs in §4, and `zf_result.py --check <this file>` must read CHECK GREEN.

```
POPULATION §G1: 46 conditions x 2 models x n = 3 = 276 cells; harvested 264; SHORT 4 condition-model pairs
STATE: COMPLETE — every SHORT pair is a condition CUT by ruling (4 pairs)
SHORT argon Paxos gf spec-change plain: 0 of 3 (CUT by ruling, council 2026-10-20 ④ (ADA at Z264))
SHORT flash Paxos gf spec-change plain: 0 of 3 (CUT by ruling, council 2026-10-20 ④ (ADA at Z264))
SHORT argon Paxos gf spec-change salt-diet: 0 of 3 (CUT by ruling, council 2026-10-20 ④ (ADA at Z264))
SHORT flash Paxos gf spec-change salt-diet: 0 of 3 (CUT by ruling, council 2026-10-20 ④ (ADA at Z264))
TABLE problem | field | card | arm | gemini-4-argon-high counted (excl.) · fired/scored/wedge/other | gemini-3.8-flash-high counted (excl.) · fired/scored/wedge/other | 3.x of record (HISTORICAL) gemini-3.1-pro-high · gemini-3.8-flash-high
ROW Crc32 | gf | none | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Crc32 | gf | none | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LRU | gf | none | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LRU | gf | none | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW FreeList | gf | none | plain | 3 / 3 · 3/3/0/0 | 2 / 3 · 3/3/0/0 | 1 / 3 · 1 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW FreeList | gf | none | salt-diet | 0 / 3 (excl. 0 / 0) · 3/0/3/0 | 0 / 3 · 3/3/0/0 | 0 / 3 · 0 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LZW | gf | none | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LZW | gf | none | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 2 / 3 · 2 / 2 (+1 unscorable) | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Paxos | gf | none | plain | 3 / 3 · 3/3/0/0 | 2 / 3 · 3/3/0/0 | 1 / 3 · 2 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Paxos | gf | none | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 0 / 1 (+2 censored) · 2 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Crc32 | gf | statement | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Crc32 | gf | statement | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LRU | gf | statement | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LRU | gf | statement | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW FreeList | gf | statement | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW FreeList | gf | statement | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 1 / 1 (+2 censored) · 3 / 3 † | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LZW | gf | statement | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LZW | gf | statement | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 2 / 3 · 2 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Crc32 | gf | spec-change | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Crc32 | gf | spec-change | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LRU | gf | spec-change | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LRU | gf | spec-change | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW FreeList | gf | spec-change | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 1 / 3 · 2 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW FreeList | gf | spec-change | salt-diet | 3 / 3 · 3/3/0/0 | 0 / 3 · 3/3/0/0 | 0 / 2 (+1 unscorable) · 0 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LZW | gf | spec-change | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LZW | gf | spec-change | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Paxos | gf | spec-change | plain | not fired | not fired | 0 / 3 · 0 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Paxos | gf | spec-change | salt-diet | not fired | not fired | 1 / 2 (+1 censored) · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Crc32 | bf | none | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Crc32 | bf | none | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 2 / 2 (+1 unscorable) · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LRU | bf | none | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LRU | bf | none | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 2 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW FreeList | bf | none | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW FreeList | bf | none | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 1 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LZW | bf | none | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LZW | bf | none | salt-diet | 3 / 3 · 3/3/0/0 | 2 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Paxos | bf | none | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Paxos | bf | none | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 2 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Crc32 | bf | statement | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW Crc32 | bf | statement | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LRU | bf | statement | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LRU | bf | statement | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 2 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW FreeList | bf | statement | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 2 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW FreeList | bf | statement | salt-diet | 3 / 3 · 3/3/0/0 | 1 / 3 · 3/3/0/0 | 1 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LZW | bf | statement | plain | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
ROW LZW | bf | statement | salt-diet | 3 / 3 · 3/3/0/0 | 3 / 3 · 3/3/0/0 | 3 / 3 · 3 / 3 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
TOTAL gemini-4-argon-high plain: COUNTED 66 / 66 · EXCLUDED 66 / 66 · fired 66 · scored 66 · wedge 0 · other 0 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
TOTAL gemini-4-argon-high salt-diet: COUNTED 63 / 66 · EXCLUDED 63 / 63 · fired 66 · scored 63 · wedge 3 · other 0 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
TOTAL gemini-3.8-flash-high plain: COUNTED 64 / 66 · EXCLUDED 64 / 66 · fired 66 · scored 66 · wedge 0 · other 0 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
TOTAL gemini-3.8-flash-high salt-diet: COUNTED 57 / 66 · EXCLUDED 57 / 66 · fired 66 · scored 66 · wedge 0 · other 0 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
TOTAL gemini-4-argon-high both arms: COUNTED 129 / 132 · EXCLUDED 129 / 129 · fired 132 · wedge 3 · other 0 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
TOTAL gemini-3.8-flash-high both arms: COUNTED 121 / 132 · EXCLUDED 121 / 132 · fired 132 · wedge 0 · other 0 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
NOT-SCORED Z019 zfafgns101 argon FreeList gf none salt-diet r1: WEDGE (TURN-TIMEOUT; end ARM-NO)
NOT-SCORED Z022 zfafgns201 argon FreeList gf none salt-diet r2: WEDGE (WEDGED; end ARM-NO)
NOT-SCORED Z023 zfafgns301 argon FreeList gf none salt-diet r3: WEDGE (WEDGED; end ARM-NO)
FAIL Z015 zfffgnp201 flash FreeList gf none plain r2: TESTS 6/7 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
FAIL Z020 zfffgns101 flash FreeList gf none salt-diet r1: TESTS 6/7 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
FAIL Z021 zfffgns201 flash FreeList gf none salt-diet r2: TESTS 6/7 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
FAIL Z024 zfffgns301 flash FreeList gf none salt-diet r3: TESTS 6/7 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
FAIL Z051 zffpgnp201 flash Paxos gf none plain r2: TESTS 16/17 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
FAIL Z152 zffzbns101 flash LZW bf none salt-diet r1: <none> | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
FAIL Z189 zfffbss201 flash FreeList bf statement salt-diet r2: TESTS 6/7 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
FAIL Z192 zfffbss301 flash FreeList bf statement salt-diet r3: TESTS 6/7 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
FAIL Z236 zfffgxs101 flash FreeList gf spec-change salt-diet r1: TESTS 8/9 REGRESSIONS 1/7 CLAUSE_TESTS 0/2 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
FAIL Z237 zfffgxs201 flash FreeList gf spec-change salt-diet r2: TESTS 8/9 REGRESSIONS 1/7 CLAUSE_TESTS 0/2 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
FAIL Z240 zfffgxs301 flash FreeList gf spec-change salt-diet r3: TESTS 8/9 REGRESSIONS 1/7 CLAUSE_TESTS 0/2 | Z verdict channel: OPEN (ZQ (a), ADDENDUM 3)
A7 gemini-4-argon-high plain: final-phase roots 66 · with a hit 6 · hits 8 | spec-change phase 1 roots 12 · with a hit 2 · hits 2 | roots with no stderr yet 0 | harvested legs 66
A7 gemini-4-argon-high salt-diet: final-phase roots 66 · with a hit 20 · hits 54 | spec-change phase 1 roots 12 · with a hit 4 · hits 13 | roots with no stderr yet 0 | harvested legs 66
A7 gemini-3.8-flash-high plain: final-phase roots 66 · with a hit 0 · hits 0 | spec-change phase 1 roots 12 · with a hit 0 · hits 0 | roots with no stderr yet 0 | harvested legs 66
A7 gemini-3.8-flash-high salt-diet: final-phase roots 66 · with a hit 12 · hits 16 | spec-change phase 1 roots 12 · with a hit 0 · hits 0 | roots with no stderr yet 0 | harvested legs 66
TRUNCATED-ROW cells (a TRUNCATED score row beside the verdict): gemini-4-argon-high plain 6 · gemini-4-argon-high salt-diet 17 · gemini-3.8-flash-high plain 0 · gemini-3.8-flash-high salt-diet 12
EMPTY-TURN cells (>= 1 turn with no output, either phase): gemini-4-argon-high plain 1 · gemini-4-argon-high salt-diet 12 · gemini-3.8-flash-high plain 0 · gemini-3.8-flash-high salt-diet 4
UNREAD fields: 0
```

# §0 · WHAT THIS FILE IS
The desk ZF set (AMENDMENT-ZF-gemini4-argon-2026-10-13.md): gemini-4-argon-high beside its same-day control gemini-3.8-flash-high on the
pilot's 46 conditions at n = 3 (§G1). Every line in the code block is printed by `harness/systems-v3/zf_result.py --print` from the
inputs it names; `--check` proves this file still carries every one of them verbatim.

# §1 · HOW TO READ THE TABLE
- Each cell is `COUNTED (excl. EXCLUDED) · fired/scored/wedge/other` (A6.2). COUNTED makes a wedge a FAIL in its arm's denominator and is the
  headline wherever the two differ, because it is the reading that goes against the arm that wedges. `other` is a NOT-SCORED cell that did not
  wedge; each one is listed by name.
- The PRIMARY comparison is a row's two model columns, fired adjacent in time on one export (§G1, §G3). The last column is HISTORICAL: the 3.x
  cells of record, a patchwork of levels and harness versions (§G4 1–2), and its Pro figures have no same-day counterpart (§G4 4).
- No p-value, no direction, and no claim that the method helps or hurts (§G3).

# §2 · LIMITS THAT RIDE WITH EVERY RATE
1. **A7, the per-turn print timeout binds salt-diet.** The `A7` lines give hits by model and arm. The final-phase figures are the A7.2 command;
   the phase-1 figures are its complement, since A7.4 (2) declares that the A7.2 command reads phase 2 only. A hit says the clock fired.
   Whether a hit changed a verdict is NOT MEASURED (A7.4 (3)). A7 counts ROOTS on the run box; the table counts HARVESTED LEGS, printed
   last on each A7 line. A root whose leg has not yet harvested (a cell in flight at the census) is in A7 and not in the table.
2. **§G4.** The historical column confounds model with harness, client and fence (§G4 1–3). The control is a Flash model, never Pro (§G4 4).
3. **§G5.** Nothing about Gemini 4 against 3.x in general, the other two effort variants, or the O29 qualification.
4. **TRUNCATED-ROW and EMPTY-TURN counts** are printed by arm because both are arm-correlated readings in this campaign (A6, A7). No ZF
   row carries a cause for an empty turn (A6.1).
5. **No token figure is reported here.** The chain's per-leg §G2 reads carry them; on the bus, 4 of the 251 §G2 posts parsed read the
   meter control FAIL with sub-agent tokens UNMEASURED (Z028 · Z172 · Z240 · Z263). Any token figure quoted from this set carries that
   beside it. No rate in this file reads a token.

# §3 · THE CUT (AMENDMENT-ZF ADDENDUM 4 rule 2; council 2026-10-20 ④)
- Rule 2 asks the lead to project the finish and, if it passes 2026-10-27, to cut WHOLE condition pairs from the tail, reporting every short
  condition as short. The Captain ruled the conditional cut at council 2026-10-20 ④: the set ran to the last LZW spec-change leg (Z264) and
  the cut was read there.
- The reading at Z264's harvest (bench's ADA line on the bus, 2026-10-24 23:55): 12 legs remained, all Paxos gf spec-change (plain and
  salt-diet, both models), priced at 51.2 h of wall from Z's own Paxos gf-none wall times the 3.x spec-change ratio, since no Z Paxos
  spec-change leg had run. The elapsed/wall factor over the last 10 · 16 · 30 · 60 · 100 legs was 1.598 · 1.968 · 2.853 · 2.474 · 2.310,
  so the condition needed 82–146 h against 72.1 h to 2026-10-27 23:59. It missed in every window and the set met in every window with it cut.
- So Paxos gf spec-change is CUT whole and reported SHORT 0 of 3 for each of its four model-arm pairs. The cut is registered in
  `zf_result.py` (`CUT`); a cut condition that held any cell would make the tool refuse.
- What the cut costs: this file says nothing about Paxos under a spec change for either Gemini 4 model. The 3.x column still prints its
  historical Paxos spec-change cells for reference only.

# §4 · INPUTS AND HOW THEY WERE MADE
- `evidence/zf-result/zf-cells.tsv` — one row per harvested leg (264), built by `evidence/zf-result/zf_flatten.py` from the harvest
  receipts (extract_legs.py over gemini's harvest directories, with phase 1 of each spec-change leg read from the run box) and the run box's
  turn-loop census (`evidence/zf-result/empty_census.py`). 0 fields UNREAD.
- `evidence/zf-result/pt-census.txt` (268 roots, 4 of them DISCARDED and excluded by A7.4 (1), leaving 264, one per harvested leg) and
  `evidence/zf-result/pt-census-p1.txt` — the A7.2 command and its phase-1 complement (`pt_census.sh`, `pt_census_p1.sh`), run on the
  run box after Z264 with no Z cell live.
- `harness/systems-v3/RESULT-correctness-tables-v3-2026-10-01.md` — the 3.x historical column.
- Rulings on single legs that this table relies on: Z019's wedge (ADDENDUM 6, not re-fired); Z263, LANDED and scored PASS although its
  supervisor line read PERSIST-INDETERMINATE, which is the persistence probe's verdict and not the cell's (bench, bus 2026-10-24 22:56).
