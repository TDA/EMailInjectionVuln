#!/usr/bin/env python
__author__ = 'saipc'

from functions import *
import time
import subprocess

def get_latest_id(form):
    query = "SELECT `id` FROM `%s` GROUP by id DESC LIMIT 1"%(form)
    db = getopenconnection()
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchone()
    # print(rows[0])
    return rows[0]

def construct_dump_query(form):
    id = get_latest_id(form)
    dump_query = "/opt/lampp/bin/mysqldump --user=root -p --host=localhost ejection %s --where='id>%s' > ~/%s_dump_%s.sql"%(form, id, form, time.strftime("%b_%d").lower())
    print(dump_query)
    # subprocess.call(dump_query, shell=True)

if __name__ == '__main__':
    construct_dump_query('form')
    construct_dump_query('email_forms')
    construct_dump_query('params')

