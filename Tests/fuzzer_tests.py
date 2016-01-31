__author__ = 'saipc'

# Sample data set
# main_url = 'http://localhost:63343/htdocs/TestProject/email.htm'
# Attributes: [{'data-hi': 'hi'}]
# method = 'get'
# test both types of url in the form
# action = 'MailTest.php'
# action = 'http://localhost:63343/htdocs/TestProject/MailTest.php'

# Input list: [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'password'}, {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'}, {'name': 'email', 'value': '', 'element_type': 'input', 'type': 'text'}, {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]
# Input list: [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'password'}, {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'}, {'name': 'mail', 'value': '', 'element_type': 'input', 'type': 'email'}, {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]
# Input list: [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'password'}, {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'}, {'name': 'mail', 'value': '', 'id': 'e-mail', 'element_type': 'input', 'type': 'text'}, {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]

# this is the format : main_url, attributes, method, action, input_list = reconstructed_form