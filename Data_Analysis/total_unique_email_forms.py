from urlparse import urlparse

__author__ = 'saipc'

from functions import *

def total_unique_email_forms(form_name, field):
    db = getopenconnection()
    cursor = db.cursor()

    search_query = generate_search_query(form_name, '`' + field + '`')
    # print(search_query)
    cursor.execute(search_query)
    form_ids = cursor.fetchall()
    domains = set()
    for form_id in form_ids:
        # print(form_id)
        search_query = generate_search_query('form', '`url`', 'id', form_id[0])
        cursor.execute(search_query)
        url = cursor.fetchone()
        if (url != None):
            scheme, netloc, path, params, query, fragment = urlparse(url[0], scheme='')
            domains.add(netloc)
    print(len(domains))



if __name__ == '__main__':
    # total_unique_email_forms('email_forms', 'form_id') # 113,663
    # total_unique_email_forms('received_emails', 'form_id') # 11,916
    total_unique_email_forms('successful_attack_emails', 'form_id') # 114