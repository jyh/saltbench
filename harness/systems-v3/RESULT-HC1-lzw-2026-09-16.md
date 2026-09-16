# RESULT — HC STAGE 1, **LZW COMPLETE AT n = 3**: three medians inside their bands, and the premium is **UNRESOLVED, AS REGISTERED** — at 1.940×, 3.4 % below the floor

## bench (SaltBench lead), 2026-09-16. Registered design: `PREDICTIONS-HC-stage1-2026-09-13.md` (PR #121, helm-signed as non-author).

> ## ⛔ READ THIS BEFORE ANY NUMBER BELOW
> §2 named LZW, before a single cell fired, as one of three problems of five whose effect size (anchor 1.3749×)
> sits **below** the n = 3 resolvable floor of 2.0072×. This problem cannot say at n = 3 whether the treatment
> helped. **The measured premium is 1.940×, 3.4 % below that floor. It is UNRESOLVED, and "nearly
> resolved" is the reading this file exists to refuse: a floor is a boundary, not a gradient.**

---

## 0 · PROVENANCE

```
  per-cell COST, T, and KIND (price / interrupt-bound)
        cell_meter.py per cell via the wave harvester, transcribed into the wave's fire order at each
        landing; the standing per-arm view is hc1_token_table.py, reading the same meter.
  registered BANDS, the FLOOR, and the ANCHOR
        PREDICTIONS-HC-stage1-2026-09-13.md, at its merged sha (LZW rows :68, :88, :136-:143).
```
⚠️ **Declared gap:** the fire order is an operational file in the run environment and is not tracked here (it
names run-environment and account detail). The authoritative source for every cost is the per-cell meter output.

## 1 · THE TRIPLE

```
  arm         cells                          MEDIAN   KIND     registered band        verdict
  plain       $9.69 · $7.53 · $8.97          $8.97    price    [$ 8.37 , $23.71]      INSIDE
  placebo     $7.47* · $13.91 · $15.32       $13.91   price    [$ 8.37 , $23.71]      INSIDE
  salt-diet   $12.56 · $17.40 · $23.76        $17.40   price    [$11.51 , $32.61]      INSIDE

      * = INTERRUPT-BOUND: one interrupted turn, understated by a measured sub-1 % share of cost
```
⇒ **12 of 15 cell groups resolved across the stage. 1 falsification (FreeList, §3a).**
⚠️ The plain median sits **$0.60 above its band's lower edge**, and all three plain cells are below the registered
point ($13.95, a reading-B median from matrix #1 on a different subscription account). Inside is inside; recorded,
not read.

## 2 · WHICH MEDIANS ARE PRICES, AND WHY — CHECKED, NOT ASSUMED

- **plain** — no bound. ⇒ **The median is a PRICE.**
- **placebo** — the bound `$7.47*` is the arm's **minimum**. Understatement can only raise it *toward* the median;
  to reach `$13.91` it would need **+86.2 %**, against a measured understatement of **0.1497 % of cost**.
  ⇒ **The median is a PRICE, protected by magnitude (576× margin).**
- **salt-diet** — no bound. ⇒ **The median is a PRICE.**

## 3 · THE PREMIUM — **UNRESOLVED**, AS §2 REGISTERED

```
  salt-diet median / plain median  =  $17.40 / $8.97  =  1.940x
  n = 3 resolvable floor                                 2.0072x    ⇒ BELOW (by 0.067x, 3.4 %) ⇒ UNRESOLVED
  matrix-#1 anchor                                       1.3749x
```

⇒ **This is the third problem of the stage to return UNRESOLVED exactly as registered**, after Crc32 (1.078×) and
LRU (1.077×). It is the one that came **nearest** the floor — and that proximity is precisely the kind of number a
pre-registration exists to stop a reader from rounding up. **To resolve, the salt-diet median would have had to be
$18.01 or more (2.0072 × $8.97 = $18.0046); it is $17.40.**
⚠️ **The measured premium is well ABOVE its anchor** (1.940× against 1.3749×). That is reported as measured, not as
agreement or disagreement: the anchor is a reading-B median on a different account, and §2's claim was only that
LZW cannot resolve at n = 3 — which it did not.

### 3.1 · The single-cell rows, which were never results
```
  n = 1 row   salt-diet / plain  =  $12.56 / $9.69  =  1.296x
  n = 2 row   salt-diet / plain  =  $17.40 / $7.53  =  2.311x
  n = 3 row   salt-diet / plain  =  $23.76 / $8.97  =  2.649x
  medians                                               1.940x
```
⚠️ **The n = 2 single-cell ratio crossed the floor (2.311×) and was recorded at its landing as NOT A RESULT.** A ratio
of single cells is a different quantity from a ratio of medians — the malformation that falsified this campaign's own
Crc32 row-factor prediction.

## 4 · THE PLACEBO READING — **UNRESOLVED**

```
  placebo median / plain median  =  $13.91 / $8.97  =  1.551x    against a registered 1.00
```
Deviation from parity 1.551×, below the floor. §3 permits the placebo prediction only to be **refuted**, never
confirmed — and a reading **above** parity is not "the placebo costs more", it is UNRESOLVED on the same terms.
**Four problems now return four placebo readings — Crc32 1.051×, FreeList 0.812×, LRU 0.794×, LZW 1.551× — two
above parity, two below, all UNRESOLVED.**

## 5 · INTERRUPTED RECORDS

One interrupt-bound in this triple (placebo n = 1), in a **sub-agent (`exec`) turn**, never the head — making that
registered observation **8 of 8** across two campaigns and both models. The plain and salt-diet arms have none.

## 6 · LIMITATIONS, DECLARED

1. **The final cell's quota bracket is VOID, declared at the fire:** a session-pool reset fell inside the reach of a
   cell whose siblings ran 27 and 45 minutes — and it did straddle: the cell landed one minute after the reset. No
   quota figure prices a single cell in any case.
2. **An exposure window on the salt-diet n = 2 cell, created by the lead and measured unused.** While that cell ran,
   the lead created a scratch directory holding a harness export (including this task) in the run environment's home,
   **outside the cell's render-time fence belt, for at most three minutes.** The subject did not touch it: zero
   occurrences in the cell's transcript and in both fence audit logs, each checked against a positive control. The
   cell is not voided; the window is declared so a reader need not take that on trust.
3. **These cells ran on a different subscription account from the matrix-#1 anchors**, by the Captain's capacity ruling.
4. **Absolute per-cell dollars are not a stable price.** Quote medians and ratios, not single cells.

## 7 · WHAT THIS DOES NOT SAY

It does not say the salt method helped on LZW, and it does not say it failed. **At n = 3 on this problem, neither
statement is available**, and that was registered before the first cell fired. It does not make 1.940× a near-miss —
a value below a floor is below it. It does not make matrix-#1's cells substitutable.
HC stage 1 has **one problem remaining**: Paxos, registered as able to resolve at n = 3, and carrying three
predicted cap-outs whose status FreeList's falsification has reopened.
