# Formatting reference

Rules distilled from the Microsoft Writing Style Guide sections on text formatting, numbers, and scannable content.

## Text formatting

### Common text elements

| Element | Convention |
|---|---|
| Database names | **Bold** |
| Emphasis | *Italic* — use sparingly |
| Error messages | Sentence-style cap; enclose in quotation marks when referenced in text |
| File attributes | All lowercase (`hidden`, `read-only`) |
| File name extensions | All lowercase (`.mdb`, `.doc`) |
| File names | Title-style capitalization |
| Folder / directory names | Sentence-style capitalization; internal caps OK for readability |
| Math constants and variables | *Italic* |
| New terms | *Italicize* the first mention when defining immediately in text |
| Ports | All uppercase (`LPT1`) |
| Products, services, apps, trademarks | Title-style capitalization; follow the official trademark list |
| UI text or strings | Sentence-style capitalization |
| URLs | All lowercase; line-break before a slash if needed; don't hyphenate |

### Formatting titles

- Use sentence-style capitalization for titles by default
- Use **bold** instead of *italics* for titles — enhances readability and accessibility
- Exceptions that keep title-style capitalization:
  - Book, white-paper, and report titles
  - Game titles
  - Event and webinar titles

### Using type

- Use sentence-style capitalization — capitalize only the first word of a sentence/phrase and proper nouns
- Avoid ALL UPPERCASE text — harder to read; words lose their recognizable shapes
- Avoid all-lowercase text — removes cues that a new section or thought is beginning
- Use left-aligned text; don't center text
- Avoid orphans (first line of a paragraph alone at the bottom of a page)
- Avoid widows (last line of a paragraph alone on the next page or containing only one word)
- Avoid lines that end with hyphens
- Don't compress line spacing to fit more text; edit the text instead
- If modifying line spacing, change it in styles, not individual paragraphs

## Numbers

### Numerals vs. words

- Spell out whole numbers **zero through nine**; use numerals for **10 or greater**
  - ✓ five databases, 10 screen savers, zero probability
- Same rule for days, weeks, and other time units
  - ✓ seven years, 28 days
- If one item in a group requires a numeral, use numerals for all items of that type
  - ✓ One article has 16 pages, one has 7 pages, and the third has only 5 pages.
- When two numbers referring to different things appear together, spell out one and use a numeral for the other
  - ✓ fifteen 20-page articles
- Don't start a sentence with a numeral; add a modifier or spell it out
  - ✗ 10 apps are included.
  - ✓ More than 10 apps are included.
- Always use numerals for:
  - Measurements (distance, temperature, volume, size, weight, pixels, points) — even below 10
  - Numbers the customer is directed to enter
  - Round numbers of 1 million or more (✓ 7 million)
  - Dimensions — spell out *by* except for tile sizes, screen resolutions, and paper sizes (use ×)
  - Time of day with AM/PM; use *noon*/*midnight* instead of 12:00
  - Percentages — numeral + *percent*; use *percentage* for unspecified quantities
  - Coordinates, rows, columns, volumes, chapters, parts, steps

### Commas in numbers

- Use commas for four or more digits: ✓ $1,024; ✓ 1,093 MB
- Exception — years, pixels, baud: commas only for five or more digits (✓ 2500 B.C.; ✓ 10,000 B.C.)
- No commas in page numbers, addresses, or after the decimal point

### Dates

- Don't use ordinal numbers for dates
  - ✗ June first, October twenty-eighth
  - ✓ June 1, October 28
- Always spell out the month name to avoid ambiguity across locales

### Phone numbers

- Use hyphens to separate parts: ✓ 612-555-0175
- Don't use parentheses, periods, or spaces

### Negative numbers

- Use a minus sign, not an en dash: ✓ −79

### Fractions and decimals

- Add a zero before the decimal point for fractions less than one: ✓ 0.5 cm
  - Exception: when the customer enters the value (✓ enter **.75"**)
- Don't use numerals separated by a slash to express fractions (except in equations)
- Hyphenate spelled-out fractions: ✓ one-third, two-thirds
  - Don't hyphenate if the numerator or denominator already contains a hyphen: ✓ three sixty-fourths
- Use the plural unit for decimal fractions; singular only for exactly 1
  - ✓ 0.5 inches, 0 inches, 1 inch, 5 inches

### Ordinal numbers

- Always spell out ordinal numbers: ✓ the first row, the twenty-first anniversary
- Don't use ordinals for dates
- Don't add *-ly* (✗ firstly, secondly)

### Ranges

- Use *from* and *through* for ranges: ✓ from 9 through 17
- Use an en dash for page ranges or where space is limited: ✓ pages 112–120
- Use *to* for time ranges: ✓ 10:00 AM to 2:00 PM
- Don't combine *from* with an en dash range (✗ from 10–15)

### Abbreviations (K, M, B)

- Don't abbreviate *thousand*, *million*, *billion* as K, M, B — spell them out or use the full number
- If space forces abbreviation: capitalize K/M/B, no space between number and letter
- Avoid decimal + K (✗ 8.21K has the same character count as 8,210)

### Compound numbers

- Hyphenate when spelled out: ✓ twenty-five, twenty-first

## Scannable content

### General principles

- Lead with what's most important — put key info above the fold and in the upper-left area
- Write short headings, short sentences, and short paragraphs
- Keep paragraphs to three to seven lines
- Establish patterns: consistent formatting, parallel structures, repeated landmarks
- Place important keywords near the beginning of headings, table entries, and paragraphs
- In long documents, provide in-page navigation (TOC with links, *Back to top* links)

### Headings

#### Writing

- Think of headings as an outline — make them specific enough to catch attention
- Use second-level headings only when there are at least two distinct subtopics
- Don't place two headings in a row with no text between them (unless organization requires it — don't add filler text)
- Keep headings short; put the most important idea first
- Focus on what matters to the customer, not product/feature names
- Use parallel sentence structure across headings at the same level
- Consider infinitive phrases for task headings (✓ *To create a heading*)
- Use noun phrases for non-task headings (✓ *Headings*)
- Don't use ampersands (&) or plus signs (+) in headings unless referring to UI or space is limited
- Avoid hyphens in headings — awkward line breaks on mobile
- Use *vs.*, not *v.* or *versus*, in headings

#### Formatting

- Use sentence-style capitalization
  - ✓ Set up the deployment environment
  - ✗ Set Up the Deployment Environment
- Don't end headings with a period; question marks and exclamation points are OK when needed for meaning
- Use *italic* in a heading only if it would be required in body text
- Don't use extra line breaks to increase heading spacing (breaks responsive design)

#### Run-in headings

- Bold run-in headings draw the eye with less space than separate headings
- Repeat common phrases like *Tip*, *Note*, *See also* as run-in headings
- Use a character style, not manual formatting

### Lists

#### General rules

- Use lists to present complex text in a scannable way
- A list needs at least two items; aim for no more than seven
- Keep items short — reader should see two to three items at a glance
- Make all items parallel in structure (all nouns, all verb phrases, etc.)

#### Bulleted lists

- Use for items that share a trait but have no required order

#### Numbered lists

- Use for sequential steps (procedures) or prioritized items

#### Term lists (definition lists)

- Use a bulleted list; number only if sequence matters
- Bold the term, sentence case; follow with a period in plain text, then the definition
- Start definitions with a capital letter and end with a period (even fragments)
  - ✓ **Draft**. You created the document, but you're still working on it.

#### Introductions

- Introduce a list with a heading, complete sentence, or a fragment ending with a colon
- Don't add explanatory text or a colon/period after a heading that introduces a list

#### Capitalization

- Begin each list item with a capital letter unless there's a reason not to (e.g., always-lowercase command)

#### Punctuation

- Don't use semicolons, commas, or conjunctions (*and*, *or*) at the end of list items
- Don't use a period unless items are complete sentences or complete the introductory sentence
- Exception: no periods if all items have three or fewer words, or are UI labels / headings / strings

### Tables

#### When to use

- Use tables for data/values, simple instructions, categories with examples, collections with two or more attributes
- Don't use a table just to present a simple list — use a list instead

#### Content

- Make the table's purpose clear; include a title or brief introduction if needed
- Put identifying information (e.g., command names) in the leftmost column
- Make entries parallel within a column
- Don't leave cells blank or use an em dash — use *Not applicable* or *None*
- Keep cell text brief (ideally one line); limit the number of columns for responsive design

#### Header rows

- Distinguish header text (larger, bolder, or different color)
- Make column headers specific (✗ "Name" → ✓ "Group" or "Employee")
- Don't let header + cell form a complete sentence (hard to localize)
- In long tables, keep the header row visible (fixed header or repeated rows)

#### Capitalization and punctuation

- Use sentence-style capitalization for the table title, column headers, and cell text
- Introductory text before a table should be a complete sentence ending with a period, not a colon
- Don't use ellipses at the end of column headers
- Use end punctuation in cells only if they contain complete sentences or a mix of fragments and sentences

### Pull quotes

- Keep pull quotes short — a few words to a few lines
- Include the author's name, title, and organization (unless the content is entirely about the quoted person)
- Use pull quotes sparingly

### Sidebars

- Use sidebars for short, interesting, related-but-not-crucial content
- Don't use for information that must be read in sequence with the main text
