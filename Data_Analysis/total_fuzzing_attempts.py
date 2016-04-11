__author__ = 'saipc'

from functions import *
db = getopenconnection()
cursor = db.cursor()

q1 = "SELECT COUNT(DISTINCT form_id) FROM `fuzzed_forms` WHERE `payload_for_fuzzing` LIKE '%nuser%'"
cursor.execute(q1)
fuzzed_form_ids = cursor.fetchone()[0]

q2 = "SELECT COUNT(DISTINCT form_id) FROM `fuzzed_forms` WHERE `payload_for_fuzzing` LIKE '%reguser%'"
cursor.execute(q2)
form_ids = cursor.fetchone()[0]

print("Fuzzed with normal", form_ids)
print("Fuzzed with mal", fuzzed_form_ids)

# ('Fuzzed with normal', 756588L)
# ('Fuzzed with mal', 38989L)