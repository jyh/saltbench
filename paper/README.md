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

Version 3 also reads the matrix for correctness (Section 5.4, Tables P1–P4, declared post hoc). Those six
blocks are copied the same way: `correctness_tables.py` parses them from
`harness/systems-v3/RESULT-correctness-tables-v3-2026-10-01.md`, `--check` refuses on any difference, and
`--self-test` perturbs one pass count and one sign.

Version 4 corrects Tables T1–T4 (O57): the Gemini lane's meter had read each cell's parent conversation and none of its
sub-agent conversations. `descriptive_tables.py` now copies from
`harness/systems-v3/RESULT-descriptive-tables-v2-O57-remeter-2026-10-13.md`, printed by the same `tables_v2.py` with
`--add-T`; `harness/systems-v3/DIFF-O57-remeter-2026-10-13.md` lists every changed row against version 3's file, which
stays as printed. No Claude row changes and no fixed sign flips. The dollar and wall tables are not re-computed; the
Gemini dollars carry the declared O57 limit.
