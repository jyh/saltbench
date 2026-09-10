# AMENDMENT — THE STATEMENT ARM ON THE FIVE-PROBLEM PILOT
## Dated 2026-09-09. ⛔ **THE COMMIT THAT FREEZES THIS FILE IS THE AUTHORISATION, AND IT LANDS BEFORE ANY CARD IS EDITED.**
Ordered by the Captain at 15:38: *"We should prioritize the statement-arm runs on the pilot over
everything. Move the 14-problem expansion until after. We don't need to cancel any cells, but let's
pivot."* ⇒ **Nothing running is cancelled.**

---

## §1 · WHAT THIS AMENDS, AND THE RECONCILIATION IT OWES

`PREREGISTRATION-matrix-opus-1-2026-09-08.md` §1 registered **5 problems × 4 arms × n = 3 = 60 cells**.
**36 were buildable.** §16 of that same freeze recorded why, before the pilot fired: **24 of 24
`--statement` builds REFUSED**, because four cards carry no `## Statement` section.
⛔⛔ **THE DESIGN WAS NEVER RE-REGISTERED TO MATCH WHAT FIRED, AND THAT IS THE DEFECT THIS AMENDMENT
EXISTS TO CLOSE.** The result reported `k = 1` honestly throughout; **no file reconciled "60" with "36"**,
and the Captain was the first to ask. ⇒ 🔑 ***A FREEZE THAT SURVIVES ITS OWN UNBUILDABLE HALF STOPS
DESCRIBING THE RUN, AND EVERY LATER READER INHERITS THE LARGER NUMBER.***

## §2 · WHAT FIRES

```
  4 problems × 2 statement arms × n = 3  =  24 cells
  problems   Crc32 · FreeList · LRU · Paxos          (LZW already has its 6)
  arms       plain+STATEMENT  ·  salt-diet+STATEMENT   ⇒ the Captain's (d) and (e)
  model      claude-opus-5, greenfield, as the pilot
  ⇒ with LZW's existing 6, the GOLD PAIR reaches k = 5 — the first time it can carry a verdict at all
```
**Prerequisite, and it is content, not harness:** four `## Statement` sections authored for Crc32,
FreeList, LRU and Paxos. **Author: systems** (default-if-silent, helm 15:38). **The Captain reads all
four before a cell fires.**

## §3 · ⛔⛔ THE CAP DECIDES THIS RUN, AND IT IS REGISTERED HERE BECAUSE IT CANNOT BE REGISTERED AFTER

The pilot's per-cell cost cap is **`C1_USD = 37.21`**. Measured against it, from the pilot's own tracked
medians (`RESULT-n3-topup-2026-09-09.md`, reading A):
```
  Crc32     diet median $ 7.21   max $ 7.63
  LRU       diet median $11.21   max $14.63
  LZW       diet median $19.18   max $31.70
  FreeList  diet median $37.60   max $37.95   ⛔ ABOVE THE CAP
  Paxos     diet median $37.65   max $37.93   ⛔ ABOVE THE CAP
```
⇒ ***TWO OF THE FOUR DIET-STATEMENT CONDITIONS ARE EXPECTED TO CAP.*** Their bare counterparts already
did: **all three CAP-COST cells in the pilot were salt-arm, none were plain.** A capped cell is
**excluded from the LANDED population** the correctness pass scores, so at the current cap **the gold
pair would reach k = 5 on cost and fewer than 5 on correctness.**
⚖️ **THE DECISION IS THE CAPTAIN'S OR THE HELM'S AND I WILL NOT TAKE IT SILENTLY. Both branches are
registered here in advance:**
* **CAP UNCHANGED at $37.21** — comparability with the pilot's bare arms is preserved exactly. **Register
  now that FreeList and Paxos diet+stmt are EXPECTED to cap**, and report them as `CAP-COST`, never as
  failures, per the correctness pre-spec's class rule.
* **CAP RAISED** — more cells land, and **the statement arm is then measured under a different budget
  than the bare arm it is compared against.** ⛔ If this branch is taken, the raise is named in this file
  with its value, and **no cost comparison between the bare and statement arms may be reported** without
  it stated in the same sentence.
⇒ **DEFAULT-IF-SILENT: CAP UNCHANGED**, because it preserves the comparison the pilot was built to make,
and because an expected outcome registered in advance is a result rather than a surprise.

## §4 · ⛔⛔ SUPERSEDED BY ADDENDUM 1 — THE SECTIONS ARE **EXTRACTED**, NOT AUTHORED

> ⛔ **THIS SECTION WAS WRONG AND WAS WRONG FOR THIRTY SECONDS.** It froze at 15:41:15 registering an
> AUTHORING hazard; `systems` posted the object at 15:41:45. **A `## Statement` is produced by
> `harness/systems-v3/extract_statement_v3.py` from `G/withheld/reference/solution.rs`, verbatim and
> closed over itself and the interface.** LZW's own card declares this at line 141 and carries its
> re-derive command; systems ran it and **reproduced LZW byte-identical at 4,405 B**. **See ADDENDUM 1
> at the end of this file. The four constraints below are VOID; §3 (the cap) and §5 (the reading) stand
> unchanged.**

### (the superseded text, kept because a struck clause must remain readable)

**The four sections will be authored by a party who knows the pilot's results** — the cost premium on
every problem, and now the correctness verdicts too. **A `## Statement` section is content the treatment
arm consumes.** ⇒ 🔑 ***WHOEVER WRITES THEM IS CHOOSING WHAT (d) AND (e) MEASURE, AFTER SEEING WHAT THE
BARE ARMS DID.***
**Registered constraints, before the first word is written:**
1. **AUTHORED FROM THE CARD'S EXISTING REQUIREMENTS ONLY** — not from any result, ranking or premium.
2. **COMPARABLE IN KIND AND SIZE TO LZW's**, the one precedent, which was authored before any result
   existed. ⛔ LZW's card is **14,575 B** against **4,087–7,341 B** for the other four: **a section that
   closes that gap is a much larger content change than "adding the missing arm"**, and this file
   records each card's byte size before and after so the change is visible rather than inferred.
3. **THE CAPTAIN READS ALL FOUR BEFORE ANY CELL FIRES** (helm 15:38), and that read is the control.
4. **NO SECTION IS REVISED AFTER A CELL USING IT HAS FIRED.**

## §5 · THE READING, FIXED NOW

**Primary:** the gold pair — per-problem median cost of `salt-diet+statement` over `plain+statement`,
then the **cross-problem sign test at k = 5**, the same statistic and the same floor as the bare-arm
reading. **p = 0.0312 is reachable for the first time.**
⛔ **THE RESOLVABLE FLOOR STILL BINDS:** `2.0072×` at n = 3, from the registered σ. **A sign is the
finding; no ratio or range is reported as the result** — unchanged from the standing rule.
⛔ **CAPPED CELLS DO NOT SILENTLY SHRINK k.** If a condition lands fewer than 3, the reading is reported
at the n actually achieved **and the shortfall is named in the same table**, per §14 of the placebo
ruling (the floor is per-problem and n is not uniform).
📌 **Correctness on these 24 is scored by the same frozen pre-spec** (`437ea70`) and is **post hoc for
the pilot's bare arms and PRE-registered for these** — the two must not be pooled into one column
without that distinction printed.

## §6 · COST AND ACCOUNT

```
  ESTIMATE  $418  — from each problem's OWN bare medians at n=3 (Crc32 40.26 · LRU 62.82 ·
                    FreeList 151.86 · Paxos 163.29). An ESTIMATE, not a measurement.
  CALIBRATION LZW is the only problem with both: stmt/bare = 0.73× plain, 0.97× diet
                    ⇒ the estimate is likely HIGH.
  BOX TIME  UNMEASURED and not guessed. The pilot ran 4-wide.
  ACCOUNT   the cells authenticate from a credential file on the run box, which no roster edit touches.
            NAMED, NOT CHOSEN: this needs a v3 run account with headroom for ~$418 plus cap margin.
            The Captain has ruled relight-to-jasonh; one account was reported at 83%.
```

## §7 · WHAT WOULD INVALIDATE THIS RUN

Editing a card before this file is committed; authoring a section from a result rather than from the
card; revising a section after a cell using it has fired; raising the cap without naming it here;
pooling these cells' correctness with the pilot's post-hoc column without the distinction printed; or
reporting a ratio as the finding.


---

# ADDENDUM 1 — 2026-09-09 15:4x. **THE PROVENANCE IS A TOOL, NOT AN AUTHOR.**

## A1.1 · WHAT REPLACES §4
```
  tool     harness/systems-v3/extract_statement_v3.py   (its closure check repaired this morning)
  source   G/withheld/reference/solution.rs             — every line VERBATIM from the reference
  closure  CLOSED over itself and the interface; the reference's lemmas and its private contracted
           helpers deliberately excluded
  driven   Crc32 1,166 B / 10 items · LRU 3,082 B / 11 · FreeList 13,849 B / 47 · LZW 4,405 B / 24
           LZW is the LANDED model and it reproduces BYTE-IDENTICAL
  Paxos    REFUSES — one extractor clause required; ruled by default: a named proof fn contributes
           its CONTRACT, body elided
```
⇒ 🔑 ***THE FOUR SECTIONS ARE DERIVED OBJECTS, NOT CHOICES.*** ⛔ **systems' argument is the load-bearing
one and I am ratifying it, not merely accepting it:** *if four sections were hand-written prose, the
treatment would be "what systems wrote about task X" on four problems and "the formal spec, verbatim" on
LZW — **and the statement arm would stop being comparable across the five problems.*** That is a defect
in the ARM, not in the writing, and no amount of care in the prose would fix it.
⚖️ **THE READ GATE STANDS, BY HIS OWN WORD AT 15:44** — *"Yes, I will try to read. If I have not by
21:00, go ahead and fire on the default."* ⛔ **An earlier draft of this addendum said the gate collapses
because a derived object is checkable rather than approvable. That reasoning is sound and IT IS NOT HIS
RULING**, and he made the ruling sixty seconds after the reasoning was written.
⇒ **FIRING CONDITION, REGISTERED: his read of the four extracted sections, OR 21:00 local, WHICHEVER IS
FIRST.** ⇒ 🔑 ***A GATE THAT AN ARGUMENT DISSOLVES IS STILL THE GATEKEEPER'S TO OPEN*** — the argument
tells him the read is cheap, it does not tell him he has read.
📌 **What the derivation adds is not permission but CHECKABILITY:** any party can regenerate a section
from the reference and diff it, so his read is a spot-check rather than an approval, and the 21:00
default is safe precisely because of that.

## A1.2 · ⛔ WHAT MUST BE REGISTERED **BECAUSE** IT IS AN EXTRACTION
1. **THE STATEMENT ARM IS HANDED A FORMAL SPECIFICATION DERIVED VERBATIM FROM THE WITHHELD REFERENCE
   SOLUTION.** That is the treatment, it is intended, LZW already did it, and it is written here so that
   **no later reader mistakes it for a fence leak.** ⇒ **The statement arm is a STRONGER treatment than
   the bare arm by construction, and the (d)/(e) comparison is WITHIN it, where both sides get it.**
2. **THE FOUR SECTION SHAS ARE THE PROVENANCE** and are recorded when systems commits them. **A section
   that does not reproduce from the tool is not admissible**, and that is checkable by anyone.
3. **THE PAXOS CLAUSE IS A RULE, NOT A SPECIAL CASE** — *a named proof fn contributes its CONTRACT, body
   elided* — and it applies to every task the extractor meets, not only to Paxos. ⛔ **If it were a
   Paxos-only exception, Paxos's statement would be a different kind of object from the other four and
   §A1.1's comparability argument would break on the one problem it was invoked for.**
4. **CARD SIZES BEFORE AND AFTER ARE STILL RECORDED**, unchanged from §4 — not as an authoring control
   now, but because **FreeList's section is 13,849 B against Crc32's 1,166 B**, and a treatment that
   varies twelve-fold in size across problems is a fact the reading must carry.

## A1.3 · ACCOUNT — NAMED
```
  NEEDS      ~$418 estimated + cap margin; two conditions expected to cap at $37.21 (§3)
  NAMED      jasonh — RULED BY THE CAPTAIN, 15:44 verbatim: "Yes, I believe we will need to use jasonh"
             weekly reset 15:00 today, so it is the freshest pool
  READING    12:47  5h 4% · weekly 53% · fable 44%
             ⛔ RE-MEASURE AT THE CREDENTIAL IMMEDIATELY BEFORE LAUNCH and record the launch-time
             reading HERE — a quota figure is a BILL, not a budget, and this one is four hours stale
  CO-TENANT  the helm relights to jasonh tonight; its draw is small but the account is SHARED during
             the run ⇒ an ACCOUNT-LEVEL delta attributes nothing to these cells. Per-cell prices come
             from each cell's own METER under SS23(e), which is unaffected.
  NOT USED   the Studio's shared run account at 83% used; the third pool is the no-regret zone
             (~10% left) and $418 is not cheap
```
⚠️ **THE ACCOUNT BOUNDARY, AND WHY IT DOES NOT TOUCH THE PRIMARY READING:** matrix #1's bare arms ran on
a different run account. **The gold pair (d) vs (e) is measured WITHIN the statement arm, both sides on
the same account**, so the primary reading is unaffected. ⛔ **Any bare-vs-statement cost comparison
crosses the boundary and must say so**, per the disclosure already at `RESULT-n3-topup-2026-09-09.md`.
📌 **The cells authenticate from a credential file on the run box that no roster edit touches** — naming
the account here is a registration, and the config dir must be verified at the object before the fire.

---

# ADDENDUM 2 — 2026-09-09 16:1x. **18 OF 24, AND THE GOLD PAIR CANNOT REACH A VERDICT.**

## A2.1 · ⛔⛔ THE ARITHMETIC, STATED TONIGHT AND NOT IN THE MORNING
```
  one-sided sign test, k of k, p = 0.5^k
    k = 3   best case 3 of 3   p = 0.1250   NO VERDICT at any outcome
    k = 4   best case 4 of 4   p = 0.0625   NO VERDICT at any outcome
    k = 5   best case 5 of 5   p = 0.0312   the ONLY k that can reach .05
```
⇒ 🔑 ***k = 5 IS THE MINIMUM, PAXOS IS ONE OF THE FIVE, AND PAXOS CANNOT CARRY AN ARM-NEUTRAL STATEMENT.
THEREFORE THE GOLD PAIR CANNOT REACH A VERDICT IN THIS DESIGN.*** Not "we fell short of five" — **at
k = 4 the best attainable outcome is p = 0.0625 and it is still no verdict.**
⛔ **This is registered BEFORE the cells land, so the morning cannot read it as a disappointment.** §16 of
the original freeze said the same thing at k = 1; **this is that finding one level up, and it survived
adding three problems.**

## A2.2 · WHY PAXOS IS A RESULT AND NOT A DEFECT
The harness's **neutrality gate** refuses a cell whose rendered `REQUIREMENTS.md` carries the treatment's
vocabulary, **because that file is read by the PLAIN arm too**. Measured on the extractions:
```
  ## Statement section     proof fn   "specification"     build
  LZW · Crc32 · LRU            0            0             ✅  (LZW is the landed control: also 0/0)
  FreeList                     0            1             ⛔ -> comment-only elision fixes it
  Paxos                        3            0             ⛔ IRREDUCIBLE
```
⇒ ***A PAXOS STATEMENT NAMES `proof fn` BECAUSE PAXOS'S SPECIFICATION **IS** PROOF OBLIGATIONS.*** The
vocabulary is not decoration that can be elided; it is the content. **A plain+statement Paxos cell would
be a control instructed to write proofs, which is not a control.**
⇒ **REGISTERED AS A FINDING: for a proof-obligation task, an arm-neutral formal statement cannot exist.**
That is a property of the benchmark's design, it is reportable, and **it is the reason the gold pair
stops at four problems rather than an accident of scheduling.**
📌 **The elision rule is admissible precisely because it is FREE:** measured, it changes **FreeList
alone** — LZW, Crc32, LRU and Paxos are byte-identical under it — so **LZW's already-landed statement is
not disturbed and comparability across problems is preserved.** ⛔ Had it changed LZW, it would have been
refused: a rule that rewrites the one landed precedent breaks the arm it is trying to complete.

## A2.3 · WHAT FIRES, AND WHAT IS REPORTED
```
  FIRE   Crc32 6 · LRU 6 · FreeList 6   = 18 cells      (FreeList on the re-cut export)
  NOT    Paxos 6                        = 6 cells       REPORTED AS A RESULT, never as a shortfall
  gold pair reaches k = 4 (Crc32 · LRU · FreeList · LZW) ⇒ p = 0.0625 floor, NO VERDICT
```
⛔ **Everything else in this amendment stands**: the cap at `C1_USD=37.21` with FreeList's diet cells
expected to cap, the account, and the reading. ⚠️ **FreeList is both the cap-risk AND the elision case** —
the one problem where two registered hazards meet, and its six cells are the ones to watch.

---

# A3 · THE SELECTION EFFECT AND THE DIFFICULTY CONFOUND, REGISTERED BEFORE FreeList'S CELLS LAND

Appended 2026-09-09 evening by `paper`, on the 41st helm head's order (`gate/paper`, the ORDER half:
*"the arm looks mild because its population is the mild end of the five. Say that BEFORE FreeList lands,
not after"*), and on systems' withdrawal of 17:49 and the maestro's rulings of 17:50 and 17:52.

⛔ **THIS SECTION IS WRITTEN WHILE FreeList's SIX CELLS ARE STILL IN FLIGHT.** That is its whole value.
Every claim below is available to either outcome, so neither outcome can be reported as having produced
it. Written afterwards it would be outcome-dependent reporting and worth nothing.

## A3.1 · THE SELECTION EFFECT: THE ARM'S LANDED POPULATION IS THE MILD END OF THE FIVE

The pilot's three landed gold problems are **LZW, Crc32 and LRU**. Those are **exactly the three whose
bare-arm premiums fall below the design's own resolvable floor of `2.0072x`** — Crc32 `1.1610`, LZW
`1.3749`, LRU `1.2826` under reading A and `1.1521` under reading B.
Paxos is excluded, as a registered result and not as a shortfall (A2.2: for a proof-obligation task an
arm-neutral formal statement cannot exist). **FreeList, the one problem still in flight, carries the
LARGEST bare premium of all five** — `2.8070` under reading A, `2.8879` under reading B.
*Bare premiums read from `RESULT-n3-topup-2026-09-09.md` section 3, not retyped from a post.*

⇒ 🔑 ***THE ARM LOOKS MILD BECAUSE ITS POPULATION IS THE MILD END OF THE FIVE, BY CONSTRUCTION AND NOT BY
CHANCE.*** Whatever mildness its result shows is predicted by the selection alone, before any account of
the treatment is reached for.

## A3.2 · THREE CONCORDANT ORDERINGS — AND NO p-VALUE ON ANY OF THEM

Three quantities rank the five problems in the same order, and that order tracks problem size:
**statement bytes** (systems' own measurement at `311b208`), **bare-arm premium**
(`RESULT-n3-topup-2026-09-09.md` section 3), and **statement-arm premium** (bench, 17:31 and 17:52 —
⛔ **not yet at a tracked path; see A3.4**).

⛔⛔ **NO p-VALUE IS ATTACHED TO ANY OF THE THREE, AND NONE MAY BE COMPUTED FROM THEM LATER.**
**All three orderings were found by inspection, after the data, while hunting an explanation for a low
cell.** A `p = 0.0083` computed on the first of them was **struck by the maestro at 17:52** on exactly
this ground and is **not revived here**.
⇒ 🔑 ***A p-VALUE ON A PATTERN DISCOVERED BY INSPECTION IS NOT A p-VALUE: IT PRICES A HYPOTHESIS THAT DID
NOT EXIST BEFORE THE DATA.*** The concordance is recorded as a **structural warning**, which is what it
is, and never as a result.

⛔⛔ **AND THE CONCORDANCE IS NOT EVEN STABLE ACROSS THE TWO READINGS OF ITS OWN DATA — MEASURED HERE, NOT
REPORTED TO ME.** Ordered by statement size (Crc32 · LRU · LZW · Paxos · FreeList), the bare premiums run

```
  reading A   1.1610  1.2826  1.3749  2.4306  2.8070    strictly increasing with size
  reading B   1.1610  1.1521  1.3749  2.2437  2.8879    ⛔ INVERTED at Crc32 / LRU
```

**The perfect rank match holds under reading A and BREAKS under reading B**, where Crc32 `1.1610` sits
above LRU `1.1521`. The two problems that swap are the two whose premiums are closest together and both
far below the floor, so the inversion is exactly what sampling noise at `n=3` looks like.
⇒ **This rescues nothing** — the qualitative warning of A3.1 and A3.3 stands untouched, and the selection
effect does not depend on any ordering being perfect. **What it kills is any temptation to price the
concordance.** A pattern that reverses when three borrowed cells leave the declared set is not a pattern a
number may be attached to, and **the strongest form of the ordering claim that survives both readings is
that the premium is near 1 on the smallest problems and rises with size.**
📌 Recorded because the concordance reached the bus as *"all five, 1-2-3-4-5"* and as *"three concordant
orderings"*, both taken over reading A alone. **A campaign that reports two readings has to check a
cross-reading claim against both**, and the discipline that caught this is the same one that produced the
two readings in the first place.

## A3.3 · THE CONSEQUENCE: FreeList CANNOT SETTLE IT, WHICHEVER WAY IT LANDS

Statement size and bare premium are **both downstream of the same latent variable — how hard the problem
is.** A harder problem takes a bigger formal statement *and* shows a bigger method premium.
⇒ **The dose account and the selection account make the SAME prediction for every outcome FreeList can
produce.** If FreeList lands high, that is what a dose account predicts and equally what a selection
account predicts. **A sixth problem that ranks with the other five adds a data point and no information.**

⇒ ⛔ ***THE CONFOUND IS STRUCTURAL, NOT ACCIDENTAL, AND NO REORDERING OF THIS POPULATION ESCAPES IT.***
**What would discriminate is a problem where the orderings DISAGREE** — a large statement on a low-premium
problem, or a terse statement on a high one. **There is no such problem among the five.** That is a
sampling requirement for the 14-problem expansion (registered by the maestro at 17:50), not something
tonight can supply.

## A3.4 · WHAT IS DEFENSIBLE WHATEVER FreeList DOES

* **The gold pair is 2 of 3 above 1, `p = 0.5000`** — not a result, and it is the registered null.
  ⛔ *"2 of 3 above 1" READS AS SUPPORT AND IS A COIN FLIP*; the `p` and the floor travel in the same breath.
* **The magnitudes are unresolved**: all three landed statement-arm premiums sit below the `2.0072x` floor.
* **The bare arms' bound**: no premium in this campaign exceeds **`2.8879x`** under either reading.
* ⛔ **THE STATEMENT-ARM NUMBERS ARE NOT YET CITABLE.** No statement-arm RESULT file is tracked at any
  path in this repository — measured this evening, `git ls-files` over the tree returns an amendment, a
  fetch script and two unrelated `.lean` exhibits, and no result. **Until bench lands that file, those
  three premiums may not enter the paper**, whatever they say. A result on the bus is not citable.

⛔⛔ **AND THE LIMIT ON THE BOUND ITSELF, WHICH IS THE POINT OF THIS SECTION:**
***THE BOUND IS A PROPERTY OF THIS POPULATION, NOT A PROMISE ABOUT LARGER ONES.*** The premium sits at or
below 1 on the smallest problem and grows to nearly 3x on the largest. **A population with larger problems
than these five is not covered by it**, and no sentence anywhere may present the bound as though it were.

## A3.5 · A NUMBER CORRECTION, FLAGGED RATHER THAN ABSORBED

The formulation **"the premium never exceeded `2.81x`" is READING-A ONLY.** Reading B's FreeList premium
is **`2.8879x`**. Any bound quoted as holding *"under both readings"* is **`2.8879x`**, and **"under
`3x`"** is the only short form true under both.
📌 Recorded here rather than silently corrected downstream, because the `2.81x` form has now appeared in a
gate and in a relayed ruling, and **a bound that is quoted one reading short is a bound that fails exactly
where the population is hardest** — on FreeList, the problem this pilot is still waiting on.

---

# A4 · HOW THE CAP PREDICTION IS SCORED — REGISTERED WHILE `sf05free` AND `sf06free` ARE STILL RUNNING

Appended 2026-09-09 19:0x by `paper`. ⛔⛔ **THIS SECTION IS WRITTEN WITH TWO OF FreeList's SIX CELLS
STILL IN FLIGHT, AND THAT IS ITS ONLY VALUE.** §3 registered a prediction; nothing in this file says
how the prediction is READ if it fails. **Written after the cells land, every word below would be
outcome-dependent reporting.** Same shape as `A3`, same reason.

## A4.1 · THE PREDICTION, AS IT STANDS IN §3

> *"Register now that FreeList and Paxos diet+stmt are EXPECTED to cap"* — on the ground that their
> bare counterparts' medians already sat above `C1_USD = 37.21` (FreeList diet-bare median **$37.60**,
> max $37.95). `A2.3` restated it unchanged. **Paxos never fires** (`A2.2`), so **FreeList is the only
> problem on which this prediction can be scored at all.**

## A4.2 · ⚖️ IT IS SCORED AS IT STANDS, IN EITHER DIRECTION, AND BOTH DIRECTIONS ARE WRITTEN HERE

* **IF THE CONDITION CAPS** — the capped cells are reported as `CAP-COST` and never as failures, per
  §3 and the correctness pre-spec's class rule, and the condition is read at the `n` it reached with
  the shortfall named in the table rather than in a footnote. The prediction is recorded as holding.
* **IF IT DOES NOT CAP** — **the prediction FAILED and is recorded as a failure, with its direction**,
  in the same paragraph of the paper that already records the estimator's five over-prices and its
  one under-price. ⛔ **A registered prediction that fails is a result of this instrument, not an
  embarrassment to be dropped**, and this campaign has recorded several.

## A4.3 · ⛔⛔ THE COMPARISON A FAILURE INVITES IS NOT THE REGISTERED READING

If FreeList's diet+statement cells land under the cap while its **diet-bare** median sat at $37.60,
the arithmetic invites the sentence *"the statement made the treatment's dearest condition cheaper."*
⛔ **THAT IS A BARE-vs-STATEMENT COMPARISON. THE REGISTERED READING OF THIS ARM IS (d) vs (e) — the
two STATEMENT conditions on the same problem** (§5). The two are different comparisons over different
populations and they are not pooled.
**What may be said of it, and it is deliberately narrow:**
1. It is **one problem at `n = 3`**, so it is an OBSERVATION and not a direction, and the resolvable
   floor of `2.0072x` at `n = 3` applies to it exactly as it applies to every other premium here.
2. It is admissible **only because the cap was NOT raised** (§3, first branch), so both sides were
   measured under the same budget. ⛔ **Had the cap been raised this comparison would be barred
   outright**, and that condition travels with any quotation of it.
3. The two sides differ in **more than the statement**: the diet-bare cells are matrix cells and the
   diet+statement cells are amendment cells, fired later, and `A3.1`'s selection effect and `A3.2`'s
   confound both bind here. **Nothing in this design licenses reading a capability or a mechanism
   from it.**

## A4.4 · WHY THIS IS REGISTERED RATHER THAN LEFT TO THE WRITE-UP

The Captain's stated end use for the cost result is a funding argument. A sentence of the form *"the
specification made the expensive arm cheaper"* is the single most quotable thing this campaign could
emit, **it would be true of one problem at `n = 3`, and it would be read as a mechanism.** ⇒ 🔑
***FORBIDDING A CLAIM IS ONLY HALF A GUARD; THE OTHER HALF IS SAYING WHAT MAY BE SAID INSTEAD*** —
the same rule §4 of the paper already applies to the bare arms' premiums, extended here to the one
cross-arm comparison this run can produce, **before anyone knows which way it falls.**
