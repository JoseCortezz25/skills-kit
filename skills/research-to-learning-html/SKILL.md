---
name: research-to-learning-html
version: 0.0.1
author: JoseCortezz25
description: Research a topic deeply and turn the findings into a self-contained, book-like educational HTML document. Use whenever the user asks to learn, explain, teach, study, document, or build a cookbook/guide about a topic and expects grounded research, many sources, chapters, diagrams, a table of contents, glossary, and IEEE-style linked citations. Prefer this skill over a generic HTML or summary workflow when the deliverable is an educational web book based on investigation.
---

# Research to Learning HTML

Turn a research question into a coherent learning experience, not a pile of notes. The output is a polished, self-contained HTML book whose chapters build on one another and whose claims can be traced to sources.

## Operating contract

- Produce every report as a single HTML file. Supporting notes, tables, or intermediate artifacts may be created during research, but the final report is always HTML.
- Write the learning content in the user's language; keep technical identifiers, URLs, and source titles in their original form when useful.
- Aim for **at least 100 relevant sources** for a broad topic. Count sources only when they materially support the subject. Never pad the bibliography with duplicates, search-result pages, weak aggregators, or sources that were not consulted.
- If the topic is genuinely narrow or the available evidence cannot support 100 sources, state the shortfall in a research note inside the artifact and explain the selection criterion. Never invent sources or citations to reach the number.
- Separate evidence from interpretation, analogy, and recommendation. Mark uncertainty, disagreement, outdated evidence, and unsupported claims.
- Do not silently turn a source's speculation, marketing copy, or opinion into fact.

## Workflow

### 1. Frame the learning problem

Before searching, define:

- target learner and assumed prior knowledge;
- the central question and the practical outcome the learner should reach;
- scope, time period, geography, and disciplines;
- explicit non-goals;
- a provisional chapter sequence from foundations to application.

If one missing decision would substantially change the research or structure, ask one focused question. Otherwise make a reasonable assumption and disclose it in the HTML.

### 2. Build a source strategy

Research in passes so the source list has coverage rather than repetition:

1. **Orientation:** authoritative overviews, standards, textbooks, review papers, institutional explainers.
2. **Foundations:** primary studies, original papers, official specifications, legislation, datasets, source code, or first-party documentation.
3. **Mechanisms and debates:** competing models, limitations, replications, critiques, negative results, and meaningful minority positions.
4. **Practice:** worked examples, case studies, benchmarks, field reports, and implementation guidance.
5. **Freshness check:** recent authoritative material and changes since the oldest important source.

Prefer sources in this order when they exist: primary research or original data; standards and official documentation; academic reviews and books; reputable institutions; expert technical writing. Use secondary sources to discover material, then trace important claims to the source that owns them.

Maintain a source ledger while researching. For every source record its stable URL or identifier, title, publisher/venue, publication date, source type, relevant chapter, claims supported, limitations, and access date when appropriate. Deduplicate by DOI, canonical URL, or equivalent identifier.

### 3. Create an evidence map before writing

Create a private claim matrix with at least these columns:

`claim | importance | source IDs | evidence type | confidence | caveat | chapter`

Use it to detect unsupported claims, citation gaps, contradictory findings, and chapters that are over-dependent on one source. A central claim should have direct evidence or be explicitly presented as synthesis. When sources disagree, explain what differs: population, method, definition, timeframe, or assumptions.

Do not start prose until each planned chapter has a purpose, prerequisite concepts, key claims, examples, and transitions to the next chapter.

### 4. Write the book-shaped explanation

Use a narrative progression such as:

1. orientation and why the topic matters;
2. vocabulary and mental model;
3. foundations and historical/contextual origin;
4. mechanisms or systems;
5. concrete examples and worked cases;
6. tradeoffs, limits, failure modes, and competing views;
7. application, practice, or decision guide;
8. synthesis and next steps;
9. glossary;
10. sources and research note.

Adapt the sequence to the topic, but preserve dependency order. Open each chapter with the question it answers and close it with a short bridge explaining why the next chapter follows. Use paragraphs to connect ideas; use lists and tables only when they improve scanning or comparison.

Explain technical terms at first use in plain language, then use the precise term consistently. Use analogy as a bridge, not as proof. Include small examples before abstractions when that reduces cognitive load. Distinguish definitions, mechanisms, evidence, and recommendations in the prose.

### 5. Design the HTML artifact

Read [`references/html-style-guide.md`](references/html-style-guide.md) before creating the document. It defines the required visual direction: light mode by default, monochrome presentation, no borders or cards, restrained typography, generous whitespace, and offline-friendly responsive layout.

Create one semantic, self-contained HTML document with:

- a clear title, subtitle, research date, scope, assumptions, and reading-time estimate;
- a navigable table of contents linking to stable section IDs;
- chapter headings in a valid `h1` → `h2` → `h3` hierarchy;
- readable line length, generous spacing, responsive layout, and print-friendly styles;
- a small visual system that feels like a calm digital book rather than a dashboard;
- diagrams or graphs in inline SVG when they clarify a mechanism, timeline, taxonomy, process, or comparison;
- text alternatives or captions for every diagram, and accessible labels for interactive elements;
- glossary entries linked from first meaningful use when practical;
- a final Sources section with one numbered entry per cited source;
- a research note describing source count, selection method, date range, limitations, and unresolved uncertainty.

Use CSS variables and include optional dark mode with a theme toggle and local persistence. **Light mode must be the default**, regardless of the operating system preference; only an explicitly saved dark-mode choice may activate dark mode before paint. Keep the file runnable offline: inline CSS, JavaScript, SVG, and essential assets. Avoid external runtime dependencies unless the user explicitly requests them.

Do not make decorative charts that imply precision without data. Label axes, units, dates, denominators, and uncertainty. If a visual is conceptual rather than empirical, label it as a model or diagram.

### 6. Apply IEEE-style linked citations

Use sequential numeric citations in square brackets, for example `[1]`, `[2, 5]`, and `[7–9]` when a range is genuinely appropriate. Each citation must link to the matching source entry at the end of the document, and each source entry must provide a stable anchor that links back to the citing locations when practical.

Use a consistent structure such as:

```html
<a class="citation" href="#source-12" id="cite-12-1" aria-label="Source 12">[12]</a>

<li id="source-12">
  ...bibliographic entry...
  <a href="#cite-12-1" aria-label="Back to citation">↩</a>
</li>
```

When the same source is cited more than once, reuse its number and add additional back-links rather than creating duplicate bibliography entries. Keep citation numbers stable while drafting by assigning them from the deduplicated source ledger, not by guessing while writing.

Citations support claims; they do not replace explanation. Place them immediately after the claim, statistic, definition, or borrowed idea they support. Cite figures and tables in their caption or nearby text. Cite direct quotations with a locator such as page, section, timestamp, or paragraph when available.

### 7. Run a coherence and integrity audit

Before delivering, verify all of the following:

- every table-of-contents link resolves;
- every in-text citation points to an existing source anchor;
- every cited source appears once in the Sources section;
- every source entry that promises a return link has a matching citation anchor;
- the reported source count equals the number of deduplicated source records, not the number of URLs merely discovered;
- distinguish **read/consulted sources** from a URL corpus checked for availability; do not call a source consulted unless its content was actually reviewed;
- every important factual claim has evidence or an explicit uncertainty label;
- source numbering is sequential and consistent;
- chapter transitions do not introduce unexplained prerequisites;
- terminology is consistent across chapters and glossary;
- diagrams match the surrounding explanation and include accessible text;
- no placeholder text, fabricated URL, duplicate source, or unsupported statistic remains;
- the HTML opens offline and has no broken internal links;
- the document works on narrow screens and in optional dark mode, while opening in light mode by default;
- the visual style follows `references/html-style-guide.md`: monochrome, minimal, borderless, and free of card-based UI.

For a large bibliography, validate mechanically before visual review: parse the HTML, collect all `id` values, check every internal `href`, count citation anchors and source anchors, and confirm that every source backlink resolves. Separately check external source URLs with HTTP requests, then label the result accurately (for example, “URL verified” versus “content reviewed”). If tools are available, inspect the generated file in a browser and report the validation result briefly alongside the artifact.

## Output contract

Deliver:

1. the final HTML file;
2. a concise research summary stating source count, date range, major evidence limits, and any unresolved disagreements;
3. a short validation report covering internal links, citations, offline loading, responsive layout, and dark mode.

When the user is interacting from a phone or chat client, attach the generated HTML as a downloadable file using the platform's native file/media attachment mechanism instead of only returning a local filesystem path. Keep the local path in the report for reproducibility, but optimize the immediate delivery for the user's device.

If the user asks for revisions, preserve the evidence map and citation IDs unless a source is removed or the research scope changes. Regenerate affected transitions and rerun the audit rather than patching isolated paragraphs blindly.

## Quality bar

A successful result feels like a carefully edited introductory book: a learner can follow it from first principles to informed application, a skeptical reader can inspect the evidence, and the HTML remains useful without network access. Depth comes from connected claims, primary evidence, counterevidence, examples, and explicit limits—not from length alone.
