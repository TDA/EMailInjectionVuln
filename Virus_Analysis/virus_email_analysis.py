__author__ = 'saipc'

from utils import *
import re

if __name__ == '__main__':
    email_virus_attachments = load_json_file('Data/email_virus_attachments.json')
    set_hashes = set()
    email_form_ids = set()
    for key in email_virus_attachments.keys():
        set_hashes.add(email_virus_attachments[key]["attachments"][0]["hash"])
        email_form_ids.add(email_virus_attachments[key]["tos"][0])
    print(len(set_hashes))
    print(len(email_form_ids))
    print(email_form_ids)

    form_ids = set()
    for id in email_form_ids:
        matches = re.match('.*(\d{7,}).*', str(id))
        # print(matches)
        if matches:
            id_number = matches.group(1)
            form_ids.add(id_number)
    print(len(form_ids))
    for id in form_ids:
        print("`form_id`=" + id)
    # 265 unique virus attachments
    # gather the unique email form ids


