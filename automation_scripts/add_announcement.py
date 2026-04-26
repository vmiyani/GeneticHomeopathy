import json

with open('header_group_raw.json', 'r') as f:
    header_group = json.load(f)

# The section type is "header-announcements"
# We add it before the header menu.
header_group['sections']['announcement_bar'] = {
    "type": "header-announcements",
    "blocks": {
        "announcement_1": {
            "type": "_announcement",
            "settings": {
                "text": "Free Canada-Wide Shipping on Orders Over $50"
            }
        }
    },
    "block_order": ["announcement_1"],
    "settings": {
        "color_scheme": "scheme-4",
        "padding-block-start": 10,
        "padding-block-end": 10
    }
}

# Add to the beginning of the order
if 'announcement_bar' not in header_group['order']:
    header_group['order'].insert(0, 'announcement_bar')

with open('header_group_new.json', 'w') as f:
    json.dump(header_group, f, indent=2)

