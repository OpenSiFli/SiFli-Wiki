#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPHINX_BUILD="${SPHINX_BUILD:-$ROOT_DIR/venv/bin/sphinx-build}"

if [[ ! -x "$SPHINX_BUILD" ]]; then
  echo "sphinx-build not found: $SPHINX_BUILD" >&2
  echo "Set SPHINX_BUILD=/path/to/sphinx-build or create the local venv first." >&2
  exit 1
fi

"$SPHINX_BUILD" -b html "$ROOT_DIR/source/zh_CN" "$ROOT_DIR/build" -E
"$SPHINX_BUILD" -b html "$ROOT_DIR/source/en" "$ROOT_DIR/build/en" -E

if [[ -f "$ROOT_DIR/lcd_frequency.html" ]]; then
  mkdir -p "$ROOT_DIR/build/tools/屏幕调试" "$ROOT_DIR/build/en/tools/屏幕调试"
  cp "$ROOT_DIR/lcd_frequency.html" "$ROOT_DIR/build/tools/屏幕调试/lcd_frequency.html"
  if [[ -f "$ROOT_DIR/lcd_frequency.en.html" ]]; then
    cp "$ROOT_DIR/lcd_frequency.en.html" "$ROOT_DIR/build/en/tools/屏幕调试/lcd_frequency.html"
  else
    cp "$ROOT_DIR/lcd_frequency.html" "$ROOT_DIR/build/en/tools/屏幕调试/lcd_frequency.html"
  fi
fi

echo "Built Chinese site: $ROOT_DIR/build"
echo "Built English site: $ROOT_DIR/build/en"
