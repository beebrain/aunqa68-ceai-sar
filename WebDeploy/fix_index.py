import re

with open('/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Hero text
html = html.replace('A dynamic intensive journey', 'A dynamic 2-year journey')

# 2. Update Graduate Journey
journey_start = html.find('<!-- Graduate Journey -->')
journey_end = html.find('<!-- Curriculum Structure -->')

new_journey = """<!-- Graduate Journey -->
<section class="py-32 bg-primary-container/10">
<div class="max-w-[1280px] mx-auto px-8">
<div class="text-center mb-20">
<h2 class="text-4xl font-black text-primary mb-6 tracking-tighter">The Graduate Journey</h2>
<p class="text-lg text-on-surface-variant font-medium">A structured 2-year path from advanced theory to innovative thesis.</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-4 gap-8">
<!-- Year 1 Sem 1 -->
<div class="bg-white p-8 rounded-xl shadow-lg border-t-8 border-primary/40 bouncy-hover text-center">
<div class="w-20 h-20 rounded-full bg-primary-container flex items-center justify-center mx-auto mb-6">
<span class="material-symbols-outlined text-primary text-4xl">psychology</span>
</div>
<span class="text-xs font-black text-primary uppercase tracking-[0.2em] mb-4 block">Year 1 &bull; Sem 1</span>
<h3 class="text-2xl font-black text-on-surface mb-4">Core Foundations</h3>
<p class="text-sm text-on-surface-variant font-medium leading-relaxed">Building deep expertise in AI algorithms and engineering research methodologies.</p>
</div>
<!-- Year 1 Sem 2 -->
<div class="bg-white p-8 rounded-xl shadow-lg border-t-8 border-secondary/40 bouncy-hover text-center">
<div class="w-20 h-20 rounded-full bg-secondary-container flex items-center justify-center mx-auto mb-6">
<span class="material-symbols-outlined text-secondary text-4xl">model_training</span>
</div>
<span class="text-xs font-black text-secondary uppercase tracking-[0.2em] mb-4 block">Year 1 &bull; Sem 2</span>
<h3 class="text-2xl font-black text-on-surface mb-4">Advanced Tech</h3>
<p class="text-sm text-on-surface-variant font-medium leading-relaxed">Focusing on advanced programming for ML and emerging AI technologies.</p>
</div>
<!-- Year 2 Sem 1 -->
<div class="bg-white p-8 rounded-xl shadow-lg border-t-8 border-tertiary-container/40 bouncy-hover text-center">
<div class="w-20 h-20 rounded-full bg-tertiary-container flex items-center justify-center mx-auto mb-6">
<span class="material-symbols-outlined text-tertiary text-4xl">design_services</span>
</div>
<span class="text-xs font-black text-tertiary uppercase tracking-[0.2em] mb-4 block">Year 2 &bull; Sem 1</span>
<h3 class="text-2xl font-black text-on-surface mb-4">Thesis Proposal</h3>
<p class="text-sm text-on-surface-variant font-medium leading-relaxed">Designing innovative research and developing architectural prototypes.</p>
</div>
<!-- Year 2 Sem 2-3 -->
<div class="bg-primary p-8 rounded-xl shadow-2xl scale-105 border-4 border-white text-center">
<div class="w-20 h-20 rounded-full bg-white flex items-center justify-center mx-auto mb-6">
<span class="material-symbols-outlined text-primary text-4xl">emoji_events</span>
</div>
<span class="text-xs font-black text-white uppercase tracking-[0.2em] mb-4 block">Year 2 &bull; Sem 2-3</span>
<h3 class="text-2xl font-black text-white mb-4">Defense & Pub</h3>
<p class="text-sm text-white/90 font-medium leading-relaxed">Finalizing research and publishing findings in international journals.</p>
</div>
</div>
</div>
</section>
"""

if journey_start != -1 and journey_end != -1:
    html = html[:journey_start] + new_journey + html[journey_end:]

# 3. Update Curriculum Structure
curr_start = html.find('<!-- Curriculum Structure -->')
curr_end = html.find('<!-- AUNQA Standards Alignment -->')

if curr_end == -1:
    curr_end = html.find('<!-- Research Focus Area -->')

new_curr = """<!-- Curriculum Structure -->
<section class="py-32 bg-surface" id="curriculum">
<div class="max-w-[1280px] mx-auto px-8">
<div class="text-center mb-16">
<h2 class="text-4xl font-black text-primary mb-6 tracking-tighter">Curriculum Structure</h2>
<p class="text-lg text-on-surface-variant font-medium">Dive into your academic adventure.</p>
</div>
<div class="bg-surface-variant rounded-xl overflow-hidden shadow-2xl border-4 border-white">
<!-- Year Tabs -->
<div class="flex flex-wrap p-2 gap-2 bg-surface-container-high">
<button class="year-tab active flex-1 py-4 px-6 text-sm font-black uppercase tracking-widest rounded-full text-center transition-all bg-primary text-white" id="year-tab-1" onclick="switchYear(1)">Year 1</button>
<button class="year-tab flex-1 py-4 px-6 text-sm font-black uppercase tracking-widest rounded-full text-center transition-all text-on-surface-variant hover:bg-white/50" id="year-tab-2" onclick="switchYear(2)">Year 2</button>
</div>
<!-- Year Content Panels -->
<div class="p-8 md:p-12">
<!-- Year 1 Panel -->
<div class="year-panel block" id="year-panel-1">
<div class="flex gap-4 mb-10 pb-6 border-b border-primary/10">
<button class="sem-tab-1 px-8 py-3 rounded-full text-xs font-black uppercase tracking-widest bg-primary text-white transition-all shadow-md" id="sem-tab-1-1" onclick="switchSemester(1, 1)">Semester 1</button>
<button class="sem-tab-1 px-8 py-3 rounded-full text-xs font-black uppercase tracking-widest bg-white text-on-surface-variant hover:bg-primary/5 transition-all" id="sem-tab-1-2" onclick="switchSemester(1, 2)">Semester 2</button>
</div>
<div class="sem-panel-1 block" id="sem-panel-1-1">
<div class="overflow-x-auto">
<table class="w-full text-left">
<thead>
<tr class="border-b-4 border-primary/10 text-xs font-black uppercase tracking-widest text-primary">
<th class="pb-6 px-4">Code</th>
<th class="pb-6 px-4">Course Title</th>
<th class="pb-6 px-4 text-right">Credits</th>
</tr>
</thead>
<tbody class="text-base font-medium">
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-primary font-black">4095101</td><td class="py-6 px-4">ปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง</td><td class="py-6 px-4 text-right text-on-surface-variant">3(2-2-5)</td></tr>
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-primary font-black">7015906</td><td class="py-6 px-4">ระเบียบวิธีวิจัยทางวิทยาศาสตร์และวิศวกรรมศาสตร์</td><td class="py-6 px-4 text-right text-on-surface-variant">3(3-0-6)</td></tr>
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-primary font-black">7015907</td><td class="py-6 px-4">สัมมนาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์</td><td class="py-6 px-4 text-right text-on-surface-variant">1(0-2-1)</td></tr>
</tbody>
</table>
</div>
</div>
<div class="sem-panel-1 hidden" id="sem-panel-1-2">
<div class="overflow-x-auto">
<table class="w-full text-left">
<thead>
<tr class="border-b-4 border-primary/10 text-xs font-black uppercase tracking-widest text-primary">
<th class="pb-6 px-4">Code</th>
<th class="pb-6 px-4">Course Title</th>
<th class="pb-6 px-4 text-right">Credits</th>
</tr>
</thead>
<tbody class="text-base font-medium">
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-primary font-black">4095102</td><td class="py-6 px-4">การเขียนโปรแกรมขั้นสูงสำหรับการเรียนรู้ของเครื่อง</td><td class="py-6 px-4 text-right text-on-surface-variant">3(2-2-5)</td></tr>
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-primary font-black">7015101</td><td class="py-6 px-4">เทคโนโลยีอุบัติใหม่ทางวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์</td><td class="py-6 px-4 text-right text-on-surface-variant">3(3-0-6)</td></tr>
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-primary font-black">7015908</td><td class="py-6 px-4">หัวข้อพิเศษทางวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์</td><td class="py-6 px-4 text-right text-on-surface-variant">3(3-0-6)</td></tr>
</tbody>
</table>
</div>
</div>
</div>
<!-- Year 2 Panel -->
<div class="year-panel hidden" id="year-panel-2">
<div class="flex gap-4 mb-10 pb-6 border-b border-primary/10">
<button class="sem-tab-2 px-8 py-3 rounded-full text-xs font-black uppercase tracking-widest bg-primary text-white transition-all shadow-md" id="sem-tab-2-1" onclick="switchSemester(2, 1)">Semester 1</button>
<button class="sem-tab-2 px-8 py-3 rounded-full text-xs font-black uppercase tracking-widest bg-white text-on-surface-variant hover:bg-primary/5 transition-all" id="sem-tab-2-2" onclick="switchSemester(2, 2)">Semester 2</button>
<button class="sem-tab-2 px-8 py-3 rounded-full text-xs font-black uppercase tracking-widest bg-white text-on-surface-variant hover:bg-primary/5 transition-all" id="sem-tab-2-3" onclick="switchSemester(2, 3)">Semester 3</button>
</div>
<div class="sem-panel-2 block" id="sem-panel-2-1">
<div class="overflow-x-auto">
<table class="w-full text-left">
<thead>
<tr class="border-b-4 border-primary/10 text-xs font-black uppercase tracking-widest text-primary">
<th class="pb-6 px-4">Code</th>
<th class="pb-6 px-4">Course Title</th>
<th class="pb-6 px-4 text-right">Credits</th>
</tr>
</thead>
<tbody class="text-base font-medium">
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-primary font-black">7015901</td><td class="py-6 px-4">วิทยานิพนธ์ 1 (Thesis 1)</td><td class="py-6 px-4 text-right text-on-surface-variant">Credits TBA</td></tr>
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-secondary font-black">ELECTIVE</td><td class="py-6 px-4">วิชาเลือก (Elective Course)</td><td class="py-6 px-4 text-right text-on-surface-variant">3 Credits</td></tr>
</tbody>
</table>
</div>
</div>
<div class="sem-panel-2 hidden" id="sem-panel-2-2">
<div class="overflow-x-auto">
<table class="w-full text-left">
<thead>
<tr class="border-b-4 border-primary/10 text-xs font-black uppercase tracking-widest text-primary">
<th class="pb-6 px-4">Code</th>
<th class="pb-6 px-4">Course Title</th>
<th class="pb-6 px-4 text-right">Credits</th>
</tr>
</thead>
<tbody class="text-base font-medium">
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-primary font-black">7015902</td><td class="py-6 px-4">วิทยานิพนธ์ 2 (Thesis 2)</td><td class="py-6 px-4 text-right text-on-surface-variant">Credits TBA</td></tr>
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-secondary font-black">ELECTIVE</td><td class="py-6 px-4">วิชาเลือก (Elective Course)</td><td class="py-6 px-4 text-right text-on-surface-variant">3 Credits</td></tr>
</tbody>
</table>
</div>
</div>
<div class="sem-panel-2 hidden" id="sem-panel-2-3">
<div class="overflow-x-auto">
<table class="w-full text-left">
<thead>
<tr class="border-b-4 border-primary/10 text-xs font-black uppercase tracking-widest text-primary">
<th class="pb-6 px-4">Code</th>
<th class="pb-6 px-4">Course Title</th>
<th class="pb-6 px-4 text-right">Credits</th>
</tr>
</thead>
<tbody class="text-base font-medium">
<tr class="border-b border-primary/5 hover:bg-primary-container/20 transition-colors"><td class="py-6 px-4 text-primary font-black">7015903</td><td class="py-6 px-4">วิทยานิพนธ์ 3 (Thesis 3)</td><td class="py-6 px-4 text-right text-on-surface-variant">Credits TBA</td></tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</section>
"""

if curr_start != -1 and curr_end != -1:
    html = html[:curr_start] + new_curr + html[curr_end:]

with open('/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html updated successfully.")
