__author__ = 'saipc'

import sys
import mailbox

def read_mails(filename):
    messages = []
    mbox = mailbox.mbox(filename)
    for message in mbox:
       messages.append(message)
    # returns instances of the mails,
    # they behave kinda like dictionaries
    return messages

def get_body_content(m):
    # thanks to http://stackoverflow.com/questions/26567843/reading-the-mail-content-of-an-mbox-file-using-python-mailbox
    if m.is_multipart():
        content = ''.join(part.get_payload(decode=True) for part in m.get_payload())
    else:
        content = m.get_payload(decode=True)
    return content


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: python Mailreader.py mailfilename'
        sys.exit(1)
    read_mails(sys.argv[1])