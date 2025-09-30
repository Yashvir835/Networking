# 🚀 Computer Networks — Interactive Examples

> A compact, hands‑on collection of **computer networking** examples implemented with **Python** and **Cisco Packet Tracer**. Designed for learners and developers who want fast, interactive experiments with client–server communication, TCP echo, DNS-like simulations, and simple topologies.

---

## 📌 Table of Contents

* [Project Overview](#project-overview)
* [Repository Structure](#repository-structure)
* [Try It — Interactive Quickstart](#try-it---interactive-quickstart)
* [Examples & Descriptions](#examples--descriptions)
* [Troubleshooting & Tests](#troubleshooting--tests)
* [Contributing](#contributing)
* [License](#license)
* [Contact & Acknowledgements](#contact--acknowledgements)

---

## Project Overview

This repository contains small, well‑commented examples that demonstrate core networking concepts using standard Python sockets and Cisco Packet Tracer topologies. The examples are intentionally minimal so you can modify and observe behavior immediately.

**Learning outcomes:**

* ✅ Socket-based client/server communication
* ✅ TCP echo pattern and round-trip observations
* ✅ Simple DNS-style query/response simulation
* ✅ Date/time request-response example
* ✅ Visual topology simulation with Packet Tracer

---

## Repository Structure

```
.git/                     # Git metadata (auto-hidden)
_basic_client_.py         # Minimal client example
_basic_server_.py         # Minimal server example
client.py                 # Simple client program
date_time_client.py       # Client requesting date & time
date_time_server.py       # Server responding with date & time
dns_client.py             # Educational DNS client
dns_server.py             # Educational DNS server
first_programing.pkt      # Packet Tracer: first networking program
ring_topology.pkt         # Packet Tracer: ring topology simulation
server.py                 # Simple server program
tcp_echo_client.py        # TCP Echo client
tcp_echo_server.py        # TCP Echo server
```

> Each file is compact and focused. Jump into any example and you should be able to run and iterate within minutes.

---

## ⚡ Try It — Interactive Quickstart

Use the following **three simple steps** to try a TCP echo round-trip locally.

<details>
<summary>1) Clone the repository 📥</summary>

```bash
git clone https://github.com/your-username/computer-networks-examples.git
cd computer-networks-examples
```

</details>

<details>
<summary>2) Start the echo server ▶️</summary>

```bash
# Start server in terminal A
python tcp_echo_server.py
# or
python3 tcp_echo_server.py
```

If the script contains configurable host/port variables, open it and adjust `HOST = '127.0.0.1'` and `PORT = 5000` (or your preferred port).

</details>

<details>
<summary>3) Run the echo client (in terminal B) 🖥️</summary>

```bash
python tcp_echo_client.py
# or
python3 tcp_echo_client.py
```

Type a message in the client terminal — the server should echo it back. ✅

</details>

> Tip: Use `127.0.0.1` for local tests. To test over LAN, bind the server to `0.0.0.0` and use the host machine IP on the client side (only in controlled lab environments).

---

## Examples & Descriptions 📚

* **`_basic_server_.py` / `_basic_client_.py`** — Bare‑minimum socket example. Good for understanding `socket()`, `bind()`, `listen()`, and `accept()`.

* **`server.py` / `client.py`** — Cleaned-up examples with input handling and basic error checks.

* **`tcp_echo_server.py` / `tcp_echo_client.py`** — Echo server pattern. Useful to measure round-trip times and practice non-blocking I/O experiments.

* **`date_time_server.py` / `date_time_client.py`** — Request/response pair where the server returns the current date/time.

* **`dns_server.py` / `dns_client.py`** — Educational simulation of name-to-address mapping and message parsing (not a production DNS).

* **`.pkt` files** — Visual simulations for topology learning in Cisco Packet Tracer: open them to inspect device configs and packet flows.

---

## 🧪 Troubleshooting & Tests

### Quick checklist

* Ensure Python 3.8+ is installed: `python --version`
* Start server before client
* If `Address already in use`, try a different port
* If `Connection refused`, check server process, host binding, firewall rules

### Common commands

```bash
# Find process using a port (Linux/macOS)
sudo lsof -i :<PORT>
# Kill a process by PID
sudo kill -9 <PID>
```

### Debugging tips

* Add `print()` statements inside server accept loop to confirm incoming connections.
* Use `tcpdump` / Wireshark (or Packet Tracer) to observe packet exchange.

---

## 🛠️ For Developers — Quick Enhancements

* Convert examples to asynchronous sockets (`asyncio`) to handle many clients.
* Add unit tests with `pytest` mocking sockets.
* Add CLI args (e.g. `--host`, `--port`) using `argparse`.

> Example CLI snippet to add to a server file:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--host', default='127.0.0.1')
parser.add_argument('--port', type=int, default=5000)
args = parser.parse_args()
HOST, PORT = args.host, args.port
```

---

## 🤝 Contributing

Contributions are welcome. Recommended workflow:

1. Fork the repository 🍴
2. Create a feature branch: `git checkout -b feature/your-change`
3. Add small, well‑commented examples
4. Run local tests and document usage
5. Open a Pull Request with description and testing steps

Please keep examples focused on pedagogy and code clarity.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## ✉️ Contact & Acknowledgements

Raise issues or PRs on the repository. For direct contact, add your preferred email to the repo profile.

Acknowledgements: Python `socket` documentation, Cisco Packet Tracer learning resources, and community contributors.

---

> Built for quick iteration and experimentation — enjoy exploring networking fundamentals! 🔬🌐
