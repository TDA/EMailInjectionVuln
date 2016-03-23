__author__ = 'Sai'
import MySQLdb
def getopenconnection():
    return MySQLdb.connect('127.0.0.1', 'root', '', 'ejection')
    # return MySQLdb.connect(DB.ip, DB.username, DB.password, DB.database_name)

def insert_query_gen(tablename, attrs):
    # simple insert query generator function
    string = ','.join(["'"+str(x)+"'" for x in attrs])
    insert_query = "INSERT INTO "+str(tablename)+" VALUES("+string+")"
    return insert_query

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
