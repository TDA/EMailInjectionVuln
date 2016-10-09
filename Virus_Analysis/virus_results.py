from utils import *

__author__ = 'saipc'

def find_positives(jsonData):
    positive_hits = []
    for entry_key in jsonData.keys():
        print("Searching key", entry_key)
        if (jsonData[entry_key]["positives"]) > 0:
            print("Found a positive", entry_key)
            positive_hits.append(jsonData[entry_key])
    return positive_hits

if __name__ == '__main__':
    json_data = load_json_file('Data/vt_results.json')
    positives = find_positives(json_data)