#!/bin/bash
# hashes.sh — regenerate HASHES.txt: every harness file, the settings, and the RENDERED arm files
# for a canonical episode path so an episode can assert its CLAUDE.md is a registered rendering.
# ⛔ The rendered CLAUDE.md contains the episode path, so its sha varies per episode; what is pinned is
# the sha of the rendering with the path replaced by the literal __EP__ — episode.sh checks the
# UN-substituted form by re-rendering.
set -u
cd "$(dirname "$0")" || exit 1
{
  echo "# HASHES — regenerate with harness/hashes.sh; sha256; generated $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  for f in base.md prompt.md rt.template episode.sh check2b.sh check2b.selftest.sh hook-deny-network.sh meter.py build_prompt.py preflight_gold.sh bridge_assert.sh score.sh run_stage0.sh predictions.py project_data.py morning_line.py pull_pilot.sh sync_studio.sh studio_phase.sh dry_exec_stub.sh settings.bench.json arms/*.md; do
    printf '%s %s\n' "$f" "$(shasum -a 256 "$f" | cut -d' ' -f1)"
  done
  printf 'settings.json %s\n' "$(shasum -a 256 settings.bench.json | cut -d' ' -f1)"
  printf 'claude-version %s\n' "2.1.251"
  for a in arms/*.md; do
    id=$(basename "$a" .md)
    printf 'rendered-%s(__EP__) %s bytes=%s\n' "$id" "$(cat base.md "$a" | shasum -a 256 | cut -d' ' -f1)" "$(cat base.md "$a" | wc -c | tr -d ' ')"
  done
} > HASHES.txt
cat HASHES.txt
# per-task CANONICAL prompt shas (prompt with the episode path replaced by __EP__), so a pair's prompts are
# provably identical up to the path (refuter F3); requires data/problem_statements.json beside the harness
if [ -f data/problem_statements.json ]; then
  python3 - >> HASHES.txt <<'PY'
import json,hashlib
t=open("prompt.md").read()
for r in sorted(json.load(open("data/problem_statements.json")),key=lambda r:r["instance_id"]):
    p=t.replace("__PROBLEM_STATEMENT__",r["problem_statement"])
    print("prompt-canonical", r["instance_id"], hashlib.sha256(p.encode()).hexdigest())
PY
  printf 'problem_statements.json %s\n' "$(shasum -a 256 data/problem_statements.json | cut -d' ' -f1)" >> HASHES.txt
fi
