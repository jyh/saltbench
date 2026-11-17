# O37: the salt-diet gate's selftest could not make its temp dir, in 6 Claude-lane cells of record (2026-11-15)

**Finding.** In six Claude-lane salt-diet cells of the complete matrix, a command's output shows the salt-diet arm's own gate failing at
its selftest: `mkdtemp failed on /tmp/claude-<uid>/gatest.XXXX: Operation not permitted`, then `gate: selftest in`, then `fatal: could not
create work tree dir`. Claude Code's sandbox gives the subject's shell `TMPDIR=/tmp/claude-<uid>`, where it may not make a directory with
`mktemp -d`. No plain cell can show this: the plain arm has no gate.

**Method.** `census_gatest.py`, run on the run box at zero spend over every Claude-lane session transcript of a cell (2,513, subagent
transcripts included), searches TOOL RESULTS only (what a command printed back), never the model's own text or the instructions it read,
for `mkdtemp failed on <path>/gatest.<x>` (signature G). `gatest-hits.tsv` is its 11 hits; in all 11, `gate: selftest` follows within
200 characters; its printed line, `census_gatest.out`, gives the 2,513 (a re-run produced a byte-identical hit file). `projects.tsv` lists
every cell transcript directory with its count of TOP-LEVEL transcripts only (1,123; subagent transcripts are not counted there; home prefix
and account removed); it serves the join, which needs only whether a directory has a transcript.
`claude_join.py` joins G to the matrix's Claude DONE rows (`harness/systems-v3/CELLMAP-descriptive-tables-v2-2026-09-27.tsv`, arm as
registered) by the cell id as a token of the directory name → `claude-join.tsv` (one row per condition-row) and `claude-join.out`:

```
  model            arm         GATE-HIT   clean   no transcript
  claude-opus-5    plain           0        65         0
  claude-opus-5    salt-diet       2        64         0
  claude-sonnet-5  plain           0        68         0
  claude-sonnet-5  salt-diet       5        55         0
```
**Salt-diet 7 of 126 condition-rows, 6 distinct cells** (d6b53ee4 is both Opus LRU none and its spec-change, whose phase 1 is the reused
matrix-1 landing, as the tables' header states); plain 0 of 133. `result_files_map.py` → `result-files-map.tsv`: the RESULT files that name
each hit cell, plus the block result whose root holds it.

**Controls** (`controls.out`): no hits → every GATE-HIT 0. One plant (a plain cell, clbbcp01) → Sonnet plain 0 → 1, nothing else moves.

**Two needles that were wrong first, and why they are not used** (`needles-not-used/`: the script, `census_wide.py`, and its rows,
`census-wide-transcripts.tsv`, one per transcript with either signature: 2,383 rows, all with A, 19 with the wide C). (1) The agy census's signature (`/tmp/claude` within 200 characters of
"not permitted") fires in 2,383 of 2,513 Claude transcripts, because every Claude-lane Bash call ends with a harmless `zsh: operation not
permitted: /tmp/claude-<uid>/cwd-XXXX` from the shell's teardown, in both arms, as the cells' own instructions say. (2) A wider
"any mkdtemp or can't-create-temp failure whose line mentions /tmp/claude" (19 transcripts) also caught zsh's here-document failure
followed by that teardown line, and a cell's instruction text being read back. G names the gate's own directory and is followed by the
gate's own selftest line, in every hit.

**Limits.** NOT read: whether each subject then ran its gate another way, and whether any cell's outcome or cost moved. A hit is a
printed failure. The join is by cell id (no root in the cell map for these rows) and over DONE rows only. Transcripts on the run box only.
**Five more G hits are outside the DONE rows:** clbczs01 and clbcps01 are cells of two of the matrix's three DECLARED conditions (Sonnet
LZW and Paxos, salt-diet, spec-change: unreached at the cap), whose cells the cell map lists as DECLARED; 1062c631, ae1693f1 and p2b002
are in no row of the cell map. Whether the gate's failure bears on a DECLARED condition's being unreached is NOT read here.
