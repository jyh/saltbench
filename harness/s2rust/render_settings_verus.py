#!/usr/bin/env python3
"""render_settings_verus.py — the AGENT's Seatbelt fence, RENDERED PER RUN from `$BENCH`. Row CO, built in.

⛔⛔ WHY THIS IS A TEMPLATE AND NOT A FILE. `settings.s2.json` — S2-Lean's agent fence — names `~/bench`
STATICALLY. Since 08/31 this campaign runs each new regime in its OWN state root (`~/bench-a8`, `~/bench-c`,
`~/bench-aw`), and `/Users/jyh/bench-a8` is a SIBLING of `/Users/jyh/bench`, not a child of it, so a subpath
deny on `~/bench` does not reach it. The landed record stayed safe only by an ACCIDENT of how those roots
were built (their `s2views` were symlinks resolving back into the denied subpath) and by the hook layer,
whose escape pattern happens to match `bench-*`.
  ⇒ 🔑 A FENCE THAT NAMES A PATH INSTEAD OF DERIVING ONE STOPS PROTECTING THE DAY THE WORK MOVES — and the
    move that broke it was a repair, adopted for good reasons, whose blast radius nobody re-measured.

S2-Lean's file is deliberately NOT edited (201 landed episodes ran under it and stage C is still frozen
against it). The S2-Rust regime instead gets the derived form FROM ITS FIRST LINE, so row CO never has to be
re-fixed here.

⛔ AN UNSET `$BENCH` IS A REFUSAL, NOT A DEFAULT. Falling back to `~/bench` would silently reinstate exactly
the defect this repairs, and it would do it at the moment a new root was introduced — the one moment the
fence matters most. The same rule as `check_verus.deny_read_paths`.

⛔ WHAT IS PINNED IS THE TEMPLATE, NOT THE RENDERING. The rendering contains the run's own root, so its sha
varies per run and cannot be a constant in `HASHES.txt` — the same reason `hashes.sh` pins the `__EP__` form
of a rendered prompt rather than the substituted one. `--check` re-derives the rendering from the pinned
template and requires the file on disk to EQUAL it byte for byte, which asserts the substitution AND the
template in one comparison.

usage: render_settings_verus.py --bench <root> [--hook <path>] [--out <file>]
       render_settings_verus.py --check <file> --bench <root> [--hook <path>]
"""
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "settings.s2rust.template.json")

# The credential/config trees, plus — DERIVED — the run's own state root. Kept in ONE place and shared with
# the checker's fence: `check_verus.DENY_READ` is the same list, and a rule stated twice is two rules.
import check_verus as C


def render(bench, hook=None):
    if not bench:
        raise SystemExit("render_settings_verus: REFUSE — $BENCH is unset. A fence that guesses its own root "
                         "is the defect row CO names; name the root explicitly.")
    root = os.path.realpath(os.path.expanduser(bench))
    hook = hook or os.path.join(root, "harness", "hook-deny-network.sh")
    deny = C.deny_read_paths(root)
    # ⛔ The hook path is DERIVED from the same root, not hardcoded. settings.s2.json names
    # `/Users/jyh/bench/harness/hook-deny-network.sh` literally — which works today only because every state
    # root's `harness` is a SYMLINK to `~/bench/harness`. A fence whose audit layer points at another root's
    # copy is one `rm` away from being unhooked without anything failing.
    txt = open(TEMPLATE, encoding="utf-8").read()
    txt = txt.replace("__DENY_READ__", json.dumps(sorted(deny), indent=8).replace("\n]", "\n      ]"))
    txt = txt.replace("__HOOK__", hook)
    json.loads(txt)          # a rendering that is not valid JSON must fail HERE, not in the agent's launch
    return txt


def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--bench"); ap.add_argument("--hook"); ap.add_argument("--out"); ap.add_argument("--check")
    a, _ = ap.parse_known_args()
    if not a.bench:
        sys.exit(__doc__)
    txt = render(a.bench, a.hook)
    if a.check:
        have = open(a.check, encoding="utf-8").read()
        if have != txt:
            print("SETTINGS DRIFT: %s is not the pinned template rendered at BENCH=%s" % (a.check, a.bench))
            return 2
        print("SETTINGS OK %s (template rendered at BENCH=%s)" % (a.check, a.bench))
        return 0
    if a.out:
        open(a.out, "w", encoding="utf-8").write(txt)
        print("wrote %s" % a.out)
    else:
        sys.stdout.write(txt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
