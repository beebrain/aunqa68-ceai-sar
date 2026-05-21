#!/usr/bin/env python3
"""
Convert Markdown meeting minutes to PDF using XeLaTeX.
Handles Thai language content.
"""

import os
import re
import subprocess
import tempfile
import sys

WORKING_DIR = "/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/meeting-minutes"
PDF_DIR = os.path.join(WORKING_DIR, "pdf")
XELATEX = "/Library/TeX/texbin/xelatex"


def escape_latex(text):
    """Escape special LaTeX characters."""
    # Order matters - backslash first
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('^', r'\^{}'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def md_table_to_latex(table_lines):
    """Convert Markdown table to LaTeX tabular."""
    rows = []
    col_count = 0
    for line in table_lines:
        line = line.strip()
        if not line.startswith('|'):
            continue
        # Skip separator line (contains dashes)
        if re.match(r'^\|[-\s|:]+\|$', line):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if col_count == 0:
            col_count = len(cells)
        escaped = [escape_latex(c) for c in cells]
        rows.append(' & '.join(escaped) + r' \\')

    if not rows:
        return ''

    col_spec = '|' + '|'.join(['l'] * col_count) + '|'
    latex = [
        r'\begin{longtable}{' + col_spec + '}',
        r'\hline',
    ]
    for i, row in enumerate(rows):
        latex.append(row)
        latex.append(r'\hline')
    latex.append(r'\end{longtable}')
    return '\n'.join(latex)


def markdown_to_latex_body(md_text):
    """Convert Markdown text to LaTeX body content."""
    lines = md_text.split('\n')
    latex_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Detect table: starts with |
        if line.strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|[-\s|:]+\|\s*$', lines[i + 1]):
            # Collect table lines
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            latex_lines.append(md_table_to_latex(table_lines))
            continue

        # Headings
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            title = escape_latex(m.group(2))
            heading_map = {
                1: r'\section*{' + title + '}',
                2: r'\subsection*{' + title + '}',
                3: r'\subsubsection*{' + title + '}',
                4: r'\paragraph{' + title + '}',
                5: r'\subparagraph{' + title + '}',
                6: r'\subparagraph{' + title + '}',
            }
            latex_lines.append(heading_map[level])
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+\s*$', line):
            latex_lines.append(r'\vspace{4pt}\hrule\vspace{4pt}')
            i += 1
            continue

        # Blockquote
        if line.strip().startswith('>'):
            content = escape_latex(line.strip().lstrip('>').strip())
            latex_lines.append(r'\begin{quote}' + content + r'\end{quote}')
            i += 1
            continue

        # Unordered list items
        if re.match(r'^(\s*[-*+])\s+', line):
            latex_lines.append(r'\begin{itemize}')
            while i < len(lines) and re.match(r'^\s*[-*+]\s+', lines[i]):
                content = re.sub(r'^\s*[-*+]\s+', '', lines[i])
                content = inline_format(content)
                latex_lines.append(r'  \item ' + content)
                i += 1
            latex_lines.append(r'\end{itemize}')
            continue

        # Ordered list items
        if re.match(r'^\s*\d+\.\s+', line):
            latex_lines.append(r'\begin{enumerate}')
            while i < len(lines) and re.match(r'^\s*\d+\.\s+', lines[i]):
                content = re.sub(r'^\s*\d+\.\s+', '', lines[i])
                content = inline_format(content)
                latex_lines.append(r'  \item ' + content)
                i += 1
            latex_lines.append(r'\end{enumerate}')
            continue

        # Empty line
        if line.strip() == '':
            latex_lines.append('')
            i += 1
            continue

        # Normal paragraph line
        latex_lines.append(inline_format(line))
        i += 1

    return '\n'.join(latex_lines)


def inline_format(text):
    """Handle inline Markdown formatting: bold, italic, code, links."""
    # Bold+italic ***text***
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\\textbf{\\textit{\1}}', text)
    # Bold **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
    # Italic *text*
    text = re.sub(r'\*(.+?)\*', r'\\textit{\1}', text)
    # Inline code `text`
    text = re.sub(r'`(.+?)`', r'\\texttt{\1}', text)
    # Links [text](url)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    # Trailing spaces (line break in MD)
    text = text.rstrip('  ')
    # Escape remaining special chars NOT already escaped
    # (escape_latex would double-escape, so handle only leftover & and #)
    # Actually we handle escape inside escape_latex per cell; here escape remaining
    text = text.replace('&', r'\&').replace('%', r'\%')
    return text


def build_latex_document(md_text, filename):
    """Wrap converted body in full XeLaTeX document."""
    body = markdown_to_latex_body(md_text)
    doc = r"""\documentclass[12pt,a4paper]{article}
\usepackage{fontspec}
\usepackage{polyglossia}
\setmainlanguage{thai}
\setotherlanguage{english}
\setmainfont{TH Sarabun New}
\setsansfont{TH Sarabun New}
\setmonofont[Scale=0.85]{Courier New}
\usepackage{geometry}
\geometry{margin=2.5cm, top=2.5cm, bottom=2.5cm}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{array}
\usepackage{parskip}
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=blue, urlcolor=blue}
\usepackage{microtype}
\usepackage{graphicx}
\pagestyle{plain}
\begin{document}
""" + body + r"""
\end{document}
"""
    return doc


def convert_file(md_path, pdf_output_dir):
    """Convert a single Markdown file to PDF."""
    filename = os.path.basename(md_path)
    pdf_name = filename.replace('.md', '.pdf')
    pdf_path = os.path.join(pdf_output_dir, pdf_name)

    print(f"  Converting: {filename} -> {pdf_name}")

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    latex_doc = build_latex_document(md_text, filename)

    # Write to temp dir and compile
    with tempfile.TemporaryDirectory() as tmpdir:
        tex_path = os.path.join(tmpdir, 'document.tex')
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(latex_doc)

        result = subprocess.run(
            [XELATEX, '-interaction=nonstopmode', '-output-directory', tmpdir, tex_path],
            capture_output=True, text=True, timeout=60
        )

        compiled_pdf = os.path.join(tmpdir, 'document.pdf')
        if os.path.exists(compiled_pdf):
            import shutil
            shutil.copy2(compiled_pdf, pdf_path)
            print(f"    OK: {pdf_path}")
            return True
        else:
            print(f"    FAILED: {filename}")
            print(f"    --- XeLaTeX stdout (last 20 lines) ---")
            for line in result.stdout.split('\n')[-20:]:
                print(f"    {line}")
            print(f"    --- XeLaTeX stderr ---")
            print(result.stderr[-500:] if result.stderr else "(none)")
            return False


def main():
    os.makedirs(PDF_DIR, exist_ok=True)

    md_files = sorted([
        f for f in os.listdir(WORKING_DIR)
        if f.endswith('.md') and f != 'INDEX.md'
    ])

    print(f"Found {len(md_files)} meeting minute files to convert.")
    print(f"Output directory: {PDF_DIR}\n")

    success_count = 0
    failed = []

    for md_file in md_files:
        md_path = os.path.join(WORKING_DIR, md_file)
        ok = convert_file(md_path, PDF_DIR)
        if ok:
            success_count += 1
        else:
            failed.append(md_file)

    print(f"\n=== Conversion Summary ===")
    print(f"Success: {success_count}/{len(md_files)}")
    if failed:
        print(f"Failed ({len(failed)}):")
        for f in failed:
            print(f"  - {f}")


if __name__ == '__main__':
    main()
