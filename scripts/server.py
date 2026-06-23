#!/usr/bin/env python3
"""Local GUI server for the sticker-travel-scrapbook skill.

This intentionally uses only the Python standard library so the GUI can run
without npm, Flask, or other runtime dependencies.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import socket
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen


SKILL_ROOT = Path(__file__).resolve().parents[1]
GUI_ROOT = SKILL_ROOT / "assets" / "gui"
DEMO_PROJECT = GUI_ROOT / "demo-project.json"
BLANK_PROJECT = GUI_ROOT / "blank-project.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the sticker travel scrapbook GUI.")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host. Default: 127.0.0.1")
    parser.add_argument("--port", type=int, default=8765, help="Preferred port. Default: 8765")
    parser.add_argument(
        "--project",
        default="sticker-travel-scrapbook-project.json",
        help="Project JSON to load/save. Default: ./sticker-travel-scrapbook-project.json",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Load the bundled Shanghai demo project when no project file exists.",
    )
    return parser.parse_args()


def find_port(host: str, preferred: int) -> int:
    for port in range(preferred, preferred + 100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((host, port))
            except OSError:
                continue
            return port
    raise RuntimeError(f"No free port found from {preferred} to {preferred + 99}")


def read_json(path: Path, use_demo: bool = False) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fallback = DEMO_PROJECT if use_demo else BLANK_PROJECT
        return json.loads(fallback.read_text(encoding="utf-8"))


def generate_openai_image(payload: dict, project_path: Path) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {
            "ok": False,
            "error": "OPENAI_API_KEY is not set. Set it in the server environment to generate images from the GUI.",
            "needsApiKey": True,
        }

    prompt = (payload.get("prompt") or "").strip()
    if not prompt:
        return {"ok": False, "error": "Prompt is required."}

    model = payload.get("model") or os.environ.get("OPENAI_IMAGE_MODEL") or "gpt-image-2"
    size = payload.get("size") or "1024x1536"
    quality = payload.get("quality") or "medium"
    output_format = payload.get("output_format") or "png"

    request_payload = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "output_format": output_format,
    }

    data = json.dumps(request_payload).encode("utf-8")
    req = Request(
        "https://api.openai.com/v1/images/generations",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urlopen(req, timeout=180) as response:
            result = json.loads(response.read().decode("utf-8"))
    except Exception as exc:  # Keep urllib errors dependency-free.
        return {"ok": False, "error": str(exc)}

    image_b64 = result.get("data", [{}])[0].get("b64_json")
    if not image_b64:
        return {"ok": False, "error": "The image response did not include b64_json.", "raw": result}

    out_dir = project_path.parent / "generated-images"
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"scrapbook-{int(time.time())}"
    image_path = out_dir / f"{stem}.{output_format}"
    image_path.write_bytes(base64.b64decode(image_b64))

    return {
        "ok": True,
        "imageUrl": f"/generated-images/{image_path.name}",
        "imagePath": str(image_path),
        "model": model,
        "size": size,
        "quality": quality,
        "output_format": output_format,
    }


def make_handler(project_path: Path, use_demo: bool = False):
    class Handler(BaseHTTPRequestHandler):
        server_version = "StickerTravelScrapbookGUI/1.0"

        def log_message(self, fmt: str, *args) -> None:
            print(f"{self.address_string()} - {fmt % args}")

        def send_json(self, payload: dict, status: int = 200) -> None:
            data = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def send_file(self, path: Path) -> None:
            if not path.exists() or not path.is_file():
                self.send_error(404, "File not found")
                return
            content_type, _ = mimetypes.guess_type(str(path))
            if path.suffix.lower() in {".html", ".css", ".js", ".json", ".txt", ".md"}:
                content_type = (content_type or "text/plain") + "; charset=utf-8"
            data = path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", content_type or "application/octet-stream")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            path = unquote(parsed.path)

            if path == "/api/project":
                project = read_json(project_path, use_demo=use_demo)
                self.send_json({"ok": True, "project": project, "projectPath": str(project_path)})
                return

            if path.startswith("/generated-images/"):
                generated_root = (project_path.parent / "generated-images").resolve()
                candidate = (generated_root / path.split("/", 2)[-1]).resolve()
                try:
                    candidate.relative_to(generated_root)
                except ValueError:
                    self.send_error(403, "Forbidden")
                    return
                self.send_file(candidate)
                return

            if path in ("/", "/index.html"):
                self.send_file(GUI_ROOT / "index.html")
                return

            candidate = (GUI_ROOT / path.lstrip("/")).resolve()
            try:
                candidate.relative_to(GUI_ROOT.resolve())
            except ValueError:
                self.send_error(403, "Forbidden")
                return
            self.send_file(candidate)

        def do_POST(self) -> None:
            parsed = urlparse(self.path)
            if parsed.path not in ("/api/project", "/api/generate-image"):
                self.send_error(404, "Not found")
                return

            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length)
            try:
                payload = json.loads(raw.decode("utf-8"))
            except json.JSONDecodeError as exc:
                self.send_json({"ok": False, "error": f"Invalid JSON: {exc}"}, status=400)
                return

            if parsed.path == "/api/project":
                project = payload.get("project", payload)
                project_path.parent.mkdir(parents=True, exist_ok=True)
                project_path.write_text(json.dumps(project, ensure_ascii=False, indent=2), encoding="utf-8")
                self.send_json({"ok": True, "projectPath": str(project_path)})
                return

            if parsed.path == "/api/generate-image":
                self.send_json(generate_openai_image(payload, project_path))
                return

    return Handler


def main() -> None:
    args = parse_args()
    project_path = Path(args.project).expanduser().resolve()
    port = find_port(args.host, args.port)
    handler = make_handler(project_path, use_demo=args.demo)
    httpd = ThreadingHTTPServer((args.host, port), handler)
    print(f"Sticker Travel Scrapbook GUI running at http://{args.host}:{port}/")
    print(f"Project file: {project_path}")
    print("Press Ctrl+C to stop.")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
