# RESULT — HC STAGE 1, **Paxos COMPLETE AT n = 3**: three medians inside their bands, §3a reads **NEAR-CAP**, and the premium is **UNRESOLVED BY CENSORING** — the cap sits below the resolvable threshold

## bench (SaltBench lead), 2026-09-16. Registered design: `PREDICTIONS-HC-stage1-2026-09-13.md` (PR #121, helm-signed as non-author).

> ## ⛔ READ THIS BEFORE ANY NUMBER BELOW
> §2 named Paxos, before a single cell fired, as one of the **two** problems of five whose anchor effect (2.4306×) sits
> **above** the n = 3 resolvable floor of 2.0072×. **It does not resolve, and the reason is the instrument, not the effect.**
> With the plain median at $20.23, resolving needs a salt-diet median of $40.61. Capped cells enter the median at the cap,
> $37.21 (§4.2), so no salt-diet median above $37.21 was attainable. §3a registered this before the fire: *"on those two
> problems a lower HC median is NOT evidence of a smaller effect; it is the cap."* **1.8× here is a censored reading. It is
> not a smaller effect.** The verdict was posted on the bus while the last cell was still running, bounded for every
> possible landing, so it could not be fitted to that cell.

---

## 0 · PROVENANCE

```
  per-cell COST, T, and KIND (price / interrupt-bound / cap-out)
        cell_meter.py per cell via the wave harvester, transcribed into the wave's fire order at each
        landing; the per-cell price receipt is hc1-price-receipt.sh, reading the same meter.
  registered BANDS, the FLOOR, the ANCHOR, §3a and §3b
        PREDICTIONS-HC-stage1-2026-09-13.md, at its merged sha.
  the §3b column, the build-wait census and the concurrency census
        evidence/hc1-stage1-instruments-2026-09-16/ (merged ab61bbe); the concurrency census re-run over all 45 cells is
        concurrency/census-45.out in that directory, added with this file.
```
⚠️ **Declared gap:** the fire order is an operational file in the run environment and is not tracked here (it
names run-environment and account detail). The authoritative source for every cost is the per-cell meter output.

## 1 · THE TRIPLE

```
  arm         cells                           MEDIAN   KIND     registered band        verdict
  plain       $20.23 · $16.51 · $22.01*       $20.23   price    [$ 9.29 , $26.33]      INSIDE
  placebo     $15.19 · $23.17* · $16.89       $16.89   price    [$ 9.29 , $26.33]      INSIDE
  salt-diet   $37.63^ · $36.76 · $36.78*      $36.78*  BOUND    [$22.59 , $64.00]      INSIDE

      * = INTERRUPT-BOUND: interrupted sub-agent turns, understated by a measured sub-1 % share of cost
      ^ = CAP-OUT: the watcher ended the cell at C1_USD; metered $37.63, it enters the median at the cap, $37.21 (§4.2)
```
⇒ **All 15 cell groups of the stage now sit inside their registered bands.**

## 2 · WHICH MEDIANS ARE PRICES, AND WHY — CHECKED, NOT ASSUMED

- **plain** — the one bound, `$22.01*`, is the arm's **maximum**. Understatement can only raise it, so it cannot move the
  median. ⇒ **The median is a PRICE.**
- **placebo** — the one bound, `$23.17*`, is the arm's **maximum**. ⇒ **The median is a PRICE**, for the same reason.
- **salt-diet** — the median cell, `$36.78*`, **is** the bound, so the median is a **LOWER BOUND**, tight to its measured
  understatement of 0.1075 % of cost ($0.039524). It cannot move past the cap cell above it. ⇒ **Every verdict below holds
  unless that one interrupted sub-agent record is understated by more than $0.43, over ten times its recorded cost.**

## 3 · §3a — THE CAP-OUT PREDICTION: **NEAR-CAP**

```
  §3a    salt-bare Paxos  PREDICTION: CAPS OUT at C1_USD 37.21, in at least 2 of its 3 cells
  §3b    NEAR-CAP band [$35.35, $37.21) is its own outcome, neither a cap-out nor a falsification

  row 39  hc1ps01   CAP-OUT    $37.63 metered, ended by the watcher at the cap    §3b column READ-NOT-SEEN
  row 42  hc1ps02   NEAR-CAP   $36.76                                              §3b column READ-NOT-SEEN
  row 45  hc1ps03   NEAR-CAP   $36.78* (watcher at END $35.84)                     §3b column READ-SAW (last seen $11.57)
```
⇒ **One cap-out of three, against the two the prediction needs, and a median of $36.78\* inside [$35.35, $37.21) ⇒
NEAR-CAP.** Per §3b that is its own outcome: **neither a confirmation nor a falsification.** Two things ride beside it:
(i) row 45 landed by its own act, with the watcher reading $35.84 at END. An unrecorded in-flight turn of $0.43 (1.16 % of
cost) would have reached the cap, and the watcher's model of in-flight cost ($0.18) under-states by construction, so the
class is the meter's reading and not a guarantee; row 42 carries the same caveat. (ii) Row 45 last saw the countdown at
$11.57, 32 minutes in, so its landing near the cap is **not** evidence of pacing to a countdown.
**§3a across the stage: FreeList FALSIFIED, Paxos NEAR-CAP.**
⚠️ **The §3b column rides beside the verdict and does not decide it.** The subjects' opening reads of `BUDGET.md` mostly
ran before the watcher's first write, so READ-NOT-SEEN is the common case across the stage (see the instruments README).

## 4 · THE PREMIUM — **UNRESOLVED BY CENSORING**, NOT BY SIZE

```
  salt-diet median / plain median  =  $36.78* / $20.23 =  1.818x
  n = 3 resolvable floor (min(n) = 3)                             2.0072x   ⇒ BELOW ⇒ UNRESOLVED
  salt-diet median needed to resolve   2.0072 × $20.23 = $40.61   >   C1_USD $37.21
  matrix-#1 anchor (reading B)                                    2.4306x
```
⇒ **Under this cap, at this plain median, no set of landings could have resolved Paxos.** The bound was posted before
the last cell landed: for every possible landing the premium lies in [1.8171×, 1.8393×].
⛔ **So this is not "the treatment premium on Paxos is 1.84×."** It is: *the instrument cannot report a Paxos salt-diet
median above $37.21, and the plain median makes $40.61 the threshold.* Reading B's anchor cells include two above the
cap ($37.93, $37.65), which is §3a's registered limitation realised.

## 5 · THE PLACEBO READING — **UNRESOLVED**

```
  placebo median / plain median  =  $16.89 / $20.23  =  0.835x    against a registered 1.00
```
§3 permits the placebo prediction only to be **refuted**, never confirmed. A reading of 0.835× is within the floor on
either side of parity, so it is UNRESOLVED. **Five problems now return five placebo readings — Crc32 1.051×, FreeList
0.812×, LRU 0.794×, LZW 1.551×, Paxos 0.835× — all UNRESOLVED.**

## 6 · INTERRUPTED RECORDS

Three interrupt-bounds in this triple (plain n = 3, placebo n = 2, salt-diet n = 3), each in a **sub-agent (`exec`) turn**,
never the head; the salt-diet one is 0.1075 % of its cell's cost. The harvester records every interrupted record measured so
far in a sub-agent turn.

## 7 · LIMITATIONS, DECLARED

1. **Concurrency, and on Paxos it is not balanced by arm.** PREDICTIONS §6.3 item 3 registered *no cell of any wave
   running*; until 2026-09-16 the fire script checked HC1 cells only. On Paxos, plain n = 2 shared 38 % of its window
   with agy cells, placebo n = 2 shared 91 % and placebo n = 3 shared 12 %; plain n = 1 and n = 3 and every salt-diet cell
   shared none, measured over the final 45 cells. **If** box load raises cost, it inflates the plain and placebo arms, which shrinks the premium and raises
   the placebo ratio. That is a sign, not a size. Across the whole stage (45 cells) the shares are plain 43.5 % · placebo 41.4 %
   · salt-diet 37.4 %: close, and the treatment arm is the least exposed, so any load effect leans toward shrinking premiums. The last cell fired through a guard enforcing the registered text.
2. **Quota brackets never price a single cell**, and several here carry the seat's own work inside the window.
3. **These cells ran on a different subscription account from the matrix-#1 anchors**, by the Captain's capacity ruling.
4. **Absolute per-cell dollars are not a stable price.** Quote medians and ratios, not single cells.

## 8 · WHAT THIS DOES NOT SAY

It does not say the salt method's cost premium on Paxos is 1.84×, and it does not say the premium is smaller than
matrix #1's. **The cap censors the treatment arm, and the file declines to read a censored median as an effect size.**
⛔ **Wherever this result is counted, it is counted as UNRESOLVED-BY-CENSORING, never as a bare UNRESOLVED.** A censored
reading and a measured null print the same word in a grid, and only the first is a fact about the instrument. How a
matrix cell or the paper carries that distinction is an open question, raised for the 2026-09-17 sitting.
It does not make matrix-#1's cells substitutable. **With Paxos complete, HC stage 1 is complete**; the stage result, with
the matrix count re-cut in the same commit (council 2026-09-16 ⑤d), is its own file.
