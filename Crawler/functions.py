__author__ = 'Sai'
from bs4 import BeautifulSoup
import mysql.connector
import json
import re


def getopenconnection():
    return mysql.connector.connect(user='root', password='',
                                   host='localhost',
                                   database='ejection')


def extract_form_attrs(form):
    # this adds the attributes of the form that are not method or action.
    # generators ftw! ps: you used a generator cause the other way required 4
    # lines. no other reason.
    attributes = {a: form[a] for a in form.attrs if a not in ['method', 'action']}
    # using json.dumps so that the single quotes in the dict key:value pairs don't
    # mess with the single quotes in the SQL queries.
    return json.dumps(attributes)
    pass


def insert_query_gen(tablename, attrs):
    # simple insert query generator function
    string = ','.join(["'"+str(x)+"'" for x in attrs])
    insert_query = "INSERT INTO "+str(tablename)+" VALUES("+string+")"
    return insert_query
    pass

def generate_search_query(tablename, fields = None, fieldname = None, value = None):
    # this is just a simple search query generator function
    search_query = "SELECT "
    if fields:
        search_query += str(fields)
    else:
        search_query += "*"
    search_query += " FROM " + tablename

    if fieldname and value:
        search_query += " WHERE %s = %s"%(fieldname, value)
    return search_query
    pass


def escape_quotes(str1):
    return (re.sub(r"'", r"\'", str(str1)))


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
    if(input.get('id') != None):
        name = input['id']
    if(input.get('name') != None):
        name = input['name']
    if(input.get('value') != None):
        value = input['value']
    # no need to check if it has a name, if the inp object got passed, it will
    # have a name. Period.
    elt_type = input.name
    # this is a set, avoids duplicates.
    params_list.add(('', elt_type, type, name, value, ''))


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
