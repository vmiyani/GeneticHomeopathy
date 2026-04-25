import json
import urllib.request
import urllib.error

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

print("Updating footer-group.json...")
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=sections/footer-group.json")
footer = json.loads(raw["asset"]["value"])

if "section_jehhzd" in footer["sections"]:
    b1 = footer["sections"]["section_jehhzd"]["blocks"]["group_wErUQf"]
    
    b1["blocks"] = {}
    
    # 1. Add Logo / Text block
    b1["blocks"]["text_brand"] = {
        "type": "text",
        "settings": {
            "text": "<h3>Genetic Homeopathy</h3>"
        }
    }
    
    # 2. Add Quick Links Menu block
    b1["blocks"]["menu_quick"] = {
        "type": "menu",
        "settings": {
            "heading": "Quick Links",
            "menu": "gh-quick-links"
        }
    }
    
    # 3. Add Contact Text block (Email and Phone, NO ADDRESS)
    b1["blocks"]["text_contact"] = {
        "type": "text",
        "settings": {
            "text": "<h3>Contact</h3><p>📞 (905) 545-0211<br>✉️ riddhi@genetichomeopathy.ca</p>"
        }
    }
    
    # 4. Email Sign Up group
    b1["blocks"]["group_signup"] = {
        "type": "group",
        "settings": {
            "content_direction": "column"
        },
        "blocks": {
            "text_signup": {
                "type": "text",
                "settings": {
                    "text": "<h3>Join our community</h3><p>Subscribe for insights into holistic wellness and exclusive offers.</p>"
                }
            },
            "email_signup": {
                "type": "email-signup",
                "settings": {
                    "inherit_color_scheme": True,
                    "border_style": "underline",
                    "border_width": 1,
                    "input_type_preset": "h4",
                    "label": "Email address",
                    "integrated_button": True,
                    "display_type": "text"
                }
            }
        },
        "block_order": ["text_signup", "email_signup"]
    }
    
    # Define block order for footer
    b1["block_order"] = ["text_brand", "menu_quick", "text_contact", "group_signup"]

api_put(f"/themes/{THEME_ID}/assets.json", {"asset": {"key": "sections/footer-group.json", "value": json.dumps(footer)}})
print("Complete!")
