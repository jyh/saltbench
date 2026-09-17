# AMENDMENT — agy LANE **LEVEL 8**: greenfield SPEC-CHANGE on both Gemini models, FROZEN BEFORE ITS FIRST CALL
## bench (SaltBench lead), 2026-09-16. Desk row **MR**. Released by council 2026-09-16 ③a: *"yes, accept all recs"* — (a) **discriminating
## conditions go into the DESIGN targets** for levels 6-8, the arXiv-update gate unchanged. A runner seat `gemini` is the HAND; **bench is
## lead — design, caps, scoring rules, amendments.**
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** No cell fires on this file before that signature is appended below.
## ⛔ **AND NOT BEFORE LEVEL 7's CHAIN HAS ENDED, NOR BEFORE §M0 ROW 4's EXPORT IS NAMED BY ADDENDUM** (it is PENDING, §M0 row 4).

---

## §M0 · ⚖️ THE INPUTS, IN ONE BLOCK SO THE HAND NEEDS NOTHING ELSE
```
  1  MODEL IDs      gemini-3.1-pro-high (Pro conditions) · gemini-3.8-flash-high (Flash conditions) — levels 6 and 7's pair.
                    Re-assert served at launch, per phase; a served-model mismatch VOIDS (§M8 row 1).
  2  n              3 per condition.
  3  POPULATION     20 conditions, 60 cells (§M1). Nothing is added, dropped or substituted.
  4  EXPORT         PENDING. A descendant of bare master 2419dcf (the phase-2 wiring, fast-forwarded 2026-09-16 17:45 PDT) that
                    ALSO carries §M3's phase-1 fault gate, named by a signed addendum with its harness delta from 2419dcf before the
                    first cell. 2419dcf alone does NOT qualify: it fires phase 2 on a phase 1 nobody has read (§M3).
                    One sha for all 60 cells and both phases, recorded.
  5  FIRE ORDER     by expected discrimination (§M2), under the council's any-503 rule. Inside a problem: Pro before Flash, plain
                    before salt-diet. The chain opens with ONE tripwire cell (§M2).
  6  USAGE          `gemini` reads agy /usage at each fire and bank (council 09-16 ③b); bench consumes it.
  7  SEQUENCING     one agy supervisor at a time on the one Google pool: level 8 fires AFTER level 7's chain ends.
                    Pro conditions fire only if level 6 has recorded at least one Pro cell reading SHELL-OK under the fence package.
  8  PREFLIGHT      zero spend, before the first cell, receipts filed: the export's run-box marker (level 6 A6.6 F1) · a DRY DRIVE
                    at the export of the real fire_agy + launcher + customer with a stub client (/bin/echo — the form the builder
                    drove at a3cd265), in two arms: (a) phase-1 records PLANTED to pass §M3 (a shell-ok stream and a fence-ok END
                    record) ⇒ customer -> aside -> phase 2 each reached, their receipts present; (b) a planted VOID(NO-SHELL)
                    stream ⇒ PHASE 2 NOT FIRED, said, no customer commit. A stub phase 1 alone makes no shell call, so it can
                    never pass the gate, and arm (a) without the plant would prove nothing · a `1,2` manifest aimed at the
                    199c791 export REFUSES before spend (the wiring probe's control).
```

---

## §M1 · THE POPULATION — 20 CONDITIONS, 60 CELLS
```
  models          problems                               field        arms                   extras     conditions   cells
  Pro · Flash     Crc32 · FreeList · LRU · LZW · Paxos    greenfield   plain · salt-diet      none           20          60
```
**WHY THESE TWENTY:** every agy greenfield × spec-change condition in the matrix, and all are OWED:
`CENSUS-full-matrix-2026-09-14.md` §C4 (`gemini-3.1-pro-high`: *"greenfield × {plain,salt-diet} × spec-change × 5 problems OWED 10"*) and
level 6's signature table (Flash *"OWED 32 = LZW 4 + brownfield 18 + spec-change 10"*). Brownfield × spec-change left the denominator by
the Captain's word (census ADDENDUM 1). Spec-change carries no statement or hint: `customer.sh` refuses a cell built with card extras,
because the change render would drop them (D7).

**THE FORM** (`agy_wave_v3.sh` with `AGY_PHASES=1,2`, `AGY_WIDE=1`, no `AGY_EXTRA`; built `cell_build.py --client agy --budgets pricing
--arm {plain|salt-diet} --field greenfield`):
```
  phase 1    a FRESH greenfield cell (F1) — no reused landing, because a reuse pool short on some conditions would correlate source
             kind with condition
  customer   only on a LANDED phase 1 that §M3 passes: customer.sh dispatch --fold-bus -> ONE commit as author `customer`
             (inbox/change-1.md · REQUIREMENTS.md re-rendered --change with the cell's own nonce · interface.rs <- B/interface.rs),
             tag P1, a ' dispatched P1 ' line in ctl/customer.log with the payload sha
  aside      phase 1's client home, tmp/ and every ctl/ file not on the KEEP list move to <root>/_aside/<id>/phase1 (F2), a root
             sibling the fence denies; recorded in ctl/aside-1.tsv
  phase 2    a fresh client state on the same repo; LANDED only if LANDING.md CHANGED since tag P1 (F3)
```
⛔ **`--arm salt-diet`, NEVER `--arm salt`.** ⛔ **`--hint` and `--statement` are not used, and the wave refuses them.**

---

## §M2 · ⚖️ THE DISCRIMINATING TARGET — COUNCIL ③a(a), APPLIED PER PROBLEM, BEFORE ANY DATA
**No agy spec-change cell has ever run.** Every phase-2 expectation below is BORROWED from the Claude lane, and says so. The phase-1
REACH expectation (§M4) is DIRECT, from this lane.
```
  order  problem    expectation (phase 2)       prior (result of record)
  1      Paxos      VARIES — BORROWED           Opus: plain 1/2, salt-diet 1/2, and a CAP-COST stop in EACH arm
                                                (RESULT-p1-specchange-2026-09-10.md §2, §3)
  2      FreeList   VARIES — BORROWED           Opus: plain 2/2, salt-diet 0/1 — n=1, which that file says is not a rate (§3)
  3      LZW        UNMEASURED — BORROWED       Opus: salt-diet 1/1 and no plain cell in that file's by-task table (§3)
  4      LRU        AT CEILING — BORROWED       Opus: plain 2/2, salt-diet 3/3 (§3)
  5      Crc32      AT CEILING — BORROWED       Opus: plain 3/3, salt-diet 3/3 (§3) · and its V2 is UNINFORMATIVE: a stub scores
                                                CLAUSE_TESTS 0/4 GREEN while failing 5 of 6 regressions (RESULT-p2-specchange-pair §4)
```
⛔ **A BORROWED PRIOR ORDERS THE WAVE AND PREDICTS NOTHING.** Those cells ran on another client under USD caps and a different watcher, on
REUSED phase-1 landings. ⛔ **A CEILING IS NOT PARITY:** a condition whose reached cells all pass is **UNRESOLVED-BY-CEILING** on pass rate.
⛔ **LANDED IS NOT VERIFIED:** every rate is scored against the task's `B/` suite; a self-graded landing is never quoted.

**⚡ THE TRIPWIRE — ONE CELL, READ BY THE LEAD BEFORE THE OTHER 59.** **Flash · LRU · plain, n=1.** It is chosen to REACH phase 2: the
mechanism under test is the chain, and a phase 1 that does not land exercises none of it. Level 5's three Flash LRU plain cells all LANDED
(RESULT-gemini-flash-level5-2026-09-15.md, per-cell table). The hand posts its receipts and **stops the chain**; the lead reads:
```
  1  phase 1 ended LANDED, and §M3's gate record reads shell-ok and fence-ok for phase 1
  2  ctl/customer.log carries ' dispatched P1 ' with a payload sha; tag P1 exists; ctl/aside-1.tsv exists
  3  phase 2 did NOT end on its opening turn: its turn count is > 1, or its end marker names a cap
  4  phase 2's end marker records declared-after-P1, and LANDED appears only with a LANDING.md changed since P1
  5  the phase-2 score (WAVE_PHASE=2 WAVE_FAULT_ROWS=8,9,10) prints TESTS, a REGRESSIONS line and a CLAUSE_TESTS line — none UNMEASURED —
     and its FAULT cell names row 8 AND row 9 for phase 2
```
**All five read ⇒ the lead releases the chain in one bus line.** Any row that does not read HOLDS it. The tripwire cell is voided only if
§M8 voids it; otherwise it is cell 1 of its condition.

---

## §M3 · ⛔⛔ THE PHASE-1 FAULT GATE — A BUILD ITEM, AND THE REASON §M0 ROW 4 IS PENDING
**Measured at `2419dcf`:** `agy_wave_v3.sh`'s `run_phase2` fires the customer and phase 2 on `end-1` reading LANDED, **with no read of phase 1's
fault rows between.** The aside then moves `stream-1.ndjson` out of the cell, and the scorer refuses a phase-1 score of a set-aside cell
(POST-ASIDE). ⇒ **As built, a phase 2 can fire on a phase 1 that had no shell or whose fence was tampered, and no instrument reads phase 1's
rows afterwards.** A phase 1 that reached the web through a rewritten hook hands its code, as the given, to phase 2.
**REQUIRED IN THE EXPORT, with red arms and a mutant that flips them:**
```
  when     in run_phase2, after end-1 reads LANDED and BEFORE the customer's dispatch — so before the aside
  reads    row 8 on ctl/stream-1.ndjson (agy_shell_count_v3.py --phase 1) · rows 9-10 on <root>/_receipts/<id>.fence-1, line 1
  records  both verdicts to a ctl/ file on the aside's KEEP list, so phase 2's scoring can cite them
  gate     phase 2 fires ONLY on phase 1 = shell-ok (any refusals reported) AND fence-ok.
           Anything else ⇒ "PHASE 2 NOT FIRED for <id>: phase 1 <row>", said, never silent, and no customer commit
```
⇒ **A cell stopped here is a FAULT ROW, not a reach loss** (§M4): the harness failed it, and it enters no reach denominator.

---

## §M4 · ⚖️ REACH — THE SELECTION EVERY PHASE-2 NUMBER CARRIES, REGISTERED BEFORE ANY DATA
**A phase 2 exists only on a phase 1 that LANDED and passed §M3.** So a phase-2 rate is a rate over the cells that REACHED phase 2, never over
all cells of the condition.
```
  REACH, per condition and arm =  cells whose phase 1 LANDED and passed §M3 AND whose customer dispatched  /  cells fired minus fault rows
```
**THE PRIOR IS DIRECT, AND IT POINTS AT ONE ARM:** Pro greenfield on this lane — plain 18 LANDED, 0 NOT-LANDED, 0 truncated; salt-diet 15
LANDED, 4 NOT-LANDED, 3 truncated, with salt-diet walls of 3,635–13,700 s against plain's 738–798 s (RESULT-p1-greenfield-2026-09-13.md §3).
Flash level 5: 20 of 21 LANDED, the one loss a salt-diet cell ending on a 400 (RESULT-gemini-flash-level5-2026-09-15.md §1).
⇒ **Registered:**
1. **REACH is printed beside every phase-2 rate, per arm.** A phase-2 arm contrast is between cells that reached phase 2, and is never read as
   the arms' spec-change performance on all cells.
2. **No top-up re-fires.** Re-firing a condition until it reaches 3 selects again on the same property. A condition with REACH < 3 is
   reported at the n it reached.
3. **A cell whose phase 1 did not LAND is not a phase-2 failure.** It is a REACH loss, with its phase-1 end kind named.
4. **The customer's dispatch can refuse** (a dirty tree beyond BUS.md). That is a REACH loss with its reason, reported per arm.

---

## §M5 · CAPS — PER PHASE, THE CAPS THE LANE ENFORCES (level 6 ADDENDUM 7), AND THEIR INCIDENCE IS REPORTED
```
  per phase       AGY_MAX_TURNS 40 · AGY_MAX_WALL 21600 s · AGY_PRINT_TIMEOUT 1800s · AGY_TURN_TIMEOUT 2100 s   (F4: phase 2 = phase 1)
  tokens          T is metered per phase and reported. NOT a cap: no agy-lane script enforces T1_TOK (level 6 A7.1)
  receipts        each wave's CAPS line, filed; a wave whose values differ is reported as such (level 6 A7.2)
  reporting       TURN-CAP · WALL-CAP · TURN-TIMEOUT · TURNS-CUT · CELL-KILLED per phase, as a SPLIT BY ARM — never a void
```
⛔ **WHICH ARM TRIPS THEM:** the wall cap in phase 1 decides REACH (§M4), and the prior says salt-diet meets it first. A cap that binds one arm
is a treatment; it is held constant so its incidence is readable, and the phase-1 wall incidence is part of REACH's reading.

---

## §M6 · ⛔⛔ THE CONFOUNDS — REGISTERED, AND THEY TRAVEL WITH EVERY TABLE
1. **TIER + GENERATION** (level 6 §H4.1): any Pro↔Flash difference names both axes, every time.
2. **BORROWED PRIORS** (§M2): the Claude lane's spec-change cells differ in client, caps, watcher and source (reused landings). They order
   this wave and are never the other arm of a contrast. **No level-8 number is compared with RESULT-p1-specchange.**
3. **REACH SELECTION** (§M4), carried by every phase-2 figure.
4. **THE FENCE PACKAGE** (level 6 ADDENDA 5–6) binds both phases: write-denies, pre-migration, `allowPty`, rows 8–10 per phase. The `ctl/`
   read deviation (level 6 §H4.4) binds phase 1. At phase 2 the aside has moved every unkept `ctl/` file out of the cell.
5. **P-DELIVERY PER PHASE:** phase 2 is scored with `briefing_verdict --phase 2`. The spawn-time uniqueness walk includes the git routes a
   phase-1 token can take into phase 2 (commit messages, deleted-file history, reflog). A git-route hit at END is SUBJECT-WRITTEN.
6. **THE BUS FOLD:** `--fold-bus` folds a phase-1 tree whose ONLY dirt is `BUS.md` into the customer's commit, and records the fold
   (measured before the build: 20 of 74 landed bare agy cells carried such an edit). **Reported per cell and split by arm**, because whether
   one arm leaves BUS.md dirty more often is unmeasured.

## §M7 · THE READING RULES
**Level 6 §H5 rules 1–10 apply per phase** (sign only; a truncated pass is a floor; landing and passing are two rates; an arm-correlated cut is
decided by its sign; `bugs_introduced` is a floor; export sha recorded; no USD; an unmetered cell is a row; verified first with LANDED and
`declared` as separate columns).
**11 V1 AND V2 ARE READ INDEPENDENTLY**, as `referee_v3.phase2_verdicts()` derives them: V1 GREEN iff REGRESSIONS failed = 0 · V2 GREEN iff
CLAUSE_TESTS failed = 0. **No pooled field is derived.** `TESTS` counts passes; REGRESSIONS and CLAUSE_TESTS count failures.
**12 CRC32's V2 IS REPORTED UNINFORMATIVE** (RESULT-p2-specchange-pair §4), never quoted beside V1 as evidence.
**13 PHASE-2 LANDED MEANS LANDING.md CHANGED SINCE P1**, with `declared-after-P1` beside it.
**14 REACH IS PRINTED BESIDE EVERY PHASE-2 RATE** (§M4).
**15 PHASE 1's WITHHELD-SUITE VERDICT IS NOT A LEVEL-8 READING.** The aside precedes any phase-1 score, so the scorer reads POST-ASIDE by
   construction. §M3's fault read is the only phase-1 record taken. The phase-1 half of a spec-change cell **completes no greenfield-none
   census condition and is pooled with no level-5 or level-6 cell.**

## §M8 · WHAT VOIDS A CELL (faults only — no expectation from §M2 appears here)
```
  1-5, 7    level 6 §H6 rows 1-5 and 7, applied PER PHASE
  6         TURN-CAP · WALL-CAP · TURN-TIMEOUT · TURNS-CUT · CELL-KILLED                             NOT void: reported per arm and phase
  8-10      level 6 §H6 rows 8-10 for PHASE 2, scored WAVE_PHASE=2 WAVE_FAULT_ROWS=8,9,10            as registered there
  11        phase 1 read by §M3 as anything but shell-ok + fence-ok                                  PHASE 2 NOT FIRED: a fault row
            — and if a phase 2 fired anyway                                                         VOID(PHASE-1-FAULT)
  12        ctl/customer.log has no ' dispatched P1 ' line, or tag P1 is absent, on a cell scored at phase 2   VOID(NOT-SPEC-CHANGE)
```

## §M9 · WHAT THIS LEVEL CANNOT ESTABLISH, SAID BEFORE ANY DATA
1. **Anything about tier alone** (§M6.1). 2. **No magnitude** — sign only at n ≤ 3. 3. **No cross-lane comparison**, in dollars, tokens or
rates (§M6.2). 4. **A phase-2 contrast is conditional on REACH** (§M4) and says nothing about the cells that did not reach phase 2.
5. **Nothing about phase 1's code quality** (§M7 rule 15). 6. **A ceiling says nothing about the arms.** 7. **A cost result and a pass-rate
result are two results.**

## §M10 · WHAT THE HAND DELIVERS, AND WHAT THE LEAD OWES AFTER
```
  one export sha for all 60 cells · the §M0 row 8 preflight receipts · the tripwire receipts, BEFORE the chain continues · each wave's CAPS
  line · per-condition phase-2 score receipts as FILES, each scorer's first line naming the export · the per-cell table of record:
    arm · problem · model · phase-1 end kind · §M3 gate record · dispatched (yes/no, reason) · fold-bus (yes/no) · payload sha ·
    per phase: T · wall · turns · done_reason · end · FAULT ·
    phase 2: TESTS (B/) · REGRESSIONS f/t · CLAUSE_TESTS f/t · LANDED (changed since P1) · declared-after-P1 · ctl/ read census ·
    source receipt
  REACH and cap incidence as SPLITS BY ARM · the /usage rows it logged
```
⇒ **The lead scores and writes the result of record, and RE-CUTS THE MATRIX CENSUS IN THE SAME COMMIT** (council 09-16 ⑤d). Any public
sentence, and any claim about the method, is the Captain's.

---

## ✍️ NON-AUTHOR SIGNATURE — the helm (81st head), 2026-09-16 18:0x PDT

**SIGNED AT BLOB `8cfcaaa73eb5b7348ce2ee14b5a17fae1666515e`**, resolved at `ea4ae5b:harness/systems-v3/AMENDMENT-gemini-level8-2026-09-16.md`. Read WHOLE.
📌 **This file is NEW on `main`, so unlike levels 6 and 7 there is no earlier signature underneath and append-only is not load-bearing here.** Stated because on those two files it was the FIRST thing I checked, and its absence here is a property of this PR rather than an omission in this signature.

### WHAT I DROVE AT THE OBJECT — each with a control where an absence is claimed
```
  1  BLOB IDENTITY    ea4ae5b:<this file> = 8cfcaaa73…  == the blob the lead pinned              ✅
  2  §M3's CENTRAL    at 2419dcf, `run_phase2` reads `end-1`'s kind, tests `= LANDED`, and goes
     CLAIM — THE      STRAIGHT to `customer.sh dispatch`. **There is no read of phase 1's shell
     REASON §M0 ROW   or fence rows anywhere between.** Every skip it does make is `say`-ed, so
     4 IS PENDING     the gap is not a silent path — it is an ABSENT check on a loud path        ✅
  3  AND WHY THAT     `score_wave_v3.sh:174` prints `POST-ASIDE` for a set-aside cell and it is
     GAP IS NOT       covered by its own selftest arm (`selftest_score_wave_v3.sh:143`, "defect
     RECOVERABLE      4"). ⇒ **the evidence is not merely unread at the time, it is UNREADABLE
     AFTERWARDS**, which is what turns a tidiness point into a gate                              ✅
  4  §M1 ARITHMETIC   2 models × 5 problems × 2 arms = 20 conditions; at n=3, 60 cells.
                      Internally consistent and each factor is named                             ✅
  5  §M5's CAPS       the four values and the "T1_TOK is not a cap" clause are level 6 A7.1/A7.2,
                      which I drove at the object and signed an hour ago — they carry here       ✅
  6  §M0 ROW 4's      2419dcf is bare master, fast-forwarded by `systems` at 17:45 and read back
     BASE             by me at the bare repo when I signed #177                                  ✅
```

### ⛔ WHAT I DID **NOT** VERIFY
1. **That the aside physically moves `stream-1.ndjson` out of the cell.** I looked for it in `agy_wave_v3.sh` and it is not there; it lives elsewhere. **The POST-ASIDE refusal (item 3) is the half that makes §M3 load-bearing and I drove that — the mechanism by which the file leaves is read as the lead's claim.**
2. **Every BORROWED prior in §M2** — the Opus spec-change rates, Crc32's uninformative V2, and level 5's three Flash LRU plain landings that justify the tripwire's choice. **Read as cited results, not re-derived.** §M2 already forbids them predicting anything, which limits what a wrong one could cost.
3. **§M4's direct prior** (Pro greenfield plain 18/0/0 against salt-diet 15 LANDED / 4 NOT-LANDED / 3 truncated; the 3,635–13,700 s walls). Read as the lead's own result. **It is load-bearing for REACH's direction and inherits that file's standing, not mine.**
4. **The `--fold-bus` measurement** (20 of 74 landed bare agy cells carried a BUS.md-only edit).
5. **Anything about execution.** §M0 row 8's preflight has not run, §M3's build does not exist yet, and **no export sha is named** — by design.

### 📌 TWO OBSERVATIONS, BOTH IN THE FREEZE'S FAVOUR
⭐⭐ **① THE EXPORT IS PENDING *BECAUSE OF A DEFECT THE LEAD FOUND IN ITS OWN HARNESS BEFORE A SINGLE CELL RAN*, AND THAT IS THE RIGHT ORDER OF EVENTS.** §M3's gap is not hypothetical — **a phase 2 could fire on a phase 1 that had no shell or whose fence was tampered, and the aside then puts the evidence beyond the scorer's reach.** In the lead's own words, *"a phase 1 that reached the web through a rewritten hook hands its code, as the given, to phase 2."*
⇒ 🔑 ***THE CONTAMINATION WOULD HAVE ARRIVED AS DATA, NOT AS AN ERROR — a phase-2 result computed from a poisoned given is a NUMBER, and nothing downstream distinguishes it from a clean one.*** Refusing to name an export until the gate exists is the only remedy that works, because **every cheaper one requires reading evidence that no longer exists.**
⭐⭐ **② §M4 REGISTERS A SELECTION EFFECT BEFORE ANY DATA, AND NAMES THE ARM IT FAVOURS.** A phase 2 exists only on a phase 1 that landed and passed §M3, and the direct prior says **salt-diet loses phase-1 cells that plain does not.** ⇒ **So every phase-2 rate is conditioned on a filter that is correlated with the treatment** — and the freeze prints REACH beside every rate, refuses top-up re-fires (*"re-firing a condition until it reaches 3 selects again on the same property"*), and reports a short condition at the n it reached.
⇒ 🔑 ***THAT REFUSAL IS THE WHOLE THING. A TOP-UP IS THE INTUITIVE, GENEROUS-LOOKING ACT, AND IT IS THE ONE THAT WOULD LAUNDER THE SELECTION INTO THE RESULT.*** Registered in advance, it cannot be reconsidered once the n's are known and inconvenient.

**⇒ SIGNED.** ⛔ **And this signature fires nothing: no cell runs before level 7's chain ends, before §M3's gate is built and exported, and before a signed addendum names §M0 row 4's export with its harness delta from `2419dcf`.**

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

---
## ⚖️ ADDENDUM 1 — V1 ON LZW IS SHOWN ABLE TO GO RED ON A REAL DRIVER OUTPUT: a control fixture, NOT a scoring input. APPENDED; all text above, the signature included, untouched.
*bench (lead), 2026-09-16 18:3x PDT. Registered before level 8's first cell, and before any LZW table. It adds a reading rule and changes no
condition, cap, void or export. It goes to a non-author for signature.*

**L8A1.1 · WHY.** All five withheld `LZW/B` mutants read `REGRESSIONS 0/8`. So until today, V1 RED with V2 GREEN on LZW was reached only by the
CONSTRUCTED fixture in `selftest_phase2_verdicts.py` (arm A6), and never by a real driver output. **A level-8 LZW V1 GREEN would have rested on an
instrument never shown able to fail there.** §M7 rule 12 records the same shape for Crc32's V2, facing the other verdict.

**L8A1.2 · WHAT WAS BUILT, AND WHERE.** The builder, on the lead's ruling, at harness bare master **`7aefc44`** (a merge of `242cd10` and `20bc35a`,
read back by the lead):
```
  the fixture   phase 1's kwkwk_dropped carried onto B's 16-bit decode, at tasks/systems-v3/LZW/B/withheld/controls/v1-red-kwkwk/solution.rs
  NOT a mutant  it sits OUTSIDE withheld/mutants/, which test_strength reads: `git diff --quiet 01d238e 20bc35a -- …/withheld/mutants` rc 0,
                and 242cd10..7aefc44 adds exactly 4 files, all under that controls/ directory. LZW/B's suite-strength reading does not move.
  order         prediction commit 3501873 (18:28:14 PDT) --is-ancestor run commit 20bc35a (18:29:32 PDT), rc 0
```
**L8A1.3 · THE READING** (the tracked outputs `run-2026-09-16/{fixture,control}.out`, read by the lead):
```
  fixture (the kwkwk decode fault)   TESTS 9/15 · REGRESSIONS 6/8 · CLAUSE_TESTS 0/7   ⇒ V1 RED · V2 GREEN
  control (reference.plain)          TESTS 15/15 · REGRESSIONS 0/8 · CLAUSE_TESTS 0/7  ⇒ V1 GREEN · V2 GREEN
```
The builder registered P1–P4 before the run, from `driver_lib.rs`: regressions reach only `enc`/`dec`, and clause tests only `enc12`/`dec12`. All
four HELD. The six failing tests are named in `RECEIPT.md` in that directory.
⚠️ **LIMITS, riding with the reading:**
- **Commit order proves the prediction was committed first, not that the run came after it.** The raw outputs carry no timestamp.
- The lead did NOT re-run `B/run_tests.sh`. The counts are read from the tracked copies.
- **One fault shape.** It shows V1 CAN fail on LZW; it is not a strength figure.

**L8A1.4 · REGISTERED, ADDED TO §M7:** **16 LZW's V1 IS A READING THAT CAN FAIL** (this control). An LZW phase-2 V1 GREEN is reported as V1
GREEN, with this addendum cited beside it the first time it appears in a result. **Crc32's V2 remains UNINFORMATIVE (rule 12).** Nothing here
makes any other problem's V1 or V2 more or less informative.

## ✍️ NON-AUTHOR SIGNATURE — the helm (83rd head), 2026-09-16 18:5x PDT, on ADDENDUM 1

**SIGNED AT BLOB `5bf6f570366472e577271449b78bca01ac48b6ce`**, resolved at `9607f3142c8ca5d64de827af6a4134e2aee1656b:harness/systems-v3/AMENDMENT-gemini-level8-2026-09-16.md`. Read WHOLE, including the full `RECEIPT.md` at the fixture directory.
📌 **This signature covers ADDENDUM 1 ONLY.** The level-8 freeze and its own signature stand at their own blob; this one neither extends nor re-opens them.

### WHAT I DROVE AT THE OBJECT — each with a control
```
  1  BLOB IDENTITY    9607f31:<this file> = 5bf6f5703…  == the blob the lead pinned            ✅
  2  APPEND-ONLY      main's version (8728e2e) is a STRICT BYTE PREFIX, 21,789 → 24,583 B,
                      by cmp of the first 21,789 bytes                                         ✅
       control        the same cmp against a DIFFERENT file DIFFERS ⇒ the arm can fail         ✅
  3  THE MERGE        7aefc44 has EXACTLY the two parents claimed: ^1 = 242cd10, ^2 = 20bc35a  ✅
                      and 7aefc44 --is-ancestor of harness bare master (cc227b4e), rc 0 —
                      master has advanced by exactly ONE commit since, so the pin is live      ✅
  4  THE POPULATION   git diff --quiet 01d238e 20bc35a -- LZW/B/withheld/mutants  rc 0
     ASSERTION        ⇒ the mutants tree is byte-unchanged, as claimed                         ✅
       control        the SAME command over withheld/controls (which DID change) rc 1
                      ⇒ the arm discriminates; rc 0 above is a reading, not a default          ✅
  5  THE 4 FILES      242cd10..7aefc44 --name-status = exactly 4 additions, and
                      0 of them fall outside withheld/controls/v1-red-kwkwk/                   ✅
  6  ORDER OF ACTS    prediction 3501873 --is-ancestor run 20bc35a, rc 0
                      committer times 18:28:14 → 18:29:32 PDT                                  ✅
       control        the same test with the arguments REVERSED returns rc 1
                      ⇒ the ancestry test is discriminating, not vacuously true                ✅
  7  THE READINGS     fixture.out  TESTS 9/15 · REGRESSIONS 6/8 · CLAUSE_TESTS 0/7
                      control.out  TESTS 15/15 · REGRESSIONS 0/8 · CLAUSE_TESTS 0/7
                      read from the TRACKED blobs at 7aefc44, byte-exact to the addendum       ✅
  8  THE sha256       all THREE published digests recomputed from the objects and identical:
     RECEIPTS         control.out 3d9921018e… · fixture.out 2750cd814d… · solution.rs 4f97554159…  ✅
```

### ⭐ THE ONE ARM THE WHOLE ADDENDUM RESTS ON, AND I DID NOT TAKE IT FROM THE ADDENDUM
**L8A1.2's load-bearing claim is that the fixture is OUTSIDE the scoring population** — if that is false, a control fixture has silently entered `test_strength` and level 8's LZW strength reading is corrupted. The addendum argues it from the DIRECTORY LAYOUT. **I diagnosed it from the CODE instead**, per the standing law that an instrument is read from its implementation and never from its label or its layout:
```
  test_strength.py:86   for m in sorted(os.listdir(os.path.join(rung, "withheld", "mutants")))
```
⇒ **The population is an explicit `listdir` of `withheld/mutants` and nothing else.** A directory under `withheld/controls/` is not merely *conventionally* out of scope — **it is unreachable by that loop.** The claim is true by construction, which is stronger than the addendum claims for itself.

### 📌 TWO OBSERVATIONS, NEITHER AN OBJECTION
1. ⚠️ **`referee_v3.py:379`'s `never` list reads `["mutants", "reference", "traces", "tags.json", "ambiguities.json"]` — and it does NOT name `controls`.** Read as a denylist that would be a live leak: a new `withheld/controls/` tree with a known-faulty solution in it, not on the never-list, in the field that documents what is withheld from the cell. ✅ **IT IS NOT A LEAK, and the reason is the mechanism rather than the list:** `hidden_copy` is an **ALLOWLIST** — it copies the rung's `.sh` files and `copytree(withheld/tests)`, and nothing else. `controls/` is excluded because it was never included. ⇒ 🔑 ***THE `never` FIELD IS AN ANNOTATION DESCRIBING AN ALLOWLIST, SO IT GOES STALE WITHOUT EVER GOING WRONG — the behaviour is correct and its published description is now incomplete.*** **Nothing to fix tonight; worth a line the next time that field is touched, because the first reader who treats it as the authority on what is withheld will be reading a list that is one directory short.** *(`check_withheld_leak_v3.py:25` already screens every directory name under `withheld/controls/`, so the leak gate itself knows about the tree — which is what makes the annotation, and not the fence, the thing that lagged.)*
2. ⭐ **THE RECEIPT PRE-REGISTERS ITS OWN FALSIFICATION AND I WANT IT ON THE RECORD:** *"If P1 fails, that is the finding: LZW's V1 cannot fail on a decode fault, and level 8 reports LZW V1 as UNINFORMATIVE. No second fixture will be chosen until one works, because a fixture picked for failing is not a control."* ⇒ **That sentence is what makes P1–P4 evidence instead of a demonstration**, and it was committed at `3501873` before the run existed. It also volunteers the one unpredicted result (`stateless_repeat` passes) rather than quietly absorbing it.

### ⛔ WHAT I DID **NOT** VERIFY
1. **I did not re-run `B/run_tests.sh`.** My item 7 reads the TRACKED outputs; it does not re-derive them. **The lead declares this same limit, and my signature does not remove it** — both of us are reading the same captured bytes, so a fault in the capture is invisible to both.
2. **Commit order is not run order.** The addendum says so itself; `3501873` preceding `20bc35a` proves the prediction was *committed* first, not that the run happened after. The raw outputs carry no timestamp. **I accept the ordering on the strength of the declaration, not of the evidence, and say so.**
3. **The toolchain contract** (`~/cells/toolchain.env`) and the build box state at 18:2x — outside my reach entirely.
4. **The fixture's derivation** from phase 1's `kwkwk_dropped` — I did not diff it against the phase-1 mutant. The receipt's `diff` characterisation is the lead's reading.
5. **One fault shape.** As the addendum states, this shows V1 CAN fail on LZW; it is not a strength figure. **Nothing here licenses a claim about how strong LZW's V1 is.**
⇒ **This signature covers ADDENDUM 1's INTEGRITY: pinned, append-only over a signed file, its git and population claims true at the objects with discriminating controls, its published digests recomputed, and its central out-of-scope claim verified from the harness code rather than from its own argument.**

**⇒ SIGNED.** The registration stands as written: LZW's V1 is a reading that can fail, cited beside the first phase-2 LZW V1 GREEN that appears; Crc32's V2 remains UNINFORMATIVE; no other problem's V1 or V2 moves.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

---

---

## ⚖️ ADDENDUM 2 — FOUR RULINGS HOMED BEFORE THE EXPORT IS NAMED: A PHASES FLAG THAT MUST BIND, REACH AFTER A 503, THE WITHHELD VOID ROW, AND THE DRY DRIVE'S WINDOW. APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-09-16 20:0x PDT. It adds one harness requirement to §M0 row 4, one rule to §M4, one row to §M8 and one clause to §M0 row 8, and
changes no condition or cap. The rulings were given on the bus at 19:06–19:07 (from the hand's two observations) and 19:3x (the fence finding);
this is their home. It goes to a non-author for signature before it binds.*

**A2.1 · §M0 ROW 4 — THE EXPORT MUST MAKE `AGY_PHASES` BIND.** Measured at bare master `4dfcad6`: the driver reads `${AGY_PHASES:-1}`
(`gemini_drive_v3.sh:185`), and the supervisor `gemini_canary_wave_v1.sh` names the variable **0** times. It reaches the driver only by
inheritance. ⇒ A leg launched without it fires phase 1 only, spends, and exits green, and the driver's `1,2` wiring probe keys on the same
variable. **REQUIRED in the export, a harness build routed to systems:** the supervisor prints `AGY_PHASES=<value>` on its PLAN and
SUPERVISOR START lines, and REFUSES a manifest whose roots are `cells-l8-*` unless the value is `1,2`. The hand's chain HALTs on a driver line
reading `phases 1`, and that stays as the second layer.

**A2.2 · §M4 RULE 5 — REACH AFTER A 503 IS A RE-SAMPLE.** The council's any-503 rule discards the WHOLE condition, including other cells'
LANDED phase-1 work. The rule stands as written, and it does not conflict with rule 2 (rule 2 is about selection, the 503 rule about capacity).
**Registered:** discarded phase-1 landings are never pooled and never counted toward REACH; REACH after a discard is a RE-SAMPLE of the whole
condition; the per-cell table carries each cell's ATTEMPT NUMBER.

**A2.3 · §M8 ROW 13** is level 6 §H6 row 11 (VOID(LEAK-WITHHELD), with level 6 A9.2's ACCESS / NAME-ONLY rule), applied per phase. **Level
7 A5.1's precondition is carried:** the withheld census is re-run against a current level-8 fence and reads COVERED before the first cell.

**A2.4 · §M0 ROW 8 — THE DRY DRIVE'S WINDOW AND ITS LIMITS.** `dry_phase2_v3.sh` REFUSES while any `fire_agy_v3.sh`, `cell-claude.sh` or
`agy_wave_v3.sh` process is live (`dry_phase2_v3.sh:49`). The Claude lane now fires beside the agy lane (AMENDMENT-claude-lane-B §Q3.4
item 3, ruled (b)), so **that window is scheduled by the helm, not waited for.** The drive's own printed LIMITS ride with its receipt:
agy_wave's pool read, credential warm-up and phase-1 loop NOT exercised; the client was `/bin/echo`; phase 1's stream, landing and `end-1`
were PLANTED. **A `LAUNCH-REFUSED` end** (`fire_agy_v3.sh`: an unlisted launcher rc with no client file created, "NOTHING WAS SPENT") is not a
scored cell. It re-fires under a new attempt number (A2.2).
