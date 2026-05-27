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

# Bootstrap the local profiles config from the shipped example if missing.
# profiles.toml is gitignored; profiles.example.toml is the public default.
CONFIG_DIR="$LIBRARY_PATH/config"
ACTIVE_CONFIG="$CONFIG_DIR/profiles.toml"
EXAMPLE_CONFIG="$CONFIG_DIR/profiles.example.toml"
if [[ -f "$ACTIVE_CONFIG" ]]; then
    : # local config already present; do not touch
elif [[ -f "$EXAMPLE_CONFIG" ]]; then
    cp "$EXAMPLE_CONFIG" "$ACTIVE_CONFIG"
    # Users may add API keys or personal calibration paths to profiles.toml
    # later. Tighten permissions now so the file is not group-readable on
    # shared filesystems (umask 022 leaves it world-readable by default).
    chmod 600 "$ACTIVE_CONFIG"
    echo "  bootstrapped: config/profiles.toml (from profiles.example.toml)"
else
    echo "  WARNING: neither $ACTIVE_CONFIG nor $EXAMPLE_CONFIG exists." >&2
    echo "  Agents will fail until config/profiles.toml or" >&2
    echo "  config/profiles.example.toml is created." >&2
fi

echo ""
echo "Done. $installed agent(s) installed to $AGENTS_DEST"
echo "They are now available in all Claude Code projects."
echo ""
echo "Local profile config: $ACTIVE_CONFIG"
echo "Edit it to add people or styles. Run the style-analyzer agent to"
echo "calibrate stylometry values for a new person."
echo ""
echo "To update after moving the repository, re-run this script."
