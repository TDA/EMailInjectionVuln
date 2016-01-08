__author__ = 'saipc'

import requests
from urllib.parse import urlparse

def fuzzer(reconstructed_form):
    # TODO have to get the individual attrs and inputs
    # from the form, and make sure that the fuzzing is only
    # done on the email fields, also, set the GET/POST right
    # and check with localmail first before whambamming

    # lets print out everything we have so we know what all we have :O
    # print(reconstructed_form)
    main_url, attributes, method, action, input_list = reconstructed_form
    # parse the url
    print("Main URL:", urlparse(main_url))
    print("Attributes:", attributes)
    print("Method:", method)
    print("Action:", action)
    print("Input list:", input_list)


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

    pass