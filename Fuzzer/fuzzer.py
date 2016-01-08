__author__ = 'saipc'

def fuzzer(reconstructed_form):
    # TODO have to get the individual attrs and inputs
    # from the form, and make sure that the fuzzing is only
    # done on the email fields, also, set the GET/POST right
    # and check with localmail first before whambamming

    # lets print out everything we have so we know what all we have :O
    # print(reconstructed_form)
    attributes, method, action, input_list = reconstructed_form
    print("Attributes:", attributes)
    print("Method:", method)
    print("Action:", action)
    print("Input list:", input_list)

    pass