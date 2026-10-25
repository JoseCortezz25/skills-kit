# Guided learning skills

Five small skills that complement each other to learn any topic with an AI agent, from the general to the particular, going down through prerequisites and reviewing with spaced repetition. Everything lives in Markdown files, so it works with any agent that can read instructions and files.

## The skills

| Skill | What it is for |
|---|---|
| `teacher-voice` | How the agent should talk: short, human, turn by turn, no artificial chatter. It overrides the others on tone. |
| `topic-map` | The big picture: syllabus, prerequisites, diagram, starter glossary, and an initial diagnostic. |
| `prerequisite-descent` | The core. Explains briefly, detects what is missing, goes down to something known, and climbs back reconnecting. |
| `check-and-review` | Checks understanding (Feynman, predict, compare) and schedules spaced reviews. |
| `interactive-explorer` | Generates a clickable HTML with the map, progress, glossary, and reviews. |

## What your progress folder looks like

```
learning/
  review.md                  cards from all topics, with their next review date
  <topic>/
    map.md                   nodes, prerequisites, statuses, and diagram
    glossary.md              terms that showed up along the way
    session.md               navigation stack and parked topics
    explorer.html            clickable view (regenerated)
```

The files are the source of truth. You can keep them in a Git repository to get a history of your progress.

## Installation

These skills ship with [`skills-kit`](https://github.com/JoseCortezz25/skills-kit) and install with the [`skills` CLI](https://skills.sh/). Nothing to clone.

Install the whole pack:

```bash
npx skills add JoseCortezz25/skills-kit \
  --skill topic-map prerequisite-descent check-and-review teacher-voice interactive-explorer
```

`--skill` takes every name that follows it, so the five install in one pass.

Install only part of the pack — for example the tone plus the core loop:

```bash
npx skills add JoseCortezz25/skills-kit --skill teacher-voice prerequisite-descent
```

Or install everything the repository offers, learning pack included:

```bash
npx skills add JoseCortezz25/skills-kit
```

Useful flags:

| Flag | Effect |
|---|---|
| `-g` | install globally (user level) instead of into the current project |
| `-a <agent>` | target one agent, e.g. `-a claude-code` or `-a opencode`; `'*'` for all detected |
| `-y` | skip confirmation prompts |
| `--list` | show what the repository offers, without installing |

The CLI discovers skills at any depth, so the extra `skills/learning/` folder does not change the result: each skill lands flat as `<agent>/skills/<name>/`, which is the layout agents read at runtime.

### Agents the CLI does not cover

- **Claude Code:** covered — the CLI writes to `~/.claude/skills/` with `-g`, or `.claude/skills/` per project.
- **Claude on the web or in the app:** upload each folder as a skill from the skills settings.
- **Anything else:** paste each `SKILL.md` into `AGENTS.md`, or ask the agent to read the files at the start of a session.

## How the five fit together

They are not five alternatives. They run as one flow, and each one owns a phase:

| Phase | Skill that drives it | What happens |
|---|---|---|
| Every turn | `teacher-voice` | Tone: one idea per turn, human, no wall of text. It governs the other four, so it is always in play. |
| 1. Start a topic | `topic-map` | Builds the big picture, writes `map.md` and `glossary.md`, runs an initial diagnostic. |
| 2. Study a node | `prerequisite-descent` | The core loop: explain briefly → check → if it does not land, descend to a known prerequisite → climb back reconnecting. |
| 3. Close a node | `check-and-review` | Confirms understanding in your own words and writes cards into `review.md`. |
| 4. Open a session | `check-and-review` | Reads `review.md` and tells you what is due before new material. |
| 5. Look at the whole | `interactive-explorer` | Regenerates `explorer.html` from the map and the progress. |

### One session, end to end

1. **"I want to learn X."** `topic-map` creates `learning/x/` with the syllabus, the diagram, a 10-term glossary, and two or three diagnostic questions.
2. **"Let's start with Y."** `prerequisite-descent` explains one idea and asks you to restate it. If you stumble, it descends. The stack in `session.md` keeps the way back visible, capped at 4 levels, with tangents parked instead of followed.
3. **"I think I got it."** `check-and-review` does not take your word for it: it asks you to reconstruct the concept, then writes a card with its next review date.
4. **Next day: "what's due?"** `check-and-review` reads `review.md` and gives you only what expired.
5. **"Show me the map."** `interactive-explorer` regenerates `explorer.html` with statuses, glossary, and due reviews.

### What makes them work together

The five skills share state only through the Markdown files in `learning/`. No hidden memory, no lock-in:

- `map.md` — the plan and the progress. Every skill reads it; updates go here.
- `glossary.md` — terms that actually showed up, not a dictionary dump.
- `session.md` — the navigation stack, so a descent can always climb back.
- `review.md` — the schedule, shared across all topics.
- `explorer.html` — generated output, never hand-edited.

Because the state is files, you can switch agents mid-topic without losing anything, and keep the folder in Git to get a history of what you learned and when.

## Language

The skills are written in English. The agent replies in whatever language you write in, and the files it creates (map, glossary, cards) follow your language too.

## Risks the design tries to cover

- **Rabbit hole with no way back:** a visible navigation stack, a limit of 4 levels, and a parked list for tangents.
- **Not knowing where to stop:** the floor is something you already know, checked with a concrete question and not with "do you know it?".
- **Understanding without being able to use it:** each node is checked in your own words before being counted as seen.
- **Artificial chatter and content avalanches:** one idea per turn and style rules in `teacher-voice`.
- **Huge glossaries:** they start with 10 terms at most and grow only with what really shows up.

## Still to test

These skills are a first draft. They should be tried with a real topic (for example "variables and references") and adjusted for step size, review intervals, and tone, according to what feels natural.
