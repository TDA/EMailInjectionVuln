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
    print("Main URL:", urlparse(main_url))
    print("Attributes:", attributes)
    print("Method:", method)
    print("Action:", action)
    print("Input list:", input_list)

    # parse the url
    # now reconstruct the form
    data = None
    # set url to action
    url = action

    # r = requests.post(url, data)

    pass