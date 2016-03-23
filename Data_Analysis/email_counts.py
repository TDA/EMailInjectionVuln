__author__ = 'saipc'

from functions import *

def email_counts(form_name, field):
    db = getopenconnection()
    cursor = db.cursor()

    # EHI alone -- 180
    ehi_alone = "SELECT DISTINCT `form_id` FROM `successful_attack_emails` WHERE `recipient_email` NOT LIKE '%bcc%' AND `recipient_email` LIKE '%mal%' LIMIT 0, 1000"
    cursor.execute(ehi_alone)
    form_ids = cursor.fetchall()
    print("Ehi Alone", len(form_ids))

    # EHI and x-check -- 137
    ehi_and_x_check = "SELECT DISTINCT `form_id` FROM `successful_attack_emails` WHERE `recipient_email` NOT LIKE '%bcc%' AND `x-check` = 1 AND `recipient_email` LIKE '%mal%' LIMIT 0, 500"
    cursor.execute(ehi_and_x_check)
    form_ids = cursor.fetchall()
    print("Ehi and x check", len(form_ids))

    # To inj Alone - 83
    to_inj = "SELECT DISTINCT `form_id` FROM `successful_attack_emails` WHERE `to_injection` = 1"
    cursor.execute(to_inj)
    form_ids = cursor.fetchall()
    print("To inj Alone", len(form_ids))

    #To inj AND x-check -- 8
    to_inj_and_x_check = "SELECT DISTINCT `form_id` FROM `successful_attack_emails` WHERE `to_injection` = 1 AND `x-check` = 1 LIMIT 0, 1000"
    cursor.execute(to_inj_and_x_check)
    form_ids = cursor.fetchall()
    print("To inj AND x-check", len(form_ids))

    # x-check alone -- 153 (137 with mal, 16 with nuser)
    x_check = "SELECT DISTINCT `form_id` FROM `successful_attack_emails` WHERE `x-check` = 1"
    cursor.execute(x_check)
    form_ids = cursor.fetchall()
    print("x-check alone", len(form_ids))

    # x-check AND nuser -- 40 (16 unique ones apart from mal)
    x_check_nuser = "SELECT DISTINCT `form_id` FROM `successful_attack_emails` WHERE `x-check` = 1 AND (`recipient_email` LIKE '%nuser%')"
    cursor.execute(x_check_nuser)
    form_ids = cursor.fetchall()
    print("x-check AND nuser", len(form_ids))

if __name__ == '__main__':
    email_counts('successful_attack_emails', 'form_id')