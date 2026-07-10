# PROJECT_STATUS.md

Version: 0.5.0-alpha
Last Updated: 2026-07-10
Maintainer: M H / ChatGPT

---

# Development Rules

These rules are mandatory for all future development.

---

## General

- Use English in all source code.
- Keep the architecture simple.
- Avoid unnecessary abstractions.
- Prefer readability over cleverness.

---

## Files

- Always generate complete files.
- Never generate patches.
- Never generate diffs.
- Existing files are always replaced completely.

---

## Classes

- One responsibility per class.
- Prefer classes below 200 lines.
- Prefer functions below 40 lines.

---

## Development Workflow

Plan

↓

Implementation

↓

Test

↓

Commit

↓

Push

---

Never start a new feature before the previous feature has been tested.

---

## Git

One feature per commit.

One sprint per feature branch.

Merge into develop only after successful testing.

---

## Version 1.0 Scope

Included

- Scan
- Analyze
- TMDb
- Language Selection
- Encoding Planning
- FFmpeg
- MKVToolNix

Excluded

- GUI
- Jellyfin Integration
- Plex Integration
- Watch Folders
- NFO
- Poster Download