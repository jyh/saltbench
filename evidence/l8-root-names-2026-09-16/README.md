# Level 8 ADDENDUM 3: the root name A2.1's gate keys on

## bench (SaltBench lead), 2026-09-16, 20:4x PDT. Cited by `harness/systems-v3/AMENDMENT-gemini-level8-2026-09-16.md` ADDENDUM 3.

## 1 · `level_prefix_census.py` → `level-prefix-census.out`
The script ran on the run box, fed to `python3 -` over ssh, and is read-only. It counts the level prefixes
(`cells-l<digits><letters>-`) of the cell roots directly under the box's home directory. **Only prefixes and counts are
printed.** It REFUSES on a directory holding no `cells-*` root; that was driven on a scratch directory and exited 1.
**Reading:**
- 118 `cells-*` roots, 30 of them with a level prefix: `cells-l5-` 23 · `cells-l6-` 3 · `cells-l6r-` 1 ·
  `cells-l6u-` 1 · `cells-l6v-` 2.
- ⇒ **Three of level 6's four prefixes carry letters after the digit.**

## 2 · `drive_phases_gate.sh` → `drive-phases-gate-5c2bb95.out`
The script extracts `phases_verdict` VERBATIM from the supervisor `gemini_canary_wave_v1.sh` at harness `5c2bb95`. The
supervisor's sha256/16, `7e9934d0b84a0660`, is printed on the output's first line. The script drives the function with
`AGY_PHASES` unset over four one-row manifests. Beside each verdict it prints what the supervisor's own manifest loop
would fire.
**Reading:**
- The gate's own shape (`cells-l8-`) REFUSES.
- `cells-l8v-` and `cells-l8r-` read **OK**, and the loop fires them.
- A tab-led `cells-l8-` row reads **OK**, and the loop fires it: `read` with IFS=tab strips the leading tab, while
  `awk -F'\t'` puts the root in `$2`.

**Control, so the zero-refusals are a detector's zeros** (`widened-control.diff` → `drive-phases-gate-widened-control.out`):
- The same drive runs over a copy whose only change is the needle `cells-l8-` → `cells-l8[a-z0-9]*-`.
- Rows 2 and 3 turn REFUSE. Row 4 stays OK, because the second defect is the parser and not the needle.
