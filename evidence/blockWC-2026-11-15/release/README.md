# Block WC — §WC3 items 3, 4 and 5(b), driven 2026-11-15 (zero model tokens)

The release addendum (ADDENDUM 1 of `harness/systems-v3/AMENDMENT-O37-wht-ntt-specchange-claude-2026-11-13.md`) cites these files.
The export is saltbench-systems `d55062a6`: the block-T candidate `09516b81` plus the block-WC stager. Paths are masked (`~`, `SCRATCH`, `EXPORT` = the export of d55062a6 on the run box).

- `wc_derive_sources.py` and `derive-sources.out`: the stager's `WC_SOURCES` (24 rows) derived from `../p1-baselines.tsv` by NC §C2
  rules 3–4, as §WC2 carries them, and compared byte for byte with `d55062a6:harness/systems-v3/clb_stage.sh`. The result is EQUALS,
  rc 0. The negative control (one row changed) gives DIFFERS, rc 1. The derived table is printed below the check.
- `clb_blockWC_selftest.out` (item 4): 44 passed, 0 failed on the candidate. The reference `09516b81` fails all 15 block-WC arms. Mutant
  (a), a fresh build for WCO/WCS, reddens 8 arms. Older blocks' dry stage output is byte-equal in 24 forms.
- `clb_blockNC_selftest.out`, `clb_blockT_selftest.out`, `clb_blockW_selftest.out`: 31/31, 14/14 and 13/13 on the candidate.
  `clb_blockG_selftest.excerpt` (FAIL lines and summary only) reads 17 passed, 5 failed. The 5 failures are the U arms against `9d87318`,
  the same five that the NC stager's commit (`ee7450ce`) declared as rot older than it.
- `copydry.log` (item 3): the copy form, one dry cell per model, on the export's own bytes. wcdry001 is a copy of clbdtp01 (Opus, NTT,
  plain) and wcdry002 a copy of clbiwp01 (Sonnet, WHT, plain). For each: `cell_copy_v3.py` then `customer.sh dispatch`, both rc 0; the
  source's tree hash is equal before and after; `inbox/change-1.md` equals the preamble plus the card's `## Change request (phase 2)`
  section; the interface equals `B/interface.rs`; `ctl/phase1/` is present; the slug differs from the source's.
  The comparer is `wc_change_cmp.py`. It was written apart from `customer.sh` and `render_requirements.py`, and its only transform is
  joining each bullet's continuation lines to the bullet. Control: the NTT card against the WHT file reads DIFFER. The first comparer
  tried (a line-containment check) reported 5 of 19 lines missing. Those were bullet continuation lines that the render joins, so that
  instrument was wrong and was replaced. It is kept in the log as run.
- `stagedry.log` (item 4, on the run box): the stager driven dry through the export. `--roots --freeze WC` gives 11 roots (5 Opus,
  6 Sonnet). T-WC-O's copy (WCO NTT salt-diet 1 ← clbdts01) was staged from a SCRATCH COPY of its source. `clb_fire.sh --phase 2 --dry`
  passed the client pin and the credential and dispatched the change request (tag P1). A WFS fresh build (clbzts02) ran dry, and three
  refusals fired. The real source's tree hash is unchanged.
- `leak.out`, `leak-selftest.out` (item 5(b)): `check_withheld_leak_v3.py` over an archive of `d55062a6` reads CLEAN: 343 identifiers
  across 13 tasks, every positive control fired, 0 in any view. Its selftest is 3/3. WHT's 30 identifiers include 19 from `B/withheld`
  and NTT's 28 include 17, so both B/ withheld trees are screened. `leak.out` sha256/16 is 61232087f298b393, equal to NC's at `ee7450ce`,
  because the task bytes are the same.

What these files do not show: the account check and the zero-cell probe (item 5(a) and the probe) wait on the PM's pool. The dry fire
stops before the settings render, the fence, trust and the launch, as NC's did.
