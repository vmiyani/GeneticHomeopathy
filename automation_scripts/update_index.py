import json

with open("index_raw.json", "r") as f:
    data = json.load(f)

# 1. Update Trust Signals in section_Y9nt3H
trust_section = data["sections"]["section_Y9nt3H"]

text_blocks = []
def find_text_blocks(obj):
    if isinstance(obj, dict):
        if obj.get("type") == "text":
            text_blocks.append(obj)
        else:
            for k, v in obj.items():
                find_text_blocks(v)
    elif isinstance(obj, list):
        for item in obj:
            find_text_blocks(item)

find_text_blocks(trust_section)

new_texts = [
    "<p><strong>📦 Canada-Wide Shipping</strong></p>", "<p>Free on orders over $50</p>",
    "<p><strong>🛡️ Authentic Products</strong></p>", "<p>Sourced directly from manufacturers</p>",
    "<p><strong>🌿 Natural & Safe</strong></p>", "<p>Gentle and effective ingredients</p>",
    "<p><strong>🔒 Secure Checkout</strong></p>", "<p>Your data is always protected</p>"
]

for i in range(min(len(text_blocks), len(new_texts))):
    text_blocks[i]["settings"]["text"] = new_texts[i]


# 2. Update Second Hero (Why Homeopathy?) - hero_w7HaTj
hero_w7HaTj_texts = []
def find_text_blocks_hero(obj):
    if isinstance(obj, dict):
        if obj.get("type") == "text":
            hero_w7HaTj_texts.append(obj)
        else:
            for k, v in obj.items():
                find_text_blocks_hero(v)

find_text_blocks_hero(data["sections"]["hero_w7HaTj"])

if len(hero_w7HaTj_texts) >= 2:
    hero_w7HaTj_texts[0]["settings"]["text"] = "<h2>Why Choose <br><em>Homeopathy?</em></h2>"
    hero_w7HaTj_texts[1]["settings"]["text"] = "<p>Discover a gentle, holistic approach to healing that stimulates your body's natural defenses without harmful side effects.</p>"

def find_buttons(obj):
    buttons = []
    def _find(o):
        if isinstance(o, dict):
            if o.get("type") == "button":
                buttons.append(o)
            else:
                for k, v in o.items():
                    _find(v)
    _find(obj)
    return buttons

hero_buttons = find_buttons(data["sections"]["hero_w7HaTj"])
if hero_buttons:
    hero_buttons[0]["settings"]["label"] = "Shop All Remedies"
    hero_buttons[0]["settings"]["link"] = "shopify://collections/all"


# 3. Add Slider
slider_section = {
    "type": "slideshow",
    "blocks": {
        "slide_1": {
            "type": "_slide",
            "settings": {
                "horizontal_alignment_flex_direction_column": "center",
                "inherit_color_scheme": False,
                "color_scheme": "scheme-6",
                "padding-inline-start": 48,
                "padding-inline-end": 48,
                "padding-block-start": 48,
                "padding-block-end": 48
            },
            "blocks": {
                "heading": {
                    "type": "text",
                    "settings": {"text": "<h2>Authentic Homeopathic<br><em>Remedies Delivered.</em></h2>", "type_preset": "h1"}
                },
                "button": {
                    "type": "button",
                    "settings": {"label": "Shop Best Sellers", "link": "shopify://collections/all"}
                }
            },
            "block_order": ["heading", "button"]
        },
        "slide_2": {
            "type": "_slide",
            "settings": {
                "horizontal_alignment_flex_direction_column": "center",
                "inherit_color_scheme": False,
                "color_scheme": "scheme-6",
                "padding-inline-start": 48,
                "padding-inline-end": 48,
                "padding-block-start": 48,
                "padding-block-end": 48
            },
            "blocks": {
                "heading": {
                    "type": "text",
                    "settings": {"text": "<h2>Discover Dr. Reckeweg<br><em>Specialties.</em></h2>", "type_preset": "h1"}
                },
                "button": {
                    "type": "button",
                    "settings": {"label": "Shop Collection", "link": "shopify://collections/all"}
                }
            },
            "block_order": ["heading", "button"]
        }
    },
    "block_order": ["slide_1", "slide_2"],
    "settings": {
        "display_mode": "full_frame",
        "section_width": "full-width",
        "autoplay": True,
        "autoplay_speed": 4
    }
}
data["sections"]["hero_p9CmMG"] = slider_section

# 4. Remove testimonial and newsletter, and rearrange order
# Current order: hero_p9CmMG, product_list_themegen, section_Y9nt3H, hero_w7HaTj, section_x8mrnx, section_Ea3hn6
# New order: hero_p9CmMG (slider later), product_list_themegen, section_Y9nt3H, hero_w7HaTj
data["order"] = [
    "hero_p9CmMG",           # Hero Slider
    "product_list_themegen", # Featured Products
    "section_Y9nt3H",        # Trust Icons
    "hero_w7HaTj"            # Why Homeopathy
]

if "section_x8mrnx" in data["sections"]:
    del data["sections"]["section_x8mrnx"]
if "section_Ea3hn6" in data["sections"]:
    del data["sections"]["section_Ea3hn6"]

with open("index_updated.json", "w") as f:
    json.dump(data, f, indent=2)

print("JSON updated successfully.")
