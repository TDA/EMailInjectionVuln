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
    all = []
    unique = set()
    for m in messages:
        try:
            user_regex = re.compile(".*(?:(?:reg)|(?:mal)|n)user(\d+)(.*)?@wackopicko\.com.*")
            #print(m["to"], m["x-original-to"])
            keys = m.keys()
            to_injection = False
            x_check = False

            for key in keys:
                if str(key).__contains__('x-ch') or str(key).__contains__('X-Ch'):
                    x_check = True
            email = m["x-original-to"]
            print(email)
            if (re.search(user_regex, m["x-original-to"])):
                matches = re.match(user_regex, m["x-original-to"])
                payload = matches.group(0)
                form_id = matches.group(1)

                # print("Mail to: ", email , form_id)
                all.append(form_id)
                unique.add(form_id)

                if ('bcc' in email):
                    to_injection = True
                    print("FOUND bcc")

            # first check if the form has been seen
                db = getopenconnection()
                cursor = db.cursor()



                search_query = generate_multi_search_query('successful_attack_emails', 'form_id', [('form_id', form_id), ('recipient_email', email)])
                print(search_query)
                cursor.execute(search_query)
                form_input_data_row = cursor.all()


                # # cuz only the forms above 1446155 are multi payload
                if form_input_data_row and (form_id >= 1446155):
                    # skip, already added
                    continue
                else:
                    # gotta insert
                    if (form_id < 1446155):
                        # add the _2, _3 etc to the
                        pass
                    insert_query = "INSERT INTO `successful_attack_emails`(`form_id`, `recipient_email`, `to_injection`, `x-check`) VALUES (%s, '%s', %s, %s)" % (form_id, email, to_injection, x_check)
                    print(insert_query)
                    cursor.execute(insert_query)

                db.commit()
                db.close()
        except Exception as e:
            print("Prolly a duplicate thing", e)
            continue
        # print unique

        print(len(all))
        print(len(unique))
    print(unique)

if __name__ == "__main__":
    # print(check_total_mails("~/maluser"))
    email_reader()
    pass