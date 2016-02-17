__author__ = 'saipc'

import sys
import mailbox

def read_mails(filename):
    messages = []
    mbox = mailbox.mbox(filename)
    for message in mbox:
       messages.append(message)
    return messages

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: python Mailreader.py mailfilename'
        sys.exit(1)
    read_mails(sys.argv[1])