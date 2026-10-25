#!/usr/bin/env node
// PreToolUse guard: block dangerous commands. Node stdlib only — no jq/rg/coreutils.
// Reads the tool call as JSON from stdin: { tool, command | path }.
// Exit 0 = allow, exit 2 = block (message on stderr).
// Adapt DENIED and PROTECTED to the repo; keep the fail-closed default.
import fs from "node:fs";

const DENIED = [
  /git\s+push\s+.*--force/i,
  /git\s+reset\s+--hard/i,
  /--no-verify/i,
  /--no-guard/i,
  /Co-Authored-By/i,
];

const PROTECTED = [/^dist\//, /^build\//, /\.next\//, /target\//];

let input = "";
try {
  input = fs.readFileSync(0, "utf8");
} catch {
  process.exit(0); // no stdin (manual run) -> allow
}

let call = {};
try {
  call = JSON.parse(input);
} catch {
  console.error("block-dangerous-commands: unreadable input, blocking to be safe.");
  process.exit(2);
}

const text = `${call.command ?? ""}\n${call.path ?? ""}`;

const denied = DENIED.find((re) => re.test(text));
if (denied) {
  console.error(
    `Blocked by harness guard (${denied}). Do the safe alternative instead: ` +
      `regular push, staged commit without bypass flags, no attribution trailers.`
  );
  process.exit(2);
}

if (call.tool !== "Bash" && PROTECTED.some((re) => re.test(call.path ?? ""))) {
  console.error(
    `Blocked: build artifacts are generated, never edited by hand. ` +
      `Change the source and rebuild instead (see knowledge/tech-stack.md).`
  );
  process.exit(2);
}

process.exit(0);
