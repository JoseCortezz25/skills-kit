---
name: interactive-explorer
description: Generates a clickable HTML page with a topic's map, where each node expands, shows its summary, status, and prerequisites, and lets the learner ask the agent to go deeper. Use it when the learner asks to see the map, an interactive diagram, a navigable overview, or their learning progress.
license: MIT
metadata:
  version: 0.1.0
  author: JoseCortezz25
---

# Interactive explorer

Turns `learning/<topic>/map.md` into a single HTML page to walk through the topic by clicking. It answers three questions: where am I, what is around me, and what do I need to get where I want. Speak following the `teacher-voice` skill.

## Inputs

- `learning/<topic>/map.md` (nodes with `id`, `name`, `summary`, `status`, `requires`).
- `learning/<topic>/glossary.md` (terms and definitions).
- `learning/<topic>/session.md` (the current stack, to mark "you are here").
- `learning/review.md` (due cards, only to show the count and the list).

If `map.md` is missing, build the map first with the `topic-map` skill.

## Output

A single file `learning/<topic>/explorer.html`, self-contained (HTML, CSS, and JavaScript in the same file, with the map data embedded as JSON). No build step and no libraries. Loading typefaces from Google Fonts is allowed, with a fallback stack in case there is no connection.

Where to deliver it:
- In Claude (claude.ai), publish it as an artifact.
- In a coding agent (Claude Code or another), write it in the topic folder and tell the learner to open it in a browser.

## What the page must do

1. **Map view.** The whole topic with the pillars visible. Clicking a node expands it and shows its children, summary, status, and prerequisites (also clickable). Prerequisites appear as a path leading backward.
2. **"You are here".** Highlights the nodes in the stack from `session.md` and shows the path in one line (for example: References, RAM).
3. **Statuses visible without relying on color.** Each status has a symbol and a text label in addition to color: ○ todo, ◐ in progress, ✓ known, ● understood, ★ mastered.
4. **"Go deeper with my agent" button.** On each node it builds a text such as "I want to go deeper on «<name>» in the topic <topic>. Use prerequisite-descent." If `window.sendPrompt` exists, it sends it. Otherwise it copies the text to the clipboard and shows a brief notice. Write the interface texts and this prompt in the learner's language.
5. **Glossary in context.** Glossary terms that appear in the summaries are underlined, and clicking one shows its definition in a panel or bubble. There is no need to leave the page.
6. **Review panel.** How many cards are due today and which ones (read-only).
7. **Local progress.** Status changes made on the page are saved in `localStorage` (wrapped in try/catch, because it may be unavailable) and can be exported with a "Copy progress" button (a YAML block ready to paste into `map.md`). The page cannot write the files by itself, so **the files in the folder are the source of truth** and the page is regenerated after each session.
8. **Basic accessibility.** Keyboard navigation (Tab, Enter, Escape), proper ARIA roles on expandable nodes, enough contrast, and respect for `prefers-reduced-motion`.
9. **Small screens.** It must work on a phone, with no horizontal scroll.

## Design

This page gets looked at many times, so design matters, although clarity comes first. Apply these guidelines:

- **Typography with character.** Pick a distinctive font pairing (one for titles, one comfortable for reading). Avoid Arial, Roboto, Inter, and system fonts, and avoid repeating the same choice from one topic to the next (Space Grotesk included).
- **Cohesive palette.** Define colors as CSS variables. A dominant color with sharp accents works better than a timid palette spread evenly. Avoid the purple gradient on a white background.
- **One aesthetic per topic.** Alternate between light and dark and between different styles (for example field notebook, engineering blueprint, old map, terminal), depending on the topic or the learner's taste. Ask if they have a preference.
- **Background with atmosphere.** Layered gradients, geometric patterns, or subtle textures instead of a flat color, without hurting text legibility.
- **Motion with intent.** One well-orchestrated entrance (staggered reveal with `animation-delay`) is worth more than many scattered micro-animations. CSS only when possible.
- **Diagrams.** They should show the real structure of the topic (dependencies and hierarchy). Avoid decorative boxes that say nothing.

## Steps

1. Read the input files and validate that every `requires` points to an existing node. If there are broken references, fix them in `map.md` or flag them.
2. Embed the data as a JSON object inside the page.
3. Write the file and open or publish it.
4. Reply with one or two sentences: what the page is and how to ask for the next step ("Click a node and use Go deeper to continue here in the chat").

## After each session

Regenerate `explorer.html` with the updated statuses. If the learner used "Copy progress" and pasted the block, merge it into `map.md` first and then regenerate.
