#!/bin/bash
# check2b.sh — THE PER-CONTAINER LEAK ASSERTION (DESIGN §4 CHECK 2b), run on the AGENT's working
# copy in EVERY arm, on the host copy and again inside the container. All four states fail-closed.
#   usage: check2b.sh <dir> [<pinned_digest> <image_ref>]      (host form; the digest args add the
#          RepoDigests assertion)   ·   docker exec -i <ctr> bash -s -- /testbed < check2b.sh
# Prints one verdict line per state and a final CHECK2B PASS|FAIL; exit 0 only on PASS.
# ⛔ The four states are tested SEPARATELY because each one alone passes a test written for another
# (a nested .git survives a top-level check; a worktree pointer is a FILE; packed refs outlive a
# removed remote). A directory that is not there is a FAIL, not a pass — absence is not evidence.
set -u
D="${1:?dir}"; DIG="${2:-}"; IMG="${3:-}"
fail=0
say() { printf '%s\n' "$*"; }
[ -d "$D" ] || { say "CHECK2B FAIL: $D is not a directory"; exit 1; }
# 1. no .git (dir OR file) at any depth
n=$(find "$D" -name .git -print 2>/dev/null | head -5)
if [ -z "$n" ]; then say "S1 PASS no .git at any depth"; else say "S1 FAIL .git present:"; say "$n"; fail=1; fi
# 2. no packed-refs at any depth
n=$(find "$D" -name packed-refs -print 2>/dev/null | head -5)
if [ -z "$n" ]; then say "S2 PASS no packed-refs"; else say "S2 FAIL packed-refs present:"; say "$n"; fail=1; fi
# 3. no worktree pointer file (a FILE named .git containing gitdir:)
n=$(find "$D" -type f -name .git -exec grep -l '^gitdir:' {} + 2>/dev/null | head -5)
if [ -z "$n" ]; then say "S3 PASS no worktree pointer file"; else say "S3 FAIL gitdir pointer:"; say "$n"; fail=1; fi
# 4. no reachable object store, with GIT_DIR / GIT_COMMON_DIR unset, from the dir AND its deepest child
if command -v git >/dev/null 2>&1; then
  if ( cd "$D" && env -u GIT_DIR -u GIT_COMMON_DIR git rev-parse --git-dir ) >/dev/null 2>&1; then
    say "S4 FAIL git rev-parse --git-dir succeeded in $D (object store reachable: $(cd "$D" && env -u GIT_DIR -u GIT_COMMON_DIR git rev-parse --git-dir 2>/dev/null))"; fail=1
  else
    say "S4 PASS no reachable object store from $D"
  fi
else
  say "S4 FAIL git is not on PATH here, so reachability cannot be tested"; fail=1
fi
# 5. (host form only) the image the container will run IS the pinned digest
if [ -n "$DIG" ]; then
  rd=$(docker image inspect --format '{{join .RepoDigests ","}}' "$IMG@$DIG" 2>/dev/null)
  case ",$rd," in *"@$DIG,"*) say "S5 PASS RepoDigests carries $DIG" ;; *) say "S5 FAIL RepoDigests=$rd lacks $DIG"; fail=1 ;; esac
fi
if [ "$fail" = 0 ]; then say "CHECK2B PASS $D"; exit 0; else say "CHECK2B FAIL $D"; exit 1; fi
