# RESULT — SCOUT DY: DeepSWE's RUST SUBSET IS **5 OF 113**, AND THE VERDICT IS **NO**

**2026-09-02, seat `bench`.** Answers `SCOUT-DY-deepswe-registration-2026-09-02.md`, whose criterion was
committed (`744989e`) **before the dataset was fetched**. Zero model tokens, zero episodes.

---

## §1 · THE DATASET, IDENTIFIED SO THE COUNT IS REPRODUCIBLE

| | |
|---|---|
| source | `https://github.com/datacurve-ai/deep-swe` |
| revision | `0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea` (clone at 2026-09-02) |
| licence | **Apache-2.0** (`LICENSE`, and the repo's SPDX field) |
| dataset id | `deep-swe-1-1`, `manifest.json:task_count = 113` |
| leaderboard | `deepswe.datacurve.ai` — 113 tasks · 91 repos · 5 languages · 27 models, frontier **74% Pass@1** |
| schema keys | `manifest.json:tasks[].language` and each `tasks/<id>/task.toml:[metadata] language` |

📌 The corpus is **seat-only** at `~/bench-src/deep-swe` and does **not** enter this repo — the same fence
as `verus-proof-synthesis`.

## §2 · ⛔ THE COUNT THAT WOULD HAVE BEEN WRONG, CAUGHT BY THE REGISTERED RULE

`ls tasks | wc -l` returns **117**. The dataset has **113** tasks. The four extra entries are
`dataset.toml`, `README.md`, `manifest.json`, `manifest.schema.json` — index files sitting beside the task
directories. Counting directory entries would have reported 117 tasks and every downstream ratio would have
been wrong by 3.5%.

> 🔑 This is the **same shape** as the census this campaign already paid for — *"Multilingual Rust is 43 and
> Multi-SWE-bench is 239 — our 08/29 census was wrong, from substring-vs-exact-key."* Rule 1 of the
> registration (exact keys, print what you keyed on) is what caught it, and it caught it in the first minute.

## §3 · `n_rust` — TWO INDEPENDENT DERIVATIONS, REQUIRED TO AGREE

```
SOURCE A — manifest.json, keyed on the EXACT field `language`
   'typescript' 35 · 'python' 34 · 'go' 34 · 'rust' 5 · 'javascript' 5      total 113
SOURCE B — the 113 task.toml files, keyed on the EXACT line  language = "..."
   'typescript' 35 · 'go' 34 · 'python' 34 · 'rust' 5 · 'javascript' 5      total 113
AGREEMENT A vs B: IDENTICAL          n_rust = 5 of 113
```
Two derivations because one is the index the harness consumes and the other is the per-task record; a
disagreement between them would have been a finding in itself. They agree exactly.

## §4 · ⭐ THE VERDICT IS DETERMINED BEFORE THE SCREEN RUNS, AND THAT IS ITS STRONGEST FORM

The commission's rule is **≥ 8 ⇒ proceeds as v2's second population; ~3 ⇒ no**. `n_amenable` is by
construction a **subset** of `n_rust`, so

> **n_amenable ≤ n_rust = 5 < 8.**

⇒ **DY: NO.** The Rust subset cannot reach the threshold whatever the screen decides.
⇒ 🔑 **THE ANSWER DOES NOT DEPEND ON MY JUDGMENT.** The screen is the part of this scout I could have got
wrong in either direction — and a threshold met by a *ceiling* is immune to it. Where a census can be tuned,
say which part of the answer the tuning cannot reach.

## §5 · THE SCREEN, RUN ANYWAY, WITH EVIDENCE PER CLAUSE

Five tasks is few enough to screen by hand at zero cost, and the number matters if the corpus grows.
Markers counted on **added lines of each `solution.patch`**:

| task | repo | files | crates | disqualifying evidence | clause |
|---|---|---|---|---|---|
| `boa-hierarchical-evaluation-cancellation` | boa-dev/boa | 7 | 1 | `async` ×2, `unsafe` ×1, `RefCell` ×8, `Cell<` ×6, `Rc<` ×1 | **S4** |
| `fd-deterministic-multi-key-sorting` | sharkdp/fd | 5 | 1 | `SystemTime` ×6 (mtime/ctime/atime sort keys), `thread` ×1; `--sort random` | **S5**, S4 |
| `oxvg-structural-selector-preservation` | noahbald/oxvg | 3 | 1 | `RefCell` ×1, `Cell<` ×1; 819 added lines over a trait-abstracted AST | **S4** |
| `pest-character-class-coalescing` | pest-parser/pest | 5 | **4** | *no S4/S5 marker at all* — spans `generator`, `grammars`, `meta`, `vm` | **S6** |
| `wasmi-trap-coredumps` | wasmi-labs/wasmi | 11 | 1 | `unsafe` ×3; 11 files across the engine executor | **S4** |

### **`n_amenable` = 0 of 5.**

📌 **THE NEAR-MISS IS WORTH NAMING.** `pest-character-class-coalescing` is **clean on every subset clause** —
no `async`, `unsafe`, interior mutability, threads or I/O anywhere in its added lines — and it is a genuinely
functional property (a semantics-preserving transformation of an expression tree, exactly the shape Verus
likes). It fails only **S6**: the scored change spans four crates. *The coalescer pass alone would be
amenable; the task as the benchmark scores it is not, and those are different objects.* If DeepSWE's Rust
subset ever grows, this is the shape to look for.

## §6 · THE PREDICTION, SCORED

| | registered | measured | |
|---|---|---|---|
| `n_rust` | **15–30** of 113 | **5** | ❌ **FAILED**, far outside the band |
| `n_amenable` | 3–8, point 5 | **0** | ❌ **FAILED**, below the band |
| shape | *"the likeliest outcome is the unruled middle"* | a clean NO | ❌ |

⛔ **THE DEFECT IN MY OWN ESTIMATE, NAMED.** I reasoned *"five languages, roughly balanced, Rust one of
them"*. The measured distribution is **35 / 34 / 34 / 5 / 5** — three dominant languages and two token ones.
> 🔑 **"FIVE LANGUAGES" DOES NOT MEAN "FIVE EQUAL LANGUAGES."** A count of *categories* says nothing about
> the distribution *over* them, and I turned one into the other without noticing I had.

📌 I registered, in the same file, that I would **not** apply a bias correction here because *a correction
for a bias inherits the population the bias was measured on*. That restraint was right: the miss is not the
under-estimating-`a0` bias in a new place, it is a **different** error — assuming uniformity over a
partition. Correcting for the first would not have touched it.

## §7 · WHAT SURVIVES FOR THE CAMPAIGN

1. **Adaptation #2 (DeepSWE Rust + a Verus specification layer) is DEAD** on this corpus. Not marginal: 5
   Rust tasks, none amenable, against a threshold of 8.
2. **Adaptation #3 is UNAFFECTED and now cheaper.** The council adopted Harbor packaging as our shipping
   format *regardless of the scout*, and the clone is a working reference for it: `task.toml` (schema 1.3),
   `instruction.md`, `solution/`, `tests/{Dockerfile,config.json,grader.py,test.patch,test.sh}`,
   `environment/Dockerfile`, plus a `manifest.json` **with its own `manifest.schema.json`**. **DZ can read a
   real Harbor dataset instead of inferring the format.**
3. ⭐⭐ **AN INDEPENDENT THIRD-PARTY ANCHOR ON EXACTLY ROW DT's AXIS, FOUND FOR FREE.** DeepSWE's public
   leaderboard reports both tiers on the same 113 contamination-free tasks, at max effort:

   | model | Pass@1 | avg cost | output tokens | agent steps |
   |---|---|---|---|---|
   | `claude-opus-5` [max] | **74% ± 4%** | $11.84 | 118k | **99** |
   | `claude-sonnet-5` [max] | **54% ± 4%** | **$26.40** | 214k | **268** |

   **The lower tier scores 20 points lower AND costs 2.2× more AND takes 2.7× the steps.** Every direction
   agrees with our probe: Sonnet passes less (their 54 vs 74; our 0 of 3 vs 2 of 3) and works far longer.

   ⭐ **AND IT SHARPENS THE ONE CAVEAT ON OUR QUOTE.** Our probe priced Sonnet at **0.71× the Opus
   per-episode quota** — *cheaper*. This anchor says that uncapped it is **more expensive**. Both are true
   and the difference is the instrument: **our episodes are truncated at 40 turns, and truncation is what
   makes the weaker tier look cheap.** DeepSWE lets it run to 268 steps and it spends accordingly.
   > 🔑 **A CAP DOES NOT MAKE THE WEAKER TIER CHEAPER — IT MAKES THE MEASUREMENT OF ITS COST SHORTER.**
   This is the same law as *"a p90 computed from data the cap produced returns the cap"*, one field over,
   and it converts the RESULT's *"1.55× is a lower bound"* from a caution into a quantified expectation.
   ⇒ It also **corroborates the warning this seat posted to row DT at 08:35** — *a lower tier is not a
   cheaper run* — which the capped probe alone appeared to soften.

   ⚠️ **IT IS AN ANCHOR, NOT OUR MEASUREMENT, AND MUST NEVER BE PRESENTED AS ONE.** Different corpus,
   different harness, different scoring; their "cost" is API dollars and their "steps" are their agent's,
   neither of which is our quota or Claude Code turns. It is citable as external evidence for the
   weaker-model hypothesis and for nothing else.
