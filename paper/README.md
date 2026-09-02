# paper/ — SaltBench v1

`saltbench-v1.tex` is the arXiv source (cs.LO, cross-list cs.SE and cs.AI). Every number in it
carries a `\src{...}` comment naming the file in this repository it was copied from; the macro
expands to nothing in the PDF, so the sources travel with the text and never print.

Build:

```
cd paper && tectonic saltbench-v1.tex
```

(any pdflatex with booktabs, enumitem, microtype and hyperref also works: `pdflatex saltbench-v1.tex` twice).
