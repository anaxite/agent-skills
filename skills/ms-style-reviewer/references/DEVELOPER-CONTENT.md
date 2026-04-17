# Developer content & chatbots/virtual agents

Distilled from the Microsoft Writing Style Guide — developer content and chatbots/virtual agents sections.

---

## Developer content

### General principles

- Apply the Microsoft brand voice even in technical content — warm, crisp, clear, ready to help.
- Assume fundamental programming knowledge; skip basics and focus on technology-specific or product-specific information.
- Two foundational content types: **reference documentation** and **code examples**.

### Code examples

#### Planning

- Start with simple examples; build complexity after covering common scenarios.
- Prioritize frequently used elements and elements that are difficult or tricky to use.
- Avoid illustrating obvious points or contrived scenarios.
- Reserve complicated examples for tutorials/walkthroughs with step-by-step explanation.
- Add an introduction describing the scenario; list requirements and dependencies.
- Provide an easy way to copy and run the code.
- Use SEO techniques (keywords, linking) to improve discoverability of code examples.

#### Writing

- Design code for reuse; help developers see what to modify.
- Add comments to explain non-obvious details — don't overdo it, don't state the obvious.
- Show expected output (in a separate section or via code comments).
- Consider accessibility for code that creates UI (e.g., alt text for images).
- Write secure code: validate user input, never hard-code passwords, use code-analysis tools.
- Show exception handling only when intrinsic to the example.
- Don't catch exceptions thrown by invalid arguments passed to parameters.
- Always compile and test code before publishing.

### Reference documentation

#### Article titles

- Use the programming element name followed by its type.
  - ✓ `Clear method`
  - ✓ `Device.Clear method`
- Add a differentiator (parent element, product, technology) when names are shared.
  - ✓ `Clear method (ADO)`

#### Standard article sections

- **Title & description:** Concise sentence(s) explaining what the element does — don't just repeat the element name.
- **Declaration/syntax:** Code signature; provide syntax for each supported language.
- **Parameters:** Describe each parameter's data type, whether required/optional, and input/output role. Don't just repeat the parameter name or data type.
- **Return value:** Describe the returned value and its data type; for booleans, describe the condition.
- **Remarks:** Additional detail, comparisons to similar elements, potential issues.
- **Example:** Code example illustrating usage.
- **Requirements / Applies to:** Language or platform requirements.
- **See also:** Links to related elements and further information.

#### Quality

- Maintain consistency: standard article design, predictable headings, consistent wording.
- If reference docs are auto-generated from source code, review for quality — developers may omit details important to customers.
- Remove internal or implementation details not suitable for documentation.

### Formatting developer text elements

#### General rule

- Use **code style** (monospace/backticks) for programmatic or code-related elements.
- Follow the capitalization appropriate to the programming language or operating environment.
- Match capitalization used in the actual code.

#### Quick-reference formatting table

| Element | Format |
|---|---|
| Attributes, classes, constants, directives, environment variables, event names, fields, functions, handles, keywords, logical operators, macros, members, methods, parameters, properties, registers, statements, structures, switches, values, variables | Code style |
| Code samples (including keywords/variables in text) | Code style |
| Command-line commands and options/switches/flags | Code style; capitalize as typed |
| Data formats, control classes | Code style, all uppercase |
| Data types | Code style; capitalization follows the API |
| Database names | **Bold** in prose; code style in code syntax |
| Error messages | Sentence-style capitalization; enclose in quotation marks in text |
| File name extensions | All lowercase (`.mdb`, `.doc`) |
| File/folder names (user examples) | Code style in code context; bold or plain in UI context |
| Markup/XML elements (tags) | Code style |
| Mathematical constants and variables | *Italic* |
| New terms | *Italic* on first mention when defining immediately |
| Operators | **Bold** for general; code style for code-related |
| Placeholders | *Italic* for UI text; angle brackets for code (`/v: <version>`) |
| Ports | All uppercase (`LPT1`) |
| Products/services/trademarks | Title-style capitalization; check Microsoft trademark list |
| Registry: subtrees | All uppercase, underscores, code style (`HKEY_LOCAL_MACHINE`) |
| Registry: keys/subkeys | Follow UI capitalization |
| UI text or strings | Sentence-style capitalization |
| URLs | All lowercase for complete URLs; code style if in code |
| User input | Usually lowercase (unless case-sensitive); **bold**; *italic* only for placeholders |

---

## Chatbots and virtual agents

### When to use a bot

- Use bots for tasks where asking is easier than navigating menus or searching.
- Ensure the bot adds value to the customer experience before building it.

### Honesty and trust

- Make sure users know they are chatting with a bot, not a person (e.g., introduce as a "virtual support agent").
- Explain the bot's purpose and what it can and can't do.
- Suggest a first task or provide buttons/shortcuts for frequent tasks.
- Admit mistakes; have a plan for dealing with failures.
- Plan for common misspellings and errors — accommodate them gracefully.

### Limitations

- Make the bot's specific role clear; don't imply open-ended "ask me anything" capability.
- Have fallback responses that point users in the right direction when the bot doesn't know the answer.
- Define conversational cues that trigger escalation to a human; let users know how to reach a human.

### Tone and style

- Tailor tone to context: serious topics (billing, security) → empathetic, brief, straightforward; mundane tasks → more relaxed; entertainment contexts → lighthearted and casual.
- Keep prompts short — customers abandon chats with lengthy prompts.
- Aim for a low Flesch-Kincaid grade level.

### Conversation structure

- Confirm the customer's intent before acting: ✓ *"You need to reset your password. Is that right?"*
- Clarify and disambiguate when necessary, but don't over-prompt unless misunderstanding could cause damage.
- Use buttons and actionable statements to guide the conversation.
- Offer suggestions when the bot is "confused."
- Break messages into separate, readable blocks for a natural pace.
- Don't let the bot respond so fast it rushes the customer — add a minimum delay if needed.
- Accommodate alternative word order and incomplete requests.
- Conclude the conversation when resolved: ✓ *"Is there anything else I can help you with?"*

### Engagement

- Invite the user into the conversation regularly — ask questions, make suggestions.
- If processing takes time, show "I'm thinking" or a typing indicator.
- Make responses specific to context.
  - ✓ "Here's how you change your privacy settings."
  - ✗ "Here's how you do that."

### Pronouns

- The bot uses *I*, *me*, *my* to refer to itself.
- When the customer uses *I*, *me*, *my*, those pronouns should appear on buttons/links the user selects.

### Common words

- Ensure the bot recognizes and responds to: *help*, *settings*, *start over*, *stop*.

### Mischief handling

- Plan responses for users who test the bot (repetitive questions, offensive language, nonsense).
- Humor can work but be careful — a humorous response to an offensive query can backfire.

### Maintenance

- Have a plan for maintaining, evolving, and eventually retiring the bot.
- Make it easy for users to give feedback directly through the bot.
- Label content blocks in the flow to identify where users drop off.
- Extend the experience based on feedback (e.g., positive → suggest rating; negative → link to support).
