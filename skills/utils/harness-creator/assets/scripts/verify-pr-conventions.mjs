#!/usr/bin/env node
// Deterministic judge: branch name, commit header, and PR body contract.
// Usage: node scripts/verify-pr-conventions.mjs --branch <name> --commit <header> --body <file>
// Exit 0 = conforms, 1 = violations listed on stdout. Single implementation used by CI and locally.
import fs from "node:fs";

const args = Object.fromEntries(
  process.argv.slice(2).flatMap((a, i, arr) => (a.startsWith("--") ? [[a.slice(2), arr[i + 1]]] : []))
);

const errors = [];

if (!/^(feat|fix|docs|chore|refactor|test|style|perf|ci|build)\/.+/.test(args.branch ?? "")) {
  errors.push(`branch '${args.branch}' must start with a valid type prefix + '/'`);
}

const header = args.commit ?? "";
if (!/^(feat|fix|docs|chore|refactor|test|style|perf|ci|build)(\(.+\))?(!)?: .+/.test(header)) {
  errors.push("commit header must be a Conventional Commit");
} else if (header.length > 100) {
  errors.push(`commit header exceeds 100 chars (${header.length})`);
}
if (/co-authored-by/i.test(header)) errors.push("no Co-Authored-By / AI attribution trailers");

const body = args.body ? fs.readFileSync(args.body, "utf8") : "";
for (const section of ["Linked Issue", "Summary", "Changes", "Test Plan"]) {
  if (!body.toLowerCase().includes(section.toLowerCase())) {
    errors.push(`PR body missing section: ${section}`);
  }
}

if (errors.length) {
  console.log(errors.map((e) => `- ${e}`).join("\n"));
  process.exit(1);
}
console.log("PR conventions: OK");
