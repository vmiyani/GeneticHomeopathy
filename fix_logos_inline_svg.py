import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

nav_pattern = r'<a href="index\.html" class="nav__logo" id="nav-logo">[\s\S]*?</a>'
nav_replacement = r'''<a href="index.html" class="nav__logo" id="nav-logo">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 120" class="nav__logo-svg">
          <image x="0" y="0" width="120" height="120" href="assets/images/logo-icon.png" />
          <text x="130" y="70" class="logo-svg-title">Genetic</text>
          <text x="135" y="105" class="logo-svg-subtitle">HOMEOPATHY</text>
        </svg>
      </a>'''

footer_pattern = r'<a href="index\.html" class="footer__logo-link">[\s\S]*?</a>'
footer_replacement = r'''<a href="index.html" class="footer__logo-link">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 120" class="footer__logo-svg">
              <image x="0" y="0" width="120" height="120" href="assets/images/logo-icon.png" />
              <text x="130" y="70" class="logo-svg-title" fill="#ffffff">Genetic</text>
              <text x="135" y="105" class="logo-svg-subtitle">HOMEOPATHY</text>
            </svg>
          </a>'''

for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()
    
    # We first replace the a tags
    content = re.sub(nav_pattern, nav_replacement, content)
    content = re.sub(footer_pattern, footer_replacement, content)
    
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Updated {filename}")
