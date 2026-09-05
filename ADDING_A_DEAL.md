# Adding a Deal to the Directory

This guide explains how to add a seasonal deal, overstock item, or sale to the Genetic Beef Directory.

## What Qualifies as a Deal

A deal must meet these criteria:

1. **Verified from Ranch Website:** Sale/clearance/overstock must be visible on the ranch's public website
2. **Listed Ranch:** The ranch must already be in `data/listings.json`
3. **Current & Active:** Deal must be currently available (not expired)
4. **Real Price Reduction:** Actual markdown or clearance pricing (not fake "sales")

## Step 1: Verify the Deal

Visit the ranch website and confirm:
- Product name and cut type
- Regular price (if shown) and sale price
- Season label (Clearance, Sale, Overstock, Weekly Deal, etc.)
- Why it's on sale (reason for markdown)
- Current availability

**Important:** Only use prices shown on the ranch website. Do not invent or estimate prices.

## Step 2: Edit `data/deals.json`

Add a new entry to the `deals` array:

```json
{
  "id": "unique-slug-for-deal",
  "listing_id": "ranch-slug-from-listings-json",
  "ranch_name": "Ranch Name",
  "website": "https://www.ranchwebsite.com/",
  "product_url": "https://www.ranchwebsite.com/specific-product-page",
  "cut": "ribeye",
  "product_name": "Exact Product Name",
  "regular_price": 50.00,
  "sale_price": 40.00,
  "currency": "USD",
  "unit": "per lb",
  "season_label": "Clearance",
  "reason": "Short description of why this is a deal",
  "verified_at": "2026-09-05",
  "gaps": null
}
```

### Field Guide

- **id** (required): Unique slug (e.g., `heartbrand-ribeye-4pack`)
- **listing_id** (required): Links to ranch in `listings.json` (e.g., `heartbrand-beef`)
- **ranch_name** (required): Official ranch name
- **website** (required): Ranch website homepage
- **product_url** (required): Direct link to the product page
- **cut** (required): Normalized cut type (see below)
- **product_name** (required): Exact product name from website
- **regular_price** (optional): Original price; use `null` if not shown
- **sale_price** (required): Current sale price (number, not string)
- **currency** (required): Always "USD"
- **unit** (required): Unit of sale (e.g., "per lb", "4-pack", "box")
- **season_label** (required): Type of deal (see below)
- **reason** (required): Brief explanation of why this is a deal
- **verified_at** (required): Date verified in ISO format (YYYY-MM-DD)
- **gaps** (optional): Note if item is sold out or has limitations

### Cut Types (Normalized)

Use these exact slugs for the `cut` field:

- `ribeye` - Ribeye steaks
- `ground` - Ground beef
- `brisket` - Brisket
- `tenderloin` - Filet mignon, tenderloin
- `short-rib` - Short ribs
- `flat-iron` - Flat iron steaks
- `skirt` - Skirt steak
- `hanger` - Hanger steak
- `strip` - NY strip, striploin
- `roast` - Chuck roast, prime rib, other roasts
- `variety-box` - Variety packs, bundles, mixed boxes

### Season Labels

Use these labels:

- `Clearance` - Clearance pricing
- `Sale` - General sale
- `Overstock` - Overstock inventory
- `Weekly Deal` - Weekly or rotating specials
- `Labor Day Sale` - Holiday sales
- `Bundle Deal` - Package/bundle pricing
- `Limited Stock` - Limited availability

## Step 3: Rebuild the Site

Run the build script to regenerate pages with the new deal:

```bash
python3 build.py
```

This will:
- Add the deal to `/deals/` (all deals page)
- Update the home page seasonal deals section
- Update "best by cut" calculations

## Step 4: Verify the Build

Check that the deal appears:
- On `/deals/` (all deals page)
- On home page if it's a top deal
- With correct pricing and formatting

## Step 5: Update STATUS.md

Update the deals count and verification date in `STATUS.md`.

## Maintaining Deals

### Removing Expired Deals

When a deal expires or sells out:
1. Remove it from `data/deals.json`
2. Rebuild the site with `python3 build.py`
3. Commit changes

### Updating Deal Prices

If a ranch changes sale prices:
1. Edit the deal entry in `data/deals.json`
2. Update `verified_at` to current date
3. Rebuild the site

### Verification Schedule

Deals should be re-verified periodically:
- Weekly for "Weekly Deal" items
- Monthly for other sales
- Immediately if users report expired deals

## Tips

### Only Real Deals
- Don't add fake "sales" where the regular price is inflated
- If you can't verify a regular price, set `regular_price: null`
- Better to omit `regular_price` than guess

### Product URL Matters
Link directly to the product page when possible. If the ranch only has a general "sale" page, use that.

### Gaps Field
Use `gaps` to note:
- "Currently sold out"
- "Limited to 10 units per order"
- "Expires Sept 15"

## Example: Adding a Deal

Here's a full example of adding a ribeye deal:

1. Visit HeartBrand Beef's sales page
2. Confirm Ribeye 4-Pack is marked $250 (was $260)
3. Add to `data/deals.json`:

```json
{
  "id": "heartbrand-ribeye-4pack",
  "listing_id": "heartbrand-beef",
  "ranch_name": "HeartBrand Beef",
  "website": "https://heartbrandbeef.com/",
  "product_url": "https://heartbrandbeef.com/pages/sales",
  "cut": "ribeye",
  "product_name": "Wagyu Ribeye 4 Pack",
  "regular_price": 260,
  "sale_price": 250,
  "currency": "USD",
  "unit": "4-pack",
  "season_label": "Overstock",
  "reason": "Active sales page marking ribeye packs at reduced price",
  "verified_at": "2026-09-05",
  "gaps": null
}
```

4. Run `python3 build.py`
5. Verify the deal appears on `/deals/` and home page

## Questions?

Review existing deals in `data/deals.json` for reference patterns.

The goal is accuracy and honesty—only list real, verified deals with transparent pricing.
