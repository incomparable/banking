from flask import Flask, render_template, json, request
from models import Customer, Transaction, db, app
import traceback
import hashlib


#app = Flask(__name__)

app.config['SQLALCH0EMY_TRACK_MODIFICATIONS'] = False

@app.route("/home")
def customer_get_all():
    customers = Customer.query.all()
    count = 0
    for customer in  customers:
        print "Custome Name: %s " % customer.name
        # count +
        #print "customers %s" %  count
    templateData = {'title' : 'Home', 'customers': customers}
    return render_template('index.html', **templateData)


@app.route("/Customer_register")
def register():
    templateData = {'title' : 'Register Here'}
    return render_template('register.html', **templateData)

@app.route("/register_user" , methods=['POST'])
def save():

    print "registering customer : ", request.form
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        aadhar = request.form['aadhar']
        pan = request.form['pan']
        phone = request.form['phone'] 
        amount = request.form['amount']
        encodepassword = hashlib.md5(password.encode())

        print "Saving Data in progress ....."
        #customer = Customer('a', 'b c', 8888, 5678, 1234)
        save = Customer(name, email, encodepassword, address, int(aadhar), int(pan), int(phone), float(amount) )
        print "saving in Progress..."

        db.session.add(save)
        print "database adding session..."
        db.session.commit()
        print " databse session committed done!!"
    except Exception as exp:

        print "exp:", exp
        print(traceback.format_exc())
    return "data saved" 

@app.route("/Login")
def login():
    templateData = {'title' : 'Login'}
    return render_template('login.html', **templateData)


@app.route("/Successful_login")
def login_done():
    return "You are Successfully Logged In"

@app.route("/transaction")
def transaction():
    templateData = {'title' : 'Transaction'}
    return render_template('Transaction.html', **templateData)

@app.route("/transaction_complete", methods=['POST'])
def save_transaction():
    print "============save_transaction:", request.form
    try:
        Cust_name = request.form['Cust_name']
        email =request.form['email']
        account = request.form['account']
        deposit = request.form['deposit']
        withdrawal = request.form['withdrawal']
        print "porgress======"
        savetransaction = Transaction(Cust_name, email, account, deposit, withdrawal)
        print "=======saveinggggg========="
        db.session.add(savetransaction)
        db.session.commit()
        print "=========committed=========="
    except Exception as exp:
        print "=======Error========",exp
        print(traceback.format_exc())
    return "=======data Save========"



if __name__ == '__main__':
    app.run(debug= True)
