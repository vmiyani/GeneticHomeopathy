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

print("Removing Announcement bar from header-group.json...")
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=sections/header-group.json")
header = json.loads(raw["asset"]["value"])

# Remove announcement bar
if "header_announcements_AwzUXA" in header.get("sections", {}):
    del header["sections"]["header_announcements_AwzUXA"]
if "order" in header and "header_announcements_AwzUXA" in header["order"]:
    header["order"].remove("header_announcements_AwzUXA")
api_put(f"/themes/{THEME_ID}/assets.json", {"asset": {"key": "sections/header-group.json", "value": json.dumps(header)}})


print("Removing Contact Text from footer-group.json...")
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=sections/footer-group.json")
footer = json.loads(raw["asset"]["value"])

if "section_jehhzd" in footer.get("sections", {}):
    b1 = footer["sections"]["section_jehhzd"]["blocks"]["group_wErUQf"]
    
    # Remove text_contact block entirely
    if "text_contact" in b1.get("blocks", {}):
        del b1["blocks"]["text_contact"]
    if "block_order" in b1 and "text_contact" in b1["block_order"]:
        b1["block_order"].remove("text_contact")

api_put(f"/themes/{THEME_ID}/assets.json", {"asset": {"key": "sections/footer-group.json", "value": json.dumps(footer)}})
print("Complete!")
