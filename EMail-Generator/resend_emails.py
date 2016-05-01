__author__ = 'saipc'
import whois
import subprocess

def populate_domains(fname):
    domains = set()
    with open(fname, 'r') as f:
        for line in f:
            domains.add(str(line).split(" --- ")[0])
    return domains

def reconstruct_emails(domain, emails):
    mail_content = subprocess.check_output("php ~/PhpstormProjects/E-Mail_Retrieval/email_gmail.php "+ domain, shell=True)
    mail_content = mail_content.replace("potentially", "completely alter")
    subject = "Potential bug on website - %s" % (domain)
    return mail_content, subject


if __name__ == '__main__':
    domains = populate_domains("failed_emails")
    mailed_domains = 0
    for domain in domains:
        try:
            whois_info = whois.whois(domain)
            print(domain)
            if "emails" in whois_info and (whois_info["emails"] != None):
                emails = whois_info["emails"]
                mailed_domains += 1
                mail_content, subject = reconstruct_emails(domain, emails)
                # TODO: finish up the emailing, and update DB with contact details

        except Exception as e:
            print("Skipping " + domain)