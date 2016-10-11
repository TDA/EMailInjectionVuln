import virustotal
import os
import sys
import time
import datetime
import json

SECONDS_BETWEEN_REQUESTS = 15.5

RESULTS_FILE = 'vt_results.json'

def load_results():
    to_return = {}
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'rb') as f:
            to_return = json.load(f)
    return to_return

def save_results(results):
    with open(RESULTS_FILE, 'wb') as f:
        f.write(json.dumps(results, ensure_ascii=False))

def main(directory):
    v = virustotal.VirusTotal('2309e69bc73268e3d124e2168c639033a818ff05d36f8593c52b811ebb6ea1fe')

    results = load_results()
    num = 0
    for i in os.listdir(directory):
        num += 1
        filename = directory + '/' + i
        # If we already have results for this, skip it
        if i in results:
            print "skipping", i
            continue
        print "scanning", i
        report = v.scan(filename)
        if 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' in report.scan_id:
            print "EMPTY WTF!"
            import pdb
            pdb.set_trace()
        if not report.done:
            report.join()
        print report.permalink
        to_save = {'id' : report.id,
                   'scan_id': report.scan_id,
                   'permalink': report.permalink,
                   'status': report.status,
                   'total': report.total,
                   'positives': report.positives,
                   'avs': []}

        num_malware = 0
        for av, malware in report:
            to_save['avs'].append({'name': av[0], 'version': av[1], 'update': av[2], 'malware': malware})
            if malware:
                num_malware += 1

        print "num_malware", num_malware

        results[i] = to_save
        if num % 10 == 0:
            save_results(results)
                

        


if __name__ == '__main__':
    main('attachments')
