__author__ = 'saipc'

import requests
import os
from urllib.parse import *

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
            pass

        print("Final URL:", url)


        # TODO have to get the individual attrs and inputs
        # from the form, and make sure that the fuzzing is only
        # done on the email fields, also, set the GET/POST right
        # and check with localmail first before whambamming

        # now reconstruct the form
        data = None

        for a_input in input_list:
            if (check_input(a_input, 'email|e-mail')):
                print("Found an email field", a_input)
            else:
                # do nothing for now
                pass

        method = str(method).lower()
        # Since we are using requests (yay!), we dont have
        # to construct the url as per get or post
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
            # or posts, no need to complicate
            return

        print(r.status_code)
        print(r.text)

        # r = requests.post(url, data)

    except Exception as e:
        print("Definitely a requests issue, well, hopefully. We are in %s" % (__name__))
        print(e)
    return
