import json
import urllib.request

SHOP = 'genetic-homeopathy.myshopify.com'
TOKEN = 'YOUR_TOKEN_HERE'
GRAPHQL_URL = f'https://{SHOP}/admin/api/2024-10/graphql.json'

def graphql(query, variables=None):
    data = json.dumps({'query': query, 'variables': variables}).encode()
    req = urllib.request.Request(GRAPHQL_URL, data=data, method='POST',
                                headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

print(graphql('''
mutation {
  menu1: menuCreate(
    title: "Quick Links",
    handle: "gh-quick-links",
    items: [
      {title: "Home", type: HTTP, url: "https://www.genetichomeopathy.ca/"},
      {title: "Shop", type: CATALOG},
      {title: "Contact", type: HTTP, url: "https://www.genetichomeopathy.ca/contact.html"}
    ]
  ) {
    menu { id handle }
    userErrors { field message }
  }
  menu2: menuCreate(
    title: "What We Treat",
    handle: "gh-what-we-treat",
    items: [
      {title: "Digestive Issue", type: HTTP, url: "https://www.genetichomeopathy.ca/we-treat.html#digestive"},
      {title: "Immunity Issues", type: HTTP, url: "https://www.genetichomeopathy.ca/we-treat.html#immunity"},
      {title: "Skin Issues", type: HTTP, url: "https://www.genetichomeopathy.ca/we-treat.html#skin"},
      {title: "Mental Health", type: HTTP, url: "https://www.genetichomeopathy.ca/we-treat.html#mental"}
    ]
  ) {
    menu { id handle }
    userErrors { field message }
  }
}
'''))
