# PROJECT_STATUS.md

Version: 0.5.0-alpha
Last Updated: 2026-07-10
Maintainer: M H / ChatGPT

---

# BluRay Encoder

## Project Status

**Version**

0.5.0-alpha

---

## Current Sprint

Sprint 5 – TMDb Integration

---

## Implemented

### Core

- [x] Configuration
- [x] Logging
- [x] CLI
- [x] Tool detection
- [x] Exception handling

### Services

- [x] DirectoryScanner
- [x] FFprobeService
- [x] FolderNameParser
- [x] FilenameParser
- [x] SearchQueryBuilder

### Pipeline

- [x] Analyzer

### Models

- [x] MovieFolder
- [x] Media
- [x] SearchQuery
- [x] MovieMetadata
- [x] MovieMatch

---

## In Progress

- [ ] TMDbService

---

## Planned

- [ ] LanguageSelector
- [ ] EncodingPlan
- [ ] FFmpegCommandBuilder
- [ ] MKVMergeBuilder
- [ ] EncodingExecutor
- [ ] MetadataWriter

---

## Finished Milestones

- [x] Scan remux directories
- [x] Detect main feature
- [x] Analyze streams using ffprobe

---

## Current Goal

First complete pipeline:

Movie Folder

↓

Search Query

↓

TMDb

↓

Language Selection

↓

Encoding Plan

---

## Last Verified

- [ ] python -m compileall .
- [ ] python encode.py scan
- [ ] python encode.py search