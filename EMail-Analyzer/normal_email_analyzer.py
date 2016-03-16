from __future__ import absolute_import
import ast
import re

__author__ = 'saipc'
import os

from mail_reader import *
from email_functions import *
import sys


# the mails in maluser are direct proof of the attack
files = ['normaluser', 'maluser2']
# but the mails in normaluser could contain the x-check
# header, if they do, then that is a successful attack
# as well. This is due to pythons way of attaching
# headers, instead of overwriting, it ignores duplicate
# headers, so we need to inject a new one.
normal_mails = []
injected_mails = []

# helper functions
def check_total_mails(filename):
    messages = read_mails(filename)
    return len(messages)

def is_header_present(message, header):
    return message.contains(header)

def email_reader():
    messages = read_mails(os.path.join('~', files[0]))

    # lets make these non-capturing, so we can directly
    # get the form_id, and the entire string alone :D double kill!!
    a = []
    b = set()
    repeats = set()
    for m in messages:
        try:
            user_regex = re.compile(".*(?:(?:reg)|(?:mal)|n)user(\d+)(.*)?@wackopicko\.com.*")
            #print(m["to"], m["x-original-to"])
            keys = m.keys()
            # print(keys)
            form_id = ''
            if (re.search(user_regex, m["x-original-to"])):
                matches = re.match(user_regex, m["x-original-to"])
                payload = matches.group(0)
                form_id = matches.group(1)

                if (int(form_id) > 123):
                    # print("Mail to: ",  m["x-original-to"], form_id)
                    db = getopenconnection()
                    cursor = db.cursor()

                    search_query = generate_multi_search_query('successful_attack_emails', 'form_id', [('form_id', form_id), ('x-check', 1)])
                    # print(search_query)
                    cursor.execute(search_query)
                    form_input_data_row = cursor.fetchone()
                    if form_input_data_row:
                        repeats.add(form_id)
                        print("Found", len(form_input_data_row))

                    for key in keys:
                        if str(key).__contains__('x-check') or str(key).__contains__('X-Check'):
                            print(key, m.get(key))
                            a.append(form_id)
                            b.add(form_id)

        except Exception as e:
            print("Prolly a duplicate thing", e)
            continue
    print(len(a))
    print(len(b))
    print(b)
    print(len(repeats))
    print(repeats)
    print(len(b.difference(repeats)))

if __name__ == "__main__":
    email_reader()
    pass