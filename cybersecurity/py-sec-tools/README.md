# 🐍 Python Security Automation Toolkit (py-sec-tools)

A collection of Python scripts that automate common cybersecurity tasks such as log analysis, intrusion detection, and IP blocking.  
This project is part of my cybersecurity portfolio and demonstrates applied skills in **Python scripting, regex, log parsing, firewall automation, and reporting**.

---

## 🚀 Features
- **SSH Failed Login Detection** → Parses `auth.log` for failed SSH attempts.
- **IP Auto-Blocker** → Blocks suspicious IPs via UFW or iptables.
- **Data Export** → Exports results into CSV/JSON for reporting.

---

## 📂 Project Structure
```
py-sec-tools/
├─ README.md
├─ requirements.txt
├─ scripts/
│  ├─ ssh_log_parser.py      # Detect failed SSH logins
│  ├─ ip_blocker.py          # Block suspicious IPs
│  └─ export_results.py      # Export findings
├─ examples/
│  ├─ sample_auth.log        # Example log input
│  └─ sample_output.csv      # Example export
└─ docs/
   └─ usage.md               # Detailed usage instructions
```

---

## 🛠️ Requirements
- Python **3.9+**
- Linux environment with **UFW** or **iptables**
- `paramiko` (optional future SSH automation)

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ⚡ Quick Start

### Detect Failed SSH Logins
```bash
python scripts/ssh_log_parser.py examples/sample_auth.log
```

### Block IPs with UFW
```bash
sudo python scripts/ip_blocker.py
```

### Export Data
```bash
python scripts/export_results.py
```

---

## 📊 Example Output
```
SSH Failed Login Report - 2025-09-10 01:00
192.168.1.50: 2 attempts
10.0.0.23: 1 attempts
```

---

## 🔗 Documentation
See the full [Usage Guide](docs/usage.md) for detailed instructions.

---

## 📜 License
Licensed under the **Apache License 2.0**.  
See the [LICENSE](../LICENSE) file for details.
