#!/bin/bash
# drives every state both ways on scratch trees; prints arms fired
set -u
H=$(cd "$(dirname "$0")" && pwd); T=$(mktemp -d); fired=0; total=6
mk() { rm -rf "$T/d"; mkdir -p "$T/d/sub"; echo x > "$T/d/sub/f"; }
mk; bash "$H/check2b.sh" "$T/d" >/dev/null 2>&1 && fired=$((fired+1)) || echo "ARM1 clean tree must PASS"
mk; mkdir "$T/d/sub/.git"; bash "$H/check2b.sh" "$T/d" >/dev/null 2>&1 && echo "ARM2 nested .git dir must FAIL" || fired=$((fired+1))
mk; touch "$T/d/sub/packed-refs"; bash "$H/check2b.sh" "$T/d" >/dev/null 2>&1 && echo "ARM3 packed-refs must FAIL" || fired=$((fired+1))
mk; printf 'gitdir: /somewhere/.git\n' > "$T/d/sub/.git"; bash "$H/check2b.sh" "$T/d" >/dev/null 2>&1 && echo "ARM4 worktree pointer must FAIL" || fired=$((fired+1))
# ARM5: a tree INSIDE a real repo (object store reachable from above) must FAIL even with no .git inside
rm -rf "$T/r"; mkdir -p "$T/r/inner/sub"; ( cd "$T/r" && git init -q . ); echo x > "$T/r/inner/sub/f"
bash "$H/check2b.sh" "$T/r/inner" >/dev/null 2>&1 && echo "ARM5 reachable parent object store must FAIL" || fired=$((fired+1))
# ARM6: absent directory must FAIL
bash "$H/check2b.sh" "$T/nope" >/dev/null 2>&1 && echo "ARM6 absent dir must FAIL" || fired=$((fired+1))
rm -rf "$T"; echo "CHECK2B SELFTEST arms fired: $fired of $total"; [ "$fired" -eq "$total" ]
