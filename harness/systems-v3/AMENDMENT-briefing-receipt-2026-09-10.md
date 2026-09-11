# AMENDMENT — THE BRIEFING RECEIPT: a cell proves its arm file LOADED, or it is not scored
**bench · 2026-09-10 · registered BEFORE the first cell runs under native arm filenames**

⛔ Named, not numbered, on purpose: the numbered AMENDMENT registry is **branch-forked** in this
repository — the root carries up to 17 and other branches carry up to 26 — so `highest + 1` names a
different document depending on which branch you read. Cite this one by **name and date**.

## §1 · WHAT HAPPENED, AND IT IS THE WHOLE ARGUMENT
Nine Antigravity cells ran on 2026-09-10 carrying `CLAUDE.md`, **5,024 bytes, byte-identical to the
file the Claude plain cells load.** Antigravity has **zero** references to that filename. So:
```
  the file was PRESENT in every cell              measured: 9 of 9, same size
  the file was never READ by that client          measured: 0 references in the binary
  nothing anywhere said so                        no error · no warning · no log line · no field
```
⇒ The cells were reported as a **plain arm**. They were a **no-briefing arm**, and it surfaced a day
later, from a question about file names rather than from any instrument.
⇒ 🔑 ***AN ARM DELIVERED AS A FILE IS ONLY REAL IF THE FILE LOADED, AND "IT IS IN THE DIRECTORY" IS A
DIFFERENT CLAIM.*** This campaign has now met that distinction four times in one day — an inherited
completion marker, a `settings.json` naming another wave, a fence sealed before its input, and a
briefing nobody read. **Each artefact was present and none was in effect.**

## §2 · THE RULE
**Every scored cell emits a BRIEFING RECEIPT.**
```
  1. the arm file carries a NONCE, unique per cell, DERIVED (not typed) at build time
  2. the boot turn asks the subject to echo it — ONE line, IDENTICAL on both arms
  3. the echo is recorded in ctl/ beside the cell's other receipts
  4. NO ECHO -> VOID(NO-BRIEFING). The cell is not scored and is never counted as its arm.
```
⛔ **A void here is not a failed cell, it is an unbuilt one**, and it is reported as such: a cell whose
arm did not load never ran the experiment the table says it ran.

## §3 · ⛔ WHAT THE RECEIPT DOES **NOT** ESTABLISH, SAID HERE SO IT IS NOT CLAIMED LATER
It proves the file **reached the subject's context**. It does **not** prove the subject **followed**
it, understood it, or weighted it as intended. ⇒ **It converts a silent absence into a loud one and
nothing more.** Any claim about the method's *effect* still rests on the arm contrast, not on this.
📌 And it is **not** a substitute for the mechanism checks: a driven check proves the client loads that
filename **on the day it was driven**; the receipt proves **this cell, on this run, under this client
version.** ⇒ ***A MECHANISM PROVEN ONCE SAYS NOTHING ABOUT A CELL THAT RUNS AFTER THE NEXT CLIENT
UPDATE*** — which is exactly the shape of the failure above, where the mechanism had never been proven
at all and every cell inherited the assumption.

## §4 · SCOPE AND COST
**Both arms, both clients, every scored cell, from the first cell that runs under native arm
filenames** (`CLAUDE.md` on the Claude arm, `AGENTS.md` on the Antigravity arm, identical bytes —
the Captain's ruling, 2026-09-10, which also removes a **competitor-named file from the subject's own
working directory**, a neutrality improvement and not only a plumbing one).
**Cost: one line in a boot prompt and one derived string at build time.** It converts the most
expensive silent failure mode in this design — an arm that does not exist while its table says it does
— into a per-cell refusal that costs nothing to check.

## §5 · WHAT IS NOT CHANGED
The nine existing Antigravity cells stay in the record as what they are: a **no-shell, no-build,
no-briefing** floor of **8/9** against the complete hidden suite. The twelve existing Claude LZW cells
stand for the cross-vendor pairing per the Captain's ruling; **no cell that used `CLAUDE.md` is
repeated.** Every within-Claude result already published compares `CLAUDE.md` cells with `CLAUDE.md`
cells and is untouched.

---

## ADDENDUM 1 — THE CLAUDE HALF IS NARROWED TO *OWED*, AND SAYING SO IS THE POINT
**bench · 2026-09-10 · written in the same act as the implementation, before any cell fired**

§4 above reads *"Both arms, both clients, every scored cell."* **The implementation covers the agy
client only.** That is a narrowing of a registered rule, so it is recorded here rather than left to a
code comment — a rule and its instrument are separately falsifiable, and the place a reader checks is
the rule.

**THE REASON, MEASURED, NOT PREFERRED: the Claude launcher has no echo gate.** `agy_launch_v3.sh`
reads the first and last results positionally and refuses a cell whose subject did not echo;
`cell-claude.sh` has no such probe. So a receipt block in `CLAUDE.md` today would:

1. **change the Claude arm's bytes mid-campaign**, forking that arm between waves and breaking the
   byte-identity every published within-Claude comparison rests on; and
2. **buy nothing**, because no instrument would read the echo.

⇒ 🔑 ***A TOKEN NOTHING CHECKS IS NOT A RECEIPT, IT IS A BYTE CHANGE WEARING ONE.*** Paying a
comparability cost for an unread field is the worse half of both options.

**WHAT IS OWED, IN ORDER, AND IT IS NOT WAIVED:**
1. an echo gate in the Claude launcher, equivalent to P-DELIVERY;
2. **then** a registered wave boundary at which the Claude arm's bytes change.

Until (1) lands, a Claude cell writes no token **and says so on stdout** — `cell_build.py` prints the
skip by name. A silent skip and a deliberate one produce identical trees, and only the printed line
tells a later reader which this was.

## ADDENDUM 2 — ⛔⛔ THE GATE'S TOKEN MUST HAVE EXACTLY ONE ROUTE, AND THIS IS NOT A DETAIL
§2 says the nonce is *derived, not typed*. **That is necessary and it is not sufficient**, and the
gap is where this mechanism would have failed silently:

```
  the receipt proves the arm file LOADED  <=>  the token cannot be obtained any other way
```

If the token also sits anywhere the subject can read — a copied source file, a `ctl/` note, the boot
prompt, or **the ACK question itself** — then it can be echoed without the briefing ever being opened.
Such a gate does not merely weaken: ***it reports DELIVERED most reliably in exactly the case it
exists to catch.*** An inverted gate, not a loose one.

**SO TWO THINGS ARE ASSERTED PER CELL, BOTH DRIVEN RED-FIRST:**
- **at BUILD**, over the finished tree: the token occurs at exactly one path, `repo/<arm file>`. The
  build REFUSES otherwise and names the colliding paths.
- **at LAUNCH**, on the bytes actually sent: neither probe turn contains the token. The file-mode ACK
  names the *place* and never the *value*, and the launcher refuses if it ever does.

📌 **BOTH WERE FOUND BY BEING DRIVEN, NOT BY BEING REASONED ABOUT.** The build-time assertion fired on
its own author on the first real build (`ctl/briefing-claim` quoted the token, and `ctl/` is inside the
fence). The launch-time one needed its RED arm moved before it tested the guard rather than an
unrelated precondition twenty checks earlier.
⇒ 🔑 ***A RECEIPT THAT SHIPS ITS OWN ANSWER IN THE QUESTION IS THIS CAMPAIGN'S OLDEST DEFECT — AN ARM
BUILT FROM THE ANSWER IT CHECKS — WEARING THE CLOTHES OF THE INSTRUMENT BUILT TO CATCH IT.***
