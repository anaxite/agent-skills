# Accessibility

Rules distilled from the Microsoft Writing Style Guide — Accessibility section.

## Writing for all abilities

- Be especially clear and concise in instructions for product setup, basic features, input methods, and accessibility features.
- Lead with what matters most so readers know immediately where to focus.
- Keep paragraphs short and sentence structure simple. Aim for one verb per sentence.
- Use parallel writing structures for similar things (e.g., same part of speech to start each list item).
- Spell out words like *and*, *plus*, and *about* — screen readers can misread special characters such as `+` and `~`.
- Write brief but meaningful link text; links should make sense without surrounding text.
- Distinguish links visually with redundant cues (both color and underline).
- Don't force line breaks (hard returns) within sentences and paragraphs — they may break in resized windows or with enlarged text.

## Person-first language

- Default to people-first language: refer to the person first, then the disability.
  - ✓ "people with disabilities"
  - ✗ "disabled people" (unless the audience prefers identity-first language)
- Use approved accessibility terminology from the Microsoft term collection.

## Content structure and location

- Use lists, headings, and tables to reinforce relationships between concepts.
- Provide a brief description of what a table contains immediately before the table.
- Use concise, specific column headings.
- Use heading levels to communicate hierarchy — don't rely on text formatting alone.
- Don't use directional terms (*left*, *right*, *above*, *below*) as the only clue to location.
  - ✗ "In the left pane …"
  - ✓ "In the **Navigation** pane …" or "the first item in the following list"

## Alternative input methods

- Document all supported input modes: mouse, keyboard, voice, game controller, gestures, and other methods.
- Use generic verbs that apply to all input methods.
  - ✗ "Click the button" (mouse-specific)
  - ✗ "Swipe left" (touch-specific)
  - ✓ "Select the button"

## Alternative text (alt text)

### General rules

- Add alt text to all images that convey important meaning.
- Purely decorative images don't need alt text. In web content, use null alt text (`alt=""`) instead of omitting the `alt` attribute.
- Begin alt text with a capital letter. End with a period (even for fragments).
- Don't start with a generic word like "Image" — screen readers already announce images.
  - ✗ "Image of a settings menu"
  - ✓ "Screenshot of the settings menu"
- Don't use the image file name as alt text.
- If text is embedded in an image and not in surrounding content, include it (paraphrased if needed).
- Limit alt text to 150 characters. For complex images, add a detailed description in surrounding text or linked content.
- Avoid repeating surrounding text in alt text.
- If an image has a caption, ensure caption and alt text aren't redundant.

### Buttons and links

- If a button or link has an image but no text, the image must have alt text.
- Focus alt text on what the button/link *does*, not what the image *shows*.
  - ✗ "Magnifying glass button for searching"
  - ✓ "Search this site"
- Don't start alt text with "Button" or "Link" — screen readers already announce these roles.
- If a button or link has both an image and text, the image is decorative and typically needs no alt text.

### Alt text examples

| Scenario | ✓ Good | ✗ Bad | Why |
|---|---|---|---|
| Screenshot illustrating preceding steps | "Screenshot of the tab for creating an account." | Long description repeating every UI element | Steps already provide the detail |
| Unlabeled settings button (gear icon) | "Open user settings." | "Image of two interlocking gears" | Purpose matters more than appearance |
| Photo as main content of a social post | "A group of people smiling, cheering, and taking photos of a speaker." | "Photograph from the launch event." | Image meaning lies in the visual details |
| Link image with existing link text | Use `alt=""` (decorative) | Describe the logo image | Redundant — link text already present |

## Colors and patterns

- Don't convey information with color alone — combine color with text, underlines, or patterns.
  - ✓ Use both color and pattern to differentiate data in charts.
- Don't hard-code colors — they become illegible in high-contrast themes.
- Use a minimum contrast ratio of 4.5:1.
- Avoid low-contrast combinations such as light green on white or red on green.
- Don't use screens, tints, or shaded backgrounds behind text.
- Don't use watermarks or images behind text — reduced contrast hinders readability and screen readers.

## Graphics, design, and media

- Use clean, simple graphic design.
- Provide alternate ways to get information conveyed by pictures, multimedia, and image maps.
- Provide clear written descriptions that don't require pictures, or provide both.
- Keep text within a rectangular grid for visibility and ease of scanning.
- Format tables according to WCAG 2.0.
- If you use frames, provide alternative pages without them.
- Don't use scrolling marquees unless the user has control over them.
- Provide text links in addition to image maps.
- Plan links and image-map links to support Tab key navigation with bidirectional text.

### Audio and video

- Provide closed captions, transcripts, or descriptions for audio and video content.
- Video requires both closed captions and audio descriptions.
- If a video has a thumbnail image, add alt text to the thumbnail.
- For complex elements requiring long descriptions, use surrounding text or a linked separate document.
