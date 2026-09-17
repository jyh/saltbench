# Level 8 ADDENDUM 4: §M0 row 4's export is named

## bench (SaltBench lead), 2026-09-17, 01:3x PDT. Cited by `harness/systems-v3/AMENDMENT-gemini-level8-2026-09-16.md` ADDENDUM 4.

## 1 · `export_delta.sh` → `export-delta-163df20.out`
The script ran read-only against the harness repository with base `2419dcf` and export `163df20`. It REFUSES a sha that does not resolve; that
was driven with `deadbeef` and exited 2.
**Reading:**
- **§1 ancestry.** All six required commits are in the export, each `rc=0`: the base, §M3's fault gate, A2.1, A3.3, R1–R3 with ROOT, and
  R4–R6 with FIELDS.
- **§1b control.** The export is NOT in the base (`rc=1`), so the ancestry check can go red.
- **§2 the delta.** 39 commits, 26 files, with numstat.
- **§3 grouping by path pattern.** The patterns are printed in the output. The counts are 9 agy-prefixed · 7 Claude-lane-prefixed · 6 shared or
  other · 4 withheld control.
  - ⚠️ **This is a reading aid, not a call graph.** A first draft grouped the files by which entry points NAME each basename. It was withdrawn
    before commit, because a generic basename (`solution.rs`) and a mention in a comment both count as a call.
- **§4 control.** 0 changed files lie under `withheld/mutants/`, and the same count over `withheld/` finds the 4 fixture files.

## 2 · `supervisor_gate_drive.sh` → `supervisor-gate-163df20.out`
The script takes `git archive 163df20` of `harness/systems-v3`. It runs the supervisor's `--selftest`, then extracts `manifest_rows` through
`phases_verdict` VERBATIM and drives them over the hand's level-8 template manifests (not tracked here). Only template basenames and
sha256/16 are printed. No ssh and no model call. It REFUSES a directory with no `l8u-*.tsv`; that was driven on an empty directory and exited 2.
**Reading:**
- **§1 selftest.** 88 of 88, rc 0, 0 FAIL lines. The supervisor's sha256/16 is `7b03c644726146e4`.
- **§2 the templates as drafted.** All 11 files (21 condition rows) REFUSE at unset and at `1` as [A2.1], and at `1,2` as [R6]. Every row
  carries an extra.
- **§3 control.** The same 11 files, with only the extra column emptied, read **OK** at `1,2`. The output checks that fields 1–5 are unchanged
  in every file.
