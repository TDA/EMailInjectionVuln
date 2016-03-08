from __future__ import absolute_import
import ast
import re

__author__ = 'saipc'
import os

from mail_reader import *
from email_functions import *
import sys


# the mails in maluser are direct proof of the attack
files = ['normaluser', 'maluser']
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
    messages = read_mails(os.path.join('~', files[1]))

    # lets make these non-capturing, so we can directly
    # get the form_id, and the entire string alone :D double kill!!
    a = []
    b = set()
    for m in messages:
        try:
            user_regex = re.compile(".*(?:(?:reg)|(?:mal)|n)user(\d+)(.*)?@wackopicko\.com.*")
            #print(m["to"], m["x-original-to"])

            if (re.search(user_regex, m["x-original-to"])):
                matches = re.match(user_regex, m["x-original-to"])
                payload = matches.group(0)
                form_id = matches.group(1)
                print("Mail to: ",  m["x-original-to"], form_id)
                a.append(form_id)
                b.add(form_id)
                keys = m.keys()
                if ('bcc' in keys):
                    a.append(form_id)
                    print("FOUND bcc")

            # first check if the form has been seen
            # db = getopenconnection()
            # cursor = db.cursor()
            #
            # body_content = get_body_content(m) # the body of the message
            # header_values = m.values() # all the header content
            #
            # # get the input data we sent for this request
            # search_query = generate_multi_search_query('fuzzed_forms', 'input_data', [('form_id', form_id), ('payload_for_fuzzing', payload)])
            # # print(search_query)
            # cursor.execute(search_query)
            # form_input_data_row = cursor.fetchone()
            # fields_to_fuzz = []
            # # print(form_input_data_row)
            # # now compare what we sent, to what we received, which of
            # # the inputs we sent were in the actual email? if we find,
            # # lets say, the name and the email in the received email,
            # # then we should prolly try fuzzing both of those :D
            # if form_input_data_row:
            #     form_input_data_row = ast.literal_eval(form_input_data_row[0])
            #     for k in form_input_data_row.keys():
            #         value = form_input_data_row.get(k)
            #         # if (value in body_content or value in header_values):
            #         #     print("Value found", value)
            #         #     fields_to_fuzz.append(k)
            #         # else:
            #         #     print("Value not found", value)
            #
            #     # now we call the malicious payload fuzzer :D
            #     db.commit()
            #     db.close()
        except Exception as e:
            print("Prolly a duplicate thing", e)
            continue
        print(len(a))
        print(len(b))

if __name__ == "__main__":
    # print(check_total_mails("~/maluser"))
    email_reader()
    pass