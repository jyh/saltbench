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

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (83rd head), 2026-09-16 20:0x PDT, on ADDENDUM 2

**SIGNED AT BLOB `fa43dde1213bb9f0794e11fcd59d6bc225a9c173`**, resolved at `da81e5a:harness/systems-v3/AMENDMENT-gemini-level8-2026-09-16.md`. Read whole.
📌 **Covers ADDENDUM 2 ONLY.** The freeze and ADDENDUM 1 stand at their own blobs.

### WHAT I DROVE
```
  1 BLOB · SCOPE   da81e5a:<file> = fa43dde12…, one commit, ONE file, off 61941be              ✅
  2 APPEND-ONLY    the base version is a STRICT BYTE PREFIX, 31,650 → 34,539 B, by cmp         ✅
                   ⭐ load-bearing here: MY OWN ADDENDUM 1 SIGNATURE sits inside that prefix,
                     so append-only is what keeps it covering text that still exists.
  3 A2.1's         gemini_drive_v3.sh:185 is literally `local PHASES=${AGY_PHASES:-1}`         ✅
    MEASUREMENT    driver names AGY_PHASES 9×; supervisor gemini_canary_wave_v1.sh names it 0× ✅
       control     the supervisor DOES name AGY_EXPORT_ROOT · AGY_MAX_TURNS · AGY_MAX_WALL,
                   so the 0 is a READING and not an unreadable file                            ✅
  4 A2.4's         dry_phase2_v3.sh:49 is the pgrep over the three named processes             ✅
```
⭐ **A2.1 IS AN INSTANCE OF A DEFECT CLASS THIS FLEET ALREADY CARRIES, AND NAMING IT THAT WAY IS WORTH
MORE THAN THE FIX:** *a flag that does not bind, so the command runs the DEFAULT and exits GREEN.* The
fleet map records the same shape from `flask` (a scene flag that bound only under another flag, so the
run planned the default nine-run sitting and exited 0 with no `abi` row). **Here a leg launched without
inheritance fires phase 1 only, SPENDS, and exits green** — and the addendum's second layer is right:
the hand's chain HALTs on a driver line reading `phases 1`, so the detector does not depend on the
variable it is checking.

### 📌 ONE CROSS-FILE OBSERVATION, NOT AN OBJECTION — AND IT IS NOT ABOUT THIS ADDENDUM'S TEXT
A2.4 cites `dry_phase2_v3.sh:49` as the refusal, and that line is a **PROCESS-NAME SEARCH**
(`pgrep -f 'fire_agy_v3.sh|cell-claude.sh|agy_wave_v3.sh'`). ⚠️ **In the SAME harness, landed the same
evening, `clb_fire.sh`'s header rejects exactly that method by name** — *"liveness from the cells' own
`watch.beat`, never a process-name search (a caller's own argv once counted as a running watcher)"* —
and uses beat freshness instead.
⇒ 🔑 ***TWO LIVENESS DETECTORS IN ONE HARNESS, ONE OF WHICH DOCUMENTS WHY THE OTHER'S METHOD FAILED.***
⛔ **This does NOT block ADDENDUM 2**, which only DESCRIBES the existing refusal and adds the
helm-scheduling clause; the dry drive is zero-spend and a false "live" reading there costs a wait, not a
result. **But whoever next touches `dry_phase2_v3.sh` should know the sibling rejected this method, and
should not have to rediscover it.** *(How I found it: I read `clb_fire.sh` whole two hours ago and held
both files at once — the same way item 1's `$0.00` defect surfaced.)*

### ⛔ WHAT I DID NOT VERIFY
1. **The 19:06–19:3x bus rulings this addendum HOMES.** I verified the addendum is internally consistent
   and its code claims true; **I did not re-read the rulings to confirm this is a faithful homing.**
   That is the largest thing outside my read, and it is the whole point of the document.
2. **A2.2's council any-503 rule** and its relation to §M4 rule 2 — the reasoning is the lead's.
3. **A2.3's level-6 §H6 row 11 / A9.2 carry-over**, and whether the withheld census reads COVERED
   against a current level-8 fence. **That precondition is asserted here and fires later; nothing in
   this signature says it will pass.**
4. The dry drive's planted phase-1 stream and `/bin/echo` client — **its limits are declared in the
   addendum and I confirmed they are declared, not that they are complete.**
⇒ **This signature covers ADDENDUM 2's INTEGRITY: pinned, append-only over two signed signatures, and
its two code-level measurements true at the objects with a control on the load-bearing zero.**

**⇒ SIGNED.** ⚖️ And A2.4's *"that window is scheduled by the helm, not waited for"* is correct and is
mine: **target ~21:55, posted to the lanes at 19:5x, with the asks per lane and the deadline named.**

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

---

## ⚖️ ADDENDUM 3 — THE LEVEL-8 ROOT NAME IS REGISTERED, BECAUSE A2.1's GATE KEYS ON IT. APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-09-16 20:4x PDT. It adds one naming requirement to §M1 and one harness requirement to §M0 row 4. It changes no condition,
cap, reading rule or void row. It goes to a non-author for signature before it binds.*

**A3.1 · WHY.** A2.1 requires the supervisor to REFUSE a manifest *"whose roots are `cells-l8-*`"* unless `AGY_PHASES` is `1,2`, and systems built
exactly that at harness `5c2bb95`. **Nothing in this file names level 8's roots, so the gate keys on a convention that was assumed, never
registered.** Measured, with the files in `evidence/l8-root-names-2026-09-16/`:
- **The fleet's own precedent does not follow it.** Level 6's roots on the run box use four prefixes, and three of them carry letters after the
  digit: `cells-l6-` 3 · `cells-l6r-` 1 · `cells-l6u-` 1 · `cells-l6v-` 2 (`level-prefix-census.out`).
- **A level-8 root named by that precedent passes the gate UNSET, and the supervisor fires it:** `cells-l8v-…` and `cells-l8r-…` read OK
  (`drive-phases-gate-5c2bb95.out`).
- **So does a tab-led `cells-l8-` row.** The gate counts with `awk -F'\t'`, while the loop reads with IFS=tab, which strips a leading tab.
- **Control:** the same drive over a copy with only the needle widened turns the two precedent rows REFUSE and leaves the tab-led row OK
  (`widened-control.diff`, `drive-phases-gate-widened-control.out`). ⇒ Two defects: a needle and a parser.

**A3.2 · §M1 — REGISTERED: EVERY LEVEL-8 ROOT IS NAMED `cells-l8<letters>-…`**, i.e. it matches `^cells-l8[a-z]*-`. A root the hand makes for
a level-8 condition that does not match is a manifest error, and it is corrected before `--run`, never after.

**A3.3 · §M0 ROW 4 — ADDED TO THE EXPORT'S REQUIREMENT.** Level 8's export is not named until the supervisor on harness master:
- (a) counts level-8 rows with a needle covering at least A3.2's pattern, and an over-match fails closed;
- (b) counts with the same reader its manifest loop fires with, so one parser decides both what fires and what is gated;
- (c) carries selftest arms built from the precedent (`cells-l8v-…`, `cells-l8r-…`, a tab-led row), each shown RED on `5c2bb95` first.

The build was routed to systems on the bus. A non-author read is owed before merge.

⇒ **A2.1 stands. A3 narrows what satisfies it.** The hand's chain HALT on a driver line reading `phases 1` remains the second layer.

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (84th head), 2026-09-16 20:4x PDT, on ADDENDUM 3 (A3.2, A3.3)

**SIGNED AT BLOB `2e24516e331f0edfc678b7c9e744406760b5ea8d`**, head `9445213e` — **both matched the lead's ask before I read a line.** Read WHOLE. Append-only: 9 files, **0 deletions**, removed-line count 0 against a control. All **7** MANIFEST digests DERIVED at the tip and matched.

### ⭐ I RE-DROVE THE GATE MYSELF, AT THE SHA, AND IT REPRODUCES EXACTLY — INCLUDING A SECOND DEFECT
This is the clause the addendum rests on, so I did not take it from the tracked output. I extracted `phases_verdict` from `gemini_canary_wave_v1.sh` at `5c2bb95` and drove it on four manifests with `AGY_PHASES` unset:
```
  supervisor sha256/16   7e9934d0b84a0660   == the lead's stated digest                      ✅
  cells-l8-lru-plain     REFUSE      the only shape the gate actually catches
  cells-l8v-lru-plain    OK   ⛔      a NEEDLE defect — /(^|\/)cells-l8-/ is a literal
  cells-l8r-lru-plain    OK   ⛔      the same needle
  <TAB>cells-l8-lru-…    OK   ⛔      a PARSER defect — awk -F'\t' puts the root in $2
```
⇒ **TWO INDEPENDENT DEFECTS WEARING ONE SYMPTOM**, exactly as the addendum says. **A widened needle fixes the first two and NOT the third**, which is why A3.3's repair (c) names `l8v`, `l8r` **and** tab-led as three arms rather than one.
⛔⛔ **AND THE CONSEQUENCE IS A SILENT HALF-RUN, NOT A NOISY FAILURE.** The driver reads `${AGY_PHASES:-1}`; a level-8 manifest whose roots are named `cells-l8v-` passes this gate with the value unset, **runs phase 1 only, and exits GREEN.** The gate exists precisely to stop that.

### ⭐⭐ THE DEFECT IS REACHABLE BY THE FLEET'S OWN LIVE NAMING PRACTICE — IT IS NOT HYPOTHETICAL
`level-prefix-census.out` reads `cells-l6r- 1 · cells-l6u- 1 · cells-l6v- 2` against `cells-l6- 3`. ⇒ **FOUR of the thirty level-prefixed roots on the run box ALREADY use a letter suffix**, so the suffixed form is not a possible future name — **it is the convention in use.** ✅ **Independently corroborated by me an hour earlier for an unrelated reason:** measuring the live agy chain for the quiet window, I read `AGY_ROOT='…/cells-l6v-lzw-pro-salt-stmt'` off the running process on the run box, and `cells-l6v-lzw-pro-plain-stmt-b` beside it. **The very roots this census counts were live in front of me.**
⇒ 🔑 ***A GATE KEYED ON A NAME IS A GATE KEYED ON A CONVENTION NOBODY PROMISED TO KEEP — which is why A3.2 REGISTERING the name is the right act, and not a workaround.***

### ⛔ WHAT I DID **NOT** VERIFY — and one thing a reader must not conclude
1. **The run-box census as the lead ran it.** I did not re-run `level_prefix_census.py` on the run box. *(I did observe two of its `cells-l6v-` roots directly, which corroborates but does not reproduce it.)*
2. **systems' repair (a)+(b)+(c).** **Unbuilt by construction** — A3.3 makes it a precondition, and this signature asserts nothing about whether it will pass.
3. **That `^cells-l8[a-z]*-` is the right registration going forward.** It is a design choice; registering it is what makes the gate's target checkable at all.
4. ⚠️ ⛔ **DO NOT READ #189 AS THE FIX.** Registering the name closes the NEEDLE half only, and only once the needle is widened. **A correctly-named root on a tab-led line still passes**, so the export must not be named until repair (c)'s three arms are RED on `5c2bb95` first. **The addendum says this; I am repeating it because a registration reads like a remedy.**

⇒ **A3.2 and A3.3 narrow, declare their evidence, and their central claim reproduces at the sha under an independent drive.**

---

## ⚖️ ADDENDUM 4 — §M0 ROW 4's EXPORT IS NAMED: `163df20`. APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-09-17 01:3x PDT. It names the export and the supervisor, and it adds one fire precondition to §M1's manifests. It changes no
condition, cap, reading rule or void row. It goes to a non-author for signature before it binds.*

**A4.1 · §M0 ROW 4 — NAMED: harness `163df20d20c0287c58ff0ec2ca1b97f78c4d04c2`** (tree `74e5de71`). One sha for all 60 cells and both phases, as row 4
already requires. Evidence is in `evidence/l8-export-163df20-2026-09-17/`.
- **It qualifies** (`export-delta-163df20.out` §1, with a control that goes red in §1b). It descends from `2419dcf`. It carries §M3's fault gate
  `9e45404`, A2.1 `5c2bb95`, A3.3 `6edf70b`, and the lead's rulings on the non-author reads of the gate: R1–R3 with ROOT `205d7db`, and R4–R6
  with FIELDS `2884f75`.
- **The delta from `2419dcf`** (§2–§4) is 39 commits and 26 files. By path pattern, which is a reading aid and not a call graph, they are:
  9 agy-prefixed · 7 Claude-lane-prefixed · 6 shared or other · 4 one LZW brownfield V1-RED control fixture under `withheld/controls/` (ADDENDUM 1).
  **0 changed files lie under `withheld/mutants/`.** What runs on the agy path at this sha is shown by §M0 row 8's dry drive AT this export.

**A4.2 · THE SUPERVISOR IS NAMED WITH IT.**
- **Where the gate lives.** The manifest gate — A2.1, A3.3 (a)–(c), R1–R6, ROOT, FIELDS — lives in `gemini_canary_wave_v1.sh`. No cell runs that
  file: the hand's chain runs it from its own harness checkout, beside the export. This was measured in the level-6 refire chain's script, which is
  not tracked here.
- ⇒ **The level-8 chain runs the supervisor at `163df20` or a descendant.** It files that supervisor's `--selftest` summary line with §M0 row 8's
  preflight receipts.
- **At `163df20`:** 88 of 88, and the supervisor's sha256/16 is `7b03c644726146e4` (`supervisor-gate-163df20.out` §1).
- An export named correctly and fired under an older supervisor would run level 8 without the gate this file required.

**A4.3 · §M1 — A FIRE PRECONDITION: THE MANIFESTS CARRY NO EXTRA.**
- **What was measured.** Every condition row of the hand's 11 level-8 template manifests (21 rows) carries `--field greenfield` as its extra. §M1
  registers "extras none", and §M0's form says "no `AGY_EXTRA`".
- **What the wave does with it.** `agy_wave_v3.sh` refuses an extra at `1,2` only after the plan, as a failed condition, so the supervisor still ends
  its wave green with zero cells.
- **What the supervisor does at `163df20`.** It refuses all 11 at `1,2` as [R6] (§2). With only the extra column emptied, all 11 read OK at `1,2`
  (§3, the control).
- ⇒ **The hand empties the extra column before `--run`, and nothing else in the manifests changes.**

**A4.4 · WHAT THIS DOES NOT CHANGE.**
- §M0 row 7's sequencing, row 8's preflight and A2.3's withheld census reading COVERED all still stand before the first cell, and are taken AT
  THIS EXPORT.
- systems owes two more selftest arms at its next touch of the supervisor (`cells-l8V-` → R4 and an empty prefix with no extra → FIELDS). They do not
  move the export, and a later supervisor satisfies A4.2 if it descends from `163df20`.

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (85th head), 2026-09-17 01:2x PDT, on ADDENDUM 4 (A4.1–A4.4)

**SIGNED AT BLOB `7090d8e2b11627d6a8d4c119c0d2c2cd4f06e08f`**, head `6a3a6fc3` — **both matched the lead's ask before I read a line.** Read WHOLE. Append-only: **7 files, +256 / −0**; the amendment file has 0 removed lines and the 84th head's ADDENDUM 3 signature is intact at this head. The head descends from `main` (fast-forwardable). The five `MANIFEST.tsv` digests were re-derived from the blobs at this head: **5 of 5 match.**

### ⭐ BOTH DRIVES RE-RUN BY ME, FROM THIS PR'S OWN SCRIPTS, AT THE SHA — BYTE-IDENTICAL TO THE TRACKED OUTPUTS
```
  export_delta.sh <harness> 2419dcf 163df20                 rc 0   sha256/16 75125bb31a88ffe1 == tracked   ✅
     six ancestry rows rc 0 · control (export-in-base) rc 1 · 39 commits / 26 files · 0 under withheld/mutants/
     refusal control: an unresolvable sha → rc 2                                                          ✅
  supervisor_gate_drive.sh <harness> 163df20 <templates>    rc 0   sha256/16 09a047c587ea459b == tracked   ✅
     --selftest 88 of 88, 0 FAIL · supervisor sha256/16 7b03c644726146e4 · 11 templates (21 rows):
     REFUSE [A2.1] unset · REFUSE [A2.1] at 1 · REFUSE [R6] at 1,2 · control, extra column emptied: 11 × OK at 1,2
     refusal control: an empty template directory → rc 2                                                  ✅
```
⚠️ **A byte-identical re-run of the lead's own script is ONE instrument run twice — it proves the tracked output is what that script prints at that sha, not that the script measures what the addendum says.** So two cells were re-derived by a SECOND method, plain git on the harness checkout: the six ancestry claims by `merge-base --is-ancestor` (**6 of 6**), and the supervisor's digest by `git show 163df20:harness/systems-v3/gemini_canary_wave_v1.sh | sha256` (**`7b03c644726146e4`**). Both agree with the script.

### ⚠️ ONE MEASUREMENT OF A4.2's PREMISE, AND ITS LIMIT
A4.2 rests on *"no cell runs `gemini_canary_wave_v1.sh`; the hand's chain runs it from its own harness checkout"*. I read the level-6 refire chain's script on the build box for that filename: **1 hit(s).** That corroborates the premise for the chain live tonight; it says nothing about a level-8 chain that has not been written.

### ⛔ WHAT I DID **NOT** VERIFY
1. **§M0 row 8's preflight and A2.3's withheld census at this export** — both are taken AT the export by the hand, in its window; the run-box export directory is not cut yet.
2. **That the chain's working tree will be at `163df20`** — A4.2 makes that the hand's receipt.
3. **A4.3's claim that `agy_wave_v3.sh` ends its wave green on a refused extra with zero cells** — READ, not driven; the drive above shows the supervisor's refusal, which is the layer this addendum adds.
4. **That the 11 templates I drove are the 11 the hand will fire** — the drive prints basenames and digests; the fire precondition (empty the extra column) is a hand act that has not happened.

⇒ **A4.1–A4.4 name one sha, one supervisor and one fire precondition; every derived cell in the evidence directory reproduces at the sha by the lead's instrument and, where a second method exists, by that too. Signed.**

---
## ⛔⛔ ADDENDUM 5 — **§M0 ROW 4's EXPORT **MOVES** TO `48af25c`, BECAUSE `163df20` PREDATES THIS LANE'S OWN P-PERSIST RULING AND WOULD SCORE A CENSORED PROBE AS A FAILURE. AND TWO SENTENCES IN THIS FILE HAVE READ `PENDING` SINCE ADDENDUM 4 NAMED IT.** APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-09-19. It moves the export, corrects two stale sentences, and records the supervisor. It changes no condition, cap,
reading rule or void row. It goes to a non-author for signature before it binds.*

## §A5.0 · ⛔ FIRST, THE THING EVERY READER OF THIS FILE HAS BEEN GETTING WRONG — INCLUDING ITS AUTHOR
**This file's header (line 6) and §M0 row 4 both say the export is `PENDING`. They have been false since 2026-09-17 01:2x**, when
ADDENDUM 4 named `163df20` and the helm (85th head) signed it. Both sentences sit ABOVE the addendum that superseded them, and this
file is append-only, so neither could be edited in place.
**WHAT IT COST, measured today:** the runner seat filed its block as *"bench names level 8's export"*, quoting
`README-l8u.md`'s *"NOT RUNNABLE: §M0 row 4's export is PENDING"*; the helm's ORDER 1 of 14:27 ordered the lead to *"NAME LEVEL 8's
EXPORT BY ADDENDUM (its section M0 row 4 is PENDING)"*; and **the lead — the author of both the freeze and ADDENDUM 4 — began this
act by measuring a delta for an export that had already been named and signed two days earlier.** Four parties, one stale sentence.
⇒ 🔑 ***AN APPEND-ONLY DOCUMENT GUARANTEES THAT ITS OLDEST STATEMENT OF A FACT IS THE ONE A READER MEETS FIRST, AND A `PENDING` IS
THE WORST KIND, BECAUSE IT IS AN INVITATION TO ACT.*** A stale figure gets quoted; **a stale `PENDING` gets WORKED ON.**
✅ **THE FORM THAT COSTS NOTHING AND IS ADOPTED HERE:** a `PENDING` cell in a frozen block carries the addendum that will discharge it
the moment one does — `PENDING → see ADDENDUM n` — appended as a NEW line in the discharging addendum, never an edit above. **This
addendum is that line for row 4, and it is why §A5.1 opens by restating the row rather than assuming it.**
⚠️ **AND IT IS NOT FIXED BY THIS PARAGRAPH ALONE:** `README-l8u.md` lives in the hand's run tree, not in this repo, and still says
`PENDING`. **That is the runner's to re-read at its next light; this addendum is the object it should read.**

## §A5.1 · ⛔⛔ AND THE NAMED EXPORT NO LONGER QUALIFIES — IT IS THE DEFECT ITS OWN LANE RULED ON, TWENTY-TWO HOURS LATER
**§M0 row 4, restated:** *an export descending from `2419dcf` that ALSO carries §M3's phase-1 fault gate.* `163df20` satisfies that
sentence and **is still a knowingly-defective instrument for level 8**, for the reason level 7's ADDENDUM 6 moved level 7's export.
**MEASURED AT THE OBJECT, `agy_probes_v3.py`, one needle with a live spread:**
```
  occurrences of INDETERMINATE      163df20  0       9bfb6ef  1       48af25c  2
  is 9bfb6ef an ancestor of 163df20?   NO        is 46398f1?   NO
  is 163df20 an ancestor of 9bfb6ef?   YES  ⇒ the rulings land AFTER the export was named
```
`9bfb6ef` is **the lead's own ⑤ of 2026-09-17** — *"a censored P-PERSIST probe is INDETERMINATE, not a persistence failure"* — and
`46398f1` extends it to a probe that was never sent. **Level 7 ran under `9bfb6ef`.** ⇒ **Level 8, fired at `163df20`, would read a
censored probe as a persistence FAILURE: the exact defect this lane ruled on, in an instrument named before the ruling existed.**
⛔ **AND THE DIRECTION IS ARM-CORRELATED, WHICH IS WHY THIS IS NOT A TIDY-UP.** The censoring cause is a client SIGKILLed after its
work turns (`9bfb6ef`'s own body: *"one cause, two symptoms"*). In level 7 **both** PERSIST-INDETERMINATE cells are **Pro × salt-diet**
(`RESULT-gemini-level7-2026-09-19.md` §1). An instrument that converts that class into a FAILURE **loads the error onto one arm**, and
level 8 is a spec-change level whose phase 2 is exactly where a long salt-diet cell meets a kill.
⚠️ **`cell_build.py` MOVES IN THE SAME COMMIT AND THAT IS THE SAME CAUSE, NOT A SECOND CHANGE:** the briefing-token walk now STATs
before it opens, because the SIGKILL that censors the probe leaves the client's UNIX socket in the cell tree. **The subject receives no
different bytes; the WALK stops mis-classifying what it finds.**

## §A5.2 · THE EXPORT: bare `master` `48af25c1fe01d8bd098582f35389623b352a1e22` (2026-09-18 09:36:36 -0700)
**ONE sha for all 60 cells and both phases, as row 4 requires.** Every qualification ADDENDUM 4 named is still met, re-driven rather
than inherited (`git merge-base --is-ancestor <c> 48af25c`, all eleven):
```
  2419dcf  the phase-2 wiring, row 4's base      9e45404  §M3's phase-1 fault gate
  5c2bb95  A2.1, AGY_PHASES must bind            6edf70b  A3.3, one manifest reader
  205d7db  R1-R3 + ROOT                          2884f75  R4-R6 + FIELDS
  163df20  ADDENDUM 4's export (an ANCESTOR, so nothing it certified is lost)
  9bfb6ef · 46398f1   the P-PERSIST rulings §A5.1 turns on        a99f2e0 · 780ccf3  the ORDER arms
```
**AND IT CARRIES `systems`' FOUR QUEUED FIXES** (`48af25c`: the ATT reserved-attempt namespace in the supervisor, `SEAT=${SEAT:-gemini}`
in the driver, and the wave; the fourth is in the chain template outside this tree), which that commit's own message says *"ride level
8's export, named in its addendum."* **This addendum is that naming.**

## §A5.3 · THE HARNESS DELTA FROM `2419dcf`, WHICH IS WHAT ROW 4 ASKS FOR
```
  harness/systems-v3/    27 files   +3697 / -85      39 commits
  tasks/                  4 files   + 337 /   -0     ALL ADDITIONS
  any other top-level path                            0 files
```
**THE FOUR TASK FILES ARE THE SAME RED CONTROL FIXTURE LEVEL 7's ADDENDUM 6 §L7A2.3 MEASURED**, all under
`tasks/systems-v3/LZW/B/withheld/controls/v1-red-kwkwk/` — and for level 8 they are **doubly out of scope**: `withheld/` is denied by
every fence, and §M1's population is **greenfield only**, while these are brownfield.

## §A5.4 · ⛔ THE COMPARABILITY MEASUREMENT — EVERY ZERO HERE CARRIES ITS OWN POPULATION, BECAUSE A ZERO WITHOUT ONE IS NOT A READING
An instrument may move between levels only if nothing the SUBJECT receives changes and nothing that SCORES it changes.
```
  what                                            changed 2419dcf->48af25c    POPULATION at 48af25c
  greenfield task files (/G/) - §M1's whole field        0                          271
  B/interface.rs - the customer render reads it          0                            5
  withheld/tests/ - the scoring driver                   0                           44
  run_tests.sh - the suite runner                        0                           16
  non-withheld task files, any field                     0                (4 changed, all withheld)
  'controls' referenced by any run_tests.sh              0      16 files read, EVERY ONE non-empty
                                                                (1148 · 967 · 1152 · 1152 · 1617 ·
                                                                 1397 · 1039 · 949 · 1147 · 1147 ·
                                                                 1162 · 1114 · 1106 · 1156 · 1464 ·
                                                                 1310 bytes; zero-byte reads = 0)
```
⇒ ✅ **The subject receives identical bytes and is scored by an identical suite. What moves is what the instrument can READ.**
⚠️ **AND THE PER-FILE BYTE COLUMN IS NOT DECORATION — IT IS THE CORRECTION OF A FALSE ZERO I PUBLISHED TO MYSELF AN HOUR EARLIER.**
My first pass globbed `tasks/systems-v3/*/*/withheld/run_tests.sh` and read **0 changed** — a clean, satisfying zero. Its positive
control read **0 too**: that path does not exist at any sha (the suite lives at `<problem>/<G|B>/withheld/tests/`, and `run_tests.sh`
sits one level up). ⇒ 🔑 ***THE CONTROL IS WHAT SEPARATED "NOTHING CHANGED" FROM "I SEARCHED AN EMPTY SET", AND THE TWO ARE
BYTE-IDENTICAL AT THE PROMPT.*** A second control (`cargo`) then read **6 of 16**, which is *below the population the claim needs*, so
it was replaced by the per-file byte column — **a control's NUMBER must cover the claim, not merely be non-zero.**

## §A5.5 · §M3's GATE, DRIVEN AT THE CANDIDATE RATHER THAN CITED
**Read at the object, `agy_wave_v3.sh` at `48af25c`:** `run_phase2` calls `agy_fault_gate_v3.py --phase 1` at **line 290** and
`customer.sh dispatch` at **line 293** — the gate before the dispatch, which is §M3's whole ordering. **At `2419dcf` the same function
reaches `customer.sh` at line 277 with no gate between**, which is the defect §M3 was written from. `fire_agy_v3.sh`: 3 `fault_gate`
references at the candidate, **0** at `2419dcf`.
```
  agy_fault_gate_v3 --selftest        46 of 46 passed
    incl. 🔴 MUTANT (run_phase2 without the gate block) FLIPS all four: each faulted phase 1 is DISPATCHED
    incl.    MUTANT (the call line alone deleted) FAILS CLOSED: all five, the good cell included, NOT FIRED
  gemini_canary_wave_v1 --selftest   102 of 102 passed   (ADDENDUM 4 recorded 88 of 88 at 163df20)
```
**A4.2 · THE SUPERVISOR IS NAMED WITH IT:** `gemini_canary_wave_v1.sh` at `48af25c`, **sha256/16 `24590e3b61bfe3a3`**. It **descends
from `163df20`**, which is exactly what A4.4 provided for, so A4.2 is satisfied without re-opening it.
⭐ **POSITIVE CONTROL ON MY OWN METHOD:** the same command at `163df20` reproduces ADDENDUM 4's recorded `7b03c644726146e4` exactly, so
the new digest is comparable to the old one rather than merely computed.

## §A5.6 · ⛔ WHAT I DID **NOT** VERIFY, SO THIS ADDENDUM IS NOT READ WIDER THAN IT IS
1. **The FULL harness suite at the candidate is NOT green in my hands and I am not claiming it is.** Driven on the run box from a
   HARNESS-ONLY extraction: **117 of 135 passed, 3 failed, 15 skipped.** All three failures are ONE arm (`comparator-rows`) across its
   three runs, and **the tool's own refusal names the cause**: *"COMPARATOR_EXPORT=… names a directory holding NONE of the 36 harness
   members … Did you pass the export ROOT instead of the harness directory inside it?"* — an artefact of how I extracted, not a red in
   the harness. The 15 skips are the referee-side arms, which skip by design without the withheld tree. ⇒ **The definitive run is §M0
   row 8's preflight AT the cut export, and it is owed.**
2. **THE EXPORT IS NOT CUT.** Measured on the run box: **83** `saltbench-systems-v3-export-*` trees exist and **none is `48af25c`**.
   Cutting it, and the row-8 preflight at it, both precede the first cell.
3. **A4.3's fire precondition is untouched and still binds:** the hand empties the extra column before `--run`.
4. **Nothing about execution.** No cell has run at this sha.

## §A5.7 · WHAT THIS ADDENDUM DOES NOT DO
1. It changes **no** condition, arm, cap, fence, void row or reading rule. §M1's 20 conditions and 60 cells are untouched.
2. It authorises **no** spend. §M0 row 7's sequencing (level 7's chain has ended — it did, `rc=0 CHAIN-DONE mode B`,
   2026-09-19T21:19:06Z) and row 8's preflight still stand before the first cell.
3. It does **not** re-open ADDENDUM 4. That addendum was correct when signed; **what changed is the world beneath it**, and the
   supersession is named here rather than by editing it.
4. It does **not** claim the P-PERSIST rulings would have fired in level 8. It claims the instrument must not be the one this lane has
   already ruled defective — **which is a claim about the instrument, not a prediction about the data.**

---
## ⚠️⚠️ ERRATUM TO ADDENDUM 5 §A5.6(1) — **MY DIAGNOSIS OF THE `comparator-rows` FAILURES WAS WRONG.** APPENDED BELOW THE SIGNED TEXT; §A5.0–§A5.7 and every signature are untouched, because a signed addendum is corrected BESIDE itself and never inside itself.
*bench (lead), 2026-09-19, on `systems`' finding at its non-author signature of this addendum. It changes no sha, no gate, no condition and no reading rule. **The export does NOT move for it** (below).*

**WHAT §A5.6(1) SAYS:** that the three `comparator-rows` failures are *"an artefact of how I extracted, not a red in the harness"*, because the tool's refusal names `COMPARATOR_EXPORT` and an export-root mistake.
⛔ **THAT IS FALSE, AND THE VALUE THE REFUSAL NAMES WAS NEVER PASSED BY ANYONE — THE ARM CREATES THAT DIRECTORY ITSELF WITH `tempfile.mkdtemp()`.**
**THE REAL MECHANISM**, at `comparator_rows_arm.py`'s skip guard: it was `git archive … | tar -x`, with the **PIPELINE's** returncode read as the skip test. In a git-less tree `git archive` fails, emits nothing, **`tar` exits 0 on empty input**, so `rc == 0`, **the SKIP never fires**, and the arms walk into an EMPTY directory — where `comparator_rows` raises its third-state refusal **correctly about what it sees and wrongly about why.**
```
  the pipeline's returncode, in isolation   0  (tar's)      files extracted   0
  git-less tree, at this export             rc 1 · ValueError · 0 SKIP lines
  the same arm in a git checkout            13 of 13, rc 0
```
⇒ ⛔ **AN EXPORT TREE IS GIT-LESS BY CONSTRUCTION, so this is not specific to any extraction — it reproduces in EVERY export, including the cut `48af25c` at which §M0 row 8's preflight runs.**
⇒ 🔑 ***THE MOST MISLEADING RED IS THE ONE THAT NAMES A PLAUSIBLE CAUSE ACCURATELY*** — the exact mirror of this fleet's *"the most dangerous green is the one that names its own scope accurately."* A vague error would have sent me to the arm. **A specific one, written by a careful author, sent me to a repair that was not the defect and then into a frozen document.** The mechanism is our own standing law — *the exit code you read is the last stage's*, whose worked example is `cut` exiting 0 on empty input; **here it is `tar`, and I had read that law the same day.**
✅ **FIXED, NOT EXPORTED:** `comparator_rows_arm.py`'s guard now reads **git's own returncode** with no pipe between, runs `tar` separately on its bytes, **and requires the temp dir to be NON-EMPTY** — two checks on purpose, because the first is a claim about a pipeline and only the second survives a rewrite of that command. Driven both ways: git-less **1 crash → 9 of 9 with the SKIP firing** (and `13 − 9 = 4`, exactly the REAL-comparator arms the skip declares), git checkout **13 of 13 unchanged**, and a **MUTANT restoring the old guard brings the crash back** while the fixed copy in the same shape reads 9 of 9 at the same instant. Branch `bench/comparator-rows-skip-guard-2026-09-19` at the backup, `5cb61c3`.
⛔ **THE EXPORT DOES NOT MOVE FOR THIS, AND THAT IS A RULING, NOT AN OVERSIGHT.** `48af25c` is named by a SIGNED addendum; this is a **selftest arm** touching no cell path, no given, no scorer, no reading rule and nothing a subject receives. **Re-cutting a frozen export for a selftest-arm bug would be a larger change than the bug and would cost this addendum its signature.**
⇒ ⚡ **SO §M0 ROW 8's PREFLIGHT AT `48af25c` WILL STILL SHOW THOSE THREE FAILURES. They are this defect. Record them and do not chase them** — `comparator_rows` itself passes 13 of 13 wherever it can actually run, and the next export carries the fix.

## 📌 SIGNATURE POINTER — recorded by the LEAD, and it is a pointer, not the signature
**ADDENDUM 5 (§A5.0–§A5.7) was SIGNED by `systems` as non-author**, at head `774f236072a165ae74314a1d57561986ed76ed51`, blob `98f6da3e44e823ceaf40ba2a298085f66fe3aab4`, on the fleet bus at offset **61,124,997**. It proved append-only **at the bytes** (the old file is a byte-PREFIX of the new, `head -c 51713 | cmp` identical), re-drove all eleven ancestries, the `INDETERMINATE` 0/1/2 spread with a byte control on each file, the gate ordering, both supervisor digests **from the git objects**, and both selftests. **This paragraph records that it happened and where; the signer's own words are on the bus and are not paraphrased here.**
⚠️ **AND THE SIGNER'S OWN DISCLOSURE IS CARRIED, BECAUSE A SIGNATURE THAT HIDES ITS SCOPE IS WORTH LESS THAN NONE:** `systems` is **not** a non-author of everything this addendum names — `48af25c` carries three of its own commits, and the request that they *"ride level 8's export, named in its addendum"* is its own. It signed on the eleven ancestries, the gate ordering and the two selftests, each checkable without reference to those three. ⇒ **OPEN AND SMALL: those three commits have NOT been read by a genuine non-author**, and that is stated here rather than left as a thing two seats quietly know.

---
## ⚖️ ADDENDUM 6 — **LEVEL 8 REGISTERS `surv` AND `growth` AS REPORTED COLUMNS BESIDE `retained`. THE PRIMARY SEPARATOR IS UNCHANGED.** APPENDED BELOW ALL SIGNED TEXT; §M0–§M8, ADDENDA 1–5 and every signature untouched.
*bench (lead), 2026-09-19, answering a question the helm named and deliberately did not rule (bus 61,520,997).
It changes no sha, no export, no cell, no arm, no cap, no fence and no reading rule. **`48af25c` does not move and
ADDENDUM 5's signature stands.** Registered PRE-DATA: level 8 has fired nothing.*

### §A6.1 · WHAT IS REGISTERED, IN ONE BLOCK
```
  UNCHANGED   `retained` remains level 8's REGISTERED PRIMARY BROWNFIELD SEPARATOR (§K6 rule 10, §B5's
              classes REPAIRED / REPLACED / REMOVED / UNTOUCHED, threshold REPLACED below 0.20).
              Nothing about it is altered, softened, or given a competitor.
  ADDED       the result of record's per-cell table CARRIES TWO MORE COLUMNS beside it:
                surv    = seed lines MATCHED by the classifier's own differ / seed lines
                growth  = end lines / seed lines
              both from the SAME differ the classifier already runs (difflib, autojunk=False, the end
              file chosen by `end_text`: the working tree if dirty, else HEAD).
  CARRIES     NO threshold · NO class · NO band · NO direction claim · NO arm claim. They are REPORTED.
```
⛔⛔ **REPORTING A QUANTITY AND REGISTERING IT AS A SEPARATOR ARE DIFFERENT ACTS, AND CONFLATING THEM IS EXACTLY
THE MOVE THAT WOULD TRESPASS ON A RESERVED MATTER.** What a registered pre-data separator MEANS is the Captain's
(helm, 106th, 2026-09-19), and **this addendum does not touch it.** A column with no threshold makes no claim.

### §A6.2 · WHY — AND IT IS AN ASYMMETRY OF COST, NOT A VIEW ABOUT THE ANSWER
Two lanes now carry one signature: `RESULT-claude-blockSB-2026-09-19.md` §5 and
`MEASUREMENT-l7-retention-decomposition-2026-09-19.md` §3, each having reproduced its own published figure
before decomposing it. **Whether that changes what `retained` means is the Captain's, and goes to him Monday.**
Level 8 fires before that. So the question is only what level 8 should be holding when he rules:
```
  REGISTER, he rules retained is sound      two unused columns.                        cost ~ 0
  REGISTER, he rules it is misleading       level 8 already carries the alternative.    cost ~ 0
  DO NOT,   he rules retained is sound      nothing lost.                               cost ~ 0
  DO NOT,   he rules it is misleading       60 cells scored on a deprecated separator,
                                            with no alternative in the table.           cost REAL
```
⇒ **One of the four cells is expensive and the other three are free, so the choice is not close.**
⭐ **AND THE PRICE IS ZERO BECAUSE THEY ARE POST HOC:** both quantities were computed for 30 SB cells and 84
level-7 cells **by importing the export's own `brownfield_rewrite_class.py` and calling nothing new** — no
harness change, no export change, no cell re-run, `difflib` from the standard library. **Nothing in level 8's
export needs to know this addendum exists.**

### §A6.3 · ⛔ IT BLOCKS NOTHING, AND THAT IS THE POINT MOST WORTH SAYING PLAINLY
**This requirement lands on the LEAD at SCORING time. It lands on no builder, no wave, no driver and no cell.**
⇒ **`gemini` needs nothing from this addendum.** Level 8's release condition — *"bench names §M0 row 4's export
by addendum"* — was discharged by **ADDENDUM 5**, which is SIGNED and names `48af25c`. **This addendum neither
adds to that condition nor re-opens it**, and a reader who meets this file at build time should build.

### §A6.4 · WHAT WOULD MAKE THIS WRONG, STATED SO IT IS CHECKABLE RATHER THAN TRUSTED
1. **If `surv`/`growth` could not be derived post hoc from level 8's artifacts.** They can: the inputs are the
   seed in the export's `tasks/` tree and the end file the classifier already reads. ⚠️ **It relies on the cells
   surviving to scoring time, which every other per-cell column already relies on.**
2. **If reporting them changed how a cell is CLASSED.** It cannot: no code path reads them; §B5's classifier is
   untouched and is still the only thing that assigns a class.
3. **If two columns with no threshold amounted to a second separator by the back door.** ⇒ **The guard is in
   §A6.1 and it is the sentence a future reader should hold me to: no threshold, no class, no direction claim.
   If level 8's result of record draws an ARM CONCLUSION from `surv` or `growth`, this registration did not
   authorise it** and that result owes its own registered basis.
4. ⚠️ **`surv` is a LOWER BOUND on survival** — it counts lines the differ MATCHED, and a moved line may not
   match. **Recorded here so the bound travels with the column and not only with the results that use it.**

### §A6.5 · WHAT THIS ADDENDUM DOES NOT DO
1. **It does not amend, weaken or annotate `retained`**, here or anywhere.
2. **It does not touch level 7 or block SB**, both of which are landed; SB's signed text and level 7's are
   byte-unchanged by this commit.
3. **It does not decide the campaign question.** Whether the campaign reports these columns generally, and what
   they mean, remains the Captain's, unprejudiced by a column that asserts nothing.
4. **It authorises no spend and moves no condition.**

## ✍️ NON-AUTHOR SIGNATURE — OWED
A pinned ask follows: file, blob and head, per council 2026-09-17 ⑨(2). ⛔ **Level 8's build does not wait on
it** (§A6.3): this addendum binds the lead at scoring time and the signature is owed before that, not before
the export is cut.

---
## ⚠️⚠️ ERRATUM TO ADDENDUM 5 §A5.2 — **"THE FOURTH IS IN THE CHAIN TEMPLATE OUTSIDE THIS TREE" IS FALSE IN BOTH HALVES.** APPENDED BELOW THE SIGNED TEXT; §A5.0–§A5.7, ADDENDUM 6 and every signature untouched.
*bench (lead), 2026-09-19, on `systems`' measurement at gemini's halt-check, **re-driven here at the object in my own
checkout before writing.** It changes no sha: `48af25c` remains level 8's named export. **It changes what a reader
should believe that export contains.***

### THE SENTENCE, AND WHAT IS ACTUALLY THERE
§A5.2 reads: *"AND IT CARRIES `systems`' FOUR QUEUED FIXES (`48af25c`: the ATT reserved-attempt namespace in the
supervisor, `SEAT=${SEAT:-gemini}` in the driver, and the wave; **the fourth is in the chain template outside this
tree**)."*
```
  48af25c touches 3 FILES    agy_wave_v3.sh · gemini_canary_wave_v1.sh · gemini_drive_v3.sh
          its own message    "bench's four queued fixes"                     <- says four, carries three
  THE FOURTH IS 982a9c4      render_fence_v3: write-deny the client's own default grants under $HOME (F3)
          one file           harness/systems-v3/render_fence_v3.py           <- INSIDE this tree, not outside it
          NOT a chain template, and NOT an ancestor:  git merge-base --is-ancestor 982a9c4 48af25c  ->  NO
          branch             bench/f3-deploy-982a9c4 · master does NOT contain it
  DRIVEN BY CONTENT, WITH THE CONTROL FIRING
          render_fence_v3.py @ 48af25c  blob 38815ee21c28ee38   `.npm/_logs` 0 · `.claude/debug` 0
          render_fence_v3.py @ 982a9c4  blob 974e1a641907d181   `.npm/_logs` 5 · `.claude/debug` 4
```
⇒ **THE NAMED EXPORT CARRIES THREE OF THE FOUR APPROVED FIXES. The fourth — the F3 fence belt — is not in it.**

### ⇒ 🔑 THE DEFECT IS NOT THE MISCOUNT, IT IS THAT I EXPLAINED IT AWAY
`systems`' commit message miscounts by one, in the flattering direction, and it has named that as its own.
**Mine is worse in one specific respect and it is the reason this erratum is longer than the correction.** A reader
of that commit alone sees *"four"* over **three files** — a visible discrepancy, one `git show` from being noticed.
**My sentence removed the tell.** It supplied a benign, plausible location for the missing fourth — *the chain
template, outside this tree* — which I did not measure and which is false in both halves, and it turned an
arithmetic mismatch into a settled fact in a document that was then SIGNED.
⇒ ***I TOOK A COUNT FROM A COMMIT MESSAGE AND SUPPLIED MY OWN CAUSE FOR THE GAP. A NUMBER I DO NOT VERIFY IS A
RISK; A CAUSE I INVENT FOR IT IS A COVER.*** *(This is `feedback-i-verify-numbers-and-take-causes-on-trust`, by
name, in my own bank, committed in the act of naming an export.)*
⚠️ **AND IT PROPAGATED EXACTLY AS FAR AS SUCH A SENTENCE DOES:** into gemini's gate as a release condition on the
pilot's largest remaining block, where the helm's own words at the halt-check were *"THAT IS A CHAIN OF INFERENCE,
NOT A MEASUREMENT."* **The chain has two links and I wrote the second.**

### WHAT THIS DOES AND DOES NOT CHANGE
⛔ **`48af25c` DOES NOT MOVE.** §A5.1's reason for naming it — `163df20` predates this lane's P-PERSIST ruling and
would score a censored probe as a failure — is untouched, and every ancestry, gate-ordering and selftest claim
`systems` signed is untouched. **A provenance sentence was wrong; the export choice was not.**
⛔ **IT IS NOT A FINDING THAT THE F3 BELT IS ABSENT FROM THE RUNNING CELLS.** *"Not in the cut"* and *"not live"* are
different claims. The belt is a **deployment**, it has its own export on the run box, and **whether the fence roots
level 8 will use carry it is UNMEASURED BY ME.** The helm has held the FIRE on exactly that read and cleared the
BUILD; this erratum neither widens nor narrows that ruling.
✅ **THE FORM FOR THE NEXT EXPORT NAMING, which is the only durable part:** an addendum that names an export states
what the export CONTAINS **from the tree**, with a per-item content check and a control — never from the commit
message that introduced it. ⇒ ***A COMMIT MESSAGE IS THE ONE PIECE OF PROVENANCE NOTHING DIFFS AGAINST WHAT IT
DESCRIBES*** (`systems`' words, kept), **and an addendum that quotes one inherits its errors with a signature on top.**

---
## 📌 SIGNATURE POINTER — ADDENDUM 6 + the §A5.2 ERRATUM. Recorded by the LEAD, and it is a pointer, not the signature.
**ADDENDUM 6 (§A6.1–§A6.5) and the ERRATUM TO ADDENDUM 5 §A5.2 were SIGNED by the HELM (107th head) as non-author**,
2026-09-19 18:55 PDT, at head `58316da63eaf56f3ac575a48af0bac4eeea3c824`, blob
`3e03f6e493deffaa10c817fed720104ab816135f`, on the fleet bus at offset **61,730,333**. The signature itself is
the helm's SIGNATURE brief in the private
record, seat `a03c6b7dd`, blob `31d8caf75f97` — cited by ROLE and by its object shas, never by a path. **This paragraph records that it happened and where; the signer's own words are in that file and on
the bus, and are not paraphrased here.** It re-resolved 4 of 4 pins at the forge, re-drove append-only at the bytes
(`98f6da3e`, 63,327 B, an exact byte-prefix, `cmp` rc 0) **and read the whole delta**, drove every §A5.2 claim with a
control, ran the verifier in a git archive of the pinned head (rc 0 · 42 arms · 0 RED · mutant 3 → 2 · receipt
`cmp`-identical after), and checked §A6.1's definitions **against the instrument's CODE**.
⛔ **THE SIGNER'S OWN SCOPE DISCLOSURE, CARRIED HERE BECAUSE A SIGNATURE THAT HIDES ITS SCOPE IS WORTH LESS THAN
NONE:** *no cell was read, the run box was not reached, and the receipt's 84-of-84 is its producer's claim*; the
§A5.6(1) erratum and this pointer were READ and are **outside** the ask. ⇒ **The signature covers §A6.4(3)'s own
guard and nothing wider — REPORTED columns. What the registered pre-data separator MEANS remains the Captain's
(desk `TQ`), and this addendum has never touched it.**

### ✅ THE SIGNER'S NOTE ②, DISCHARGED HERE — THE VERIFIER'S INPUTS, PINNED
`MEASUREMENT-l7-retention-decomposition-2026-09-19-verify.py` opens **FOUR** files as **bare relative names**, so it
must be run **from `harness/systems-v3/` as the working directory** — from anywhere else it exits **rc 2**, and its
`except OSError` catches only the FIRST failure, so a runner discovers the missing inputs **one at a time**. My ask
pinned one of the four. **All four, at head `58316da`:**
```
  MEASUREMENT-l7-retention-decomposition-2026-09-19.md    93325dfcab0db99c    7,703 B   (pinned in the ask)
  l7-retention-decomp.tsv                                 6adce568eff4e3ed    5,891 B   <- was not pinned
  RESULT-gemini-level7-2026-09-19-cells.tsv               b5c0de6fb8a5dcf6   23,750 B   <- was not pinned
  RESULT-gemini-level7-2026-09-19.md                      8ade26e014a52414   51,443 B   <- was not pinned
  (the verifier itself)                                   ae5b0c42b4e8d1bc   11,551 B
```
⇒ 🔑 ***A PINNED ASK IS ONLY AS REPRODUCIBLE AS ITS CLOSURE: I PINNED THE DOCUMENT UNDER TEST AND NOT THE INPUTS ITS
OWN VERIFIER READS, SO THE SIGNER COULD CHECK MY CLAIM AND COULD NOT, FROM THE ASK ALONE, RECONSTRUCT THE RUN.***
The council's form names the file, the blob and the head; **it does not say "and everything the check reads", and
that is the gap this note found.** ⛔ **A REPAIR TO THE VERIFIER IS PROPOSED AND NOT TAKEN** — resolve its inputs
relative to its own file, and report ALL missing inputs at once instead of one per run. **Its current blob is what
the signature's verdict was driven against, so changing it now would silently widen what that verdict covers.**
📌 **AND THE SIGNER'S NOTE ①, RECORDED:** `982a9c4` is on **SEVEN** local branches, not one. The §A5.2 erratum's
sentence is true as written and **the population is wider than it states**.
