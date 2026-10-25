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

- **Claude Code:** copy the five folders into `~/.claude/skills/` (global) or `.claude/skills/` (per project).
- **Claude on the web or the app:** upload each folder as a skill from the skills settings.
- **Other agents:** paste the content of each `SKILL.md` into the agent's instructions (`AGENTS.md` or the equivalent), or ask it to read the files at the start of a session.

## Language

The skills are written in English. The agent replies in whatever language you write in, and the files it creates (map, glossary, cards) follow your language too.

## How to use it

1. "I want to learn X, give me the map." This creates `learning/x/` with the big picture.
2. "Let's start with Y." The descent begins. When something does not click, the agent goes down to the prerequisite and climbs back up.
3. When the stretch ends, review cards are saved.
4. In the next session the agent tells you what is due for review today.
5. "Show me the interactive map." This generates `explorer.html`.

## Risks the design tries to cover

- **Rabbit hole with no way back:** a visible navigation stack, a limit of 4 levels, and a parked list for tangents.
- **Not knowing where to stop:** the floor is something you already know, checked with a concrete question and not with "do you know it?".
- **Understanding without being able to use it:** each node is checked in your own words before being counted as seen.
- **Artificial chatter and content avalanches:** one idea per turn and style rules in `teacher-voice`.
- **Huge glossaries:** they start with 10 terms at most and grow only with what really shows up.

## Still to test

These skills are a first draft. They should be tried with a real topic (for example "variables and references") and adjusted for step size, review intervals, and tone, according to what feels natural.
