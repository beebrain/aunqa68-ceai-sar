import re

with open('/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/website/courses.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_courses = """            <!-- Course 1 -->
            <div class="bg-white p-8 rounded-xl shadow-xl border-l-8 border-primary hover:shadow-2xl transition-all">
                <div class="flex items-start justify-between mb-4">
                    <div>
                        <span class="text-xs font-black text-primary uppercase tracking-[0.2em] block mb-2">4095101 | 3(2-2-5)</span>
                        <h2 class="text-2xl font-black text-on-surface mb-2">
                            <span class="text-th">ปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง</span>
                            <span class="text-en">Artificial Intelligence and Machine Learning</span>
                        </h2>
                    </div>
                    <span class="material-symbols-outlined text-primary text-3xl">psychology</span>
                </div>
                <p class="text-on-surface-variant font-medium leading-relaxed">
                    <span class="text-th">พื้นฐานของปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง การแก้ปัญหาด้วยการค้นหา การจัดการและการวิเคราะห์ข้อมูลเบื้องต้น</span>
                    <span class="text-en">Fundamentals of artificial intelligence and machine learning, problem-solving through search, and application of data analysis techniques.</span>
                </p>
            </div>

            <!-- Course 2 -->
            <div class="bg-white p-8 rounded-xl shadow-xl border-l-8 border-secondary hover:shadow-2xl transition-all">
                <div class="flex items-start justify-between mb-4">
                    <div>
                        <span class="text-xs font-black text-secondary uppercase tracking-[0.2em] block mb-2">4095102 | 3(2-2-5)</span>
                        <h2 class="text-2xl font-black text-on-surface mb-2">
                            <span class="text-th">การเขียนโปรแกรมขั้นสูงสำหรับการเรียนรู้ของเครื่อง</span>
                            <span class="text-en">Advanced Programming for Machine Learning</span>
                        </h2>
                    </div>
                    <span class="material-symbols-outlined text-secondary text-3xl">terminal</span>
                </div>
                <p class="text-on-surface-variant font-medium leading-relaxed">
                    <span class="text-th">การเขียนโปรแกรมด้วยภาษาโปรแกรมสมัยใหม่สำหรับการเรียนรู้ของเครื่อง การเตรียมและจัดการข้อมูล การทำความสะอาด และการแสดงผลข้อมูล</span>
                    <span class="text-en">Modern programming languages for machine learning, data preparation, cleaning, visualization, and version control systems.</span>
                </p>
            </div>

            <!-- Course 3 -->
            <div class="bg-white p-8 rounded-xl shadow-xl border-l-8 border-tertiary hover:shadow-2xl transition-all">
                <div class="flex items-start justify-between mb-4">
                    <div>
                        <span class="text-xs font-black text-tertiary uppercase tracking-[0.2em] block mb-2">7015101 | 3(3-0-6)</span>
                        <h2 class="text-2xl font-black text-on-surface mb-2">
                            <span class="text-th">เทคโนโลยีอุบัติใหม่ทางวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์</span>
                            <span class="text-en">Emerging Technologies in Computer Engineering and AI</span>
                        </h2>
                    </div>
                    <span class="material-symbols-outlined text-tertiary text-3xl">lightbulb</span>
                </div>
                <p class="text-on-surface-variant font-medium leading-relaxed">
                    <span class="text-th">การศึกษาด้านคอมพิวเตอร์หรือปัญญาประดิษฐ์ที่น่าสนใจ และสอดคล้องกับเทคโนโลยีปัจจุบันและเทคโนโลยีอุบัติใหม่</span>
                    <span class="text-en">Study of current interesting and relevant emerging technologies in computer engineering and artificial intelligence.</span>
                </p>
            </div>

            <!-- Course 4 -->
            <div class="bg-white p-8 rounded-xl shadow-xl border-l-8 border-primary hover:shadow-2xl transition-all">
                <div class="flex items-start justify-between mb-4">
                    <div>
                        <span class="text-xs font-black text-primary uppercase tracking-[0.2em] block mb-2">7015906 | 3(3-0-6)</span>
                        <h2 class="text-2xl font-black text-on-surface mb-2">
                            <span class="text-th">ระเบียบวิธีวิจัยทางวิทยาศาสตร์และวิศวกรรมศาสตร์</span>
                            <span class="text-en">Science and Engineering Research Methodology</span>
                        </h2>
                    </div>
                    <span class="material-symbols-outlined text-primary text-3xl">science</span>
                </div>
                <p class="text-on-surface-variant font-medium leading-relaxed">
                    <span class="text-th">ศึกษาทฤษฎีที่เกี่ยวข้องกับหลักการและระเบียบวิธีการวิจัย การทบทวนวรรณกรรม การวิเคราะห์ปัญหา การตั้งสมมติฐานและจริยธรรมการวิจัย</span>
                    <span class="text-en">Theories related to research methodology, literature review, problem analysis, hypothesis formulation, and research ethics.</span>
                </p>
            </div>

            <!-- Seminar & Special Topics -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Course 5 -->
                <div class="bg-white p-8 rounded-xl shadow-lg border border-secondary/10 relative overflow-hidden group hover:border-secondary transition-colors">
                    <div class="absolute -right-10 -top-10 w-32 h-32 bg-secondary/5 rounded-full group-hover:scale-150 transition-transform"></div>
                    <span class="text-xs font-black text-secondary uppercase tracking-[0.2em] block mb-2 relative z-10">7015907 | 1(0-2-1)</span>
                    <h4 class="text-xl font-bold text-on-surface mb-2 relative z-10">
                        <span class="text-th">สัมมนาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์</span>
                        <span class="text-en">Seminar in Computer Engineering and AI</span>
                    </h4>
                    <p class="text-sm text-on-surface-variant font-medium relative z-10">
                        <span class="text-th">ศึกษาบทความวิจัยในหัวข้อที่สนใจ การแลกเปลี่ยนความคิดเห็น และการนำเสนอบทความ</span>
                        <span class="text-en">Study of research articles, exchanging ideas, and presenting research papers.</span>
                    </p>
                </div>

                <!-- Course 6 -->
                <div class="bg-white p-8 rounded-xl shadow-lg border border-tertiary/10 relative overflow-hidden group hover:border-tertiary transition-colors">
                    <div class="absolute -right-10 -top-10 w-32 h-32 bg-tertiary/5 rounded-full group-hover:scale-150 transition-transform"></div>
                    <span class="text-xs font-black text-tertiary uppercase tracking-[0.2em] block mb-2 relative z-10">7015908 | 3(3-0-6)</span>
                    <h4 class="text-xl font-bold text-on-surface mb-2 relative z-10">
                        <span class="text-th">หัวข้อพิเศษทางวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์</span>
                        <span class="text-en">Special Topics in CE and AI</span>
                    </h4>
                    <p class="text-sm text-on-surface-variant font-medium relative z-10">
                        <span class="text-th">หัวข้อพิเศษเกี่ยวกับการใช้งานเทคโนโลยีด้านวิศวกรรมคอมพิวเตอร์และ AI ตามความสนใจเฉพาะทาง</span>
                        <span class="text-en">Specialized topics regarding the application of CE and AI technologies based on specific interests.</span>
                    </p>
                </div>
            </div>

            <!-- Thesis -->
            <div class="mt-16 pt-16 border-t border-primary/20">
                <h3 class="text-3xl font-black text-primary mb-8 text-center">
                    <span class="text-th">วิทยานิพนธ์ (Thesis)</span>
                    <span class="text-en">Thesis</span>
                </h3>
                
                <div class="bg-white p-8 rounded-xl shadow-lg border border-primary/10 relative overflow-hidden group hover:border-primary transition-colors max-w-3xl mx-auto">
                    <div class="absolute -right-10 -top-10 w-40 h-40 bg-primary/5 rounded-full group-hover:scale-150 transition-transform"></div>
                    <span class="text-xs font-black text-primary uppercase tracking-[0.2em] block mb-2 relative z-10">7015901, 7015902, 7015903 | 12 Credits</span>
                    <h4 class="text-xl font-bold text-on-surface mb-2 relative z-10">
                        <span class="text-th">วิทยานิพนธ์ 1, 2 และ 3 (Thesis 1, 2, 3)</span>
                        <span class="text-en">Master's Thesis 1, 2, 3</span>
                    </h4>
                    <p class="text-sm text-on-surface-variant font-medium relative z-10">
                        <span class="text-th">การศึกษาค้นคว้าด้วยตนเองในหัวข้อที่สนใจตามระเบียบวิธีวิจัย การทบทวนวรรณกรรมเพื่อจัดทำเค้าโครงวิทยานิพนธ์ การวิเคราะห์ข้อมูล การสรุปผล และการเขียนวิทยานิพนธ์ จนถึงสอบป้องกันและการเผยแพร่ผลงานวิจัยระดับนานาชาติ</span>
                        <span class="text-en">Independent research on topics of interest. Includes literature review, proposal development, data analysis, writing, and successful defense and publication of the research.</span>
                    </p>
                </div>
            </div>
"""

start_str = '<div class="max-w-[1000px] mx-auto px-8 space-y-12">'
end_str = '</div>\n    </main>'

start_idx = html.find(start_str)
end_idx = html.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx + len(start_str)] + '\n' + new_courses + '\n' + html[end_idx:]
    with open('/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/website/courses.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("courses.html updated successfully.")
else:
    print("Could not find the injection points in courses.html")

