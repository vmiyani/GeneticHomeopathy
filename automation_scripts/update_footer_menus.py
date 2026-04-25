import json
import urllib.request
import urllib.error
import string
import random

SHOP = 'genetic-homeopathy.myshopify.com'
TOKEN = 'YOUR_TOKEN_HERE'
THEME_ID = '138759471179'
API = f'https://{SHOP}/admin/api/2024-10'

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
        print("API Error:", e.code, e.reason)
        print("Response body:", e.read().decode())
        raise

def generate_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print("Updating footer-group.json to use interactive menus...")
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=sections/footer-group.json")
footer = json.loads(raw["asset"]["value"])

if "section_jehhzd" in footer["sections"]:
    b1 = footer["sections"]["section_jehhzd"]["blocks"]["group_wErUQf"]
    
    # We want to replace the `group_TwfRJd` text block completely with a menu blocks.
    # Actually, we can just put a menu block next to the contact info text block.
    # Let's clear the inner blocks.
    b1["blocks"] = {}
    
    # Add Logo / Text block
    b1["blocks"]["text_brand"] = {
        "type": "text",
        "settings": {
            "text": "<h3>Genetic Homeopathy</h3>"
        }
    }
    
    # Add Quick Links Menu block
    b1["blocks"]["menu_quick"] = {
        "type": "menu",
        "settings": {
            "heading": "Quick Links",
            "menu": "gh-quick-links"
        }
    }
    
    # Add What We Treat Menu block
    b1["blocks"]["menu_treat"] = {
        "type": "menu",
        "settings": {
            "heading": "What We Treat",
            "menu": "gh-what-we-treat"
        }
    }
    
    # Add Contact Text block
    b1["blocks"]["text_contact"] = {
        "type": "text",
        "settings": {
            "text": "<h3>Contact</h3><p>📍 442 Dewitt Rd, Stoney Creek, ON<br>📞 (905) 545-0211</p>"
        }
    }
    
    # Define block order
    b1["block_order"] = ["text_brand", "menu_quick", "menu_treat", "text_contact"]

api_put(f"/themes/{THEME_ID}/assets.json", {"asset": {"key": "sections/footer-group.json", "value": json.dumps(footer)}})
print("Complete!")
