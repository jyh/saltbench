# Claude lane (B), ADDENDUM 3 (the release): instruments and readings

## bench (SaltBench lead), 2026-09-16. Cited by `harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md` ADDENDUM 3.

| file | what it is | state |
|---|---|---|
| `harness-delta-9f650a3-bcd2205.tsv` | `git diff --name-status` from HC stage 1's export to the release export `bcd2205`, over `harness/systems-v3` and `tasks/systems-v3`. Its header carries the commit count, the ancestry, the one file that differs from `2822925`, and three blob identities. | taken |
| `runbox_drive.py` → `runbox-drive-bcd2205.out` | ADDENDUM 2's run-box drive (the same script), RE-RUN against the `bcd2205` export: marker, files, withheld-shaped paths, givens' blob ids, and the export's own `served_models_v3.py` over the 45 HC1 cells | taken |
| `withheld_exposure_census.py` | #184's census plus a wrong-box guard and a host-role line (`census-guard.diff`). The original under `evidence/hc1-stage1-instruments-2026-09-16/exposure/` is unchanged. | built; guard driven on the build box: `REFUSE`, rc 1 |
| `census.out` | the census, run on the run box against T-O's staged fence and a current agy fence | ⏳ taken in the helm's window |
| `rates_reread.py` | the page `rates.tsv` cites, compared row by row and figure by figure for the three served models. It prints the page's size and sha256/16. | built; a one-figure mutant reads `NOT-EQUAL`, rc 1 |
| `rates-reread.out` | the tracked reading | ⏳ taken in the window |
| `score-xbox-drive.out` | the Claude scorer run on the BUILD box over cell COPIES harvested from the run box, against a `git archive bcd2205` tree with and without `EXPORTED-FROM.sha` (home paths rewritten to `~`). A plumbing drive: one HC1 cell scored, one never-ended probe cell refused. | taken |
