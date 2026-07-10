# PROJECT_STATUS.md

Version: 0.5.0-alpha
Last Updated: 2026-07-10
Maintainer: M H / ChatGPT

---

# Architecture Decisions

This document records important architectural decisions.

Only decisions with long-term impact belong here.

---

# AD-001

## Project Scope

Version: 1.0

Status: Accepted

### Decision

The project focuses exclusively on creating an automated Blu-ray/DVD encoder.

The workflow is:

Movie Folder

↓

Analyze

↓

Metadata

↓

Language Selection

↓

Encoding

↓

Final MKV

### Out of Scope

- GUI
- Web Interface
- Jellyfin Integration
- Plex Integration
- Watch Folders
- Poster Downloads
- NFO Generation

These features may be implemented after Version 1.0.

---

# AD-002

## Programming Language

Status: Accepted

### Decision

All source code shall be written in English.

Comments, identifiers, filenames and documentation inside the source code use English only.

Reason

International readability and maintainability.

---

# AD-003

## File Generation

Status: Accepted

### Decision

Generated code is always delivered as complete files.

Partial patches or diffs are not used.

Reason

Simplifies integration and avoids inconsistencies.

---

# AD-004

## Project Architecture

Status: Accepted

### Decision

The application follows a simple layered architecture.

Application

↓

DirectoryScanner

↓

Analyzer

↓

SearchQueryBuilder

↓

TMDbService

↓

LanguageSelector

↓

EncodingPlanner

↓

FFmpegCommandBuilder

↓

MKVMergeBuilder

↓

EncodingExecutor

Reason

Simple structure with clearly separated responsibilities.

No additional abstraction layers before Version 1.0.

---

# AD-005

## Metadata Provider

Status: Accepted

### Decision

Version 1.0 supports TMDb only.

Reason

One high-quality metadata source is sufficient for the first release.

Additional providers may be added after Version 1.0 if necessary.

---

# AD-006

## Coding Style

Status: Accepted

### Decision

- Use pathlib.
- Use dataclasses.
- Use type hints.
- Prefer immutable models where appropriate.
- Keep classes small.
- Keep methods focused.

Reason

Readable and maintainable code.

---

# AD-007

## Development Workflow

Status: Accepted

### Decision

Every sprint follows the same workflow.

Planning

↓

Implementation

↓

Testing

↓

Git Commit

↓

Git Push

Reason

Every commit represents a working project state.

---

# AD-008

## Testing Policy

Status: Accepted

### Decision

A sprint is finished only after:

- Project compiles
- Feature test succeeds
- Git commit exists
- Git push completed

Reason

Avoid broken intermediate states.

---

# AD-009

## Git Workflow

Status: Accepted

### Decision

Feature branches are used for development.

Flow:

develop

↓

feature/<name>

↓

develop

↓

main

Reason

Clean history and isolated feature development.

---

# AD-010

## Project Memory

Status: Accepted

### Decision

The repository is the single source of truth.

Project documentation is stored inside the repository.

Chats are considered temporary working sessions.

Reason

Allows continuing development in new chats without losing architectural knowledge.