 Parsing and Normalizing Firewall Logs
This script reads firewall logs, normalizes the data, and prepares it for import into a SIEM.

python
Copy code
import json
import re

def parse_firewall_log(log_line):
    # Regex pattern for a hypothetical firewall log
    pattern = re.compile(r'(\S+) (\S+) (\S+) (\S+) (\S+)')
    match = pattern.match(log_line)

    if match:
        return {
            "timestamp": match.group(1),
            "src_ip": match.group(2),
            "dest_ip": match.group(3),
            "port": match.group(4),
            "action": match.group(5)
        }
    else:
        return None

def main():
    log_file_path = '/path/to/firewall/logs'
    normalized_logs = []

    with open(log_file_path, 'r') as file:
        for line in file:
            parsed_log = parse_firewall_log(line)
            if parsed_log:
                normalized_logs.append(parsed_log)

    # Exporting to JSON for SIEM import
    with open('normalized_firewall_logs.json', 'w') as outfile:
        json.dump(normalized_logs, outfile)

if __name__ == "__main__":
    main()
	