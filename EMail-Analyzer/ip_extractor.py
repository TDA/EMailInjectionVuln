import os
import re
from mail_reader import *
from email_functions import *

__author__ = 'saipc'

def extract_ips(filename):
    ip_regex = re.compile("(((\d{0,3})\.){3}\d{0,3})")
    user_regex = re.compile(".*(?:(?:reg)|(?:mal)|n)user(\d+)(.*)?@wackopicko\.com.*")

    messages = read_mails(os.path.join('~', filename))
    for m in messages:
        received = m["received"]
        if (re.search(user_regex, m["x-original-to"])):
                matches = re.match(user_regex, m["x-original-to"])
                form_id = matches.group(1)

        if (re.search(ip_regex, str(received))):
            print("Found match")
            # print(received)
            # cuz middle of the string, use search
            # instead of match
            ip = re.search(ip_regex, str(received)).group(0)
            print(ip)


if __name__ == "__main__":
    extract_ips('maluser')
    pass