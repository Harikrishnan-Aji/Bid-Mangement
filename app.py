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
        V_title = request.form["V_title"]
        Vendor_ID = request.form["Vendor_ID"]
        Vendor_Name = request.form["Vendor_Name"]
        Duration = request.form["Duration"]
        Experience = request.form["Experience"]
        Expected_Cost = request.form["Expected_Cost"]
        Demo = request.form["Demo"]
        Skills = request.form["Skills"]
        Bid_ID = request.form["BID_ID"]
        Description = request.form["Description"]
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dbo.vendor(V_title, Vendor_ID, Vendor_Name, Duration, Experience, Expected_Cost, Demo, Skills, BID_ID, Description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", V_title, Vendor_ID, Vendor_Name, Duration, Experience, Expected_Cost, Demo, Skills, Bid_ID, Description)
        conn.commit()
        conn.close()
        return render_template("bid_v_dashboard.html")
       
    

@app.route('/vendor-dashboard-page')
def vdash():
    vds = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT V_title,Expected_Cost,Duration FROM dbo.vendor")
    for row in cursor.fetchall():
        vds.append({"V_title": row[0], "Expected_Cost": row[1],"Duration": row[2]})        
        # vendors.append({"title": row[0], "duration": row[1], "experience": row[2], "expectedCost": row[3],"demo": row[4], "skills": row[5], "bidno": row[6], "description": row[7]})
    conn.close()
    return render_template("bid_v_dashboard.html",vds=vds)
   

  
     
@app.route('/approver-active-bid')
def activebid():
    return  render_template('bid_approver_activeBid.html')

@app.route('/approver-dashboard')
def adash():
    return  render_template('bid_approver_dashboard.html')
  
    


if __name__=='__main__':
    app.run(debug=True)