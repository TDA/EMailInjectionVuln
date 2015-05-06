__author__ = 'Sai'
from bs4 import BeautifulSoup
import mysql.connector
import re


def extract_form_attrs(form):
    method = form.get('method') or ''
    action = form.get('action') or ''
    attributes = []
    # this adds the attributes of the form that are not method or action.
    # generators ftw! ps: you used a generator cause the other way required 4
    # lines. no other reason.
    attributes.append({a: form[a] for a in form.attrs if a not in ['method', 'action']})
    return method, action, attributes
    pass


def store_form(url, form):
    #removed code as you aren't sure if the db queries will work with the queue. 
    #Query code is in your scripts folder on F:\xampp\htdocs\EMI\
    #Don't forget to add later.
    pass


def process_input(input, params_list):
    # input is a soup object and has a dictionary called attrs
    # retrieve the attrs that exist and return them in a tuple
    # using .get() to check for existence, as the dictionary, if directly
    # accessed, will throw a keyerror
    name = ''
    type = ''
    value = ''
    if(input.get('type') != None):
        type = input['type']
    if(input.get('name') != None or input.get('id') != None):
        name = input['name'] or input['id']
    if(input.get('value') != None):
        value = input['value']
    # no need to check if it has a name, if the inp object got passed, it will
    # have a name. Period.
    elt_type = input.name
    # this is a set, avoids duplicates.
    params_list.add(('', name, value, type, elt_type))


def check_input(input, value):
    search_string = re.compile(value, re.IGNORECASE)
    if(input.get('name') != None):
        return (re.search(search_string, input.get('name')) != None)
    elif(input.get('id') != None):
        return (re.search(search_string, input.get('name')) != None)
    return False
    # returns true if the input field has name or id set to be the 'value'
    # provided, else returns false.
    pass
