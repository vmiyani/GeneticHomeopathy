import urllib.request
import sys
import os
sys.path.append(os.getcwd())
from shopify_config import SHOP, TOKEN, THEME_ID
import json


def get_asset(asset_key, output_file):
    url = f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json?asset[key]={asset_key}'
    req = urllib.request.Request(url, headers={'X-Shopify-Access-Token': TOKEN})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            value = data['asset']['value']
            with open(output_file, 'w') as f:
                f.write(value)
            print(f"Downloaded {asset_key} to {output_file}")
    except Exception as e:
        print(f"Error downloading {asset_key}: {e}")

get_asset('sections/slideshow.liquid', 'slideshow_schema.liquid')
get_asset('sections/collection-list.liquid', 'collection_list_schema.liquid')
