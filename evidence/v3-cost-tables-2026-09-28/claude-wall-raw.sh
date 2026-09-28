while IFS=$'\t' read c r; do
  L=~/$r/$c/ctl/watch.log
  for ph in 1 2; do
    E=~/$r/$c/ctl/end-$ph; [ -s "$E" ] || continue
    # the last METER line of this phase: watch.log is appended across phases; the phase-2 section starts after end-1's timestamp
    t1=$(cut -d' ' -f1 ~/$r/$c/ctl/end-1)
    if [ $ph = 1 ]; then w=$(awk -v t="$t1" '$2=="METER" && $1<=t' "$L" | tail -1 | grep -oE 'wall [0-9]+/[0-9]+'); else w=$(awk -v t="$t1" '$2=="METER" && $1>t' "$L" | tail -1 | grep -oE 'wall [0-9]+/[0-9]+'); fi
    held=$(grep -E "^[^ ]+ HOLD .* closed after" "$L" | awk -v ph=$ph -v t="$t1" '(ph==1 && $1<=t) || (ph==2 && $1>t)' | grep -oE 'after [0-9]+' | awk '{s+=$2} END{print s+0}')
    printf "%s\t%s\t%s\t%s\t%s\t%s\n" "$c" "$ph" "${w:-NONE}" "$held" "$(cut -d' ' -f2 $E)" "$r"
  done
done < ~/bench-dry/v3-claude-cells.tsv
