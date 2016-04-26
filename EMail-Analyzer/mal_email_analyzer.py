from __future__ import absolute_import
import ast
import re

__author__ = 'saipc'
import os

from mail_reader import *
from email_functions import *
import sys


# the mails in maluser are direct proof of the attack
files = ['normaluser', 'maluser4']
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
    messages = read_mails(os.path.join('~/maluser', files[1]))
    print(len(messages))

    # lets make these non-capturing, so we can directly
    # get the form_id, and the entire string alone :D double kill!!

    all = []
    unique = set()
    for m in messages:
        try:
            user_regex = re.compile(".*(?:(?:reg)|(?:mal)|n)user(\d+)(.*)?@wackopicko\.com.*")
            ip_regex = re.compile("(((\d{0,3})\.){3}\d{0,3})")
            received = m["received"]
            ip = ""
            if (re.search(ip_regex, str(received))):
                ip = re.search(ip_regex, str(received)).group(0)

            #print(m["to"], m["x-original-to"])
            keys = m.keys()
            to_injection = False
            x_check = False

            for key in keys:
                if str(key).__contains__('x-ch') or str(key).__contains__('X-Ch'):
                    x_check = True
            email = m["x-original-to"]
            # print(email)

            if (re.search(user_regex, m["x-original-to"])):

                matches = re.match(user_regex, m["x-original-to"])
                payload = matches.group(0)
                form_id = matches.group(1)

                # print("Mail to: ", email , form_id)
                all.append(form_id)
                unique.add(form_id)

                if ('bcc' in email):
                    to_injection = True
                    # print("FOUND bcc")

            # first check if the form has been seen
                db = getopenconnection()
                cursor = db.cursor()



                search_query = generate_multi_search_query('successful_attack_emails', 'form_id', [('form_id', form_id), ('recipient_email', email)])
                # print(search_query)
                cursor.execute(search_query)
                form_input_data_row = cursor.fetchall()


                # # cuz only the forms above 1446155 are multi payload
                if form_input_data_row:
                    # skip, already added
                    print("Skipping")
                    continue
                else:
                    # gotta insert
                    # if (int(form_id) < 1446155 and int(form_id) > 123):
                    #     # add the _2, _3 etc to the
                    #     if ('bcc' not in email):
                    #         updated_mail = str(email).split('@')[0] + '_' + str(len(form_input_data_row)) + '@' + str(email).split('@')[1]
                    #     else:
                    #         updated_mail = str(email).split('"@')[0] + '_' + str(len(form_input_data_row)) + '"@' + str(email).split('"@')[1]
                    #     email = updated_mail

                    insert_query = "INSERT INTO `successful_attack_emails`(`form_id`, `recipient_email`, `to_injection`, `x-check`, `ip_addr`) VALUES (%s, '%s', %s, %s, '%s')" % (form_id, email, to_injection, x_check, ip)
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