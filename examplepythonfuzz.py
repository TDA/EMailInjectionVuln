__author__ = 'saipc'

from email.parser import FeedParser

to = input()
#print to
msg = """To: """ + to + """\n
        From: <user@example.com>\n
        Subject: Test message\n
        \n
        Body would go here\n"""

#print msg
f = FeedParser()
f.feed(msg)
headers = FeedParser.close(f)

#  Now the header items can be accessed as a dictionary:
# attack string => 'sai@sai.com\nBCC:spc@spc.com\nbcc:saipc@saipc.com'
# Parser().parsestr checks for the BCC/bcc field, and
# only takes in the FIRST found field
# this behavior is opposite to that of
# the PHP mail() function :O
print 'To: %s' % headers['to']
print 'From: %s' % headers['from']
print 'Subject: %s' % headers['subject']
print 'BCC: %s' % headers['bcc']