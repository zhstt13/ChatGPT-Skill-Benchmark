# Evolve Workflow

Use when an existing repository must be refactored, migrated, hardened, reorganized, or prepared for continued growth.

## Procedure

1. **Analyze first** — prove the current structure and problem before proposing mutation.
2. **Define the target contract** — state what should become simpler, safer, more discoverable, or more enforceable, and what behavior must remain unchanged.
3. **Build change impact** — identify affected modules, configs, docs, skills, tests, CI, generated files, integrations, and migration consumers.
4. **Prefer consolidation/deletion** — remove stale, duplicated, unreachable, or ownerless surfaces before introducing new abstractions.
5. **Migrate in bounded slices** — use the smallest complete change that proves the target boundary without forcing a broad rewrite.
6. **Harden the new structure** — add or update the checks that prevent drift back to the old pattern when practical.
7. **Validate preservation** — run targeted tests/checks and verify documentation/routing references after mutation.
8. **Record durable decisions** — write an ADR/decision record only when future maintainers need the rationale to avoid reversing the choice accidentally.

## Change Safety

Do not conflate architectural cleanup with product behavior changes. If a proposed structural change also changes a user-facing contract, external API, persistence model, security boundary, or irreversible data path, surface that explicitly before mutation.

## Output Shape

- Current → Target
- Change impact
- Ordered migration slices
- Preservation constraints
- Enforcement/validation plan
- Completed verification and unresolved risks
