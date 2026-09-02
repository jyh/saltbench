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
