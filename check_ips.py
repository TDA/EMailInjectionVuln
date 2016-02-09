__author__ = 'saipc'

import requests

for i in range(0, 61):
    ip = "http://129.219.234." + str(194 + i)
    r = requests.get(ip)
    if (r.status_code != 200):
        print(ip + " is not reachable")
        break
    else:
        print(ip + " is reachable")