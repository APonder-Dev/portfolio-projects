import subprocess

def block_ip(ip, firewall="ufw"):
    if firewall == "ufw":
        cmd = ["sudo", "ufw", "deny", "from", ip]
    else:  # fallback to iptables
        cmd = ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"]

    try:
        subprocess.run(cmd, check=True)
        print(f"[+] Blocked IP: {ip}")
    except subprocess.CalledProcessError:
        print(f"[-] Failed to block {ip}")

if __name__ == "__main__":
    suspicious_ips = ["192.168.1.50", "10.0.0.23"]  # demo list
    for ip in suspicious_ips:
        block_ip(ip)
