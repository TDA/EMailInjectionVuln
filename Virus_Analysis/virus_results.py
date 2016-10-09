from utils import *

__author__ = 'saipc'

if __name__ == '__main__':
    jsonData = load_json_file('Data/vt_results.json')
    print(get_size_json(jsonData))