from sqlite3 import Cursor
import pyodbc



def connection():

    s = 'NITRVSP047LT' 

    d = 'bid_management'

    u = 'REVENUEMED\sjoseph003' 

    p = 'Guide@297087' 

    cstr = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';trusted_connection=yes;UID='+u+';PWD='+ p)

    conn = pyodbc.connect(cstr)

    return conn


