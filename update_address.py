import os
import re
import glob

html_files = glob.glob('*.html')
files_to_update = html_files + ['unify_top_bar.py']

for file in files_to_update:
    if not os.path.exists(file):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    # 1. Top bar and general
    content = content.replace("Leduc County, AB, Canada", "1707 62 Ave NE, Nisku, AB")
    
    # 2. Footers: 📍 1707 62 Ave NE, Leduc County, AB T4X 3C8, Canada
    content = content.replace("📍 1707 62 Ave NE, Leduc County, AB T4X 3C8, Canada", "📍 1707 62 Ave NE, Nisku, AB T4X 3C8")
    
    # 3. contact.html specific blocks
    content = content.replace("120 Healing Path<br>Leduc County, AB, Canada 90210", "1707 62 Ave NE<br>Nisku, AB T4X 3C8")
    content = content.replace("Located in Leduc County, Alberta — serving patients across Canada", "Located in Nisku, Alberta — serving patients across Canada")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated addresses across {len(files_to_update)} files.")
