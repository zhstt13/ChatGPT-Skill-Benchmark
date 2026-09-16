# Source Catalog

External repositories below are **reference material**, not benchmark ground truth and not copied implementations. Their current verified repository revisions are pinned in [`SOURCE_LOCK.json`](SOURCE_LOCK.json).

| ID | Source | Use in synthesis |
|---|---|---|
| `skill-based-architecture` | `WoJiSama/skill-based-architecture` | modular skill architecture and progressive disclosure |
| `software-architecture-skill` | `tvmaly/software-architecture-skill` | architecture extraction patterns |
| `reposkillopt` | `objectivlabs/reposkillopt` | evidence-bounded repository analysis and evolution |
| `architect-skills` | `imadnan4/architect-skills` | system-design decision framing |
| `agent-skills-codebase-architecture` | `mblode/agent-skills` / `skills/codebase-architecture` | codebase boundaries and maintainability patterns |
| `anthropics-skills` | `anthropics/skills` | public skill packaging conventions |
| `awesome-copilot` | `github/awesome-copilot` | reusable agent/configuration patterns |
| `agent-skills-kit` | `bcastelino/agent-skills-kit` | authoring and validation patterns |

## Verification rule

A source is usable as a reference only when its repository and any named path have been checked and a revision is recorded in the lock file. If a source changes, refresh the lock deliberately; do not silently treat a moving default branch as stable evidence.

## Synthesis rule

The `ai-repository-engineer` Candidate synthesizes ideas from these references, but must be benchmarked against the same cases as narrower Candidates. A source link is never evidence that the Candidate performs well.

