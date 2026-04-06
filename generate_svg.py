import base64

with open('assets/images/logo-icon.png', 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 120" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&amp;family=Inter:wght@700&amp;display=swap');
      .brand-title {{
        font-family: 'Playfair Display', serif;
        font-size: 46px;
        font-weight: 700;
        fill: #1a3a4a;
      }}
      .brand-subtitle {{
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        font-weight: 700;
        fill: #7cb342;
        letter-spacing: 0.35em;
      }}
    </style>
  </defs>
  
  <!-- Icon Image -->
  <image x="0" y="0" width="120" height="120" href="data:image/png;base64,{b64_data}" />
  
  <!-- Text Elements -->
  <text x="125" y="66" class="brand-title">Genetic</text>
  <text x="130" y="98" class="brand-subtitle">HOMEOPATHY</text>
</svg>
"""

with open('assets/images/logo.svg', 'w') as f:
    f.write(svg_content)
    
print("Created logo.svg")
