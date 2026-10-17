#!/usr/bin/env python3
"""inroot.py < record-cells (cell<TAB>root<TAB>start<TAB>end) — item 7, relight 149. Runs ON THE RUN BOX, read-only.
The IN-ROOT form of the mid-cell gap (systems item 15): a SIBLING cell dir born inside the cell's own root strictly inside its window.
Each such sibling's id is counted in the cell's own record (ctl/ minus its fence renders, plus any Claude transcript of its slug)."""
import glob, os, sys
H = os.path.expanduser("~"); FENCE = ("fence.json", "srt-settings.json")
def slurp(ps):
    b = b""
    for p in ps:
        try: b += open(p, "rb").read()
        except OSError: pass
    return b
print("#cell\troot\tsiblings_born_inside\tverdict\tsibling_hits")
for l in sys.stdin:
    cell, root, s, e = l.rstrip("\n").split("\t")[:4]
    s, e = float(s), float(e)
    sib = []
    for d in glob.glob(os.path.join(H, root, "*")):
        n = os.path.basename(d)
        if n == cell or n.startswith("_") or not os.path.isdir(d): continue
        bt = os.stat(d).st_birthtime
        if s < bt < e: sib.append(n)
    if not sib:
        print("%s\t%s\t0\tNONE\t" % (cell, root)); continue
    cd = os.path.join(H, root, cell)
    hay = slurp(p for p in glob.glob(cd + "/ctl/**", recursive=True) if os.path.isfile(p) and os.path.basename(p) not in FENCE)
    slug = (cd + "/repo").replace("/", "-").replace(".", "-")
    # a transcript record of type "attachment" is the CLIENT echoing the cell's own settings (its deny list) into the session: not a read
    for d in glob.glob(H + "/.claude*/projects/" + slug):
        for p in glob.glob(d + "/**/*.jsonl", recursive=True):
            for ln in open(p, "rb"):
                if b'"type":"attachment"' not in ln and b'"type": "attachment"' not in ln: hay += ln
    fence = slurp(p for p in glob.glob(cd + "/ctl/*") if os.path.basename(p) in FENCE)
    fenced = [n for n in sib if ("/" + n + "/").encode() in fence]
    hits = {n: hay.count(n.encode()) for n in sib}
    v = ("NAMED" if any(hits.values()) else "NOT-NAMED") + ("+FENCED:%d/%d" % (len(fenced), len(sib)) if fenced else "")
    print("%s\t%s\t%d\t%s\t%s" % (cell, root, len(sib), v, ",".join("%s=%d" % kv for kv in hits.items())))
