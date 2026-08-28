#!/bin/bash
# dry_exec_stub.sh — stands in for `claude` in a --dry-exec run so every line of episode.sh AFTER the launch executes
# on the Studio with NO model call: writes a minimal result.json to stdout and a one-call session jsonl where
# episode.sh will look for it. Never used in a real episode (episode.sh takes CLAUDE_BIN from PATH unless CLAUDE_BIN_STUB=1).
[ "${1:-}" = "--version" ] && { echo "2.1.251 (Claude Code) [dry-exec stub]"; exit 0; }
sid=""; prev=""
for a in "$@"; do [ "$prev" = "--session-id" ] && sid="$a"; prev="$a"; done
d="$CLAUDE_CONFIG_DIR/projects/-stub"; mkdir -p "$d"
printf '{"type":"assistant","isSidechain":false,"version":"stub","timestamp":"2026-01-01T00:00:00Z","requestId":"req_stub","message":{"id":"msg_stub1","model":"claude-sonnet-5","usage":{"input_tokens":10,"cache_creation_input_tokens":100,"cache_read_input_tokens":0,"output_tokens":5,"service_tier":"standard"},"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"ls"}}]}}\n' > "$d/$sid.jsonl"
printf '{"type":"user","message":{"content":[{"type":"tool_result","tool_use_id":"t1","content":"CLAUDE.md"}]}}\n' >> "$d/$sid.jsonl"
printf '{"type":"result","subtype":"success","is_error":false,"num_turns":1,"result":"OK","session_id":"%s","usage":{"input_tokens":10,"cache_creation_input_tokens":100,"cache_read_input_tokens":0,"output_tokens":5},"modelUsage":{"claude-sonnet-5":{"inputTokens":10,"cacheCreationInputTokens":100,"cacheReadInputTokens":0,"outputTokens":5}}}\n' "$sid"
exit 0
