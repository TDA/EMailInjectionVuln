import json

__author__ = 'saipc'

def load_json_file(file):
    with open(file, 'r') as json_file:
        json_data = json.loads(json_file)
        return json_data

if __name__ == '__main__':
    load_json_file('')