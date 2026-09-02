# EVIDENCE — amendment 13 (row AW): `a1` (placebo) at `claude-opus-5`, stage A+B on U15

Root `/Users/jyh/bench-aw` on kriterion, built BY HAND (`ship A` hangs). Stage A 2026-09-01T22:20:20Z →
22:54:05Z; stage B 22:54:50Z → 2026-09-02T00:31:59Z. Every file sha-verified against its source AFTER copying.

| file | what it proves |
|---|---|
| `morning_line_AW_READ.txt` | **THE READ: `a1 proven 9/15`, `Δ1 = +1` ⇒ ARM-INDEPENDENT**; classes, terms, and the full integrity block. ⚠️ Its `pairs` line is VOID at this root (only `a1` landed here) — the cross-root comparison is in the RESULT §2. |
| `logs-s2-landings.log` | 30 rows: 15 stage-A + 15 stage-B, one per U15 id per stage, exactly the registered population. |
| `logs-run_s2_stage0.log` | both stages' gates green, resolved `ONLY_IDS`, every knob printed (`TOKEN_CEILING=30000000` — the a8-matched value), both DRIVER DONE lines. |
| `logs-halt_watch.log` | enforcer armed before EACH stage, peak `tok=14,164,874/35,000,000` = 40 %, both watches exiting 0 on the driver's own DONE. No HALT written. |
| `bc_gate_PASS.txt` | **PASS 15/15 by CONTENT before stage B ran** — every cell's `a_bodies_sha256` matched to its own episode's `bodies.json`, in-root, 0.0–0.5 h old. The first run this gate could actually verify. |
| `p112_canonical_STATEMENT_ALTERED.lean` | ⛔ **THE FALSE POSITIVE, kept as the specimen.** 61 lines, **ZERO `start_def`/`end_def` markers**, and its `problem_spec` block is **byte-identical to frozen** (sha256 `de0d91aa2312317bebf501798e81502c` both sides). The agent deleted the harness's section markers; the specification was never altered. |
| `state-s2-controls.json` | the fresh controls record, verified by `controls_gate.py` against the LIVE checker shas at both stages. |
| `episode-records.tar` | all 30 episodes' `manifest.json` + `check.json` + `meter.json` (90 files). |

SET-HASH(evidence, at collection) = `af64acb5e09e9e65`
