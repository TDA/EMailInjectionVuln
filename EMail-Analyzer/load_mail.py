__author__ = 'saipc'
import os

mail_folder = '/var/mail'
os.chdir(mail_folder)

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

for f in files:
    # read each and load into memory
    with open(f, 'r') as file_handle:
        mail_data = file_handle.read()

