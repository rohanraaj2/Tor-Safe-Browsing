
# Tor Privacy Tools Bundle

This toolkit is designed for journalists, whistleblowers, activists, and privacy-conscious users to easily set up and verify secure Tor-based communication and .onion addresses.

---

## 🔧 Included Files

### 1. `verify_onion.py`
- Verifies .onion URLs by:
  - Checking valid v2/v3 onion address format
  - Checking if the onion URL is indexed by Ahmia search engine
  - Checking if the onion site is reachable via Tor SOCKS proxy
- **Requires:** Python 3, [requests[socks]](https://pypi.org/project/requests/) (`pip install requests[socks]`), Tor running locally (default: `127.0.0.1:9050`)

**Usage:**
```bash
python3 verify_onion.py
```

---

### 2. `check_tor_bridge.sh`
- Verifies whether your system is routing traffic through **Tor SOCKS5 proxy**.
- Compatible with **obfs4 bridges** or standard Tor routing.

**Usage:**
```bash
bash check_tor_bridge.sh
```

---

### 3. `torrc-bridge-tails`
- Minimal Tor configuration using **obfs4 bridge**.
- Ideal for Tails OS or CLI environments.
- Replace `[REPLACE_WITH_BRIDGE]` with your real bridge line from [https://bridges.torproject.org/](https://bridges.torproject.org/).

**Usage:**
```bash
tor -f ~/torrc-bridge-tails
```

---

### 4. `autostart-tor.sh`
- Simple helper to autostart Tor using the `torrc-bridge-tails` config.
- Add to autostart routines or run manually after boot.

**Usage:**
```bash
chmod +x autostart-tor.sh
./autostart-tor.sh
```

---

## 📌 Notes

- Ensure `curl` and `obfs4proxy` are installed for full functionality.
- Works best on **Linux** and **Tails OS**.
- Requires internet access and obfs4 bridge from Tor Project.
- Only use these tools for legal and ethical purposes.
- The scripts do not store or log any addresses.

Stay safe ✊

---

## License
MIT License
