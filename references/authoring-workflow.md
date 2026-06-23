# Authoring Workflow

Use this for full creation requests. The goal is a controllable authoring process, not a one-shot image prompt.

## Flow

`materials -> memory extraction -> page form -> editable object manifest -> style/character bible -> prompt pack -> QA -> revision contract`

## Step 1: Inventory Materials

Group all inputs into:

- itinerary facts: day, place, route, transport, hotel, tickets, times.
- memory materials: photos, screenshots, receipts, ticket stubs, maps, souvenirs, chat fragments.
- subjective notes: mood, surprise, fatigue, jokes, quotes, food reactions, "must keep" details.
- character/style references: people, pets, mascots, previous generated pages, preferred art style.
- constraints: aspect ratio, number of pages, language, whether to generate images now.

If material is missing, write `待补充`. Do not fabricate personal memories.

## Step 2: Extract Memory Scenes

Convert raw material into scenes. A scene is not just a location; it combines:

`where + what happened + who appeared + what object/photo proves it + what feeling or caption belongs there`

Good scene examples:

- `Night festival`: illuminated skyline, crowd silhouettes, celebration badge, excited final note.
- `Museum peach vase`: artifact photo, phone close-up, "一起合影" bubble, quiet awe.
- `Bar movie night`: bottle wall, dog stickers, ticket card, warm after-movie note.

## Step 3: Select Page Form

Use the form that best preserves memory density:

| Form | Use when | Output tendency |
| --- | --- | --- |
| Single highlight page | one place or event dominates | large anchor image plus labels/stickers |
| Daily scrapbook page | one day has several episodes | dense collage with 3-6 memory clusters |
| Multi-day spread | travel has a sequence users want compared | wide or long page with day columns |
| Mini-comic page | emotional/funny/character actions matter | panels, speech bubbles, reaction stickers |
| Hybrid scrapbook-comic | user wants both photos and character scenes | anchor collage plus 2-4 comic vignettes |

## Step 4: Plan Page Zones

For each page, specify:

- title/date zone.
- anchor scene zone.
- memory material slots.
- caption/speech zone.
- character sticker or comic panel zone.
- decorative sticker/tape/stamp zone.
- fact anchor zone for times, tickets, place names, or route fragments.

## Step 5: Produce The Contract

Always produce an editable object manifest before final prompts. Each prompt should be traceable back to object IDs.

## Step 6: Prepare Iteration

End each prompt pack with revision instructions:

- regenerate a whole page only when composition fails.
- replace `IMG/TXT/CHR/STK/PNL/BG` objects when the layout is mostly good.
- keep liked regions explicit, for example `preserve P1-CHR1, P1-IMG3, title zone, and lower-right food cluster`.
