import os
import re

html_files = ['courses.html', 'staff.html']

for file in html_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(
            r'<script src="https://cdn\.tailwindcss\.com.*?"></script>\s*<link href="https://fonts\.googleapis\.com/css2\?family=Dm\+Sans:wght@300;400;500;600;700;800&amp;display=swap"\s*rel="stylesheet" />\s*<link\s*href="https://fonts\.googleapis\.com/css2\?family=Material\+Symbols\+Outlined:wght,FILL@100\.\.700,0\.\.1&amp;display=swap"\s*rel="stylesheet" />\s*<script id="tailwind-config">.*?</script>\s*<style>.*?</style>',
            '''<link href="output.css" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Dm+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />''',
            content,
            flags=re.DOTALL
        )
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
