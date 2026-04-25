import json
import urllib.request
import urllib.parse
import sys

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
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

print("📥 Fetching index.json template...")
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=templates/index.json")
template = json.loads(raw["asset"]["value"])

hero_id = template.get("order", [])[0]
hero_section = template["sections"][hero_id]

# Find the group block
group_id = hero_section["block_order"][0]
group_block = hero_section["blocks"][group_id]

# The group block contains the text and button blocks
blocks = group_block["blocks"]
block_order = group_block["block_order"]

# Assuming order is Title, Subtitle, Button
title_id = block_order[0]
subtitle_id = block_order[1]
button_id = block_order[2]

# Update Title
blocks[title_id]["settings"]["text"] = "<h2>Healing from <br><em>the Root.</em></h2>"
blocks[title_id]["settings"]["type_preset"] = "h1"

# Update Subtitle
blocks[subtitle_id]["settings"]["text"] = "<p>Explore our curated collection of carefully formulated homeopathic medicines. Delivered to your doorstep.</p>"
blocks[subtitle_id]["settings"]["font_size"] = "1.125rem"

# Update Button
blocks[button_id]["settings"]["label"] = "Shop Medicines"
blocks[button_id]["settings"]["link"] = "shopify://collections/all"
blocks[button_id]["settings"]["style_class"] = "button" # Primary button

# Add Label (above title)
import time
label_id = f"text_{int(time.time())}"
blocks[label_id] = {
    "type": "text",
    "settings": {
        "text": "<p><strong>GENETIC HOMEOPATHY</strong></p>",
        "font_size": "0.75rem",
        "letter_spacing": "widest",
        "color": "#c9a84c" # Gold accent
    }
}
# Insert label at beginning
group_block["block_order"] = [label_id, title_id, subtitle_id, button_id]

# Update color scheme so it uses scheme-3 (dark sage with white text) or overlay
hero_section["settings"]["color_scheme"] = "scheme-1"
hero_section["settings"]["overlay_color"] = "#2c3527a6" # Dark Sage overlay with opacity

print("📤 Pushing updated index.json to Shopify...")
result = api_put(f"/themes/{THEME_ID}/assets.json", {
    "asset": {
        "key": "templates/index.json",
        "value": json.dumps(template)
    }
})

print("✅ Homepage hero updated successfully!")
