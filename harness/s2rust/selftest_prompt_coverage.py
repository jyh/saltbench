#!/usr/bin/env python3
"""selftest_prompt_coverage.py — ROW AV's GATE: what the checker refuses, the agent must have been told.

Zero model tokens. Amendment 16.

THE DEFECT THIS EXISTS TO STOP. Row AV was opened against S2-Lean — `native_decide` is effectively out of
bounds and no prompt says so — and the helm ruled it ripens at this regime boundary. Measured on the S2-Rust
prompts BEFORE the repair: the screen enforced **29** refusal rules and the prompts named **12**, leaving
**17 unstated**, among them `todo!` / `unimplemented!` (a natural placeholder reflex) and a new `use` import
(only `broadcast use` is allowed).

⛔ AND THE UNSTATED SURFACE WAS ARM-RELEVANT. The `use` rule bites hardest in the HELPERS region, and `a2`
is the arm that ENCOURAGES helper lemmas — the same shape as amendment 15's FATAL 3, where an instrument
penalised the treatment for applying the treatment. That is why this is a gate and not an edit: prose fixes
today and rots tomorrow, because the NEXT rule added to `RULES` would be unstated again and nothing would
notice. Here the prompt is a CONSUMER of the rule set.

THE ARMS:
  B1  COVERAGE   — every live rule name has a `PROMPT_COVERAGE` entry.
  B2  STATED     — every entry's phrase literally appears in the agent-visible prompt text.
  B3  NO ORPHANS — no registry entry names a rule the screen no longer enforces (a stale entry would let a
                   retired rule vouch for a live one, and the count would still look complete).
  B4  RED ARM    — a rule added to the screen with no registry entry MUST turn B1 red. Driven here, in
                   process, on a copy of the live table: the gate is proven to fail on the broken version
                   rather than asserted to.
  B5  RED ARM    — a registry entry whose phrase is absent from the prompt MUST turn B2 red.

usage: selftest_prompt_coverage.py
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import screen_verus as S

# The agent-visible prompt surface. ⛔ `base.md` and `prompt_P.md` are BOTH here because the agent reads
# both: a rule stated in either has been stated. The arm files (`arms/*.md`) are deliberately NOT included —
# an arm is a treatment, and a rule that only the salt arm is told about is exactly the arm-correlated
# instrument amendment 15 caught.
PROMPT_FILES = ["base.md", "prompt_P.md"]

PASS, FAIL = [], []


def arm(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print("  %s %-38s %s" % ("PASS" if ok else "FAIL", name, detail))


def prompt_text(root=HERE):
    return "\n".join(open(os.path.join(root, f), encoding="utf-8").read() for f in PROMPT_FILES)


def audit(names, coverage, text):
    """Return (unregistered, unstated, orphans) — the three ways this can be wrong."""
    unregistered = [n for n in names if n not in coverage]
    unstated = [n for n in names if n in coverage and coverage[n].lower() not in text.lower()]
    orphans = [n for n in coverage if n not in names]
    return unregistered, unstated, orphans


def main():
    names = S.rule_names()
    text = prompt_text()
    unreg, unstated, orphans = audit(names, S.PROMPT_COVERAGE, text)
    print("screen enforces %d refusal rules; prompt surface = %s" % (len(names), ", ".join(PROMPT_FILES)))

    arm("B1 every rule is registered", not unreg, "unregistered=%s" % (unreg or "none"))
    arm("B2 every rule is STATED in the prompt", not unstated, "unstated=%s" % (unstated or "none"))
    arm("B3 no orphan registry entries", not orphans, "orphans=%s" % (orphans or "none"))

    # B4 — a new rule with no registry entry must be caught.
    u4, _, _ = audit(names + ["__mutant_rule__"], S.PROMPT_COVERAGE, text)
    arm("B4 RED: unregistered rule is caught", u4 == ["__mutant_rule__"], "caught=%s" % u4)

    # B5 — a registered phrase absent from the prompt must be caught.
    cov5 = dict(S.PROMPT_COVERAGE); cov5[names[0]] = "a phrase no prompt contains zzq"
    _, u5, _ = audit(names, cov5, text)
    arm("B5 RED: unstated phrase is caught", u5 == [names[0]], "caught=%s" % u5)

    print("\nprompt-coverage selftest: %d arms, %d failed" % (len(PASS) + len(FAIL), len(FAIL)))
    if FAIL:
        print("  failed: %s" % ", ".join(FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
