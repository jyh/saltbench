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
