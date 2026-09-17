# Claude lane (B), ADDENDUM 2: two read-only drives on the run box

## bench (SaltBench lead), 2026-09-16, 20:2x PDT. Cited by `harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md` ADDENDUM 2.

Both scripts ran on the run box, fed to `python3 -` over ssh. Nothing was written there. Each takes the box's home
directory, or the export directory, as its only argument. **Each cell's config directory is read from that cell's own
`ctl/run-cfg.tsv`, never passed in.** Both scripts **REFUSE (exit 1) when they find no HC1 cell**. A census of a home
directory names no host, so on the wrong machine it would otherwise print an empty table that looks clean. The refusal
was driven on the build box, which holds no HC1 cells: both scripts printed `REFUSE` and exited 1.
⚠️ **Taken while a level-6 agy cell was live on the same box.** These are reads only: no file moved, and no process was
signalled.

---

## 1 · `hc1_subject_model_census.py` → `hc1-subject-model-census.out`

For every HC1 cell, the script reads every Agent/Task spawn in the HEAD's own transcripts. For each spawn it records the
`model` parameter the SUBJECT passed. An absent `model` means the agent definition decides. The arm comes from
`ctl/arm`, and the task is the first field of `ctl/task`.
- **Population:** 45 cells, 15 per arm. None lacks a transcript.
- **Excluded:** two directories set aside beside `hc1cp01` (`.FAILED-BUILD`, `.NO-RUN`). They are printed as `ASIDE`
  rows and counted on their own line. Only the id and the suffix's upper-case class are printed.
- **Reading** (the `# ARM` and `# TOTAL` lines):
  - 11 of 45 cells passed an explicit `model` on at least one spawn.
  - 7 of 45 asked for `opus`: salt-diet 5/15 · plain 2/15 · placebo 0/15.
- **Second method, agreeing:** the builder's own census ran over a pulled copy and all `.jsonl` files recursively. It
  read the same 11 and 7, and the same spawn totals: 11 spawns asked for `opus` and 10 for `sonnet`. Here those are the
  sums of the per-cell `models_asked` column.
- **The detector can discriminate:** placebo has 3 cells with an explicit model and 0 that asked for `opus`.

## 2 · `runbox_drive.py` → `runbox_drive.out`

**The release export** (`EXPORTED-FROM.sha` reads `2822925e3f5b…`):
- **Files:** 363, which is 362 plus the marker.
- **Withheld-shaped content:** no directory is named `withheld` or `mutants`. Exactly one path contains either word:
  `harness/systems-v3/check_withheld_leak_v3.py`, the leak INSTRUMENT, not a withheld byte.
- No refusal file.

**The five brownfield givens:** each is the git blob id of `tasks/systems-v3/<P>/brownfield/solution.rs`, computed from
the export's bytes.

**Then the EXPORT'S OWN `served_models_v3.py check-cell` over all 45 HC1 cells, under both conditions:**
- 45 of 45 read `clean` (set `clean`, rc 0) as Opus.
- 45 of 45 read `SUBSTITUTED` (set `SUBSTITUTED`, rc 1) as Sonnet.

⚠️ This script skips the two aside directories without printing them. Census 1 is where they are declared.
