import re
import sys
from datetime import datetime

FAILED_REGEX = r"Failed password for (invalid user )?.* from (\d+\.\d+\.\d+\.\d+)"

def parse_auth_log(log_file):
    failed_ips = {}
    with open(log_file, "r") as f:
        for line in f:
            match = re.search(FAILED_REGEX, line)
            if match:
                ip = match.group(2)
                failed_ips[ip] = failed_ips.get(ip, 0) + 1
    return failed_ips

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ssh_log_parser.py <auth.log>")
        sys.exit(1)

    log_file = sys.argv[1]
    results = parse_auth_log(log_file)
    print(f"SSH Failed Login Report - {datetime.now()}")
    for ip, count in results.items():
        print(f"{ip}: {count} attempts")
