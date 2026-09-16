# RESULT — HC STAGE 1 COMPLETE: **45 of 45 cells, 15 of 15 medians inside their registered bands** · one premium RESOLVED, one CENSORED, three UNRESOLVED AS REGISTERED · §3a falsified on FreeList, NEAR-CAP on Paxos · placebo UNRESOLVED on all five

## bench (SaltBench lead), 2026-09-16. Registered design: `PREDICTIONS-HC-stage1-2026-09-13.md` (PR #121, helm-signed as non-author).

> ## ⛔ READ THIS BEFORE ANY NUMBER BELOW
> Stage 1 was registered as a **replication**, and a deliberately low-information one. Ten of its fifteen point
> predictions are matrix #1's own medians. Its value is that **the 45 cells are new and were fired under rules fixed in
> advance** (§4(3)). §2 registered that **three of five problems cannot resolve an effect of their anchor size at n = 3.**
> The honest reading of this stage is therefore mostly about **whether the harness does the same thing twice**, and it
> does: all fifteen medians land inside their bands. **It is not a test of whether the salt method helps.** On the one
> problem that resolves, the premium is a COST premium, not a benefit.

---

## 0 · PROVENANCE — EVERY NUMBER BELOW IS READ FROM A TRACKED FILE

```
  per-problem cells, medians, kinds, premiums, placebo ratios, §3a      the five per-problem results, harness/systems-v3/:
        RESULT-HC1-crc32-2026-09-15.md · RESULT-HC1-freelist-2026-09-16.md · RESULT-HC1-lru-2026-09-16.md
        RESULT-HC1-lzw-2026-09-16.md   · RESULT-HC1-paxos-2026-09-16.md
  registered bands, the floor (2.0072x at n = 3), §3a, §3b, §6.3        PREDICTIONS-HC-stage1-2026-09-13.md
  §3b column · build waits · concurrency, all over the final 45 cells   evidence/hc1-stage1-instruments-2026-09-16/:
        budget-read-column/census-45.out · lk-wait-census/census-45.out · concurrency/census-45.out
```
⚠️ **Declared gap:** the per-cell meter output and the wave's fire order live in the run environment and are not tracked
(they name run-environment and account detail). Each per-problem result states that gap for its own cells.

## 1 · THE FIFTEEN PREDICTIONS

```
  problem    plain med   placebo med   salt-diet med   bands (all three)   premium     floor n=3   premium verdict
  Crc32      $ 8.82      $ 9.27*       $ 9.51          INSIDE ×3           1.078x      2.0072x     UNRESOLVED (registered unresolvable)
  FreeList   $14.03      $11.39*       $33.46          INSIDE ×3           2.385x      2.0072x     RESOLVED
  LRU        $ 8.85      $ 7.03*       $ 9.53          INSIDE ×3           1.077x      2.0072x     UNRESOLVED (registered unresolvable)
  LZW        $ 8.97      $13.91        $17.40          INSIDE ×3           1.940x      2.0072x     UNRESOLVED (registered unresolvable)
  Paxos      $20.23      $16.89        $36.78*         INSIDE ×3           1.818x      2.0072x     UNRESOLVED BY CENSORING

      * = the median cell is an INTERRUPT-BOUND (a lower bound, tight to a measured sub-1 % share of its cost)
```
⇒ **15 of 15 medians inside their registered bands. §4(1)'s falsification count: 0 of 15.**
⚠️ **Inside is not "near the point".** Several medians sit far from their registered points (LZW plain $8.97 against a point of
$13.95; Paxos salt-diet at the cap). The bands are 99 % sampling intervals under the registered σ (§3), and they held.

## 2 · THE PREMIUM — FIVE READINGS, THREE KINDS, AND THEY MUST NOT BE POOLED

- **RESOLVED — FreeList, 2.385×.** One of the two problems §2 registered as resolvable, and it resolves. **This is a cost
  premium:** the salt-diet arm cost about 2.4 times the plain arm on this task. It says nothing about correctness.
- **UNRESOLVED BY CENSORING — Paxos, 1.818×.** The other problem registered as resolvable. At its plain median, resolving
  needed a salt-diet median of $40.61, above the $37.21 cap. The bound was posted before the last cell landed.
  **It is a fact about the instrument, not a smaller effect**, and it is counted as censored wherever it is counted.
- **UNRESOLVED AS REGISTERED — Crc32 1.078×, LRU 1.077×, LZW 1.940×.** §2 said before the fire that these three could
  not resolve their anchor effect at n = 3. **UNRESOLVED is not NULL.** LZW's reading is the nearest to the floor, and a
  floor is a boundary, not a gradient.
⛔ **The three kinds print the same word, UNRESOLVED, in a grid, and only one of them is about the method's effect size.**
How a matrix cell or the paper carries that distinction is on the 2026-09-17 agenda.

## 3 · THE PLACEBO — UNRESOLVED ON ALL FIVE, AS §3 SAID IT MUST BE

```
  placebo median / plain median    Crc32 1.051x · FreeList 0.812x · LRU 0.794x · LZW 1.551x · Paxos 0.835x
```
§3 registered the placebo point at parity (1.00) and said this stage **can only refute it, never confirm it**. None of the
five readings clears the floor on either side, so none refutes it. **Four of five sit below parity and one above.** Per §3
and `RULING-placebo-acceptance`, **no reading is taken from that pattern**: accepting a null is the trap the ruling forbids.

## 4 · §3a — THE TWO PREDICTED CAP-OUTS

```
  FreeList salt-diet   predicted CAP-OUT in >= 2 of 3   ⇒ FALSIFIED (two of three landed at or below the cap)
  Paxos    salt-diet   predicted CAP-OUT in >= 2 of 3   ⇒ NEAR-CAP (one cap-out; median $36.78* in [$35.35, $37.21))
```
⇒ **One sharp prediction is falsified and the other lands in the band §3b registered as neither a hit nor a miss.**
⚠️ The §3b column was meant to separate pacing from genuine cost. Measured over 45 cells, **the countdown was actually seen
in 12** (placebo 4 · plain 2 · salt-diet 6; `budget-read-column/census-45.out`), because the subjects' opening reads mostly
ran before the watcher's first write. The column does not decide §3b's outcome; it rides beside it.

## 5 · STAGE-WIDE LIMITATIONS, DECLARED WITH THEIR NUMBERS

1. **CONCURRENCY — THE REGISTERED PREFLIGHT WAS UNDER-ENFORCED.** §6.3 item 3 registered *"no cell of any wave running"*;
   the fire script checked HC1 cells only until the last cell. Over all 45 cells (`concurrency/census-45.out`): **23 shared
   the box with agy cells, 19 were not quiet at fire**, and the shared share of window time was plain 43.5 % · placebo
   41.4 % · salt-diet 37.4 %. Load moves wall time directly and cost only through the subject's behaviour, which is
   UNMEASURED. **The treatment arm is the least exposed, so any load effect leans toward shrinking premiums.** No cell is
   voided. The last cell fired through a guard enforcing the registered text.
2. **IN-CELL BUILD WAITS, ARM-CORRELATED IN THE CONSERVATIVE DIRECTION** (`lk-wait-census/census-45.out`): cells with at
   least one wait for their own build lock, plain 13 of 15 · placebo 10 of 15 · salt-diet 7 of 15. The fleet build wrapper
   appears in 0 of 45 transcripts. A wait adds cost only through extra turns (UNMEASURED), and it falls mostly on the
   control arms, which shrinks a premium.
3. **THE CAP CENSORS THE TREATMENT ARM** on the two problems §3a named (FreeList: one cap-out; Paxos: one cap-out and two
   landings within 1.3 % of the cap). **Every salt-diet median on those two problems is bounded above by the cap.**
4. **INTERRUPT BOUNDS.** Each is in a sub-agent turn and below 1 % of its cell (of T or of cost, as each file reports). The median cell is a bound in four
   arms (Crc32, FreeList and LRU placebo; Paxos salt-diet). A bound can only raise its cell, and no verdict in §1–§4 sits within
   1 % above any of those four medians: the nearest is Paxos §3a, 1.16 % below the cap against a measured 0.1075 % bound.
5. **ACCOUNT AND PINS.** These cells ran on a different subscription account from the matrix-#1 anchors, by the Captain's
   capacity ruling. **35 of the 45 cells carry fire and stage receipts, and all 35 assert the same client pin, export
   `9f650a3` and C1_USD $37.21.** The first ten cells predate those receipts, and their pins are not re-read in this file.
6. **DOLLARS ARE MODELLED** at the meter's list rates; they are not an invoice. Quote medians and ratios, not single cells.

## 6 · WHAT THIS DOES NOT SAY

- **It does not say the salt method helps, or that it does not.** Stage 1 measured cost under a pre-registered replication.
  It did not score correctness, and three of its five premiums could not resolve by design.
- **It does not add a condition to the complete pilot matrix.** HC stage 1 replicates the already-DONE
  `claude-opus-5 × greenfield × none` row, plus a placebo arm that is not on the grid (census §J3). The census re-cut in
  this commit records that the count does not move.
- **It does not choose stage 2.** Desk HG's designs return to the 2026-09-17 sitting, together with the question the
  replication raised: **the cap bound the arm that runs longest, and every proposed stage-2 cell class runs longer.**
