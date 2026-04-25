import os
import re

with open('we-treat.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

categories = [
    {"id": "skin", "filename": "treatment-skin.html", "title": "Skin Diseases"},
    {"id": "respiratory", "filename": "treatment-respiratory.html", "title": "Respiratory Conditions"},
    {"id": "digestive", "filename": "treatment-digestive.html", "title": "Digestive Disorders"},
    {"id": "mental", "filename": "treatment-mental.html", "title": "Mental & Emotional Health"},
    {"id": "joint", "filename": "treatment-joint.html", "title": "Joint & Musculoskeletal"},
    {"id": "women", "filename": "treatment-women.html", "title": "Women's Health"},
    {"id": "children", "filename": "treatment-pediatric.html", "title": "Pediatric"}
]

print("Updating we-treat.html with Learn More buttons...")
for cat in categories:
    # Pattern to match the entire treat-category-section
    pattern = r'(<div class="treat-category-section[^>]*data-category="' + cat["id"] + r'".*?<div class="treat-expand__list">.*?</div>)\s*</div>'
    match = re.search(pattern, base_html, flags=re.DOTALL)
    if match:
        original_inner = match.group(1)
        button_html = f'''
        <div style="margin-top: var(--space-8); display: flex; justify-content: center;">
          <a href="{cat["filename"]}" class="btn btn--primary" style="display: inline-flex; align-items: center; gap: var(--space-2);">
            Learn More About {cat["title"]} Care 
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width: 16px; height: 16px;"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </a>
        </div>'''
        new_block = original_inner + button_html + '\n      </div>'
        base_html = base_html.replace(match.group(0), new_block)
    else:
        print(f"Failed to find match for {cat['id']}")

with open('we-treat.html', 'w', encoding='utf-8') as f:
    f.write(base_html)
print("we-treat.html updated successfully!")
