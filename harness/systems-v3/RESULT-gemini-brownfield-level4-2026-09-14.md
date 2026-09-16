# RESULT OF RECORD — THE GEMINI BROWNFIELD LEVEL-4 WAVE, 24 OF 24 CELLS
## bench (SaltBench lead), 2026-09-14. Registered freeze: `AMENDMENT-gemini-brownfield-level4-2026-09-13.md`.
## ⛔ **EVERY NUMBER BELOW WAS RE-DERIVED AT THE OBJECT BY THE LEAD.** Nothing here is retyped from a bus
## post, including the hand's. Where a figure came from a receipt file, the file is named.
## ⛔ **NO PUBLIC SENTENCE AND NO CLAIM ABOUT THE METHOD IS MADE HERE. Both are the Captain's.**

---

## §R0 · PROVENANCE, BEFORE ANY NUMBER

```
  RUNTIME  export_sha         ecd3924828cb3b1255115a3094e2ceee51d62dfd   (all 24 cells, one sha)
  SCORER   scorer_export_sha  saltbench-systems-v3 @ d20f95b             (NEWER than the runtime)
  W1       task tree          <export_root>/tasks/systems-v3             w1_fenced COVERED on all 24
  CLIENT   agy · vendor google · model_requested = model_served = gemini-3.1-pro-high
  CAPS     T1_TOK 250,000,000 · max_wall 21,600 s · max_turns 40 · turn_timeout 2,100 s
           print_timeout 1,800 s (per TURN)
  RUN BOX  the designated run box (named in the private run record, never here)
```
§L-rule 6 permits the scorer to be newer than the runtime and requires both to be recorded; they are.
**The runtime is pinned; the instrument is not.** The classifier's selftest was **re-run by the lead**
(35 of 35), not accepted from the hand's report.

⛔ **`built-from.tsv` records the BUILDER, and a reader will take it for the TOOLCHAIN** (§L5 rule 6).

---

## §R1 · THE 24 CELLS — THE FULL TABLE, ONE ROW PER CELL

Classes and retention from `brownfield_rewrite_class.py` (fixed `run_state` build) against W1.
PASS/FAIL and TRUNCATED from `score_wave_v3.sh`, per-condition receipts under
`~/.fleet/executors/gemini.runs/l4-score-2026-09-14/`.

```
  cell      task      arm        class     run_state  retained  end_sha (16)       suite   trunc
  b4fp01    FreeList  plain      REPAIRED  LANDED     0.779     dfd5db6cfb2e4910   7/7     -
  b4fp02    FreeList  plain      REPAIRED  LANDED     0.621     e28ceef389ecdc12   7/7     -
  b4fp03    FreeList  plain      REPAIRED  LANDED     0.926     6df4ef52b455df95   7/7     -
  b4fs01    FreeList  salt-diet  REPLACED  LANDED     0.137     42639464ad9bd249   3/7     -
  b4fs02    FreeList  salt-diet  REPAIRED  LANDED     0.449     36645dc3bdde4c15   3/7     2 turns
  b4fs03    FreeList  salt-diet  REPLACED  LANDED     0.183     908c1e42dd48702f   7/7     4 turns
  b4lrp01   LRU       plain      REPAIRED  LANDED     0.981     5de38fa13f67a5a6   16/16   -
  b4lrp02   LRU       plain      REPAIRED  LANDED     0.981     5b15c6e7ebfa14bf   16/16   -
  b4lrp03   LRU       plain      REPAIRED  LANDED     0.981     4e7fd6aacf1be526   16/16   -
  b4lrs01   LRU       salt-diet  REPAIRED  LANDED     0.517     c267ec19596a1e4b   16/16   -
  b4lrs02   LRU       salt-diet  REPAIRED  LANDED     0.322     369b0a6ce70134fa   16/16   -
  b4lrs03   LRU       salt-diet  REPAIRED  LANDED     0.397     51df60ee630ce206   10/16   -
  b4lzp01   LZW       plain      REPAIRED  LANDED     0.985     d15a046c8adb74d0   8/8     -
  b4lzp02   LZW       plain      REPAIRED  LANDED     0.990     ad52b5e65b810f55   8/8     -
  b4lzp03   LZW       plain      REPAIRED  LANDED     0.985     d15a046c8adb74d0   8/8     -
  b4lzs01   LZW       salt-diet  REPAIRED  LANDED     0.463     2c1679c7febb7eec   8/8     1 turn
  b4lzsb01  LZW       salt-diet  REPAIRED  LANDED     0.523     25949c2dcf8ce050   8/8     -
  b4lzsb02  LZW       salt-diet  REPAIRED  LANDED     0.406     4f31f2c121590281   3/8     1 turn
  b4pp01    Paxos     plain      REPAIRED  LANDED     0.992     8d6bfc362890143d   17/17   -
  b4pp02    Paxos     plain      REPAIRED  LANDED     0.978     254b98d33e2cabf0   17/17   -
  b4pp03    Paxos     plain      REPAIRED  LANDED     0.978     2cf0b5c24a8cf7e7   17/17   -
  b4ps01    Paxos     salt-diet  REPAIRED  LANDED     0.696     ad4cbccb754a6fef   17/17   -
  b4ps02    Paxos     salt-diet  REPAIRED  LANDED     0.756     56e31f246cff7e9d   17/17   -  SELF-NOT
  b4ps03    Paxos     salt-diet  REPAIRED  LANDED     0.670     8b24652f1eab8458   12/17   1 turn
```
`ENDED 24/24 · LANDED 24 · SCORABLE 24 · EXCLUDED 0 · UNFETCHED 0 · NOT-LANDED 0 · VOID 0.`
**No cell met any §L6 void condition.** `UNTOUCHED` (§L9 item 4) occurs **zero** times.

---

## §R2 · THE WITHHELD SUITE — TWO RATES, NEVER ONE NUMBER (§L5 rule 3)

```
  arm         cells   FULL PASS      TRUNCATED      SELF-DECLARED NOT
  plain         12    12 of 12        0 of 12           0 of 12
  salt-diet     12     7 of 12        5 of 12           1 of 12
```
⛔ **The TRUNCATED column is not a subtraction from the FULL PASS column.** Of the 5 truncated
salt-diet cells, **2 are FULL PASS** (`b4fs03` 7/7, `b4lzs01` 8/8) and their passes stand as a **FLOOR**
(§L5 rule 2). Their **token, turn and wall figures are NOT POOLABLE across arms** and appear in no
premium anywhere in this file.

---

## §R3 · RETENTION — THE SIGN, AND THE SEPARATION THAT DOES NOT SURVIVE

```
  arm         n    retained min .. max     mean      REPLACED (< 0.20, pre-registered §B5)
  plain       12   0.621 .. 0.992          0.9314    0
  salt-diet   12   0.137 .. 0.756          0.4599    2   (b4fs01 0.137 · b4fs03 0.183, both FreeList)
```
✅ **THE SIGN HOLDS AND IT IS ALL §L5 rule 1 PERMITS:** the control retains more of the seed than the
treatment, and both REPLACED cells are on the treatment arm against zero on the control.
⛔ **NO MAGNITUDE AND NO RATIO IS CLAIMED.** §B6's resolvable floor rests on a sigma measured on a
GREENFIELD population and no brownfield dispersion has been measured. The two means appear so the sign
has a referent, not as an effect size.

### ⛔⛔ THE INTERIM "NO OVERLAP" IS WITHDRAWN, AND THE CELLS THAT KILLED IT WERE THE NAMED TEST
At 16 of 24 the hand reported *"lowest plain 0.621 > highest salt-diet 0.523 → NO OVERLAP"*. At 24 of 24:
```
  SEPARATION TEST   lowest plain 0.621   vs   highest salt-diet 0.756   ->   OVERLAP
  salt-diet ABOVE the lowest plain cell:  3  ->  b4ps01 0.696 · b4ps02 0.756 · b4ps03 0.670   ALL PAXOS
  plain BELOW the highest salt-diet cell: 1  ->  b4fp02 0.621
```
**Paxos was absent from the interim slice, and the interim post named Paxos as the test of whether the
pattern tracked seed size or arm.** It ran. It resolved the seed-size confound **against** the interim
reading — Paxos has the largest seed (377 lines) and produced no REPLACED cell — **and in the same
stroke it destroyed the separation.**
⇒ 🔑 ***A SEPARATION IS A UNIVERSAL QUANTIFIER OVER TWO EXTREMA AND DIES TO ONE CELL; A SIGN IS A
CLAIM ABOUT TWO MEANS AND SURVIVED.*** The freeze permitted only the sign, and the sign is what stood.
⚠️ **The interim post scoped itself correctly — "wave INCOMPLETE, 16 of 24, Paxos absent" — and the
scoping did not save the claim.** A caveat under a bolded sentence does not stop the sentence
travelling; it only makes the retraction cheaper.
⭐ **AND THE OVERLAP IS WORTH MORE THAN THE SEPARATION WAS:** a salt-diet cell at 0.756 retained is a
genuine repair of the existing implementation, while `b4fs01` at 0.137 is the same arm replacing it.
**The treatment's behaviour is problem-dependent, not uniformly rewrite-heavy** — which a clean
separation would have concealed.

---

## §R4 · DISTINCT `end_sha` — ADOPTED AS A STANDING COLUMN

```
  task      arm         n   distinct
  FreeList  plain       3      3
  FreeList  salt-diet   3      3
  LRU       plain       3      3
  LRU       salt-diet   3      3
  LZW       plain       3      2      <== ONE COLLISION
  LZW       salt-diet   3      3
  Paxos     plain       3      3
  Paxos     salt-diet   3      3
  WAVE      all        24     23
```
⚖️ **RULED: every condition table from here carries `n` and `distinct` as two columns.** The plain arm's
**12 of 12 covers eleven distinct end states.**

### THE ONE COLLISION, MEASURED — AND IT IS INDEPENDENT CONVERGENCE, NOT SHARED STATE
`b4lzp01` and `b4lzp03` have byte-identical `solution.rs` (2,749 B), verified with a **positive control
in both directions**: `01 vs 03` = 0 diff lines, `01 vs 02` = 5 diff lines.
⛔ **A COLLISION ALONE CANNOT TELL TWO MECHANISMS APART** — (a) a low-entropy task on which independent
runs converge, where n stays 3, and (b) shared state between cells, where they are dependent. Measured
at the object:
```
  cell      T (tokens)   commands   wall_s   HEAD tree (16)
  b4lzp01      861,030       8       160.3   3a23a8d50a7fcea0
  b4lzp02      746,412       6       163.0   117c1aa419ecb3dd
  b4lzp03    1,272,333      15       217.2   1cc1955a1e537710
```
⇒ ✅ **MECHANISM (a).** The two colliding cells differ by **48% in tokens, 88% in commands and 36% in
wall clock, carry different work-order ids, and have different HEAD trees.** Only `solution.rs` agrees.
**A cache or a replay returns identical cost; these two runs paid different prices and arrived at the
same file.** The hand's independent evidence points the same way: `b4lrp01/02/03` share a retention
fraction of 0.981 across **three** distinct `end_sha` — a cache would give identical bytes, not
identical fractions.
⛔ **THEREFORE THE PHRASE "EFFECTIVE n" DOES NOT APPEAR IN THIS FILE.** It is a claim about mechanism,
and the mechanism here is measured to be the one under which **n stays 3**. The column's value is that
it FLAGGED the pair for exactly this measurement.

---

## §R5 · ⚖️ RULING — THE SELF-DECLINED CELL `b4ps02` COUNTS AS A PASS

`b4ps02` (Paxos, salt-diet) declares **nine requirements `[PARTIAL]`** in its own `LANDING.md` and passes
**17 of 17** on the withheld suite. Its own words: *"proof fn agreement (drafted, proof deferred)"* …
`NOT ESTABLISHED: Verus full verification.`

⚖️ **IT COUNTS IN THE LANDING RATE, AND THE RULE THAT DECIDES IT WAS REGISTERED BEFORE THE WAVE FIRED**
— §L5 rule 3: *"LANDING AND PASSING ARE TWO RATES AND ARE NEVER ONE NUMBER."* The withheld suite
measures **behaviour** and is outside the subject's reach; the self-declaration measures the subject's
**proof state**. A subject that honestly declined to claim completion on work that fully satisfies the
suite is not a failed attempt, and binning it as one would flatter the control.
⛔ **AND A SELF-DECLARATION RATE IS NOT COMPARABLE ACROSS ARMS — BY CONSTRUCTION, NOT BY SMALL n.**
Measured on the two arms' briefings (`repo/AGENTS.md`, Paxos pair):
```
  token     plain   salt-diet
  Verus       0         5
  proof       0        10
  ghost       0         2
```
**The control carries no proof obligation at all, so it cannot produce this class of `PARTIAL`.** The
axis is arm-incomparable in the same way token, turn and wall are.
⇒ **REPORT IT AS ITS OWN NUMBER — salt-diet 1 of 12, plain 0 of 12 — NEVER as a deduction from a
behavioural denominator and never as a cross-arm rate.**
⚠️ **n = 1.** Nothing about the frequency of this behaviour is claimed.

---

## §R6 · ⛔ AN INSTRUMENT DEFECT: THE POOLING CHECK READS THE SPEC FROM THE SUBJECT'S WRITABLE TREE

The `cells-b4-lzw-saltdiet-b` receipt reads: *"POOLING REFUSED: b4lzsb02's interface is
c93a0e063c5b44b9, not 32440ef2728bf782. These cells were not given the same problem."*
✅ **THE REFUSAL FIRED CORRECTLY. ITS STATED CAUSE IS FALSE — THEY WERE GIVEN THE SAME PROBLEM.**

Measured at the object, W1 first:
```
  W1          one card.md per task in the export.  LZW: sha256/16 f5c3e8c943520815
  ISSUED      REQUIREMENTS.md at each cell's ROOT COMMIT, author `customer@bench` (the harness)
                FreeList 90721f712dea91e9 · LRU a7c0bddaf5698b10
                LZW      c93a0e063c5b44b9 · Paxos d9836b833c7ee32c
              -> FOUR issued specs, ONE PER TASK, IDENTICAL ACROSS BOTH ARMS, on all 24 cells
  DIVERGENT   b4lzsb01 ONLY:  HEAD 32440ef2728bf782  vs  its own root commit c93a0e063c5b44b9
```
The cause is a **subject edit**: `b4lzsb01` prefixed all eight requirements with `DONE ` — 8 x 5 bytes =
the exact +40-byte delta, on an unchanged 46 lines — and committed it as `1485dcb "Requirements DONE"`,
a subject commit sitting above the harness root commit `3d249eb`.

⇒ 🔑 ***THE SCORER READS THE SPEC FROM THE SUBJECT'S WRITABLE POST-RUN TREE, SO IT MEASURES THE END
STATE AND NOT THE ISSUED ONE.***
- **Here it failed LOUD**, which is the safe direction, and no result is harmed.
- ⛔ **IT CAN FAIL QUIET.** Two subjects in one root making the same edit agree with each other, and the
  gate prints ✅ POOLABLE over a file that is nobody's issued spec.
- ✅ **FIX, ONE LINE:** hash W1's `card.md`, or `REQUIREMENTS.md` at the root commit whose author is
  `customer`. Both are outside the subject's reach; the working tree is not.

### ⭐ AND A SECOND, LARGER GAP THE SAME READ CLOSED: THE CROSS-ARM INTERFACE WAS NEVER CHECKED
`ifsha` is reset per invocation and the scorer is invoked **once per root**, so the pooling check has
only ever compared cells **within one condition**. The question the campaign actually rests on — *were
the two ARMS given the same problem?* — **had not been asked by any instrument.**
✅ **IT HAS NOW BEEN ASKED, FOR ALL FOUR TASKS, AND IT HOLDS** (the four issued hashes above).
**Cross-arm comparability is intact, and `b4lzsb01`'s 8 of 8 stands.**

---

## §R7 · ⛔⛔ THE PER-TURN WALL CLOCK — AND A CONFLATION IN THIS CAMPAIGN'S OWN FREEZE

```
  wave                   instrument                         salt-diet        plain
  greenfield             done_reason TURN-TIMEOUT           4 of 21 (19.0%)  0 of 24
  greenfield             scorer per-turn PRINT DEADLINE     3 of 16 (18.8%)  0 of 21
  level-4 brownfield     scorer per-turn PRINT DEADLINE     5 of 12 (41.7%)  0 of 12
```
⛔⛔ **THE TWO GREENFIELD ROWS ARE DIFFERENT INSTRUMENTS ANSWERING DIFFERENT QUESTIONS, AND THEY BOTH
ROUND TO 19%.** `done_reason` answers *"was this cell KILLED by the controller?"*; the scorer answers
*"were any of this cell's TURNS cut by the 1,800 s print deadline?"* A cell can be cut on several turns
and still land.

⚠️ **THE CONFLATION ORIGINATES IN THE FREEZE, WHICH IS MINE, NOT IN THE HAND'S READING OF IT.**
`AMENDMENT-…-level4-2026-09-13.md` reports greenfield's wall-clock incidence **twice, in two sections,
from two instruments, under one name**: §L0's table gives `TURN-TIMEOUT 4 ... 19% of the treatment arm`
(`done_reason`), while §L5 rule 2 speaks of *"its three truncated cells, all of which were also
salt-diet"* (the print deadline) **and calls that cell a "TURN-TIMEOUT cell" in the same sentence.**
Nothing in the freeze says these are different measurements. The hand read §L0's 19% as the comparable
prior, which is the only thing the freeze let it do.
⇒ 🔑 ***A NUMBER IS SAFE TO QUOTE ONLY IF ITS INSTRUMENT TRAVELS WITH IT, AND A FREEZE THAT GIVES ONE
NAME TO TWO INSTRUMENTS GUARANTEES THE MISQUOTE IT WILL LATER BE USED TO DIAGNOSE.***
✅ **THE HAND'S CONCLUSION SURVIVES ITS OWN CITATION.** Like-for-like on one instrument, the incidence
is higher in level-4 than in greenfield (41.7% vs 18.8%).
⛔ **THIS IS NOT A TREND.** Different fields, different and unbalanced denominators (greenfield's 16
includes `-stmt` variants at n of 1, 2 and 3 per condition; level-4's 12 is balanced 3 per condition).
✅ **WHAT IT IS, AND IT IS WORTH MORE THAN A TREND: THE SAME SIGN IN TWO WAVES, ON ONE INSTRUMENT —
ALL TRUNCATION ON THE TREATMENT ARM, NONE ON THE CONTROL, TWICE.** §L9 item 5 registered exactly this
possibility before the data: the greenfield incidence *"is not a prediction of the brownfield rate, and
if the brownfield rate differs that is a result about the field."* It differs.

### 📌 THE REMEDY HAD ALREADY BEEN APPLIED, AND THE ASYMMETRY OUTLIVED IT
`ctl/built-from.tsv`, verbatim: `print_timeout 1800s (per-TURN wall clock. The old 300s default
truncated 5 of 5 salt-diet cells and 0 of 3 plain ones: a cap that binds one arm is a treatment, not a
default.)` **The cap was already raised six-fold as the fix for this exact asymmetry, and at 1,800 s the
asymmetry is 41.7% against 0%.** Beside it in the same file: `max_wall ... Arm-correlated by
construction: plain 738-798s, salt-diet 3635-13700s.`
⇒ **The remedy moved the cap; it did not remove the treatment.** §L4 held the caps constant and made the
incidence a reported quantity, which is why this is readable at all.
⛔ **§L5 rule 5 governs the disposal: an arm-correlated cut is decided by its SIGN.** Every truncated
cell is a treatment cell, and dropping them would flatter the control. **None is dropped.**

---

## §R8 · WHAT THIS RESULT DOES NOT ESTABLISH (§L9, restated against the data that arrived)

1. **`k = 1`.** One planted defect per problem, four problems, chosen by this desk on a kill-margin
   criterion. **Not a sample of the defects real code has.**
2. **No magnitude, no ratio, no confidence claim.** Sign only, until a variance pilot re-derives the
   floor from a brownfield sigma. **No USD anywhere** (§L5 rule 7).
3. **A cost premium and a V1 rate are two results** and must never be joined with "and therefore".
4. **`bugs_introduced = 0` is a FLOOR, never a zero** — suite-limited, and the withheld suites read
   1.000 against mutants authored beside them, which is a CEILING and not a strength.
5. **n = 3 per condition, 12 per arm.** At these n the design resolves only a very large effect; the
   sign is what is reported, and nothing here is a significance claim.
6. **One vendor, one model** (`gemini-3.1-pro-high`). Nothing here transfers to another client.
7. **The 5 truncated salt-diet cells make every treatment-arm cost figure a FLOOR**, so no wall-clock or
   token comparison between the arms appears in this file at all.

---

## §R9 · WHAT IS OWED, WITH OWNERS

```
  1  the pooling check must hash W1 or the `customer` root commit, not the working tree   bench
  2  the pooling check must run ACROSS arms, not only within a root                       bench
  3  ADDENDUM 4: name the two wall-clock instruments apart in the freeze                  bench (below)
  4  `exec-registry` row for the wave driver: retire + the `ended` hook patch             gemini
  5  the §L10 variance pilot (top one condition 3 -> 9) remains an OPTION, ungated        the council
```
⛔ **Item 3 changes NO cut, NO threshold and NO verdict in this file.** It renames two instruments that
the freeze already used, and it is written AFTER the data and declared as such, so that it cannot be
read as retro-fitting. Every number in §R7 is reproducible from the receipts named there.


---

# ⛔⛔ ADDENDUM 1 — **12 OF THE 24 CELLS ARE VOID FOR THE FIND-THE-DEFECT CLAIM: THE FreeList AND LZW GIVENS ANNOUNCED THEIR OWN PLANTED DEFECT**
## bench (lead), 2026-09-15. **Nothing above is rewritten.** The measurements stand as taken; what
## changes is what they are measurements OF. LRU and Paxos are unaffected and are not in doubt.

## §V1 · THE DEFECT IN THE GIVENS
Two of the four brownfield givens named their planted defect in plain English, on or beside the defect
line, and were committed that way for roughly **57 hours** — a window that contains this wave.
```
  FreeList/brownfield/solution.rs:115   self.head = h0;   // MUTATION: the released block is
                                                          // never published
  LZW/brownfield/solution.rs:83         // is one lower than it should be.
```
FreeList's is the mutant generator's own inline marker, never stripped. LZW's is the orphaned second
line of a two-line tell whose first line was cut, sitting directly above the defect. **A cell built on
either given cannot measure whether a subject FINDS the defect, because the given tells it.**

## §V2 · CONFIRMED AT TWO DIFFERENT OBJECTS BY THREE PARTIES, WITH A CONTROL
```
  gemini · systems   read the tells IN EXPORT COMMIT ecd3924 — the export all 24 cells ran from
  bench (lead)       read each cell's OWN FIRST COMMIT, i.e. the given as the subject received it,
                     before the subject touched anything:
      FreeList  b4fp01 b4fp02 b4fp03 b4fs01 b4fs02 b4fs03   "MUTATION:"                     6 of 6
      LZW       b4lzp01-03 b4lzsb01-02 b4lzs01  "is one lower than it should be"             6 of 6
  CONTROL            LRU b4lrp01-03 · Paxos b4pp01-03, the same two literals                0 of 6
```
⇒ **The control discriminates, which is what makes this a measurement rather than an artefact of the
search string.** Two routes, two objects, one answer, and a control that could have cleared it and
did not.

## §V3 · ⚖️ THE RULING, AND THE VOID IS SCOPED RATHER THAN TOTAL
**The 12 FreeList and LZW cells are VOID for any claim about whether a subject FINDS a planted defect.**
The 12 LRU and Paxos cells **STAND**.
⛔ **What dies is the FINDING half only.** Whether those 12 cells say anything about *fixing an
already-named defect* is a DIFFERENT question from the registered one, and **it is not rescued by being
interesting** — it would need its own registration, written before looking at the data.
⇒ **Do not re-read those cells as a weaker version of this result. Read them as answering a question
nobody asked.**

## §V4 · ⛔ THE AUDIT CERTIFIED IT, WHICH IS WHY NOBODY LOOKED AGAIN
The strip was audited with `grep -E 'WRONG|MUTANT|<name>|reference'`, which returns **clean on all four
givens, including both compromised ones** — because **`MUTANT` is not a substring of `MUTATION`**.
⇒ 🔑 ***A VOCABULARY-KEYED AUDIT TESTS THE VOCABULARY YOU THOUGHT OF, AND A TELL IS WRITTEN BY
SOMEONE WHO WAS NOT THINKING OF YOUR LIST.***
⛔ **And the clean report did not merely fail to catch the tell — it CERTIFIED it**, which is worse: an
absence reported as an assurance is what stops the next person looking.
✅ **The form that would have caught it:** audit a stripped given by reading the diff against the
unstripped mutant, or by asserting the given contains no comment on or adjacent to the defect line —
**a structural test, not a word list.**

## §V5 · WHAT THIS ADDENDUM DOES NOT DO
1. It does not re-fire anything. Re-firing 12 brownfield cells is a SPEND and is the Captain's.
2. It casts no doubt on LRU or Paxos, and none on the instrument findings of §R4–§R7, which are about
   the harness and do not depend on the givens' content.
3. It makes no claim that any subject DID read the tell — only that the cells cannot distinguish a
   subject that found the defect from one that was told. **That is the whole point: the cell lost the
   ability to answer, whatever any individual subject did.**
