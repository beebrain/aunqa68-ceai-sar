% ==============================================================================
% aunqa.cls — AUN-QA Self-Assessment Report (SAR) Document Class
% มหาวิทยาลัยราชภัฏอุตรดิตถ์
% Version: 1.0 (2568)
%
% Usage:
%   \documentclass[master]{aunqa}
%   \documentclass[bachelor]{aunqa}
%
% Options:
%   master   — ระดับปริญญาโท (default)
%   bachelor — ระดับปริญญาตรี
%   phd      — ระดับปริญญาเอก
% ==============================================================================

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{aunqa}[2025/04/13 v1.0 AUN-QA SAR Document Class for URU]

% --- Class Options ---
\newif\if@master \@mastertrue
\newif\if@bachelor \@bachelorfalse
\newif\if@phd \@phdfalse

\DeclareOption{master}{\@mastertrue\@bachelorfalse\@phdfalse}
\DeclareOption{bachelor}{\@masterfalse\@bachelortrue\@phdfalse}
\DeclareOption{phd}{\@masterfalse\@bachelorfalse\@phdtrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

% --- Base Class ---
\LoadClass[12pt,a4paper]{article}

% ==============================================================================
% PACKAGES
% ==============================================================================

% --- Language (must come before fontspec) ---
\RequirePackage{polyglossia}
\setdefaultlanguage{thai}
\setotherlanguage{english}

% --- Thai Line Breaking (XeTeX) ---
% ให้ XeTeX ตัดบรรทัดที่ขอบเขตคำภาษาไทย ไม่ใช่ตัดกลางคำ
\XeTeXlinebreaklocale "th"
\XeTeXlinebreakskip = 0pt plus 1pt
\XeTeXlinebreakpenalty = 0

% --- Font (local folder) ---
\RequirePackage{fontspec}
\setmainfont{THSarabunNew}[
    Path           = ./fonts/,
    Extension      = .ttf,
    UprightFont    = *,
    BoldFont       = * Bold,
    ItalicFont     = * Italic,
    BoldItalicFont = * BoldItalic,
]
\setmonofont{THSarabunNew}[
    Path           = ./fonts/,
    Extension      = .ttf,
    UprightFont    = *,
    BoldFont       = * Bold,
    ItalicFont     = * Italic,
    BoldItalicFont = * BoldItalic,
]
\newfontfamily\thaifont{THSarabunNew}[
    Path           = ./fonts/,
    Extension      = .ttf,
    UprightFont    = *,
    BoldFont       = * Bold,
    ItalicFont     = * Italic,
]

% --- Page Layout ---
\RequirePackage[a4paper,
    top        = 2.54cm,
    bottom     = 2.54cm,
    left       = 2.54cm,
    right      = 2.54cm,
    headheight = 1.18cm,
    footskip   = 1.18cm,
]{geometry}

% --- Core Packages ---
\RequirePackage{setspace}
\RequirePackage{indentfirst}
\RequirePackage{enumitem}
\RequirePackage{array}
\RequirePackage{tabularx}
\RequirePackage{longtable}
% Full-width multipage tables (tabularx + longtable); use \linewidth inside table body
\RequirePackage{xltabular}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\newcolumntype{Z}{>{\centering\arraybackslash}X}
\RequirePackage{multirow}
\RequirePackage{booktabs}
\RequirePackage{makecell}
\RequirePackage{graphicx}
\RequirePackage{caption}
\RequirePackage{float}
\RequirePackage{ifthen}
\RequirePackage{pdflscape}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage[table]{xcolor}
\RequirePackage{calc}
\RequirePackage{amssymb}
\RequirePackage{etoolbox}
\RequirePackage{hyperref}
\RequirePackage{bookmark}

% ==============================================================================
% TYPOGRAPHY
% ==============================================================================

% --- Caption alignment (tables/figures) ---
% Match Word-style: caption text flush-left (not centered),
% including single-line captions.
\captionsetup[table]{justification=raggedright,singlelinecheck=false,font=normalsize}
\captionsetup[figure]{justification=raggedright,singlelinecheck=false,font=normalsize}

% --- Line Spacing (Word single = font × 1.2) ---
\singlespacing
\setlength{\parskip}{0pt}
\setlength{\parindent}{1.27cm}

% --- Prevent Overfull Boxes ---
% อนุญาตให้ขยาย spacing เล็กน้อยแทนการตัดคำผิด
\tolerance=9999
\emergencystretch=3em
\hyphenpenalty=10000
\exhyphenpenalty=10000

% --- Font Size Commands ---
\newcommand{\fontcover}   {\fontsize{28pt}{33.6pt}\selectfont}
\newcommand{\fontsection} {\fontsize{20pt}{24pt}\selectfont}
\newcommand{\fontpart}    {\fontsize{18pt}{21.6pt}\selectfont}
\newcommand{\fontbody}    {\fontsize{16pt}{19.2pt}\selectfont}
\newcommand{\fontsub}     {\fontsize{14pt}{16.8pt}\selectfont}

% Default normalsize
\renewcommand{\normalsize}{\fontsize{16pt}{19.2pt}\selectfont}

% Lock relative-size commands to the unified system so any stray
% \small / \large / \Large in section files cannot leak in
\renewcommand{\tiny}        {\fontsub}
\renewcommand{\scriptsize}  {\fontsub}
\renewcommand{\footnotesize}{\fontsub}
\renewcommand{\small}       {\fontbody}
\renewcommand{\large}       {\fontbody}
\renewcommand{\Large}       {\fontpart}
\renewcommand{\LARGE}       {\fontpart}
\renewcommand{\huge}        {\fontsection}
\renewcommand{\Huge}        {\fontsection}

% Section / subsection / subsubsection use the unified font system.
% (Inside a .cls file `@` is already a letter — no \makeatletter needed.)
\renewcommand\section{%
    \@startsection{section}{1}{\z@}%
    {-3.5ex \@plus -1ex \@minus -.2ex}%
    {2.3ex \@plus.2ex}%
    {\fontpart\bfseries}}
\renewcommand\subsection{%
    \@startsection{subsection}{2}{\parindent}%
    {-3.0ex\@plus -1ex \@minus -.2ex}%
    {1.5ex \@plus .2ex}%
    {\fontbody\bfseries}}
\renewcommand\subsubsection{%
    \@startsection{subsubsection}{3}{\z@}%
    {-2.5ex\@plus -1ex \@minus -.2ex}%
    {1.0ex \@plus .2ex}%
    {\fontbody\bfseries}}

% --- Hyperref Setup ---
\hypersetup{
    colorlinks = false,
    pdfborder  = {0 0 0},
}

% --- No Section Numbering ---
\setcounter{secnumdepth}{0}

% ==============================================================================
% HEADER & FOOTER
% ==============================================================================
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\fontsub\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% ==============================================================================
% PROGRAM INFO STORAGE
% ==============================================================================
\newcommand{\@programnameth}{}
\newcommand{\@programbranch}{}
\newcommand{\@programnameen}{}
\newcommand{\@degreeth}{}
\newcommand{\@degreeen}{}
\newcommand{\@degreeabbrevth}{}
\newcommand{\@degreeabbreben}{}
\newcommand{\@faculty}{}
\newcommand{\@university}{มหาวิทยาลัยราชภัฏอุตรดิตถ์}
\newcommand{\@academicyear}{}
\newcommand{\@programyear}{}
\newcommand{\@programcode}{}
\newcommand{\@credits}{}
\newcommand{\@reportdate}{}
\newcommand{\@reportperiod}{}
\newcommand{\@programstatus}{ใหม่/ปรับปรุง}
\newcommand{\@chairperson}{...................................}

\newcommand{\programnameth}[1]{\renewcommand{\@programnameth}{#1}}
\newcommand{\programbranch}[1]{\renewcommand{\@programbranch}{#1}}
\newcommand{\programnameen}[1]{\renewcommand{\@programnameen}{#1}}
\newcommand{\degreeth}[1]{\renewcommand{\@degreeth}{#1}}
\newcommand{\degreeen}[1]{\renewcommand{\@degreeen}{#1}}
\newcommand{\degreeabbrevth}[1]{\renewcommand{\@degreeabbrevth}{#1}}
\newcommand{\degreeabbreben}[1]{\renewcommand{\@degreeabbreben}{#1}}
\newcommand{\faculty}[1]{\renewcommand{\@faculty}{#1}}
\newcommand{\university}[1]{\renewcommand{\@university}{#1}}
\newcommand{\academicyear}[1]{\renewcommand{\@academicyear}{#1}}
\newcommand{\programyear}[1]{\renewcommand{\@programyear}{#1}}
\newcommand{\programcode}[1]{\renewcommand{\@programcode}{#1}}
\newcommand{\totalcredits}[1]{\renewcommand{\@credits}{#1}}
\newcommand{\reportdate}[1]{\renewcommand{\@reportdate}{#1}}
\newcommand{\reportperiod}[1]{\renewcommand{\@reportperiod}{#1}}
\newcommand{\programstatus}[1]{\renewcommand{\@programstatus}{#1}}
\newcommand{\chairperson}[1]{\renewcommand{\@chairperson}{#1}}

% ==============================================================================
% COVER PAGE
% ==============================================================================
\newcommand{\makecover}{%
    \thispagestyle{empty}
    \begin{center}
        \vspace*{1.2cm}
        {\fontcover\bfseries รายงานประเมินตนเอง}\\[0.4cm]
        {\fontcover\bfseries การประกันคุณภาพการศึกษาภายใน~~ระดับหลักสูตร}\\[0.4cm]
        {\fontcover\bfseries ตามเกณฑ์คุณภาพ AUN-QA}\\[1.8cm]
        {\fontsection\bfseries หลักสูตร\@programnameth\space สาขาวิชา\@programbranch}\\[0.3cm]
        {\fontsection\bfseries หลักสูตร\@programstatus\space พ.ศ.~\@programyear}\\[0.3cm]
        {\fontsection\bfseries คณะ \@faculty}\\[0.3cm]
        {\fontsection\bfseries \@university}\\[2.0cm]
        {\fontsection\bfseries ประจำปีการศึกษา \@academicyear}\\[0.4cm]
        {\fontbody\bfseries \@reportperiod}\\[0.4cm]
        {\fontbody\bfseries รายงาน ณ วันที่ \@reportdate}
    \end{center}
    \newpage
}

% ==============================================================================
% PART SEPARATOR PAGE
% ==============================================================================
\newcommand{\partpage}[2]{%
    % Chapter-style opener: start a new page but keep the next section
    % on the SAME page (no standalone separator page).
    \clearpage
    \thispagestyle{empty}
    \vspace*{0.8cm}
    \begin{center}
        {\fontpart\bfseries #1}\\[0.3cm]
        {\fontpart\bfseries #2}
    \end{center}
    \vspace{0.8cm}
}

% ==============================================================================
% PREFACE PAGE
% ==============================================================================
% \makeprefacepage{content} — ใช้ \@chairperson จาก \chairperson{...}
\newcommand{\makeprefacepage}[1]{%
    \newpage
    \thispagestyle{empty}
    \begin{center}
        {\fontpart\bfseries คำนำ}
    \end{center}
    \vspace{0.6cm}
    #1
    \vspace{2.5cm}
    \begin{center}
        \begin{minipage}{9cm}
            \centering
            ({\@chairperson})\\
            ประธานหลักสูตร\@programnameth
        \end{minipage}
    \end{center}
    \newpage
}

% ==============================================================================
% TABLE OF CONTENTS (manual, matches docx layout)
% ==============================================================================
% เปิดหน้าสารบัญพร้อมหัว "สารบัญ" และคอลัมน์ "หน้า"
\newcommand{\maketoc}[1]{%
    \newpage
    \thispagestyle{empty}
    \begin{center}
        {\fontpart\bfseries สารบัญ}
    \end{center}
    \vspace{0.4cm}
    \hfill{\fontbody\bfseries หน้า}\par
    \vspace{0.2cm}
    {\fontbody #1}\par
    \newpage
}

% \tocpart{title}     — หัวข้อระดับ "ส่วนที่ N ..." (ไม่มี dot leader)
\newcommand{\tocpart}[1]{%
    \par\vspace{4pt}
    \noindent{\fontbody\bfseries #1}\par
}

% \tocitem{indent}{title}{page}  — รายการพร้อม dot leader และเลขหน้า
\newcommand{\tocitem}[3]{%
    \par\noindent\hspace*{#1}%
    \begin{minipage}[t]{\dimexpr\linewidth-#1-1.5cm\relax}%
        \raggedright #2\dotfill%
    \end{minipage}\hspace*{0.3cm}\makebox[1.2cm][r]{#3}\par
}

% ==============================================================================
% BLANK FIELD
% ==============================================================================
\newcommand{\blankfield}[1]{\makebox[#1]{\dotfill}}

% ==============================================================================
% APA-STYLE REFERENCE LIST (hanging indent; reliable inside tabular/longtable)
% Uses \hangindent/\hangafter — list env. often fails inside \multicolumn{p}{}.
% ==============================================================================
\newlength{\APArefhang}
\setlength{\APArefhang}{1.27cm}
\newenvironment{apareflist}{%
    \begingroup
    \setlength{\parindent}{0pt}%
    \setlength{\parskip}{0.4em plus 0.08em minus 0.06em}%
}{%
    \endgroup
}
\NewDocumentCommand{\aparefpar}{+m}{%
    \ifhmode\par\fi
    \hangindent=\APArefhang
    \hangafter=1
    \noindent\ignorespaces #1\par
}

% ==============================================================================
% CRITERION COMMANDS
% ==============================================================================

% Main criterion header: \criterion{number}{Thai name}{English name}
\newcommand{\criterion}[3]{%
    \vspace{8pt}
    \noindent{\fontbody\bfseries Criteria #1~:~#2 (#3)}
    \vspace{4pt}
    \par
}

% Sub-criterion: \subcriterion{number}{description}
\newcommand{\subcriterion}[2]{%
    \vspace{6pt}
    \noindent{\fontbody\bfseries #1\quad #2}
    \par\vspace{4pt}
}

% AUN QA narrative criterion line (e.g. ``1.1 The programme \ldots'') —
% flush left, roman body weight (not bold); body paragraphs stay indented (\parindent).
\newcommand{\criterionsub}[1]{%
    \vspace{6pt}%
    \noindent{\fontbody\normalfont\mdseries #1}%
    \par\vspace{4pt}%
}

% Numbered lists under criterion text: ``1)'' style with extra inset vs body text.
\newenvironment{criterionsubenumerate}{%
    \begingroup
    \begin{enumerate}[%
        align=left,
        label=\arabic*),
        labelsep=0.35em,
        leftmargin=*,
        itemindent=!,
        labelindent=\dimexpr\parindent\relax,
        listparindent=\parindent,
        itemsep=2pt plus 2pt minus 1pt,
        topsep=4pt plus 3pt minus 2pt,
        parsep=0pt,
        partopsep=0pt,
    ]%
}{%
    \end{enumerate}%
    \endgroup
}

% Criteria block rating: \sarrating{score}{justification}
\newcommand{\sarrating}[2]{%
    \vspace{4pt}
    \noindent\begin{tabular}{@{}p{3.5cm}@{}p{\linewidth-3.5cm}@{}}
        {\fontbody\bfseries คะแนนประเมินตนเอง:} & {\fontbody\bfseries #1 / 7}\\
        {\fontbody\bfseries เหตุผล:} & #2\\
    \end{tabular}
    \par\vspace{4pt}
}

% ==============================================================================
% PLO COMMANDS
% ==============================================================================

% \plo{number}{description}
\newcommand{\plo}[2]{%
    \noindent{\fontbody PLO#1\quad #2}\par
}

% \peo{number}{description}
\newcommand{\peo}[2]{%
    \noindent{\fontbody PEO#1\quad #2}\par
}

% ==============================================================================
% EVIDENCE COMMANDS
% ==============================================================================

% Evidence list environment
\newenvironment{evidencelist}{%
    \vspace{6pt}
    \noindent{\fontbody\bfseries รายการหลักฐาน}
    \vspace{2pt}
    \begin{itemize}[leftmargin=2cm, label={}, itemsep=0pt, parsep=0pt]
}{%
    \end{itemize}
    \vspace{4pt}
}

% Single evidence item: \evidence{code}{description}
\newcommand{\evidence}[2]{%
    \item {\fontbody #1\quad #2}%
}

% Alias for evidence-list (used in sections)
\newenvironment{evidence-list}{%
    \vspace{6pt}
    \begin{itemize}[leftmargin=2cm, label={}, itemsep=0pt, parsep=0pt]
}{%
    \end{itemize}
    \vspace{4pt}
}

% ==============================================================================
% EVIDENCE REFERENCE — cites supporting documents
% ==============================================================================
\newcommand{\evidenceref}[1]{%
    \par\vspace{2pt}%
    \noindent{\bfseries หลักฐานอ้างอิง:} #1%
    \par\vspace{2pt}%
}

% ==============================================================================
% MARK NOTE — flags missing evidence
% ==============================================================================
\newcommand{\marknote}[1]{%
    \par\vspace{4pt}%
    \noindent\fcolorbox{red}{red!10}{%
        \parbox{\linewidth-2\fboxsep-2\fboxrule}{%
            {\bfseries MARK:} #1%
        }%
    }%
    \par\vspace{4pt}%
}

% ==============================================================================
% SELF-ASSESSMENT BOX
% ==============================================================================
% \begin{selfassessmentbox}{score}{description}
\newenvironment{selfassessmentbox}[2]{%
    \vspace{4pt}
    \noindent\fbox{%
        \parbox{\linewidth-2cm}{%
            \centering
            {\fontbody\bfseries ผลการประเมินตนเอง : #1 / 7} \\[4pt]
            #2
        }%
    }
    \par\vspace{4pt}
}{}

% ==============================================================================
% STRENGTH / WEAKNESS BOXES
% ==============================================================================
\newenvironment{strengthbox}{%
    \vspace{4pt}
    \noindent{\fontbody\bfseries จุดแข็ง:}\space
}{
    \par\vspace{4pt}
}

\newenvironment{weaknessbox}{%
    \vspace{4pt}
    \noindent{\fontbody\bfseries จุดที่ควรพัฒนา:}\space
}{
    \par\vspace{4pt}
}

% ==============================================================================
% STAFF TABLE ROW COMMAND
% ==============================================================================

% \staffrow{no}{rank}{name}{degree}{field}{institution}{year}
\newcommand{\staffrow}[7]{%
    #1 & #2 & #3 & #4~(#5) & #6 & #7 \\
    \hline
}

% ==============================================================================
% STANDARD STAFF TABLE
% ==============================================================================
\newenvironment{stafftable}{%
    \vspace{6pt}
    \begin{center}
    \begin{tabular}{|c|p{2cm}|p{3cm}|p{3.5cm}|p{2.5cm}|c|}
    \hline
    \textbf{ลำดับ} & \textbf{ตำแหน่งทางวิชาการ} & \textbf{ชื่อ--นามสกุล} &
    \textbf{คุณวุฒิ (สาขา)} & \textbf{สถาบัน} & \textbf{ปี} \\
    \hline
}{%
    \end{tabular}
    \end{center}
    \vspace{4pt}
}

% ==============================================================================
% ASSESSMENT TABLE
% ==============================================================================
\newenvironment{assessmenttable}{%
    \vspace{6pt}
    \begin{center}
    \begin{tabular}{|p{3cm}|p{8cm}|c|}
    \hline
    \multicolumn{1}{|c|}{\textbf{ตัวบ่งชี้ / Criteria}} &
    \multicolumn{1}{c|}{\textbf{รายการ}} &
    \textbf{ประเมินตนเอง} \\
    \hline
}{%
    \end{tabular}
    \end{center}
    \vspace{4pt}
}

% Row command for assessment table
% \assessrow{code}{description}{result}
\newcommand{\assessrow}[3]{%
    #1 & #2 & #3 \\ \hline
}

% ==============================================================================
% PLO MAPPING TABLE
% ==============================================================================

% \plomaptable{ncols}{header cols}{rows}
% Use standard tabular for custom PLO maps

% ==============================================================================
% SCORE BOX (for Criteria summary)
% ==============================================================================
\newcommand{\scorebox}[2]{%
    % #1 = score, #2 = max (usually 7)
    \vspace{4pt}
    \noindent\fbox{%
        \parbox{6cm}{%
            \centering
            {\fontbody\bfseries ผลการประเมินตนเอง : #1 / #2}
        }%
    }
    \par\vspace{4pt}
}

% ==============================================================================
% SECTION TITLE FORMATTING
% ==============================================================================

% Numbered section heading style
\newcommand{\sectiontitle}[1]{%
    \vspace{8pt}
    \noindent{\fontbody\bfseries #1}
    \par\vspace{4pt}
}

% Sub-section heading
\newcommand{\subsectiontitle}[1]{%
    \vspace{6pt}
    \noindent{\fontbody\bfseries #1}
    \par\vspace{2pt}
}

% ==============================================================================
% TOPIC BLOCK (label + paragraph) — Word-like narrative blocks
% ==============================================================================
% Usage: \topicblock{หัวข้อ}{เนื้อหา}
\newcommand{\topicblock}[2]{%
    \medskip
    \noindent{\fontbody\bfseries #1}\par
    \vspace{2pt}
    \noindent\hspace*{\parindent}#2\par
}

% Topic line (label + text on same line) — hanging indent like Word tab
% Usage: \topicline{หัวข้อ}{เนื้อหา}
\newcommand{\topicline}[2]{%
    \medskip
    \noindent{\fontbody\bfseries #1}\quad
    \begingroup
        \hangindent=\parindent\hangafter=1
        #2\par
    \endgroup
}

% ==============================================================================
% GAP ANALYSIS TABLE
% ==============================================================================
\newenvironment{gaptable}[1][ปีการศึกษาหน้า]{%
    \vspace{6pt}
    \noindent{\fontbody\bfseries แผนพัฒนาหลักสูตร (#1)}
    \vspace{4pt}
    \begin{center}
    \begin{tabular}{|c|p{4cm}|p{4cm}|p{3cm}|}
    \hline
    \textbf{Criteria} & \textbf{ประเด็นที่ต้องพัฒนา} & \textbf{แนวทางการพัฒนา} & \textbf{ผู้รับผิดชอบ} \\
    \hline
}{%
    \end{tabular}
    \end{center}
    \vspace{4pt}
}

% Row for gap table: \gaprow{criteria}{issue}{plan}{responsible}
\newcommand{\gaprow}[4]{%
    #1 & #2 & #3 & #4 \\ \hline
}

% ==============================================================================
% STANDARD DEGREE TYPE TEXT
% ==============================================================================
\newcommand{\degreelabel}{%
    \if@master ปริญญาโท\fi
    \if@bachelor ปริญญาตรี\fi
    \if@phd ปริญญาเอก\fi
}

% ==============================================================================
% END OF CLASS
% ==============================================================================
