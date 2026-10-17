# AMENDMENT — desk OD: THE EFFORT MATRIX. Fable/xhigh · Fable/high · Opus/xhigh, greenfield bare plain, CLAUDE LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-10-16. The Captain, council 2026-09-15: *"what is the relative cost/ability between Fable/xhigh to Fable/high
## to Opus/xhigh? I chose xhigh as the default because of a message several months ago that xhigh had the same price as high -- but surely
## that can't be."* Then: *"yes, charter it."* Council 2026-09-17 ㉓: *"helm's rec, charter stands"* (the one-line `--effort` build and an
## honest v3 baseline). bench is lead AND hand on this lane, as in lane B and block N.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES BEFORE §D2's ITEMS ARE DRIVEN AND A RELEASE ADDENDUM NAMES THE EXPORT SHA.**
## Signature and release are two acts, as in lane B.

**What this file carries by citation.** It is a block under `AMENDMENT-claude-lane-B-2026-09-16.md`, narrowed exactly as block N
(`AMENDMENT-O37-nine-greenfield-claude-2026-09-25.md`) narrowed it for greenfield × `none`: lane B's preflight (§Q3.4, with its ADDENDUM 5's
one-live-cell-per-pool rule and §CLB-A's required ancestors), caps (§Q4), confounds (§Q5), reading rules (§Q6 rules 1, 2, 3, 6–9), voids
(§Q7 less rows 6–7) and deliverables (§Q9). Its outcomes are `DESIGN-correctness-primary-2026-10-02.md` §D3 (the design of record, PR #311),
and this file is that design's §D8 freeze for this run. A clause below that differs from any of these says so, and says why.

---

## §D0 · THE INPUTS
```
  1  CONFIGURATIONS  three, each a HEAD model and a HEAD effort:
                       FX  Fable/xhigh   head claude-fable-5-1   CELL_EFFORT=xhigh
                       FH  Fable/high    head claude-fable-5-1   CELL_EFFORT=high
                       OX  Opus/xhigh    head <the Opus id, row 1b>   CELL_EFFORT=xhigh
                     Every id is passed to the client IN FULL, never as an alias (`fable`, `opus`), because an alias resolves at
                     launch and may resolve differently between cells. `claude-fable-5-1` is the id `claude --model fable` resolved
                     to at the object (CLAUDE.md fleet map, the 2026-09-22 measurement).
  1b THE OPUS ID     the Opus id the fleet's `opus` resolves to on the run box at the release, read at the object and named in the
                     release addendum (this session reads `claude-opus-5-5`; that is a reading on another box, not the registration).
                     ⚖️ FORK F3' (§D6). It links to the pilot's `claude-opus-5` cells of record ONLY if it is that same id; otherwise
                     OX is a NEW baseline and every table says so (kent's rider R2).
  1c THE TEAM        the sub-agent rows of the run root's models.tsv (worker-opus · worker-sonnet · reviewer · designer) are HELD at
                     the pilot's Opus table in all three configurations; only the `head` row moves. So a cell differs from its
                     neighbour in the HEAD's model and effort, and in nothing else the harness sets. ⚠️ A team row whose id is not
                     served on the release day moves in the release addendum, by name, for ALL three configurations at once.
  2  n               3 per (configuration × problem).
  3  POPULATION      3 configurations × 3 problems × n 3 = 27 cells (§D1). Nothing is added, dropped or substituted.
  4  EXPORT          ONE bare-master sha of saltbench-systems, named in the release addendum BEFORE the first cell, carrying §D2's
                     build items (S1 `CELL_EFFORT` at or descending from cf0033e; the rates rows of item 2) and descending from
                     block N's last release export. One sha for all 27 cells, recorded per cell.
  5  CLIENT PIN      lane B §Q0 row 5's form (the versioned client by ABSOLUTE PATH, its sha asserted per launch). The VERSION is
                     named in the release addendum, and it must accept both `--effort xhigh` and `--effort high` with a Fable head
                     (§D2 item 3). A cell launched on another version is refused.
  6  TASK TREE       the EXPORT's own tasks/systems-v3, and nothing else.
  7  CAPS            lane B §Q4: C1_USD $37.21, W1_SEC 144,000; CAP-COST and CAP-WALL armed. Read WU (a) below.
  8  CHAIN           runs/clb-sg-2026-09-18/clb_chain.v8.sh (v7 + flock), the only chain in the run dir that can start: every older
                     script exits rc 2 at its line 2 (retired 2026-10-16). Its sha256/16 is quoted in the release addendum.
  9  POOL            Fable heads draw the Fable-only meter. His charter names Fable configurations, so the word the commission
                     asks for is given. The pool is named per cell, with `cells_account_check.sh --expect <identity>` reading OK
                     before each fire. The PM places the 27 on the day lines from the identity cells' readings (§D3); nothing here
                     asks for spend past the budget.
```
⛔ **WU (a), C2_USD's MEANING, WRITTEN WHERE A READER MEETS THE CAPS:** `C2_USD` is a CELL-TOTAL cap evaluated during phase 2, NOT a phase-2
budget (`cell-watch.sh` compares it against the whole slug's meter). **No cell here has a phase 2** (greenfield × `none`), so it binds no
cell in this block, and it is written here because the Claude lane's next spec-change block will inherit this text.

---

## §D1 · THE POPULATION — 27 CELLS
```
  problems        Crc32 · LZW · FreeList       as chartered; each has a claude-opus-5 bare-plain result of record at 3 / 3
                                               (RESULT-correctness-tables-v3-2026-10-01.md, Table P1)
  field · extras  greenfield · none (bare)
  arm             plain ONLY                   fork F1: the question is about the knob, not the method
  configurations  FX · FH · OX                 §D0 row 1
  ⇒ 3 × 3 × 3 = 27 cells
```
**Not in this block, and why:** salt-diet (F1; it doubles the spend and folds the method's cap correlation into a knob reading) · Opus/high
(not in the charter; the pilot ran it at `claude-opus-5`, and it re-enters only by F3') · any other problem (F5 was measured EMPTY on the
Claude lane: every Claude bare-plain cell of record is 3 / 3 except claude-sonnet-5 FreeList at 2 / 3, already chartered).

---

## §D2 · ⛔⛔ THE BUILD ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **`--effort` AS A VARIABLE (systems' backlog S1).** saltbench-systems `cf0033e`: `--effort "${CELL_EFFORT:-high}"`, a value outside
   `low medium high xhigh max` HOLDs `EFFORT` by name before any ARGV line. The lead's re-drive (the bus, 2026-10-16): the selftest suite
   on the branch, plus a mutant hard-wiring `--effort high`. The unset default is the literal it replaces, so every earlier cell's argv
   is unchanged. *The release addendum quotes both runs' tallies.*
2. **THE RATES TABLE PRICES EVERY HEAD.** `rates.tsv` (read 2026-09-05) carries `claude-fable-5-1` and `claude-opus-5` and NO row for
   `claude-opus-5-5`, and the meter prints a model with no row as `VOID(UNPRICED)`. ⇒ **An OX head the table cannot price has no armed
   CAP-COST.** Before release: the pricing page is RE-READ and every row the block uses is re-dated (the table's own header asks for this
   before any run whose caps are set in cost), and a row for the §D0 row 1b id is added from that page. The meter's selftest on a record
   carrying that id is green, and red with the row removed.
3. **A ZERO-SPEND DRY LAUNCH (kent's R4).** On the pinned client, `cell-claude.sh --launch` with the DRY stub prints three ARGV lines
   that differ in `--model` and `--effort` exactly as §D0 row 1 says, and the pinned client's own `--help` lists `xhigh` among its effort
   levels. The effort modal (desk MZ) was measured interactively only, so the identity cells (§D3) are also the first `-p` drive of a
   Fable head at xhigh: a cell that stalls on a dialog is a FAULT (§D7), never a result.
4. **THE CLAUDE-LANE FIRE PREREQUISITES:** (a) the chain is v8 (§D0 row 8); (b) WO (b): a `declined-subject` probe
   verdict (the subject answered the sandbox probe and refused) is RECORDED on that cell's RESULT row, never silently re-routed to another
   pool or re-fired as an instrument fault; (d) WO (d): `credgate identity` per pool and the status line's `strands=` are read before the
   first cell and quoted in the release addendum; (c) WU (a), written in §D0; (e) ⚠️ `cells_account_check.sh` (block N §N2 item 2) is
   at saltbench-systems `0da916f` and is NOT an ancestor of master at `cf0033e`: the export carries it, or the release addendum names the
   path and sha the check runs from. A check that is not in the export is not evidence that the export was checked.

---

## §D3 · THE ORDER, THE IDENTITY CELLS, THE TRIPWIRE
- **Identity cells first: ONE per configuration, on Crc32** (the cheapest chartered problem). Each must show, in its transcript, every head
  `message.model` equal to the requested id, and every sub-agent `message.model` equal to its models.tsv row. An unrecognised id
  SUBSTITUTES silently, so this read is the only evidence of what was served. **The applied effort is NOT in the transcript**: the argv in
  the launch record is the only record of it, and that limit rides beside every figure. An identity cell that reads clean counts as cell 1
  of its (configuration × Crc32) condition unless §D7 voids it.
- **The tripwire is the identity triple**, read by the lead and posted before the block continues: the three served-set reads · each
  cell's T, output tokens, wall and list-USD · the Fable-meter reading before and after each Fable cell. **The PM's points-per-cell
  estimate is written from these three cells and from nothing else**, and the remaining 24 are placed on the day
  lines from it.
- **Then interleaved by configuration within each problem**, one cell at a time on one pool: Crc32 #2–#3 (FX FH OX FX FH OX), then LZW #1–#3,
  then FreeList #1–#3. Interleaving removes the time-of-day and quota-state confound a blocked order would build in.
- **Stop rule.** If the tripwire price puts the 27 past desk OD's review (2026-10-30) on the day lines, the lead posts that with an order
  before any cell beyond the tripwire: a cut removes a WHOLE PROBLEM (all three configurations), never one configuration alone, and n is
  never reduced quietly.

---

## §D4 · THE OUTCOMES — design §D3, mapped onto the v3 classes, and the ceiling rule FIRST
- **Classes** (`REGISTRATION-correctness-tables-v3-2026-10-01.md` §P2, registered here BEFORE the run): PASS · FAIL · CENSORED · UNSCORABLE,
  read as design §D2's ACCEPTED · REJECTED · HALTED · UNSCORABLE. The subject's landing claim never decides a class.
- ⛔ **THE CEILING RULE (kent's R1), REGISTERED BEFORE ANY CELL:** if every cell of two configurations on a problem PASSES, that problem's
  ABILITY reading for that pair is **NO INFORMATION**, never "equal", and the problem reports its COST reading alone. ⇒ **THIS BLOCK IS
  REGISTERED COST-FIRST:** all three problems sit at 3 / 3 for `claude-opus-5` at high, so ability is EXPECTED to read NO INFORMATION.
  Ability against effort belongs to a population that can show it (HV item 4's harder problems), not to this one.
- **Ability, where the ceiling rule permits:** design §D3 1, (i) and (ii), per configuration per problem, with §P4's interval rule for a sign.
- **Cost per task, per configuration per problem:** design §D3 2's row `a · r · h · u` and (c0) · (c1) · (c2), in METERED T (input + output +
  cache reads + cache writes), with **OUTPUT TOKENS printed beside T in every row** (T is ~97 % cache reads in this lane; the knob is
  expected to move output). A halted cell's spend enters as METERED, never clipped (design §D3 2, overriding lane B §Q6 6). Wall time is
  printed beside, never as a cost. **List-USD** from the re-dated `rates.tsv` (§D2 item 2) is printed as a third column, labelled
  *list price at <date>*: a subscription meter is not a price, and the Fable-meter reading per cell is printed beside it where measured.
- Rule 3 holds: no cost figure is pooled across problems.

## §D5 · PREDICTIONS — REGISTERED PER CONFIGURATION BEFORE THE FIRST FIRE
Each is descriptive at n = 3 (no test) and is reported MET or NOT MET:
- **P1** FX spends more OUTPUT tokens per cell than FH on at least 2 of 3 problems (median of 3).
- **P2** FX's acceptance is not below FH's on any problem by §P4's interval rule. *Scored only on a problem where some configuration falls
  below 3 / 3 (R1); at 3 / 3 it passes by construction and is reported NOT SCORED.*
- **P3** The ratio of median OUTPUT tokens, FX over FH, is above 1.2 on every problem. This is the direct test of "the same price": if it
  fails, the remembered message was right per task as well as per token.
- **P4** OX's acceptance equals FX's on all three problems. *Same R1 scoring as P2.*
- **P5** (new, from §D0 row 7) CAP-COST binds no cell. One USD cap is a different token budget per head (lane B §Q5 3): at `rates.tsv`'s
  rows (2026-09-05) Fable's input, cache-write and output rates are 2 × `claude-opus-5`'s and its cache-read rate is 0.5 ×, so the cap
  costs Fable more per OUTPUT token and less per cache read. If it binds at all, it binds FX first, the output-heaviest configuration.
  A miss is a result, and a cap-out enters (c0) as metered.

## §D6 · FORKS — each with the lead's recommendation, taken unless overturned
- **F1, the arm:** plain only (taken).
- **F2, n:** 3 (taken). n = 1 cannot report a per-condition comparison, so a 9-cell pass would be spent again.
- **F3', the Opus id:** the fleet's current Opus (rec: it is the knob he is asking about), or `claude-opus-5` if still served (it links OX
  to the pilot's cells of record, at another effort). The release addendum names which, and why, from the identity read.
- **F6, the team (new):** hold the sub-agent rows at the pilot's Opus table (rec, §D0 row 1c), or make each configuration single-model.
  Single-model would move the team with the head, so a configuration difference would be a TEAM difference (lane B §Q5 1). Holding the
  team keeps the knob on the head, which is what `--effort` sets.

## §D7 · CONFOUNDS AND VOIDS — lane B §Q5 and §Q7 carried, plus these
1. **THE KNOB IS THE HEAD'S.** `--effort` is the head session's flag. Whether a sub-agent inherits it is UNMEASURED, and no transcript
   field records the applied effort. A configuration difference is a HEAD-effort difference in argv, and is never described as more.
2. **FX ↔ OX IS A CONTRAST, NEVER A TIER RESULT:** model tier and generation move together (desk OD's own clause). It is reported as "these two
   configurations", never "Opus vs Fable".
3. **THE CEILING:** three problems at a ceiling-prone difficulty. A knob that matters only on hard problems reads as no difference here.
4. **ONE CLIENT VERSION:** a client update between cells is a confound, so the pin is enforced per launch (§D0 row 5).
5. **VOID ROWS ADDED:** a head or sub-agent `message.model` other than its requested id ⇒ VOID(SERVED), the cell re-fired once after the
   release addendum names a corrected id · a cell that stalls on a client dialog ⇒ FAULT, re-fired once · `cells_account_check.sh` not
   OK ⇒ DO NOT FIRE (block N's row 11).

## §D8 · WHAT THIS BLOCK CANNOT ESTABLISH, SAID BEFORE ANY DATA
1. Ability against effort, on these problems: it is registered to read NO INFORMATION wherever all cells pass. 2. Anything about salt-diet
or about the method. 3. Anything about Opus/high at the current Opus. 4. The effort the client APPLIED: only the effort it was ASKED for.
5. A price: list-USD is a list price at a date, and the subscription meter is the fleet's real cost.

## §D9 · WHAT THE HAND DELIVERS
Lane B §Q9's per-cell list, less its brownfield columns, plus: the configuration and its argv per cell · the head and sub-agent served set ·
output tokens beside T · list-USD at its dated rate · the Fable-meter reading per Fable cell · the account-check line. ⇒ **A RESULT file with
§D4's rows per configuration per problem and §D5's predictions MET / NOT MET / NOT SCORED, merged with a non-author read.** Desk OD is
re-read against it. Any public sentence, and any claim about the method, is the Captain's.
