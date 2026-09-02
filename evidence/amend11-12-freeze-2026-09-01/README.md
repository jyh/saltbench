# EVIDENCE — the AMENDMENT 11 + 12 freeze, 2026-09-01 (desk row AS)

Everything here is ZERO MODEL TOKENS. Each file is the raw output of a check named in
`AMENDMENT-11-stageC-2026-09-01.md` §12 or `AMENDMENT-12-instrument-2026-09-01.md`.

| file | what it is |
|---|---|
| `seat_selftests.txt` | the four seat-side gates driven back to back: `c_dead_merge` **11/0**, `controls_gate` **17/0**, `halt_watch` **23/0 three times** (it was intermittent before the two-clock repair — see amendment 12 §4), `s2_morning_line` **10/0**. ⚠️ `c_oracle_preflight --selftest` is **rc 2 on the seat with no Lean and no `SSH_HOST`, by design** — it refuses loudly rather than reporting a verdict it did not compute. Its real runs are in `preflight_selftest_STUDIO.log`. |
| `preflight_selftest_STUDIO.log` | the stage-C oracle pre-flight's own gate, **driven two ways, 9 arms / 0 failed both times**: on the Studio at the synced sha, and **from the seat over ssh** (`SSH_HOST=<the Studio host>`, the tool's own transport flag). Arms: four REFUSE, the red control (`problem_18` ⇒ rc 3, `SLICE_EQ_RISK`), the green control (`problem_0` ⇒ rc 0), a mixed call, and an honesty arm asserting the report never calls an unrefuted problem "clean". The third block records what the seat does with **no** Lean and no `SSH_HOST`: **rc 2, a HARNESS refusal — it declines to report a verdict it did not compute**, which is why `seat_selftests.txt` shows it red there. |
| `preflight12.log` | the pre-flight over the **registered 12**, at the synced sha: `REFUSED: (none)`, CHECK 1 reaching **12/12**, CHECK 2 reaching **5/12** (`0,4,16,31,73`), **7 printed UNREACHED**. *The gate refutes; it does not certify.* |
| `ml_before.txt` · `ml_after.txt` · `morning_line_NOOP_DIFF.txt` | the amendment-12 §3 **no-op proof on the real state** (`~/bench-a8/state`, k=27, `ML_ARMS=a0,a2`): **53 → 56 lines, every stage-A and stage-B line byte-identical**; the whole delta is the header's `c_dead∩D`, 18 moving to `NOT_RUN(view_dead)`, the C denominator 23 → 22, and **three added lines**. |
| `ml_morning_line_BEFORE.py.txt` | the pre-change `s2_morning_line.py`, kept so the red-first claim can be re-driven by anyone: the same selftest against this file flips **6 assertions red** while all 9 frozen arms stay green. |
| `s2controls-run.log` · `s2-controls-NEW.json` | the checker controls **re-run at the current checker: 31/31 PASS** — the 30 frozen plus `C_decide`. ⭐ `C_decide` (the differential sibling of `C_ax`: same problem, same gold implementation and proof, same helper lemma, `by decide` instead of `by native_decide`) returns **PASS** where `C_ax` returns **KERNEL_REJECTED**. That pair is the measured half of the row-AV sentence now in `prompt_C.md`. |
| `controls_gate_differential.txt` | the new gate driven on **both real records**: **REFUSE** on the landed one (naming the `screen.py` drift `aa2c9376…` → `cc591ca6…` *and* the absent `C_decide`), **PASS** on the fresh one. The old one-line predicate passes the record the new gate refuses. |
| `views_setcheck.txt` | the C views on the host verified **by content and by set-hash**: **644/644 files match their `HASHES.txt` pins**, zero mismatches; GT set-hash `cf67a9c0ed805f36` and A-views `bc4d6eafc0430ed2` both **reproduce the banked figures**. |
| `smoke_gate_check.txt` | the driver's **own** smoke predicate, run verbatim at both state roots: PASS, on the LAST verdict per id, carrying the current `episode_s2.sh` sha `cfb8a714…`. |
| `dry_stageC_green.log` | the **run-shaped dry of stage C** at a fresh root: the registered 12, all `DONE`, `S2 STAGE C DRIVER DONE k=27`, exit 0. |
| `dry_stageC_red_cdead.log` | its **red arm**: `ONLY_IDS="problem_18 problem_112 problem_54 problem_73"` ⇒ all three C-dead ids land `SYNTHETIC … NOT_RUN(view_dead)` and only `problem_73` runs. The new `c_dead` entry is a branch the driver takes, not a sentence in a document. |

**No stage-C model call has been made.** The freeze commit is the authorization, and the commission's objection
window runs to 09/02.
