import os
import re

svg_pattern = r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 120"(.*?)>\s*<image x="0" y="0" width="120" height="120" href="assets/images/logo-icon.png" />\s*<text x="130"([^>]+)>([^<]+)</text>\s*<text x="135"([^>]+)>([^<]+)</text>\s*</svg>'

replacement_nav = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 120" class="nav__logo-svg">
          <image x="0" y="0" width="170" height="120" href="assets/images/logo-icon.png" />
          <text x="180" y="70" class="logo-svg-title">Genetic</text>
          <text x="185" y="105" class="logo-svg-subtitle">HOMEOPATHY</text>
        </svg>"""

replacement_footer = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 120" class="footer__logo-svg">
              <image x="0" y="0" width="170" height="120" href="assets/images/logo-icon.png" />
              <text x="180" y="70" class="logo-svg-title" fill="#ffffff">Genetic</text>
              <text x="185" y="105" class="logo-svg-subtitle">HOMEOPATHY</text>
            </svg>"""

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r') as f:
            content = f.read()
        
        # Replace nav logo
        new_content = re.sub(
            r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 120" class="nav__logo-svg">.*?HOMEOPATHY</text>\s*</svg>',
            replacement_nav,
            content,
            flags=re.DOTALL
        )
        
        # Replace footer logo
        new_content = re.sub(
            r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 120" class="footer__logo-svg">.*?HOMEOPATHY</text>\s*</svg>',
            replacement_footer,
            new_content,
            flags=re.DOTALL
        )
        
        if new_content != content:
            with open(file, 'w') as f:
                f.write(new_content)
            print(f"Updated {file}")
