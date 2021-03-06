from urlparse import urlparse

__author__ = 'saipc'

# from functions import *

def total_unique_domains(form_name, field):
    db = getopenconnection()
    cursor = db.cursor()

    search_query = generate_search_query(form_name, '`' + field + '`')
    # print(search_query)
    cursor.execute(search_query)
    form_url_rows = cursor.fetchall()
    return get_domains_from_list(form_url_rows)

def get_domains_from_list(url_list):
    domains = set()
    for row in url_list:
        scheme, netloc, path, params, query, fragment = urlparse(row, scheme='')
        domains.add(netloc)
    # print(domains)
    print(len(domains))
    return domains

def total_unique_ips(form_name, field):
    db = getopenconnection()
    cursor = db.cursor()

    search_query = generate_search_query(form_name, '`' + field + '`')
    # print(search_query)
    cursor.execute(search_query)
    form_url_rows = cursor.fetchall()
    ips = set()
    for row in form_url_rows:
        ips.add(row[0])
    # print(ips)
    print(len(ips))
    return ips

if __name__ == '__main__':
    # total_unique_domains('form', 'url') # 1085365
    total_unique_ips('successful_attack_emails', 'ip_addr') # 604
    # total_unique_domains('fuzzed_forms', 'url_fuzzed') # 198,306
