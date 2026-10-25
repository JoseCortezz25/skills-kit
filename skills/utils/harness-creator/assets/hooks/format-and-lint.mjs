#!/usr/bin/env node
// PostToolUse: format + lint-fix files the agent just edited. Node stdlib only.
// Reads the tool call as JSON from stdin: { path }.
// Adapt FORMATTERS to the repo toolchain declared in knowledge/tech-stack.md.
// Silent on success; non-zero exit surfaces the tool output to the agent.
import { execFileSync } from "node:child_process";
import fs from "node:fs";

const FORMATTERS = [
  // [file pattern, command, args]
  [/\.(ts|tsx|js|jsx|json|md)$/, "npx", ["prettier", "--write"]],
  [/\.(ts|tsx)$/, "npx", ["eslint", "--fix"]],
  // [/\.rs$/, "cargo", ["fmt"]],
  // [/\.py$/, "ruff", ["format"]],
];

let call = {};
try {
  call = JSON.parse(fs.readFileSync(0, "utf8"));
} catch {
  process.exit(0);
}
const file = call.path;
if (!file || !fs.existsSync(file)) process.exit(0);

for (const [pattern, cmd, args] of FORMATTERS) {
  if (!pattern.test(file)) continue;
  try {
    execFileSync(cmd, [...args, file], { stdio: "pipe" });
  } catch (err) {
    console.error((err.stdout ?? "") + (err.stderr ?? "") || `${cmd} failed on ${file}`);
    process.exit(1);
  }
}
process.exit(0);
