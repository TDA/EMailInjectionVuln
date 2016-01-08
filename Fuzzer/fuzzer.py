__author__ = 'saipc'

import requests
import os
from urllib.parse import *

def fuzzer(reconstructed_form):
    try:
        # TODO have to get the individual attrs and inputs
        # from the form, and make sure that the fuzzing is only
        # done on the email fields, also, set the GET/POST right
        # and check with localmail first before whambamming

        # lets print out everything we have so we know what all we have :O
        # print(reconstructed_form)
        main_url, attributes, method, action, input_list = reconstructed_form
        print("Main URL:", main_url)
        print("Attributes:", attributes)
        print("Method:", method)
        print("Action:", action)
        print("Input list:", input_list)

        # parse the url
        scheme, netloc, path, params, query, fragment = urlparse(main_url, scheme='')

        # replace the paths last item alone with 'action'
        print(os.path.split(path))
        print("Final URL:", urlunparse((scheme, netloc, action, params, query, fragment)))

        method = str(method).lower()
        # Since we are using requests (yay!), we dont have
        # to construct the url as per get or post
        if method == 'get':
            # make a get request with requests
            pass
        elif method == 'post':
            # make a post request with requests
            pass
        else:
            # we dont have to do this, handle only gets
            # or posts, no need to complicate
            return

        # now reconstruct the form
        data = None
        # set url to action
        url = action

        # r = requests.post(url, data)

    except Exception as e:
        print("Definitely a requests issue, well, hopefully. We are in %s" % (__name__))
        print(e)
    return
