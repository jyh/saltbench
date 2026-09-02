# EVIDENCE — AMENDMENT 15 (S2-Rust: the arm, the grader, stage 0). 2026-09-01, seat `bench`.

**ZERO MODEL TOKENS.** Every artifact here is a read of the benchmark or a run of the Verus referee.

⛔ **NO GROUND TRUTH IS STORED IN THIS DIRECTORY OR ANYWHERE IN THIS REPO** (protocol §8.8). The scripts read
`tasks.jsonl` from the SEAT-ONLY clone at `~/bench-src/verus-proof-synthesis` (pin
`cbf9c0c6337b224fd8e5b7cb4e01ae65c0f98bc1`, jsonl sha256
`d9b23ed7066ea6a7d782b98d3660f1fee514633b6a3e12b2801c3691f1cf689a`) and emit **counts, task_ids, verdicts and
timings only**. The only Rust fragments present are short excerpts of the *stripped task* bodies (the empty and
`// TODO` placeholder scaffolding the benchmark ships publicly), never of `ground_truth`.

| file | what it is |
|---|---|
| `census.py` → (inline) | the 849-record project census; establishes `AC` = `Anvil-Advanced` (63), `NR` = `NRKernel` (204) |
| `classify.py` → `population-census-AC-NR.txt` | the item-level target classification over all 267, by lynette's own target rule with a brace-matching parser |
| `faithful.py` → `faithfulness-and-shape.txt` | the shape recovery (163 → **207**) and **the fatal**: DD §3.2 clause (b) reproduces **31 / 207** |
| `gtpass.py` → `gtpass-0.2026.08.30.b432e82.json`, `gtpass-today-release.log` | ground-truth pass, seeded 15 (seed 20260902), §3.5's chosen binary: **10/15**, five RUSTC FRONT-END failures |
| `gtpass_pin.py` → `gtpass-0.2025.09.12.bb1f342.json`, `gtpass-pin-release.log` | the same 15 under the benchmark's pin: **15/15**, reference `COMPILE` = **0** |

⚠️ `gtpass_pin.py` is `gtpass.py` with the binary path substituted; its printed banner still reads
*"at today's release"* — **that string is stale in the copied script and the log inherits it.** The binary
actually exercised is `~/bench-src/verus-release-pin/…/verus` = `release/0.2025.09.12.bb1f342`, which the log's
own line 4 records. Left uncorrected on purpose: the log is the artifact as it ran, and the correction belongs
here rather than in a re-run that would no longer be the run that produced the numbers.

**The two standing receipts named in the amendment:**
- **§7, the `--no-cheating` retirement** — on the pristine 536-B file
  `NR__spec_t__os_invariant__lemma_map_insert_values_equality` (1 `external_body` stub), the flag adds
  `error: external_body/assume_specification not allowed with --no-cheating`. Reproduce:
  extract that record's `task` to `task.rs` and run the referee with and without the flag.
- **§5, the pin** — the two-row table above. Reproduce by running both scripts.

**Toolchain prerequisite** (found by running the binary, not by unpacking it): the pin release requires
`rustup` toolchain **`1.88.0-aarch64-apple-darwin`**; `release/0.2026.08.30.b432e82` requires `1.97.1`. Without
it the binary exits 1 before verifying anything.
