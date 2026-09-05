# Genetic Beef Directory

**Find ranch-direct beef where the genetics are named, registered, or DNA-verified—Fullblood Wagyu, Akaushi, Japanese Black, and rare heritage breeds—not grocery "Wagyu" marketing.**

Static directory site listing verified ranches selling genetics-documented beef direct to consumers.

🔗 **[View Site](https://genetic-beef.netlify.app)** (will be live after Netlify deploy)

---

## What This Is

A curated directory of 18 U.S. ranches selling:
- **Fullblood Wagyu** (DNA-verified, registered Japanese genetics)
- **Akaushi** (Japanese Brown Wagyu)
- **Heritage breeds** (Randall Lineback, Dexter, Piedmontese)

All direct-to-consumer. No retail "Wagyu" marketing. Every ranch has a public website with verifiable genetics claims.

**New:** Seasonal deals section tracking verified sale, clearance, and overstock pricing across ranches.

## Architecture

Static HTML site generated from `data/listings.json`:

```
data/listings.json     # Source of truth: 18 ranch listings
data/deals.json        # Current deals: 14 verified deals
build.py              # Python generator: data → HTML pages
css/site.css          # Styling
index.html            # Home page (generated)
listings/             # All ranch pages (generated)
deals/                # Deals hub (generated)
wagyu/                # Hub pages (generated)
akaushi/              # Hub pages (generated)
texas/                # Hub pages (generated)
guides/               # Guide pages (generated)
about/                # About page (generated)
```

**Build:** `python3 build.py`  
**Output:** 26 static HTML pages

## Repository Structure

```
├── data/
│   ├── listings.json          # 18 ranch listings (source of truth)
│   └── deals.json             # 14 current deals (verified pricing)
├── css/
│   └── site.css              # Site styles
├── build.py                  # Static site generator
├── netlify.toml              # Netlify build config
├── README.md                 # This file
├── STATUS.md                 # Build status, counts, known gaps
├── ADDING_A_PAGE.md          # Guide for adding ranches
├── ADDING_A_DEAL.md          # Guide for adding deals
└── [generated files]         # index.html, listings/, deals/, etc.
```

## Local Development

### Build the site
```bash
python3 build.py
```

This generates all 25 pages in the root directory.

### View locally
```bash
python3 -m http.server 8000
open http://localhost:8000
```

## Deployment

**Platform:** Netlify  
**Build command:** `python3 build.py`  
**Publish directory:** `/` (root)

Every push to `main` triggers a build and deploy via `netlify.toml`.

## Adding Content

### Adding a Ranch
See **[ADDING_A_PAGE.md](ADDING_A_PAGE.md)** for full instructions.

Quick version:
1. Verify ranch has public website with genetics claims
2. Add entry to `data/listings.json`
3. Run `python3 build.py`
4. Commit and push

### Adding a Deal
See **[ADDING_A_DEAL.md](ADDING_A_DEAL.md)** for full instructions.

Quick version:
1. Verify deal on ranch website (sale/clearance/overstock)
2. Add entry to `data/deals.json`
3. Run `python3 build.py`
4. Commit and push

## Data Quality

All 18 ranches verified from public websites as of September 2026.

**We record:**
- Genetics claims (exact wording from ranch sites)
- Location, products, shipping
- Contact info (phone, website)

**We don't include:**
- Real-time pricing or inventory
- Breeding stock / live cattle
- Retail products without ranch attribution

See [STATUS.md](STATUS.md) for known gaps and limitations.

## Site Statistics

- 18 ranches
- 14 active deals (verified Sept 5, 2026)
- 11 Wagyu, 5 Akaushi, 3 heritage breeds
- 26 total pages (home, listings, deals, hubs, guides)
- Mobile-first, warm ranch/editorial design

## Technology

- **Generator:** Python 3
- **Templating:** Python string formatting (build.py)
- **Styling:** Vanilla CSS (css/site.css)
- **JavaScript:** None (currently)
- **Deployment:** Netlify

No framework. No build toolchain. Just Python + HTML + CSS.

## Maintenance

**Owner:** BeefBot  
**Repository:** github.com/beefbot/genetic-beef (placeholder - update to real repo)  
**Status:** See [STATUS.md](STATUS.md)

To update ranch info:
1. Edit `data/listings.json`
2. Run `python3 build.py`
3. Commit changes
4. Push to `main`

Netlify auto-deploys.

## License

Data: Public information compiled from ranch websites  
Code: MIT License (build.py, site structure)

## Contact

This is a directory site. We don't sell beef.  
Contact ranches directly via links in each listing.

For directory questions or ranch additions: Open an issue on GitHub.

---

**Last Updated:** September 5, 2026  
**Ranches:** 18 | **Deals:** 14 | **Pages:** 26 | **Build:** ✅ Passing
