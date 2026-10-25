# Changelog

## Unreleased
- Documented `skills` CLI installation for the `learning` pack and how its five skills run as a single workflow.
- Added the `learning` pack under `skills/learning/`: `topic-map`, `prerequisite-descent`, `check-and-review`, `teacher-voice`, and `interactive-explorer`. Guided learning from the big picture down through prerequisites, with Markdown progress files and spaced-repetition reviews.
- Reorganized skills into `skills/engineering/`, `skills/utils/`, and `skills/creative/`. Installation is unchanged: `npx skills add` still discovers every skill and installs it flat.
- Added `code-edge-cases` to identify code-grounded edge cases and candidate tests after implementation.
- Added `harness-creator` to scaffold or audit a project's AI agent harness (knowledge, rules, hooks, skills, deterministic judges) from technical research.

## 1.0.2
- Added `random-word`: lateral-thinking sessions with De Bono's random stimulus (draws an unrelated word via `scripts/draw.py`, links it to the problem through stepping-stone chains).
- Added `idea-edge-cases` to surface assumptions, open decisions, and unconsidered scenarios before implementation.
- Documented single-skill install in README (`--skill`, `--list`, `-g`/`-a`/`-y` flags).

## 1.0.1
- Added `research-to-learning`, which replaces `research-to-learning-html`: the skill decomposes a topic into subtopics, delegates each subtopic to research subagents in waves, preserves the full extracted content of every consulted source on disk, verifies relevance and authority, resolves contradictions and gaps, and consolidates a long-form Markdown guide. The HTML report became an optional rendering of that guide instead of the deliverable.

## 0.0.1
- Initial repository setup.
- Added `research-to-learning-html`, created by JoseCortezz25.
