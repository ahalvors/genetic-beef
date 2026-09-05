#!/usr/bin/env python3
"""
Acre & Plate - Static Site Generator
Generates all pages from data/listings.json and data/deals.json
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any

# Load listings data
with open('data/listings.json', 'r') as f:
    data = json.load(f)
    listings = data['listings']

# Load deals data
with open('data/deals.json', 'r') as f:
    deals_data = json.load(f)
    deals = deals_data['deals']

def ensure_dir(path: str):
    """Create directory if it doesn't exist"""
    Path(path).mkdir(parents=True, exist_ok=True)

def write_page(path: str, content: str):
    """Write HTML content to file"""
    ensure_dir(os.path.dirname(path))
    with open(path, 'w') as f:
        f.write(content)
    print(f"✓ {path}")

def base_template(title: str, content: str, meta_description: str = "") -> str:
    """Base HTML template for all pages"""
    if not meta_description:
        meta_description = "Find local, sustainable, ranch-direct beef—Fullblood Wagyu, Akaushi, Japanese Black, and rare heritage breeds from ranches you can trace."
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Acre & Plate</title>
    <meta name="description" content="{meta_description}">
    <link rel="stylesheet" href="/css/site.css">
</head>
<body>
    <header>
        <nav class="container">
            <div class="logo">
                <a href="/">Acre & Plate</a>
            </div>
            <ul class="nav-links">
                <li><a href="/listings/">All Listings</a></li>
                <li><a href="/deals/">Deals</a></li>
                <li><a href="/wagyu/">Wagyu</a></li>
                <li><a href="/akaushi/">Akaushi</a></li>
                <li><a href="/texas/">Texas</a></li>
                <li><a href="/guides/wagyu-vs-akaushi/">Guide</a></li>
                <li><a href="/about/">About</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        {content}
    </main>
    
    <footer>
        <div class="container">
            <p class="tagline">Ranch-direct beef for people who care where dinner came from—local pasture, named herds, honest sourcing.</p>
            <p class="disclaimer">Acre & Plate connects you with ranches raising cattle with traceable genetics. We do not sell beef. Contact ranches directly. Claims verified from public ranch websites as of {get_build_date()}.</p>
            <p class="links">
                <a href="/about/">About This Directory</a> · 
                <a href="/listings/">All Ranches</a> · 
                <a href="https://github.com/beefbot/genetic-beef" target="_blank">GitHub</a>
            </p>
        </div>
    </footer>
</body>
</html>"""

def get_build_date() -> str:
    """Get current date for footer"""
    from datetime import datetime
    return datetime.now().strftime("%B %Y")

def breed_chip(breed: str) -> str:
    """Generate breed chip HTML"""
    breed_map = {
        'wagyu': 'Wagyu',
        'akaushi': 'Akaushi',
        'heritage': 'Heritage',
        'randall-lineback': 'Randall Lineback',
        'dexter': 'Dexter',
        'piedmontese': 'Piedmontese'
    }
    return f'<span class="breed-chip breed-{breed}">{breed_map.get(breed, breed)}</span>'

def get_best_deals_by_cut() -> Dict[str, Dict[str, Any]]:
    """Get the best deal for each cut type"""
    best_by_cut = {}
    
    for deal in deals:
        cut = deal['cut']
        
        # Calculate discount percentage
        discount_pct = 0
        if deal.get('regular_price') and deal['regular_price'] > 0:
            discount_pct = ((deal['regular_price'] - deal['sale_price']) / deal['regular_price']) * 100
        
        # If we don't have this cut yet, or this deal is better, save it
        if cut not in best_by_cut:
            best_by_cut[cut] = {'deal': deal, 'discount_pct': discount_pct}
        else:
            # Compare by absolute price (lower is better)
            if deal['sale_price'] < best_by_cut[cut]['deal']['sale_price']:
                best_by_cut[cut] = {'deal': deal, 'discount_pct': discount_pct}
    
    return best_by_cut

def deal_card(deal: Dict[str, Any]) -> str:
    """Generate deal card HTML"""
    # Calculate discount percentage
    discount_pct = 0
    discount_html = ''
    price_html = f'<span class="sale-price">${deal["sale_price"]:.2f}</span>'
    
    if deal.get('regular_price') and deal['regular_price'] > 0:
        discount_pct = ((deal['regular_price'] - deal['sale_price']) / deal['regular_price']) * 100
        discount_html = f'<span class="discount-badge">-{discount_pct:.0f}%</span>'
        price_html = f'<span class="regular-price">${deal["regular_price"]:.2f}</span> <span class="sale-price">${deal["sale_price"]:.2f}</span>'
    
    # Get listing link if available
    listing_link_html = ''
    if deal.get('listing_id'):
        listing_link_html = f'<a href="/listings/{deal["listing_id"]}/" class="btn-secondary">View Ranch</a>'
    
    gaps_html = ''
    if deal.get('gaps'):
        gaps_html = f'<p class="note">{deal["gaps"]}</p>'
    
    verified_date = deal.get('verified_at', '')
    
    return f"""<article class="deal-card">
        <div class="deal-header">
            <span class="season-badge">{deal['season_label']}</span>
            {discount_html}
        </div>
        <h3><a href="{deal['product_url']}" target="_blank" rel="noopener">{deal['product_name']}</a></h3>
        <div class="ranch-name">{deal['ranch_name']}</div>
        <div class="cut-type">{deal['cut'].replace('-', ' ').title()}</div>
        <div class="deal-price">
            {price_html}
            <span class="unit">/ {deal['unit']}</span>
        </div>
        <p class="deal-reason">{deal['reason']}</p>
        {gaps_html}
        <div class="deal-verified">Verified {verified_date}</div>
        <div class="actions">
            {listing_link_html}
            <a href="{deal['product_url']}" target="_blank" rel="noopener" class="btn-primary">View Deal →</a>
        </div>
    </article>"""

def listing_card(listing: Dict[str, Any], show_full: bool = False) -> str:
    """Generate listing card HTML"""
    breeds_html = ''.join([breed_chip(b) for b in listing['breeds']])
    
    products_text = ', '.join(listing['products'][:3])
    if len(listing['products']) > 3:
        products_text += '…'
    
    shipping_class = ''
    shipping_text = listing['shipping']
    if 'pickup' in shipping_text.lower() or 'florida only' in shipping_text.lower():
        shipping_class = ' limited'
    
    note_html = ''
    if 'note' in listing:
        note_html = f'<p class="note">{listing["note"]}</p>'
    
    return f"""<article class="listing-card">
        <h3><a href="/listings/{listing['slug']}/">{listing['name']}</a></h3>
        <div class="location">{listing['city']}, {listing['state']}</div>
        <div class="breeds">{breeds_html}</div>
        <p class="genetics">{listing['genetics']}</p>
        <p class="products"><strong>Products:</strong> {products_text}</p>
        <p class="shipping{shipping_class}"><strong>Shipping:</strong> {shipping_text}</p>
        {note_html}
        <div class="actions">
            <a href="/listings/{listing['slug']}/" class="btn-secondary">View Details</a>
            <a href="{listing['url']}" target="_blank" rel="noopener" class="btn-primary">Visit Ranch →</a>
        </div>
    </article>"""

def build_index():
    """Build home page"""
    featured = [l for l in listings if l.get('featured', False)]
    
    featured_html = '\n'.join([listing_card(l) for l in featured[:3]])
    
    # Get best deals by cut for seasonal deals section
    best_by_cut = get_best_deals_by_cut()
    top_deals = sorted(best_by_cut.items(), key=lambda x: x[1]['discount_pct'], reverse=True)[:3]
    
    deals_html = ''
    if top_deals:
        deals_cards = '\n'.join([deal_card(item[1]['deal']) for item in top_deals])
        deals_html = f"""
    <section class="seasonal-deals">
        <div class="container">
            <h2>Seasonal Deals & Overstock</h2>
            <p class="section-intro">The best current deals across ranches—sale, clearance, and overstock inventory verified from ranch websites.</p>
            <div class="deals-grid">
                {deals_cards}
            </div>
            <div class="view-all">
                <a href="/deals/" class="btn-primary">View All {len(deals)} Deals</a>
            </div>
            <p class="deals-disclaimer">⚠️ Prices verified {deals[0].get('verified_at', '')} — confirm current availability and pricing on ranch websites before ordering.</p>
        </div>
    </section>
    """
    
    content = f"""
    <section class="hero">
        <div class="container">
            <h1>Acre & Plate</h1>
            <p class="tagline">Ranch-direct beef for people who care where dinner came from—local pasture, named herds, honest sourcing. Find Fullblood Wagyu, Akaushi, Japanese Black, and rare heritage breeds from ranches you can trace.</p>
            <div class="hero-actions">
                <a href="/listings/" class="btn-primary">Browse All Ranches</a>
                <a href="/deals/" class="btn-secondary">Deals</a>
                <a href="/wagyu/" class="btn-secondary">Wagyu</a>
                <a href="/akaushi/" class="btn-secondary">Akaushi</a>
            </div>
        </div>
    </section>
    
    {deals_html}
    
    <section class="how-it-works">
        <div class="container">
            <h2>How It Works</h2>
            <div class="steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <h3>Browse</h3>
                    <p>Explore ranches with named, traceable herds—Fullblood Wagyu, Akaushi, heritage breeds.</p>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <h3>Verify</h3>
                    <p>Each ranch lists their cattle's bloodlines, breed registrations, or DNA verification. Real sourcing, not marketing.</p>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <h3>Order Direct</h3>
                    <p>Contact ranches directly. Most ship nationwide, some offer local pickup.</p>
                </div>
            </div>
        </div>
    </section>
    
    <section class="featured">
        <div class="container">
            <h2>Featured Ranches</h2>
            <div class="listings-grid">
                {featured_html}
            </div>
            <div class="view-all">
                <a href="/listings/" class="btn-primary">View All {len(listings)} Ranches</a>
            </div>
        </div>
    </section>
    
    <section class="hubs">
        <div class="container">
            <h2>Browse by Breed or State</h2>
            <div class="hub-links">
                <a href="/wagyu/" class="hub-link">Wagyu <span class="count">({len([l for l in listings if 'wagyu' in l['breeds']])})</span></a>
                <a href="/akaushi/" class="hub-link">Akaushi <span class="count">({len([l for l in listings if 'akaushi' in l['breeds']])})</span></a>
                <a href="/texas/" class="hub-link">Texas <span class="count">({len([l for l in listings if l['state'] == 'TX'])})</span></a>
                <a href="/guides/wagyu-vs-akaushi/" class="hub-link">Wagyu vs Akaushi →</a>
            </div>
        </div>
    </section>
    """
    
    html = base_template("Home", content)
    write_page('index.html', html)

def build_listings_index():
    """Build all listings page"""
    all_cards = '\n'.join([listing_card(l) for l in listings])
    
    content = f"""
    <section class="page-header">
        <div class="container">
            <h1>All Ranches</h1>
            <p>{len(listings)} ranches with named herds, registered cattle, or DNA-verified bloodlines</p>
        </div>
    </section>
    
    <section class="listings-section">
        <div class="container">
            <div class="listings-grid">
                {all_cards}
            </div>
        </div>
    </section>
    """
    
    html = base_template("All Ranches", content, "Complete directory of ranch-direct beef with traceable bloodlines and named herds.")
    write_page('listings/index.html', html)

def build_listing_detail(listing: Dict[str, Any]):
    """Build individual listing page"""
    breeds_html = ''.join([breed_chip(b) for b in listing['breeds']])
    
    products_list = '</li><li>'.join(listing['products'])
    
    phone_html = ''
    if 'phone' in listing:
        phone_html = f'<p><strong>Phone:</strong> {listing["phone"]}</p>'
    
    note_html = ''
    if 'note' in listing:
        note_html = f'<div class="note-box"><strong>Note:</strong> {listing["note"]}</div>'
    
    content = f"""
    <section class="page-header">
        <div class="container">
            <div class="breadcrumb">
                <a href="/">Home</a> / <a href="/listings/">All Ranches</a> / {listing['name']}
            </div>
            <h1>{listing['name']}</h1>
            <div class="location">{listing['city']}, {listing['state']}</div>
            <div class="breeds">{breeds_html}</div>
        </div>
    </section>
    
    <section class="listing-detail">
        <div class="container">
            <div class="detail-main">
                <h2>Genetics</h2>
                <p class="genetics-detail">{listing['genetics']}</p>
                
                <h2>About</h2>
                <p>{listing.get('description', '')}</p>
                
                {note_html}
                
                <h2>Products Available</h2>
                <ul class="products-list">
                    <li>{products_list}</li>
                </ul>
                
                <h2>Shipping</h2>
                <p>{listing['shipping']}</p>
                
                <div class="contact-info">
                    <h2>Contact</h2>
                    <p><strong>Website:</strong> <a href="{listing['url']}" target="_blank" rel="noopener">{listing['url']}</a></p>
                    {phone_html}
                </div>
                
                <div class="cta">
                    <a href="{listing['url']}" target="_blank" rel="noopener" class="btn-primary">Visit Ranch Website →</a>
                </div>
            </div>
            
            <aside class="detail-sidebar">
                <div class="quick-facts">
                    <h3>Quick Facts</h3>
                    <dl>
                        <dt>Location</dt>
                        <dd>{listing['city']}, {listing['state']}</dd>
                        <dt>Breeds</dt>
                        <dd>{', '.join(listing['breeds'])}</dd>
                        <dt>Shipping</dt>
                        <dd>{listing['shipping']}</dd>
                    </dl>
                </div>
            </aside>
        </div>
    </section>
    """
    
    meta = f"{listing['name']} - {listing['genetics']} in {listing['city']}, {listing['state']}"
    html = base_template(listing['name'], content, meta)
    write_page(f"listings/{listing['slug']}/index.html", html)

def build_hub_page(title: str, slug: str, filter_fn, intro: str):
    """Build hub pages (Wagyu, Akaushi, Texas)"""
    filtered = [l for l in listings if filter_fn(l)]
    cards_html = '\n'.join([listing_card(l) for l in filtered])
    
    content = f"""
    <section class="page-header">
        <div class="container">
            <h1>{title}</h1>
            <p>{intro}</p>
            <p class="count">{len(filtered)} ranches</p>
        </div>
    </section>
    
    <section class="listings-section">
        <div class="container">
            <div class="listings-grid">
                {cards_html}
            </div>
        </div>
    </section>
    """
    
    html = base_template(title, content, intro)
    write_page(f'{slug}/index.html', html)

def build_guide():
    """Build Wagyu vs Akaushi guide"""
    content = """
    <section class="page-header">
        <div class="container">
            <h1>Wagyu vs Akaushi: What's the Difference?</h1>
        </div>
    </section>
    
    <section class="guide-content">
        <div class="container">
            <article class="guide">
                <h2>The Quick Answer</h2>
                <p>Akaushi is a specific breed of Wagyu. "Wagyu" means Japanese cattle and includes four breeds: Japanese Black (Kuroge), Brown (Akaushi), Polled, and Shorthorn. In the U.S., "Wagyu" usually refers to Japanese Black, while Akaushi is specifically the Japanese Brown breed.</p>
                
                <h2>Wagyu (Usually Japanese Black)</h2>
                <ul>
                    <li><strong>Genetics:</strong> Most common Wagyu breed, known for intense marbling</li>
                    <li><strong>Flavor:</strong> Rich, buttery, highly marbled</li>
                    <li><strong>Availability:</strong> More ranches raising Fullblood Wagyu in the U.S.</li>
                    <li><strong>Verification:</strong> Look for DNA-tested, registered, or traceable bloodlines</li>
                </ul>
                
                <h2>Akaushi (Japanese Brown Wagyu)</h2>
                <ul>
                    <li><strong>Genetics:</strong> Rarer breed, originally from Kumamoto Prefecture</li>
                    <li><strong>Flavor:</strong> Balanced marbling, slightly less fat than Japanese Black</li>
                    <li><strong>Health:</strong> Higher in monounsaturated fats and oleic acid</li>
                    <li><strong>Certification:</strong> HeartBrand Beef holds the "Certified Akaushi Beef®" trademark</li>
                </ul>
                
                <h2>What to Look For</h2>
                <p><strong>Fullblood vs. Crossbred:</strong> "Fullblood" or "100%" means pure Japanese bloodlines. "American Wagyu" or "F1" typically means crossed with Angus. Both can be excellent—depends on your preference.</p>
                
                <p><strong>Verification:</strong> Ranches on Acre & Plate claim DNA testing, registration with breed associations (American Wagyu Association, American Akaushi Association), or traceable herds. Check ranch websites for details.</p>
                
                <p><strong>Not Grocery Store "Wagyu":</strong> Acre & Plate focuses on ranch-direct beef with traceable sourcing—not retail products using "Wagyu-style" marketing without proof.</p>
                
                <div class="cta">
                    <a href="/wagyu/" class="btn-primary">Browse Wagyu Ranches</a>
                    <a href="/akaushi/" class="btn-primary">Browse Akaushi Ranches</a>
                </div>
            </article>
        </div>
    </section>
    """
    
    html = base_template("Wagyu vs Akaushi Guide", content, "Understand the difference between Wagyu and Akaushi beef, and what to look for when buying ranch-direct.")
    write_page('guides/wagyu-vs-akaushi/index.html', html)

def build_deals_page():
    """Build deals hub page"""
    # Group deals by cut
    deals_by_cut = {}
    for deal in deals:
        cut = deal['cut']
        if cut not in deals_by_cut:
            deals_by_cut[cut] = []
        deals_by_cut[cut].append(deal)
    
    # Sort cuts alphabetically
    sorted_cuts = sorted(deals_by_cut.keys())
    
    # Generate all deal cards
    all_deals_html = '\n'.join([deal_card(deal) for deal in deals])
    
    # Generate by-cut sections
    by_cut_html = ''
    for cut in sorted_cuts:
        cut_deals = deals_by_cut[cut]
        cut_cards_html = '\n'.join([deal_card(deal) for deal in cut_deals])
        cut_title = cut.replace('-', ' ').title()
        by_cut_html += f"""
        <div class="deals-by-cut">
            <h3 class="cut-heading">{cut_title} ({len(cut_deals)})</h3>
            <div class="deals-grid">
                {cut_cards_html}
            </div>
        </div>
        """
    
    content = f"""
    <section class="page-header">
        <div class="container">
            <h1>Seasonal Deals & Overstock</h1>
            <p>Current sale, clearance, and overstock deals from verified ranches</p>
            <p class="count">{len(deals)} active deals</p>
        </div>
    </section>
    
    <section class="deals-section">
        <div class="container">
            <div class="deals-intro">
                <h2>How This Works</h2>
                <p>Acre & Plate scouts ranch websites for sale, clearance, and overstock inventory. When a ranch marks down ribeyes, ground beef, or other cuts, we verify the deal and list it here. <strong>Always confirm pricing and availability on the ranch website before ordering</strong>—deals change frequently.</p>
                <p class="deals-disclaimer">⚠️ Prices last verified {deals[0].get('verified_at', '')}. Deals subject to ranch inventory and may sell out or expire.</p>
            </div>
            
            <h2>All Current Deals</h2>
            <div class="deals-grid">
                {all_deals_html}
            </div>
            
            <h2 class="section-divider">Deals by Cut</h2>
            {by_cut_html}
        </div>
    </section>
    """
    
    meta = f"Current seasonal deals and overstock on Wagyu, Akaushi, and heritage beef from ranch-direct sources. {len(deals)} active deals."
    html = base_template("Seasonal Deals & Overstock", content, meta)
    write_page('deals/index.html', html)

def build_about():
    """Build about page"""
    content = """
    <section class="page-header">
        <div class="container">
            <h1>About This Directory</h1>
        </div>
    </section>
    
    <section class="about-content">
        <div class="container">
            <article class="about">
                <h2>What Acre & Plate Is</h2>
                <p>A curated directory of ranches selling beef direct to consumers—ranches that name their herds, register their cattle, or verify bloodlines. Find Fullblood Wagyu, Akaushi, Japanese Black, and rare heritage breeds like Randall Lineback, Dexter, and Piedmontese.</p>
                
                <p>Not grocery store "Wagyu" marketing. Not breeding stock. Local, sustainable, ranch-direct beef you can trace.</p>
                
                <h2>Methodology</h2>
                <p>Each ranch listing is verified from the ranch's own public website. We record:</p>
                <ul>
                    <li>Breed and bloodline claims (DNA-tested, registered, traceable herds)</li>
                    <li>Available products (steaks, ground, shares)</li>
                    <li>Shipping info (nationwide, regional, pickup only)</li>
                    <li>Direct contact information</li>
                </ul>
                
                <p>We note gaps where information is thin or shipping is limited. We prefer omitting details over inventing them.</p>
                
                <h2>What We Don't Include</h2>
                <ul>
                    <li>Breeding stock / live cattle sales</li>
                    <li>Retail products without ranch attribution</li>
                    <li>"Wagyu-style" products without traceable sourcing</li>
                    <li>Restaurants (unless they're the ranch's direct retail channel)</li>
                </ul>
                
                <h2>Who Built This</h2>
                <p>Acre & Plate is maintained by BeefBot. Data is verified from ranch websites and updated periodically. If you're a ranch owner and need to update your listing, please contact us through GitHub.</p>
                
                <h2>How to Use Acre & Plate</h2>
                <ol>
                    <li><strong>Browse</strong> by breed, state, or all listings</li>
                    <li><strong>Check breed claims</strong> on each ranch's detail page</li>
                    <li><strong>Visit ranch websites</strong> to verify current availability and pricing</li>
                    <li><strong>Order direct</strong> from the ranch</li>
                </ol>
                
                <p class="disclaimer"><strong>Disclaimer:</strong> We don't sell beef. We don't receive commissions. We list publicly available information. Contact ranches directly for orders. Verify claims independently if needed.</p>
                
                <div class="cta">
                    <a href="/listings/" class="btn-primary">Browse All Ranches</a>
                    <a href="https://github.com/beefbot/genetic-beef" target="_blank" class="btn-secondary">GitHub</a>
                </div>
            </article>
        </div>
    </section>
    """
    
    html = base_template("About", content, "How Acre & Plate works and what makes it different from grocery store 'Wagyu' marketing.")
    write_page('about/index.html', html)

def main():
    """Build all pages"""
    print("Building Acre & Plate...\n")
    
    # Home page
    build_index()
    
    # All listings index
    build_listings_index()
    
    # Individual listing pages
    for listing in listings:
        build_listing_detail(listing)
    
    # Hub pages
    build_hub_page(
        "Wagyu Ranches",
        "wagyu",
        lambda l: 'wagyu' in l['breeds'],
        "Fullblood Wagyu ranches with registered or DNA-verified Japanese bloodlines. Most are Japanese Black (Kuroge), the breed known for intense marbling."
    )
    
    build_hub_page(
        "Akaushi Ranches",
        "akaushi",
        lambda l: 'akaushi' in l['breeds'],
        "Akaushi (Japanese Brown) ranches with traceable bloodlines. Akaushi is a rarer Wagyu breed known for balanced marbling and high monounsaturated fats."
    )
    
    build_hub_page(
        "Texas Ranches",
        "texas",
        lambda l: l['state'] == 'TX',
        "Texas ranches raising Wagyu, Akaushi, and other traceable-bloodline beef. Ranch-direct shipping available."
    )
    
    # Guide
    build_guide()
    
    # About
    build_about()
    
    # Deals page
    build_deals_page()
    
    print(f"\n✓ Built {len(listings)} listing pages")
    print("✓ Built hub pages (wagyu, akaushi, texas)")
    print("✓ Built guide and about pages")
    print(f"✓ Built deals page with {len(deals)} deals")
    print(f"\n✨ Site build complete! Total pages: {len(listings) + 8}")

if __name__ == '__main__':
    main()
