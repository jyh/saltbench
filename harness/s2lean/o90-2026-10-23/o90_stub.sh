#!/bin/bash
# o90_stub.sh — the O90 amendment's run-shaped-dry client (desk AEY, 2026-10-23). It is dry_exec_stub_s2.sh with ONE addition:
# if the file stub-bodies.json sits beside this script, its keys are written into the task file's marked sections INSTEAD of
# the base stub's shapes (so a dry stage B can PASS the real kernel check with a recorded real body), and if stub-EXPLAIN.md
# sits beside it, it is copied to repo/EXPLAIN.md. The episode launches the client under `env -i`, so a FILE beside the
# script is the only channel; o90_selftest.sh writes and removes those files around each episode.
# dry_exec_stub_s2.sh — stands in for `claude` in the S2 run-shaped dry (repair D13/M5): every line of episode_s2.sh AFTER
# the launch executes with NO model call, AND the extract → assemble → check seam is exercised, because the stub writes a
# gold-SHAPED body into $BENCH_EP/repo/task.lean by stage before it exits:
#   A: generated_spec_body := `True`                       (compiles; check A passes ⇒ the dry's A.bodies.json is written)
#   B: spec_isomorphism_proof := a sorry-free WRONG attempt (the check RUNS and fails; the dry needs a verdict, not a pass)
#   C: implementation := `default`, correctness_proof := a sorry-free wrong attempt (same)
# Then it writes a one-call session jsonl where episode_s2.sh looks for it (a Bash + an Edit tool_use, both inside the
# episode) and prints a result.json with subtype success and a minimal usage block (the S1 stub's shape).
# Never used in a real episode: episode_s2.sh takes CLAUDE_BIN from PATH unless CLAUDE_BIN_STUB=1, the driver unsets both
# unless DRY_RUN=1, and a stub-driven run lands as DRYEXEC(...) in dryexec.log with its bodies under state/s2-dry.
[ "${1:-}" = "--version" ] && { echo "2.1.251 (Claude Code) [dry-exec stub s2]"; exit 0; }
sid=""; prev=""
for a in "$@"; do [ "$prev" = "--session-id" ] && sid="$a"; prev="$a"; done
EP="${BENCH_EP:?BENCH_EP must be exported by episode_s2.sh}"
HERE="$(cd "$(dirname "$0")" && pwd)"
if [ -f "$HERE/stub-bodies.json" ]; then
python3 - "${BENCH_EP:?}/repo/task.lean" "$HERE/stub-bodies.json" <<'PY'
import re, sys, json
p = sys.argv[1]; s = open(p, encoding="utf-8").read(); b = json.load(open(sys.argv[2]))
for name, body in b.items():
    if name.startswith("_"): continue
    rx = re.compile(r"(--\s*start_def\s+%s\s*\n)(.*?)(--\s*end_def\s+%s)" % (name, name), re.DOTALL)
    s, n = rx.subn(lambda m: m.group(1) + body + "\n" + m.group(3), s, count=1)
    if n != 1: raise SystemExit("o90_stub: section %s not found" % name)
open(p, "w", encoding="utf-8").write(s)
PY
[ -f "$HERE/stub-EXPLAIN.md" ] && cp "$HERE/stub-EXPLAIN.md" "$BENCH_EP/repo/EXPLAIN.md"
fi
if [ ! -f "$HERE/stub-bodies.json" ]; then
python3 - "$EP/repo/task.lean" <<'PY'
import re, sys
p = sys.argv[1]; s = open(p, encoding="utf-8").read()
def put(name, body):
    global s
    rx = re.compile(r"(--\s*start_def\s+%s\s*\n)(.*?)(--\s*end_def\s+%s)" % (name, name), re.DOTALL)
    s, n = rx.subn(lambda m: m.group(1) + body + "\n" + m.group(3), s, count=1)
    return n
if "start_def spec_isomorphism_proof" in s:
    put("spec_isomorphism_proof", "by\n  intro impl\n  constructor <;> intro h <;> exact h")
elif "start_def correctness_proof" in s:
    put("implementation", "default")
    put("correctness_proof", "by\n  unfold problem_spec implementation\n  simp")
else:
    put("generated_spec_body", "True")
open(p, "w", encoding="utf-8").write(s)
PY
fi
d="$CLAUDE_CONFIG_DIR/projects/-stub"; mkdir -p "$d"
printf '{"type":"assistant","isSidechain":false,"version":"stub","timestamp":"2026-01-01T00:00:00Z","requestId":"req_stub","message":{"id":"msg_stub1","model":"claude-sonnet-5","usage":{"input_tokens":10,"cache_creation_input_tokens":100,"cache_read_input_tokens":0,"output_tokens":5,"service_tier":"standard"},"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"ls"}}]}}\n' > "$d/$sid.jsonl"
printf '{"type":"user","message":{"content":[{"type":"tool_result","tool_use_id":"t1","content":"CLAUDE.md"}]}}\n' >> "$d/$sid.jsonl"
printf '{"type":"assistant","isSidechain":false,"version":"stub","timestamp":"2026-01-01T00:00:01Z","requestId":"req_stub2","message":{"id":"msg_stub2","model":"claude-sonnet-5","usage":{"input_tokens":10,"cache_creation_input_tokens":0,"cache_read_input_tokens":100,"output_tokens":5,"service_tier":"standard"},"content":[{"type":"tool_use","id":"t2","name":"Edit","input":{"file_path":"%s/repo/task.lean","old_string":"sorry","new_string":"True"}}]}}\n' "$EP" >> "$d/$sid.jsonl"
printf '{"type":"user","message":{"content":[{"type":"tool_result","tool_use_id":"t2","content":"The file has been updated."}]}}\n' >> "$d/$sid.jsonl"
printf '{"type":"result","subtype":"success","is_error":false,"num_turns":2,"result":"OK","session_id":"%s","usage":{"input_tokens":20,"cache_creation_input_tokens":100,"cache_read_input_tokens":100,"output_tokens":10},"modelUsage":{"claude-sonnet-5":{"inputTokens":20,"cacheCreationInputTokens":100,"cacheReadInputTokens":100,"outputTokens":10}}}\n' "$sid"
exit 0
