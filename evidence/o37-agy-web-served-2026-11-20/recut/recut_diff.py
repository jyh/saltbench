#!/usr/bin/env python3
"""recut_diff.py — print every table row that moves between a table tool's output on the cell map of record (OLD) and on
the same map with the WEB-SERVED cells marked '#EXCLUDED-BY-RECORD' (NEW), the old line beside the new one.

Rows are keyed by (section heading, the row's LABEL = its non-figure fields, and the occurrence number of that key in the
section; K > 0 keys by the first K fields instead); a key in one file only is printed as GONE or ADDED. Separator rows (|---|) are skipped.
usage: recut_diff.py OLD.md NEW.md LABEL [K]
"""
import collections, re, sys

old, new, label = sys.argv[1], sys.argv[2], sys.argv[3]


def rows(p):
    out, head = [], "-"
    for l in open(p, encoding="utf-8"):
        l = l.rstrip("\n")
        if l.startswith("#"):
            head = l
        elif l.startswith("|") and not set(l.replace("|", "").strip()) <= set("-: "):
            out.append((head, l))
    return out


def fields(l):
    return [f.strip() for f in l.strip().strip("|").split("|")]


NUMERIC = re.compile(r"^[\s≥≤~<>=+\-—–.,%×/†‡*0-9]*$|^(unmeasured|declared|-|—)$", re.I)


def row_label(l):
    # the row's LABEL: its fields that are not figures (a figure, a dash or 'unmeasured' is a value, not a label)
    return tuple(f for f in fields(l) if not NUMERIC.match(f))


def keyed(rs, k):
    # a key repeated within a section gets its occurrence number, so duplicates pair in order
    d, seen = collections.OrderedDict(), collections.Counter()
    for h, l in rs:
        base = (h, row_label(l)) if k == 0 else (h, tuple(fields(l)[:k]))
        seen[base] += 1
        d[base + (seen[base],)] = l
    return d


a, b = rows(old), rows(new)
k = int(sys.argv[4]) if len(sys.argv) > 4 else 0
da, db = keyed(a, k), keyed(b, k)
moved = gone = added = 0
last = None


def sec(h):
    global last
    if h != last:
        print(f"\n{h}")
        last = h


for key, la in da.items():
    lb = db.get(key)
    if lb is None:
        gone += 1; sec(key[0]); print(f"  GONE {la}")
    elif la != lb:
        moved += 1; sec(key[0]); print(f"  OLD  {la}"); print(f"  NEW  {lb}")
for key, lb in db.items():
    if key not in da:
        added += 1; sec(key[0]); print(f"  ADDED {lb}")
print(f"\n#RECUT {label}: key width {k}; old {len(a)} rows, new {len(b)}; moved {moved}, gone {gone}, added {added}")
