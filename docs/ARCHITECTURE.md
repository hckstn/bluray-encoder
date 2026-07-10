# PROJECT_STATUS.md

Version: 0.5.0-alpha
Last Updated: 2026-07-10
Maintainer: M H / ChatGPT

---

# Architecture

## Main Pipeline

```text
Application
      │
      ▼
DirectoryScanner
      │
      ▼
Analyzer
      │
      ▼
SearchQueryBuilder
      │
      ▼
TMDbService
      │
      ▼
LanguageSelector
      │
      ▼
EncodingPlanner
      │
      ▼
FFmpegCommandBuilder
      │
      ▼
MKVMergeBuilder
      │
      ▼
EncodingExecutor
```

---

## Responsibilities

### Application

Coordinates the complete workflow.

### DirectoryScanner

Detects movie folders.

### Analyzer

Determines the main movie and extracts media information.

### SearchQueryBuilder

Creates a search query from folder and filename.

### TMDbService

Retrieves movie metadata.

### LanguageSelector

Applies project language rules.

### EncodingPlanner

Creates the encoding plan.

### FFmpegCommandBuilder

Creates ffmpeg commands.

### MKVMergeBuilder

Creates final MKV.

---

## Design Principles

- Simple architecture
- No plugins
- No dependency injection
- No provider abstraction
- No GUI before Version 1.0
- Keep responsibilities small