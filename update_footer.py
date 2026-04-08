import os
import glob
import re

html_files = glob.glob('*.html')

new_block = '''<div>
          <h4 class="footer__heading">What We Treat</h4>
          <nav class="footer__links" aria-label="Treatment categories">
            <a href="treatment-skin.html" class="footer__link">Skin Diseases</a>
            <a href="treatment-respiratory.html" class="footer__link">Respiratory Conditions</a>
            <a href="treatment-digestive.html" class="footer__link">Digestive Disorders</a>
            <a href="treatment-mental.html" class="footer__link">Mental & Emotional Health</a>
            <a href="treatment-joint.html" class="footer__link">Joint & Musculoskeletal</a>
            <a href="treatment-women.html" class="footer__link">Women's Health</a>
            <a href="treatment-pediatric.html" class="footer__link">Pediatric Care</a>
            <a href="treatment-kidney.html" class="footer__link">Kidney & Urinary</a>
            <a href="treatment-hair.html" class="footer__link">Hair Health</a>
          </nav>
        </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the Resources block
    # We will match from <div>\s*<h4 class="footer__heading">Resources</h4>... up to its closing </div> block right before <div>\s*<h4 class="footer__heading">Contact</h4>
    pattern = r'<div>\s*<h4 class="footer__heading">Resources</h4>\s*<nav class="footer__links"[^>]*>.*?</nav>\s*</div>'
    content = re.sub(pattern, new_block, content, flags=re.DOTALL)
    
    # 2. Remove YouTube social link
    # Matches <a ... id="social-youtube" ...>...</a>
    yt_pattern = r'<a[^>]*id="social-youtube"[^>]*>.*?</a>'
    content = re.sub(yt_pattern, '', content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated footer in {len(html_files)} files.")
