import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NITRVSP047LT;'
                      'Database=bid_management;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


cursor.execute('''
                insert into course values('csd234','java','advance java','java training','online')
                ''')
conn.commit()

cursor = conn.cursor()
cursor.execute('SELECT * FROM course')
 
for i in cursor:
    print(i)