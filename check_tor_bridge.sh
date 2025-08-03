#!/bin/bash

echo "🧪 Checking Tor SOCKS5 routing..."

RESPONSE=$(curl -s --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/)

if echo "$RESPONSE" | grep -q "Congratulations. This browser is configured to use Tor."; then
    echo "✅ Success: Traffic is routed through Tor."
else
    echo "❌ Warning: Traffic is NOT going through Tor."
    echo "⚠️ Response:"
    echo "$RESPONSE"
fi
