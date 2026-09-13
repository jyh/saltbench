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

---

# ADDENDUM 1 — §S7 ITEM 4 DRIVEN, STATIC HALF. **THE PREMISE IS REFUTED AS WRITTEN, AND THE DESIGN SURVIVES.**
## bench, 2026-09-13, relight 49. Every number below measured at the object on the run box.
## ⛔ STILL A DESIGN. NOTHING IS BUILT, AND NO CLAIM ABOUT ANY PAST CELL CHANGES.

§S7 item 4 said the first build step is to drive the `-p`/`--settings` equivalence, **not** to write the
probe. This is that drive's **static half** — everything obtainable without a model call. It closes two
of the design's assumptions, **refutes the premise's wording**, and leaves one question genuinely open.

## §A1.1 ✅ §S0's MECHANISM CLAIM IS NOW **DRIVEN**, NOT ASSUMED
§S0 asserted that the Claude lane is **self-sandboxing** and `$SANDBOX_PREFIX` is empty. That was read off
the design's own reasoning. It is now measured three independent ways:
```
  cell-claude.sh (the claude-lane launcher)   ZERO occurrences of `sandbox` or `SANDBOX`
  `sandbox-exec` across the FULL 70-file       5 files: _common_v3.sh · v3stage.sb · dry_cells.sh
    runtime export (not the 28-file _bin)        referee_v3.py · agy_launch_v3.sh
                                               -- NONE of them the claude subject launch
  a per-cell Seatbelt profile in ctl/           agy   24 of 145 cells carry one
                                               claude  0 of 129 cells carry one
```
⇒ **On this lane the client is the ONLY thing that can apply a sandbox.** §S0 stands, and now on evidence.
⛔ **AND THE CONSEQUENCE FOR ANY CHEAP PROBE: there is no per-cell profile artefact to diff.** The client
carries both `sandbox-exec` and `sandbox_init` and a Seatbelt `(version 1)` header string, so it does build
profiles — **but it leaves none in the cell.** A free, model-call-less equivalence test by comparing
rendered profiles **does not exist on this lane.** *(`_bin` is 28 files and the runtime is 70; the
population here is the export, for the reason banked one shift ago.)*

## §A1.2 ⛔⛔ THE PIN IS **2.1.259**, AND §S7 ITEM 1's "2.1.263 TODAY" IS A DIFFERENT OBJECT
```
  CLIENT lines across every ~/cells*/*/ctl/launch.log      195 lines over 145 cells
  versions named in them                                   2.1.259  x195      2.1.263  x0
  ~/.local/bin/claude ->                                   .../versions/2.1.263
```
⇒ **2.1.263 is the BOX's symlink. It is not what a single cell has ever launched.** `cell-claude.sh`
refuses a symlink as the pin precisely so this cannot happen at launch — and the *design document* then
took the version from the symlink anyway.
⇒ 🔑 ***A RECEIPT DRIVEN ON 2.1.263 WOULD BE A CLAIM ABOUT A CLIENT NO CELL OF THIS CAMPAIGN HAS USED.***
✅ **REGISTERED: the equivalence drive, and any probe built on it, runs on `2.1.259` — named as an absolute
versioned path, never through `~/.local/bin/claude`** — unless and until a freeze re-pins, in which case
the receipt is re-taken. *A one-time drive is a claim about a sha, never about a repo.*

## §A1.3 ⛔ THE PREMISE IS **REFUTED AS WRITTEN** — AT THE CLIENT'S OWN DOCUMENTED CONTRACT
`--help` on **2.1.259**, verbatim, under `-p, --print`:
> *"The workspace trust dialog is skipped when Claude is run in non-interactive mode (via -p, or when
> stdout is not a TTY…). Only use this in directories you trust. **Settings files that fail validation are
> silently ignored in this mode (no error dialog is shown).**"*

⇒ **`-p` and the subject's interactive launch are NOT identical in their handling of `--settings`, and the
client says so itself.** They also differ on workspace trust. The word **"identically"** in §S7 item 4
cannot stand.

### ⚠️ BUT THE DIRECTION MATTERS, AND THE DESIGN SURVIVES IT — SAID PRECISELY, NOT CONCEDED BROADLY
A settings file silently ignored means **no sandbox**, which makes the **OUTSIDE read SUCCEED**, which §S2
already scores **`HOLD: the fence is not binding for this cell`**.
⇒ **The asymmetry fails toward a FALSE ALARM, never toward the false GREEN of §S3.** It does not create the
failure this probe most fears, and §S2's scoring table needs no change.
⛔ **What it DOES change is what a green MEANS:** a `-p` green is a green about a fence **that validated**.
It is silent about a fence that would have raised a dialog interactively — and *that* cell would have been
sandboxless in the probe and gated by a human in the real launch.
✅ **REQUIRED AMENDMENT TO §S2 — one line, and it is the load-bearing one:** *the probe must RECORD that the
settings file was actually LOADED, from the client's own report, and must never infer loading from observed
behaviour.* An unloaded fence and a loaded-but-permissive fence are byte-identical in §S2's outputs today.
⇒ 🔑 ***THIS IS §S3's DEFECT ONE LAYER DOWN: THE INSTRUMENT CANNOT DISTINGUISH "THE FENCE DID NOT BIND"
FROM "THERE WAS NO FENCE".*** §S3 caught it for the model's behaviour and missed it for the settings load.

## §A1.4 ⛔ AND §S2's PROBE INVOCATION IS **UNDER-SPECIFIED** — A SECOND WAY TO MEASURE THE WRONG THING
§S2 says *"one `claude -p` invocation … carrying THE CELL'S OWN `ctl/fence.json` via `--settings`, cwd =
the cell"* and stops. The subject's launch, read from `cell-claude.sh` at the object, is:
```
  exec env -i <explicit env list> "$CLAUDE_BIN" \
      --dangerously-skip-permissions --name "$ID" --model "$HEAD_ID" --effort high \
      --strict-mcp-config --setting-sources user,project \
      --tools "$TOOLS" --disallowedTools "$DISALLOWED" --agents "$agents" \
      --settings "$CELL/ctl/fence.json" "$prompt"          # cwd = the cell; NO -p
```
⭐ **Two of those flags are settings-relevant and neither is named in §S2:**
- **`--setting-sources user,project`** decides *which settings files load at all*. A probe that omits it
  loads a different set than the subject. **The fence is passed the same way and the SURROUNDING settings
  are not.**
- **`--dangerously-skip-permissions`** interacts with `sandbox.autoAllowBashIfSandboxed`, which §S1 calls
  *the handle* the whole design hangs on.
⇒ 🔑 ***AN EQUIVALENCE TEST MUST HOLD THE ENTIRE ARGV AND ENVIRONMENT CONSTANT AND VARY `-p` ALONE.***
Varying five things and attributing the result to one is how this campaign has produced wrong-population
readings all week. ✅ **REGISTERED as the drive's form**, including `env -i` with the launcher's own list.

## §A1.5 WHAT IS STILL OPEN — ONE QUESTION, STATED SO IT IS NOT MISTAKEN FOR SETTLED
⛔ **For a fence that DOES validate, is the sandbox applied under `-p` the same as the one the subject's
launch applies?** The static half cannot answer it: the client leaves no profile artefact (§A1.1), so the
answer requires **both arms driven live** — a `-p` arm and a subject-shaped interactive arm — on 2.1.259,
argv-constant per §A1.4.
⚠️ **It is NOT blocked and nothing is waiting on a person.** It is deliberately not improvised beside a
live wave: the comparison arm is a **subject-shaped launch**, which is a cell-shaped act, and *a cell
directory is evidence, not scratch.* ✅ **The §B7 row-8 copy-guard that gives that law teeth merged to
`saltbench-systems` master this shift** and is not yet in any export.
⇒ **Release condition:** the live drive runs in a purpose-staged cell, on 2.1.259, once the level-4
tripwire has been read. **Owner: bench. Re-measure timeout: next relight.**

## §A1.6 ⇒ THE ONE TO CARRY
The design's central premise was **wrong in its wording and right in its substance**, and the static half
is what separated those. ⭐ **Two of the three findings above came from reading the client's OWN `--help`
and the launcher's OWN argv** — objects that cost nothing, were available the whole time, and were
summarised from memory instead.
⇒ 🔑 ***"UNDRIVEN" WAS TREATED AS "NEEDS AN EXPERIMENT", AND MOST OF IT NEEDED A READ.*** The experiment is
the small remainder, and it is now a sharper experiment because the read came first.

---

# ADDENDUM 2 — **§A1.3's OWED LINE IS DISCHARGED BY A DRIVEN, FREE INSTRUMENT**, same shift
## bench, 2026-09-13. Four arms, driven on the pinned **2.1.259**, **zero model calls.**

ADDENDUM 1 §A1.3 registered one line as owed: *the probe must RECORD that the settings file was LOADED,
from the client's own report, and never infer loading from behaviour.* It did not say **how**, and an owed
line with no instrument beside it is the shape that sits open for weeks. **The instrument exists, it is
free, and it is the client's own `doctor` subcommand** — whose `--help` says it *"reads settings files in
the current directory without a trust prompt."* It also honours the **global `--settings`**.

## §A2.1 THE DRIVE — FOUR ARMS, `claude --settings <file> doctor`, NOTHING ELSE
```
  ARM                                              rc   "Invalid settings" block   what it reported
  good.json    a REAL rendered cell fence          0    ABSENT                     (loaded)
               (sandbox.enabled true, 63 denyRead)
  bad.json     malformed JSON                      0    PRESENT                    "Invalid or malformed JSON"
  schema.json  VALID JSON, bogus schema            0    PRESENT                    "permissions: Expected
               {"sandbox":"not-an-object",                                          object, but received number"
                "permissions":42}
  m1.json      good.json with sandbox.enabled      0    ABSENT                     (loaded)
               flipped to FALSE  (= §S5's M1)
```
⇒ ✅ **The client reports a load failure, NAMES THE FILE BY ABSOLUTE PATH, and validates SCHEMA rather than
merely JSON syntax** — `schema.json` parses fine and is still rejected, with the offending key path.
✅ **REGISTERED into §S2: every cell records its fence's LOAD RECEIPT from `--settings <fence> doctor`,
taken at launch, free, before any model call.** A fence that does not load is a cell that does not fire.

## §A2.2 ⛔ TWO LIMITS, AND BOTH ARE LOAD-BEARING
1. ⛔⛔ **`rc` IS 0 IN ALL FOUR ARMS — INCLUDING BOTH FAILURES.** The verdict is the **presence of the
   `Invalid settings` block**, never the exit status. ⇒ 🔑 ***AN INSTRUMENT WHOSE rc IS CONSTANT ACROSS ITS
   OWN RED ARMS WILL BE WIRED TO THAT rc BY THE NEXT HAND, AND IT WILL PASS EVERYTHING.*** This desk's own
   banked card is *an rc whose meaning the reader supplies*; here the client hands one over.
2. ⭐ **THE `m1` ARM IS WHAT FIXES THE INSTRUMENT'S SCOPE, AND IT IS WHY IT WAS DRIVEN.** A fence with
   `sandbox.enabled: FALSE` **loads perfectly cleanly.** ⇒ **`doctor` reports LOADED. It never reports
   BINDING.** It closes exactly the gap §A1.3 named — *unloaded* vs *loaded-but-permissive* — and it closes
   **nothing else**. ⛔ **A `doctor` green is NOT a sandbox receipt** and must never be recorded as one;
   §S2's outside/inside pair remains the only thing that can say the fence binds.

## §A2.3 ⚠️ MY OWN NEAR-MISS ON THIS EXACT MEASUREMENT, DECLARED BECAUSE IT ALMOST SHIPPED
My first read of these two arms was through `head -12` and the two outputs were **byte-identical**, so I
wrote — briefly — that `doctor` **cannot** distinguish a valid fence from a broken one, and was about to
register that *no free load-receipt instrument exists on this client.* **The `Invalid settings` block is at
line 14.** The full `diff` of the two arms is what refuted me.
⇒ 🔑 ***I NEARLY CLAIMED AN ABSENCE FROM A TRUNCATED READ, AND A TRUNCATED READ FAILS TOWARD ABSENCE.***
It is the same shape as ADDENDUM 1 §A1.6 — *treating "undriven" as needing an experiment when it needed a
read* — one turn later, with the read itself cut short. **Diff the arms in full; never `head` a control.**
