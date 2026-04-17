---
name: ms-style-reviewer
description: "Review content against the Microsoft Writing Style Guide, reporting issues by severity (Critical/High/Medium/Low) with specific fixes. Use this skill whenever the user asks you to review, edit, or check text for compliance with Microsoft style, including documentation, UI strings, developer docs, blog posts, error messages, chatbot dialogue, or procedures. Also trigger when the user mentions Microsoft style, MSFT style guide, or MS style review."
---

# Microsoft Writing Style Guide - Review Skill

Review content against the [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) and report findings organized by severity.

## Review workflow

### 1. Understand the content

Before reviewing, identify:
- **Content type**: documentation, UI text, blog post, developer/API docs, error messages, chatbot dialogue, procedures/instructions
- **Audience**: end users, developers, IT admins, general public
- **Scope**: full document, specific section, or single string

This determines which reference files to load. DO NOT load everything upfront.

### 2. Quick-scan pass

Read [CHECKLISTS.md](references/CHECKLISTS.md) and scan the content against it. This catches the most common issues fast: capitalization, grammar, punctuation, word choice, acronym handling, numbers, formatting, procedures, and responsiveness.

Also read [COMMON-TERM-PITFALLS.md](references/COMMON-TERM-PITFALLS.md) and check whether the content uses any flagged terms.

### 2b. Term lookup

For any terms flagged in the quick scan—or any word that might be on the MSFT prohibited/preferred list—look up in the term index using grep:

```bash
grep -i ",term," references/TERM-INDEX-*.tsv
```

The index is split into four range files: [TERM-INDEX-AD.tsv](references/TERM-INDEX-AD.tsv) (A–D), [TERM-INDEX-EL.tsv](references/TERM-INDEX-EL.tsv) (E–L), [TERM-INDEX-MS.tsv](references/TERM-INDEX-MS.tsv) (M–S), [TERM-INDEX-TZ.tsv](references/TERM-INDEX-TZ.tsv) (T–Z and symbols). The glob `TERM-INDEX-*.tsv` searches all four at once.

The `match_variants` column (column 2) uses leading and trailing comma delimiters for exact matching. Always search the `match_variants` column, not just the `canonical` column (column 1).

TSV columns: `canonical | match_variants | file | type | thumbnail`

- If the `thumbnail` (column 5) resolves the question, record the finding and move on.
- If the `type` is `conditional` or the thumbnail indicates complexity, load the full entry from the letter file. The `file` column gives the filename (e.g., `S.md`):

```bash
grep -n "^## canonical term" references/S.md
```

Read from that line number down to the next `---` or `##` heading.

- If the term isn't found in any index file, check the relevant term collection file: [TC-ACCESSIBILITY.md](references/TC-ACCESSIBILITY.md), [TC-AI-BOT.md](references/TC-AI-BOT.md), [TC-BIT-BYTE.md](references/TC-BIT-BYTE.md), [TC-CLOUD-COMPUTING.md](references/TC-CLOUD-COMPUTING.md), [TC-COMPUTER-DEVICE.md](references/TC-COMPUTER-DEVICE.md), [TC-DATE-TIME.md](references/TC-DATE-TIME.md), [TC-KEYS-KEYBOARD.md](references/TC-KEYS-KEYBOARD.md), [TC-MOUSE.md](references/TC-MOUSE.md), [TC-SECURITY.md](references/TC-SECURITY.md), [TC-SPECIAL-CHARS.md](references/TC-SPECIAL-CHARS.md), [TC-TOUCH-PEN.md](references/TC-TOUCH-PEN.md), [TC-UNITS.md](references/TC-UNITS.md).

**No bash access?** Read the relevant range file directly and scan for the term, or read the letter file directly (e.g., [S.md](references/S.md) for terms starting with S).

### 3. Deep review: load references by topic

Load reference files based on issues the quick scan surfaced and the content type identified in step 1. Use the table below to decide which files to load; skip files that don't apply.

| Reference file | Load when... |
|---|---|
| [TERM-INDEX-AD.tsv](references/TERM-INDEX-AD.tsv), [TERM-INDEX-EL.tsv](references/TERM-INDEX-EL.tsv), [TERM-INDEX-MS.tsv](references/TERM-INDEX-MS.tsv), [TERM-INDEX-TZ.tsv](references/TERM-INDEX-TZ.tsv) | Always: grep for flagged terms (see step 2b) |
| [A.md](references/A.md), [B.md](references/B.md), [C.md](references/C.md), [D.md](references/D.md), [E.md](references/E.md), [F.md](references/F.md), [G.md](references/G.md), [H.md](references/H.md), [I.md](references/I.md), [J.md](references/J.md), [K.md](references/K.md), [L.md](references/L.md), [M.md](references/M.md), [N.md](references/N.md), [O.md](references/O.md), [P.md](references/P.md), [Q.md](references/Q.md), [R.md](references/R.md), [S.md](references/S.md), [T.md](references/T.md), [U.md](references/U.md), [V.md](references/V.md), [W.md](references/W.md), [X.md](references/X.md), [Y.md](references/Y.md), [Z.md](references/Z.md) | When a TSV thumbnail is insufficient and full term guidance is needed |
| [TC-ACCESSIBILITY.md](references/TC-ACCESSIBILITY.md), [TC-AI-BOT.md](references/TC-AI-BOT.md), [TC-BIT-BYTE.md](references/TC-BIT-BYTE.md), [TC-CLOUD-COMPUTING.md](references/TC-CLOUD-COMPUTING.md), [TC-COMPUTER-DEVICE.md](references/TC-COMPUTER-DEVICE.md), [TC-DATE-TIME.md](references/TC-DATE-TIME.md), [TC-KEYS-KEYBOARD.md](references/TC-KEYS-KEYBOARD.md), [TC-MOUSE.md](references/TC-MOUSE.md), [TC-SECURITY.md](references/TC-SECURITY.md), [TC-SPECIAL-CHARS.md](references/TC-SPECIAL-CHARS.md), [TC-TOUCH-PEN.md](references/TC-TOUCH-PEN.md), [TC-UNITS.md](references/TC-UNITS.md) | When a term isn't in the TERM-INDEX but may belong to a thematic collection |
| [VOICE-AND-TONE.md](references/VOICE-AND-TONE.md) | Always: voice and tone apply to all content |
| [GRAMMAR.md](references/GRAMMAR.md) | Content has multiple paragraphs or complex sentence structures |
| [PUNCTUATION.md](references/PUNCTUATION.md) | Quick scan flagged punctuation issues, or content uses dashes, colons, semicolons, quotation marks |
| [CAPITALIZATION.md](references/CAPITALIZATION.md) | Headings, titles, UI labels, or product names are present |
| [FORMATTING.md](references/FORMATTING.md) | Content has lists, tables, numbers, headings, or code references |
| [WORD-CHOICE.md](references/WORD-CHOICE.md) | Content uses jargon, technical terms, or formal language |
| [PROCEDURES.md](references/PROCEDURES.md) | Content includes step-by-step instructions or UI interaction verbs |
| [ACCESSIBILITY.md](references/ACCESSIBILITY.md) | Content has images, alt text, references to visual elements, or describes user interactions |
| [GLOBAL-READY.md](references/GLOBAL-READY.md) | Content may be translated or targets international audiences |
| [DEVELOPER-CONTENT.md](references/DEVELOPER-CONTENT.md) | Content is API docs, code examples, reference docs, or chatbot/virtual agent dialogue |

### 4. Report findings

Organize findings by severity, then by topic. Use this structure:

```
## Review summary

<1-2 sentence overall assessment>

## Critical

<Issues that are clearly wrong: grammar errors, incorrect terminology, factual errors, accessibility failures>

## High

<Issues that significantly affect quality: voice/tone violations, capitalization errors, bias-free language issues, clarity problems>

## Medium

<Style preferences and consistency: formatting inconsistencies, word choice suggestions, punctuation style>

## Low

<Optimization suggestions: brevity improvements, alternative phrasings, minor structural tweaks>
```

Rules for the report:
- Quote the problematic text, then explain the issue and suggest a fix
- Cite the specific rule area (e.g., "Voice and tone: bias-free communication", "Punctuation: em dashes")
- If no issues found at a severity level, omit that section
- If the content is clean, say so; don't invent issues
- Group related issues together (e.g., if the same capitalization mistake appears 5 times, report it once with a note about frequency)
- Keep suggestions actionable: show the exact replacement text

## Content-type shortcuts

For efficiency, prioritize reference files by content type:

- **UI strings / error messages**: VOICE-AND-TONE → WORD-CHOICE → COMMON-TERM-PITFALLS → CAPITALIZATION
- **Procedures / how-to docs**: PROCEDURES → FORMATTING → GRAMMAR → VOICE-AND-TONE
- **API / developer docs**: DEVELOPER-CONTENT → FORMATTING → GRAMMAR → WORD-CHOICE
- **Blog posts / marketing**: VOICE-AND-TONE → WORD-CHOICE → GRAMMAR → PUNCTUATION
- **Chatbot dialogue**: DEVELOPER-CONTENT → VOICE-AND-TONE → WORD-CHOICE → ACCESSIBILITY
