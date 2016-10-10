from utils import *

__author__ = 'saipc'

def find_positives(json_data):
    positive_hits = {}
    for entry_key in json_data.keys():
        print("Searching key", entry_key)
        if (json_data[entry_key]["positives"]) > 0:
            print("Found a positive", entry_key)
            positive_hits[entry_key] = json_data[entry_key]
    return positive_hits

if __name__ == '__main__':
    json_data = load_json_file('Data/vt_results.json')
    positives = find_positives(json_data)
    print("Positives found: ", len(positives)) # 265 unique entries
    save_json_file('Data/virus_positives.json', positives)