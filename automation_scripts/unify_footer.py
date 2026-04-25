import os
import glob
import re

# 1. Read the gold-standard footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract from <footer to </footer>
footer_match = re.search(r'(<footer[^>]*>.*?</footer>)', index_html, flags=re.DOTALL)
if not footer_match:
    print("Failed to find footer in index.html")
    exit(1)

gold_footer = footer_match.group(1)
html_files = glob.glob('*.html')

count = 0
for file in html_files:
    if file == 'index.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the existing footer with the gold standard footer
    new_content = re.sub(r'<footer[^>]*>.*?</footer>', gold_footer, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    count += 1

print(f"Unified footer across {count} files using index.html as the gold standard.")
