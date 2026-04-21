# Large File Strategy

Include this block in subagent instructions when any individual file is large enough to
risk exhausting context (rough threshold: a single file over ~100KB, or total content
approaching 200KB).

---

## Instructions for subagents reviewing large files

One or more files in this review set is large. Work through the following strategy in
order, stopping at the first approach that gives you enough coverage to review meaningfully:

### Tier 1: Structural tools (preferred)

If you have access to any of the following, use them to get an overview without loading
the full file:

- **grep / ripgrep**: Search for key terms, headings, function names, exports, or
  structural markers. A targeted grep pass can tell you a lot about organization and
  coverage without reading every line.
- **ctags or similar symbol extractors**: If available, extract a symbol map to understand
  the structure of code files.
- **wc / file stats**: Get line counts, word counts, and section distribution.
- **MCP filesystem or code analysis tools**: If a connected MCP server offers file
  inspection or code analysis, use it.
- **find**: Identify related files, imports, or dependencies without loading them.

Combine these to build a structural picture, then load only the sections most relevant
to the review.

### Tier 2: Targeted sampling (fallback)

If structural tools are not available or insufficient:

- Read the **beginning** of the file (first ~20%)
- Read a **middle section** (around the 50% mark, ~10%)
- Read the **end** of the file (last ~20%)
- Note explicitly in your review that it is based on a sample, not the full file

### Tier 3: Flag and skip (last resort)

If neither tier 1 nor tier 2 is viable (e.g., the file is inaccessible, or so
large that even sampling is impractical):

- Note the file in your review
- Explain that you were unable to review it and why
- Review the remaining files normally

---

**Important:** Always be explicit in your review about which files you read in full, which
you sampled, and which you skipped. The dispatching agent and the user need to know the
coverage of your review.
