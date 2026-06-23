# Memory Structure

Use this when parsing travel materials into scrapbook-ready content.

## Memory Table Contract

Output a compact table:

| Day | Place | Memory Scene | Materials | Emotion | Visual Motifs | Text Snippets | Fact Anchors | Missing Items |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Extraction Rules

- Preserve exact user-provided dates, place names, captions, ticket details, and personal wording.
- Separate confirmed memories from suggested decoration.
- Treat photos and ticket stubs as evidence materials; treat model-generated art as style reference unless the user says it is factual.
- Record emotional tone explicitly: excited, tired, moved, cozy, funny, rushed, quiet, romantic, nostalgic, surprised.
- Capture "small things" because scrapbook value often lives in them: a drink, stamp, plush toy, signboard, hand pose, queue, weather, quote, facial expression, receipt, bag, souvenir.

## Memory Scene Types

- arrival / departure.
- theme park / ride / parade / fireworks.
- museum / exhibition / artifact close-up.
- food / cafe / bar / dinner table.
- city walk / street / skyline / transport.
- hotel / rest / packing / late night.
- souvenir / ticket / stamp / receipt.
- companion moment / pet / mascot / joke.

## Fact And Invention Boundary

Use labels:

- `已提供`: explicitly provided by user or visible in source material.
- `可推断`: strongly inferable from provided materials; say what it was inferred from.
- `建议补充`: optional content proposed by the agent.
- `待补充`: necessary but missing.
- `待核实`: external real-world fact that needs lookup.

Do not turn `建议补充` into a memory claim.
