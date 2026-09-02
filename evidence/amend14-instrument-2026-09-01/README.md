# EVIDENCE — amendment 14 (instrument): four repairs, one refuted premise, one registered rider

Zero model tokens. Every number here was measured at an artifact on the Studio or reproduced on the seat.

| file | what it proves |
|---|---|
| `01-s2_morning_line.PRE.py` · `02-check.PRE.py` · `03-s2audit.PRE.lean` | the three pre-change files, so every red control below can be re-driven |
| `04-probe112-matcher-proof.py` | **THE MECHANISM.** Rebuilds `problem_112` stage-B canonical + pristine under the harness's own `sandbox_check.sb` fence (reusing `check.py`'s `render_profile`/`run_fenced`) and prints both modules' constants and both `problem_spec` values' used constants. They differ in **exactly one of 31**: `generated_spec.match_1` vs `problem_spec.match_1`. |
| `05-sweep-trip-condition-239-oleans.py` | the trip condition read at the **Expr level over all 239 landed `canonical.olean`** files: *does `problem_spec`'s value use a matcher it does not own?* ⇒ **1 of 239**, the same episode the recorded `audit.json` sweep found. Two independent measurements, one answer. |
| `06-reread-driver.py` + `10-reread-110-episodes.log` | the 08/31 comparability re-read, driven: **110 stage-B/C episodes across all four state roots, both checkers, FLIPS: 1, ERRORS: 0** — the registered prediction, held on both clauses. |
| `07-morning-line-red-then-green.txt` | `selftest_morning_line.py` at **12 arms**: driven against the PRE-change tool (**5 amendment-14 assertions FLIP, all 4 controls PASS**), then GREEN twice consecutively. |
| `08-HASHES-diff.txt` | the pin delta: **4 files changed, 3 gates added**, and the three `leanproj-*` pins reproduce byte-identically. |
| `09-selftests-scaffold-and-audit.txt` | ⛔ **kept deliberately: the run in which `selftest_scaffold.py` FAILED.** This is the intermittency that led to §6 — it was green when published and red when re-run beside the controls. |
| `11-controls-31of31-clean.log` + `13-s2-controls-amend14-clean.json` | **`CONTROLS PASS (31/31)`** at the amended checker; the record certifying the live checker shas. `B_notation_noscreen` / `C_notation_noscreen` still return `STATEMENT_ALTERED` — the refuter-F3 hijack controls fire exactly as before. |
| `12-controls-28of31-SPECIMEN-of-repair4.log` | ⛔ **THE SPECIMEN, KEPT AND NOT TRUSTED.** The first re-run: `C_pos`/`C_neg`/`C_ax` all `HARNESS` at `audit=0.1 s`, because my own selftests were sweeping the same harness path and killing their audits — §6's defect, caught in the act on the gate itself. |
| `14-gates-red-and-green.txt` | every gate driven RED then GREEN on the live machine: `controls_gate.py` PASS on the fresh record / REFUSE on the stale one naming both drifted files; `selftest_check_concurrency.py` **RED 3/3 (`decoy=KILLED`) · GREEN 3/3 (`decoy=ALIVE`)**; `selftest_scaffold.py` and `selftest_s2audit.py` each PASS twice. |

## The one thing to carry out of here
The routed finding was **measured at a real file with a real sha, and was still wrong**, because the file was
the harness's own composition rather than anything the agent wrote. Nothing downstream could have caught it.
⇒ ***"Verified at the artifact" names a habit, not a guarantee — the question is always which artifact, and
who wrote it.***
