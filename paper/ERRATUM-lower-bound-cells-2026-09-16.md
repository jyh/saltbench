# ERRATUM — 19 of the 57 cell prices the paper prints are lower bounds, printed as prices

**Status: STANDING ERRATUM, beside the tex. The posted arXiv version is not revised by it, and nothing here
edits the paper.** Ruled by the author at council 2026-09-16 ("accept rec": a standing erratum in the repo
beside the tex, not an arXiv v2). Drafted by bench (SaltBench lead). **The text is read back to the author
before it merges**, because it is a public statement under his name.

Every number below is printed by one receipt, and none is typed from memory or from a message:
`harness/systems-v3/RECEIPT-ol-lower-bound-cells-2026-09-16.txt`, produced by
`harness/systems-v3/ol_lower_bound_margins.py` over `paper/saltbench-v1.tex` as tracked (blob `45f8d1979134`).

---

## 1 · What the paper prints

The appendix table of `paper/saltbench-v1.tex` prints **57 per-cell prices over 18 conditions**: the bare matrix
(33 prices under reading A, 30 under reading B, which drops the three underlined smoke cells) and the statement
arm (24 prices). The scoreboard's premiums, the reading's qualifiers, and the statement arm's k=4 reading are
all computed from those prices.

## 2 · What is wrong

**19 of the 57 printed prices come from cells whose own meter declares its total a LOWER BOUND, and the paper
prints them as prices, without a flag.** Each of the 19 contains at least one interrupted turn: a record with
no `stop_reason`. The client stops writing usage where the interrupt lands, so what is recorded of that turn
is known and what is missing from it is not. The instrument classifies every price by two methods (the
meter's declaration, and the null `stop_reason` records in the cell's `RECORDS.tsv`), which agree on 57 of 57.

```
  group           reading   printed prices   lower bounds   plain   diet
  bare matrix     A              33               13           10      3
  bare matrix     B              30               11            8      3
  statement arm   (A = B)        24                6            3      3
  all printed                    57               19           13      6
```
The receipt lists all 19 by problem, arm, price, harvest and the tex line that prints them.

## 3 · What is measured, and what is not

**The recorded cost of the interrupted records is 0.0583 % to 0.7579 % of each affected cell's cost**, over the
19 (bare matrix 0.0583 %–0.4958 %; statement arm 0.0639 %–0.7579 %).

⛔ **That figure is a SHARE, not a bound.** It says where the understatement lives and how large the recorded
part of those turns is. The unrecorded remainder is not measured by anything in the record, so this erratum
does not state a bound on it. §4 states instead how large that remainder would have to be to change anything
the paper concludes.

⚠️ **The figure ruled on 2026-09-16, "0.033 %–0.743 % of cost", is not used here.** It was computed over five
records, and all five ran after the tex was last changed (2026-09-10): two cells of a later wave on 2026-09-15
and three top-up cells that ended on 2026-09-11. It describes none of the 57 prices the paper prints. Over the
paper's own 19 cells the recorded share runs to 0.7579 %, above that figure's upper end.

## 4 · The direction, and how far each conclusion sits from it

A lower bound on a **plain** cell makes that arm look cheaper and **overstates** a diet-to-plain premium; one on
a **diet** cell understates it. Only a lower-bound cell that a median rests on can move a premium. By problem:

```
  bare matrix (both readings)   the median that rests on a lower-bound cell
    Crc32                       BOTH arms, so the direction of the bias is not determined
    FreeList · LRU · Paxos      plain only, so the premium is overstated by this cause
    LZW                         neither: both medians are prices
  statement arm                 no median rests on a lower-bound cell, in any of the four problems
```

**The margins.** For each conclusion, the receipt prints the smallest rise in the relevant arm's lower-bound
cells that would change it, as a relative uplift and as **k, the unrecorded remainder of each interrupted turn
as a multiple of what was recorded of it**:

```
  conclusion the paper states                           nearest problem        uplift     k
  bare sign, 5 of 5 above parity (both readings)        Crc32, plain side      +16.1 %    178x
  "Only FreeList and Paxos clear" the 2.0072x floor     Paxos, reading B       +11.8 %    121x
    (and no other problem crosses it upward)            Crc32, diet side      +101.4 %    844x
                                                        LRU, LZW               cannot be moved by their lower-bound cells
  statement arm: no premium clears the floor            LZW, diet side         +34.0 %     77x
  statement arm: 3 of 4 above parity (Crc32 below)      all four               none can be moved across parity by its lower-bound cells
```

⇒ **No sign, floor count or verdict the paper states changes unless an interrupted turn's unrecorded remainder
is at least 77 times what was recorded of it (121 times for the bare matrix).** The record does not measure the
remainder; 77 and 121 are the sizes it would need, not estimates of it.

## 5 · What does NOT change

- **No printed price or premium changes.** The prices are what the meters recorded; this erratum adds a flag,
  not a number.
- The bare sign test stays 5 of 5 at p = 0.0312 under both readings, subject to §4's margins.
- The statement arm's reading stays at no verdict (3 of 4 above parity, no premium clearing the floor), subject
  to §4's margins.

## 6 · Corrections to `harness/systems-v3/RESULT-n3-topup-2026-09-09.md` §A4, which this erratum supersedes

That section first disclosed the lower bounds on 2026-09-11. Four of its statements do not stand, and a banner
under its heading now points here:

1. **"Seventeen of the cells priced in this reading … plain 12 · salt-diet 5" does not reproduce.** Over the 39
   prices of that file's §A3 table, both methods find **15 (plain 11 · diet 4)**: the 13 bare-matrix cells of §2
   plus LZW's two statement cells, which that table includes. The file records no instrument for 17, and no
   population built from the record (the 39 priced cells, the 4 refused cells, the unstamped harvests) gives 17
   with that split.
2. **"0.03 %–1.4 % of the cell's total"** is replaced by §3's measured share, 0.0583 %–0.7579 %.
3. **"every per-problem magnitude was already below the registered resolvable floor"** is contradicted by that
   file's own §3, and by the paper: FreeList and Paxos clear the floor under both readings.
4. **"Any salt-diet-to-plain ratio taken from either column is therefore biased upward"** holds only where the
   plain median alone rests on a lower bound: FreeList, LRU and Paxos. Crc32's direction is not determined, and
   LZW's medians are prices (§4).

## 7 · Reproduce it

On the box holding the harvest archive, with `harvest_view_asof.sh` from `harness/systems-v3/`:
```
  bash harvest_view_asof.sh 20260910T040648Z <view-dir>        # cut at the commit that last changed the tex
  python3 ol_lower_bound_margins.py paper/saltbench-v1.tex <view-dir>
```
The view is cut at a date because the whole archive cannot be used: a later re-harvest can carry the same
price as a published cell (it does, at $11.19), and the instrument refuses a price that matches two harvests.
