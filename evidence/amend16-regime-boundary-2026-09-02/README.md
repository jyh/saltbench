# EVIDENCE — AMENDMENT 16 (the VeruSAGE stage-0 regime boundary). 2026-09-02, seat `bench`.

**ZERO MODEL TOKENS.** Every artifact is a run of the referee, the fence, a gate, or a transport.

⛔ **NO GROUND TRUTH IS STORED HERE** (protocol §8.8). `fencediff.py` reads `tasks.jsonl` from the seat-only
clone and emits **task_ids, verdicts and timings only**; `sample.json` is a list of task_ids.

| file | what it is |
|---|---|
| `exec-ladder.txt` | the four-step exec ladder: each red arm's error NAMES the next binary; arm d green |
| `fencediff.py` → `fencediff.json` | the fence differential — 61 seeded reference files FENCED vs UNFENCED |
| `sample.json` | the seeded sample (seed 20260902) over `AC ∪ NR`, + the 4 rarest-shape records |
| `selftest-fence.txt` | the fence's 18 arms, including CO's planted-GT pair (A11d/A11e) |
| `selftest-prompt-coverage.txt` | row AV's 5 arms — every refusal rule is stated in the agent's prompt |
| `smoke-red-arms.txt` | the toolchain gate refusing, incl. the REJECTED 0.2026.08.30 release |
| `smoke-on-studio.txt` | the same gate GREEN on the Studio against the merged `HASHES.txt` |
| `provision-verify.log` | the Studio transport verified BY CONTENT, both ends, 22 s |
| `provision-transport-firstrun.log` | the first run's log, kept as it ran (its set-hash step was the slow one) |
| `hashes-merge-additions-only.diff` | **the merge proof: 0 changed/removed, 37 added** |
| `suite-97-arms.txt` | the whole S2-Rust suite at HEAD: 97 arms, 0 failed |

**Reproduce the headline claims:**
- the exec set is four, each necessary: `python3 harness/s2rust/selftest_fence_verus.py` (arms A1–A4)
- the fence changes no verdict: `python3 evidence/.../fencediff.py` (needs the seat clone + the pin)
- the merge is additions-only: regenerate `harness/hashes.sh` with `CLEVER_SRC`/`VERUS_ROOT`/`LYNETTE_BIN`/
  `BENCH_REPO` set and diff against the committed table
- the gate refuses the wrong toolchain: `VERUS_ROOT=<the 0.2026.08.30 release> harness/s2rust/smoke_toolchain_verus.sh`
