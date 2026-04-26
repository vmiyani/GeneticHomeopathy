import json

with open("index_updated.json", "r") as f:
    data = json.load(f)

# 3. Add "Shop by Brand" (collection_list)
collection_list = {
    "type": "collection-list",
    "blocks": {
        "group_1": {
            "type": "group",
            "name": "Header",
            "settings": {
                "content_direction": "column",
                "vertical_on_mobile": True,
                "horizontal_alignment": "center",
                "vertical_alignment": "center",
                "gap": 16,
                "width": "fill",
                "padding-block-end": 24
            },
            "blocks": {
                "text_1": {
                    "type": "text",
                    "settings": {
                        "text": "<h3>Shop by Brand</h3>",
                        "type_preset": "rte",
                        "font": "var(--font-body--family)",
                        "width": "fit-content",
                        "alignment": "center"
                    }
                }
            },
            "block_order": ["text_1"]
        }
    },
    "block_order": ["group_1"],
    "settings": {
        "collection_list": [],
        "layout_type": "grid",
        "columns": 3,
        "mobile_columns": "2",
        "padding-block-start": 48,
        "padding-block-end": 48
    }
}
data["sections"]["shop_by_brand"] = collection_list

if "shop_by_brand" not in data["order"]:
    data["order"].insert(1, "shop_by_brand")

with open("index_updated.json", "w") as f:
    json.dump(data, f, indent=2)

print("Added shop by brand")
