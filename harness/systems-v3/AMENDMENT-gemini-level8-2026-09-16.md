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
