# Procedures and Instructions

Distilled from the Microsoft Writing Style Guide — Procedures and instructions section.

## General principles

- Prefer no procedure at all — if the UI is clear, skip the procedure
- Choose the simplest format: illustration, video, one-sentence instruction, or numbered steps
- Document all input methods (mouse, keyboard, voice, touch, game controller) for accessibility

## Writing step-by-step instructions

### Scannability

- Use headings to help customers find instructions quickly
- Use parallel structure in headings
  - ✓ "Create a profile" / "Add an account"
- Don't repeat the heading in an introductory sentence — add only necessary information

### Multiple-step procedures

- Use a numbered list
- Provide an introductory step about where to start if there's any chance of confusion
- Use a separate step for each instruction (OK to combine short steps in the same UI location)
- Include completion actions (e.g., selecting **OK** or **Apply**)
- Don't overwhelm — fit all steps on one screen

### Single-step procedures

- Use a bullet instead of a number for a single step
  - ✓ "To move a group of tiles:\n  - On the **Start** screen, zoom out and drag the group where you want it."

### Tips for writing steps

- Use complete sentences — capitalize the first word, end with a period
- Start steps with an imperative verb (after any necessary location phrase)
- State the location before the action
  - ✓ "For **Alignment**, select **Left**."
  - ✓ "On the **Design** tab, select **Header Row**."
- Abbreviate simple sequential selections with `>` (space before and after, not bold)
  - ✓ Select **Accounts** > **Other accounts** > **Add an account**.
  - Note: screen readers may skip brackets — check accessibility before using

## Describing interactions with UI

Use input-neutral verbs. Avoid input-specific verbs like *click* or *swipe*.

| Verb | Use for |
|------|---------|
| **Open** | Apps, programs, panes, File Explorer, files, folders, shortcut menus. Don't use for commands/menus. |
| **Close** | Apps, programs, panes, dialogs, files, folders, notifications, tabs. |
| **Leave** | Websites and webpages. |
| **Go to** | Menus, tabs, specific UI locations, websites. OK to use "On the **X** tab" for brief instructions. |
| **Select** | Buttons, checkboxes, list-box values, links, menu items, gallery items, keys/keyboard shortcuts. |
| **Select and hold** | Press-and-hold interactions. OK to add "(or right-click)" when not touch-specific. |
| **>** | Separating sequential steps of the same selection type. Don't bold the `>`. |
| **Clear** | Clearing a checkbox. |
| **Choose** | Options based on customer preference. Also use when the UI label starts with "Select" to avoid repetition. |
| **Switch / turn on / turn off** | Toggle keys and toggle switches. |
| **Enter** | Typing or inserting a value, or typing/selecting in a combo box. |
| **Move / drag** | Moving items (tiles, windows, files) from one place to another. Use *move through* for navigating pages/screens. |
| **Zoom / zoom in / zoom out** | Changing magnification. |

### Key verb rules

- ✗ "Click **Save**" — ✓ "Select **Save**"
- ✗ "Swipe left" — ✓ Use input-neutral language or touch-specific section
- ✗ "Open the **File** command" — use **Go to** for menus
- ✗ "Double-click" — ✓ "Select" (or "double-tap" only in touch-specific content)

## Describing alternative input methods

### Mouse procedures

- List mouse method before keyboard method consistently
- Don't combine keyboard and mouse actions as shortcuts
  - ✗ "Shift+click" — ✓ "Select Shift while clicking …"

### Keyboard procedures

- Always document keyboard procedures for accessibility, even when indicated in UI (e.g., underlined letters)

### Pen and touch procedures

- Use **tap** and **double-tap** (not *click*/*double-click*) for touch/pen content
- Don't say "tap on" or "double-tap on"
- Use **tap and hold** only if the app requires it; don't say "touch and hold"
- Use **pan** for controlled-rate movement (not *drag* or *scroll*)
- Use **flick** for quick finger scrolling (not *scroll*)
- Use **swipe** for short quick movements opposite to scroll direction

### Presenting multiple input methods

- **Table format:** separate columns for each input method
- **Inline parenthetical:** primary method first, alternative in parentheses
  - ✓ "To pan, slide one finger in any direction (or drag the mouse pointer, or use the arrow keys)."
- **Separate sentence:** primary method, then "You can also …"
  - ✓ "To copy the selection, click **Copy** on the toolbar. You can also press **Ctrl+C**."
- **Bulleted list within a step:** for several choices at one step

## Formatting text in instructions

### UI elements (documentation and technical content)

- **Buttons, checkboxes, options:** bold the name; use sentence-style capitalization unless matching UI
  - ✓ Select **Save as** — ✗ Select **Save as…** (drop trailing colon/ellipsis)
  - Don't include the UI element type (button, checkbox) unless needed for clarity
- **Commands:** bold name; don't include the word "command" unless needed
- **Menus, tabs, panes, palettes, toggles, windows:** avoid referring to them; when necessary, bold the name; don't include the element type word unless needed for clarity
- **Dialogs:** use "dialog" (not "pop-up window," "dialog box," or "dialogue box"); bold the name
- **Checkboxes:** use "Clear" (not "Uncheck" or "Deselect") for removing a selection

### Code and technical elements

- **Command-line commands and options (flags):** code style (`copy`, `/a`)
- **Markup language elements:** code style (`<img>`)
- **XML schema elements:** code style
- **Database names:** bold in text, code style in syntax

### Names and text

- **File name extensions:** all lowercase (`.mdb`, `.doc`)
- **File names (user examples):** title-style capitalization; bold if user interacts with the name; code style in code
- **Folder/directory names (user examples):** sentence-style capitalization; bold if interactive; code style in code
- **Device and port names:** all uppercase (`USB`)
- **Key names and shortcuts:** capitalize; bold in instructions; no space around `+` (`Ctrl+Alt+Del`)
- **Error messages:** sentence-style capitalization; enclose in quotation marks in running text
- **New terms:** italicize first mention when defining immediately
- **Placeholders:** italic for UI text; angle brackets for code placeholders (when not part of language syntax)
- **User input:** usually lowercase; bold or italic depending on element; italic for placeholder portions
- **URLs:** all lowercase; line-break before a slash if needed; don't hyphenate
- **Slashes:** spell out ("backslash") followed by the symbol in parentheses

### UI and general (non-documentation) content

- Avoid bold and italic formatting in UI text and non-technical content
- Prefer describing the action without naming the UI element
- If naming is necessary, use wording that clearly sets off the element name, or use quotation marks sparingly, or use bold
- Be consistent with whichever approach you choose
