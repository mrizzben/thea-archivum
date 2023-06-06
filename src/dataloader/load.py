import json


def json_load(filepath: str):
    with open(filepath, 'r') as file:
        json_data = file.read()
    data = json.loads(json_data)
    return data
