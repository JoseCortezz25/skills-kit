# AGENTS.md — agent entrypoint (template)

> Adapt the pointers below to this repo. This file is an index, not a manual:
> it points at knowledge; it never duplicates it.

## Stack

<one line: language(s), framework(s), package manager — from `knowledge/tech-stack.md`>

## Read first (progressive disclosure)

1. `knowledge/critical-constraints.md` — non-negotiable guardrails. Read before any change.
2. `knowledge/architecture-patterns.md` — layers and dependency rules.
3. `knowledge/file-structure.md` — where files go, cross-language naming.
4. `knowledge/business-logic.md` — domain entities, invariants, open questions.
5. `knowledge/tech-stack.md` — versions and canonical commands.

`rules/` apply by path (`paths:` frontmatter). `.agents/skills/` holds multi-step
guides — check the skill index before improvising a workflow.

## Canonical commands

```bash
<dev> | <build> | <test> | <lint> | <typecheck> | <format:check>
```

## Hard rules

- Never bypass deterministic judges (`--no-verify`, `--no-guard`, force-push, hard reset).
- No AI attribution trailers (`Co-Authored-By`) in commits.
- Conventional Commits, header ≤ 100 chars.
- Claim a check ran only if it actually executed.
