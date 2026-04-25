import os
import glob
import re

html_files = glob.glob('*.html')
files_to_check = html_files + ['generate_full.py', 'update_footer.py']

# Hours Replacement
old_hours = "Mon–Sun: 9 AM – 7 PM"
new_hours = "Mon–Fri: 9 AM – 7 PM, Sat–Sun: 9 AM – 5 PM"

# Common phrasing refinements (removing and rephrasing based on user's examples)
replacements = {
    # Hours
    old_hours: new_hours,
    "Mon-Sun: 9 AM – 7 PM": new_hours, # sometimes slightly different dash
    
    # Negative allopathy phrases
    "inherently safe, non-toxic, and devoid of the harsh side effects associated with frequent antibiotic or steroid use.": "exceptionally gentle, safe for all ages, and designed to support the body's natural healing processes effectively.",
    "Rather than relying on synthetic hormone replacement therapies or birth control to mask the symptoms of PCOS or Endometriosis": "Our holistic treatments work in harmony with the female body to balance hormones naturally",
    "Conventional treatments frequently rely heavily on painkillers, NSAIDs, and steroids that carry a heavy burden of long-term side effects.": "Homeopathy offers a gentle, non-invasive approach that focuses on long-term relief and metabolic recovery.",
    "Conventional medicine often relies on topical steroids and ointments that merely suppress symptoms, pushing the inflammation deeper": "Homeopathy believes in treating skin issues from within to achieve a lasting internal balance rather than temporary external relief.",
    "mask the symptoms": "support the body in resolving underlying issues",
    "suppressing symptoms": "focusing on internal restoration",
    "Contrary to conventional procedures that often forcefully sedate or temporarily mask symptoms": "Recognizing the deep link between mind and body",
    "without the withdrawal symptoms associated with conventional psychiatric drugs": "without dependency concerns or harsh systemic effects",
    "without antibiotic resistance": "by strengthening natural immunity",
    "reliance on antacids or laxatives": "systemic dependence",
    "chemical dependency": "internal reliance",
    "harsh side effects": "systemic burden",
    "toxic side effects": "harmful interactions",
    "material doses of plants for their biochemical effects — similar to how conventional drugs work": "biological extracts in a highly specific way",
    "Unlike conventional medicine": "Complementary to traditional wellness and often used",
}

def clean_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            changed = True
            
    # Case insensitive search/replace for specific keywords in a safer way
    # If "conventional medicine often" or similar is found
    patterns = [
        (re.compile(r'conventional medicine', re.IGNORECASE), "standard western protocols"),
        (re.compile(r'side effects', re.IGNORECASE), "systemic effects"),
        (re.compile(r'substances — similar to how conventional drugs work', re.IGNORECASE), "substances in a way that respects body chemistry"),
    ]
    
    # Actually, user was very specific. Let's stick to their specific strings mostly to avoid over-editing.
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned: {filepath}")

for f in files_to_check:
    clean_file(f)
