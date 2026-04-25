import os
import re

patterns = [
    (r'reducing the need for long-term NSAID medication', 'supporting the body\'s intrinsic restorative power'),
    (r'reducing the need for long-term NSAID use', 'supporting the body\'s intrinsic restorative power'),
    (r'offering natural alternatives to antibiotics and steroids', 'designed to support the body\'s natural healing processes effectively'),
    (r'without harmful side effects', 'with gentle, root-cause focused care'),
    (r'without the need for lifetime reliance on antacids or laxatives', 'by restoring the body\'s natural rhythms'),
    (r'devoid of the harsh side effects associated with frequent antibiotic or steroid use', 'designed to support the body\'s natural healing processes effectively'),
    (r'without the withdrawal symptoms associated with conventional psychiatric drugs', 'naturally and gently'),
    (r'mask the symptoms', 'address the root cause'),
    (r'synthetic hormone replacement therapies', 'external hormonal supplements'),
    (r'birth control to address hormonal issues', 'external cycle regulators')
]

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for pattern, replacement in patterns:
        new_content = re.sub(pattern, replacement, new_content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned extra: {filepath}")

for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith('.html') or name == 'generate_full.py':
            clean_file(os.path.join(root, name))
