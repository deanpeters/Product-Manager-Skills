#!/usr/bin/env bash
#
# build-release.sh - Validate and build all downloadable release artifacts.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DIST_DIR="$ROOT/dist"
RELEASE_DIR="$DIST_DIR/release"

if ! command -v zip >/dev/null 2>&1; then
  echo "Error: 'zip' command not found. Install zip and retry." >&2
  exit 1
fi

version="$(git -C "$ROOT" describe --tags --exact-match 2>/dev/null || true)"
if [[ -z "$version" ]]; then
  version="dev"
fi

echo "[1/4] Validating skills"
bash "$SCRIPT_DIR/validate-skills.sh"

echo
echo "[2/4] Building Claude Desktop/Web packs"
bash "$SCRIPT_DIR/build-claude-desktop-packs.sh"

echo
echo "[3/4] Building Codex package"
bash "$SCRIPT_DIR/build-codex-skills.sh"

echo
echo "[4/4] Building master release artifact"
rm -rf "$RELEASE_DIR"
mkdir -p "$RELEASE_DIR/docs"

cp -R "$DIST_DIR/claude-desktop" "$RELEASE_DIR/"
cp -R "$DIST_DIR/codex" "$RELEASE_DIR/"
cp "$ROOT/README.md" "$RELEASE_DIR/README.md"

for doc in \
  INSTALL-CLAUDE-DESKTOP.md \
  INSTALL-CLAUDE-CODE.md \
  INSTALL-CODEX.md \
  RELEASE-PACKAGING.md
do
  if [[ -f "$ROOT/docs/$doc" ]]; then
    cp "$ROOT/docs/$doc" "$RELEASE_DIR/docs/$doc"
  fi
done

artifact="$DIST_DIR/Product-Manager-Skills-$version-release.zip"
rm -f "$artifact"
(cd "$RELEASE_DIR" && zip -qr "$artifact" claude-desktop codex docs README.md)

echo
echo "Release artifacts:"
echo "  $artifact"
echo "  $DIST_DIR/claude-desktop/*.zip"
echo "  $DIST_DIR/codex/codex-product-manager-skills.zip"
