connection = pyodbc.connect('Driver = {SQL Server};' 'Server=LAPTOP-NITRVSP047LT;'
              'Database = bid_management;' 'Trusted_Connection = yes;' )

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
    cursor.execute('insert into course( Course_ID,Course_Name,Levels, Course_Description,Training_Mode)values(?,?,?,?,?);',( Course_ID,Course_Name,Levels,Course_Description, Training_Mode))
    Read(conn)
    conn.commit()

    Write(conn)