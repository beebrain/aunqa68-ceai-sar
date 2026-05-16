% mko3.cls -- LaTeX class for แผนการจัดการเรียนรู้รายวิชา (มคอ.3)
% Uttaradit Rajabhat University
% Compile with XeLaTeX
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{mko3}[2026/05/14 v1.1 Course Learning Plan (มคอ.3) template]

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
\RequirePackage{ragged2e}
\RequirePackage{titlesec}
\RequirePackage{xcolor}
\RequirePackage{calc}

\renewcommand{\arraystretch}{1.35}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}

% Column types
\newcolumntype{L}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\Centering\arraybackslash}p{#1}}

% Standard text width = 16cm
\newcommand{\mko@tw}{16cm}

\titleformat{\section}{\normalfont\bfseries\large}{}{0pt}{}
\titlespacing*{\section}{0pt}{12pt}{6pt}

\newcommand{\mkothreetitle}{%
  \begin{center}{\Large\bfseries แผนการจัดการเรียนรู้รายวิชา}\end{center}
}

% ===== 1. Course info =====
\makeatletter
\newcommand{\@coursecode}{}\newcommand{\coursecode}[1]{\renewcommand{\@coursecode}{#1}}
\newcommand{\@coursename}{}\newcommand{\coursename}[1]{\renewcommand{\@coursename}{#1}}
\newcommand{\@program}{}\newcommand{\program}[1]{\renewcommand{\@program}{#1}}
\newcommand{\@coursegroup}{}\newcommand{\coursegroup}[1]{\renewcommand{\@coursegroup}{#1}}
\newcommand{\@semester}{}\newcommand{\semester}[1]{\renewcommand{\@semester}{#1}}
\newcommand{\@instructor}{}\newcommand{\instructor}[1]{\renewcommand{\@instructor}{#1}}
\newcommand{\@contact}{}\newcommand{\contact}[1]{\renewcommand{\@contact}{#1}}
\newcommand{\@coursedesc}{}\newcommand{\coursedesc}[1]{\renewcommand{\@coursedesc}{#1}}

\newcommand{\courseinfotable}{%
\noindent\begin{tabular}{|L{4.5cm}|L{11cm}|}\hline
\textbf{รหัสรายวิชา} & \@coursecode \\ \hline
\textbf{ชื่อวิชา} & \@coursename \\ \hline
\textbf{ผู้เรียนในหลักสูตร} & \@program \\ \hline
\textbf{กลุ่มวิชาในหลักสูตร} & \@coursegroup \\ \hline
\textbf{ภาคการศึกษา/ปีการศึกษา} & \@semester \\ \hline
\textbf{ชื่ออาจารย์ผู้สอน} & \@instructor \\ \hline
\textbf{ข้อมูลการติดต่อ (Email หรือเบอร์โทร)} & \@contact \\ \hline
\textbf{คำอธิบายรายวิชา} & \@coursedesc \\ \hline
\end{tabular}\par%
}
\makeatother

% ===== 2. CLO Domain/Level =====
\newenvironment{clodomaintable}{%
  \section*{โดเมนและระดับการเรียนรู้ของ CLOs (Course Learning Outcomes: CLOs)}
  \noindent\begin{tabular}{|C{1.6cm}|L{8.5cm}|C{3cm}|C{1.8cm}|}\hline
  \multicolumn{2}{|c|}{\textbf{ผลลัพธ์การเรียนรู้รายวิชา (CLOs)}} &
  \multicolumn{2}{c|}{\textbf{Level of Learning Domain}} \\ \cline{3-4}
  \multicolumn{2}{|c|}{} & \textbf{Domain} & \textbf{Level} \\ \hline
}{%
  \end{tabular}\par
}
\newcommand{\cloitem}[4]{\textbf{#1} & #2 & #3 & #4 \\ \hline}

% ===== 3.1 CLO ↔ PLO =====
% Usage: \begin{cloplotable}{3}{ & \textbf{PLO1} & \textbf{PLO2} & \textbf{PLO3}}
%   then write rows manually:  \textbf{CLO1} & X & & X \\ \hline
\newenvironment{cloplotable}[2]{%
  \section*{ความสอดคล้องและระดับการส่งเสริมพัฒนาผู้เรียนจากระดับรายวิชา (CLOs) เพื่อการสัมฤทธิ์ผลในระดับหลักสูตร (PLOs)}
  \textbf{\quad 1. ความสอดคล้อง}\par\vspace{4pt}
  \noindent\begin{tabular}{|C{1.6cm}|*{#1}{C{1.6cm}|}}\hline
  \textbf{CLOs} #2 \\ \hline
}{%
  \end{tabular}\par
}

% ===== 3.2 Bloom + LLL =====
\newenvironment{bloomtable}{%
  \par\vspace{4pt}\textbf{\quad 2. ระดับการส่งเสริม}\par\vspace{4pt}
  \noindent\begin{tabular}{|C{1.4cm}|C{3.4cm}|C{3.2cm}|C{3.4cm}|C{2.8cm}|}\hline
  \multirow{2}{*}{\textbf{CLOs}} & \multicolumn{3}{c|}{\textbf{Bloom's Taxonomy}} &
  \multirow{2}{*}{\makecell{\textbf{การเรียนรู้}\\\textbf{ตลอดชีวิต (LLL)}}} \\ \cline{2-4}
   & \makecell{\textbf{พุทธิพิสัย}\\Cognitive}
   & \makecell{\textbf{จิตพิสัย}\\Affective}
   & \makecell{\textbf{ทักษะพิสัย}\\Psychomotor} & \\ \hline
}{%
  \end{tabular}\par
}
\newcommand{\bloomrow}[5]{\textbf{#1} & #2 & #3 & #4 & #5 \\ \hline}

% ===== 4. Content analysis =====
\newenvironment{contentanalysistable}{%
  \section*{การวิเคราะห์เนื้อหาให้สอดคล้องกับระดับการเรียนรู้ (Level of Learning Domain)}
  \noindent\begin{tabular}{|L{3.2cm}|C{2.4cm}|C{2.2cm}|L{4.6cm}|C{1.8cm}|}\hline
  \textbf{Object of Verb} & \makecell{\textbf{Level of}\\\textbf{Learning Domain}} &
  \textbf{Action Verb} & \makecell[l]{\textbf{Context/Condition/}\\\textbf{Qualifying Phrase}} &
  \makecell{\textbf{เวลาเรียน}\\\textbf{(ชั่วโมง)}} \\ \hline
}{%
  \end{tabular}\par
}
\newcommand{\contentrow}[5]{#1 & #2 & #3 & #4 & #5 \\ \hline}

% ===== 5. Teaching & assessment =====
\newenvironment{teachingtable}{%
  \section*{กิจกรรมการเรียนการสอนและการวัดผลที่สอดคล้องกับ CLOs}
  \noindent\begin{tabular}{|C{1.6cm}|L{6.7cm}|L{6.7cm}|}\hline
  \textbf{CLOs} & \makecell{\textbf{Teaching and Learning}\\\textbf{Activities}} & \textbf{Assessment Methods} \\ \hline
}{%
  \end{tabular}\par
}
\newcommand{\teachrow}[3]{\textbf{#1} & #2 & #3 \\ \hline}

% ===== 6. Assessment plan =====
\newenvironment{assessmenttable}{%
  \section*{การประเมินผลการจัดการเรียนรู้}
  \noindent\begin{tabular}{|L{8cm}|C{4cm}|C{2.5cm}|}\hline
  \textbf{รูปแบบการประเมิน} & \textbf{CLOs ที่สัมพันธ์} & \textbf{คะแนน (\%)} \\ \hline
}{%
  \end{tabular}\par
}
\newcommand{\assessrow}[3]{#1 & #2 & #3 \\ \hline}

% ===== 7. Support resources =====
\newenvironment{supporttable}{%
  \section*{สิ่งสนับสนุนการเรียนการสอน}
  \noindent\begin{tabular}{|L{6cm}|C{2.2cm}|C{3.4cm}|C{3.4cm}|}\hline
  \textbf{สิ่งสนับสนุน} & \textbf{จำนวน} & \textbf{ความพร้อมใช้} & \textbf{ความทันสมัย} \\ \hline
}{%
  \end{tabular}\par
}
\newcommand{\supportrow}[4]{#1 & #2 & #3 & #4 \\ \hline}

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
