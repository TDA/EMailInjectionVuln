import mailbox
import base64
import os
import sys
import email
import hashlib
import json

BLACKLIST = ('signature.asc', 'message-footer.txt', 'smime.p7s')
VERBOSE = 1

RESULT_FILE = "email-attachment-data.json"


def return_attachments(payload):
    to_return = []

    global attachments
    filename = payload.get_filename()

    if filename is not None:
	print "\nAttachment found!"
        print filename
	if filename.find('=?') != -1:
	    ll = email.header.decode_header(filename)
	    filename = ""
	    for l in ll:
		filename = filename + l[0]
			
	if filename in BLACKLIST:
	    if (VERBOSE >= 1):
		print "Skipping %s (blacklist)\n" %filename
		return

	content = payload.get_payload(decode=True)
        to_return.append({'filename': filename, 'content': content})

    else:
	if payload.is_multipart():
	    for payl in payload.get_payload():
		to_return = return_attachments(payl)
    return to_return


def load_results():
    to_return = {}
    if os.path.exists(RESULT_FILE):
        with open(RESULT_FILE, 'rb') as f:
            try:
                to_return = json.load(f)
            except:
                pass
    return to_return

def save_results(emails):
    with open(RESULT_FILE, 'wb') as f:
        f.write(json.dumps(emails))


def convert_to_unicode(s):
    if isinstance(s, str):
        return s.decode('utf-8', 'ignore')
    elif isinstance(s, unicode):
        return s
    else:
        raise Exception()

def main(filename, attachment_dir):
    emails = load_results()
    num = 0
    with open(filename, 'rb') as fp:
        mb = mailbox.PortableUnixMailbox(fp, factory = email.message_from_file)
        if not os.path.exists(attachment_dir):
            os.mkdir(attachment_dir)
        for message in mb:
            num += 1

            if num-1 in emails:
                if num % 1000 == 0:
                    print "skipping", num 
                continue
            attachments = return_attachments(message)
            # We only want to store those emails that have attachments
            if attachments:
                saved_attachments = []
                for a in attachments:
                    content_hash = hashlib.sha256(a['content']).hexdigest()
                    new_location = attachment_dir + '/' + content_hash
                    if not os.path.exists(new_location):
                        with open(new_location, 'wb') as f:
                            f.write(a['content'])
                    saved_attachments.append({'filename': convert_to_unicode(a['filename']), 'hash': content_hash})

                if message['date']:
                    date = convert_to_unicode(message['date'])
                else:
                    date = None
                subject = convert_to_unicode(message['subject'])
                froms = map(convert_to_unicode,  message.get_all('from', 'ignore'))
                tos = map(convert_to_unicode, message.get_all('to', 'ignore'))
                
                emails[num-1] = {'attachments': saved_attachments, 'date': date, 'subject': subject, 'froms': froms, 'tos': tos}
            if num % 1000 == 0:
                print num
                save_results(emails)
    print num


if __name__ == '__main__':
    main("reguser", 'attachments')
