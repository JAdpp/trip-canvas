# Authoring Workflow

Use this for full creation requests. The goal is a controllable agent-led authoring process, not a one-shot image prompt.

## Flow

`materials -> sufficiency check -> focused questions or labeled defaults -> memory extraction -> page form -> editable object manifest -> visual route -> style/character bible -> component draft -> low-fidelity layout/object-map preview -> confirmation -> prompt pack, direct generation, or GUI project -> QA -> revision contract`

## Step 0: Decide How Much To Ask

Do not require the user to already know the final scrapbook design. Many users will only provide an itinerary and photos.

- If the brief is clear enough, proceed with labeled default assumptions.
- If important choices are missing, ask up to three focused questions at a time.
- If the user explicitly asks for immediate generation and the materials are sufficient, do not force a confirmation round.
- If the user asks for full manual control, move to the GUI workflow.

High-value questions usually concern visual route, character/persona treatment, page count/aspect ratio, must-keep captions, and whether to generate components first or the final page directly.

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

## Step 4: Choose Visual Route And Plan Page Zones

Choose the route that best fits the materials before writing final prompts: East Asian sticker comic, kawaii sticker journal, black-and-white cartoon doodle, map infographic scrapbook, polaroid photo collage, watercolor travel journal, vintage ephemera scrapbook, urban sketch journal, minimalist line journal, comic book travel page, mixed-media collage, or a hybrid.

For each page, specify:

- title/date zone.
- anchor scene zone.
- memory material slots.
- caption/speech zone.
- character sticker or comic panel zone.
- decorative sticker/tape/stamp zone.
- fact anchor zone for times, tickets, place names, or route fragments.

## Step 5: Produce The Contract And Component Draft

Always produce an editable object manifest before final prompts. Each prompt should be traceable back to object IDs.

Also draft the visible components before final image generation:

- source photo or photo-slot objects.
- generated scene panels or mini-comic panels.
- character stickers or avatar appearances.
- text cards, title/date badges, speech bubbles, and exact text list.
- decorative stickers, stamps, tape, maps, tickets, and background paper.

When the user wants staged control, present these components for confirmation or revision before generating the final scrapbook page.

## Step 6: Generate A Low-Fidelity Planning Preview

After the page form, zones, visual route, and object manifest are clear, create a visual planning preview when an image-generation tool/API is available. This preview is part of planning, not the final artwork, so do not ask the user to approve final generation before making it unless they opted out of previews.

Generate one concise planning-board image by default:

- left side: rough page layout sketch showing the chosen page format, major zones, relative scale, flow, and visual rhythm.
- right side or overlay layer: editable object map with visible IDs such as `P1-IMG1`, `P1-TXT1`, `P1-CHR1`, `P1-PNL1`, `P1-STK1`, and `P1-BG1`.
- style: low-fidelity scrapbook wireframe, loose pencil/marker sketch, colored blocks, tape outlines, arrows, dashed boxes, placeholder thumbnails, no polished final art.
- text: large object IDs only; keep exact user-facing captions outside the preview when text fidelity matters.
- privacy: use generic silhouettes or blank photo placeholders unless the user explicitly provided and approved references for preview use.

Use this prompt shape for the preview:

```text
Create a low-fidelity planning-board preview for a [aspect ratio] travel scrapbook page. This is not final artwork. Show a rough scrapbook layout sketch plus an editable object map. Include large readable object IDs: [ID list]. Use simple placeholder photo frames, comic panel boxes, title/date zone, caption cards, map/ticket scraps, decorative sticker slots, arrows, tape outlines, and paper texture blocks. Keep the composition readable and useful for layout review. Do not render exact long captions; keep text labels short and large. Do not invent real ticket details or private faces.
```

If image generation is unavailable, output this preview prompt and a compact text fallback. Do not stop at a pure prose layout description when image generation is available.

## Step 7: Generate, Export, Or Prepare Iteration

After the component draft is clear, choose the next step:

- generate the final scrapbook page when the user requests direct generation and an image tool/API is available.
- generate component drafts first when the user wants to inspect stickers, characters, or photo slots.
- export a prompt pack when direct generation is unavailable or the user wants to use another tool.
- export or launch a GUI project when the user wants full manual control.

End each prompt pack with revision instructions:

- regenerate a whole page only when composition fails.
- replace `IMG/TXT/CHR/STK/PNL/BG` objects when the layout is mostly good.
- keep liked regions explicit, for example `preserve P1-CHR1, P1-IMG3, title zone, and lower-right food cluster`.
