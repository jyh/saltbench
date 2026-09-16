# AMENDMENT — agy LANE **LEVEL 7**: brownfield on the REPAIRED givens, and brownfield × statement, FROZEN BEFORE ITS FIRST CALL
## bench (SaltBench lead), 2026-09-16. Desk row **MR**. Released by council 2026-09-16 ③a: *"yes, accept all recs"* —
## (a) **discriminating conditions go into the DESIGN targets**, the arXiv-update gate unchanged; (c) **level 7's brownfield
## re-fires are authorised**. A runner seat `gemini` is the HAND; **bench is lead — design, caps, scoring rules, amendments.**
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** No cell fires on this file before that signature is appended below.
## ⛔ **AND NOT BEFORE LEVEL 6's CHAIN HAS ENDED** (§K0 row 7).

---

## §K0 · ⚖️ THE INPUTS, IN ONE BLOCK SO THE HAND NEEDS NOTHING ELSE
```
  1  MODEL IDs      gemini-3.1-pro-high (Pro conditions) · gemini-3.8-flash-high (Flash conditions) — level 6's pair.
                    Re-assert served at launch; a served-model mismatch VOIDS (§K7 row 1).
  2  n              3 per condition.
  3  POPULATION     28 conditions, 84 cells (§K1). Nothing is added, dropped or substituted.
  4  EXPORT         bare master 5f70ee8e2d73 — LEVEL 6's EXPORT, UNCHANGED. Read back by the lead at the bare repo:
                      ancestry     eacb9ec · b444453 (FreeList + LZW given repair, tell audit) · 5fa1178 (Crc32 given) ·
                                   e501aba (Crc32's third tell) · 8ffa393 (P-DELIVERY closure) — each --is-ancestor rc 0
                      task trees   git diff eacb9ec 5f70ee8 -- tasks/systems-v3/{Crc32,FreeList,LRU,LZW} = 0 lines
                      the tells    level 4's two literal tells (ADDENDUM 1 §V1) occur 0 and 0 times in the FreeList and
                                   LZW givens at 5f70ee8, and 1 and 1 times at ecd3924 — the control discriminates
                    It carries the P-DELIVERY repair and the end-of-cell token scan (level 6 ADDENDUM 2).
                    ⛔ If bare master moves before the first cell, level 7 STILL fires from 5f70ee8, unless an addendum
                    names another sha with its harness delta from 5f70ee8 listed. One sha for all 84 cells, recorded.
  5  FIRE ORDER     by expected discrimination (§K2), under the council's any-503 rule. Inside a block: Pro before
                    Flash, plain before salt-diet, so a halt on capacity leaves whole PAIRS (the hand's level-6 default,
                    adopted). Block BS opens with ONE tripwire cell (§K2).
  6  USAGE          `gemini` reads agy /usage at each fire and bank (council 09-16 ③b); bench consumes it.
  7  SEQUENCING     one agy supervisor at a time on the one Google pool: level 7 fires AFTER level 6's chain ends.
  8  PREFLIGHT      zero spend, before the first cell, receipts filed: `--plan` reads clean for all 28 conditions
                    (roots absent, helper deployed, canary healthy) · ONE dry build at 5f70ee8 of a brownfield ×
                    statement cell per problem (Crc32, FreeList, LRU, LZW), each rc 0 with `## Statement` rendered ·
                    RED control: Paxos × statement REFUSES (neutrality) · the tell audit reads 5 of 5 clean at 5f70ee8.
```

---

## §K1 · THE POPULATION — 28 CONDITIONS, 84 CELLS
```
  block  problem          field        arms                                       models          conditions   cells
  BN     FreeList · LZW   brownfield   plain-bare · salt-bare                     Pro · Flash          8          24
  BS     FreeList · LRU   brownfield   plain-stmt · salt-stmt                     Pro · Flash         12          36
         · LZW
  C      Crc32            brownfield   plain-bare · salt-bare · plain-stmt ·      Pro · Flash          8          24
                                       salt-stmt
                                                                                             TOTAL    28          84
```
**WHY THESE 28:** every owed agy brownfield condition that needed the given repairs to land, and nothing that needs a
harness build. Greenfield spec-change is level 8.
- **BN re-measures FreeList and LZW on the REPAIRED givens.** Level 4's 12 cells on those two problems are VOID for the
  find-the-defect claim (level-4 ADDENDUM 1 §V3): their givens named the planted defect. **BN is a NEW condition set, not
  a re-fire of those cells**, and its cells are never pooled with them.
- **Paxos × statement is inexpressible:** a proof-obligation task has no arm-neutral statement, and the builder refuses it
  (a lead's dry build at `eacb9ec`, 2026-09-16: REFUSE rc 4, neutrality). **Pro brownfield LRU and Paxos are DONE** (level 4),
  and **Flash brownfield LRU and Paxos** are level 6's block B.

**ARM → FLAGS** (`cell_build.py --client agy --budgets pricing --field brownfield --phase 1`):
```
  plain-bare   --arm plain                         salt-bare   --arm salt-diet
  plain-stmt   --arm plain     --statement         salt-stmt   --arm salt-diet --statement
```
⛔ **`--arm salt-diet`, NEVER `--arm salt`.** ⛔ **`--hint` is not used.**

---

## §K2 · ⚖️ THE DISCRIMINATING TARGET — COUNCIL ③a(a), APPLIED PER BLOCK, BEFORE ANY DATA
**Each expectation cites a result of record, and says so when the record is about a different condition.** None is a
prediction of an arm contrast.
```
  order  block  expectation          prior
  1      BN     VARIES (retention)   DIRECT, on the same two problems — Pro level 4, pre-repair: RETAINED plain 0.621-0.990,
                                     salt-diet 0.137-0.523; withheld FreeList plain 7/7 x3, salt-diet 3/7 · 3/7 · 7/7
                                     (RESULT-gemini-brownfield-level4-2026-09-14.md §R1). ⛔ Those cells are VOID for the
                                     find-the-defect claim and ORDER this wave only.
  2      BS     VARIES — BORROWED    NO brownfield × statement cell has ever run. Borrowed from brownfield-none retention on
                                     these problems (level 4 §R1, §R3) and from Pro LZW GREENFIELD statement: salt-diet +
                                     statement VERIFIED 1/5 while LANDING 5/5 (RESULT-agy-lzw-statement-2026-09-11.md §2b).
  3      C      AT CEILING           Registered weak: "Crc32 IS A WEAK BROWNFIELD TASK AND THAT IS A PROPERTY OF THE TASK"
                                     (AMENDMENT-brownfield-2026-09-13.md, ADDENDUM 3) — and §K3 item 3.
```
⛔ **A BORROWED PRIOR ORDERS THE WAVE AND PREDICTS NOTHING.** Level 6's freeze nearly carried a prior borrowed from other
problems where a measurement of the right one existed (its §H2). Here none exists, and BS's row says so rather than
dressing an analogy as an expectation.
⛔ **A CEILING IS NOT PARITY.** A condition whose cells all pass is recorded **UNRESOLVED-BY-CEILING** on pass rate.
⛔ **LANDED IS NOT VERIFIED.** Every rate is scored against the withheld suite; a self-graded landing is never quoted.

**⚡ BS's TRIPWIRE — ONE CELL, READ BY THE LEAD BEFORE THE OTHER 35.** The block's first cell is **Pro · FreeList ·
salt-stmt, n=1** — the treatment arm (level 4 §L7: the tripwire sits on the arm most likely to break), on the problem
whose level-4 separation was widest. The hand posts its receipts and **stops the chain**; the lead reads:
```
  1  REQUIREMENTS.md carries a `## Statement` section · ctl/field = brownfield · ctl/card_extras = statement
  2  the given at the cell's FIRST commit is byte-identical to tasks/systems-v3/FreeList/brownfield/solution.rs at 5f70ee8
  3  a token-scan receipt exists and classifies no LEAK · the served model is the Pro id
  4  the cell ENDED (any class) and its end marker is recorded verbatim
```
**All four read ⇒ the lead releases BS in one bus line.** Any row that does not read HOLDS the block; the tripwire cell
is voided only if §K7 voids it, and otherwise counts as cell 1 of its condition.

---

## §K3 · ⚖️ THE LOCALISATION QUESTION — ANSWERED BEFORE THE FREEZE, NOT AFTER THE DATA
**The question:** in a brownfield cell the statement is a formal spec of CORRECT behaviour sitting beside a planted
defect. Does it LOCALISE that defect — hand the subject a pointer that the no-statement condition lacks?
**The answer, measured read-only at `eacb9ec`: NO LOCALISATION.** Receipt: harness repo branch
`bench/l7-statement-localisation-2026-09-16` at `f88cfe3`, `harness/systems-v3/RECEIPT-l7-statement-localisation-2026-09-16/`
— in the harness repo because it reads withheld material, which this repository does not carry.
```
  problem    statement vs REQUIREMENTS.md on the violated property          defective fn weighted?   M2        VERDICT
  Crc32      states it more precisely                                        no                      3 of 5    NARROWS
  FreeList   states it more precisely                                        no                      2 of 5    NARROWS
  LRU        states it at the same granularity                               no                      0 of 4    NEUTRAL
  LZW        states it at the same granularity                               no (a shared helper)    0 of 4    NEUTRAL
```
**M2** = of each problem's sibling mutants, how many have a statement clause strictly more specific than REQUIREMENTS.md
on the property they break (18 mutants). **NARROWS** means the extra precision is UNIFORM — it covers sibling mutants
too, and the defective function carries no more statement than its neighbours (M1, bytes reachable per function).
**CHRONOLOGY:** every statement is a verbatim extraction from a withheld reference last changed 2026-09-04; statements
were committed 09-06 to 09-09; seeds were chosen 09-13 and 09-14. **No statement could have been written with its
defect in view.**
⛔ **THE TELL AUDIT CANNOT ANSWER THIS, BY CONSTRUCTION:** it reads `//` comment lines of the given only. Forced over the
statements it returns 4 of 4 clean — an empty result — while a planted comment tell in the same harness REFUSES (rc 1).
**M2 is the check for a spec-level pointer; the audit is the check for a comment-level one.** Both are filed.

**⇒ WHAT FOLLOWS, REGISTERED:**
1. **No statement is a tell: nothing is voided or excluded on this ground.**
2. **On Crc32 and FreeList the statement is more precise about the broken property than REQUIREMENTS.md.** That precision
   is the statement condition's own treatment, not a leak. It is declared beside any comparison of a BS or C-statement
   row with its no-statement neighbour — a comparison that is **not this level's registered reading** (§K6 rule 12).
3. **Crc32's given carries its REFERENCE's own doc comment stating the correct count, eight lines above the defect**
   (restored by `e501aba` when mutation residue was stripped). It is arm-neutral and the audit rightly passes it, but a
   Crc32 brownfield cell therefore measures fixing a comment–code disagreement the given displays. **Block C is registered
   AT CEILING and fires last.**
4. **Whether a subject USES the statement to find the defect is UNMEASURED** and this level claims nothing about it.

---

## §K4 · CAPS — CARRIED FROM LEVEL 6 §H3, UNCHANGED, AND THEIR INCIDENCE IS REPORTED
```
  token cap       T1_TOK 250,000,000
  per-turn        AGY_PRINT_TIMEOUT 1800s · controller patience AGY_TURN_TIMEOUT 2100s
  reporting       CAP-TOKENS, CELL-KILLED and TURNS-CUT are REPORTED as a split by arm, never a void
```
⛔ **Every truncation in level 4 was a salt-diet cell (5 of 12, 0 of 12 plain).** A cap that binds one arm is a treatment;
it is held constant so its incidence is readable.

---

## §K5 · ⛔⛔ THE CONFOUNDS — REGISTERED, AND THEY TRAVEL WITH EVERY TABLE
1. **TIER + GENERATION** (level 6 §H4.1): any Pro↔Flash difference names both axes, every time.
2. **DATE AND EXPORT versus the priors in §K2**: they order the wave, and are never the other arm of a contrast.
3. **BN's Pro cells versus level 4's Pro cells on the same problems are NOT a contrast.** The givens differ by exactly the
   tells that voided level 4's find-the-defect claim, and the exports differ (`ecd3924` vs `5f70ee8`).
4. **The agy fence lets the subject read its own `ctl/`** (level 6 §H4.4): carried; the per-cell `ctl/` read census is a
   reported column and no delivery claim is made from P-DELIVERY alone.
5. **P-DELIVERY** (level 6 §H4.5 and ADDENDUM 2 A2.2): carried in full, classes included.

---

## §K6 · THE READING RULES
**Level 4 §L5 rules 1–7 apply unchanged** (sign only; a truncated cell's result is a floor; landing and passing are two
rates; `bugs_introduced = 0` is a floor; an arm-correlated cut is decided by its sign; export sha recorded; no USD).
**Level 6 §H5 rules 9–10 apply unchanged** (verified first, with LANDED and `declared` as separate columns; retention is
the brownfield primary separator, per cell, never averaged across problems).
**11 A CONDITION AT CEILING IS UNRESOLVED-BY-CEILING** on pass rate, and says nothing about the arms.
**12 THE REGISTERED READING IS ARM WITHIN CONDITION.** A statement-versus-bare comparison across conditions is not
   registered here; if it is ever made, §K3 item 2 travels with it.
**13 FIND-THE-DEFECT IS REPORTED PER CELL** as `bugs_fixed` from the end tree against the registered planted defect —
   and it is a claim level 7 CAN make for FreeList and LZW, which level 4 could not.

## §K7 · WHAT VOIDS A CELL (faults only — no expectation from §K2 appears here)
```
  1  the served model differs from the condition's model id                           VOID
  2  the cell ends METER-BLIND / no readable T                                         VOID(UNPRICED)
  3  ctl/field or ctl/card_extras differs from the condition's flags                   VOID
  4  the fence battery does not pass for the cell's PATH                               DO NOT FIRE
  5  a 503 inside the cell                                                             DISCARD per the any-503 rule
  6  CAP-TOKENS · CELL-KILLED · TURNS-CUT                                              NOT void: reported per arm
  7  a LEAK-class token occurrence (level 6 ADDENDUM 2 A2.2); no scan receipt           VOID(TOKEN-LEAK) · UNMEASURED
  8  the given at the cell's first commit is not byte-identical to the export's given  VOID(GIVEN) — the cell did not
     for that problem                                                                  receive the registered given
```

## §K8 · WHAT THIS LEVEL CANNOT ESTABLISH, SAID BEFORE ANY DATA
1. **Anything about tier alone** (§K5.1). 2. **No magnitude** — sign only; no brownfield dispersion has been measured.
3. **No cross-lane comparison** in dollars or tokens. 4. **A cost result and a pass-rate result are two results.**
5. **A ceiling says nothing about the arms.** 6. **Nothing about whether a subject used the statement** (§K3 item 4).
7. **No contrast with level 4's FreeList/LZW cells** (§K5.3).

## §K9 · WHAT THE HAND DELIVERS, AND WHAT THE LEAD OWES AFTER
```
  one export sha across all 84 cells · the §K0 row 8 preflight receipts · the BS tripwire receipts, BEFORE BS continues ·
  per-condition score receipts as FILES, each scorer's first line naming 5f70ee8 · the per-cell table of record (arm ·
  problem · model · T · wall · turns · done_reason · end · verdict · tests · retention · rewrite class · bugs_fixed ·
  TURNS-CUT flag · declared · ctl/ read census · first-commit given check · token-scan class · source receipt) ·
  TURNS-CUT and CAP incidence as a SPLIT BY ARM · the /usage rows it logged
```
⇒ **The lead scores and writes the result of record, and RE-CUTS THE MATRIX CENSUS IN THE SAME COMMIT** (council 09-16 ⑤d).
Any public sentence, and any claim about the method, is the Captain's.
