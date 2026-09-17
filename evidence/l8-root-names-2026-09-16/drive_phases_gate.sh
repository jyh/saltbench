#!/bin/bash
# drive_phases_gate.sh <gemini_canary_wave_v1.sh> -- extract the supervisor's phases_verdict function VERBATIM and drive it, with
# AGY_PHASES unset, over four one-row manifests: the gate's own shape, two roots named by level 6's precedent, and a tab-led row.
# Beside each verdict it prints what the supervisor's OWN manifest loop (IFS=tab read, '#'/empty skipped) would fire.
set -u
SUP=$1
[ -f "$SUP" ] || { echo "REFUSE: no supervisor at $SUP"; exit 2; }
T=$(mktemp -d "${TMPDIR:-/tmp}/pvdrive.XXXXXX")
sed -n '/^phases_verdict() {/,/^}/p' "$SUP" > "$T/pv.sh"
[ -s "$T/pv.sh" ] || { echo "REFUSE: no phases_verdict function in $SUP"; exit 2; }
. "$T/pv.sh"
echo "supervisor sha256/16 $(shasum -a 256 "$SUP" | cut -c1-16) · phases_verdict $(wc -l < "$T/pv.sh" | tr -d ' ') lines"
printf 'cells-l8-lzw-pro-plain-stmt\tLZW\tplain\t3\tl8a\t\n'    > "$T/1-gate-shape.tsv"
printf 'cells-l8v-lzw-pro-plain-stmt\tLZW\tplain\t3\tl8v\t\n'   > "$T/2-precedent-v.tsv"
printf 'cells-l8r-lzw-pro-salt-stmt\tLZW\tsalt-diet\t3\tl8r\t\n' > "$T/3-precedent-r.tsv"
printf '\tcells-l8-lzw-pro-plain-stmt\tLZW\tplain\t3\tl8t\t\n'  > "$T/4-tab-led.tsv"
# the supervisor's own manifest reader (a function: bash 3.2 cannot parse a case pattern inside $( ))
loop_fires() {
  while IFS=$'\t' read -r root task arm reps prefix extra; do
    case "${root:-}" in ''|'#'*) continue ;; esac
    echo "FIRES $root"
  done < "$1"
}
printf 'manifest\tphases_verdict(unset)\tsupervisor loop\n'
for m in "$T"/*.tsv; do
  v=$(phases_verdict "$m" '' | cut -d: -f1)
  f=$(loop_fires "$m")
  printf '%s\t%s\t%s\n' "$(basename "$m" .tsv)" "$v" "${f:-SKIPS}"
done
[ -d "${T:?}" ] && rm -rf -- "${T:?}"
