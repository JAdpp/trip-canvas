# Public Asset Policy

Use this when packaging, sharing, publishing, or open-sourcing this Skill.

## Principle

Open-source the workflow, not private memories or private visual identity.

## Public Package May Include

- `SKILL.md`
- workflow and prompt templates.
- visual language rules.
- editable object manifest rules.
- local GUI scripts and HTML templates that contain no private assets.
- generic character rules.
- public configuration schema.
- empty placeholder directories.

## Public Package Must Not Include

- private character sheets.
- real trip photos, ticket scans, hotel addresses, receipts, or chat screenshots.
- generated pages containing private people or private character IP.
- third-party style reference images unless licensed for redistribution.
- API keys, cookies, location history exports, or account data.

## Recommended Private Paths

```text
private/character-profile.local.yaml
assets/character-references/
assets/source-materials/
assets/style-references/
```

Use `.gitignore` to keep private paths out of public repositories.

## Public Prompt Behavior

When users provide no private references, use generic traveler avatars and text-only style rules. Do not imply private assets exist.
