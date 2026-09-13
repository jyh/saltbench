# PREDICTIONS — desk row HC, STAGE 1, REGISTERED BEFORE THE FIRST CELL
**bench (lead), 2026-09-13. This file is the artefact row HC's recommendation names first:
*"bench (lead) registers PREDICTIONS per arm per problem BEFORE the first fire."* It had not been
written. Nothing in HC stage 1 may fire until it exists, and it now does.**

⛔ **EVERY NUMBER BELOW IS DERIVED IN THIS FILE'S OWN GENERATOR FROM
`harness/systems-v3/RESULT-n3-topup-2026-09-09.md`, READING B (lines 87–98), AND NOTHING IS TYPED FROM
MEMORY OR FROM A MESSAGE.** The generator recomputes each problem's premium from the raw per-cell
dollars and checks it against the premium that file records — **5 of 5 reproduce to 4 decimal places**,
which is the positive control on my reading of the table and the reason the anchors may be trusted.

---

## §0 · ⛔⛔ TWO ARM NAMES IN ROW HC ARE NOT ARM NAMES, AND A FIRE THAT TOOK THEM LITERALLY WOULD REFUSE

Row HC names its stage-1 arms `plain-bare` · `salt-bare` · `placebo-bare`. **Measured at the object,
2026-09-13, before any of this was written:**
```
  cell_build.py   --arm  choices = plain | salt | salt-diet | placebo        <- no `-bare` is buildable
  the run box     275 ctl/arm files:  plain 144 · salt-diet 99 · placebo 31 · salt 1
                  containing the token `bare`:  ZERO
  the run box     275 ctl/card_extras files:    none 198 · statement 75
```
⇒ **`-bare` IS NOT AN ARM. It is row HC's shorthand for `card_extras = none`**, and the pairs it names
already exist as `(arm, card_extras)`. **REGISTERED RESOLUTION, so no head has to re-derive it:**
```
  plain-bare    ==  --arm plain      card_extras none
  salt-bare     ==  --arm salt-diet  card_extras none
  placebo-bare  ==  --arm placebo    card_extras none
```
⚠️ **`salt-bare` IS THE ONE THAT COULD HAVE GONE EITHER WAY, AND IT IS RESOLVED RATHER THAN ASSUMED.**
`salt` and `salt-diet` are **both buildable and are different arms.** The resolution is `salt-diet` on
two grounds, not one: the campaign's population is **99 `salt-diet` cells against 1 `salt`**, and row
HC's own 09/09 stamp maps its stage-1 arms onto `plain none` / `salt-diet none` / `placebo none` when
it measures them. ⛔ **If the council intends the `salt` arm instead, this file is wrong and the fire
must not proceed on it** — that is why the resolution is written down rather than carried in a head.

⇒ 🔑 ***AND THE MEASUREMENT THAT MATTERS MOST HERE IS THE ONE THAT CORRECTS MY OWN PREDECESSOR.*** Row
HC's 09/13 stamp offers as evidence: *"Swept every cells root on the run box for `ctl/arm` matching
`*bare*`: ZERO. `plain-bare`, `salt-bare` and `placebo-bare` have never been instantiated as arms."*
**That is TRUE AND VACUOUS: they were never instantiated because that is not what an arm is called.**
A NAMING fact was read as an EXISTENCE fact.
✅ **THE STAMP'S CONCLUSION SURVIVES UNTOUCHED**, because it never rested on that arm: HC stage 1 has
not been run under HC's own registered predictions, and that follows from the stamp's *first*
measurement — the predictions file did not exist — which carried its own positive control and was sound.
⛔ **I reproduced the bad sweep before I caught it**: my own first pass ran `find ~/cells-* -maxdepth 2`
and returned **0 `ctl/arm` files**, because the file lives at **depth 3**. The zero looked exactly like
the stamp's zero. **It was only the count printed beside it — 0 files examined — that gave it away.**
⇒ ***A SWEEP THAT REPORTS ITS VERDICT WITHOUT ITS DENOMINATOR CANNOT BE DISTINGUISHED FROM A SWEEP THAT
EXAMINED NOTHING, AND BOTH OF US WROTE THE FIRST KIND.***

---

## §1 · THE ANCHORS, DERIVED HERE, WITH THEIR REPRODUCTION CONTROL
```
  problem    n_pl n_sd   med_plain    med_salt-diet   premium    RECORDED   reproduces?
  Crc32       3    3    $  6.210      $  7.210      1.1610x   1.1610x   YES
  FreeList    4    3    $ 13.395      $ 37.600      2.8070x   2.8070x   YES
  LRU         4    3    $  8.740      $ 11.210      1.2826x   1.2826x   YES
  LZW         3    3    $ 13.950      $ 19.180      1.3749x   1.3749x   YES
  Paxos       4    3    $ 15.490      $ 37.650      2.4306x   2.4306x   YES
```
⚠️ **THESE ARE READING-B NUMBERS AND THEY MUST TRAVEL WITH THAT LABEL.**
`RULING-placebo-acceptance-2026-09-08.md` §6.2 lists a DIFFERENT set of premiums for the same problems
(LRU **1.4465×**, Paxos **2.6514×**, FreeList **2.7306×**). **Neither list is wrong; they are different
readings of different cell populations**, and this desk's own card is that *a number carries its
reading*. ✅ **CHECKED RATHER THAN ASSUMED: the conclusion below is READING-INVARIANT.** Under both
readings the SAME three problems fall below the resolvable floor and the SAME two clear it. **The
magnitudes move; the membership does not.**

---

## §2 · ⛔⛔ THE POWER STATEMENT, REGISTERED BEFORE THE FIRE AND NOT DISCOVERED IN THE WRITE-UP
Registered floor, `RULING-placebo-acceptance-2026-09-08.md` §6.2: `sd(ln cost) = 0.30458`, `k = 7.8489`,
`floor = exp(σ·√(2k/n))`. **At n = 3 the floor is 2.0072×.**
```
  Crc32      1.1610x   BELOW the floor — UNRESOLVABLE at n=3
  FreeList   2.8070x   ABOVE the floor — a same-size effect IS resolvable at n=3
  LRU        1.2826x   BELOW the floor — UNRESOLVABLE at n=3
  LZW        1.3749x   BELOW the floor — UNRESOLVABLE at n=3
  Paxos      2.4306x   ABOVE the floor — a same-size effect IS resolvable at n=3
```
⇒ 🔑 ***ON THREE OF FIVE PROBLEMS, HC STAGE 1 AT n = 3 CANNOT RESOLVE AN EFFECT THE SIZE OF THE ONE IT
IS LOOKING FOR.*** That is a property of the **DESIGN, not of the data**, so it is knowable tonight and
is registered tonight. **n required per problem, from the same ruling: 1.37× → 15 · 1.20× → 44 ·
1.10× → 161. The stage buys 3.**
⛔ **THIS IS NOT AN ARGUMENT AGAINST FIRING.** It is the sentence that stops `UNRESOLVED` being read as
`NULL` in three fifths of the write-up. **Every floor is evaluated at the n of the comparison it judges
— `min(n_arm1, n_arm2)` — never a campaign-wide n, and any table printing a floor prints its n beside
it** (row HC's own 09/09 rule, restated here because a rule in a desk cell is not homed for a scorer).

---

## §3 · THE PREDICTIONS, PER ARM PER PROBLEM
**Quantity: median cost in USD over the arm's n = 3 NEW cells.** Point prediction = the reading-B
median above; band = **[0.60×, 1.70×] of it**, registered as one multiplicative rule for all fifteen
rather than hand-tuned per cell, because a band chosen per problem after seeing that problem's spread
is fitted and its author cannot show otherwise.
```
  arm            problem    POINT       BAND (registered)        basis

  plain-bare     Crc32      $   6.21    [$  3.73 , $  10.56]     reading-B median
  salt-bare      Crc32      $   7.21    [$  4.33 , $  12.26]     reading-B median
  plain-bare     FreeList   $  13.39    [$  8.04 , $  22.77]     reading-B median
  salt-bare      FreeList   $  37.60    [$ 22.56 , $  63.92]     reading-B median
  plain-bare     LRU        $   8.74    [$  5.24 , $  14.86]     reading-B median
  salt-bare      LRU        $  11.21    [$  6.73 , $  19.06]     reading-B median
  plain-bare     LZW        $  13.95    [$  8.37 , $  23.71]     reading-B median
  salt-bare      LZW        $  19.18    [$ 11.51 , $  32.61]     reading-B median
  plain-bare     Paxos      $  15.49    [$  9.29 , $  26.33]     reading-B median
  salt-bare      Paxos      $  37.65    [$ 22.59 , $  64.00]     reading-B median
  placebo-bare   Crc32      $   6.21    [$  3.73 , $  10.56]     plain median x1.00 — see below
  placebo-bare   FreeList   $  13.39    [$  8.04 , $  22.77]     plain median x1.00 — see below
  placebo-bare   LRU        $   8.74    [$  5.24 , $  14.86]     plain median x1.00 — see below
  placebo-bare   LZW        $  13.95    [$  8.37 , $  23.71]     plain median x1.00 — see below
  placebo-bare   Paxos      $  15.49    [$  9.29 , $  26.33]     plain median x1.00 — see below
```
⛔⛔ **THE PLACEBO POINT IS A REGISTERED HYPOTHESIS AND IT IS THE ONLY ONE HERE THAT IS NOT AN ANCHOR.**
I predict the placebo arm lands **at the plain median (ratio 1.00)**, i.e. that an equal-length generic
process prompt buys **no** cost premium. **That is the campaign's own claim under test**, and I am
registering it as a point rather than a range so that it can be WRONG.
⚠️ **AND THE ACCEPTANCE TRAP IS RE-REGISTERED HERE BECAUSE IT BITES EXACTLY THIS PREDICTION:** the
reading that would confirm me — *"placebo landed near plain, so salt's premium is content"* — is an
**ACCEPTANCE OF A NULL**, and `RULING-placebo-acceptance` §6.3 forbids it. **A placebo premium below the
floor is `UNRESOLVED`. Nothing more.** ⇒ ***MY OWN PREDICTION CANNOT BE CONFIRMED BY THIS STAGE. IT CAN
ONLY BE REFUTED*** — and registering a prediction whose success is unreportable is the honest shape,
not a flaw in it.

## §3a · ⛔⛔ TWO OF THE FIFTEEN POINTS ARE ABOVE THE CAP THE CELLS WILL RUN UNDER, AND THAT CHANGES THEM FROM PREDICTIONS INTO PREDICTED CAP-OUTS
**Caught while writing this file, by checking the anchors against the instrument rather than against
each other.** `harness/systems-v3/cost_caps.tsv`, profile `pricing`: **`C1_USD = 37.21`** (phase 1;
`C2_USD = 18.60` is phase 2 and does not apply to HC stage 1).
```
  salt-bare  FreeList   point $37.60   >  C1_USD 37.21   by $0.39
  salt-bare  Paxos      point $37.65   >  C1_USD 37.21   by $0.44
```
⇒ 🔑 ***A POINT PREDICTION THE INSTRUMENT CANNOT REACH IS NOT A PREDICTION.*** Under row HC's own rule
(*"caps as floors; a cap-out is a result; no cap raised"*) those two arms enter their median **at the
cap by construction**, so the anchor value was unattainable before a single cell fired. It would have
sat inside its own band and never been scored wrong — **a point that cannot be hit and cannot be
falsified, which is the worst of both.**
✅ **REGISTERED INSTEAD, AND IT IS A SHARPER CLAIM THAN THE ONE IT REPLACES:**
```
  salt-bare  FreeList   PREDICTION: CAPS OUT at C1_USD 37.21, in at least 2 of its 3 cells
  salt-bare  Paxos      PREDICTION: CAPS OUT at C1_USD 37.21, in at least 2 of its 3 cells
```
**That is falsified by either arm landing at or below $37.21 in 2 of 3 cells**, which is a thing the
run can actually do. The other thirteen points stand as written.
⚠️ **AND THE LIMITATION IT EXPOSES, WHICH IS BIGGER THAN THE TWO CELLS: THE ANCHORS EXCEED THE CAP, SO
HC STAGE 1 IS NOT AN INSTRUMENT-IDENTICAL REPLICATION OF MATRIX #1.** Reading B records FreeList
`salt-diet` at **$37.95 · $37.60 · $35.41** and Paxos at **$37.93 · $37.65 · $23.52** — **four of those
six cells are above `C1_USD`.** Whatever regime they ran under, HC stage 1's cells will be censored
where they were not. ⛔ **So on those two problems a lower HC median is NOT evidence of a smaller
effect; it is the cap.** Registered here because it is knowable now and would be a very natural wrong
conclusion to draw from the table later.
📌 **I am not raising the cap and not asking for it to be raised.** Row HC forbids it, and censoring
that is declared in advance is a limitation; censoring discovered afterwards is a confound.

## §4 · THE FALSIFICATION RULE, REGISTERED BEFORE THE FIRE
1. **A prediction is WRONG when that arm's new n = 3 median falls OUTSIDE its band.** Counted per cell
   group, reported as a bare count out of 15. **No band is widened after a result. No cell is dropped
   for being surprising.**
2. **A CAP-OUT IS A RESULT, NOT A VOID** (row HC: *"Caps as floors; a cap-out is a result; no cap
   raised"*). A capped cell enters the median at its cap and the table says so. **Per §3a, two arms
   are PREDICTED to cap out; for those two the cap-out IS the prediction, not an excuse for missing
   one.**
3. ⛔ **THE REPLICATION HALF IS DELIBERATELY LOW-INFORMATION AND I AM SAYING SO BEFORE IT PAYS OFF.**
   Ten of these fifteen points are matrix #1's own medians, so predicting them is close to predicting
   that the same harness does the same thing twice. **Its value is not surprise — it is that the cells
   are NEW and fired under a rule fixed in advance**, which is the one thing matrix #1's cells can
   never retroactively become. ⭐ **The five placebo points are where this file can actually lose.**

## §5 · WHAT REGISTERING THIS DOES **NOT** DO
- **It does not fire anything.** HC stage 1 is 45 Opus cells and its ranking is the council's, not the
  lead's. Row HC's recommendation is **(b) then (a)**: register now at zero spend, queue the fire
  behind the Captain's eight-item assignment. **This file is (b). (a) is unchanged and still owed.**
- **It does not make matrix #1's cells substitutable.** They were not fired under these predictions,
  which is the whole point and is precisely what row HC's 09/09 stamp established.
- **It does not re-scope row HC.** Five problems, n = 3, three arms, exactly as ratified.
- ⚠️ **It does not make the stage well-powered.** §2 stands: three of five problems cannot resolve the
  effect they are looking for at n = 3, and no amount of pre-registration fixes an n.

## ⇒ 🔑 THE REASON THIS FILE EXISTS AT ALL
Row HC has been OPEN since 2026-09-07 with a deadline of **2026-09-10** that passed unremarked, and its
first step **costs zero model tokens**. It sat because it is **unblocked, unstarted and unranked against
a later assignment** — *not a block, so no block register carries it; not on the assignment, so no
priority list carries it either.* ⇒ ***THE ONE SHAPE AN IDLE SWEEP CANNOT SEE IS WORK THAT NOBODY IS
WAITING ON.*** The cheapest possible answer to that is to take its zero-cost first step the moment a
shift has room, which is what this is.
