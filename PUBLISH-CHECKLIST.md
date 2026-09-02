# PUBLISH-CHECKLIST — v1 hygiene and provenance, DRIVEN 2026-09-02 (seat `paper`); REPAIRED the same day after the flip package's refuter pass (section (f))

Commission: the v1 writing head's boot brief (council 2026-09-02, minute sections 0, 2 and 3.1).
IARC approval covers arXiv, GitHub and data. This file records each item's verdict as measured,
the command that measured it, and what remains for the Captain's hand. Items are lettered as the
brief lettered them. Nothing here is an intention; every verdict was produced by running the gate
named beside it, on this tree, on this date.

## (a) The session trailer in history — FINDING: there is none; NO REWRITE

The brief expected one session trailer among 90 commits. Measured:

```
git log --format=%B | grep -c 'Claude-Session'          -> 1
git log --format=%B | grep -cE '^Claude-Session: '      -> 0
```

The single match is the sentence "Claude-Session trailers are banned here from the start" in the
body of commit `2ef7505` (the wave-1 pre-registration, 2026-08-27). It is prose stating the rule,
not a trailer, and the fleet's gate is built to pass exactly that shape (`check_commit_trailers.py`
self-test arm 4, "a message describing the rule must not trip it").

Verdict: **no trailer exists, no rewrite is performed.** A rewrite would also have been the wrong
tool for this repository regardless of the count: the frozen record pins commit shas everywhere
(`harness/FREEZE-COMMIT` on the Studio, `HASHES.txt`, every episode manifest's freeze commit, and
the RESULT files' "THIS COMMIT IS THE AUTHORIZATION" lines such as `8de0b74`, `2219c23`,
`15cfdc2`). Rewriting history would orphan every one of those citations. The repository's
zero-remote status makes a rewrite technically safe and semantically destructive.

## (b) The Scrub gates, ported and driven — GREEN; tree residue 0 after section (f); 3 historical messages baselined and HELD

Ported byte-identical from `salt` (which carries the jas port): `scripts/check_commit_trailers.py`,
`scripts/check_private_paths.py` (gate id `819d4ebd77620b0d` at the port; `04ad5a4385236cac` after adopting salt's 2026-09-02 fleet sync, which adds the `safe_gif` root), `scripts/check_pr_descriptions.py`,
`.githooks/commit-msg`, and `.github/workflows/scrub.yml` with a saltbench header. The hook is
armed in this checkout (`git config core.hooksPath .githooks`) and was driven red and green.

| gate | command | verdict |
|---|---|---|
| trailer self-test | `python3 scripts/check_commit_trailers.py --self-test` | OK |
| trailer, full history and tree | `python3 scripts/check_commit_trailers.py` | OK: 94 commit messages and 1039 tracked files, 0 forbidden strings (re-run after (f)) |
| private-paths self-test | `python3 scripts/check_private_paths.py --self-test` | OK (16 planted shapes caught, 16 compliant forms passed) |
| private-paths, tree ratchet | `--tree` | first run: 13 residue lines in 8 files, all baselined. After (f): **0 residue lines, 0 baseline entries** |
| private-paths, message ratchet | `--messages` | 3 historical commits baselined, 0 new |
| private-paths, full delta | `--range <root>..HEAD` | fires on the historical commits that ADDED the 13 lines and the 3 messages, nothing else; history is not rewritten, so this range reads the same after (f). The CI scans each push's delta, and the tree ratchet reads the tree |
| infra names (host, account) | `python3 scripts/check_infra_names.py --self-test`, then the tree scan | OK: 5 planted forms caught, role words pass; tree 1039 files, 0 occurrences (was 41 in 21 files, section (f)) |
| PR-description self-test | `python3 scripts/check_pr_descriptions.py --self-test` | OK |
| commit-msg hook | a planted trailer line, then a Co-Authored-By line | rc 1, then rc 0 (re-driven after (f)) |

The 13 tree lines and 3 messages all cite the private record by path, in the frozen protocol
documents (`PRE-REGISTRATION.md`, `SCOUT-STAGE0.md`, `SCOUT-S2LEAN-STAGE0.md`,
`AMENDMENT-15-s2rust-2026-09-01.md`), in `README.md`, `CLAUDE.md`, `.gitignore`, and one line of
`harness/s2rust/gt_leak_check.py`. The first pass ACCEPTED them into the two baselines. The refuter
pass on the flip package refuted that for the tree: a regression ratchet's accepted residue is not a
publication clearance. Section (f) records what was done instead: the three non-frozen lines were
removed by the flip commit; the nine frozen-document lines were REWRITTEN to role wording with the
private sha dropped (the remedy salt uses: "the fleet's delegation brief", "the bench seat's boot
brief"); the fixture's comment text was changed. The tree baseline is now empty and `--tree` reads
0. The 3 commit MESSAGES stay in `scripts/private_paths_message_baseline.tsv`: a pre-flip history
rewrite is lawful here (no public remote exists) and is HELD for the Captain, because it would
re-sha every commit the private record cites.

Fleet item, closed the same day: the gate's employer-lane root list predated the `safe_gif` seat. The
helm synced the gate across the public repos on 2026-09-02 and this repository adopted salt's
`origin/main` copy (the only difference: the fifth root). Measured here: zero occurrences of any
employer-lane name in the tree or history.

## (c) Provenance of every population — WRITTEN, `PROVENANCE.md`

Every source, its pin, its licence as read at the object on 2026-09-02, and what this repository
redistributes from it. Summary:

| population | source and pin | licence | redistributed here |
|---|---|---|---|
| S2-Lean | CLEVER `trishullab/clever@8348039` | MIT (UT Austin 2025) | the 161 problems' docstrings, human specs, statement headers and tests, as stage views |
| S2-Rust | VeruSAGE-Bench `microsoft/verus-proof-synthesis@cbf9c0c6` | MIT (Microsoft 2024) | nothing of the task text; verdict records keyed by id |
| S1 | SWE-bench Verified, HF revision `c104f840` | code repo MIT; dataset card has no licence field; issue text under the nine source repositories' licences (BSD-3, BSD-2, Apache-2.0, MIT, matplotlib's PSF-style) | 30 problem statements, the id list, the image digests |

~~Open for the Captain~~ — RULED 2026-09-02, section (k) ruling 3: the SWE-bench Verified dataset
card states no licence, so the reading is not relied on and the 30 statements are DROPPED from the
public tree. `harness/data/problem_statements.json` is untracked and gitignored; the ids, the pinned
revision and two checksums stay, and `harness/fetch_problem_statements.py` rebuilds the projection
and verifies it against the pin. The rebuild was measured byte-identical to the dropped file before
it was removed, so the cost to reproducibility is zero.

## (d) Secrets, private paths, transcripts — CLEAN; provider-terms note written

| scan | scope | result |
|---|---|---|
| `git grep -I -n -E 'sk-ant-|AKIA[0-9A-Z]{12}|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20}|xox[bp]-[0-9]'` | tracked tree | 0 |
| the same pattern with `grep -rlE` | `runs/` (61 MB, untracked) and `data/` | 0 files |
| `FLEET.md`, the seat repo path, the kit path, session URLs | `runs/` (untracked) | 0 files |
| the same class, re-scoped to the WHOLE tracked tree after the refuter pass (a case-insensitive grep for the bus file's name, the seat repository's path, the kit path under the Documents folder, session URLs, the memory-mirror directory, the seat loop and the bus tool's name; spelled in words here because the gate reads a literal pattern as an instance) | tracked | 6 lines, no path: the hook's own refusal text, the gate's own fixture, this table's row, two docstring mentions of a fleet tool's name (`harness/s2lean/bc_gate.py:14` and its evidence copy), one mention of the bus file's name (`SCOUT-S2LEAN-STAGE0.md:1785`). The three name mentions are fleet VOCABULARY, held with the vocabulary item below |
| the run host's and the subscription account's names | tracked | 41 occurrences in 21 files, all replaced by role words and GATED (`scripts/check_infra_names.py`, section (f)); one commit body in history still names the host (history, held with the messages) |
| absolute home paths (`/Users/jyh`) | tracked | 127 files (103 under `evidence/`, 17 under `harness/`, 7 documents) |
| absolute home paths | `runs/` | 292 files |

Home paths reveal a machine layout and nothing else. The private-paths gate declares them out of
scope by ruling (its own header: "absolute paths into PUBLIC repos ... DECLARED, therefore, and
left alone"). They are KEPT in transcripts and manifests, because a transcript is a measurement
and an edited transcript is a different object. In the harness scripts they are defaults and
comments; they are left as they are for v1 and listed for a v2 tidy.

Keep / strip decisions per artifact:

| artifact | decision | why |
|---|---|---|
| `evidence/` (tracked, 3.1 MB) | KEEP in the public tree | the morning-line outputs, manifests and probes the RESULT files cite |
| `runs/` (untracked, 61 MB: S1 stage-0 transcripts, audit runs, Studio controls and scoring) | KEEP, in the data asset (DOI assigned at release, Zenodo, recorded here on the flip day) | 61 MB of jsonl belongs in a release asset; nothing in it is private |
| `data/verified.json` (untracked, 7.7 MB) | STRIP (stays untracked) | a copy of a third-party dataset; re-derived from the pinned revision |
| the S2-Lean and S2-Rust episode archives on the Studio (278 + 16 episode dirs, inventoried in `PROVENANCE.md` section 4) | OWED to the data asset: INVENTORIED, NOT YET SCRUBBED, NOT A REPO ARTIFACT; the flip does not wait on them | a `session.jsonl` carries host paths, session ids and the agent's reasoning; it needs its own content scrub gate and a non-git channel before release |
| `harness/s2rust/views/` | not tracked, rebuilt from the pin | contains the benchmark's task text and ground truth |

Provider terms: CONFIRMED 2026-09-02, section (k) ruling 2. `PROVENANCE.md` section 3 now cites both
documents at the version read — the Consumer Terms effective 2025-10-08 (section 4: Outputs are the
user's; publication is not forbidden) and the Usage Policy dated 2025-09-15 (the no-training clause
binds the subscriber, not a downloader).

## (e) The flip — PREPARED on branch `public-v1`, NOT MERGED

Prepared on a separate worktree so the shared checkout on `master` (bench commits into it) is never
switched. The branch carries: the public README (the PRIVATE banner replaced; a real command block since (f)), `LICENSE` (proposal:
Apache-2.0 for code, marked PROPOSAL in the file itself since (f)) and `LICENSE-DATA` (proposal: CC-BY-4.0 for data and documents), a
`CITATION.cff` (its licence field held as a comment until the choice is made), a public `CLAUDE.md` replacing the seat instructions, the `.gitignore` comment
cleaned, the baselines regenerated (the three removed lines shrink the tree baseline to 10), and
the scrub CI armed. ~~The licence choice is the Captain's; the branch says "proposal" in both
files until he chooses.~~ RULED 2026-09-02, section (k) ruling 1: Apache-2.0 for the code, CC BY 4.0
for the data and documents. Both files now state the choice, and `CITATION.cff` carries both SPDX
ids. The branch sha is in the READY post on the bus.

**The flip shape, ruled 2026-09-02 (section (k) ruling 6).** `public-v1` becomes the public `main`,
and `master` is then fast-forwarded onto it. This is lawful precisely because `public-v1` is
`master` plus its own commits and nothing behind it — `git rev-list --left-right --count
master...public-v1` reads `0 N`. One gated branch results, as in the sibling repository. ⛔ The
consequence a later hand must not undo: **the public history is `public-v1`'s, never `master`'s.**
`master` carries the private-vocabulary lines and the infrastructure names that the flip layer
removed, so merging `master` into a public `main` would publish exactly what the gates were built to
stop. Fast-forward `master` onto the flipped branch; never the reverse.

Not done by this seat, by construction: creating the public GitHub repository, pushing, and the
arXiv submission. The helm carries the READY post to the Captain.

## What the flip still needs from others

1. ~~The Captain: the licence choice; confirmation of the provider-terms reading; the SWE-bench issue
   text decision.~~ ALL THREE RULED 2026-09-02 — section (k).
2. bench: the S2 episode archives pulled into the data asset; the DT Sonnet two-tier read if it
   lands before the flip (the paper carries a slot for it, section 6).
3. The helm: the fleet-level note that the private-paths gate's root list predates `safe_gif`.
4. ~~The Captain, HELD by the refuter pass~~ — BOTH RULED 2026-09-02, section (k) rulings 4 and 5:
   (i) the 3 commit messages and the 1 commit body are ACCEPTED as they stand, no rewrite; (ii) the
   fleet vocabulary is ACCEPTED, with a glossary added to the public README.
5. The data asset's channel (Zenodo proposed) and its transcript scrub gate, before the archives ship.

## (f) Repairs after the refuter pass on the flip package (2026-09-02, the same day)

The refuter verified the science and the gates and refuted the flip layer. Six repairs needed no
ruling and were made on `public-v1`, each driven:

1. `paper/saltbench-v1.tex`, the stage-C population sentence: it read "18 ids" for the views that fail
   to elaborate. That 18 is the count over all 161 problems and collides with problem 18's id. The
   registered derivation (`AMENDMENT-11-stageC-2026-09-01.md` section 2) is U15 minus the two
   c-dead views (problems 54 and 112) minus problem 18 (unsatisfiable by theorem) = 12. Rewritten;
   every other population sentence re-read against its source. PDF rebuilt (10 pages).
2. `LICENSE` carried no proposal marking and `CITATION.cff` asserted Apache-2.0 outright. `LICENSE`
   now opens with the PROPOSAL paragraph (the licence text below it unchanged); the cff `license`
   field is a comment until the owner chooses.
3. The nine private-record paths in frozen documents rewritten to role wording, the private sha
   dropped; the fixture comment in `gt_leak_check.py` reworded (its self-test: 7 arms, 0 failed).
   The tree baseline is empty; `--tree` reads 0.
4. The run host's and the subscription account's names (41 occurrences, 21 files: frozen documents,
   evidence READMEs, one evidence listing's headers, and the `STUDIO` default of seven harness
   scripts) replaced by role words: "the Studio", "the bench account", the ssh alias `studio`
   (`STUDIO` stays an environment variable; a rerun sets it). Gated by `scripts/check_infra_names.py`
   (self-test first; wired into `scrub.yml` as the `infra-names` job).
5. `README.md`: a real command block (pin verification, both view builders, the three drivers, the
   two morning lines), and ONE locator sentence for the data asset, used identically in the README,
   `PROVENANCE.md` and the paper: DOI assigned at release (Zenodo), recorded here on the flip day.
6. Item (d)'s seat-path scan was scoped to `runs/` and `evidence/`, away from the documents where the
   answer lived; re-scoped to the whole tracked tree and re-run (row above).

Also carried onto the branch by rebasing it onto `master` `b692514`: the relocation of
`at_first_rc0.py` out of the fenced `harness/s2rust/` set, so the flip does not ship an unpinned
file in a directory the episode driver refuses on.

### The byte changes to frozen and pinned files (the shamap)

Frozen documents are appended to, never edited; this pass edited them, on the refuter's finding and
the helm's word, and only in the citations named above (no number, no result, no protocol text
changed). Every file whose bytes changed is listed with its sha256 before and after, so a citation
in the private record that names a byte hash can be mapped. The eight harness files are re-pinned in
`harness/HASHES.txt` by the same formula `hashes.sh` uses (sha256 of the file); the other 87 file
pins verified unchanged (`shasum -a 256 -c` over the table, 95 OK). The frozen run record's
manifests recorded the OLD hashes of these eight files at run time; the map below is how a reader
reconciles them.

| file | sha256 before | sha256 after |
|---|---|---|
| `AMENDMENT-11-stageC-2026-09-01.md` | `c2dee901a436fa11ad67ba8bf28005db5295a1f1895b8ae10a97970a23bd2be1` | `90cf20251653fedbd1a16798a8eda7919d1ec09608bdfbf272a0d5c80ae327f4` |
| `AMENDMENT-13-AW-2026-09-01.md` | `baeb28c5ac50ee1d8a9f310f0fb97ac4cb6b8cad838cf7b1bfae88579409a9c4` | `9c275119d3a1ea3e2a955b3e8387dc050dc24288696d2fc861c92cc13c492f7e` |
| `AMENDMENT-15-s2rust-2026-09-01.md` | `bd76beac4b2767b6fda0db9d2704bb19958747d8836cfd31da586dcf3d10a9bf` | `f04e4baddb77fae4ba80cce29392ea0ff0bf81a5bb73b47b38be542f4a14af65` |
| `DIAGNOSIS-replay-vs-axioms-2026-08-31.md` | `7b935416bdf08aeac8e825a517b018e1c31d8850ec059a639a62f3be105b744b` | `1a868c9170c6cf17f81415a1f5b1b8370234641815e4c1e6f680b4503b0bffc6` |
| `PRE-REGISTRATION.md` | `b6bc1dd61a03af177aa27afc2c8c4f58fd18d31d77124715a0a3e7118c097226` | `fcf6c2f461a9beeb2f8babff87acc5e3843e6fc9c4d053f2a761335f88129aec` |
| `RESULTS-stage0-2026-08-29.md` | `ef163aafbb9d74c12b8406c41c0cede223c3a930906dbd4cde96e90b000dde51` | `375a4b8dcd26b5323b613f1e24d7dbf1cf6cd2d37ace9f8465a6277b0c349c9b` |
| `S2-RUST-SCOUT-2026-09-02.md` | `63e8fbb901c6d64a376ba3a6afba559f84a2c2b28d67571a3aa879ff1701b01a` | `7ffffa2bc56914e46369ba085a8785fc0f676b72a6b4b40faf69c3d96ad5bfbb` |
| `SCOUT-S2LEAN-STAGE0.md` | `0676037c7912aac55e23651048ad9d026083a4c2bc8b23ae8f8df2f1d7e08efb` | `01afb719b69ceaa2f6772b4a691a330194da23d03f9914e0884071a323e266e8` |
| `SCOUT-STAGE0.md` | `a1eb5785d5fdd140bb8951a27dce0cb68e3ccd9bb714a6c71a682d90b9f6af62` | `9d2a00ade4c74123c47138013f8c20875a346648d36b339214f49913d4cd9649` |
| `TRIAGE-B-failures-2026-09-01.md` | `f243adcf7842f76ceb246c260b4ec64e5e229478a2a97d3b4019af1038e834e2` | `8ca99ec1cb17f42cb6a2fe53ec2123cfd4037b3e0620e026254abbfc7e6ef011` |
| `evidence/amend11-12-freeze-2026-09-01/README.md` | `2bd8186ef65c13f9c2b485cac6a14b54a1c779106f8abab48ad838129d5a9e64` | `74030912f0bc6baa784703541330c6eac9b72f26cf99f80b9d427c42411c630c` |
| `evidence/amend11-stageC-step1-2026-09-01/README.md` | `be63eae645b9a5e221675903c8772a04503bc54828f1c55f2f91cb507c53de35` | `6b88c1497053effd1e8d32d4a4cdf251e14a3b94c773fdf0015a75c713f6ccb4` |
| `evidence/amend13-AW-2026-09-02/README.md` | `b7c9845a8ca35d62dccfc512b96b08c2675b1efda59efa749bb4b273151d8baf` | `41dbc08ec0243e73a380ab1c41368ca3441ea0c8af594b700dbd2b67382a9f0c` |
| `evidence/amend14-instrument-2026-09-01/README.md` | `ae1682cfeca8cf9b336f8581f0678b25d07f00c04e5af9d6651043fbef2ad037` | `afdd3d96210f713ee114c3404a176aaacff0cad8b8fb65476f2bdc8e8bf79987` |
| `evidence/rowAB-replay-diagnosis-2026-08-31/05-the-sweep-scripts.txt` | `0247ce2579cf4e60dc7dd94474606d89a400bb23f4d19e6eb06e420e83a696f7` | `2cd8190122c0d1748b8847075f5e11fac7888928ddb30783e6447c63d1fe850c` |
| `harness/s2lean/c_oracle_preflight.py` | `07daa08fb418240818954b66d42b542227c071f571e637b0606a0419871df037` | `75407c6173e4508434ea2a15572a28f955cb1fe16dc26ec1cbd67230d6fb7851` |
| `harness/s2lean/run_s2_stage0.sh` | `1849c8ac227ef8744dc9a8331a8982dde683259e71bd51df48f7e9ea89116d6b` | `636d4a3e6924dddbf2cc26ff2c89e75adf031f2d4858fb55e0a07d5fa39636ee` |
| `harness/s2lean/stage_views.sh` | `a99fabf4b5010ca1434d71f0e4c84bf42ac254f3479dbf4f4cdc07998a6d3c74` | `904a5a31dcbf2592acf50ba10616d7112355ca6c6d4361673ffa2348f39d823b` |
| `harness/s2rust/provision_studio.sh` | `49ddf37d001118df4b6da0c494033609be219ec5ebbfa454dcc418c89ed75d07` | `0dfe02ca109a0b8613fe0d2fdf0fa1796f29487d4807ba4cec1dcd3077365cc5` |
| `harness/s2rust/sync_studio_s2rust.sh` | `7512a0a71c560d66813ccb16b9e1c1053de6491baa6e9d8001eec789c7314220` | `576777e83c8a493f85efa90955ecab36716419b596e937be1dea290dd9574c8e` |
| `harness/studio_phase.sh` | `e6e22e17aa9cd8d78de654fcfffeae0c9679b7a4eb120aaca7704d59d6569cf6` | `9ff553e3f9123b8ebcf909c3d1f8597f1f67f199d6401be9668574681d6681ad` |
| `harness/sync_studio.sh` | `12ff2709b366fa662f97a151ec9ea9ebfba1df3ef9a2a7a6bd1ee30ef911bc23` | `db3dc160b3c67d64cee05608df2f994a71655faa328b246bf5a10725efe61f89` |
| `harness/s2rust/gt_leak_check.py` | `ae9eb3ed38f3ae3a75b6dd8b01229cd37e620305598f38852a93cdca4ef73b39` | `955abe8a5d2f688112619ff7cf0c51d6bdaac8f7056943280498026a3fe5dd80` |

`harness/s2rust-analysis/dt_quote.py` (not pinned; two occurrences) changed too and is not in the
map. The commit shas of the frozen record are untouched: no history was rewritten.

## (g) Repairs after the paper's refuter pass (the numbers against the frozen record, 2026-09-02)

The second refuter traced about 45 numeric claims in the paper to the frozen record: all but one
verified, no treatment effect claimed, voice clean. Thirteen repairs were ordered and all were made on
`public-v1`:

1. The stage-C population sentence (the same defect as (f).1; the two ids removed from U15 are 54 and 112).
2. `PROVENANCE.md`: z3 is 4.12.5 as bundled in the Verus release (`HASHES.txt` key `z3-version`), not 4.16.0.
3. The claim that the private-paths gate ships byte-identical to three repositories was FALSE (saltworks
   and jas had drifted) and is struck; the helm synced the three on 2026-09-02 and this repository adopted
   salt's synced copy (gate id `04ad5a4385236cac`, the `safe_gif` root added).
4. The branch rebased past `master` `b692514` so the flip does not ship `at_first_rc0.py` unpinned inside the
   fenced `harness/s2rust/`; the paper's citation re-pointed to `harness/s2rust-analysis/`.
5. The 2.2 to 2.8 re-timing figure is sourced to `harness/s2rust/difficulty_band.py`'s header, where it lives.
6. The triage body now reads 31 cells as 30 triageable plus one outside the taxonomy, as Appendix B does.
7. The pilot's 3 of 3 is disclosed at the figure as a re-score: the landing file still reads the grader's
   refusal (`RESULT-amend16-driver-2026-09-02.md` sections 4c and 5).
8. Appendix C carries the lower-bound sentence for the 9 PASS (the failure at 40 of 40 one obligation
   short; p90 of the passing call counts 39 against a cap of 40; one pass at exactly 40).
9. The SWE-bench 13 of 15 carries its cap-bound caveat in the abstract and the body (both failures at the
   40-call cap; cap-bound episodes 3 and 2), and the abstract names the contamination finding.
10. The 0 of 9 flagged contrast is stated at its own cap (40) against the 8 of 15 at 100.
11. Source comments added to the stage-0 setup sentence and to the failure-surface paragraph.
12. The fourth triage label, HUMAN-BUGGY, is named with its count (0) and why it is unreachable on U15.
13. The receipts re-recorded at the tip, below.

Receipts, measured on the tree of the second repair commit before it was committed (that commit adds one
message and no file):

| gate | verdict |
|---|---|
| `check_commit_trailers.py --self-test`, then full | OK; 95 commit messages and 1040 tracked files, 0 forbidden strings |
| `check_private_paths.py --self-test` (gate `04ad5a4385236cac`) | OK |
| `check_private_paths.py --tree` | 0 residue lines, 0 baseline entries |
| `check_private_paths.py --messages` | 95 messages, 3 accepted historical commits, 0 new |
| `check_pr_descriptions.py --self-test` | OK |
| `check_infra_names.py --self-test`, then the tree | OK; 1040 tracked text files, 0 occurrences |
| the pin table against the tree | 95 file pins, all OK |
| `.githooks/commit-msg`, planted trailer then clean | rc 1, then rc 0 |
| `paper/saltbench-v1.pdf` | rebuilt with tectonic, 10 pages |

## (h) The hermeticity claim, corrected after amendment 17 (2026-09-02, the same day)

bench's amendment 17 and its same-day addendum (section 9) found, by a canary driven on the run
host in both arms, that the sandbox's read denials bind sandboxed subprocesses only. The agent
harness's own file-reading tool never enters that sandbox, and neither substrate's settings carried
a tool-permission rule, so no scored episode of this campaign had the agent's tools fenced by path.
The paper's fence section had said "reads denied on the harness state, the credential trees, and
the run root" of the agent as a whole. The helm carried the finding to this seat at 09:24.

What changed, and only this:

| where | change |
|---|---|
| `paper/saltbench-v1.tex` abstract | one clause added to the instrument-findings sentence: a fence probed only in its sandbox's language cannot see the layer above it, and no scored episode had the agent's own file tool fenced by path |
| `paper/saltbench-v1.tex` section 2, the fence | the first sentence now says the agent's SUBPROCESSES run under the sandbox; the hook is named as a shell-tool hook and the audit layer is named; a third paragraph states the finding, what did hold (subprocess sandbox, empty network allowlist, shell-tool hook, ground-truth leak check, audit layer), the S2-Rust read's audit (15 Opus episodes, none voided, no unblocked read of a fenced path, one shell attempt blocked), the one observed escape (a Sonnet episode of the in-flight probe, void), the S2-Lean scope (layer absent; no audit summary in a result file, nothing claimed), and the repair with its canary in both arms; source `AMENDMENT-17-fence-config-dir-2026-09-02.md` sections 2 and 9 |
| `paper/saltbench-v1.tex` section 5, the instrument findings | one item added: a deny list is only as broad as the layer that enforces it; a probe has to speak every tool's language and has to be neutral, because a refusal by the subject is not a refusal by the instrument |
| `README.md` item 2 of the protocol | two sentences added stating the v1 probes' scope and pointing at amendment 17 |
| the branch | `public-v1` rebased past master `88b4610` (amendments 17 and its addendum, the two-layer fence, arms 26 to 29) so the flip carries the finding and the repair; one adjacent-line conflict in `harness/HASHES.txt` resolved by taking this branch's re-pin of `provision_studio.sh` and master's re-pin of `render_settings_verus.py`; every gate re-run green at the tip |

No number in the paper moved. The S2-Rust hard band stays 9 of 10; the S2-Lean null stays 8 of 15 on
every arm. The S2-Lean episodes' per-episode audit counts (unblocked reads of a fenced path through the
file tool) are OWED by the archive owner before any sentence stronger than "the layer was absent" can be
written about them; asked on the bus with this pass.

## (i) The lower-tier row, written once from the landed result files (2026-09-02, the same day)

The paper's section 6 had held a slot for a two-tier read that was in flight. The read was withdrawn
and the withdrawal is itself the result, so the slot is now filled from two files in this tree rather
than left as a promise. Numbers copied from those files' verbatim tool-output blocks; none retyped
from a message.

| where | change | source |
|---|---|---|
| `paper/saltbench-v1.tex` section 6 item 1 | rewritten: the paired three-task quote at a 40-call cap (aggregate paired token ratio 1.55, per-episode median 2.06, lower tier at 0.71 of the higher tier's per-episode quota, 0 of 3 passing against 2 of 3, all three at the cap), then one episode at a 120-call cap as a three-line table (opus 40/23/957,722/307/9 verified; sonnet 40/40/3,051,144/768/0 verified; sonnet 120/79/8,375,623/1071/10 verified), the clean-gate list for the pass, the withdrawal of the 13-id read at 40 calls, and the read at 120 priced as a lower bound at roughly 218 million tokens for 26 episodes | `RESULT-DT-sonnet-probe-2026-09-02.md`, the `dt_quote.py` block and the appended 120-turn amendment |
| `paper/saltbench-v1.tex` section 4.4, the cap caveat | one sentence: the cap cutting an episode that would otherwise have passed is now evidenced directly, not inferred from the shoulder | same |
| `paper/saltbench-v1.tex` section 5, instrument finding 1 | extended: recording the censored state does not rescue the estimate on its own, because under a verifier an obligation is discharged or it is not, so a partial count is a distance and a zero count is an absent measurement | same |
| `paper/saltbench-v1.tex` section 2, the fence | the void escape episode is no longer described as belonging to a probe "still in flight"; it points at section 6 | same |
| `paper/saltbench-v1.tex` section 6 item 3 | the conditional second version-2 population resolved: the scout returned no (5 of 113 tasks are Rust, below the registered threshold of 8 before any screening; 0 of the 5 survived the screen) | `RESULT-DY-deepswe-scout-2026-09-02.md` sections 3, 4 and 5 |
| `README.md` index | the amendment row extended to 17; the two new result files listed | the tree |
| the branch | `public-v1` rebased past master `78c6e3a` (the DT quote, the DY scout, the 120-turn discriminator), no conflict | `git rebase` |

No number already in the paper moved. The S2-Rust hard band stays 9 of 10; the S2-Lean null stays
8 of 15 on every arm.

NOT taken into the paper, and named so the omission is deliberate rather than an oversight: the DY
result file also carries a third party's published figures for the two tiers on its own 113 tasks.
Those are someone else's measurement on a population this benchmark does not run, and quoting them
beside our own would blur the line the whole protocol is built on.

The two-tier comparison itself remains OPEN and is a version-2 question. A read at a 120-call cap is
a spend the owner decides, not this seat.

## (j) The escape sentence corrected and the campaign-wide audit taken in (2026-09-02, the same day)

Master moved again while section (i) was being written. Amendment 17's section 11, appended not edited
in, retracts the evidence sentence of its own sections 1 and 9 and supplies the S2-Lean audit sum this
checklist's section (h) recorded as OWED. Both go in.

| where | change | source |
|---|---|---|
| `paper/saltbench-v1.tex` section 2, the fence | the void probe episode is no longer described as having READ a file under its configuration directory. Read at the transcript the call returned that the file did not exist; the audit field had recorded only that the call was not blocked. The episode stays void and unscorable. The paragraph now carries the campaign-wide audit in its place: 278 landed Lean episodes with a transcript, 278 parsed, zero file-tool calls at a fenced path either served or not served; the detector driven on all three branches; and the limit stated, that this measures what the agents did and not what they could have done | `AMENDMENT-17-fence-config-dir-2026-09-02.md` section 11; `harness/s2rust-analysis/s2lean_escape_audit.py` |
| `paper/saltbench-v1.tex` section 5, instrument finding 6 | extended: the audit built to find the hole carried the same shape of defect as the probe. A field that records "not blocked" conflates a denial, an absent file and a served read, and it reported as an escape a read that had returned no bytes | same |
| `README.md` item 2 | the audit sum added, with its limit | same |
| `paper/saltbench-v1.tex` abstract | one clause: the instrument-findings sentence named the hole without its measured exploitation, which reads as a stronger defect than the record supports; it now carries the 278-episode zero | same |
| the branch | `public-v1` rebased past master `8cbe46f`, no conflict | `git rebase` |

This closes the item section (h) left open. Nothing stronger than the audit is claimed: the gap was
open, its measured exploitation is zero, and an absence of exploitation is not a presence of protection.

## (k) The owner's six rulings on the flip, applied (2026-09-02, the same day)

Every open question this checklist had held for the repository owner was ruled at a sitting on
2026-09-02, one by one. What follows is each ruling and what was done under it. Nothing here changes
a number, a protocol text or a result; ruling 3 removes a file from the tree and rulings 1, 2, 5 and
6 are documentation.

| # | ruling | applied |
|---|---|---|
| 1 | Licence: **Apache-2.0 for the code, CC BY 4.0 for the data and documents.** Accepted as proposed | `LICENSE` and `LICENSE-DATA` state the choice instead of marking a proposal; `CITATION.cff` sets `license: [Apache-2.0, CC-BY-4.0]`; the README's Licence section and `PROVENANCE.md` section 3 drop the word "proposed" |
| 2 | Provider terms: the reading is **confirmed**, checked live against the documents; cite both at the version read | `PROVENANCE.md` section 3 item 1 rewritten: Consumer Terms **effective 2025-10-08** section 4 (Outputs are the user's; publication not forbidden) and the Usage Policy **dated 2025-09-15** (the no-training clause binds the subscriber, not a downloader). Both are revised in place upstream, which is why the version is cited and not just the URL |
| 3 | The 30 SWE-bench issue texts: **dropped**. Keep the ids, the pinned revision and a fetch script; re-addable by one commit | `harness/data/problem_statements.json` removed from the tree and gitignored; `harness/fetch_problem_statements.py` added (self-test 13 arms, all green) which rebuilds the projection from the pinned revision `c104f840cc67f8b6eec6f759ebc8b2693d585d4a` and verifies it against `rows_sha256_canonical` in `TASKLIST.json` and the `problem_statements.json` pin in `harness/HASHES.txt`. `PROVENANCE.md` section 1.3 and section 4, the README's Licence and Reproducing sections, and item (c) above all updated |
| 4 | The 3 commit messages carrying private paths and the 1 body naming the run host: **accepted, no rewrite** | Nothing done, deliberately. They stay in the baseline `scripts/check_private_paths.py --messages` accepts (3 accepted historical, 0 new). A rewrite would re-sha roughly a hundred commits that the frozen record cites by hash, for filenames that name no third party |
| 5 | The fleet vocabulary in the frozen documents: **accepted**, with a README glossary | The README gains "A glossary for the record's vocabulary": Captain, helm, seat, bus, council, desk row, refuter, commission, Studio, morning line, fleet. It says plainly that none of it is a technical term of the benchmark and that the frozen documents keep it because frozen documents are appended to, never edited |
| 6 | Flip shape: **`public-v1` becomes the public `main`; `master` is then fast-forwarded onto it** | Recorded in item (e) above, with the direction stated as a prohibition — the public history is `public-v1`'s and never `master`'s, because `master` still carries the vocabulary lines and infrastructure names the flip layer removed |

### The one thing worth checking twice

Ruling 3 is the only one that removes bytes, so it was driven rather than asserted. Before the file
was deleted, `fetch_problem_statements.py` was run against a local copy of the 500 pinned rows and
its output compared to the tracked file with `cmp`: **byte-identical**, and green against both
checksums. The claim "re-addable by one commit at zero cost to reproducibility" is therefore
measured, not argued. The two pins that make it verifiable are already in the public tree and were
not regenerated: `harness/HASHES.txt` keeps the `problem_statements.json` line and the 30
`prompt-canonical <id> <sha>` lines, which are value pins and do not depend on the file's presence.

`harness/fetch_problem_statements.py` is deliberately NOT in `harness/hashes.sh`'s pin list and says
so in its own header. It was written after every episode had run; pinning it would dress a
publication convenience as run-time apparatus.

One consequence of the drop is named rather than left to be discovered. `harness/build_prompt.py`'s
self-test asserts that the projection holds exactly the five fields, and that arm is guarded by a
file-existence test: with the file absent the arm does not run and the self-test still prints
`SELF-TEST OK`, one check lighter. It was driven in that state and is green. The assertion itself
did not go away; it is in `fetch_problem_statements.py`'s `project()`, which refuses a row carrying
a sixth field and refuses a pilot id the rows do not supply, so it now fires when the file is BUILT
instead of only when a copy happens to be present. `build_prompt.py` is pinned and was deliberately
not edited: adding a printed "skipped" line would change bytes that the frozen run manifests
recorded, which is a worse trade than writing this paragraph.
