Normalizing Syslog from Network Devices
This script normalizes Syslog messages from various network devices.

import json
import re

def parse_syslog(log_line):
    pattern = re.compile(r'<(\d+)>(\S+ \d+ \d+:\d+:\d+) (\S+) (\S+): (.*)')
    match = pattern.match(log_line)

    if match:
        return {
            "severity": match.group(1),
            "timestamp": match.group(2),
            "device": match.group(3),
            "process": match.group(4),
            "message": match.group(5)
        }
    else:
        return None

def main():
    log_file_path = '/path/to/syslog'
    normalized_logs = []

    with open(log_file_path, 'r') as file:
        for line in file:
            parsed_log = parse_syslog(line)
            if parsed_log:
                normalized_logs.append(parsed_log)

    with open('normalized_syslog.json', 'w') as outfile:
        json.dump(normalized_logs, outfile)

if __name__ == "__main__":