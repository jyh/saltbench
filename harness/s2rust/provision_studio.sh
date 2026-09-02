#!/bin/bash
# provision_studio.sh — put the S2-Rust toolchain on the Studio, BY TRANSPORT FROM THE SEAT, and verify it
# BY CONTENT. Run FROM THE SEAT. Zero model tokens.   env: STUDIO (ssh host, default kriterion-lan)
#
# ⛔ WHY TRANSPORT AND NOT `curl https://sh.rustup.rs | sh`. The wave's firewall line is "no binary of
# unestablished provenance; saltbench pins its own download by sha256". A fresh network install on the Studio
# would fetch binaries nothing in this campaign has ever hashed, and would do it on the machine that runs the
# episodes. The seat's copies are already pinned in the hash table, so shipping THOSE makes the Studio's
# toolchain a byte-identical copy of the one every stage-0 number was measured on.
#   ⇒ VERIFY A TRANSPORT BY CONTENT, NEVER BY ITS EXIT CODE (the 08/30 law, paid for by `ship A`'s silent
#     hang). Every payload below is sha256'd on BOTH ends and the script REFUSES on any mismatch.
#
# ⛔ NOTHING HERE TOUCHES `~/bench/harness`. That tree is the ONE harness on the Studio (the state roots'
# `harness` are SYMLINKS to it) and it is frozen at the stage-C freeze commit, whose 09/02 dispatch window is
# still open. The toolchain lands in `~/verus-pin`, outside it, and `--verify` asserts that afterwards.
#
# usage: provision_studio.sh [--verify]     --verify skips the copy and only re-checks what is there
set -u
STUDIO="${STUDIO:-kriterion-lan}"
SSH="ssh -o ConnectTimeout=10"
HERE="$(cd "$(dirname "$0")" && pwd)"
VERIFY_ONLY=0; [ "${1:-}" = "--verify" ] && VERIFY_ONLY=1

VERUS_SRC="${VERUS_ROOT:-$HOME/bench-src/verus-release-pin/verus-arm64-macos}"
LYNETTE_SRC="${LYNETTE_BIN:-$HOME/bench-src/verus-proof-synthesis/utils/lynette/source/target/release/lynette}"
CHANNEL="1.88.0-aarch64-apple-darwin"
TC_SRC="$HOME/.rustup/toolchains/$CHANNEL"
RUSTUP_SRC="$(command -v rustup)"
DEST=/Users/jyh/verus-pin

fail(){ echo "PROVISION REFUSE: $*" >&2; exit 2; }
sha(){ shasum -a 256 "$1" | cut -d' ' -f1; }
rsha(){ $SSH "$STUDIO" "shasum -a 256 '$1' 2>/dev/null | cut -d' ' -f1"; }

for p in "$VERUS_SRC/verus" "$VERUS_SRC/z3" "$VERUS_SRC/rust_verify" "$VERUS_SRC/libvstd.rlib" \
         "$LYNETTE_SRC" "$RUSTUP_SRC"; do
  [ -e "$p" ] || fail "missing on the seat: $p"
done
[ -d "$TC_SRC" ] || fail "missing rust toolchain on the seat: $TC_SRC"

if [ "$VERIFY_ONLY" = 0 ]; then
  echo "== transport =="
  $SSH "$STUDIO" "mkdir -p $DEST ~/.cargo/bin ~/.rustup/toolchains" || fail "cannot mkdir on $STUDIO"
  rsync -a --delete -e "$SSH" "$VERUS_SRC/"  "$STUDIO:$DEST/verus-arm64-macos/" || fail "verus rsync"
  rsync -a          -e "$SSH" "$LYNETTE_SRC" "$STUDIO:$DEST/lynette"            || fail "lynette rsync"
  rsync -a          -e "$SSH" "$RUSTUP_SRC"  "$STUDIO:.cargo/bin/rustup"        || fail "rustup rsync"
  rsync -a --delete -e "$SSH" "$TC_SRC/"     "$STUDIO:.rustup/toolchains/$CHANNEL/" || fail "toolchain rsync"
  # rustup needs a default channel or `rustup run` refuses; written only if absent so an existing Studio
  # rustup configuration is never silently rewritten by a provisioning step.
  $SSH "$STUDIO" "[ -f ~/.rustup/settings.toml ] || printf 'default_toolchain = \"%s\"\nprofile = \"default\"\nversion = \"12\"\n' '$CHANNEL' > ~/.rustup/settings.toml"
fi

echo "== verify BY CONTENT (both ends) =="
rc=0
check(){ # check <label> <local> <remote>
  local l r; l=$(sha "$2"); r=$(rsha "$3")
  if [ "$l" = "$r" ] && [ -n "$l" ]; then printf '  OK    %-12s %s\n' "$1" "${l:0:16}"
  else printf '  DRIFT %-12s seat=%s studio=%s\n' "$1" "${l:0:16}" "${r:0:16}"; rc=2; fi
}
check verus       "$VERUS_SRC/verus"        "$DEST/verus-arm64-macos/verus"
check rust_verify "$VERUS_SRC/rust_verify"  "$DEST/verus-arm64-macos/rust_verify"
check z3          "$VERUS_SRC/z3"           "$DEST/verus-arm64-macos/z3"
check vstd        "$VERUS_SRC/libvstd.rlib" "$DEST/verus-arm64-macos/libvstd.rlib"
check lynette     "$LYNETTE_SRC"            "$DEST/lynette"
check rustup      "$RUSTUP_SRC"             "$HOME/.cargo/bin/rustup"

# the toolchain is a TREE, so it is verified by a SET-HASH, not by one file: a single-file check would pass
# on a half-copied 1.2 GB directory. The set-hash folds sorted "relpath sha" lines — one implementation,
# computed the same way on both ends by the same shell pipeline.
# ⛔ `find -exec shasum {} \;` SPAWNS ONE PROCESS PER FILE. A rust toolchain is ~1.2 GB across thousands of
# files, on BOTH ends, so the first cut of this line turned a 90-second verify into a many-minute one for no
# extra assurance whatsoever. `-print0 | xargs -0` hashes the same bytes in batches.
#   ⇒ A CORRECT MEASUREMENT THAT IS TOO SLOW TO RUN GETS SKIPPED, AND A SKIPPED GATE IS AN ABSENT ONE.
SETHASH='find . -type f -print0 | xargs -0 shasum -a 256 | sed "s| \./| |" | sort | shasum -a 256 | cut -d" " -f1'
sethash_local=$(cd "$TC_SRC" && eval "$SETHASH")
sethash_remote=$($SSH "$STUDIO" "cd ~/.rustup/toolchains/$CHANNEL && $SETHASH")
if [ "$sethash_local" = "$sethash_remote" ] && [ -n "$sethash_local" ]; then
  printf '  OK    %-12s %s (tree set-hash)\n' "toolchain" "${sethash_local:0:16}"
else
  printf '  DRIFT %-12s seat=%s studio=%s\n' "toolchain" "${sethash_local:0:16}" "${sethash_remote:0:16}"; rc=2
fi

# the harness must be untouched by provisioning — this is the assertion, not the intention
n=$($SSH "$STUDIO" "find ~/bench/harness -name 'verus*' -o -name 'z3' -o -name 'lynette' 2>/dev/null | wc -l | tr -d ' '")
[ "$n" = "0" ] && echo "  OK    harness      no toolchain file under ~/bench/harness" \
               || { echo "  FAIL  harness      $n toolchain file(s) under ~/bench/harness"; rc=2; }

# and it must actually RUN there — a byte-identical copy that cannot execute is not a provisioned toolchain
echo "== smoke: verus runs on the Studio =="
$SSH "$STUDIO" "mkdir -p ~/verus-smoke && printf 'use vstd::prelude::*;\nverus!{\nproof fn p(x: int) ensures x + 0 == x {}\n}\nfn main() {}\n' > ~/verus-smoke/t.rs && cd ~/verus-smoke && PATH=\$HOME/.cargo/bin:\$PATH $DEST/verus-arm64-macos/verus --crate-type=lib t.rs 2>&1 | tail -2"

[ "$rc" = 0 ] && echo "PROVISION OK" || echo "PROVISION FAILED (rc=$rc)"
exit $rc
