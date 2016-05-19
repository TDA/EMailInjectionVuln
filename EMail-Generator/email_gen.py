from email.mime.text import MIMEText
import smtplib
import MySQLdb
from urlparse import *
import time
import db as Data

import sys
# sys.path.insert(0, '')

# from Fuzzer.fuzzer import construct_url

__author__ = 'saipc'

def getopenconnection():
    return MySQLdb.connect('127.0.0.1', 'root', '', 'ejection')

def get_domain(url):
    return urlparse(url, scheme='')[1]

def generate_email(domain, urls = None):
    if domain == None or urls == None:
        return
    # generates an email template for the given forms
    email_template = """
Hi,<br>
I found a potential bug on your website, "%s".<br><br>

<p>I'm a Masters student in computer security at Arizona State University, and I'm
researching E-Mail Header Injection (more information here: http://wackopicko.com/) vulnerabilities.
I created a tool to crawl and analyze E-Mail Header Injection vulnerabilities on the World Wide Web
and it found this vulnerability in your website "%s" on the following URL(s): [%s].</p>

<h4>Quick E-Mail Header Injection vulnerability overview:</h4>
<p>When an application uses user input to construct emails, and does not sanitize the user input,
it can result in E-Mail Header Injection. An attacker can then exploit this vulnerability by using
a payload like "user@example.com%%0Abcc:maluser@example.com" to add additional headers (bcc header
in this example) and and to completely alter the content of the email.</p><br>

I would appreciate it if you could confirm our findings. I am happy to help reproduce the exploit input.
<br><br>
Thanks for your help, and feel free to email me with any questions!
<br><br>
- Sai Prashanth Chandramouli
"""
    filled_email_template = email_template % (domain, domain, ', '.join(urls))
    subject = "Potential bug on website - %s" % (domain)
    return filled_email_template, subject

def gather_urls(form_ids):
    # looks at the form_ids, and gathers all URLs that need to be added to the email
    domain_to_url_map = dict()
    for id in ids:
        retrieve_query = "SELECT url, absolute_action FROM form WHERE id = '%s';"%(id)
        cursor.execute(retrieve_query)
        tup = cursor.fetchone()
        url, sub_url = tup

        domain = remove_www(get_domain(url))

        # vuln_url = str(construct_url(sub_url, url))
        get_fuzzed_url_query = "SELECT url_fuzzed FROM fuzzed_forms WHERE form_id = '%s';"%(id)
        cursor.execute(get_fuzzed_url_query)
        tup = cursor.fetchone()
        if tup:
            vuln_url = tup[0]
            print(vuln_url)
            # use a dict here :D
            if not domain_to_url_map.has_key(domain):
                temp_set = set()
            else:
                temp_set = domain_to_url_map.get(domain)
            temp_set.add(vuln_url)
            domain_to_url_map[domain] = temp_set
    print(domain_to_url_map)
    return domain_to_url_map

def send_email(to, subject, email_msg):

    msg = MIMEText(email_msg, 'html')
    me = "saipc@asu.edu"
    # me == the sender's email address
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = to

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #socket = server._get_socket()
    #Next, log in to the server
    server.login("schand31@asu.edu", Data.password)
    server.sendmail(me, [to, me], msg.as_string())
    server.quit()


def remove_www(param):
    if (str(param).startswith('www.')):
        return str(param)[4:]
    else:
        return str(param)


if __name__ == '__main__':
    db = getopenconnection()
    cursor = db.cursor()
    query = "SELECT `form_id` FROM successful_attack_emails LIMIT 1479, 581;"
    cursor.execute(query)
    ids = cursor.fetchall()
    domain_to_url_map = gather_urls(ids)

    for domain in domain_to_url_map.keys():
        dup_check_query = "SELECT `website` FROM emailed_websites WHERE `website` = '%s' ;" % (domain)
        print(dup_check_query)
        cursor.execute(dup_check_query)
        is_exists = cursor.fetchone()
        if (is_exists):
            print("Already emailed, continuing")
            continue

        filled_email_template, subject = generate_email(domain, domain_to_url_map[domain])
        # print(filled_email_template)
        sec_to = "security@" + domain
        web_to = "webmaster@" + domain
        adm_to = "admin@" + domain
        print(sec_to, web_to, adm_to)
        time.sleep(10)
        send_email(sec_to, subject, filled_email_template)
        time.sleep(15)
        send_email(web_to, subject, filled_email_template)
        time.sleep(15)
        send_email(adm_to, subject, filled_email_template)
        ins_query = "INSERT INTO emailed_websites (website, urls)  VALUES ('%s', '%s');" % (domain, ', '.join(domain_to_url_map[domain]))
        cursor.execute(ins_query)
        print(ins_query)
    db.commit()
    db.close()

    #urls = gather_urls()