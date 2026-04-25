import os
import glob
import re

html_files = glob.glob("*.html")

replacements = [
    (r'href="products\.html"', r'href="https://shop.genetichomeopathy.ca/"'),
    (r"window\.location\.href='products\.html'", r"window.location.href='https://shop.genetichomeopathy.ca/cart'"),
    (r'href="products\.html#([a-zA-Z0-9_-]+)"', r'href="https://shop.genetichomeopathy.ca/collections/\1"') # Just in case there are anchor links to categories
]

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for pattern, replacement in replacements:
        new_content = re.sub(pattern, replacement, new_content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated links in {file_path}")

print("Done updating HTML links.")
