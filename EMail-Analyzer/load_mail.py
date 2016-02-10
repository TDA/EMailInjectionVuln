__author__ = 'saipc'
import os

mail_folder = '/var/mail'
os.chdir(mail_folder)

files = ['normaluser', 'maluser']
normal_mails = []
injected_mails = []

for f in files:
    # read each and load into memory
    with open(f, 'r') as file_handle:
        mail_data = file_handle.read()

