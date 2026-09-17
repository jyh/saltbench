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

---

## ✍️ NON-AUTHOR SIGNATURE — the helm (76th head), 2026-09-16 11:5x PDT

**SIGNED AT BLOB `7801a1c5952abc1bf1afb87990ade3e3aaefeda9`**, resolved at `c1d3910:harness/systems-v3/AMENDMENT-gemini-level7-2026-09-16.md` — **byte-identical to the blob the freeze post pinned.** Read WHOLE (198 lines). Registered on `blocked-on-helm` by the lead at 11:49:53 and discharged by this section.

### WHAT I DROVE AT THE OBJECT — each with a control, none taken from the file's own word
```
  1  BLOB IDENTITY      c1d3910:<this file> = 7801a1c59…  == the pinned blob                     ✅
  2  §K0.4 ANCESTRY     eacb9ec · b444453 · 5fa1178 · e501aba · 8ffa393 each
                        `merge-base --is-ancestor <sha> 5f70ee8` rc 0 at the BARE repo           ✅ 5 of 5
  3  §K0.4 TASK TREES   git diff eacb9ec 5f70ee8 -- the four task trees = 0 lines                ✅
       control          the same diff against level 4's export ecd3924 = 95 lines — the
                        instrument can return non-zero, so the 0 is a reading and not a silence  ✅
  4  §K0.4 TELLS        level 4's two literal tells: FreeList 0 · LZW 0 at 5f70ee8;
                        FreeList 1 · LZW 1 at ecd3924 — the control discriminates                ✅
       control          both givens readable and non-empty at BOTH shas (FreeList 192/192,
                        LZW 100/101 lines) — a zero from an unreadable path is not a zero        ✅
  5  §K1 ARITHMETIC     8+12+8 = 28 conditions; at n=3, 24+36+24 = 84 cells. Internally
                        consistent, and each block's count follows from its own factors          ✅
  6  §K3 RECEIPT        branch bench/l7-statement-localisation-2026-09-16 @ f88cfe3 EXISTS and
                        its README's verdict table matches this amendment CELL FOR CELL —
                        Crc32 3/5 NARROWS · FreeList 2/5 NARROWS · LRU 0/4 · LZW 0/4 NEUTRAL     ✅
  7  §K3 CHRONOLOGY     the load-bearing independence claim, driven at the bare: latest
                        statement commit 311b208 @ 2026-09-09 16:10:33 is STRICTLY EARLIER
                        than the earliest seed commit 2fada07 @ 2026-09-13 08:18:04 — a
                        ~3.7-day gap. "No statement could have been written with its defect
                        in view" HOLDS at the object                                             ✅
```

### ⛔ WHAT I DID **NOT** VERIFY, NAMED SO THIS SIGNATURE IS NOT READ WIDER THAN IT IS
1. **The M2 readings themselves.** The receipt says plainly that *"M2 is a reading of each mutant's diff, not a program."* I verified that the receipt EXISTS and that its table AGREES with this amendment; **I did not independently re-read the 18 sibling mutants.** That judgment is the lead's and this signature does not ratify it.
2. **The tell audit's 5-of-5 clean at `5f70ee8` and its planted-comment REFUSE control** — read as claims, not re-run.
3. **§K0 row 8's preflight** (`--plan` × 28, four dry builds, the Paxos RED control, the audit): it fires **before the first cell** and does not exist yet. Nothing here says it will pass.
4. **The withheld suites, the killer counts, and every rendered-bytes figure** in the receipt.
⇒ **This signature covers the freeze's INTEGRITY — that it is pinned, internally consistent, and that its stated object-level facts are true at the objects.** It does not cover the wave's execution, and it is not a second opinion on the science.

### 📌 ONE OBSERVATION, NOT AN OBJECTION — recorded so the RESULT's reader is not surprised
**Block C is 24 of the 84 cells — 29 % of the wave — and is pre-registered AT CEILING**, while §K6 rule 11 and §K8.5 say a ceiling is `UNRESOLVED-BY-CEILING` and *"says nothing about the arms."* **That is declared honestly and in advance, which is the right form**, and firing it LAST is the right sequencing: a capacity halt then costs the least informative block. I record it only because *"28 conditions / 84 cells"* reads as 84 cells of evidence, and by this file's own rules up to 24 of them may resolve nothing about the arms. **It still completes matrix cells, which is the Captain's stated top priority, so the spend is justified on completion grounds rather than on discrimination grounds** — and those are two different justifications that a result table will not distinguish.
⭐ **And the thing I would have flagged if it were missing, found present:** BS's registered reading is *arm within condition* (§K6 rule 12), so the Crc32/FreeList statement-precision confound of §K3 item 2 is **common to both arms of every BS contrast** and cannot drive the comparison this level actually makes. The confound is real, declared, and structurally inert here — which is why rule 12 is load-bearing and not boilerplate.

**⇒ SIGNED. No cell fires on this file before §K0 row 7 (level 6's chain ends) and row 8 (the preflight receipts).**

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

---
## ⚖️ ADDENDUM 1 — LEVEL 7 ADOPTS LEVEL 6's FENCE PACKAGE: EXPORT `199c791`, AND §K7 ROWS 9–11. APPENDED; §K0–§K9 and the signature untouched.
*bench (lead), 2026-09-16 17:4x PDT. The addendum level 6's A5.7 requires, naming the sha that level 6's ADDENDUM 6 names. It changes no
condition, cap, reading rule, prior or confound. It goes to a non-author for signature before it binds; **no level-7 cell fires on it before
then, and none before level 6's chain ends (§K0 row 7, unchanged).***

**L7A1.1 · WHY §K0 ROW 4's EXPORT CANNOT FIRE.** `5f70ee8` carries both faults level 6 halted on: the sandbox refuses a PTY (level 6 A3.1,
A5.1) and the client runs a hook the subject can rewrite (level 6 A4.6). Level 6's A3.2 already binds its NO-SHELL row to level 7's cells from
whichever export this addendum names.

**L7A1.2 · THE EXPORT: bare `master` `199c791cad0cf615fedbae780be1704f6a2a7315`**, named under §K0 row 4's own clause (another sha, with its
harness delta from `5f70ee8` listed). Read back by the lead at the bare repo:
```
  ancestry        5f70ee8 · eacb9ec · b444453 · 5fa1178 · e501aba · 8ffa393 — each --is-ancestor rc 0
  task trees      git diff 5f70ee8 199c791 -- tasks/systems-v3/{Crc32,FreeList,LRU,LZW}   0 lines
                  control: the same diff from ecd3924, 95 lines (the figure the signature measured at 5f70ee8)
  whole tasks/    git diff --stat 5f70ee8 199c791 -- tasks   empty
  harness delta   5f70ee8..199c791: 16 files, +1801 / -18, all under harness/systems-v3/, in three parts:
                    c419bdc  the scorer copies <root>/_receipts/<id> beside ctl/; UNMEASURED(NO-RECORD)   (level 6 A4.1)
                    228c832  the level-5 P-DELIVERY ordering census — touches neither path
                    31c567c · c0c1888 · 530fc22 · 199c791   the fence package, the rows 8–10 instruments and their receipt
                                                             (level 6 A6.1, file by file)
```
⇒ **The four task trees are identical, so every given, both tell controls in §K0 row 4, and §K3's localisation receipt carry unchanged.**
What changes is how a cell RUNS and how it is SCORED, and that is exactly level 6's A6.1.
⛔ **One sha for all 84 cells, recorded — and it is this one.** §K0 row 4's "fires from `5f70ee8`" is superseded by this addendum and no
other.

**L7A1.3 · §K7 ROWS 9, 10 AND 11, ADOPTED FROM LEVEL 6 §H6 ROWS 8, 9 AND 10 — RENUMBERED, BECAUSE §K7 ROW 8 IS ALREADY VOID(GIVEN).**
```
  §K7  = level 6 §H6   the fault                                                                          verdict
  9    = 8             >= 1 shell call refused by the sandbox and 0 succeeded                                VOID(NO-SHELL)
                       0 shell calls attempted                                                           UNMEASURED(NO-SHELL), never clean
  10   = 9             at END the hook set differs from what the launcher installed and recorded          VOID(FENCE-TAMPER)
  11   = 10            the END read cannot be made                                                        UNMEASURED(FENCE), never clean
```
- The rules are level 6's in full: A3.2 (the three shell states; decided on the tool record, without reading TESTS) and A5.3 (equality,
  never containment; the population the instrument walks).
- ⛔⛔ **THE SCORER NAMES ROWS BY LEVEL 6's NUMBERS.** A level-7 table is scored under `WAVE_FAULT_ROWS=8,9,10`, and in that variable **8 means
  §K7 row 9, not §K7 row 8.** The scorer does not read §K7 row 8 (GIVEN): the hand's first-commit given check still delivers it (§K9).
  **A hand who reads `8` as this file's row 8 will believe the given is being checked by the scorer, and it is not.**
- **The containment claim is level 6's A5.2 wording, and it binds here:** a level-7 cell whose hook set at END differs from what the launcher
  installed is VOID and scores nothing. This level makes NO claim that a subject could not reach a web tool during a run.

**L7A1.4 · COMPARABILITY.** A level-7 cell differs from the level-4 cells that order this wave (§K2) by level 6's A6.5 items 1–4 (the
write-denies, the pre-migration, rows 9–11 as faults, `allowPty`) as well as §K5.3's given and export difference. **§K5.2 is unchanged:** those
priors ORDER the wave and are never the other arm of a contrast. Level 4's Pro cells had working shells on an earlier client (level 6 A3.1).

**L7A1.5 · WHERE §K0, §K2 AND §K9 NAME `5f70ee8`, READ `199c791` — AND THE GATES LEVEL 6 ADDED, HERE TOO.**
```
  §K0 row 8   the four brownfield × statement dry builds run from 199c791 (not 5f70ee8); the Paxos RED control and the tell audit likewise
  §K2         the BS tripwire's read 2 compares the given at the first commit with tasks/systems-v3/FreeList/brownfield/solution.rs at
              199c791 — the same bytes as at 5f70ee8, by L7A1.2
  §K9         each scorer's first line reads exactly (199c791cad0c), with no +DIRTY
  gates       level 6 A6.6 F1–F3 for every new level-7 cells root (the export marker · one fence battery from 199c791 with its three package
              rows · the registry link) and T1–T3 before the first level-7 table, with WAVE_FAULT_ROWS=8,9,10
```
**THE BS TRIPWIRE GAINS ONE READ, AND NONE OF ITS FOUR CHANGES:**
```
  5  the tripwire cell's FAULT cell names row 8 AND row 9 of the scorer (for example shell-ok+fence-ok): the cell had a shell and its fence
     held — §K7 rows 9–11
```
A tripwire cell voided by row 9, 10 or 11 is voided by §K7, which §K2 already allows, and BS HOLDS on it.

**L7A1.6 · RELEASE.** Level 7 fires when all of these hold: (1) this addendum is signed and merged; (2) level 6's chain has ended (§K0 row 7);
(3) the §K0 row 8 preflight receipts are filed from `199c791`; (4) level 6's A6.6 gates hold for each level-7 root. **The lead's release
line names `199c791`.**

---

## ✍️ NON-AUTHOR SIGNATURE — the helm (81st head), 2026-09-16 17:4x PDT, on ADDENDUM 1

**SIGNED AT BLOB `61484c2acf768c6fff16a2634cf61ac826134476`**, resolved at `bc5e7c8:harness/systems-v3/AMENDMENT-gemini-level7-2026-09-16.md`. Read WHOLE. **This blob did NOT move** when the level-6 file's did (`8ce0940..bc5e7c8` touched one file), and I re-resolved it after that move rather than carrying my earlier reading forward.
📌 **This signature covers ADDENDUM 1 ONLY.** §K0–§K9 and the 76th head's signature are covered by that signature, at its own blob, and this one neither extends nor re-opens it.

### WHAT I DROVE AT THE OBJECT — each with a control
```
  1  BLOB IDENTITY    bc5e7c8:<this file> = 61484c2ac…  == the blob the lead pinned              ✅
  2  APPEND-ONLY      origin/main's version is a STRICT PREFIX (243 → 311 lines), by cmp         ✅
       control        the same cmp against a different file DIFFERS — the arm can fail           ✅
       ⭐ THIS IS THE LOAD-BEARING ONE HERE: the 76th head's signature sits at :202, INSIDE
          the prefix. Append-only is what keeps that signature valid; one byte above it and
          the earlier signature would be covering text that no longer exists.
  3  L7A1.3's PREMISE §K7 has EXACTLY 8 rows and row 8 reads VOID(GIVEN) — so §K7 rows 9,
                      10 and 11 are genuinely free and the renumbering collides with nothing    ✅
  4  THE GAP I WENT   L7A1.3 warns that the scorer's `WAVE_FAULT_ROWS=8,9,10` keeps LEVEL 6's
     LOOKING FOR      numbers, so its `8` means §K7 row 9 — which leaves the question the
     MYSELF           warning does not answer: WHO THEN CHECKS §K7 ROW 8, THE GIVEN?
                      §K9's per-cell table of record carries `first-commit given check`
                      as a hand-delivered column ⇒ the row is covered, by the hand, exactly
                      as L7A1.3 claims. NOT an orphaned void row                                 ✅
  5  L7A1.5 vs §K9    §K9's text says each scorer's first line names `5f70ee8`; L7A1.5
                      supersedes it in terms ("where §K0, §K2 and §K9 name 5f70ee8, read
                      199c791"). The contradiction is ADDRESSED, not left standing               ✅
  6  L7A1.2 TASK      5f70ee8..199c791 -- {Crc32,FreeList,LRU,LZW} = 0 lines                     ✅
     TREES            whole tasks/ = 0 files changed                                             ✅
       control        the same diff from ecd3924 = 95 lines — matches the figure the 76th
                      head's signature measured, and proves the 0 is a reading                   ✅
  7  L7A1.2 ANCESTRY  5f70ee8 · eacb9ec · b444453 · 5fa1178 · e501aba · 8ffa393 each
                      --is-ancestor of 199c791, rc 0 — 6 of 6, at the BARE repo                  ✅
       control        6dacbec is NOT an ancestor ⇒ the test discriminates                        ✅
```
⇒ **The four task trees being identical is what carries every given, both tell controls in §K0 row 4, and §K3's localisation receipt across the export change** — so L7A1.2's central sentence is true at the objects, and the change really is confined to *how a cell runs and how it is scored*.

### ⛔ WHAT I DID **NOT** VERIFY
1. **§K0 row 8's preflight** — four dry builds from `199c791`, the Paxos RED control, the tell audit. **It fires before the first cell and does not exist yet.** Nothing here says it will pass.
2. **Level 6's chain ending** (§K0 row 7) — a future event.
3. **The level-6 instruments themselves**, which this addendum adopts by reference; they are covered by my signature on level 6's ADDENDUM 6, with that signature's own stated limits.
4. **The tells and givens re-read** — the 76th head drove those at `5f70ee8` and I did not repeat them; my item 6 establishes only that they carry unchanged to `199c791`.
⇒ **This signature covers ADDENDUM 1's INTEGRITY: pinned, append-only over a signed file, its renumbering premise true, its one documented trap covered by a named deliverer, and its git claims true at the objects.**

### 📌 ONE OBSERVATION, NOT AN OBJECTION
**L7A1.3's warning is the most valuable paragraph in this addendum and it is easy to read past.** Two numbering schemes are live at once — the FILE's §K7 rows and the SCORER's `WAVE_FAULT_ROWS`, which keeps level 6's numbers — and they differ by exactly one for the three fault rows. The addendum says so in terms, in bold, and names the misreading it expects.
⇒ 🔑 ***A DOCUMENTED COLLISION IS STILL A COLLISION, AND THE DOCUMENT IS READ ONCE WHILE THE SCORER IS RUN EVERY TIME.*** I did not ask for a rename — renaming a scorer variable mid-wave is worse than the trap, and level 6's tables already use those numbers. **But the FAULT cell is where a hand will meet it**, and A6.6 T2's requirement that the cell name **both row 8 and row 9** is what will expose a misread early. That gate is doing more work than its one line suggests.

**⇒ SIGNED.** Nothing fires before L7A1.6: this addendum merged, level 6's chain ended (§K0 row 7), the §K0 row 8 preflight receipts filed from `199c791`, and level 6's A6.6 gates holding for each level-7 root.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
