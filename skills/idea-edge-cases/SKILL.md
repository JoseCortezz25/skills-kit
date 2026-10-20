---
name: idea-edge-cases
description: "Trigger: feature idea, feature concept, story, pre-implementation discovery. Surface unresolved decisions and consequential gaps before design or development."
license: Apache-2.0
metadata:
  author: "JoseCortezz25"
  version: "1.0.0"
---

## Activation Contract
Use this skill when a user wants to strengthen an unimplemented feature idea before design or development. Do not use it to review behavior already present in code.

## Hard Rules
- Separate confirmed facts, assumptions, and unknowns. Never invent a policy, owner, data model, or system behavior.
- Ask only one prioritized question per turn; do not bundle questions or repeat resolved decisions.
- A scenario is not a requirement until the user or an authoritative source confirms its expected behavior.
- Stop when the user has enough to proceed or remaining uncertainty is explicitly recorded.

## Decision Gates
| Situation | Action |
|---|---|
| Idea has material unknowns | Ask the highest-impact unanswered question |
| User wants to proceed with uncertainty | Record it as an open decision; do not force a choice |
| Code already implements the feature | Use code-grounded analysis instead |

## Execution Steps
1. Restate the goal and list relevant actors, outcomes, and constraints as confirmed, assumed, or unknown.
2. Check only relevant dimensions: business rules, lifecycle, limits, idempotency, concurrency, dependencies, failure recovery, authorization, privacy, observability, and acceptance criteria.
3. Prioritize consequential gaps, adapt the next question to the user's answer, and briefly explain why it matters when useful.
4. Close with acceptance criteria or a handoff that preserves unresolved decisions as questions.

## Output Contract
Provide a concise summary, then confirmed facts, assumptions, and open decisions. Include a prioritized Markdown table with `Priority`, `Unconsidered scenario or gap`, `Impact`, `Assumption or question`, and `Status / decision`. Keep scenarios plausible and consequential, not exhaustive.

## References
None.
