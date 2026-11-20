# The re-cut: every comparison that held a WEB-SERVED cell of record, old line beside new (O37, 2026-11-20)

The lead's ruling (bus 2026-11-20 00:29:42, helm-reversible) puts each WEB-SERVED cell of record out of every comparison
(`../README.md`). This directory shows what that moves. The table re-cut **replaces no table of record** and is not the source of
any figure in the paper. It is a reading beside the record, appended to each RESULT it touches as a dated addendum.

```
python3 recut.py <OUTDIR>            # run every instrument on its input of record (OLD) and with the WEB-SERVED cells out (NEW)
python3 recut.py <OUTDIR> --check    # the same, and exit 1 unless each <label>-moved.txt equals the tracked one here
```

- **The cells are read, not typed:** `recut.py` takes the WEB-SERVED cells from `../join.tsv` (10: three in the matrix, five in
  block NA, two in ZF).
- **No instrument is changed.** A cell leaves each one by the route that instrument already has. For `tables_v2.py`, `tables_v3.py`
  and `tables_correctness_v3.py`, the cell-map row's model gets the prefix `#EXCLUDED-BY-RECORD`. For block NA's
  `RESULT-gemini-blockNA-2026-09-28-prose-verify.py`, the cell's row is dropped from a scratch copy of the cells TSV. For
  `zf_result.py`, the row is dropped from a copy passed as `--cells`.
- **Control, every run:** each OLD output must reproduce its RESULT of record's table rows exactly, and `zf_result.py --check`
  must be green on the ZF RESULT. Otherwise the run stops before any comparison. On 2026-11-20 all five controls held:
  descriptive v2 864/864 rows, descriptive v2 + O57 864/864, cost v3 922/922, correctness v3 781/781, and ZF CHECK GREEN.
- **The moved lines:** `recut_diff.py` keys each markdown table row by its section and its LABEL (the fields that are not
  figures), so a row that only moves within its section pairs as OLD/NEW. A row whose label exists on one side only is printed
  as GONE or ADDED. Block NA's and ZF's outputs are lines, not tables, and are diffed with `diff -U0`.

Files: `descriptive-v2-moved.txt`, `descriptive-v2-O57-moved.txt`, `cost-v3-moved.txt`, `correctness-v3-moved.txt`,
`blockNA-moved.txt`, `ZF-moved.txt`.

## Two places where an instrument's own guard reads the removal as missing data (declared, not changed)

1. **`tables_correctness_v3.py`, Flash × Paxos × greenfield × salt-diet × none.** Level 5 recorded this condition's verdict by
   condition (ADDENDUM 3d: 2 of 3), not per cell. Without `l5psra202`, the tool cannot know which of the 2 remaining cells passed,
   so it prints the condition `unmeasured` and its own arithmetic check goes red: *"conditions with a k/n 180 + — 16 +
   declared 3 + unmeasured 1 = 200"*. The re-cut prints that as the tool prints it, and it is right: the condition has no
   pass count without the excluded cell.
2. **`zf_result.py`, STATE.** The tool reads a condition with fewer than 3 harvested cells as SHORT, and a SHORT pair that is not
   CUT by ruling as a set that has not ended, so the NEW run prints `STATE: PARTIAL`. The ZF set has ended. PARTIAL here means
   two Flash Paxos salt-diet conditions hold 2 of 3 cells after the exclusion, nothing more.

## Limits

- This is the comparison without the cells, beside the record. It is not a new result of record, and no table that the paper
  prints has changed.
- `zf_result.py`'s A7 print-timeout figures come from a root census file (`evidence/zf-result/pt-census*.txt`) that the re-cut
  does not filter, so their root counts do not move. Only the harvested-legs count beside them does.
- The O57 sub-agent `addT.tsv` and the v3 cost evidence are read as recorded. A WEB-SERVED cell's rows in them are simply never
  reached.
