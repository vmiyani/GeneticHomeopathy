import urllib.request
import sys
import os
sys.path.append(os.getcwd())
from shopify_config import SHOP, TOKEN, THEME_ID
import urllib.parse
import json


with open('index_updated.json', 'r') as f:
    content = f.read()

data = {
    "asset": {
        "key": "templates/index.json",
        "value": content
    }
}

url = f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json'
req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={
    'X-Shopify-Access-Token': TOKEN,
    'Content-Type': 'application/json'
}, method='PUT')

try:
    with urllib.request.urlopen(req) as response:
        print(f"Successfully uploaded templates/index.json")
except Exception as e:
    print(f"Error uploading: {e}")
    if hasattr(e, 'read'):
        print(e.read().decode())
