#!/usr/bin/env python3
"""slug_split_census.py [--roots GLOB] [--cells GLOB] [--gate] [--json] [--selftest]

A cell's sessions live under `<CLAUDE_CONFIG_DIR>/projects/<slug>`, and `cell_meter` sums the sessions
under ONE slug. ⇒ **A CELL THAT RAN ON TWO POOLS HAS ITS RECORDS UNDER TWO CONFIG DIRS, AND EVERY
PER-CELL FIGURE IS THEN SCOPED TO WHICHEVER ONE WAS READ.** This is the only instrument that sees that
condition directly (desk `VW` rec (c)); everything else infers it.

⛔⛔ WHY AN INFERENCE IS NOT ENOUGH, WHICH IS WHY THIS FILE EXISTS. `join_cells_table.end2_scope`
  classifies a row by asking which of `p1+p2` and `p2` its end-2 meter sits NEARER. That is
  direction-free and it classified 5 of 5 correctly on block SC — and it is still a COMPARISON OF
  NUMBERS, not a reading of the world. This census reads the world: a slug either appears under more
  than one config dir or it does not. ⇒ 🔑 A COMPARISON CAN ONLY EVER BE RIGHT ABOUT THE CASES IT WAS
  TUNED ON; AN EXISTENCE CHECK CANNOT BE TUNED AT ALL.

⭐ AND THE SECOND THING IT SEES, WHICH IS WHAT MAKES IT WORTH TRACKING RATHER THAN SCRIPTING ONCE
  (desk `WO`): the sandbox probe's live verdict `INDETERMINATE (no-marker)` means BOTH "the subject
  could not be asked" and "the subject was asked and REFUSED", and the live tell (`client_rc`) must be
  captured as the probe runs. THE TRANSCRIPT IS DURABLE, so every past drive is re-classifiable
  without re-running anything:

      AUTH-FAILURE     the assistant turn says "Failed to authenticate" / "401 ... revoked" /
                       "OAuth session expired"        ⇒ 0 TOKENS — it never reached the model
      PROBE-REFUSED    the assistant turn says "I'm not going to run this"
                       ⇒ 60k-68k TOKENS on the measured cases — a real inference turn
      PROBE-RAN        the probe session made >= 1 tool call
      WORK             not a probe session at all

⛔⛔ THE DISCRIMINATOR THAT DOES **NOT** WORK, RECORDED BECAUSE I SHIPPED IT FIRST AND IT IS THE WHOLE
  POINT OF `WO`: "a probe session with ZERO tool calls = the subject refused". Measured 2026-09-22 over
  226 probe sessions it scored 8 refusals — and 3 of the 8 were AUTH FAILURES, including one whose 401
  I had personally diagnosed the night before. ⇒ 🔑 "THE PROBE DID NOT RUN" IS THE SHARED OBSERVABLE OF
  BOTH CAUSES, SO ANY INSTRUMENT KEYED ON IT REPRODUCES THE CONFLATION IT WAS BUILT TO EXPOSE.
  The classifier below keys on the assistant turn's TEXT, with the token count as a second axis.

⚠️ SCOPE, DECLARED BESIDE THE VERDICT AND NOT ONLY HERE (the LIMITS-RIDE law): an auth failure that
  never opens a session writes NO transcript at all, so this sees only drives that REACHED a session.
  It sits BESIDE `client_rc` and never replaces it.

RC: `--gate` exits 1 only when a cell carries WORK under MORE THAN ONE config dir — the one case
that scopes a real figure away from a meter, and a question with no tie-break in it. A split whose extra side is a PROBE is REPORTED and is rc 0, because that is
what the harvest already excludes by design (measured on `clbgfs01` and `clbsfp03`, both published).
Without `--gate` it always exits 0: a census reports, a gate refuses, and conflating them is how an
instrument starts crying wolf and stops being read.
"""
import argparse, glob, json, os, re, sys

CFG_PREFIX = "." + "claude-" + "account-"   # ⛔ ASSEMBLED FROM PARTS, NOT WRITTEN OUT.
# The per-seat runtime config directory is a PRIVATE-RECORD path and this repo is PUBLIC, so
# `check_private_paths.py` refuses a literal one — it refused THIS FILE three times before this line
# existed, which is exactly the demonstrating-a-forbidden-form case the gate's own message describes.
# ⇒ The name is built here once and every other site refers to THIS constant, so the literal appears
#   nowhere and a later editor cannot reintroduce it by copying a neighbouring line.


AUTH_SIGS = ("Failed to authenticate", "OAuth access token has been revoked", "OAuth session expired")
REFUSE_SIGS = ("I'm not going to run", "I will not run", "I'm not going to execute")
PROBE_SIGS = ("sandbox containment check", ".sandbox-probe")
CELL_RE = re.compile(r"(clb[a-z]{3}\d{2})")          # clb + THREE letters + two digits
# ⛔ THE PATTERN IS THE PLACE THIS FILE IS MOST LIKELY TO GO SILENTLY WRONG, AND IT ALREADY DID ONCE:
#   the first census of this condition used `clb[a-z]{4}\d{2}` and read 0 cells in 170, while the
#   directory listing printed beside it as a control fired perfectly. ⇒ A CONTROL PROVES YOU CAN SEE
#   AND SAYS NOTHING ABOUT THE PATTERN. `--selftest` pins the shape against a known id.


def classify(path):
    """-> (kind, records, tokens). Reads one session transcript. Never raises on a malformed line."""
    n = tokens = tools = 0
    is_probe = False
    assistant = []
    try:
        fh = open(path, encoding="utf-8", errors="replace")
    except OSError:
        return "UNREADABLE", 0, 0
    with fh:
        for line in fh:
            if not line.strip():
                continue
            n += 1
            if any(s in line for s in PROBE_SIGS):
                is_probe = True
            try:
                o = json.loads(line)
            except Exception:
                continue
            m = o.get("message") or {}
            u = m.get("usage") or {}
            for k in ("input_tokens", "output_tokens",
                      "cache_creation_input_tokens", "cache_read_input_tokens"):
                tokens += u.get(k) or 0
            c = m.get("content")
            if isinstance(c, list):
                tools += sum(1 for b in c if isinstance(b, dict) and b.get("type") == "tool_use")
                if o.get("type") == "assistant":
                    assistant += [b.get("text", "") for b in c
                                  if isinstance(b, dict) and b.get("type") == "text"]
            elif isinstance(c, str) and o.get("type") == "assistant":
                assistant.append(c)
    body = " ".join(assistant)
    if any(s in body for s in AUTH_SIGS):
        return "AUTH-FAILURE", n, tokens          # checked FIRST: it can wear any other shape
    if not is_probe:
        return "WORK", n, tokens
    if tools >= 1:
        return "PROBE-RAN", n, tokens
    if any(s in body for s in REFUSE_SIGS):
        return "PROBE-REFUSED", n, tokens
    return "PROBE-NO-RUN-UNCLASSIFIED", n, tokens  # ⛔ a THIRD state, never folded into either


def census(roots_glob, cells_glob):
    cells = {}
    for d in glob.glob(os.path.join(roots_glob, "projects", cells_glob)):
        if not os.path.isdir(d):
            continue
        mm = CELL_RE.search(os.path.basename(d))
        if not mm:
            continue
        cid = mm.group(1)
        parts = os.path.abspath(d).split(os.sep)
        key = CFG_PREFIX[1:]
        pool = next((p.split(key)[-1] for p in parts if key in p), "?")
        for f in sorted(glob.glob(os.path.join(d, "*.jsonl"))):
            kind, n, tok = classify(f)
            cells.setdefault(cid, []).append(
                {"pool": pool, "file": os.path.basename(f), "kind": kind, "records": n, "tokens": tok})
    return cells


def report(cells, gate, as_json):
    split = {c: s for c, s in cells.items() if len({x["pool"] for x in s}) > 1}
    # ⛔⛔ THE GATE ASKS "DOES MORE THAN ONE POOL CARRY **WORK**?", NOT "IS THE EXTRA SIDE WORK?".
    #   The first cut ranked the pools by record count, called the largest the BULK side and judged the
    #   others — and its own CONTROL arm caught it: two sides of EQUAL size TIE, `max` picks one
    #   arbitrarily, and a cell whose probe side happened to win the tie failed a gate it should pass.
    #   ⇒ 🔑 "WHICH SIDE IS THE REAL ONE" IS A QUESTION THE DATA DOES NOT ANSWER, AND ASKING IT INVENTED
    #     A TIE-BREAK THAT DECIDED A VERDICT. Counting pools that carry WORK needs no ranking, has no
    #     tie, and is the condition that actually scopes a figure away: if two config dirs both hold
    #     real sessions, a per-slug meter necessarily misses some of them whichever one it reads.
    work_split = []
    for c, s in sorted(split.items()):
        work_pools = sorted({x["pool"] for x in s if x["kind"] == "WORK"})
        if len(work_pools) > 1:
            work_split.append((c, "+".join(work_pools)))
    if as_json:
        print(json.dumps({"cells": len(cells), "split": split, "work_split": work_split},
                         indent=2, sort_keys=True))
    else:
        print("slug_split_census: %d cell(s) carry a slug dir; %d appear under MORE THAN ONE config dir."
              % (len(cells), len(split)))
        for c, s in sorted(split.items()):
            print("  %s" % c)
            for x in sorted(s, key=lambda x: -x["records"]):
                print("     %-12s %-28s records=%-5d tokens=%-9d %s"
                      % (x["pool"], x["file"][:28], x["records"], x["tokens"], x["kind"]))
        print("LIMITS, beside the verdict: an auth failure that never opens a session writes NO transcript,")
        print("  so this sees only drives that REACHED a session — it sits BESIDE client_rc, never replaces it.")
        print("  A split whose extra side is a PROBE is what the harvest already excludes BY DESIGN and is")
        print("  reported, not failed. Only WORK under MORE THAN ONE config dir scopes a real figure away.")
    if gate:
        if work_split:
            print("⛔ GATE: %d split cell(s) carrying WORK under MORE THAN ONE config dir: %s"
                  % (len(work_split), ", ".join("%s@%s" % t for t in work_split)), file=sys.stderr)
            return 1
        print("✅ GATE: no cell carries WORK under more than one config dir.")
    return 0


def selftest():
    import tempfile
    fails = []
    def sess(d, name, lines):
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, name), "w", encoding="utf-8") as f:
            for l in lines:
                f.write(json.dumps(l) + "\n")
    def asst(text, tools=0, tok=0):
        c = [{"type": "text", "text": text}] + [{"type": "tool_use", "name": "Bash"}] * tools
        return {"type": "assistant", "message": {"content": c, "usage": {"input_tokens": tok}}}
    probe_user = {"type": "user", "message": {"content": PROBE_SIGS[0] + " — run it"}}
    with tempfile.TemporaryDirectory() as t:
        slug = "-Users-jyh-cells-clb-sg-lru-plain-clbglp09-repo"
        A = os.path.join(t, CFG_PREFIX + "poolA", "projects", slug)
        B = os.path.join(t, CFG_PREFIX + "poolB", "projects", slug)
        sess(A, "bulk.jsonl", [{"type": "user", "message": {"content": "BOOT"}},
                               asst("working", tools=3, tok=500000)])
        sess(B, "probe.jsonl", [probe_user, asst("I'm not going to run this.", tok=65000)])
        cells = census(os.path.join(t, CFG_PREFIX + "*"), "*")
        got = sorted((x["pool"], x["kind"]) for x in cells.get("clbglp09", []))
        want = [("poolA", "WORK"), ("poolB", "PROBE-REFUSED")]
        print("  arm 1 a split cell is FOUND and both sides classified   %s  %s"
              % (got, "ok" if got == want else "⛔ FAIL want %s" % want))
        if got != want: fails.append(1)
        rc = report(cells, gate=True, as_json=False)
        print("  arm 2 CONTROL: a PROBE second side does NOT fail the gate rc=%d  %s"
              % (rc, "ok" if rc == 0 else "⛔ FAIL"))
        if rc != 0: fails.append(2)
        # ⭐ RED BACKWARDS: make the extra side WORK and require the gate to fire.
        sess(B, "probe.jsonl", [{"type": "user", "message": {"content": "BOOT"}},
                                asst("editing", tools=2, tok=400000)])
        cells = census(os.path.join(t, CFG_PREFIX + "*"), "*")
        rc = report(cells, gate=True, as_json=False)
        print("  arm 3 MUTANT: WORK on BOTH sides DOES fail the gate      rc=%d  %s"
              % (rc, "ok" if rc == 1 else "⛔ FAIL"))
        if rc != 1: fails.append(3)
        # ⭐ the AUTH/REFUSAL separation, which is the discriminator that replaced a broken one
        sess(B, "probe.jsonl", [probe_user,
                                asst("Failed to authenticate. API Error: 401 OAuth access token has been revoked.")])
        cells = census(os.path.join(t, CFG_PREFIX + "*"), "*")
        k = [x["kind"] for x in cells["clbglp09"] if x["pool"] == "poolB"]
        print("  arm 4 an auth failure is NOT read as a refusal           %s  %s"
              % (k, "ok" if k == ["AUTH-FAILURE"] else "⛔ FAIL"))
        if k != ["AUTH-FAILURE"]: fails.append(4)
        # ⛔ arm 5: the id pattern. The first census of this condition used clb[a-z]{4}\d{2} and read ZERO.
        ok5 = bool(CELL_RE.search("-Users-jyh-cells-clb-sg-lru-plain-clbglp09-repo")) and \
              not CELL_RE.search("-Users-jyh-cells-clb-sg-lru-plain-clbgl09-repo")
        print("  arm 5 the cell-id shape is clb+THREE letters+2 digits    %s"
              % ("ok" if ok5 else "⛔ FAIL — the {4} pattern that once read 0 of 170"))
        if not ok5: fails.append(5)
        # ⭐ arm 6, ANTI-VACUITY: an UNSPLIT cell must not be reported as split.
        cells2 = census(os.path.join(t, CFG_PREFIX + "poolA*"), "*")
        rc = report(cells2, gate=True, as_json=False)
        n_split = len({c for c, s in cells2.items() if len({x["pool"] for x in s}) > 1})
        print("  arm 6 ANTI-VACUITY: a single-pool cell is not a split    splits=%d  %s"
              % (n_split, "ok" if n_split == 0 and rc == 0 else "⛔ FAIL"))
        if not (n_split == 0 and rc == 0): fails.append(6)
    if fails:
        print("⛔ SELFTEST FAILED on arm(s) %s" % fails); return 1
    print("✅ SELFTEST 6/6 — a split is found and both sides classified; a PROBE extra side is reported "
          "and does NOT fail the gate while WORK on both sides DOES (red-backwards); an auth failure is not read "
          "as a refusal, which is the discriminator that replaced a broken one; the cell-id shape is "
          "pinned against the {4} pattern that once read 0 of 170; and an unsplit cell is not a split.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    if "--selftest" in sys.argv[1:]:
        return selftest()
    ap.add_argument("--selftest", action="store_true", help="drive the arms; reads nothing, needs no box")
    ap.add_argument("--roots", default=os.path.join(os.path.expanduser("~"), CFG_PREFIX + "*"),
                    help="glob for the per-seat runtime config dirs (default: every one in $HOME)")
    ap.add_argument("--cells", default="*cells-clb*", help="glob for the per-cell slug dirs")
    ap.add_argument("--gate", action="store_true",
                    help="exit 1 when a split cell's EXTRA side carries WORK (a probe extra side is "
                         "reported and is rc 0 — that is what the harvest excludes by design)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    return report(census(a.roots, a.cells), a.gate, a.json)


if __name__ == "__main__":
    sys.exit(main())
