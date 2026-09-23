# Consolidation Guide

The consolidated guide is what the learner actually reads. It must be a connected, progressive explanation — not a stack of per-source summaries, and not a summary of the research process.

## Document skeleton

1. Title, subtitle, date, scope, assumed prior knowledge, and what the learner will be able to do at the end.
2. How to read this guide, including the prerequisite order.
3. Table of contents with links to stable anchors.
4. One chapter per subtopic, in dependency order.
5. A closing chapter: decision guide, common pitfalls recap, and where to continue.
6. Glossary (when terminology is dense).
7. Uncertainty section: unresolved contradictions and open questions.
8. Bibliography with stable numbering, derived from `research/fuentes-globales.md`.

## Chapter anatomy

Every chapter follows the same shape, adapted to the material:

1. **Opening question** — the question this chapter answers.
2. **Prerequisite recap** — one short paragraph connecting to what came before.
3. **Explanation** — the concept in plain language first, then the precise terminology.
4. **Mechanism or why** — how it works, and why it is designed that way.
5. **Worked example** — concrete, with enough context to be reproducible.
6. **Failure modes** — what goes wrong, the predictable misconceptions, and how they look in practice.
7. **Limits and alternatives** — when this is the wrong tool, and what is used instead.
8. **Evidence and disagreement** — cited claims, and any conflict stated where it appears.
9. **Bridge** — why the next chapter follows.

## Depth standards

- Depth means connected explanation with evidence, counterevidence, examples, and stated limits. Length is a consequence, not the goal.
- Practical minimum for a technical or conceptually dense topic: **1,500 words of real explanation per subtopic chapter**, and **15,000 words for a broad-topic guide**. For lighter topics, hold the explanation density and let the length follow.
- Every non-obvious claim carries a citation `[n]`. Every chapter contains at least one worked example and one failure mode.
- Explain every term at first use; then use the precise term consistently.
- Use analogies as bridges, never as proof. Mark them as analogies.
- Distinguish definition, mechanism, evidence, and recommendation in the prose.

## Prohibited patterns

- Bullet-only chapters. Lists serve comparison and scanning; they cannot carry an explanation.
- One- or two-paragraph chapters.
- "X is a library that does Y" followed by features. That is a brochure, not a lesson.
- Pasted abstracts or translated source fragments presented as explanation.
- Unexplained jargon, or jargon introduced before its prerequisites.
- Toy examples with no context, or code with no output and no reasoning.
- Unsourced statistics and unsourced performance claims.
- Silent disagreement: a contested claim presented as settled.
- Filler paragraphs that restate the heading.

## Citations and bibliography

- Sequential numeric citations `[n]`, assigned from the deduplicated ledger, stable across drafts.
- Reuse a number for a source cited several times; never create duplicate bibliography entries.
- `output/bibliografia.md` holds one entry per source: number, title, publisher or venue, date, type, URL, and access date.
- Citations support claims; they do not replace explanation. Place the citation immediately after the claim it supports.
- Only `consulted` sources may be cited. Never cite a `url-verified` or `rejected` source.

## Revision behavior

When the user asks for changes: preserve the subtopic map, the ledger, and citation IDs unless scope changed or a source was removed. Regenerate the affected chapters and their bridges, then rerun the audit. Do not patch isolated paragraphs while leaving the surrounding explanation inconsistent with them.
