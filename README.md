# Sticker Travel Scrapbook Skill

`sticker-travel-scrapbook` is a Codex Skill for creating, planning, revising, and interactively editing East Asian sticker-style travel scrapbook pages and mini-comic travel diaries.

It is designed for memory-first visual authoring rather than route-first travel guides. The Skill helps Codex turn travel photos, notes, tickets, screenshots, character references, and generated scrapbook images into structured memory scenes, editable object manifests, image prompts, and localized revision instructions.

## What It Does

- Structures travel materials into scrapbook-ready memory scenes.
- Plans East Asian sticker-style layouts and mini-comic pages.
- Creates editable object manifests with stable IDs such as `P1-IMG1`, `P1-TXT1`, `P1-CHR1`, `P1-STK1`, and `P1-PNL1`.
- Maintains character and style consistency across pages.
- Generates copyable image prompts.
- Supports localized revision prompts such as replacing one image slot without redesigning the full page.
- Includes a local web GUI for project editing, prompt building, and optional API-backed image generation.

## Repository Layout

Recommended GitHub layout:

```text
sticker-travel-scrapbook-skill/
  README.md
  sticker-travel-scrapbook/
    SKILL.md
    agents/
      openai.yaml
    scripts/
      server.py
    assets/
      gui/
        index.html
        blank-project.json
        demo-project.json
    references/
      authoring-workflow.md
      memory-structure.md
      east-asian-visual-language.md
      comic-panel-patterns.md
      character-consistency.md
      editable-object-manifest.md
      prompt-template.md
      revision-protocol.md
      qa-checklist.md
      gui-workflow.md
      public-asset-policy.md
      default-config.yaml
      character-profile.example.yaml
```

Keep private travel photos, character sheets, ticket scans, hotel details, and generated personal images out of the public repository.

## Installation

Copy the `sticker-travel-scrapbook` folder into a Codex skills directory.

On Windows, a user-level location is typically:

```powershell
C:\Users\<you>\.codex\skills\sticker-travel-scrapbook
```

If Codex does not detect the Skill immediately, restart Codex or start a new thread.

## Basic Usage In Codex

Explicitly invoke the Skill:

```text
Use $sticker-travel-scrapbook。

我想做一张东亚粘贴式旅行手帐/小漫画页面，不是规整旅行攻略。

旅行内容：
6月19日，上海城市乐园夜游，端午节，园区周年庆。重点记忆包括：夜间灯光、花车巡游、过山车、烟花表演。整体情绪是兴奋、热闹、庆祝感。

请输出：
1. 旅行记忆结构化
2. 页面形式与版式建议
3. 可编辑对象清单，使用 P1-IMG1 / P1-TXT1 / P1-CHR1 / P1-PNL1 这类 ID
4. 风格与角色设定
5. 可复制到图像模型的生图 prompt
6. 如果后续只想替换烟花区域，应该怎么局部修改
```

Revision example:

```text
Use $sticker-travel-scrapbook。

这张手帐整体满意，只想把 P3-IMG2 的手机合影区域换成我上传的真实照片。
请保留人物、标题、文物卡片和整体版式，只给我局部修改 prompt。
```

## Local GUI

The Skill includes a lightweight local GUI. It starts from a blank project by default.

Launch it with:

```powershell
python "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

Then open the printed local URL, usually:

```text
http://127.0.0.1:8765/
```

The GUI supports:

- travel brief and style-bible editing.
- material notes and image previews.
- page and object creation.
- editable object IDs.
- current-page image prompt generation.
- project JSON import/export.
- generated-image gallery when API generation is enabled.

## Optional GUI Image Generation

The GUI can call the OpenAI Images API if `OPENAI_API_KEY` is set in the server environment before launch:

```powershell
$env:OPENAI_API_KEY="sk-..."
python "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

Without `OPENAI_API_KEY`, the GUI still builds and exports prompts, but direct image generation will show a clear API-key warning.

## Demo Project

To start with the bundled Shanghai travel scrapbook demo instead of a blank project:

```powershell
python "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\demo-trip-project.json" --demo
```

Inside the GUI, the `载入示例` button can also load the demo.

## Privacy

Do not commit:

- private character references.
- real travel photos.
- ticket scans or hotel details.
- personal location/history exports.
- generated images containing private people or private IP.
- API keys or cookies.

The public Skill should contain reusable workflow rules, prompt templates, GUI code, and empty/private-safe placeholders only.

## Validation

Validate the Skill with the built-in skill creator validator:

```powershell
$env:PYTHONUTF8='1'
python "C:\Users\<you>\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook"
```

Expected output:

```text
Skill is valid!
```

## Current Boundary

This is a Skill plus local GUI prototype. The GUI can either:

- build/export prompts for Codex or another image tool, or
- call the OpenAI Images API directly when `OPENAI_API_KEY` is configured.

It does not yet implement a full plugin/MCP bridge where a GUI button automatically wakes Codex and makes Codex call its internal image tool.
