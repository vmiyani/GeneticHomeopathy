from PIL import Image
import os
import glob
import re

# 1. Create a white version of the logo for the footer
img_path = 'assets/images/logo-icon.png'
out_path = 'assets/images/logo-icon-footer.png'

img = Image.open(img_path).convert("RGBA")
data = img.getdata()

new_data = []
for item in data:
    # item is (R, G, B, A)
    # Give all visible pixels a crisp white color, preserving their original alpha (transparency)
    if item[3] > 0:
        new_data.append((255, 255, 255, item[3]))
    else:
        new_data.append(item)

white_img = Image.new("RGBA", img.size)
white_img.putdata(new_data)
white_img.save(out_path, "PNG")
print(f"Successfully generated {out_path} for footer placement.")

# 2. Update HTML footers globally
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The footer logo uses this exact snippet based on our recent unification
    old_logo_tag = '<image x="0" y="0" width="170" height="120" href="assets/images/logo-icon.png" />'
    new_logo_tag = '<image x="0" y="0" width="170" height="120" href="assets/images/logo-icon-footer.png" />'
    
    # We must only replace it inside the footer block
    # Find the footer bounds
    footer_start = content.find('<footer class="footer" id="site-footer">')
    if footer_start != -1:
        # replace the specific target within the substring from footer_start onwards
        pre_footer = content[:footer_start]
        post_footer = content[footer_start:]
        post_footer = post_footer.replace(old_logo_tag, new_logo_tag)
        content = pre_footer + post_footer
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Globally updated footer logo across {len(html_files)} files.")
