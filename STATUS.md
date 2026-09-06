# Acre & Plate - Status

**Last Updated:** September 6, 2026  
**Build Status:** ✅ Passing

## Site Statistics

- **Total Ranches:** 19
- **Active Deals:** 14
- **Wagyu Ranches:** 12
- **Akaushi Ranches:** 5
- **Heritage Breeds:** 3
- **Texas Ranches:** 6
- **Total Pages:** 27

## Pages Built

### Core Pages
- ✅ Home (`index.html`)
- ✅ All Listings (`/listings/`)
- ✅ Seasonal Deals (`/deals/`) - 14 active deals
- ✅ About (`/about/`)

### Hub Pages
- ✅ Wagyu hub (`/wagyu/`) - 11 ranches
- ✅ Akaushi hub (`/akaushi/`) - 5 ranches
- ✅ Texas hub (`/texas/`) - 6 ranches

### Guide Pages
- ✅ Wagyu vs Akaushi Guide (`/guides/wagyu-vs-akaushi/`)

### Listing Pages (19 ranches)
- ✅ Lone Mountain Wagyu (NM)
- ✅ HeartBrand Beef (TX)
- ✅ Long Hill Wagyu (TX)
- ✅ Circle H Ranch (WY/ID)
- ✅ Hawks Hill Ranch (WY)
- ✅ Slickhorn Ranch (Northern Rockies)
- ✅ Pasture Prime Wagyu (FL)
- ✅ Rutledge Ryan Ranch (TX)
- ✅ Mahan Wagyu (TX)
- ✅ Mossyrock Wagyu (WA)
- ✅ Grant Cattle Company (KS)
- ✅ Black Wagyu Beef Co. (FL)
- ✅ Quinn Beef (TX)
- ✅ Tribe Ranch (AR)
- ✅ Hook & Cleaver Ranch (CA/AZ)
- ✅ Chapel Hill Farm (VA)
- ✅ Certified Piedmontese (NE)
- ✅ Mahanaim Farms (UT)
- ✅ Vermont Wagyu (VT)

## Known Gaps & Notes

### Limited Shipping
- **Black Wagyu Beef Co.** - Florida only (beta testing)
- **Mahanaim Farms** - Pickup only in Salt Lake City (no shipping)

### Contact Info Gaps
- Most ranches have public websites and contact info verified
- Grant Cattle Company - form-based inquiry (no direct phone on main site)
- Vermont Wagyu - email contact available (farm@vermontwagyu.com), phone not listed on public site

### Product Availability
- Several ranches list products as "sold out" seasonally
- Availability changes frequently - users should verify on ranch sites

## Data Quality

### Verified Information
All 19 ranch listings on Acre & Plate have been verified from:
- Public ranch websites
- Direct product pages
- Contact information pages
- Shipping policy pages

### Deals & Pricing
- ✅ **14 active deals** verified from ranch websites (as of Sept 5, 2026)
- ✅ Sale prices confirmed from ranch sales/clearance pages
- ✅ Regular prices included when shown by ranch
- ⚠️ Deals updated periodically—users should confirm current pricing on ranch sites
- ⚠️ Certified Piedmontese Labor Day Sale ends Sep 7, 2026 midnight CST

### What We Record
- ✅ Ranch name and location
- ✅ Breed and bloodline claims (DNA-verified, registered, traceable herds)
- ✅ Available products
- ✅ Shipping information
- ✅ Contact details (website, phone where available)
- ✅ Current deals (sale, clearance, overstock)

### What We Don't Include
- ❌ Real-time inventory/stock levels
- ❌ Breeding stock sales
- ❌ Retail products without ranch attribution
- ❌ Fake "sales" with inflated regular prices

## Build Process

```bash
python3 build.py
```

**Output:** 26 static HTML pages + CSS

**Publish Directory:** Root (all HTML files in root and subdirectories)

## Next Steps / Future Enhancements

- [ ] Add state hub pages (beyond Texas)
- [ ] Add heritage breeds hub page
- [ ] Expand to more ranches (verified genetics only)
- [ ] Add search/filter functionality (JavaScript)
- [ ] Weekly/monthly deal verification cron
- [ ] Consider RSS feed for new listings and deals

## Maintenance

**Data Sources:**
- `data/listings.json` - Ranch listings
- `data/deals.json` - Current deals

**Template Engine:** `build.py` (Python)  
**Styling:** `css/site.css`

To add a ranch, see `ADDING_A_PAGE.md`.  
To add a deal, see `ADDING_A_DEAL.md`.
