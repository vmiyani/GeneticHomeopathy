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
        raise

print("Fetching settings_data.json...")
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=config/settings_data.json")
settings = json.loads(raw["asset"]["value"])

if "scheme-2" in settings.get("current", {}).get("color_schemes", {}):
    settings["current"]["color_schemes"]["scheme-2"]["settings"]["text"] = "#ffffff"
    settings["current"]["color_schemes"]["scheme-2"]["settings"]["button"] = "#c9a84c"
    settings["current"]["color_schemes"]["scheme-2"]["settings"]["button_label"] = "#ffffff"
    settings["current"]["color_schemes"]["scheme-2"]["settings"]["secondary_button_label"] = "#ffffff"

print("Pushing updated settings_data.json...")
api_put(f"/themes/{THEME_ID}/assets.json", {"asset": {"key": "config/settings_data.json", "value": json.dumps(settings)}})
print("Done!")
