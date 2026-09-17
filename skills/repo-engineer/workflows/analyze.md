# Analyze Workflow

Use for understanding, auditing, or documenting an existing repository.

## Procedure

1. **Establish scope** — identify the repository snapshot, task boundary, and requested outputs.
2. **Map entry surfaces** — root files, apps/services/packages, build/test/config, agent instructions, skills, docs, CI, and deployment surfaces that actually exist.
3. **Trace ownership** — for each important concern, identify the canonical owner and flag duplicate or conflicting owners.
4. **Trace dependencies** — record module/package direction, runtime integrations, generated surfaces, and key data/control flows where evidence supports them.
5. **Find architecture pressure** — coupling, naming divergence, duplicated concepts, unclear boundaries, stale/dormant configuration, unreachable rules, or missing enforcement.
6. **Rank findings by evidence and impact** — prefer concrete path-backed findings over general style advice.
7. **Produce only necessary artifacts** — repository map, architecture document, risk list, or improvement plan as required.

## Evidence Standard

Every repository-specific claim should be traceable to a file, path, configuration, dependency declaration, commit history, or executed check. Mark uncertain conclusions as hypotheses.

## Output Shape

- Current architecture
- Canonical owners
- Dependency/boundary observations
- Proven risks or friction points
- Ranked improvement opportunities
- Verification performed / unavailable
