# RESULT — MATRIX #1 (opus). ⛔ DRAFTED BEFORE THE DECIDING CELL LANDED, WITH **BOTH** CONCLUSIONS WRITTEN.
# Every number names the file it came from. Nothing here is retyped from a message.

## ⛔⛔ READ THIS FIRST: WHY THIS FILE CONTAINS TWO HEADLINES

At the moment of writing, 4 of 5 problems have premiums and **all four are above 1**
(`score_matrix1.py` over `~/harvest-v3`). The fifth, `LRU`, waits on ONE cell — `d6b53ee4`, the
§18 replacement for `879326db`, which VOIDed in the fence-drift outage I caused. §21 records that
**I can estimate what that cell is worth before it runs**: LRU plain's median is $7.75 and its two
surviving diet cells are $11.19 and $11.21, so a third near them makes the premium ≈1.44 and turns
4-of-4 into 5-of-5 at p = 0.0312 — **the only significant outcome this design can produce.**

⇒ **SO BOTH CONCLUSIONS ARE WRITTEN HERE, NOW, BLIND TO WHICH ONE LANDS.** When the cell reports,
the surviving headline is marked KEPT and the other is marked STRUCK — **struck, not deleted**, so
the record shows both were composed with equal care before the number existed.
🔑 ***THE EFFORT YOU PUT INTO A CONCLUSION IS ITSELF A THUMB ON THE SCALE.*** Pre-registration
stops you choosing the test after the data; it does not stop you writing the expected conclusion
beautifully and the unexpected one in two grudging lines. This is the fix for that.

## THE SCOREBOARD — SIGN FIRST, BECAUSE THE SIGN IS THE REGISTERED READING (§2)

    problem     plain median      diet median       premium
    Crc32       $6.21             $7.21             1.1610x
    FreeList    $13.77            $37.60            2.7306x
    LZW         $13.95            $19.18            1.3749x
    Paxos       $14.20            $37.65            2.6514x
    LRU         $7.75             $11.21            1.4465x

    GOLD PAIR (LZW only)   plain+stmt $10.24 $11.39 $9.82   diet+stmt $22.53 $15.34 $18.54
                           premium 1.8105x · k=1 · p=0.5000 · NO VERDICT

## ✅ HEADLINE A — **KEPT**. `d6b53ee4` landed at $14.63; LRU's median is $11.21 and its premium 1.4465x.
**5 of 5 problems show a cost premium for the salt-diet arm, p = 0.0312.**
⛔ AND EVERY QUALIFIER BELOW IS PART OF THE HEADLINE, NOT A FOOTNOTE:
* the test is **ONE-SIDED** (§20) — it can confirm this hypothesis and **cannot significantly
  refute it**; five premiums *below* 1 would have returned p = 1.0000;
* **the magnitudes are UNRESOLVED** (G2): Crc32 1.1610 and LZW 1.3749 fall below the registered
  2.0072× floor, so **no ratio may be reported as the finding** — not "2.7×", not "1.5–3×";
* the result is **a sign across five problems at n=3**, and one problem's condition spans
  $13.02–$23.38 within a single arm (FreeList plain), a 1.80× spread that is noise;
* the gold pair — the comparison the campaign most wanted — is **k=1 and cannot reach .05**.

## ~~HEADLINE B~~ — **STRUCK, NOT DELETED.** It did not land. It is kept in full, below, because
it was written with equal care before the number existed and deleting it would destroy the only
evidence of that. Everything it says about 4-of-5 remains the registered reading had it fallen so.
**4 of 5 problems show a premium, p = 0.1875. THIS IS NOT A POSITIVE RESULT** — registered as such
in §2 before the first cell fired, precisely so it could not be written as "nearly significant".
⛔ It may not be reported as *"salt costs more on four of five problems"* without the p-value beside
it, and it may not be called a trend. The four premiums above 1 are still reported by name (§33),
as is LRU's below-1 premium (§67), and **the design's inability to call an opposite-direction
result significant (§20) applies here too**: 4/5 is weak evidence in the direction tested, not
evidence against.

## WHAT IS TRUE UNDER EITHER HEADLINE
* **CENSUS:** 36 cells · 32 priced · 4 VOID · 0 unharvested, counted by hand over the cells rather
  than taken from the harvester's own DONE. One cell (`f33c7e65`, $35.41) was recovered by a
  final-pass sweep **after the daemon exited reporting DONE** — without it FreeList would have had
  no premium at all.
* **THE FOUR VOIDS** (`59c93bbe` `7fa6c322` `823de693` `879326db`) produced no subject behaviour;
  three were caused by a fence-drift outage I caused by building a replacement cell into a live
  cells root. §18(b) records the procedure that prevents it.
* **PROVENANCE IS A RECONSTRUCTION, NOT A RECEIPT** (`PROVENANCE-matrix1-2026-09-08.tsv`): these
  cells carry no `ctl/built-from.tsv`. Client binary confirmed identical to stage 1's by byte size
  against stage 1's own record — 200225968 — so the two stages ran the same binary.
* **THE REGISTERED FLOOR WAS WELL-CALIBRATED:** registered sd 0.30458 from stage 1; matrix #1's own
  pooled sd finished at 0.2536. The gate was not conservative, and the value it would have taken
  had it been fitted to this run mid-flight (0.1082 at 20 cells) was wrong by a factor of three.


---

## ⚖️ THE RESULT, AS SCORED FROM THE ARCHIVE (`score_matrix1.py`, 37 cells, census hand-counted)

    Crc32 1.1610x · FreeList 2.7306x · LRU 1.4465x · LZW 1.3749x · Paxos 2.6514x
    5 of 5 problems show a premium > 1        p = 0.0312        SIGNIFICANT

⛔ **AND THE QUALIFIERS ARE THE HEADLINE, NOT A FOOTNOTE — all four registered before the fire:**
1. **THE TEST IS ONE-SIDED (§20).** It can confirm this hypothesis and **cannot significantly
   refute it**. Five premiums *below* 1 would have returned p = 1.0000. A one-sided test is a claim
   about which surprise you were willing to be surprised by; this one measured the expected surprise.
2. **THE MAGNITUDES ARE UNRESOLVED (G2).** Crc32 (1.1610) and LZW (1.3749) fall below the registered
   2.0072x floor. ⇒ **no ratio may be reported as the finding.** Not "2.7x", not "1.5-3x", not "about
   45% more". The finding is a SIGN across five problems.
3. **THE GOLD PAIR IS k=1 AND HAS NO VERDICT.** LZW 1.8105x, p = 0.5000. Four cards lack a
   `## Statement` section (§16), so the comparison the campaign most wanted **cannot reach .05 at any
   outcome**, and did not.
4. **n = 3 PER CONDITION, AND THE NOISE IS LARGE.** `FreeList plain` spans $13.02-$23.38 within one
   arm on one problem — a 1.80x spread that is noise, against a headline premium of 1.16x on Crc32.

## ⭐ THE PREDICTION, MADE BEFORE THE CELL EXISTED
§21 (commit `8477ca2`, before `d6b53ee4` ran) predicted the premium would be **"near 1.44"** from the
two surviving cells and LRU's plain median. **It came in at 1.4465.** That paragraph exists so no
reader has to take on trust that the prediction preceded the number — and so that the cell which
decided significance was fired under a rule (§18) written at 12:5x, hours before anyone knew a
campaign would turn on it.

📌 The run's own pooled sd finished at **0.2468** against the registered **0.30458**.

## ⛔ LIMITATION FOUND AFTER THE RESULT — CROSS-STAGE COST IS CONFOUNDED BY CONCURRENCY (2026-09-09 01:0x)

Measured while answering an unrelated question about what concurrency the placebo arm should use:

    stage 1     `ctl/pair_launch.log` receipts, distinct launch timestamps   ->  mostly ONE cell at a time
    matrix #1   `-ge 4` in both its fire and resume schedulers               ->  FOUR

⇒ **STAGE 1 AND MATRIX #1 WERE MEASURED UNDER A 4× DIFFERENCE IN BOX CONTENTION**, and this
harness's own harvest notes record box-busyness as a thing worth recording (*"3 OTHER client
processes are live on this box … the box was busy while this was taken"*).

⛔ **THIS IS A CORRECTION TO MY OWN EARLIER CLAIM.** I established that the two stages ran the
**same client binary** — 200225968 bytes, confirmed against stage 1's own record rather than from
matching version strings — and treated the stages as cost-comparable on that basis. **They are not
comparable on contention, and I never checked that axis.** ⇒ *I verified the axis I thought of and
then generalised the verdict past it* — the same defect as measuring the nodes and claiming the
edge, on my own claim, hours after making it.

**SCOPE, STATED PRECISELY:**
* It does **NOT** touch matrix #1's result. The sign test is computed entirely **within** matrix #1,
  where plain and salt-diet were both measured at 4-wide. The premiums and p = 0.0312 stand.
* It **DOES** bar any cross-stage cost claim — stage 1's premiums (1.1655–1.3560) against matrix
  #1's (1.1610–2.7306) — from being read as a replication of magnitude. The two sets differ in
  concurrency as well as in date, and nothing here separates those.
* The placebo arm therefore fires at **4-wide**, matching the arms it controls, so that this
  confound is not reproduced inside the comparison the placebo exists to make.

---

## ⛔⛔ CORRECTNESS: **N = 0.** NO CELL IN MATRIX #1 CARRIES A REFEREE VERDICT ON A WITHHELD SUITE.

> ✅⛔ **SUPERSEDED 2026-09-09 15:1x — N = 0 WAS TRUE WHEN WRITTEN AND IS NOW FALSE. THE REFEREE HAS BEEN
> INVOKED.** On the Captain's order, a declared post-hoc pass scored the whole declared set against the
> withheld suites. **Zero model tokens, 43 cells, 246 seconds.**
> ```
>   PASS 35 · FAIL 1 · CAP-COST 3 · FAILED-BOOT 4        of 36 LANDED cells, 35 pass
>   four of five problems TIE at 100% on both bare arms  ⇒ the instrument did not separate them
>   all six +stmt cells PASS 8/8, both arms
> ```
> **Full per-cell verdicts:** `RESULT-posthoc-correctness-verdicts-2026-09-09.tsv`. **The reading:**
> `RESULT-posthoc-correctness-2026-09-09.md`. **Frozen before the first suite ran:**
> `PRESPEC-posthoc-correctness-matrix1-2026-09-09.md` (commit `437ea70`, 14:57:28).
> ⛔⛔ **WHAT SURVIVES THIS SECTION UNCHANGED, AND IT IS THE HALF THAT MATTERED:** this run was
> **REGISTERED AS A COST EXPERIMENT**, and the correctness column is **POST HOC and labelled so
> everywhere**. It is not a pre-registered result and may never be presented as one.
> ⭐ **AND THE PASS FOUND A SELECTION EFFECT THIS SECTION COULD NOT HAVE SEEN:** all three budget-capped
> cells are `salt-diet`, none is `plain`, so the correctness column scores **18 plain against 12 salt**.
> The dropped salt cells are the ones that ran long enough to hit a cap — **the hard ones** — so **salt's
> pass rate is biased UP by construction.** ⇒ ***THE ARM THAT COSTS MORE IS SYSTEMATICALLY LESS LIKELY TO
> BE ASKED THE CORRECTNESS QUESTION.***
> 📌 **A PASS IS STILL NOT "CORRECT"** — it is *the withheld suite did not fail it*, and that suite's
> 44/44 is a **ceiling, not a strength**. **No sentence joins the premium to correctness with "and
> therefore".**


**The Captain's question at council 2026-09-09, answered at the object and written here because the
question was asked of this file: *of the priced cells, how many carry a referee GREEN on the withheld
suite, and from what path are the verdicts read?***

### THE ANSWER, AND THE PATH IS THE ANSWER
```
  cells with a ctl/ in ~/cells-matrix1 .................. 37
  PRICED (numeric at_end_COST in ctl/post-end-N.tsv) .... 33
  carrying a referee GREEN on a withheld suite .......... 0        ← N = 0 of 33
  PATH the verdicts are read from ....................... THERE IS NONE
```
**Measured across the whole root, five patterns, each zero:** files matching `*referee*` **0** ·
`*withheld*` **0** · `*hidden*` **0** · `*verdict*` **0** · `*green*` **0**. **And
`score_matrix1.py` reads no referee verdict of any kind** — it reads `COST` off the archive. ⛔ The
only per-cell artefact that looks like a check is `ctl/check.out`, whose content is
`manifest: check clean` — **a manifest integrity check, not a correctness verdict.**
⇒ 🔑 ***MATRIX #1 IS A COST RESULT WITH NO CORRECTNESS EVIDENCE ATTACHED. THE SCOREBOARD IS SILENT ON
CORRECTNESS BECAUSE NOTHING EVER MEASURED IT, NOT BECAUSE THE MEASUREMENT WAS OMITTED FROM THE
WRITE-UP.***
⚠️ **This does not say the code was wrong.** It says **no instrument in this run asked.** A premium is
a price for work whose correctness this run did not verify, and any paper sentence pairing the premium
with quality is unsupported by this dataset.

### (a) "PRICED" DOES **NOT** IMPLY "LANDED" — THREE OF THE PRICED CELLS WERE CAPPED
```
  kind (field 1 of ctl/post-end-N.tsv), all 37:
     30  LANDED
      3  CAP-COST        ⇐ PRICED AND NOT LANDED
      4  FAILED-BOOTS    ⇐ not priced
  ⇒ 33 priced = 30 LANDED + 3 CAP-COST
```
⛔ **So the census counts three cells that hit their COST cap and stopped.** A capped cell has a real
price and an unfinished job; **pricing it beside a landed one prices two different events under one
name.** ⚠️ **The question said 32 priced; I measure 33** — stated rather than silently adopted, and the
breakdown above is what any reconciliation should use. **Neither number changes N, which is 0.**

### (b) G-P2's "TESTS GREEN" IS NEITHER — IT IS A PLACEBO CLAUSE AND IT IS UNWIRED
`G-P2` is defined in `DESIGN-placebo-behavioural-gate-2026-09-08.md:47` — *"THE CELL STILL LANDS.
landed-N present, tests green, END LANDED, no cap"* — as an **acceptance gate for the PLACEBO ARM**,
not a matrix #1 scoring clause. ⇒ **It does not apply to these 33 cells at all.**
⛔ **And within its own scope it is a design clause that was never implemented:** `tests green` occurs
in that design line and **nowhere else in the harness.** It names no suite, reads no file, and has no
call site. ⇒ **It is therefore neither the withheld suite nor the cell's own tests — it is an
unbound phrase**, and a reader pairing it with "the referee" would be attributing a check that does
not exist.
📌 The hidden-suite work that DOES exist (`test_strength_v3.py`, `hidden_test_strength_table_v3.py`)
characterises the suite's **MUTANT-KILL STRENGTH** — 44/44, score 1.000, *a ceiling and not a strength*
because the mutants were authored beside the tests. **That is a property of the SUITE. It is not a
verdict on any CELL.**

⇒ ⚖️ **BINDING ON THE PAPER:** matrix #1 may be reported as a **COST** result only. **No sentence may
pair its premium with correctness, quality, or "working code"**, and the absence is structural — there
is no path from which such a verdict could be read.

## ⛔⛔ THE HEADLINE'S n=3 ON THREE PROBLEMS RESTS ON CELLS FROM ANOTHER ROOT

**systems' sensitivity, confirmed here at the object.** `score_matrix1.py:88` declares the scored set
as *the cells in `MATRIX_ROOT` **plus three named SMOKE cells**, and nothing else*:
```
  SMOKE = { ae304f63 , a69e9131 , b7537006 }   ← root `~/cells`, NOT ~/cells-matrix1
  measured: all three are arm=plain, kind=LANDED, one each for FreeList · LRU · Paxos
  plain-arm LANDED cells IN THE MATRIX ROOT:   FreeList 2 · LRU 2 · Paxos 2
  ⇒ those three problems reach n=3 ONLY by counting one §12 smoke cell each
```
⇒ **Without them the registered rule takes no median and the three problems leave the sign test
entirely: 2 of 2, p = 0.25.** ⇒ 🔑 ***THE 5/5 · p = 0.0312 HEADLINE DEPENDS ON THREE CELLS THAT WERE
BUILT AS A SMOKE, IN A DIFFERENT ROOT, AND THE SCOREBOARD DOES NOT SAY SO.***
⛔ **This is not a defect in the declaration** — the set is declared explicitly in the scorer, by id,
with a comment saying why a glob would be wrong. **It is a defect in the WRITE-UP: the reader of the
headline is not told that three of its five problems stand on a borrowed cell.**
⚠️ **And it is the same class as the correctness gap above** — *a structural property of the dataset
that the scoreboard is silent about.* ⇒ **Both must travel with the number into the paper.**
📌 **THE REMEDY IS THE ORDER ALREADY GIVEN:** three plain cells — FreeList · LRU · Paxos — fired on
systems' construction top up the matrix root so the three problems reach n=3 **within their own run**.
**Until they land, any published p-value carries this dependency**, and the honest form names it.

### ✅ DISCHARGED 2026-09-09 — BY MEASUREMENT, AND THE DISCHARGE IS NARROWER THAN IT LOOKS

The three cells landed. **The scorer now computes the declared set BOTH ways and prints the comparison
itself**, so this is the instrument's verdict rather than an argument:
```
  READING A  matrix root + top-up + the SS12 smoke cells   43 cells   5 of 5   p = 0.0312
  READING B  matrix root + top-up ONLY                     40 cells   5 of 5   p = 0.0312
  ⇒ IDENTICAL SIGN VERDICT WITHOUT THE BORROWED CELLS.
```
**The dependency this section reports is discharged: the headline does not rest on the smoke cells.**
Full capture, cut from the instrument's own stdout with its sha beside it, in
`RESULT-n3-topup-2026-09-09.md`.

⛔⛔ **AND IT IS DISCHARGED ONLY FOR THE SIGN. A AND B DO NOT AGREE ON THE MAGNITUDES.**
```
  LRU       1.2826 -> 1.1521   the CHEAPEST plain cell leaves; the plain median RISES
  Paxos     2.4306 -> 2.2437   same direction, same cause
  FreeList  2.8070 -> 2.8879   a mid-range cell leaves; the median falls
```
**B's LRU premium, 1.1521x, is the closest to 1.0 any premium has come in this campaign, and the smoke
cells were flattering it.** Three of five moved and two moved DOWN. ⇒ 🔑 ***THE SIGN AND THE p-VALUE ARE
ROBUST TO THE BORROWED CELLS; THE MAGNITUDES ARE NOT — WHICH IS WHY THE INSTRUMENT PRINTS BOTH READINGS
AND WHY NEITHER MAY TRAVEL ALONE.***
⛔ **What the top-up did NOT do, stated so it cannot be written up as more:** because it could not move
any premium to 1 — that invariance was computed and registered before the cells ran — **it could not
have changed the verdict, so it did not confirm it.** It bought precision and removed a dependency.
**It is not a replication.**
📌 **The correctness gap above is UNTOUCHED by all of this.** These three cells carry no referee verdict
either, so **N = 0 stands at 36 priced cells instead of 33.** No number of cost cells closes a
correctness gap.
