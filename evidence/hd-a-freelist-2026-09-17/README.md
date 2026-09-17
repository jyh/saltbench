# HD (a) — the receipts the declaration rests on
bench (SaltBench lead), 2026-09-17. Landed on the 90th helm head's finding at signature: **the pivot of the
declaration had no tracked receipt, so a reader who wanted to check the one fact it turns on had nothing to open.**

## `client-split.tsv` — the pivot
Every FreeList greenfield cell, its arm, its **client binary sha** and its root, read at each cell's own
`ctl/launch.log` on the run box, read-only. **12 rows: `s3fp01` alone on `98724c5370d91a2f`; the other eleven on
`cabadc15a6194437`.**
⇒ This is what §R4 and §R5 turn on. **It is also what refutes the client explanation**, because three of the eleven
(`s3fq01`, `s3fq02`, `s3fqk01`, the `plain + statement` condition) PASS in full on `cabadc15`.

## `rescore.tsv` — the scores, with controls that had to reproduce
`run_tests.sh` from each era tree over a `solution.rs` fetched read-only, VERUS pinned **by sha** (measured ==
declared in `~/cells/toolchain.env`).
- **Two controls with already-published figures**, `s3fp01` and `s3fq01`, both **PASS 7/7** — they reproduce.
- **Two targets**, `s3fpk01` and `s3fpk02`, both **FAIL 6/7**.
- **Driven in BOTH era trees (`s2g`, `s2k`), which agree cell for cell**, bounding the scorer's contribution to zero.
⛔ **The controls are not ceremony.** The first pass returned **rc 4 on all four** (`VERUS_ROOT` unset), which
`score_wave_v3.sh:275` classifies as `FAIL` — byte-identical to a real crash. **Without the controls the two targets
would have been recorded as failures for the wrong reason.**

## What is NOT here
The level-4 brownfield corroboration is **absent on purpose**: those cells are VOID per
`RESULT-gemini-brownfield-level4` ADDENDUM 1 §V3, and §R5 strikes the citation rather than filing it.
