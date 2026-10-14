# O57: agy sub-agent tokens the meter never saw (2026-10-13)

**Finding.** The agy cost figures (v3 cost tables, `evidence/v3-cost-tables-2026-09-28/`) take T from `ctl/agy-meter-N.json`, which
`agy_meter_v3.py` reads from the PARENT conversation's stream-json. A sub-agent the subject dispatches runs in its own conversation, and
its usage is not in that stream. So its tokens are never metered.

**Method.** Every conversation keeps its own record in the client home, `conversations/<id>.db`, whose `gen_metadata` protobuf carries
usage at field path 1.4.x (1.4.2 input, 1.4.3 output, 1.4.5 cache-read, 1.4.9 thinking). `pbsum.py` sums every varint by field path.
**Positive control:** on cell l8cpss01's parent conversation it reproduces that cell's meter exactly: input 661,970, output 50,434,
cache-read 7,119,442, thinking 27,376, so meter T 7,831,846 = input + output + cache-read. `unmetered2.py` classes each db as METERED (an id
the parent stream itself carries) or SUB-AGENT (any other), over every AGY cell of `evidence/v3-cost-tables-2026-09-28/cellroots.tsv`, run on
the run box at zero spend. `unmetered2.out` holds one row per cell and the per-arm totals as its last lines.

```
  arm        cells   meter T          sub-agent T never metered     cells with a sub-agent
  plain      135       566,780,515          884,196   (+0.2 %)       2
  salt-diet  137     2,858,155,649      434,359,169   (+15.2 %)      76
```
**The defect is arm-correlated, and its sign favours the arm under test:** salt-diet's method dispatches refuter sub-agents and plain's does
not. Every agy salt-diet ÷ plain token or dollar ratio is biased LOW, toward salt-diet looking cheaper.

**Limits.** Both arms' figures are FLOORS. 60 of the 332 metered conversations have no db, one per level-8 cell of either arm (the phase-1
conversation of a spec-change cell, set aside before phase 2), so a sub-agent inside one of those phases is missing too. The metered conversations' db T is NOT
reconciled with the meter cell by cell here, and nothing is claimed about the meter's own accuracy. Price impact (per-model tier rules) is
not computed here. The Claude lane is a different meter and is not covered by this finding.
