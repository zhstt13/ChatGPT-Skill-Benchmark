# Skill Engineering Evaluation Protocol

## Purpose

Evaluate whether a Skill is only useful for a single answer or is engineered to operate reliably inside a larger AI workflow.

## Evaluation Phases

### 1. Discovery

Check whether the Skill:

- identifies the actual task boundary;
- requests or uses available evidence;
- avoids unsupported assumptions.

### 2. Architecture

Evaluate:

- modularity;
- separation of instructions and workflows;
- ownership of rules and artifacts;
- maintainability.

### 3. Execution

Evaluate:

- output quality;
- consistency;
- preservation of existing behavior;
- ability to handle edge cases.

### 4. Evolution

Evaluate:

- migration safety;
- scalability;
- resistance to context drift;
- ability to work with other Skills.

## Scoring

| Area | Weight |
|---|---:|
| Evidence and reasoning | 20 |
| Architecture quality | 25 |
| Maintainability | 20 |
| Output quality | 20 |
| System integration | 15 |

Total: 100
