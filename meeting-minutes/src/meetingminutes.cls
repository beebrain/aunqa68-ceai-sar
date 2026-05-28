% ============================================================
%  meetingminutes.cls
%  รูปแบบรายงานการประชุม สไตล์ มหาวิทยาลัยราชภัฏอุตรดิตถ์
%  Requires: XeLaTeX
%  Version : 1.0  (2026-05-20)
% ============================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{meetingminutes}[2026/05/20 v1.0 Thai Meeting Minutes]

% ── Base class ──────────────────────────────────────────────
\LoadClass[a4paper]{article}

% ── Core packages ───────────────────────────────────────────
\RequirePackage{fontspec}
\RequirePackage{polyglossia}
\RequirePackage{geometry}
\RequirePackage{array}
\RequirePackage{longtable}
\RequirePackage{tabularx}
\RequirePackage{setspace}
\RequirePackage{fancyhdr}
\RequirePackage{enumitem}
\RequirePackage{xcolor}
\RequirePackage{etoolbox}
\RequirePackage{xparse}
\RequirePackage{ifthen}
\RequirePackage{calc}
\RequirePackage{ragged2e}
\RequirePackage{booktabs}
\RequirePackage{multirow}

% ── Language ────────────────────────────────────────────────
\setmainlanguage{thai}
\setotherlanguage{english}

% ── Thai line breaking ──────────────────────────────────────
% Enable XeTeX to break Thai text at character boundaries
\AtBeginDocument{%
  \XeTeXlinebreaklocale "th"%
  \XeTeXlinebreakskip = 0pt plus 1pt%
  \XeTeXlinebreakpenalty = 0%
  \emergencystretch = 3em%
  \tolerance = 10000%
  \pretolerance = 10000%
}

% ── Font ────────────────────────────────────────────────────
\setmainfont{TH Sarabun New}[
  BoldFont       = TH Sarabun New Bold,
  ItalicFont     = TH Sarabun New Italic,
  BoldItalicFont = TH Sarabun New Bold Italic,
  Script         = Thai,
]
\newfontfamily\thaifont{TH Sarabun New}[
  BoldFont       = TH Sarabun New Bold,
  ItalicFont     = TH Sarabun New Italic,
  BoldItalicFont = TH Sarabun New Bold Italic,
  Script         = Thai,
]

% ── Page geometry ───────────────────────────────────────────
\geometry{
  a4paper,
  top    = 2.5cm,
  bottom = 2.5cm,
  left   = 3.0cm,
  right  = 2.5cm,
  headheight = 30pt,
  headsep    = 8pt,
  footskip   = 1.2cm,
}

% ── Font sizes ──────────────────────────────────────────────
\renewcommand\normalsize  {\@setfontsize\normalsize  {16pt}{26pt}}
\renewcommand\small       {\@setfontsize\small       {14pt}{22pt}}
\renewcommand\footnotesize{\@setfontsize\footnotesize{12pt}{18pt}}
\renewcommand\large       {\@setfontsize\large       {18pt}{28pt}}
\renewcommand\Large       {\@setfontsize\Large       {20pt}{30pt}}
\renewcommand\LARGE       {\@setfontsize\LARGE       {22pt}{32pt}}
\AtBeginDocument{\normalsize\setstretch{1.0}}

% ── Paragraph ───────────────────────────────────────────────
\setlength\parindent{1.5cm}
\setlength\parskip  {3pt plus 2pt}

% ============================================================
%  THAI NUMERALS
%  รองรับ 0–9999  ใช้กับ \thainum{<integer>}
% ============================================================
\newcommand\@ThaiDigit[1]{%
  \ifcase\numexpr#1\relax
    ๐\or๑\or๒\or๓\or๔\or๕\or๖\or๗\or๘\or๙%
  \fi
}

\newcommand\thainum[1]{%
  \ifnum\numexpr#1\relax>999
    \@ThaiDigit{\the\numexpr(#1)/1000\relax}%
    \@ThaiDigit{\the\numexpr((#1)-(((#1)/1000)*1000))/100\relax}%
    \@ThaiDigit{\the\numexpr((#1)-(((#1)/100)*100))/10\relax}%
    \@ThaiDigit{\the\numexpr(#1)-(((#1)/10)*10)\relax}%
  \else\ifnum\numexpr#1\relax>99
    \@ThaiDigit{\the\numexpr(#1)/100\relax}%
    \@ThaiDigit{\the\numexpr((#1)-(((#1)/100)*100))/10\relax}%
    \@ThaiDigit{\the\numexpr(#1)-(((#1)/10)*10)\relax}%
  \else\ifnum\numexpr#1\relax>9
    \@ThaiDigit{\the\numexpr(#1)/10\relax}%
    \@ThaiDigit{\the\numexpr(#1)-(((#1)/10)*10)\relax}%
  \else
    \@ThaiDigit{#1}%
  \fi\fi\fi
}

% Thai page number
\renewcommand\thepage{\thainum{\arabic{page}}}

% ============================================================
%  HEADER / FOOTER
%  หน้า ๒ เป็นต้นไป: เลขหน้าไทยกึ่งกลางด้านบน
% ============================================================
\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{%
  \ifnum\value{page}>1\relax
    \fontsize{16pt}{24pt}\selectfont\thainum{\arabic{page}}%
  \fi
}
\renewcommand\headrulewidth{0pt}
\renewcommand\footrulewidth{0pt}

\fancypagestyle{firstpage}{%
  \fancyhf{}%
  \renewcommand\headrulewidth{0pt}%
  \renewcommand\footrulewidth{0pt}%
}

% ============================================================
%  METADATA COMMANDS
% ============================================================
\newcommand\meetingcommittee[1]{\def\@mtgcommittee{#1}}
\newcommand\meetingnumber[2]{%      {ครั้งที่}{ปี}  — รับ Arabic หรือ Thai string ก็ได้
  \def\@mtgno{#1}\def\@mtgyear{#2}%
}
\newcommand\meetingdate[1]{\def\@mtgdate{#1}}    % เช่น วันพุธที่ ๒๗ สิงหาคม พ.ศ. ๒๕๖๘
\newcommand\meetingplace[1]{\def\@mtgplace{#1}}
\newcommand\meetingstart[1]{\def\@mtgstart{#1}}  % เช่น ๑๓.๓๐ น.
\newcommand\meetingend[1]{\def\@mtgend{#1}}      % เช่น ๑๖.๓๐ น.

% Defaults
\meetingcommittee{คณะกรรมการ}
\meetingnumber{๑}{๒๕๖๘}
\meetingdate{วันที่ ๑ มกราคม พ.ศ. ๒๕๖๘}
\meetingplace{ห้องประชุม}
\meetingstart{๑๓.๓๐ น.}
\meetingend{๑๖.๐๐ น.}

% ============================================================
%  TITLE BLOCK  — \maketitle
% ============================================================
\renewcommand\maketitle{%
  \thispagestyle{firstpage}%
  \begin{center}%
    {\large\bfseries รายงานการประชุม\par}%
    \vspace{2pt}%
    {\large\bfseries\@mtgcommittee\par}%
    \vspace{4pt}%
    {\large\bfseries ครั้งที่ \@mtgno{} / \@mtgyear\par}%
    \vspace{4pt}%
    {\large\bfseries \@mtgdate\par}%
    \vspace{4pt}%
    {\normalsize ณ~\@mtgplace\par}%
  \end{center}%
  \vspace{10pt}%
}

% ============================================================
%  PARTICIPANT SECTION HEADERS
%  \psection{ผู้มาประชุม}  \psection{ผู้ไม่มาประชุม}  ...
% ============================================================
\newcommand\psection[1]{%
  \vspace{10pt}%
  \noindent{\large\bfseries #1}\par
  \vspace{4pt}%
}

% ============================================================
%  PARTICIPANT TABLE
%  3 columns: num.name (wide) | org-position (mid) | mtg-role (right)
%
%  Usage:
%    \begin{participants}
%      \pmember{1}{ผู้ช่วยศาสตราจารย์ ดร.ชัชพล เกษวิริยะกิจ}{คณบดี}{ประธาน}
%      \pmember{2}{...}{...}{รองประธาน}
%    \end{participants}
% ============================================================
\newenvironment{participants}{%
  \par\small\sloppy
  \setlength\tabcolsep{4pt}%
  \begin{tabular}{@{}>{\RaggedRight\arraybackslash}p{6.5cm}>{\RaggedRight\arraybackslash}p{6.0cm}>{\RaggedRight\arraybackslash}p{2.2cm}@{}}%
}{%
  \end{tabular}\par\normalsize
}

% Normal member row
\newcommand\pmember[4]{%
  \thainum{#1}.\allowbreak{}#2 & #3 & #4 \\[4pt]%
}

% Long member — same as \pmember (\RaggedRight handles wrapping automatically)
\newcommand\pmemberL[4]{%
  \thainum{#1}.\allowbreak{}#2 & #3 & #4 \\[4pt]%
}

% Absent member: \pabsent{num}{name}{position}{reason}
\newcommand\pabsent[4]{%
  \thainum{#1}.\allowbreak{}#2 & #3 & #4 \\[3pt]%
}

% Observer (ผู้เข้าร่วมประชุม) — 2-column only
\newenvironment{observers}{%
  \par
  \setlength\tabcolsep{4pt}%
  \begin{tabular}{@{}p{7.8cm}l@{}}%
}{%
  \end{tabular}\par
}

\newcommand\pobserver[3]{%
  \thainum{#1}.\allowbreak{}#2 & #3 \\[3pt]%
}

% ============================================================
%  MEETING OPEN / CLOSE
% ============================================================
\newcommand\startmeeting{%
  \vspace{8pt}%
  \noindent{\bfseries เริ่มประชุม}\quad เวลา \@mtgstart\par
  \vspace{6pt}%
}

% ปิดการประชุม (ไม่ใช้ \endmeeting — TeX แยกเป็น \end + meeting)
\newcommand\adjournmeeting{%
  \vspace{10pt}%
  \noindent{\bfseries เลิกประชุม}\quad เวลา \@mtgend\par
}
\let\endmeeting\adjournmeeting

% Opening paragraph — ประธานกล่าวเปิดประชุม
% \openingchair{ชื่อ-ตำแหน่งประธาน}{ข้อความ}
\newcommand\openingchair[2]{%
  \noindent #1 #2\par
}

% ============================================================
%  AGENDA STRUCTURE
%
%  Level 1 — \agenda{๑}{เรื่องแจ้ง...}
%             bold, left-aligned, no indent
%
%  Level 2 — \subagenda{๑.๑}{เรื่องที่ประธาน...}
%             bold, centered
%
%  Level 3 — \subsubagenda{๑.๑.๑}{ขอเข้าไป...}
%             bold, centered
% ============================================================
\newcommand\agenda[2]{%
  \vspace{12pt}%
  \noindent{\bfseries ระเบียบวาระที่ #1\quad #2}\par
  \vspace{4pt}%
}

\newcommand\subagenda[2]{%
  \vspace{10pt}%
  \noindent{\bfseries วาระที่ #1\quad #2}\par%
  \vspace{4pt}%
}

\newcommand\subsubagenda[2]{%
  \vspace{8pt}%
  \noindent{\bfseries วาระที่ #1\quad #2}\par%
  \vspace{4pt}%
}

% Note inside an agenda item (เช่น "- ย้ายไปวาระสืบเนื่อง -")
\newcommand\agendanote[1]{%
  \begin{center}
    — #1 —
  \end{center}%
}

% ============================================================
%  RESOLUTION  — มติที่ประชุม
% ============================================================
\newcommand\resolution[1]{%
  \vspace{6pt}%
  \noindent\textbf{มติที่ประชุม}\quad #1\par
  \vspace{6pt}%
}

% ============================================================
%  FOLLOW-UP TABLE  (สรุปผลการดำเนินงานตามมติที่ประชุม)
%
%  Usage:
%    \begin{followuptable}
%      \followupheader{๗/๒๕๖๘}{๒๓ กรกฎาคม ๒๕๖๘}
%      ๔.๑ & เรื่อง... & เห็นชอบ... & ดำเนินการเรียบร้อย \\
%    \end{followuptable}
% ============================================================
\newenvironment{followuptable}{%
  \vspace{6pt}%
  \small
  \setlength\tabcolsep{5pt}%
  \begin{longtable}{|>{\centering\arraybackslash}p{1.2cm}|>{\RaggedRight\arraybackslash}p{4.6cm}|>{\RaggedRight\arraybackslash}p{4.6cm}|>{\RaggedRight\arraybackslash}p{3.0cm}|}%
  \hline
  \bfseries วาระที่ &
  \centering\bfseries เรื่อง &
  \centering\bfseries มติที่ประชุม &
  \centering\bfseries\arraybackslash ผลการดำเนินการ \\
  \hline
  \endfirsthead
  \hline
  \bfseries วาระที่ &
  \centering\bfseries เรื่อง &
  \centering\bfseries มติที่ประชุม &
  \centering\bfseries\arraybackslash ผลการดำเนินการ \\
  \hline
  \endhead
  \hline
  \endfoot
  \endlastfoot
}{%
  \end{longtable}%
}

% Header row inside follow-up table
% \followupheader{ครั้งที่}{วันที่}
\newcommand\followupheader[2]{%
  \multicolumn{4}{|l|}{\bfseries การประชุม ครั้งที่ #1 เมื่อวันที่ #2} \\ \hline
}

% ============================================================
%  SIGNATURE BLOCK
% ============================================================
\newenvironment{sigblock}{%
  \vspace{24pt}%
  \begin{center}%
}{%
  \end{center}%
}

% Typist — \typist{ชื่อ}
\newcommand\typist[1]{%
  \vspace{8pt}%
  (#1)\par
  ผู้พิมพ์รายงานการประชุม\par
}

% Reviewer — \reviewer{ชื่อ}{ตำแหน่ง}
\newcommand\reviewer[2]{%
  \vspace{16pt}%
  (#1)\par
  #2\par
  ผู้ตรวจทานรายงานการประชุม\par
}

% Chair sign-off — \chairsig{ชื่อ}{ตำแหน่ง}
\newcommand\chairsig[2]{%
  \vspace{16pt}%
  (#1)\par
  #2\par
}

% ============================================================
%  THAI NUMBERED LIST  (ตัวเลขไทย ๑. ๒. ๓.)
%
%  \begin{thailist}
%    \item ...
%  \end{thailist}
% ============================================================
\newlist{thailist}{enumerate}{3}
\setlist[thailist,1]{
  label   = \protect\thainum{\arabic*}.,
  leftmargin = 2.5cm,
  topsep     = 4pt,
  itemsep    = 2pt,
  parsep     = 0pt,
}
\setlist[thailist,2]{
  label   = \protect\thainum{\arabic*}.,
  leftmargin = 3.5cm,
}
\setlist[thailist,3]{
  label   = \protect\thainum{\arabic*}.,
  leftmargin = 4.5cm,
}

% ── End of class ─────────────────────────────────────────────
\endinput
