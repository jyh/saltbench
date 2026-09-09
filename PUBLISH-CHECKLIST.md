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

## (b) The Scrub gates, ported and driven — GREEN; tree residue 0 after section (f); 5 historical messages baselined, DISCHARGED 09-09

Ported byte-identical from `salt` (which carries the jas port): `scripts/check_commit_trailers.py`,
`scripts/check_private_paths.py` (gate id `819d4ebd77620b0d` at the port; `04ad5a4385236cac` after adopting salt's 2026-09-02 fleet sync, which adds the `safe_gif` root), `scripts/check_pr_descriptions.py`,
`.githooks/commit-msg`, and `.github/workflows/scrub.yml` with a saltbench header. The hook is
armed in this checkout (`git config core.hooksPath .githooks`) and was driven red and green.

| gate | command | verdict |
|---|---|---|
| trailer self-test | `python3 scripts/check_commit_trailers.py --self-test` | OK |
| trailer, full history and tree | `python3 scripts/check_commit_trailers.py` | OK: 94 commit messages and 1039 tracked files, 0 forbidden strings (re-run after (f)) |
| private-paths self-test | `python3 scripts/check_private_paths.py --self-test` | OK (16 planted shapes caught, 16 compliant forms passed) |
| private-paths, tree ratchet | `--tree` | first run: 13 residue lines in 8 files, all baselined. After (f): 0 residue lines, 0 baseline entries. ⛔ **RE-MEASURED 2026-09-09: 2 accepted residue lines in 2 files (both the kit run surface, ratified by path AND content hash), 24 baseline rows, 22 of them debt already paid. 0 NEW.** The zero was true when written and the table kept asserting it; the ratchet's verdict is `0 NEW residue`, which is not the same sentence. |
| private-paths, message ratchet | `--messages` | **5** historical commits baselined (3 Aug + the Captain's 2, ACCEPT 09-09), 0 new |
| private-paths, full delta | `--range <root>..HEAD` | fires on the historical commits that ADDED the 13 lines and the 3 messages, nothing else; history is not rewritten, so this range reads the same after (f). The CI scans each push's delta, and the tree ratchet reads the tree |
| infra names (host, account) | `python3 scripts/check_infra_names.py --self-test`, then the tree scan | OK: 5 planted forms caught, role words pass; tree 1039 files, 0 occurrences (was 41 in 21 files, section (f)). ⛔ **CAUGHT A REAL ONE 2026-09-09**: the placebo ruling carried the run host once and the run account once, and they reached the public repo's CI before any local run saw them — because the four arms above were run from memory and this fifth one was not. Rewritten as role wording (`the Studio`, `the Studio's shared run account`). |
| PR-description self-test | `python3 scripts/check_pr_descriptions.py --self-test` | OK |
| commit-msg hook | a planted trailer line, then a Co-Authored-By line | rc 1, then rc 0 (re-driven after (f)) |
| paper source markers | `python3 scripts/check_paper_sources.py --self-test`, then the paper scan | self-test OK (both empty scans fatal proven first, 7 real marker shapes pass, 4 planted failures caught one per class). Scan: **RED at `e56375e`** (18 findings over 100 markers, 5 cited paths absent), **GREEN at `abdb0fd`** (101 markers, every cited path tracked) after PR #6. Wired into `scrub.yml` in the same act. See section (m). |


⛔⛔ **RUN THE GATES FROM THIS TABLE, NOT FROM MEMORY — MEASURED 2026-09-09 BY THE SEAT THAT WROTE IT.**
Preparing the ACCEPT push I ran four gates, read four greens, and pushed. **There are five**, and the
fifth is the one that had a finding: two infrastructure names in the placebo ruling, which went public
on a branch and were caught by CI rather than by me. Every one of the four I ran was a gate I could
name from memory; the one I missed was the one only this table knows about.
⇒ 🔑 ***A CHECKLIST YOU ARE WORKING INSIDE IS NOT A CHECKLIST YOU HAVE READ.*** The four greens made the
set feel complete, which is exactly what a partial sweep does: **it is the COUNT that reassures, and the
count is the one thing a partial sweep gets right.** The fix is not vigilance — it is running the column
above end to end, every time, and refusing to treat a green as coverage until the last row has printed.

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
| 4 | The 3 commit messages carrying private paths and the 1 body naming the run host: **accepted, no rewrite** | Nothing done, deliberately. They stay in the baseline `scripts/check_private_paths.py --messages` accepts (**5** accepted historical as of 2026-09-09, 0 new). A rewrite would re-sha roughly a hundred commits that the frozen record cites by hash, for filenames that name no third party |
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

## ⛔ HISTORY DEBT ON `bench/v3-referee-rust` — MUST BE SETTLED BEFORE THIS BRANCH GOES PUBLIC

Recorded 2026-09-06 by bench, as a **declared hole with a named trigger** rather than an open question
that a publication step would have to rediscover.

**What:** six paths into the private record entered the *committed history* of this branch on 2026-09-06,
in four files bench authored that day (the helm's REGISTRATION briefs; the MEASURE brief, twice; a
COMMISSION brief; the kit's watch surface). Council 2026-08-25 rules the firewall line at PATHS.

**State:** the working tree is CLEAN — rewritten as role wording at `7990e26`. ⛔⛔ **THIS PARAGRAPH
CLAIMED `check_private_paths.py --range` READS `rc 0` FROM THAT COMMIT FORWARD. THAT IS FALSE AS OF
2026-09-09 AND THE DEBT IS LARGER THAN RECORDED HERE.** Measured at the object 06:3x, after `evidence`
armed this checkout at the outside hook form (row HU) and told me before I met it cold:
```
  check_private_paths.py --range 7990e26..bench/v3-referee-rust     ->  rc 1
  TWO further commits, both AFTER 7990e26, both in their COMMIT MESSAGE, not the tree:
    58d821f  2026-09-07 21:09   a bare private-record path, briefs-shaped
    064911f  2026-09-07 14:20   a bare private-record path, runbooks-shaped
    ⛔ DESCRIBED, NOT QUOTED. Reproducing the literal strings here made this very
      section trip the gate — 3 findings, all of them my own documentation of the
      defect. The gate warns of exactly this: "a literal example is still an
      instance." A record of a forbidden form must name its SHAPE, never its text.
```
⇒ 🔑 ***A "CLEAN FROM HERE FORWARD" CLAIM IS A CLAIM ABOUT THE FUTURE, AND THIS ONE WAS WRITTEN THREE
DAYS BEFORE THE COMMITS THAT FALSIFIED IT.*** It was true when written, it is the sentence a publisher
would rely on, and nothing re-checked it until a gate was armed. **A declared-clean line decays exactly
like a declared-open one, and it is more dangerous because it invites no work.**
⛔ **The offending text survives in `d2d4a0f..7990e26^` AND in the messages of the two commits above.**
⚠️ **The `.seat/` findings in the same gate run are FALSE POSITIVES and are NOT part of this debt** —
`evidence` measured that at the gate with both controls: it cannot distinguish a cell's own
`repo/.seat/` scratch dir from the fleet's private record. That is a gate defect, reported and not
patched by this seat. **No public surface was ever reached: the sole remote on
this checkout is the local bare repository on the Saltworks volume.**

**THE TRIGGER: this branch may not be pushed to any public remote until this line is discharged**, by one
of two acts, and the choice is the Captain's or the helm's, not a lead's:
1. **ACCEPT THE FOLLOW-ON** — the history stays, on the grounds that it never reached a public surface and
   the publication step is itself the gate. Discharge by striking this section with the ruling cited.
2. **PURGE** — the 08/16 treatment, rewriting the range. ⛔ Note the cost honestly: `systems` fetches this
   ref, so a purge invalidates a live worker's clone and must be sequenced with it.

### ✅ DISCHARGED 2026-09-09 — ACCEPT RULED, AND THE MECHANIC RATIFIED MORE THAN THE RULING NAMED

**The Captain ruled ACCEPT (option 1) on `58d821f` + `064911f`, delivered via the helm on bus 45083690.**
Executed here, and the trigger above is lifted: this branch may be pushed.
```
  BEFORE   baseline 3 rows (Aug S2-Lean: 4a26604, 58a3ecc, cb8cea3) · --messages FAIL, 3 unaccepted
  AFTER    baseline 5 rows = those 3 + the Captain's 2 · --messages OK, 0 new
  arms     --self-test OK · --tree OK (0 new residue) · --range 778fc25..HEAD OK (0 paths)
```
⛔⛔ **THE MECHANIC HAS NO SELECTION, AND THE THIRD COMMIT IT SWEPT IN WAS MINE.** `--write-baseline`
takes no revision list: it accepts **every message reachable from HEAD that the gate reds on**. At the
moment the ruling arrived that was **three** commits, not two — the Captain's two, plus `d2633e9`
(bench, 2026-09-09), whose message quoted both offending paths *literally while recording that they are
offending*: the identical defect `89f5685` had just repaired in this file, committed one hour later in
the message of the commit that repaired it.
⇒ **It was NOT baselined.** It was **unpushed** — contained in the local branch and in neither `origin`
nor `backup` — so the gate's own stated remedy applied: *"the ONLY acceptable fix is catching it BEFORE
the push."* Reworded at the object (`d2633e9` → `118b4ea`), the three commits above it replayed, and the
result verified **tree-identical** to the pre-rewrite ref (`git diff` empty, `presha-accept-2026-09-09`
retained as the safety ref). The gate then reds on **exactly the two the Captain named**, so the write
ratifies his ruling and nothing else.
⇒ 🔑 ***AN ACCEPT RULING NAMES COMMITS; THE TOOL THAT EXECUTES IT NAMES A REACHABILITY SET. WHERE THOSE
TWO SETS DIFFER, THE TOOL WINS SILENTLY AND THE RECORD SAYS THE RULING WAS FOLLOWED.*** The gap is not
in the ruling and not in the gate — the gate's docstring says a baseline growth *"needs a council word,
not a green build,"* which is exactly the property `--write-baseline` cannot enforce for itself.
📌 **STANDING CONSEQUENCE FOR THE NEXT ACCEPT:** run `--messages` and read the finding list BEFORE
`--write-baseline`, and compare it commit-by-commit against the words of the ruling. A count is not a
check: three findings and two named commits agree on neither, and the run that would have hidden it
prints `5 accepted commit(s) written` either way.

⛔ **Why it is written HERE and not only on the desk:** a desk row is read by whoever sweeps the desk; a
publication checklist is read by whoever publishes. **This debt's only dangerous moment is the push, so
its record belongs where the push is prepared** — the same reason `ctl/harvest-owed` is written before the
harvest rather than after.

---

## (m) THE PAPER'S SOURCE MARKERS MUST RESOLVE AT THE PUBLISHED BRANCH — DISCHARGED 2026-09-09, GATE GREEN AND WIRED

Added 2026-09-09 by `paper`, on a defect found while revising the paper onto matrix #1.

**THE DEFECT.** The paper's discipline is that every number carries a `\src{...}` marker naming the
file in this repository it was copied from, and `paper/README.md` says the macro expands to nothing
in the PDF so the sources travel with the text and never print. That last property is what hides the
failure: a marker naming a file that reaches no public branch looks exactly like a marker naming one
that does, from the paper, from the PDF, and from a clean build.

Measured at the object after PR #3 merged, over `paper/saltbench-v1.tex` at `main`:

```
  source markers ............ 100
  cited paths that resolve ..  95
  cited paths that do NOT ...   5
```

```
  harness/systems-v3/PREREGISTRATION-matrix-opus-1-2026-09-08.md   <- THE PRE-REGISTRATION
  harness/systems-v3/PRICE-campaign-matrix-opus-1-2026-09-08.md
  harness/systems-v3/PREDICTIONS-pricing-set-2026-09-06.md
  harness/systems-v3/RESULT-hidden-test-strength-v3.md
  harness/systems-v3/score_matrix1.py
```

⇒ 🔑 ***THE PAPER'S CENTRAL METHODOLOGICAL CLAIM IS THAT THE READING WAS PRE-REGISTERED BEFORE THE
FIRST CELL, AND THE DOCUMENT THAT SUBSTANTIATES IT IS THE ONE A READER CANNOT OPEN.*** PR #3 carried
the two required DISCLOSURES, which was the right first cut and is not the criticism. The
registration, the price, the predictions, the suite-strength table and the scorer are the second cut.

**THE GATE.** `scripts/check_paper_sources.py`, same fail-closed shape as its siblings: a scan
finding no `.tex` file, or no source marker, reds; `--self-test` proves both of those before the real
scan is trusted, drives 7 real marker shapes green (including a cited directory, a continuation
segment naming no file, and a later token that is a locator rather than a path) and 4 planted
failures red, one per class.

⛔ **IT IS RED RIGHT NOW AND THAT IS THE POINT.** It was written against a live defect, not a
fixture, and its red arm is in production on the real paper. It is **deliberately NOT wired into
`.github/workflows/scrub.yml` yet**, because a gate that reds on a condition nobody can clear is a
gate that gets disabled.

**RELEASE CONDITION, AND IT IS TWO ACTS IN ONE ORDER:**

1. the five files above reach `main` (a small gated PR off main, artefacts and not history, the
   route PR #3 established) — **owner: `bench`**;
2. **in the same act**, add a `paper-sources` job to `scrub.yml` beside its four siblings, running
   `--self-test` then the scan. **The wiring belongs with the fix**: five files landing makes the
   gate green, and a green gate nobody runs is what this section exists to prevent.

⛔ **UNTIL BOTH ARE DONE, THE ARXIV UPLOAD IS NOT CLEAR.** Not because the paper is wrong, but
because five of its provenance markers point outside the artifact a reader is given, and the whole
`\src{}` convention is a promise that they do not.

### ✅ DISCHARGED THE SAME DAY, BOTH ACTS, IN THE ORDER THE CONDITION NAMED

| act | who | receipt |
|---|---|---|
| 1. the five files reach `main` | `bench` | PR #6 merged at `abdb0fd`, 8 of 8 CI green, verified file by file |
| 2. the scrub job wired, in the same act | `paper` | `paper-sources` job in `.github/workflows/scrub.yml`, `--self-test` then the scan |

```
  BEFORE (main @ e56375e)   FAIL: 18 findings over 100 markers -- 5 cited paths not in the repo
  AFTER  (main @ abdb0fd)   OK: 101 source markers in 1 paper file(s), every cited path tracked
```

⭐ **THE RED ARM RAN IN PRODUCTION, ON THE REAL PAPER, BEFORE THE GREEN ONE DID.** That is the whole
value of writing the gate at the moment the defect was live: the arm that matters was exercised
against a real defect rather than a planted one, and the fixture arms in `--self-test` are there to
keep it exercised after the defect is gone.

⛔ **AND ONE PROVENANCE GAP THIS DOES NOT CLOSE, NAMED BY `bench` WITH THE FILES:** the
`score_matrix1.py` now public is the UNPATCHED scorer, whose declared set is the matrix root plus the
three smoke cells. The topped-up n=3 numbers are produced by a PATCHED COPY on the run box that exists
in no repository. ⇒ **The published scorer over the published archive reproduces the numbers this paper
prints, because the top-up cells sit in a root the published scorer does not declare** — that is what
makes today's table citable. ⇒ ⛔ **It also means NO TOPPED-UP FIGURE MAY ENTER THE PAPER until the
amendment's declared-set change is in the tracked scorer.** An artefact cited by name that resolves to
something other than what produced the result is the same defect class this section was opened for.

### ⛔⛔ THE PARAGRAPH ABOVE IS STALE AT `main`, AND PR #7 IS WHAT MADE IT STALE

Recorded 2026-09-09 by `paper`, measured at `a01c5c6` after PR #4 merged. **The paragraph above stays
as written** — a correction to this file is appended, never edited away — and this is the correction.

**WHAT CHANGED.** PR #7 (`bench/scorer-both-readings-2026-09-09`, `ea476cc`, merged `143b8b6`) landed
the declared-set change in the TRACKED scorer. `harness/systems-v3/score_matrix1.py` at `main` now
carries `TOPUP_ROOT` and computes BOTH readings:

```
  READING A   matrix root + top-up + the SS12 smoke cells   the continuity reading
  READING B   matrix root + top-up only                     every cell from this run
```

✅ **SO THE BAR THIS PARAGRAPH SET IS DISCHARGED.** Its release condition was *"NO TOPPED-UP FIGURE
MAY ENTER THE PAPER until the amendment's declared-set change is in the tracked scorer."* PR #7 IS
that change. The condition was met by a merge that landed BELOW PR #4 while PR #4 was open, so no
head had read the two against each other until this entry.

⛔ **AND ITS STATED MECHANISM IS NOW FALSE AT ITS OWN SHA.** The sentence above says the published
scorer reproduces the paper's numbers *"because the top-up cells sit in a root the published scorer
does not declare."* At `a01c5c6` **the published scorer declares that root.** The conclusion survives
and the reason has changed underneath it:

| | the mechanism as written | the mechanism as measured at `a01c5c6` |
|---|---|---|
| why the table is citable | the top-up root is UNDECLARED | the top-up root is **EMPTY** |
| what would move the numbers | a scorer change | **a cell landing** |

Measured: `~/cells-n3-topup` does not exist on the box this was read from, and PR #7's own message
states that reading A reproduces the previously published behaviour exactly when the top-up root is
absent. ⚠ That is a measurement of ONE box and is not a claim about the run box; whether the three
top-up cells have landed is `systems`'/`bench`'s to report.

⇒ 🔑 ***A DOCUMENT THAT EXPLAINS WHY A NUMBER IS SAFE HAS TO BE RE-READ WHEN THE THING IT NAMES
CHANGES.*** The number never moved, the paper is untouched, and both sentences were true when written.
What failed is that a document and the file it describes were merged in the same range and read by
nobody together. **A stale safety rationale is more dangerous than a stale number**, because the number
has a gate and the rationale has a reader.

### ⛔ OPEN, WITH AN OWNER AND A RELEASE CONDITION: `AMENDMENT 26` IS ON NO REF IN THIS REPOSITORY

Found 2026-09-09 by `paper` while reading PR #7 at the object. `score_matrix1.py` at `main` names
**AMENDMENT 26** four times (lines 83, 86, 97, 130) as the authority for the new root. Swept across
every local and remote ref, with a positive control:

```
  AMENDMENT-20 -22 -23 -24 -25   FOUND on refs (bench/v3-referee-rust, backup/systems-v3, ...)
  AMENDMENT-26                   FOUND ON NO REF, and at no path at `main`
```

This repository's own law, from its `CLAUDE.md`: *"A change to what a run measures is a new dated
amendment, written before that run's first model call."* The paper asserts that discipline as a claim
in its section 2.3, so a reader who opens the scorer meets an amendment number and can go looking.

⚠ **STATED AT ITS LIMIT:** what is measured is that the DOCUMENT is absent from THIS REPOSITORY. It
may be written and uncommitted, or live in a campaign tree. The repo already discloses this class —
`harness/systems-v3/PREDICTIONS-pricing-set-2026-09-06.md` lines 10-11 record that AMENDMENT-21 and
-22 live only on branches — and 26 is simply not named in that disclosure.

```
  OWNER               systems / bench
  RELEASE CONDITION   the amendment document reaches `main`, OR a line in this section recording
                      that it lives on a named branch, the way 21 and 22 already are
  RE-MEASURE          at the next READY post, by the sweep above with its positive control
  GATES THE UPLOAD?   NO. The paper does not cite AMENDMENT 26 and no number in it depends on the
                      amendment. It gates the provenance claim, not the artifact.
```

### ⛔⛔ READING B HAS BEEN REPORTED AND ITS NUMBERS ARE ON **NO REF** — THE DISCHARGE IS BLOCKED ON PROVENANCE, NOT ON THE RESULT

Recorded 2026-09-09 by `paper`, on `systems`' report of 10:51:49 PDT and measured at the object
immediately afterwards. **This entry is appended beneath the two above, never edited over them.**

**WHAT ARRIVED, AND IT IS GOOD NEWS.** The three AMENDMENT 26 top-up cells landed, none capped, none
void. Both readings were computed by the tracked scorer PR #7 landed. **Reading B — the smoke cells
OUT, every cell from this run — reads 5 of 5 at p = 0.0312**, agreeing with reading A on the sign and
on the p-value. By the criterion `bench` stated in advance, that discharges the smoke dependency.

⛔ **AND NOT ONE OF THOSE NUMBERS MAY ENTER THE PAPER YET.** Swept at every ref tip in this
repository, with a positive control on the same instrument:

```
  READING B premiums        (FreeList, LRU, Paxos)      0 ref-hits
  READING A premiums        (FreeList, LRU, Paxos)      0 ref-hits
  both pooled sd values                                 0 ref-hits
  a top-up cell identifier                              0 ref-hits
  ---- POSITIVE CONTROL, published numbers, same sweep ----
  2.7306                                               63 ref-hits
  1.4465                                               34 ref-hits
  0.0312                                              123 ref-hits
```

The scorer that computes both readings is tracked and correct. It reads a harvest root, a matrix
cells root and the top-up cells root, and **all three are absent from the box the paper is written
on**, so it reproduces nothing here. Reading B exists in exactly one place: a bus post.

⇒ This repository's own `CLAUDE.md`: *"Every number in a result file or in the paper names the file
it came from. Never retype a number from memory or from a message."* And it is not only a
convention — `scripts/check_paper_sources.py` is wired into `scrub.yml` and reds on any `\src{}`
marker naming an untracked path. A reading-B table sourced to a bus post fails CI; one with no
marker breaks the promise the paper makes about all 101 of its markers.

⇒ 🔑 ***THE NUMBERS ARE NOT IN DOUBT; THEIR PROVENANCE IS.*** This is the defect class this very
section was opened for — an artefact cited by name that resolves to something other than what
produced the result. **A disclosure must not be closed by committing an instance of it.**

```
  OWNER               systems / bench
  RELEASE CONDITION   a RESULT file on `main`, the shape RESULT-matrix-opus-1-2026-09-08.md
                      already has, carrying: the three top-up cells with harvest METER and
                      post-end COST; both readings' premium tables, pooled sds and p-values;
                      the per-problem A-to-B divergence; the AMENDMENT 26 registered bounds
                      beside the landed values; and the two censuses.
  RE-MEASURE          the sweep above, with its positive control, at the next READY post
  GATES THE UPLOAD?   NO. The paper at `main` is correct as it stands: it DISCLOSES the smoke
                      dependency rather than claiming the discharge. This blocks an
                      improvement, not the artifact.
```

**AND `AMENDMENT 26` IS STILL ON NO REF, re-measured at this READY as the entry above requires.**
The document exists at no path on any of the 50 refs. Positive control: the amendment documents for
11 through 25 are all present as files. Same owner, same fix — the release condition above closes
this one too.

### 📌 WHAT READING B WILL CHANGE IN THE PAPER, PRICED NOW SO THE NEXT HEAD DOES NOT RE-DERIVE IT

Measured against `paper/saltbench-v1.tex` at `main`. **Nothing here is written into the paper yet.**

| site | what changes |
|---|---|
| the scoreboard table | the premium column on FreeList, LRU and Paxos. **Crc32 and LZW do not move** — neither has a smoke cell |
| qualifier 2 | the three below-floor values are re-quoted; the **count stays three of five** under both readings |
| the declared-set paragraph | must name the top-up root and its amendment beside the three smoke cells |
| the smoke-dependency paragraph | **this is the one that discharges.** It currently says the sign test becomes 2 of 2 at p = 0.25 without the smoke cells; under B all five problems reach n=3 inside their own run |
| the census sentence | the priced-cell count moves |
| the future-work list, gap 2 | **closes.** It registered exactly this top-up, and it registered the reading rule quoted below |
| the abstract | **the sign and the p-value do not move.** 5 of 5 and p = 0.0312 hold in both readings. Its qualifier-2 clause was corrected the same day (PR #9) to *three of the five*, and **that count is already the count reading B gives**, so the abstract needs no further edit |

⛔⛔ **THE TRAP, AND IT IS THE PAPER'S OWN REGISTERED RULE, SO IT BINDS.** The future-work list says
the sign test is to be reported with and without the smoke cells, and then: *"if the two readings
agree the dependency is discharged, and if they diverge the divergence is the result and is reported
ahead of the headline."*

**Both halves fire at once, and reading only the first half is the error waiting here.** The
readings AGREE on the sign and the p-value, which is what the rule means by agreement, so the
dependency is discharged. **The magnitudes DIVERGE**: three of the five premiums moved and two moved
down, one of them to the closest any premium in this campaign has come to 1.0.

⇒ **So the discharge and the divergence are reported TOGETHER, and the divergence is not a footnote
to it.** `systems` led with the worst of it rather than burying it, and the paper must do the same.
⇒ 🔑 ***A DEPENDENCY CAN BE DISCHARGED AND THE THING IT WAS PROPPING UP CAN STILL GET WEAKER, AND A
READER IS OWED BOTH FACTS IN THE SAME BREATH.*** The magnitudes were never reportable as the finding
(G2 bars it in both readings), which makes it tempting to treat their movement as immaterial. It is
not immaterial: it is the measurement of how much the smoke cells were flattering the table.

📌 **THE ABSTRACT DEFECT THIS SITTING FOUND HAS A ROOT CAUSE, AND `bench` FOUND IT THE SAME HOUR.**
The abstract's false clause was corrected in PR #9; PR #10 corrected **the place it came from**. The
scorer printed the G2 **reporting rule** in the language of a **measurement** — *"every per-problem
magnitude is UNRESOLVED"* — and the abstract quoted it as one. The scorer now names the two sets
apart, the below-floor and the clearing, and says in its own output that the rule is not a claim that
every magnitude fell below.
⇒ 🔑 ***AN INSTRUMENT THAT STATES A RULE IN THE GRAMMAR OF A MEASUREMENT WILL BE QUOTED AS A
MEASUREMENT.*** The paper's sentence was a faithful quotation of an instrument that was itself
imprecise, which is why reading the paper against its own table found the symptom and only reading
the scorer found the cause. **Both were needed, and neither gate could have fired.**
⇒ Where this entry says G2 bars a ratio from being reported as the finding, that is the **rule**
sense, which is unchanged and still binds.

📌 **AND THE TOP-UP IS NOT A REPLICATION.** The registered bounds proved no outcome of it could move
a premium to 1, which is why it could not confirm the result either. It bought precision and removed
a dependency. Nobody may write it as a second run agreeing with the first.


## (n) UPLOAD DAY — THE EXACT SITES THE ARXIV ID AND THE ZENODO DOI GO INTO, MEASURED IN ADVANCE

Added 2026-09-09 by `paper`. The order is *"on upload day: the arXiv id and the Zenodo DOI into
README, PROVENANCE and the paper."* This section is that order resolved to file and line **before
the day**, because on the day the identifier exists and the memory of where it belongs does not.

### THE ZENODO DOI — THREE SITES OUTSIDE THIS FILE, TWO INSIDE IT
All five carry the same promise, and all five must move together or the repository asserts an
unassigned DOI in one place and a real one in another.

| file | line at `abdb0fd` | the sentence that must change |
|---|---|---|
| `README.md` | 33-35 | *"its DOI is assigned at release (Zenodo) and recorded here on the flip day"* |
| `PROVENANCE.md` | 67 | the same sentence, in the data-asset paragraph |
| `PROVENANCE.md` | 97-98 | *"Status on 2026-09-02: OWED, INVENTORIED"* — the status line, not only the DOI |
| `paper/saltbench-v1.tex` | the Reproducibility section | *"its DOI is assigned at release (Zenodo) and recorded in the repository on the flip day"* |
| this file | 120 and 189 | the `runs/` disposition row and the data-asset item |

⛔ **THE DOI IS NOT A STRING SUBSTITUTION.** Four of the five sentences say the DOI *will be*
assigned; after release they must say what it *is*. A find-and-replace on the identifier leaves the
future tense standing beside the number.

### ⛔⛔ THE ARXIV ID HAS EXACTLY ONE SITE TODAY, AND IT IS NOT ONE OF THE THREE THE ORDER NAMES
Measured across the tree: the only place prepared for it is `CITATION.cff`,
`preferred-citation.notes: "arXiv identifier to be added at submission"`. **`README.md` and
`PROVENANCE.md` have no arXiv line at all**, so on upload day those are ADDITIONS and not edits.

⇒ 🔑 ***AN EDIT YOU HAVE TO REMEMBER TO MAKE IS A DIFFERENT RISK FROM AN EDIT YOU HAVE TO REMEMBER TO
FIND, AND THE ORDER NAMED THREE FILES OF WHICH TWO HAVE NO SITE.*** What upload day needs:

1. `CITATION.cff` — replace the `notes` line with the identifier, and set `preferred-citation.url`.
2. `README.md` — a citation line beside the paper reference at line 10, naming the arXiv id.
3. `PROVENANCE.md` — the paper's own entry, alongside the third-party ones it already lists.
4. `paper/saltbench-v1.tex` — nothing. **An arXiv paper does not print its own identifier**; arXiv
   stamps it. Recording it in the tex would be a second, hand-maintained copy of a number the
   service owns.

### ⚖️ A FORK I AM NOT TAKING ALONE: THE TITLE NAMES TWO SUBSTRATES AND THE PAPER NOW HAS THREE
The title ends *"with Frontier Baselines on Lean and Verus"*. Since the matrix #1 revision the paper
reports a third population, five components authored here in Rust.

* **arm A, change the title.** It would describe the contents.
* **arm B, leave it.** ⭐ **RECOMMENDED, and taken unless the owner says otherwise.** The third
  population's result is a COST reading with correctness unmeasured and no independent authorship.
  It is **not a baseline**, and the title's claim is about where the baselines are, which is still
  exactly Lean and Verus. Advertising the systems population in the title would make the strongest
  claim in the paper the one the run supports least, which is precisely what Section~(l) exists to
  prevent everywhere else.

⛔ **WHICHEVER ARM IS TAKEN, `CITATION.cff` AND THE `\title{}` MUST MATCH BYTE FOR BYTE.** They carry
the same string twice today, and a title change that moves one of them is a citation that disagrees
with the paper it cites.


## (l) REQUIRED DISCLOSURES FOR ANY WRITE-UP OF MATRIX #1 (v3) — BINDING, not advisory
<!-- ⛔ RELABELLED 2026-09-09 by bench: this section stood as a SECOND "(j)" beside the
     09/02 escape-sentence section, so a citation to "section (j)" resolved to two different
     sections and a reader reached whichever came first. Earlier receipts and bus posts cite
     it as (j) — they mean THIS section, the matrix #1 disclosures. The old label is recorded
     rather than erased, for the same reason a superseded line is replaced and not deleted. -->

⛔ **SCOPE: this section is about the v3 opus matrix, not the v1 flip that the rest of this file
covers.** It is here because this is the surface a publisher reaches; a rule binding the write-up
that lives only in the pre-registration binds nobody who does not read the pre-registration.

**Ruled by the helm 2026-09-08 on bench's own disclosure (§20 of
`harness/systems-v3/PREREGISTRATION-matrix-opus-1-2026-09-08.md`). Each item appears where the
reader meets the claim — NOT in a methods section, NOT in an appendix, NOT in a footnote.**

1. ⛔ **THE PRIMARY TEST IS ONE-SIDED, AND THIS APPEARS BESIDE THE p-VALUE.**
   `P(at least k premiums ABOVE 1)`. Five above 1 → p = 0.0312 and the hypothesis is CONFIRMED at
   .05; five BELOW 1 → p = 1.0000 and it **cannot be refuted at .05**. ⇒ **this design can confirm
   its hypothesis and cannot significantly refute it.** A one-sided test is a claim about which
   surprise you were willing to be surprised by; a reader who meets that in an appendix has
   already read the headline and priced it as two-sided.
2. ⛔ **THE HEADLINE IS THE SIGN ACROSS PROBLEMS, NEVER A RATIO.** 5/5 → p=0.031. **4/5 → p=0.1875
   and is registered IN ADVANCE as NOT a result** — it may not be reported as "nearly". The
   per-problem MAGNITUDES are UNRESOLVED at n=3 against the registered floor of 2.007254… (printed
   2.0072 truncated here, 2.0073 rounded in some receipts — **one number, two renderings**).
3. ⛔ **THE GOLD PAIR IS k=1 AND MUST BE LABELLED AS SUCH.** Only LZW carries a `## Statement`
   card (§16), so the statement-arm comparison cannot reach significance at ANY outcome. It is the
   pair the campaign most wants and the one this matrix cannot answer.
4. ⛔ **THE PLACEBO'S ZEROS ARE NECESSARY AND NOT SUFFICIENT.** A shingle count cannot fail a
   construction that replaced the words. The placebo arm may never be reported as "provably
   contains no method" (`RULING-placebo-acceptance-2026-09-08.md`).
5. ⛔ **COST IS COMPARABLE ACROSS THE TWO EXPORTS; CONTAINMENT MEASUREMENTS ARE NOT.** No table may
   place placebo and stage-1 escape/containment columns side by side (same ruling, §2).
6. ⛔ **THE CELLS CARRY NO `built-from.tsv`.** Matrix #1's provenance is a RECONSTRUCTION
   (`PROVENANCE-matrix1-2026-09-08.tsv`), not a receipt written at build time. Say which it is.

7. ⛔ **CROSS-STAGE COST COMPARISONS ARE CONFOUNDED BY CONCURRENCY.** Stage 1 ran roughly ONE
   cell at a time; matrix #1 ran FOUR. The two stages ran the same client binary (confirmed by byte
   size against stage 1's own record) but **not under the same box contention**, and this harness
   records box-busyness as material. ⇒ **stage 1's premiums (1.1655–1.3560) may not be presented as
   a replication of matrix #1's (1.1610–2.7306)**: the sets differ in concurrency as well as date,
   and nothing separates those. Matrix #1's own result is unaffected — its sign test is computed
   entirely within one run where both arms were at 4-wide.

8. ⛔⛔ **EVERY PUBLISHED COST CARRIES AN UNMEASURED BOX-LOAD TERM, AND NOTHING IN THIS CAMPAIGN
   MEASURES IT.** Item 7 discloses a *known* concurrency difference between stages. This one is
   worse in kind: **the harness reaps the client and the watcher, and nothing reaps what the SUBJECT
   forked.** Measured 2026-09-09 by `systems` — 24 busy-wait processes forked by the subject of one
   placebo cell, re-parented to init, burning ~11 cores for **3h23m**, outliving their own cell's END
   by **3h09m**, with 11 of 16 priced cells in that wave metered wholly or partly inside the window.
   ⇒ **A cell's END is not the end of the cell's processes**, so any cell may have been priced on a
   box carrying the residue of earlier cells. **No arm looks, so no run can state its own load.**
   ⛔ **Direction on COST: UNMEASURED.** Extra CPU does not spend tokens; it could reach cost only
   indirectly (timeouts, retries, extra turns) and that was not driven. **Do not report this as
   having inflated or deflated anything.**
   ✅ **BOUNDED FOR MATRIX #1 SPECIFICALLY, and the bound is the only reason the headline is
   unaffected:** every one of matrix #1's 37 cells reached END by `2026-09-09T00:51:59Z`; that leak
   opened at `2026-09-09T03:34:51Z` — a margin of **2h 42m 52s**. ⇒ **No matrix #1 cell was metered
   inside it** (`RULING-placebo-acceptance-2026-09-08.md` §8.1). **This clears matrix #1 of THAT
   leak and of no other.**

⇒ 🔑 **THE GENERALISATION, WHICH IS THE HELM'S AND OUTLIVES THIS CAMPAIGN: *OF EVERY GATE,
STATISTICAL ONES INCLUDED, ASK WHICH ARM TRIPS IT — AND ASK WHILE NO RESULT EXISTS, BECAUSE
AFTERWARDS THE ANSWER IS UNPUBLISHABLE EITHER WAY.*** An instrument is validated only when good and
bad outputs DIFFER; ours returns p=1.0000 on the arm that would be the larger surprise.

### ✅ BOTH BLOCKS ABOVE ARE DISCHARGED — 2026-09-09, AND I FOUND THE SECOND ONE BY RE-MEASURING MY OWN ABSENCE

Recorded by `paper`. **Appended beneath the two entries above, never edited over them.**

**READING B: released by arm 1 of its own condition.** The RESULT file exists on `main` and carries
every field the condition specified. Re-measured with the same sweep and the same positive control:

```
  harness/systems-v3/RESULT-n3-topup-2026-09-09.md      the three cells, both readings, verbatim stdout
  harness/systems-v3/RESULT-matrix-opus-1-2026-09-08.md the discharge recorded against the dependency
  the three top-up cells, harvest METER + post-end COST  section 1        ✅
  both readings' premium tables, pooled sds, p-values    section 3        ✅  cut from the instrument
  the per-problem A-to-B divergence                      section 5        ✅
  the AMENDMENT 26 registered bounds beside the landed    section 4       ✅
  the account-boundary disclosure                        section 1b       ✅  (not required; volunteered)
```

⭐ **The file is cut from the unmodified instrument's stdout with the scorer's sha beside it.** That
is the thing the block was actually about, and it is worth naming: the block was never doubt about
the numbers, and this file answers the doubt that existed.

**AMENDMENT 26: released by arm 2, and arm 2 was always MINE.** The condition read *"the amendment
document reaches `main`, OR a line in this section recording that it lives on a named branch, the way
21 and 22 already are."* **This is that line:**

```
  AMENDMENT-26-n3-topup-2026-09-09.md   lives on   refs/remotes/backup/systems-v3
  commit                                1556db7    2026-09-09 08:48:38 -0700
  at `main`                             absent, as AMENDMENT-21 and -22 are absent from main
  positive control                      AMENDMENT-25-cross-vendor-agy-2026-09-07.md found by the same sweep
```

⛔⛔ **AND THE FINDING IS THAT MY EARLIER MEASUREMENT WAS WRONG IN A WAY ITS OWN INSTRUMENT COULD NOT
SEE.** The entry above says AMENDMENT 26 was `FOUND ON NO REF`, measured with a positive control at
~11:0x today. **The document had been committed at 08:48:38, two hours and some minutes earlier.**
The sweep enumerated `git for-each-ref`, which lists the refs **this checkout has fetched**, and
`backup` is a second remote that had not been fetched in this working copy.
⇒ 🔑 ***AN ABSENCE MEASURED OVER `for-each-ref` IS A CLAIM ABOUT AN OBJECT STORE, NOT ABOUT A FLEET.***
It is the same shape as the fleet-root `grep` defect: a population silently emptied, exit 0, no
warning, and a true absence and a stale one are byte-identical in the output.
✅ **THE REMEDY, AND IT IS ONE WORD:** `git fetch --all` before any absence sweep over refs, and say
in the finding which remotes were fetched.
📌 **The entry above did state itself at its limit** (*"what is measured is that the DOCUMENT is
absent from THIS REPOSITORY... it may live in a campaign tree"*), which is the only reason this is a
correction to my own record and not a false accusation against `systems`. **The limit clause earned
its keep**, and a measurement stated at its limit is the one that survives being wrong.

### 📌 THREE SITES READING B TOUCHED THAT THE PRICING ABOVE DID NOT NAME

The priced table above listed seven sites and was accurate on all seven. Three more moved, found by
reading the paper against the new declared set rather than against the old numbers.

1. ⛔ **THE MEDIAN COLUMNS COULD NOT SURVIVE, AND THE REASON IS PROVENANCE, NOT LAYOUT.** The table
   carried `plain median` and `diet median` beside each premium. The old hand-written scoreboard
   printed those medians; **the instrument that computes readings A and B prints the per-cell prices
   and the premium and does not print the median.** At n=4 a median is the mean of the middle pair
   and is not any cell's price, so under reading A the column could only have been arithmetic of
   mine. Under this repo's own first rule that number could not name a file, so **the columns are
   retired and the table's SHAPE changed, not only its values.** ⇒ 🔑 ***AN INSTRUMENT THAT GAINS A
   READING CAN LOSE A COLUMN, AND THE WRITE-UP FINDS OUT ONLY BY TRYING TO CITE IT.***
   ⚖️ **A cheap fix that is `systems`/`bench`'s and not mine:** have the scorer print the two medians
   it already computes. The column returns the moment it is in the stdout.
2. ⛔⛔ **A BOUND WAS STATED OVER THE MATRIX ROOT AND THE DECLARED SET OUTGREW IT.** The box-load
   paragraph cleared this matrix of the 24-process leak by a margin: *"all 37 of its cells reached
   their end at or before 2026-09-09T00:51:59Z and that leak opened at 03:34:51Z."* **The three cells
   AMENDMENT 26 added are in the declared set and are not in that 37**, and no file on `main` records
   an end time for them. The paper now states the bound over the matrix root, says the three added
   cells are not covered, and does not claim they are.
   ⇒ 🔑 ***A SET THAT GROWS AFTER A BOUND IS WRITTEN OVER IT DOES NOT INHERIT THE BOUND, AND THE
   GROWTH IS SILENT*** — the scoreboard, the premium and the p-value do not change shape when a cell
   no timing record covers joins the set. **This is the priced-table's own defect class one level up:
   the pricing asked what reading B CHANGES and not what it ENLARGES.**
   ⚖️ **OWED, `systems`/`bench`, not gating:** an end time for the three top-up cells in a file on
   `main`. The construction stamp `2026-09-09T15:44:50Z` exists in AMENDMENT 26 section 3, which is on
   `backup/systems-v3` and therefore uncitable by `check_paper_sources`. One line on `main` closes it.
3. **Qualifier 4's span endpoint and its comparison term both moved.** `FreeList` plain now includes
   the $13.01 top-up cell, so the within-condition span is \$13.01 to \$23.38 rather than \$13.02 to
   \$23.38; the ratio is $1.80\times$ at both. And the **smallest premium in the table is no longer
   the same problem under both readings**: Crc32 at $1.16\times$ under A, LRU at $1.15\times$ under B.
   The abstract's clause *"larger than the smallest premium"* is true under both and was left alone.

**WHAT WAS DELIBERATELY NOT DONE:** the abstract was not reopened. The pricing above found it needs
no edit, the sweep of it against the body last sitting found it clean, and its two relevant claims
(three of five below the floor; the spread larger than the smallest premium) hold under both readings.
Re-opening the most-read paragraph in the paper on a change that does not touch it is scope, not care.
