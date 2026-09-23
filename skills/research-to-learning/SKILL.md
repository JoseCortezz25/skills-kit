---
name: research-to-learning
description: Use when the user wants to learn, understand, study, or teach a topic and expects real investigation instead of a quick summary. Runs a supervised deep-research process - decompose the topic into subtopics, delegate each subtopic to research subagents, preserve the raw content of every source on disk, verify relevance and authority, resolve contradictions and gaps, then consolidate a long-form learning guide in Markdown with an optional HTML rendering.
license: MIT
metadata:
  version: 0.1.0
  author: JoseCortezz25
  previous-name: research-to-learning-html
---

# Research to Learning

Turn a topic into deep, verifiable, reusable learning material. The output is a research corpus someone can audit plus a consolidated guide someone can actually learn from. A single pretty page with no stored evidence is a failure, not a deliverable.

## Operating contract

- Two deliverables, always: the **raw research** (auditable, complete) and the **consolidated guide** (learnable, connected). Never trade one for the other.
- **Markdown is the primary output.** HTML is an optional rendering of the same content. The existence of a nice HTML file must never shorten, gate, or replace the research.
- Never fabricate a source, quotation, statistic, date, or URL. Every factual claim in the guide must be traceable to a stored source file.
- Label evidence honestly and consistently:
  - `consulted` — the content was actually retrieved, read, and stored in `research/`;
  - `url-verified` — only reachability was checked;
  - `discovered` — seen in a search listing, citation, or index but never opened.
  Never count `discovered` or `url-verified` as research. Report the three numbers separately.
- Depth floors, as minimums not targets: **8+ `consulted` sources per subtopic** (12+ for foundational or contested subtopics) and **60+ for a broad topic**. Duplicates, search-result pages, thin aggregators, marketing pages, and unopened links do not count. If the evidence cannot reach a floor, record the shortfall and its cause in `README.md` — never pad to reach a number.
- Write the learning material in the user's language. Keep identifiers, code, URLs, and source titles in their original form.
- Preserve disagreement and uncertainty instead of smoothing it over: contradictions, outdated evidence, and unresolved claims are stated as such.

## Workspace layout

Create the structure before searching. `learning/` sits at the project root, or under `~/development/learning/` when the session has no project.

```text
learning/<tema>/
├── research/
│   ├── plan-de-subtemas.md
│   ├── 01-fundamentos/
│   │   ├── fuente-01-<slug>.md
│   │   ├── fuente-02-<slug>.md
│   │   └── fuentes.md
│   ├── 02-<subtema>/
│   ├── fuentes-globales.md          # deduplicated source ledger
│   └── verificacion-de-fuentes.md
├── output/
│   ├── guia-completa.md
│   ├── inconsistencias-y-resoluciones.md
│   ├── bibliografia.md
│   └── guia-completa.html           # optional rendering
└── README.md                        # state index: progress, counts, open questions
```

Folder and file names are lowercase with hyphens. When the material is written in another language, translate the names but keep this structure and ordering.

`README.md` is the resume point. It records the subtopic map, which wave finished which subtopic, files written, consulted counts, rejected sources, open gaps, and open questions. Update it after every wave so a long run can resume from it alone.

## Phase 1 — Frame the learning problem

1. Extract from the request: the topic, the learner (who and with what prior knowledge), the practical outcome (what they should be able to do or explain), scope, non-goals, and the desired output formats.
2. Ask **at most one** question, and only when a missing decision would materially change scope or structure (for example beginner versus practitioner level, or a specific version/ecosystem). Otherwise assume a reasonable default and record the assumption in `README.md`.
3. If the topic is too broad to teach in one pass, say so and propose the first slice.

Write the frame at the top of `README.md`.

## Phase 2 — Decompose into subtopics

Never research a topic as one undifferentiated block. Read `references/subtopic-decomposition.md` and build a subtopic map:

- 4–10 subtopics for a learning goal, ordered by dependency, not by importance.
- Every subtopic answers: why it is needed for this learning goal, which prerequisite it assumes, its key questions (3–6, answerable ones), its search angles, the evidence type it needs, and its exit criteria.
- Merge overlapping subtopics instead of keeping several keyword variants. A subtopic with no key questions is not a subtopic.
- Validate coverage explicitly against the full axis checklist in the reference and mark each unused axis `n/a` with a reason. Do not silently skip an axis.
- Add research targets that raise depth: predictable misconceptions, contested claims, and the "why" behind the design of the subject.

Write the map to `research/plan-de-subtemas.md` and mirror its summary in `README.md`.

Then present the map to the user and ask **one** question: confirm, adjust, or hand off. Do not start delegating waves until you have the answer, unless the user already authorized running to completion.

## Phase 3 — Distributed research in waves

Read `references/subagent-brief.md` before launching anything. It contains the brief template.

- Run waves of **at most 3 concurrent subagents** (or the runtime's limit, whichever is lower), one subtopic per subagent.
- Each brief is self-contained: subagents share no context with this conversation or with each other. Include the subtopic, its key questions, the exact output directory, the file format, the naming convention, the honesty rules, and the structured return manifest.
- Subagents write the raw content to disk themselves. The parent keeps a thin context and never pastes raw source text into its own reasoning.
- Verify on disk what a subagent claims: count files, open the index, spot-check one source file. A child's self-report is a claim, not a fact.
- Do not stop after one wave. Run further waves while any key question is unanswered or thin.

Every subtopic must produce, inside `research/<nn>-<subtema>/`:

1. one file per consulted source, `fuente-NN-<slug>.md`, following `references/source-file-format.md` — full extracted content, not a summary;
2. `fuentes.md` — the subtopic index with per-source verdicts.

## Phase 4 — Preserve the raw research

This is the invariant that makes the whole process auditable:

- Every consulted source becomes a file with a metadata header (source, URL, access date, subtopic, relevance assessment) plus the **complete extracted content**, key fragments, and any contradiction or gap it suggests.
- If extraction came back truncated, page the saved file until the content is complete. Never store a truncated source and call it read.
- Never overwrite another subtopic's files. Reassigned sources move, they do not duplicate.
- Maintain `research/fuentes-globales.md`: one row per deduplicated source (dedupe by canonical URL, DOI, or equivalent identifier), with type, date, subtopic, and status (`consulted` / `url-verified` / `rejected`).

## Phase 5 — Verify sources

Read `references/verification-and-contradictions.md`. Build `research/verificacion-de-fuentes.md` covering **every** source found, judged on relevance to the subtopic's key questions, authority, recency where versioned, depth and clarity, coherence with other sources, and real usefulness for the learning goal. Each row gets a verdict — `accept`, `context-only`, or `reject` — with a one-line reason.

Hard rules:

- A source must answer at least one key question of the subtopic. Otherwise it is rejected, or reassigned to the subtopic it actually serves.
- Content that belongs to another topic never enters the consolidated guide.
- Marketing copy, SEO filler, unattributed summaries, and undated opinion pieces are `context-only` at best, and must not carry a central claim.
- When only a claim's primary source counts, trace it to the source that owns it instead of citing the aggregator.

## Phase 6 — Resolve gaps and contradictions

**Gap audit.** For every key question of every subtopic, mark `covered`, `thin`, or `unanswered`. `thin` and `unanswered` questions drive a targeted second wave with sharper queries (specifications, changelogs, errata, maintainer docs, replications, review papers, benchmarks).

**Contradictions.** Never pick a side silently. For each conflict: identify it, classify the cause (different version, different context, different date, different definition, different method, or plain error), search for more authoritative evidence, then resolve it with a stated rule or mark it unresolved with the competing positions presented.

Write every conflict to `output/inconsistencias-y-resoluciones.md`: the claim, each position with its source and date, the cause classification, the deciding evidence, the resolution or the explicit `unresolved` verdict.

Loop waves until no key question is unanswered or only explicitly flagged as open with a reason.

## Phase 7 — Consolidate the guide

Read `references/consolidation-guide.md`. Write `output/guia-completa.md` as a progressive, connected, long-form guide:

- narrative order by dependency, chapter headings `h1` → `h2` → `h3`;
- each chapter opens with the question it answers and closes with a bridge to the next;
- explain mechanisms and the "why", not only the "what"; each concept gets a concrete example, a failure mode, and its limits or alternatives;
- cite sequentially as `[n]` mapped to `output/bibliografia.md`, which is generated from the deduplicated ledger with stable numbering;
- include a glossary when terminology is dense, and an explicit uncertainty section when the evidence is unsettled.

Prohibited in the final guide: bullet-only chapters, one-paragraph chapters, unexplained jargon, pasted abstracts instead of explanations, toy examples with no context, and any claim without a source. Depth comes from connected explanation, evidence, counterevidence, examples, and stated limits.

Optionally render the same content to `output/guia-completa.html` following `references/html-style-guide.md`. The rendering must not change, shorten, or add content.

## Phase 8 — Run the audit and deliver

Verify, with real tool output rather than memory:

- the number of source files on disk matches the declared `consulted` count (count them, do not trust the total);
- every consulted source has a raw file, an entry in `fuentes-globales.md`, and a row in `verificacion-de-fuentes.md`;
- every key question in `plan-de-subtemas.md` is `covered` or flagged open with a reason;
- no fabricated URL, duplicate source, placeholder section, or unsupported statistic remains;
- every `[n]` citation resolves to a bibliography entry that resolves to a stored source;
- the guide meets the depth floors and reads as connected prose;
- `README.md` reflects the final state.

Deliver: the consolidated guide (attached through the platform's file mechanism when the user is on a chat client), the workspace path, the three evidence counts (`consulted` / `url-verified` / `rejected`), coverage per subtopic, unresolved contradictions, and any question still open.

Report shortfalls plainly. "The evidence does not settle X" is a valid, useful result; an invented resolution is not.

## Anti-patterns (the failures this process exists to prevent)

- One search pass and a page of summaries.
- Counting discovered URLs as research, or counting `url-verified` links as `consulted` sources.
- Retrieving content and then discarding it instead of storing the raw text.
- Fixed subtopic lists that ignore the actual topic.
- Shallow chapters that define a term and move on.
- Keeping irrelevant or off-topic material in the consolidated guide.
- Ignoring contradictions, or resolving them by preference.
- Treating the HTML rendering as the goal.
