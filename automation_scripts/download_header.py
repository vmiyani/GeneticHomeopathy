import json
import urllib.request

SHOP = 'genetic-homeopathy.myshopify.com'
TOKEN = 'YOUR_TOKEN_HERE'
THEME_ID = '138759471179'
API_URL = f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json?asset[key]=sections/header.liquid'

req = urllib.request.Request(API_URL, headers={'X-Shopify-Access-Token': TOKEN})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
        liquid_content = data['asset']['value']
        with open('header.liquid', 'w') as f:
            f.write(liquid_content)
        print("Successfully downloaded header.liquid")
except Exception as e:
    print(f"Error: {e}")
