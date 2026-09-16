# RESULT — HC STAGE 1, **LRU COMPLETE AT n = 3**: three medians inside their bands, and the premium is **UNRESOLVED, AS REGISTERED**

## bench (SaltBench lead), 2026-09-16. Registered design: `PREDICTIONS-HC-stage1-2026-09-13.md` (PR #121, helm-signed as non-author).

> ## ⛔ READ THIS BEFORE ANY NUMBER BELOW
> **The 1.077× premium is a PREDICTED-UNDERPOWERED reading, NOT A NULL.** §2 named LRU, before a single
> cell fired, as one of three problems of five whose effect size (anchor 1.2826×) sits **below** the n = 3
> resolvable floor of 2.0072×. This problem was never able to say whether the treatment helped at n = 3.
> **"The method did not help on LRU" is the reading this file exists to refuse.**

---

## 0 · PROVENANCE

```
  per-cell COST, T, and KIND (price / interrupt-bound)
        cell_meter.py per cell via the wave harvester, transcribed into the wave's fire order at each
        landing; the standing per-arm view is hc1_token_table.py, reading the same meter.
  registered BANDS, the FLOOR, and the ANCHOR
        PREDICTIONS-HC-stage1-2026-09-13.md, at its merged sha.
```
⚠️ **Declared gap:** the fire order is an operational file on the run box and is not tracked here (it
names run-box and account detail). The authoritative source for every cost is the per-cell meter output.

## 1 · THE TRIPLE

```
  arm         cells                          MEDIAN   KIND     registered band        verdict
  plain       $10.26 · $8.85 · $7.04*        $8.85    price    [$ 5.24 , $14.86]      INSIDE
  placebo     $6.30 · $9.00 · $7.03*         $7.03    BOUND    [$ 5.24 , $14.86]      INSIDE
  salt-diet   $9.53 · $12.74 · $8.64         $9.53    price    [$ 6.73 , $19.06]      INSIDE

      * = INTERRUPT-BOUND: one interrupted turn, understated by a measured sub-1 % share of cost
```
⇒ **9 of 15 cell groups resolved across the stage. 1 falsification (FreeList, §3a).**

## 2 · WHICH MEDIANS ARE PRICES, AND WHY — CHECKED, NOT ASSUMED

A median of three is whichever cell sits in the middle, so it **inherits that cell's kind**. Each arm
containing a bound was checked for where the bound sits:

- **plain** — the bound `$7.04*` is the arm's **minimum**. Understatement can only raise it *toward* the
  median; to reach `$8.85` it would need **+25.7 %**, against a measured understatement of **0.3597 % of
  cost**. ⇒ **The median is a PRICE, protected by magnitude (71× margin).**
- **placebo** — the bound `$7.03*` **is** the median cell. ⇒ **The median is a BOUND.** Numerically it is
  within $0.0056 of $7.03 (0.0800 % of cost) — **and the size is not the point; the kind is.**
- **salt-diet** — no bound. ⇒ **The median is a PRICE.**

⚠️ The margin above is stated in **% of cost**, the unit of the median it protects. An earlier computation
used % of T, which is a bound on a different quantity; it was corrected before this file was written.

## 3 · THE PREMIUM — **UNRESOLVED**, AS §2 REGISTERED

```
  salt-diet median / plain median  =  $9.53 / $8.85  =  1.077x
  n = 3 resolvable floor                                 2.0072x    ⇒ BELOW ⇒ UNRESOLVED
  matrix-#1 anchor                                       1.2826x
```

This is the second problem of the stage to return UNRESOLVED **exactly as registered**, after Crc32
(1.078×). Between them sits FreeList, which §2 named as able to resolve — and which did, at 2.385×.
⇒ **A design that names in advance which of its problems can lose is the reason the one that resolved
means something.**

### 3.1 · The single-cell rows pointed opposite ways, which is why neither was ever a result
```
  n = 1 row   salt-diet / plain  =  $9.53 / $10.26  =  0.929x   (salt-diet CHEAPER)
  n = 2 row   salt-diet / plain  =  $12.74 / $8.85  =  1.440x   (salt-diet dearer)
  medians                                               1.077x
```
The n = 1 figure was recorded at its landing as **unusable in either direction**, *before* the n = 2 row
reversed it. A ratio of single cells is a different quantity from a ratio of medians.

## 4 · THE PLACEBO READING — **UNRESOLVED**

```
  placebo median / plain median  =  $7.03 / $8.85  =  0.794x    against a registered 1.00
```
Deviation from parity 1.259×, below the floor. §3 permits the placebo prediction only to be **refuted**,
never confirmed. **Three problems now return three placebo readings — Crc32 1.051×, FreeList 0.812×,
LRU 0.794× — two below parity, one above, all UNRESOLVED.** And this one is additionally a bound.

## 5 · INTERRUPTED RECORDS

Both interrupt-bounds sit in **sub-agent (`exec`) turns**, never the head — making that registered
observation **7 of 7** across two campaigns and both models.

## 6 · LIMITATIONS, DECLARED

1. **The placebo median is a bound** (§2).
2. **The final cell's quota bracket is VOID, declared at the fire:** it straddled a session-pool reset,
   exactly as computed before firing (siblings ran 22 and 27 minutes; this cell ran 28). No quota figure
   prices a single cell in any case.
3. **These cells ran on a different subscription account from the matrix-#1 anchors**, by the Captain's
   capacity ruling.
4. **Absolute per-cell dollars are not a stable price.** Quote medians and ratios, not single cells.

## 7 · WHAT THIS DOES NOT SAY

It does not say the salt method helped on LRU, and it does not say it failed. **At n = 3 on this problem,
neither statement is available**, and that was registered before the first cell fired. It does not make
matrix-#1's cells substitutable. HC stage 1 has **two problems remaining**: LZW, registered as unable to
resolve at n = 3, and Paxos, registered as able — and carrying three predicted cap-outs whose status
FreeList's falsification has reopened.
