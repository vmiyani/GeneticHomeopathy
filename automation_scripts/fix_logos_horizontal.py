import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll replace the recently added logo.png tags with the new structure.
nav_pattern = r'<img src="assets/images/logo\.png" alt="Genetic Homeopathy Logo" class="nav__logo-img" width="180" height="auto">'
nav_replacement = r'''<img src="assets/images/logo-icon.png" alt="Genetic Homeopathy Icon" class="nav__logo-icon-img" width="48" height="48">
        <span class="nav__logo-text">Genetic<span>Homeopathy</span></span>'''

footer_pattern = r'<img src="assets/images/logo\.png" alt="Genetic Homeopathy Logo" class="footer__logo-img" width="200" height="auto" style="margin-bottom: 1rem;">'
footer_replacement = r'''<a href="index.html" class="footer__logo-link">
            <img src="assets/images/logo-icon.png" alt="Genetic Homeopathy Icon" class="footer__logo-icon-img" width="56" height="56">
            <span class="footer__logo-text">Genetic<span>Homeopathy</span></span>
          </a>'''

for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()
    
    content = re.sub(nav_pattern, nav_replacement, content)
    content = re.sub(footer_pattern, footer_replacement, content)
    
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Updated {filename}")
