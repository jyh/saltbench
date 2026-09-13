# DESIGN — THE CLAUDE-CLIENT SANDBOX PROBE (§B7 ROW 3's SECOND LAYER)
## bench (SaltBench lead), 2026-09-13. On maestro's ruling that row 3's closer is a DESIGN task.
## ⛔ THIS IS A DESIGN. NOTHING HERE IS BUILT, AND NO CLAIM ABOUT ANY PAST CELL CHANGES.

---

## §S0 · THE PROBLEM, AND WHY THE OBVIOUS FIX IS REFUSED BY RULING
ADDENDUM 17 measured it: across 262 launch logs, **134 `client=agy` drive the OS sandbox layer, both
halves, per cell; 124 `client=claude` never have.** The split is perfect and it is on the CLIENT.
⛔ **UNMEASURED, NOT UNSOUND** — the hook layer (`permissions.deny`) *is* driven and green, no leak is
claimed, and no published number moves.

**A straight port of `probe_sandbox()` is REFUSED, and the reason is mechanical:**
```
  agy     an EXTERNAL WRAPPER.  $SANDBOX_PREFIX = `sandbox-exec -f <profile>`, so the harness can run
          /bin/cat under the very profile the launch uses — NO MODEL CALL, per cell, free.
  claude  SELF-SANDBOXING.  The fence is handed to the client as `--settings ctl/fence.json` and the
          client applies `sandbox.filesystem.denyRead` ITSELF.  $SANDBOX_PREFIX IS EMPTY.
```
⇒ **The ported function reaches its first branch — `if [ -z "$SANDBOX_PREFIX" ]` — and prints
*"n/a (there is no OS fence to prove)"* over a `fence.json` that sets `sandbox.enabled: true`.**
⇒ 🔑 ***A CLEAN RECORD PRINTED OVER AN UNDRIVEN LAYER, IN EVERY CELL, FOREVER — AND IT WOULD READ AS
COVERAGE BECAUSE IT NAMES ITS OWN SCOPE ACCURATELY.*** That is this fleet's "most dangerous green": a
declaration of limits, printed where the reader has already decided the answer is yes.

## §S1 · THE MECHANISM, ENUMERATED RATHER THAN GUESSED
*Read at the object on a rendered Claude fence. The lesson that produced this section is `gemini`'s, from
the `BUDGET.md` line the same afternoon: **an enumerated population is a guess wearing a denominator.***
```
  fence.json top-level keys   theme · skipDangerousModePermissionPrompt · permissions · sandbox
  permissions.deny            338 entries — Read()/Edit()/Grep() per path, plus WebFetch, WebSearch
  sandbox.enabled             true          sandbox.failIfUnavailable        true
  sandbox.allowUnsandboxedCommands  false   sandbox.autoAllowBashIfSandboxed true
  sandbox.filesystem.denyRead       a list of absolute directory paths
  sandbox.network             allowedDomains [] · strictAllowlist true
```
⭐ **`autoAllowBashIfSandboxed: true` IS THE HANDLE.** It means Bash-tool commands run **inside** the
sandbox and are auto-approved. ⇒ **There is a path by which an ordinary shell command executes under the
very mechanism the client applies — and it runs through the client's Bash tool, which is reachable.**
⛔ **THE DESIGN DOES NOT DEPEND ON *HOW* THE CLIENT ENFORCES IT** (Seatbelt, or anything else). It drives
the enforcement through the tool the subject itself would use. **That is the point: a probe of the
mechanism the client APPLIES, not of the mechanism we believe it applies.** ⇒ *An implementation detail I
have not measured must not become a premise, and here it need not be one.*

## §S2 · THE PROBE — BOTH HALVES, THROUGH THE CLIENT
```
  PLANT     OUTSIDE  a file under a denyRead root                  content OUTSIDE-THE-CELL
            INSIDE   a file in the cell's own ctl/                 content INSIDE-THE-CELL
  DRIVE     one `claude -p` invocation, NON-INTERACTIVE, carrying THE CELL'S OWN ctl/fence.json
            via --settings, cwd = the cell, asked to cat BOTH files and report each result
  SCORE     OUTSIDE denied  AND  INSIDE readable   ->  P-SANDBOX yes
            OUTSIDE readable                       ->  HOLD: the fence is not binding for this cell
            INSIDE  denied                         ->  HOLD: a profile that denies everything is not a
                                                        fence, it is a cell that cannot run
            neither observed                       ->  ⛔ INDETERMINATE, see §S3. NEVER `yes`, NEVER `no`.
```

## §S3 · ⛔⛔ THE DEFECT THIS PROBE IS MOST LIKELY TO HAVE, AND THE HALF THAT CURES IT
**An agy probe's failure modes are a wrapper's. A Claude probe's failure modes include A MODEL THAT DID
NOT DO WHAT IT WAS ASKED** — and *"the model never ran the outside `cat`"* produces **no output for the
outside read**, which is **byte-identical to a denial.**
⇒ 🔑 ***AN INSTRUMENT THAT REPORTS ABSENCE FAILS TOWARD ABSENCE, AND THIS ONE'S FAILURE DIRECTION IS
EXACTLY ITS GREEN VERDICT.*** A probe that scores "no output ⇒ denied ⇒ the fence works" **certifies the
fence most reliably in the one case where nothing was tested.**

✅ **THE CURE IS THE GREEN HALF, AND IT DOES DOUBLE DUTY HERE THAT IT DOES NOT DO ON THE agy LANE:**
```
  on agy     the INSIDE-readable half catches an OVER-BROAD profile (deny-everything passes a deny-only
             check while making the cell unrunnable) — the reason agy's own comment gives.
  on claude  it ALSO catches A SUBJECT THAT NEVER RAN A COMMAND AT ALL.  An inside read that SUCCEEDS is
             positive evidence that the Bash tool executed and that this probe's needle reached the
             filesystem.  ⇒ WITHOUT IT, A SILENT MODEL AND A WORKING FENCE ARE THE SAME RECORD.
```
⛔ **AND ONE MORE ARM THE agy PROBE DOES NOT NEED: the denial must be IDENTIFIED, not inferred.** The
probe requires a **positive denial signature** from the outside read — an error, a refusal, a non-zero
status **that is distinguishable from an empty result** — and records it verbatim. **"I saw nothing" is
`INDETERMINATE`; "I saw a denial" is `denied`.** *An rc whose meaning the reader supplies is this desk's
own banked defect, and it is the shape this probe would take by default.*

## §S4 · COST, AND WHY IT IS **NOT** ONE DRIVE PER CELL
A `claude -p` turn is a model call. Per cell, on a 24-cell wave, that is 24 calls of pure overhead.
⚠️ **But per-cell is not negotiable in the way it looks:** agy's own comment is right that a fence proven
on one cell says nothing about another, **and in this campaign that is not theoretical** — the deny-set is
a **glob taken at RENDER time**, so a cells root that grows leaves an earlier cell's fence permissive.
✅ **THE RESOLUTION — KEY ON THE ARTEFACT, NOT THE CELL:**
```
  1  per cell, ALWAYS and FREE:   sha256 of the cell's rendered ctl/fence.json, recorded at launch
  2  per DISTINCT fence sha:      drive §S2 ONCE.  A cell whose fence sha is already driven inherits
                                  that receipt BY IDENTITY, and the receipt NAMES the sha it was taken on
  3  a NEW fence sha              -> an UNDRIVEN fence -> DRIVE IT, or the cell does not fire
```
⇒ **Byte-identical fences are the same fence; a cell with a fence nobody has driven is a cell without a
receipt.** ⛔ **The inheritance is BY SHA, never by cells root, never by wave, never by date** — *a gate
keyed to one member of a set does not fail when the set changes, it goes vacuous and keeps printing green.*

## §S5 · THE SELFTEST, WITH THE MUTATION THE GATE REQUIRES
⛔ **A probe whose RED arm has never fired is an untested arm that looks exactly like a passing one.**
```
  M1  sandbox.enabled: false             -> outside read SUCCEEDS -> probe RED.   THE REQUIRED MUTATION.
  M2  denyRead: []  (enabled, empty)     -> outside read SUCCEEDS -> probe RED.   ⇒ separates "the
                                            sandbox is off" from "the sandbox is on and denies nothing",
                                            which M1 alone cannot, and which is the likelier live defect
  M3  denyRead: ["/"]  (deny everything) -> INSIDE read fails    -> probe RED via the GREEN half
  M4  a stub that answers plausibly and  -> INSIDE read absent   -> INDETERMINATE, never `yes`
      runs NO commands                      ⇒ this is §S3's defect, driven rather than argued
  P1  the real fence, unmutated          -> probe GREEN
  CONTROL  each RED must name WHICH arm failed; a RED that cannot say which is not a pass either
```
⚠️ **M4 IS THE ARM THAT MATTERS AND IT IS THE ONE A BUILDER WILL SKIP**, because it requires standing up
a client that answers without acting. **It is the only arm that tests the probe's own worst failure**, and
`claude-stub.sh` already exists in the harness as the shape to build it from.
⛔ **DRIVE THE MUTATIONS AHEAD OF ANY EARLIER GATE.** *An arm that fires behind an earlier refusal is not
a weak arm, it is an untested one — and something did refuse, so it looks like it passed.*

## §S6 · WHAT THIS PROBE WOULD AND WOULD NOT ESTABLISH
```
  WOULD      that for THIS fence sha, a read outside the allowed tree is DENIED through the client's own
             mechanism, and that a read inside it SUCCEEDS — i.e. the layer is DRIVEN, not merely RENDERED
  WOULD NOT  anything about the 124 Claude cells already run.  ⛔ Their layer stays UNMEASURED, and a
             probe built today CANNOT be applied retroactively to a cell that has landed.
  WOULD NOT  anything about the HOOK layer, which is separately driven and green
  WOULD NOT  make `permissions.deny` and `sandbox.filesystem.denyRead` one thing.  They are TWO LAYERS
             with overlapping but non-identical scope, and this desk's standing card is that historically
             only one of them was ever populated.  ⇒ A GREEN HERE IS A GREEN ON ONE LAYER.
```
⚠️ **AND THE HONEST HEADLINE, unchanged:** the Claude-lane gap is **UNMEASURED, NOT UNSOUND.** Building
this probe would close it going forward. **It would not retro-certify anything, and no published number
moves either way.**

## §S7 · WHAT IS OPEN, NAMED SO IT IS NOT MISTAKEN FOR SETTLED
1. ⛔ **THE CLIENT VERSION IS A MOVING PREMISE.** The run box carries **2.1.263** today; this campaign has
   already been bitten by a pin drifting under a copied contract. **The probe records the client version
   it was driven under, and a version change invalidates the receipt** — *a one-time drive is a claim
   about a sha, never about a repo.*
2. **Where the probe's own session artefacts land is unspecified here.** They must not enter the cell's
   evidence as though the subject produced them. **A cell directory is evidence, not scratch.**
3. **The quota cost of one drive per distinct fence sha is not measured.** §S4 bounds the COUNT, not the
   price.
4. ⛔ **I have NOT verified that a `-p` invocation carrying `--settings` applies the sandbox identically
   to the subject's own launch.** **That is the probe's central premise and it is UNDRIVEN.** If the two
   paths differ, this design measures the wrong thing — and **the first build step is to drive that
   equivalence, not to write the probe.** *This campaign's fifth wrong-population reading in a day was a
   true number read off an object the claim was not about; this is where that would happen here.*
