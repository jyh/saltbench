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
