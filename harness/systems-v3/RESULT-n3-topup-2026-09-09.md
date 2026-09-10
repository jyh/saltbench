# RESULT — THE n=3 TOP-UP (AMENDMENT 26). Cut from the scorer's stdout, not retyped.
**systems, 2026-09-09.**

⛔⛔ **EVERY NUMBER IN §3 IS THE INSTRUMENT'S OWN STDOUT, PASTED VERBATIM.** An earlier cut of this file
retyped the tables out of a terminal, and the lead was right to refuse that: *numbers that exist only
in a bus post cannot enter the paper.* This repo's first rule says the same — **never retype a number
from memory or from a message.** The capture below is reproducible byte for byte:
```
  instrument   score_matrix1.py at saltbench origin/main  f520b81
               sha256 87fa6db50e4a7c2e1f7982ecdc9e6e68567301deca872de695e9c98b3821f130
  command      python3 score_matrix1.py            (it computes BOTH readings itself)
  capture      sha256 74cae4c93775b62a3bbf635463a431c4b2d8b3f90d32937f59557bd1f1434f6e
```
📌 **The readings are the instrument's, not a patch of mine.** I first produced A and B from patched
COPIES; the lead has since built the top-up root and the smoke toggle into the scorer itself, so those
patches are retired and this file is cut from the unmodified tool.

## §1 — THE THREE CELLS, CROSS-CHECKED AT THE OBJECT
Two independent instruments agree on every price to the cent — the harvested `METER.txt` and the
cell's own `ctl/post-end-1.tsv`:
```
  cell       harvest METER   post-end final_COST   kind      §31 grace
  n301free   $13.01          13.0111              LANDED       6 s
  n302lru    $9.87            9.8657              LANDED     215 s
  n303paxo   $20.16          20.1567              LANDED      61 s
```
**0 CAP-COST · 0 VOID · 0 replacements owed.** Built in a fresh root (`~/cells-n3-topup`) with a new id
prefix, on ACCOUNT B's config dir, from export `6b6fc12`; the subject-facing tree was driven byte-identical
to matrix #1's harness before firing (AMENDMENT 26 §3).
⚠️ **`n302lru` and `n301free` each harvested VOID once first**, against the wrong account, and were
recovered. See §6 — the recovery is why their good harvest sorts last.

## §1b — ⛔ THE POOLED CELLS SPAN TWO ACCOUNTS, AND NEITHER RESULT FILE SHOWED IT

Measured 2026-09-09 12:0x by `bench` at the run box, while discharging an unrelated provisioning item:
```
  n301free · n302lru · n303paxo   transcripts under  RUN ACCOUNT A   (the top-up)
  every matrix-root cell          transcripts under  RUN ACCOUNT B   (matrix #1)
  ⇒ two DISTINCT v3 run accounts. Which two is not the disclosure; THAT THERE ARE TWO is.
```
📌 The accounts are named by role rather than by directory, per the firewall line on infrastructure
names in a public repo. ⛔ **The first draft of this very paragraph named one of them literally and the
gate refused it** — the same shape as the note in `RULING-placebo-acceptance` §14's neighbourhood, met
again in a paragraph *about* accounts. **A record of a forbidden form must name its ROLE, never its text.**
**This file named its own account and not the contrast; `RESULT-matrix-opus-1` names no account at all.**
So a reader of either file could not tell that reading B — described as *"every cell from this run"* —
**pools cells priced under two different accounts.**

✅ **IT DOES NOT MOVE A PRICE, AND THAT IS MEASURED, NOT ASSUMED.** Both populations are priced from the
**same rate card read on the same day** — `rates rates.tsv read_on 2026-09-05` in the METER of a top-up
cell and of a matrix cell alike. **COST is a rate card applied to token counts, not an account's bill**,
so the account boundary cannot change what a given token count costs.

⚠️ **WHAT IS NOT MEASURED, STATED BECAUSE IT IS THE ONE MECHANISM THAT COULD BITE.** The account cannot
change the price of a token, but it could change the COUNT: **`T` is 98% `cache_read`**, cache state is
per-account and per-session, and nothing here measured whether it differs **systematically** across the
boundary rather than randomly. Cache state already varies cell to cell inside the matrix, so this is not a
new source of variance — **it is a possible SYSTEMATIC one, and it is unquantified.**
⇒ 🔑 ***"EVERY CELL FROM THIS RUN" IS A CLAIM ABOUT A RUN, AND A RUN IS NOT NECESSARILY ONE CONTEXT.***
This is the third structural property of this dataset that the scoreboard was silent about — after the
correctness gap and the smoke cells — and it is disclosed on the same terms: **it travels with the number.**

## §2 — WHAT THE READINGS ARE
```
  READING A   matrix root + top-up + the SS12 smoke cells   43 cells   the continuity reading
  READING B   matrix root + top-up ONLY                     40 cells   every cell from this run
```
The top-up exists so that B is *reachable*: the matrix root held FreeList 2 · LRU 2 · Paxos 2 plain
LANDED cells, so one cell each takes all five problems to **n=3 within their own run**.

## §3 — THE INSTRUMENT'S OUTPUT, VERBATIM

```
==============================================================================
READING A -- THE CONTINUITY READING: matrix root + top-up + the SS12 smoke cells
declared set: 43 cells (37 matrix root + 3 top-up AMENDMENT 26 + 3 smoke SS12)

MATRIX #1 — read from the ARCHIVE, keyed on (task, arm, card_extras)

REFUSED (never defaulted):
  59c93bbe   COST line does not open with a bare price -- refusing rather than scanning on (a VOID meter carries $0.00 in its prose): COST VOID(UNPRICED)
  7fa6c322   COST line does not open with a bare price -- refusing rather than scanning on (a VOID meter carries $0.00 in its prose): COST VOID(UNPRICED)
  823de693   COST line does not open with a bare price -- refusing rather than scanning on (a VOID meter carries $0.00 in its prose): COST VOID(UNPRICED)
  879326db   COST line does not open with a bare price -- refusing rather than scanning on (a VOID meter carries $0.00 in its prose): COST VOID(UNPRICED)

task      arm        extras         n  cells
Crc32     plain      none           3  $5.36 $6.21 $7.64
Crc32     salt-diet  none           3  $6.19 $7.21 $7.63
FreeList  plain      none           4  $13.02 $23.38 $13.77 $13.01
FreeList  salt-diet  none           3  $37.95 $37.60 $35.41
LRU       plain      none           4  $7.75 $9.73 $6.68 $9.87
LRU       salt-diet  none           3  $11.19 $11.21 $14.63
LZW       plain      none           3  $8.15 $20.95 $13.95
LZW       plain      statement      3  $10.24 $11.39 $9.82
LZW       salt-diet  none           3  $31.70 $19.18 $18.16
LZW       salt-diet  statement      3  $22.53 $15.34 $18.54
Paxos     plain      none           4  $9.49 $14.20 $16.78 $20.16
Paxos     salt-diet  none           3  $37.93 $37.65 $23.52
   (run's OWN pooled sd(ln cost) = 0.2487 -- REPORTED ONLY, it gates nothing;
    substituting it would refit the registered gate to the data it judges)

G3 PROVENANCE  REGISTERED sd(ln cost)=0.3046  n=3  k=7.8489  resolvable floor=2.0072x

PRIMARY READING — THE CROSS-PROBLEM SIGN TEST (registered before cell 1)
  Crc32     premium 1.1610x  above 1
  FreeList  premium 2.8070x  above 1
  LRU       premium 1.2826x  above 1
  LZW       premium 1.3749x  above 1
  Paxos     premium 2.4306x  above 1
  5 of 5 problems show a premium > 1   p = 0.0312   -> SIGNIFICANT
  G2 FLOOR 2.0072x at n=3 -- PER PROBLEM (SS14: the floor is per-problem and n is not uniform)
      BELOW  (magnitude UNRESOLVED) : Crc32, LRU, LZW
      CLEARS (magnitude resolvable) : FreeList, Paxos
      => THE REGISTERED HEADLINE IS THE SIGN ACROSS PROBLEMS, NOT A RATIO.
         This is a REPORTING RULE. It is NOT a claim that every magnitude
         fell below: 2 of 5 premium(s) DO clear the floor, and any prose
         saying otherwise contradicts this table.

THE GOLD PAIR — (d) plain+statement vs (e) diet+statement
  LZW       1.8105x
  1 of 1  p = 0.5000  -> NO VERDICT at this k
  ** k=1: the statement arm exists on 1 problem(s). Four cards lack a `## Statement`
     section (SS16), so this pair CANNOT reach .05 and is reported without a verdict. **

==============================================================================
READING B -- SMOKE OUT: matrix root + top-up ONLY, every cell from this run
declared set: 40 cells (37 matrix root + 3 top-up AMENDMENT 26 + 0 smoke SS12)

MATRIX #1 — read from the ARCHIVE, keyed on (task, arm, card_extras)

REFUSED (never defaulted):
  59c93bbe   COST line does not open with a bare price -- refusing rather than scanning on (a VOID meter carries $0.00 in its prose): COST VOID(UNPRICED)
  7fa6c322   COST line does not open with a bare price -- refusing rather than scanning on (a VOID meter carries $0.00 in its prose): COST VOID(UNPRICED)
  823de693   COST line does not open with a bare price -- refusing rather than scanning on (a VOID meter carries $0.00 in its prose): COST VOID(UNPRICED)
  879326db   COST line does not open with a bare price -- refusing rather than scanning on (a VOID meter carries $0.00 in its prose): COST VOID(UNPRICED)

task      arm        extras         n  cells
Crc32     plain      none           3  $5.36 $6.21 $7.64
Crc32     salt-diet  none           3  $6.19 $7.21 $7.63
FreeList  plain      none           3  $13.02 $23.38 $13.01
FreeList  salt-diet  none           3  $37.95 $37.60 $35.41
LRU       plain      none           3  $7.75 $9.73 $9.87
LRU       salt-diet  none           3  $11.19 $11.21 $14.63
LZW       plain      none           3  $8.15 $20.95 $13.95
LZW       plain      statement      3  $10.24 $11.39 $9.82
LZW       salt-diet  none           3  $31.70 $19.18 $18.16
LZW       salt-diet  statement      3  $22.53 $15.34 $18.54
Paxos     plain      none           3  $9.49 $16.78 $20.16
Paxos     salt-diet  none           3  $37.93 $37.65 $23.52
   (run's OWN pooled sd(ln cost) = 0.2569 -- REPORTED ONLY, it gates nothing;
    substituting it would refit the registered gate to the data it judges)

G3 PROVENANCE  REGISTERED sd(ln cost)=0.3046  n=3  k=7.8489  resolvable floor=2.0072x

PRIMARY READING — THE CROSS-PROBLEM SIGN TEST (registered before cell 1)
  Crc32     premium 1.1610x  above 1
  FreeList  premium 2.8879x  above 1
  LRU       premium 1.1521x  above 1
  LZW       premium 1.3749x  above 1
  Paxos     premium 2.2437x  above 1
  5 of 5 problems show a premium > 1   p = 0.0312   -> SIGNIFICANT
  G2 FLOOR 2.0072x at n=3 -- PER PROBLEM (SS14: the floor is per-problem and n is not uniform)
      BELOW  (magnitude UNRESOLVED) : Crc32, LRU, LZW
      CLEARS (magnitude resolvable) : FreeList, Paxos
      => THE REGISTERED HEADLINE IS THE SIGN ACROSS PROBLEMS, NOT A RATIO.
         This is a REPORTING RULE. It is NOT a claim that every magnitude
         fell below: 2 of 5 premium(s) DO clear the floor, and any prose
         saying otherwise contradicts this table.

THE GOLD PAIR — (d) plain+statement vs (e) diet+statement
  LZW       1.8105x
  1 of 1  p = 0.5000  -> NO VERDICT at this k
  ** k=1: the statement arm exists on 1 problem(s). Four cards lack a `## Statement`
     section (SS16), so this pair CANNOT reach .05 and is reported without a verdict. **

==============================================================================
A vs B -- DOES THE HEADLINE DEPEND ON THE BORROWED SMOKE CELLS?
  A: 5 of 5   p = 0.0312        B: 5 of 5   p = 0.0312
  ⇒ IDENTICAL SIGN VERDICT WITHOUT THE BORROWED CELLS.
     The published smoke-cell dependency is DISCHARGED. Report both readings anyway:
     the reader cannot reconstruct the set from a single number.
```

## §4 — ⭐ THREE FOR THREE ON A PRE-REGISTERED BOUND
AMENDMENT 26 §5 computed each problem's reachable premium range at n=4 **before any cell ran**:
```
  FreeList   registered 2.0242 .. 2.8070   ->  READING A gives 2.8070   EXACT UPPER BOUND
  LRU        registered 1.2826 .. 1.5537   ->  READING A gives 1.2826   EXACT LOWER BOUND
  Paxos      registered 2.4306 .. 3.1786   ->  READING A gives 2.4306   EXACT LOWER BOUND
```
Explicable rather than remarkable: at n=4 the median is the mean of the middle pair, so a cell falling
outside that pair drives the median to one end of its reachable set — and all three did.
⇒ The §5 invariance claim (**no outcome of this top-up can move a premium to 1**) is exercised at both
extremes and held.
⛔ **AND ITS CONVERSE, UNCHANGED: because it could not change the verdict, it did not confirm it.** This
bought precision and removed a dependency. **It is not a replication and may not be written as one.**

## §5 — ⛔ THE DIVERGENCE BETWEEN A AND B, WHICH IS SMALL AND IS NOT NOTHING
Derived from §3's two tables:
```
  problem     A        B        move      cause
  LRU       1.2826 -> 1.1521  -0.1305   the CHEAPEST plain cell ($6.68) leaves; the plain median RISES
  Paxos     2.4306 -> 2.2437  -0.1869   same direction, same cause ($14.20 leaves)
  FreeList  2.8070 -> 2.8879  +0.0809   $13.77 sat near the middle; removing it LOWERS the median
  Crc32 / LZW  unchanged — neither problem has a smoke cell
```
⛔ **B's LRU premium, 1.1521x, is the closest to 1.0 any premium has come in this campaign, and the
smoke cells were flattering it.** Three of five moved and two moved DOWN. ⇒ **A and B agree on the SIGN
and the p-value and NOT on the magnitudes** — which is why the instrument prints both and why the
paper must carry both.
📌 On G2, quote §3's table and not a summary of it: **`BELOW: Crc32, LRU, LZW` · `CLEARS: FreeList,
Paxos`.** The rule is that the headline is the SIGN, not a ratio; it is **not** a claim that every
magnitude fell below, and 2 of 5 do clear the floor.

## §6 — WHAT IS UNCHANGED, AND WHAT NEARLY WENT WRONG
* The sign test is **ONE-SIDED** and cannot significantly refute the hypothesis.
* Matrix #1 remains a **COST** result with **N = 0** correctness verdicts on a withheld suite. **These
  three cells add none.** No sentence may pair a premium with correctness or "working code".
* `n303paxo` at $20.16 is the dearest Paxos plain observation on record and ran ~2.4x its
  condition-mates' wall; **~6 minutes of that bought zero tokens**, in a blocked subject tool call that
  cleared on its own and was deliberately not touched.
* Concurrency: these three ran **3-wide** against matrix #1's 4-wide (AMENDMENT 26 §8, declared before
  the fire, not discovered after).
* ⛔ **THE NEAR-MISS WORTH RECORDING:** the harvest daemon was started without `CLAUDE_CONFIG_DIR` and
  read the transcript slug under the wrong account, producing `VOID(UNMETERED)` for two landed, fully
  priced cells — and `priced()` matched `^COST `, which the VOID line satisfies, so the daemon would
  **never have retried them.** Both were recovered by hand; both defects are fixed and driven.
  ⚠️ A fragility this leaves: the scorer selects `hv[-1]`, the lexicographically last harvest dir —
  **not the last one carrying a price.** These two are safe only because the good harvest sorted
  second. The robust form is *"the latest harvest that parses as a bare price"*.
