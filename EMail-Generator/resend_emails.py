__author__ = 'saipc'

def populate_domains(fname):
    domains = set()
    with open(fname, 'r') as f:
        for line in f:
            domains.add(str(line).split(" --- ")[0])
    print(domains)
    print(len(domains))

if __name__ == '__main__':
    populate_domains("failed_emails")