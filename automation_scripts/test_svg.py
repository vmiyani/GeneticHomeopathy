import json
import urllib.request
import time
import base64
import os

SHOP = 'genetic-homeopathy.myshopify.com'
TOKEN = 'YOUR_TOKEN_HERE'
GRAPHQL_URL = f'https://{SHOP}/admin/api/2024-10/graphql.json'

def graphql(query, variables=None):
    data = json.dumps({'query': query, 'variables': variables}).encode()
    req = urllib.request.Request(GRAPHQL_URL, data=data, method='POST',
                                headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

print("Testing if we can upload an SVG directly")
