---
name: tavily-extract
description: |
  Extract clean markdown or text from specific URLs via the Tavily CLI. Use this skill whenever a URL must be opened to be cited — papers, changelogs, release pages, blog posts, docs — including JavaScript-rendered pages. Processes up to 20 URLs per call and supports query-focused chunking for long pages.
allowed-tools: Bash(tvly *)
---

# tavily extract

Extract clean markdown/text content from one or more URLs. In this repo,
"opened" means extracted with this skill (or fetched with a built-in web tool) —
only opened URLs are citable as evidence.

## Before running any command

Check `tvly --status`. If `tvly` is not on PATH:

```bash
pip install -q tavily-cli || uv tool install tavily-cli
```

Auth comes from the `TAVILY_API_KEY` environment variable (already set in this
environment). Never print it. If it is unset, report that and fall back to the
built-in web tools.

## Quick start

```bash
# Single URL
tvly extract "https://example.com/article" --json

# Batch (max 20 per call)
tvly extract "https://arxiv.org/abs/XXXX.XXXXX" "https://github.com/org/repo" --json

# Long pages: only the relevant chunks
tvly extract "https://example.com/docs" --query "release date changelog" --chunks-per-source 3 --json

# JS-heavy pages
tvly extract "https://app.example.com" --extract-depth advanced --json
```

## Key options

| Option | Description |
|--------|-------------|
| `--query` + `--chunks-per-source` | Return only chunks relevant to a query (1–5 per URL) |
| `--extract-depth` | `basic` (default, try first) or `advanced` (JS-rendered pages) |
| `--format` | `markdown` (default) or `text` |
| `--timeout` | 1–60 seconds for slow pages |
| `--json` / `-o FILE` | Structured output / save to file |

## Tips

- Always quote URLs (shell interprets `?` and `&`).
- Try `basic` first; escalate to `advanced` only if content is missing.
- arXiv abs pages often hide authors/dates in the extraction — cross-check exact
  metadata with `curl -sL 'https://export.arxiv.org/api/query?id_list=...'`
  (see `radar-source-verify`).
- If a search already used `--include-raw-content`, skip the extract step.
