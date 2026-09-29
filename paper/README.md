# paper/ — SaltBench v1

`saltbench-v1.tex` is the arXiv source (cs.LO, cross-list cs.SE and cs.AI). Every number in it
carries a `\src{...}` comment naming the file in this repository it was copied from; the macro
expands to nothing in the PDF, so the sources travel with the text and never print.

Build:

```
cd paper && tectonic saltbench-v1.tex
```

(any pdflatex with booktabs, enumitem, microtype and hyperref also works: `pdflatex saltbench-v1.tex` twice).

Version 2 of the report adds the complete pilot matrix. Its table is derived, not typed:
`matrix_census_table.py` reads the matrix census's live row, checks the twenty rows against it, and
with `--check` refuses if the rows in the tex differ from what it derives.

Its four descriptive tables (Section 5.2) are copied, not typed: `descriptive_tables.py` parses them
from `harness/systems-v3/RESULT-descriptive-tables-v2-2026-09-27.md`, prints the LaTeX rows, and with
`--check` refuses if the rows in the tex differ from the result file (`--self-test` perturbs one digit and
requires the refusal).

Version 3 adds the same matrix in modelled list-price dollars and in wall time (Section 5.3), and the
Opus head-versus-subagent split (Appendix S1). Those eleven blocks are copied the same way:
`cost_tables.py` parses them from `harness/systems-v3/RESULT-cost-tables-v3-2026-09-29.md`, and
`--check` refuses on any difference (`--self-test` perturbs one dollar, one wall and one share digit).
