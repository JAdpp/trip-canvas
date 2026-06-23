# Character Consistency

Use this for recurring travelers, pets, mascots, couple/friend avatars, or generated character continuity.

## Priority

1. Use user-uploaded character reference images in the current request.
2. Use local private profile at `private/character-profile.local.yaml`, if present.
3. Use a generic public-safe traveler cast.

Do not ship or expose private character sheets in public Skill packages.

## Local Private Profile

Users may create:

```yaml
characters:
  - id: traveler_a
    display_name: "private name"
    identity_prompt: "face, hair, glasses, outfit family, age impression, body proportion"
    role: "main traveler / narrator / photographer / food lover"
    must_keep:
      - "round glasses"
      - "short black hair"
    avoid:
      - "changing age"
      - "different hairstyle"
    assets:
      - "assets/character-references/traveler-a-sheet.png"
  - id: traveler_b
    display_name: "private name"
    identity_prompt: "..."
    role: "companion / reaction partner"
    assets:
      - "assets/character-references/traveler-b-sheet.png"
```

## Public-Safe Cast

If no reference exists, use neutral generic travelers. Do not mention private names or distinctive private traits.

Example:

```text
Two generic cute young adult traveler avatars in East Asian sticker-comic style, one route/photo-oriented and one food/mood-oriented, consistent hairstyles and outfits across pages, small expressive chibi reactions, no proprietary character likeness.
```

## Consistency Checklist

For every page/prompt, specify:

- character ID.
- visual identity.
- outfit or outfit family.
- role in the scene.
- pose or action.
- emotional expression.
- which memory object they interact with.

## Character Scale

- In scrapbook pages, characters can be primary actors when the user wants comic diary style.
- In dense memory spreads, keep characters to 1-4 main moments per page.
- Do not let characters cover exact text, photo slots, tickets, or key artifacts.
