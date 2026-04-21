---
name: three-way-review
description: >
  Perform a three-way review of one or more files with text content, dispatching three independent subagents: one
  predisposed to find problems, one predisposed to find strengths, and one with no initial bias.
  Use when the user asks for a "three-way review", "tripartite review", "devil's advocate review",
  "positive/negative/neutral review", or any review framing that explicitly involves multiple
  perspectives on the same content. Requires a subagent-capable environment; do not attempt in
  environments without subagent support. Do not use to review binary files.
---

# Three-Way Review

Dispatches three independent subagents to review one or more files from distinct starting
perspectives, then synthesizes their findings. Each subagent approaches the content as a
reviewer with a different personality: one skeptical and critical, one generous and
appreciative, one balanced with no prior lean. The goal is to surface insights that a single
perspective would miss.

**This skill requires subagents.** If the environment does not support subagent dispatch,
tell the user and stop.
**This skill requires textual content.** Do not use this skill to review binary files.

---

## Step 0: Confirm environment

Check that subagents can be dispatched. If not, explain the limitation and stop.

---

## Step 1: Understand the files

Load and read each file. For each file:

- Note its type (prose, markdown, code, config, etc.)
- Note its apparent purpose
- Estimate its size

Then assess relationships between files (see "Multi-file handling" below).

**Size check — do this before proceeding:**

- If total content across all files exceeds **200KB**, warn the user explicitly and ask
  whether they want to proceed. Explain that reviews may be incomplete or sampled.
- If content is under 200KB but there are many files, use a temporary staging area
  (e.g. a project-approved temp location, or "project memory" in environments that support memory)
  to avoid passing oversized context to subagents.

---

## Step 2: Multi-file handling

If more than one file is provided:

1. **Infer relationships first.** Look for: shared imports or links, matching terminology,
   complementary structure (e.g., a spec and its implementation), overlapping concepts, or
   naming conventions that group them. Check surrounding files in the same directory if
   accessible; those may clarify context.

2. **If the relationship is clear**, proceed. Note the relationship briefly so subagents
   can factor it in.

3. **If the relationship is unclear**, ask the user before dispatching subagents:
   > "Before I start, I want to confirm these files are meant to be reviewed together.
   > Can you describe how they relate?"

4. By default, each subagent reviews **all files as a set**. Individual per-file reviews
   are only done if the user requests it.

---

## Step 3: Understand the review scope

Before dispatching, determine:

- **Are there guidelines?** If the user mentioned specific goals, criteria, an audience,
  a style guide, or a particular angle (e.g., "focus on clarity", "this is for a junior
  audience"), pass those to all three subagents.
- **Is there a requested output format?** Default is a chat summary. If the user asked
  for file output, set `write_to_file: true` (see Output section).
- **Any structural preferences?** Default is agent-determined structure. If the user
  specified a format, pass it through.

---

## Step 4: Dispatch subagents

Dispatch all three subagents in parallel. Pass each one:

- The full content of all files (or the staging path if using temp files)
- The relationship context (if multiple files)
- Any user-provided guidelines or goals
- The output mode (summary or file)
- Their specific reviewer persona (described below — do **not** use these labels in output)

Read `references/subagent-personas.md` for the detailed persona instructions to pass to
each subagent. Read `references/large-file-strategy.md` for instructions to pass to
subagents when any individual file is large enough to risk context limits.

**If either reference file is not accessible**, stop and tell the user: "The skill package
appears to be incomplete — one or more required reference files are missing. Please
reinstall the skill."

---

## Step 5: Collect and present results

Once all three subagents return:

### Default (chat summary)

Present four sections in the response:

1. **Review 1** — The skeptical reviewer's findings, summarized
2. **Review 2** — The generous reviewer's findings, summarized
3. **Review 3** — The balanced reviewer's findings, summarized
4. **Overall** — A synthesis that reconciles disagreements and leans toward
   actionable recommendations (see Output section)

Keep each review summary concise: the key points, not a full transcript. The overall
section should be the most substantive.

### File output mode

Write a more comprehensive document to the requested path (or to a user/project-approved
staging area if no path was given). Include:

- Full review from each subagent (not summarized, agent-determined structure unless
  user specified one)
- A synthesis section at the end

Then post a brief summary in chat and provide the file path.

---

## Output: Overall synthesis

The synthesis is not a fourth review. It is a meta-view that:

- Notes where the three reviews agree (amplify those points, they are robust)
- Reconciles disagreements (explain the tension; recommend a direction)
- Gives concrete, prioritized recommendations
- Reflects any user-provided goals or guidelines in its framing

The synthesis should be the most actionable part of the output.
