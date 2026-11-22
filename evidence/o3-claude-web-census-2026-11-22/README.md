# The Claude lane's web-tool census (2026-11-22, bench)

**Finding.** No Claude-lane cell transcript on the run box contains a `WebSearch` or `WebFetch` tool call: 0 calls in 3,175
transcripts across 748 cell project directories. The parser can see such calls: on the same run, a Bash control counts 72,597 Bash
calls, and two positive controls (below) count every planted and real call. This is an absence of ATTEMPTS. It does not show that
the cell fence's deny of the CLI's own web tools binds under `--dangerously-skip-permissions`, because no cell ever made an attempt
for it to refuse.

**Why it was run.** Paper v5 (saltbench #459) narrowed its abstract's isolation clause to the Claude lane. The CLI's own web tools
run outside the subprocess sandbox; the rendered fence lists both under `permissions.deny`, and cells launch with
`--dangerously-skip-permissions`. So the outcome was measured instead of assuming the deny binds.

**Method.** `claude_web_census.py`, run on the run box at zero spend. It reads every `*.jsonl` (subagent transcripts included, by
recursive glob) under each Claude config dir's `projects/<slug>`, where `<slug>` contains `cells`. For each `WebSearch`/`WebFetch`
`tool_use` it finds the matching `tool_result` by id and classifies the call: SERVED (a result, no error, no refusal text), REFUSED
(`is_error`, or a permission/deny text), or NO-RESULT. `census.out` is its whole output (sha256/16 `2ce72f1bca3117ca`; script
`c79887d46ad04676`):

```
cell project dirs 748 · transcript files 3175 · control Bash tool_use 72597
WEB CALLS 0 · {}
```

By config-dir family (a separate count over the same glob, same run box, same hour): the per-account dirs hold 565 directories and
2,549 transcripts, and the earlier harness dirs (the `-v3-` family) hold 183 and 626. 565 + 183 = 748 and 2,549 + 626 = 3,175.

**The first run of this census (2026-11-20) had a narrower population, and this run replaces it.** `census-2026-11-20.out`
(sha256/16 `a13b4fbacff700bc`) read 560 directories, 2,522 transcripts, Bash control 56,230, web calls 0. Its glob took the
per-account dirs only and missed the 183 directories of the `-v3-` family (`population-fix.diff` is the one line that changed). The
bench post that cited it on the bus also compared its 2,522 with ADDENDUM 42's 2,513. Those are different file sets (ADDENDUM 42
read top-level and `subagents/` transcripts under every config dir; the 11-20 run read every nested transcript under the
per-account dirs only), so that comparison meant nothing. The per-account family's 5 extra directories (565 against 560) are
block T cells born after the 11-20 run, read by directory birth time: four on 11-20 and one on 11-22, which was still running
when this census read it.

**Positive controls.**
- PLANTED (`control-plant/`): one synthetic transcript holding three web calls, one in each state, plus one Bash call
  (committed as `planted-transcript.jsonl.txt` because this repo ignores `*.jsonl`; copy it to a `.jsonl` name to re-run). The same
  script, run with `HOME` pointed at a directory holding only that transcript under a `cells` slug, reads SERVED 1 · REFUSED 1 ·
  NO-RESULT 1, Bash 1 (`plant.out`). So each of the three classes is reachable.
- REAL (not published; the transcripts are a project seat's own sessions, not cell material): two session transcripts from outside
  the cells that are known to use web tools, copied under a `cells` slug in a scratch `HOME`. The script reads
  `WEB CALLS 10 · {('WebSearch', 'SERVED'): 6, ('WebFetch', 'SERVED'): 4}`, Bash 126. So the parser matches the record shape the
  CLI writes, not only the shape this README planted.
- A negative-population run on the run box (the same glob, slugs NOT containing `cells`: 244 directories, 278 transcripts) also
  reads 0 web calls and Bash 3. It holds no positive, so it is not a control. It is listed so nobody reads it as one.

**Limits.**
- Transcripts on the run box only. A cell whose transcript was deleted or never written is invisible here. The census does not
  join transcripts to cells of record. Its population is every cell transcript present, which includes probes, smoke cells and
  cells outside the matrix.
- The REFUSED class is a regex over the result's first 300 characters (`permission|denied|not allowed|blocked|disallowed`). With 0
  calls nothing was classified, so the regex's reach on a real refusal is unmeasured. Only the planted refusal exercises it.
- It does not read the subjects' Bash commands for network use (curl, cargo fetching a crate, and so on). That is the subprocess
  sandbox's question, and §fence of the paper covers it.
- Whether the deny binds when a subject does call a web tool under `--dangerously-skip-permissions` is UNMEASURED. A probe that
  drives that call and reads the refusal is owed for the next Claude-lane export (bench's queue).
