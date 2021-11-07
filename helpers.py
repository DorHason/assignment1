def validate_payload(json_data):
    if not json_data:
        return False
    # entries must be non-negative integer
    if 'entries' not in json_data.keys() or type(json_data['entries']) != int or json_data['entries'] < 0:
        return False
    return True
