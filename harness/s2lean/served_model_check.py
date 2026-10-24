#!/usr/bin/env python3
"""served_model_check.py — the O90 served-model halt's check (desk AEY; systems' re-reads F3, G2). Prints NOTHING when the
episode's manifest shows the requested model served; otherwise prints the reason (the driver then writes HALT and stops).
Rule: an episode that made calls (manifest `calls` > 0, or unknown) must show `models[model_requested]` > 0; any other entry
must be a claude-haiku* auxiliary AND sit beside the requested model. A missing or empty `models`, a haiku-only map and a
substituted id all HALT. An episode with calls == 0 (refused before the model) passes: it served nothing.
  usage: served_model_check.py <manifest.json>    ·    served_model_check.py --selftest"""
import json, sys
def check(m):
    want = m.get("model_requested"); calls = m.get("calls")
    if calls == 0 and not m.get("models"): return ""   # L3: calls 0 WITH a served-model record is checked like any other
    models = m.get("models")
    if not isinstance(models, dict) or not models: return "NO SERVED-MODEL RECORD (models=%r), REQUESTED %s" % (models, want)
    if not models.get(want): return "REQUESTED %s NOT SERVED (served %s)" % (want, ",".join(sorted(models)))
    bad = sorted(k for k in models if k != want and not k.startswith("claude-haiku"))
    return "SERVED %s, REQUESTED %s" % (",".join(bad), want) if bad else ""
def selftest():
    R = "claude-opus-5"
    cases = [("clean", {"models": {R: 8}}, False), ("clean+haiku", {"models": {R: 8, "claude-haiku-4-5": 1}}, False),
             ("substituted", {"models": {"claude-sonnet-5": 8}}, True), ("haiku_only", {"models": {"claude-haiku-4-5": 9}}, True),
             ("empty", {"models": {}}, True), ("missing", {}, True), ("zero", {"models": {R: 0, "claude-haiku-4-5": 1}}, True),
             ("no calls", {"calls": 0, "models": {}}, False), ("mixed", {"models": {R: 4, "claude-sonnet-5": 4}}, True),
             ("calls0 substituted", {"calls": 0, "models": {"claude-sonnet-5": 1}}, True)]
    bad = []
    for name, m, halts in cases:
        m = dict(m, model_requested=R); m.setdefault("calls", 9)
        if bool(check(m)) != halts: bad.append(name)
    print("SELFTEST %s (%d cases%s)" % ("PASS" if not bad else "FAIL", len(cases), (": " + ", ".join(bad)) if bad else ""))
    return 1 if bad else 0
if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]: sys.exit(selftest())
    try: m = json.load(open(sys.argv[1]))
    except Exception as e: print("MANIFEST-UNREADABLE %s" % e); sys.exit(0)
    r = check(m)
    if r: print(r)
