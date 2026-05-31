% mko5.cls -- LaTeX class for รายงานการสัมฤทธิ์ผลของผู้เรียนระดับรายวิชา (มคอ.5)
% Uttaradit Rajabhat University — แม่แบบจาก mko5template.docx
% Compile with XeLaTeX
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{mko5}[2026/05/20 v1.0 Course Achievement Report (มคอ.5) template]

\LoadClass[a4paper,12pt]{article}

\RequirePackage[a4paper,margin=2.5cm,top=2cm,bottom=2cm]{geometry}
\RequirePackage{fontspec}
\defaultfontfeatures{Ligatures=TeX}
\setmainfont{TH Sarabun New}[Scale=1.3]
\XeTeXlinebreaklocale "th"
\XeTeXlinebreakskip = 0pt plus 1pt

\RequirePackage{array}
\RequirePackage{multirow}
\RequirePackage{makecell}
\renewcommand{\theadalign}{cc}
\renewcommand{\theadfont}{\bfseries}
\setcellgapes{3pt}
\makegapedcells
\RequirePackage{ragged2e}
\RequirePackage{titlesec}
\RequirePackage{xcolor}
\RequirePackage{calc}
\RequirePackage{longtable}
\RequirePackage{enumitem}

\renewcommand{\arraystretch}{1.35}
\setlist[itemize]{leftmargin=2em, topsep=2pt, itemsep=2pt, parsep=0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}

\newcolumntype{L}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\Centering\arraybackslash}p{#1}}
\newcommand{\mkotablesetup}{%
  \setlength{\tabcolsep}{4pt}%
  \renewcommand{\arraystretch}{1.35}%
}

\titleformat{\section}{\normalfont\bfseries\large}{}{0pt}{}
\titlespacing*{\section}{0pt}{12pt}{6pt}

\newcommand{\mkotopheader}{%
  \begin{flushright}\small มคอ.5\end{flushright}%
}

\newcommand{\mkofivetitle}{%
  \mkotopheader
  \begin{center}%
    {\Large\bfseries รายงานการสัมฤทธิ์ผลของผู้เรียนระดับรายวิชา}\\[4pt]%
    {\large\itshape COURSE ACHIEVEMENT REPORT}%
  \end{center}
  \vspace{6pt}%
}

% ===== Metadata (หัวรายงาน) =====
\makeatletter
\newcommand{\@coursecode}{}\newcommand{\coursecode}[1]{\renewcommand{\@coursecode}{#1}}
\newcommand{\@coursename}{}\newcommand{\coursename}[1]{\renewcommand{\@coursename}{#1}}
\newcommand{\@curriculumnote}{หลักสูตรใหม่/ปรับปรุง พ.ศ. 2568}
\newcommand{\curriculumnote}[1]{\renewcommand{\@curriculumnote}{#1}}
\newcommand{\@coursegroup}{}\newcommand{\coursegroup}[1]{\renewcommand{\@coursegroup}{#1}}
\newcommand{\@credits}{3 (3-0-6)}
\newcommand{\coursecredits}[1]{\renewcommand{\@credits}{#1}}
\newcommand{\@studyplan}{}\newcommand{\studyplan}[1]{\renewcommand{\@studyplan}{#1}}
\newcommand{\@semester}{}\newcommand{\semester}[1]{\renewcommand{\@semester}{#1}}
\newcommand{\@prerequisite}{ไม่มี}
\newcommand{\prerequisite}[1]{\renewcommand{\@prerequisite}{#1}}
\newcommand{\@corequisite}{ไม่มี}
\newcommand{\corequisite}[1]{\renewcommand{\@corequisite}{#1}}
\newcommand{\@studyplace}{มหาวิทยาลัยราชภัฏอุตรดิตถ์}
\newcommand{\studyplace}[1]{\renewcommand{\@studyplace}{#1}}
\newcommand{\@registered}{}\newcommand{\registeredstudents}[1]{\renewcommand{\@registered}{#1}}
\newcommand{\@completed}{}\newcommand{\completedstudents}[1]{\renewcommand{\@completed}{#1}}
\newcommand{\@instructor}{}\newcommand{\instructor}[1]{\renewcommand{\@instructor}{#1}}
\newcommand{\@coinstructors}{}\newcommand{\coinstructors}[1]{\renewcommand{\@coinstructors}{#1}}

\newcommand{\mkoheaderinfo}{%
  \mkotablesetup
  \noindent\begin{tabular}{|@{}L{4.2cm}@{}|@{}L{\dimexpr\linewidth-4.2cm-4\tabcolsep-3\arrayrulewidth\relax}@{}|}\hline
  \textbf{รหัสวิชา} & \@coursecode \\ \hline
  \textbf{วิชา} & \@coursename \\ \hline
  \textbf{หลักสูตร} & \@curriculumnote \\ \hline
  \textbf{กลุ่มวิชา} & \@coursegroup \\ \hline
  \textbf{หน่วยกิต} & \@credits \\ \hline
  \textbf{แผนการศึกษา} & \@studyplan \\ \hline
  \textbf{ภาคการศึกษา/ปีการศึกษา} & \@semester \\ \hline
  \textbf{รายวิชาที่ต้องเรียนมาก่อน} & \@prerequisite \\
  & \textit{Pre-requisites (if any)} \\ \hline
  \textbf{รายวิชาที่ต้องเรียนพร้อมกัน} & \@corequisite \\
  & \textit{Co-requisites (if any)} \\ \hline
  \textbf{สถานที่เรียน} & \@studyplace \\ \hline
  \textbf{จำนวนนักศึกษาลงทะเบียน} & \@registered \\
  & \textit{(ณ วันหมดกำหนดการเพิ่ม-ถอน)} \\ \hline
  \textbf{จำนวนนักศึกษาที่คงอยู่เมื่อสิ้นสุดภาคการศึกษา} & \@completed \\ \hline
  \textbf{อาจารย์ผู้สอน/ผู้สอนร่วม} & \@instructor%
  \ifx\@coinstructors\empty\else\par\@coinstructors\fi \\ \hline
  \end{tabular}\par\vspace{8pt}%
}

% ===== หมวดที่ 1 — กิจกรรมที่ดำเนินการจริง =====
\newcommand{\mkosectionone}{%
  \noindent\textbf{1.\ กิจกรรมการเรียนการสอนที่ได้ดำเนินการ เพื่อพัฒนาผู้เรียนให้สัมฤทธิ์ผลลัพธ์การเรียนรู้รายวิชา}\par\vspace{4pt}%
}
\newenvironment{teachingactualtable}{%
  \mkosectionone
  \mkotablesetup
  \noindent\begin{tabular}{|C{2.2cm}|L{\dimexpr\linewidth-2.2cm-2\tabcolsep-3\arrayrulewidth\relax}|}\hline
  \textbf{ผลลัพธ์การเรียนรู้รายวิชา} &
  \textbf{กิจกรรมการเรียนการสอนที่ได้ดำเนินการ} \\
  & \textit{(Actual Teaching \& Learning Activities)} \\ \hline
}{%
  \end{tabular}\par\vspace{8pt}%
}
\newcommand{\actualrow}[2]{\textbf{#1} & #2 \\ \hline}

% ===== หมวดที่ 2 — วิธีการวัดผลที่ใช้ =====
\newcommand{\mkosectiontwo}{%
  \noindent\textbf{2.\ วิธีการ/เครื่องมือที่ใช้ เพื่อวัดและประเมินการสัมฤทธิ์ผลลัพธ์การเรียนรู้รายวิชาของผู้เรียน}\par\vspace{4pt}%
}
\newenvironment{assessmentusedtable}{%
  \mkosectiontwo
  \mkotablesetup
  \noindent\begin{tabular}{|C{2.2cm}|L{\dimexpr\linewidth-2.2cm-2\tabcolsep-3\arrayrulewidth\relax}|}\hline
  \textbf{ผลลัพธ์การเรียนรู้รายวิชา} &
  \textbf{วิธีการวัดผลที่ใช้} \\
  & \textit{(Assessment Methods/Tools Used)} \\ \hline
}{%
  \end{tabular}\par\vspace{8pt}%
}
\newcommand{\assessusedrow}[2]{\textbf{#1} & #2 \\ \hline}

% ===== หมวดที่ 3 — สรุปการสัมฤทธิ์ผล =====
\newcommand{\mkosectionthree}{%
  \noindent\textbf{3.\ สรุปการสัมฤทธิ์ผลของผู้เรียนเมื่อสิ้นสุดการเรียนการสอนระดับรายวิชา}\par\vspace{6pt}%
}

% \closummaryblock{CLO1}{คำอธิบาย CLO}{เป้าหมาย %}
\newcommand{\closummaryblock}[3]{%
  \par\noindent\textbf{#1\ :}\ #2\par\vspace{2pt}%
  \noindent\textbf{เป้าหมายจำนวนนักศึกษาที่สัมฤทธิ์ผล}\ #3\%\par\vspace{4pt}%
  \mkotablesetup
  \noindent\small
  \begin{tabular}{|L{3.8cm}|C{2.2cm}|C{2.2cm}|L{\dimexpr\linewidth-8.2cm-6\tabcolsep-5\arrayrulewidth\relax}|}\hline
  & \textbf{จำนวนคน} & \textbf{ร้อยละ (\%)} & \textbf{คำอธิบาย/คำชี้แจง} \\ \hline
}
\newcommand{\achievementpass}[3]{%
  \textbf{จำนวน นศ.\ ที่สัมฤทธิ์ผล} & #1 & #2 & #3 \\ \hline
}
\newcommand{\achievementfail}[3]{%
  \textbf{จำนวน นศ.\ ที่ไม่สัมฤทธิ์ผล} & #1 & #2 & #3 \\ \hline
}
\newcommand{\closummaryend}{\end{tabular}\normalsize\par\vspace{8pt}}

% ===== หมวดที่ 4–6 — ข้อความยาว =====
\newcommand{\mkosectionfour}{%
  \par\vspace{4pt}%
  \noindent\textbf{4.\ ปัญหาหรืออุปสรรคในการดำเนินการจัดการเรียนการสอน และ/หรือการวัดและประเมินผล}\par\vspace{4pt}%
}
\newcommand{\mkosectionfive}{%
  \par\vspace{4pt}%
  \noindent\textbf{5.\ แผนการปรับปรุงในการดำเนินการจัดการเรียนการสอน และ/หรือการวัดและประเมินผลครั้งต่อไป}\par\vspace{4pt}%
}
\newcommand{\mkosectionsix}{%
  \par\vspace{4pt}%
  \noindent\textbf{6.\ ข้อเสนอแนะเพื่อให้ภาควิชา/คณะ/มหาวิทยาลัยพิจารณาดำเนินการต่อไป}\par\vspace{4pt}%
}
\newenvironment{mkotextblock}{%
  \noindent
}{%
  \par\vspace{8pt}%
}

% ===== หมวดที่ 7 — ลงลายมือชื่อ =====
\newcommand{\mkosectionseven}{%
  \par\vspace{12pt}%
  \noindent\textbf{7.\ ลงลายมือชื่ออาจารย์ผู้สอน/อาจารย์ผู้รับผิดชอบรายวิชา/คณบดีหรือรองคณบดีที่ได้รับมอบหมาย}\par\vspace{12pt}%
}
\newcommand{\mkosignaturepair}[4]{%
  % #1 instructor name #2 instructor date #3 dean name #4 dean date
  \begin{tabular}[t]{@{}p{0.48\linewidth}@{\hspace{0.04\linewidth}}p{0.48\linewidth}@{}}%
    ลงชื่อ \rule{5.5cm}{0.4pt}\par
    วันที่รายงาน #2\par\vspace{6pt}%
    \textbf{อาจารย์ผู้สอน}\par
    (#1)\par
    &
    ลงชื่อ \rule{5.5cm}{0.4pt}\par
    วันที่รายงาน #4\par\vspace{6pt}%
    \textbf{คณบดีหรือรองคณบดีที่ได้รับมอบหมาย}\par
    (#3)\par
  \end{tabular}\par
}
\makeatother

\endinput
