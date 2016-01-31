__author__ = 'saipc'

# Sample data set
main_url = 'http://localhost:63343/htdocs/TestProject/email.htm'
attributes = [{'data-hi': 'hi'}]
method = 'get'
# test both types of url in the form
action_1 = 'MailTest.php'
action_2 = 'http://localhost:63343/htdocs/TestProject/MailTest.php'

# test all types of input fields in the form
input_list_1 = [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'password'}, {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'}, {'name': 'email', 'value': '', 'element_type': 'input', 'type': 'text'}, {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]
input_list_2 = [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'date'}, {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'}, {'name': 'mail', 'value': '', 'element_type': 'input', 'type': 'email'}, {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]
input_list_3 = [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'text'}, {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'}, {'name': 'mail', 'value': '', 'id': 'e-mail', 'element_type': 'input', 'type': 'text'}, {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]

# this is the format : main_url, attributes, method, action, input_list = reconstructed_form
reconstructed_form = ()