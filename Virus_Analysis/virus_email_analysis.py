__author__ = 'saipc'

from utils import *

if __name__ == '__main__':
    email_virus_attachments = load_json_file('Data/email_virus_attachments.json')
    set_hashes = set()
    for key in email_virus_attachments.keys():
        set_hashes.add(email_virus_attachments[key]["attachments"][0]["hash"])
    print(len(set_hashes))
    # 265 unique virus attachments
