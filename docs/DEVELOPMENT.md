# PROJECT_STATUS.md

Version: 0.5.0-alpha
Last Updated: 2026-07-10
Maintainer: M H / ChatGPT

---

# Development Process

## Sprint Workflow

1. Planning
2. Full implementation
3. Testing
4. Git Commit
5. Git Push

Only then start the next sprint.

---

## Coding Style

- Python 3.13
- Type hints everywhere
- Dataclasses where appropriate
- Pathlib instead of os.path
- Rich for CLI output
- HTTPX for HTTP
- YAML configuration

---

## Testing

Each sprint must end with

```bash
python -m compileall .

python encode.py scan

python encode.py search
```

---

## Documentation

After every sprint update

- PROJECT_STATUS.md
- ROADMAP.md

---

## Code Generation Rules

Always generate complete files.

Never generate patches.

Never modify files partially.

Always return files ready to replace.