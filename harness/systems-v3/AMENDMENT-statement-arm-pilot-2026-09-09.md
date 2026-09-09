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

## §4 · ⛔⛔ THE AUTHORING HAZARD, WHICH IS SHARPER THAN THE COST

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
