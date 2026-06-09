"""
AI Image Studio — Python example
----------------------------------
Generate images with multiple Puter.js models from a Python script.

The browser Puter.js SDK isn't directly callable from Python, so this
example uses the underlying Puter REST API (the same one the browser
SDK calls) with the `requests` library. Authentication is via a free
Puter user token (set the `PUTER_TOKEN` env var).

Setup:
    pip install requests
    export PUTER_TOKEN=puter-...        # Linux / macOS
    setx PUTER_TOKEN puter-...          # Windows (PowerShell: $env:PUTER_TOKEN=...)
    python examples/python-example.py "A cyberpunk dragon"

Docs:
    https://docs.puter.com/AI/txt2img/
    https://developer.puter.com/
"""

import argparse
import base64
import mimetypes
import os
import re
import sys
import time
from pathlib import Path

import requests

API_URL = "https://api.puter.com/ai/txt2img"

# ─── Model catalog (newest first) ────────────────────────────────────────
MODELS = [
    {
        "label": "GPT Image 2 (NEW · reasoning)",
        "model": "gpt-image-2",
        "provider": "openai-image-generation",
        "options": {"quality": "high", "ratio": {"w": 1024, "h": 1024}},
    },
    {
        "label": "Gemini 3 Pro Image (Nano Banana Pro)",
        "model": "gemini-3-pro-image-preview",
        "provider": "gemini",
        "options": {"ratio": {"w": 1024, "h": 1024}},
    },
    {
        "label": "FLUX.2 Pro (NEW · photorealism)",
        "model": "black-forest-labs/flux-2-pro",
        "provider": "replicate-image-generation",
        "options": {"ratio": {"w": 1024, "h": 1024}, "output_quality": 90},
    },
    {
        "label": "FLUX.2 Flex (NEW · customizable)",
        "model": "black-forest-labs/flux.2-flex",
        "provider": "replicate-image-generation",
        "options": {"width": 1024, "height": 1024, "steps": 30},
    },
    {
        "label": "FLUX.2 Dev (NEW · open weights)",
        "model": "black-forest-labs/flux-2-dev",
        "provider": "replicate-image-generation",
        "options": {"ratio": {"w": 1024, "h": 1024}, "output_quality": 90},
    },
    {
        "label": "FLUX.1 Schnell (fast)",
        "model": "black-forest-labs/FLUX.1-schnell",
        "provider": "together",
        "options": {"width": 1024, "height": 1024},
    },
    {
        "label": "GPT Image Mini (fastest)",
        "model": "gpt-image-1-mini",
        "provider": "openai-image-generation",
        "options": {"quality": "low", "ratio": {"w": 1024, "h": 1024}},
    },
]


def generate(prompt: str, model_spec: dict, token: str, out_dir: Path) -> None:
    """Call the Puter REST API and save the resulting image to disk."""
    body = {
        "prompt": prompt,
        "model": model_spec["model"],
        "provider": model_spec["provider"],
        **model_spec["options"],
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    t0 = time.time()
    resp = requests.post(API_URL, json=body, headers=headers, timeout=180)
    elapsed = time.time() - t0

    if resp.status_code != 200:
        print(f"   ✗ HTTP {resp.status_code}: {resp.text[:200]}")
        return

    # The endpoint returns either JSON {image: "data:..."} or the raw bytes
    ctype = resp.headers.get("Content-Type", "")
    if ctype.startswith("application/json"):
        data = resp.json()
        src = data.get("image") or data.get("src") or data.get("data", {}).get("src")
    elif ctype.startswith("image/"):
        out = out_dir / f"out-{re.sub(r'[^\w.-]+', '_', model_spec['model'])}.{ctype.split('/')[-1]}"
        out.write_bytes(resp.content)
        print(f"   ✓ saved {out.name} ({len(resp.content)} bytes) in {elapsed:.1f}s")
        return
    else:
        # Try to parse JSON anyway
        try:
            data = resp.json()
            src = data.get("image") or data.get("src")
        except Exception:
            print(f"   ✗ Unexpected content-type {ctype!r}")
            return

    if not src:
        print("   ✗ No image in response")
        return

    # Save data URL or remote URL
    m = re.match(r"^data:(image/\w+);base64,(.+)$", src, re.DOTALL)
    if m:
        ext = mimetypes.guess_extension(m.group(1)) or ".png"
        out = out_dir / f"out-{re.sub(r'[^\w.-]+', '_', model_spec['model'])}{ext}"
        out.write_bytes(base64.b64decode(m.group(2)))
        print(f"   ✓ saved {out.name} in {elapsed:.1f}s")
    elif src.startswith("http"):
        out = out_dir / f"out-{re.sub(r'[^\w.-]+', '_', model_spec['model'])}.png"
        out.write_bytes(requests.get(src, timeout=60).content)
        print(f"   ✓ saved {out.name} (from {src}) in {elapsed:.1f}s")
    else:
        print(f"   ✓ (returned value): {src[:120]}...")


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Image Studio — Python example")
    parser.add_argument("prompt", nargs="*", help="Prompt text (else uses default)")
    parser.add_argument("--out", default=".", help="Output directory")
    parser.add_argument(
        "--model",
        choices=[m["label"] for m in MODELS],
        help="Generate using only this model (else runs all)",
    )
    args = parser.parse_args()

    token = os.environ.get("PUTER_TOKEN")
    if not token:
        print(
            "ERROR: Puter token missing. Set the PUTER_TOKEN env var.\n"
            "  1. Sign up free at https://puter.com\n"
            "  2. Open https://puter.com/app/settings to find your token\n"
            "  3. export PUTER_TOKEN=puter-...   (or setx on Windows)\n"
        )
        sys.exit(1)

    prompt = " ".join(args.prompt) or "A serene Japanese garden with cherry blossoms and a koi pond, ultra detailed"
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Prompt: {prompt}\nOutput: {out_dir.resolve()}\n")

    selected = MODELS if not args.model else [m for m in MODELS if m["label"] == args.model]
    for m in selected:
        print(f"→ {m['label']}")
        try:
            generate(prompt, m, token, out_dir)
        except Exception as e:  # noqa: BLE001
            print(f"   ✗ failed: {e}")


if __name__ == "__main__":
    main()
