# GUI Workflow

Use this when the user asks for an interface, GUI, canvas, local app, object editor, or interactive project review.

## What The GUI Does

The bundled GUI is a local web workbench for the Skill's authoring contract:

- start from a blank project by default.
- manage a project title and style bible.
- add material notes or image previews.
- inspect pages and scrapbook objects.
- create and edit object IDs using the `IMG/TXT/CHR/STK/PNL/BG` scheme.
- build page-level image-generation prompts.
- call the OpenAI Images API from the GUI when `OPENAI_API_KEY` is configured in the server environment.
- import/export project JSON.
- export a prompt pack markdown file.

It is not a full Photoshop/Figma replacement. Treat it as a generation workbench: structure materials, create editable object slots, generate prompts, call an image API when configured, and keep generated results linked to the project.

## Launch Command

From a workspace folder where the project JSON should live:

```powershell
python "C:\Users\74783\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

Optional arguments:

```powershell
python "C:\Users\74783\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --host 127.0.0.1 --port 8765 --project ".\my-trip-project.json"
```

The server automatically moves to the next available port if the preferred port is occupied.

To start with the bundled Shanghai demo instead of a blank project when the project file does not exist:

```powershell
python "C:\Users\74783\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\demo-trip-project.json" --demo
```

To enable GUI image generation, set `OPENAI_API_KEY` before launching the server:

```powershell
$env:OPENAI_API_KEY="sk-..."
python "C:\Users\74783\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

## Runtime Files

- `scripts/server.py`: local HTTP server using only Python standard library.
- `assets/gui/index.html`: single-page GUI.
- `assets/gui/blank-project.json`: blank default project.
- `assets/gui/demo-project.json`: manually loadable Shanghai demo project.

## Typical Use

1. Start the GUI with `scripts/server.py`.
2. Open the printed local URL.
3. Write the travel brief and style bible.
4. Add or import travel materials.
5. Add pages and editable objects.
6. Build the current-page image prompt.
7. Click `通过 API 生图` when `OPENAI_API_KEY` is configured, or export the prompt for Codex/another image tool.
8. Export JSON to preserve the project state.

## Agent Behavior

When the user asks Codex to launch the GUI, start the server and provide the local URL. If starting a background process on Windows, use `Start-Process` with `-WindowStyle Hidden`. Verify the URL with a quick HTTP request before reporting it.

If the user expects direct image generation, check whether `OPENAI_API_KEY` is configured. If it is absent, explain that the GUI can still build/export prompts but direct API generation requires the key in the server environment.

When the user asks for GUI files without launching, point to:

```text
assets/gui/index.html
scripts/server.py
```

## Privacy

Do not store private travel photos, real ticket scans, hotel addresses, or character sheets inside public skill assets. Use project JSON in the user's workspace or private local folders.
