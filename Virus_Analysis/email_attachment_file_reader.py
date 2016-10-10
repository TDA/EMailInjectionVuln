from utils import *

__author__ = 'saipc'

if __name__ == '__main__':
    json_data = load_json_file('Data/email-attachment-data.json')
    print(get_size_json(json_data))