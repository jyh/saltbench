# The Claude lane's web-tool census (2026-11-22, bench)

**Finding.** No Claude-lane cell transcript on the run box contains a `WebSearch` or `WebFetch` tool call: 0 calls in 3,175
transcripts across 748 cell project directories. The reason is upstream of any refusal. Every recorded cell launch left both
web tools off the subject's tool surface: 786 of 786 recorded launches pass a `--tools` allowlist without them and strike
both again in `--disallowedTools`. 728 of the 748 transcript directories join to such a launch by cell id. The client refused
the subjects' calls to a tool struck the same way (SendMessage, 3 of 3, "No such tool available"). What this does NOT show is
the client refusing a web call, because no subject ever made one.

**Why it was run.** Paper v5 (saltbench #459) narrowed its abstract's isolation clause to the Claude lane. The CLI's own web
tools run outside the subprocess sandbox; the rendered fence lists both under `permissions.deny`, and cells launch with
`--dangerously-skip-permissions`. So the outcome was measured instead of assuming the deny binds.

## 1 · The web-call census (`claude_web_census.py` → `census.out`)
Run on the run box at zero spend. It reads every `*.jsonl` (subagent transcripts included, by recursive glob) under each
Claude config dir's `projects/<slug>`, where `<slug>` contains `cells`. For each `WebSearch`/`WebFetch` `tool_use` it finds
the matching `tool_result` by id and classifies the call: SERVED (a result, no error, no refusal text), REFUSED (`is_error`,
or a permission/deny text), or NO-RESULT. It also prints distinct (slug, file) pairs, every block type, and every tool name
called. `census.out` (sha256/16 `0c65feaee8ff0106`; script `5b03c4ab1249a4df`):

```
cell project dirs 748 · transcript files 3175 · control Bash tool_use 72616
WEB CALLS 0 · {}
distinct (slug, file) pairs 3175
block types (lines holding tool_use or tool_result): {'tool_use': 127939, 'tool_result': 127919, 'thinking': 41470, 'text': 21764}
tool_use names: {'Bash': 72616, 'Edit': 23613, 'Read': 20285, 'Write': 7841, 'Agent': 1811, 'Grep': 1252, 'Glob': 364, 'TaskStop': 149, 'SendMessage': 3, 'EndConversation': 2, 'Grash': 1, 'Grag': 1, 'Str_replace_editor': 1}
```
- Distinct (slug, file) pairs equal the file count, so no transcript is counted twice by a config dir holding a copy.
- No block type other than `tool_use`, `tool_result`, `thinking` and `text` occurs, so no `server_tool_use` (or other) web
  record is hiding under another type. The web names are absent from the full list of names called.
- By config-dir family (same glob, same hour): the per-account dirs hold 565 directories and 2,549 transcripts, and the
  earlier harness dirs (the `-v3-` family) hold 183 and 626.
- `census-v1.out` (`2ce72f1bca3117ca`) is the first 11-22 run, by the script before the three extra lines were added: the
  same 748 · 3,175 · 0, with a Bash control of 72,597. The 19 more Bash calls in `census.out` are from block T's cell
  `clbvrs01`, which was running during both runs.

## 2 · The tool surface as launched (`argv_census.py` → `argv.out`, `join_census.py` → `join.out`, `noargv_census.py` → `noargv.out`)
Every Claude-lane launch writes its full argument vector to the cell's `ctl/launch.log` as an `ARGV <id> phase <n>:` line.
- `argv.out`: 1,939 launch logs, 786 ARGV lines, and all 786 are `WEB-NOT-OFFERED · struck=WebSearch+WebFetch · fence ·
  skip-perms`. The `--tools` list is `Bash,Read,Edit,Write,MultiEdit,NotebookEdit,Glob,Grep,Agent,Task,TodoWrite,TaskStop`.
  Client: 758 launches on 2.1.259, 27 on 2.1.280, and 1 by the bare name `claude`.
- `noargv.out`: the 1,223 logs without an ARGV line are the Gemini lane (908 launched + 93 not), Claude cells never launched
  (46), and logs with no client file (154 launched + 18 not launched + 4 dry stubs). Of the 154, 153 are `l8`/`l8zf` Gemini
  families and 1 is a Claude pilot cell halted on 2026-09-05 and archived (`e0b7e947`), launched before launches wrote an
  ARGV line. Its launch surface is not recorded.
- `join.out`: of the 748 transcript directories, 728 join by cell id to an ARGV line, all WEB-NOT-OFFERED. 20 have no ARGV
  line, all in probe or test families (x86net 8, the 09-05 probe cells 5, sandbox probes 3, `cells` 2, `pcells` 1,
  agentstest 1). They read 0 web calls in section 1 like the rest.

## 3 · What the client did with calls to tools not on the surface (`offsurface.py` → `offsurface.out`)
Eight calls in the population name a tool outside the `--tools` list:
- `SendMessage` ×3 (struck in `--disallowedTools` like the web tools): all `is_error`, "No such tool available: SendMessage.
  SendMessage is disabled for this session, in subagents as well as here."
- Made-up names (`Grag`, `Grash`, `Str_replace_editor`): all `is_error`, "No such tool available".
- `EndConversation` ×2 (neither offered nor struck): ANSWERED with the tool's own guidance text, not an error. So the
  `--tools` list does not remove every built-in tool, and the surface is not exactly that list. Whether the web tools
  behave like `SendMessage` or like `EndConversation` is not shown by these records. They were struck, as `SendMessage` was.

## Positive controls for section 1
- PLANTED (`control-plant/`): one synthetic transcript holding three web calls, one in each state, plus one Bash call
  (committed as `planted-transcript.jsonl.txt` because this repo ignores `*.jsonl`; copy it to a `.jsonl` name to re-run).
  The script, run with `HOME` pointed at a directory holding only that transcript under a `cells` slug, reads SERVED 1 ·
  REFUSED 1 · NO-RESULT 1, Bash 1, and its name list holds both web names (`plant.out`, by the committed script).
- REAL (not published; the transcripts are a project seat's own sessions, not cell material): two session transcripts from
  outside the cells that are known to use web tools, copied under a `cells` slug in a scratch `HOME`. The script reads
  `WEB CALLS 10 · {('WebSearch', 'SERVED'): 6, ('WebFetch', 'SERVED'): 4}`, Bash 126.
- A negative-population run on the run box (slugs NOT containing `cells`: 244 directories, 278 transcripts) also reads 0 web
  calls and Bash 3. It holds no positive, so it is not a control. It is listed so nobody reads it as one.

## The first run of this census (2026-11-20), which this replaces
`census-2026-11-20.out` (`a13b4fbacff700bc`) read 560 directories, 2,522 transcripts, Bash control 56,230, web calls 0. Its
glob took the per-account config dirs only and missed the 183 directories of the `-v3-` family (`population-fix.diff` is the
code line that changed). The bench post that cited it on the bus also compared its 2,522 with ADDENDUM 42's 2,513. Those are
different file sets (ADDENDUM 42 read top-level and `subagents/` transcripts under every config dir; the 11-20 run read every
nested transcript under the per-account dirs only), so that comparison meant nothing. The per-account family's 5 extra
directories (565 against 560) are block T cells born after the 11-20 run, read by directory birth time: four on 11-20 and one
on 11-22, which was still running when this census read it.

## Limits
- Transcripts and launch logs on the run box only. A cell whose transcript or log was deleted, or never written, is
  invisible here. The population is every cell transcript present (probes, smoke cells and cells outside the matrix
  included), joined to launches by cell id, not to the cells of record.
- The REFUSED class is a regex over the result's first 300 characters (`permission|denied|not allowed|blocked|disallowed`).
  With 0 web calls nothing was classified; only the planted refusal exercises it.
- Section 1 does not read the subjects' Bash commands for network use (curl, cargo fetching a crate, and so on). That is the
  subprocess sandbox's question, and §fence of the paper covers it.
- Whether a web call made under this launch line would be refused is UNMEASURED. The `SendMessage` refusals are the same
  flag and the same client, not the same tool, and `EndConversation` shows the surface is not exactly the `--tools` list. A
  probe that reads the pinned client's own tool list under the cell launch line is owed for the next Claude-lane export.
