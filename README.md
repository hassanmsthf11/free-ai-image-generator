# 🎨 Free AI Image Generator — No Signup, No API Key, Unlimited

> **Generate stunning AI images for free — no signup, no API keys, no usage limits.** Stop paying $10–30/month for DALL-E or Midjourney. AI Image Studio gives you access to **8 powerful AI models** entirely in your browser.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Made with Puter.js](https://img.shields.io/badge/Powered%20by-Puter.js-6d5bf7)](https://puter.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/hassanmsthf11/free-ai-image-generator/pulls)

---

## ⚡ Why Use This Free AI Image Generator?

Most AI image generators charge $10–30/month, require signups, or limit you to 2–5 images per day. **AI Image Studio** removes all of that:

- ✅ **100% Free** — No hidden costs, no credit card required
- ✅ **No Signup Required** — Start generating images instantly
- ✅ **No API Keys Needed** — Everything works out of the box
- ✅ **Unlimited Generations** — No daily caps or rate limits
- ✅ **8 AI Models** — DALL-E 3, GPT Image, Gemini, FLUX and more
- ✅ **Browser-Only** — No installation, no server, no dependencies
- ✅ **Instant Download** — Save any generated image with one click
- ✅ **Open Source** — MIT licensed, fork and modify freely

---

## ✨ Key Features

### 🤖 8 AI Image Generation Models

| Provider | Model | Best For |
|----------|-------|----------|
| **OpenAI** | DALL-E 3 | Creative illustrations, detailed scenes |
| **OpenAI** | GPT Image Mini | Fast drafts and quick iterations |
| **OpenAI** | GPT Image 1 | High-quality photorealistic images |
| **OpenAI** | GPT Image 1.5 | Best quality, complex compositions |
| **Google** | Gemini 2.5 Flash | Fast generation with good quality |
| **Google** | Gemini 3 Pro | Premium quality from Google's latest |
| **Together** | FLUX.1 Schnell | Ultra-fast open source generation |
| **Together** | FLUX 1.1 Pro | High-quality open source generation |

### 🎭 9 Built-In Style Presets

Transform any prompt with one click:

| Style | Effect |
|-------|--------|
| ✨ None | Raw prompt, unmodified |
| 📷 **Photorealistic** | Ultra detailed, 8K, professional photography |
| 🎌 **Anime** | Manga illustration, vibrant colors, Studio Ghibli inspired |
| 🖌️ **Digital Art** | Concept art, fantasy illustration, highly detailed |
| 🧊 **3D Render** | Octane render, Cinema 4D, volumetric lighting |
| 🎨 **Watercolor** | Soft brushstrokes, traditional art style |
| 🖼️ **Oil Painting** | Classical art, museum quality, masterpiece |
| 👾 **Pixel Art** | Retro game style, 16-bit, nostalgic |
| ✏️ **Line Art** | Minimal, clean vector illustration, flat design |

### 📐 Multiple Aspect Ratios

Generate images in 4 aspect ratios: **1:1** (Square), **3:2** (Landscape), **2:3** (Portrait), **16:9** (Widescreen)

### 🖼️ Full Image Gallery

- **Local history** — All generated images saved to your browser automatically
- **Lightbox preview** — Click any image for a full-screen, high-res view
- **One-click download** — Save any image as PNG instantly
- **Copy prompt** — Re-use your best prompts with a single click
- **Delete & clear** — Manage your gallery easily

---

## 🚀 Quick Start Guide

### Option 1: Double-Click (Windows)

1. Download or clone this repo
2. Double-click **`run_server.bat`**
3. Browser opens → start generating!

### Option 2: Command Line

```bash
# Clone the repository
git clone https://github.com/hassanmsthf11/free-ai-image-generator.git
cd free-ai-image-generator

# Start a local server
python -m http.server 8000

# Open http://localhost:8000/index.html in your browser
```

### Option 3: Just Open the File

Simply open `index.html` directly in any modern browser — it works immediately!

---

## 🧠 How Does It Work?

AI Image Studio uses [Puter.js](https://puter.com) to connect your browser directly to powerful AI models — no backend, no API keys, no server required.

```
Your Browser → Puter.js SDK → AI Models (DALL-E, Gemini, FLUX)
                    ↓
              Generated Image → Your Gallery (saved in localStorage)
```

**First time?** A small authentication popup appears and closes automatically in ~1 second. After that, you get unlimited generations — forever.

---

## 🆚 Free AI Image Generator vs Paid Alternatives

| Feature | AI Image Studio | DALL-E (ChatGPT) | Midjourney | Other Free Tools |
|---------|:-:|:-:|:-:|:-:|
| **Price** | Free ✅ | $20/mo ❌ | $10/mo ❌ | Free ✅ |
| **Daily Limits** | Unlimited ✅ | ~50/day ❌ | ~200/mo ❌ | 2-5/day ❌ |
| **Signup** | None ✅ | Required ❌ | Required ❌ | Required ❌ |
| **AI Models** | 8 models ✅ | 1 model ❌ | 1 model ❌ | 1 model ❌ |
| **Style Presets** | 9 styles ✅ | None ❌ | Limited ⚠️ | None ❌ |
| **Instant Download** | Yes ✅ | Extra steps ⚠️ | Extra steps ⚠️ | Watermarks ❌ |
| **Open Source** | Yes ✅ | No ❌ | No ❌ | Rarely ⚠️ |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Vanilla HTML, CSS, JavaScript (single file, ~50KB) |
| **AI Backend** | [Puter.js](https://puter.com) — serverless AI gateway |
| **Image Storage** | Browser localStorage for gallery history |
| **Server** | Any static file server (Python, Node) or open HTML directly |
| **Design** | Custom dark theme with Inter font, gradient accents |

---

## 📂 Project Structure

```
free-ai-image-generator/
├── index.html        # Complete application (single file, no deps)
├── run_server.bat    # Windows one-click launcher
├── README.md         # This file
└── LICENSE           # MIT License
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## ❓ Frequently Asked Questions

**Q: Is this really free?**
A: Yes, 100% free. No hidden costs, no premium tier, no credit card required.

**Q: Do I need to create an account?**
A: No signup needed. A Puter authentication popup appears briefly on first use and closes automatically.

**Q: What AI models can I use?**
A: 8 models from OpenAI (DALL-E 3, GPT Image family), Google (Gemini), and Together AI (FLUX).

**Q: Can I use the generated images commercially?**
A: Check each AI provider's terms of service regarding commercial use of generated images.

**Q: How are my images stored?**
A: Images are stored locally in your browser's localStorage. They never leave your device.

**Q: Does this work on mobile?**
A: Yes! The interface is fully responsive with a collapsible sidebar for mobile devices.

---

## 📄 License

This project is licensed under the MIT License — use it however you want.

---

## ⭐ Star This Repo

If you find this free AI image generator useful, **please give it a star** ⭐ — it helps others discover this tool and keeps the project growing!

---

<p align="center">
  <b>Built with ❤️ using <a href="https://puter.com">Puter.js</a> — Making AI accessible to everyone</b>
</p>
