from __future__ import absolute_import
import random
from CeleryFuzzer import app

__author__ = 'saipc'
from celery import Celery

import requests
from urlparse import *
from functions import *

# for tests in python3
# from urllib.parse import *
# from Fuzzer.functions import *



def construct_url(action, main_url):
    # only do the following IFF the action is relative, and NOT absolute
    # (ie) if /submit.php and NOT http://xyz.com/submit.php, since in the latter
    # case, we can simply submit

    # initially we can directly get/post a request
    # to the url, so set url to action
    url = action
    if not str(action).startswith('http:'):
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
def fuzzer(reconstructed_form, form_id):
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
            "name": "asuSefcomResearcher",
            "submit": "submit"
        }

        data = {}
        data_2 = {}
        data_3 = {}
        # add x-dummy-header too
        payload = 'nuser123@wackopicko.com%0abcc:maluser123@wackopicko.com%0ax-check:in'
        payload_2 = 'nuser123@wackopicko.com%0d%0abcc:maluser123@wackopicko.com%0d%0ax-check:in'
        payload_3 = 'reguser123@wackopicko.com'

        for a_input in input_list:
            if (check_input(a_input, r"email|e-mail")):
                # this is the field to be fuzzed
                # print("Found an email field", a_input["name"])
                # enter the fuzzing data here
                # also add to the data list/tuple
                data[str(a_input["name"])] = payload
                data_2[str(a_input["name"])] = payload_2
                data_3[str(a_input["name"])] = payload_3
                # need to add the payload to the field here --> DONE
            else:
                # this is a normal field, just enter
                # valid, but irrelevant data
                # if name, password, or date, OR submit!!!
                #  directly fill from the dict
                if (check_input(a_input, r"date")):
                    data[str(a_input["name"])] = form_data_dict["date"]
                    data_2[str(a_input["name"])] = form_data_dict["date"]
                    data_3[str(a_input["name"])] = form_data_dict["date"]
                    continue
                if (check_input(a_input, r"password")):
                    data[str(a_input["name"])] = form_data_dict["password"]
                    data_2[str(a_input["name"])] = form_data_dict["password"]
                    data_3[str(a_input["name"])] = form_data_dict["password"]
                    continue
                if (check_input(a_input, r"name|username")):
                    data[str(a_input["name"])] = form_data_dict["name"]
                    data_2[str(a_input["name"])] = "asuSefcomResearcher2"
                    data_3[str(a_input["name"])] = "asuSefcomResearcher3"
                    continue
                if (check_input(a_input, r"submit")):
                    data["submit"] = form_data_dict["submit"]
                    data_2["submit"] = form_data_dict["submit"]
                    data_3["submit"] = form_data_dict["submit"]
                    continue
                # this is the default case where the field is a text field,
                # only reached if its none of the above
                if (check_input(a_input, r"text")):
                    data[str(a_input["name"])] = form_data_dict["text"]
                    data_2[str(a_input["name"])] = form_data_dict["text"]
                    data_3[str(a_input["name"])] = form_data_dict["text"]
                    continue
        # print("HERES THE DATA", data)

        method = str(method).lower()
        # Since we are using requests (yay!), we don't have
        # to construct the url as per get or post, just call
        # r.get or r.post and it'll take care of it
        if method == 'get':
            # make a get request with requests,
            # and pass the payload as params
            r = requests.get(url, params = data)
            r_2 = requests.get(url, params = data_2)
            r_3 = requests.get(url, params = data_3)
        elif method == 'post':
            # make a post request with requests,
            # and pass the payload as data
            r = requests.post(url, data = data)
            r_2 = requests.post(url, data = data_2)
            r_3 = requests.post(url, data = data_3)
        else:
            # we dont have to do this, we handle only gets
            # or posts, no need to complicate by handling put etc
            return

        # UPDATE DB after fuzzing!!!!
        db = getopenconnection()
        cursor = db.cursor()
        print("INSERT INTO `fuzzed_forms`(`form_id`, `url_fuzzed`, `payload_for_fuzzing`) VALUES (%s, '%s', '%s')" % (form_id, db.escape_string(url), db.escape_string(payload)))
        cursor.execute("INSERT INTO `fuzzed_forms`(`form_id`, `url_fuzzed`, `payload_for_fuzzing`) VALUES (%s, '%s', '%s')" % (form_id, db.escape_string(url), db.escape_string(payload)))
        cursor.execute("INSERT INTO `fuzzed_forms`(`form_id`, `url_fuzzed`, `payload_for_fuzzing`) VALUES (%s, '%s', '%s')" % (form_id, db.escape_string(url), db.escape_string(payload_2)))
        cursor.execute("INSERT INTO `fuzzed_forms`(`form_id`, `url_fuzzed`, `payload_for_fuzzing`) VALUES (%s, '%s', '%s')" % (form_id, db.escape_string(url), db.escape_string(payload_3)))
        db.commit()
        db.close()
        # print(r.status_code)
        # print(r.text)
        # this is only for testing that the data is right,
        # we do not do anything with the data
        # print("HERES THE DATA afterwards", data)
        return (data, data_2, data_3)

    except Exception as e:
        print("Definitely a requests issue, well, hopefully. We are in %s" % (__name__))
        print(e)
        with open('log_fuzzer', 'a') as file_handle:
            file_handle.write(str(e) + '\n' + "We are in %s" % (__name__) + '\n')
