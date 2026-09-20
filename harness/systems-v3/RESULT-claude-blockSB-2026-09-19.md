# RESULT OF RECORD — BLOCK SB (the Claude lane's first BROWNFIELD block), `claude-opus-5`
## bench (SaltBench lead), 2026-09-19. 10 conditions · 30 cells · 30 of 30 scorable on EVERY column.
## Cells built from export `283362105d75d4ca68336875aa358049748fe019` ("2833621"), one sha across all 30.
## ⛔ Every number below names the file it came from. Nothing is retyped from a bus post or a message.
## 📌 The per-cell table is also a FILE: `RESULT-claude-blockSB-2026-09-19-cells.tsv` (30 rows, 24 columns),
## and `RESULT-claude-blockSB-2026-09-19-verify.py` re-derives every figure in §1–§7 from it.

---
# §1 · THE HEADLINE, AND IT IS THREE THINGS: TWO CEILINGS, AND A SEPARATOR THAT IS MEASURING THE WRONG QUANTITY

```
  ①  PASS RATE IS A TOTAL CEILING.  suite PASS 30/30 — ten of ten conditions at 3/3, both arms
     identical on every problem.  V1 bugs_fixed is ALSO at ceiling: 30 of 30 cells fixed every
     seeded bug (1 of 1 ×6 · 5 of 5 ×12 · 6 of 6 ×12).   ⇒ NEITHER CAN DISCRIMINATE THE ARMS.
  ②  THE REGISTERED BROWNFIELD PRIMARY SEPARATOR (§B5 `retained`) SEPARATES THEM PERFECTLY —
     DISJOINT ON 5 OF 5 PROBLEMS — AND §5 SHOWS IT IS READING **GROWTH**, NOT REWRITING.
  ③  COST IS THE ONE UNAMBIGUOUS SEPARATION.  salt-diet / plain = 18.59x TOTAL TOKENS,
     10.65x SPEND, AND BOTH ARE **LOWER BOUNDS**: 4 salt cells were censored at the cost cap
     and 0 plain cells were (§6).
```
⇒ **NO ARM CLAIM ON CORRECTNESS IS MADE OR AVAILABLE FROM THIS BLOCK.** Both arms passed everything they were
scored on. What this block establishes is a **price** and an **instrument defect**, not a quality difference.

---
# §2 · ⛔⛔ THE FINDING THAT OUTRANKS EVERY NUMBER ABOVE — 18 OF 30 CELLS WERE FIRST SCORED AGAINST THE WRONG SEED TREE, AND THE INVOCATION WAS MINE

The first scoring pass (harvested 2026-09-19T22:46Z; its raw table is `sb-score1-pinned-tree.tsv`, copied into
this repo so §2 cites a public object) returned **18 of 30
cells with `class REFUSED`** and **6 with `V1 UNMEASURED`**, and was published by me as *"a total ceiling that
resolves nothing."* **That was my scoring invocation, not the cells.**

## §2a · THE TWO EXPORTS ARE EXACT COMPLEMENTS, AND ONE `--tasks` FLAG CANNOT BE RIGHT
`score_claude_v3.py` takes a single `--tasks` root and feeds it to **two different consumers**:
```
  (a) the rung's run_tests.sh   — the SUITE      (b) W1, the external SEED WITNESS of the rewrite classifier
```
**Measured at the object, on the run box, all five problems:**
```
  export 2833621  (the cells were BUILT from it)   5 of 5 seeds      0 of 5 suites   <- suites stripped BY DESIGN
  export 9f650a3  (pinned for its suites)          4 of 5 seeds      5 of 5 suites   <- no Crc32/brownfield AT ALL
```
⇒ **Neither tree can serve both, and the tree I passed was right for the suite and wrong for the witness.**
**The seed shas, `sha256/16` of `<tree>/<problem>/brownfield/solution.rs`:**
```
  Crc32     2833621  61a04675715e66c1      9f650a3  ABSENT              ⇒ "W1 absent"
  FreeList  2833621  528ea4a5097cab56      9f650a3  4ebaf3df8b2a10c1    ⇒ DIFFER
  LZW       2833621  478b2035f6fcc7a4      9f650a3  aa968d046528530b    ⇒ DIFFER
  LRU       2833621  d9b2f3d364f3a6c6      9f650a3  d9b2f3d364f3a6c6    ⇒ SAME
  Paxos     2833621  1ce92803be426d32      9f650a3  1ce92803be426d32    ⇒ SAME
```
⭐ **`528ea4a5097cab56` AND `478b2035f6fcc7a4` ARE, VERBATIM, THE `W2 ctl/seed-sha` VALUES IN THE CLASSIFIER'S
OWN REFUSAL NOTES.** The cells' seeds match **their** export exactly. The classifier compared them against a
different export and **refused rather than guessing, which is the tool being right.**
⛔ **AND THE REFUSAL WEARS THE SIGNATURE OF A REAL FINDING.** Reading rule §241 item 6 makes *"the given at the
first commit is not the export's"* a **`VOID(GIVEN)`** — a finding **about the cells**. Taken at face value the
first TSV said 18 cells were unclassifiable. ⇒ ***A FALSE VOID IS NOT A CAUTIOUS ERROR: IT WOULD HAVE ENTERED
THE CENSUS AS EVIDENCE AGAINST THE HARNESS.***

## §2b · ⛔ THE OBVIOUS REMEDY FAILED, AND THE REASON IS WORTH MORE THAN THE REMEDY
A composed **tasks tree** (suites from 9f650a3, every `<problem>/brownfield/` from 2833621) made **every** cell's
suite read `UNPARSED` — **including LRU, whose `G/` directory is byte-identical to the original by `diff -rq`.**
**The cause, read at the object:** each rung's `_common.sh` is a one-line shim that sources
`"$(dirname $0)/../../../../harness/systems-v3/_common_v3.sh"` — **four levels up and OUT of the tasks tree
entirely, into its export's `harness/`.**
⇒ 🔑 ***A TASKS ROOT IS NOT RELOCATABLE. THE SUITE IS NOT A DIRECTORY OF FILES, IT IS A DIRECTORY OF FILES AT A
FIXED DEPTH INSIDE A COMPLETE EXPORT*** — so "just build the tree that serves both" is wrong in a way no file
comparison can show.
⭐ **AND THE SCORER'S OWN GUARD IS WHY THIS COST NOTHING:** `run_suite` refuses a verdict whose PASS/FAIL names
do not account for the `TESTS p/t` line — *"the names must account for the count, or the name sets are not the
suite's"*. **A relocated tree produced `UNPARSED`, never a plausible number.** A scorer trusting `rc` alone would
have scored 30 cells silently against a suite that never ran.
✅ **WHAT WORKS IS A COMPOSED *EXPORT*, AT THE RIGHT DEPTH:** `~/bench-dry/sb-composed-export/{harness,tasks}`,
harness and tasks from 9f650a3, each `<problem>/brownfield/` replaced from 2833621, with per-file provenance in
its own `COMPOSED-FROM.txt`. One invocation is then correct for both consumers.

## §2c · ⭐ THE CONTROLS, CHOSEN BEFORE LOOKING, AND ALL THREE PASSED
```
  1  SUITE VERDICT must reproduce on all 30 between the pinned-tree pass and the composed pass    0 mismatches
  2  CLASS + RETAINED must equal the standalone classifier run against the build export           0 mismatches
  3  the 24 V1 values already measured must not move                                              0 moved
  ⭐ AND THE ONE THAT MAKES IT A TEST RATHER THAN A RE-RUN: LRU and Paxos have a BYTE-IDENTICAL
     witness in both trees, so those 12 cells COULD NOT change. They did not — class and `retained`
     to three decimals. THE 12 THAT COULD NOT CHANGE DID NOT; THE 18 THAT COULD, DID.
```
✅ **AFTER THE CORRECTION: `class REFUSED` 18 → 0 · `V1 UNMEASURED` 6 → 0.** Every column is populated for all 30.

---
# §3 · POPULATION — 10 CONDITIONS, 30 CELLS, 3 OF 3 EVERYWHERE
```
  conditions   claude-opus-5 x brownfield x {Crc32,FreeList,LRU,LZW,Paxos} x {plain,salt-diet} x extras=none
  cells        30 declared, 30 harvested, 30 scored.  Cells per condition: 3 of 3, on every one of the ten.
  run state    ENDED: LANDED 25 · ENDED: CAP-COST 4 · ENDED: DIALOG 1   — 30 of 30 TERMINAL
  w1_fenced    COVERED 30/30        suite  PASS 30/30        class  30/30      V1  30/30
```
⛔ **`run_state` IS NOT A CORRECTNESS SIGNAL AND THIS BLOCK IS THE PROOF.** Self-graded `LANDED` is **25 of 30**;
verified suite PASS is **30 of 30**. ⇒ 🔑 ***A LANDING IS THE SUBJECT GRADING ITSELF; A COST CAP IS THE HARNESS
INTERRUPTING IT. NEITHER IS A STATEMENT ABOUT THE CODE.*** `saltbench/CLAUDE.md`'s rule — *"a self-graded landing
rate is an upper bound on a verified one"* — holds when the subject fails and **inverts when a cap cuts a
succeeding subject off.** The rule's purpose (never quote a landing rate as a correctness rate) is untouched;
only its DIRECTION is refuted, and only where a cap is the cutter.

---
# §4 · THE PER-CELL TABLE OF RECORD
`RESULT-claude-blockSB-2026-09-19-cells.tsv` — 30 rows, 24 columns, built by a mechanical join of three
receipts (the composed-export scoring pass, the retention decomposition, and each cell's own frozen meter),
with `class`/`retained` asserted equal across two independently produced sources at join time.

---
# §5 · ⛔⛔ RETENTION — THE REGISTERED PRIMARY SEPARATOR SEPARATES THE ARMS PERFECTLY AND IS READING **GROWTH**

`retained` is, in the classifier's own words, ***"difflib's line-level ratio of the END file against the SEED"***
— a **similarity ratio, symmetric in additions and deletions.** §B5's language is about **rewriting**:
`REPLACED` = *"present and rewritten wholesale"*, `REPAIRED` = *"present and EDITED"*. **Those are claims about
what SURVIVED, and a similarity ratio cannot see survival separately from growth.** So it is decomposed here —
`surv` = seed lines matched / seed lines, `growth` = end lines / seed lines, **both from the same differ, with
every `retained` asserted equal to the tool's own value** (the producing script imports the classifier and
fails otherwise):
```
                     retained            SURVIVAL             GROWTH            REPLACED
  plain      n=15    0.426 .. 0.981      0.420 .. 0.990       0.96x ..  1.18x    0 of 15
  salt-diet  n=15    0.102 .. 0.346      0.419 .. 0.995       3.92x .. 14.70x    7 of 15
                     DISJOINT 5 of 5     DISJOINT 3 of 5      DISJOINT, 3.3x apart
```
⛔ **THE TWO ARMS' SURVIVAL RANGES ARE THE SAME RANGE.** What differs with no overlap is how much the salt-diet
arm **ADDS**.
⭐ **THE PAIR THAT SETTLES IT, AND IT IS TWO ROWS OF THE TABLE OF RECORD:**
```
  clbbfs02  FreeList  salt-diet   survival 0.995  (191 of 192 seed lines kept — HIGHEST in the block)  retained 0.301
  clbbzp01  LZW       plain       survival 0.420  ( 42 of 100 seed lines kept — lowest of the 15 PLAIN)  retained 0.426
```
***THE CELL THAT KEPT 99.5 % OF THE GIVEN SCORES WORSE ON "RETENTION" THAN THE CELL THAT KEPT 42 %.***
⚠️ **`clbbzp01` is the lowest-survival PLAIN cell and not the lowest in the block** — `clbbps03` (Paxos,
salt-diet) is 0.419, lower by 0.001. **The first draft of this line said "LOWEST in the block" and the
verifier reddened it**, which is what an arm derived from the table is for; the pair is chosen to put a
plain cell against a salt one, so the plain minimum is the figure that belongs here.
⭐⭐ **AND ON LZW THE METRIC POINTS THE WRONG WAY OUTRIGHT.** `retained` plain 0.426–0.818 vs salt 0.102–0.132,
disjoint — *"the salt arm rewrote far more."* **`surv` plain 0.420–0.830 vs salt 0.670–0.800 —** ***the salt arm
kept MORE of the given than plain did.*** Same cells, same differ, opposite conclusions.
⚠️ **THE HONEST HALF: SURVIVAL *IS* DISJOINT ON 3 OF 5 (Crc32, LRU, Paxos).** There is a real effect and it is
in the same direction. **It is a fraction of the size `retained` reports, it reverses on LZW, and it cannot
carry a `REPLACED` label on 7 cells that retained 41.9–80.0 % of the given.** *(That band is the seven
`REPLACED` cells' OWN survival range, derived; 99.5 % belongs to `clbbfs02`, which is `REPAIRED`. An earlier
draft reached for the block maximum and the verifier caught it.)*
⚠️⚠️ **THE MECHANISM IS HYPOTHESISED, NOT DRIVEN, AND IS LABELLED SO.** The salt-diet method file is a Verus
proof method (`proof` ×9, `ensures` ×4, `invariant` ×3, `requires`, `spec`); the plain method file contains the
string `Verus` **zero** times. A method whose prescribed output is *"the code AND its proof"* scores low on any
similarity-to-the-given measure **by construction, without touching a line.** ⛔ **Nothing in §1–§7 depends on
this reading being right** — §5's arithmetic stands without it. *(The helm checked at the object that
`BROWNFIELD-BRIEFING-DIFF.md` establishes each arm's method file is byte-identical between greenfield and
brownfield, which removes an alternative explanation without being evidence for this one.)*
⇒ 🔑 ***THE INSTRUMENT SEPARATES THE ARMS PERFECTLY AND IT IS SEPARATING THEM ON THE TREATMENT'S OWN DEFINITION
OF ITSELF.***
⛔ **THE §B5 THRESHOLD WAS REGISTERED PRE-DATA, WHICH IS CORRECT PRACTICE AND DOES NOT RESCUE IT.**
***PRE-REGISTRATION PROTECTS AGAINST CHOOSING THE THRESHOLD AFTER THE DATA. IT IS NO PROTECTION AT ALL AGAINST
CHOOSING THE WRONG QUANTITY BEFORE IT — AND THE SECOND FAILURE LOOKS EXACTLY LIKE THE FIRST ONE BEING HANDLED
WELL.***
✅ **THE REMEDY PROPOSED HERE IS ADDITIVE AND COSTS NOTHING: REPORT `surv` AND `growth` BESIDE `retained`.** Both
fall out of the differ the tool already runs. **`retained` is KEPT, not struck** — it is the right alarm for a
lane where both arms ship the same kind of artifact. ⛔ **WHAT THIS DOCUMENT DOES NOT DO IS CHANGE WHAT THE
REGISTERED SEPARATOR MEANS.** That is a statement about a public claim and it is the Captain's; it goes to
Monday's pack with these measurements intact (helm, 106th, at the object).

---
# §6 · ⛔ THE COST CAP BINDS ONE ARM AND NOT THE OTHER, SO IT IS A TREATMENT
```
  cap   COST 37.21 per cell, identical for both arms by construction
  hit   salt-diet 4 of 15   ·   plain 0 of 15
  the four:  clbbfs01 37.8501 · clbbfs03 37.4300 · clbbps02 37.9576 · clbbps03 37.9185
```
⇒ **Those four are CENSORED: their true cost is `>=` the cap, so every premium in §7 is a LOWER BOUND.**
⇒ ⛔ **AND IT IS NOT ONLY A COST EFFECT: the ceiling in §1① IS A CEILING REACHED BY THE SALT ARM WHILE UNDER A
CAP THAT ONLY IT HITS.** A cap that binds one arm is part of that arm's treatment, and it is named here rather
than left in the `run_state` column.

---
# §7 · TOKENS AND COST (council 2026-09-17 ⑯: tokens are the price of record, by direction)
```
                       TOTAL TOKENS (final_T)                         SPEND (final_COST)
  problem        plain          salt-diet      x            plain        salt-diet        x
  Crc32          4,846,094      36,985,336     7.63x        2.3651       13.4405      5.68x
  FreeList      17,459,742     364,934,532    20.90x        8.7513      104.1953     11.91x
  LRU            6,250,693      69,505,436    11.12x        2.8935       23.2915      8.05x
  LZW            8,765,916     166,159,851    18.96x        4.7014       54.0169     11.49x
  Paxos         18,734,412     404,549,721    21.59x        9.3820      104.1904     11.11x
  ------------------------------------------------------------------------------------------
  TOTAL         56,056,857   1,042,134,876    18.59x       28.0933      299.1346     10.65x
```
⛔⛔ **DO NOT SET THIS BESIDE LEVEL 7's `4.295x total / 2.676x output` AS A LIKE-FOR-LIKE.** The comparable pair
is **TOTAL TOKENS: 18.59x here against 4.295x there.** The **output-token split is NOT in this receipt** —
`ctl/post-end-1.tsv` carries `T` and `COST` and no direction breakdown — so level 7's `2.676x output` **has no
counterpart in this block.** ⚠️ It matters: `T` is dominated by cache reads, and `$/T` and `$/output` have
ranked arms oppositely in this campaign before.
⚠️ **AND THE PREMIUM IS A LOWER BOUND** (§6): four salt cells stopped at the cap, one stopped on a dialog.

---
# §8 · WHAT THIS RESULT DECLARES RATHER THAN RESOLVES
1. **No correctness claim.** Both ceilings (§1①) are total. The block cannot rank the arms on suite pass or on
   bugs fixed, and does not try.
2. **`bugs_introduced` is a FLOOR, not a measurement** — all 30 rows read `>=0 (suite-limited)`. The suite
   bounds what an introduced bug can be seen as; it does not enumerate them.
3. **The retention separation is not usable as an arm claim** until §5's question is settled, which is the
   Captain's (the registered separator's meaning), not this document's.
4. **The output-token split is absent** (§7), so the cost decomposition that levels 6 and 7 and HC1 carry — how
   much of the premium is context versus generation — **cannot be computed for this block from this receipt.**
5. **This is one model on one field.** `claude-opus-5 × brownfield × extras=none`. It says nothing about the
   Claude lane's `statement` or `spec-change` conditions, and nothing about any other lane.
6. **The level-7 question is OPEN and OWED BY ME, not answered here.** Level 7's §1 calls retention *"the
   registered primary separator"* and reports it moving in 7 of 8 pairs; measured in its own cells file,
   brownfield only, **plain n=42 0.291–1.000 · salt-diet n=42 0.107–1.000** — same metric, same direction,
   **overlapping rather than disjoint.** ⛔ **Whether that separation is also growth is UNMEASURED.** Running
   the same `surv`/`growth` split over level 7's 84 cells is the next act; if it is growth there too, level 7
   owes an ERRATUM on its §1 headline — appended below its signed text, never inside it, and its wording is
   the Captain's.

---
# §9 · PROVENANCE
```
  cells        30, built from export 283362105d75d4ca68336875aa358049748fe019, on the run box
  suites       the G-rung run_tests.sh of export 9f650a3adf36 — the only tree carrying them
  seeds (W1)   <problem>/brownfield/solution.rs of export 283362105d75 — the export the cells were BUILT from
  scored by    score_claude_v3.py and brownfield_rewrite_class.py from 283362105d75's harness/systems-v3,
               --tasks pointed at the composed export (§2b), --declared a 30-line file, never a glob,
               --toolchain-env ~/cells/toolchain.env
  executors    clb-sb-score-2026-09-19 (pass 1, pinned tree; ENDED rc=0 2026-09-19T22:46:00Z) and
               clb-sb-score2-composed-2026-09-19 (pass 2, composed export; ENDED rc=0 2026-09-20T00:08:29Z),
               both registered in ~/.fleet/executors/bench/ with liveness, landing and harvester
  receipts     RESULT-claude-blockSB-2026-09-19-cells.tsv      the table of record, 30 rows
               sb-score2-composed.tsv                          pass 2, raw
               sb-class-correct-witness.tsv                    the standalone classifier, build-export witness
               sb-retention-decomp.tsv                         surv/growth, retained asserted == the tool's
               sb-meters.tsv                                   each cell's own frozen meter
               sb-score1-pinned-tree.tsv                       pass 1, kept in-repo because §2 is about it
  verifier     RESULT-claude-blockSB-2026-09-19-verify.py — re-derives every figure in §1–§7 from the table of
               record and asserts it against the BYTES of this document. No typed expectations.
```
## §9b · ⚠️ WHAT I DID NOT VERIFY, SAID HERE SO THIS IS NOT READ WIDER THAN IT IS
- **I did not re-run any cell.** Every number is a re-reading of artifacts that existed before this shift.
- **The Verus mechanism (§5) is hypothesised.** I read two method files' headings and needle-counted them; I
  did not measure how much of any end file is proof.
- **I did not decompose level 7** (§8 item 6), and I did not touch its signed text.
- **`surv` is a lower bound on survival**: it counts lines the differ MATCHED, and a moved line may not match.

## ✍️ NON-AUTHOR SIGNATURE — OWED
A pinned ask follows: file, blob and head, per council 2026-09-17 ⑨(2).

---
## ⚠️⚠️ ERRATUM 1 — **THE SUBJECT MODEL NAMED IN THIS RESULT IS WRONG. BLOCK SB WAS SERVED `claude-sonnet-5`, NOT `claude-opus-5`.** APPENDED BELOW ALL PRIOR TEXT; nothing above is edited.
*bench, 2026-09-20, on the 109th helm head's routed finding. It asked me to re-drive at my own receipts before believing it. I did, and it is right.*

### §E1.1 · THE RECEIPTS, WITH A CONTROL THAT FIRES
```
  served-clbb*.out in the run dir          30 files
    containing claude-sonnet-5             30      <- every cell of this block
    containing claude-opus-5                0
  CONTROL — the O block's served files     17 of 17 DO carry claude-opus-5
                                           ⇒ the needle works and the partition is clean
  the chain's own rule, clb_chain.v5.sh:69  case "$1" in O|OS) m=opus;; *) m=sonnet;; esac
                                           ⇒ SB is neither O nor OS, so SB fires SONNET by construction
  AMENDMENT-claude-lane-B-2026-09-16.md     ":279  Sonnet 46 = SG+SB+SS+SBS+SC"  ·  ":712  SB = Sonnet brownfield none"
                                           ⇒ the signed amendment had it RIGHT all along
  this file, before this erratum            claude-opus-5 x3 (title · :90 · :205) · "sonnet" x0
```

### §E1.2 · WHAT IS WRONG AND WHAT STANDS
⛔ **WRONG — the three statements of the subject:** the TITLE, the `conditions` line at `:90`, and the scope limit at `:205` all name `claude-opus-5`. **Read them as `claude-sonnet-5`.**
✅ **STANDS — every per-cell measurement in this file.** Not one number was derived from the model name: the suite results, `V1_bugs_fixed`, the class and retention columns, the run-state split (`LANDED 25 · CAP-COST 4 · DIALOG 1`), and §2's own headline finding that *"run_state is not a correctness signal"* are all unaffected. **The 24-column `-cells.tsv` is unchanged and correct.**
✅ **STANDS — *"the Claude lane's first BROWNFIELD block"***. That claim was never about the model.
⇒ **So this is an ATTRIBUTION error, not a measurement error**, and it is confined to which model's row these ten conditions belong in.

### §E1.3 · WHY NO GATE CAUGHT IT, WHICH IS THE PART WORTH KEEPING
⛔ **The `-cells.tsv` has 24 columns and NO model column.** `-verify.py` re-derives every figure in this result from that table — **so it cannot see the one field that is wrong, and its green was accurate about everything it could reach.**
⛔ **AND THIS RESULT WAS NEVER SIGNED:** `:243` still reads *"NON-AUTHOR SIGNATURE — OWED"*. **No signer missed the model; it never reached a signer.**
⇒ 🔑 ***A RESULT'S TITLE WAS ITS ONLY STATEMENT OF ITS SUBJECT, AND NOTHING MECHANICAL READ THE TITLE.*** Every instrument pointed at the table, and the subject was never in the table.
✅ **THE DURABLE FIX, OWED AND NOT TAKEN HERE:** a `model_served` column in every per-cell table, derived from the `served-*.out` receipts, and a `verify.py` arm that reads it against the result's prose. **Blocks SG · SS · SBS are harvested with no result of record yet, so it is cheapest to land before they are written** — which is the helm's recommendation and I adopt it.

### §E1.4 · SCOPE OF THE ERROR — measured, not assumed
```
  published RESULT files carrying a wrong model   1 of 1 (this one; it is the only result of record so far)
  the paper                                       block SB cited 0 times ("block SB" 0 files, "blockSB" 0 files,
                                                  CONTROL "saltbench" 5 files) ⇒ NO PUBLICATION EXPOSURE
  AMENDMENT-claude-lane-B                         CORRECT — it is the authority that contradicted me
  CENSUS ADDENDUM 11                              WRONG the same way; corrected by census ADDENDUM 12
```
⚠️ **The fleet-wide per-model tally (`Opus 28 · Sonnet 10` rather than `38 · 0`) is the helm's derivation, quoted here and NOT independently re-derived by me.** What I measured is this block: 30 of 30 cells served Sonnet.
