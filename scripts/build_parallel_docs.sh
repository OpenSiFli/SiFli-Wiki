#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ -n "${SPHINX_BUILD:-}" ]]; then
  SPHINX_CMD=("$SPHINX_BUILD")
elif [[ -x "$ROOT_DIR/venv/bin/sphinx-build" ]]; then
  SPHINX_CMD=("$ROOT_DIR/venv/bin/sphinx-build")
elif command -v sphinx-build >/dev/null 2>&1; then
  SPHINX_CMD=("$(command -v sphinx-build)")
else
  echo "sphinx-build not found." >&2
  echo "Install the Python requirements, set SPHINX_BUILD=/path/to/sphinx-build, or create the local venv first." >&2
  exit 1
fi

"${SPHINX_CMD[@]}" -b html "$ROOT_DIR/source/zh_CN" "$ROOT_DIR/build" -E
"${SPHINX_CMD[@]}" -b html "$ROOT_DIR/source/en" "$ROOT_DIR/build/en" -E

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
