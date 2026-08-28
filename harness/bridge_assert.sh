#!/bin/bash
# bridge_assert.sh — before ANY harness run: for each id, the key the harness will open
# (<image>:latest) must be the SAME image object as the pinned <image>@<digest>. The harness prefers
# a local :latest and never compares a digest (refuter v3/v4), so this assertion is the certificate.
set -u
BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; bad=0
for i in "$@"; do
  read -r img dig < <(python3 -c "import json;d=json.load(open('$H/IMAGE-DIGESTS.json'))['images']['$i'];print(d['image'],d['digest'])")
  a=$(docker image inspect --format '{{.Id}}' "$img@$dig" 2>/dev/null); b=$(docker image inspect --format '{{.Id}}' "$img:latest" 2>/dev/null)
  if [ -n "$a" ] && [ "$a" = "$b" ]; then echo "BRIDGE OK   $i $img:latest == @${dig:7:12}"; else echo "BRIDGE FAIL $i latest=$b digest=$a"; bad=1; fi
done
exit $bad
