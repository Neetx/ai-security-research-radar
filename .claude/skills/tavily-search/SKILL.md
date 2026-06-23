---
name: tavily-search
description: |
  Search the web with LLM-optimized results via the Tavily CLI. Use this skill whenever a scan needs to find papers, releases, announcements or articles, discover sources on a topic, or check what is new — i.e. whenever there is no specific URL yet. Returns relevant results with content snippets, relevance scores and metadata. Supports domain filtering, time ranges and multiple search depths.
allowed-tools: Bash(tvly *)
---

# tavily search

Web search returning LLM-optimized results with content snippets and relevance scores.

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
# Basic search
tvly search "your query" --json

# Precision search with more results
tvly search "trellis coded quantization LLM" --depth advanced --max-results 10 --json

# Recent items only
tvly search "open-weight model release" --time-range week --topic news --json

# Primary sources only
tvly search "KV cache quantization" --include-domains arxiv.org,github.com --json

# Full page content inline (saves a separate extract call)
tvly search "vLLM disaggregated serving" --include-raw-content --max-results 3 --json
```

## Key options

| Option | Description |
|--------|-------------|
| `--depth` | `ultra-fast`, `fast`, `basic` (default), `advanced` (highest relevance) |
| `--max-results` | 0–20 (default 5) |
| `--topic` | `general` (default), `news`, `finance` |
| `--time-range` | `day`, `week`, `month`, `year` |
| `--start-date` / `--end-date` | Bound results by date (YYYY-MM-DD) |
| `--include-domains` / `--exclude-domains` | Comma-separated domain filters |
| `--include-raw-content` | Full page content (`markdown` or `text`) |
| `--chunks-per-source` | Chunks per source (advanced/fast depth) |
| `--json` / `-o FILE` | Structured output / save to file |

## Tips

- Keep queries under 400 characters; break complex questions into sub-queries.
- `--include-domains arxiv.org,github.com,huggingface.co` biases toward primary sources.
- Search snippets are NEVER citable evidence on their own — open the URL with
  the `tavily-extract` skill first (see `radar-source-verify`).
