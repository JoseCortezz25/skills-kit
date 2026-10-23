# Step 3 — Path-scoped rules (`rules/`)

Modular rule files with `paths:` frontmatter so agents load only the rules relevant to the files they touch.

## Frontmatter contract

```yaml
---
paths:
  - "src/components/**/*.tsx"
---
```

A rule without `paths:` applies globally — use sparingly (naming language, commit conventions). Everything else is scoped.

## Standard set (adapt, do not blindly copy)

| File | Scope | Covers |
|---|---|---|
| `code-quality.md` | stack source dirs | Lint baselines, complexity limits, error handling idioms |
| `naming-conventions.md` | stack source dirs | File, symbol, and test naming per language |
| `naming-language.md` | global | Identifier language policy (e.g. English-only identifiers) |
| `folder-structure.md` | repo root | Where new files go, by kind |
| `atomic-design.md` | UI dirs only | Component levels, when each is mandatory vs optional |
| `<stack-specific-rules>.md` | stack dirs | The one file that only makes sense here (e.g. Tauri command boundaries, Prisma migration discipline) |

## Rules

- One concern per file. If a rule needs "and also…", split it.
- Each rule states the expected behavior AND the deterministic judge that enforces it (or "unenforced — relies on review" if none exists). Unenforced rules are second-class: prefer wiring a judge (step 6) over writing wishful prose.
- Delete standard files the stack does not need (no UI → no `atomic-design.md`), and record the omission.
