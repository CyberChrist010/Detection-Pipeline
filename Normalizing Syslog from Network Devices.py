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

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                parsed_log = parse_syslog(line)
                if parsed_log:
                    normalized_logs.append(parsed_log)
                else:
                    print(f"Malformed log entry: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file {log_file_path} was not found.")
        return
    except IOError:
        print(f"Error: Unable to read the file {log_file_path}.")
        return

    try:
        with open('normalized_syslog.json', 'w') as outfile:
            json.dump(normalized_logs, outfile)
    except IOError:
        print("Error: Unable to write to normalized_syslog.json.")

if __name__ == "__main__":
    main()
