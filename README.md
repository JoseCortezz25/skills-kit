# skills-kit

My personal skills kit: a curated set of skills I use in my day-to-day workflow and have created or adapted for myself.

## Install

Install everything:

```bash
npx skills add JoseCortezz25/skills-kit
```

Install a single skill (example with `random-word`):

```bash
npx skills add JoseCortezz25/skills-kit --skill random-word
```

List what's available without installing:

```bash
npx skills add JoseCortezz25/skills-kit --list
```

Useful flags:

- `-g` installs globally instead of per-project
- `-a <agent>` picks the target agent (e.g. `-a claude-code`), `'*'` for all
- `-y` skips confirmation prompts

More info: https://skills.sh/

## Repository layout

Skills are grouped by purpose under `skills/<category>/<skill-name>/SKILL.md`:

```
skills/
├── engineering/   # writing and reviewing code
├── utils/         # agent workflow and tooling
├── creative/      # ideation and research
└── learning/      # studying a topic with an agent
```

Categories are organizational only. `npx skills add` discovers skills at any depth under `skills/` and installs each one flat as `<agent>/skills/<skill-name>/`, which is the layout agents load.

## Available skills

### Engineering

- **atomic-design** — guide for creating, splitting, and refactoring UI components using Atomic Design.
- **code-edge-cases** — analyzes existing code for grounded edge cases and candidate tests, with a prioritized scenario table.
- **commit-conventions** — helps write and enforce proper Git commit messages.
- **forms** — React Hook Form + Zod patterns for building and validating forms.
- **nextjs-project-setup** — best practices for starting a new Next.js project.
- **react-19** — React 19 patterns, especially around the React Compiler and memoization.
- **tailwind-4** — Tailwind CSS 4 styling patterns and best practices.
- **typescript** — TypeScript strict patterns, types, interfaces, and generics.
- **zod-4** — Zod 4 schema validation patterns.
- **zustand** — Zustand state management patterns and best practices.

### Utils

- **goal-prompting** — turns vague requests into strong /goal prompts for coding agents.
- **harness-creator** — scaffolds or audits a project's AI agent harness from technical research: synchronized agent dirs, path-scoped rules, runtime hooks, and deterministic judges.

### Creative

- **idea-edge-cases** — surfaces missing decisions and failure scenarios in unimplemented feature ideas, with a prioritized gap table.
- **random-word** — runs a lateral-thinking session with De Bono's random stimulus: draws an unrelated word and links it to the problem through stepping-stone chains.
- **research-to-learning** — turns a topic into deep, verifiable learning material: decomposes it into subtopics, delegates research to subagents, preserves the raw content of every source on disk, verifies relevance and authority, resolves contradictions and gaps, then consolidates a long-form Markdown guide with an optional HTML rendering. Created by JoseCortezz25, version 0.1.0.

### Learning

A pack of skills that work together to study any topic with an agent, from the big picture down through prerequisites, keeping progress in Markdown files. See [skills/learning/README.md](skills/learning/README.md).

- **check-and-review** — checks real understanding and schedules spaced-repetition reviews.
- **interactive-explorer** — generates a clickable HTML map with progress, glossary, and due reviews.
- **prerequisite-descent** — explains briefly, finds the missing prerequisite, goes down to something already known, and climbs back reconnecting.
- **teacher-voice** — how to talk while teaching: short, human, one idea per turn.
- **topic-map** — builds the big picture of a topic: syllabus, prerequisites, diagram, and starter glossary.
