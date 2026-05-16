# SyncTeX: required for inverse search (PDF click → .tex) in LaTeX Workshop
$synctex = 1;
# This project uses XeLaTeX (fontspec / polyglossia in aunqa.cls)
$pdf_mode = 5;

# Force SyncTeX flag for XeLaTeX runs (ensures .synctex.gz is generated)
$xelatex = 'xelatex -synctex=1 %O %S';
