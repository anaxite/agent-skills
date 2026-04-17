# Grammar and Parts of Speech

> Distilled from the Microsoft Writing Style Guide — grammar section.
> Source: <https://learn.microsoft.com/en-us/style-guide/grammar/grammar-and-parts-of-speech>

Keep grammar simple — conversational and easy to read. Basic grammar is right for most content.

---

## Verbs

### Tense

- Prefer present tense. It is easier to read and understand than past or future.
  - ✓ "Windows Update installs important updates automatically."
  - ✗ "Windows Update will install important updates automatically."

### Mood

- Use **indicative** mood for statements of fact, questions, assertions, and explanations (most content).
  - ✓ "Style sheets are powerful tools for formatting complex documents."
- Use **imperative** mood for instructions, procedures, and direct commands.
  - ✓ "Enter a file name, and then save the file."
- Avoid **subjunctive** mood (wishes, hypotheses, suggestions).
  - ✗ "We recommend that you be careful about opening email attachments."
- Do not switch moods within a sentence.

### Active and passive voice

- Use active voice whenever possible. The subject performs the action.
  - ✓ "Divide your document into as many sections as you want."
- Reserve passive voice for:
  - Avoiding blaming the customer (errors, warnings, notifications): ✓ "That site can't be found."
  - Avoiding awkward constructions.
  - Emphasizing the receiver of the action (developer content): ✓ "When the user clicks **OK**, the transaction is committed."

### Verb agreement

- A group of things takes a **singular** verb.
  - ✓ "A variety of games is available from Microsoft Store."
- Two or more singular subjects joined by *and* take a **plural** verb.
  - ✓ "Facebook and Instagram are available from Microsoft Store."
- Two or more singular subjects joined by *or* take a **singular** verb.
  - ✓ "Your tablet or phone is all you need."
- Mixed singular + plural subjects joined by *or* — match the verb to the **closest** subject.

---

## Person

### Second person (you, your) — default choice

- Write as though speaking to the reader. Use *you* and *your*.
- Omit "you can" whenever the sentence works without it.
- In product UI, avoid phrasing that sounds like a command; provide options instead.
- For AI-generated content, use past tense or words conveying uncertainty ("Suggested for you").
  - ✓ "Check if you have local admin rights."
  - ✓ "Change your settings"

### First person singular (I, me, my) — use sparingly

- Never use in marketing or support documentation.
- OK in product UI for checkbox, button, or toggle labels showing personal control.
  - ✓ "Notify me when a new Bluetooth device tries to connect to my computer"
  - ✓ "I agree to the terms of service"
- OK in navigation or filter labels to distinguish a person's content from other content.

### First person plural (we, us) — avoid

- Avoid *we* — it can feel like a daunting corporate presence.
- OK to use *we recommend* to dodge awkward passive phrasing, but rewrite if possible.
- OK in privacy and security settings where Microsoft must be the explicit speaker.
  - ✓ "We protect your privacy at every step."
  - ✗ "We recommend that you change your password." → ✓ "Change your password."
  - ✗ "We weren't able to run the Solution Checker." → ✓ "That didn't work. Try again."

---

## Nouns and pronouns

### Proper nouns — capitalize

- Capitalize unique people, places, things, product names, trademarks, titles of published works, and managed standards (e.g., Bluetooth).
- Do not capitalize common nouns (technology concepts, product categories, devices, features) unless they begin a sentence or title-style capitalization applies.
  - Common nouns: *cloud computing, smartphone, e-commerce, open source*
- Capitalize technology terms as proper nouns only to distinguish a specific product (SQL Server vs. SQL database server) or when industry convention requires it.
- When unsure, default to lowercase.

### Plural nouns

- Nouns ending in *s* → add *es*: Joneses, biases.
- Singular abbreviations → add *s*: ISVs, DBMSs.
- Abbreviations already plural → do not add *s*: MFC (Microsoft Foundation Classes).
- Single letters → apostrophe + *s*, letter in italic: *x*'s.
- Numbers → add *s*: the 1950s.
- Avoid adding *(s)* to indicate singular or plural — use the plural form instead.
  - ✗ "Wait for *x* minute(s)." → ✓ "Wait for *x* minutes."

### Pronouns and gender

- Do not use gendered pronouns in generic references. Rewrite using second person (*you*) or a role (*customer, employee*).
- *They* is OK as a singular non-binary pronoun.
- Use *he*, *she*, or *they* only when writing about real people who use those pronouns.

### Pronouns and collective nouns

- Collective nouns (e.g., *company*) take a **singular** pronoun.
  - ✓ "The company upgraded its cloud storage solution."
  - ✗ "The company upgraded their cloud storage solution."
- Exception: if emphasizing individuals in a group, a plural pronoun is OK.

---

## Words ending in -ing

- An *-ing* word can be a verb, noun, or adjective. Ensure the sentence makes the role clear.
- Flag ambiguous *-ing* headings.
  - ✗ "Meeting requirements" (ambiguous — meeting them, or requirements for a meeting?)
  - ✓ "The meeting requirements" / "How to meet the requirements"

---

## Prepositions

### Prepositional phrases

- Avoid chaining more than two prepositional phrases — they are hard to read and easy to misinterpret.

### Sentence-ending prepositions

- Ending a sentence with a preposition is OK when it improves readability.
  - ✓ "Specify which event hub you want to send the data to."

### Prepositions with UI elements

Use the correct preposition for each UI element type:

| Element | Preposition |
|---|---|
| bar (command bar, search bar, taskbar, toolbar) | **on** |
| box (list box, search box, text box) | **in** |
| command line | **on** |
| dialog | **in** |
| list | **in** |
| menu | **on** |
| page | **on** |
| pane | **in** |
| ribbon | **on** |
| search results | **in** |
| system tray | **in** |
| tab | **on** |
| window | **in** |

- ✓ "In the **Server name** box, enter the name."
- ✓ "On the ribbon, select **Options**."
- ✓ "On the toolbar, select **File** > **Save**."

---

## Dangling and misplaced modifiers

- Position modifiers directly next to the word they modify.
- Keep sentences short, simple, and in active voice to avoid modifier problems.
- A **dangling** modifier doesn't modify anything in the sentence — flag it.
- A **misplaced** modifier is too far from its target or too close to something else — flag it.
- Watch placement of *only* — its position changes meaning.
  - ✓ "*Only* the selected text is deleted." (nothing else is deleted)
  - ✗ "The selected text *only* is deleted." (ambiguous)
- Watch relative clauses at the end of sentences.
  - ✓ "There are files *that can't be removed* on the disk." (clear: files can't be removed)
  - ✗ "There are files on the disk *that can't be removed*." (ambiguous: disk or files?)
