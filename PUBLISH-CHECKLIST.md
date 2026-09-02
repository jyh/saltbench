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
`scripts/check_private_paths.py` (gate id `819d4ebd77620b0d`), `scripts/check_pr_descriptions.py`,
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

Fleet item, not this repository's: the gate's employer-lane root list predates the `safe_gif`
seat. Measured here: zero occurrences of any employer-lane name in the tree or history
(`git grep -I -n -E 'safe_gif|safe_dav1d|pcc-bios|/loca/|/holl/'` returns nothing).

## (c) Provenance of every population — WRITTEN, `PROVENANCE.md`

Every source, its pin, its licence as read at the object on 2026-09-02, and what this repository
redistributes from it. Summary:

| population | source and pin | licence | redistributed here |
|---|---|---|---|
| S2-Lean | CLEVER `trishullab/clever@8348039` | MIT (UT Austin 2025) | the 161 problems' docstrings, human specs, statement headers and tests, as stage views |
| S2-Rust | VeruSAGE-Bench `microsoft/verus-proof-synthesis@cbf9c0c6` | MIT (Microsoft 2024) | nothing of the task text; verdict records keyed by id |
| S1 | SWE-bench Verified, HF revision `c104f840` | code repo MIT; dataset card has no licence field; issue text under the nine source repositories' licences (BSD-3, BSD-2, Apache-2.0, MIT, matplotlib's PSF-style) | 30 problem statements, the id list, the image digests |

Open for the Captain: the SWE-bench Verified dataset card states no licence. The reading taken in
`PROVENANCE.md` section 1.3 (issue text redistributable under the source repository's licence plus
the SWE-bench release) is a reading. If the Captain prefers, `harness/data/problem_statements.json`
can be dropped from the public tree at zero cost to reproducibility, since it is re-derived from the
pinned revision by `harness/project_data.py`.

## (d) Secrets, private paths, transcripts — CLEAN; provider-terms note written

| scan | scope | result |
|---|---|---|
| `git grep -I -n -E 'sk-ant-|AKIA[0-9A-Z]{12}|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20}|xox[bp]-[0-9]'` | tracked tree | 0 |
| the same pattern with `grep -rlE` | `runs/` (61 MB, untracked) and `data/` | 0 files |
| `FLEET.md`, the seat repo path, the kit path, session URLs | `runs/` (untracked) | 0 files |
| the same, re-scoped to the WHOLE tracked tree after the refuter pass (`git grep -n -I -i -E 'FLEET\.md\|projects/claude/seat\|Documents/seat\|claude\.ai/code/session_\|memory-seats\|seat-loop\|helm_append'`) | tracked | 6 lines, no path: the hook's own refusal text, the gate's own fixture, this table's row, two docstring mentions of a fleet tool's name (`harness/s2lean/bc_gate.py:14` and its evidence copy), one mention of the bus file's name (`SCOUT-S2LEAN-STAGE0.md:1785`). The three name mentions are fleet VOCABULARY, held with the vocabulary item below |
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

Provider terms: `PROVENANCE.md` section 3 records the reading (outputs are the user's; publication
is not forbidden) and marks it for the Captain's confirmation.

## (e) The flip — PREPARED on branch `public-v1`, NOT MERGED

Prepared on a separate worktree so the shared checkout on `master` (bench commits into it) is never
switched. The branch carries: the public README (the PRIVATE banner replaced; a real command block since (f)), `LICENSE` (proposal:
Apache-2.0 for code, marked PROPOSAL in the file itself since (f)) and `LICENSE-DATA` (proposal: CC-BY-4.0 for data and documents), a
`CITATION.cff` (its licence field held as a comment until the choice is made), a public `CLAUDE.md` replacing the seat instructions, the `.gitignore` comment
cleaned, the baselines regenerated (the three removed lines shrink the tree baseline to 10), and
the scrub CI armed. The licence choice is the Captain's; the branch says "proposal" in both files
until he chooses. The branch sha is in the READY post on the bus.

Not done by this seat, by construction: creating the public GitHub repository, pushing, and the
arXiv submission. The helm carries the READY post to the Captain.

## What the flip still needs from others

1. The Captain: the licence choice; confirmation of the provider-terms reading; the SWE-bench issue
   text decision (keep or drop the 30 statements).
2. bench: the S2 episode archives pulled into the data asset; the DT Sonnet two-tier read if it
   lands before the flip (the paper carries a slot for it, section 6).
3. The helm: the fleet-level note that the private-paths gate's root list predates `safe_gif`.
4. The Captain, HELD by the refuter pass, not acted on here: (i) the 3 commit messages carrying private
   paths and the 1 commit body naming the run host: a pre-flip history rewrite is lawful (no public
   remote) and would re-sha every commit the private record cites, so it needs a shamap of its own;
   (ii) the fleet vocabulary (Captain, helm, seat, council, bus) in 53 non-frozen files: scrub or
   accept.
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
