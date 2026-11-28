# Blocks NCA and WCA — result evidence (bench, 2026-11-28)
The four RESULT files (`harness/systems-v3/RESULT-gemini-block{NCA,WCA}-{flash,argon}-2026-11-28.md`) quote figure lines printed from this
directory. Each input, how it is made, and what it does not see:

- **`manifests/`** — byte copies of the hand's four chain manifests (`cmp` EQUAL to the hand's at each re-fetch). They ARE the population
  (96 rows): a cell not yet scored reads UNSCORED, never absent.
- **`cell_facts.json`** — `nca_facts.py`, run on the run box by `nca_cells_gen.py --fetch HOST`, read-only, over the 96 rows: each row's
  standing attempt (a 503 re-queue is `<root>-a<k>`), its cell's own `ctl/` (meters, turn loops, end markers, launch lines, copy record),
  the phase-1 record the wave set aside (`<root>/_aside/<id>/phase1/ctl/`, or the cell's own `ctl/` when no phase 2 ran), the §A9.2 gate
  lines, a fresh cell's G baseline, and the P-PERSIST probe: the registered reader's word (`ctl/agy-probes-2.tsv`) beside whether the
  subject's validated ack token follows the probe in its own brain transcript or stream (a hand read, 2026-11-28). A value it cannot read is UNREAD, never blank or zero.
- **Score receipts** — the hand's (`score_wave_v3.sh`, one per cell), in its run directory on the lead's box, NOT in this repository (they
  name paths in a local-only tree). Each row's `score_receipt` column names the receipt it was read from; two receipts for one root are
  admitted only when they agree on every scored field (both are cited), and two that disagree refuse. WCA's sit in `wca-*-harvest*` dirs.
- **G receipts** — the hand's harvest ROW lines (`gbase.sh`'s own line with its rc), cross-checked against the box's G log per fresh cell;
  a disagreement refuses.
- **ctl census** — `ctl_census_join_input.tsv` (`--join-input`: a copy read in its standing root AND its source's family, a fresh cell in
  its standing root) → main's `evidence/o37-agy-ctl-read-census-2026-11-25/ctl_census.py` on the run box (`--fetch-ctl`: its `--selftest`
  first, then `--join`) → `ctl_census_join.tsv` + `ctl_census_hits.tsv` → `ctl_census.tsv` (`--derive-ctl`: manifest roots, reads =
  `ctl_named`, the paths its CTL hits name; an ambiguous id refuses). Its LIMIT: NONE-NAMED is a lower bound on contact with `ctl/`.
- **web census** — `web_census.tsv` + `web_transcripts.tsv` (`--fetch-web`): main's `evidence/o37-agy-web-served-2026-11-20/web_brain_census.py`,
  unchanged, run on the run box over a farm of symlinks to the standing roots. A cell with no brain transcript is UNMEASURED, never CLEAN.
  A copy's SOURCE state is the 11-20 census's `join.tsv`, keyed by (root, id).
- **`cells.tsv`** — the per-cell table of record, `nca_result_gen.py --write`; `--check` asserts it equals the table printed now, and that
  each RESULT file and this README carry every figure line of their own.
- **`nca_gen_selftest.sh`** — every refusal and every reading rule above driven on fixtures (the real receipt root is read, never written);
  each arm added since 2026-11-28 was shown to fail on a mutant of the rule it guards.

The population-wide lines (`nca_cells_gen.py --summary`, the lines no block owns):
```
rows 96 · scored 92 · receipts 96 · facts 96
attempts: standing at attempt 1 94 · at attempt 2+ 2 [cells-nca-linearscan-argon-plain-r2=a2 cells-nca-linearscan-argon-salt-r2=a2] · discarded attempts 2 · root not found 0
ctl census: CTL-READ 1 [cells-na-aes-flash-salt-ncacp1] · read 0 95 · UNREAD 0
phase-2 gate (§A9.2, its own lines): FIRED 95 · NOT-FIRED 1 [cells-nca-liveness-argon-salt-r1] · no line 0 · no cell 0 · UNREAD 0
p2_model UNREAD=2 gemini-3.8-flash-high=48 gemini-4-argon-high=46
p2_client16 62f2102784bb74b7=94 UNREAD=2
p2_export 88b63df9c5be=96
hook16 FRESH=38 a6e064e307a8651d=58
done_reason LANDED=94 UNREAD=2
```
