__author__ = 'saipc'

import dns.resolver
from functions import *

bls = ["zen.spamhaus.org", "spam.abuse.ch", "cbl.abuseat.org", "virbl.dnsbl.bit.nl", "dnsbl.inps.de",
    "ix.dnsbl.manitu.net", "dnsbl.sorbs.net", "bl.spamcannibal.org", "bl.spamcop.net", "dnsbl-1.uceprotect.net", "dnsbl-2.uceprotect.net",
    "dnsbl-3.uceprotect.net", "db.wpbl.info"]

db = getopenconnection()
query = "SELECT `id`, `ip_addr` FROM `successful_attack_emails` GROUP BY(`ip_addr`) ORDER BY id"
cursor = db.cursor()
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    myIP = row[1]
    for bl in bls:
        try:
            my_resolver = dns.resolver.Resolver()
            query = '.'.join(reversed(str(myIP).split("."))) + "." + bl
            answers = my_resolver.query(query, "A")
            answer_txt = my_resolver.query(query, "TXT")
            print 'IP: %s IS listed in %s (%s: %s)' %(myIP, bl, answers[0], answer_txt[0])
        except dns.resolver.NXDOMAIN:
            print 'IP: %s is NOT listed in %s' %(myIP, bl)
        except Exception as e:
            print("Some random issue", myIP, bl, e, "continuing")
            continue
    print(myIP, " is DONE")