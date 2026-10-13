# agy ctl/ census, 2026-10-13

The question: did any agy-lane subject WRITE its cell's `ctl/` directory, which the harness trusts? And, beside it: can a
subject READ the briefing-receipt token anywhere but the arm file? Run on the run box over every AGY-shape cell in
`evidence/v3-cost-tables-2026-09-28/cellroots.tsv` (272 cells), reading `~/<root>/<cell>`. Zero spend. Home paths in the
outputs are written `~/`.

| file | what it is |
|---|---|
| `ctl_census.py` | the write census: arm T (every subject tool call in every `transcript_full.jsonl`, main and subagents, plus the streams) and arm M (ctl mtimes against each phase's subject window). `--selftest` plants two writes and one read. One literal in the selftest was changed from a home path for this copy; the selftest passes on the copy. |
| `ctl-census.out` | its output. Line 1 is the verdict: `N=272 CLEAN 165 · CLEAN-READS-CTL 107`. Line 2 lists the ctl files with an mtime inside a subject window. |
| `ctl-refs.out` | every tool call that names ctl/, deduplicated by shape, with the number of cells it occurs in (751 shapes). All are reads. |
| `nonce_order.py`, `nonce-order.out` | the cells whose `ctl/` holds `briefing-nonce` (92), and the 12 whose subject read it or searched ctl/ for the token. Its "emit" index comes from streamed text fragments and is not used. |
| `side_route_all_legacy.py`, `side-route-all-legacy.out` | the 2026-09-16 level-5 side-route census (routes `ctl/briefing-nonce` and `ctl/launch.log`) extended to every legacy-layout cell of record, s3 and b4 included: 92 cells, 27 used a side route after the arm file, 0 before it. |
| `arm_first.py`, `arm-first.out` | for those 12, the step in the same conversation where the subject first named the arm file and first named the token route: ARM-FIRST in all 12. |

Limits: arm T sees the call, not what a called program wrote; arm M sees only a file's last write. The population is the
cells of record in the cost tables' map.
