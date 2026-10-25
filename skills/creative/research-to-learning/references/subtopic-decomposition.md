# Subtopic Decomposition

Read this before proposing the subtopic map. The map decides the quality of everything downstream: a bad decomposition produces a shallow guide no amount of research can fix.

## Rules

- Propose **4–10 subtopics** for a learning goal. Fewer means the topic was not decomposed; more means the map is a keyword list, not a plan.
- Order subtopics by **dependency**, not by importance. A learner cannot understand lifetimes before ownership.
- Each subtopic carries: id, name, why it is required for this learning goal, prerequisites, 3–6 key questions, search angles, expected evidence type, exit criteria, expected source count.
- **Key questions must be answerable.** "What is Rust?" is not a key question. "Why does the borrow checker reject a mutable borrow while an immutable one is alive, and what is the underlying aliasing rule?" is.
- All key questions across the map must be answerable from covered subtopics. If a question has no home, add a subtopic or split one.
- Merge overlaps. `syntax`, `basic syntax`, and `types` are one subtopic.
- Never reuse a canned list. Derive the map from the topic and the learner's stated outcome, then justify each entry in one line.

## Coverage axis checklist

Validate the proposed map against every axis below. For each axis, mark it `covered by <subtopic>` or `n/a` **with a reason**. Silently skipping an axis is a defect.

1. **Fundamentals and definitions** — the precise vocabulary and the mental model.
2. **Problem and context** — the problem it solves, its origin, how it evolved.
3. **Internal mechanism** — how it works under the hood, not just its interface.
4. **Prerequisites** — the concepts a learner must already hold, named explicitly.
5. **Use cases** — where it fits, where it does not.
6. **Ecosystem, tools, versions** — the surrounding tooling and what changes between versions.
7. **Tradeoffs, limitations, alternatives** — costs, failure domains, and what people use instead.
8. **Best practices** — idiomatic use and the reasoning behind the idioms.
9. **Common errors and failure modes** — including predictable misconceptions.
10. **Practical examples and worked cases** — enough to make the mechanism concrete.
11. **Contested claims** — where experts disagree or the evidence is unsettled.
12. **Further study** — the frontier, open problems, and the resources worth continuing with.

Adapt the axes to the domain. For non-technical topics, the equivalent axes are chronology, actors and interests, debates and their evidence quality, practical application, regulation and ethics, and common misconceptions.

## Depth-raising targets

Always consider adding these, because they separate a deep guide from a summary:

- **Predictable misconceptions** — what learners reliably get wrong, and why the wrong model is attractive.
- **The "why" of the design** — why it is built this way and what constraint forced the choice.
- **Decision boundaries** — when to use this versus the alternative, with criteria rather than opinions.
- **Historical inflection points** — the version or event that changed the recommended practice.

## Record format

Write the map to `research/plan-de-subtemas.md` using this shape per subtopic:

```markdown
## 03 - Ownership and borrowing

- **Why**: Without this, every later chapter about async, threads, or lifetimes reads as magic.
- **Prerequisites**: 02 (types and memory layout).
- **Key questions**:
  1. What rule does the borrow checker enforce, and at what point does a borrow end?
  2. Why is one mutable borrow exclusive while many immutable borrows coexist?
  3. How does a lifetime annotation differ from a reference's actual validity?
  4. What problem does ownership solve that a garbage collector solves differently?
- **Search angles**: official book chapters, RFCs, compiler error documentation, performance papers.
- **Evidence type**: first-party docs and specifications, then expert technical writing, then benchmarks.
- **Exit criteria**: each key question answered with at least two independent sources, one of them primary.
- **Expected sources**: 12+ consulted, 3 rejected.
```

End the file with the axis validation table and a one-line note on what is explicitly out of scope for this pass.

## Anti-patterns

- Subtopics that are keyword variants of each other.
- Skipping the prerequisites axis, then writing a guide that assumes knowledge the learner does not have.
- Ordering by what is easy to search rather than by what must be understood first.
- A map with no contested claims and no misconceptions — that map will produce a brochure.
