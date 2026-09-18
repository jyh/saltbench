#!/usr/bin/env python3
"""withheld_exposure_census.py --claude-fence <ctl/fence.json> --agy-fence <ctl/srt-settings.json>

Which withheld-carrying trees in $HOME does each lane's CURRENT fence deny at the OS layer (sandbox denyRead)?
Walks $HOME read-only (skipping cells*, .claude*, Library and toolchain caches; depth <= 7) for entries named
`withheld`, `mutants` or `BROWNFIELD-PLANTS.tsv`, groups them by top-level tree, and tests one entry per tree against
each fence's denyRead by realpath prefix. Paths print relative to ~ so no account or host name reaches the output.
LIMITS, printed with the verdict: depth 7; tarballs and cells roots are not opened; a withheld file saved under another
name is invisible to a name walk. The count is a FLOOR on the population. The HOOK layer is not measured here.

RELEASE COPY (Claude lane (B), 2026-09-16), differing from evidence/hc1-stage1-instruments-2026-09-16/exposure/ ONLY by
the guard below and the host-role line it prints: a census of $HOME names no host, so on a machine that holds no cells it
would print a clean, empty table. It REFUSES instead when $HOME holds no cells-* root. The original is unchanged because it
backs a published MANIFEST digest.
"""
import argparse, collections, json, os

NAMES = {"withheld", "mutants", "BROWNFIELD-PLANTS.tsv"}
SKIP_TOP = ("cells", "Library", ".Trash", ".cargo", ".rustup", ".claude")


def deny_of(path):
    d = json.load(open(path))
    fs = d.get("filesystem") or d.get("sandbox", {}).get("filesystem", {}) or {}
    return [os.path.realpath(os.path.expanduser(e)).rstrip("/") for e in fs.get("denyRead", [])]


def covered(deny, t):
    t = os.path.realpath(t)
    return any(t == r or t.startswith(r + os.sep) for r in deny)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--claude-fence", required=True)
    ap.add_argument("--agy-fence", required=True)
    a = ap.parse_args()
    home = os.path.expanduser("~")
    ncells = sum(1 for d in os.listdir(home) if d.startswith("cells-") and os.path.isdir(os.path.join(home, d)))
    if ncells == 0:
        raise SystemExit("REFUSE: no cells-* root under ~ -- this is not the box the cells ran on, and a census here would read clean")
    found = []
    for top in sorted(os.listdir(home)):
        p = os.path.join(home, top)
        if top.startswith(SKIP_TOP) or not os.path.isdir(p) or os.path.islink(p):
            continue
        for dp, dns, fns in os.walk(p):
            if dp.count(os.sep) - home.count(os.sep) > 7:
                dns[:] = []
                continue
            dns[:] = [d for d in dns if d not in (".git", "target", "node_modules", "registry")]
            found += [os.path.join(dp, n) for n in list(dns) + fns if n in NAMES]
            if "withheld" in dns:
                dns.remove("withheld")
    claude, agy = deny_of(a.claude_fence), deny_of(a.agy_fence)
    tops = collections.OrderedDict()
    for f in found:
        tops.setdefault(f[len(home) + 1:].split("/")[0], []).append(f)
    rel = lambda p: "~/" + os.path.relpath(p, home)
    print("# host role: the run box (cells-* roots under ~: %d)" % ncells)
    print("# fences: claude %s (denyRead %d) · agy %s (denyRead %d)" % (rel(a.claude_fence), len(claude), rel(a.agy_fence), len(agy)))
    print("# withheld-shaped entries: %d in %d top-level trees (a FLOOR: depth 7, no tarballs, name-based)" % (len(found), len(tops)))
    print("tree\tentries\tclaude\tagy")
    for t, fs in sorted(tops.items(), key=lambda x: -len(x[1])):
        print("~/%s\t%d\t%s\t%s" % (t, len(fs), "COVERED" if covered(claude, fs[0]) else "NOT-COVERED",
                                    "COVERED" if covered(agy, fs[0]) else "NOT-COVERED"))


if __name__ == "__main__":
    main()
