# PROVENANCE — every population, every third-party artifact, its licence and its attribution

Written 2026-09-02 for the v1 publication (PUBLISH-CHECKLIST.md item (c)). Each row names the
source, the exact pin the campaign used, the licence as read at the object on 2026-09-02, what this
repository redistributes from it, and where the source is cited in the record. Where a licence was
read from a secondary record rather than the object, the row says so.

## 1. Task populations

### 1.1 CLEVER (the S2-Lean population)

| field | value |
|---|---|
| source | `trishullab/clever`, https://github.com/trishullab/clever |
| pin | commit `8348039a7ff7730a126d761e71d0439735eeb3e2` (2026-08-26), `HASHES.txt` key `clever-commit` |
| licence | MIT. LICENSE at the pinned commit: "Copyright (c) 2025 Trishul: Trustworthy Intelligent Systems @ UT Austin" (read at the object 2026-09-02) |
| paper | Thakur, Chaudhary, Sosso, Arora, et al., "CLEVER: A Curated Benchmark for Formally Verified Code Generation", arXiv:2505.13938. The flagged-specification list and the four structural exclusions come from Sosso, Arora, Spitters, "Agentic Proving for Program Verification", arXiv:2605.23772, Table 1 and section 4.2 |
| upstream of the upstream | the natural-language docstrings and the test cases derive from OpenAI HumanEval (MIT) |
| redistributed here | `harness/s2lean/views/problem_<k>/{A.lean,C.lean,frozen.json,frozenA.json}` for the 161 problems: the docstring, the human `problem_spec`, the statement headers, the `#test` lines, and the `shipped_generated_spec_body`, re-cut into stage views by `harness/s2lean/build_views.py`. No reference implementation and no reference proof is redistributed. `harness/s2lean/flagged.json` carries the id lists of arXiv:2605.23772. `harness/s2lean/c_dead_unsat.json`, `view_status.json` are this campaign's own derived records |
| attribution in the record | `SCOUT-S2LEAN-STAGE0.md` section 1, `S2-SOURCE-READ-2026-08-29.md`, `AUDIT-FINDING-s2lean-2026-08-29.md` |
| obligation | MIT: keep the copyright notice with the redistributed text. The public README's Acknowledgements section carries it |

### 1.2 VeruSAGE-Bench (the S2-Rust population)

| field | value |
|---|---|
| source | `microsoft/verus-proof-synthesis`, https://github.com/microsoft/verus-proof-synthesis (the VeruSAGE-Bench and Verus-Bench release; lynette lives in the same repository) |
| pin | commit `cbf9c0c6337b224fd8e5b7cb4e01ae65c0f98bc1`; `tasks.jsonl` sha256 `d9b23ed7066ea6a7d782b98d3660f1fee514633b6a3e12b2801c3691f1cf689a`, 58,418,193 bytes (`AMENDMENT-15-s2rust-2026-09-01.md` section 2) |
| licence | MIT. LICENSE at the pinned commit: "Copyright (c) 2024 Microsoft" (read at the object 2026-09-02) |
| paper | the VeruSAGE paper, arXiv:2512.18436 (cited for the 11.8 percent rerun-flip prior in `AMENDMENT-15-s2rust-2026-09-01.md` section 9) |
| upstream of the upstream | the 849 tasks are cut from eight public Verus projects (Anvil, Anvil-Advanced, NRKernel, ATMO, and others named in the benchmark's own table). Their licences are the projects' own and were not re-verified here; nothing from them is redistributed by this repository beyond what item "redistributed here" states |
| redistributed here | nothing of the task text. `harness/s2rust/state/task_dead.json` and `rlimit_curve.json` are this campaign's verdict records keyed by task id (`RESULT-amend15-stage0-2026-09-01.md`). The views (`task.rs`, `frozen.json`, `gt.json`) are REBUILT from the pinned `tasks.jsonl` by `harness/s2rust/build_views_verus.py` and verified by set-hash (`views_sethash.py`); they are not tracked |
| attribution in the record | `AMENDMENT-15-s2rust-2026-09-01.md`, `S2-RUST-SCOUT-2026-09-02.md`, `S2-SOURCE-READ-2026-08-29.md` |
| obligation | MIT: keep the copyright notice wherever the benchmark's text is reproduced. The count guard in `check_verus.py` is a four-line hand port of the benchmark's `proof_completion_code_change_is_safe` rule and says so in place |

### 1.3 SWE-bench Verified (the abandoned S1 substrate; the saturation datum)

| field | value |
|---|---|
| source | `princeton-nlp/SWE-bench_Verified` on the Hugging Face Hub, split `test`, 500 rows |
| pin | dataset repo revision `c104f840cc67f8b6eec6f759ebc8b2693d585d4a`; sha256 over the canonicalised rows recorded in `TASKLIST.json` (`rows_sha256_canonical`) |
| licence | the SWE-bench code repository (`SWE-bench/SWE-bench`) is MIT (read at the object 2026-09-02). The dataset card carries NO licence field (read 2026-09-02). The problem statements are GitHub issue text authored by the issue reporters of the source repositories; the gold patches and tests are code of the source repositories under their licences (next row). This repository treats the issue text as redistributable under the source repository's licence plus the SWE-bench release, and states that this is a reading, not a ruling |
| source repositories of the 30 drawn statements | astropy/astropy BSD-3-Clause · django/django BSD-3-Clause · matplotlib/matplotlib "License agreement for matplotlib versions 1.3.0 and later" (PSF-style, BSD-compatible) · psf/requests Apache-2.0 · pydata/xarray Apache-2.0 · pytest-dev/pytest MIT · scikit-learn/scikit-learn BSD-3-Clause · sphinx-doc/sphinx BSD-2-Clause (GitHub reports NOASSERTION; the file is the two-clause BSD text) · sympy/sympy BSD-3-Clause with derived-code notices. All read at the repositories' current default branch on 2026-09-02, not at the task base commits |
| redistributed here | `harness/data/problem_statements.json` (30 rows: `instance_id`, `repo`, `base_commit`, `version`, `problem_statement`), `TASKLIST.json` (ids only), `IMAGE-DIGESTS.json` (public `swebench/sweb.eval.x86_64.*` image names and digests). `data/verified.json` is the local copy of the dataset and is NOT tracked; it is re-derived from the pinned revision |
| attribution in the record | `PRE-REGISTRATION.md` section 3, `SCOUT-STAGE0.md`, `RESULTS-stage0-2026-08-29.md` |
| obligation | keep the repository attributions with the redistributed issue text (the `repo` field does this per row); the scorer is `swebench` 4.1.0 (MIT), used unmodified through the pinned images |

## 2. Third-party tools the harness pins (not redistributed)

| tool | pin | licence |
|---|---|---|
| Lean 4 | `leanprover/lean4:v4.27.0` | Apache-2.0 |
| mathlib | `a3a10db0e9d66acbebf76c5e6a135066525ac900` | Apache-2.0 |
| Verus | `release/0.2025.09.12.bb1f342` (arm64-macos zip, sha256 `95c5d5a5…6933`), rust channel `1.88.0-aarch64-apple-darwin` | MIT |
| z3 | 4.16.0 as bundled in the Verus release | MIT |
| lynette | from `microsoft/verus-proof-synthesis` at the pin above | MIT |
| swebench | 4.1.0 | MIT |
| Claude Code | 2.1.251 headless, the agent under test; models `claude-sonnet-5`, `claude-opus-5` | proprietary; not redistributed. Transcripts of its runs are the campaign's data (section 3) |

## 3. Model outputs and run records

The run records (`evidence/`, tracked; `runs/`, untracked, 61 MB; the S2-Lean and S2-Rust episode
archives, on the Studio state roots and NOT in this repository) contain the agent's transcripts,
its patches, proofs and specifications, and the referee's verdicts. They are this campaign's
measurements and are released with the paper as data under the data licence proposed in the
public README. Two notes travel with them:

1. Provider terms. The agent is Claude Code on a consumer subscription. Anthropic's published
   terms assign output ownership to the user and do not forbid publication of outputs; this is the
   author's reading of the terms as of 2026-09-02 and the Captain confirms it before the flip
   (PUBLISH-CHECKLIST.md item (d)).
2. Content of the transcripts. The transcripts quote task text (issue text, Lean and Rust source
   from the populations above, under those licences) and agent-written code. They also carry
   absolute paths of the machines the episodes ran on (`/Users/jyh/...`). Those paths identify a
   machine layout, not a private record; they are kept, because rewriting a transcript is an edit
   to a measurement. Zero secrets and zero fleet or seat content were found (item (d)).

## 4. What is NOT in this repository, and where it is

- `data/verified.json` (the SWE-bench Verified rows): re-derive from the pinned revision.
- `runs/` (the S1 stage-0 and audit archives): released as a data asset beside the repository,
  not in the git tree.
- The S2-Lean episode archives (`~/bench*/state/` on the Studio: `task.lean`, `bodies.json`,
  `canonical.lean`, `check.json`, `audit.json`, `session.jsonl`, `manifest.json` per episode) and
  the S2-Rust archives (`~/bench-rust/`): the bench seat owns them; they are pulled into the data
  asset before the flip. The paper's numbers are read from the RESULT files, which were computed
  from these archives by the pinned morning-line instruments.
- The refuter reports and the commissions this record cites by name live in the private record
  and are not published; the record cites them where it always did (PUBLISH-CHECKLIST.md item (b)
  explains why those citations stay).
