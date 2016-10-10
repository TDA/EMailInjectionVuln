__author__ = 'saipc'

from utils import *

if __name__ == '__main__':
    virus_data = load_json_file('Data/virus_positives.json')
    email_data = load_json_file('Data/email-attachment-data.json')
    #  generator to figure out which ones are common and print them
    virus_to_email_data = {key : email_data[key] for key in email_data.keys() if email_data[key]["attachments"][0]["hash"] in virus_data.keys() }
    print(virus_to_email_data) # 443 non-unique entries
    save_json_file('Data/email_virus_attachments.json', virus_to_email_data)