# Adding a Ranch to the Directory

This guide explains how to add a new ranch listing to Acre & Plate.

## Prerequisites

A ranch must meet these criteria to be added:

1. **Direct to Consumer:** Sells beef directly to consumers (not just wholesale)
2. **Traceable Bloodlines:** Named herds, registered cattle, or DNA-verified bloodlines (Fullblood Wagyu, Akaushi, heritage breeds)
3. **Public Information:** Has a public website with verifiable claims
4. **Not Breeding Stock Only:** Sells beef for consumption, not just live cattle

## Step 1: Verify Ranch Information

Visit the ranch's website and gather:
- Ranch name
- Location (city, state)
- Website URL
- Breed and bloodline claims (exact wording from their site)
- Breeds (wagyu, akaushi, heritage, etc.)
- Products available (steaks, ground, boxes, shares, etc.)
- Shipping information (nationwide, regional, pickup only)
- Contact info (phone, email if publicly listed)

**Important:** Only use information from their public website. Do not invent or assume details.

## Step 2: Edit `data/listings.json`

Add a new entry to the `listings` array:

```json
{
  "slug": "ranch-name-lowercase",
  "name": "Ranch Name",
  "url": "https://www.ranchwebsite.com/",
  "state": "ST",
  "city": "City Name",
  "genetics": "Exact genetics claim from their website",
  "breeds": ["wagyu", "akaushi", "heritage", "etc"],
  "products": ["steaks", "ground", "boxes", "whole/half beef"],
  "shipping": "Ships nationwide / Regional / Pickup only",
  "description": "Brief description from their about page",
  "phone": "555-555-5555",
  "note": "Optional note about gaps or limitations",
  "featured": false
}
```

### Field Guide

- **slug** (required): URL-friendly version of ranch name (lowercase, hyphens)
- **name** (required): Official ranch name
- **url** (required): Ranch website
- **state** (required): Two-letter state code (or region like "Northern Rockies")
- **city** (required): Primary location
- **genetics** (required): Exact breed/bloodline claim from ranch website
- **breeds** (required): Array of breed tags (see below)
- **products** (required): What they sell
- **shipping** (required): Shipping details
- **description** (optional but recommended): Brief ranch description
- **phone** (optional): Public phone number
- **note** (optional): Important limitations or gaps
- **featured** (optional): Set to `true` for homepage feature (max 3-4)

### Breed Tags

Use these exact tags (lowercase):
- `wagyu` - Fullblood Wagyu, Japanese Black
- `akaushi` - Akaushi, Japanese Brown
- `heritage` - Heritage breeds in general
- `randall-lineback` - Specific heritage breed
- `dexter` - Specific heritage breed
- `piedmontese` - Piedmontese breed

## Step 3: Rebuild the Site

Run the build script to generate the new pages:

```bash
python3 build.py
```

This will:
- Create a new listing detail page at `/listings/{slug}/`
- Update the all listings page
- Update relevant hub pages (Wagyu, Akaushi, state pages)
- Update counts on home page

## Step 4: Verify the Build

Check that the new ranch appears:
- On `/listings/` (all ranches)
- On relevant hub pages (`/wagyu/`, `/akaushi/`, `/texas/`, etc.)
- Has its own detail page at `/listings/{slug}/`

## Step 5: Update STATUS.md

Update the statistics in `STATUS.md`:
- Total ranches count
- Breed-specific counts
- State-specific counts
- Add the ranch to the listing list

## Tips

### Handling Gaps
If information is thin or missing:
- Use the `note` field to flag limitations
- Mark shipping restrictions clearly
- Better to omit a detail than to invent it

Example:
```json
"note": "Florida-only shipping at this time"
```

### Verifying Claims
Look for:
- Mentions of "DNA-tested", "registered", "traceable herds"
- Association memberships (American Wagyu Association, etc.)
- Specific breed documentation

If claims seem vague or marketing-only, don't add the ranch.

### Featured Ranches
Only 3-4 ranches should be featured on the home page. Choose based on:
- Exceptional breed/bloodline documentation
- Nationwide shipping
- Well-documented operations
- Representative of different breeds

## Example: Adding a Ranch

Here's a full example of adding "Example Ranch":

1. Visit https://exampleranch.com, verify they sell DNA-verified Akaushi beef
2. Add to `data/listings.json`:

```json
{
  "slug": "example-ranch",
  "name": "Example Ranch",
  "url": "https://exampleranch.com/",
  "state": "CO",
  "city": "Denver",
  "genetics": "DNA-verified Akaushi, registered with American Akaushi Association",
  "breeds": ["akaushi"],
  "products": ["steaks", "ground", "roasts", "quarter/half beef"],
  "shipping": "Ships to Western states",
  "phone": "303-555-1234",
  "description": "Family ranch raising registered Akaushi cattle in Colorado since 2015."
}
```

3. Run `python3 build.py`
4. Verify pages were created
5. Update `STATUS.md` total count to 19 ranches

## Questions?

Review existing listings in `data/listings.json` for reference patterns.

The goal is accuracy and honesty—only list ranches with real, verifiable breed claims.
