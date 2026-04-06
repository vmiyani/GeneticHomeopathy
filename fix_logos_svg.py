import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The current blocks
nav_pattern = r'<img src="assets/images/logo-icon\.png" alt="Genetic Homeopathy Icon" class="nav__logo-icon-img"(.*)>[\s\S]*?<span class="nav__logo-text">Genetic<span>Homeopathy</span></span>'
nav_replacement = r'<img src="assets/images/logo-light.svg" alt="Genetic Homeopathy" class="nav__logo-full-img" style="height: 65px; width: auto; object-fit: contain;">'

footer_pattern = r'<img src="assets/images/logo-icon\.png" alt="Genetic Homeopathy Icon" class="footer__logo-icon-img"(.*)>[\s\S]*?<span class="footer__logo-text">Genetic<span>Homeopathy</span></span>'
footer_replacement = r'<img src="assets/images/logo-dark.svg" alt="Genetic Homeopathy" class="footer__logo-full-img" style="height: 80px; width: auto; object-fit: contain;">'

for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()
    
    content = re.sub(nav_pattern, nav_replacement, content)
    content = re.sub(footer_pattern, footer_replacement, content)
    
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Updated {filename}")
