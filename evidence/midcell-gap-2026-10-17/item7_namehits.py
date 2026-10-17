#!/usr/bin/env python3
"""item7_namehits.py < exposed.tsv — item 7 (b) (bench, relight 149). Zero spend; runs ON THE RUN BOX; reads, never writes a cell.
stdin rows: model <TAB> cell <TAB> root <TAB> born_inside (comma-separated root names).
For each EXPOSED record cell, the haystack is (1) every file under its own ctl/ (watch/launch logs, the agy lane's stream-*.ndjson, hook
logs) and (2) for a Claude cell, every session jsonl of the cell's slug found under ANY ~/.claude* config dir (pools moved during the
pilot, so the dir is searched for, never assumed). Each born-inside root's NAME is counted in that haystack.
CONTROLS, printed per cell, both must be > 0 or the row is VOID (never clean): ctl bytes; and the cell's own id counted in the haystack.
For a Claude cell, transcript bytes = 0 is printed as NO-TRANSCRIPT: the ctl half was still read, so the row is a FLOOR, not a zero.
"""
import glob, os, sys

H = os.path.expanduser("~")


def slurp(paths):
    b = bytearray()
    for p in paths:
        try:
            with open(p, "rb") as f:
                b += f.read() + b"\n"
        except OSError:
            pass
    return bytes(b)


def main():
    print("#(ctl_bytes and the name hits EXCLUDE the cell's own fence renders; FENCED k/n = k of its n born-inside roots are on its own deny list)")
    print("#model\tcell\troot\tctl_bytes\ttranscript_bytes\ttranscript_dirs\town_id_hits\tverdict\tname_hits")
    for line in sys.stdin:
        if not line.strip() or line.startswith("#"):
            continue
        model, cell, root, inside = (line.rstrip("\n").split("\t") + [""] * 4)[:4]
        cd = os.path.join(H, root, cell)
        FENCE = ("fence.json", "srt-settings.json")   # the cell's OWN deny-list renders: a name there means DENIED, never a read
        files = [p for p in glob.glob(cd + "/ctl/**", recursive=True) if os.path.isfile(p)]
        fence = slurp(p for p in files if os.path.basename(p) in FENCE)
        ctl = slurp(p for p in files if os.path.basename(p) not in FENCE)
        tr, dirs = b"", []
        if model.startswith("claude"):
            slug = (cd + "/repo").replace("/", "-").replace(".", "-")
            dirs = [d for d in glob.glob(H + "/.claude*/projects/" + slug) if os.path.isdir(d)]
            tr = slurp(p for d in dirs for p in glob.glob(d + "/**/*.jsonl", recursive=True))
        hay = ctl + tr
        own = hay.count(cell.encode())
        names = [n for n in inside.split(",") if n]
        fenced = [n for n in names if n.encode() in fence]
        hits = {n: hay.count(n.encode()) for n in names}
        if not ctl or not own:
            v = "VOID"
        elif model.startswith("claude") and not tr:
            v = "NO-TRANSCRIPT(floor)"
        else:
            v = ("NAMED" if any(hits.values()) else "NOT-NAMED") + ("+FENCED:%d/%d" % (len(fenced), len(names)) if fenced else "")
        print("\t".join([model, cell, root, str(len(ctl)), str(len(tr)), ",".join(os.path.basename(os.path.dirname(os.path.dirname(d))) for d in dirs) or "-",
                         str(own), v, ",".join("%s=%d" % kv for kv in hits.items())]))


if __name__ == "__main__":
    main()
