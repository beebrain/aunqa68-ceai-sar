% mko3.cls -- LaTeX class for แผนการจัดการเรียนรู้รายวิชา (มคอ.3)
% Uttaradit Rajabhat University
% Compile with XeLaTeX
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{mko3}[2026/05/18 v1.4 Course Specification (มคอ.3 AUN-QA/SU217) template]

\LoadClass[a4paper,12pt]{article}

\RequirePackage[a4paper,margin=2.5cm,top=2cm,bottom=2cm]{geometry}
\RequirePackage{fontspec}
\defaultfontfeatures{Ligatures=TeX}
\setmainfont{TH Sarabun New}[Scale=1.3]
\newfontfamily\thaifont{TH Sarabun New}[Scale=1.3]
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

% Column types — fixed width
\newcolumntype{L}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\Centering\arraybackslash}p{#1}}
% ความกว้างตารางมาตรฐาน = เต็มพื้นที่ข้อความ
\newcommand{\mko@tw}{\linewidth}
\newcommand{\mkotablesetup}{%
  \setlength{\tabcolsep}{4pt}%
  \renewcommand{\arraystretch}{1.35}%
}
\newlength{\mkoplow}
\newlength{\mkobloomcol}
\newcommand{\mkoplowidth}[1]{%
  \setlength{\mkoplow}{%
    \dimexpr(\linewidth-1.5cm-2\tabcolsep*(#1+1)-\arrayrulewidth*(#1+2))/#1\relax}%
}
\newcommand{\mkobloomcolwidth}{%
  \setlength{\mkobloomcol}{%
    \dimexpr(\linewidth-1.4cm-10\tabcolsep-5\arrayrulewidth)/4\relax}%
}

\titleformat{\section}{\normalfont\bfseries\large}{}{0pt}{}
\titlespacing*{\section}{0pt}{12pt}{6pt}

\newcommand{\mkotopheader}{%
  \begin{flushright}\small มคอ.3 (AUN-QA)\end{flushright}%
}

\newcommand{\mkothreetitle}{%
  \mkotopheader
  \begin{center}%
    {\Large\bfseries รายละเอียดของรายวิชา}\\[4pt]%
    {\large แผนการจัดการเรียนรู้รายวิชา (มคอ.3)}%
  \end{center}
  \vspace{4pt}%
}

% ----- หัวข้อหมวด (รูปแบบ SU217) -----
\newcommand{\mkosection}[1]{%
  \clearpage
  \par\vspace{10pt}%
  \begin{center}\textbf{#1}\end{center}%
  \vspace{4pt}%
}
\newcounter{mkoSec}
\newcounter{mkoSub}
\newcommand{\mkoendsubsection}{\par\vspace{10pt}}
\newcommand{\mkosubsection}[1]{%
  \ifnum\value{mkoSub}>0 \mkoendsubsection\fi
  \refstepcounter{mkoSub}%
  \noindent\textbf{\arabic{mkoSec}.\arabic{mkoSub}\ #1}\par\vspace{4pt}%
}
\newcount\mkoOpenedSecTwo
\newcount\mkoOpenedSecThree
\newcount\mkoOpenedSecFour
\newcount\mkoOpenedSecFive
\newcount\mkoOpenedSecSix
\newcommand{\mkosectiontwo}{%
  \ifnum\mkoOpenedSecTwo>0 \else
    \global\advance\mkoOpenedSecTwo by 1\relax
    \mkosection{หมวดที่ 2 จุดมุ่งหมายและวัตถุประสงค์}%
    \setcounter{mkoSec}{2}%
    \setcounter{mkoSub}{0}%
  \fi
}
\newcommand{\mkosectionthree}{%
  \ifnum\mkoOpenedSecThree>0 \else
    \global\advance\mkoOpenedSecThree by 1\relax
    \mkosection{หมวดที่ 3 ลักษณะและการดำเนินการ}%
    \setcounter{mkoSec}{3}%
    \setcounter{mkoSub}{0}%
  \fi
}
\newcommand{\mkosectionfour}{%
  \ifnum\mkoOpenedSecFour>0 \else
    \global\advance\mkoOpenedSecFour by 1\relax
    \mkosection{หมวดที่ 4 การจัดการเรียนการสอน}%
    \setcounter{mkoSec}{4}%
    \setcounter{mkoSub}{0}%
  \fi
}
\newcommand{\mkosectionfive}{%
  \ifnum\mkoOpenedSecFive>0 \else
    \global\advance\mkoOpenedSecFive by 1\relax
    \mkosection{หมวดที่ 5 เกณฑ์การให้คะแนน (Rubric)}%
    \setcounter{mkoSec}{5}%
    \setcounter{mkoSub}{0}%
  \fi
}
\newcommand{\mkosectionsix}{%
  \ifnum\mkoOpenedSecSix>0 \else
    \global\advance\mkoOpenedSecSix by 1\relax
    \mkosection{หมวดที่ 6 ทรัพยากรประกอบการเรียนการสอน}%
    \setcounter{mkoSec}{6}%
    \setcounter{mkoSub}{0}%
  \fi
}

% ===== หมวดที่ 1 ข้อมูลทั่วไป (รูปแบบ มคอ.3 SU217 v1.65) =====
\makeatletter
\newcommand{\@institution}{มหาวิทยาลัยราชภัฏอุตรดิตถ์}
\newcommand{\institution}[1]{\renewcommand{\@institution}{#1}}
\newcommand{\@facultyunit}{คณะเทคโนโลยีอุตสาหกรรม สาขาวิชาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์}
\newcommand{\facultyunit}[1]{\renewcommand{\@facultyunit}{#1}}

\newcommand{\@coursecode}{}\newcommand{\coursecode}[1]{\renewcommand{\@coursecode}{#1}}
\newcommand{\@coursename}{}\newcommand{\coursename}[1]{\renewcommand{\@coursename}{#1}}
\newcommand{\@program}{หลักสูตรวิศวกรรมศาสตรมหาบัณฑิต สาขาวิชาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์}
\newcommand{\program}[1]{\renewcommand{\@program}{#1}}
\newcommand{\@coursegroup}{}\newcommand{\coursegroup}[1]{\renewcommand{\@coursegroup}{#1}}
\newcommand{\@credits}{3 หน่วยกิต (3-0-6)}
\newcommand{\coursecredits}[1]{\renewcommand{\@credits}{#1}}
\newcommand{\@semester}{}\newcommand{\semester}[1]{\renewcommand{\@semester}{#1}}
\newcommand{\@yearlevel}{ตามแผนการศึกษาหลักสูตรปริญญาโท}
\newcommand{\yearlevel}[1]{\renewcommand{\@yearlevel}{#1}}
\newcommand{\@instructor}{}\newcommand{\instructor}[1]{%
  \renewcommand{\@instructor}{#1}%
  \renewcommand{\mkoInstructor}{#1}%
}
\newcommand{\mkoInstructor}{}
\newcommand{\@contact}{}\newcommand{\contact}[1]{\renewcommand{\@contact}{#1}}
\newcommand{\@prerequisite}{ไม่มี}
\newcommand{\prerequisite}[1]{\renewcommand{\@prerequisite}{#1}}
\newcommand{\@corequisite}{ไม่มี}
\newcommand{\corequisite}[1]{\renewcommand{\@corequisite}{#1}}
\newcommand{\@studyplace}{มหาวิทยาลัยราชภัฏอุตรดิตถ์ (คณะเทคโนโลยีอุตสาหกรรม)}
\newcommand{\studyplace}[1]{\renewcommand{\@studyplace}{#1}}
\newcommand{\@revisiondate}{พฤษภาคม 2568}
\newcommand{\revisiondate}[1]{\renewcommand{\@revisiondate}{#1}}
\newcommand{\@coursedesc}{}\newcommand{\coursedesc}[1]{\renewcommand{\@coursedesc}{#1}}

% PLO หลักสูตรป.โท CEAI (แผนสารนิพนธ์ PLO1--PLO5) — ปรับด้วย \ploitem{n}{...}
\newcommand{\@ploone}{ใช้ซอฟต์แวร์หรือฮาร์ดแวร์ทางคอมพิวเตอร์ในการสร้างสรรค์ผลงาน องค์ความรู้ และนวัตกรรม}
\newcommand{\@plotwo}{ประยุกต์ใช้ความรู้ในสาขาวิชาวิศวกรรมคอมพิวเตอร์เพื่อแก้ไขปัญหาความต้องการขององค์กร ชุมชน และท้องถิ่น}
\newcommand{\@plothree}{สร้างต้นแบบนวัตกรรมที่ตอบสนองความต้องการขององค์กร}
\newcommand{\@plofour}{ปฏิบัติตามหลักจริยาบรรณวิชาชีพวิศวกรรมคอมพิวเตอร์}
\newcommand{\@plofive}{สามารถคิดวิเคราะห์ การสื่อสาร การทำงานร่วมกัน การปรับตัว และการเรียนรู้ตลอดชีวิต}
\newcommand{\ploitem}[2]{%
  \ifcase#1\relax
  \or \renewcommand{\@ploone}{#2}%
  \or \renewcommand{\@plotwo}{#2}%
  \or \renewcommand{\@plothree}{#2}%
  \or \renewcommand{\@plofour}{#2}%
  \or \renewcommand{\@plofive}{#2}%
  \fi
}
\newcommand{\mko@plotable}{%
  \mkosubsection{ผลลัพธ์การเรียนรู้ของหลักสูตร (PLOs)}%
  \par\small\noindent
  หลักสูตรวิศวกรรมศาสตรมหาบัณฑิต สาขาวิชาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์
  (แผนสารนิพนธ์ — PLO1--PLO5)\par\vspace{4pt}%
  \mkotablesetup
  \noindent\begin{tabular}{|C{2.6cm}|L{\dimexpr\linewidth-2.6cm-4\tabcolsep-3\arrayrulewidth\relax}|}\hline
  \textbf{PLO} & \textbf{ข้อความผลการเรียนรู้ที่คาดหวัง} \\ \hline
  \textbf{PLO1 (Create)} & \@ploone \\ \hline
  \textbf{PLO2 (Apply)} & \@plotwo \\ \hline
  \textbf{PLO3 (Create Knowledge)} & \@plothree \\ \hline
  \textbf{PLO4 (Ethics)} & \@plofour \\ \hline
  \textbf{PLO5 (Analyze/Comm./LLL)} & \@plofive \\ \hline
  \end{tabular}\normalsize
}

\newcommand{\@instructorline}{%
  \@instructor%
  \ifx\@contact\empty\else\ (\@contact)\fi%
}

\newcommand{\mkoinstitution}{%
  \mkosectionone
}

\newcommand{\mkosectionone}{%
  \begin{center}\textbf{หมวดที่ 1 ข้อมูลทั่วไป}\end{center}
  \vspace{4pt}%
  \setcounter{mkoSec}{1}%
  \setcounter{mkoSub}{0}%
  \mkosubsection{ชื่อสถาบันอุดมศึกษา}\@institution
  \mkosubsection{วิทยาเขต/คณะ/ภาควิชา}\@facultyunit
  \mkosubsection{รหัสและชื่อรายวิชา}\@coursecode\ \@coursename
  \ifx\@coursedesc\empty\else\mkosubsection{คำอธิบายรายวิชา}\@coursedesc\fi
  \mkosubsection{จำนวนหน่วยกิต}\@credits
  \mkosubsection{หลักสูตรและประเภทของรายวิชา}%
    \@program\par เป็นวิชา \@coursegroup
  \mkosubsection{อาจารย์ผู้สอน}\@instructorline
  \mkosubsection{ภาคการศึกษา/ระดับการศึกษา}%
    ภาคการศึกษา \@semester\par
    ระดับปริญญาโท (บัณฑิตศึกษา) --- \@yearlevel
  \mkosubsection{รายวิชาบังคับก่อน (ถ้ามี)}\@prerequisite
  \mkosubsection{รายวิชาที่ต้องเรียนพร้อมกัน (ถ้ามี)}\@corequisite
  \mkosubsection{สถานที่เรียน}\@studyplace
  \mkosubsection{วันที่จัดทำหรือปรับปรุงรายละเอียดของรายวิชาครั้งล่าสุด}\@revisiondate
  \mko@plotable
  \mkoendsubsection
}

% คงคำสั่งเดิมเพื่อความเข้ากันได้ (ชี้ไปรูปแบบใหม่)
\newcommand{\courseinfotable}{\mkosectionone}

% คำอธิบายรายวิชาแสดงในหมวดที่ 1.4 (หลัง 1.3 รหัสและชื่อรายวิชา) ผ่าน \coursedesc แล้ว
\newcommand{\mkocoursedesc}{}
\makeatother

% ===== หมวดที่ 6 — เอกสารและสื่อ (เพิ่มเติมจากแม่แบบ มรอ.) =====
\newenvironment{learningmaterials}{%
  \mkosectionsix
  \mkosubsection{ตำราและเอกสารที่ใช้ประกอบการเรียนการสอน}%
  \begin{itemize}
}{%
  \end{itemize}\mkoendsubsection
}
\newcommand{\matitem}[1]{\item #1}

% ===== หมวดที่ 4 ข้อ 1 — กิจกรรมที่มีในรายวิชา (รวมในการจัดการเรียนการสอน) =====
\newenvironment{courseactivities}{%
  \mkosectionfour
  \mkosubsection{กิจกรรมที่มีในรายวิชา}%
  \begin{itemize}
}{%
  \end{itemize}\mkoendsubsection
}
\newcommand{\actitem}[1]{\item #1}

% ===== หมวดที่ 2 ข้อ 1 — จุดมุ่งหมาย CLOs (SU217) =====
\newenvironment{clodomaintable}{%
  \mkosectiontwo
  \mkosubsection{จุดมุ่งหมายของรายวิชา (CLOs)}%
  \mkotablesetup
  \noindent\begin{tabular}{|C{1.5cm}|L{\dimexpr\linewidth-1.5cm-2.8cm-2cm-8\tabcolsep-4\arrayrulewidth\relax}|C{2.8cm}|C{2cm}|}\hline
  \multicolumn{2}{|c|}{\textbf{ผลลัพธ์การเรียนรู้รายวิชา (CLOs)}} &
  \multicolumn{2}{c|}{\textbf{Level of Learning Domain}} \\ \cline{3-4}
  \multicolumn{2}{|c|}{} & \textbf{Domain} & \textbf{Level} \\ \hline
}{%
  \end{tabular}\mkoendsubsection
}
\newcommand{\cloitem}[4]{\textbf{#1} & #2 & #3 & #4 \\ \hline}

% ===== 2.2 CLO ↔ PLO =====
% Usage: \begin{cloplotable}{3}{ & \textbf{PLO1} & \textbf{PLO2} & \textbf{PLO3}}
%   then write rows manually:  \textbf{CLO1} & X & & X \\ \hline
\newenvironment{cloplotable}[2]{%
  \mkosubsection{ความสอดคล้อง CLOs กับ PLOs}%
  \mkotablesetup
  \mkoplowidth{#1}%
  \noindent\begin{tabular}{|C{1.5cm}|*{#1}{>{\Centering\arraybackslash}p{\mkoplow}|}}\hline
  \textbf{CLOs} #2 \\ \hline
}{%
  \end{tabular}\mkoendsubsection
}

% ===== 2.3 Bloom + LLL =====
\newenvironment{bloomtable}{%
  \mkosubsection{ระดับการส่งเสริม (Bloom's Taxonomy และ LLL)}%
  \mkotablesetup
  \mkobloomcolwidth
  \noindent\begin{tabular}{|C{1.4cm}|C{\mkobloomcol}|C{\mkobloomcol}|C{\mkobloomcol}|C{\mkobloomcol}|}\hline
  \multirow{2}{*}{\textbf{CLOs}} & \multicolumn{3}{c|}{\textbf{Bloom's Taxonomy}} &
  \multirow{2}{*}{\makecell{\textbf{การเรียนรู้}\\\textbf{ตลอดชีวิต (LLL)}}} \\ \cline{2-4}
   & \makecell{\textbf{พุทธิพิสัย}\\Cognitive}
   & \makecell{\textbf{จิตพิสัย}\\Affective}
   & \makecell{\textbf{ทักษะพิสัย}\\Psychomotor} & \\ \hline
}{%
  \end{tabular}\mkoendsubsection
}
\newcommand{\bloomrow}[5]{\textbf{#1} & #2 & #3 & #4 & #5 \\ \hline}

% ===== 2.4 Content analysis =====
\newenvironment{contentanalysistable}{%
  \mkosubsection{การวิเคราะห์เนื้อหาให้สอดคล้องกับระดับการเรียนรู้ (Level of Learning Domain)}%
  \mkotablesetup
  \noindent\footnotesize
  \begin{tabular}{|%
    L{\dimexpr(\linewidth-8\tabcolsep-6\arrayrulewidth)*225/1000\relax}|%
    C{\dimexpr(\linewidth-8\tabcolsep-6\arrayrulewidth)*159/1000\relax}|%
    C{\dimexpr(\linewidth-8\tabcolsep-6\arrayrulewidth)*144/1000\relax}|%
    L{\dimexpr(\linewidth-8\tabcolsep-6\arrayrulewidth)*358/1000\relax}|%
    C{\dimexpr(\linewidth-8\tabcolsep-6\arrayrulewidth)*114/1000\relax}|%
  }%
  \hline
  \thead{Object of\\Verb} &
  \thead{Level of\\Learning Domain} &
  \thead{Action\\Verb} &
  \thead{Context/Condition/\\Qualifying Phrase} &
  \thead{เวลาเรียน\\(ชั่วโมง)} \\ \hline
}{%
  \end{tabular}\normalsize\mkoendsubsection
}
\newcommand{\contentrow}[5]{#1 & #2 & #3 & #4 & #5 \\ \hline}

% ===== 4.2 Teaching & assessment =====
\newenvironment{teachingtable}{%
  \mkosectionfour
  \mkosubsection{กิจกรรมการเรียนการสอนและการวัดผลที่สอดคล้องกับ CLOs}%
  \mkotablesetup
  \noindent\begin{tabular}{|C{1.5cm}|L{\dimexpr(\linewidth-1.5cm-8\tabcolsep-4\arrayrulewidth)/2\relax}|L{\dimexpr(\linewidth-1.5cm-8\tabcolsep-4\arrayrulewidth)/2\relax}|}\hline
  \textbf{CLOs} & \makecell{\textbf{Teaching and Learning}\\\textbf{Activities}} & \textbf{Assessment Methods} \\ \hline
}{%
  \end{tabular}\mkoendsubsection
}
\newcommand{\teachrow}[3]{\textbf{#1} & #2 & #3 \\ \hline}

% ===== 4.3 Assessment plan =====
\newenvironment{assessmenttable}{%
  \mkosubsection{การประเมินผลการจัดการเรียนรู้}%
  \mkotablesetup
  \noindent\begin{tabular}{|L{\dimexpr(\linewidth-2.2cm-8\tabcolsep-4\arrayrulewidth)/2\relax}|L{\dimexpr(\linewidth-2.2cm-8\tabcolsep-4\arrayrulewidth)/2\relax}|C{2.2cm}|}\hline
  \textbf{รูปแบบการประเมิน} & \textbf{CLOs ที่สัมพันธ์} & \textbf{คะแนน (\%)} \\ \hline
}{%
  \end{tabular}\mkoendsubsection
}
\newcommand{\assessrow}[3]{#1 & #2 & #3 \\ \hline}

% ===== หมวดที่ 5 — Rubric =====
\newenvironment{rubricsection}{%
  \mkosectionfive
  \mkosubsection{หลักการให้คะแนน (Marking Scheme) และระเบียบที่เกี่ยวข้อง}%
  \noindent
  ใช้เกณฑ์คะแนน 4 ระดับ (4 = ดีเยี่ยม, 3 = ดี, 2 = พอใช้, 1 = ต้องปรับปรุง)
  สำหรับนักศึกษาระดับปริญญาโท โดยคาดหวังความลึกเชิงวิชาการ การวิเคราะห์เชิงวิพากษ์
  และการอ้างอิงหลักฐาน/วรรณกรรมตามความเหมาะสมของรายวิชา
  สอดคล้องกับ CLO แต่ละข้อและสัดส่วนการประเมินในข้อ 4.3
  กำหนดการส่งงานและการสอบเป็นไปตามแผนรายสัปดาห์ข้อ 4.4
  เกณฑ์ผ่านรายวิชาบัณฑิตศึกษาเป็นไปตามข้อบังคับมหาวิทยาลัยฯ ว่าด้วยการจัดการศึกษาระดับบัณฑิตศึกษา
  และระเบียบการประเมินผล/การอุทธรณ์ของมหาวิทยาลัยราชภัฏอุตรดิตถ์\par\vspace{6pt}%
}{%
  \mkoendsubsection
}
\newenvironment{subrubric}[2]{%
  \mkosubsection{Rubric #1}%
  \if\relax\detokenize{#2}\relax\else\noindent\textit{#2}\par\vspace{4pt}\fi
  \mkotablesetup
  \footnotesize
  \begin{tabular}{|C{1.5cm}|L{\dimexpr\linewidth-1.5cm-4\tabcolsep-3\arrayrulewidth\relax}|}%
  \hline
  \thead{ระดับ} & \thead{คำอธิบายผลการเรียนรู้} \\ \hline
}{%
  \end{tabular}\normalsize\mkoendsubsection
}
\newcommand{\rubricrow}[2]{#1 & #2 \\ \hline}

% ===== 6.2 สิ่งสนับสนุน (รายการ ความเรียงสั้น) =====
\newenvironment{supporttable}{%
  \mkosectionsix
  \mkosubsection{สิ่งสนับสนุนการเรียนการสอน}%
  \begin{itemize}[itemsep=4pt, topsep=2pt, parsep=0pt]
}{%
  \end{itemize}\mkoendsubsection
}
\newcommand{\supportitem}[1]{\item #1}
\newcommand{\supportrow}[4]{%
  \item #1 จำนวน #2 อยู่ในสภาพที่ #3 และ #4 ตามความต้องการของการจัดการเรียนการสอน%
}

% ===== 4.4 แผนรายสัปดาห์ (SU217) =====
\newenvironment{weeklyplan}{%
  \mkosectionfour
  \mkosubsection{แผนการจัดการเรียนรู้รายสัปดาห์}%
  \mkotablesetup
  \noindent\small
  \setlength\LTleft{0pt}%
  \setlength\LTright{0pt}%
  \begin{longtable}{|%
    C{0.07\linewidth}|%
    L{0.22\linewidth}|%
    C{0.10\linewidth}|%
    C{0.07\linewidth}|%
    L{0.36\linewidth}|%
    L{0.18\linewidth}|%
  }
  \hline
  \textbf{สัปดาห์ที่} & \textbf{หัวข้อ / รายละเอียด} & \textbf{CLOs} &
  \textbf{ชม.} & \textbf{กิจกรรมการเรียนการสอนและสื่อที่ใช้} & \textbf{ผู้สอน} \\ \hline
  \endfirsthead
  \hline
  \textbf{สัปดาห์ที่} & \textbf{หัวข้อ / รายละเอียด} & \textbf{CLOs} &
  \textbf{ชม.} & \textbf{กิจกรรมการเรียนการสอนและสื่อที่ใช้} & \textbf{ผู้สอน} \\ \hline
  \endhead
  \hline
  \endfoot
}{%
  \end{longtable}\normalsize\mkoendsubsection
}
\makeatletter
\newcommand{\weekrow}[5]{%
  #1 & #2 & #4 & 3 & #3%
  \if\relax\detokenize{#5}\relax\else\ (\textit{#5})\fi
  & \mkoInstructor \\ \hline
}
\makeatother
\newcommand{\weekmid}[1]{\multicolumn{6}{|c|}{\textbf{#1}} \\ \hline}

% ===== Signatures =====
\newcommand{\signatureblock}[2]{%
  \par\vspace{20pt}
  \begin{flushright}
  \begin{tabular}{c}
    \rule{8cm}{0.4pt} \\
    (#1) \\
    (อาจารย์ผู้สอน) \\
    วัน.............เดือน..........................พ.ศ................ \\[20pt]
    \rule{8cm}{0.4pt} \\
    (#2) \\
    รองคณบดีฝ่ายวิชาการ \\
    วัน.............เดือน..........................พ.ศ................ \\
  \end{tabular}
  \end{flushright}
}
