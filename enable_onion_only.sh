#!/bin/bash

# Must be run as root
if [[ $EUID -ne 0 ]]; then
   echo "❌ This script must be run as root."
   exit 1
fi

TORRC_PATH="/etc/tor/torrc"
BACKUP_PATH="/etc/tor/torrc.backup.$(date +%s)"

echo "🔧 Backing up current torrc to $BACKUP_PATH"
cp "$TORRC_PATH" "$BACKUP_PATH"

# Enforce onion-only mode
echo "🔒 Applying onion-only exit policy..."
echo -e "\n# --- Onion-only mode enforced ---" >> "$TORRC_PATH"
echo "ExitPolicy reject *:*" >> "$TORRC_PATH"

echo "🔄 Restarting Tor..."
systemctl restart tor

echo "✅ Onion-only mode enabled. ExitPolicy now blocks all clearnet."
grep "ExitPolicy" "$TORRC_PATH"
