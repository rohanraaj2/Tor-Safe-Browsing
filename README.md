# Tor-Safe-Browsing

A simple Python script to verify and check the reputation and reachability of .onion (Tor hidden service) addresses.

## Features
- **Format Validation:** Checks if the provided .onion address is a valid v2 or v3 address.
- **Reputation Check:** Queries the Ahmia search engine to see if the onion address is indexed (suggesting reputation).
- **Online Status:** Attempts to connect to the onion site via the Tor SOCKS proxy to check if it is online.

## Requirements
- Python 3
- [requests[socks]](https://pypi.org/project/requests/) (`pip install requests[socks]`)
- Tor running locally (default: `127.0.0.1:9050`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/rohanraaj2/Tor-Safe-Browsing.git
   cd Tor-Safe-Browsing
   ```
2. Install dependencies:
   ```bash
   pip install requests[socks]
   ```
3. Start Tor (if not already running):
   ```bash
   tor &
   ```

## Usage
Run the script and follow the prompt:
```bash
python3 verify_onion.py
```
- Enter a .onion address (e.g., `abcdefghijklmnop.onion`)
- The script will:
  - Validate the address format
  - Check if it is indexed by Ahmia
  - Attempt to connect to the site via Tor

## Example Output
```
Enter the .onion address (e.g. abcdefghijklmnop.onion): exampleonionaddress.onion
[+] Valid .onion address format.
[+] Address is indexed by Ahmia — likely reputable.
[+] Onion site is reachable via Tor.
```

## Notes
- Only use this tool for legal and ethical purposes.
- The script does not store or log any addresses.
- For best results, ensure Tor is running and accessible on the default port.

## License
MIT License
