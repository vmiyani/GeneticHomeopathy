import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Global Button updates
    content = content.replace("Book Free Consultation", "Book Consultation")
    
    # 2. specific fixes for free/complimentary
    if "reviews.html" in file:
        content = content.replace("Book your free consultation today.", "Book your consultation today.")
    
    if "about.html" in file:
        content = content.replace("Book a complimentary consultation and see why", "Book a consultation and see why")
        
    if "about-homeopathy.html" in file:
        content = content.replace("Book a complimentary consultation to discover", "Book a consultation to discover")
        
    if "faq.html" in file:
        old_faq = "Your <strong>first introductory consultation is complimentary</strong> — we believe everyone should have access to homeopathic guidance without financial barriers. During this 45-minute session, we'll assess your health profile and provide initial recommendations."
        new_faq = "We believe everyone should have access to homeopathic guidance. Our <strong>First Consultation is $80</strong> (which includes a comprehensive 45-minute health profile assessment), and <strong>Follow-Up Sessions are $60</strong>. Importantly, all customized homeopathic medicine is strictly <strong>included at no extra cost</strong>."
        content = content.replace(old_faq, new_faq)

    # 3. Modify contact.html to inject the pricing module card!
    if "contact.html" in file:
        promo_card = '''<div class="promo-card" style="background: var(--cream-100); border: 2px dashed var(--sage-400); border-radius: var(--radius-lg); padding: var(--space-4); margin: var(--space-4) 0 var(--space-6) 0;">
            <h4 style="color: var(--sage-700); margin-bottom: var(--space-2); display: flex; align-items: center; gap: var(--space-2);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width: 20px; height: 20px;"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
              Special Promotional Offer
            </h4>
            <p style="font-size: 0.95rem; margin-bottom: var(--space-3); color: var(--text-color);">Start your healing journey with affordable, personalized care:</p>
            <ul style="list-style: none; padding: 0; margin: 0; font-weight: 600; color: var(--text-color); font-size: 0.95rem;">
              <li style="margin-bottom: var(--space-2); display: flex; align-items: center; gap: var(--space-2);"><span style="color: var(--primary);">•</span> First Consultation: $80</li>
              <li style="margin-bottom: var(--space-2); display: flex; align-items: center; gap: var(--space-2);"><span style="color: var(--primary);">•</span> Follow-Up Sessions: $60</li>
              <li style="padding-top: var(--space-2); border-top: 1px solid var(--border); margin-top: var(--space-2); display: flex; align-items: center; gap: var(--space-2); color: var(--sage-700);">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" style="width: 18px; height: 18px;"><polyline points="20 6 9 17 4 12"/></svg>
                Medicine included at no extra cost
              </li>
            </ul>
          </div>'''
        
        # Replace the <p> associated with the free consultation
        content = re.sub(r'<p>\s*Connect with Dr\. Mayani for a personalized consultation.*?complimentary.*?</p>', promo_card, content, flags=re.DOTALL)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated pricing details across {len(html_files)} files.")
