import pandas as pd
import json
from dateutil import parser
import re

def parse_json_log(log_line):
    try:
        return json.loads(log_line)
    except json.JSONDecodeError:
        return None

def anonymize_ip(ip_address):
    if ip_address:
        return re.sub(r'\.\d+$', '.0', ip_address)
    return ip_address

def sanitize_string(input_string):
    if input_string:
        return re.sub(r'[^a-zA-Z0-9\s]', '', input_string).lower()
    return input_string

def normalize_datetime(datetime_str):
    try:
        return parser.parse(datetime_str).isoformat()
    except (ValueError, TypeError):
        return None

def normalize_log_entry(log_entry):
    # Normalize timestamps
    datetime_keys = ['timestamp', 'time', 'logTime', 'eventTime', 'eventDateTime', 'date', 'event_time', 'time_logged']
    log_entry['normalized_timestamp'] = None
    for key in datetime_keys:
        if key in log_entry:
            log_entry['normalized_timestamp'] = normalize_datetime(log_entry.pop(key))
            break

    # Normalize IP addresses
    ip_keys = ['ip_address']
    log_entry['normalized_ip'] = None
    for key in ip_keys:
        if key in log_entry:
            log_entry['normalized_ip'] = anonymize_ip(log_entry.pop(key))
            break

    # Normalize event types
    event_keys = ['event', 'activity', 'action', 'eventType', 'log_event', 'activityType', 'event_type']
    log_entry['normalized_event'] = None
    for key in event_keys:
        if key in log_entry:
            log_entry['normalized_event'] = sanitize_string(log_entry.pop(key))
            break

    # Normalize user-related fields
    user_keys = ['user', 'account', 'changed_by', 'executed_by', 'updated_by']
    log_entry['normalized_user'] = None
    for key in user_keys:
        if key in log_entry:
            log_entry['normalized_user'] = sanitize_string(log_entry.pop(key))
            break

    # Normalize status messages
    status_keys = ['status', 'outcome', 'result']
    log_entry['normalized_status'] = None
    for key in status_keys:
        if key in log_entry:
            log_entry['normalized_status'] = sanitize_string(log_entry.pop(key))
            break

    # Additional specific fields normalization
    # Normalize file paths
    if 'file_path' in log_entry:
        log_entry['normalized_file_path'] = sanitize_string(log_entry.pop('file_path'))

    # Normalize error codes
    if 'error_code' in log_entry:
        log_entry['normalized_error_code'] = int(log_entry.pop('error_code', 0))

    # Add more fields and normalization rules as needed

    return log_entry

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            parsed_log = parse_json_log(line)
            if parsed_log:
                yield normalize_log_entry(parsed_log)

# File path
log_file_path = 'sample_logs.json'

# Processing log file
logs = list(read_log_file(log_file_path))

# Creating DataFrame
df = pd.DataFrame(logs)
print(df)
