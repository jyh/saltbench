# Working notes
- The file to complete is `__EP__/repo/task.lean`. Replace every `sorry` inside the marked body sections
  (`-- start_def … -- end_def`). Do not change anything outside those sections: the statements and
  signatures are fixed and the checker discards edits to them.
- Compile with `__EP__/rt lake env lean task.lean` (Mathlib is prebuilt; the first run takes a while).
  To use shell features, quote the whole command as one argument.
- There is no network. Do not try to install or update anything (`lake update`, `lake exe cache`).
- The checkout has no git history; do not use git. Do not create commits.
