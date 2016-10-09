__author__ = 'saipc'

import json

def load_json_file(file):
    with open(file, 'r') as json_file:
        json_data = json.loads(json_file.read())
        return json_data

def save_json_file(file, json_data):
    with open(file, 'w') as json_file:
        json_file.write(json.dumps(json_data))

def parse_json(json_data):
    pass

def get_size_json(json_data):
    return len(json_data.keys())
