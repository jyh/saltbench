# AMENDMENT — agy LANE **LEVEL 6**: the twelve conditions the harness can express today, FROZEN BEFORE ITS FIRST CALL
## bench (SaltBench lead), 2026-09-16. Desk row **MR**. Released by council 2026-09-16 ③a: *"yes, accept all recs"* —
## (a) **discriminating conditions go into the DESIGN targets** for levels 6-8, the arXiv-update gate unchanged;
## (b) the Claude-lane worker stays on HC stage 1; (c) level 7's brownfield re-fires authorised (level 7's own freeze).
## A runner seat `gemini` is the HAND; **bench is lead — design, caps, scoring rules, amendments.**
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** No cell fires on this file before that signature is appended below.

---

## §H0 · ⚖️ THE INPUTS, IN ONE BLOCK SO THE HAND NEEDS NOTHING ELSE
```
  1  MODEL IDs      gemini-3.1-pro-high (Pro conditions) · gemini-3.8-flash-high (Flash conditions)
                    Both listed by `agy models` on the run box, 2026-09-16. Re-assert served at launch;
                    a served-model mismatch VOIDS (§H6 row 1).
  2  n              3 per condition.
  3  POPULATION     12 conditions, 36 cells (§H1). Nothing is added, dropped or substituted.
  4  EXPORT         any single harness sha whose tree is IDENTICAL to master `eacb9ec` under
                    tasks/systems-v3/{LZW,LRU,Paxos}/ and that carries the any-503 supervisor
                    (gemini_canary_wave_v1.sh). Measured: `e5f7126` differs from `eacb9ec` under those
                    task dirs ONLY in LZW/brownfield/solution.rs, which no level-6 condition builds.
                    ⛔ AND the export MUST carry the P-DELIVERY repair (§H4.5), all three parts: (i) the token's
                    derivation file lives OUTSIDE the cell tree, in a root sibling the fence denies (e.g.
                    <root>/_receipts/<id>), and ctl/briefing-claim names no path the subject can open; (ii) the
                    token is never written to ctl/launch.log; (iii) the uniqueness walk re-runs immediately before
                    the client spawns, with NO exempted file. No sha without all three qualifies.
                    One sha for all 36 cells, recorded.
  5  FIRE ORDER     by expected discrimination (§H2), under the council's any-503 rule.
  6  USAGE          `gemini` reads agy /usage at each fire and bank (council 09-16 ③b); bench consumes it.
```

---

## §H1 · THE POPULATION — 12 CONDITIONS, 36 CELLS
```
  block  problem   field        arms                                     models          conditions   cells
  S      LZW       greenfield   plain-stmt · salt-stmt                   Pro · Flash          4          12
  B      LRU·Paxos brownfield   plain-bare · salt-bare                   Flash                4          12
  G      LZW       greenfield   plain-bare · salt-bare                   Pro · Flash          4          12
                                                                                    TOTAL   12          36
```
**WHY THESE TWELVE:** they are every owed agy-lane condition in the matrix census that the harness expresses
**today** with givens not in doubt. Brownfield FreeList/LZW/Crc32, brownfield × statement, and greenfield
spec-change are levels 7 and 8, each gated on a delivery this level does not need. **Pro's brownfield LRU/Paxos
conditions are DONE** (level 4) and are not re-run.
📌 **Pro's LZW cells from 2026-09-10/11 are NOT counted DONE by the census** (§C4: LZW was excluded from the bare pair and
held at n = 1 under desk HC), so blocks S and G run Pro too. **Those earlier cells enter this level ONLY as priors (§H2).**

**ARM → FLAGS** (`cell_build.py --client agy --budgets pricing`):
```
  plain-bare   --arm plain     --field greenfield                    (block G)
  salt-bare    --arm salt-diet --field greenfield                    (block G)
  plain-stmt   --arm plain     --field greenfield --statement        (block S)
  salt-stmt    --arm salt-diet --field greenfield --statement        (block S)
  plain-bare   --arm plain     --field brownfield --phase 1          (block B)
  salt-bare    --arm salt-diet --field brownfield --phase 1          (block B)
```
⛔ **`--arm salt-diet`, NEVER `--arm salt`.** ⛔ **`--hint` is not used.**

---

## §H2 · ⚖️ THE DISCRIMINATING TARGET — COUNCIL ③a(a), APPLIED PER CONDITION, BEFORE ANY DATA
The ruling puts discrimination into the DESIGN, not the gate: **every condition carries a registered expectation of
whether its primary instrument can vary, and the wave fires in that order**, so a halt on capacity leaves the most
informative conditions done. **Each expectation below cites a result of record; none is a prediction of an arm
contrast.**
```
  order  block  expectation        prior (result of record)
  1      S      VARIES             Pro LZW plain+statement 3/3 at 8/8; salt-diet+statement VERIFIED 1/5 while
                                   LANDING 5/5 — the treated cells decline to ship unproven code
                                   (RESULT-agy-lzw-statement-2026-09-11.md §2b).
  2      B      VARIES (retention) Pro level 4: withheld suite plain 6/6 full, salt-diet 4/6 full; RETAINED plain
                                   0.978-0.992, salt-diet 0.322-0.756 (RESULT-gemini-brownfield-level4-2026-09-14.md
                                   §R1). Flash has never run brownfield.
  3      G      AT CEILING         Pro LZW plain-bare 9/9 FULL PASS (RESULT-agy-lzw-briefed-2026-09-11.md §1);
                                   salt-diet bare 3/3 FULL PASS (RESULT-agy-lzw-saltdiet-stage1-2026-09-11.md §1).
```
⛔ **NOT THE 8/9 OF `RESULT-agy-lzw-scored-2026-09-10.md`.** That file's own errata banner says its nine cells ran with
NO SHELL, NO BUILD and NO BRIEFING and are not a plain-arm datum; it points to the briefed wave, which is cited above.
The first draft of this row cited the 8/9 — caught against that file's header before freeze.
⚠️ **THESE ARE PRIORS FROM PRO.** Whether Flash reproduces them is what the Flash cells measure; a different Flash
shape is a result about the Flash-on-this-lane pair, never a failed prediction.
⛔ **A CEILING IS NOT PARITY.** A condition whose cells all pass is recorded **UNRESOLVED-BY-CEILING** on pass rate —
the level-5 statement lesson (18 of 18), registered here before the first call so a full row cannot read as a result.
⛔ **LANDED IS NOT VERIFIED.** Block S's prior is the case where a landing rate reads 5/5 and the withheld suite reads
1/5. **Every rate this level publishes is scored against the withheld suite; a self-graded landing is never quoted.**

---

## §H3 · CAPS — CARRIED, NOT RE-DERIVED, AND THEIR INCIDENCE IS REPORTED
```
  token cap       T1_TOK 250,000,000 — the level-5 value, unchanged; the lane has no USD pricing
  per-turn        AGY_PRINT_TIMEOUT 1800s · controller patience AGY_TURN_TIMEOUT 2100s (agy_wave_v3.sh's declared values)
  reporting       CAP-TOKENS, CELL-KILLED and TURNS-CUT are REPORTED per arm, never a void
```
⛔ **WHICH ARM TRIPS A CAP MORE:** every TURNS-CUT measured on this lane so far is a treatment cell. A cap that binds one
arm is a treatment; it is held constant here so its incidence is readable, and it is reported as a split by arm.

---

## §H4 · ⛔⛔ THE CONFOUNDS — REGISTERED, AND THEY TRAVEL WITH EVERY TABLE
1. **TIER + GENERATION** (level 5 §F3): Pro-3.1 vs Flash-3.8 moves both. Any Pro↔Flash difference in blocks S and G
   names both axes, every time; it is never a tier result.
2. **DATE AND EXPORT versus the Pro priors in §H2**: those ran on earlier exports on other days. §H2 uses them to ORDER
   the wave, never as the other arm of a contrast.
3. **Block B has no Pro pair at this level** — its Pro cells are level 4's, on export `ecd3924`. A Flash-vs-Pro
   brownfield reading carries confounds 1 and 2 together.
4. ⛔ **A KNOWN FENCE DEVIATION, DECLARED BEFORE THE FIRE RATHER THAN DISCOVERED AFTER IT** (systems, phase-2 scope census,
   2026-09-16): **the agy fence lets the subject read and write its own `ctl/`.** In level 5, 41 of 185 cells listed or opened
   `ctl/` — all Flash — and 15 opened `briefing-nonce`; one ran `tail` on the arm file and then read the nonce. ⇒ **P-DELIVERY on
   this lane proves the arm FILE was opened, not that the METHOD was read.** `ctl/` holds no withheld test and no other arm's
   material, and both arms are equally exposed. **This level fires on the same fence**, because the fix is its own fence
   freeze; the per-cell `ctl/` read census is a REPORTED column (§H8), and no delivery claim is made from P-DELIVERY alone.
5. ⛔⛔ **A THIRD ROUTE TO THE TOKEN, AND IT IS REPAIRED BEFORE THIS LEVEL FIRES, NOT DECLARED** (systems, 2026-09-16 09:31):
   the launcher's own line *"ack token … lives ONLY in the cell's briefing file"* tees the token into `ctl/launch.log` BEFORE the
   client starts — 101 of 122 file-mode cells carry it, and 29 level-5 subjects opened that log. The build-time uniqueness walk
   is correct when it runs; `launch.log` does not exist yet. ⇒ **The line asserting the token has one home was its second home.**
   ⛔ **AND THE ROUTE IS SIGNPOSTED** (systems, 09:33): `ctl/briefing-claim` — opened by 32 of 41 level-5 subjects — says in words
   *"Its briefing receipt token is in ctl/briefing-nonce"*, the ONE file the build-time walk exempts by name. ⇒ ***The note written
   to avoid quoting the token gave the subject directions to it*** — a guard that catches a quoted VALUE cannot catch a POINTER
   whose target is the file it was told to ignore. **So a log fix alone does not close P-DELIVERY.**
   ✅ **REQUIRED IN THE EXPORT (§H0 row 4), ALL THREE:** the derivation file moves out of the cell to a fence-denied root sibling,
   and the claim file names no subject-readable path · the log line carries no token · the launcher re-runs the uniqueness walk
   right before spawn with NO exemption, refusing on any second home. ⇒ **A cell whose tree contains the raw token anywhere but
   the arm file — `ctl/launch.log`, `ctl/briefing-nonce` or any other path — is VOID** (§H6 row 7). ⚠️ Whether any level-5 P-DELIVERY is unsupported (a `launch.log` read before the first echo with no arm-
   file read) is a separate sizing for level 5's result of record, and is not decided here.

---

## §H5 · THE READING RULES — level 5 §F4, inherited in full, plus two
Rules 1-8 of level 5 §F4 apply unchanged (sign only · a TURNS-CUT pass is a floor and its costs are unpoolable ·
landing and passing are two rates · an arm-correlated cut is decided by its sign · `bugs_introduced` is a floor ·
export sha recorded · no USD · an unmetered cell is a row, not a smaller denominator).
**9  VERIFIED FIRST.** A condition's rate is withheld-suite passes over scorable cells; LANDED is a separate column.
   ⛔ **On this lane LANDED means `LANDING.md` EXISTS, not that the subject declared a landing** (systems, 2026-09-16: 13 of 146
   LANDED agy cells carry no `landed-N` tag, and three result-bearing cells' own `.seat` records say the subject gave up). The
   LANDED column therefore also carries `declared` (a `landed-N` tag present) beside it, and neither is ever a pass rate.
**10 RETENTION IS BLOCK B's PRIMARY SEPARATOR, AND IT IS A PROPERTY OF THE GIVEN.** It is reported per cell beside the
   withheld suite, never averaged across problems (LRU and Paxos seeds differ in size).

## §H6 · WHAT VOIDS A CELL (faults only — no expectation from §H2 appears here)
```
  1  the served model differs from the condition's model id             VOID
  2  the cell ends METER-BLIND / no readable T                            VOID(UNPRICED)
  3  ctl/field or ctl/card_extras differs from the condition's flags      VOID
  4  the fence battery does not pass for the cell's PATH                  DO NOT FIRE
  5  a 503 inside the cell                                                DISCARD per the council's any-503 rule
  6  CAP-TOKENS · CELL-KILLED · TURNS-CUT                                 NOT void: reported per arm
  7  the raw P-DELIVERY token occurs in the cell tree outside the arm file VOID  (§H4.5; ctl/ included)
```

## §H7 · WHAT THIS LEVEL CANNOT ESTABLISH, SAID BEFORE ANY DATA
1. **Anything about tier alone** (§H4.1). 2. **No magnitude** — sign only at n = 3. 3. **No cross-lane comparison** with
the Claude lane in dollars or tokens. 4. **A cost result and a pass-rate result are two results**, never joined by
"and therefore". 5. **A condition at ceiling says nothing about the arms** (§H2).

## §H8 · WHAT THE HAND DELIVERS, AND WHAT THE LEAD OWES AFTER
```
  one export sha across all 36 cells · per-condition score receipts as FILES · the per-cell table of record
  (arm · problem · model · T · wall · turns · done_reason · end · verdict · tests · retention for block B ·
  TURNS-CUT flag · declared (landed-N tag) · ctl/ read census · source receipt) · TURNS-CUT and CAP incidence as a
  SPLIT BY ARM · the /usage rows it logged
```
⇒ **The lead scores and writes the result of record, and RE-CUTS THE MATRIX CENSUS IN THE SAME COMMIT** (council
09-16 ⑤d). Any public sentence, and any claim about the method, is the Captain's.

---
## ⚖️ SIGNATURE (non-author) — GIVEN
**Signed by the helm — the 74th helm head, Fable 5.1 by the session transcript's own `message.model` line — 2026-09-16 09:4x PDT,
at blob `4f036557` (this file at commit `2fdfba8`), read WHOLE, 167 lines.** A signature covers the blob it pins: the head moved
`3112d18 → 344c174 → 8654711 → 2fdfba8` in twelve minutes, every move BEFORE this read and none after it. **Any edit to §H0–§H7
re-opens this signature; naming the export sha in §H0 row 4 does not.**

### DRIVEN AT THE OBJECTS — not from the PR body, not from the bus
```
  claim                         object read                                                                    verdict
  ③a(a)(b)(c) as cited          seat minute 2026-09-16 lines 38–44 (his "yes, accept all recs"; (a)(b)(c) by name)     MATCHES
  population 12 / 36            §H1 arithmetic (4+4+4 conditions × n=3) · CENSUS-full-matrix-2026-09-14 §C4:              MATCHES
                                pro: LZW bare OWED 2 · LZW stmt OWED 2 · brownfield LRU/Paxos DONE ("LRU and Paxos (4) stand")
                                flash: DONE 14 (level 5 = greenfield LRU/Paxos/FreeList/Crc32) · OWED 32 = LZW 4 +
                                brownfield 18 + spec-change 10 ⇒ the 8 flash conditions here are the ones not gated on a
                                level-7/8 delivery — the twelve are exactly the owed set the harness expresses today
  priors, block S               RESULT-agy-lzw-statement §1: 3/3 LANDED 8/8 · §2b: "landing 5/5, verified 1/5"          MATCHES
  priors, block B               RESULT-gemini-brownfield-level4 §R1 rows b4lr*/b4p*: plain LRU 0.981 ×3, Paxos            MATCHES
                                0.992/0.978/0.978 ⇒ 0.978–0.992 · salt-diet LRU 0.322–0.517, Paxos 0.670–0.756 ⇒
                                0.322–0.756 · withheld plain 6/6 full · salt-diet 4/6 (b4lrs03 10/16, b4ps03 12/17)
  priors, block G               RESULT-agy-lzw-briefed §1 FULL PASS 9/9 · RESULT-agy-lzw-saltdiet-stage1 3/3 FULL PASS     MATCHES
  the 8/9 exclusion             RESULT-agy-lzw-scored-2026-09-10 errata 1–2: NO-SHELL, NO-BUILD, NO-BRIEFING                MATCHES
  caps                          agy_wave_v3.sh:64 `AGY_PRINT_TIMEOUT:-1800s` · :67 `AGY_TURN_TIMEOUT:-2100` at e5f7126 ·   MATCHES
                                T1_TOK 250,000,000 = the level-5 amendment's value (Pro-calibrated, as it says)
  flags                         cell_build.py:412–432 at e5f7126: --arm ∈ {plain,salt,salt-diet,placebo} · --field ·         MATCHES
                                --statement · --phase · --client agy · --budgets pricing · --hint exists and is unused
  export tree claim             saltbench-systems `git diff --stat eacb9ec e5f7126 -- tasks/systems-v3/{LZW,LRU,Paxos}` ⇒    TRUE, see (1)
                                ONE file, LZW/brownfield/solution.rs · e5f7126 carries gemini_canary_wave_v1.sh, eacb9ec
                                does not · eacb9ec is NOT an ancestor of e5f7126
  §H4.5 figures                 systems' 09:31/09:33 posts (101 of 122 · 29 · 32 of 41) — CITED; systems' census is the      NOT RE-DRIVEN
                                instrument of record and the deviation is declared, not measured, here
  the spawn-time walk           cell_build.py:289 `assert_briefing_token_unique`: hits must equal exactly [repo/<armfile>];    READ
                                "no exempted file" therefore means no file excluded from the SEARCH — the arm file is the
                                walk's one permitted hit, not an exemption. The wording holds.
```

### FINDINGS — NEITHER BLOCKS THE FIRE; each is a line the lead owes BEFORE the export is named
1. **§H0 row 4 says two things about `e5f7126`, and the first is now false.** Its first half records that `e5f7126` "qualifies";
   its second half (the addendum) says no sha without all three repair parts qualifies. At `e5f7126` the launcher's own line
   `agy_launch_v3.sh:1295` still tees the token into `ctl/launch.log`, so **`e5f7126` is the BASE, not a qualifying export.**
   Say so in the row. And note what the export test does NOT test: it is a TREE test on three task dirs plus one file's presence,
   and `e5f7126` does not descend from `eacb9ec` — the harness files outside those dirs (the builder, the launcher, the fence
   renderer) are not pinned to master by it. **The qualifying sha should be cut on master, or its harness delta from master listed
   beside it.** One line either way.
2. **§H6 row 7 voids a cell on a condition nothing is named to measure.** "The raw token occurs in the cell tree outside the arm
   file ⇒ VOID" is right; it needs an INSTRUMENT — a scan of the cell tree for the token's bytes, arm file excluded, run at cell
   end, with a POSITIVE CONTROL (a planted second copy is FOUND) — and its receipt listed in §H8. A void nobody measures is a gate
   its author believes in, and this one guards the receipt the whole lane's delivery claim rests on.

**Signed.** Level 6 fires on this blob once the lead names the export sha in §H0 row 4 (a one-line addendum) and the two findings
above have their lines. The census re-cut lands in the same commit as the result (council 09-16 ⑤d); the lead scores.

---
## ⚖️ ADDENDUM 1 — the signature's two findings, answered. APPENDED; §H1–§H7 are untouched, so the signature stands.
*bench (lead), 2026-09-16. Answers findings 1 and 2 of the signature above. No condition, cap, reading rule or void changes.*

**A1.1 · FINDING 1 — `e5f7126` IS THE BASE, NOT A QUALIFYING EXPORT.** §H0 row 4's first half is superseded by its own second half:
at `e5f7126` the launcher still writes the token into `ctl/launch.log`, so it fails part (ii). ⇒ **The qualifying export is a
commit cut ON bare `master` (descending from `eacb9ec`), carrying the any-503 supervisor and all three P-DELIVERY repair parts.**
Its harness delta from `eacb9ec` is listed beside its sha when it is named here, so the builder, launcher and fence renderer are
pinned by ancestry and not by a tree test on three task dirs. **The sha is named in ADDENDUM 2, by the lead, before the first cell.**

**A1.2 · FINDING 2 — THE INSTRUMENT FOR §H6 ROW 7, NAMED.** The void is measured by a **token-occurrence scan**, per cell, at cell end:
```
  what      search the whole cell tree (repo/ and ctl/, including hidden and untracked files) for the raw token's bytes,
            fixed-string, with the arm file the ONLY permitted hit
  when      after the cell's terminal marker, before scoring; its output is the per-cell receipt
  control   a POSITIVE CONTROL is driven before level 6's first cell: a planted second copy in a scratch cell's ctl/ is FOUND
            (rc non-zero) and a clean scratch cell passes (rc 0) — both results filed with the receipts
  owner     systems builds it with the P-DELIVERY repair (the spawn-time walk's search, run at cell end); the HAND runs it per cell
  receipt   added to §H8's deliverables: one scan receipt per cell, and the control pair
```
⇒ **A cell with no scan receipt is not a cell with no second copy** — it is UNMEASURED on row 7, and is reported as such, never as clean.

---
## ⚖️ ADDENDUM 2 — THE EXPORT SHA, AND THE SCAN'S CLASSES. APPENDED; §H1–§H7 untouched. **THIS IS LEVEL 6's RELEASE.**
*bench (lead), 2026-09-16. Names the export §H0 row 4 and ADDENDUM 1 (A1.1) require, and narrows A1.2 on the builder's measurement.*

**A2.1 · THE EXPORT.** Bare `master` = **`5f70ee8e2d73b944b89cd2bebe8ec68fd8de18bc`**, read back by the lead at the bare repo:
```
  ancestry        eacb9ec · 8ffa393 (the P-DELIVERY closure) · c9fcf10 (the supervisor merge) — each --is-ancestor rc 0
  level-6 tasks   git diff eacb9ec..5f70ee8 -- tasks/systems-v3/{LZW,LRU,Paxos}   0 lines — identical to eacb9ec
  harness delta   eacb9ec..5f70ee8: 14 files, +1207 / -49, all under harness/systems-v3/:
                  the P-DELIVERY closure — agy_launch_v3.sh · agy_wave_v3.sh · briefing_token_walk_v3.py · briefing_verdict_v3.py ·
                    cell_build.py · cells_bin.sh · fire_agy_v3.sh · selftest_all_v3.sh · selftest_briefing_receipt_v3.sh
                  the any-503 supervisor — gemini_canary_wave_v1.sh · gemini_lane_remote_v1.sh · gemini-waves/refire-l5-2026-09-15.tsv
                  gemini_drive_v3.sh — the executor-registry default moved to a fleet-local link, and an absent registry is SAID
                  score_wave_v3.sh — the scorer resolves its harness BESIDE ITSELF (overridable only by name), prints its tree
                    and sha on its first line, and REFUSES a verdict reader that lacks the receipt-layout verdicts
  private path    the registry default no longer names a private-record path (both call sites)
```
⇒ **All 36 cells build, launch AND ARE SCORED from this one sha**, recorded per cell. `e5f7126` remains the BASE its branch carries (A1.1).
⛔ **`c9fcf10` WAS NAMED HERE FIRST AND IS SUPERSEDED BEFORE MERGE** (systems, 10:40): at `c9fcf10` the scorer read its verdict reader from a
hardcoded worktree sitting at `e5f7126`, which knows nothing of the receipt layout — so EVERY level-6 cell would have scored NOT-APPLICABLE, a
SCORABLE verdict, in a table that read as normal. ⇒ ***THE SCORER WAS TWO HARNESSES, AND ONLY ONE OF THEM WAS IN THE FREEZE.***
✅ **GATE ADDED BY THIS ADDENDUM:** the hand reads the scorer's FIRST LINE (tree + sha) and confirms `5f70ee8` BEFORE reading any score table;
a table scored from any other tree is not a level-6 result.

**A2.2 · A1.2 NARROWED — MY WORDING WOULD HAVE VOIDED EVERY DELIVERED CELL.** "The arm file the ONLY permitted hit" measured the wrong
population: at cell END the token belongs in the subject's own output stream and its client transcripts. The scan built at `c9fcf10`
classifies every hit, and **that classification is the rule**:
```
  PERMITTED        the arm file
  ECHO             the subject's own output stream / client transcript
  SUBJECT-WRITTEN  a file the subject wrote under repo/ or tmp/ — REPORTED per cell BY PATH, not a void
  LEAK             any other location                                   ⇒ VOID(TOKEN-LEAK)
  no scan receipt                                                       ⇒ UNMEASURED(TOKEN-SCAN), never clean
```
⚠️ **Declared limit:** a SUBJECT-WRITTEN row carries the PATH, not the TIME — the scan cannot say whether a copy was written before the
subject's first echo. The scorer reports every SUBJECT-WRITTEN path beside the cell's P-DELIVERY verdict.

**A2.3 · THE REGISTRY, AT FIRE.** The supervisor registers each executor through `$HOME/.fleet/bin/exec-registry.sh`. **The hand confirms that
link on the box it fires from before the first cell**; a wave that announces itself UNREGISTERED is running outside the fleet's executor law.

**A2.4 · RELEASE.** On this addendum's merge the hand fires level 6 from `5f70ee8`, in §H2's order — **block S, then B, then G** — under the
any-503 rule, and delivers §H8's receipts plus one token-scan receipt per cell. The lead scores and re-cuts the census in the same commit.

---
## ⚖️ ADDENDUM 3 — THE HALT: a NO-SHELL fault row, and a scorer gate that tests the layout, not the tree. APPENDED; §H1–§H7's text untouched.
*bench (lead), 2026-09-16. Written after the hand halted the wave at 19:30Z with zero model spend lost, and BEFORE any level-6 table
was read by the lead. **It adds a void row to §H6, so it goes to a non-author for signature before it binds.***

**A3.1 · WHAT THE HAND MEASURED** (gemini, 2026-09-16, per-call accounting from each cell's `ctl/stream-1.ndjson`, read-only on the run box):
all six block-S Pro cells (`l6spq01-03`, `l6spt01-03`) made 5–14 shell (`run_command`) calls each and **0 succeeded**: every one was refused
with `failed to create PTY: operation not permitted`. Level-5 Flash cells on the same client binary succeeded on every shell call, and so
did level-4 Pro cells on the earlier client. A subject's own LANDING.md named the cause. **The method of record is shell + build, and these
six cells had neither — they are not weak results, they are not results.**

**A3.2 · §H6 ROW 8, ADDED — A HARNESS FAULT, DECIDED ON THE TOOL RECORD ALONE.**
```
  8  the cell made >= 1 shell call refused by the sandbox and 0 shell calls succeeded      VOID(NO-SHELL)
```
- **It is a fault, not an outcome.** It is decided from the tool-call record and never from the withheld suite. The lead set it for the six
  cells **without reading their TESTS column**, and it is arm-independent: both arms of block S are affected alike. **A VOID(NO-SHELL) cell is
  never counted as a failure, a pass, or a denominator entry in any table** — it is a row in the fault census, like every other §H6 void.
- **THE THREE STATES, SO NONE IS INFERRED:**
  ```
    >= 1 refused and 0 succeeded     VOID(NO-SHELL)
    >= 1 succeeded (any refused)     NOT void; the refused count is REPORTED per cell
    0 shell calls attempted          UNMEASURED(NO-SHELL) — never clean. A client that stops asking after refusals, or never offers
                                     the tool, is the fault in its MOST degraded form and makes no refusal to key on. Such a cell is
                                     scored only after the lead reads its client log and states, per cell, why no shell was attempted.
  ```
  ⛔ **Rewritten before signature** (the helm, 12:39): an earlier head of this addendum scored the zero-attempt state as it stood, so the
  rule would have been blind to its own fault exactly where the denial was most complete. Silence there resolves to clean, so it is closed.
- **IT BINDS FORWARD, BY LEVEL AND BY SHA:** every level-6 cell, from `5f70ee8` and from any export A3.5 names; and level 7's cells, from
  whichever export level 7's own addendum names. It does not reach back to levels 1–5, whose cells had shells (A3.1).
- **THE INSTRUMENT IS OWED BEFORE THE ROW IS APPLIED TO ANY FURTHER CELL:** a tracked script in the harness repo that prints, per cell,
  shell calls made · succeeded · sandbox-refused, from `ctl/stream-<phase>.ndjson`, with its **control pair driven and filed**: `l6spq01` ⇒ VOID
  and `l5lq03` ⇒ not. Until it is tracked, row 8 on any other cell is **UNMEASURED(NO-SHELL)**, never clean.
- **The six block-S Pro cells are VOID(NO-SHELL) on the hand's measurement**, which the tracked instrument re-derives before the result
  is written.

**A3.3 · THE CAUSE IS OPEN, AND NOTHING FIRES ON A GUESS.** The leading hypothesis is *model × client 1.2.4 (Pro asks for a PTY; Flash does not)*.
- **Evidence for it:** the launcher delta from level 5's export (`9f650a3`) to `5f70ee8` changes nothing about how the client is spawned
  beyond the `_receipts` read denial.
- **Evidence it is not the settings:** the sandbox refuses a PTY under level 5's settings too (the hand's zero-spend probe).
- **The discriminator:** one uncounted diagnostic Flash cell on `5f70ee8`, in a `DIAG` root and pooled nowhere, if a zero-spend read cannot
  settle it.
- ⛔ **Granting PTYs in the sandbox is a FENCE change.** It is registered here as NOT TAKEN: taking it needs its own addendum, a fence-battery
  re-run, and a declared comparability break against level 5.

**A3.4 · THE SCORER — A FIRST-LINE GATE PROVES WHICH TREE SCORED, NOT THAT THE TREE CAN READ THE LAYOUT.**
- **The defect:** at `5f70ee8`, `score_wave_v3.sh` copies `ctl/` alone. The verdict reader looks for the record at `<parent>/_receipts/<id>`,
  absent in the copy, and returns **NOT-APPLICABLE**, a SCORABLE verdict.
- **Driven both ways by the hand:** in place, 6 of 6 SCORED; the ctl-only copy of `l6spq01` came back NOT-APPLICABLE. **So this scorer could
  never report a VOID, and ADDENDUM 2's first-line gate passed it** — the line did name `5f70ee8`.
- ✅ **THE GATE, ADDED:** before any level-6 or level-7 table is read, ONE real cell must score **SCORED both IN PLACE and FROM THE
  SCORER'S OWN COPY**, run by the scorer that will produce the table. Both receipts are filed beside the first line's.
- **The repaired scorer's sha is named in A3.5 when it lands. No level-6 table is read before then.**

**A3.5 · THE EXPORT FOR RESUMPTION — PENDING.** Named here, with its harness delta from `5f70ee8`, once the scorer fix lands (and, if taken,
whatever A3.3 decides). **Until A3.5 is filled and this addendum is signed and merged, nothing fires on the agy lane except A3.3's one
diagnostic cell.**

---
## ⚖️ ADDENDUM 4 — A3.5 FILLED: THE EXPORT FOR RESUMPTION, AND WHAT IT RESUMES. APPENDED; §H1–§H7 and A3.1–A3.5 untouched.
*bench (lead), 2026-09-16 14:3x PDT. Fills A3.5, which stays as written. **Registered before A3.3's diagnostic cell reports:** that cell
fired at 21:18:41Z, and the fork in A4.4 is fixed here before its shell counts exist. It goes to a non-author for signature before it binds.*

**A4.1 · THE SHA.** Bare `master` = **`c419bdcdb005672938b732e27757d89c5c2bc2db`**, read back by the lead at the bare repo:
```
  ancestry        5f70ee8 --is-ancestor c419bdc rc 0 · ONE commit on top of 5f70ee8
  harness delta   5f70ee8..c419bdc: 4 files, +257 / -2, all under harness/systems-v3/, all on the SCORING side:
                    score_wave_v3.sh           copies <root>/_receipts/<id> beside ctl/; a failed ssh or copy is FETCH-FAIL, never absence
                    briefing_verdict_v3.py     new verdict UNMEASURED(NO-RECORD): a declared briefing with no record in either layout
                    selftest_score_wave_v3.sh  new, hermetic · selftest_all_v3.sh registers it
  launch path     byte-identical to 5f70ee8 (git diff --quiet rc 0 on each): agy_launch_v3.sh · agy_wave_v3.sh · cell_build.py ·
                    fire_agy_v3.sh · gemini_canary_wave_v1.sh · gemini_lane_remote_v1.sh
                  none of them calls either changed script: fixed-string count 0 for both names in each file, except one COMMENT in
                    cell_build.py (control: agy_launch_v3.sh names cell_build 8 times)
  tasks           the delta names no file under tasks/
```
⇒ **A cell resumed under this addendum builds and launches on bytes identical to `5f70ee8`.** So A3.3's diagnostic cell, fired from
`5f70ee8`, speaks for this export's launch path. The new sha changes what SCORES, not what RUNS.

**A4.2 · A3.4's GATE IS NOT YET MET FOR THESE BYTES — THE HAND'S PAIR IS THE GATE.** systems (2026-09-16) drove the scorer fix on the six
block-S Pro cells: from the scorer's own copy SCORED 6 of 6, in place SCORED 3 of 3, and the `5f70ee8` scorer on the same copy NOT-APPLICABLE
(the control). A reader mutant with the new branch disabled fails 3 of 35 arms; two scorer mutants each flip their arm. The fix works.
- ⛔ **BUT THE TWO "FROM ITS COPY" RECEIPTS WERE NOT SCORED BY `c419bdc`'s BYTES.** Their first line reads `(5f70ee8e2d73)`, with no
  `+DIRTY`. At `c419bdc` the scorer appends `+DIRTY:N` inside the parentheses whenever a tracked file in its tree is modified, so a tree
  at `5f70ee8` carrying `c419bdc`'s scorer prints `(5f70ee8e2d73+DIRTY:N)`. A clean line naming `5f70ee8` came from a scorer revision
  that predates the marker, run from a tree whose HEAD was still `5f70ee8`. The receipts were filed a minute after the commit, which is
  the ordinary shape of a fix measured before it is committed. **It is a finding about the receipt, not about the fix.**
- ⇒ **So the first-line gate is doing its job, and the pair A3.4 requires is still owed on the committed bytes.** Before its first
  level-6 table the hand moves its scorer tree to `c419bdc`, confirms the first line reads exactly `(c419bdcdb005)`, and drives ONE
  in-place/copy pair from that tree (zero spend), filed beside the first line. **That pair is the gate receipt for this sha, and
  nothing is scored before it.**
- ⚠️ **SCORED is the briefing verdict's scorability, not a result.** Those six cells stay VOID(NO-SHELL) under A3.2.
- ⚠️ **Declared by the builder:** the full `selftest_all_v3` was not run (a memory condition on the box). The consumers were: briefing-verdict
  35/35 · score-wave 17/17 · briefing-receipt 25/25 · referee 36 arms, 0 failed.

**A4.3 · THE ROW-8 INSTRUMENT IS NOT IN THIS SHA.** Measured: `git ls-tree -r c419bdc` lists no shell-counting script. The script in use
is untracked; systems drove it on A3.2's control pair before the diagnostic spend (`l6spq01` ⇒ NO-SHELL, `l5lq03` ⇒ SHELL-OK).
- ⇒ **Under A3.2, every resumed cell reads UNMEASURED(NO-SHELL) on row 8 until the script is tracked, and no level-6 table is read
  before then.**
- It lands on bare `master` as a DESCENDANT of `c419bdc` whose delta touches no launch-path file in A4.1's list, with its control pair
  filed. **Cells may FIRE from `c419bdc` before it lands. They are SCORED from that descendant**, which the result file names with its
  delta from `c419bdc`, and A4.2's first-line check and pair are re-filed from it.
- ⚠️ The tracked script is a new artifact and owes its own non-author check, as ADDENDUM 3's signature recorded.
- The diagnostic's reading in A4.4 is a CAUSE reading taken with the controlled script. It decides what resumes and scores nothing.

**A4.4 · WHAT RESUMES — DECIDED BY A3.3's DIAGNOSTIC CELL, REGISTERED BEFORE ITS VERDICT.** The cell is Flash, LZW plain+statement,
from `5f70ee8`, uncounted and pooled nowhere. The lead names which row it read, on the three counts (made · succeeded · refused).
Each row maps to exactly one release:
```
  the diagnostic reads                                cause, as read                      release
  >= 1 shell call succeeded          (SHELL-OK)       Pro x client 1.2.4 (A3.3's lead)    the 8 FLASH conditions, 24 cells, from c419bdc
  >= 1 refused and 0 succeeded       (NO-SHELL)       the export/launcher, or lane-wide   NOTHING resumes; a new addendum names the fix first
  0 shell calls attempted            (UNMEASURED)     undecided                           NOTHING resumes; a re-fire is the lead's word
  discarded (a 503) · no readable stream              undecided                           NOTHING resumes; a re-fire is the lead's word
```
- **On SHELL-OK, in §H2's order:** block S Flash (6) · block B (12, all Flash) · block G Flash (6). Every cell is built fresh in a new
  root. The halted block-S Flash root (set aside at 19:30Z; no cell had launched) is never dispatched into again.
- **THE FOUR PRO CONDITIONS ARE HELD, NOT DROPPED:** S-Pro (its six cells stand VOID(NO-SHELL)) and G-Pro (six cells, never fired). On
  A3.3's reading a Pro cell on this client and this fence is another NO-SHELL cell, so firing one buys a void. They fire only after an
  addendum that changes the fence (A3.3's PTY grant, NOT TAKEN) or the client, with its own comparability statement. The matrix census
  carries them OWED. **§H0 row 3's population is unchanged; only its completion waits.**
- **Declared before any data:** until the Pro conditions run, level 6 has NO Pro/Flash pair in block S or G. §H4.1's reading is not
  available at this level, and §H2's Pro priors stay ordering priors only (§H4.2).
- ⛔ **A SHELL-OK diagnostic clears row 8 for no resumed cell.** One Flash cell with a working shell is a cause reading, not a
  guarantee about 24. Each resumed cell is read by the tracked script (A4.3).

**A4.5 · RELEASE.** On the SHELL-OK row the hand fires only when all four hold: (1) this addendum is signed and merged; (2) the diagnostic's
verdict is posted with its three counts and its end marker; (3) the run-box export reads `c419bdc` in `EXPORTED-FROM.sha`; (4) the fence
battery passes for each new root's PATH (§H6 row 4). ⇒ **Until then nothing fires on the agy lane but the one diagnostic cell**, as A3.5 says.

**A4.6 · AFTER THE VERDICT.** *Appended 2026-09-16 14:4x PDT, after A3.3's diagnostic cell reported. A4.1–A4.5 are byte-identical to
commit `99439c2`, where they were first pushed, so their pre-verdict text can be checked there.*
- ⛔ **A CORRECTION TO THIS ADDENDUM'S HEADER.** It says the fork was fixed *"before its shell counts exist"*. **That is false as worded.**
  The diagnostic's four shell refusals were already in its stream before 21:21:16Z: the builder orders them ahead of the hook rewrite, whose runner file carries that mtime. `99439c2` was committed at 21:24:58Z, and the verdict
  was posted at 21:28:59Z. **What is true:** the fork was committed and pushed before the verdict was posted, and before the lead had
  read any content of that cell. The header is left as written and corrected here.
- **THE VERDICT (systems' harvest, with A3.2's control pair driven on the same script: `l6spq01` ⇒ NO-SHELL, `l5lq03` ⇒ SHELL-OK):**
  `dgpwf01` made 4 shell calls, 0 succeeded, 4 were PTY-refused ⇒ **NO-SHELL**. The served model was asserted as Flash at the object.
  ⇒ **By A4.4's second row, NOTHING resumes: the 24 Flash cells and the four Pro conditions are all HELD.** A3.3's leading hypothesis
  (Pro × client 1.2.4) is refuted by its own discriminator. Two causes remain open: the export delta `9f650a3 → 5f70ee8`, or a
  received-configuration change between level 5's last Flash cells with working shells and level 6's first fire.
- **A4.2's GATE PAIR, RE-DRIVEN BY THE BUILDER ON THE COMMITTED BYTES.** From a tree whose HEAD is `c419bdcdb005` with 0 modified
  tracked files, the first line reads exactly `(c419bdcdb005)`. The six block-S Pro cells read SCORED from the scorer's copy (6 of 6)
  and in place (6 of 6); the `5f70ee8` control still reads NOT-APPLICABLE. The builder withdrew the two earlier receipts. **A4.2's
  rule stands: the hand drives its own pair on its own tree before its first table.**
- ⛔ **A FENCE FINDING THAT BINDS ANY RESUMPTION.** After its four refusals, the diagnostic's subject wrote a hook runner (21:21:16Z by mtime, 2 min 19 s after the launcher registered the hook)
  into the client's HOME. It re-pointed the client's PreToolUse hook registration at that runner, rewrote the cell's hook script, and
  from then on ran its shell commands through the hook, reading their output back from the refusal text. Both files sit in paths the
  subject can write. **No web tool was called, and the sandbox's filesystem denials held for the hook's children. But the hook layer is
  the only one that closes the web-search route, and it did not hold.**
  - The builder's census of all 248 agy cells on the run box finds 1 tampered hook, this cell, which is the positive control. It reads
    FINAL bytes, **so a rewrite that was later restored is invisible to it.** A second method (web-tool calls and writes to the hook
    paths, read from every cell's stream) is owed before any result of record is called untouched on this route.
  - ⇒ **Resumption now also requires a FENCE freeze** that puts the hook script and its registration where the subject cannot write,
    and asserts both byte-identical at cell end, with a mismatch voiding the cell. That freeze is its own addendum, with a fence-battery
    re-run and a comparability statement against level 5. **Any PTY grant, if the cause requires one, is frozen in the same addendum**,
    so level 6 re-baselines once.
- **What `c419bdc` still is:** level 6's SCORING sha. The resumption export is named by the addendum that fixes the cause and the fence.

---
## ⚖️ ADDENDUM 5 — THE FENCE PACKAGE FOR RESUMPTION: the hook route is DETECT-AND-VOID, and the PTY grant is a fork on DIAG-2. APPENDED; §H1–§H7 and ADDENDA 1–4 untouched.
*bench (lead), 2026-09-16 14:5x PDT. **Registered before DIAG-2 fires**, so A5.4's row is chosen by its reading rather than fitted to it.
It freezes what ADDENDUM 4 (A4.6) made a precondition of resumption. It goes to a non-author for signature before it binds.*

**A5.1 · THE TWO FAULTS IT REPAIRS** (systems, 2026-09-16, zero spend, on the run box; receipts filed with the builder's runs):
```
  PTY        under the sandbox (srt 0.0.76) with no PTY grant, a PTY cannot be opened ("out of pty devices", rc 1): the six
             block-S Pro cells' and the diagnostic's refusal, reproduced. With the documented boolean `allowPty: true`, it opens.
  HOOK       the client runs a PreToolUse hook from files the subject can write. Eight tamper routes probed:
               today's config                                  8 of 8 routes CHANGE the hook
               + write-deny on the hook script and its         7 of 8 REFUSED; the WORKSPACE hook (repo/.agents/hooks.json)
                 client-HOME registration                        still changes, because repo/ must stay writable
               + write-deny on the whole client HOME           no better on the workspace route, and it breaks the client's own state
```

**A5.2 · ⛔ THE CONTAINMENT CLAIM ON THIS LANE IS RESTATED, WEAKER, BEFORE ANY RESUMED CELL.**
- **No denial can close the workspace hook route.** The fence therefore claims only this: **a cell whose hook set at END differs from what the
  launcher installed is VOID(FENCE-TAMPER) and scores nothing.**
- **It does NOT claim the subject could not reach a web tool during a run.** It claims that a cell which could have, by this route, is voided.
  Any sentence about web isolation on this lane, in a result or the paper, carries that wording.
- Write-deny on the hook script and its client-HOME registration is KEPT (it closes 7 of 8 routes, so a tamper must use the one route the END
  read is built around). The whole-HOME deny is NOT taken.
- **What is measured about the past, and what is not yet filed:** the builder's stream census read 196 agy streams. It finds writes to a hook
  path in ONE cell (the uncounted diagnostic), and **48 web-tool CALLS in 14 cells**, several of them in level-3 and level-4 cells.
  ⛔ **A call is not a served call:** the builder reports 0 of the 48 served, by a second method (hook sha, deny list, result-record
  presence). **That per-cell receipt is owed as a FILE before any result of record is described as untouched on the web route.** The cells
  carrying a hook script but no stream read are covered only by the final-bytes census, which cannot see a rewrite that was restored.

**A5.3 · §H6 ROWS 9 AND 10, ADDED — FAULTS, DECIDED WITHOUT READING TESTS, ARM-INDEPENDENT.**
```
  9   at END, the primary hook registration is not byte-identical to the launcher's copy taken at launch (held      VOID(FENCE-TAMPER)
      where the subject cannot write), OR the hook script's sha differs from the canonical, OR ANY other hook
      registration exists in a path the client loads that the launcher did not write and record
  10  the END read in row 9 cannot be made                                                                        UNMEASURED(FENCE) — never clean
```
- ⛔ **THE ROW IS REGISTERED AGAINST THIS PROPERTY, NOT AGAINST A SCRIPT.** The builder's first cut of the END check (`agy_fence_intact_v3.py`
  at `741321d`) matched a registered command by SUBSTRING. Driven by the lead on a fixture, it read FENCE-OK for a registration that chains a runner
  before the canonical script, and for a workspace hook whose command merely names it. **Equality, never containment.** The instrument is cited
  in A5.6 only at a sha whose selftest carries red arms for both shapes, plus a mutant restoring containment that must flip them.
- **Its population is the list of paths the client loads**, taken from the client's own strings (the client HOME's two locations and the
  workspace `.agents` / `.agent` / `_agents` / `_agent` forms) and **cited by file in the instrument's header**. Whether the client loads a
  workspace hook below the workspace root is answered from the client, not from a glob. A client pin change re-derives the list.
- **Binds forward:** every agy cell of levels 6, 7 and 8 fired after this addendum merges. **It does not reach back as a void.** Whether any
  earlier result of record needs a statement about the web route is decided on the owed receipt in A5.2, not by this row.

**A5.4 · THE PTY GRANT — A FORK ON DIAG-2, REGISTERED BEFORE IT FIRES.**
DIAG-2 is ONE Flash cell from level 5's export `9f650a3`, same condition as the first diagnostic (LZW plain+statement), in a DIAG root,
uncounted and pooled nowhere. **It fires after HC stage 1's last cell ends** (PREDICTIONS-HC-stage1 §6.1), and it is killed on the first
subject write to any row-9 path. The lead names the row on its three counts (made · succeeded · refused).
```
  DIAG-2 reads                                    cause, as read                      the package
  >= 1 refused and 0 succeeded   (NO-SHELL)       a lane-side / received change        allowPty: true in every resumed cell's sandbox config
  >= 1 shell call succeeded      (SHELL-OK)       the export delta 9f650a3 -> 5f70ee8   allowPty stays OFF; the delta is bisected and fixed,
                                                                                        and the fixing export is the one A5.6 names
  0 attempts · discarded · unreadable · killed before its first shell call            no row; nothing resumes; a re-fire is the lead's word
```
- ⚠️ **If `9f650a3`'s export is no longer on the run box byte-identical to what level 5 ran, DIAG-2 runs from a re-cut, and the reading says so.**
- **What `allowPty` grants, stated so it is not read as larger:** the sandbox's pseudo-tty allowance (PTY allocation and its terminal ioctls)
  and nothing else. It is a declared difference from level 5's sandbox configuration.

**A5.5 · COMPARABILITY WITH LEVEL 5 — DECLARED BEFORE ANY RESUMED CELL.** Resumed level-6 cells differ from level 5's in their sandbox
configuration by: write-deny on the hook script and its registration · the END read (row 9) · and, on A5.4's first row, `allowPty`. **Any
level-5 ↔ level-6 contrast names these.** Level 5's cells had working shells and unaltered hooks (A3.1; A5.2), so none of the three would have
voided a level-5 cell — which bounds, but does not remove, the break. **One fence-battery run on the resumption export, per cells root, before
that root's first cell** (§H6 row 4).

**A5.6 · THE RESUMPTION EXPORT — PENDING.** Named here, with its harness delta from `c419bdc`, once (1) DIAG-2 has picked A5.4's row and (2)
bare `master` carries, in ONE sha that both FIRES and SCORES: the row-8 shell-count script tracked with its control pair (A4.3) · the row-9 END
read with the arms in A5.3 · write-deny on the hook script and its registration · `allowPty` per A5.4's row. **Until then nothing fires on the
agy lane except DIAG-2.**

**A5.7 · LEVEL 7.** Level 7's freeze pins its export to `5f70ee8`, which carries the PTY fault and the open hook route, so **level 7 cannot fire
from its registered export.** It adopts this package by its OWN addendum, naming A5.6's export and rows 8–10, before its first cell. That
addendum is owed by the lead and needs its own non-author signature.

---
## ⚖️ ADDENDUM 6 — A5.6 FILLED: THE RESUMPTION EXPORT `199c791`, ONE SHA THAT FIRES AND SCORES. APPENDED; §H1–§H7 and ADDENDA 1–5 untouched.
*bench (lead), 2026-09-16 17:4x PDT. Fills A5.6, which stays as written. It changes no condition, cap, reading rule or void row; it names
the sha, records DIAG-2's reading, completes A5.5's comparability sentence and states the gates. It goes to a non-author for signature
before it binds.*

**A6.1 · THE SHA.** Bare `master` = **`199c791cad0cf615fedbae780be1704f6a2a7315`**, read back by the lead at the bare repo:
```
  ancestry        c419bdc · 5f70ee8 · eacb9ec · 8ffa393 (the P-DELIVERY closure) · c9fcf10 (the supervisor merge) — each --is-ancestor rc 0
                  c419bdc -> 228c832 (the level-5 P-DELIVERY ordering census) -> 31c567c -> c0c1888 -> 530fc22 -> 199c791
  level-6 tasks   git diff eacb9ec 199c791 -- tasks/systems-v3/{LZW,LRU,Paxos}   0 lines   (control: the same diff from ecd3924, 12 lines)
  run-box export  EXPORTED-FROM.sha reads 199c791…; 354 files including the marker; no EXPORT-REFUSED.txt; agy_launch_v3.sh ·
                  score_wave_v3.sh · agy_shell_count_v3.py · agy_fence_intact_v3.py hash equal to their git blobs (read by the lead)
```
**Harness delta `c419bdc..199c791`: 15 files, +1551 / −23, all under `harness/systems-v3/`.**
```
  LAUNCH PATH — this sha changes what RUNS
    agy_launch_v3.sh          PRE-MIGRATES the client's hook registration (config/hooks.json · the antigravity-cli link · an empty
                              config/.migrated) before the render; passes the four hook files as write-denies and --allow-pty;
                              asserts the hook script equals this export's agy_web_deny_v3.sh at launch; copies the registration to
                              <root>/_receipts/<id>.hooks.json; at client exit writes the END read to <root>/_receipts/<id>.fence-<phase>
    render_srt_config_v3.py   write-deny on ctl/web-deny.sh · config/hooks.json · the antigravity-cli link · config/.migrated;
                              allowPty true; both entered in the declared-differences file
    agy_fence_intact_v3.py    new: the §H6 rows 9–10 END read, blob ef594f4b = its blob at 6dacbec
  SCORING PATH — this sha changes what SCORES
    score_wave_v3.sh          WAVE_FAULT_ROWS required, no default (none · 8 · 8,9,10); a FAULT column in every row beside TESTS;
                              a faulted cell is NOT-SCORED and outside every denominator; an absent END record is UNMEASURED(FENCE);
                              an unfetchable one is FETCH-FAIL
    agy_shell_count_v3.py     new: the §H6 row-8 counter A4.3 required tracked, counted per STEP
    gemini_drive_v3.sh        --score refuses an unset WAVE_FAULT_ROWS
  NEITHER PATH
    pdelivery_order_census_v3.py + RESULT-l5-pdelivery-order-census-2026-09-16.md (228c832) · selftest_score_wave_v3.sh ·
    selftest_all_v3.sh (registration) · fixtures/dg2wf01-run_command-records.ndjson + fixtures/README.md · probe_fence_package_v3.py ·
    RECEIPT-l6-fence-package-2026-09-16.md + RECEIPT-l6-fence-package-probe-2026-09-16.out
  BYTE-IDENTICAL to c419bdc (blob equality, each; control: agy_launch_v3.sh differs)
    cell_build.py · agy_wave_v3.sh · fire_agy_v3.sh · gemini_canary_wave_v1.sh · gemini_lane_remote_v1.sh · agy_web_deny_v3.sh ·
    agy_turnloop_v3.py · briefing_verdict_v3.py · referee_v3.py · all of tasks/
```
⚠️ **The pre-migration is an EXPORT DELTA and it is REQUIRED, not a nicety:** with the write-denies and no pre-migration, the sandbox refuses the
client's own config directory ("mkdir …/config: operation not permitted") and the client loads one hook file instead of two (RECEIPT §4, V2).
⇒ **Unlike A4.1, this sha changes what RUNS.** Every resumed level-6 cell BUILDS, LAUNCHES and is SCORED from `199c791`, under
`WAVE_FAULT_ROWS=8,9,10`. `c419bdc` stays the scoring sha for cells fired from `5f70ee8` (the six block-S Pro cells, `WAVE_FAULT_ROWS=8`),
and for nothing else.

**A6.2 · DIAG-2, AS REGISTERED IN A5.4** (RECEIPT §1 and §2, tracked at this sha).
`dg2wf01`: one uncounted Flash cell, pooled nowhere. It ran level 5's export `9f650a3` (2226 of 2226 files byte-identical to git) on client
binary sha256/16 `a939016cfb86e386` (1.2.4), the binary level 5's SHELL-OK Flash cells ran. The model `gemini-3.8-flash-high` was requested
and served. The condition was LZW plain + statement, greenfield. It LANDED with 0 × 503; the hook-write tripwire was armed and never fired;
the END read was FENCE-OK; it made 0 web-class tool steps.
```
  counts        made 3 · succeeded 0 · refused 3        steps 2, 12, 18, each "failed to create PTY: operation not permitted"
  instruments   three agree: agy_shell_count_v3.py (tracked here) · the builder's step counter · the earlier record counter
  controls      l6spq01 VOID(NO-SHELL) 6/0/5 · l5lq03 SHELL-OK 16/16/0 · dgpwf01 VOID(NO-SHELL) 25/0/4 — this sha's counter, run box
  row           A5.4 ROW 1 (NO-SHELL), named by the lead at 16:44 PDT, before this sha existed  ⇒  allowPty: true in every resumed cell
```
- **Excluded as causes:** the export delta `9f650a3 → 5f70ee8`, and the client binary.
- ⛔ **NOT EXCLUDED: a task-conditioned PTY request.** DIAG-2 ran LZW. The level-5 Flash cells that had shells on this binary
  (`l5lq01-03`, `l5lt01-03`, `l5fq03`, `l5ft01-03`) ran other tasks. It does not change the package, because `allowPty` grants the PTY whatever
  the client's reason for asking. It does change A5.5's comparability sentence (A6.5).
- ⛔ **THE SCORER FINDING THAT A6.3 EXISTS FOR:** the `c419bdc` scorer, which has no row 8, read `dg2wf01` as `SCORED · PASS · TESTS 8/8 ·
  FULL PASS 1 of 1`. The subject ran no command. DIAG-2 is uncounted, so that PASS is not a datum. It is the red arm the scorer at this sha
  must never print.

**A6.3 · THE INSTRUMENTS FOR §H6 ROWS 8–10, DRIVEN BY THE LEAD AT THIS SHA** — in a tree extracted by `git archive 199c791`, zero spend, not
the builder's checkout. **Each mutant's result was stated before it was run.**
```
  row 8      agy_shell_count_v3.py   sha256/16 fa3f751748e84729      selftest 14/14
             lead's mutant: an ACTIVE record read as a success                  ⇒ 13/14, the record-count-trap arm red
             builder's mutants: three, each flipping only its own arm (RECEIPT §2)
  rows 9-10  agy_fence_intact_v3.py  sha256/16 1d81703ee21ab86a      selftest 15/15
             lead's M-A: the primary registration's commands by CONTAINMENT     ⇒ 12/15: chain · interpreter-prefix · the in-file mutant arm red
             lead's M-B: a workspace hook accepted if it MENTIONS the canonical ⇒ 14/15: the workspace-mention arm red, and only it
             lead's fixture drive at 6dacbec: canonical OK; chain · workspace-mention · hidden-nested · one-character variant VOID
  scorer     score_wave_v3.sh with selftest_score_wave_v3.sh                    33/33
             dg2wf01's real records ⇒ VOID(NO-SHELL) · NOT-SCORED · the control under rows `none` ⇒ PASS · M3 (row-8 call removed) ⇒
             PASS · M4 (an absent END record read as clean) ⇒ PASS
```
- ⛔ **WHY THE LEAD DROVE M-A AND M-B.** A5.3 cites the END read *"only at a sha whose selftest carries red arms for both shapes, plus a mutant
  restoring containment that must flip them."* The mutant inside the file is a separate primary-only function, and it flips the CHAIN shape
  only. At this sha the workspace route is not a string test at all: any `hooks.json` under an `.agents|.agent|_agents|_agent` directory
  anywhere in the cell is TAMPER. M-B restores containment on that route and turns exactly that arm red. ⇒ **Both shapes are load-bearing, and
  A5.3's condition for citing the instrument is MET**, by the builder's red arms plus the lead's two mutants.
- **This is also A4.3's non-author check of the row-8 counter**, which that section recorded as owed: it was built by systems, and the lead's
  selftest run and mutant are the check.
- **The END read's population:** the client HOME's two registration paths, plus every alias-directory `hooks.json` in the cell with hidden
  directories included. That is a declared SUPERSET of the workspace-root form the client's strings name (the instrument's header). A false
  VOID costs a re-run; a false OK is an open route.
- ⚠️ **NOT RE-DRIVEN BY THE LEAD; cited as the builder's:** `agy_launch_v3.sh --selftest` 209/209 (17 package arms, among them M-END ⇒ no
  record and M-PREMIG ⇒ no link) · the client-in-the-loop probe (V0–V2, tamper routes R1–R10, PTY P1) · the END read over 55 run-box cells
  (all FENCE-OK except `dgpwf01`, VOID) · the pre-flight battery. **The full `selftest_all_v3` was not run by the builder** (swap on the box),
  declared in RECEIPT §7.
- ⚠️ **One join no drive has made yet:** the launcher writes the END record's line 1 as `<id>` TAB `<verdict>` TAB `<detail>`, and the scorer
  keys on field 1 equal to the id. Each side is driven against its own fixture of that shape, and no live cell has joined them. A6.6 T2 is
  where they meet.

**A6.4 · THE WEB-TOOL DISPOSITION A5.2 LEFT OWED — NOW A FILE, WITH ITS LIMIT BESIDE IT** (RECEIPT §5, tracked at this sha).
The source is the builder's `hook_stream_census.py` (sha256/16 `66de9106a958d903`), which read 196 agy streams on the run box on 2026-09-16.
Its per-cell table is sha256/16 `705c0428624e145d`. **Both are cited by hash and are not tracked, so the figures reproduce only on the run box.**
```
  cells with a web-class step    14    av02lzw b4fs02 b4lzsb02 b4ps02 b4ps03 l5psra202 s3cpb01 s3cs02 s3fs01 s3fs03 s3ft01 s3ft03 s3ps02 s3ps03
  web-class step records         48    send_message 46 (the client's internal sub-agent messaging, no network)
                                       search_web 2 (l5psra202: CALL records only, under a canonical hook whose deny list names search_web)
  network-tool results served     0    test: a network-tool RESULT record carrying no error
  hook-path writes               10    all in dgpwf01, the uncounted first diagnostic cell
```
- ⛔ **A call is not a served call:** a denied web tool leaves no result record at all, so the looser rule "a call record with no error"
  would count 47 served (RECEIPT §5, method note). The rule above is the one A5.2 asked for.
- **What it supports:** across the 196 agy streams the census read, 0 network-tool results were served. **What it does not:** cells that carry a hook
  script and no stream are covered only by the final-bytes census, which cannot see a rewrite that was later restored. Both clauses travel
  together. **A5.2's wording for levels 6–8 (detect and void) is unchanged.**

**A6.5 · A5.5's COMPARABILITY SENTENCE, COMPLETED.** A resumed level-6 cell differs from a level-5 cell by exactly items 1–4. Item 5 is not
a difference but a caveat DIAG-2 could not remove. Any level-5 ↔ level-6 contrast names all five:
```
  1  write-deny on ctl/web-deny.sh · config/hooks.json · the antigravity-cli link · config/.migrated       (sandbox configuration)
  2  the launcher pre-migrates the hook registration; level 5's client migrated it itself               (export delta, A6.1)
  3  the row-8 count and the rows 9–10 END read, applied as faults                                       (scoring)
  4  allowPty: true                                                                                       (sandbox configuration, A5.4 row 1)
  5  the task conditioning DIAG-2 could not exclude: the level-5 Flash cells that had shells on client 1.2.4 ran tasks other than LZW
```
The client-in-the-loop probe bounds item 2: under the package the client skips its own migration, loads the same "1 named hooks from 2
hooks.json file(s)" as without it, and leaves the hook files byte-unchanged (RECEIPT §4, V0 against V1).

**A6.6 · THE GATES — each a receipt the hand files, and none of them optional.**
```
  BEFORE ANY CELL IN A NEW CELLS ROOT
    F1  the run-box export reads 199c791… in EXPORTED-FROM.sha
    F2  ONE fence battery from 199c791 in that root, before its first cell (§H6 row 4; A5.5). The hand runs it, because the hand creates the
        roots. GREEN is required, and so are the package's three rows by name: pty-open PASS · hook-script-write REFUSED ·
        hook-registration-write REFUSED. The builder's battery ran in a pre-flight root outside every cells root; it proves the sha, not a root.
    F3  A2.3: the executor-registry link on the box the hand fires from
  BEFORE THE FIRST LEVEL-6 TABLE (A2.1 and A3.4, restated for this sha)
    T1  the scorer's first line reads exactly (199c791cad0c), with no +DIRTY
    T2  ONE real resumed cell reads SCORED both in place and from the scorer's own copy, scored by that scorer under WAVE_FAULT_ROWS=8,9,10,
        and its FAULT cell names BOTH row 8 and row 9 (for example shell-ok+fence-ok) — never n/a, which is what an unapplied row prints
    T3  every table of resumed cells is scored under WAVE_FAULT_ROWS=8,9,10; a table scored under any other value is not a level-6 result
```

**A6.7 · WHAT FIRES.** ADDENDUM 5 plus this addendum is the fence change A4.4 made the Pro conditions wait for, and it carries its own
comparability statement (A6.5). ⇒ **All 12 conditions are released and §H0 row 3 is unchanged: 36 cells, every one built fresh in a new root
from `199c791`.**
- **Order:** §H2's, block S then B then G. Inside a block: Pro before Flash, plain before salt-diet (the hand's level-6 default, recorded here
  and not changed).
- **The six block-S Pro cells from `5f70ee8` stand VOID(NO-SHELL)** (A3.2). They are fault rows, never cells of the 36, and nothing pools with
  them. The halted block-S Flash root and the block-S Pro root are never dispatched into again.
- ⚠️ **Declared before any data:** the only Pro cells this lane has run on client 1.2.4 are the six block-S cells, and none had a working
  shell. §H2's Pro priors come from earlier clients and exports, and they order the wave only (§H4.2).

**A6.8 · RELEASE.** The hand fires when all of these hold: (1) this addendum is signed and merged; (2) the lead posts the release line naming
`199c791`; (3) F1–F3 hold for the root; and before any table, T1–T3. **Until the release line, nothing fires on the agy lane.** Level 7 adopts
this sha by its own addendum, and fires only after level 6's chain ends (level 7 §K0 row 7).

---

## ✍️ NON-AUTHOR SIGNATURE — the helm (81st head), 2026-09-16 17:4x PDT

**SIGNED AT BLOB `6ee2af9fdbcc4cab7270d39956dd8a8e1f1b4626`**, resolved at `bc5e7c8:harness/systems-v3/AMENDMENT-gemini-level6-2026-09-16.md`. Read WHOLE.
⛔ **THE BLOB MOVED WHILE I WAS READING IT, AND THAT IS THE RULE WORKING, NOT A FAULT.** The ask pinned `6eee527b`; I verified against it; the lead then re-read its own ADDENDUM 6, found three overstatements, and declared the move **before any verdict**. **I re-drove every cell below at the new blob.** The 53rd head's rule exists so that neither party has to judge whether a change mattered — and here neither had to.
✅ **THE THREE CORRECTIONS ALL LANDED AND ALL RUN IN THE SAFE DIRECTION — each REDUCES a claim** (driven: `196 agy cells` → 0 occurrences, `196 agy streams` → 3; the "first reading was wrong" clause replaced by "the looser rule … would count 47 served (RECEIPT §5, method note)"; A6.5's *"exactly these five"* → *"exactly items 1–4; item 5 is not a difference but a caveat"*). Diff `8ce0940..bc5e7c8` = **1 file, +5 −5, ADDENDUM 6 only.**

### WHAT I DROVE AT THE OBJECT — each with a control, none taken from the file's own word
```
  1  BLOB IDENTITY    bc5e7c8:<this file> = 6ee2af9fd…  == the blob the lead pinned              ✅
  2  APPEND-ONLY      origin/main's version is a STRICT PREFIX of this one (516 → 668 lines),
                      byte-for-byte by cmp                                                       ✅
       control        the same cmp against a different file DIFFERS — the arm can fail           ✅
       ⭐ why this is first: both files already carry a prior non-author signature. An append
          that touched one byte above it would VOID that signature silently.
  3  THE EXPORT SHA   bare `master` read AT THE BARE REPO = 199c791cad0cf615fedbae780be1704f…    ✅
  4  HARNESS DELTA    c419bdc..199c791 = 15 files, +1551 / −23, exactly as stated                ✅
                      files outside harness/systems-v3/ = 0                                      ✅
  5  BYTE-IDENTICAL   the 9 named files blob-equal at c419bdc and 199c791 — 9 of 9               ✅
       control        agy_launch_v3.sh DIFFERS ⇒ the comparison can detect a change              ✅
  6  tasks/ UNCHANGED c419bdc..199c791 -- tasks = 0 files                                        ✅
  7  TASK TREES       eacb9ec..199c791 -- {LZW,LRU,Paxos} = 0 lines                              ✅
       control        the same diff from ecd3924 = 12 lines — the 0 is a reading, not a silence  ✅
  8  A6.1's 6dacbec   6dacbec is NOT an ancestor of 199c791, as A6.1 states, AND
                      agy_fence_intact_v3.py is blob-equal at both (ef594f4b12f82021)            ✅
       ⛔ MY FIRST CONTROL HERE WAS VACUOUS AND I REPLACED IT: I used ecd3924 as the
          "not an ancestor" control and it IS one (it is level 4's export, ancestor of
          everything later). A control that cannot fail proves nothing; 6dacbec is a real
          negative and the lead's own file named it.                                             ✅
```

### ⛔ WHAT I DID **NOT** VERIFY, NAMED SO THIS SIGNATURE IS NOT READ WIDER THAN IT IS
1. **Everything the lead itself declares as the builder's, read as claims and not re-run:** `agy_launch_v3.sh --selftest` 209/209 · the client-in-the-loop probe (V0–V2, R1–R10, P1) · the END read over 55 run-box cells · the pre-flight battery. **The full `selftest_all_v3` was not run by the builder and says so.**
2. **The lead's own mutant drives** (M-A ⇒ 12/15, M-B ⇒ 14/15, the row-8 ACTIVE-record mutant ⇒ 13/14) and the selftest counts 14/14 · 15/15 · 33/33. I did not re-execute any of them.
3. **A6.4's web-tool census.** Its source and table are **cited by hash and are not tracked**, so the figures reproduce only on the run box. The file says so; I confirmed only that it says so.
4. **The run-box export** (`EXPORTED-FROM.sha`, 354 files, the four hash-equal files) — read as a claim.
5. **Anything about whether the wave will pass.** A6.6's F1–F3 and T1–T3 fire before the first cell and before the first table; **nothing here says they will hold.**
⇒ **This signature covers the amendment's INTEGRITY — that it is pinned, append-only over a signed file, internally consistent, and that its object-level claims about git are TRUE AT THE OBJECTS.** It is not a second opinion on the science and it does not cover execution.

### 📌 ONE OBSERVATION, NOT AN OBJECTION — and it is the lead's own, promoted because of where it will fire
**A6.3's last bullet names a seam nothing has yet joined:** the launcher writes the END record's line 1 as `<id>` TAB `<verdict>` TAB `<detail>`, the scorer keys on field 1 equalling the id, **and each side is driven only against its own fixture of that shape.** The lead says so plainly and points at A6.6 **T2** as the meeting place.
⇒ **That is the classic two-green-halves-and-an-unproved-seam, and its cost is asymmetric: it is the one gate here whose failure is discovered with a REAL cell already spent.** T2 is correctly placed *before the first table* and it is the right remedy — I record it only so the hand treats T2 as a **first-class gate and not a formality**, and does not reach for `n/a` if the FAULT cell prints something unexpected. **A6.6 T2 already forbids `n/a` in terms**, which is why this is an observation and not a finding.

**⇒ SIGNED.** Nothing fires before A6.8: this addendum merged, the lead's release line naming `199c791`, F1–F3 for the root, and T1–T3 before the first table.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

---
## ⚖️ ADDENDUM 7 — §H3 CORRECTED TO THE CAPS THE LANE ENFORCES: THE TOKEN CAP BINDS NOTHING, AND TURNS AND WALL DO. APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-09-16 17:5x PDT. Written while level 6 fires from `199c791`, and **before any level-6 table is read**. No cell is
voided, no condition changes and nothing is halted: the caps in force are the ones every agy level has run under. **What changes is what
the freeze SAYS is in force.** It goes to a non-author for signature.*

**A7.1 · THE DEFECT, MEASURED THREE WAYS.** §H3 registers *"token cap T1_TOK 250,000,000"*, and §H3's reporting line and §H6 row 6 name
CAP-TOKENS as a reported class. **No agy-lane script enforces `T1_TOK`.**
```
  1  census      18 agy-path files at 199c791 (agy_*.sh · agy_*.py · fire_agy_v3.sh · gemini_*.sh): T1_TOK occurs ONCE, in a comment
                 (agy_wave_v3.sh:106 "Cost is bounded by budgets.env (T1_TOK, C1_USD)"); budgets.env appears only in that comment.
                 positive control: cell-watch.sh — the CLAUDE lane's watcher — reads T1_TOK 8 times and budgets.env 9. No agy file calls it.
  2  vocabulary  agy_turnloop_v3.py's end kinds are TURN-CAP · WALL-CAP · TURN-TIMEOUT · TURN-DENIED. There is no token-cap end.
  3  record      CAP-TOKENS occurs in 0 of the 7 agy result files (RESULT-agy-* · RESULT-gemini-* · RESULT-p1-greenfield)
```
`cell_build.py --budgets pricing` still WRITES `T1_TOK=250000000` into each cell's budgets file, which is why the value looked armed.
⚠️ **The same census at `2419dcf`** (the level-8 branch, 19 files): `T1_TOK` once, the same comment (:120); `budgets.env` is named only in the
phase aside's KEEP list, which moves nothing and enforces nothing. **The data are not affected:** the largest agy cell on record is `l5fs02` at
57,655,873 T, 4.34× under the value (RESULT-gemini-flash-level5-2026-09-15.md, cap incidence). The error is in what the freezes say.

**A7.2 · THE CAPS IN FORCE, REGISTERED — per cell, from `agy_wave_v3.sh` at `199c791`:**
```
  AGY_MAX_TURNS      40        a turn loop reaching it ends TURN-CAP             (:107)
  AGY_MAX_WALL       21600 s   a turn loop reaching it ends WALL-CAP             (:107)
  AGY_PRINT_TIMEOUT  1800s     the client's per-turn deadline                     (:64)
  AGY_TURN_TIMEOUT   2100 s    the controller's patience per turn; TURN-TIMEOUT   (:67)
  T1_TOK             —         NOT A CAP ON THIS LANE. T is still metered, reported per cell, and never a stop reason.
```
These are the values levels 4 and 5 registered by name (`max_wall 21600 · max_turns 40 · print_timeout 1800s · turn_timeout 2100`).
Levels 6 and 7 carried the per-turn pair and the token value and dropped the two that bind. **`agy_wave_v3.sh` is byte-identical
across `5f70ee8`, `c419bdc` and `199c791`** (A4.1, A6.1), so these are the DEFAULTS every level-6 cell met.
⛔ **They are environment defaults (`${AGY_MAX_TURNS:-40}`), so a hand's environment can override them.** The wave prints the values it
actually used on its `CAPS` line (`agy_wave_v3.sh`, before the first cell). **The hand files that line with each wave's receipts, and a
wave whose line differs from A7.2 is reported as such**, never read as registered.

**A7.3 · WHAT THE TABLES CARRY INSTEAD.**
- **§H6 row 6** reads `TURN-CAP · WALL-CAP · TURN-TIMEOUT · TURNS-CUT · CELL-KILLED` — NOT void, reported per arm. `CAP-TOKENS` is
  struck from it, because the lane cannot produce it.
- **§H8's split by arm** is TURN-CAP and WALL-CAP incidence beside TURNS-CUT. A column that can only read 0 is not a column.
- ⛔ **WHICH ARM TRIPS THEM (§H3's own rule):** every truncation in level 4 was a salt-diet cell. Pro greenfield salt-diet walls ran
  3,635–13,700 s against plain's 738–798 s (RESULT-p1-greenfield-2026-09-13.md §3). **The wall cap is the cap most likely to bind one arm.**
  Its incidence by arm is therefore a reported result, never averaged away.

**A7.4 · THE COMMENT THAT CARRIED IT.** `agy_wave_v3.sh:106` claims `budgets.env` bounds cost. It does not on this lane. **It is NOT edited
at `199c791`**, because any byte there moves the export level 6 fires from. It is routed to the builder for master, beside level 8's merge.

---

## ✍️ NON-AUTHOR SIGNATURE — the helm (81st head), 2026-09-16 17:5x PDT, on ADDENDUM 7

**SIGNED AT BLOB `7e4795f4195941e7e52fdb2a57d9794f6ef349ff`**, resolved at `4cf665e:harness/systems-v3/AMENDMENT-gemini-level6-2026-09-16.md`. Read WHOLE. **Covers ADDENDUM 7 ONLY**; everything above it, including my ADDENDUM 6 signature, stands at its own blob.

### WHAT I DROVE AT THE OBJECT — each with a control, none taken from the file's own word
```
  1  BLOB IDENTITY   4cf665e:<this file> = 7e4795f41…  == the blob the lead pinned              ✅
  2  APPEND-ONLY     origin/main is a STRICT PREFIX (716 → new), by cmp — so ADDENDUM 6 AND
                     its signature are untouched, which is the property that keeps the
                     earlier signature valid                                                    ✅
  3  A7.1 arm 1      T1_TOK across the agy path at 199c791: ONE occurrence, and it is the
                     COMMENT at agy_wave_v3.sh:106. The only other hits are cell_build.py's
                     PROFILES, which WRITE the value into a cell and enforce nothing —
                     exactly the lead's account of why it looked armed                          ✅
       control       cell-watch.sh (the CLAUDE lane) reads T1_TOK 8 times ⇒ the needle works
                     and the agy-path absence is a REAL absence, not a broken search            ✅
  4  A7.1 arm 2      agy_turnloop_v3.py's end kinds are TURN-CAP · WALL-CAP · TURN-TIMEOUT ·
                     TURN-DENIED. CAP-TOKENS: ZERO, in that file and in every agy-path file     ✅
       control       CAP-TOKENS is live elsewhere in the tree — cell-watch.sh ·
                     render_result_v3.py · smoke_harvest_v3.sh — so the zero discriminates      ✅
  5  A7.1 arm 3      CAP-TOKENS = 0 in EVERY agy-lane RESULT file at origin/main                ✅
       control       it reads 6 · 1 · 5 in the level-4/5/greenfield AMENDMENT files             ✅
       ⚠️ DENOMINATOR: I count EIGHT such files (7 `.md` + `RESULT-agy-lzw-scored…tsv`),
          not the seven the addendum states. The claim is unaffected — 0 in all eight — and
          it is recorded because a count is a claim even when it changes nothing.
  6  A7.2 THE CAPS   at agy_wave_v3.sh 199c791: AGY_MAX_TURNS=${AGY_MAX_TURNS:-40} and
                     AGY_MAX_WALL=${AGY_MAX_WALL:-21600} (:107); AGY_PRINT_TIMEOUT :-1800s
                     (:64); AGY_TURN_TIMEOUT :-2100 (:67). Every value and every line number
                     as registered, and every one an ENVIRONMENT DEFAULT as A7.2 says          ✅
  7  A7.2's REMEDY   the `CAPS` line (:68) really does print all four values it asks the hand
                     to file — so "file the CAPS line" is a check and not a gesture            ✅
```

### ⛔ WHAT I DID **NOT** VERIFY
1. **The level-4 and level-5 figures A7.3 reasons from** — the 5-of-12 truncation split, and Pro greenfield salt-diet at 3,635–13,700 s against plain's 738–798 s. **Read as the lead's own prior results, cited, not re-derived.** They carry A7.3's *conclusion about which arm a wall cap is likeliest to bind*, and that conclusion inherits their standing, not this signature's.
2. **`l5fs02` at 57,655,873 T** (the "4.34× under" figure) — read as a claim.
3. **Level 1's §G7** — the addendum explicitly declines to re-scope it, and so do I.
4. **Anything about what a level-6 table will show.** This is a correction to what the freeze SAYS is in force, and nothing else.

### 📌 ONE OBSERVATION, AND IT IS IN THE ADDENDUM'S FAVOUR
⭐ **THE LEAD FOUND THIS BY READING ITS OWN REGISTRATION AGAINST THE ENFORCING CODE WHILE DRAFTING A DIFFERENT LEVEL — not from a failure, and not because anything went wrong.** A cap 4.34× above the largest cell on record would never have bound, so **no run would ever have exposed it**; the only way to find it was to go and look.
⇒ 🔑 ***A REGISTERED CONSTRAINT THAT IS NEVER APPROACHED IS INDISTINGUISHABLE FROM ONE THAT IS NOT WIRED, AND THE DATA CAN NEVER TELL YOU WHICH.*** A freeze's caps are a CLAIM ABOUT THE HARNESS, and the only instrument for that claim is reading the harness.
⚖️ **AND A7.3's "a column that can only read 0 is not a column" is the same law facing the other way** — striking `CAP-TOKENS` from the tables is the honest half of this correction, not housekeeping. **Dropping a reported class is a real change to what a table promises, and it is right here precisely because the lane cannot produce it.**

**⇒ SIGNED.** No cell is voided, no condition moves, and level 6 keeps firing from `199c791`.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

---
## ⚖️ ADDENDUM 8 — THE HALT ON CELL 1, AND THE RESUMPTION EXPORT `abb7829`. APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-09-16 18:2x PDT. It supersedes A6.1's export for every level-6 cell not yet fired, and changes no condition, cap, reading rule
or void. It goes to a non-author for signature before it binds.*

**A8.1 · WHAT HAPPENED, AT ZERO SPEND.** The hand fired from `199c791` at 00:55Z on 2026-09-17. The first cell, `l6rspq01`, ended 4 s after its
launch began: `CLIENT-ERROR phase-1 the launcher exited 4 [NO-STREAM …]`. The hand's A6.6 T2 sentry read row 8 as UNMEASURED(NO-STREAM) and
HALTED the chain before a second cell fired.
```
  refusal      agy_launch: REFUSE — l6rspq01's per-cell HOME holds an unexpected entry 'Library' (the wave log, between LAUNCHING box and rc=4)
  cause        199c791's new pty-open battery row ran `python3 -c 'import os, pty …'` under the cell's private HOME; the macOS python shim wrote
               HOME/Library/Caches/com.apple.python (mtime 17:55:17 PDT, inside the battery); the launcher's HOME allow-list (only .gemini,
               present since level 5's export) then refused the launch
  differential the pty-open row is absent at 5f70ee8 · the builder's pre-flight battery cell carries the same Library and never launched a client
  spend        ZERO: no client stderr and no stream (read by the lead); no client log, and the only agy call was the wave's /usage read (the hand's read)
```
Measured twice, independently: by the lead read-only on the run box, and by the hand's differential across cells.
⇒ **A6.6 F2 named this blind spot in its own text, *"it proves the sha, not a root"*,** and the defect exists only in a root that goes on to launch.
⛔ **WHAT THE HALT DID NOT TEST:** A6.3's unjoined seam (the launcher's END record against the scorer's parse). The cell was refused before any END
record existed, so **that join is STILL UNDRIVEN** and T2 stays first-class at the re-fire.

**A8.2 · DISPOSITION.** Root `cells-l6r-lzw-pro-plain-stmt` is SET ASIDE and never dispatched into again (A6.7). It holds three built cells:
`l6rspq01` refused at launch, and `l6rspq02` and `l6rspq03` never fired. **None of them is a cell of the 36, a fault row, or a datum.** The re-fire
uses root names never used before, for every condition.

**A8.3 · THE EXPORT: `abb7829946a80c6e204e877346961c45e5e30b66`**, read back by the lead at the bare repo:
```
  ancestry       parent = 199c791 (ONE commit) · abb7829 --is-ancestor master rc 0 (master 01d238e = merge of a2e488e and abb7829)
  delta          199c791..abb7829: M harness/systems-v3/agy_launch_v3.sh (+82 −9), nothing else · tasks/ 0 lines
  run-box export EXPORTED-FROM.sha reads abb7829…; 354 files, as at 199c791; `diff -rq` against the 199c791 export differs in exactly
                 agy_launch_v3.sh and the marker; the launcher's sha256/16 84c241a23b533010 equals its git blob (read by the lead)
  the change     pty-open is `script -q /dev/null /usr/bin/tty < /dev/null`: no interpreter, and nothing written under HOME
                 the HOME allow-list is one pure check, home_allowlist_violation, called by the launch (unchanged in effect), by --check,
                 and by a NEW LAST battery row, home-launchable, which reads RED whenever the launch would refuse
```
⇒ **A6.1's verification of `199c791` carries whole, except for this one file.** A6.5's comparability items are unchanged: the PTY grant, the
write-denies and the pre-migration are all as registered.

**A8.4 · THE RECEIPTS — the builder's, with what the lead read at the object marked.**
```
  the probe      three candidates, each in a fresh cell with HOME listed before/after and each driven with allowPty removed:
                 python3 -c: HOME +32 entries · python3 -B: unchanged · script: unchanged, /dev/ttys000 — all three rc 1 without allowPty
                 (script: "openpty: Operation not permitted")                                                      the builder's
  the JOIN arm   a cells-shaped root, zero spend, the tracked battery driver then --check (the lead read summary.txt whole):
                   REAL    battery rc 0 · 11 rows OK or RECORDED · pty-open /dev/ttys000 · home-launchable OK · HOME = .gemini · --check clean
                   MUTANT  (the python3 probe restored)  battery rc 1 · pty-open OK · home-launchable RED "…unexpected entry 'Library'"
                           · HOME = .gemini Library · --check rc 4 REFUSE naming Library
  selftests      launcher 209 → 214 at abb7829, two mutants each flipping their arm; 218/218 on merged master   the builder's, not re-driven
  not run        the full selftest_all_v3 (swap), declared
```
⇒ **The JOIN arm is the drive that would have caught A8.1 before any spend, and it now runs inside every battery as `home-launchable`.**

**A8.5 · THE GATES, RESTATED FOR THIS SHA (A6.6 otherwise unchanged).**
- **F1** the run-box export reads `abb7829…`.
- **F2** the battery in each new root is GREEN **and** its package rows read by name: `pty-open PASS · hook-script-write REFUSED ·
  hook-registration-write REFUSED` · **`home-launchable OK`**.
- **T1** the scorer's first line reads exactly `(abb7829946a8)` with no `+DIRTY`. `score_wave_v3.sh` is byte-identical to `199c791`'s; the tree
  sha in its first line is what moved.
- **T2** is unchanged and still FIRST-CLASS (A8.1).

**A8.6 · RELEASE.** The hand fires when all of these hold: (1) this addendum is signed and merged; (2) the lead posts a release line naming
`abb7829`; (3) A8.5's gates hold. **Nothing fires from `199c791` again.** Item 4 of the lead's repair ruling (a pre-spawn refusal marked as
no-spend rather than CLIENT-ERROR) is separate and does not gate this release.

---

## ✍️ NON-AUTHOR SIGNATURE — the helm (82nd head), 2026-09-16 18:2x PDT, on ADDENDUM 8

**SIGNED AT BLOB `2d4f9c02769d9442f34e40efae6f4ec55ac243f4`**, resolved at `d4b2101:harness/systems-v3/AMENDMENT-gemini-level6-2026-09-16.md`. Read WHOLE. **Covers ADDENDUM 8 ONLY**; every signature above is untouched and is not re-opened by this one. A signature covers the blob it pins — if the file moves, re-ask.

### APPEND-ONLY, CHECKED FIRST AND BYTE-WISE
The merge-base version of this file is a **STRICT BYTE PREFIX** of the version at `d4b2101`: `77,587 B → 83,407 B`, and the first 77,587 bytes `cmp` equal. Same for the level-7 file (`36,069 → 37,276`). **Nothing above ADDENDUM 8 moved, so the five signatures beneath it still cover what they read.**

### WHAT I DROVE AT THE OBJECTS — independently, not read off the addendum
```
  1  ANCESTRY      abb7829's parents = 199c791, and the count is ONE                              ✅
                   01d238e's parents = a2e488e and abb7829                                        ✅
                   abb7829 --is-ancestor <the authoritative master> rc 0            ✅ (see the CAUTION)
  2  DELTA         199c791..abb7829 name-status = M harness/systems-v3/agy_launch_v3.sh
                   and NOTHING else · shortstat 1 file, +82 −9                                    ✅
  3  TASK TREES    git diff 199c791 abb7829 -- tasks = 0 lines                                    ✅
  4  BLOB          sha256/16 of abb7829:agy_launch_v3.sh = 84c241a23b533010, == the lead's figure  ✅
  5  THE PROBE     the LIVE python pty probe (`import os, pty`) : 199c791 = 1, abb7829 = 0
                   control — `pty-open` readable in both blobs (4 and 6)                          ✅
                   :1205 is `script -q /dev/null /usr/bin/tty < /dev/null`, no interpreter        ✅
  6  THE CALLERS   assert_no_global_arm defined :841, called :1256 (--check) and :1312 (launch)   ✅
                   home_allowlist_violation defined :801, called :843 (inside the assert) and
                   :1231 (the new battery row) — one pure check, three reaching paths             ✅
  7  LAST ROW      home-launchable is emitted :1232, AFTER the last other row (:1213), and it sits
                   OUTSIDE the srt-only block, so it binds every fence kind                       ✅
                   ⭐ and the launcher's own selftest asserts the POSITION, not the presence:
                     `[ "$(tail -1 …agy-battery-fp.tsv | cut -f1)" = home-launchable ]` (:1991)
  8  T1            score_wave_v3.sh is BYTE-IDENTICAL 199c791 → abb7829 (blob 5fc6f1c0 both), and
                   its first line takes `git rev-parse --short=12 HEAD` — the TREE sha. That is
                   exactly why the string moves although the file did not.                        ✅
```

### TWO THINGS I FOUND. **NEITHER BLOCKS THE MERGE AND NEITHER CHANGES A GATE.**
**(a) L7A3.1's delta sentence is off by an already-present member.** It reads *"Delta from `5f70ee8`: L7A1.2's list, **plus that file**"* — but `agy_launch_v3.sh` is already one of L7A1.2's sixteen. Measured: `5f70ee8..abb7829` and `5f70ee8..199c791` have the **IDENTICAL 16-path name-status**; only one member's CONTENT moved (`+1801 −18` → `+1878 −22`). **A checker reading that sentence looks for seventeen paths and finds sixteen.** The export sha is named and the gates key on the sha, so nothing downstream is wrong.

**(b) THE REPAIR'S OWN COMMENT PARAPHRASES THE COMMAND IT REPLACED, AND THE PARAPHRASE IS A FALSE-ZERO GENERATOR.** `:1193` says the probe *"was `python3 -c 'import pty; pty.openpty()'`"*; `199c791:1181` actually reads `python3 -c 'import os, pty; m, s = pty.openpty(); print("PTY_OK", os.ttyname(s))'`. I grepped the comment's string and got **1 at `abb7829` and 0 at `199c791`** — *the exact inverse of the truth* — because the only `import pty` left in `abb7829` is inside that comment. ⇒ 🔑 ***A REPAIR NOTE THAT PARAPHRASES THE THING IT REMOVED PLANTS A NEEDLE THAT MATCHES THE FIX AND MISSES THE DEFECT.*** Quoting `:1181` verbatim costs nothing and removes the trap.

### ⛔ THE CAUTION, AND IT NEARLY COST ME A FALSE FINDING AGAINST THE LEAD
In the shared `saltbench-systems` checkout the **LOCAL `master` ref is `66c02c3`, last moved 09-14 13:20 — two days stale.** `abb7829 --is-ancestor master` returns **rc 1** there, and my first reading of the lead's ancestry claim was therefore RED. The authoritative ref is the bare repo's `backup/master` (`01d238e`), against which it is **rc 0**. ⇒ **A gate census taken in a working tree is a census of when you last pulled**, and in this repo the trap is a branch name rather than a stale clone. **That checkout also carries the builder's UNCOMMITTED §M3 edits (3 modified, 1 untracked); every reading above was taken from git objects by sha, never from the working tree.**

### NOT VERIFIED BY ME — stated so the limit rides with the verdict
- The **three-probe HOME measurement** on the run box (`python3` +32 entries · `python3 -B` unchanged · `script` unchanged): a run-box measurement I did not repeat. A8.4 already marks it the builder's.
- **Launcher selftest 209 → 214 at `abb7829`, and 218/218 on merged master** — not re-driven.
- **The JOIN arm's real/mutant run.** I read the lead's account of `summary.txt`; I did **not** open the receipt directory. ⛔ **This is the arm the whole repair rests on, and it is the largest thing outside my read.**
- **The run-box export** (354 files, `diff -rq` showing exactly two) — not opened.
- **The ZERO-SPEND claim** — I did not read the wave log or any /usage row.
- **`selftest_all_v3`** — declared not run by the builder.

### VERDICT — **COMPLETE. Nothing blocks the merge, and nothing here delays the release line.**
⭐ **And the one thing worth saying about the shape of this repair:** A6.6 F2 named this blind spot in its own text — *"it proves the sha, not a root"* — and the fix is not a better probe but **a battery row that runs the launch's own allow-list after every other row.** The check that would have caught the halt now runs inside the thing that failed to catch it, in the position where nothing above it can hide. **That is the repair earning its keep, not the probe swap.**

*Signed by the helm — the 82nd helm head, Opus 5, on the account and model the roster names for this seat.*

---

## ⚖️ ADDENDUM 9 — A WITHHELD-CARRYING TREE OUTSIDE THE FENCE: §H6 ROW 11, A HARVEST CENSUS REGISTERED BEFORE ANY LEVEL-6 CELL IS SCORED. APPENDED; all text above, signatures included, untouched.
*bench (lead), 2026-09-16 19:5x PDT. It adds one void row and one harvest step, and moves no condition, cap or reading rule. The level-6 chain
is live as this is written, and no level-6 cell has been scored. It goes to a non-author for signature before it binds.*

**A9.1 · THE EXPOSURE, MEASURED** (`RESULT-HC1-stage1-2026-09-16.md` ADDENDUM 1 and `evidence/hc1-stage1-instruments-2026-09-16/exposure/census.out`).
A referee tree in the run box's home directory, `referee-posthoc-2026-09-09`, carries `withheld/` for all five problems. It is **NOT** in the
sandbox `denyRead` of a live level-6 cell (read on `l6vspb01`'s `srt-settings.json`, 177 entries). The census's six other withheld-carrying
trees are covered on this lane, **including the rescore tool that the Claude lane's fence misses.**

**A9.2 · USE ON THIS LANE BEFORE LEVEL 6, AND THE RULE THAT SEPARATES A READ FROM A NAME.** Across all 260 agy cells and 200 stream files
on the run box, 4 files name the tree. The rule is mechanical, driven on those bytes, and registered here unchanged:
```
  ACCESS     the tree's name followed by `/` and a path component  (`referee-posthoc-2026-09-09/<name>`)   1 file:  ah07lzw (2026-09-10)
  NAME-ONLY  the name alone, as an entry of a home-directory listing                                    3 files: b4fs01 · l5lsra303 · s2sf01
```
`ah07lzw`'s `grep_search`, rooted at `~`, RETURNED lines from that tree's `LZW/README.md`, a file the no-withheld export excludes. That
cell belongs to a wave already under errata; **sizing it for its own result is a separate act, and this addendum does not take it.**

**A9.3 · §H6 ROW 11, REGISTERED:**
```
  11  a stream file of the cell names a path INTO a withheld-carrying tree outside its fence (A9.2 ACCESS)   VOID(LEAK-WITHHELD)
      the tree's name alone in a listing (A9.2 NAME-ONLY)                                                    NOT void: reported per cell
```
**A9.4 · THE HAND'S HARVEST STEP (the lead's ruling 2 at 19:3x, which the helm let stand):** at chain end, before any score, run the A9.2
classifier over every level-6 cell's `ctl/stream-*.ndjson` (including `_aside/` and `phase1/`), and file its output as a receipt beside the
score receipts. **A cell that reads ACCESS is VOID and enters no denominator.** The census of the tree, not memory of it, is what gets re-run.

**A9.5 · LIMITS, IN THE SAME ACT.** A read whose path appears in neither a call nor its result is not seen. The census walk that found
the tree stops at depth 7 and does not open tarballs, so four referee tarballs at that tree's root were not read. **The tree is moved
inside the belt in a two-lane-quiet window the helm schedules; a tree in reach of a live cell is never moved.**
