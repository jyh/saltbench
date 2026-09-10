# saltbench — notes for an assistant working in this repository

- The frozen protocol documents (`PRE-REGISTRATION.md`, `SCOUT-*.md`, `AMENDMENT-*.md`) are
  appended to, never edited in. A change to what a run measures is a new dated amendment,
  written before that run's first model call.
- Every number in a result file or in the paper names the file it came from. Never retype a
  number from memory or from a message.
- Commit messages carry no chat-session trailers or URLs. `Co-Authored-By` is allowed. The
  commit-msg hook (`git config core.hooksPath .githooks`) and the Scrub CI enforce this.
- The harness is its own implementation of field-standard methodology and takes no code from
  elsewhere without licence and provenance recorded in `PROVENANCE.md`.
- A cell directory is evidence, not scratch. `customer.sh` commits and tags inside
  `$CELL/repo`, so dispatching a phase into a cell that already holds a run rewrites that
  run's git history. Where the cell backs a published or submitted result, that is not a lost
  experiment, it is a corrupted record. Reuse a cell BY COPY, never by dispatch.
- A landing is the subject grading itself. `false_done_claims: 0` means only that the subject
  did not claim done while the turn loop disagreed, and the loop does not compile anything, so
  a cell can land with code that does not build. A self-graded landing rate is an upper bound
  on a verified one: score against the withheld suite before quoting any rate.
