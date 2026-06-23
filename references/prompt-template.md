# Prompt Template

Use this for final image prompts. Fill every bracket with page-specific content. Do not write "same as above".

```text
Create a [aspect ratio] East Asian sticker-style travel scrapbook / mini-comic page in Chinese. The page should feel handmade, dense, cute, layered, and memory-first, not like a clean travel itinerary board or generic photo book.

Page concept:
[Page title, date, city/place, emotional theme, and chosen form: daily scrapbook / multi-day spread / mini-comic / hybrid scrapbook-comic.]

Memory scenes:
[List 3-8 memory scenes with place, event, emotion, and source material. Preserve exact user facts.]

Layout:
[Describe title/date zone, anchor scene, supporting clusters, comic panels, photo/ticket/map/food slots, character positions, caption zones, and decorative sticker/tape/stamp areas.]

Editable object slots:
[List object IDs and roles, e.g. P1-IMG1 city park night photo, P1-TXT1 title "DAY 1 城市乐园夜游", P1-CHR1 traveler pair smiling, P1-PNL1 roller-coaster reaction panel.]

Character consistency:
[Use provided/local character references if available. Otherwise use public-safe generic traveler avatars. Specify identity, outfit family, pose, expression, and memory object interaction.]

Visual style:
East Asian 手帐 collage, cute sticker scrapbook, light manga diary details, white-border cutout photos, washi tape, torn paper, grid/notebook paper, ticket stubs, stamp marks, handwritten Chinese labels, short speech bubbles, small hearts/stars/check marks, warm varied colors matched to the trip, high-density but legible composition.

Text handling:
Use large readable handwritten Chinese for intentional text. Keep labels short. Exact text to render: [list exact titles, captions, labels, speech bubbles]. Avoid tiny paragraphs or garbled small text.

Negative constraints:
Do not make a route-first travel guide page unless explicitly requested. Do not invent bookings, place facts, or personal events. Do not change character identity. Do not cover important photos, tickets, captions, or object slots. Do not use proprietary character likenesses unless provided by the user.
```

## Prompt Assembly Rules

- Put exact text in a separate list before or after the prompt when text correctness matters.
- Use object IDs in the page plan and in the prompt so later revisions can target them.
- For generated model prompts, describe visual text as large labels and keep the precise text list outside the image when possible.
- For multi-day spreads, keep each day visually separated while sharing one style bible.
- For mini-comics, include panel count and panel purpose.
- For photo replacement workflows, ask the image model to leave clear, separate sticker slots.
