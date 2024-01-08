import json
import re

def parse_linux_log(log_line):
    # Pattern for a standard Linux log line
    pattern = re.compile(r'(\S+ \d+ \d+:\d+:\d+) (\S+) (\S+): (.*)')
    match = pattern.match(log_line)

    if match:
        return {
            "timestamp": match.group(1),
            "host": match.group(2),
            "process": match.group(3),
            "message": match.group(4)
        }
    else:
        return None

def main():
    log_file_path = '/var/logs/'
    normalized_logs = []

    with open(log_file_path, 'r') as file:
        for line in file:
            parsed_log = parse_linux_log(line)
            if parsed_log:
                normalized_logs.append(parsed_log)

    # Exporting to JSON for SIEM import
    with open('normalized_linux_host_logs.json', 'w') as outfile:
        json.dump(normalized_logs, outfile)

if __name__ == "__main__":
    main()
