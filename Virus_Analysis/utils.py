__author__ = 'saipc'

import json

def load_json_file(file):
    with open(file, 'r') as json_file:
        json_data = json.loads(json_file.read())
        return json_data

def parse_json(jsonData):
    pass

def get_size_json(jsonData):
    return len(jsonData.keys())
