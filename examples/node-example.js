/**
 * AI Image Studio — Node.js example
 * ---------------------------------
 * Generate images with multiple Puter.js models from a Node.js script.
 *
 * Setup:
 *   1. Install Puter.js:   npm install puter
 *   2. Authenticate (one of the following):
 *        a. Set PUTER_TOKEN env var with a Puter user token
 *        b. Run `puter signin` once (uses your free Puter account)
 *   3. Run:  node examples/node-example.js "A cyberpunk dragon"
 *
 * Note: Puter.js also ships a browser SDK; for server-side usage
 * we use the Node SDK. If you don't want to set up auth, the
 * `puter.com` hosted model router (the same one the browser
 * SDK uses) accepts requests with a token in the Authorization
 * header. See https://docs.puter.com/ for full details.
 */

const { Auth, AI } = require('puter'); // hypothetical Node SDK import path

// Try dynamic import for ESM compatibility
(async () => {
  let puter;
  try {
    puter = require('puter');
  } catch (e) {
    console.error(
      'Could not require("puter"). Install it via `npm install puter` ' +
        'or use the global Puter CLI: `npm i -g puter` and run `puter signin`.'
    );
    process.exit(1);
  }

  const prompt = process.argv.slice(2).join(' ') ||
    'A serene Japanese garden with cherry blossoms and a koi pond, ultra detailed';

  // ─── Model catalog (newest first) ────────────────────────────────
  const models = [
    {
      label: 'GPT Image 2 (NEW · reasoning)',
      model: 'gpt-image-2',
      provider: 'openai-image-generation',
      options: { quality: 'high', ratio: { w: 1024, h: 1024 } },
    },
    {
      label: 'Gemini 3 Pro Image (Nano Banana Pro)',
      model: 'gemini-3-pro-image-preview',
      provider: 'gemini',
      options: { ratio: { w: 1024, h: 1024 } },
    },
    {
      label: 'FLUX.2 Pro (NEW · photorealism)',
      model: 'black-forest-labs/flux-2-pro',
      provider: 'replicate-image-generation',
      options: { ratio: { w: 1024, h: 1024 }, output_quality: 90 },
    },
    {
      label: 'FLUX.2 Flex (NEW · customizable)',
      model: 'black-forest-labs/flux.2-flex',
      provider: 'replicate-image-generation',
      options: { width: 1024, height: 1024, steps: 30 },
    },
    {
      label: 'FLUX.2 Dev (NEW · open weights)',
      model: 'black-forest-labs/flux-2-dev',
      provider: 'replicate-image-generation',
      options: { ratio: { w: 1024, h: 1024 }, output_quality: 90 },
    },
    {
      label: 'FLUX.1 Schnell (fast)',
      model: 'black-forest-labs/FLUX.1-schnell',
      provider: 'together',
      options: { width: 1024, height: 1024 },
    },
    {
      label: 'GPT Image Mini (fastest)',
      model: 'gpt-image-1-mini',
      provider: 'openai-image-generation',
      options: { quality: 'low', ratio: { w: 1024, h: 1024 } },
    },
  ];

  for (const m of models) {
    console.log(`\n→ ${m.label}`);
    try {
      // puter.ai.txt2img returns an image element / data URL in the browser SDK.
      // In Node it returns a PuterImage object with a `.src` (data URL) field.
      const imageEl = await puter.ai.txt2img(prompt, {
        model: m.model,
        provider: m.provider,
        ...m.options,
      });

      const src = imageEl?.src || imageEl;
      if (!src) {
        console.log('   (no image returned)');
        continue;
      }

      // Strip the data URL prefix and write to disk
      const match = /^data:(image\/\w+);base64,(.+)$/.exec(src);
      if (match) {
        const ext = match[1].split('/')[1] || 'png';
        const buf = Buffer.from(match[2], 'base64');
        const filename = `out-${m.model.replace(/[^\w.-]+/g, '_')}.${ext}`;
        require('fs').writeFileSync(filename, buf);
        console.log(`   ✓ saved ${filename} (${buf.length} bytes)`);
      } else {
        // Remote URL — just log it
        console.log(`   ✓ URL: ${src}`);
      }
    } catch (err) {
      console.error(`   ✗ failed: ${err.message || err}`);
    }
  }
})();
