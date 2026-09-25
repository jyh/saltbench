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
