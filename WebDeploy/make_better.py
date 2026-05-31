import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace tailwind CDN and config with output.css
content = re.sub(
    r'<script src="https://cdn\.tailwindcss\.com\?plugins=forms,container-queries"></script>\s*<link href="https://fonts\.googleapis\.com/css2\?family=Dm\+Sans:wght@300;400;500;600;700;800&amp;display=swap"\s*rel="stylesheet" />\s*<link\s*href="https://fonts\.googleapis\.com/css2\?family=Material\+Symbols\+Outlined:wght,FILL@100\.\.700,0\.\.1&amp;display=swap"\s*rel="stylesheet" />\s*<script id="tailwind-config">.*?</script>\s*<style>.*?</style>',
    '''<link href="output.css" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Dm+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />''',
    content,
    flags=re.DOTALL
)

# 2. Enhance UI: Add animations to sections
content = content.replace(
    'class="py-24 bg-surface"',
    'class="py-24 bg-surface animate-fade-in-up"'
)
content = content.replace(
    'class="py-32 bg-surface-variant"',
    'class="py-32 bg-surface-variant animate-fade-in-up"'
)
content = content.replace(
    'class="py-32 bg-surface"',
    'class="py-32 bg-surface animate-fade-in-up"'
)
content = content.replace(
    'class="py-32 bg-surface-container-low"',
    'class="py-32 bg-surface-container-low animate-fade-in-up"'
)

# 3. Enhance cards with glassmorphism
content = content.replace(
    'bg-white p-8 rounded-xl shadow-lg border-2 border-white hover:border-primary',
    'glass p-8 rounded-xl hover:border-primary'
)
content = content.replace(
    'bg-white p-8 rounded-xl shadow-lg border-2 border-white hover:border-secondary',
    'glass p-8 rounded-xl hover:border-secondary'
)
content = content.replace(
    'bg-white p-8 rounded-xl shadow-lg border-2 border-white hover:border-tertiary',
    'glass p-8 rounded-xl hover:border-tertiary'
)
content = content.replace(
    'bg-white p-10 rounded-xl shadow-xl',
    'glass p-10 rounded-xl shadow-xl'
)

# 4. Interactive Tabs script improvements
js_replacement = """
    function switchPlan(plan) {
        // Simple animation logic addition
        document.querySelectorAll('.plan-tab').forEach(t => {
            t.classList.remove('active', 'bg-secondary', 'text-white');
            t.classList.add('bg-white', 'text-on-surface-variant');
        });
        const activeTab = document.getElementById('plan-tab-' + plan);
        activeTab.classList.add('active', 'bg-secondary', 'text-white');
        activeTab.classList.remove('bg-white', 'text-on-surface-variant');
        
        document.querySelectorAll('.plan-panel').forEach(p => {
            p.classList.remove('block');
            p.classList.add('hidden');
        });
        const activePanel = document.getElementById('plan-panel-' + plan);
        activePanel.classList.remove('hidden');
        activePanel.classList.add('block', 'animate-fade-in');
    }

    function switchYear(year, plan) {
        document.querySelectorAll('.year-tab-p' + plan).forEach(t => {
            t.classList.remove('active', 'bg-primary', 'text-white');
            t.classList.add('bg-white', 'text-on-surface-variant');
        });
        const activeTab = document.getElementById('year-tab-' + year + '-p' + plan);
        activeTab.classList.add('active', 'bg-primary', 'text-white');
        activeTab.classList.remove('bg-white', 'text-on-surface-variant');

        document.querySelectorAll('.year-panel-p' + plan).forEach(p => {
            p.classList.remove('block');
            p.classList.add('hidden');
        });
        const activePanel = document.getElementById('year-panel-' + year + '-p' + plan);
        activePanel.classList.remove('hidden');
        activePanel.classList.add('block', 'animate-fade-in');
    }

    function switchSemester(year, sem, plan) {
        document.querySelectorAll('.sem-tab-' + year + '-p' + plan).forEach(t => {
            t.classList.remove('active', 'bg-primary', 'text-white');
            t.classList.add('bg-white', 'text-on-surface-variant');
        });
        const activeTab = document.getElementById('sem-tab-' + year + '-' + sem + '-p' + plan);
        activeTab.classList.add('active', 'bg-primary', 'text-white');
        activeTab.classList.remove('bg-white', 'text-on-surface-variant');

        document.querySelectorAll('.sem-panel-' + year + '-p' + plan).forEach(p => {
            p.classList.remove('block');
            p.classList.add('hidden');
        });
        const activePanel = document.getElementById('sem-panel-' + year + '-' + sem + '-p' + plan);
        activePanel.classList.remove('hidden');
        activePanel.classList.add('block', 'animate-fade-in-up');
    }
"""

content = re.sub(r'function switchPlan.*?function switchSemester.*?}', js_replacement, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
