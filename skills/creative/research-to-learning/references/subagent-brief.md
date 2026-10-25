# Subagent Research Brief

Template for the brief handed to each research subagent. Subagents share no context with the main conversation, so every brief must be self-contained: never reference "the topic above", earlier messages, or another subagent's output.

## Wave size

Run at most 3 subagents concurrently, or fewer if the runtime is stricter. One subtopic per subagent — never split one subtopic across two subagents, and never give one subagent two subtopics.

## Brief template

Replace every `<...>` placeholder. Keep the brief in the language of the material.

```markdown
You are researching one subtopic of a larger learning project. Work only on your assigned subtopic.

## Context
- Learning goal: <outcome the learner must reach>
- Learner: <who they are and their prior knowledge>
- Whole topic: <main topic>
- Your subtopic: <NN> - <name>
- Why this subtopic exists: <one line>
- Prerequisites already covered elsewhere: <list, so you do not re-research them>

## Key questions you must answer
1. <question>
2. <question>
3. <question>

## Where to work
- Output directory: <absolute path>/research/<NN>-<subtema>/
- Index file you must write: <same>/fuentes.md
- Source file naming: fuente-NN-<slug>.md (lowercase, hyphens, sequential)
- Read the format requirements first: <absolute path to references/source-file-format.md>

## Method
1. Search broadly first, then narrow. Cover the spectrum: primary sources and official documentation,
   academic or review material where it exists, expert technical writing, and field reports.
2. Prefer primary and first-party sources. Trace claims back to the source that owns them instead of
   citing an aggregator, and treat marketing pages and SEO summaries as context only.
3. For every source you actually consult, write one file containing the metadata header plus the
   COMPLETE extracted content, followed by the key fragments you expect to use.
   - If the extraction is truncated, page the saved file until you have the whole content.
   - Never store a truncated page and call it read. Never summarize in place of extracting.
4. Record contradictions, gaps, and doubts as you find them, in the source file and in the index.
5. Verdict each source in fuentes.md: accept, context-only, or reject, with a one-line reason.
   A source that answers none of the key questions is rejected or reported as belonging elsewhere.

## Budget and floors
- Target: at least <N> consulted sources (8 minimum, 12+ for foundational or contested subtopics).
- Do not pad. Duplicates, search-result pages, thin aggregators, and unopened links do not count.
- If the evidence for a key question is thin or missing, say so explicitly instead of filling the gap.

## Honesty rules
- Never invent a source, URL, quotation, statistic, or date. If you cannot retrieve content, say so.
- Distinguish consulted sources (content read and stored) from url-verified links (reachability only)
  and discovered links (never opened). Report the three counts separately.
- State access dates as the real date you retrieved the content.

## What to return
Return a compact manifest only - never paste raw source content back:
1. subtopic id and name, status (complete / partial / blocked);
2. file paths written, with a count;
3. counts: consulted, url-verified, discovered, rejected;
4. key questions still unanswered or thin, with the reason;
5. contradictions or conflicts found, with the competing sources;
6. off-topic material you found that belongs to another subtopic;
7. the most promising search angles for a follow-up wave.
```

## Why the manifest is strict

The parent verifies work by looking at the disk, not by trusting the return text. Count files, open an index, and spot-check one source file before marking a subtopic complete. A subagent that reports "researched thoroughly" without files on disk has produced nothing usable.

## Common failure modes to watch for

- A subagent that returns an essay in chat instead of files on disk.
- A subagent that stores summaries instead of extracted content, so nothing can be re-read later.
- A subagent that stops at the first page of results and calls the subtopic covered.
- A subagent that keeps off-topic material because it was interesting.
- A subagent that quietly drops a key question it could not answer.
