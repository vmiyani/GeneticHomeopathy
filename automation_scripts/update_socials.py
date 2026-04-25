import os
import re
import glob

html_files = glob.glob('*.html')
files_to_update = html_files + ['unify_top_bar.py']

fb_url = "https://www.facebook.com/profile.php?id=100094415055135"
insta_url = "https://www.instagram.com/genetic_homeopathy/"

for file in files_to_update:
    if not os.path.exists(file):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Facebook href="#" with fb_url but ONLY for aria-label="Facebook" element
    content = re.sub(r'href="#"([^>]*aria-label="Facebook")', rf'href="{fb_url}"\1 target="_blank" rel="noopener noreferrer"', content)
    
    # Replace Instagram href="#" with insta_url but ONLY for aria-label="Instagram" element
    content = re.sub(r'href="#"([^>]*aria-label="Instagram")', rf'href="{insta_url}"\1 target="_blank" rel="noopener noreferrer"', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated social links across {len(files_to_update)} files.")
