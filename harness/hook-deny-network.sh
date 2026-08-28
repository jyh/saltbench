#!/bin/bash
# hook-deny-network.sh — PreToolUse hook on Bash: REFUSES commands that reach for the network.
# Harness code, byte-identical in every arm, hashed in HASHES.txt. Reads the hook JSON on stdin,
# exits 2 (block) with the reason on stderr, else 0. The same pattern is used by meter.py's post-hoc
# audit, so a command that slips past this hook is still caught in the transcript.
# usage: hook (stdin JSON) · --selftest · --pattern (print the regex)
PAT='(^|[^A-Za-z0-9_./-])(curl|wget|ssh|scp|sftp|nc|ncat|telnet|rsync|ftp)([^A-Za-z0-9_-]|$)|git[ ]+(clone|fetch|pull|push|ls-remote|remote|submodule)|(pip[0-9.]*|python[0-9.]*[ ]+-m[ ]+pip|conda|mamba|npm|yarn|pnpm|apt(-get)?|brew|gem|cargo|uv)[ ]+(install|download|add|sync)|docker[ ]+(pull|login|push|build)|https?://|urllib|http\.client|socket\.'
case "${1:-}" in
  --pattern) printf '%s\n' "$PAT"; exit 0 ;;
  --selftest)
    fired=0; total=8
    deny() { printf '{"tool_name":"Bash","tool_input":{"command":%s}}' "$1" | bash "$0" >/dev/null 2>&1; }
    deny '"curl https://example.com"'        && echo "A1 curl must be denied" || fired=$((fired+1))
    deny '"git clone https://github.com/x/y"' && echo "A2 git clone must be denied" || fired=$((fired+1))
    deny '"pip install requests"'            && echo "A3 pip install must be denied" || fired=$((fired+1))
    deny '"python3 -c \"import urllib.request\""' && echo "A4 urllib must be denied" || fired=$((fired+1))
    deny '"grep -rn \"http://\" src/"'       && echo "A5 a URL in any command is denied (both arms alike)" || fired=$((fired+1))
    deny '"ls -la && cat f.py"'              || echo "A6 plain command must PASS"; deny '"ls -la && cat f.py"' && fired=$((fired+1))
    deny '"/E/rt python -m pytest tests -x"' && fired=$((fired+1)) || echo "A7 rt pytest must PASS"
    deny '"echo scp_like_name"'              && fired=$((fired+1)) || echo "A8 scp as a substring of a word must PASS"
    echo "HOOK SELFTEST arms fired: $fired of $total"; [ "$fired" -eq "$total" ]; exit $? ;;
esac
cmd=$(python3 -c 'import json,sys
try:
    o=json.load(sys.stdin); print(o.get("tool_input",{}).get("command",""))
except Exception: print("")')
if printf '%s' "$cmd" | grep -Eq "$PAT"; then
  printf 'BLOCKED by the episode harness: this command reaches for the network or a package index, and the environment has none. Work with what is in the checkout.\n' >&2
  exit 2
fi
exit 0
