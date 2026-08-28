# EXCLUSIONS — wave 1

Created with its header **before the first model call**, because a named log that does not
exist is a stale known hole: the first exclusion would otherwise invent its own fields,
after the outcome is visible.

⛔ **Exclusion is ARM-INDEPENDENT BY CONSTRUCTION.** An instance is excluded **iff**:

- **(i) pre-flight** — an empty patch at the base commit fails to produce all-F2P-fail and
  all-P2P-pass; or
- **(ii) gold-control** — the gold patch, applied in the same image, fails to resolve.

Both run **before either arm**, so the decision cannot depend on arm outcomes.

⛔ **A per-arm run failure that an arm-independent control does not reproduce scores
UNSOLVED for that arm. It is NEVER an exclusion.** One-arm failures are discordant pairs,
and discordant pairs carry 100% of the McNemar information — dropping two unfavourable
ones can flip significance at this n.

📌 Pre-flight and gold-control results are logged for **ALL 80 selected instances**, not
only excluded ones. **The absence of rows for survivors is what makes the exclusion set
auditable**; a log containing only exclusions proves nothing about what was not excluded.

Excluded pairs are **not refilled** (refilling is a re-draw). `n_effective` and the
exclusion count appear in the headline.

| instance_id | decided_at | trigger | report.json sha256 | raw log | arm_scores_sealed | decider |
|---|---|---|---|---|---|---|
| *(none yet — no run has occurred)* | | | | | | |
