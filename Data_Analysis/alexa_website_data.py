__author__ = 'saipc'

if __name__ == '__main__':
  with open('domains_list', 'r') as domains_file:
    for domain in domains_file:
      print(domain.strip())
