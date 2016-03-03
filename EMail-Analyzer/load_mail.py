import ast
import re

__author__ = 'saipc'
import os

from mail_reader import *
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
    #print(m["to"], m["x-original-to"])
    matches = re.match(user_regex, m["x-original-to"])
    payload = matches.group(0)
    form_id = matches.group(1)
    print("Form id: ", form_id, payload)
    body_content = get_body_content(m) # the body of the message
    header_values = m.values() # all the header content

    # get the input data we sent for this request
    search_query = generate_multi_search_query('fuzzed_forms', 'input_data', [('form_id', form_id), ('payload_for_fuzzing', payload)])
    # print(search_query)
    db = getopenconnection()
    cursor = db.cursor()
    cursor.execute(search_query)
    form_input_data_row = cursor.fetchone()
    fields_to_fuzz = []
    # print(form_input_data_row)
    # now compare what we sent, to what we received, which of
    # the inputs we sent were in the actual email? if we find,
    # lets say, the name and the email in the received email,
    # then we should prolly try fuzzing both of those :D
    if form_input_data_row:
        form_input_data_row = ast.literal_eval(form_input_data_row[0])
        for k in form_input_data_row.keys():
            value = form_input_data_row.get(k)
            if (value in body_content or value in header_values):
                print("Value found", value)
                fields_to_fuzz.append(k)
            else:
                print("Value not found", value)
    print("These are the fields to fuzz", fields_to_fuzz)
    # now we call the malicious payload fuzzer :D

    # keys = m.keys()
    # for k in keys:
    #     print("Key: ", k, "Value: ", m.get(k))

