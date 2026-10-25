# Step 2 — Knowledge synthesis (`knowledge/`)

Five documents, no more, no fewer. Each answers one question an agent will otherwise guess at.

## The five documents

1. **`critical-constraints.md`** — Non-negotiable guardrails. What must an agent NEVER do here? (e.g. "never bypass the ports/adapters boundary", "never commit migrations without a down script"). Each constraint states the rule, the reason, and what breaks if violated.
2. **`architecture-patterns.md`** — Layers, dependency matrix (who may import whom), and communication protocols between modules. Include a small diagram or table; prose alone rots.
3. **`file-structure.md`** — Directory layout plus the cross-language naming table (e.g. Rust `snake_case` <-> TypeScript `camelCase` for shared Tauri commands). An agent working across languages needs the mapping written down.
4. **`business-logic.md`** — Domain entities, state transitions, invariants, and open questions. State what is known; mark the rest **Unspecified** instead of inventing domain rules.
5. **`tech-stack.md`** — Stack versions (pinned, from lockfiles), canonical commands (`dev`, `build`, `test`, `lint`, `typecheck`, `format:check`), and which deterministic judges enforce what.

## Rules

- Every claim cites its source: a research doc, a manifest, or an inspected file. Unsourced claims are marked **Unspecified**.
- Keep each document scannable: tables and bullets over paragraphs. These files are read by agents under context pressure, not by humans over coffee.
- Root entrypoints (`AGENTS.md`, `CLAUDE.md`) only *point* here — they never duplicate content. Duplication drifts; pointers do not.
