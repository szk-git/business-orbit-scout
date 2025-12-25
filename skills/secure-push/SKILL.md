---
name: secure-push
description: Enforce secret-safe workflow when given API keys or asked to push/commit. Use when handling credentials, environment files, git commits, or git push operations to ensure keys are masked and never committed or pushed.
---

# Secure Push

## Core rules
- Mask any API key or secret provided by the user in all outputs, logs, and examples.
- Never commit or push API keys or secrets, even if asked.
- Always use `.env` or `.secrets` files for local storage of secrets.
- Ensure `.env` and `.secrets` are in `.gitignore` before any commit/push.

## Workflow
1. If the user provides a key, store it only in `.env` or `.secrets`; do not echo it back unmasked.
2. Keep a local `.env` with real values and use placeholders in any tracked files (e.g., `.env.example`).
3. Before commit/push, verify secrets are not staged; if they are, reset them and keep only redacted placeholders.
4. If a commit or push is requested and secrets are detected, stop and explain the issue; propose safe alternatives.
5. When sharing configuration examples, use placeholders (e.g., `API_KEY=REDACTED`) instead of real values.

## Examples
- "Here is my API key, please push" -> Mask key, add to `.env`, verify `.gitignore`, push without secrets.
- "Commit these changes" -> Check for secrets in tracked files; keep secrets only in `.env`/`.secrets`.
