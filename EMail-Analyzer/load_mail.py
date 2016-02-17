__author__ = 'saipc'
import os

mail_folder = '/var/mail'
os.chdir(mail_folder)

# the mails in maluser are direct proof of the
files = ['normaluser', 'maluser']
NO_INJECTION_FILE = 'reguser'

normal_mails = []
injected_mails = []

for f in files:
    # read each and load into memory
    with open(f, 'r') as file_handle:
        mail_data = file_handle.read()

