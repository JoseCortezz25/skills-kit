# Verification, Gaps, and Contradictions

Two jobs live here: deciding which sources and claims are trustworthy, and driving follow-up research when they are not.

## Verification rubric

Cover **every** source found — including the rejected ones — in `research/verificacion-de-fuentes.md`. Judge each on the six criteria below and give exactly one verdict.

| Criterio | Pregunta que responde |
|----------|----------------------|
| Relevancia directa | ¿Responde al menos una pregunta clave de su subtema? |
| Autoridad | ¿Quién lo publica y con qué respaldo: primera parte, institución, revisión, anónimo? |
| Actualidad | Para temas versionados, ¿sigue vigente, o describe una versión superada? |
| Profundidad y claridad | ¿Explica el mecanismo o repite el titular de otra fuente? |
| Coherencia | ¿Concuerda con las demás fuentes, o contradice sin explicar por qué? |
| Utilidad | ¿Aporta algo que el material final pueda usar, o solo confirma lo ya sabido? |

Verdicts:

- **accept** — serves at least one key question with authority, can carry a claim in the guide.
- **context-only** — useful background, but cannot support a central claim (marketing pages, undated posts, thin summaries, single-source claims).
- **reject** — answers no key question, off-topic, duplicative, or untrustworthy. Record the reason even when rejecting.

Hard rules:

- A source must map to at least one key question of its subtopic. Otherwise it is rejected or reassigned.
- Material belonging to another topic never enters the consolidated guide. Reassign it to the right subtopic's folder or reject it — do not keep it where it was found.
- Never let an aggregator carry a claim that has a primary owner. Trace and cite the owner.
- If a criterion cannot be evaluated (undated, unattributed), mark it `no evaluable` and treat the source as `context-only` at most.

## Gap audit

For each key question in `research/plan-de-subtemas.md`, set a state: `covered` (answered by 2+ sources, at least one primary), `thin` (answered once or only by weak sources), `unanswered`.

Every `thin` and `unanswered` question drives a **targeted follow-up wave**, not a general re-search. Aim the queries at the source type that would decide the question:

- versioned or changed behaviour → official changelogs, release notes, upgrade guides, migration docs;
- normative or definitional questions → standards, specifications, RFCs, legal text;
- "does this actually hold" questions → replications, benchmarks, errata, issue trackers;
- contested questions → review papers, maintainer statements, sustained critical writing;
- missing prerequisites → introductory texts and course material from institutions.

Stop the loop when every key question is `covered` or explicitly flagged open with a reason. Never mark a question `covered` because two weak sources agree.

## Contradiction handling

A contradiction is a research asset, not an inconvenience. Procedure:

1. **State it precisely.** Both positions, each with its source, date, and the exact claim in conflict.
2. **Classify the cause** — most conflicts are not real:
   - *version*: both are right for different releases;
   - *context*: different use case, scale, or domain;
   - *date*: one is superseded;
   - *definition*: the same word means different things in each source;
   - *method*: different measurement, dataset, or benchmark setup;
   - *error or interest*: marketing, miscitation, or plain mistake.
3. **Prefer authority over democracy.** Resolve with a stated precedence rule, not by counting sources.
4. **Search for the deciding source** when the cause is unclassified — the specification, the changelog, the maintainer, the replication.
5. **Record the outcome**, resolved or unresolved. An unresolved conflict is reported with the competing positions, the reason it stands unresolved, and what evidence would settle it.
6. **Reflect it in the guide**: state the disagreement where the claim appears, do not hide it in an appendix.

Precedence order to apply unless the topic demands otherwise: primary research or the owning specification > official first-party documentation > standards and reviews > institutionally published material > expert technical writing > community consensus > vendor or promotional material.

## Output: `output/inconsistencias-y-resoluciones.md`

```markdown
## C-01 - <short claim in conflict>

- **Afirmación en disputa**: <the claim>
- **Posición A**: <statement> — fuente S<nn> (<title>, <date>)
- **Posición B**: <statement> — fuente S<nn> (<title>, <date>)
- **Causa clasificada**: version | context | date | definition | method | error o interés
- **Evidencia decisoria**: S<nn> — <what it settles and why it outranks the others>
- **Resolución**: <the stated resolution>
- **Estado**: resuelta | no resuelta
- **Cómo se refleja en la guía**: <section where it is stated>
```

If no conflicts were found, say so explicitly, along with the contradiction check that was actually run. Claiming there were none without having compared sources is a defect.
