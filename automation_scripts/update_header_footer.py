import json
import urllib.request
import time

SHOP = 'genetic-homeopathy.myshopify.com'
TOKEN = 'YOUR_TOKEN_HERE'
THEME_ID = '138759471179'
API = f'https://{SHOP}/admin/api/2024-10'
GRAPHQL_URL = f'{API}/graphql.json'

def graphql(query, variables=None):
    data = json.dumps({'query': query, 'variables': variables}).encode()
    req = urllib.request.Request(GRAPHQL_URL, data=data, method='POST',
                                headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

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

print('1. Uploading Logo Image...')
create_mut = """
mutation fileCreate($files: [FileCreateInput!]!) {
  fileCreate(files: $files) {
    files { id }
    userErrors { message }
  }
}
"""
res = graphql(create_mut, {
  'files': [{'alt': 'Genetic Homeopathy Logo', 'contentType': 'IMAGE', 'originalSource': 'https://vmiyani.github.io/GeneticHomeopathy/assets/images/logo.png'}]
})
logo_id = res['data']['fileCreate']['files'][0]['id']
print(f'Logo created: {logo_id}')

print('Waiting for processing...')
time.sleep(3)

print('2. Updating settings_data.json (Logo)...')
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=config/settings_data.json")
settings = json.loads(raw["asset"]["value"])
# Extract just the filename to use in shopify:// url
settings["current"]["logo"] = "shopify://shop_images/logo.png"
settings["current"]["logo_height"] = 60
settings["current"]["logo_height_mobile"] = 50
api_put(f"/themes/{THEME_ID}/assets.json", {"asset": {"key": "config/settings_data.json", "value": json.dumps(settings)}})

print('3. Updating header-group.json...')
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=sections/header-group.json")
header = json.loads(raw["asset"]["value"])
if "header_announcements_AwzUXA" in header["sections"]:
    header["sections"]["header_announcements_AwzUXA"]["settings"]["color_scheme"] = "scheme-2" # Dark
    announce_blocks = header["sections"]["header_announcements_AwzUXA"]["blocks"]
    b_id = list(announce_blocks.keys())[0]
    announce_blocks[b_id]["settings"]["text"] = "📞 (905) 545-0211 &nbsp;&nbsp;|&nbsp;&nbsp; ✉️ riddhi@genetichomeopathy.ca &nbsp;&nbsp;|&nbsp;&nbsp; 📍 442 Dewitt Rd, Stoney Creek"
    announce_blocks[b_id]["settings"]["font"] = "var(--font-body--family)"

if "header_section" in header["sections"]:
    header["sections"]["header_section"]["settings"]["color_scheme_top"] = "scheme-1" # Sage 50

api_put(f"/themes/{THEME_ID}/assets.json", {"asset": {"key": "sections/header-group.json", "value": json.dumps(header)}})

print('4. Updating footer-group.json...')
raw = api_get(f"/themes/{THEME_ID}/assets.json?asset%5Bkey%5D=sections/footer-group.json")
footer = json.loads(raw["asset"]["value"])

if "section_jehhzd" in footer["sections"]:
    footer["sections"]["section_jehhzd"]["settings"]["color_scheme"] = "scheme-2" # Dark green background for footer
    
    # Update text to look more like the main site footer
    b1 = footer["sections"]["section_jehhzd"]["blocks"]["group_wErUQf"]
    if "group_TwfRJd" in b1["blocks"] and "text_pF6rVi" in b1["blocks"]["group_TwfRJd"]["blocks"]:
        b1["blocks"]["group_TwfRJd"]["blocks"]["text_pF6rVi"]["settings"]["text"] = "<h3>Genetic Homeopathy</h3><h3>Quick Links</h3><p>Home<br>Shop<br>Contact</p>"
    if "group_TwfRJd" in b1["blocks"] and "text_HafH7P" in b1["blocks"]["group_TwfRJd"]["blocks"]:
        b1["blocks"]["group_TwfRJd"]["blocks"]["text_HafH7P"]["settings"]["text"] = "<h3>What We Treat</h3><p>Digestive Issue<br>Immunity Issues<br>Skin Issues<br>Mental Health</p><h3>Contact</h3><p>📍 442 Dewitt Rd, Stoney Creek, ON<br>📞 (905) 545-0211</p>"

api_put(f"/themes/{THEME_ID}/assets.json", {"asset": {"key": "sections/footer-group.json", "value": json.dumps(footer)}})
print("Complete!")
