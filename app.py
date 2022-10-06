from flask import Flask, render_template, request,redirect,url_for
import pyodbc
app = Flask(__name__)

def connection():
    s = 'NITRVSP158LT' #Your server name
    d = 'bidDB'
    u = 'REVENUEMED\haji001' #Your login
    p = 'Guide@297105' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';trusted_connection=yes;UID='+u+';PWD='+ p
    conn = pyodbc.connect(cstr)
    return conn

@app.route('/')
def home():
    return render_template('bid_main.html')


@app.route('/auction-details/<int:course_id>',methods=['POST', 'GET'])
def auction(course_id):
    auctions = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("select * from course where course_id=?",course_id)
        for row in cursor.fetchall():
            auctions.append({"course_id": row[0], "c_title": row[1], "c_description": row[2], "image_url": row[3]})
        conn.close()
    return render_template('bid_auctiondetails.html',auctions = auctions )
    

@app.route('/auction-details/vendor-registration-form/<int:course_id>',methods=['POST', 'GET'])
def form(course_id):
  forms = []
  conn = connection()
  cursor = conn.cursor()
  if request.method == 'GET':
    cursor.execute("select * from course where Course_id=?",course_id)
    for row in cursor.fetchall():
        forms.append({"course_id": row[0], "c_title": row[1], "c_description": row[2], "image_url": row[3]})
    conn.close()
    return render_template('bid_v_form.html',forms = forms)
  if request.method == 'POST':
        Vendor_ID = request.form["Vendor_ID"]
        Vendor_Name = request.form["Vendor_Name"]
        Duration = int(request.form["Duration"])
        Experience = int(request.form["Experience"])
        Expected_Cost = float(request.form["Expected_Cost"])
        Demo = request.form["Demo"]
        Skills = request.form["Skills"]
        BID_ID = int(request.form["BID_ID"])
        Description = request.form["Description"]
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dbo.vendor (Vendor_ID,Vendor_Name,Duration,Experience,Expected_Cost,Demo,Skills,BID_ID,Description) VALUES (?, ?, ?, ?, ?, ?,? ,?,?)", Vendor_ID,Vendor_Name,Duration,Experience,Expected_Cost,Demo,Skills,BID_ID,Description)
        conn.commit()
        conn.close()
        return render_template('bid_v_form.html',forms = forms)

@app.route('/vendor-dashboard')
def vdash():
    vendors = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT title,expectedCost,duration FROM dbo.vendor")
    for row in cursor.fetchall():
        vendors.append({"title": row[0], "expectedCost": row[1],"duration": row[2]})        
        # vendors.append({"title": row[0], "duration": row[1], "experience": row[2], "expectedCost": row[3],"demo": row[4], "skills": row[5], "bidno": row[6], "description": row[7]})
    conn.close()
    # return render_template("bid_v_dashboard.html", vendors = vendors)
    return redirect('/')

  
     
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