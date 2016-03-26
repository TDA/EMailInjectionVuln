from urlparse import urlparse

__author__ = 'saipc'

from functions import *

def total_unique_domains(form_name, field):
    db = getopenconnection()
    cursor = db.cursor()

    search_query = generate_search_query(form_name, '`' + field + '`')
    # print(search_query)
    cursor.execute(search_query)
    form_url_rows = cursor.fetchall()
    domains = set()
    for row in form_url_rows:
        scheme, netloc, path, params, query, fragment = urlparse(row[0], scheme='')
        domains.add(netloc)
    # print(domains)
    print(len(domains))
    return domains

if __name__ == '__main__':
    total_unique_domains('form', 'url')