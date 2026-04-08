import os
import glob
import re

html_files = glob.glob('*.html')
files_to_update = html_files + ['unify_top_bar.py', 'unify_footer.py']

google_map_url = "https://maps.google.com/?q=1707+62+Ave+NE,+Nisku,+AB+T4X+3C8"

for file in files_to_update:
    if not os.path.exists(file): continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Telehealth WhatsApp update
    content = content.replace("Secure, HIPAA-compliant video platform", "Telehealth consultation via WhatsApp video chat")

    # 2. Email Address update
    content = content.replace("rm.genetichomeopath@gmail.com", "Rm.genetichomeopathy@gmail.com")

    # 3. Doctor Image update
    content = content.replace("doctor-sarah.png", "doctor-riddhi.png")

    # 4. Link Google Maps
    # A. Footer: `📍 1707 62 Ave NE, Nisku, AB T4X 3C8`
    footer_target = "📍 1707 62 Ave NE, Nisku, AB T4X 3C8"
    footer_replacement = f'📍 <a href="{google_map_url}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: underline; text-decoration-color: rgba(255,255,255,0.3); text-underline-offset: 4px;">1707 62 Ave NE, Nisku, AB T4X 3C8</a>'
    if footer_target in content:
        content = content.replace(footer_target, footer_replacement)
        
    # B. Top bar: `1707 62 Ave NE, Nisku, AB` not preceded by 📍 or inside <a>
    # Pattern: \n\s*1707 62 Ave NE, Nisku, AB\n
    header_target = "          1707 62 Ave NE, Nisku, AB\n"
    header_replacement = f'          <a href="{google_map_url}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;">1707 62 Ave NE, Nisku, AB</a>\n'
    if header_target in content:
        content = content.replace(header_target, header_replacement)

    # C. Contact.html specifically:
    # <p>1707 62 Ave NE<br>Nisku, AB T4X 3C8</p>
    contact_target = "<p>1707 62 Ave NE<br>Nisku, AB T4X 3C8</p>"
    contact_replacement = f'<p><a href="{google_map_url}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;">1707 62 Ave NE<br>Nisku, AB T4X 3C8</a></p>'
    if contact_target in content:
        content = content.replace(contact_target, contact_replacement)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated final client requests across {len(files_to_update)} files.")
