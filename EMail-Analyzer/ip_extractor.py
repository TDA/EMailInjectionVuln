import os
import re
from mail_reader import *
from email_functions import *

__author__ = 'saipc'

def extract_ips(filename):
    ip_regex = re.compile("(((\d{0,3})\.){3}\d{0,3})")
    db = getopenconnection()
    cursor = db.cursor()
    messages = read_mails(os.path.join('~', filename))
    for m in messages:
        received = m["received"]

        if (re.search(ip_regex, str(received))):
            print("Found match")
            # print(received)
            # cuz middle of the string, use search
            # instead of match
            ip = re.search(ip_regex, str(received)).group(0)
            print(ip)
            update_query = "UPDATE `successful_attack_emails` SET `ip_addr` = '%s' where `recipient_email` = '%s'"%(ip, m["x-original-to"])
            print(update_query)
            cursor.execute(update_query)
    db.commit()
    db.close()


if __name__ == "__main__":
    extract_ips('normaluser2')
    pass