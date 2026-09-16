# Source Catalog

This catalog tracks external skills and repositories used as evidence or inspiration for the benchmark. A source must be verified before it is treated as a reference implementation.

## Verified — Repository / Architecture

1. **WoJiSama/skill-based-architecture**  
   https://github.com/WoJiSama/skill-based-architecture  
   Use: modular skill architecture, progressive disclosure, large-skill decomposition.

2. **tvmaly/software-architecture-skill**  
   https://github.com/tvmaly/software-architecture-skill  
   Use: generating `ARCHITECTURE.md` and architecture diagrams from a codebase.

3. **objectivlabs/reposkillopt**  
   https://github.com/objectivlabs/reposkillopt  
   Use: evidence-grounded repository understanding, legacy repository analysis, bounded skill evolution.

4. **imadnan4/architect-skills**  
   https://github.com/imadnan4/architect-skills  
   Use: modular system-design practices and architect-level decision frameworks.

5. **mblode/agent-skills — codebase-architecture**  
   https://github.com/mblode/agent-skills/tree/main/skills/codebase-architecture  
   Use: codebase structure, boundaries, maintainability, architecture-focused eval patterns.

## Verified — Skill / Template Engineering

6. **anthropics/skills**  
   https://github.com/anthropics/skills  
   Use: public Agent Skills examples, packaging patterns, conventions, and skill organization.

7. **github/awesome-copilot**  
   https://github.com/github/awesome-copilot  
   Use: community-contributed skills, agents, instructions, and reusable configuration patterns.

8. **bcastelino/agent-skills-kit**  
   https://github.com/bcastelino/agent-skills-kit  
   Use: authoring, templates, validation, packaging, and meta-skill patterns.

## Verification Rule

A repository is only promoted into `Verified` when its GitHub repository and relevant path have been confirmed. Earlier candidate links that are not yet verified must not be used as benchmark ground truth.

## Synthesis Direction

The benchmark will use these references to build and test a composite **AI Repository Engineer** skill with three major modes:

- **Create** — generate repository templates and project scaffolding.
- **Analyze** — understand, map, and audit existing repositories.
- **Evolve** — plan refactors, migrations, and architecture-preserving changes.

The benchmark must compare this composite approach against narrower specialist skills rather than assuming the composite design is superior.
