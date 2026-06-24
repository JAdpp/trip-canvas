# Prompt Template

Use this for final page prompts or component-level prompts after the memory structure, object manifest, visual route, and component draft are clear. Fill every bracket with page-specific content. Do not write "same as above".

```text
Create a [aspect ratio] memory-first travel scrapbook / visual journal page using the selected visual route: [East Asian sticker comic / kawaii sticker journal / black-and-white cartoon doodle / map infographic scrapbook / polaroid photo collage / watercolor travel journal / vintage ephemera scrapbook / urban sketch journal / minimalist line journal / comic book travel page / mixed-media collage / hybrid]. The page should feel handmade, layered, object-rich, and memory-first, not like a clean travel itinerary board or generic photo book.

Page concept:
[Page title, date, city/place, emotional theme, and chosen form: daily scrapbook / multi-day spread / mini-comic / hybrid scrapbook-comic.]

Visual route:
[Name the route and explain why it fits the user's materials. Keep this stable across related pages unless the user asks for a style change.]

Memory scenes:
[List 3-8 memory scenes with place, event, emotion, and source material. Preserve exact user facts.]

Layout:
[Describe title/date zone, anchor scene, supporting clusters, comic panels, photo/ticket/map/food slots, character positions, caption zones, and decorative sticker/tape/stamp areas.]

Editable object slots:
[List object IDs and roles, e.g. P1-IMG1 city park night photo, P1-TXT1 title "DAY 1 城市乐园夜游", P1-CHR1 traveler pair smiling, P1-PNL1 roller-coaster reaction panel.]

Character consistency:
[Use provided/local character references if available. Otherwise use public-safe generic traveler avatars. Specify identity, outfit family, pose, expression, and memory object interaction.]

Visual style:
[Write route-specific rendering language. Examples: East Asian sticker comic with light manga diary details; kawaii sticker journal with soft rounded icons; black-and-white cartoon doodle with thick marker lines, simple icons, and no grey wash; map infographic with numbered memory stops; polaroid photo collage with taped instant-photo frames; watercolor travel journal with soft washes; vintage ephemera scrapbook with aged paper and stamps; urban sketch journal with loose pen-and-wash architecture notes; minimalist line journal with sparse accents. Keep scrapbook cues such as white-border slots, tape, torn paper, notebook paper, stamp marks, handwritten labels, and legible composition.]

Text handling:
Use large readable handwritten Chinese for intentional text. Keep labels short. Exact text to render: [list exact titles, captions, labels, speech bubbles]. Avoid tiny paragraphs or garbled small text.

Negative constraints:
Do not make a route-first travel guide page unless explicitly requested. Do not invent bookings, place facts, or personal events. Do not change character identity. Do not cover important photos, tickets, captions, or object slots. Do not use proprietary character likenesses unless provided by the user.
```

## Prompt Assembly Rules

- Put exact text in a separate list before or after the prompt when text correctness matters.
- Use object IDs in the page plan and in the prompt so later revisions can target them.
- If the user wants staged control, write separate prompts for character stickers, scene panels, photo-slot backgrounds, text-card layouts, or decorative sticker sheets before the final page prompt.
- For generated model prompts, describe visual text as large labels and keep the precise text list outside the image when possible.
- For multi-day spreads, keep each day visually separated while sharing one style bible.
- For mini-comics, include panel count and panel purpose.
- For photo replacement workflows, ask the image model to leave clear, separate sticker slots.
- For style diversity, explicitly name the visual route; do not let every prompt drift back to colorful chibi manga or any single default style.
