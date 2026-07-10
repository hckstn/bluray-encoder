# PROJECT_STATUS.md

Version: 0.5.0-alpha
Last Updated: 2026-07-10
Maintainer: M H / ChatGPT

---

# PROJECT_STATUS.md

Version: 0.5.0-alpha
Last Updated: 2026-07-10
Maintainer: M H / ChatGPT

---

# BluRay Encoder

## Project Charter

### Vision

BluRay Encoder is a command-line application that automates the creation of
high-quality movie files from Blu-ray and DVD remuxes.

The application is designed for long-term personal media archiving with a
strong focus on quality, reproducibility and maintainability.

---

# Objectives

The software shall

- automatically analyze remuxes
- automatically identify movies
- automatically select the correct languages
- automatically generate optimized encoding commands
- automatically create the final MKV

The user should only need to verify the results before starting an encode.

---

# Target Audience

Private users with legally created Blu-ray/DVD remuxes.

The project is **not** intended as a media server.

---

# Core Principles

## Quality First

Encoding quality is always more important than encoding speed.

---

## Automation

Every repetitive task should be automated whenever possible.

---

## Simplicity

Prefer simple solutions over complex abstractions.

Avoid unnecessary dependencies.

---

## Transparency

Every important processing step should be understandable.

Generated commands should always be visible.

---

## Maintainability

Readable code is preferred over clever code.

Small classes.

Small functions.

Clear responsibilities.

---

# Version 1.0 Scope

Included

- Scan remux folders
- Analyze media
- TMDb lookup
- Automatic language selection
- Encoding planning
- FFmpeg command generation
- MKVToolNix remux
- Metadata writing
- CLI

Excluded

- GUI
- Plex
- Jellyfin
- Watch folders
- Poster download
- NFO generation
- TV shows

---

# Success Criteria

Version 1.0 is complete when a complete movie can be processed automatically:

Movie Folder

↓

Analysis

↓

Metadata

↓

Language Selection

↓

Encoding

↓

Final MKV

without manual intervention.