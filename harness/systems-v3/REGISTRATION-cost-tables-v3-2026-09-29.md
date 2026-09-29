# REGISTRATION: THE COMPLETE PILOT MATRIX IN THREE CURRENCIES — TOKENS, DOLLARS, WALL TIME (arXiv v3), DECLARED POST HOC
## bench (SaltBench lead), 2026-09-29, written before any v3 table number is computed. Council 2026-09-28 §1 A2′, the Captain's words: *"We have tokens (incomparable across models), dollar cost (comparable), and wall time (comparable). Can we get tables for everything?"* and *"yes, let's add all three metrics in the paper."* Plan and price: desk YP (the private record).

⛔ **THIS READING IS POST HOC, AND IT IS DECLARED AS SUCH**, for the reason v2's registration gives: every condition already
has a result of record, and many per-cell dollar figures (the Claude block tables' `final_COST`) have been read. What is fixed
here is the METHOD. ⛔ **AND WHAT HAS ALREADY BEEN SEEN, STATED EXACTLY:** the raw extractions of steps b–e are tracked in
`evidence/v3-cost-tables-2026-09-28/`, and their READMEs print aggregate counts: step coverage, the largest observed Pro request
prompt (144,717), the share of Opus-headed T outside the head session (11.65 %), and the list rates themselves. **No median, no ratio and no
per-condition dollar or wall figure has been computed.**

⛔ **IT IS DESCRIPTIVE.** No test, no p-value, no verdict on the arms; the registered tests remain §4's. A dollar ratio is a
cost description, not a quality comparison, exactly as v2's token ratio is.

## §V1 · THE POPULATION: v2's, UNCHANGED
The 200 conditions and 540 cells of record in `CELLMAP-descriptive-tables-v2-2026-09-27.tsv`, as reprinted at v2 ADDENDUM 2
(every cell of record in its condition). Each cell's cells root is the one `evidence/v3-cost-tables-2026-09-28/cellroots.tsv`
names (step a: 517 of 517 ids resolved, 0 ambiguous). **No cell is added, dropped or re-fired for this reading.** The ten
conditions at n < 3 (census ADDENDUM 25) stay at their n; bringing them to 3 is a spend under its own freeze (desk YP step g),
not part of this reading. Blocks N and NA (O37) are outside this population and carry their own columns in their own results.

## §V2 · THE CELL FIGURE, ONE PER CURRENCY
**Tokens.** v2's `T`, unchanged, cited from v2's result file and not recomputed.

**Dollars, Claude lane.** Modelled list-price dollars, never an invoice (every cell ran on a subscription).
- The figure is `cell_meter.py`'s COST: every record priced at its SERVED model's own rates, so an Opus cell's Sonnet subagent
  tokens are priced at Sonnet's rates. Rates: `rates.tsv` (read 2026-09-05), whose rows for `claude-opus-5` and `claude-sonnet-5`
  were re-read against the Claude pricing page on 2026-09-29 and AGREE on all five columns (step b).
- Source, in order: (1) the cost column of the SAME tracked row v2 read `T` from, where that row carries one; (2) otherwise the
  step-e-form extraction (`cell_meter.py --json`, export `9d873183acab`, over the cell's own slug), tracked in the evidence dir.
  **Second method, and it gates the run:** wherever (1) exists, (2) is computed too, and the two must agree to the cent or the
  instrument exits non-zero naming the cell.
- A spec-change cell's figure is the SUM of its phases (v2 A1.1).

**Dollars, agy lane.** Priced here for the first time, from `rates-gemini-2026-09-29.tsv` (step b).
- **Per request:** `input × in + cache_read × cache + (output + thinking) × out`, at the tier of that request's PROMPT, where
  prompt = `input + cache_read`. Three definitions, each MEASURED rather than assumed: `input` excludes cache reads (in 263 of 264
  COMPLETE rows, `cache_read` exceeds `input`, so `input` cannot contain it); `output` excludes thinking (`total_tokens == input +
  output` on 472 of 472 steps sampled); and the page bills thinking as output.
- **Basis:** the stream's per-request records, where they account for at least the meter's fold on every key (COMPLETE, or
  EXCEEDS-METER, step c). Otherwise: **Flash** is priced from the meter's per-key totals, because Flash has one tier and its price
  is linear in the totals; **Pro is `unmeasured`**, because a request whose usage is lost cannot be put in a tier, and pricing it
  at one tier is the error this rule exists to refuse.
- Context-caching STORAGE is not priced (no stream records cache-hours); the caption says so.
- The six EXCEEDS-METER rows are priced from the per-request records and flagged in the result file, because there the dollar
  basis is larger than the basis of v2's `T`.

**Wall time.** Seconds, per cell, per phase, summed over phases for a spec-change cell.
- **Claude lane:** step d's reading: the last `METER … wall N/CAP` line of each phase in the cell's own `watch.log`, NET of held time
  (a hold is printed beside it). It understates by at most one watcher tick (~60 s), and the caption says so.
- **agy lane:** the turn loop's `wall_seconds`; where a phase has no turn-loop file (level 8 phase 1), the wall column of the
  tracked record that condition's result cites; otherwise `unmeasured`.
- **Wall measures the box, not only the model** (his words): the result file names, per lane, what else was running where a record
  says (`claude_live_at_fire`, the agy concurrency column, the one-heavy-job lock). It does not quantify the effect; no per-cell
  load series exists outside one sampler day.

## §V3 · THE CONDITION CELL AND ITS MARKS
The median over the condition's cells of record, by v2 §D3's rule, applied per currency. **A lower-bound cell (`≥`)** is one whose
record classifies it CAP-COST, FLOOR or DEADLINE (v2 A1.2), in every currency, plus:
- **Dollars:** a CAP-COST cell enters AT THE CAP (lane B §Q6 rule 6), `≥`. A `VOID(UNDERSTATED)` meter reading is `≥`.
- **Wall:** a cell whose wall reached its registered wall cap is `≥`, read BY TIMING (the recorded wall within one turn timeout of
  the cap), because the turn loop labels a mid-wait wall `TURN-TIMEOUT` (the NA result, §4); a cell cut by a deadline other than
  wall is `≥` in wall too.
- `—` INEXPRESSIBLE (16) and `declared` (3) exactly as v2. `unmeasured` exactly as v2: never hand-recovered.

## §V4 · THE TABLES
```
  $1–$3   dollars: v2's T1 (greenfield), T2 (brownfield), T3 (spec-change) shape, same rows, same columns
  $4      dollar ratios: v2's T4 shape, sign counts by v2's rule
  W1–W4   wall seconds: the same four, the same rules
  S1      the Opus head-vs-subagent split: per Opus condition, the median share of T and of dollars outside the head session
  CHECK   in every one of $1–$3 and W1–W3: numbers + "—" + "declared" + "unmeasured" = 200, or the instrument exits non-zero
```
- **Tokens are NOT reprinted**: the paper cites v2's T1–T4. **Dollars are the cross-model column**, which is the reason he asked for
  them: one list schedule per vendor, both read on 2026-09-29.
- The result file prints, per currency, how many conditions are `unmeasured` and why, so a count lower than v2's 171 is visible.

## §V5 · THE INSTRUMENT AND THE FILE OF RECORD
ONE instrument (`tables_v3.py`), ONE result file (`RESULT-cost-tables-v3-2026-09-29.md`), ONE sha. It reads v2's CELLMAP, the
tracked sources v2 names, and the tracked step a–e extractions, and it lands in the SAME COMMIT as the result. It carries a
selftest, and each rule above has an arm that a mutant of that rule reddens. Captions: *a descriptive reading; no test, no verdict
on the arms; dollars are list-price models, not invoices, one schedule per vendor read 2026-09-29; wall includes the box.*

## §V6 · WHAT THIS READING CANNOT ESTABLISH, SAID BEFORE ANY NUMBER
- It cannot say the salt method helps or hurts. A cheaper arm is cheaper, not better.
- Dollars across vendors are comparable only as LIST prices on one date. Neither lane paid them.
- Every `≥` is an arm-correlated censoring, as in v2: the cap binds the salt-diet arm more often, so a capped salt-diet numerator
  makes a ratio an UNDERSTATEMENT.
- Wall time depends on what else the box was doing, and on the vendor's service at that hour. It is a description of these runs.
- n = 3 per condition (n < 3 for ten). A median of three is one cell's figure.

---

## ⚖️ ADDENDUM 1 — THREE DEFINITIONS THE EXTRACTIONS REQUIRE, FIXED BEFORE THE INSTRUMENT RUNS. APPENDED; §V1–§V6 untouched.
Building the instrument's inputs found three things §V2–§V3 did not settle. No median, ratio or per-condition figure has been
computed; the facts below are per-cell properties of the inputs.
- **A1.1 · Level 8's phase 1 is read from where level 8 put it.** §V2 names level 8 phase 1 as a phase with no turn-loop file. That was
  a reading of the cell's own `ctl/` only. Level 8 set each finished phase ASIDE before the next ran, and its tracked `phase_facts.json`
  names the path (`<root>/_aside/<cell>/phase1/ctl/`). The stream and the turn loop are read there; the meter file stays the cell's
  own. With it, every one of the 332 agy phase rows has a stream: 321 COMPLETE · 8 EXCEEDS-METER · 3 PARTIAL (Pro: 154 · 7 · 3).
  **Second method for those 60 walls:** `phase_facts.json`'s `wall_seconds` must equal the turn loop's to 0.1 s, or the run exits non-zero.
- **A1.2 · The Claude extraction covers every Claude cell, and it carries each cell's own caps.** `claude-cost-raw.tsv`: cell_meter
  over all 245 Claude cells (two cells ran their phases under two config dirs and are summed), with `C1_USD`/`C2_USD` read from each
  cell's own `ctl/budgets.env` (37.21 / 18.60 in all 245).
- **A1.3 · WHAT "ENTERS AT THE CAP" MEANS WHEN THE METER RAN PAST IT.** Lane B rule 6 says a capped cell's cost enters at the cap. Two
  facts of record make that literal reading print a figure BELOW money the cell had already spent: the watcher prints an overrun and
  never clips it, and **the phase-2 cap is CUMULATIVE** (the SC block's result: `clbczs01` was cut 32 cents into phase 2 at 24.29 of
  18.60, `clbczs02` likewise). So a CAP-COST cell's dollar figure is **the larger of its metered COST and the cap its end marker names,
  marked `≥`**. This departs from the literal rule in the upward direction only, and only by spend the meter recorded; every such figure
  is a floor either way. The result file prints, per capped cell, the cap, the metered COST and which one entered.

---

## ⚖️ ADDENDUM 2 — THE NON-AUTHOR READ (kent, blob 2445c62ba3b6 at head 00d5d67de4b0): 1 KILL · 2 DEFECT, ALL TAKEN, BEFORE THE RUN. APPENDED; §V1–§V6 and ADDENDUM 1 untouched.
- **A2.1 · KILL TAKEN: `output` INCLUDES thinking, so thinking is NOT added.** §V2 priced `(output + thinking) × out` on the evidence
  `total_tokens == input + output`, which holds under BOTH readings and so decides nothing (the reader's point). The discriminating
  test is per request: if `output` contains thinking, no request can show thinking > output. **Over every agy stream of record
  (332 streams, 36,510 requests; `agy-field-tests.py`, output in `agy-field-tests.out`): thinking > output on 0, thinking = output on 0,
  and the largest thinking/output is 0.998.** A ratio that hugs 1 from below and never reaches it is what inclusion predicts. ⇒ **A
  request's price is `input × in + cache_read × cache + output × out`**, and `thinking` is a part of `output`, printed beside it and
  never priced again. The rates file's own column name (`output_incl_thinking`) already said so.
- **A2.2 · DEFECT 2 TAKEN: `input` excludes cache reads, now shown per request.** The same test in the other field: if `input`
  contained cache reads, no request could show cache_read > input. **34,406 of the 36,510 requests do** (the largest ratio is 124.6).
  A field's definition belongs to the client, not to a cell, so this covers the one row the per-row inference left undecided
  (`l6vgfs02` phase 1, Flash, 9 requests).
- **A2.3 · DEFECT 1 TAKEN: rule 1's check is a REPRODUCTION, not a second method.** The tracked cost columns and the extraction both
  come from `cell_meter.py` and `rates.tsv`, so agreement tests that the same meter, over the same slug, at the same rates, gives the
  same figure. A disagreement detects a rate change, a different slug, or a meter version change, and never an independent error.
  ⇒ **The dollar figure is the tracked row's cost where one exists (it is the figure of record), and the re-run is printed beside it
  per cell with the difference.** Disagreements are counted in the result's header and do NOT stop the run, because a meter fixed after
  a cell ran would otherwise fail a true figure (the reader's case).
- **A2.4 · The Pro upper tier is never selected by these data.** The largest Pro request prompt is 144,717; all 1,399 requests over
  200k are Flash, which has one tier. Only the instrument's selftest exercises the upper-tier arm, and the result file says so.
- **A2.5 · Wall `≥` by timing errs toward the floor.** Marking a cell `≥` because its wall came within one turn timeout of the cap can
  mark a TRUE figure as a floor, never the reverse. The result says so beside the mark. None of this population's cells carries the
  `wait_bound` field (it was built on 2026-09-28, after every cell here ran), so no second method exists for this mark here.

---

## ⚖️ ADDENDUM 3 — A DRY RUN TO SCRATCH FOUND ONE RULE MISSING AND EXPLAINED THE REPRODUCTION'S GAPS. APPENDED; everything above untouched.
**What was run and what was read, exactly.** The instrument ran once to a scratch file outside the repo. Read from it: the two checks'
counts, the reason each unmeasured cell gave, and the reproduction's list of differing cells. **No table cell, median or ratio was
read.** The checks then read: dollars 178 numbers + 16 — + 3 declared + 3 unmeasured = 200; wall 171 + 16 + 3 + 10 = 200.
- **A3.1 · A spec-change cell whose phase 2 ran in a COPY is read from the copy.** The ten wall conditions came from 23 Opus
  spec-change cells whose phase 1 is the reused matrix-1 landing: the cell id resolves (step a) to the landing's root, while phase 2
  ran in a copy of that cell under another root (`cells-specchange-2`), which also holds the INHERITED phase-1 end marker (the
  reuse-by-copy rule in this repository's instructions). **Rule:** where the cell's own root holds phase 1 only, its wall is read from
  the ONE other root, listed in `cellroots-inventory.tsv`, that holds both phases, and only if that root's phase-1 row equals the own
  root's phase-1 row (wall, held time and end kind: the copy check). Zero or several such roots leave it `unmeasured`.
  `claude-wall-raw-allroots.tsv` is the step-d extraction over every CLAUDE (cell, root) pair in the inventory (315 phase rows).
  After the rule, the wall check reads 181 + 16 + 3 + 0 = 200; the six cells still unmeasured sit in DECLARED conditions.
- **A3.2 · Every reproduction difference has one of two causes, both shown at the object.** 46 of 262 cell rows differ by a cent or more,
  all spec-change cells. (a) 23 are block SC cells: their tracked figure is `p1_COST + p2_COST`, which the SC file separates from the
  harness's sandbox probe, exactly as v2 read their `T` (v2's cell map: "per-phase harvest T (probe separated)"); the re-run meters the
  whole slug, probe included, and equals the file's own cumulative `cell_COST_at_end2` to the cent in 22 of 24 SC cells (the other two
  record `end2_scope = phase-2-only`). (b) 23 are the A3.1 cells: the re-run metered the landing's slug, which holds phase 1 only.
  **Neither is an error in a figure of record,** so, by A2.3, the tracked figures stand and the differences are printed.
