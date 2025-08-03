#!/usr/bin/env python3
"""
verify_onion.py

Verify .onion URLs by:
- Checking valid v2/v3 onion address format
- Checking if the onion URL is indexed by Ahmia search engine
- Checking if the onion site is reachable via Tor SOCKS proxy

Requires:
- Python 3
- requests[socks] package (pip install requests[socks])
- Tor running locally on 127.0.0.1:9050
"""

import re
import requests

# Regex for valid onion v2 (16 chars) or v3 (56 chars) addresses
ONION_REGEX = re.compile(r'^([a-z2-7]{16}|[a-z2-7]{56})\.onion$', re.IGNORECASE)

def is_valid_onion(url: str) -> bool:
    """Check if URL has a valid .onion hostname format."""
    hostname = url.lower().replace('http://', '').replace('https://', '').split('/')[0]
    return bool(ONION_REGEX.fullmatch(hostname))

def check_ahmia(onion_url: str) -> bool:
    """Check if onion URL is indexed by Ahmia search engine."""
    try:
        search_url = f'https://ahmia.fi/search/?q={onion_url}'
        resp = requests.get(search_url, timeout=5)
        return onion_url.lower() in resp.text.lower()
    except Exception:
        return False

def check_onion_online(onion_url: str) -> bool:
    """Try connecting to the onion site via Tor SOCKS proxy."""
    try:
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        resp = requests.get(f"http://{onion_url}/", proxies=proxies, timeout=15)
        return resp.status_code == 200
    except Exception:
        return False

def main():
    onion = input("Enter the .onion address (e.g. abcdefghijklmnop.onion): ").strip()
    if not is_valid_onion(onion):
        print("[!] Invalid .onion address format.")
        return
    print("[+] Valid .onion address format.")

    if check_ahmia(onion):
        print("[+] Address is indexed by Ahmia — likely reputable.")
    else:
        print("[!] Address not found on Ahmia — caution advised.")

    if check_onion_online(onion):
        print("[+] Onion site is reachable via Tor.")
    else:
        print("[!] Onion site is offline or unreachable.")

if __name__ == '__main__':
    main()
