# Canonical harness structure

Generate this skeleton first, before filling content, so it is reviewable early.
Paths marked `->` are symlinks to the canonical location.

```text
project-root/
├── AGENTS.md                         # Concise index + context pointers (OpenCode / general agents)
├── CLAUDE.md                         # Concise index + context pointers (Claude Code)
├── RULES.md                          # Quick-reference engineering card
├── .mcp.json & opencode.json         # Project MCP servers + formatter bindings
├── .agents/skills/                   # Canonical project skills (LLM-first SKILL.md contracts)
├── .agents/hooks/                     # Canonical runtime hooks (Node stdlib only, single implementation)
│   ├── block-dangerous-commands.mjs  # PreToolUse: blocks force-push, hard-reset, --no-verify, Co-Authored-By, build artifact edits
│   └── format-and-lint.mjs           # PostToolUse: auto-formats & lint-fixes edited files
├── .claude/ & .opencode/             # Synchronized agent runtime directories
│   ├── settings.json                 # PreToolUse & PostToolUse bindings -> canonical .agents/hooks/
│   ├── knowledge/                    # Disclosed deep reference
│   │   ├── critical-constraints.md   # Non-negotiable architectural & boundary guardrails
│   │   ├── architecture-patterns.md  # Layers, dependency matrix, communication protocols
│   │   ├── file-structure.md         # Directory layout & cross-language naming table
│   │   ├── business-logic.md         # Domain entities, state transitions, invariants, open questions
│   │   └── tech-stack.md             # Stack versions, commands, and deterministic judges
│   ├── rules/                        # Path-scoped rules (`paths:` frontmatter)
│   │   ├── atomic-design.md
│   │   ├── code-quality.md
│   │   ├── naming-conventions.md
│   │   ├── naming-language.md
│   │   ├── folder-structure.md
│   │   └── <stack-specific-rules>.md
│   └── skills -> ../.agents/skills   # Symlink to canonical project skills (same pattern as hooks: runtimes link, never duplicate)
├── .husky/                           # Git deterministic judges
│   ├── pre-commit                    # Branch name validation + lint-staged + secondary language fmt check
│   ├── commit-msg                    # Conventional Commits + <=100 chars + no Co-Authored-By + commitlint
│   └── pre-push                      # Branch validation + typecheck + lint
├── scripts/
│   └── verify-pr-conventions.mjs     # Deterministic judge for branch, commit header, and PR body contract
└── .github/
    ├── PULL_REQUEST_TEMPLATE.md      # Enforced PR structure (Linked Issue, PR Type, Summary, Changes, Test Plan)
    └── workflows/pr-judge.yml        # CI enforcement of PR & code judges
```

## Adaptation rules

- Drop what the stack does not need (e.g. no `naming-language.md` for a single-language repo), but record every omission and why.
- `<stack-specific-rules>.md` is mandatory: at least one rule file that only makes sense for *this* stack. If you cannot name one, you have not inspected the stack closely enough.
- Keep `.claude/` and `.opencode/` synchronized: same knowledge, same rules, same hook bindings. Agent-specific surface goes only in `settings.json` bindings and the root entrypoint for that agent.
- Single implementation per hook in `.agents/hooks/`; runtimes only bind. Duplicated hook logic drifts exactly like duplicated judge logic (see `deterministic-judges.md`).
