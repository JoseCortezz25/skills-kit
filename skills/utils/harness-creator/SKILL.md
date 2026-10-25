---
name: harness-creator
description: Use when scaffolding or auditing a project's AI agent harness from technical research and architecture docs. Builds synchronized agent directories (.claude/ and .opencode/) with progressive disclosure across knowledge/, rules/, hooks/, and skills/, plus root entrypoints (AGENTS.md, CLAUDE.md, RULES.md), MCP config, and deterministic judges (Husky hooks, linters, PR verifier). Trigger when the user sets up agent infrastructure for a new repo, asks for agent guardrails, or wants deterministic checks wired to agent runtime hooks.
license: MIT
metadata:
  version: 0.1.0
  author: JoseCortezz25
---

# Harness Creator

Scaffold or audit a complete **Project Agent Harness** driven by a project's technical research and architecture patterns. The harness gives every agent (Claude Code, OpenCode, others) the same structured knowledge, the same path-scoped rules, and the same deterministic guardrails — tailored strictly to the target stack.

## Operating contract

- **Stack fidelity is the prime directive.** Every generated file must reflect the inspected stack of *this* repo. Never copy rules, hooks, or knowledge from another stack (e.g. Next.js conventions into a Tauri/Rust app). When in doubt, inspect; when unknowable, mark **Unspecified** and ask.
- **Two layers, always:** the **knowledge layer** (what agents need to know: `knowledge/`, `rules/`, `skills/`, entrypoints) and the **deterministic layer** (what machines enforce: Husky judges, linters, PR verifier, runtime hooks). A harness with only one layer is incomplete — say so explicitly.
- **Analyze by default; change on approval.** Auditing an existing harness reports findings first. Scaffolding writes files only within the agreed scope.
- **Canonical layout first.** Generate the structure in `references/harness-structure.md` before filling content, so the skeleton is reviewable early.

## Inputs the skill consumes

1. **Technical research / architecture docs** — research reports, ADRs, wireframes, domain specs. If none exist, run stack inspection first and note the gap.
2. **Repository stack inspection** — `package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`, lockfiles, existing linters/formatters, CI workflows.
3. **Architectural & UI conventions** — e.g. Modular Monolith, Hexagonal Ports/Adapters, Atomic Design `Atom -> Molecule -> Organism`.

## Execution steps

1. **Research & stack discovery.** Extract architecture style, trust boundaries, state ownership, and open questions from the research docs and repo manifests. See `references/stack-discovery.md`.
2. **Knowledge synthesis (`knowledge/`).** Populate the 5 core knowledge documents, tailored to the target stack. See `references/knowledge-guide.md`.
3. **Path-scoped rules (`rules/`).** Generate modular rule files with `paths:` frontmatter: code quality, naming, folder structure, UI componentization, boundary security. See `references/rules-guide.md`.
4. **Project skills (`.agents/skills/`).** Create stack-specific LLM-first skills and symlink them from `.claude/skills` and `.opencode/skills`. See `references/project-skills-guide.md`.
5. **Runtime hooks (`hooks/`).** Install Node-based `PreToolUse` / `PostToolUse` hooks with zero external binary dependencies. See `references/hooks-guide.md`. Templates in `assets/hooks/`.
6. **Deterministic judges.** Configure and smoke-test formatters, linters, typecheckers, Husky hooks, Commitlint, and the PR verifier. See `references/deterministic-judges.md`. Templates in `assets/husky/`, `assets/scripts/`, `assets/github/`.
7. **Verification gate.** Run every judge end-to-end (format check, lint, typecheck, negative hook tests) before completing. Nothing ships red.

Root entrypoints (`AGENTS.md`, `CLAUDE.md`, `RULES.md`) and MCP config (`.mcp.json`, `opencode.json`) are generated alongside steps 2–4. Template in `assets/AGENTS.md`.

## Verification gate (all must pass)

- `format:check`, `lint`, and `typecheck` (or stack equivalents) run green.
- Negative hook tests: a blocked command is actually blocked; a dirty file is actually reformatted.
- Husky `pre-commit`, `commit-msg`, `pre-push` execute without errors.
- The PR verifier accepts a conforming PR and rejects a violating one.
- Record which checks ran and which were skipped (with reason).

## Output contract

Summarize the harness in three parts: (1) what was scaffolded or audited, file by file; (2) the verification gate results, check by check; (3) open questions marked **Unspecified** that need a human decision. If auditing, prioritize findings by risk and distinguish observed gaps from inferred risks.

## What to avoid

- Copy-pasting stack rules, hooks, or knowledge from an unrelated project.
- Shelling out to binaries not guaranteed on the host (e.g. `jq`) inside runtime hooks — use Node stdlib.
- Claiming a check ran unless it was actually executed.
- Generating the whole harness in one shot without a reviewable skeleton first.
