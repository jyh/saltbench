#!/bin/bash
# hook-deny-network.sh — PreToolUse hook on Bash. Harness code, byte-identical in every arm, hashed in
# HASHES.txt. Reads the hook JSON on stdin; exits 2 (block, reason on stderr) or 0.
# Two classes, blocked alike but AUDITED APART by meter.py (refuter R4/L7):
#   ESCAPE  — fetchers/installers/sockets, the docker CLI, and any literal path into the harness's own
#             trees ($BENCH_ROOT, the config dir, another episode) — an attempt is evidence, a success VOIDs.
#   URL     — a URL scheme in the command text (an issue often quotes one; grepping for it is innocent):
#             blocked so nothing is fetched, counted, never a VOID on its own.
# The agent's own episode dir is exempt from the path rule via $BENCH_EP (exported by episode.sh).
# usage: hook (stdin JSON) · --selftest · --pattern-escape · --pattern-url
ESC='(^|[^A-Za-z0-9_./-])(curl|wget|ssh|scp|sftp|nc|ncat|telnet|rsync|ftp|nscurl|gh|docker|nerdctl|podman)([^A-Za-z0-9_-]|$)|git[ ]+(-C[ ]+[^ ]+[ ]+)?(clone|fetch|pull|push|ls-remote|remote|submodule)|(pip[0-9.]*|python[0-9.]*[ ]+-m[ ]+pip|conda|mamba|npm|yarn|pnpm|apt(-get)?|brew|gem|cargo|uv)[ ]+(install|download|add|sync)|urllib|http\.client|socket\.|requests\.(get|post)|/Users/[^ ]*/(bench|\.claude)|~/(bench|\.claude)|\$HOME/(bench|\.claude)|/Users/[^ ]*/work/ep-'
URL='https?://'
case "${1:-}" in
  --pattern-escape) printf '%s\n' "$ESC"; exit 0 ;;
  --pattern-url) printf '%s\n' "$URL"; exit 0 ;;
  --selftest)
    fired=0; total=12
    deny() { printf '{"tool_name":"Bash","tool_input":{"command":%s}}' "$1" | BENCH_EP=/Users/x/work/ep-own bash "$0" >/dev/null 2>&1; }
    deny '"curl https://example.com"'          && echo "A1 curl must be denied" || fired=$((fired+1))
    deny '"git -C /tmp clone https://github.com/x/y"' && echo "A2 git -C clone must be denied" || fired=$((fired+1))
    deny '"pip install requests"'              && echo "A3 pip install must be denied" || fired=$((fired+1))
    deny '"python3 -c \"import urllib.request\""' && echo "A4 urllib must be denied" || fired=$((fired+1))
    deny '"grep -rn \"http://\" src/"'         && echo "A5 a URL mention is blocked" || fired=$((fired+1))
    deny '"ls -la && cat f.py"'                && fired=$((fired+1)) || echo "A6 plain command must PASS"
    deny '"/Users/x/work/ep-own/rt python -m pytest tests -x"' && fired=$((fired+1)) || echo "A7 own rt must PASS"
    deny '"echo scp_like_name"'                && fired=$((fired+1)) || echo "A8 scp as a word fragment must PASS"
    deny '"docker run --rm img bash"'          && echo "A9 docker must be denied" || fired=$((fired+1))
    deny '"cat /Users/jyh/bench/harness/data/x.json"' && echo "A10 harness tree must be denied" || fired=$((fired+1))
    deny '"cat /Users/x/work/ep-other/CLAUDE.md"' && echo "A11 another episode must be denied" || fired=$((fired+1))
    deny '"gh pr diff 1 -R a/b"'               && echo "A12 gh must be denied" || fired=$((fired+1))
    echo "HOOK SELFTEST arms fired: $fired of $total"; [ "$fired" -eq "$total" ]; exit $? ;;
esac
cmd=$(python3 -c 'import json,sys
try:
    o=json.load(sys.stdin); c=o.get("tool_input",{}).get("command",""); print(c if isinstance(c,str) else "")
except Exception: print("")')
own="${BENCH_EP:-}"
# strip the agent's own episode path before matching so its rt/repo/CLAUDE.md are never an escape
if [ -n "$own" ]; then probe=$(printf '%s' "$cmd" | sed "s|$own||g"); else probe="$cmd"; fi
if printf '%s' "$probe" | grep -Eq "$ESC"; then
  printf 'BLOCKED by the episode harness: this command reaches outside the checkout (network, package index, container tooling, or a path outside the working copy). Work with what is in the checkout, through the rt wrapper.\n' >&2
  exit 2
fi
if printf '%s' "$cmd" | grep -Eq "$URL"; then
  printf 'BLOCKED by the episode harness: URLs cannot be used here (there is no network). Search for the path or text without the scheme.\n' >&2
  exit 2
fi
exit 0
