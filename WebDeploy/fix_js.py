import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the whole <script>...</script> block at the end
script_content = """<script>
    function switchPlan(plan) {
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
</script>
</body>
</html>"""

content = re.sub(r'<script>\s*function switchPlan.*?</script>\s*</body>\s*</html>', script_content, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed JS")
