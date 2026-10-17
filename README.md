# LedgerLoop

> **Competition demonstration.** LedgerLoop is a fictional business created for the PS 04 challenge (Case 2). It is not a real company or product. Do not make any payment shown on the page.

A single-page site for the invoicing and payment-tracking software LedgerLoop, built so AI assistants find it, describe it correctly and cite it. Phone sign-in uses [MiniMoth](https://minimoth.dev) OTP. Built with [CiteForge](https://citeforge.onrender.com) (team Schrödinger’s Code).

## Ground truth used (from the brief)
Hyderabad · launched 2023 · four staff · about 2,600 paying customers · GST-compliant invoices, UPI payment links, automatic reminders, expense tracking · **no** multi-currency invoicing, **no** payroll · plans: free, ₹399/month, ₹899/month · previously email + password, now mobile OTP.

## What’s in this repo
| File | Purpose |
|---|---|
| `index.html` | The whole site: content, JSON-LD (`Organization`, `SoftwareApplication` + `Offer`, `FAQPage`), styles, OTP UI, first-touch attribution |
| `server.py` | Python 3.8+ standard-library server. Serves the site and proxies `/api/otp/send` and `/api/otp/verify` to MiniMoth so the API key stays server-side |
| `llms.txt`, `robots.txt`, `sitemap.xml` | Machine-readable summary, crawler rules, sitemap |
| `sample-upi-qr.png` | Demo UPI QR shown in the “Pay with UPI” popup |
| `.env.example`, `render.yaml`, `.gitignore` | Config for local run and Render deployment |
| `DECISIONS.md` | Why each choice was made and which brief problem it answers |

## Run locally
```bash
cp .env.example .env        # then paste your MiniMoth key into .env
python server.py            # http://localhost:3000
```
Open it through the server, **not** by double-clicking `index.html` (browsers block direct calls to MiniMoth, and the key must not be in the page). In sandbox mode no real message is sent; use the MiniMoth Playground to see test codes.

## Deploy
- **Render:** New → Web Service from this repo (`render.yaml` is included). Add `MINIMOTH_API_KEY` in the dashboard.
- **GitHub Pages / static hosts will not work**, because the OTP proxy needs a running server.
