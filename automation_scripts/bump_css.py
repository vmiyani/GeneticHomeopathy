import os
import re

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r') as f:
            content = f.read()
        
        # Replace styles.css?v=3 (or v=2) with v=4
        new_content = re.sub(r'css/styles\.css\?v=\d+', 'css/styles.css?v=4', content)
        
        if new_content != content:
            with open(file, 'w') as f:
                f.write(new_content)
            print(f"Bumped cache in {file}")
