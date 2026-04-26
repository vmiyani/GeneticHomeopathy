import json

# Read the original and the updated
with open("index_raw.json", "r") as f:
    original_data = json.load(f)

with open("index_updated.json", "r") as f:
    current_data = json.load(f)

# Revert the hero section
current_data["sections"]["hero_p9CmMG"] = original_data["sections"]["hero_p9CmMG"]

# Remove shop by brand
if "shop_by_brand" in current_data["sections"]:
    del current_data["sections"]["shop_by_brand"]

if "shop_by_brand" in current_data["order"]:
    current_data["order"].remove("shop_by_brand")

with open("index_updated.json", "w") as f:
    json.dump(current_data, f, indent=2)

print("Reverted hero and removed shop_by_brand")
