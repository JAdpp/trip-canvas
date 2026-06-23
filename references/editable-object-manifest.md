# Editable Object Manifest

Use this for every page plan, prompt pack, and localized revision. It is the core mechanism that turns a flat generated image into a controllable authoring process.

## Object ID Scheme

- `P{page}-IMG{n}`: photo, food, landmark, ticket scan, receipt, map fragment, generated scene image.
- `P{page}-TXT{n}`: title, date, caption, checklist, note, speech bubble, label.
- `P{page}-CHR{n}`: traveler, companion, pet, mascot, recurring avatar.
- `P{page}-STK{n}`: sticker, tape, stamp, doodle, icon, heart, sparkle, weather mark.
- `P{page}-PNL{n}`: comic panel or vignette.
- `P{page}-BG{n}`: paper texture, backdrop, city skyline, section background.

## Manifest Table

For each page, output:

| Object ID | Type | Page Area | Content | Source | Editable Rule |
| --- | --- | --- | --- | --- | --- |

Use `Source` values:

- `user-provided`
- `visible in uploaded image`
- `generated suggestion`
- `needs user material`
- `needs verification`

## Editable Rules

- Photo slots should keep border, tilt, approximate size, and label position during replacement.
- Text slots should have an exact text list outside the image prompt when correctness matters.
- Character slots should keep identity and role stable even if pose changes.
- Sticker slots can be regenerated more freely, but should not cover memory objects.
- Comic panel slots can be replaced panel-by-panel; do not rewrite the whole page unless requested.
- Background slots should stay stable during local edits unless the user asks for a style redesign.

## Revision Targeting

If the user says "改这里", infer the likely object from context. If ambiguous between multiple objects, ask one concise question or present the top two candidate object IDs.

For existing images without a manifest, first create an inferred manifest from visible regions, then target the revision.
