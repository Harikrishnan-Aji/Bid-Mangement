import pyodbc
def connection():

    s = 'NITRVSP047LT' 

    d = 'bid_management'

    u = 'REVENUEMED\sjoseph003' 

    p = 'Guide@297087' 

    cstr = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';trusted_connection=yes;UID='+u+';PWD='+ p)

    conn = pyodbc.connect(cstr)

    return conn



def Read(conn):
    cursor = conn.cursor()
    print("Read")
    cursor.excute('Select * from course')
    for row in cursor:
        print(row)
    conn.commit()

def Write(conn):
    cursor = conn.cursor()
    print('Write')
    Course_ID = input('Enter Course ID:')
    Course_Name = input('Enter Course Name:')
    Levels = input('Enter the Course Level:')
    Course_Description = input('Explain about Course:')
    Training_Mode = input('Enter Training Mode:')
    cursor.execute('insert into course values( Course_ID,Course_Name,Levels, Course_Description,Training_Mode)values(?,?,?,?,?);',( Course_ID,Course_Name,Levels,Course_Description, Training_Mode))
    Read(conn)
    conn.commit()

    Write(conn)