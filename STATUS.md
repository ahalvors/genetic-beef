# Genetic Beef Directory - Status

**Last Updated:** September 5, 2026  
**Build Status:** ✅ Passing

## Site Statistics

- **Total Ranches:** 18
- **Wagyu Ranches:** 11
- **Akaushi Ranches:** 5
- **Heritage Breeds:** 3
- **Texas Ranches:** 6
- **Total Pages:** 25

## Pages Built

### Core Pages
- ✅ Home (`index.html`)
- ✅ All Listings (`/listings/`)
- ✅ About (`/about/`)

### Hub Pages
- ✅ Wagyu hub (`/wagyu/`) - 11 ranches
- ✅ Akaushi hub (`/akaushi/`) - 5 ranches
- ✅ Texas hub (`/texas/`) - 6 ranches

### Guide Pages
- ✅ Wagyu vs Akaushi Guide (`/guides/wagyu-vs-akaushi/`)

### Listing Pages (18 ranches)
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

## Known Gaps & Notes

### Limited Shipping
- **Black Wagyu Beef Co.** - Florida only (beta testing)
- **Mahanaim Farms** - Pickup only in Salt Lake City (no shipping)

### Contact Info Gaps
- Most ranches have public websites and contact info verified
- Grant Cattle Company - form-based inquiry (no direct phone on main site)

### Product Availability
- Several ranches list products as "sold out" seasonally
- Availability changes frequently - users should verify on ranch sites

## Data Quality

### Verified Information
All 18 ranch listings have been verified from:
- Public ranch websites
- Direct product pages
- Contact information pages
- Shipping policy pages

### What We Record
- ✅ Ranch name and location
- ✅ Genetics claims (DNA-verified, registered, traceable)
- ✅ Available products
- ✅ Shipping information
- ✅ Contact details (website, phone where available)

### What We Don't Include
- ❌ Real-time pricing (changes frequently)
- ❌ Current inventory/stock levels
- ❌ Breeding stock sales
- ❌ Retail products without ranch attribution

## Build Process

```bash
python3 build.py
```

**Output:** 25 static HTML pages + CSS

**Publish Directory:** Root (all HTML files in root and subdirectories)

## Next Steps / Future Enhancements

- [ ] Add state hub pages (beyond Texas)
- [ ] Add heritage breeds hub page
- [ ] Expand to more ranches (verified genetics only)
- [ ] Add search/filter functionality (JavaScript)
- [ ] Consider RSS feed for new listings

## Maintenance

**Data Source:** `data/listings.json`  
**Template Engine:** `build.py` (Python)  
**Styling:** `css/site.css`

To add a ranch, see `ADDING_A_PAGE.md`.
