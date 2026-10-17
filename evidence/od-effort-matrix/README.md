# desk OD — the effort matrix's per-cell table (AMENDMENT-OD-effort-matrix-2026-10-16.md, §D9)
`od-d9-cells.tsv` holds the 27 REGISTERED matrix cells (§D1 with ADDENDA 5 and 7's labels), keyed on ROOT + CELL, each `HARVESTED` or `OWED`.
It is rebuilt whole after each harvest by the lead's extractor (`od_d9_extract.py`, sha256/16 `081d56419adf90ad` at this commit; it reads the run's
own records: the harvest, served-set, escape, fire and post-launch-check outputs, the chain's suite line, and each cell's launch-log ARGV,
end marker and staging record). It refuses a row whose meter does not sum or whose end markers disagree. An OWED row is never omitted.
`harness/systems-v3/od_d9_result.py` derives the RESULT's lines from this table and nothing else, and WITHHOLDS every condition row,
ceiling reading and prediction until all 27 are harvested. Three post-launch checks (FX#2, FH#2, OX#1) were re-run from fixed birth
times after the fact; their config-dir column is the at-harvest reading posted at the time, labelled with its bus offset.
