from flask import Flask, render_template, json, request, redirect
from models import User, Customer, Transaction, db, app
import traceback
import md5
# flask login
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)

# flask admin 
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app, name='State Bank', template_mode='bootstrap3')
admin.add_view(ModelView(Customer, db.session))
admin.add_view(ModelView(Transaction, db.session))

# app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/home")
def home():
    templateData = {'title': 'Login Page'}
    return render_template('admin/index.html', **templateData)


@app.route("/Customer_register")
def register():
    templateData = {'title': 'Register Here'}
    return render_template('register.html', **templateData)


@app.route("/register_user", methods=['POST'])
def register_user():

    print "register_user() :: ", request.form
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        aadhar = request.form['aadhar']
        pan = request.form['pan']
        phone = request.form['phone']
        amount = request.form['amount']
        encodepassword = md5.new(password).hexdigest()
        customerRegister = Customer(name, email, encodepassword, address, int(aadhar), int(pan), int(phone), amount )
        db.session.add(customerRegister)
        db.session.commit()

    except Exception as exp:
        print "exp:", exp
        print(traceback.format_exc())
    return "data saved"


@app.route("/login")
def login():
    templateData = {'title': 'Login'}
    return render_template('login.html', **templateData)


@app.route("/login_done", methods=['GET', 'POST'])
def login_done():
    if request.method =="GET":
        print "login Get"
        templateData = {'title' : 'login'}
        return render_template('login.html', **templateData)
    else:
        email = request.form['email']
        pswd = request.form['pswd']
        user = User.query.filter_by(email=email).filter_by(pswd=pswd).first()
        if not user:
            print "email and password dos't match"
            return "email and password dos't match"
        else:
            # print "you are login Successfully"
            print "You are Successfully Logged In"
            templateData = {'title': 'Home Page'}
            return render_template("index.html", **templateData)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/home")


@app.route("/transaction")
def transaction():
    templateData = {'title': 'Transaction'}
    return render_template('transaction.html', **templateData)


@app.route("/transaction_complete", methods=['POST'])
def save_transaction():
    print "============save_transaction:", request.form
    try:
        Cust_name = request.form['Cust_name']
        email =request.form['email']
        account = request.form['account']
        deposit = request.form['deposit']
        withdrawal = request.form['withdrawal']

        savetransaction = Transaction(Cust_name, email, account, deposit, withdrawal)
        db.session.add(savetransaction)
        db.session.commit()
    except Exception as exp:
        print "save_transaction() :: Got Ecveption: %s" % exp
        print(traceback.format_exc())
    return "=======data Save========"


if __name__ == '__main__':
    app.run(debug= True)
