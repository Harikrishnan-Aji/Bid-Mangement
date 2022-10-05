
from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('bid_main.html')


@app.route('/auction-details')
def auction():
    return render_template('bid_auctiondetails.html')

@app.route('/vendor-registration-form')
def form():
    return  render_template('bid_vendorform.html')

@app.route('/vendor-dashboard')
def vdash():
    return render_template('vd_dashbord.html')   
     
@app.route('/approver-active-bid')
def activebid():
    return  render_template('bid_approver_activeBid.html')

@app.route('/approver-dashboard')
def adash():
    return render_template('bid_appdashboard.html')    
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