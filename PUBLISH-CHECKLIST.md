# PUBLISH-CHECKLIST — v1 hygiene and provenance, DRIVEN 2026-09-02 (seat `paper`)

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

## (b) The Scrub gates, ported and driven — GREEN, with 16 accepted residue lines baselined

Ported byte-identical from `salt` (which carries the jas port): `scripts/check_commit_trailers.py`,
`scripts/check_private_paths.py` (gate id `819d4ebd77620b0d`), `scripts/check_pr_descriptions.py`,
`.githooks/commit-msg`, and `.github/workflows/scrub.yml` with a saltbench header. The hook is
armed in this checkout (`git config core.hooksPath .githooks`) and was driven red and green.

| gate | command | verdict |
|---|---|---|
| trailer self-test | `python3 scripts/check_commit_trailers.py --self-test` | OK |
| trailer, full history and tree | `python3 scripts/check_commit_trailers.py` | OK: 90 commit messages and 1023 tracked files, 0 forbidden strings |
| private-paths self-test | `python3 scripts/check_private_paths.py --self-test` | OK (16 planted shapes caught, 16 compliant forms passed) |
| private-paths, tree ratchet | `--tree` | 13 residue lines in 8 files, ALL baselined, 0 new |
| private-paths, message ratchet | `--messages` | 3 historical commits baselined, 0 new |
| private-paths, full delta | `--range <root>..HEAD` | the same 13 lines and 3 messages, nothing else |
| PR-description self-test | `python3 scripts/check_pr_descriptions.py --self-test` | OK |
| commit-msg hook | a planted trailer line, then a Co-Authored-By line | rc 1, then rc 0 |

The 13 tree lines and 3 messages all cite the private record by path, in the frozen protocol
documents (`PRE-REGISTRATION.md`, `SCOUT-STAGE0.md`, `SCOUT-S2LEAN-STAGE0.md`,
`AMENDMENT-15-s2rust-2026-09-01.md`), in `README.md`, `CLAUDE.md`, `.gitignore`, and one line of
`harness/s2rust/gt_leak_check.py`. They are ACCEPTED into `scripts/private_paths_baseline.tsv`
and `scripts/private_paths_message_baseline.tsv`, for the reason the fleet ruled on 2026-08-30 and
for this repository's own rule: frozen documents are appended to, never edited, and the shas are
pinned in the run record (item (a)). The CI ratchets red on anything NEW on every push.

Three of the 13 are NOT in frozen documents and are removed on the flip branch (item (e)): the
README banner, the seat-instructions file `CLAUDE.md` (replaced by a public contributor note), and
the `.gitignore` comment. The `gt_leak_check.py` line is a gate false positive: a Python string
containing the two characters backslash and `n` after the word, which the gate's separator class
reads as a path separator. Baselined rather than edited, because the fixture is right and the
gate's separator class is a fleet-level file that ships byte-identical to three repositories.

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
| `FLEET.md`, the seat repo path, the kit path, session URLs | `runs/` and `evidence/` | 0 files |
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
| `runs/` (untracked, 61 MB: S1 stage-0 transcripts, audit runs, Studio controls and scoring) | KEEP, release as a data asset beside the repo, not in git | 61 MB of jsonl belongs in a release asset; nothing in it is private |
| `data/verified.json` (untracked, 7.7 MB) | STRIP (stays untracked) | a copy of a third-party dataset; re-derived from the pinned revision |
| the S2-Lean and S2-Rust episode archives on the Studio | PULL into the data asset before the flip | they are the primary data behind every S2 number; bench owns them |
| `harness/s2rust/views/` | not tracked, rebuilt from the pin | contains the benchmark's task text and ground truth |

Provider terms: `PROVENANCE.md` section 3 records the reading (outputs are the user's; publication
is not forbidden) and marks it for the Captain's confirmation.

## (e) The flip — PREPARED on branch `public-v1`, NOT MERGED

Prepared on a separate worktree so the shared checkout on `master` (bench commits into it) is never
switched. The branch carries: the public README (the PRIVATE banner replaced), `LICENSE` (proposal:
Apache-2.0 for code) and `LICENSE-DATA` (proposal: CC-BY-4.0 for data and documents), a
`CITATION.cff`, a public `CLAUDE.md` replacing the seat instructions, the `.gitignore` comment
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
