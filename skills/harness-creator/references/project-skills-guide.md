# Step 4 — Project skills (`.agents/skills/`)

Stack-specific LLM-first skills live in one canonical place and are linked into every agent runtime.

## Layout

```text
.agents/skills/<skill-name>/SKILL.md   # canonical contract
.claude/skills  -> ../.agents/skills   # symlink
.opencode/skills -> ../.agents/skills  # symlink
```

## Skill contract (SKILL.md)

- Frontmatter: `name`, one-paragraph `description` with triggers, `license`, `metadata` (`version`, `author`).
- Body: operating contract (hard rules first), execution steps, output contract, what-to-avoid list.
- References in `references/`, runnable helpers in `scripts/`, static templates in `assets/`. Progressive disclosure: SKILL.md alone must be enough to decide *whether* to read deeper.

## Which skills to create

Derive them from the discovery note (step 1), not from a fixed list. Typical candidates: the stack's testing idiom, the UI componentization pattern, the migration discipline, the PR/commit conventions. Two to four focused skills beat one mega-skill.

## Rules

- Never symlink in the other direction, and never duplicate a skill per agent. One canonical copy, links everywhere.
- A project skill that merely restates a `rules/` file is redundant — delete one of them. Rules constrain; skills guide through multi-step work.
