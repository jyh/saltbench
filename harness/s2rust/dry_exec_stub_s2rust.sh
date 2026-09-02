#!/bin/bash
# dry_exec_stub_s2rust.sh — stands in for `claude` in the S2-Rust run-shaped dry. ZERO MODEL TOKENS.
#
# Every line of episode_s2rust.sh AFTER the launch executes for real, and the extract → assemble → screen →
# lynette → referee seam is exercised end to end, because the stub writes a gold-SHAPED proof body into
# $BENCH_EP/repo/task.rs before it exits.
#
# ⛔ THE STUB DELIBERATELY WRITES A WRONG-BUT-HONEST PROOF, NOT A PASSING ONE. The dry needs a VERDICT, not a
# green light: a stub that made the referee pass would exercise only the happy path and would hide exactly
# the failures the driver exists to classify. `assert(false)` would be worse still — it trips the screen and
# the episode would never reach the referee at all, so the seam under test would go unmeasured.
# ⇒ THE DRY'S JOB IS TO PROVE THE MACHINERY RUNS, AND A DRY THAT ONLY EVER PASSES PROVES HALF OF IT.
#
# ⛔ It also honours `STUB_MODE`, so the dry can drive the OTHER outcomes on demand without a model:
#     proof   (default) a sorry-free wrong proof            -> expect VERIFY_FAIL
#     clean   the body left exactly as shipped (empty)       -> expect VERIFY_FAIL (nothing proved)
#     screen  an `assume(false)` in the body                 -> expect SCREEN
#     helper  a valid helper `proof fn` plus a wrong proof    -> expect VERIFY_FAIL, HELPERS_SHAPE clean
#     badhelp a `spec fn` in the helpers region              -> REGISTERED: HELPERS_SHAPE. MEASURED: SCREEN.
#             ⛔ THE PREDICTION WAS WRONG AND THE INSTRUMENT WAS RIGHT — kept here rather than edited out.
#             `screen_verus.violations` ALREADY applies the `_HELPER_BAD` table to the helpers key, so the
#             screen fires first and the ordered classifier never reaches the HELPERS_SHAPE layer. Measured
#             both ways on the same artifact: with the screen -> SCREEN
#             (`helpers: spec fn (helpers must be proof fn)@1`); with `--no-screen` -> HELPERS_SHAPE
#             (`helpers: item 1 is not a proof fn@1`). That is EXACTLY the design — HELPERS_SHAPE exists to
#             hold when the screen is disabled — so the dry confirmed the layering by failing its own guess.
#     damage  the `end_def proof` marker deleted             -> expect SCAFFOLD_DAMAGED
# Never used in a real episode: episode_s2rust.sh takes CLAUDE_BIN from PATH unless CLAUDE_BIN_STUB=1, and a
# stub-driven run lands as DRYEXEC(...) in dryexec.log.
[ "${1:-}" = "--version" ] && { echo "2.1.251 (Claude Code) [dry-exec stub s2rust]"; exit 0; }
sid=""; prev=""
for a in "$@"; do [ "$prev" = "--session-id" ] && sid="$a"; prev="$a"; done
EP="${BENCH_EP:?BENCH_EP must be exported by episode_s2rust.sh}"
# ⛔ THE MODE ARRIVES AS A FILE, NOT AS AN ENVIRONMENT VARIABLE, AND THAT IS THE DRIVER BEING RIGHT.
# episode_s2rust.sh launches the agent under `env -i` with an explicit allowlist — the hermeticity the whole
# campaign rests on — so a `STUB_MODE=…` on the driver's command line NEVER reaches here. My first cut used
# exactly that, and all six modes silently ran as the default: six episodes, six identical VERIFY_FAILs,
# each one looking like a real measurement.
#   ⇒ 🔑 A TEST RIG THAT STEERS THE SUBJECT THROUGH A CHANNEL THE SUBJECT FENCES OFF MEASURES THE DEFAULT
#     PATH SIX TIMES AND CALLS IT SIX CASES. The fence was not the bug; believing my knob was connected was.
# CLAUDE_CONFIG_DIR is on the allowlist because the agent genuinely needs it, so the mode travels beside the
# settings the agent reads — and it is a DRY-ONLY path: a real episode has no such file and takes the default.
MODE="${STUB_MODE:-}"
[ -z "$MODE" ] && [ -r "${CLAUDE_CONFIG_DIR:-}/stub_mode" ] && MODE=$(tr -d " \n" < "$CLAUDE_CONFIG_DIR/stub_mode")
MODE="${MODE:-proof}"
MODE="$MODE" python3 - "$EP/repo/task.rs" <<'PY'
import os, re, sys
p = sys.argv[1]; s = open(p, encoding="utf-8").read(); mode = os.environ.get("MODE", "proof")

def put(name, body):
    global s
    rx = re.compile(r"(//\s*start_def\s+%s\s*\n)(.*?)(//\s*end_def\s+%s)" % (name, name), re.DOTALL)
    s, n = rx.subn(lambda m: m.group(1) + body + "\n" + m.group(3), s, count=1)
    if n == 0:
        raise SystemExit("dry stub: no '%s' region in the view — the stub and the builder disagree" % name)

if mode == "clean":
    pass
elif mode == "screen":
    put("proof", "    assume(false);")
elif mode == "badhelp":
    put("proof", "    // a wrong but honest attempt\n    assert(true);")
    put("helpers", "spec fn stub_bad_helper(x: int) -> bool { true }")
elif mode == "helper":
    put("proof", "    // a wrong but honest attempt\n    assert(true);")
    put("helpers", "proof fn stub_helper(x: int)\n    ensures x + 0 == x\n{\n}")
elif mode == "damage":
    put("proof", "    assert(true);")
    s = s.replace("// end_def proof", "", 1)
else:                                   # proof (default)
    put("proof", "    // a wrong but honest attempt: sorry-free, and it will not discharge the obligation\n    assert(true);")
open(p, "w", encoding="utf-8").write(s)
PY
d="$CLAUDE_CONFIG_DIR/projects/-stub"; mkdir -p "$d"
printf '{"type":"assistant","isSidechain":false,"version":"stub","timestamp":"2026-01-01T00:00:00Z","requestId":"req_stub","message":{"id":"msg_stub1","model":"claude-sonnet-5","usage":{"input_tokens":10,"cache_creation_input_tokens":100,"cache_read_input_tokens":0,"output_tokens":5,"service_tier":"standard"},"content":[{"type":"tool_use","id":"t1","name":"Bash","input":{"command":"./rt verus task.rs"}}]}}\n' > "$d/$sid.jsonl"
printf '{"type":"user","message":{"content":[{"type":"tool_result","tool_use_id":"t1","content":"verification results:: 0 verified, 1 errors"}]}}\n' >> "$d/$sid.jsonl"
printf '{"type":"assistant","isSidechain":false,"version":"stub","timestamp":"2026-01-01T00:00:01Z","requestId":"req_stub2","message":{"id":"msg_stub2","model":"claude-sonnet-5","usage":{"input_tokens":10,"cache_creation_input_tokens":0,"cache_read_input_tokens":100,"output_tokens":5,"service_tier":"standard"},"content":[{"type":"tool_use","id":"t2","name":"Edit","input":{"file_path":"%s/repo/task.rs","old_string":"","new_string":"assert(true);"}}]}}\n' "$EP" >> "$d/$sid.jsonl"
printf '{"type":"user","message":{"content":[{"type":"tool_result","tool_use_id":"t2","content":"The file has been updated."}]}}\n' >> "$d/$sid.jsonl"
printf '{"type":"result","subtype":"success","is_error":false,"num_turns":2,"result":"OK","session_id":"%s","usage":{"input_tokens":20,"cache_creation_input_tokens":100,"cache_read_input_tokens":100,"output_tokens":10},"modelUsage":{"claude-sonnet-5":{"inputTokens":20,"cacheCreationInputTokens":100,"cacheReadInputTokens":100,"outputTokens":10}}}\n' "$sid"
exit 0
