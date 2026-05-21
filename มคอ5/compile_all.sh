#!/bin/bash
# คอมไพล์ มคอ.5 ทุกรายวิชา
set -e
cd "$(dirname "$0")"
for f in AUN3_7015101 AUN3_7015906 AUN3_4095101 AUN3_4095102 example; do
  echo "=== $f ==="
  xelatex -interaction=nonstopmode "${f}.tex" 2>&1 | tail -1
  xelatex -interaction=nonstopmode "${f}.tex" 2>&1 | tail -1
done
echo "Done."
