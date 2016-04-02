import MySQLdb
from urlparse import *

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
Hi,
I found a potential bug on your website, <%s>.

I'm a Masters student in computer security at Arizona State University, and I'm researching E-Mail Header Injection (more information here: http://wackopicko.com/) vulnerabilities. I created a tool to crawl and analyze E-Mail Header Injection vulnerabilities on the World Wide Web and it found this vulnerability in your website <%s> on the following URL(s): <%s>.

Quick E-Mail Header Injection vulnerability overview:
When an application uses user input to construct emails, and does not sanitize the user input, it can result in E-Mail Header Injection. An attacker can then exploit this vulnerability by using a payload like "user@example.com%0Abcc:maluser@example.com" to add additional headers (bcc header in this example) and potentially the contents of the email.

I would appreciate it if you could confirm our findings. I am happy to help reproduce the exploit input.

Thanks for your help, and feel free to email me with any questions!

- Sai Prashanth Chandramouli
"""
    filled_email_template = email_template%(domain, domain, urls)
    return filled_email_template

def gather_urls(form_id):
    # looks at the form_ids, and gathers all URLs that need to be added to the email
    pass

def send_email(to, msg):
    pass

if __name__ == '__main__':
    db = getopenconnection()
    cursor = db.cursor()
    query = "SELECT `form_id` FROM successful_attack_emails;"
    cursor.execute(query)
    ids = cursor.fetchall()
    domain_to_url_map = dict()
    for id in ids:
        retrieve_query = "SELECT url, absolute_action FROM form WHERE id = '%s';"%(id)
        cursor.execute(retrieve_query)
        tup = cursor.fetchone()
        url, sub_url = tup
        print(url, sub_url)
        domain = get_domain(url)

        # use a dict here :D

    #urls = gather_urls()