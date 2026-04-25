import json
import urllib.request
import os

SHOP = 'genetic-homeopathy.myshopify.com'
TOKEN = 'YOUR_TOKEN_HERE'
THEME_ID = '138759471179'
API_URL = f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json'

with open('header-logo.liquid', 'r') as f:
    liquid_content = f.read()

payload = {
    "asset": {
        "key": "blocks/_header-logo.liquid",
        "value": liquid_content
    }
}

req = urllib.request.Request(
    API_URL, 
    data=json.dumps(payload).encode('utf-8'),
    headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'},
    method='PUT'
)

try:
    with urllib.request.urlopen(req) as resp:
        print("Successfully uploaded modified _header-logo.liquid")
except Exception as e:
    import traceback
    traceback.print_exc()
