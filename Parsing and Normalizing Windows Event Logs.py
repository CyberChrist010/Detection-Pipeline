Parsing and Normalizing Windows Event Logs
This script parses Windows Event Logs, focusing on security-related events.

import json
import xml.etree.ElementTree as ET

def parse_windows_event_log(xml_log):
    root = ET.fromstring(xml_log)
    event_data = {}

    for child in root:
        if child.tag.endswith('System'):
            for item in child:
                if item.tag.endswith('EventID'):
                    event_data['event_id'] = item.text
                elif item.tag.endswith('TimeCreated'):
                    event_data['timestamp'] = item.attrib['SystemTime']
                elif item.tag.endswith('Computer'):
                    event_data['computer'] = item.text

    return event_data

def main():
    log_file_path = '/path/to/windows/event/logs'
    normalized_logs = []

    with open(log_file_path, 'r') as file:
        for line in file:
            normalized_logs.append(parse_windows_event_log(line))

    with open('normalized_windows_event_logs.json', 'w') as outfile:
        json.dump(normalized_logs, outfile)

if __name__ == "__main__":
    main()