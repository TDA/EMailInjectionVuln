from __future__ import absolute_import
import json
import random
from CeleryFuzzer import app

__author__ = 'saipc'
from celery import Celery

import requests
from urlparse import *
from functions import *
# from time import sleep
# for tests in python3
# from urllib.parse import *
# from Fuzzer.functions import *

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

def construct_url(action, main_url):
    # only do the following IFF the action is relative, and NOT absolute
    # (ie) if /submit.php and NOT http://xyz.com/submit.php, since in the latter
    # case, we can simply submit

    # initially we can directly get/post a request
    # to the url, so set url to action
    url = action
    if not str(action).startswith('http'):
        # if action is empty, it means we submit to same page
        if action == "#" or action == '' or action == '/':
            url = main_url
        else:
            # parse the url
            if (str(action).startswith('/')):
                # if the action starts
                # with '/', remove actions '/'
                # this is best effort, cant really know
                # whether this is right or wrong, on a case by case basis
                # this will be right for MOST things tho, so.
                action = action[1:]
            scheme, netloc, path, params, query, fragment = urlparse(main_url, scheme='')

            # replace the paths last item alone with 'action'
            # this is for urls like: main_url = 'https://loc.com/sai/pc/ssspcs.php'
            # the form url might be like above, so we need to submit it right to
            # https://loc.com/sai/pc/submit.php, could there be an easier way??
            path_vars = str(path).split('/')
            path_vars[len(path_vars) - 1] = action
            path = '/'.join(path_vars)

            url = urlunparse((scheme, netloc, path, params, query, fragment))
    # print("FINAL URL:", url)
    return url

@app.task(name='Fuzzer.fuzzer')
def fuzzer(reconstructed_form, form_id, payload, fields_to_fuzz):
    # a function which takes in a payload and fuzzes that into
    # every field. Changes after talking to Adam as
    # of Feb 19, 2016.
    try:
        # lets print out everything we have so we know what all we have :O
        # print(reconstructed_form, form_id)
        main_url, attributes, method, action, input_list = reconstructed_form
        # print("Main URL:", main_url)
        # print("Attributes:", attributes)
        # print("Method:", method)
        # print("Action:", action)
        # print("Input list:", input_list)

        url = construct_url(action, main_url)

        ## THIS IS PURELY FOR BLACKLISTING
        unparsed_url = urlparse(url, scheme='')
        netloc = unparsed_url[1]
        # print(netloc)

        db = getopenconnection()
        cursor = db.cursor()
        search_query = "Select * from `blacklisted_urls` where `blacklist_url` like  '%s' " % (str('%' + netloc + '%'))
        cursor.execute(search_query)
        print(search_query)
        rows = cursor.fetchall()
        if (rows and len(rows) > 0):
            # blacklisted, dont fuzz
            # print("blacklisted, dont fuzz")
            return("blacklisted, dont fuzz")
        else:
            print("Not blacklisted, proceed")

        # get the individual attrs and inputs
        # from the form, and make sure that the fuzzing is only
        # done on the email fields, also, set the GET/POST right
        # and check with localmail first before whambamming

        # now reconstruct the form
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        form_data_dict = {
            # this complex looking iterator is like this:
            # it chooses 10 random letters from the alphabets
            # string using a generator syntax, then joins the list
            # created into a single string
            "text": ''.join([random.choice(alphabets) for x in range(0, 10)]),
            "year": "1993", # these are for edge cases, might remove them
            "month": "07",
            "day": "03",
            "date": "03/07/1993",
            # this complex looking iterator is like this:
            # it chooses 5 random letters from the alphabets
            # followed by 2 uppercase letters, 2 numbers, and
            # 2 special characters, mainly to get through weak
            # password checks
            "password": ''.join([random.choice(alphabets) for x in range(0, 5)]) +
                        ''.join([random.choice(alphabets) for x in range(0, 2)]).upper() +
                        str(12) + "!#",
            "name": payload.split('@')[0], # set it to the username part
            # of the payload for easy identification
            "submit": "submit"
        }


        # instead of fuzzing the email field alone,
        # check whether the other fields need to be fuzzed
        if (fields_to_fuzz != None and len(fields_to_fuzz) >= 1):
            # need to fuzz the specified fields as well,
            # so update the dictionary with the values
            for field in fields_to_fuzz:
                form_data_dict[field] = payload

        # print(form_data_dict)
        data = {}
        # print("Data dict ", form_data_dict)
        for a_input in input_list:
            if (check_input(a_input, r"email|e-mail")):
                # this is the field to be fuzzed
                # print("Found an email field", a_input["name"])
                # enter the fuzzing data here
                # also add to the data list/tuple
                data[str(a_input["name"])] = payload
                # need to add the payload to the field here --> DONE
            else:
                # if the dict has the field, just use it, else check for other stuff
                # this is for the second round of fuzzing :D
                if (form_data_dict.has_key(a_input.get('name'))):
                    data[str(a_input["name"])] = form_data_dict[a_input["name"]]
                    continue
                # this is a normal field, just enter
                # valid, but irrelevant data
                # if name, password, or date, OR submit!!!
                #  directly fill from the dict
                if (check_input(a_input, r"date")):
                    data[str(a_input["name"])] = form_data_dict["date"]
                    continue
                if (check_input(a_input, r"password")):
                    data[str(a_input["name"])] = form_data_dict["password"]
                    continue
                if (check_input(a_input, r"name|username")):
                    data[str(a_input["name"])] = form_data_dict["name"]
                    continue
                if (check_input(a_input, r"submit")):
                    if a_input["name"] == '':
                        a_input["name"] = 'submit'
                    data[str(a_input["name"])] = a_input.get('value') or form_data_dict["submit"]
                    continue
                # this is the default case where the field is a text field,
                # only reached if its none of the above
                if (check_input(a_input, r"text")):
                    data[str(a_input["name"])] = form_data_dict["text"]
                    continue

                # add hidden fields if present
                if (check_input(a_input, r"hidden")):
                    data[str(a_input["name"])] = a_input.get('value')
                    continue

        # print("HERES THE DATA", data)
        # print("HERES THE DATA", data_2)
        # print("HERES THE DATA", data_3)


        method = str(method).lower()
        headers = {'content-type': 'application/x-www-form-urlencoded',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0'}
        # Since we are using requests (yay!), we don't have
        # to construct the url as per get or post, just call
        # r.get or r.post and it'll take care of it
        if method == 'get' or method == '':
            # make a get request with requests,
            # and pass the payload as params
            r = requests.get(url, params = data, headers = headers, timeout=2.5)
        elif method == 'post':
            # make a post request with requests,
            # and pass the payload as data
            # req = requests.Request('POST', url, headers=headers,data=data)
            # prepared = req.prepare()
            # pretty_print_POST(prepared)
            r = requests.post(url, data = data, headers = headers, timeout=2.5)
        else:
            # we dont have to do this, we handle only gets
            # or posts, no need to complicate by handling put etc
            return

        # UPDATE DB after fuzzing!!!!

        # print("INSERT INTO `fuzzed_forms`(`form_id`, `url_fuzzed`, `payload_for_fuzzing`) VALUES (%s, '%s', '%s')" % (form_id, db.escape_string(url), db.escape_string(payload)))
        cursor.execute("INSERT INTO `fuzzed_forms`(`form_id`, `url_fuzzed`, `payload_for_fuzzing`, `input_data`) VALUES (%s, '%s', '%s', '%s')" % (form_id, db.escape_string(url), db.escape_string(payload), db.escape_string(json.dumps(data))))
        db.commit()
        db.close()
        # print(r.status_code)
        # print(r.text)
        # this is only for testing that the data is right,
        # we do not do anything with the data
        print("HERES THE DATA afterwards", data, form_data_dict['name'])
        return data

    except Exception as e:
        print("Definitely a requests issue, well, hopefully. We are in %s" % (__name__))
        print(e)
        with open('log_fuzzer', 'a') as file_handle:
            file_handle.write(str(e) + '\n' + "We are in %s" % (__name__) + '\n')


@app.task(name='Fuzzer.call_fuzzer_with_payload')
def call_fuzzer_with_payload(reconstructed_form, form_id):

    # nuser123%0abcc%3amaluser123@wackopicko.com
    # nuser123@wackopicko.com%0abcc%3amaluser123@wackopicko.com
    # nuser123@wackopicko.com%0abcc:maluser123@wackopicko.com
    # user_id = random.randint(0, 100000)
    payload = 'reguser' + str(form_id) + '@wackopicko.com'
    fields_to_fuzz = []
    fuzzer.delay(reconstructed_form, form_id, payload, fields_to_fuzz)
    pass


@app.task(name='Fuzzer.call_fuzzer_with_malicious_payload')
def call_fuzzer_with_malicious_payload(form_id, fields_to_fuzz):
    print("RECEIVED ", form_id, fields_to_fuzz)
    form_id = str(form_id)
    # retrieve that form
    FORM_TABLE_NAME = 'form'
    db = getopenconnection()
    cursor = db.cursor()
    # we get the form again
    search_query = generate_search_query(FORM_TABLE_NAME, 'url, attributes, method, absolute_action, params', 'id', str(form_id))
    cursor.execute(search_query)
    row = cursor.fetchone()

    # set the payloads
    payloads = [
                'nuser' + form_id + '_1@wackopicko.com\r\nbcc:maluser' + form_id + '_1@wackopicko.com\r\nx-check:in',
                'nuser' + form_id + '_2@wackopicko.com\nbcc:maluser' + form_id + '_2@wackopicko.com\nx-check:in',
                'nuser' + form_id + '_3@wackopicko.com\nbcc:maluser' + form_id + '_3@wackopicko.com',
                'nuser' + form_id + '_4@wackopicko.com\r\nbcc:maluser' + form_id + '_4@wackopicko.com'
                ]
    # get the reconstructed form
    reconstructed_form = reconstruct_form(cursor, row)
    # print(reconstructed_form, form_id, payloads, fields_to_fuzz)
    for payload in payloads:
        # fuzz the form with each payload, and multiple
        # fields in the form if necessary
        fuzzer.delay(reconstructed_form, form_id, payload, fields_to_fuzz)

    db.commit()
    db.close()
    pass
