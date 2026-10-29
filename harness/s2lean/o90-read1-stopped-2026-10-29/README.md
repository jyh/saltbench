# O90 read 1 as fired: the 46 attempts (ADDENDUM 8 A8.1)

`attempts.tsv` is the output of `attempts.py RUNDIR --since 2026-10-28T17:43:37` over the reader's run directory (gemini's driver
`run-truth1.py`, sha256/16 8adaa8b090a3aa0b), read on 2026-10-29 after the process exited at 07:08:15Z. One row per model attempt,
joined from `out/meter.tsv` and `calls/*.json` by session id. The summary lines at its foot are what A8.1 quotes.

It is a record of a STOPPED set (A8.2), not a result. No verdict from these reads is scored, and none is pooled with a later set.
The run directory itself stays on the reader's box. This file carries ids, counts and causes only, and no model output.
