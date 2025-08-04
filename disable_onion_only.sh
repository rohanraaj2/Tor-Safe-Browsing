#!/bin/bash

# Must be run as root
if [[ $EUID -ne 0 ]]; then
   echo "❌ This script must be run as root."
   exit 1
fi

TORRC_PATH="/etc/tor/torrc"
TEMP_PATH="/tmp/torrc.cleaned.$(date +%s)"

echo "🧹 Removing onion-only ExitPolicy..."

# Remove the ExitPolicy reject line
grep -v "ExitPolicy reject \*\:\*" "$TORRC_PATH" > "$TEMP_PATH"
mv "$TEMP_PATH" "$TORRC_PATH"

# Restart Tor
echo "🔄 Restarting Tor..."
systemctl restart tor

echo "✅ Onion-only mode disabled. Clearnet access via Tor restored."
grep "ExitPolicy" "$TORRC_PATH"
