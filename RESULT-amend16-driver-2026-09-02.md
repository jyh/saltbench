# RESULT — AMENDMENT 16's DRIVER, AND THE FIRST METERED EPISODES ON THE S2-RUST SUBSTRATE

**2026-09-02, seat `bench`.** Companion to `AMENDMENT-16-regime-boundary-2026-09-02.md`.
Authorization: the helm's 09/01 23:12 release and its 09/02 00:02 word (*"the S2-Rust episode driver + its
agent fence, derived from `$BENCH` from the first line, run-shaped dry at zero model tokens, THEN stage 0.5
priced and posted, then run"*).

---

## §1 · WHAT WAS BUILT

`episode_s2rust.sh` (the episode driver) · `settings.s2rust.template.json` + `render_settings_verus.py` (the
agent fence, derived) · `dry_exec_stub_s2rust.sh` + `selftest_dry_s2rust.sh` (the run-shaped dry as an
outcome matrix) · `sync_studio_s2rust.sh` (the isolated transport) · `selftest_settings_verus.py`.

**Suite: 97 → 113 arms, 0 failed.** A dry episode lands on the Studio, on an isolated root, under the
provisioned toolchain, at zero model tokens.

**The isolation, asserted rather than intended.** `~/bench-rust` has its own REAL harness and its own config
dir `~/.claude-bench-rust`. Every sync receipt asserts `~/bench/harness` **BYTE-UNCHANGED** (`c30746f0…`,
freeze commit `15cfdc2`) and `~/.claude-bench/settings.json` **BYTE-UNCHANGED** (`59c0b2fa…`), because stage
C's dispatch window is still open and its harness is the only one on that machine.

---

## §2 · ⛔⛔ THE FINDING THAT COST THE MOST AND IS WORTH THE MOST

**The first scored S2-Rust episode PASSED — and could not be audited.**

`ep-b5e58301` · `a0` · `claude-opus-5` · `DONE` · **`PASS`** · 1,208,459 metered · 386 s · 30 calls.
The verdict itself is sound at the artifact: `screen_violations []`, `helpers_shape_violations []`,
`lynette_rc 0`, count guard `external_body` **2 → 2** (the benchmark's own stubs, none added),
referee **11 verified, 0 errors**, not partial, no rlimit hit, and — the field that exists because of this
amendment — **`fenced: true`** with the profile sha recorded.

But its manifest read **`rt_calls = 0`**: the agent never invoked the referee wrapper. That is either a
choice or an inability, and the two have opposite consequences for every arm comparison this campaign will
make — an agent that *cannot* check its work is being given a different task than the one registered.

**I could not tell which.** The artifact that answers it — the session transcript — had never been archived,
and the next episode's cleanup deleted it.

> 🔑 **A PORT THAT KEEPS THE SHAPE AND DROPS THE EVIDENCE PRODUCES EPISODES THAT SCORE BUT CANNOT BE
> AUDITED — and a result you cannot audit is not a cheaper result, it is a different kind of object.**

### What the port had dropped, all of it present in `s2lean/episode_s2.sh:297-311`

| dropped | what it is for |
|---|---|
| `cp "$JSONL" "$ST/session.jsonl"` | the transcript — the only record of what the agent did |
| escape/url pattern audit → `network_audit.txt` | the hermeticity evidence the campaign certifies runs with |
| VOID detection (subagent dirs, extra jsonls, `void_reasons`) | an episode that spawned a subagent would have scored normally |
| the `QUOTA(no_call)` rule | zero model calls is a quota symptom, never a result |
| the config-dir archive and RESET | hermeticity for the NEXT episode |

**None of it is on the happy path**, which is why nothing complained: the driver refused, prepared, launched,
checked and landed exactly as designed, and produced a clean-looking `PASS`.

⇒ The first scored episode is **UNCERTIFIABLE** and is kept as the specimen at
`~/bench-rust/specimen-unauditable/`, not deleted. It is re-run under the repaired driver.

### The manifest now carries the audit, not only the verdict

`escape_attempts_blocked` · `escape_unblocked` · `url_mentions` · `void` · `void_reasons` ·
`session_jsonl_sha256` (tying the record to the exact transcript that produced it) · `tool_uses` ·
`bash_commands` — the last being precisely the field that answers the `rt` question.

📌 **And one of mine caught before it landed:** my first cut wrote `tool_counts`, a key `meter.py` has never
emitted. It would have recorded `null` in every manifest and read, to anyone scanning, as *"this episode used
no tools"*. **A DEAD FIELD IS NOT A CHEAP FIELD** — a law this seat banked the day before and re-earned.

---

## §3 · THE OTHER DEFECTS OF MINE, EACH CAUGHT BY DRIVING

1. **The dry's outcome matrix returned the same class six times and looked healthy.** The rig steered the
   stub with `STUB_MODE=` on the driver's command line — and the driver launches the agent under `env -i`.
   The knob was never connected: six runs, one measurement.
   ⇒ ***A TEST RIG THAT STEERS ITS SUBJECT THROUGH A CHANNEL THE SUBJECT FENCES OFF MEASURES THE DEFAULT PATH
   N TIMES AND CALLS IT N CASES.*** Now arm **D0**: three modes must yield three classes.
2. **A registered prediction failed and the instrument was right.** `badhelp` → predicted `HELPERS_SHAPE`,
   measured `SCREEN`; the screen already carries the helpers table and fires first. Under `--no-screen` the
   same artifact returns `HELPERS_SHAPE`, which is what that layer is for. Corrected in the record, not deleted.
3. **The pin emitter carried a hand-written file list** and was stale within one commit.
   ⇒ ***AN ABSENCE-LIST CARRIES THE SAME STALENESS AS THE PRESENCE-LIST IT COMPLEMENTS*** — while reading,
   to a reviewer, exactly like an audit. It now enumerates every file and excludes by KIND; verified by
   counting keys against the directory (27 = 27, both ways).
4. **The sync receipt reported green while checking 1 file of 67** — `ssh` inside a `while read` loop ate the
   loop's input. ⇒ ***A RECEIPT THAT DOES NOT STATE ITS OWN DENOMINATOR CAN PASS ON A SAMPLE OF ONE.***
   Coverage is now BINDING, not printed.
5. **A probe whose fallback branch meant two things.** `readlink X || echo "REAL DIR"` prints the same for a
   path that does not exist; I nearly justified the whole isolation design on a precedent that was not there.
6. **The toolchain gate asked its two halves about two different machines** — T1 used the ambient PATH, T3
   set its own. On the Studio (where rustup was transported, not `rustup-init`'d) it reported
   *"no rustup on PATH"* and *"the fenced referee verifies"* three lines apart. Both true, of two machines.
   ⇒ ***A GATE THAT MEASURES TWO PROPERTIES UNDER TWO DIFFERENT ENVIRONMENTS IS TWO GATES, AND ONLY ONE OF
   THEM DESCRIBES THE RUN.*** ⭐ It refused all three episodes **before any model call** — the gate paying for
   itself on its first live use.
7. **The pilot's config reset was a delete-list, not a keep-list**, and killed two episodes on a directory it
   did not know about (`session-env/`). The same blacklist shape this wave already caught once.
8. **A killed episode never reaches its own cleanup**, so it poisons the config dir for every later episode.
   ⇒ **The RUN owns the precondition; the EPISODE owns the cleanup after itself.** Conflating them is what
   broke two attempts. The residue is preserved as a specimen, never deleted — it is the only surviving trace
   of the episode that was killed.

---

## §4 · THE PRICING, AND WHY IT CAME BEFORE THE SPEND

⛔ **The authorization's arithmetic could not hold, and the pricing step said so before a token was spent.**
*"cap 15M else n=30"* reads as though 30 episodes fit inside 15M. Against the campaign's own landed unit
costs (S2-Lean, stage B, `a0`):

| source | tokens/episode | 60 episodes | 30 episodes |
|---|---|---|---|
| stage-B **p50** (n=15) | 1,010,831 | ≈ 60.6M | ≈ 30.3M |
| stage-B **mean @R=100** (n=9) | 2,749,871 | ≈ 165M | ≈ 82M |

**15M buys ≈ 15 episodes at the p50, ≈ 5 at the mean.** ⇒ 🔑 **A CAP AND A SAMPLE SIZE ARE ONE CONSTRAINT,
NOT TWO — and a fallback `n` that was never priced is not a fallback.** Ratified by the helm as law.

📌 A second unit problem rides with it, already on the record: **the metered sum is not the quota unit**
(19.67M metered moved the 5-hour arm 0% → 9%), so "15M tokens" must say which it means.

⚖️ **The tier is the commission's, not the helm's memory of it:** §"Arms" registers **`claude-opus-5`**, so
the null is priced at Opus. A Sonnet price is a floor and does not transfer.

**§5 below carries the measured price. It is a PILOT median at n=3 and is reported with its denominator: the
campaign has already paid once for reading a small selected mean as a population mean.**

---

## §5 · THE MEASURED PRICE

*(pending — the pilot is re-running under the repaired driver; this section is filled from
`price.py` against the four registered predictions P1–P4, which were posted to the bus BEFORE the spend.)*
