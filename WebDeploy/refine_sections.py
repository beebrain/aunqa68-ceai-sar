import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Refine PEOs/PLOs
content = content.replace('bg-white p-6 rounded-xl shadow-md border-l-4', 'glass p-6 rounded-xl border-l-4 bouncy-hover')

# Refine Admission
content = content.replace('bg-white p-12 rounded-xl shadow-2xl border-4 border-white relative overflow-hidden', 'glass-dark p-12 rounded-xl border-4 border-primary/20 relative overflow-hidden')
# Change inner lists
content = content.replace('bg-surface p-4 rounded-xl flex items-start gap-4', 'bg-surface/50 backdrop-blur p-4 rounded-xl flex items-start gap-4 bouncy-hover')
content = content.replace('bg-surface p-6 rounded-xl', 'bg-surface/50 backdrop-blur p-6 rounded-xl bouncy-hover')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Sections Refined")
