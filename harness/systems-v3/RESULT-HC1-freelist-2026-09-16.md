# RESULT — HC STAGE 1, **FreeList COMPLETE AT n = 3**: §3a's cap-out prediction is **FALSIFIED**, and the premium **RESOLVES at 2.385×**

## bench (SaltBench lead), 2026-09-16. Registered design: `PREDICTIONS-HC-stage1-2026-09-13.md` (PR #121, helm-signed as non-author).
## Companion instrument correction carried by this wave: `AUDIT-hc1-budget-read-column-2026-09-15.md`.

> ## ⭐ WHAT IS NEW HERE, IN ONE SENTENCE
> **This is the first problem of HC stage 1 that could decide anything, and it decided two registered
> questions in opposite directions: the sharpest prediction in the design is refuted, and the effect the
> campaign exists to measure is resolved for the first time.**

---

## 0 · PROVENANCE OF EVERY NUMBER IN THIS FILE

Per this repository's rule that every number names the file it came from and is never retyped from
memory or from a message:

```
  per-cell COST, T, the four token classes, and the price/bound/floor KIND
        cell_meter.py per cell, via the wave harvester, transcribed into the wave's fire order AT
        EACH LANDING; the standing per-arm view is hc1_token_table.py, which reads the same meter.
  registered BANDS, the resolvable FLOOR, the cost cap and the falsification rules
        PREDICTIONS-HC-stage1-2026-09-13.md, in this repository, at its merged sha.
  the §3b per-cell budget-read column
        budget_read_column.py over each cell's own session transcript; see the companion AUDIT for
        why the earlier reading of this column was inoperative.
  the terminal CLASS of each cell (LANDED / capped)
        each cell's own ctl/end-1 marker, read as its own text and never summarised.
```

⚠️ **One provenance gap, declared:** the wave's fire order is an operational file on the run box and is
**not tracked here**, because it names run-box and account detail that must not enter a public tree. The
authoritative source for every cost is the per-cell meter output, which the fire order records and does
not replace.

## 1 · THE TRIPLE

Nine cells, fired **one at a time**, per problem and cheapest-first. Every cell `card_extras = none`.

```
  arm         cells                             MEDIAN    registered band        verdict
  plain       $14.03 · $19.94 · $10.96          $14.03    [$ 8.04 , $22.77]      INSIDE
  placebo     $11.39* · $9.89 · $14.14          $11.39    [$ 8.04 , $22.77]      INSIDE
  salt-diet   $33.46 · $37.72^ · $29.80         $33.46    [$22.56 , $63.92]      INSIDE

      * = INTERRUPT-BOUND   one interrupted turn; understated by a MEASURED, sub-1 % share
      ^ = CAP-FLOOR         stopped at the cost cap; understated by an UNKNOWN amount
```

⇒ **6 of 15 cell groups resolved across the stage.**

⚠️ **The placebo median IS the interrupt-bound cell, so that median is a bound.** A median of three is
whichever cell sits in the middle, so it inherits that cell's *kind*. The understatement is 0.0852 % of
cost — **and the size is not the point; the kind is.**

## 2 · ⛔ §3a's CAP-OUT PREDICTION IS **FALSIFIED**

§3a registered, before the first cell fired:

> `salt-bare FreeList   PREDICTION: CAPS OUT at C1_USD 37.21, in at least 2 of its 3 cells`
> falsified by the arm landing at or below $37.21 in 2 of 3 cells.

```
  hc1fs01   $33.46   at or below the cap
  hc1fs02   $37.72   CAPPED OUT (ENDED-NOT-LANDED)
  hc1fs03   $29.80   at or below the cap
  ⇒ TWO OF THREE AT OR BELOW.  FALSIFIED.
```

**This is the first falsification of HC stage 1.** It was registered by this seat and refuted by this
seat's own cells.

### 2.1 · The rescue that was available three times and was never taken

§3b establishes that the cost cap is visible to the subject, so a landing just under it may be *pacing*
rather than evidence. That caveat was available **three times**:

- **at row 12**, when `hc1fs01` landed below the cap and invoking it would have *hurt* the prediction;
- **at row 15**, when `hc1fs02` capped out and the §3b column made the contrast vivid — `hc1fs01` had
  read `BUDGET.md` **seven times** including three late `sed -n '4p'` reads, while `hc1fs02` read it
  **once, early**, and ran past the cap;
- **tonight**, when invoking it would have rescued §3a outright.

**It was not taken.** §3b bands the pacing zone at `[$35.35, $37.21)`; both below-cap cells landed
**below that band**, and the registered rule for BELOW is FALSIFIES. The §3b column is reported beside
every cell in this result and rescues none of them.

⇒ 🔑 **A caveat registered to stop an instrument flattering its author must not be reached for the
moment it would rescue them.**

⚠️ The read-count contrast is recorded as an **observation**, never as a mechanism: it is n = 1 against
n = 1, and reverse causality is fully live — a cell in difficulty may read its budget *because* it is in
difficulty.

## 3 · ⭐ THE PREMIUM **RESOLVES** — THE FIRST TIME IN THIS STAGE

```
  salt-diet median / plain median  =  $33.46 / $14.03  =  2.385x
  n = 3 resolvable floor                                  2.0072x    ⇒ ABOVE ⇒ RESOLVED
  matrix-#1 anchor                                        2.8070x    ⇒ measured LOWER than anchor
```

§2 registered, before any cell fired, that **three of the five problems cannot resolve an effect of this
size at n = 3** — and named FreeList as one of the two that can. **Crc32 duly came back UNRESOLVED at
1.078×; FreeList resolves at 2.385×.**

⇒ **A design that names in advance which of its problems can lose is a design whose wins mean
something.** The measured premium is reported as measured, not as agreement with the anchor.

## 4 · ✅ THE CAP DID NOT CONTAMINATE THE MEDIAN — AND THAT WAS NOT GUARANTEED

`hc1fs02` is a **cap-floor**: stopped at the cap, its true cost unknown and strictly higher. It is also
the arm's **maximum**, and uncapping can only raise it further.

```
  sorted: [ $29.80 , $33.46 , $37.72^ ]   ⇒ the median is the MIDDLE cell, and it is a PRICE
```

⇒ **A cap-floor ABOVE the median cannot move the median.** Had the capped cell landed *below* the
median, the median would itself have been a floor and the premium a **lower bound**.

⚠️ **This was an accident of arrangement, not of care.** Any future scorer must check **where** a floor
sits relative to the median before quoting a premium from an arm containing one.

## 5 · THE §3b COLUMN, PER CELL

```
  plain      hc1fp01 READ   hc1fp02 READ   hc1fp03 READ
  placebo    hc1fb01 READ   hc1fb02 READ   hc1fb03 READ
  salt-diet  hc1fs01 READ (7 reads)   hc1fs02 READ (1, early)   hc1fs03 READ (1)
  ⇒ 9 of 9 READ. Zero via the Read tool; every one via a read verb inside a Bash call.
```

Under the criterion as it was operationally restated before 2026-09-15, this column would have scored
**0 of 9**. See the companion AUDIT.

## 6 · THE PLACEBO READING — **UNRESOLVED**, FOR THE SECOND TIME AND IN THE OPPOSITE DIRECTION

```
  placebo median / plain median  =  $11.39 / $14.03  =  0.812x   against a registered 1.00
  deviation from parity 1.232x, far below the n=3 resolvable floor of 2.0072x
```

§3 registers that the placebo prediction **can only be refuted, never confirmed**. Crc32 returned
**1.051×** (just above parity); FreeList returns **0.812×** (below it). **Opposite directions, same
verdict: UNRESOLVED.** Claimed, 0.812× would assert the placebo is *cheaper* than plain — noise inside
an unresolvable band, and n = 3 does not make it a finding.

## 7 · LIMITATIONS, DECLARED

1. **One cell of the salt-diet arm is censored at the cap.** The arm's true central tendency is not
   observable above $37.21. The median is unaffected (§4), but the arm's *mean* and its upper spread are
   not measurable from these cells.
2. **The placebo median is a bound** (§1).
3. **`hc1fs03`'s quota bracket is VOID and was declared void at the fire**: the cell ran 99 minutes
   across a session-pool reset, computed before firing. Three of the wave's other brackets are valid and
   none prices a single cell in any case.
4. **These cells ran on a different subscription account from the matrix-#1 anchors**, by the Captain's
   capacity ruling — a declared limitation, not a drift.
5. **Absolute per-cell dollars are time-dependent and are not a stable per-cell price.** The plain arm
   spans **1.82× min to max** on identical conditions, with sub-agent cost share running 30 % · 51 % ·
   40 %. Quote medians and ratios, not single cells.

## 8 · WHAT THIS DOES NOT SAY

It does not say the salt method is worth 2.385× on FreeList in general: it says that **on this problem,
at n = 3, under this harness and these caps, the salt-diet median stands at 2.385× the plain median, and
that ratio is above the floor this design registered as its resolution limit.** It does not make
matrix-#1's cells substitutable. It does not close HC stage 1: **9 of 15 cell groups remain**, and the
three problems still to fire — LRU, LZW, Paxos — were registered in advance as **two that cannot resolve
an effect this size at n = 3 and one that can.**
