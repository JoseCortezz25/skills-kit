# Step 5 — Runtime hooks (`hooks/`)

Node.js `PreToolUse` / `PostToolUse` hooks with **zero external binary dependencies** — Node stdlib only. Hooks run on contributor machines you do not control; assuming `jq`, `rg`, or GNU coreutils is how harnesses break on arrival.

## The two hooks

1. **`block-dangerous-commands.mjs` (`PreToolUse`)** — Deny-list guard. Blocks force-push, hard reset, `--no-verify` / `--no-guard` bypasses, `Co-Authored-By` / AI attribution trailers, and edits to build artifacts (`dist/`, `build/`, lockfiles by hand). Fail closed: on error, block and explain. Template in `assets/hooks/`.
2. **`format-and-lint.mjs` (`PostToolUse`)** — Auto-formats and lint-fixes edited files using the repo's own toolchain (Prettier/ESLint, `rustfmt`/`clippy`, `gofmt`, `ruff`…). Only touches files the agent edited, only with tools declared in `tech-stack.md`. Template in `assets/hooks/`.

## Binding (per agent, in `settings.json`)

Both `.claude/settings.json` and `.opencode/` config bind the same two hooks from the canonical `.agents/hooks/` location — never a per-runtime copy. Agent-specific surface stays in the binding; hook logic stays shared. Template in `assets/settings.json`.

## Rules

- Hooks must be fast (< a few seconds) and silent on success. A slow or chatty hook gets disabled — and a disabled hook is worse than none, because the harness claims protection it lacks.
- Every block message tells the agent what to do instead, not just what was forbidden.
- Smoke-test both directions: a forbidden command is actually blocked (negative test), and a normal edit flows through untouched.
