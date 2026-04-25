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

print("Fetching index.json...")
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=templates/index.json")
template = json.loads(raw["asset"]["value"])
hero_id = template.get("order", [])[0]

template["sections"][hero_id]["settings"]["color_scheme"] = "scheme-2"

print("Pushing updated index.json to Shopify...")
res = api_put(f"/themes/{THEME_ID}/assets.json", {"asset": {"key": "templates/index.json", "value": json.dumps(template)}})
print("Done!")
