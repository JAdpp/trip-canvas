---
name: sticker-travel-scrapbook
description: "Use when the user wants to create, plan, revise, evaluate, or interactively edit East Asian sticker-style travel scrapbook pages, visual travel diaries, dense collage journals, cute itinerary-memory pages, mini-comic travel handbooks, black-and-white cartoon doodle journals, map-infographic scrapbook pages, or polaroid photo collage travel journals from photos, itinerary text, tickets, notes, screenshots, character references, or an existing generated scrapbook image. Also use when the user asks for a GUI, canvas, local app, object editor, project JSON, prompt-pack exporter, or local web workbench for travel scrapbook authoring. Specializes in memory-first multimodal authoring: guiding non-expert users from messy materials through focused questions, visual-route choices, component/object drafts, confirmation, image prompts or direct image generation when available, local GUI control, and localized revisions such as replacing one sticker/photo/text card/panel without redesigning the whole page."
---

# Sticker Travel Scrapbook

## Mission

Turn travel materials into an agent-led, editable East Asian sticker-style scrapbook authoring workflow. Do not stop at being a prompt generator: guide users from itinerary/photos/notes to memory structure, style and character decisions, component/object drafts, prompts, optional image generation, and later revisions. Prioritize personal memory-making, visual play, sticker collage, character continuity, visual-route choice, and local editability over route-first travel-guide readability.

Use this Skill for:

- Guiding non-expert users from travel photos, itineraries, notes, tickets, routes, chat fragments, or rough memory descriptions into a finished scrapbook image workflow.
- Creating scrapbook prompt packs when the user wants exportable prompts instead of direct generation.
- Converting an existing generated scrapbook image into an editable plan and object manifest.
- Revising one region of a generated page while preserving the rest of the layout, characters, text, and style.
- Choosing among visual routes such as cute sticker comic, black-and-white cartoon doodle, map-infographic scrapbook, polaroid photo collage, and hybrid variants.
- Designing a workflow or GUI concept for sticker-style travel memory authoring.

## Core Stance

Do not treat the output as a normal travel diary, photo book, itinerary board, or generic collage poster. Treat it as a handmade-feeling visual memory artifact:

`real trip materials -> sufficiency check -> memory scenes -> page/story structure -> editable object manifest -> visual route + style/character bible -> component draft -> user confirmation -> image prompts, direct generation, GUI project, or local revision instructions`

The page may include route facts, weather, tickets, hotel, or maps, but these are supporting anchors. The main subject is the user's remembered experience, scenes, moods, companions, food, objects, jokes, and small visual episodes.

## Load References

- Load `references/authoring-workflow.md` for full agent-led creation, from materials to questions, components, prompts, generation, and revision.
- Load `references/memory-structure.md` when parsing travel photos, itinerary text, notes, tickets, screenshots, or rough memories.
- Load `references/east-asian-visual-language.md` before page planning or prompt writing.
- Load `references/comic-panel-patterns.md` when the user asks for mini-comic, manga-style moments, character scenes, or multi-panel storytelling.
- Load `references/character-consistency.md` when the user provides character references, asks for recurring travelers, mascots, pets, couple/friend avatars, or wants identity consistency.
- Load `references/editable-object-manifest.md` whenever generating page plans, prompts, or revision instructions.
- Load `references/prompt-template.md` when writing final image prompts.
- Load `references/revision-protocol.md` when the user wants to revise an existing page, replace a visual, fix text, preserve layout, or regenerate only part of a page.
- Load `references/qa-checklist.md` before finalizing prompts, generated-image critique, or revision instructions.
- Load `references/gui-workflow.md` when the user asks for an interface, GUI, canvas, local app, object editor, or wants to inspect/edit a project interactively.
- Load `references/public-asset-policy.md` when the user asks to package, share, publish, or open-source the Skill or related assets.
- Load `references/default-config.yaml` when the user asks about defaults, modes, aspect ratios, GUI behavior, or project JSON.

## Workflow

### 0. Choose Interaction Mode

Default to `agent-led guided workflow` when the user provides travel materials but does not know exactly how the page should look. In this mode, read the materials, infer a reasonable first draft, and ask only the smallest useful set of follow-up questions.

Use `direct execution` when the user already gives clear style, character, layout, text, and generation instructions. Do not slow them down with unnecessary questions.

Use `GUI control mode` when the user asks for GUI, canvas, local app, object editor, manual control, or project JSON. The GUI gives the user direct control over materials, pages, objects, prompts, and optional API-backed image generation.

If key decisions are missing, ask up to three focused questions at a time, such as visual route, character/persona treatment, page count/aspect ratio, must-keep text, or whether to generate the final image now. If the missing choice is low-risk, make a labeled default assumption and continue.

### 1. Normalize Inputs

Accept messy materials: pasted itinerary, OCR text, screenshots, generated scrapbook images, photos, ticket stubs, map fragments, restaurant notes, museum labels, chats, voice-transcribed notes, or casual descriptions.

Preserve user-provided facts exactly. Do not rewrite dates, place names, flight/train numbers, ticket times, hotel names, or user-written captions unless the user asks.

If a fact is missing, mark it as `待补充`. If adding optional visual or factual suggestions, mark them as `建议补充`, not confirmed memory.

### 2. Build A Memory Structure

Create a compact memory table with:

`Day / Place / Memory Scene / Materials / Emotion / Visual Motifs / Text Snippets / Fact Anchors / Missing Items`

Keep route order visible only when it helps the memory artifact. For scrapbook pages, a day can be organized by highlight, mood, object, or comic scene rather than strict chronology.

### 3. Choose Page Form

Pick a form based on materials and user intent:

- `single highlight page`: one core place, meal, museum, performance, or ride.
- `daily scrapbook page`: one day with several memory clusters.
- `multi-day spread`: several days in a wide collage or scrolling page.
- `mini-comic page`: 3-8 panels around funny, emotional, or character-heavy moments.
- `hybrid scrapbook-comic page`: anchor images plus small character panels and speech bubbles.

Default to the user's existing image ratio when revising an uploaded/generated image. For new work, choose the most natural format: 9:16 for phone pages, 16:9 or 3:1 for multi-day spreads, square for social-card style pages, and A4/A5 for printable handbooks.

### 4. Create An Editable Object Manifest

For every planned page, assign stable IDs to replaceable objects:

- `P{page}-IMG{n}`: photo, landmark image, food image, ticket scan, map fragment.
- `P{page}-TXT{n}`: title, caption, note, checklist, date label, speech bubble text.
- `P{page}-CHR{n}`: traveler, companion, pet, mascot, or recurring avatar.
- `P{page}-STK{n}`: decorative sticker, stamp, tape, icon, doodle, heart, sparkle, weather mark.
- `P{page}-PNL{n}`: mini-comic panel or scene vignette.
- `P{page}-BG{n}`: background paper, city skyline, texture, or section backdrop.

Never flatten the plan into one undifferentiated image. The manifest is the contract for later local edits.

### 5. Plan Visual Route, Style, And Character Consistency

Select a visual route before writing prompts. Do not default every page to cute chibi comic rendering.

Useful visual routes include:

- `cute sticker comic`: colorful chibi or light manga travel diary, strong character moments, speech bubbles, food and souvenir stickers.
- `black-and-white cartoon doodle`: simple black marker line art, rounded cartoon shapes, icons, blank caption cards, and generous white space; do not use grayscale detailed manga, grey wash, realistic hatching, or a full illustration merely converted to black and white.
- `map infographic scrapbook`: route map as the main object, numbered stops, photo slots, transport icons, stamps, concise labels, suitable when place sequence or geography matters.
- `polaroid photo collage`: instant-photo frames, taped snapshots, film grain, pressed flowers, receipts or map scraps, minimal character presence, suitable when real photos should dominate.
- `hybrid`: combine a main route above with small comic panels, sticker objects, or photo slots when the memory needs both structure and emotion.

If user-provided character/style references exist, use them as the top priority. Otherwise define a public-safe generic style bible for the selected visual route. Keep character traits consistent across pages when characters are used: face shape, hair, glasses, clothing family, body proportion, pose vocabulary, and role in the story.

Do not use copyrighted/proprietary character names, likenesses, or distinctive traits unless the user supplied them and explicitly wants that reference used.

### 6. Prepare Components, Prompts, Or Generation

For new pages, produce a staged authoring result rather than only a prompt:

1. `【1. 旅行记忆结构化】`
2. `【2. 缺失信息与默认假设】`
3. `【3. 页面形式与版式建议】`
4. `【4. 可编辑对象清单与组件草案】`
5. `【5. 风格、人物形象与文字清单】`
6. `【6. 生图 prompt / 组件 prompt】`
7. `【7. 下一步确认】`

In the component draft, separate the final page into replaceable units: photo slots, generated scene panels, character stickers, decorative stickers, map/ticket scraps, text cards, speech bubbles, and background paper. If the user wants staged control, ask them to confirm or revise these components before final page generation.

When an image-generation tool or API is available and the user asks for direct generation, use it after the component plan is clear. If the user has not explicitly asked to generate immediately, ask whether to generate component drafts, generate the final scrapbook page, export a prompt pack, or open the GUI project.

For revision-only requests, do not redesign the whole page. Identify the target object ID or ask for the smallest missing identifier. Keep successful regions stable and produce a localized replacement instruction.

### 7. Use The Local GUI When Requested

When the user asks for GUI, interface, canvas, local app, object editor, or interactive project review, load `references/gui-workflow.md` and use `scripts/server.py`.

Default launch command, blank project:

```powershell
python "C:\Users\74783\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

The GUI is a local web workbench and manual control mode for materials, pages, editable object IDs, object inspection, JSON import/export, prompt-pack export, localized revision prompt generation, and optional API-backed image generation. It complements the agent-led workflow: Codex can create or revise a project plan conversationally, while the GUI lets the user inspect and directly edit the same structure.

If `OPENAI_API_KEY` is set before launching the server, the GUI can call the OpenAI Images API through `/api/generate-image` and save generated images beside the project JSON. Without the key, the GUI still builds/export prompts and shows a clear "API key not configured" status.

## Hard Rules

- Optimize for personal memory, sticker collage, and visual authorship before travel-guide utility.
- Do not reduce full creation requests to one prompt. Use guided questions, object/component planning, confirmation, and generation/export steps.
- Preserve user facts and user-written captions unless explicitly asked to revise them.
- Keep every page locally editable through stable object IDs.
- Keep characters consistent, but do not let character art erase memory materials.
- Use large, readable Chinese labels for intentional text; avoid tiny paragraph text inside image prompts.
- Treat AI-generated Chinese text as high-risk; provide a text overlay plan or separate exact text list when correctness matters.
- Do not invent real bookings, ticket details, place facts, or personal events.
- When using external facts that may change, verify live or mark as `待核实`.
- For existing generated images, preserve the user's liked composition unless they ask for a redesign.
- Keep public Skill logic separate from private character sheets, private trip photos, real tickets, and third-party style references.
- If using the GUI, keep user materials local and avoid saving private photos into public skill assets.
