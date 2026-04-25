import json
import urllib.request
import os

SHOP = 'genetic-homeopathy.myshopify.com'
TOKEN = 'YOUR_TOKEN_HERE'
THEME_ID = '138759471179'
API_URL = f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json?asset[key]=blocks/_header-logo.liquid'

req = urllib.request.Request(API_URL, headers={'X-Shopify-Access-Token': TOKEN})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
        liquid_content = data['asset']['value']
        with open('header-logo.liquid', 'w') as f:
            f.write(liquid_content)
        print("Successfully downloaded _header-logo.liquid")
except Exception as e:
    print(f"Error: {e}")
