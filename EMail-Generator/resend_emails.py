__author__ = 'saipc'
import whois
import subprocess
from email_gen import send_email
import MySQLdb

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

def getopenconnection():
    return MySQLdb.connect('127.0.0.1', 'root', '', 'ejection')

if __name__ == '__main__':
    domains = populate_domains("failed_emails")
    mailed_domains = 0
    need_to_mail = 0
    db = getopenconnection()
    cursor = db.cursor()
    for domain in domains:
        try:
            whois_info = whois.whois(domain)
            #print(domain)
            if "emails" in whois_info and (whois_info["emails"] != None):
                emails = whois_info["emails"]
                if (isinstance(emails, basestring)):
                    emails = [emails]
                    print("NEED TO MAIL", emails)
                    need_to_mail += 1
                print(domain, emails)
                mailed_domains += 1
                mail_content, subject = reconstruct_emails(domain, emails)
                for email in emails:
                    if ("abuse" in email):
                        print("Skipping this email", email)
                        continue
                    #send_email(email, subject, mail_content)
                    query = "SELECT `contact_email` from `emailed_websites` WHERE website LIKE '%s'"%(domain)
                    cursor.execute(query)
                    val = cursor.fetchone()[0]
                    val = email if (val == '') else (val + ',' + email)
                    print(val)
                    update_query = "UPDATE `emailed_websites` SET `contact_email` = '%s' WHERE website LIKE '%s'"%(val, domain)
                    print(update_query)
                    cursor.execute(update_query)
                    db.commit()
        except Exception as e:
            print("Skipping " + domain + " cuz " + str(e))
    db.close()
    print(mailed_domains)
    print(need_to_mail)