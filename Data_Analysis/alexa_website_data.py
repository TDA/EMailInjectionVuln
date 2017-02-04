__author__ = 'saipc'

if __name__ == '__main__':
  with open('domains400', 'r') as file:
    domains = file.readlines()
    for domain in domains:
      print(domain)
