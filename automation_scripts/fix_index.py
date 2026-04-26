import json

with open("index_updated.json", "r") as f:
    data = json.load(f)

if "section_x8mrnx" in data["sections"]:
    del data["sections"]["section_x8mrnx"]

if "section_Ea3hn6" in data["sections"]:
    del data["sections"]["section_Ea3hn6"]

with open("index_updated.json", "w") as f:
    json.dump(data, f, indent=2)

