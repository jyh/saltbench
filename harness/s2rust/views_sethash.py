#!/usr/bin/env python3
"""views_sethash.py — THE set-hash over a built views directory. ONE implementation, two callers.

The views are not shipped: 207 views of multi-hundred-KB Rust are a pure function of two pinned inputs
(`bench-jsonl-sha` and `build_views_verus.py`), so they are REBUILT and verified by this hash instead.

⛔ WHY THIS IS A FILE AND NOT TWO SHELL PIPELINES. The first cut computed the pin in `hashes_s2rust.sh` with
`shasum | cut | tr` and verified it in Python over raw digests. Both are honest set-hashes and they DISAGREE,
because one folds hex strings and the other folds bytes. A future head verifying a rebuild with the "wrong"
one would have seen a mismatch on identical files and gone hunting a scaffold defect that was not there.
⇒ 🔑 ***A CHECKSUM DEFINED TWICE IS TWO CHECKSUMS. The generator and the verifier must be the same code, not
the same idea.*** (The seat has paid this before: a normalisation routed through a printed form, amendment 14.)

usage: views_sethash.py <viewsdir>            -> "<sha256> count=<n>"
       views_sethash.py <viewsdir> --verify <sha256>   -> exit 0 match / 4 mismatch
"""
import hashlib, os, sys

FILES = ("task.rs", "frozen.json")


def sethash(root):
    if os.path.isdir(os.path.join(root, "views")):
        root = os.path.join(root, "views")
    ids = sorted(os.listdir(root))
    h = hashlib.sha256()
    for t in ids:
        h.update(t.encode("utf-8"))
        for f in FILES:
            h.update(hashlib.sha256(open(os.path.join(root, t, f), "rb").read()).digest())
    return h.hexdigest(), len(ids)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    digest, n = sethash(args[0])
    if "--verify" in sys.argv:
        want = sys.argv[sys.argv.index("--verify") + 1]
        ok = want == digest
        print("views set-hash %s (count=%d) %s" % (digest, n, "MATCHES" if ok else "DOES NOT MATCH %s" % want))
        sys.exit(0 if ok else 4)
    print("%s count=%d" % (digest, n))
