from flask import Flask, render_template, request,redirect,url_for
import pyodbc
app = Flask(__name__)

def connection():
    s = 'NITRVSP158LT' #Your server name
    d = 'CarSales'
    u = 'REVENUEMED\haji001' #Your login
    p = 'Guide@297105' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';trusted_connection=yes;UID='+u+';PWD='+ p
    conn = pyodbc.connect(cstr)
    return conn

@app.route('/')
def home():
    return render_template('bid_main.html')


@app.route('/auction-details/<int:course_id>')
def auction(course_id):
    cars = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("select * from course where course_id=?",course_id)
        for row in cursor.fetchall():
            cars.append({"course_id": row[0], "title": row[1], "description": row[2], "image_url": row[3]})
        conn.close()
    return render_template('bid_auctiondetails.html',cars = cars )
    

@app.route('/auction-details/vendor-registration-form/<int:empid>',methods=['POST', 'GET'])
def form(empid):
  cr = []
  conn = connection()
  cursor = conn.cursor()
  if request.method == 'GET':
    cursor.execute("select * from tbl_course where Course_id=?",empid)
    for row in cursor.fetchall():
        cr.append({"courseid": row[0], "coursename": row[1], "courseduration": row[2], "coursecontent": row[3],"coursetutor": row[4],"coursedes": row[5],"coursereq": row[6]})
    conn.close()
  return render_template('bid_v_form.html',car = cr[0])


@app.route('/vendor-dashboard')
def vdash():
    return render_template('bid_v_dashboard.html')   
     
@app.route('/approver-active-bid')
def activebid():
    return  render_template('bid_approver_activeBid.html')

@app.route('/approver-dashboard')
def adash():
    return render_template('bid_approver_dashboard.html')    
@app.route("/confirm", methods=['POST', 'GET'])
def suggestions():
    if request.method == 'POST':
        n = request.form.get('fname')
        a = request.form.get('lname')
        c = request.form.get('city')
        d = request.form.get('comments')
        return  render_template('page4.html',fname=n,lname=a,city=c,comments=d)

@app.route("/final",methods=['GET','POST'])
def final():
    if request.method == 'POST':
        return redirect(url_for('final'))
    else:
        return  render_template('final.html')

if __name__=='__main__':
    app.run(debug=True)