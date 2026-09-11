#!/bin/bash
# harvest_view_asof.sh CUTOFF OUTDIR — a view of the harvest archive as of a moment.
#
# ⛔⛔ WHY THIS EXISTS.  `score_matrix1.py` prices each cell from "the latest harvest that parses",
#   and the archive GROWS: cells are re-harvested, and a cell that continued into phase 2 genuinely
#   costs more the second time.  So re-running the scorer does NOT reproduce a table published a week
#   earlier — measured 2026-09-11, RESULT-n3-topup-2026-09-09 §3 reads $5.36 $6.21 $7.64 for Crc32
#   plain and the same scorer read $12.42 $13.68 $15.52 that day.  Neither reading is wrong.
#   ⇒ 🔑 A RESULT THAT QUOTES PRICES FROM A MUTABLE ARCHIVE THROUGH A "LATEST" RULE IS A CLAIM ABOUT
#     A MOMENT NOBODY RECORDED.
# ✅ Point HARVEST_ROOT at this view and the old reading comes back — AND REPRODUCING THE PUBLISHED
#   TABLE IS THE PROOF that the restriction is the right one.  That is what makes it safe to add a
#   token column to a published table (row KS) without silently replacing its prices.
#
# ⛔ The cutoff is compared against the harvest directory's OWN NAME SUFFIX (-YYYYMMDDTHHMMSSZ),
#   never against mtime: a copy, a restore or an rsync moves mtime and does not move the name.
set -u
CUT=${1:?usage: harvest_view_asof.sh YYYYMMDDTHHMMSSZ OUTDIR}
OUT=${2:?usage: harvest_view_asof.sh YYYYMMDDTHHMMSSZ OUTDIR}
SRC=${HARVEST_SRC:-$HOME/harvest-v3}
[ -d "$SRC" ] || { echo "REFUSE — no archive at $SRC"; exit 64; }
mkdir -p "$OUT" || exit 8
n=0; skipped=0; unstamped=0
for d in "$SRC"/*/; do
  b=$(basename "$d")
  stamp=${b##*-}
  case "$stamp" in
    2[0-9][0-9][0-9][0-1][0-9][0-3][0-9]T[0-9][0-9][0-9][0-9][0-9][0-9]Z) ;;
    # ⛔ A DIRECTORY WHOSE NAME CARRIES NO STAMP IS REPORTED, NEVER SILENTLY INCLUDED OR DROPPED:
    #   either choice would be an undeclared edit to the population the reading is about.
    *) unstamped=$((unstamped+1)); echo "  ⚠️ UNSTAMPED, NOT IN THE VIEW: $b"; continue ;;
  esac
  if [ "$stamp" \< "$CUT" ] || [ "$stamp" = "$CUT" ]; then
    ln -sfn "$d" "$OUT/$b"; n=$((n+1))
  else
    skipped=$((skipped+1))
  fi
done
echo "view $OUT: $n harvest(s) at or before $CUT · $skipped later · $unstamped unstamped (excluded, named above)"
