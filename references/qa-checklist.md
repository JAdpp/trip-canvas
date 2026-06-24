# QA Checklist

Use this before finalizing page plans, prompts, generated-image critiques, or revision instructions.

## Memory And Fact QA

- User-provided dates, places, captions, tickets, and names are preserved.
- Suggested additions are labeled `建议补充`.
- Missing materials are labeled `待补充`.
- External factual claims that may change are verified or labeled `待核实`.
- The page does not invent personal events.

## Visual QA

- The output reads as the selected scrapbook visual route, not a clean itinerary board or generic photo book.
- The route is explicit: East Asian sticker comic, kawaii sticker journal, black-and-white cartoon doodle, map infographic scrapbook, polaroid photo collage, watercolor travel journal, vintage ephemera scrapbook, urban sketch journal, minimalist line journal, comic book travel page, mixed-media collage, or hybrid.
- If the route is black-and-white cartoon doodle, it uses simple marker-like line art and avoids grayscale detailed manga or realistic shading.
- Memory anchor scenes are more prominent than route logistics.
- Photos/tickets/objects have clear replaceable slots.
- Characters support memory scenes and remain consistent.
- Text labels are short and large enough for image models.
- Decorative stickers do not cover important objects.

## Editability QA

- Each page has a manifest.
- Object IDs are stable and unique.
- Revision instructions name what is preserved and what changes.
- The prompt does not flatten every element into an inseparable illustration.

## Output QA

- New-creation output uses the required section order from `SKILL.md`.
- If the user is non-expert, the workflow asks only high-impact missing questions and otherwise proceeds with labeled defaults.
- Component drafts are separated before final page generation when the user wants staged control.
- If direct image generation is requested and available, the output does not stop at prompt export.
- Revision-only output avoids unnecessary full regeneration.
- The user can copy prompts directly.
- The user can point to object IDs for the next edit.
