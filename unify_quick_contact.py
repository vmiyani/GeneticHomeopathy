import os
import re

quick_contact_html = """  <div class="quick-contact" id="quick-contact">
    <a href="tel:+18258890473" class="quick-contact__btn quick-contact__btn--phone" aria-label="Call us">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      <span class="quick-contact__label">Call Us</span>
    </a>
    <a href="https://wa.me/18258890473" class="quick-contact__btn quick-contact__btn--whatsapp" aria-label="WhatsApp">
      <svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.625.846 5.059 2.284 7.034L.789 23.492l4.625-1.462A11.936 11.936 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818c-2.168 0-4.183-.592-5.923-1.621l-.425-.252-2.742.868.876-2.694-.277-.44A9.777 9.777 0 0 1 2.182 12c0-5.418 4.4-9.818 9.818-9.818S21.818 6.582 21.818 12 17.418 21.818 12 21.818z"/></svg>
      <span class="quick-contact__label">WhatsApp</span>
    </a>
    <a href="contact.html" class="quick-contact__btn quick-contact__btn--book" aria-label="Book appointment">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
      <span class="quick-contact__label">Book Appointment</span>
    </a>
    <a href="mailto:rm.genetichomeopathy@gmail.com" class="quick-contact__btn quick-contact__btn--email" aria-label="Email us">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
      <span class="quick-contact__label">Email Us</span>
    </a>
  </div>"""

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r') as f:
            content = f.read()
        
        # Replace existing quick-contact div
        # Regex explanation: match `<div class="quick-contact" id="quick-contact">`
        # and non-greedily everything up to its closing `</div>` right before the next `<!--` or `<` or `\n\n`
        # Simple balanced approach for known html structure:
        new_content = re.sub(
            r'  <div class="quick-contact" id="quick-contact">.*?</div>\n',
            quick_contact_html + '\n',
            content,
            flags=re.DOTALL
        )
        
        if new_content != content:
            with open(file, 'w') as f:
                f.write(new_content)
            print(f"Updated {file}")
