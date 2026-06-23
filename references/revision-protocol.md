# Revision Protocol

Use this when the user wants to modify an existing generated page, uploaded image, or prompt pack.

## First Principle

Do not redesign a liked page when the user asks for a local change. Preserve the successful baseline and target only the relevant object(s).

## Revision Steps

1. Identify the page and target object ID.
2. If no manifest exists, infer one from visible regions.
3. State what will be preserved.
4. State what will change.
5. Write a localized edit instruction.
6. Warn if the requested change is likely to disturb text, character consistency, or composition.

## Local Edit Instruction Pattern

```text
Keep the same overall scrapbook layout, page ratio, background paper, title/date zone, object positions, character identity, text cards, and surrounding stickers. Replace only [Object ID] ([object label]) with [new content]. Preserve its approximate size, border/tape style, tilt, label position, and spacing. Do not change [explicit preserved objects].
```

## Common Revision Types

### Replace Photo Or Visual

Target `IMG`. Keep slot border, tilt, label, and nearby text.

### Fix Chinese Text

Target `TXT`. Provide exact corrected text. If image generation may distort text, recommend external overlay or design-tool edit.

### Adjust Character

Target `CHR`. Preserve identity; change only pose, expression, outfit detail, or interaction.

### Add Sticker Or Caption

Target `STK` or `TXT`. Check it will not cover memory materials.

### Change Style

If style change is global, ask whether to preserve layout. If local, target background/sticker/panel objects only.

## When To Regenerate Whole Page

Regenerate only when:

- composition is fundamentally wrong.
- character identity is globally inconsistent.
- text is unusable across most of the page.
- page form is wrong for the user's intention.
- user explicitly asks for a redesign.
