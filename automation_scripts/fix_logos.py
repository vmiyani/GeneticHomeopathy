import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

nav_pattern = r'<a href="index\.html" class="nav__logo" id="nav-logo">[\s\S]*?<span class="nav__logo-text">Genetic<span>Homeopathy</span></span>\s*</a>'
nav_replacement = r'''<a href="index.html" class="nav__logo" id="nav-logo">
        <img src="assets/images/logo.png" alt="Genetic Homeopathy Logo" class="nav__logo-img" width="180" height="auto">
      </a>'''

# For the footer, we want to replace <div class="footer__logo">Genetic<span>Homeopathy</span></div>
footer_pattern = r'<div class="footer__logo">Genetic<span>Homeopathy</span></div>'
footer_replacement = r'<img src="assets/images/logo.png" alt="Genetic Homeopathy Logo" class="footer__logo-img" width="200" height="auto" style="margin-bottom: 1rem;">'


for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()
    
    content = re.sub(nav_pattern, nav_replacement, content)
    content = re.sub(footer_pattern, footer_replacement, content)
    
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Updated {filename}")
