import random

__author__ = 'saipc'

import requests
import os
from urllib.parse import *
from Crawler.functions import *

def fuzzer(reconstructed_form):
    try:
        # lets print out everything we have so we know what all we have :O
        # print(reconstructed_form)
        main_url, attributes, method, action, input_list = reconstructed_form
        print("Main URL:", main_url)
        print("Attributes:", attributes)
        print("Method:", method)
        print("Action:", action)
        print("Input list:", input_list)
        # sorry for these overrides
        # TODO: remove these later, these are for testing
        method = 'get'
        main_url = 'http://localhost:63343/htdocs/TestProject/email.htm'
        action = 'http://localhost:63343/htdocs/TestProject/MailTest.php'

        # only do the following IFF the action is relative, and NOT absolute
        # (ie) if /submit.php and NOT http://xyz.com/submit.php, since in the latter
        # case, we can simply submit

        if not str(action).startswith('http:'):
            # parse the url
            scheme, netloc, path, params, query, fragment = urlparse(main_url, scheme='')

            # replace the paths last item alone with 'action'
            # this is for urls like: main_url = 'https://loc.com/sai/pc/ssspcs.php'
            # the form url might be like above, so we need to submit it right to
            # https://loc.com/sai/pc/submit.php, could there be an easier way??
            path_vars = str(path).split('/')
            path_vars[len(path_vars) - 1] = action
            path = '/'.join(path_vars)

            url = urlunparse((scheme, netloc, path, params, query, fragment))
        else:
            # we can directly get/post a request to the url, so
            # set url to action
            url = action

        print("FINAL URL:", url)


        # get the individual attrs and inputs
        # from the form, and make sure that the fuzzing is only
        # done on the email fields, also, set the GET/POST right
        # and check with localmail first before whambamming

        # now reconstruct the form
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        form_data_dict = {
            # this complex looking iterator is like this:
            "text": ''.join([random.choice(alphabets) for x in xrange(0, 10)])
        }
        data = {}
        # TODO: change this email to the ones we will use for fuzzing
        payload = 'saiprash_thegreatest@yahoo.co.in%0Abcc:schand31@asu.edu'

        for a_input in input_list:
            #print(a_input)
            if (check_input(a_input, r"email|e-mail")):
                # this is the field to be fuzzed
                print("Found an email field", a_input["name"])
                # enter the fuzzing data here
                # also add to the data list/tuple
                data[str(a_input["name"])] = payload
                print("HERES THE DATA", data)
                # TODO: need to add the payload to the field here
            else:
                # do nothing for now
                # TODO: this is a normal field, just enter
                # valid, but irrelevant data
                pass
            # add a_input to data

        method = str(method).lower()
        # Since we are using requests (yay!), we don't have
        # to construct the url as per get or post, just call
        # r.get or r.post and it'll take care of it
        if method == 'get':
            # make a get request with requests
            r = requests.get(url, data)
            pass
        elif method == 'post':
            # make a post request with requests
            r = requests.post(url, data)
            pass
        else:
            # we dont have to do this, we handle only gets
            # or posts, no need to complicate by handling put etc
            return

        print(r.status_code)
        print(r.text)

    except Exception as e:
        print("Definitely a requests issue, well, hopefully. We are in %s" % (__name__))
        print(e)
    return
