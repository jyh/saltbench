# `harness/s2rust-analysis/` — tools that READ a finished run, and never run inside one

⛔ **THIS DIRECTORY EXISTS BECAUSE `harness/s2rust/` IS A FENCED SET, NOT MERELY A SET OF PINNED FILES.**
`episode_s2rust.sh:69-71` walks `for f in "$S2R"/*` and REFUSES any file that is present on the host but
absent from `HASHES.txt`, and the driver halts at once on a REFUSE. So a file added to `harness/s2rust/`
without its pin is not untidy — **it is a live charge that detonates on the next `sync_studio_s2rust.sh`,
killing every episode of whatever run is paid for next.**

**That is not hypothetical: `at_first_rc0.py` was committed into `harness/s2rust/` unpinned on 2026-09-02
(`032d25d`) and sat there armed.** It did no harm only because it was never shipped — the P0 read had
already finished, and the Studio's copy of the directory never received it. The next sync would have been
the first episode of the next run.

⛔ **AND THE GATE THAT EXISTS TO CATCH THIS COULD NOT SEE IT.** `sync_studio_s2rust.sh`'s coverage check
derives its file list *from the pin table*, so a file missing from the table is missing from the check too:
the sync reports a clean receipt and the failure surfaces later, inside an episode, as a REFUSE.
⇒ 🔑 **A COVERAGE CHECK DRIVEN BY THE LIST IT IS CHECKING CANNOT REPORT AN OMISSION FROM THAT LIST.**

## The rule this directory encodes

**An analysis tool is not part of the runtime instrument, so it does not belong in the runtime instrument's
fenced set.** Pinning it would have worked, and would have been the wrong repair: it grows the set of files
the episode must verify with files the episode never executes, and it makes every future read-only tool a
pin-table transaction against a table the still-open stage-C dispatch is frozen against.

Files here are:
- read-only over landed artifacts (`state/ep-*/manifest.json`, `session.jsonl`, landings logs),
- never invoked by `episode_s2rust.sh` or any driver,
- therefore unpinned, and harmless if shipped (the fence walks one directory and skips subdirectories).

## Contents

| file | what it reads | what it answers |
|---|---|---|
| `at_first_rc0.py` | a run's episodes | how much of an episode is spent BEFORE its first clean referee run (the 81% finding) |
| `dt_quote.py` | the DT probe's manifests + the Opus read | the row-DT Sonnet quote, gates G1 (per-episode quota) and G2 (censoring) |

📌 `RESULT-amend16-driver-2026-09-02.md` §6.2 cites `at_first_rc0.py` at its old path. The tool is the same
file with the same behaviour; only its directory moved, and it moved for the reason written above.
