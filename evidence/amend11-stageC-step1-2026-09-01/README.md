# EVIDENCE — amendment 11 Step 1 (S2-Lean stage C, `a0`, the registered 12, `claude-opus-5`)

Run root `/Users/jyh/bench-c` on the Studio. Dispatch 2026-09-01T21:13:09Z, DRIVER DONE 22:09:49Z.
Every file copied from the Studio and **sha-verified against its source after the copy** — the receipt is
the content, never scp's exit code.

| file | what it proves |
|---|---|
| `morning_line_GATE_READ.txt` | THE READ. `REGISTERED POPULATION … n=12 … a0 proven 12/12 = 100.0%` ⇒ CEILING HOLD. Integrity block all empty; `constants` uniform at the registered regime. |
| `logs-s2-landings.log` | §2's GUARD: exactly 12 rows, one per registered id, all `DONE`. |
| `logs-run_s2_stage0.log` | both gates green at the fresh root, the resolved `ONLY_IDS`, every knob printed, and the driver's own DONE line. |
| `logs-halt_watch.log` | the enforcer ARMED 21:12:33Z — **56 s before the first episode** — polling to `tok=4339167 landed=12`, exiting **0 on the driver's DONE**. No HALT was ever written. |
| `logs-smoke.log` | the INHERITED smoke log, carrying `episode_s2.sh=cfb8a714…` — the sha that makes an inherited log honest (§5: the smoke gate and stage C are mutually exclusive at one root, by construction). |
| `state-s2-controls.json` | the FRESH controls record (2026-09-01, 31/31), the one `controls_gate.py` verified BY CONTENT against the live checker shas. |
| `vac_probe.txt` / `.json` | §8: `f_vac = 0/4`, each probe point, value and verdict. |
| `episode-records.tar` | all 12 episodes' `manifest.json` + `check.json` + `meter.json` (36 files) — the per-episode record, including `models` = `claude-opus-5` measured at the manifest. |

SET-HASH(evidence, at collection) = `53a340788a73681c`
