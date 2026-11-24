# AMENDMENT — O37 BLOCK NCA: BLOCK NA's SIX × SPEC-CHANGE, agy LANE. FROZEN BEFORE THE FIRST BASELINE
## bench (SaltBench lead), 2026-11-23, from gemini's draft (the hand; saltbench-systems branch `gemini/o37-nca-wca-registration-drafts-2026-11-22`
## at 098430ec, backup only), taken whole except where a line says it changed at landing. Its sibling is block WCA
## (`AMENDMENT-O37-blockWCA-wht-ntt-specchange-agy-2026-11-23.md`).
## The form is block NC's (`AMENDMENT-O37-blockNC-specchange-claude-2026-11-13.md`, ADDENDA 1–5, cited as "NC"), carried BY CITATION, with
## the agy lane's phase-2 machinery from level 8 (`AMENDMENT-gemini-level8-2026-09-16.md` §M3, §M4, §A9.4, cited as "L8"). The frame is
## block NA's (`AMENDMENT-O37-nine-greenfield-agy-2026-09-25.md`, cited as "NA") and block WA's model seam (`AMENDMENT-O37-wht-ntt-greenfield-agy-2026-11-13.md`
## ADDENDUM 2, cited as "WA A2"). A clause that differs from NC says so and why.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ No phase-1 baseline before the signature (NC's rule). ⛔ No cell fires before a release
## addendum names the export, the client, each §NCA3 receipt as MET, and the first post-install battery fire (§NCA9 clause 5).
## The agy cell lane was RELEASED by the helm on 2026-11-23 (bus offset 109,690,931) on export aa071afc; every agy fire is a NEW build
## through that export's own drivers (desk AHH), never a pre-built cell. That release is what this file's row 4 now names.

**Why now.** O37's agy lane holds greenfield on the six (NA) and the Claude lane holds spec-change on them (NC, census ADDENDUM 46). By the
11-09 remainder plan (seat brief `2026-11-09-bench-O37-REMAINDER-census-and-price.md` §2) the agy lane's spec-change × the six is owed, and
the six B/ suites NC drove exist, so authoring does not gate it. Census ADDENDUM 46 §AQ2 lists it as "x {statement, spec-change}, agy lane:
in no block" (48; this block is 24 of them).

---

## §NCA0 · THE INPUTS
```
  1  MODEL IDs     gemini-3.8-flash-high (NA row 1) · gemini-4-argon-high (the Pro slot as WA A2 re-registered it, with WA A2's MODEL
                   SEAM carried: an argon cell is never pooled, tabled beside or compared with a gemini-3.1-pro-high result). The release
                   re-measures both on its client by the lane-live battery (WA §WA2 item 4); a served-model mismatch VOIDS (NA, level 6 §H6).
  2  n             3 per condition.
  3  POPULATION    24 conditions, 72 phase-2 cells (§NCA1). Nothing added, dropped or substituted.
  4  EXPORT        ONE saltbench-systems sha, named in the release addendum, that (i) carries the agy production line the lane fires
                   on at release, ⚖️ RE-POINTED AT LANDING: the RELEASED agy export aa071afc (the helm @109,690,931; kent's read @109,660,929).
                   It descends from the draft's candidate base d16d1173 (merge-base --is-ancestor: yes) by 91755585 (the six-tree overlay
                   below, in one commit) and five hook-lane commits (adbd25f1 · c250c11a · f7ebe50e · b10cfe99 · aa071afc), which touch
                   exactly five harness files (agy_battery_cell.sh · agy_deny_probe_v3.py · agy_fence_intact_v3.py · agy_launch_v3.sh ·
                   agy_web_deny_v3.sh): the hook fix that released firing, and nothing else in harness/. And (ii) it carries the six WHOLE task trees at NC's driven task-tree hashes (NC
                   ADDENDUM 2: AES 00b919ce · BinomialHeap df6427a9 · LinearScan a3c8ae15 · Liveness 143296d6 · Luby 6db3c763 · MaxFlow
                   5b89c4df, i.e. 36ca596b's), OVERLAID in one commit as WA overlaid WHT/NTT (WA §WA0 row 4: no merge of Claude-lane harness
                   files into the agy line). Whole trees, not B/ alone: 36ca596b also adds each card's change-request section (git diff
                   3fd5edf1..36ca596b outside B/: BinomialHeap, LinearScan, Luby, MaxFlow card.md, Luby README.md).
                   MEASURED 2026-11-22 (`git rev-parse <sha>:tasks/systems-v3/<P>/G`): each of the six G/ trees is the SAME at NA's
                   e10f420 and 8ed8cb3, at 3fd5edf1 and at 36ca596b (AES 32241f14 · BinomialHeap abb8fd83 · LinearScan 3ecbfc30 ·
                   Liveness ae7d8878 · Luby c1b15126 · MaxFlow 14c96110), so a copied source and a fresh cell meet one G/ suite.
                   At drafting no agy-line sha carried the six B/ trees (3fd5edf1 and d16d1173: none). aa071afc carries all six, each
                   equal to 36ca596b's whole tree (gemini's §NCA3 item 1 receipt, 2026-11-23).
                   ⚠️ d16d1173 carries block TA's six cards (397864e8: the statement sections overlaid on all six card.md files, +1664
                   lines). The overlay REPLACES them with 36ca596b's whole trees, so an NCA subject reads NC's card exactly (change-request
                   section, no statement section); the release checks each of the six task trees equals 36ca596b's by git rev-parse.
                   Measured on aa071afc: the Luby card there has no `## Statement` section.
  5  CLIENT        the release's agy client by version and sha (WA A1: the client self-updates; the version is read AFTER the first
                   call). Each pair records both clients (§NCA6 item 3).
  6  CAPS          NA row 5 as NA ADDENDUM 4 left it and WA carried it, per phase: T1_TOK 250,000,000 · AGY_PRINT_TIMEOUT 1800 s ·
                   AGY_TURN_TIMEOUT 2100 s; the persistence probe at L8 §A9.5's 600 s. Cut turns, truncated cells and CUT-BOUND are
                   reported per arm and phase, a truncated PASS is a FLOOR. No cap is raised.
  7  QUOTA         P3 on the agy subscription pool, yielding to any O4 agy cell live or queued; agy /usage read at each fire and bank.
  8  FIRE ORDER    §NCA4.
```

## §NCA1 · THE POPULATION — 24 CONDITIONS, 72 PHASE-2 CELLS
```
  problems   AES · BinomialHeap · LinearScan · Liveness · Luby · MaxFlow     NA's six, each with NC's driven B/ rung
  models     gemini-3.8-flash-high · gemini-4-argon-high
  arms       plain · salt-diet        field greenfield → spec-change         extras none
  ⇒ 6 × 2 × 2 = 24 conditions · × n 3 = 72 phase-2 cells
```
The agy client registers exactly these two arms (`cell_build.py --client agy` refuses `--arm salt`, WA §WA1). Not in this block: WHT/NTT ×
spec-change on this lane (block WCA, its sibling draft), the statement arm, and anything on the Claude lane.

## §NCA2 · ⛔⛔ THE SOURCES — THE RULE, REGISTERED BEFORE ANY BASELINE
**FLASH (copies of NA's cells of record).** NC §C2 steps 1–6 carried, with ADDENDUM 1's instrument (the G rung on landed-1, `gbase.sh`'s
form: ELIGIBLE iff rc 0 and passed == total > 0, one attempt, on a CLONE, never in the cell). Sources: NA's 36 Flash cells of record
(`RESULT-gemini-blockNA-2026-09-28-cells.tsv`, `in_registered_n = yes`; `nabhfsr01` is outside n and is not a source). Every eligible
cell is used, once, ascending id. A shortfall is filled by a FRESH cell under rule 4 (one attempt; a reach loss is never retried).
⚖️ **THE CHANGE FROM NC: the copy form is the agy lane's, L8 §A9.4** (`agy_cell_copy_v3.py`: the WHOLE cell to a new root `<source root>-ncacp`,
the SAME id, lineage in `ctl/copied-from.tsv`, path-keyed files deleted and re-rendered, a copy not re-rendered REFUSED at launch), then the
standard path AGY_PHASES=2: L8 §A9.2's landing gate → L8 §M3's phase-1 fault gate (shell-ok AND fence-ok) → customer dispatch → aside
(`.agyhome/` and every phase-1 session record out of the subject's reach) → phase 2. `cell_copy_v3.py` refuses agy cells by design.
**A fresh Flash cell** is level 8's form: phase 1 and phase 2 in one cell (AGY_PHASES=1,2) under the same gates, its G baseline read on
landed-1 by the same instrument BEFORE its phase 2 is counted (NC rule 4).

**ARGON (fresh cells, all 36).** ⚖️ **THE CHANGE FROM NC, AND THE ONE DESIGN FORK THIS DRAFT CARRIES (§NCA7):** NA's Pro slot ran
gemini-3.1-pro-high, which today's client does not serve (WA A1), and no argon cell exists on the six. Under NC's "same problem, model and
arm" rule every argon condition has 0 sources, so rule 4 fills all three: 36 fresh cells in level 8's one-cell form, each a REACH loss if
its phase 1 does not land or its G baseline is not full.

**What is already public, recorded so it cannot be dropped later:**
- One Flash source has no landing: `nabhfs03` (BinomialHeap · salt-diet, end-1 ARM-NOT-RECEIVED, NOT-SCORED). One known shortfall.
- One landed Flash source failed its own G suite at NA: `nalsfs202` (LinearScan · salt-diet, 8/9). Its baseline decides it.
- ⚠️ **FIVE OF THE SIX Flash LinearScan sources are WEB-SERVED** (census ADDENDUM 47; `evidence/o37-agy-web-served-2026-11-20/README.md`):
  nalsfp201 (7 results), nalsfp202 (16), nalsfp203 (22), nalsfs202 (3), nalsfs203 (3). §NCA6 item 5.

**DECLARED UNREACHED, carried as a rule (census ADDENDUM 46 §AQ1):** a condition with no cell of record after its sources and its one-attempt
fresh cells is DECLARED unreached, beside the census section, never re-run. LinearScan × salt-diet is the expected case (NC: both Claude
models; NA Pro: 0 of 3 scored at FULL PASS); the rule is the same for every condition.

## §NCA3 · ⛔⛔ THE BUILD ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **THE SIX B/ TREES ON THIS EXPORT EQUAL NC's DRIVEN TREES** by git tree hash (NC ADDENDUM 2). Equal ⇒ NC §C3 item 1's non-builder
   drive is cited; any difference ⇒ re-driven by a non-builder, or the task is WITHDRAWN and its conditions NOT-FIRED(TASK).
2. **THE REFEREE ON DRY agy CELLS** (WA §WA2 item 2's form, on the B/ rung): the B/ reference PASSes on both arms, and one clause mutant and
   one regression mutant per task fail, with counts.
3. **THE 35 FLASH BASELINES** (§NCA2: 36 less nabhfs03, which has no landing), after the signature, on the run box, each on a clone (`gbase.sh`): table, eligible count per arm, and
   the shortfall list in the release.
4. **THE COPY FORM ON A DRY agy CELL** (NC §C3 item 3's form for L8 §A9.4): `agy_cell_copy_v3.py --apply` on one eligible source, then
   AGY_PHASES=2 with a STUB client (L8 §M0 row 8's dry drive): copied-from.tsv present; fence re-rendered at the copy's own path and denying
   its own `_receipts`; the §M3 gate reads the copied stream-1 and fence-1; `inbox/change-1.md` equals the card's change-request section;
   the aside moved `.agyhome/`; and the SOURCE cell's tree hash is byte-unchanged before and after. A planted un-re-rendered copy is REFUSED.
5. **NO LEAK INTO A VIEW:** `check_withheld_leak_v3.py` over the export, screening the six B/withheld trees.
6. **THE LANE IS LIVE:** the battery on one dry cell per model on the release's client (credential window, served model, fence intact, TMPDIR
   identity, the TREE-HASH line), ⛔ AND its P-SWARM and P-WEB rows DENIED (d16d1173's brain-read deny probe), which is the hook condition
   firing is held on.

## §NCA4 · THE ORDER, THE TRIPWIRES
```
  models     Flash first (copies; NA §NA2's reason), then argon.
  problems   ascending B/ reference size, the release's own `wc -l` (NC ADDENDUM 3: Luby first … LinearScan last).
  cells      per problem: plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3, through the canary wave supervisor
             (`gemini_canary_wave_v1.sh`: any 503 ⇒ kill tree, discard, re-queue); a fresh Flash cell takes its source's slot.
```
Tripwires, each ONE cell, read by the lead before its model continues: `T-NCA-F` = Flash · Luby · salt-diet#1 (a copy), `T-NCA-A` = argon ·
Luby · salt-diet#1 (a fresh cell, both phases). Reading list: L8's (end kinds per phase, §M3 verdicts, B/ suite with REGRESSIONS and
CLAUSE_TESTS, cut turns per phase, served model per phase) plus the WEB-SERVED brain read (§NCA6 item 5).

## §NCA5 · PREDICTIONS AND THE PRICE — REGISTERED BEFORE ANY DATA
A cut-out is a RESULT and enters at its floor. Predictions, per model, where a miss is a result: (i) the eligible count (Flash) and REACH
(argon) are lower for salt-diet than plain; (ii) within a condition, salt-diet's cut-turn incidence in phase 2 is ≥ plain's; (iii) CELL-KILLED
binds no cell outside a declared 503 episode. ⛔ No prediction about the phase-2 pass rate or a premium.
**The price** is in cell wall, the lane's binding resource (the agy pool's unit did not move over WA's 24 cells, WA A2). Printed by
`nca_price.py --saltbench <clone> --ref 9efec234e988` (`evidence/blockNCA-2026-11-23/`, with its output `nca_price.out`; re-run at landing against saltbench 9efec234e988, `cmp` EQUAL):
```
  L8 phase2/phase1 wall, model letter f: n 29 median 0.809 (min 0.177 max 1.361)
  L8 phase2/phase1 wall, model letter p: n 28 median 0.844 (min 0.157 max 5.814)
  Z argon/flash wall, plain: argon n 15 · flash n 15 · ratio 2.301
  Z argon/flash wall, salt-diet: argon n 12 · flash n 15 · ratio 0.733
  KNOWN Flash shortfalls (landed != True): 1 nabhfs03
  Flash: 37 launches floor · 37004 s = 10.3 h of cell wall
  argon: 72 launches · 81362 s = 22.6 h of cell wall
  NCA total: 109 launches floor · 32.9 h of cell wall; agy pool points per cell UNMEASURED
```
LIMITS, beside the figure: (a) argon's phase-2 ratio is gemini-3.1-pro-high's (no argon phase 2 has run on this lane); (b) the argon/flash
ratio is the Z wave's five problems, not these six, and its salt-diet median excludes three argon wedges (WA A2); (c) Flash shortfalls beyond
`nabhfs03` are decided by the baselines, so Flash is a FLOOR; (d) the credential warm-wait is not in cell wall; (e) the first problem's
cells per model re-cut the estimate before the rest fire (NC §C5's form).

## §NCA6 · CONFOUNDS — NC §C6 carried (items 1–4), plus this block's own (and §NCA9–10, the declared client line and its noise)
1. **A PHASE 1 SHARED ACROSS TWO CONDITIONS** (NC item 1): each Flash copy's source is a cell of record in NA's `none` condition.
2. **REACH IS ARM-CORRELATED, AND THE SOURCES ARE FILTERED BY IT** (NC item 2; L8 §M4): the eligible count / REACH travels with every figure.
3. **TWO EXPORTS AND TWO CLIENTS PER FLASH PAIR, ONE FOR ARGON.** A Flash copy's phase 1 ran at NA's export and client (the version the NA record names), its
   phase 2 at this block's; and phase 2 starts about two months after phase 1 in wall-clock time (L8 §A9.4's declared difference, larger).
   An argon cell runs both phases at this block's. So **Flash and argon pairs differ in FORM** (copy vs one cell): nothing here compares a
   Flash phase-2 figure with an argon one (also WA §WA5: nothing Flash-versus-argon as models).
4. **ONE AUTHOR FOR THE SIX B/ SUITES, WHO IS THE LEAD** (NC item 4); NC's Liveness clause-test finding (census ADDENDUM 46 NOTE 1) is
   carried: the card is amended before any later Liveness run, so the release names the Liveness card and B/ tree it fires on.
5. **WEB-SERVED SOURCES (Flash LinearScan, 5 of 6).** A phase 2 continuing a WEB-SERVED phase 1 inherits code written with served search
   results. ⚖️ DEFAULT (§NCA7 fork 2): such a source is not excluded (eligibility stays one validity filter, the same for every arm); each pair
   carries `source_web_served` with its count, and the pair leaves every comparison exactly as its source did (bench's ruling, census
   ADDENDUM 47 §AR3). A phase 2 that is itself served a search is WEB-SERVED in its own right.

## §NCA7 · THE FORKS, DECIDED BY THE LEAD AT LANDING (written before any data)
⚖️ **bench takes all three defaults, as drafted.** Fork 1's default needs no ruling beyond WA A2. Fork 2's keeps eligibility as one
validity filter for every arm (census ADDENDUM 47 §AR3). Fork 3's alternative has no record to stand on. Each is reversible by a later
amendment written before the data it would change.
1. **ARGON HAS NO SOURCE.** DEFAULT (above): 36 fresh argon cells in level 8's one-cell form, model-pure under WA A2's seam.
   ALTERNATIVES: (b) argon phase 2 on COPIES of NA's gemini-3.1-pro-high phase 1s, which puts two models in one pair and breaks WA A2's seam
   (not recommended); (c) if the release's battery finds gemini-3.1-pro-high SERVED again, re-register the slot on it and copy NA's Pro
   cells as Flash does (changes a registered input: his word through the helm, WA A1's precedent). The default needs no ruling beyond WA A2.
2. **WEB-SERVED SOURCES.** DEFAULT: carried and flagged (§NCA6 item 5). ALTERNATIVE: ineligible, filled by fresh cells. Not recommended: the
   fresh cells would run on the same lane whose hook did not bind, and a second filter would select Flash LinearScan's sources on a property
   that is not a validity property.
3. **LinearScan × salt-diet, argon.** DEFAULT: the rule unchanged (three fresh cells, one attempt each), as NC §C7's default. ALTERNATIVE:
   DECLARE unreached without firing; there is NO argon LinearScan record to declare it from, so the alternative has no basis here.

## §NCA8 · READING RULES, VOIDS, WHAT THIS BLOCK CANNOT ESTABLISH, DELIVERABLES
Reading rules: L8 §M7 and NC §C8, carried; every premium UNRESOLVED-UNDERPOWERED. Voids: L8 §M8 (faults only). It cannot establish: any
magnitude; anything Flash-versus-argon or Claude-versus-agy; anything about a spec-change reached from a phase 1 that did not land; anything
about a gemini-3.1-pro-high condition; anything outside §NCA1. Deliverable: a result of record per model (NA §NA6's per-cell list, L8 §M10's
phase columns, plus `source_web_served`, the copy lineage and both clients per pair), with O37's census section re-cut in the same commit.
Any public sentence, and any claim about the method, is the Captain's.

## §NCA9 · §H-CLIENT — the agy client's network tools across the install line (DECLARED, not a treatment within this block)
1. **Before the install (every agy cell of record, 705 cells: MATRIX, NA, ZF, WA, WA-pro, TA).**
   - OUTCOME, all 705: the PreToolUse web-deny hook was registered in every cell and denied nothing. It allowed every web call the
     census found served: 96 search_web, of which 80 are in the 10 cells of record (clients 1.2.3–1.4.3) and the rest in the l8
     pair, which is not of record (saltbench-systems drafts `o37-hook-census-2026-11-22` RESULT, ADDENDUM 1, and `o37-damage-account-2026-11-23` RESULT, at a0426dea).
   - MECHANISM, measured on agy 1.5.11 only: the hook read `tool_name`, and 1.5.11 sends `toolCall.name` (the lead's measurement, the
     raw event in the hook log of an OC step-1 tool-census invocation, b9e392bb5838, held in the private record).
   - MECHANISM on 1.2.x–1.5.10: UNMEASURED. Two candidates, not separated by any record (the hook census
     RESULT, "WHY ALLOWED"): (A) python3 did not run under the cell's fence, so the hook read an empty name and stood aside; (B) python3 ran
     and the event carried no `tool_name` equal to `search_web`. (A) is refuted for the CURRENT rendered profile only.
   - What was served: search_web in 10 cells (80 searches of record); read_url_content was refused by the client's own permission
     layer, before the hook (2 calls of record). Source: the damage-account RESULT and saltbench
     `evidence/o37-agy-web-served-2026-11-20/`.
2. **In this block (the DESIGN; it holds only after the install of the export that carries systems' row 235):** the export
   configures the hook to deny search_web, and the hook also LISTS read_url_content; a refusal of read_url_content is by the
   client's permission layer, which refuses it before the hook runs, so it does not exercise the hook (P-WEB tests search_web
   only). The export configures the hook to deny the swarm family (`swarm`, `swarm_*`, `*_board`; bench row 10). Every launch
   drives the registered hook under the cell's own fence, in the client's measured event shape, before any model call: search_web
   must exit 2, run_command must exit 0. That launch drive is the hook's own reply; the FIRST measurement that the CLIENT consults
   the hook is clause 5's battery fire. This line lands on saltbench no earlier than the install, inside the first registration it
   binds (NCA/WCA; bench row 14); a signature may come first, the landing waits.
3. **send_message is SERVED, as in every cell of record.** It is the subagent report-back channel: 768 calls in 361 of the 705
   cells of record, and every recipient is a conversation id or an agent name
   (saltbench-systems drafts `o37-damage-account-2026-11-23` sendmsg.tsv, script sendmsg.py: the data rows only, the six `#BLOCK` summary rows
   excluded; bench's ruling (B)). Exfiltration through it is MEASURED at the END read (`agy_fence_intact_v3.py` check 5).
   LIMIT, declared in the check's own words: the brain lives under .agyhome, which the subject can write, so this reads what the
   client recorded, the same trust as the rest of that file's hook reads; a send the client never recorded, or a record the subject
   rewrote, is outside it. A send DELIVERED to a recipient that is not a conversation id, `parent`, `self`, or an
   agent the cell defined VOIDs the cell (VOID(FENCE-TAMPER), declared). A send the CLIENT refused delivered
   nothing: it is COUNTED in check 5's detail and never voids. A send is client-refused only when its OWN result (the k-th GENERIC
   row of its turn, before the next PLANNER_RESPONSE; there is no call id) says "Encountered error" AND names the recipient, or when
   the client's log or step output names that recipient as not found (the 1.2.x log-only shape); an unrelated error beside a send
   excuses nothing, so a mis-attribution errs toward VOID. A cell with ZERO brain transcripts reads UNMEASURED(FENCE), never clean.
   Calibrated at the export candidate (saltbench-systems aa071afc, kent's findings 1-4 closed @109,469,279) over the 705 cells of
   record, 719 directory reads (MATRIX's ambiguous families read under each family): 0 VOID, FENCE-OK 712, UNMEASURED(FENCE) 7, the 7
   being unfired copies (ABORTED-unfired, UNFIRED, HALTED family names) whose cells of record live under the other name; by
   the damage account's recip_real.py (sha256/16 6f97ad46b7bd1952) → recip_real5.out (sha256/16 0764c292c01c9b1b). The earlier cut's output `recip_real4.out` (570489eab84f94c7) read 0 VOID with no UNMEASURED. Two sends of record were client-refused and would have voided under an earlier cut (s3ps03
   'subagent-paxos', nalsps03 'worker-sonnet'; RESULT.md ADDENDUM 1).
4. **Comparisons across the line are reported side by side and never pooled.** Within this block both arms run under the same
   client configuration, so within-block contrasts are unaffected. A contrast against a cell of record names the line.
5. **The first post-install fire is a battery fire, not a cell of record.** It must show P-WEB DENIED and P-SWARM DENIED, and a
   subagent-using turn must COMPLETE with send_message served (bench's arm (b), re-aimed). If any of the three fails, it is a HOLD
   that goes to bench, not a default.

## §NCA10 · §H-CLIENT-NOISE: the xcrun cache line the subject reads under the agy fence (DECLARED, the same in both arms)
1. **What the subject sees.** On the run box, `/usr/bin/git` and `/usr/bin/python3` are xcrun shims. Under the cell's fence the shim
   cannot write its cache file in the per-user temp directory, and it prints one line to stderr per attempt:
   `<tool>: error: couldn't create cache file '/var/folders/…/T/xcrun_db-XXXXXXXX' (errno=Operation not permitted)`.
   The tool itself then runs, and its exit code is unchanged.
2. **Where it appears.** It appears in two places, and the second is not new:
   - in every hook REFUSAL. The hook's one `python3 -c` writes the line(s) ahead of the reason. The client puts the hook's whole
     stderr into the step's error text. It has appeared there only since the install, because before the install the hook
     denied nothing (§H-CLIENT clause 1).
   - in the subject's own command output, whenever it runs `git` or `python3`. This happens in every agy cell read under the
     srt fence, before and after the install.
   Counted on the run box over each cell's brain transcripts (records that contain `xcrun_db`; the lead's script noise.py, held in
   the private record; gemini signed the count at bus offset 109,716,976):
   o37lf02 (the release battery, export aa071af): 15 in command output, 2 in hook refusals ·
   talf01 (battery, 11-17): 15 in command output, 0 in hook refusals · tamfs301 (cell of record, export 397864e): 43 in command output,
   0 in hook refusals.
3. **Why it is declared and not fixed in this block.** Both arms run under the same fence and the same hook, so the line is a
   constant across the arms, and within-block contrasts are unaffected. A fix would change the subject's environment:
   - silencing the hook's `python3` changes the hook bytes that were signed and released (blob 0e96efa2e82d), so it needs a new
     export and a new battery drive;
   - making the cache writable changes the fence.
   Either change would put a second line inside the block. Neither is made here.
4. **What a reader must not infer.** A refusal's text starts with this noise and then gives the reason (`BLOCKED by the harness: …`).
   §H-CLIENT clause 2 describes a deny by its exit code and reason, and both are as stated. The noise is not a second reason, and
   it is not a failure of the hook. A subject that reacts to the noise reacts to a constant of the lane.
5. **LIMIT.** I counted three cells, not the 705 cells of record. "Every agy cell under the srt fence" is a claim about the
   mechanism (the shim and the fence's temp-dir rule), and it is checked in those three cells only. A census of all 705 is
   possible and has not been run.
6. **Owed, at the next export (not this block):** the hook's `python3` gets `2>/dev/null`. A parse failure already fails closed,
   and the hook prints its own message for it, so no refusal reason is lost. The export's selftest gets one arm: on a block, the
   hook's stderr is exactly the reason line.

---
# ⚖️ ADDENDUM 1 (2026-11-23, bench) — RELEASE, ⛔ DRAFT: NOT A RELEASE UNTIL ITEM 6 FIRES AND THE QUOTA IS READ. APPENDED.
**Signature.** kent's non-author read of this file and WCA's at 97e81bb9 (bus offset 109,849,201), counted as the signature by the helm
(desk VN). Its coverage rides with the word: the §NCA9/§NCA10 citations and text, row 4's ancestry, commits and five files, and the
task trees by hash were checked by a non-author. The prices, source counts and the rules carried by citation were not.
**Export: saltbench-systems `88b63df9`** ("candidate 3") = the released aa071afc + the copy and fire repair of the lead's ruling (A)
(systems 339437fe..85301cdd: agy_cell_copy_v3.py re-installs ctl/web-deny.sh from the phase-2 export and records the replaced hash;
fire_agy_v3.sh fires a copy on the export its copied-from.tsv names and refuses a copy from another export's driver or with another
hook) + bench cadbf91f (dry_phase2_v3.sh, a dry tool no cell runs). ⚖️ **A DEPARTURE FROM §NCA0 row 4, DECLARED:** the harness differs
from aa071afc in 5 files (agy_cell_copy_v3.py, fire_agy_v3.sh, agy_wave_v3.sh by 2 lines, dry_phase2_v3.sh, one fixture). The web-deny
hook, the launcher, the referee, the builder and every task tree are unchanged. Why: at aa071afc no copy could fire (58/58 sources
carry the pre-fix hook a6e064e307a8651d, which aa071afc's launcher refuses), and a copy's phase 2 took its harness from the SOURCE
export. Both contradict this file's row 4. Reads: kent on 339437fe (bus offset 109,902,645) and its deltas (109,917,950; 109,935,907).
On the run box as `saltbench-systems-v3-export-88b63df` (EXPORTED-FROM.sha 88b63df9c5be).
**Client:** agy 1.5.11, sha256/16 62f2102784bb74b7, read on the run box 2026-11-23.
**§NCA3 receipts (WCA's §WCA3 the same, by citation):**
1. MET by hash at 88b63df9: AES 00b919ce · BinomialHeap df6427a9 · LinearScan a3c8ae15 · Liveness 143296d6 · Luby 6db3c763 · MaxFlow
   5b89c4df, each 36ca596b's whole tree; WHT 44b92115 and NTT 77c64177, WC's d55062a6 trees. NC's and WC's non-builder drives are CITED.
2. MET at aa071afc (gemini, 2026-11-23, harvest 24/24 match for NCA and 8/8 for WCA): both references PASS on both arms at full count,
   and one clause and one regression mutant per task fail with the builder's counts. The referee and builder are byte-unchanged at
   88b63df9, so the drive is CITED.
3. MET (gemini, 2026-11-23 19:12–19:20Z, gbase.sh on clones; controls GREEN AES 8/8, RED LinearScan 0/0): NCA Flash plain 18/18,
   salt-diet 16/17; WCA Flash 12/12, argon 12/12. 58 of 59 sources ELIGIBLE. SHORTFALLS: nabhfs03 (no landing) and nalsfs202
   (LinearScan salt-diet, 8/9, as at NA). So the copies are NCA Flash 34 · WCA Flash 12 · WCA argon 12, and the fresh cells are NCA
   Flash 2 plus NCA argon 36. ⚖️ The instrument read landed-1, as registered (lead's ruling, bus offset 109,861,760 ff.). A
   NON-REGISTERED side reading on each of the 27 sources that also carry landed-2 passed in full on the newer tag: no eligibility
   would change. It is declared here, never used as the instrument.
4. MET at 88b63df9 (gemini, 2026-11-23 21:15–21:20Z, stub client, zero spend; real eligible sources nalbfq01 Flash and wanap101 argon):
   C-flash and C-argon REACHED (copy re-installs the canonical hook 5383c08a19eb8171 over the source's a6e064e307a8651d; FIRE line
   names 88b63df9; landed gate rc 0; §M3 PASS; change-1.md equal; aside; source byte manifest unchanged). D (stale fence) and E (pre-fix
   hook) HELD. Red backwards: on aa071afc both C arms are NOT REACHED. LIMITS: a stub client in phase 2; 2 of 58 sources.
5. MET by citation: the leak run at aa071afc (CLEAN, 343 identifiers across 13 tasks, 0 in any view). The task trees and the checker
   are unchanged at 88b63df9.
6. ⛔ OPEN: the lane-live battery on the release export, one dry cell per model on the client above, with P-WEB and P-SWARM DENIED and a
   subagent turn completing with send_message served (§NCA9 clause 5). Flash was measured at aa071afc (o37lf02). Both models re-run at
   88b63df9 because fire_agy_v3.sh changed. Any failure is a HOLD to the lead (§NCA9 clause 5).
**The replaced-hook gate (kent's MEDIUM 2, the lead's statement):** a copy's phase 2 runs the PHASE-2 export's canonical hook, and the
source's hook is replaced by design, never trusted. Each copy records the replaced hash. TWO checks: (i) the TOOL (since 8ec128b7)
refuses a source whose hook differs from the hook its own build recorded (built-from.tsv `web_deny_hook … sha256=`); (ii) the RELEASE
compares every copy's replaced hash with the census value a6e064e307a8651d (gemini's census: 58/58 eligible sources), and any other
value HOLDS that copy for a lead ruling before its phase 2 fires.
**Copies and fresh roots are made in a QUIET WINDOW** on the run box: no Claude-lane or agy cell live, as cells roots are made. A root
created or removed under $HOME during a live cell drifts that cell's fence (measured 2026-11-23 21:12Z on clbpwp01: held, nothing spent).
**Quota: ⛔ OPEN** (§NCA0 row 7: P3 on the agy pool, yielding to any O4 agy cell; agy /usage read at each fire). **Order:** §NCA4 / §WCA4.

---
# ⚖️ ADDENDUM 2 (2026-11-24, bench) — THE RELEASE. ADDENDUM 1's two open items are filled here, and this heading is the release, effective when it reaches `main` after a non-author read. APPENDED; ADDENDUM 1 is unchanged.
**Item 6: MET at 88b63df9** (the agy lane's battery r3, bus offset 110,083,627; driver blob 52875cd1c451969f, END rc 0 at 2026-11-24
04:27:55Z; marker checked; the five hook-lane blobs equal kent's read-back). One dry cell per model on client agy 1.5.11 / 62f2102784bb74b7,
read before AND after:
```
gemini-3.8-flash-high   o37lf03   preflight BATTERY GREEN   SERVED verdict OK, 168 steps   P-SWARM DENIED · P-WEB DENIED · P-SUBAGENT COMPLETED
gemini-4-argon-high     o37la03   preflight BATTERY GREEN   SERVED verdict OK, 264 steps   P-SWARM DENIED · P-WEB DENIED · P-SUBAGENT COMPLETED
```
P-SUBAGENT COMPLETED means one `invoke_subagent` answered with one `send_message` delivered and no refusal (§NCA9 clause 5). This is the
first post-install battery fire on the release export. LIMITS, carried: n = 1 per model, Luby salt-diet, `--statement` dropped; the live
artefact line reads RC-1=0 RC-2=0 RC-3=1 on both, the same as r2 (11-23) and ta-r4 (11-18).
**The quota: NAMED** (the PM, bus offset 110,146,697). NCA and WCA fire on the agy pool (Gemini Models weekly), read at each fire, **ahead of
any O29 OC scored call** (O37 is priority 2, O29 priority 3). Their stop is the pool's 10 % reserve: no NCA/WCA cell fires at a reading
≤ 10 % remaining before the 11-30 reset, and a reading that cannot be taken counts as a stop. The OC wave's own stop is 30 %, so OC yields
first.
**Every §NCA3 receipt is MET** (items 1–5 in ADDENDUM 1, item 6 above). Export 88b63df9, client agy 1.5.11 / 62f2102784bb74b7, the
signature as ADDENDUM 1 states it.
**At the first fire, three things are read and posted, and each refuses if it fails:** the pool reading (the stop above); the client's sha
on the run box (a moved client HOLDS, §NCA9); and a QUIET WINDOW for copy and fresh roots (ADDENDUM 1). The OC scored wave, live on the
same box at this writing, is an agy cell lane: it is brought to a seam, never killed, before NCA/WCA roots are made, and NCA/WCA then take
the pool ahead of it.

---
# ⚖️ ADDENDUM 3 (2026-11-24, bench) — THE SUPERVISOR AND THE COPY ROOT: TWO DECLARED DEPARTURES THE FIRST FIRE FOUND. ⛔ NOT IN FORCE UNTIL
# A NON-AUTHOR READ OF THE SUPERVISOR CANDIDATE IS CITED HERE AND THIS REACHES `main` ON THE HELM'S WORD. APPENDED; ADDENDA 1–2 unchanged.
**What the fire found** (the hand, bus offset 110,337,678, driven by `--plan`, zero spend, nothing made): (1) §NCA4 fires "through the canary
wave supervisor", and the supervisor at 88b63df9 admits level 8 only, so it refuses every NCA and WCA row (copy rows at its C2 gate, fresh rows
at R2). The item-4 copy drive had called `agy_wave_v3.sh` directly, so nothing had exercised that gate. (2) §NCA2's copy root,
`<source root>-ncacp`, collides under §NCA4's per-cell order: a condition's later cells need the root that its first cell's wave made, and the
driver refuses an existing root.
**THE LEAD'S RULINGS** (bus offset 110,343,209, before any data):
**(A) THE SUPERVISOR: saltbench-systems `991ac98a`** (backup `gemini/o37-nca-supervisor-gate-2026-11-24`, = 88b63df9 + ONE file,
`harness/systems-v3/gemini_canary_wave_v1.sh`, sha256/16 db6dab3562e26d07). It admits three anchored forms: copy rows
`^cells-na-…-ncacp[1-3]$` and `^cells-wa-…-wcacp[1-3]$` at AGY_PHASES=2 only, with the source checks C1/C3 kept (C3 requires every source's
root to equal the row's base), and fresh rows `^cells-nca-…$` at AGY_PHASES=1,2 only. Every level-8 row is classified as before. It also
CLOSES A HOLE: at 88b63df9, a copy or fresh row with AGY_PHASES unset or 1 read OK and would have fired phase 1 only into a spec-change root
(new refusals S2/S3). Receipts (the hand, bus offset 110,351,659): selftest 131/131 (110 pre-existing + 21 new); a mutant with 88b63df9's
classification reads 117/131 and fails exactly the 4 admit arms and 10 refusal-tag arms; 88b63df9's own file refuses all 4 admit shapes at
the phases gate (rc 4) before any ssh; `--plan` on the tripwire rows T-NCA-F and T-NCA-A reaches their plan lines against the run box.
⚖️ **DEPARTURE FROM ADDENDUM 1's EXPORT, DECLARED:** the supervisor runs on the lead's box and no cell reads it. The launcher, the hook,
fire_agy, agy_wave, the copy tool, the referee and every task tree stay byte-equal to the release export 88b63df9. **Non-author read: ⛔ OWED**
(asked of kent by the hand at 110,351,659).
**(B) THE COPY ROOT: one root per cell, `<source root>-ncacp<k>` and `<source root>-wcacp<k>`**, where k is the cell's rep within its
condition (1 to 3). §NCA4's interleave and the one-cell tripwires stay as registered. **DEPARTURE FROM §NCA2 / §WCA2, DECLARED:** the root
NAME only. The lineage stays in each copy's `ctl/copied-from.tsv`.
**THE FIRST FIRE, IN ORDER:** (1) the canary supervisor's standing probe is started on the run box (no cell; it read "UNMEASURED (no pidfile)"
in the hand's plan, and its gate needs HEALTHY); (2) the lead writes the OC wave's `ledger/HOLD`, and OC halts before its next call (its
seam); (3) `nca-quiet-gate.sh` reads QUIET (rc 0) on the run box; (4) ADDENDUM 2's pool and client reads; (5) the tripwire T-NCA-F, posted
before its model continues. The three refusals were driven RED in the code that runs (bus offset 110,323,681: pool rc 6 ×2, client
rc 10, quiet gate rc 3, seat 0dbbfa92c7).
