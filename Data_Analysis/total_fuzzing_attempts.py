__author__ = 'saipc'

from functions import *
db = getopenconnection()
cursor = db.cursor()

q1 = "SELECT DISTINCT form_id FROM `fuzzed_forms` WHERE `payload_for_fuzzing` LIKE '%nuser%'"
cursor.execute(q1)
fuzzed_form_ids = cursor.fetchall()

q2 = "SELECT DISTINCT form_id FROM `fuzzed_forms` WHERE `payload_for_fuzzing` LIKE '%reguser%'"
cursor.execute(q2)
form_ids = cursor.fetchall()

print("Fuzzed with normal", len(form_ids))
print("Fuzzed with mal", len(fuzzed_form_ids))