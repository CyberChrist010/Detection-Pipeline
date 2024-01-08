import pandas as pd
import json
from dateutil.parser import parse as date_parse
import re

def parse_json_log(log_line):
    try:
        return json.loads(log_line)
    except json.JSONDecodeError:
        return None

def anonymize_ip(ip_address):
    # Simple anonymization: Replace the last octet with 0
    # For IPv4 addresses. You can modify it for more complex scenarios or IPv6
    return re.sub(r'\.\d+$', '.0', ip_address)

def sanitize_string(input_string):
    # Basic sanitization to remove potential harmful characters
    # Can be expanded based on the data and security requirements
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def normalize_log_entry(log_entry):
    if 'timestamp' in log_entry:
        log_entry['timestamp'] = date_parse(log_entry['timestamp']).isoformat()
    if 'ip_address' in log_entry:
        log_entry['ip_address'] = anonymize_ip(log_entry['ip_address'])
    if 'event' in log_entry:
        log_entry['event'] = sanitize_string(log_entry['event']).lower()
    # Add more fields and normalization rules as needed

# Example usage
log_line = '{"timestamp": "2024-01-08T12:00:00", "event": "LoginAttempt", "status": "success", "ip_address": "192.168.1.100"}'
parsed_log = parse_json_log(log_line)

if parsed_log:
    normalize_log_entry(parsed_log)

df = pd.DataFrame([parsed_log])
print(df)
