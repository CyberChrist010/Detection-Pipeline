import json
from urllib.parse import urlparse

def parse_web_access_log(log_line):
    parts = log_line.split()
    return {
        "timestamp": parts[3] + ' ' + parts[4],
        "client_ip": parts[0],
        "request_method": parts[5],
        "request_url": urlparse(parts[6]).path,
        "response_code": parts[8],
        "user_agent": ' '.join(parts[11:])
    }

def main():
    log_file_path = '%SystemDrive%\inetpub\logs\'
    normalized_logs = []

    with open(log_file_path, 'r') as file:
        for line in file:
            normalized_logs.append(parse_web_access_log(line))

    with open('normalized_web_access_logs.json', 'w') as outfile:
        json.dump(normalized_logs, outfile)

if __name__ == "__main__":
    main()
