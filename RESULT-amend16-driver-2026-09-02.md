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

## §2b · ⛔⛔ AND THEN THE AUDIT PAID FOR ITSELF IMMEDIATELY: TWO EPISODES HAD PASSED **BLIND**

The repaired driver archived a transcript, and the very first thing it showed was that `rt_calls = 0` was
not a choice.

| measured on `ep-3fba0475` | |
|---|---|
| `denyRead` contains | `/Users/jyh/bench-rust` |
| episode dir | `/Users/jyh/bench-rust/work/ep-3fba0475` — **inside it** |
| `tool_uses` | `{"Bash": 18, "Edit": 2, "Read": 4, "ToolSearch": 1}` |
| `rt_calls` | **0** — the wrapper never logged even a START |
| `escape_unblocked` / `void` | `[]` / `False` — the fence itself held |

The transcript shows the agent trying `../rt verus task.rs`, then the absolute path, then a wrapper script in
`$TMPDIR` — **three attempts** — and then spending ten Bash calls hunting for a `verus` it was never going to
reach. It then wrote a proof it could not check. **The proof PASSED. Twice** (1,208,459 and 846,079 tokens).

**The cause is row CO's own repair meeting a placement decision.** Deriving `denyRead` from `$BENCH` makes the
fence follow the state root — correct, and the whole point of CO. It becomes self-defeating the moment the
episode tree is placed *inside* that root, because the agent's `rt` and task file then sit in a denied
subpath. S2-Lean never hit it only because its `EPROOT` (`$HOME/work`) happens to sit outside `~/bench` — an
accident, exactly like the symlink accident that protected the sibling roots *before* CO.

> 🔑 **A FENCE DERIVED FROM THE RUN ROOT MUST NOT CONTAIN THE AGENT'S OWN WORKSPACE.**
>
> 🔑 **AND THE EPISODE STILL SCORED.** A blind agent that passes is not a cheap pass — it is a measurement of
> a **different task** than the one registered, and nothing downstream could have told the difference.

⚠️ **The `rt` probe gave false comfort.** It runs harness-side, unfenced, so it certified that the wrapper
works *for the harness* while the agent could not execute the same file. That is the toolchain gate's lesson
in a second costume: two claims measured under two environments, only one of which describes the run.

**The repair is a REFUSAL, not a warning** — an episode the agent cannot check its work in must not be
scored. Driven both ways: `EPROOT` inside `$BENCH` → `FENCE SELF-BLOCK`, naming the dir and the denied path;
outside → `fence/workspace disjoint`, episode lands. Plus arms **C10/C11** (settings suite now 11 arms).

📌 **The two blind PASSes are kept at `~/bench-rust/specimen-unauditable/` and are NOT counted.** They are
also the only evidence that `a0` can pass this benchmark *with no referee at all* — a question worth its own
registered experiment, but not the one that was registered.

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

## §4b · ⭐ THE COST OF THE BLINDNESS, QUANTIFIED — AND MY OWN PRICING CLAIM CORRECTED

The same task, the same arm, the same model. The only difference is whether the agent could reach `rt`:

| | blind (`ep-b5e58301`) | blind (`ep-3fba0475`) | **sighted (`ep-b115dc91`)** |
|---|---|---|---|
| metered | 1,208,459 | 846,079 | **76,003** |
| wall | 386 s | 447 s | **65 s** |
| tool calls | 30 | 26 | **4** |
| `rt_calls` | 0 | 0 | **1** (rc 0) |
| escape attempts blocked | — | 2 | **0** |
| class | PASS | PASS | **PASS** |

**A blind episode cost 11-16x a sighted one** — the tokens went into hunting for a binary the agent could
never reach, and the escape attempts were that hunt hitting the fence.

⛔ **AND THIS CORRECTS A CLAIM I POSTED TO THE BUS BEFORE THE SPEND.** I wrote that *"15M buys ~15 episodes,
not 30"*, priced off S2-Lean's stage-B p50 of 1,010,831 — while explicitly warning, in the same post, that
every number I had came from another substrate. A sighted S2-Rust episode measures **76,003**, roughly
**13x cheaper**, at which 60 episodes cost ≈ 4.6M and sit comfortably **inside** the 15M cap.

**What survives and what does not:**
- **SURVIVES (and the helm banked it as law):** *a cap and a sample size are one constraint, not two* — a
  fallback `n` that was never priced is not a fallback. That is a statement about the shape of the
  authorization and it is independent of the number.
- **DOES NOT SURVIVE:** my specific arithmetic. "15M buys ~15 episodes" was a cross-substrate extrapolation,
  and I made exactly the error I had named one paragraph earlier.

⇒ 🔑 **NAMING A HAZARD IS NOT THE SAME AS BEING PROTECTED FROM IT.** I labelled the S2-Lean figures as
foreign, reasoned from them anyway because they were the only figures I had, and posted the conclusion in
bold. The pilot was the right instrument and it arrived one post too late to stop the claim.

---

## §4c · THE HELPERS WHITELIST REFUSED A LEGITIMATE HELPER LEMMA — ARM-CORRELATED, THIRD INSTANCE

`ep-ef8d8dbb` wrote a memory-region helper lemma and was landed `HELPERS_SHAPE`:

```
proof fn lemma_...(...)
    ensures !overlap(
        MemRegion { base: i, size: s.core_states[ci].pte_size(...) },
        MemRegion { base: j, size: s.core_states[cj].pte_size(...) })
{ ... }
```

`helpers_shape` split items by **brace depth**, so the **struct literals in the `ensures` clause** opened and
closed depth at top level and ended the item **mid-signature**; the remainder scored "not a `proof fn`".

> 🔑 **A FIXTURE SUITE PROVES THE SHAPES YOU IMAGINED; ONLY THE POPULATION PROVES THE ONES YOU DIDN'T.**
> 29 screen arms, 18 fence arms and an 11-arm fixture kit all passed. The **third episode ever run** found it.
>
> 🔑 **AND IT IS ARM-CORRELATED, IN THE SAME DIRECTION AS AMENDMENT 15's FATAL 3.** `a2` encourages helper
> lemmas; richer helpers carry struct literals in their specs; so the gate refused the treatment for applying
> the treatment — **inside the very layer added to prevent the first instance of that error.** Ask of every
> gate which arm is likelier to trip it, and ask it again of the gate you added to answer that question last time.

**Repair:** items split by **top-level line structure**, not brace depth — the region is top-level by
construction, so an item begins at a line at the region's base indentation starting with an attribute or an
identifier, and a bare `{`/`}` there is body punctuation. Fails **closed**: non-blank content with no
recognisable item start is a violation.

⛔ **A second defect inside my own repair, caught by a GREEN arm:** `#[verifier::rlimit(50)]` sits at the same
column as the `proof fn` it decorates, so the split made it a separate item declaring nothing — and `rlimit`
is one of the five attributes lynette itself calls a proof instruction, i.e. **explicitly allowed**, and
exactly what a helper-writing arm reaches for. Attributes now attach forward; a dangling attribute is its own
violation. ⇒ **A REPAIR VALIDATED ONLY ON THE CASE THAT PROMPTED IT IS HALF-MEASURED.**

**Driven:** 14 arms on `helpers_shape` (5 green including the real shape, 9 red). `screen_verus` 29 → 32 arms.

📌 **The registered control holds: the screen over all 207 REFERENCE BODIES returns 0 defects.** ⛔ My first
run of it reported **207 of 207** and I nearly filed a regression — I had fed it whole ground-truth **files**
instead of the proof **bodies** the screen operates on, and a whole file legitimately contains `use`,
`fn main` and `external_body`. ⇒ 🔑 **A CONTROL FED THE WRONG OBJECT REPORTS A CATASTROPHE OR AN ALL-CLEAR
WITH EQUAL CONFIDENCE.** The right object is `frozen.json:proof_interior_original`.

---

## §5 · THE MEASURED PRICE, AND THREE OF FOUR REGISTERED PREDICTIONS FAILED

**Pilot: n = 3, `a0`, `claude-opus-5`, seeded 20260902 from the LIVE 180.** Registered on the bus BEFORE the
spend. Total metered **1,154,783**.

| task | class | metered | wall | calls | `rt_calls` |
|---|---|---|---|---|---|
| `…lemma_interp_of_entry_between` | **PASS** | 76,003 | 65 s | 4 | 1 |
| `…lemma_candidate_mapping_inflight_pmem_overlap_hl_implies_os` | **PASS** | 466,390 | 126 s | 17 | ≥1 |
| `…no_overlaps_applied_mappings` | **PASS** *(re-scored)* | 612,390 | 286 s | 19 | ≥1 |

**median 466,390 · mean 384,928 · min 76,003 · max 612,390 (n=3)** · wall 1.1–4.8 min.

📌 The third was landed `HELPERS_SHAPE` by the false refusal of §4c and **re-scored from its archived agent
artifact** under the repaired checker — no new spend: `45 verified, 0 errors`, `fenced true`, `lynette_rc 0`,
count guard `external_body` 12→12 and 1→1, both unchanged.

### The predictions, scored

| | prediction | measured | |
|---|---|---|---|
| **P1** | median **>** S2-Lean p50 (1,010,831); band 3M–8M | **466,390** | ❌ **FAILED** — and ~10x below the band |
| **P2** | `a0` passes **0 or 1** of 3 | **3 of 3** | ❌ **FAILED** |
| **P3** | wall 5–25 min each | **1.1 / 2.1 / 4.8 min** | ❌ **FAILED** |
| **P4** | ≤ 1 `ROUNDS_EXHAUSTED` | **0** | ✅ HELD |

**I was wrong in the same direction three times: I priced S2-Rust as harder and slower than it is.** My
reasoning was that the task files are large (median 32,979 B), so reading alone would be expensive.
⇒ 🔑 **A BIG FILE IS NOT A BIG TASK.** Episode cost is driven by the difficulty of the proof, not the bytes
of context.

### ⭐⭐ AND `a0` PASSING 3 OF 3 IS A CAMPAIGN-LEVEL SIGNAL, NOT A CONVENIENCE

Plain `a0`, no salt, cleared every drawn LIVE task at Opus-5. That is the **CEILING** shape S2-Lean already
met once (`P0 = 12/12 ⇒ CEILING HOLD`): **an arm at ceiling leaves no room for a treatment effect to show**,
and the drawn `n`, the tier and the task difficulty band all have to be re-read before a scored comparison is
worth paying for. **n = 3**, so this is a signal and not a reading — but it is the signal that decides what
stage 0.5 is even measuring.

### Sizing, at the measured median, with its denominator

| | at median 466,390 | at worst observed 612,390 |
|---|---|---|
| 60 episodes (the commission's null) | **≈ 28.0M** | ≈ 36.7M |
| 30 episodes (the fallback `n`) | **≈ 14.0M** | ≈ 18.4M |

**15M buys ≈ 32 episodes at the median.** So `n = 30` fits the cap at the median (14.0M) and **breaks it at
the worst observed (18.4M)** — the authorization is marginal rather than impossible, which is neither what I
claimed earlier nor what the wording assumed.

⛔ **This is the second correction to my own pricing in one hour, and both were the same error.** First I
priced 60 episodes off S2-Lean's p50 — a foreign substrate — and got 60.6M. Then, from the single cheapest
sighted episode (76,003), I reasoned toward 4.6M. The n=3 median says 28.0M.
⇒ 🔑 **THE FIX FOR A NUMBER FROM THE WRONG POPULATION IS NOT A NUMBER FROM A SMALLER ONE.**
