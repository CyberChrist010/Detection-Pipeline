import json

def parse_json_log(log_line):
    try:
        return json.loads(log_line)
    except json.JSONDecodeError:
        return None

# Example usage
log_line = '{"timestamp": "2024-01-08T12:00:00", "event": "login", "status": "success"}'
parsed_log = parse_json_log(log_line)
print(parsed_log)
