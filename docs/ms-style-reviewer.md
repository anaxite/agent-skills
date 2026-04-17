# ms-style-reviewer

A skill that reviews content against the [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) and reports findings organized by severity.

## What it does

Give the skill a piece of writing (documentation, UI strings, error messages, blog posts, API docs, chatbot dialogue, or procedural instructions) and it will:

1. Identify the content type and audience
2. Check for common issues using a quick-scan checklist
3. Look up any suspicious terms against the full MSFT A-Z word list
4. Load topic-specific reference files as needed
5. Return a structured report with issues grouped by severity (Critical / High / Medium / Low), quoted text, rule citations, and specific replacement suggestions

## Trigger phrases

The skill activates on:
- "Review this against the Microsoft Writing Style Guide"
- "MSFT style review", "MS style guide", "Microsoft style"
- Any content submitted alongside a request for style feedback related to Microsoft style.

## Reference file structure

```
ms-style-reviewer/
├── SKILL.md                     Skill definition and review workflow
└── references/
    ├── TERM-INDEX-AD.tsv        Term index, A–D (227 rows)
    ├── TERM-INDEX-EL.tsv        Term index, E–L (226 rows)
    ├── TERM-INDEX-MS.tsv        Term index, M–S (286 rows)
    ├── TERM-INDEX-TZ.tsv        Term index, T–Z and symbols (127 rows)
    ├── A.md … Z.md              Full guidance per term, one file per letter
    ├── NUMBERS-SYMBOLS.md       Numeric and symbol entries (2D, 3D, 24/7, etc.)
    ├── TC-ACCESSIBILITY.md      Term collection: accessibility
    ├── TC-AI-BOT.md             Term collection: AI and bots
    ├── TC-BIT-BYTE.md           Term collection: bits, bytes, storage units
    ├── TC-CLOUD-COMPUTING.md    Term collection: cloud computing
    ├── TC-COMPUTER-DEVICE.md    Term collection: computers and devices
    ├── TC-DATE-TIME.md          Term collection: dates and times
    ├── TC-KEYS-KEYBOARD.md      Term collection: keys and keyboard shortcuts
    ├── TC-MOUSE.md              Term collection: mouse and pointer actions
    ├── TC-SECURITY.md           Term collection: security terminology
    ├── TC-SPECIAL-CHARS.md      Term collection: special characters
    ├── TC-TOUCH-PEN.md          Term collection: touch and pen input
    ├── TC-UNITS.md              Term collection: units of measurement
    ├── VOICE-AND-TONE.md        Voice, tone, and bias-free language
    ├── GRAMMAR.md               Grammar rules
    ├── PUNCTUATION.md           Punctuation rules
    ├── CAPITALIZATION.md        Capitalization rules
    ├── FORMATTING.md            Formatting: lists, tables, numbers, code
    ├── WORD-CHOICE.md           Word choice guidance
    ├── PROCEDURES.md            Step-by-step instructions and UI verbs
    ├── ACCESSIBILITY.md         Accessibility guidelines
    ├── GLOBAL-READY.md          Localization and global readiness
    ├── DEVELOPER-CONTENT.md     API docs, code examples, chatbot dialogue
    ├── CHECKLISTS.md            Quick-scan checklist (used in every review)
    └── COMMON-TERM-PITFALLS.md  Curated list of frequently misused terms
```

Total: 866 indexed terms, 26 letter files, 12 thematic collections, 10 topic reference files.


## Architecture

### The term lookup problem

The Microsoft style guide has an A-Z word list with 866 entries, each with detailed guidance per term. Loading all terms every review would cost ~95,000 tokens per call. To avoid this cost, the skill tries to use a two-tier lookup:

**Tier 1: TSV index (grep)**

Four TSV files (`TERM-INDEX-AD/EL/MS/TZ.tsv`) each hold roughly 200 rows. When the agent wants to check a term, it can run:

```bash
grep -i ",term," references/TERM-INDEX-*.tsv
```

Because the `match_variants` column uses leading and trailing comma delimiters (`,sign-in,login,log in,`), it should lead to an exact match. There should be no false positives from partial word matches.

Each row returns five columns:

| Column | Content |
|---|---|
| `canonical` | The term as it appears in the style guide |
| `match_variants` | Comma-delimited list of alternate forms to match on |
| `file` | Which letter file holds the full guidance (e.g., `S.md`) |
| `type` | Rule type: `prohibit`, `subst`, `format`, `clarify`, or `conditional` |
| `thumbnail` | One sentence capturing the core rule |

For most terms, the thumbnail is enough to make a finding. When the type is `conditional`, or when the thumbnail says to read more, the agent can open a letter file.

**Tier 2: Letter files (selective load)**

When the thumbnail isn't enough, the agent should perform a targeted read:

```bash
grep -n "^## Sign In, Sign Out" references/S.md
# → line 412
```

It reads from that line number down to the next `---` or `##` heading. This process pulls exactly one term's guidance into context rather than the whole letter file.

**Net effect:** if a typical review touches 5–15 term lookups, a lookup costs one grep, which is a few tokens per matched line. Full-entry reads are rare. Total per-review cost stays well under 15,000 tokens regardless of how large the reference corpus is.

### Selective topic file loading

The 10 topic reference files (GRAMMAR, PUNCTUATION, etc.) are also loaded selectively. The skill's workflow step 3 has a decision table mapping content type and quick-scan findings to specific files. A UI string review might load VOICE-AND-TONE, WORD-CHOICE, and CAPITALIZATION. An API doc review loads DEVELOPER-CONTENT, FORMATTING, and GRAMMAR. Files with no relevance to the content are never loaded.

### Why TSV instead of JSON or a database

- **Grep works without tools.** The agent can run `grep` in any environment. No database driver, no Python, no parsing library.
- **Exact matching via delimiters.** The `,term,` pattern avoids partial matches without regex complexity.
- **One matched line = one term.** The agent never has to parse a larger structure to extract the relevant row.
- **Files stay under ~10K tokens each.** The index is split into four range files (A–D, E–L, M–S, T–Z) so even a "load the whole index" fallback stays reasonable.

### Why split into four range files instead of one

A single `TERM-INDEX.tsv` with 866 rows weighs ~25,000 tokens. The four range files average ~6,500 tokens each. The glob `TERM-INDEX-*.tsv` still searches all four in one grep command, so there's no query overhead. Only the matched lines enter context.

### Why term collections are separate files

Twelve term collections (accessibility, cloud computing, keyboard shortcuts, etc.) use a table format with multiple entries per file. Extracting each row into the TSV would add ~150–200 rows and require parsing brittle markdown tables. Instead, the skill instructs the agent to check the relevant TC file directly when a term isn't found in the TSV. The 12 files are small enough (500–2,800 tokens each) that loading one on demand is cheap.

### The `match_variants` column

Variants cover:
- Hyphenated forms (`sign-in` alongside `sign in`)
- Run-together forms (`signin`)
- Wrong forms explicitly named in the guidance (`login`, `logon`, `log on` all point to the `sign in, sign out` entry)

Variants do not include generic synonyms. Only forms that the style guide itself names as wrong or alternative are listed. This keeps matches precise and avoids false positives.

### How the reference files were built

The source material is the Microsoft Style Guide's A-Z word list, scraped as ~878 individual markdown files (one per term). A Python script:

1. Stripped YAML frontmatter from each source file
2. Extracted the canonical term from the H1 heading
3. Grouped entries by starting letter into 26 letter files
4. Applied regex heuristics to classify each term's `type`

A separate LLM pass (one batch per letter) then filled in the `match_variants` and `thumbnail` columns, and corrected any misclassified `type` values.

## Known constraints

**Total file size error from the skill validator**

The validator reports ~117,000 total tokens across all reference files. This trips its size threshold. In practice, no review should load more than a fraction of those files; the architecture is specifically designed to avoid loading everything. The error is a false positive from a validator that counts total corpus size rather than per-call token cost.

If we find out that agents cannot load references selectively, we'll have to revisit this section.

**Scorer truncation**

The skill quality scorer truncates files at 8,000 characters. The content-type shortcuts section at the end of `SKILL.md` falls past this cutoff and is therefore not evaluated. The section itself is complete.
