#!/usr/bin/env python3
"""copies_census.py — flattened phrase census at a git ref: every sentence that says a web tool was denied,
or that no web result was served / no web was used. Files are read with `git show <ref>:<path>`, whitespace
flattened (hard wraps undone), and each window of +-220 chars around a needle hit is printed with the file and
the source line number of the hit.

usage: copies_census.py <repo> <ref> [--paths-glob ...]
"""
import re, subprocess, sys

repo, ref = sys.argv[1], sys.argv[2]
NEEDLES = [  # case-insensitive regexes over the flattened text
    r"denied by (the )?(canonical )?hook", r"hook (denied|refused|blocked)", r"canonical hook",
    r"network[- ]tool results? (were |was )?served", r"0 network[- ]tool", r"no network[- ]tool",
    r"search_web", r"read_url_content", r"web[- ]deny", r"agy_web_deny",
    r"\b0 web\b", r"no web (call|search|access|result|retriev)", r"web (calls?|searches|access|retrieval|route)",
    r"(could not|cannot|can't) (search|reach) the web", r"without (the )?web", r"retriev(ing|al) rather than solv",
    r"internet",
]
rx = re.compile("|".join(f"(?:{n})" for n in NEEDLES), re.I)
files = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", ref], capture_output=True, text=True,
                       check=True).stdout.split("\n")
files = [f for f in files if re.search(r"\.(md|tex|txt|tsv|py|sh)$", f)]
nhit = nfile = 0
for f in files:
    raw = subprocess.run(["git", "-C", repo, "show", f"{ref}:{f}"], capture_output=True).stdout
    s = raw.decode("utf-8", "replace")
    # map flattened offsets back to line numbers
    flat, lines_at = [], []
    line = 1
    prev_space = False
    for ch in s:
        if ch.isspace():
            if not prev_space:
                flat.append(" "); lines_at.append(line)
            prev_space = True
        else:
            flat.append(ch); lines_at.append(line); prev_space = False
        if ch == "\n":
            line += 1
    t = "".join(flat)
    hits = list(rx.finditer(t))
    if not hits:
        continue
    nfile += 1
    last_end = -1
    for m in hits:
        if m.start() < last_end:
            continue
        a, b = max(0, m.start() - 220), min(len(t), m.end() + 220)
        last_end = b
        nhit += 1
        print(f"{f}:{lines_at[m.start()]}\t[{m.group(0)}]\t{t[a:b]}")
print(f"#CENSUS ref={ref} files_scanned={len(files)} files_hit={nfile} windows={nhit}")
