__author__ = 'saipc'

from functions import *

def form_counts(form_name):
    query = "SELECT COUNT(*) FROM %s"%(form_name)
    db = getopenconnection()
    cursor = db.cursor()
    cursor.execute(query)
    count = cursor.fetchone()[0]
    print(form_name, count)
    return count

if __name__ == '__main__':
    form_counts('form')
    form_counts('email_forms')
    form_counts('received_emails')
