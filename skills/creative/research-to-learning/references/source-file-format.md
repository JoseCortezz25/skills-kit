# Source File and Ledger Formats

Every consulted source is stored twice: once as its own file with the full content, and once as a row in the ledgers. Formats are fixed so the corpus stays auditable and machine-checkable.

## One source, one file

Path: `research/<NN>-<subtema>/fuente-NN-<slug>.md` — lowercase, hyphens, sequential numbering, slug from the source title or host.

```markdown
# <Source title>

- **URL**: <canonical URL>
- **Tipo de fuente**: primary research | official documentation | standard/specification | book/review | institutional | vendor page | technical article | forum/community | media
- **Autor o entidad**: <who publishes it>
- **Fecha de publicación**: <date or "undated">
- **Fecha de consulta**: <real retrieval date>
- **Subtema**: <NN> - <name>
- **Relevancia**: alta | media | baja - <which key question(s) it serves>
- **Estado**: consulted | url-verified

## Contenido extraído

<Complete extracted content, in the source's language, in order. If the extraction was truncated,
page the saved file until the whole consulted portion is present. Do not summarize here.>

## Fragmentos clave

> "<verbatim fragment>" — (sección/página/timestamp)

> "<verbatim fragment>"

## Notas

- <what this source adds that others do not>
- <where it conflicts with another source, with the other source named>
- <what it leaves unanswered>
- <any claim that looks promotional or unsupported>
```

If a source is long, keep the extraction complete for the parts relevant to the key questions and mark the omitted ranges explicitly (`## Contenido extraído — secciones 5-9 omitidas (no relevantes: material de marketing)`). Silent truncation is the defect this format exists to prevent.

## Subtopic index: `fuentes.md`

```markdown
# Fuentes - <NN> <Subtema>

| # | Fuente | Tipo | Fecha | Estado | Relevancia | Archivo |
|---|--------|------|-------|--------|------------|---------|
| 1 | <title> | official documentation | 2024-03 | consulted | alta | fuente-01-<slug>.md |
| 2 | <title> | vendor page | undated | url-verified | baja | - |
| 3 | <title> | competitor blog | 2023-11 | rejected | baja | - |

Contradicciones detectadas: <summary, or "ninguna">
Preguntas sin responder: <list, or "ninguna">
```

The index is the subtopic's truth. If a file exists but is not in the index, the subtopic is inconsistent — fix it before the verification phase.

## Global ledger: `research/fuentes-globales.md`

One row per **deduplicated** source across all subtopics. Dedupe by canonical URL, DOI, ISBN, or equivalent identifier — the same document reached through two paths is one source.

```markdown
# Fuentes globales

| ID | Fuente | URL/identificador | Tipo | Fecha | Subtemas | Estado |
|----|--------|-------------------|------|-------|----------|--------|
| S01 | <title> | <url or doi> | specification | 2021 | 03, 07 | consulted |
| S02 | <title> | <url> | vendor page | undated | 05 | rejected |
```

Rules:

- IDs are stable and sequential (`S01`, `S02`, …). The bibliography numbering in `output/bibliografia.md` is derived from this ledger, never guessed while writing.
- A source used by two subtopics appears once, with both subtopics listed.
- `Estado` is one of `consulted`, `url-verified`, `rejected`. Only `consulted` sources may carry a claim in the consolidated guide.
- When a source is rejected after verification, keep the row and set the status — do not delete it. Rejections are evidence of the process.
