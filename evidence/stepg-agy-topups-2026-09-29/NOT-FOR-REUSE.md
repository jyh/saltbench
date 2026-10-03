# `score-topups.sh` is a receipt of a run already made. Do not reuse it to score a new one.

`score-topups.sh` maps the test runner's exit code ALONE to a verdict: rc 0 reads PASS. It never checks that a `TESTS p/t` line was printed.
A solution that calls `process::exit(0)` before the suite prints its count therefore reads PASS. The run box measured this class on
2026-10-02 with Crc32's reference plus one `std::process::exit(0)`: rc 0, no TESTS line.

- **The record this script produced is not affected.** Census ADDENDUM 34 (`harness/systems-v3/CENSUS-full-matrix-2026-09-14.md`) read
  every PASS it scored: each carries `TESTS p/p` with p > 0.
- **The script is left byte-for-byte as it ran**, because a RESULT cites it by hash. Editing it would falsify that receipt.
- **Any NEW scoring takes `score_wave_v3.sh`'s rule as fixed on 2026-10-02:** PASS needs `TESTS p/t` with p = t > 0, and anything else at
  rc 0 is NOT-MEASURED.
