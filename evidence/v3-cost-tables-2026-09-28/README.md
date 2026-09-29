# v3 cost tables, step a (desk YP): every cell of record resolved to one cells root on the run box

- `cellroots-inventory.tsv`: one row per (cell, root) on the run box whose `<root>/<cell>/ctl` exists, for the 517 distinct ids in
  `CELLMAP-descriptive-tables-v2-2026-09-27.tsv`, with the artifact shape: CLAUDE (a watch.log METER line), AGY (an agy turn loop), or NONE.
  It was listed on the run box on 2026-09-28 and is a snapshot of that day.
- `cellroots-resolved.tsv`: the three cells the rule REFUSED as ambiguous, each settled by a cited record (`l5cp01` by its meter's T
  matching level 5's line 30; `l8cpss01`/`03` by chain D ADDENDUM A's copy note).
- `cellroots.tsv`: `harness/systems-v3/cellroots_v3.py --map … --inventory … --resolved …`, rc 0: SOURCE-ROOT 54 · UNIQUE 453 ·
  DEAD-SUFFIX-EXCLUDED 7 · RECORD 3 · AMBIGUOUS 0 · ABSENT 0. Every resolved cell carries an artifact (none reads NONE).
- The tool's selftest has 13 arms. A pick-the-first-candidate mutant reddens 3 of them.

Nothing here is a registration, and no figure is printed from it. It is the input steps c and d read.

## Step d (Claude wall), raw: `claude-wall-raw.tsv`, produced on the run box by `claude-wall-raw.sh`
For each CLAUDE-shape cell in `cellroots.tsv` (245) and each phase with an end marker, the last `METER … wall N/CAP` line of that phase
in the cell's own `ctl/watch.log`. There are 269 phase readings (245 phase 1, 24 phase 2) and none is missing. **Limits, beside the figure:**
the watcher computes `wall` NET of held time (`t - T0 - hold_total`), so a hold is printed in its own column (1 cell). The last METER line
precedes the end marker by up to one tick (about 60 s), so the figure understates a cell's wall by at most one tick. It is a raw
extraction, not the registered reading.

## Step e (the Opus head-vs-subagent split), raw: `opus-split-raw.tsv`, produced on the run box by `opus-split-raw.sh`
`cell_meter.py` (export `9d873183acab`) `--json` over every CLAUDE-shape cell in `cellroots.tsv`, one row per (cell, config dir). The tracked script differs from the one run in its line 4 only: the meter's path is taken from `CELL_METER` rather than written out, because that path names a private tree. A cell
without `ctl/run-cfg.tsv` (the 09-09/09-10 roots) is metered from the one config dir that holds its slug; none was missing or ambiguous.
The tracked file keeps the 108 Opus-headed cells and drops the config-dir column. **Second method:** for the 54 cells it shares with
`harness/systems-v3-analysis/RESULT-tokens-table-all-roots-2026-09-10.tsv`, T agrees exactly in 54 of 54. Each row's
`T_head + T_exec_opus + T_exec_sonnet + T_wf == T` is asserted as it is written.
Over the 108 cells (computed from the file, not typed): 11.65 % of T is outside the head session; 90 cells carry Opus subagent tokens and
74 carry Sonnet subagent tokens; no cell has no subagent. **Limits, beside the figures:** 30 rows carry `VOID(UNDERSTATED)` (an interrupted
turn whose usage the client never finished writing), so their T and COST are LOWER BOUNDS. COST is modelled at list rates from `rates.tsv`
read on 2026-09-05, not an invoice, and the rates page is owed a re-read before any dollar is registered. Block N (#274, and the Opus column
still running) is not in this population. It is a raw extraction, not the registered reading.

## Step c (agy token categories, per request, and wall), raw: `agy-steps-raw.tsv`, produced on the run box by `agy-steps-raw.py`
For each AGY-shape cell in `cellroots.tsv` (272 cells; 332 phase rows, 60 of them a phase 2) and each phase with `ctl/agy-meter-N.json`:
the meter's turn-level fold (which is T), the per-REQUEST usage the stream carries on each DONE `agent_response` step (deduped by
conversation and step, with whole records recovered from interleaved lines), and the turn loop's wall. **Why per request:** Pro's list
price has a 200k-prompt tier, so a price needs each request's prompt (`input + cache_read`), and a per-cell total cannot give it.
**What it shows (computed from the file):** 264 phase rows are COMPLETE (the step sums equal the meter on all four keys); 2 are
PARTIAL (`s3ft02`, `l7cpbs03`: steps lost in interleaved lines); 6 EXCEED the meter (the step sums are larger than the turn-level fold,
which is a question about the fold, not yet answered); 60 have NO STREAM (all level 8 phase 1: a meter file and no stream in the cell; where the stream lives is not measured here).
No Pro request in any stream has a prompt over 200,000 tokens; the largest observed is 144,717. **Limits, beside the figures:** that
maximum covers observed requests only, so a PARTIAL or NO-STREAM Pro row cannot be put in a tier from this file. The served labels are
the lane's thinking-level ids, not the price page's ids (ADDENDUM 2 of the price plan). It is a raw extraction, not the registered reading.

## Step b (list rates), tracked: `rates-gemini-2026-09-29.tsv`, derived by `rates-reread.py` from the page text
Both price pages were fetched by curl at 2026-09-29T03:28Z and their tags stripped: the Gemini API pricing page (257286 B, sha256/16
`c90575411bc6866b`, which reads "Last updated 2026-09-24 UTC") and the Claude pricing page (820915 B, sha256/16 `36ab2abda5cad48c`). Neither page is
tracked here; the digests say which bytes were read. Every rate in the TSV is matched out of the page text, each inside its own model's
Standard block, and a pattern that matches zero or several times refuses by name. **Three facts the registration must carry:** thinking
tokens are billed as OUTPUT (the page's column header); Pro has a tier on the PROMPT SIZE of each request (200k); Flash's rates are
dated (valid through 2026-12-31, and every cell ran in 2026). The page's context-caching STORAGE price per hour is not in the TSV,
because no agy stream records cache-hours. The lane's served labels are not the page's ids, and the TSV states the mapping it assumes.
**The Claude rows the meter prices with (`claude-opus-5`, `claude-sonnet-5`) AGREE with the Claude page on all five columns**, so
`rates.tsv`'s 2026-09-05 rows stand at the 2026-09-29 read. **Red drives:** a changed Sonnet cache-read rate in a copy of `rates.tsv`
gives DISAGREE and rc 1; Flash's output label removed from the page text refuses (this caught an unscoped first pattern that had read a
later model's row, rc 0); Pro's cache row made single-tier refuses.
