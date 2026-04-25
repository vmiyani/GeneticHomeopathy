import json
import urllib.request

SHOP = 'genetic-homeopathy.myshopify.com'
TOKEN = 'YOUR_TOKEN_HERE'
THEME_ID = '138759471179'
API_URL = f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json?asset[key]=config/settings_data.json'

req = urllib.request.Request(API_URL, headers={'X-Shopify-Access-Token': TOKEN})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
        settings_data = json.loads(data['asset']['value'])
        
        # update logo
        settings_data['current']['logo'] = "shopify://shop_images/logo.svg"
        
        # We need a proper height for the logo because the horizontal logo is wide (500x120 aspect ratio is ~ 4.16).
        # Normal height for header might be 60px max width 250px
        # Let's set logo_height carefully
        settings_data['current']['logo_height'] = 60
        settings_data['current']['logo_height_mobile'] = 45

        new_content = json.dumps(settings_data, indent=2)
        
        put_req = urllib.request.Request(
            f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json',
            data=json.dumps({
                "asset": {
                    "key": "config/settings_data.json",
                    "value": new_content
                }
            }).encode('utf-8'),
            headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'},
            method='PUT'
        )
        with urllib.request.urlopen(put_req) as put_resp:
            print("Successfully updated settings_data.json logic")
            
except Exception as e:
    import traceback
    traceback.print_exc()
