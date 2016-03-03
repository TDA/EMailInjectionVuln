__author__ = 'saipc'
import MySQLdb


def getopenconnection():
    return MySQLdb.connect('127.0.0.1', 'root', '', 'ejection')
    # return MySQLdb.connect(DB.ip, DB.username, DB.password, DB.database_name)


def insert_query_gen(tablename, attrs):
    # simple insert query generator function
    string = ','.join(["'"+str(x)+"'" for x in attrs])
    insert_query = "INSERT INTO "+str(tablename)+" VALUES("+string+")"
    return insert_query
    pass

def generate_multi_search_query(tablename, fields = None, conditions = None):
    # this is just a simple search query generator function
    search_query = "SELECT "
    if fields:
        search_query += str(fields)
    else:
        search_query += "*"
    search_query += " FROM " + tablename

    if conditions:
        search_query += " WHERE "
        # this exceptionally cute generator line does this:
        # constructs a list with items which look like,
        # a = b, which is then concated into one string 'and'
        # SO => a = b AND c = d AND e =f etc.
        query = (' and '.join([("`%s` = '%s'")%(fieldname, value) for (fieldname, value) in conditions]))
        search_query += query
    return search_query
    pass
