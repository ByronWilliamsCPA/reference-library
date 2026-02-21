#!/usr/bin/env bash
# Install reference-library agents globally for Claude Code.
#
# Run once after cloning. Re-run if you move the repository.
# Agents are installed to ~/.claude/agents/ and become available
# in every Claude Code project without any per-project configuration.
#
# Usage:
#   bash scripts/setup.sh

set -euo pipefail

LIBRARY_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENTS_SRC="$LIBRARY_PATH/agents"
AGENTS_DEST="$HOME/.claude/agents"

echo "reference-library agent installer"
echo "  Library path : $LIBRARY_PATH"
echo "  Agents dest  : $AGENTS_DEST"
echo ""

if [[ ! -d "$AGENTS_SRC" ]]; then
    echo "Error: agents/ directory not found at $AGENTS_SRC" >&2
    exit 1
fi

mkdir -p "$AGENTS_DEST"

installed=0
for src in "$AGENTS_SRC"/*.md; do
    filename="$(basename "$src")"
    dest="$AGENTS_DEST/$filename"
    sed "s|{{LIBRARY_PATH}}|$LIBRARY_PATH|g" "$src" > "$dest"
    echo "  installed: $filename"
    installed=$((installed + 1))
done

echo ""
echo "Done. $installed agent(s) installed to $AGENTS_DEST"
echo "They are now available in all Claude Code projects."
echo ""
echo "To update after moving the repository, re-run this script."
