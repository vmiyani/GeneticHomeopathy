import json
import urllib.request
import time

SHOP = 'genetic-homeopathy.myshopify.com'
TOKEN = 'YOUR_TOKEN_HERE'
GRAPHQL_URL = f'https://{SHOP}/admin/api/2024-10/graphql.json'

def graphql(query, variables=None):
    data = json.dumps({'query': query, 'variables': variables}).encode()
    req = urllib.request.Request(GRAPHQL_URL, data=data, method='POST',
                                headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

print('Creating file from URL...')
create_mut = """
mutation fileCreate($files: [FileCreateInput!]!) {
  fileCreate(files: $files) {
    files {
      id
      fileStatus
    }
    userErrors {
      field
      message
    }
  }
}
"""
variables = {
  'files': [
    {
      'alt': 'Hero Slide 1',
      'contentType': 'IMAGE',
      'originalSource': 'https://vmiyani.github.io/GeneticHomeopathy/assets/images/hero-slide-1.png'
    }
  ]
}
res = graphql(create_mut, variables)
print(json.dumps(res, indent=2))

if 'userErrors' in res['data']['fileCreate'] and res['data']['fileCreate']['userErrors']:
    print('Failed to create file.')
    exit(1)

file_id = res['data']['fileCreate']['files'][0]['id']
print(f'File created: {file_id}')

print('Waiting for processing...')
query = """
query getFile($id: ID!) {
  node(id: $id) {
    ... on GenericFile {
      id
      url
    }
    ... on MediaImage {
      id
      image {
        url
      }
    }
  }
}
"""
for i in range(10):
    time.sleep(2)
    check = graphql(query, {'id': file_id})
    node = check['data']['node']
    if node:
        print(f"Status: ready, url: {node.get('image', {}).get('url') or node.get('url')}")
        break
    else:
        print("Status: processing...")
