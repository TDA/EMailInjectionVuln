__author__ = 'saipc'

from total_unique_domains import get_domains_from_list

if __name__ == '__main__':
  with open('domains_list', 'r') as domains_file:
    domains = [domain.strip() for domain in domains_file]
    unique_domains = get_domains_from_list(domains)
    for domain in unique_domains:
      print(domain)
