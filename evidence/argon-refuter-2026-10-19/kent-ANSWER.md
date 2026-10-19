# kent's answer: a non-author read of RESULT-claude-blockSBS-2026-09-21.md (bench's Argon-refuter control, registered 2026-10-19)
# Read by kent (Sonnet 5.5), 2026-10-19 10:1x PDT, from the bundle's three files ALONE (BRIEF.md, the result file, blockSBS-cells.tsv, blockSBS-retention-decomp.tsv). Bundle verified before reading: `shasum -a 256 -c BUNDLE-MANIFEST.sha256` OK on all four files; the manifest's own sha256 is c8ecf7b8273fc1d5a269d548900c85e51c3e9fe7c9effd9e64e8016a05530ff6, as registered. Nothing else under the directory was opened, and no other copy, repository or network source was used.
# METHOD: every figure is re-derived by a script that reads only the two TSVs (comment lines starting with # skipped); the script also asserts that each STATED value is the token on the cited line of the result file, so none of the stated values below is typed from memory. Medians over an even count are the mean of the two middle values; the file's own rounding is kept.

FIGURE | WHERE | STATED | DERIVED | VERDICT | HOW
rows in the table | line 3 | 24 | 24 | CONFIRMED | count of non-# data rows in blockSBS-cells.tsv
columns in the table | line 3 | 25 | 25 | CONFIRMED | count of header fields in blockSBS-cells.tsv
conditions | §1 line 8 | 8 | 8 | CONFIRMED | distinct (problem,arm) pairs
cells | §1 line 8 | 24 | 24 | CONFIRMED | rows
reps per condition | §1 line 8 | 3 | 3 | CONFIRMED | rows per (problem,arm); all equal 3
problems (Paxos note) | §1 line 8 | 4 | 4 | CONFIRMED | distinct problem values (Crc32, FreeList, LRU, LZW)
ENDED: LANDED | §1 run_state line (10) | 21 | 21 | CONFIRMED | count of run_state == ENDED: LANDED
ENDED: CAP-COST | §1 run_state line (10) | 3 | 3 | CONFIRMED | count of run_state == ENDED: CAP-COST
suite PASS | §1 line 10 | 23 | 23 | CONFIRMED | count of suite == PASS
suite BUILD-FAIL | §1 line 10 | 1 | 1 | CONFIRMED | count of suite == BUILD-FAIL
model_served claude-sonnet-5 | §1 line 11 | 24 of 24 | 24 of 24 | CONFIRMED | count of model_served == claude-sonnet-5 over rows (the served-*.out files are not in the bundle)
w1_fenced COVERED | §1 line 12 | 24 of 24 | 24 of 24 | CONFIRMED | count of w1_fenced == COVERED over rows
plain n | §2 table, plain row | 12 | 12 | CONFIRMED | rows with arm == plain
plain retained min | §2 plain row | 0.611 | 0.611 | CONFIRMED | min of retained over plain rows
plain retained max | §2 plain row | 0.984 | 0.984 | CONFIRMED | max of retained over plain rows
plain surv min | §2 plain row | 0.590 | 0.590 | CONFIRMED | min of surv over plain rows
plain surv max | §2 plain row | 0.995 | 0.995 | CONFIRMED | max of surv over plain rows
plain growth min | §2 plain row | 0.89 | 0.89 | CONFIRMED | min of growth over plain rows
plain growth max | §2 plain row | 1.07 | 1.07 | CONFIRMED | max of growth over plain rows
plain end_lines min | §2 plain row | 50 | 50 | CONFIRMED | min of end_lines over plain rows
plain end_lines max | §2 plain row | 206 | 206 | CONFIRMED | max of end_lines over plain rows
salt-diet n | §2 table, salt-diet row | 12 | 12 | CONFIRMED | rows with arm == salt-diet
salt-diet retained min | §2 salt-diet row | 0.101 | 0.101 | CONFIRMED | min of retained over salt-diet rows
salt-diet retained max | §2 salt-diet row | 0.297 | 0.279 | WRONG | max of retained over salt-diet rows (the largest is clbuls02 = 0.279; 0.297 is not a value in the column)
salt-diet surv min | §2 salt-diet row | 0.646 | 0.646 | CONFIRMED | min of surv over salt-diet rows (clbufs02)
salt-diet surv max | §2 salt-diet row | 0.882 | 0.882 | CONFIRMED | max of surv over salt-diet rows (clbuls02)
salt-diet growth min | §2 salt-diet row | 4.66 | 4.66 | CONFIRMED | min of growth over salt-diet rows
salt-diet growth max | §2 salt-diet row | 15.77 | 15.77 | CONFIRMED | max of growth over salt-diet rows
salt-diet end_lines min | §2 salt-diet row | 263 | 263 | CONFIRMED | min of end_lines over salt-diet rows
salt-diet end_lines max | §2 salt-diet row | 3027 | 3027 | CONFIRMED | max of end_lines over salt-diet rows
"worst survival" salt-diet | §2 line 22 | 0.646 | 0.646 | CONFIRMED | min surv, salt-diet
"worst survival" plain | §2 line 22 | 0.590 | 0.590 | CONFIRMED | min surv, plain
REPLACED cells (salt-diet) | §2 line 22 ("SIX") | 6 | 6 | CONFIRMED | count of class == REPLACED in salt-diet rows
growth range quoted | §2 line 23 | 4.66x-15.77x | 4.66x-15.77x | CONFIRMED | min and max growth, salt-diet
end_lines up to | §2 line 23 | 3,027 | 3,027 | CONFIRMED | max end_lines, salt-diet
plain's ceiling | §2 line 23 | 206 | 206 | CONFIRMED | max end_lines, plain
plain class REPAIRED | §2 line 25 ("12/12") | 12/12 | 12/12 | CONFIRMED | count of class == REPAIRED over plain rows
salt-diet class split | §2 line 25 | 6 REPAIRED / 6 REPLACED | 6 REPAIRED / 6 REPLACED | CONFIRMED | class counts over salt-diet rows
plain capped | §3 table (31/line 30-31) | 0 of 12 | 0 of 12 | CONFIRMED | count capped == yes, plain
salt-diet capped | §3 table | 3 of 12 | 3 of 12 | CONFIRMED | count capped == yes, salt-diet
CAPPED threshold | §3 header | 37.21 | 37.21 | CONFIRMED | cap column; all 24 rows carry 37.21 (cap_unit COST)
plain suite | §3 table | PASS 12 · BUILD-FAIL 0 | PASS 12 · BUILD-FAIL 0 | CONFIRMED | suite counts, plain
salt-diet suite | §3 table | PASS 11 · BUILD-FAIL 1 | PASS 11 · BUILD-FAIL 1 | CONFIRMED | suite counts, salt-diet
plain class | §3 table | REPAIRED 12 | REPAIRED 12 | CONFIRMED | class counts, plain
salt-diet class | §3 table | REPAIRED 6 · REPLACED 6 | REPAIRED 6 · REPLACED 6 | CONFIRMED | class counts, salt-diet
capped cells are all FreeList salt-diet | §3 line 33 | 3 | 3 | CONFIRMED | capped rows with problem FreeList and arm salt-diet (of 3 capped)
capped cells passing 7/7 | §3 line 33 ("TWO OF THEM") | 2 | 2 | CONFIRMED | capped rows with suite PASS and tests 7/7
clbufs01 suite/tests/COST | §3 line 34 | PASS 7/7 $38.58 | PASS 7/7 $38.58 | CONFIRMED | clbufs01: suite, tests, final_COST rounded to 2 dp
clbufs02 suite/tests/COST | §3 line 34 | BUILD-FAIL 0/0 $37.46 | BUILD-FAIL 0/0 $37.46 | CONFIRMED | clbufs02: suite, tests, final_COST rounded to 2 dp
clbufs03 suite/tests/COST | §3 line 34 | PASS 7/7 $37.60 | PASS 7/7 $37.60 | CONFIRMED | clbufs03: suite, tests, final_COST rounded to 2 dp
cap rate wording | §3 line 36 | 3 of 12 salt-diet, 0 of 12 plain | 3 of 12 salt-diet, 0 of 12 plain | CONFIRMED | capped counts by arm
plain median COST | §4 plain row | $1.54 | $1.54 | CONFIRMED | median of final_COST over 12 plain rows (mean of the 6th and 7th: 1.5196 and 1.5639 = 1.54175)
salt-diet median COST | §4 salt-diet row | $7.25 | $7.25 | CONFIRMED | median of final_COST over 12 salt-diet rows (mean of 5.5829 and 8.9140 = 7.24845)
plain total COST | §4 plain row | $19.69 | $19.69 | CONFIRMED | sum of final_COST over plain rows = 19.6859
salt-diet total COST | §4 salt-diet row | $188.69 | $188.69 | CONFIRMED | sum of final_COST over salt-diet rows = 188.6926
plain total T | §4 plain row | 37,112,938 | 37,112,938 | CONFIRMED | sum of final_T over plain rows
salt-diet total T | §4 salt-diet row | 637,280,728 | 637,280,728 | CONFIRMED | sum of final_T over salt-diet rows
plain capped | §4 plain row | 0 of 12 | 0 of 12 | CONFIRMED | count capped == yes, plain
salt-diet capped | §4 salt-diet row | 3 of 12 | 3 of 12 | CONFIRMED | count capped == yes, salt-diet
ratio, median COST | §4 ratio row | 4.71x | 4.71x | CONFIRMED | 7.25 / 1.54 as printed = 4.7078; ON UNROUNDED medians 7.24845/1.54175 = 4.7014 -> 4.70x. The file's own rounding is taken to be ratio-of-printed-figures (see the next row, which only comes out right that way)
ratio, total COST | §4 ratio row | 9.58x | 9.58x | CONFIRMED | 188.69 / 19.69 as printed = 9.5830; ON UNROUNDED totals 188.6926/19.6859 = 9.5852 -> 9.59x
ratio, total T | §4 ratio row | 17.17x | 17.17x | CONFIRMED | 637,280,728 / 37,112,938 = 17.1714 (integers, no rounding ambiguity)
plain median T | §T line 76 | 2,551,108 | 2,551,108 | CONFIRMED | median of final_T over plain rows (mean of the 6th and 7th; the mean is an exact integer)
salt-diet median T | §T line 77 | 18,401,035 | 18,401,035.5 | CONFIRMED | median of final_T over salt-diet rows = mean of the 6th and 7th = 18,401,035.5; the file prints the integer part. The file states no rule for a .5, so this is CONFIRMED to the file's precision; half-up would print 18,401,036
plain median COST (§T) | §T line 76 | $1.54 | $1.54 | CONFIRMED | as §4
plain total COST (§T) | §T line 76 | $19.69 | $19.69 | CONFIRMED | as §4
plain total T (§T) | §T line 76 | 37,112,938 | 37,112,938 | CONFIRMED | as §4
salt-diet median COST (§T) | §T line 77 | $7.25 | $7.25 | CONFIRMED | as §4
salt-diet total COST (§T) | §T line 77 | $188.69 | $188.69 | CONFIRMED | as §4
salt-diet total T (§T) | §T line 77 | 637,280,728 | 637,280,728 | CONFIRMED | as §4
Paxos x statement INEXPRESSIBLE (§C4) | §1 line 8 | "INEXPRESSIBLE (§C4)" | - | NOT DERIVABLE | the tables carry only Crc32, FreeList, LRU, LZW and no Paxos row; why Paxos is absent (§C4) is not in these files
three blocks show the shape (SB §5, O §3, here) and surv overlapped in the first two | §2 line 24 | "three blocks" / "overlapped" | - | NOT DERIVABLE | only this block's table is in the bundle; blocks SB and O are other files
cap appears for the THIRD time (blocks SG, SS, here) | §3 line 36 | "THIRD time" | - | NOT DERIVABLE | blocks SG and SS are not in the bundle; this block's own count (3 of 12 salt-diet, 0 of 12 plain) is derived above
blocks_stepg.py reproduces every median and total dollar figure | §T lines 72-74 | "reproduces every median and total" | - | NOT DERIVABLE | the script and blocks_stepg.tsv are not in the bundle; I re-derived every §4 and §T median and total from the cells table myself (rows above) and they match
model derived per cell from its own served-*.out | §1 line 11 | "derived per cell from its own served-*.out" | - | NOT DERIVABLE | the served-*.out files are not in the bundle; only the model_served column is, and it reads claude-sonnet-5 on 24 of 24 (row above)

## CONTRADICTED PROSE CLAIMS
1. §2 line 23: "THE ARM `retained` CALLS 'REWRITTEN WHOLESALE' IS THE ARM THAT PRESERVED MORE OF THE SEED." Contradicted by the tables on every measure except the single worst cell: median surv is 0.980 for plain and 0.810 for salt-diet; kept lines are 1,228 of 1,332 seed lines for plain and 1,027 of 1,332 for salt-diet; and per problem plain's surv is higher on Crc32 (clbucp01-03: 0.980 x3 against clbucs01-03: 0.800, 0.820, 0.860), on FreeList (clbufp01-03: 0.984, 0.995, 0.974 against clbufs01-03: 0.849, 0.646, 0.854) and on LRU (clbulp01-03: 0.990 x3 against clbuls01-03: 0.824, 0.882, 0.676); on LZW plain's median is 0.700 against 0.680 (clbuzp01-03: 0.700, 0.820, 0.590 against clbuzs01-03: 0.740, 0.670, 0.680). What the tables DO support is the narrower statement in the title and line 22: salt-diet's WORST surv (0.646, clbufs02) is higher than plain's worst (0.590, clbuzp03), and its whole surv range sits inside plain's; that floor comparison turns on the three LZW plain cells, and does not make salt-diet "preserve more".

## NOTES (not counted above; findings I am not certain enough to call contradictions)
- §5 item 4 says surv is a lower bound "which makes §2's claim conservative: the true survival gap can only be larger in salt-diet's favour". The tables do not carry what would settle this: the lower-bound shortfall is not given per arm, and salt-diet's end files are 5x to 15x longer, so the matched-line undercount need not be equal across arms. Not contradicted by the tables; not supported by them either.
- §6 (outside the sections I was asked to check) says class and retained agree between the scorer and the decomposition for all 24 cells. I can confirm only that the two TSVs agree with each other on retained, surv, growth, seed_lines, end_lines, kept, class and end_from for all 24 cells (no mismatch).
- The two ratios 4.71x and 9.58x in §4 come out only as the ratio of the PRINTED dollar figures (7.25/1.54, 188.69/19.69); on the unrounded medians and totals they would print 4.70x and 9.59x. I counted them CONFIRMED under the file's own rounding and say so here.

SUMMARY: 75 figures checked · 69 CONFIRMED · 1 WRONG · 5 NOT DERIVABLE · 1 contradicted claims
