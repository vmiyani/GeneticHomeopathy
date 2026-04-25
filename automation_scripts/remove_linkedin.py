import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove linkedin social link
    li_pattern = r'<a[^>]*id="social-linkedin"[^>]*>.*?</a>'
    content = re.sub(li_pattern, '', content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Removed LinkedIn from {len(html_files)} files.")
