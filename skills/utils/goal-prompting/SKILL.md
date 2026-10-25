---
name: goal-prompting
version: 1.0.0
description: Use when creating, rewriting, reviewing, or optimizing prompts for /goal, goal mode, Codex goal mode, long-running coding agents, autonomous coding tasks, or concrete agent milestones. This skill turns vague work requests into short, verifiable, measurable /goal prompts with guidance, constraints, progress tracking, and cleanup criteria. Trigger even when the user says "make this a goal", "goal prompt", "optimize this prompt for an agent", "run this with /goal", or asks how to structure work for a coding agent.
---

# Goal Prompting

Use this skill to create prompts that work well with `/goal` or any long-running coding agent that must continue until a concrete outcome is reached.

The key idea: a goal prompt is not just an initial instruction. It is the agent's exit criteria. If the criteria are fuzzy, the agent cannot reliably know when to stop.

## Core Principles

Design every goal around these seven checks:

1. Verifiable completion criteria: define what must be true before the agent stops.
2. Starting guidance: give useful pointers, likely files, tools, constraints, and known risks.
3. Progress measurement: state how the agent should measure improvement or parity.
4. Realistic environment: specify the environment that counts as valid proof.
5. Visual caution: treat images as context, not the only success criterion.
6. Progress tracking: ask for durable checkpoints when the work may take a long time.
7. Cleanup and review: require reflection, removal of failed attempts, and final validation.

## Workflow

When asked to create or improve a `/goal` prompt:

1. Extract the actual desired outcome.
2. Convert vague language into observable acceptance criteria.
3. Prefer numeric targets when they are meaningful.
4. Add measurement commands, tests, benchmarks, screenshots, logs, or review artifacts.
5. Add boundaries that prevent bad shortcuts.
6. Keep the final `/goal` prompt concise enough to act as exit criteria.
7. If important information is missing, ask one focused question before drafting.

Do not turn the goal into a giant implementation plan. A goal prompt can reference a plan file, issue, spec, or benchmark, but the prompt itself should stay focused on the outcome.

## Goal Prompt Template

Use this structure by default:

```text
/goal [Outcome]

Completion criteria:
- [Verifiable criterion 1]
- [Verifiable criterion 2]
- [Verifiable criterion 3]

Start here:
- [Likely files, commands, docs, logs, screenshots, or systems]

Measure progress with:
- [Tests, benchmarks, production-like checks, visual diff tools, traces, coverage, timing, metrics]

Constraints:
- [No shortcuts, no reduced coverage, no fake data unless allowed, no visual asset hacks, no broad rewrites unless needed]

Progress tracking:
- [Commit/checkpoint/report cadence if long-running]

Before finishing:
- [Review, cleanup failed attempts, rerun validation, summarize evidence]
```

If the user wants a shorter output, collapse the sections into one compact prompt while preserving the same information.

## What Good Looks Like

Strong goal prompts include proof:

```text
/goal Reduce CI build time by at least 30% without weakening tests.

Completion criteria:
- Median CI build time on the same branch drops from the current baseline by >=30% across 3 comparable runs.
- Test coverage and required quality gates are not reduced.
- The final PR explains each optimization and includes before/after timings.

Start here:
- Inspect the CI workflow files, dependency installation, caching, and build steps first.

Measure progress with:
- Record the current baseline, then rerun comparable CI or local CI-equivalent commands after each meaningful change.

Constraints:
- Do not skip tests, remove checks, or hide failures to improve timing.

Before finishing:
- Remove failed experiments, run the full validation path, and summarize evidence.
```

Weak goal prompts lack stopping power:

```text
/goal Make CI faster.
```

That is too vague because the agent cannot know what "faster" means, whether shortcuts are allowed, or what proof is sufficient.

## Handling Visual Goals

For UI or design work, avoid using "100% pixel perfect" as the only target. Visual matching can send agents into low-value loops.

Prefer a combined goal:

```text
/goal Implement the dashboard UI from the provided reference using the existing design system.

Completion criteria:
- All states in the referenced spec are implemented: loading, empty, error, populated, and mobile.
- The page passes accessibility checks for keyboard navigation, labels, color contrast, and responsive layout.
- A screenshot comparison shows no major layout, spacing, typography, or color mismatch against the reference.

Constraints:
- Do not inline the reference image as a shortcut.
- Do not spend time reproducing decorative illustrations exactly unless they are part of the product requirement.
```

## When The Goal Is Not Ready

If the user's request is too ambiguous, ask one question that unlocks verifiability. Good questions are specific:

- "What metric should count as success: build time, deploy time, runtime latency, or all three?"
- "Which environment counts as proof: local, staging, deploy preview, or production-like?"
- "Is generated test data acceptable, or must the agent use the real dataset?"

After the user answers, draft the goal.

## Prompt Review Checklist

Before returning the final prompt, verify:

- The outcome is concrete enough for an agent to stop.
- At least one completion criterion is externally checkable.
- The prompt includes enough starting context to avoid wasting time.
- The measurement method cannot be gamed by weakening quality.
- The environment is realistic for the work.
- Long-running work has a tracking artifact or checkpoint strategy.
- The final instruction includes cleanup and final evidence.

## Output Format

Return the optimized prompt first.

If useful, add a short note after the prompt explaining the most important tradeoff or missing assumption. Keep the explanation brief; the user usually needs a prompt they can paste into `/goal`.
