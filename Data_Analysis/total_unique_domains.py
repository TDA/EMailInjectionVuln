from urlparse import urlparse

__author__ = 'saipc'

from functions import *

def total_unique_domains(form_name):
    db = getopenconnection()
    cursor = db.cursor()

    search_query = generate_search_query(form_name, '`url`')
    # print(search_query)
    cursor.execute(search_query)
    form_input_data_row = cursor.fetchall()
    domains = set()
    for row in form_input_data_row:
        scheme, netloc, path, params, query, fragment = urlparse(row[0], scheme='')
        domains.add(netloc)

    # print(domains)
    print(len(domains))


if __name__ == '__main__':
    total_unique_domains('form')