#!/usr/bin/env python3
"""rates_reread.py <prompt-caching.md> <rates.tsv> -- the release re-read of rates.tsv against the public page it cites.
Reads the page's "Prompt caching pricing" table rows for the models this lane's cells are served (Claude Opus 5, Claude
Sonnet 5, Claude Fable 5.1), takes each row's dollar figures IN COLUMN ORDER (base input, 5m cache write, 1h cache write,
cache read, output), and compares them to rates.tsv's row for the served id. Prints the page's size and sha256/16 so the
reading names the bytes it read. rc 0 only if every row is found on both sides and every figure is equal; a row missing
on either side is MISSING, never equal."""
import hashlib, re, sys
page_b = open(sys.argv[1], "rb").read(); page = page_b.decode("utf-8", "replace")
ROWS = {"Claude Opus 5": "claude-opus-5", "Claude Sonnet 5": "claude-sonnet-5", "Claude Fable 5.1": "claude-fable-5-1"}
COLS = ("input", "cache_write_5m", "cache_write_1h", "cache_read", "output")
rates = {}
for line in open(sys.argv[2]):
    if line.startswith("#") or line.startswith("model\t") or not line.strip(): continue
    f = line.rstrip("\n").split("\t"); rates[f[0]] = [float(x) for x in f[1:6]]
print("page %d B sha256/16 %s" % (len(page_b), hashlib.sha256(page_b).hexdigest()[:16]))
ok = True
for name, sid in ROWS.items():
    cells = None
    for line in page.splitlines():
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) >= 6 and parts[0] == name:
            cells = parts[1:6]; break
    if cells is None or sid not in rates:
        print("%s\tMISSING (page row %s · rates row %s)" % (sid, "found" if cells else "absent", "found" if sid in rates else "absent")); ok = False; continue
    page_v = [float(re.search(r"\$([0-9.]+)", c).group(1)) for c in cells]
    eq = page_v == rates[sid]
    ok = ok and eq
    print("%s\t%s\tpage %s\trates %s" % (sid, "EQUAL" if eq else "DIFFERS", " · ".join("%g" % v for v in page_v), " · ".join("%g" % v for v in rates[sid])))
print("VERDICT %s" % ("ALL-EQUAL" if ok else "NOT-EQUAL"))
sys.exit(0 if ok else 1)
