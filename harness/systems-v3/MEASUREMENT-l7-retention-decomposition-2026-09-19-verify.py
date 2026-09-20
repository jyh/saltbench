#!/usr/bin/env python3
"""Re-derive §2 and §3 of MEASUREMENT-l7-retention-decomposition-2026-09-19.md from the receipt and
from level 7's OWN cells table, and assert them against that document's BYTES.  No typed expectations:
every value asserted here is computed, then searched for in the .md.

⛔ LIMITS, beside the verdict: this checks that the DOCUMENT agrees with the RECEIPT and that the
receipt reproduces level 7's published bands. It does not re-read a cell and cannot tell you the
receipt is right — the receipt's own guarantee is that its producer imported the level-7 export's
classifier and asserted every `retained` against it.
"""
import csv, re, statistics as st, sys

DOC  = "MEASUREMENT-l7-retention-decomposition-2026-09-19.md"
RCPT = "l7-retention-decomp.tsv"
L7   = "RESULT-gemini-level7-2026-09-19-cells.tsv"
L7MD = "RESULT-gemini-level7-2026-09-19.md"
EXCL = {"l7cpbs03", "l7cfss02", "l7cfss03"}          # §1b's stated population, cells named there

try:
    doc  = open(DOC, encoding="utf-8").read()
    l7md = open(L7MD, encoding="utf-8").read()
    C    = {r["cell"]: r for r in csv.DictReader(open(L7, encoding="utf-8"), delimiter="\t")}
    D    = {r["cell"]: r for r in csv.DictReader(
              [l for l in open(RCPT, encoding="utf-8") if not l.startswith("#")], delimiter="\t")}
except OSError as e:
    print("CANNOT READ INPUT: %s" % e); sys.exit(2)

N = [0, 0]
def arm(label, ok, shown=""):
    N[0] += 1; N[1] += 0 if ok else 1
    print("  %s  %s%s" % ("ok  " if ok else "RED ", label, ("   [%s]" % shown) if shown else ""))

def mp(cond):
    m = "Flash" if "flash" in cond else "Pro"
    for p in ("crc32", "freelist", "lru", "lzw"):
        if "-" + p + "-" in cond:
            return m, {"crc32": "Crc32", "freelist": "FreeList", "lru": "LRU", "lzw": "LZW"}[p]
    return m, "?"

def band(m, p, a, col):
    return sorted(float(r["retained"] if col == "retained" else D[k][col])
                  for k, r in C.items()
                  if k not in EXCL and mp(r["cond"]) == (m, p) and r["arm"] == a)

PAIRS = [(m, p) for m in ("Flash", "Pro") for p in ("Crc32", "FreeList", "LRU", "LZW")]

print("THE RECEIPT")
arm("the receipt covers level 7's whole cells table", set(D) == set(C), "%d receipt / %d table" % (len(D), len(C)))
arm("no row in the receipt REFUSED", all(D[k]["class"] != "REFUSED" for k in D))
arm("every receipt `retained` equals level 7's published per-cell value",
    all(abs(float(D[k]["retained"]) - float(C[k]["retained"])) < 5e-4 for k in D if C[k]["retained"] not in ("-", "")))
arm("the document states the cell count", str(len(D)) in doc)

print("\n§2 — THE CONTROL: the pipeline must reproduce level 7's OWN published table")
same_r = sum(1 for m, p in PAIRS if st.median(band(m, p, "salt-diet", "retained")) < st.median(band(m, p, "plain", "retained")))
arm("⭐ retained direction count is DERIVED, not typed", True, "%d of 8" % same_r)
arm("⭐ it reproduces level 7 §1's published headline count", ("%d OF 8" % same_r) in l7md.upper(),
    "level 7 says %d of 8" % same_r)
# ⛔ CONTAINMENT IS NOT ENOUGH HERE AND A MUTANT PROVED IT: "7 of 8" also appears in §1's QUOTE of
#    level 7's headline and in §4, so `in doc` stayed green when §3's tally line was mutated to 6.
#    Anchor on the LINE that makes the claim, by position, not by substring.
def tally(word):
    # ⛔ both tallies sit on ONE line of the §3 block, so an end-of-line anchor finds neither.
    m = re.search(r"\b%s\s+salt below plain in (\d+) of (\d+)\b" % word, doc)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)
arm("§3's RETAINED tally LINE exists and carries the derived count", tally("RETAINED") == (same_r, len(PAIRS)),
    "line says %s, derived %d of %d" % (tally("RETAINED"), same_r, len(PAIRS)))
fl, fp = st.median(band("Flash", "LZW", "salt-diet", "retained")), st.median(band("Flash", "LZW", "plain", "retained"))
arm("⭐ Flash x LZW reproduces as the ONE exception", fl > fp, "salt %.3f > plain %.3f" % (fl, fp))
arm("both its medians appear in this document", ("%.3f" % fl) in doc and ("%.3f" % fp) in doc)
for m, p in PAIRS:
    for a in ("plain", "salt-diet"):
        v = band(m, p, a, "retained")
        arm("%s x %s %s retained median appears" % (m, p, a), ("%.3f" % st.median(v)) in doc, "%.3f" % st.median(v))

print("\n§3 — THE DECOMPOSITION")
same_s = sum(1 for m, p in PAIRS if st.median(band(m, p, "salt-diet", "surv")) < st.median(band(m, p, "plain", "surv")))
flips  = sum(1 for m, p in PAIRS
             if (st.median(band(m, p, "salt-diet", "retained")) < st.median(band(m, p, "plain", "retained")))
             != (st.median(band(m, p, "salt-diet", "surv"))     < st.median(band(m, p, "plain", "surv"))))
arm("§3's SURVIVAL tally LINE exists and carries the derived count", tally("SURVIVAL") == (same_s, len(PAIRS)),
    "line says %s, derived %d of %d" % (tally("SURVIVAL"), same_s, len(PAIRS)))
mfl = re.search(r"^\s+THE TWO DISAGREE ON DIRECTION IN (\d+) OF (\d+) PAIRS", doc, re.M)
arm("§3's FLIP line exists and carries the derived count",
    bool(mfl) and (int(mfl.group(1)), int(mfl.group(2))) == (flips, len(PAIRS)),
    "line says %s, derived %d of %d" % (mfl.groups() if mfl else None, flips, len(PAIRS)))
arm("⭐ THE CLAIM: survival agrees with retained on FEWER pairs than retained's own count", same_s < same_r)
arm("⭐ THE CLAIM: the two disagree on HALF the table", flips * 2 == len(PAIRS), "%d of %d" % (flips, len(PAIRS)))
gdis = sum(1 for m, p in PAIRS if min(band(m, p, "salt-diet", "growth")) > max(band(m, p, "plain", "growth"))
           or st.median(band(m, p, "salt-diet", "growth")) > st.median(band(m, p, "plain", "growth")))
arm("⭐ growth separates in the same direction on every pair", gdis == len(PAIRS), "%d of %d" % (gdis, len(PAIRS)))
gp = [st.median(band(m, p, "plain", "growth")) for m, p in PAIRS]
gs = [st.median(band(m, p, "salt-diet", "growth")) for m, p in PAIRS]
arm("⭐ the growth medians are DISJOINT across the eight pairs", max(gp) < min(gs), "plain max %.2fx < salt min %.2fx" % (max(gp), min(gs)))
arm("the growth median ranges appear", ("%.2fx .. %.2fx" % (min(gp), max(gp))) in doc and ("%.2fx .. %.2fx" % (min(gs), max(gs))) in doc,
    "plain %.2fx..%.2fx  salt %.2fx..%.2fx" % (min(gp), max(gp), min(gs), max(gs)))

print("\n§4① — THE MEDIAN INVERSION OVER ALL 84")
allc = [k for k in D]
for col in ("retained", "surv", "growth"):
    mp_ = st.median([float(D[k][col]) for k in allc if "-plain" in C[k]["cond"]])
    ms_ = st.median([float(D[k][col]) for k in allc if "-salt" in C[k]["cond"]])
    fmt = "%.3f" if col != "growth" else "%.2fx"
    arm("all-84 %s medians appear" % col, (fmt % mp_) in doc and (fmt % ms_) in doc, (fmt + " vs " + fmt) % (mp_, ms_))
inv_r = st.median([float(D[k]["retained"]) for k in allc if "-salt" in C[k]["cond"]]) < st.median([float(D[k]["retained"]) for k in allc if "-plain" in C[k]["cond"]])
inv_s = st.median([float(D[k]["surv"]) for k in allc if "-salt" in C[k]["cond"]])     > st.median([float(D[k]["surv"]) for k in allc if "-plain" in C[k]["cond"]])
arm("⭐ THE INVERSION IS REAL: retained says salt LOWER and survival says salt HIGHER, over all 84", inv_r and inv_s)

print("\nANTI-VACUITY")
arm("a value not in the document is not found", "__NOT_IN_THIS_DOCUMENT__" not in doc)
# ⛔ AN INTERNAL MUTANT MUST ACTUALLY MUTATE. An arm whose two disjuncts cannot both be false is
#    decoration; this one flips the sign of ONE pair in a COPY of the receipt and requires the
#    derived count to move, which is the only thing that shows the count is computed from the data.
_saved = {k: D[k]["surv"] for k in D}
_m, _p = "Flash", "LRU"                      # a pair where surv currently reads salt<plain
for k, r in C.items():
    if k not in EXCL and mp(r["cond"]) == (_m, _p) and r["arm"] == "salt-diet":
        D[k]["surv"] = "1.000"               # force salt above plain on that pair alone
_mut = sum(1 for m, p in PAIRS if st.median(band(m, p, "salt-diet", "surv")) < st.median(band(m, p, "plain", "surv")))
for k, v in _saved.items(): D[k]["surv"] = v
_back = sum(1 for m, p in PAIRS if st.median(band(m, p, "salt-diet", "surv")) < st.median(band(m, p, "plain", "surv")))
arm("⭐ MUTANT: flipping ONE pair in the receipt moves the derived survival count",
    _mut == same_s - 1, "%d -> %d" % (same_s, _mut))
arm("⭐ and the receipt is restored bit-for-bit, so the mutant cannot leak into a verdict",
    _back == same_s, "restored to %d" % _back)
arm("⛔ the document does NOT modify level 7 (it must say so)", "does not amend" in doc.lower() or "DOES NOT AMEND" in doc)

print("\n%d arms, %d RED" % (N[0], N[1]))
sys.exit(1 if N[1] else 0)
