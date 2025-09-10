# 📖 Usage Guide – Python Security Automation Toolkit

This document explains how to run and combine the scripts in **py-sec-tools**.

---

## 1. SSH Log Parser
The **ssh_log_parser.py** script scans an `auth.log` file for failed SSH login attempts.

### Run:
```bash
python scripts/ssh_log_parser.py examples/sample_auth.log
```

### Example Output:
```
SSH Failed Login Report - 2025-09-10 01:00
192.168.1.50: 2 attempts
10.0.0.23: 1 attempts
```

---

## 2. IP Blocker
The **ip_blocker.py** script blocks IP addresses using either **UFW** or **iptables**.

### Run:
```bash
sudo python scripts/ip_blocker.py
```

⚠️ **Note**: Root privileges are required since this modifies firewall rules.

---

## 3. Export Results
The **export_results.py** script saves IP → failed login attempt mappings into **CSV** or **JSON**.

### Run:
```bash
python scripts/export_results.py
```

### Example Output:
- `examples/sample_output.csv`
- `examples/sample_output.json`

---

## 4. Suggested Workflow
1. Parse the log:
   ```bash
   python scripts/ssh_log_parser.py /var/log/auth.log > results.txt
   ```
2. Extract IPs with multiple failed attempts.  
3. Pass those IPs into `ip_blocker.py`.  
4. Export the data into CSV/JSON with `export_results.py`.  

---

## 🔧 Customization
- Update `FAILED_REGEX` in `ssh_log_parser.py` to detect different log formats.  
- Modify `suspicious_ips` in `ip_blocker.py` to block custom IP lists.  
- Change filenames in `export_results.py` to save under different paths.

---

## 📌 Example Workflow Demo
```bash
# Step 1: Parse logs
python scripts/ssh_log_parser.py examples/sample_auth.log

# Step 2: Block suspicious IPs
sudo python scripts/ip_blocker.py

# Step 3: Export data
python scripts/export_results.py
```

---

## ✅ Best Use Case
This toolkit is designed for **educational and portfolio demonstration purposes**.  
In real-world production systems, intrusion detection and firewall blocking should be handled by enterprise security tools (IDS/IPS, SIEMs).
