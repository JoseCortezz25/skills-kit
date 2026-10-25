# Step 6 — Deterministic judges

Machines enforce; prose advises. Wire these four, in this order, and smoke-test each.

## 1. Formatters & linters (per stack language)

Use the language-native toolchain — Prettier/ESLint for TS/JS, `rustfmt`/`clippy` for Rust, `ruff` for Python, `gofmt`/`go vet` for Go — invoked through package scripts (`format:check`, `lint`, `typecheck`) so CI, Husky, and agents run the exact same command. Templates for hook wiring in `assets/hooks/`.

## 2. Husky judges (`.husky/`)

| Hook | Enforces |
|---|---|
| `pre-commit` | Branch-name validation + `lint-staged` + secondary-language format check |
| `commit-msg` | Conventional Commits + header ≤ 100 chars + no `Co-Authored-By` + commitlint |
| `pre-push` | Branch-name validation + `typecheck` + `lint` |

Keep hooks thin: validate and delegate to scripts. A hook containing business logic cannot be tested. Templates in `assets/husky/`.

## 3. PR verifier (`scripts/verify-pr-conventions.mjs`)

One deterministic script checking the branch name, the commit header, and the PR body contract (Linked Issue, PR Type, Summary, Changes, Test Plan). It must accept a conforming PR and reject a violating one — test both. Template in `assets/scripts/`.

## 4. CI enforcement (`.github/workflows/pr-judge.yml`)

Runs the same judges on every PR so local bypasses (`--no-verify`, which the runtime hook already blocks) cannot slip through. CI and local must invoke the same scripts, never reimplemented logic. Template in `assets/github/`, PR body contract in `assets/github/PULL_REQUEST_TEMPLATE.md`.

## Rules

- One implementation per check, invoked everywhere. Duplicated logic drifts; a single script does not.
- Record what runs where: local-only, CI-only, or both — and why.
