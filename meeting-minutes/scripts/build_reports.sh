#!/usr/bin/env bash
# ============================================================
#  build_reports.sh
#  Compile all meeting .tex files → PDF using meetingminutes.cls
#  Usage:  bash build_reports.sh          # compile all
#          bash build_reports.sh SLUG     # compile one file (no extension)
# ============================================================
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="$DIR/pdf"
mkdir -p "$OUT"

compile_one() {
  local tex="$1"
  local base="${tex%.tex}"
  local name="$(basename "$base")"
  echo "▶  $name"
  xelatex -interaction=nonstopmode \
           -output-directory="$OUT" \
           "$tex" > /dev/null 2>&1 && echo "   ✓  $name.pdf" \
                                  || echo "   ✗  FAILED — check $OUT/$name.log"
}

if [[ -n "$1" ]]; then
  compile_one "$DIR/$1.tex"
else
  for tex in "$DIR"/*.tex; do
    [[ "$(basename "$tex")" == example-* ]] && continue
    compile_one "$tex"
  done
fi
echo "Done — PDF files in: $OUT"
