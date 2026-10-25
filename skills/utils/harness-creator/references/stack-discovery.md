# Step 1 — Research & stack discovery

Goal: extract architecture style, trust boundaries, state ownership, and open questions *before* writing any harness file.

## What to read, in order

1. **Provided research docs first** (research reports, ADRs, wireframes, domain specs). They define intent: architecture style, module boundaries, invariants.
2. **Repo manifests second** (`package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`, lockfiles). They define reality: actual stack versions, scripts, dependencies.
3. **Existing automation third** (CI workflows, Husky hooks, linters, formatters). They define what is already enforced — reuse, do not duplicate.

## What to extract

| Question | Where to look | If unanswerable |
|---|---|---|
| Architecture style (monolith, modular monolith, hexagonal…)? | Research docs / ADRs | Mark **Unspecified**, propose the simplest fitting style |
| Trust boundaries (auth, payments, external I/O)? | Research docs, API routes | Mark **Unspecified**, list candidate boundaries as questions |
| State ownership (who writes what)? | Research docs, store/service layout | Mark **Unspecified** |
| Stack versions and commands? | Manifests, lockfiles | Inspect deeper (`--version` runs); never guess |
| UI conventions (Atomic Design…)? | Wireframes, component tree | Default to the repo's existing component shape |

## Output of this step

A short discovery note (kept in the session, or as `knowledge/` drafts) listing: confirmed facts with sources, and open questions marked **Unspecified**. Steps 2–4 build directly on it. If there are no research docs at all, say so and build from manifests alone — but flag the harness as **stack-derived, intent-unverified**.
