---
name: code-edge-cases
description: "Trigger: implementation edge cases, code-grounded analysis, candidate tests. Find and prioritize plausible failure scenarios in an existing or partially implemented feature."
license: Apache-2.0
metadata:
  author: "JoseCortezz25"
  version: "1.0.0"
---

## Activation Contract
Use this skill when a user asks what could fail in implemented behavior or wants candidate tests grounded in code. Analyze by default; do not change code.

## Hard Rules
- Ground each finding in inspected implementation, tests, or documentation; cite paths and symbols or test names.
- Distinguish observed behavior from inferred risk. Expected behavior comes only from explicit requirements; mark it **Unspecified** otherwise.
- Do not claim a test ran unless it was actually executed.
- Keep findings focused; combine duplicates and avoid theoretical noise.

## Decision Gates
| Situation | Action |
|---|---|
| Relevant code and requirements are available | Compare observed behavior with documented expectations |
| Expected behavior is not established | Mark it **Unspecified** and frame a product question |
| User requests a code change | Report findings first; wait for implementation scope |

## Execution Steps
1. Establish the feature boundary; inspect relevant implementation, tests, and documentation.
2. Check applicable input boundaries, state transitions, authorization, concurrency, persistence, external failures, performance, security, and recovery.
3. For each candidate, record the trigger, current behavior, documented expectation or **Unspecified**, evidence, impact, and a concrete test shape.
4. Prioritize by plausible impact and likelihood; state which files/tests were inspected and which tests actually ran.

## Output Contract
Summarize the main risk areas, then provide a prioritized Markdown table with `Priority`, `Scenario / trigger`, `Observed vs expected / unspecified`, `Evidence`, `Likely impact`, and `Coverage / test suggestion`. Clearly distinguish proposed tests from executed tests.

## References
None.
