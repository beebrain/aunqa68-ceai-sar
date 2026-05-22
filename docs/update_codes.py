import re

with open('/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Thesis credits
html = html.replace('>วิทยานิพนธ์ 1 (Thesis 1)</td><td class="py-6 px-4 text-right text-on-surface-variant">Credits TBA</td>', '>วิทยานิพนธ์ 1 (Thesis 1)</td><td class="py-6 px-4 text-right text-on-surface-variant">3 Credits</td>')
html = html.replace('>วิทยานิพนธ์ 2 (Thesis 2)</td><td class="py-6 px-4 text-right text-on-surface-variant">Credits TBA</td>', '>วิทยานิพนธ์ 2 (Thesis 2)</td><td class="py-6 px-4 text-right text-on-surface-variant">3 Credits</td>')
html = html.replace('>วิทยานิพนธ์ 3 (Thesis 3)</td><td class="py-6 px-4 text-right text-on-surface-variant">Credits TBA</td>', '>วิทยานิพนธ์ 3 (Thesis 3)</td><td class="py-6 px-4 text-right text-on-surface-variant">6 Credits</td>')

# Update Elective
html = html.replace('<td class="py-6 px-4 text-secondary font-black">ELECTIVE</td>', '<td class="py-6 px-4 text-secondary font-black">XXXXXXX</td>')
html = html.replace('วิชาเลือก (Elective Course)', 'วิชาเฉพาะด้านเลือก (Elective Course)')

with open('/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")

with open('/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/website/courses.html', 'r', encoding='utf-8') as f:
    html2 = f.read()

html2 = html2.replace('7015901, 7015902, 7015903 | 12 Credits', '7015901, 7015902, 7015903 | 3, 3, 6 Credits')

with open('/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/website/courses.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print("Updated courses.html")
