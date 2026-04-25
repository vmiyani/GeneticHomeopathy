import json
import urllib.request

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

raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=templates/index.json")
template = json.loads(raw["asset"]["value"])
hero_id = template.get("order", [])[0]

# Update the hero section to use the new image
template["sections"][hero_id]["settings"]["image_1"] = "shopify://shop_images/hero-slide-1.png"
template["sections"][hero_id]["settings"]["overlay_color"] = "#2c3527b3" # Slight darker overlay to make text pop

print("Pushing updated index.json to Shopify...")
result = api_put(f"/themes/{THEME_ID}/assets.json", {
    "asset": {
        "key": "templates/index.json",
        "value": json.dumps(template)
    }
})
print("Done!")
