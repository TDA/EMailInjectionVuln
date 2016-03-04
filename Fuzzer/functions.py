__author__ = 'Sai'
import MySQLdb
import DB
import re
import ast


def getopenconnection():
    return MySQLdb.connect('127.0.0.1', 'root', '', 'ejection')
    # return MySQLdb.connect(DB.ip, DB.username, DB.password, DB.database_name)


def extract_form_attrs(form):
    # this adds the attributes of the form that are not method or action.
    # generators ftw! ps: you used a generator cause the other way required 4
    # lines. no other reason.
    attributes = {a: form[a] for a in form.attrs if a not in ['method', 'action']}
    return attributes
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
    params_list.add((0, elt_type, type, name, value, ''))


def check_input(input, value):
    search_string = re.compile(value, re.IGNORECASE)
    is_present = False
    if(input.get('name') != None):
        is_present = (re.search(search_string, input.get('name')) != None)
    if(input.get('id') != None):
        # if already found, we should not reset it to false later
        is_present = is_present or (re.search(search_string, input.get('id')) != None)
    if(input.get('type') != None):
        is_present = is_present or (re.search(search_string, input.get('type')) != None)
    return is_present
    # returns true if the input field has name OR id
    # OR type set to be the 'value' provided,
    # else returns false.

def reconstruct_form(cursor, row):
    # this complicated looking line basically converts the --> nvm
    # string into a list, and gets the first element of the --> nvm
    # list, which is actually a dictionary, i have no idea --> nvm
    # why i saved it that way in the db, but i think cuz json --> Fixed this in functions
    main_url = row[0]
    # now attributes is just a dict
    attributes = ast.literal_eval(row[1])
    method = row[2]
    action = row[3]
    params = row[4]
    # lets you reconstruct a list from its string representation
    params = ast.literal_eval(params)
    input_list = []
    for param_id in params:
        TABLE_NAME = 'params'
        param_search_query = generate_search_query(TABLE_NAME, 'element_type, type, name, value', 'id', str(param_id))
        # print(param_search_query)
        cursor.execute(param_search_query)
        param_row = cursor.fetchone()
        if param_row == None or (len(param_row)) == 0:
            # no such params stored, return
            continue
        # construct a dict of the params of each input and append to list
        param_dict = {'element_type' : param_row[0],
                      'type' : param_row[1],
                      'name' : param_row[2],
                      'value': param_row[3]}
        input_list.append(param_dict)
        # print(param_dict)
    # now we have all the data to reconstruct the form and fuzz it
    # send this as an immutable tuple
    reconstructed_form = (main_url, attributes, method, action, input_list)
    return reconstructed_form
