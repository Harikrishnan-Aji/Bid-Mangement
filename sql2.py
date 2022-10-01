from sqlite3 import Cursor
import pyodbc


            

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='NITRVSP047LT';DATABASE='bid_management';trusted_connection=yes;UID='REVENUEMED\sjoseph003';PWD=Guide@297087')