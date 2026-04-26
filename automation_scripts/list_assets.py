import urllib.request
import sys
import os
sys.path.append(os.getcwd())
from shopify_config import SHOP, TOKEN, THEME_ID
import json


url = f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json'
req = urllib.request.Request(url, headers={'X-Shopify-Access-Token': TOKEN})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        assets = data['assets']
        for asset in assets:
            if asset['key'].startswith('sections/') or asset['key'].startswith('templates/'):
                print(asset['key'])
except Exception as e:
    print(f"Error: {e}")
