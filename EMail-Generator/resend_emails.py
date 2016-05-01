__author__ = 'saipc'
import whois

def populate_domains(fname):
    domains = set()
    with open(fname, 'r') as f:
        for line in f:
            domains.add(str(line).split(" --- ")[0])
    return domains

if __name__ == '__main__':
    domains = populate_domains("failed_emails")
    mailed_domains = 0
    for domain in domains:
        try:
            whois_info = whois.whois(domain)
            # print(whois_info)
            print(domain)
            if "emails" in whois_info and (whois_info["emails"] != None):
                emails = whois_info["emails"]
                mailed_domains += 1
        except Exception as e:
            print("Skipping " + domain)