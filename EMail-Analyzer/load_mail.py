import re

__author__ = 'saipc'
import os

from mail_reader import read_mails
from functions import *

# the mails in maluser are direct proof of the attack
files = ['normaluser', 'maluser']
# but the mails in normaluser could contain the x-check
# header, if they do, then that is a successful attack
# as well. This is due to pythons way of attaching
# headers, instead of overwriting, it ignores duplicate
# headers, so we need to inject a new one.
NO_INJECTION_FILE = 'reguser'

normal_mails = []
injected_mails = []

# for f in files:
#     # read each and load into memory
#     if (os._exists(f)):
#         with open(f, 'r') as file_handle:
#             mail_data = file_handle.read()

# helper functions
def check_total_mails(filename):
    messages = read_mails(filename)
    return len(messages)

def is_header_present(message, header):
    return message.contains(header)

messages = read_mails(os.path.join('~', NO_INJECTION_FILE))

# lets make these non-capturing, so we can directly
# get the form_id, and the entire string alone :D double kill!!
user_regex = re.compile("(?:(?:reg)|(?:mal)|n)user(\d+)@wackopicko\.com")

for m in messages:
    print(m["to"], m["x-original-to"])
    matches = re.match(user_regex, m["x-original-to"])
    print("Form id: ", matches.group(1), matches.group(0))
    payload = matches.group(0)
    form_id = matches.group(1)
    #TODO: write a SQL query to fetch the right row
    search_query = generate_multi_search_query('fuzzed_forms', 'input_data', [('form_id', form_id), ('payload', payload)])
    print(search_query)


    # keys = m.keys()
    # for k in keys:
    #     print("Key: ", k, "Value: ", m.get(k))

