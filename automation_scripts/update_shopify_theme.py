"""
Update Shopify Whisper theme to match GeneticHomeopathy main website design.
Updates: color schemes, typography, button styles, and global settings.
"""
import json
import urllib.request
import urllib.parse
import copy

SHOP = "genetic-homeopathy.myshopify.com"
TOKEN = "YOUR_TOKEN_HERE"
THEME_ID = "138759471179"
API = f"https://{SHOP}/admin/api/2024-10"

def api_get(path):
    req = urllib.request.Request(f"{API}{path}", headers={"X-Shopify-Access-Token": TOKEN})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def api_put(path, data):
    body = json.dumps(data).encode()
    req = urllib.request.Request(f"{API}{path}", data=body, method="PUT",
                                headers={"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        print(e.read().decode())
        raise

# ── 1. Fetch current settings ──────────────────────────────────────────
print("📥 Fetching current theme settings...")
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=config/settings_data.json")
settings = json.loads(raw["asset"]["value"])
current = settings["current"]

# ── 2. Update Color Schemes ────────────────────────────────────────────
print("🎨 Updating color schemes...")

# Scheme 1 — Default Light (sage-50 bg, sage-600 primary)
current["color_schemes"]["scheme-1"]["settings"] = {
    "background": "#f6f7f4",           # sage-50
    "foreground_heading": "#3d4a35",   # sage-800
    "foreground": "#2d2d2d",           # text-primary
    "primary": "#6b7e5e",              # sage-600
    "primary_hover": "#556448",        # sage-700
    "border": "#d4daca",               # sage-200 / border-sage
    "shadow": "#000000",
    "primary_button_background": "#6b7e5e",    # sage-600
    "primary_button_text": "#ffffff",
    "primary_button_border": "#6b7e5e",
    "primary_button_hover_background": "#556448",  # sage-700
    "primary_button_hover_text": "#ffffff",
    "primary_button_hover_border": "#556448",
    "secondary_button_background": "rgba(0,0,0,0)",
    "secondary_button_text": "#6b7e5e",
    "secondary_button_border": "#6b7e5e",
    "secondary_button_hover_background": "#6b7e5e",
    "secondary_button_hover_text": "#ffffff",
    "secondary_button_hover_border": "#6b7e5e",
    "input_background": "#ffffff",
    "input_text_color": "#2d2d2d",
    "input_border_color": "#d4daca",
    "input_hover_background": "#faf8f5",
    "variant_background_color": "#ffffff",
    "variant_text_color": "#2d2d2d",
    "variant_border_color": "#d4daca",
    "variant_hover_background_color": "#f6f7f4",
    "variant_hover_text_color": "#2d2d2d",
    "variant_hover_border_color": "#b5c0a7",
    "selected_variant_background_color": "#6b7e5e",
    "selected_variant_text_color": "#ffffff",
    "selected_variant_border_color": "#6b7e5e",
    "selected_variant_hover_background_color": "#556448",
    "selected_variant_hover_text_color": "#ffffff",
    "selected_variant_hover_border_color": "#556448",
}

# Scheme 2 — Dark (sage-800 bg, cream text)
current["color_schemes"]["scheme-2"]["settings"] = {
    "background": "#3d4a35",           # sage-800
    "foreground_heading": "#faf8f5",   # cream-50
    "foreground": "#f5f0e8",           # cream-100
    "primary": "#c9a84c",              # gold-400
    "primary_hover": "#b8943f",        # gold-500
    "border": "#556448",               # sage-700
    "shadow": "#000000",
    "primary_button_background": "#c9a84c",    # gold-400
    "primary_button_text": "#ffffff",
    "primary_button_border": "#c9a84c",
    "primary_button_hover_background": "#b8943f",
    "primary_button_hover_text": "#ffffff",
    "primary_button_hover_border": "#b8943f",
    "secondary_button_background": "rgba(0,0,0,0)",
    "secondary_button_text": "#f5f0e8",
    "secondary_button_border": "#f5f0e8",
    "secondary_button_hover_background": "#f5f0e8",
    "secondary_button_hover_text": "#3d4a35",
    "secondary_button_hover_border": "#f5f0e8",
    "input_background": "#556448",
    "input_text_color": "#ffffff",
    "input_border_color": "#b5c0a7",
    "input_hover_background": "#6b7e5e",
    "variant_background_color": "#556448",
    "variant_text_color": "#f5f0e8",
    "variant_border_color": "#6b7e5e",
    "variant_hover_background_color": "#6b7e5e",
    "variant_hover_text_color": "#ffffff",
    "variant_hover_border_color": "#b5c0a7",
    "selected_variant_background_color": "#c9a84c",
    "selected_variant_text_color": "#ffffff",
    "selected_variant_border_color": "#c9a84c",
    "selected_variant_hover_background_color": "#b8943f",
    "selected_variant_hover_text_color": "#ffffff",
    "selected_variant_hover_border_color": "#b8943f",
}

# Scheme 3 — Accent/Hero (sage-600 bg, white text)
current["color_schemes"]["scheme-3"]["settings"] = {
    "background": "#6b7e5e",           # sage-600
    "foreground_heading": "#ffffff",
    "foreground": "#f5f0e8",           # cream-100
    "primary": "#f5f0e8",
    "primary_hover": "#ede5d8",        # cream-200
    "border": "#94a87e",               # sage-400
    "shadow": "#000000",
    "primary_button_background": "#c9a84c",    # gold-400
    "primary_button_text": "#ffffff",
    "primary_button_border": "#c9a84c",
    "primary_button_hover_background": "#b8943f",
    "primary_button_hover_text": "#ffffff",
    "primary_button_hover_border": "#b8943f",
    "secondary_button_background": "rgba(0,0,0,0)",
    "secondary_button_text": "#ffffff",
    "secondary_button_border": "#ffffff",
    "secondary_button_hover_background": "#ffffff",
    "secondary_button_hover_text": "#3d4a35",
    "secondary_button_hover_border": "#ffffff",
    "input_background": "#ffffff",
    "input_text_color": "#2d2d2d",
    "input_border_color": "#d4daca",
    "input_hover_background": "#f6f7f4",
    "variant_background_color": "#ffffff",
    "variant_text_color": "#2d2d2d",
    "variant_border_color": "#d4daca",
    "variant_hover_background_color": "#f6f7f4",
    "variant_hover_text_color": "#2d2d2d",
    "variant_hover_border_color": "#b5c0a7",
    "selected_variant_background_color": "#c9a84c",
    "selected_variant_text_color": "#ffffff",
    "selected_variant_border_color": "#c9a84c",
    "selected_variant_hover_background_color": "#b8943f",
    "selected_variant_hover_text_color": "#ffffff",
    "selected_variant_hover_border_color": "#b8943f",
}

# Scheme 4 — Light sage (sage-100 bg)
current["color_schemes"]["scheme-4"]["settings"] = {
    "background": "#e8ebe3",           # sage-100
    "foreground_heading": "#3d4a35",   # sage-800
    "foreground": "#2d2d2d",           # text-primary
    "primary": "#6b7e5e",              # sage-600
    "primary_hover": "#556448",        # sage-700
    "border": "#d4daca",               # sage-200
    "shadow": "#000000",
    "primary_button_background": "#6b7e5e",
    "primary_button_text": "#ffffff",
    "primary_button_border": "#6b7e5e",
    "primary_button_hover_background": "#556448",
    "primary_button_hover_text": "#ffffff",
    "primary_button_hover_border": "#556448",
    "secondary_button_background": "rgba(0,0,0,0)",
    "secondary_button_text": "#3d4a35",
    "secondary_button_border": "#3d4a35",
    "secondary_button_hover_background": "#ffffff",
    "secondary_button_hover_text": "#3d4a35",
    "secondary_button_hover_border": "#ffffff",
    "input_background": "#ffffff",
    "input_text_color": "#2d2d2d",
    "input_border_color": "#d4daca",
    "input_hover_background": "#f6f7f4",
    "variant_background_color": "#ffffff",
    "variant_text_color": "#2d2d2d",
    "variant_border_color": "#d4daca",
    "variant_hover_background_color": "#f6f7f4",
    "variant_hover_text_color": "#2d2d2d",
    "variant_hover_border_color": "#b5c0a7",
    "selected_variant_background_color": "#6b7e5e",
    "selected_variant_text_color": "#ffffff",
    "selected_variant_border_color": "#6b7e5e",
    "selected_variant_hover_background_color": "#556448",
    "selected_variant_hover_text_color": "#ffffff",
    "selected_variant_hover_border_color": "#556448",
}

# ── 3. Update Typography ──────────────────────────────────────────────
print("✏️  Updating typography...")
current["type_heading_font"] = "playfair_display_n7"   # Playfair Display Bold
current["type_body_font"] = "inter_n4"                  # Inter Regular
current["type_subheading_font"] = "inter_n5"            # Inter Medium (subheadings)
current["type_accent_font"] = "playfair_display_n4"     # Playfair Display Regular (accent/italic)

# H1 — large, serif
current["type_font_h1"] = "heading"
current["type_size_h1"] = "64"
current["type_line_height_h1"] = "display-tight"
current["type_letter_spacing_h1"] = "heading-normal"
current["type_case_h1"] = "none"

# H2 — section titles
current["type_font_h2"] = "heading"
current["type_size_h2"] = "40"
current["type_line_height_h2"] = "display-loose"
current["type_case_h2"] = "none"

# H3
current["type_font_h3"] = "heading"
current["type_size_h3"] = "28"
current["type_line_height_h3"] = "heading-tight"
current["type_letter_spacing_h3"] = "heading-normal"
current["type_case_h3"] = "none"

# Body text
current["type_size_paragraph"] = "16"

# ── 4. Update Button Styles ───────────────────────────────────────────
print("🔘 Updating button styles...")
current["button_border_radius_primary"] = 100       # Pill/rounded buttons (like main site)
current["button_border_radius_secondary"] = 100
current["primary_button_border_width"] = 0
current["secondary_button_border_width"] = 2
current["inputs_border_radius"] = 8
current["popover_border_radius"] = 12

# ── 5. Update Global Settings ─────────────────────────────────────────
print("⚙️  Updating global settings...")
current["page_width"] = "wide"
current["cart_type"] = "drawer"
current["icon_stroke"] = "thin"

# Badge styling
current["badge_position"] = "top-right"
current["badge_corner_radius"] = 100
current["badge_text_transform"] = "none"

# ── 6. Push updated settings ──────────────────────────────────────────
print("📤 Pushing updated settings to Shopify...")
updated_value = json.dumps(settings)
result = api_put(f"/themes/{THEME_ID}/assets.json", {
    "asset": {
        "key": "config/settings_data.json",
        "value": updated_value
    }
})

print("✅ Theme settings updated successfully!")
print(f"   Theme: {result['asset']['key']}")
print(f"   Updated at: {result['asset']['updated_at']}")
print()
print("🔗 Preview your store at:")
print(f"   https://{SHOP}")
print(f"   Admin: https://{SHOP}/admin/themes/{THEME_ID}/editor")
